# Hyperliquid Spaces Archive

A community archive of X Spaces about Hyperliquid. Audio + searchable transcripts.

## What this is

A CLI tool that takes an X Space URL and produces a self-contained archive entry:
audio file, metadata, diarized transcript, and a standalone HTML page.

```
archive/
└── 1AbCdEfGhIjKl/         # Space ID
    ├── audio.m4a
    ├── metadata.json
    ├── transcript.json    # diarized chunks with timestamps
    ├── transcript.md      # human-readable
    └── index.html         # standalone page
```

The static site (separate, not in this MVP) reads these folders. Decoupling capture
from the site means if scraping breaks, the archive stays online.

## Setup

Requires Python 3.10+ and ffmpeg.

```bash
# System dependencies
sudo apt install ffmpeg     # or: brew install ffmpeg

# Python dependencies
pip install -r requirements.txt

# Get a HuggingFace token (free) for pyannote diarization model:
# 1. Make account at huggingface.co
# 2. Accept terms at https://huggingface.co/pyannote/speaker-diarization-3.1
# 3. Create access token at https://huggingface.co/settings/tokens
# 4. Set HF_TOKEN env var or put in .env

cp .env.example .env
# Fill in HF_TOKEN and X_BEARER_TOKEN
```

## Usage

Archive a single Space:

```bash
python -m hlspaces archive https://x.com/i/spaces/1AbCdEfGhIjKl
```

Backfill all Spaces from known hosts (uses X API):

```bash
python -m hlspaces backfill --hosts hosts.json
```

`hosts.json` format:
```json
{
  "hosts": ["HyperliquidX", "chameleon_jeff", "...other handles..."]
}
```

## What works, what doesn't

- **Audio capture** works only while the Space is live OR within ~30 days of ending
  if the host enabled recording. Otherwise you get metadata-only.
- **Metadata** via the X API works for most ended Spaces but some return 404 after
  enough time passes. Expect ~60-70% recovery on older Spaces.
- **Diarization** identifies distinct speakers but doesn't name them. After the first
  pass, edit `transcript.json` to map `SPEAKER_00 → "Jeff"` etc., and the HTML
  regenerates with names.

## Takedown policy

If you hosted a Space and want it removed, open an issue or email
[your-email]. We'll take it down. No questions asked.
