"""Generate title, description, tags, and key moments for a Space using Claude Haiku."""
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


SYSTEM_PROMPT = f"""You are summarizing X Spaces (audio conversations) about Hyperliquid, a decentralized perpetual futures exchange.

Given a transcript with timestamps, produce a JSON object with FOUR fields:

1. "title": A descriptive title for the Space, 8-15 words, sentence case. Capture the actual topic, not a generic "weekly call" label. Examples:
   - "Why HLP outperformed every quarter of 2025 and what changes next year"
   - "How a quant team rewrote their execution stack around Hyperliquid"

2. "description": A one-line standfirst (under 20 words) describing what listeners get. Concrete and intriguing.

3. "tags": Array of 2-3 topic tags from this controlled vocabulary ONLY: {TOPIC_VOCAB}
   Don't invent tags outside this list.

4. "key_moments": Array of 5-8 objects, each with:
   - "timestamp_seconds": integer, the start time in seconds of that moment
   - "label": short description (under 12 words) of what happens at that moment
   The moments should map a listener through the Space — intro/setup, main topics, demos or specific examples, Q&A, roadmap/wrap-up. Spread them roughly across the full duration. Use timestamps that actually appear in the transcript.

Return ONLY valid JSON, no markdown fences, no commentary."""


def _build_timestamped_transcript(transcript: Transcript, char_limit: int = 60000) -> str:
    """Format transcript with timestamps so the LLM can pick key moments."""
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


def summarize_transcript(transcript: Transcript) -> Optional[dict]:
    """Call Claude Haiku to generate title, description, tags, and key moments."""
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
            max_tokens=800,
            system=SYSTEM_PROMPT,
            messages=[{
                "role": "user",
                "content": f"Transcript:\n\n{timestamped}"
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

    # Validate and clean key_moments
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

    return data