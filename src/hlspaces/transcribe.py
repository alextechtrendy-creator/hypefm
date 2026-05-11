"""Transcription + diarization pipeline.

Strategy:
  1. Run faster-whisper to get word-level timestamps and text.
  2. Run pyannote.audio to get speaker turns (intervals labeled SPEAKER_00, etc.).
  3. Merge: assign each word to the speaker whose turn covers its midpoint,
     then group consecutive same-speaker words into chunks.

This is more robust than asking Whisper to "do diarization" itself — Whisper
doesn't actually diarize, and pyannote is purpose-built for it.
"""
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Optional

from .config import HF_TOKEN, HYPERLIQUID_VOCAB, WHISPER_DEVICE, WHISPER_MODEL
from .models import Transcript, TranscriptChunk


@dataclass
class _Word:
    start: float
    end: float
    text: str


@dataclass
class _Turn:
    start: float
    end: float
    speaker: str


def _resolve_device(device: str) -> str:
    # Honor explicit setting first
    if device == "cuda":
        return "cuda"
    if device == "cpu":
        return "cpu"
    # Auto: check for CUDA via env var (Modal sets these), then PyTorch as fallback
    import os
    if os.environ.get("CUDA_VISIBLE_DEVICES") or os.path.exists("/usr/local/cuda"):
        return "cuda"
    try:
        import torch
        if torch.cuda.is_available():
            return "cuda"
    except Exception:
        pass
    return "cpu"

def _transcribe_words(audio_path: Path) -> tuple[list[_Word], str, float]:
    """Returns (words, language, duration)."""
    from faster_whisper import WhisperModel

    device = _resolve_device(WHISPER_DEVICE)
    compute_type = "float16" if device == "cuda" else "int8"

    model = WhisperModel(WHISPER_MODEL, device=device, compute_type=compute_type)

    segments, info = model.transcribe(
        str(audio_path),
        word_timestamps=True,
        vad_filter=True,  # skip silence — much faster on Spaces with long pauses
    )

    words: list[_Word] = []
    for seg in segments:
        if seg.words:
            for w in seg.words:
                if w.start is None or w.end is None:
                    continue
                words.append(_Word(start=w.start, end=w.end, text=w.word))
        else:
            # Fallback: no word-level timestamps for this segment
            words.append(_Word(start=seg.start, end=seg.end, text=seg.text))

    return words, info.language, info.duration


def _diarize(audio_path: Path) -> list[_Turn]:
    """Run pyannote diarization. Returns list of speaker turns."""
    if not HF_TOKEN:
        raise RuntimeError(
            "HF_TOKEN not set. Required for pyannote diarization model. "
            "See README setup instructions."
        )

    from pyannote.audio import Pipeline
    import torch

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        token=HF_TOKEN,
    )

    device = _resolve_device(WHISPER_DEVICE)
    if device == "cuda":
        pipeline.to(torch.device("cuda"))

    diarization = pipeline(str(audio_path))

    turns: list[_Turn] = []
    for turn, _, speaker in diarization.itertracks(yield_label=True):
        turns.append(_Turn(start=turn.start, end=turn.end, speaker=speaker))

    return turns


def _assign_speakers(words: list[_Word], turns: list[_Turn]) -> list[TranscriptChunk]:
    """Assign each word to a speaker, then group into chunks."""
    if not turns:
        # No diarization: split into time-based chunks (~30 seconds each)
        if not words:
            return []
        chunks: list[TranscriptChunk] = []
        current_words: list[_Word] = []
        chunk_start = words[0].start
        for w in words:
            current_words.append(w)
            if w.end - chunk_start >= 30.0:
                chunks.append(TranscriptChunk(
                    start=current_words[0].start,
                    end=current_words[-1].end,
                    speaker='SPEAKER_00',
                    text=' '.join(cw.text.strip() for cw in current_words),
                ))
                current_words = []
                if words.index(w) + 1 < len(words):
                    chunk_start = w.end
        if current_words:
            chunks.append(TranscriptChunk(
                start=current_words[0].start,
                end=current_words[-1].end,
                speaker='SPEAKER_00',
                text=' '.join(cw.text.strip() for cw in current_words),
            ))
        return chunks

    turns_sorted = sorted(turns, key=lambda t: t.start)

    def speaker_for(midpoint: float) -> str:
        # Linear scan is fine for typical Space length (hundreds of turns).
        # Bisect would be a micro-optimization.
        for t in turns_sorted:
            if t.start <= midpoint <= t.end:
                return t.speaker
        # Outside any turn — pick nearest
        nearest = min(turns_sorted, key=lambda t: min(abs(t.start - midpoint), abs(t.end - midpoint)))
        return nearest.speaker

    # Tag each word
    tagged: list[tuple[_Word, str]] = []
    for w in words:
        mid = (w.start + w.end) / 2
        tagged.append((w, speaker_for(mid)))

    # Group consecutive same-speaker words
    chunks: list[TranscriptChunk] = []
    if not tagged:
        return chunks

    current_speaker = tagged[0][1]
    current_words: list[_Word] = [tagged[0][0]]

    for word, speaker in tagged[1:]:
        if speaker == current_speaker:
            current_words.append(word)
        else:
            chunks.append(TranscriptChunk(
                start=current_words[0].start,
                end=current_words[-1].end,
                speaker=current_speaker,
                text=" ".join(w.text.strip() for w in current_words),
            ))
            current_speaker = speaker
            current_words = [word]

    if current_words:
        chunks.append(TranscriptChunk(
            start=current_words[0].start,
            end=current_words[-1].end,
            speaker=current_speaker,
            text=" ".join(w.text.strip() for w in current_words),
        ))

    return chunks


def transcribe_with_diarization(
    audio_path: Path,
    space_id: str,
    skip_diarization: bool = False,
) -> Transcript:
    """Full transcription + diarization pipeline."""
    words, language, duration = _transcribe_words(audio_path)
    turns = [] if skip_diarization else _diarize(audio_path)
    chunks = _assign_speakers(words, turns)

    return Transcript(
        space_id=space_id,
        language=language,
        duration_seconds=duration,
        chunks=chunks,
        speaker_map={},
    )
