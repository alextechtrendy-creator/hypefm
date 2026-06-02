"""Modal YouTube ingest — transcribe + summarize YouTube videos via yt-dlp."""
import modal

app = modal.App("hype-fm-youtube")

image = (
    modal.Image.debian_slim(python_version="3.12")
    .apt_install("ffmpeg")
    .pip_install(
        "yt-dlp",
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
        modal.Secret.from_name("youtube-cookies"),
    ],
    timeout=60 * 90,
    max_containers=1,
)
def ingest_video(video_id: str, host_username: str = "B33Fbanks") -> dict:
    import os, subprocess, time, json, traceback
    from pathlib import Path
    from datetime import datetime

    def log(msg):
        ts = time.strftime("%H:%M:%S")
        print(f"[{ts}] {msg}", flush=True)

    entry_id = f"yt-{video_id}"
    log(f"=== START {entry_id} ===")

    archive_root = Path("/archive")
    entry_dir = archive_root / entry_id

    if (entry_dir / "metadata.json").exists() and (entry_dir / "transcript.json").exists():
        log("already archived, skipping")
        return {"id": entry_id, "status": "skipped"}

    entry_dir.mkdir(parents=True, exist_ok=True)
    os.environ["HF_HOME"] = "/models/hf"
    os.environ["XDG_CACHE_HOME"] = "/models"
    os.environ["WHISPER_DEVICE"] = "cuda"

    cookies_path = Path("/tmp/yt_cookies.txt")
    cookies_path.write_text(os.environ["YT_COOKIES_TXT"])
    log(f"cookies written ({cookies_path.stat().st_size} bytes)")

    video_url = f"https://www.youtube.com/watch?v={video_id}"

    log("fetching YouTube metadata...")
    try:
        info_result = subprocess.run(
            ["yt-dlp", "--cookies", str(cookies_path), "--dump-json", "--no-warnings", video_url],
            capture_output=True, text=True, timeout=120,
        )
        info = json.loads(info_result.stdout)
        yt_title = info.get("title", "Untitled video")
        upload_date_str = info.get("upload_date")
        duration = info.get("duration", 0)
        log(f"  title: {yt_title!r}")
        log(f"  date: {upload_date_str}, duration: {duration}s")
    except Exception as e:
        log(f"metadata fetch failed: {e}")
        log(f"  stderr tail: {info_result.stderr[-300:] if 'info_result' in dir() else 'no stderr'}")
        return {"id": entry_id, "status": "metadata_failed", "error": str(e)}

    log("downloading audio with yt-dlp...")
    audio_path = entry_dir / "audio.m4a"
    result = subprocess.run([
        "yt-dlp", "--cookies", str(cookies_path),
        "-x", "--audio-format", "m4a",
        "-o", str(entry_dir / "audio.%(ext)s"),
        "--no-warnings", video_url,
    ], capture_output=True, text=True, timeout=60 * 30)
    log(f"  yt-dlp exit: {result.returncode}")
    if not audio_path.exists():
        candidates = sorted(entry_dir.glob("audio.*"), key=lambda p: p.stat().st_mtime, reverse=True)
        if candidates:
            candidates[0].rename(audio_path)
    if not audio_path.exists():
        log(f"  audio download FAILED. stderr tail: {result.stderr[-300:]}")
        return {"id": entry_id, "status": "audio_failed", "error": result.stderr[-200:]}
    log(f"  audio file: {audio_path.stat().st_size} bytes")

    from hlspaces.models import SpaceMetadata, Transcript

    meta = SpaceMetadata(
        space_id=entry_id,
        title=yt_title,
        state="ended",
        host_username=host_username,
        space_url=video_url,
        audio_captured=True,
    )
    if upload_date_str:
        try:
            meta.started_at = datetime.strptime(upload_date_str, "%Y%m%d")
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
            summary = summarize_transcript(transcript, host_username=host_username)
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
    video_ids = [
        "KoDXBbN-3cs",  # Kinetiq Is Dominating Hyperliquid
        "a0GliNinkgs",  # Hyperliquid Strategies CEO
        "VL18kbuj_u4",  # Felix Protocol - HIP-3 Markets, RWAs
    ]
    print(f"\nDispatching {len(video_ids)} YouTube videos to Modal...\n")
    successes = 0
    failures = []
    for result in ingest_video.map(video_ids, return_exceptions=True):
        if isinstance(result, Exception):
            failures.append(("?", f"container exception: {result}"))
            continue
        vid = result["id"]
        status = result["status"]
        if status == "ok":
            print(f"  music {vid}: {result.get('title', '(no title)')}")
            successes += 1
        elif status == "skipped":
            print(f"  skip {vid}: already archived")
            successes += 1
        else:
            print(f"  FAIL {vid}: {status}")
            failures.append((vid, result.get("error", "")[:120]))
    print(f"\n=== Summary ===")
    print(f"  Successes: {successes}")
    print(f"  Failures: {len(failures)}")
    for vid, err in failures:
        print(f"  {vid}: {err}")