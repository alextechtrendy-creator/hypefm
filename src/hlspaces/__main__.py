"""CLI entrypoint."""
from __future__ import annotations

import json
import sys
import traceback
from datetime import datetime, timezone
from pathlib import Path

import click

from .capture import CaptureError, capture_space_audio
from .config import ARCHIVE_DIR
from .models import Transcript, TranscriptChunk
from .render import write_archive_entry
from .transcribe import transcribe_with_diarization
from .x_api import extract_space_id, fetch_space_metadata, find_space_ids_in_user_tweets


def _empty_transcript(space_id: str) -> Transcript:
    return Transcript(
        space_id=space_id,
        language="unknown",
        duration_seconds=0.0,
        chunks=[],
        speaker_map={},
    )


@click.group()
def cli() -> None:
    """Hyperliquid Spaces Archive."""


@cli.command()
@click.argument("space_url_or_id")
@click.option("--no-audio", is_flag=True, help="Skip audio capture (metadata only)")
@click.option("--no-diarize", is_flag=True, help="Skip speaker diarization")
@click.option("--archive-dir", type=click.Path(path_type=Path), default=None,
              help="Override archive output directory")
def archive(space_url_or_id: str, no_audio: bool, no_diarize: bool, archive_dir: Path | None) -> None:
    """Archive a single Space by URL or ID."""
    archive_dir = archive_dir or ARCHIVE_DIR
    space_id = extract_space_id(space_url_or_id)

    click.echo(f"→ Archiving space {space_id}")

    # 1. Metadata
    click.echo("  Fetching metadata from X API...")
    try:
        meta = fetch_space_metadata(space_id)
    except Exception as e:
        click.echo(f"  ✗ Metadata fetch failed: {e}", err=True)
        sys.exit(1)
    click.echo(f"    Title: {meta.title or '(no title)'}")
    click.echo(f"    State: {meta.state}")
    click.echo(f"    Host:  @{meta.host_username or '?'}")

    # 2. Audio
    audio_path: Path | None = None
    if not no_audio:
        click.echo("  Capturing audio...")
        entry_dir = archive_dir / space_id
        entry_dir.mkdir(parents=True, exist_ok=True)
        target = entry_dir / "audio.m4a"
        try:
            audio_path = capture_space_audio(meta.space_url, target)
            meta.audio_captured = True
            click.echo(f"    ✓ {audio_path.name}")
        except CaptureError as e:
            meta.capture_failure_reason = str(e)
            click.echo(f"    ✗ Audio capture failed: {e}", err=True)
    else:
        meta.capture_failure_reason = "Audio capture skipped (--no-audio)"

    # 3. Transcribe
    transcript: Transcript
    if audio_path and audio_path.exists():
        click.echo("  Transcribing (this can take a while)...")
        try:
            transcript = transcribe_with_diarization(
                audio_path, space_id, skip_diarization=no_diarize
            )
            meta.audio_duration_seconds = transcript.duration_seconds
            click.echo(f"    ✓ {len(transcript.chunks)} chunks, "
                       f"{transcript.duration_seconds:.0f}s, lang={transcript.language}")
        except Exception as e:
            click.echo(f"    ✗ Transcription failed: {e}", err=True)
            traceback.print_exc()
            transcript = _empty_transcript(space_id)
    else:
        transcript = _empty_transcript(space_id)
    # 3.5. Summarize with Claude (cheap, optional)
    if transcript.chunks:
        click.echo("  Summarizing with Claude Haiku...")
        from .summarize import summarize_transcript
        summary = summarize_transcript(transcript)
        if summary:
            meta.summary_title = summary.get("title")
            meta.summary_description = summary.get("description")
            meta.topic_tags = summary.get("tags", [])
            meta.key_moments = summary.get("key_moments", [])
            meta.pull_quote = summary.get("pull_quote")
            click.echo(f"    ✓ {meta.summary_title}")
            if meta.topic_tags:
                click.echo(f"    tags: {', '.join(meta.topic_tags)}")
    # 4. Render
    click.echo("  Writing archive entry...")
    entry_dir = write_archive_entry(archive_dir, meta, transcript, audio_path)
    click.echo(f"    ✓ {entry_dir}")
    click.echo(f"  Open: {entry_dir / 'index.html'}")


@cli.command()
@click.option("--hosts", "hosts_path", type=click.Path(exists=True, path_type=Path),
              required=True, help="JSON file with {\"hosts\": [\"handle1\", ...]}")
@click.option("--out", "out_path", type=click.Path(path_type=Path),
              default=Path("./space_ids.json"), help="Where to write discovered IDs")
