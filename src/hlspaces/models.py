"""Data models for archive entries."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class Participant(BaseModel):
    user_id: str
    username: str
    display_name: Optional[str] = None
    role: str  # "host", "co_host", "speaker", "listener"


class SpaceMetadata(BaseModel):
    space_id: str
    title: Optional[str] = None
    state: str  # "live", "scheduled", "ended"
    created_at: Optional[datetime] = None
    started_at: Optional[datetime] = None
    ended_at: Optional[datetime] = None
    scheduled_start: Optional[datetime] = None
    lang: Optional[str] = None
    is_ticketed: bool = False
    participant_count: Optional[int] = None
    host_username: Optional[str] = None
    participants: list[Participant] = Field(default_factory=list)
    space_url: str
    summary_title: Optional[str] = None
    summary_description: Optional[str] = None
    topic_tags: list[str] = Field(default_factory=list)
    key_moments: list[dict] = Field(default_factory=list)
    pull_quote: Optional[str] = None

    # Capture status
    audio_captured: bool = False
    audio_duration_seconds: Optional[float] = None
    capture_failure_reason: Optional[str] = None


class TranscriptChunk(BaseModel):
    """A single utterance: one speaker, one continuous span of speech."""

    start: float  # seconds from start of audio
    end: float
    speaker: str  # "SPEAKER_00", "SPEAKER_01", or a real name after manual labeling
    text: str


class Transcript(BaseModel):
    space_id: str
    language: str
    duration_seconds: float
    chunks: list[TranscriptChunk]
    speaker_map: dict[str, str] = Field(default_factory=dict)  # SPEAKER_00 -> "Jeff"
