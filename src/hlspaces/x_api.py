"""X API wrapper — Space metadata and host tweet enumeration."""
from __future__ import annotations

import re
from datetime import datetime
from typing import Iterator, Optional

import tweepy

from .config import X_BEARER_TOKEN
from .models import Participant, SpaceMetadata

SPACE_URL_RE = re.compile(r"(?:x|twitter)\.com/i/spaces/([A-Za-z0-9]+)")


def extract_space_id(url_or_id: str) -> str:
    """Accept a full URL or a bare space ID."""
    m = SPACE_URL_RE.search(url_or_id)
    if m:
        return m.group(1)
    return url_or_id.strip()


def _client() -> tweepy.Client:
    if not X_BEARER_TOKEN:
        raise RuntimeError("X_BEARER_TOKEN not set in environment")
    return tweepy.Client(bearer_token=X_BEARER_TOKEN, wait_on_rate_limit=True)


def fetch_space_metadata(space_id: str) -> SpaceMetadata:
    """Fetch metadata for a Space. Works for live, scheduled, and recently-ended Spaces.

    May raise tweepy.NotFound for older ended Spaces that X has cleaned up.
    """
    client = _client()

    space_fields = [
        "host_ids", "created_at", "creator_id", "ended_at", "lang",
        "participant_count", "scheduled_start", "speaker_ids", "started_at",
        "state", "title", "is_ticketed",
    ]
    expansions = ["host_ids", "creator_id", "speaker_ids"]
    user_fields = ["username", "name"]

    response = client.get_space(
        id=space_id,
        space_fields=space_fields,
        expansions=expansions,
        user_fields=user_fields,
    )

    if not response.data:
        raise ValueError(f"No data returned for space {space_id}")

    space = response.data
    users_by_id: dict[str, dict] = {}
    if response.includes and "users" in response.includes:
        for u in response.includes["users"]:
            users_by_id[str(u.id)] = {"username": u.username, "name": u.name}

    host_ids = set(str(h) for h in (space.host_ids or []))
    speaker_ids = set(str(s) for s in (space.speaker_ids or []))
    creator_id = str(space.creator_id) if space.creator_id else None

    participants: list[Participant] = []
    host_username = None
    for uid, info in users_by_id.items():
        if uid in host_ids:
            role = "host"
            if not host_username:
                host_username = info["username"]
        elif uid in speaker_ids:
            role = "speaker"
        elif uid == creator_id:
            role = "creator"
        else:
            role = "participant"
        participants.append(Participant(
            user_id=uid,
            username=info["username"],
            display_name=info["name"],
            role=role,
        ))

    return SpaceMetadata(
        space_id=space_id,
        title=getattr(space, "title", None),
        state=space.state,
        created_at=getattr(space, "created_at", None),
        started_at=getattr(space, "started_at", None),
        ended_at=getattr(space, "ended_at", None),
        scheduled_start=getattr(space, "scheduled_start", None),
        lang=getattr(space, "lang", None),
        is_ticketed=getattr(space, "is_ticketed", False) or False,
        participant_count=getattr(space, "participant_count", None),
        host_username=host_username,
        participants=participants,
        space_url=f"https://x.com/i/spaces/{space_id}",
    )


def find_space_ids_in_user_tweets(
    username: str,
    max_tweets: int = 3200,
    since: Optional[datetime] = None,
) -> Iterator[str]:
    """Enumerate Space IDs linked in a user's tweets.

    Yields unique Space IDs. The X API returns up to ~3200 most recent tweets
    via user timeline pagination on Basic tier.
    """
    client = _client()
    user_resp = client.get_user(username=username)
    if not user_resp.data:
        raise ValueError(f"User @{username} not found")
    user_id = user_resp.data.id

    seen: set[str] = set()
    paginator = tweepy.Paginator(
        client.get_users_tweets,
        id=user_id,
        max_results=100,
        tweet_fields=["created_at", "entities"],
        exclude=["replies"],
        start_time=since,
        limit=max(1, max_tweets // 100),
    )
    for tweet in paginator.flatten(limit=max_tweets):
        text = tweet.text or ""
        urls = []
        if tweet.entities and "urls" in tweet.entities:
            urls = [u.get("expanded_url", "") for u in tweet.entities["urls"]]
        for candidate in [text, *urls]:
            for match in SPACE_URL_RE.finditer(candidate):
                sid = match.group(1)
                if sid not in seen:
                    seen.add(sid)
                    yield sid
