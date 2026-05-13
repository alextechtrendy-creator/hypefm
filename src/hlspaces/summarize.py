"""Generate title, description, tags, key moments, and pull quote for a Space."""
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


SYSTEM_PROMPT = f"""You are writing titles, descriptions, and pull quotes for archived X Spaces about Hyperliquid (a decentralized perpetual futures exchange).

The goal: make someone in the Hyperliquid community stop scrolling and click. Wrong tone is press release. Right tone is intriguing fact.

Given a transcript with timestamps, produce JSON with FIVE fields:

1. "title": 8-15 words, sentence case. Rules:
   - Lead with the most interesting fact, claim, or angle — not the company name
   - Use specific numbers when meaningful ("488% backtest", "45% win rate", "80+ teams")
   - Promise tension or contrast when present
   - Avoid generic verbs: "launches", "building", "introduces", "explains"
   - Avoid press-release pattern "[Name]: [Generic descriptor]"
   - If a project name appears, only include it when the name itself is the hook

   Good: "Trading exotic perpetuals on Hyperliquid from weather to Fed rates"
   Good: "HyperLiquid ecosystem drama, EVM adoption challenges, and Cosmos collapse lessons"
   Good: "Pair Protocol's 45% win rate strategy: pair trading on Hyperliquid"
   Bad: "How [Company X] became Hyperliquid's [thing]"
   Bad: "[Company X]: Building the Complete [Y] on Hyperliquid"

2. "description": One line under 20 words. Concrete and intriguing. Add detail the title didn't.

3. "tags": Array of 2-3 topic tags from this controlled vocabulary ONLY: {TOPIC_VOCAB}
   Don't invent tags outside this list.

4. "key_moments": Array of 5-8 objects, each with:
   - "timestamp_seconds": integer
   - "label": short description under 12 words
   Spread roughly across full duration. Use actual transcript timestamps.

5. "pull_quote": ONE quote from the transcript, 8-25 words, that works standalone. Rules:
   - Must be intriguing, opinionated, surprising, funny, or specific
   - Must read as a coherent sentence — no filler like "yeah" "like" "you know"
   - Must NOT be context-dependent ("as I was saying", "that thing we mentioned")
   - Prefer concrete claims, numbers, contrarian takes, vivid metaphors
   - Light cleanup is OK (remove "um", "uh", fix obvious word slips); preserve meaning
   - If no quote in the transcript meets the bar, return null. A bad quote is worse than no quote.
   - Do NOT include quotation marks in the value itself.

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


def summarize_transcript(transcript: Transcript) -> Optional[dict]:
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
            max_tokens=1000,
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

    # Clean pull_quote: strip wrapping quotes, allow None
    pq = data.get("pull_quote")
    if pq and isinstance(pq, str):
        pq = pq.strip().strip('"').strip("'").strip()
        data["pull_quote"] = pq if pq else None
    else:
        data["pull_quote"] = None

    return data