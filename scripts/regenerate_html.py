"""Regenerate index.html and transcript.md for every archive entry.

Use after changing render.py templates — refreshes existing entries without
redoing transcription.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))

from hlspaces.models import SpaceMetadata, Transcript
from hlspaces.render import render_html, render_markdown

ARCHIVE_DIR = ROOT / "archive"

count = 0
for entry_dir in sorted(ARCHIVE_DIR.iterdir()):
    if not entry_dir.is_dir():
        continue
    meta_path = entry_dir / "metadata.json"
    transcript_path = entry_dir / "transcript.json"
    if not meta_path.exists() or not transcript_path.exists():
        print(f"  skip {entry_dir.name}: missing files")
        continue

    meta = SpaceMetadata(**json.loads(meta_path.read_text(encoding="utf-8")))
    transcript = Transcript(**json.loads(transcript_path.read_text(encoding="utf-8")))

    (entry_dir / "index.html").write_text(render_html(meta, transcript), encoding="utf-8")
    (entry_dir / "transcript.md").write_text(render_markdown(meta, transcript), encoding="utf-8")
    count += 1
    print(f"  ✓ {entry_dir.name}")

print(f"\nRegenerated {count} entries.")