@click.option("--max-tweets", type=int, default=3200,
              help="Max tweets to scan per host (Basic tier ceiling: 3200)")
def discover(hosts_path: Path, out_path: Path, max_tweets: int) -> None:
    """Enumerate Space IDs linked from known hosts' tweets."""
    hosts_data = json.loads(hosts_path.read_text())
    hosts = hosts_data.get("hosts", [])
    if not hosts:
        click.echo("No hosts in file.", err=True)
        sys.exit(1)

    all_ids: dict[str, list[str]] = {}  # space_id -> [hosts who linked it]
    for handle in hosts:
        click.echo(f"→ Scanning @{handle}")
        try:
            count = 0
            for sid in find_space_ids_in_user_tweets(handle, max_tweets=max_tweets):
                all_ids.setdefault(sid, []).append(handle)
                count += 1
            click.echo(f"    found {count} space link(s)")
        except Exception as e:
            click.echo(f"    ✗ {e}", err=True)

    out_path.write_text(json.dumps({
        "discovered_at": datetime.now(timezone.utc).isoformat(),
        "spaces": [
            {"space_id": sid, "linked_by": linkers}
            for sid, linkers in sorted(all_ids.items())
        ],
    }, indent=2))
    click.echo(f"\n✓ {len(all_ids)} unique Spaces written to {out_path}")


@cli.command()
@click.argument("ids_file", type=click.Path(exists=True, path_type=Path))
@click.option("--no-audio", is_flag=True, help="Metadata only (faster, always works)")
@click.option("--no-diarize", is_flag=True, help="Skip diarization")
@click.option("--limit", type=int, default=None, help="Process only first N IDs")
@click.pass_context
def backfill(ctx: click.Context, ids_file: Path, no_audio: bool, no_diarize: bool, limit: int | None) -> None:
    """Archive every Space ID listed in a discover-output file."""
    data = json.loads(ids_file.read_text())
    spaces = data.get("spaces", [])
    if limit:
        spaces = spaces[:limit]

    click.echo(f"Backfilling {len(spaces)} spaces...\n")

    successes = 0
    failures: list[tuple[str, str]] = []
    for entry in spaces:
        sid = entry["space_id"]
        try:
            ctx.invoke(archive, space_url_or_id=sid, no_audio=no_audio, no_diarize=no_diarize, archive_dir=None)
            successes += 1
        except SystemExit:
            failures.append((sid, "metadata fetch failed (likely 404)"))
        except Exception as e:
            failures.append((sid, str(e)))
        click.echo("")

    click.echo(f"\n=== Backfill complete: {successes} succeeded, {len(failures)} failed ===")
    for sid, reason in failures:
        click.echo(f"  {sid}: {reason}")


@cli.command()
@click.option("--archive-dir", type=click.Path(path_type=Path), default=None)
@click.option("--limit", type=int, default=None)
def resummarize_all(archive_dir: Path | None, limit: int | None) -> None:
    """Re-run LLM summarization across every archive entry."""
    from .summarize import summarize_transcript
    from .models import SpaceMetadata, Transcript

    archive_dir = archive_dir or ARCHIVE_DIR
    entry_dirs = sorted(d for d in archive_dir.iterdir() if d.is_dir())
    if limit:
        entry_dirs = entry_dirs[:limit]

    successes = 0
    for entry_dir in entry_dirs:
        meta_path = entry_dir / "metadata.json"
        transcript_path = entry_dir / "transcript.json"
        if not meta_path.exists() or not transcript_path.exists():
            click.echo(f"  ⏭️  {entry_dir.name}: missing files")
            continue

        meta_data = json.loads(meta_path.read_text(encoding="utf-8"))
        transcript_data = json.loads(transcript_path.read_text(encoding="utf-8"))
        meta = SpaceMetadata(**meta_data)
        transcript = Transcript(**transcript_data)

        click.echo(f"  → {entry_dir.name}...")
        summary = summarize_transcript(transcript)
        if not summary:
            click.echo(f"    ✗ failed")
            continue

        meta.summary_title = summary.get("title")
        meta.summary_description = summary.get("description")
        meta.topic_tags = summary.get("tags", [])
        meta.key_moments = summary.get("key_moments", [])
        meta.pull_quote = summary.get("pull_quote")

        meta_path.write_text(meta.model_dump_json(indent=2), encoding="utf-8")
        click.echo(f"    ✓ {meta.summary_title}")
        if meta.pull_quote:
            click.echo(f"      quote: \"{meta.pull_quote[:80]}...\"")
        successes += 1

    click.echo(f"\nResummarized {successes}/{len(entry_dirs)} entries.")

def main() -> None:
    cli()


if __name__ == "__main__":
    main()
