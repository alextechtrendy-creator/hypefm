"""Generate title, description, tags, key moments, pull quote, and participants for a Space."""
from __future__ import annotations

import json
import os
from typing import Optional

from anthropic import Anthropic

from .models import Transcript


TOPIC_VOCAB = [
    "HLP", "vaults", "listings", "funding", "perps",
    "governance", "infrastructure", "L1", "market-making",
    "execution", "trading", "tokenomics", "ecosystem",
    "community", "roadmap"
]


SYSTEM_PROMPT = f"""You are writing titles, descriptions, pull quotes, and participant lists for archived X Spaces about Hyperliquid (a decentralized perpetual futures exchange).

The goal: make someone in the Hyperliquid community stop scrolling and click. Wrong tone is press release. Right tone is intriguing fact.

Given a transcript with timestamps, produce JSON with SEVEN fields:

1. "title": 8-15 words, sentence case. Rules:
   - Lead with the most interesting fact, claim, or angle — not the company name
   - Use specific numbers when meaningful ("488% backtest", "45% win rate", "80+ teams")
   - Promise tension or contrast when present
   - Avoid generic verbs: "launches", "building", "introduces", "explains"
   - Avoid press-release pattern "[Name]: [Generic descriptor]"

   Good: "Trading exotic perpetuals on Hyperliquid from weather to Fed rates"
   Good: "HyperLiquid ecosystem drama, EVM adoption challenges, and Cosmos collapse lessons"
   Good: "Pair Protocol's 45% win rate strategy: pair trading on Hyperliquid"
   Bad: "How [Company X] became Hyperliquid's [thing]"
   Bad: "[Company X]: Building the Complete [Y] on Hyperliquid"

2. "description": One line under 20 words. Concrete and intriguing.

3. "tags": Array of 2-3 from this controlled vocabulary ONLY: {TOPIC_VOCAB}

4. "key_moments": Array of 5-8 objects with "timestamp_seconds" (int) and "label" (under 12 words).

5. "pull_quote": ONE quote from the transcript, 8-25 words, that works standalone. Rules:
   - Intriguing, opinionated, surprising, funny, or specific
   - Reads as a coherent sentence — no filler ("yeah", "like", "you know")
   - Not context-dependent
   - Light cleanup OK (remove "um", "uh"), preserve meaning
   - If nothing meets the bar, return null
   - Do NOT include quotation marks in the value

6. "quote_attribution": Object identifying who said the pull_quote. Rules:
   - Read the transcript carefully — who is the speaker at that moment?
   - Use context (who was just introduced, who's been speaking) to identify
   - If you cannot identify with confidence, return null
   - Object shape: {{"name": "Jeff", "team": "Hydromancer", "role": "co-founder"}}
   - "name": first name or commonly-used name from the transcript
   - "team": company/project they represent. Use canonical name (just "Hydromancer", not "the Hydromancer team")
   - "role": short role like "co-founder", "head of growth", "engineer". null if not stated.

7. "participants": Array of objects for the people speaking on the Space. Rules:
   - Include host AND all named guests who actually spoke
   - Order: host first, then guests by importance to the conversation
   - Exclude people only mentioned in passing
   - Maximum 6
   - Object shape: {{"name": "Jeff", "handle": "rekt_gang", "team": "Hydromancer", "role": "host"}}
     - "name": as used in the transcript
     - "handle": X handle WITHOUT the @ sign, only if explicitly mentioned in the transcript. null otherwise.
     - "team": canonical company/project name, or null
     - "role": "host" or "guest"
   - If you cannot reliably identify anyone, return an empty array

Return ONLY valid JSON, no markdown fences, no commentary."""


def _build_timestamped_transcript(transcript: Transcript, char_limit: int = 60000) -> str:
    lines = []
    total_chars = 0
    for chunk in transcript.chunks:
        ts = int(chunk.start)
        line = f"[{ts}s] {chunk.text}"
        if total_chars + len(line) > char_limit:
            lines.append("[transcript truncated]")
            break
        lines.append(line)
        total_chars += len(line)
    return "\n".join(lines)


def summarize_transcript(transcript: Transcript, host_username: Optional[str] = None) -> Optional[dict]:
    api_key = os.getenv("ANTHROPIC_API_KEY")
    if not api_key:
        print("  warn: ANTHROPIC_API_KEY not set, skipping summarization")
        return None

    if not transcript.chunks:
        print("  warn: empty transcript, skipping summarization")
        return None

    full_text = " ".join(c.text for c in transcript.chunks)
    if len(full_text) < 200:
        print("  warn: transcript too short, skipping summarization")
        return None

    timestamped = _build_timestamped_transcript(transcript)
    client = Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model="claude-haiku-4-5",
            max_tokens=2000,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": (
                    (f"This Space was hosted by @{host_username}. When identifying the host, use this handle.\n\n" if host_username else "")
                    + f"Transcript:\n\n{timestamped}"
                )
            }]
        )
    except Exception as e:
        print(f"  warn: Anthropic API call failed: {e}")
        return None

    text = response.content[0].text.strip()
    if text.startswith("```"):
        lines = text.split("\n")
        text = "\n".join(lines[1:-1] if lines[-1].startswith("```") else lines[1:])

    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"  warn: could not parse LLM response as JSON: {e}")
        print(f"  raw response: {text[:200]}")
        return None

    required = ["title", "description", "tags", "key_moments"]
    if not all(k in data for k in required):
        print(f"  warn: LLM response missing required fields")
        return None

    if isinstance(data.get("tags"), list):
        data["tags"] = [t for t in data["tags"] if t in TOPIC_VOCAB]

    cleaned_moments = []
    for moment in data.get("key_moments", []):
        if isinstance(moment, dict) and "timestamp_seconds" in moment and "label" in moment:
            try:
                cleaned_moments.append({
                    "timestamp_seconds": int(moment["timestamp_seconds"]),
                    "label": str(moment["label"]).strip(),
                })
            except (ValueError, TypeError):
                continue
    data["key_moments"] = cleaned_moments

    pq = data.get("pull_quote")
    if pq and isinstance(pq, str):
        pq = pq.strip().strip('"').strip("'").strip()
        data["pull_quote"] = pq if pq else None
    else:
        data["pull_quote"] = None

    qa = data.get("quote_attribution")
    if qa and isinstance(qa, dict) and qa.get("name"):
        data["quote_attribution"] = {
            "name": str(qa.get("name", "")).strip() or None,
            "team": (str(qa.get("team", "")).strip() or None) if qa.get("team") else None,
            "role": (str(qa.get("role", "")).strip() or None) if qa.get("role") else None,
        }
    else:
        data["quote_attribution"] = None

    cleaned_participants = []
    for p in data.get("participants", []):
        if not isinstance(p, dict) or not p.get("name"):
            continue
        cleaned_participants.append({
            "name": str(p.get("name", "")).strip(),
            "handle": (str(p.get("handle", "")).strip().lstrip("@") or None) if p.get("handle") else None,
            "team": (str(p.get("team", "")).strip() or None) if p.get("team") else None,
            "role": (str(p.get("role", "")).strip() or "guest"),
        })
    data["participants"] = cleaned_participants

    return data