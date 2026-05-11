"""Modal backfill — one Space at a time, with verbose logging."""
import sys
import modal

app = modal.App("hype-fm-backfill")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("ffmpeg")
    .pip_install(
        "yt-dlp",
        "tweepy>=4.14.0",
        "faster-whisper>=1.0.0",
        "anthropic>=0.40.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
        "nvidia-cublas-cu12",
        "nvidia-cudnn-cu12==9.*",
    )
    .env({
        "PYTHONPATH": "/root",
        "PYTHONUNBUFFERED": "1",
        "LD_LIBRARY_PATH": "/usr/local/lib/python3.12/site-packages/nvidia/cublas/lib:/usr/local/lib/python3.12/site-packages/nvidia/cudnn/lib",
    })
    .add_local_dir("src/hlspaces", remote_path="/root/hlspaces")
)

volume = modal.Volume.from_name("hype-fm-archive", create_if_missing=True)
model_cache = modal.Volume.from_name("hype-fm-models", create_if_missing=True)


@app.function(
    image=image,
    gpu="L4",
    volumes={"/archive": volume, "/models": model_cache},
    secrets=[
        modal.Secret.from_name("anthropic-api-key"),
        modal.Secret.from_name("x-bearer-token"),
        modal.Secret.from_name("x-cookies"),
        modal.Secret.from_name("huggingface-token"),
    ],
    timeout=60 * 60,
)
def archive_one_space(space_id: str) -> dict:
    import os, sys, subprocess, time, traceback
    from pathlib import Path

    def log(msg):
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)
        sys.stdout.flush()

    log(f"=== START {space_id} ===")
    archive_root = Path("/archive")
    entry_dir = archive_root / space_id

    if (entry_dir / "metadata.json").exists() and (entry_dir / "transcript.json").exists():
        log(f"already archived, skipping")
        return {"space_id": space_id, "status": "skipped"}

    entry_dir.mkdir(parents=True, exist_ok=True)
    log(f"entry_dir created: {entry_dir}")

    cookies_path = Path("/tmp/cookies.txt")
    cookies_path.write_text(os.environ["X_COOKIES_TXT"])
    log(f"cookies written ({cookies_path.stat().st_size} bytes)")

    os.environ["HF_HOME"] = "/models/hf"
    os.environ["XDG_CACHE_HOME"] = "/models"
    os.environ["WHISPER_DEVICE"] = "cuda"

    space_url = f"https://x.com/i/spaces/{space_id}"

    try:
        log("fetching X API metadata...")
        from hlspaces.x_api import fetch_space_metadata
        meta = fetch_space_metadata(space_id)
        log(f"  title: {meta.title!r}")
        log(f"  host: @{meta.host_username}")
    except Exception as e:
        log(f"METADATA FAILED: {e}")
        return {"space_id": space_id, "status": "metadata_failed", "error": str(e)}

    log("downloading audio with yt-dlp...")
    audio_path = entry_dir / "audio.m4a"
    result = subprocess.run([
        "yt-dlp", "--cookies", str(cookies_path),
        "-o", str(audio_path), space_url,
    ], capture_output=True, text=True, timeout=60 * 30)
    log(f"  yt-dlp exit: {result.returncode}")
    if not audio_path.exists():
        candidates = sorted(entry_dir.glob(f"{audio_path.stem}.*"),
                            key=lambda p: p.stat().st_mtime, reverse=True)
        if candidates:
            candidates[0].rename(audio_path)
    audio_ok = audio_path.exists()
    if audio_ok:
        log(f"  audio file: {audio_path.stat().st_size} bytes")
        meta.audio_captured = True
    else:
        log(f"  audio NOT downloaded; stderr tail: {result.stderr[-300:]}")
        meta.audio_captured = False
        meta.capture_failure_reason = f"yt-dlp failed: {result.stderr[-200:]}"

    from hlspaces.models import Transcript
    transcript = Transcript(
        space_id=space_id, language="unknown",
        duration_seconds=0.0, chunks=[],
    )

    if audio_ok:
        try:
            log("transcribing on GPU...")
            from hlspaces.transcribe import transcribe_with_diarization
            transcript = transcribe_with_diarization(audio_path, space_id, skip_diarization=True)
            meta.audio_duration_seconds = transcript.duration_seconds
            log(f"  done: {len(transcript.chunks)} chunks, {transcript.duration_seconds:.0f}s")
        except Exception as e:
            log(f"TRANSCRIPTION FAILED: {e}")
            traceback.print_exc()
            return {"space_id": space_id, "status": "transcription_failed", "error": str(e)}

    if transcript.chunks:
        try:
            log("summarizing with Claude...")
            from hlspaces.summarize import summarize_transcript
            summary = summarize_transcript(transcript)
            if summary:
                meta.summary_title = summary.get("title")
                meta.summary_description = summary.get("description")
                meta.topic_tags = summary.get("tags", [])
                meta.key_moments = summary.get("key_moments", [])
                log(f"  title: {meta.summary_title}")
        except Exception as e:
            log(f"summary failed (non-fatal): {e}")

    log("rendering archive entry...")
    from hlspaces.render import write_archive_entry
    write_archive_entry(archive_root, meta, transcript, audio_path if audio_ok else None)
    volume.commit()
    log(f"=== DONE {space_id} ===")

    return {
        "space_id": space_id, "status": "ok",
        "audio_captured": audio_ok,
        "title": meta.summary_title,
    }


@app.local_entrypoint()
def main(space_id: str = "", limit: int = 0, ids_file: str = "space_ids.json"):
    """Archive Spaces. Either single (--space-id ID) or batch (--limit N from JSON file)."""
    import json
    from pathlib import Path

    if space_id:
        # Single-Space mode (use this for testing one Space at a time)
        result = archive_one_space.remote(space_id)
        print("\nResult:", result)
        return

    # Batch mode
    data = json.loads(Path(ids_file).read_text())
    space_ids = [s["space_id"] for s in data.get("spaces", [])]
    if limit:
        space_ids = space_ids[:limit]

    print(f"\nDispatching {len(space_ids)} Spaces to Modal...\n")

    successes = 0
    audio_captured = 0
    failures = []

    for result in archive_one_space.map(space_ids, return_exceptions=True):
        if isinstance(result, Exception):
            failures.append(("?", f"container exception: {result}"))
            continue
        sid = result["space_id"]
        status = result["status"]
        if status == "ok":
            audio_icon = "🎵" if result.get("audio_captured") else "📝"
            print(f"  {audio_icon} {sid}: {result.get('title', '(no title)')}")
            successes += 1
            if result.get("audio_captured"):
                audio_captured += 1
        elif status == "skipped":
            print(f"  ⏭️  {sid}: already archived")
            successes += 1
        else:
            print(f"  ✗ {sid}: {status}")
            failures.append((sid, result.get("error", "")[:120]))

    print(f"\n=== Summary ===")
    print(f"  Successes: {successes}")
    print(f"  Audio captured: {audio_captured}")
    print(f"  Metadata-only: {successes - audio_captured}")
    print(f"  Failures: {len(failures)}")
    if failures:
        print(f"\nFailures:")
        for sid, err in failures:
            print(f"  {sid}: {err}")
    print(f"\nNext: download results with")
    print(f"  modal volume get hype-fm-archive ./modal_results")