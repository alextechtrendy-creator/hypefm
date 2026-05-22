"""Modal podcast ingest — transcribe + summarize pre-downloaded podcast episodes."""
import modal

app = modal.App("hype-fm-podcast")

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
    timeout=60 * 60,
)
def ingest_episode(ep: dict, audio_bytes: bytes) -> dict:
    import os, sys, time, traceback
    from pathlib import Path

    def log(msg):
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)

    ep_id = ep["id"]
    log(f"=== START {ep_id} ===")

    archive_root = Path("/archive")
    entry_dir = archive_root / ep_id
    entry_dir.mkdir(parents=True, exist_ok=True)

    audio_path = entry_dir / "audio.m4a"
    audio_path.write_bytes(audio_bytes)
    log(f"audio written: {audio_path.stat().st_size} bytes")

    os.environ["HF_HOME"] = "/models/hf"
    os.environ["XDG_CACHE_HOME"] = "/models"
    os.environ["WHISPER_DEVICE"] = "cuda"

    from hlspaces.models import SpaceMetadata, Transcript

    meta = SpaceMetadata(
        space_id=ep_id,
        title=ep["title"],
        state="ended",
        host_username=ep["host_username"],
        space_url=ep["episode_url"],
        audio_captured=True,
    )
    # Seed the date
    if ep.get("date_iso"):
        from datetime import datetime
        try:
            meta.started_at = datetime.fromisoformat(ep["date_iso"])
        except Exception:
            pass

    try:
        log("transcribing on GPU...")
        from hlspaces.transcribe import transcribe_with_diarization
        transcript = transcribe_with_diarization(audio_path, ep_id, skip_diarization=True)
        meta.audio_duration_seconds = transcript.duration_seconds
        log(f"  done: {len(transcript.chunks)} chunks, {transcript.duration_seconds:.0f}s")
    except Exception as e:
        log(f"TRANSCRIPTION FAILED: {e}")
        traceback.print_exc()
        return {"id": ep_id, "status": "transcription_failed", "error": str(e)}

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
    log(f"=== DONE {ep_id} ===")

    return {"id": ep_id, "status": "ok", "title": meta.summary_title}


@app.local_entrypoint()
def main():
    from pathlib import Path

    episodes = [
        {
            "id": "podcast-ep43-hyperlend",
            "title": "Exit Liquidity Ep 43 - All the alpha on Hyperlend",
            "host_username": "rekt_gang",
            "episode_url": "https://open.spotify.com/episode/6KYOxwbIYdKRsfoMaUownG",
            "date_iso": "2026-02-28T01:30:37",
            "file": "podcast_audio/ep43-hyperlend.mp3",
        },
        {
            "id": "podcast-ep37-nest",
            "title": "Exit Liquidity Ep 37 - MEGAHYPE'd w/ Nest",
            "host_username": "rekt_gang",
            "episode_url": "https://open.spotify.com/show/5fSUkDXU8a4yz3HJcDwgnx",
            "date_iso": "2026-01-16T00:12:25",
            "file": "podcast_audio/ep37-nest.mp3",
        },
        {
            "id": "podcast-ep29-hypurrfi",
            "title": "Exit Liquidity - HypurrFi Everything",
            "host_username": "rekt_gang",
            "episode_url": "https://open.spotify.com/show/5fSUkDXU8a4yz3HJcDwgnx",
            "date_iso": "2025-12-23T01:50:47",
            "file": "podcast_audio/ep29-hypurrfi.mp3",
        },
        {
            "id": "podcast-ep19-hyperliquid-update",
            "title": "Exit Liquidity - Hyperliquid Update",
            "host_username": "rekt_gang",
            "episode_url": "https://open.spotify.com/show/5fSUkDXU8a4yz3HJcDwgnx",
            "date_iso": "2025-11-30T00:52:16",
            "file": "podcast_audio/ep19-hyperliquid-update.mp3",
        },
    ]

    for ep in episodes:
        audio_bytes = Path(ep["file"]).read_bytes()
        print(f"\nDispatching {ep['id']} ({len(audio_bytes)} bytes)...")
        result = ingest_episode.remote(ep, audio_bytes)
        print("  Result:", result)