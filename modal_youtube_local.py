"""Modal YouTube ingest (local audio) — pre-downloaded m4a, no yt-dlp on Modal."""
import modal

app = modal.App("hype-fm-youtube-local")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("ffmpeg")
    .pip_install(
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
    secrets=[modal.Secret.from_name("anthropic-api-key")],
    timeout=60 * 90,
)
def ingest_video(ep: dict, audio_bytes: bytes) -> dict:
    import os, time, traceback
    from pathlib import Path
    from datetime import datetime

    def log(msg):
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)

    entry_id = ep["id"]
    log(f"=== START {entry_id} ===")

    archive_root = Path("/archive")
    entry_dir = archive_root / entry_id
    entry_dir.mkdir(parents=True, exist_ok=True)

    audio_path = entry_dir / "audio.m4a"
    audio_path.write_bytes(audio_bytes)
    log(f"audio written: {audio_path.stat().st_size} bytes")

    os.environ["HF_HOME"] = "/models/hf"
    os.environ["XDG_CACHE_HOME"] = "/models"
    os.environ["WHISPER_DEVICE"] = "cuda"

    from hlspaces.models import SpaceMetadata

    meta = SpaceMetadata(
        space_id=entry_id,
        title=ep["title"],
        state="ended",
        host_username=ep["host_username"],
        space_url=ep["video_url"],
        audio_captured=True,
    )
    if ep.get("date_iso"):
        try:
            meta.started_at = datetime.fromisoformat(ep["date_iso"])
        except Exception:
            pass

    try:
        log("transcribing on GPU...")
        from hlspaces.transcribe import transcribe_with_diarization
        transcript = transcribe_with_diarization(audio_path, entry_id, skip_diarization=True)
        meta.audio_duration_seconds = transcript.duration_seconds
        log(f"  done: {len(transcript.chunks)} chunks, {transcript.duration_seconds:.0f}s")
    except Exception as e:
        log(f"TRANSCRIPTION FAILED: {e}")
        traceback.print_exc()
        return {"id": entry_id, "status": "transcription_failed", "error": str(e)}

    if transcript.chunks:
        try:
            log("summarizing with Claude...")
            from hlspaces.summarize import summarize_transcript
            summary = summarize_transcript(transcript, host_username=ep["host_username"])
            if summary:
                meta.summary_title = summary.get("title")
                meta.summary_description = summary.get("description")
                meta.topic_tags = summary.get("tags", [])
                meta.key_moments = summary.get("key_moments", [])
                meta.pull_quote = summary.get("pull_quote")
                meta.quote_attribution = summary.get("quote_attribution")
                meta.participants = summary.get("participants", [])
                log(f"  title: {meta.summary_title}")
        except Exception as e:
            log(f"summary failed (non-fatal): {e}")

    log("rendering archive entry...")
    from hlspaces.render import write_archive_entry
    write_archive_entry(archive_root, meta, transcript, audio_path)
    volume.commit()
    log(f"=== DONE {entry_id} ===")

    return {"id": entry_id, "status": "ok", "title": meta.summary_title}


@app.local_entrypoint()
def main():
    from pathlib import Path

    episodes = [
        {
            "id": "yt-qO8-nn1jFBI",
            "title": "Tokenized Leverage on Hyperliquid | Bounce.Tech",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=qO8-nn1jFBI",
            "date_iso": "2026-06-22",
            "file": "youtube_audio/yt-qO8-nn1jFBI.m4a",
        },
    ]

    for ep in episodes:
        audio_bytes = Path(ep["file"]).read_bytes()
        print(f"\nDispatching {ep['id']} ({len(audio_bytes):,} bytes)...")
        result = ingest_video.remote(ep, audio_bytes)
        print("  Result:", result)