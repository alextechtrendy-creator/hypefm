"""Build site/spaces.json from the archive/ folder.

Scans every archive entry and produces a single JSON file the homepage
reads at load time. Includes full transcripts for in-browser search.

Run from project root:
    python scripts/build_manifest.py
"""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ARCHIVE_DIR = ROOT / "archive"
SITE_DIR = ROOT / "site"


def _safe_load_json(path: Path) -> dict | None:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"  warn: could not read {path.name}: {e}", file=sys.stderr)
        return None


def _flatten_transcript(transcript_data: dict) -> str:
    chunks = transcript_data.get("chunks", [])
    return " ".join(c.get("text", "") for c in chunks)


def build() -> None:
    if not ARCHIVE_DIR.exists():
        print(f"No archive/ directory at {ARCHIVE_DIR}", file=sys.stderr)
        sys.exit(1)

    SITE_DIR.mkdir(exist_ok=True)
    spaces = []

    entry_dirs = sorted(d for d in ARCHIVE_DIR.iterdir() if d.is_dir())
    print(f"Scanning {len(entry_dirs)} archive entries...")

    for entry_dir in entry_dirs:
        meta_path = entry_dir / "metadata.json"
        transcript_path = entry_dir / "transcript.json"

        if not meta_path.exists():
            print(f"  skip {entry_dir.name}: no metadata.json")
            continue

        meta = _safe_load_json(meta_path)
        if not meta:
            continue

        transcript_text = ""
        if transcript_path.exists():
            transcript = _safe_load_json(transcript_path)
            if transcript:
                transcript_text = _flatten_transcript(transcript)

        spaces.append({
            "id": meta.get("space_id"),
            "title": meta.get("summary_title") or meta.get("title"),
            "description": meta.get("summary_description"),
            "tags": meta.get("topic_tags", []),
            "host": meta.get("host_username"),
            "date": meta.get("started_at") or meta.get("created_at"),
            "duration": meta.get("audio_duration_seconds"),
            "audio": meta.get("audio_captured", False),
            "url": meta.get("space_url"),
            "quote": meta.get("pull_quote"),
            "quote_attribution": meta.get("quote_attribution"),
            "participants": meta.get("participants", []),
            "_transcript": transcript_text,
        })

    output = {"spaces": spaces}
    out_path = SITE_DIR / "spaces.json"
    out_path.write_text(json.dumps(output, indent=2, default=str), encoding="utf-8")

    site_archive = SITE_DIR / "archive"
    if site_archive.exists():
        shutil.rmtree(site_archive)
    shutil.copytree(ARCHIVE_DIR, site_archive)

    total_size_mb = sum(
        f.stat().st_size for f in site_archive.rglob("*") if f.is_file()
    ) / 1024 / 1024

    print(f"\n✓ Wrote {out_path} with {len(spaces)} spaces")
    print(f"✓ Mirrored archive to {site_archive} ({total_size_mb:.1f} MB)")
    print(f"\nNext: deploy the site/ folder to Vercel.")


if __name__ == "__main__":
    build()