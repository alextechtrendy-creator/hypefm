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
            "id": "yt-JF5-eg8wr2M",
            "title": "HyperMeat YouTube JF5-eg8wr2M",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=JF5-eg8wr2M",
            "date_iso": "2026-09-22",
            "file": "youtube_audio/yt-JF5-eg8wr2M.m4a",
        },
        {
            "id": "yt-2M9Vd-cQdt0",
            "title": "HyperMeat YouTube 2M9Vd-cQdt0",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=2M9Vd-cQdt0",
            "date_iso": "2026-09-15",
            "file": "youtube_audio/yt-2M9Vd-cQdt0.m4a",
        },
        {
            "id": "yt-HAyMUJvm0N8",
            "title": "HyperMeat YouTube HAyMUJvm0N8",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=HAyMUJvm0N8",
            "date_iso": "2026-08-03",
            "file": "youtube_audio/yt-HAyMUJvm0N8.m4a",
        },
        {
            "id": "yt-HP9gtA7K5_E",
            "title": "HyperMeat YouTube HP9gtA7K5_E",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=HP9gtA7K5_E",
            "date_iso": "2026-07-21",
            "file": "youtube_audio/yt-HP9gtA7K5_E.m4a",
        },
        {
            "id": "yt--Hgq2PlQjPI",
            "title": "HyperMeat YouTube -Hgq2PlQjPI",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=-Hgq2PlQjPI",
            "date_iso": "2026-07-07",
            "file": "youtube_audio/yt--Hgq2PlQjPI.m4a",
        },
        {
            "id": "yt-V2a7OXBDzvA",
            "title": "HyperMeat YouTube V2a7OXBDzvA",
            "host_username": "B33Fbanks",
            "video_url": "https://www.youtube.com/watch?v=V2a7OXBDzvA",
            "date_iso": "2026-06-30",
            "file": "youtube_audio/yt-V2a7OXBDzvA.m4a",
        },
    ]

    for ep in episodes:
        audio_bytes = Path(ep["file"]).read_bytes()
        print(f"\nDispatching {ep['id']} ({len(audio_bytes):,} bytes)...")
        result = ingest_video.remote(ep, audio_bytes)
        print("  Result:", result)