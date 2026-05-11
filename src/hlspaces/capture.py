"""Audio capture for X Spaces using yt-dlp."""
from __future__ import annotations

import shutil
import subprocess
from pathlib import Path


class CaptureError(RuntimeError):
    """Raised when audio capture fails for any reason."""


def capture_space_audio(space_url: str, output_path: Path) -> Path:
    """Download the Space's audio to output_path (.m4a) using yt-dlp."""
    if not shutil.which("ffmpeg"):
        raise CaptureError("ffmpeg not found on PATH — install it first")
    if not shutil.which("yt-dlp"):
        raise CaptureError("yt-dlp not found on PATH — run: pip install yt-dlp")

    cookies_file = Path("cookies.txt")
    if not cookies_file.exists():
        raise CaptureError("cookies.txt not found in project folder")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    cmd = [
        "yt-dlp",
        "--cookies", str(cookies_file),
        "-o", str(output_path),
        space_url,
    ]

    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=60 * 60 * 6
        )
    except subprocess.TimeoutExpired as e:
        raise CaptureError(f"Capture timed out: {e}") from e

    if result.returncode != 0:
        raise CaptureError(
            f"yt-dlp failed (exit {result.returncode}): {result.stderr.strip()[:500]}"
        )

    if not output_path.exists():
        # yt-dlp sometimes writes with a different extension
        candidates = sorted(
            output_path.parent.glob(f"{output_path.stem}.*"),
            key=lambda p: p.stat().st_mtime,
            reverse=True,
        )
        if candidates:
            candidates[0].rename(output_path)
        else:
            raise CaptureError("yt-dlp reported success but no audio file was found")

    return output_path