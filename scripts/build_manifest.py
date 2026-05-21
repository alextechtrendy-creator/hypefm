"""Build site/spaces.json from the archive folder, merging in teams.json data."""
from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).parent.parent
ARCHIVE = ROOT / "archive"
TEAMS_FILE = ROOT / "teams.json"
SITE = ROOT / "site"
SITE_ARCHIVE = SITE / "archive"
SPACES_JSON = SITE / "spaces.json"


def load_teams() -> dict:
    if not TEAMS_FILE.exists():
        return {}
    try:
        return json.loads(TEAMS_FILE.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"warn: could not parse teams.json: {e}")
        return {}


def main():
    if not ARCHIVE.exists():
        print(f"archive directory not found: {ARCHIVE}")
        sys.exit(1)

    teams = load_teams()
    entry_dirs = sorted([d for d in ARCHIVE.iterdir() if d.is_dir()])
    print(f"Scanning {len(entry_dirs)} archive entries...")

    spaces = []
    for entry_dir in entry_dirs:
        meta_path = entry_dir / "metadata.json"
        transcript_path = entry_dir / "transcript.json"
        if not meta_path.exists():
            continue

        try:
            meta = json.loads(meta_path.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"  warn: could not read metadata.json: {e}")
            continue

        transcript_text = ""
        if transcript_path.exists():
            try:
                transcript = json.loads(transcript_path.read_text(encoding="utf-8"))
                transcript_text = " ".join(c.get("text", "") for c in transcript.get("chunks", []))
            except Exception:
                pass

        team_info = None
        attr = meta.get("quote_attribution")
        if attr and attr.get("team"):
            team_name = attr["team"]
            t = teams.get(team_name)
            if t:
                team_info = {
                    "name": team_name,
                    "logo": t.get("logo"),
                    "x_handle": t.get("x_handle"),
                    "website": t.get("website"),
                    "description": t.get("description"),
                }
            else:
                team_info = {
                    "name": team_name,
                    "logo": None,
                    "x_handle": None,
                    "website": None,
                    "description": None,
                }

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
            "team_info": team_info,
            "participants": meta.get("participants", []),
            "_transcript": transcript_text,
        })

    SPACES_JSON.parent.mkdir(parents=True, exist_ok=True)
    SPACES_JSON.write_text(json.dumps({"spaces": spaces}, indent=2), encoding="utf-8")
    print(f"\u2713 Wrote {SPACES_JSON} with {len(spaces)} spaces")

    if SITE_ARCHIVE.exists():
        shutil.rmtree(SITE_ARCHIVE)
    shutil.copytree(ARCHIVE, SITE_ARCHIVE)
    size_mb = sum(f.stat().st_size for f in SITE_ARCHIVE.rglob("*")) / (1024 * 1024)
    print(f"\u2713 Mirrored archive to {SITE_ARCHIVE} ({size_mb:.1f} MB)")
    print(f"Next: deploy the site/ folder to Vercel.")


if __name__ == "__main__":
    main()