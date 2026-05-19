"""Render an archive entry: markdown transcript + standalone HTML page."""
from __future__ import annotations

from pathlib import Path

from .models import SpaceMetadata, Transcript


def _format_timestamp(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    if h:
        return f"{h}:{m:02d}:{s:02d}"
    return f"{m}:{s:02d}"


def _resolve_speaker(speaker_id: str, speaker_map: dict[str, str]) -> str:
    return speaker_map.get(speaker_id, speaker_id)


def _escape(text: str) -> str:
    return (text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def render_markdown(meta: SpaceMetadata, transcript: Transcript) -> str:
    lines: list[str] = []
    title = meta.summary_title or meta.title or "Untitled Space"
    lines.append(f"# {title}")
    lines.append("")
    if meta.summary_description:
        lines.append(f"_{meta.summary_description}_")
        lines.append("")
    if meta.pull_quote:
        lines.append(f"> {meta.pull_quote}")
        if meta.quote_attribution and meta.quote_attribution.get("name"):
            name = meta.quote_attribution.get("name", "")
            team = meta.quote_attribution.get("team")
            attrib = f"— {name}" + (f", {team}" if team else "")
            lines.append(f"> {attrib}")
        lines.append("")
    if meta.host_username:
        lines.append(f"**Host:** @{meta.host_username}")
    if meta.started_at:
        lines.append(f"**Date:** {meta.started_at.strftime('%Y-%m-%d')}")
    if transcript.duration_seconds:
        lines.append(f"**Duration:** {_format_timestamp(transcript.duration_seconds)}")
    if meta.topic_tags:
        lines.append(f"**Tags:** {', '.join(meta.topic_tags)}")
    lines.append(f"**Source:** {meta.space_url}")
    lines.append("")
    if meta.participants:
        lines.append("## Who's talking")
        lines.append("")
        for p in meta.participants:
            name = p.get("name", "")
            handle = p.get("handle")
            team = p.get("team")
            role = p.get("role", "guest")
            line = f"- **{name}**"
            if handle:
                line += f" (@{handle})"
            if team:
                line += f" — {team}"
            line += f" _{role}_"
            lines.append(line)
        lines.append("")
    if meta.key_moments:
        lines.append("## Key moments")
        lines.append("")
        for m in meta.key_moments:
            ts = _format_timestamp(m.get("timestamp_seconds", 0))
            lines.append(f"- **[{ts}]** {m.get('label', '')}")
        lines.append("")
    lines.append("## Transcript")
    lines.append("")
    for chunk in transcript.chunks:
        speaker = _resolve_speaker(chunk.speaker, transcript.speaker_map)
        ts = _format_timestamp(chunk.start)
        lines.append(f"**[{ts}] {speaker}:** {chunk.text}")
        lines.append("")
    return "\n".join(lines)


_HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{title} - hype.fm</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{
    --bg: #fafaf7;
    --bg-card: #ffffff;
    --fg: #222;
    --fg-muted: #777;
    --fg-faint: #999;
    --accent: #0d6856;
    --accent-bg: rgba(13, 104, 86, 0.1);
    --quote-bg: #043b30;
    --quote-fg: #fafaf7;
    --quote-accent: #97FCE4;
    --border: #d4d2c5;
    --border-light: #e5e5e0;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: Verdana, Geneva, sans-serif;
    background: var(--bg); color: var(--fg);
    margin: 0; line-height: 1.5; -webkit-font-smoothing: antialiased;
  }}
  .container {{ max-width: 760px; margin: 0 auto; padding: 1.5rem 1.25rem 4rem; }}
  .back {{
    font-size: 11px; color: var(--fg-muted);
    text-decoration: none; display: inline-block; margin-bottom: 1.25rem;
  }}
  .back:hover {{ color: var(--accent); }}
  h1 {{
    font-size: 24px; font-weight: 500; line-height: 1.25;
    margin: 0 0 0.5rem; letter-spacing: -0.01em;
  }}
  .description {{
    font-size: 14px; color: #555;
    margin: 0 0 1rem; line-height: 1.55;
  }}
  .quote-card {{
    background: var(--quote-bg);
    border-radius: 8px;
    padding: 22px 24px;
    margin: 0 0 1.25rem;
  }}
  .quote-text {{
    font-family: Georgia, serif;
    font-style: italic;
    font-size: 17px;
    color: var(--quote-fg);
    line-height: 1.4;
    margin: 0;
    font-weight: 500;
  }}
  .quote-byline {{
    margin: 14px 0 0; padding-top: 12px;
    border-top: 1px solid rgba(151, 252, 228, 0.18);
    display: flex; gap: 8px; align-items: baseline; flex-wrap: wrap;
    font-size: 12px; line-height: 1.4;
  }}
  .quote-byline-name {{ color: var(--quote-fg); font-weight: 600; }}
  .quote-byline-role {{ color: rgba(151, 252, 228, 0.85); }}
  .quote-byline-sep {{ color: rgba(151, 252, 228, 0.4); }}
  .quote-byline-team {{
    display: inline-flex; align-items: center;
    background: rgba(151, 252, 228, 0.12);
    border: 1px solid rgba(151, 252, 228, 0.3);
    color: var(--quote-accent); font-weight: 500;
    padding: 2px 9px; border-radius: 12px;
    text-decoration: none; font-size: 11px;
    transition: background 0.1s;
  }}
  .quote-byline-team:hover {{
    background: rgba(151, 252, 228, 0.22);
    border-color: rgba(151, 252, 228, 0.5);
  }}
  .meta {{ font-size: 11px; color: var(--fg-faint); margin: 0 0 1.25rem; }}
  .meta .tag {{ color: var(--accent); font-weight: 500; cursor: pointer; }}
  .meta .tag:hover {{ text-decoration: underline; }}
  audio {{ width: 100%; height: 42px; margin-bottom: 1.5rem; }}
  .audio-unavailable {{
    font-size: 12px; color: var(--fg-muted); font-style: italic;
    padding: 0.7rem 0.9rem; background: white;
    border: 1px solid var(--border-light); border-radius: 6px;
    margin-bottom: 1.5rem;
  }}
  .section-label {{
    font-size: 11px; color: var(--fg-muted);
    margin: 1.5rem 0 0.5rem; font-weight: 500;
    text-transform: uppercase; letter-spacing: 0.06em;
  }}
  .participants {{ display: flex; flex-direction: column; margin-bottom: 1.75rem; }}
  .participant {{
    display: flex; gap: 16px; padding: 10px 0;
    border-top: 1px solid var(--border-light);
    align-items: baseline;
  }}
  .participant:first-of-type {{ border-top: 0; padding-top: 4px; }}
  .participant-name {{
    font-size: 13px; font-weight: 500; color: var(--fg);
    min-width: 120px;
  }}
  .participant-name a {{ color: var(--accent); text-decoration: none; }}
  .participant-name a:hover {{ text-decoration: underline; }}
  .participant-affiliation {{
    font-size: 12px; color: #666; flex: 1; line-height: 1.45;
  }}
  .participant-role {{
    font-size: 10px; color: var(--accent); font-weight: 500;
    text-transform: uppercase; letter-spacing: 0.05em;
    background: var(--accent-bg); padding: 2px 7px; border-radius: 3px;
  }}
  .moments {{ display: flex; flex-direction: column; gap: 2px; margin-bottom: 1.75rem; }}
  .moment {{
    display: flex; gap: 12px; align-items: baseline;
    padding: 8px 10px; margin: 0 -10px;
    border-radius: 4px; cursor: pointer;
    transition: background 0.1s;
  }}
  .moment:hover {{ background: white; }}
  .moment-ts {{
    font-size: 12px; color: var(--accent); font-weight: 500;
    min-width: 52px; font-variant-numeric: tabular-nums;
  }}
  .moment-label {{ font-size: 13px; margin: 0; line-height: 1.45; color: #444; }}
  .transcript-toggle {{
    border-top: 1px solid var(--border-light); padding: 1rem 0 0 0;
    margin-top: 1.5rem;
    font-size: 12px; color: var(--accent); cursor: pointer;
    background: none; border-left: none; border-right: none; border-bottom: none;
    font-family: inherit; font-weight: 500;
  }}
  .transcript-toggle:hover {{ text-decoration: underline; }}
  #transcript {{ display: none; margin-top: 1rem; }}
  #transcript.visible {{ display: block; }}
  .chunk {{
    padding: 0.7rem 0.85rem; margin-bottom: 0.4rem; background: white;
    border: 1px solid var(--border-light); border-radius: 6px; cursor: pointer;
    transition: border-color 0.1s;
  }}
  .chunk:hover {{ border-color: var(--border); }}
  .chunk-header {{
    display: flex; gap: 0.6rem; font-size: 11px; margin-bottom: 0.25rem;
    color: var(--fg-muted);
  }}
  .chunk-ts {{ color: var(--accent); font-variant-numeric: tabular-nums; font-weight: 500; }}
  .chunk-speaker {{ font-weight: 500; }}
  .chunk-text {{ color: #333; font-size: 13px; line-height: 1.55; }}
  .footer {{
    margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border-light);
    color: var(--fg-faint); font-size: 11px; text-align: center;
  }}
  .footer a {{ color: var(--fg-muted); text-decoration: none; }}
  .footer a:hover {{ color: var(--accent); }}
  @media (max-width: 600px) {{
    h1 {{ font-size: 20px; }}
    .quote-text {{ font-size: 15px; }}
    .quote-card {{ padding: 18px 20px; }}
  }}
</style>
</head>
<body>
<div class="container">

<a href="../../index.html" class="back">&larr; back to hype.fm</a>

<h1>{title}</h1>
{description_html}
{quote_card_html}
<p class="meta">{meta_html}</p>

{audio_section}

{participants_section}

{moments_section}

{transcript_section}

<div class="footer">
  <a href="../../index.html">hype.fm</a> &nbsp;&middot;&nbsp;
  <a href="{space_url}" target="_blank" rel="noopener">view on X</a>
</div>

</div>

<script>
  const audio = document.querySelector('audio');
  function seekTo(t) {{
    if (!audio) return;
    audio.currentTime = t;
    audio.play();
    audio.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
  }}
  document.querySelectorAll('[data-start]').forEach(el => {{
    el.addEventListener('click', () => {{
      const t = parseFloat(el.dataset.start);
      if (!isNaN(t)) seekTo(t);
    }});
  }});
  const toggle = document.getElementById('transcript-toggle');
  const transcript = document.getElementById('transcript');
  if (toggle && transcript) {{
    toggle.addEventListener('click', () => {{
      const visible = transcript.classList.toggle('visible');
      toggle.textContent = visible ? '- hide full transcript' : '+ show full transcript';
    }});
  }}
</script>
</body>
</html>
"""


def render_html(meta: SpaceMetadata, transcript: Transcript, audio_filename: str = "audio.m4a") -> str:
    audio_url = f"https://pub-09a0dd3dd2e44d25b3f0948f1c3d2b33.r2.dev/{meta.space_id}/audio.m4a"
    title = meta.summary_title or meta.title or "Untitled Space"

    description_html = ""
    if meta.summary_description:
        description_html = f'<p class="description">{_escape(meta.summary_description)}</p>'

    quote_card_html = ""
    if meta.pull_quote:
        quote_html = f'<p class="quote-text">"{_escape(meta.pull_quote)}"</p>'
        byline_html = ""
        attr = meta.quote_attribution
        if attr and attr.get("name"):
            parts = [f'<span class="quote-byline-name">{_escape(attr["name"])}</span>']
            if attr.get("role"):
                parts.append(f'<span class="quote-byline-role">{_escape(attr["role"])}</span>')
            if attr.get("team"):
                team_url = "../../index.html?team=" + _escape(attr["team"])
                parts.append('<span class="quote-byline-sep">&middot;</span>')
                parts.append(f'<a class="quote-byline-team" href="{team_url}">{_escape(attr["team"])}</a>')
            byline_html = f'<div class="quote-byline">{"".join(parts)}</div>'
        quote_card_html = f'<div class="quote-card">{quote_html}{byline_html}</div>'

    meta_parts = []
    if meta.host_username:
        meta_parts.append(f"@{_escape(meta.host_username)}")
    if meta.started_at:
        meta_parts.append(meta.started_at.strftime("%b %d, %Y").lower())
    if transcript.duration_seconds:
        meta_parts.append(_format_timestamp(transcript.duration_seconds))
    meta_html = " &middot; ".join(meta_parts)
    if meta.topic_tags:
        tag_html = ", ".join(f'<a class="tag" href="../../index.html?tag={_escape(t)}">{_escape(t)}</a>' for t in meta.topic_tags)
        meta_html += f' &middot; {tag_html}'

    if meta.audio_captured:
        audio_section = f'<audio controls preload="metadata" src="{audio_url}"></audio>'
    else:
        reason = meta.capture_failure_reason or "Audio not available."
        audio_section = f'<div class="audio-unavailable">{_escape(reason)}</div>'

    participants_section = ""
    if meta.participants:
        participant_items = []
        for p in meta.participants:
            name = _escape(p.get("name", ""))
            handle = p.get("handle")
            team = p.get("team")
            role = p.get("role", "guest")
            if handle:
                name_html = f'<a href="https://x.com/{_escape(handle)}" target="_blank" rel="noopener">{name}</a>'
                if name:
                    name_html += f' <span style="color:#999;font-weight:400;">@{_escape(handle)}</span>'
            else:
                name_html = name
            affiliation = team if team else "&mdash;"
            participant_items.append(
                f'<div class="participant">'
                f'<div class="participant-name">{name_html}</div>'
                f'<div class="participant-affiliation">{_escape(affiliation) if affiliation != "&mdash;" else affiliation}</div>'
                f'<span class="participant-role">{_escape(role)}</span>'
                f'</div>'
            )
        participants_section = (
            '<p class="section-label">who\'s talking</p>'
            f'<div class="participants">{"".join(participant_items)}</div>'
        )

    moments_section = ""
    if meta.key_moments:
        moment_items = []
        for m in meta.key_moments:
            ts_seconds = m.get("timestamp_seconds", 0)
            ts_label = _format_timestamp(ts_seconds)
            label = _escape(m.get("label", ""))
            moment_items.append(
                f'<div class="moment" data-start="{ts_seconds}">'
                f'<span class="moment-ts">{ts_label}</span>'
                f'<p class="moment-label">{label}</p>'
                f'</div>'
            )
        moments_section = (
            '<p class="section-label">key moments</p>'
            f'<div class="moments">{"".join(moment_items)}</div>'
        )

    chunks_html_parts = []
    for chunk in transcript.chunks:
        speaker = _resolve_speaker(chunk.speaker, transcript.speaker_map)
        ts = _format_timestamp(chunk.start)
        text = _escape(chunk.text)
        chunks_html_parts.append(
            f'<div class="chunk" data-start="{chunk.start:.2f}">'
            f'<div class="chunk-header">'
            f'<span class="chunk-ts">{ts}</span>'
            f'<span class="chunk-speaker">{_escape(speaker)}</span>'
            f'</div>'
            f'<div class="chunk-text">{text}</div>'
            f'</div>'
        )

    transcript_section = ""
    if chunks_html_parts:
        transcript_section = (
            '<button id="transcript-toggle" class="transcript-toggle">+ show full transcript</button>'
            f'<div id="transcript">{"".join(chunks_html_parts)}</div>'
        )

    return _HTML_TEMPLATE.format(
        title=_escape(title),
        description_html=description_html,
        quote_card_html=quote_card_html,
        meta_html=meta_html,
        audio_section=audio_section,
        participants_section=participants_section,
        moments_section=moments_section,
        transcript_section=transcript_section,
        space_url=_escape(meta.space_url),
    )


def write_archive_entry(
    archive_dir: Path,
    meta: SpaceMetadata,
    transcript: Transcript,
    audio_path: Path | None,
) -> Path:
    """Write metadata.json, transcript.json, transcript.md, index.html into the entry folder."""
    entry_dir = archive_dir / meta.space_id
    entry_dir.mkdir(parents=True, exist_ok=True)

    (entry_dir / "metadata.json").write_text(meta.model_dump_json(indent=2), encoding="utf-8")
    (entry_dir / "transcript.json").write_text(transcript.model_dump_json(indent=2), encoding="utf-8")
    (entry_dir / "transcript.md").write_text(render_markdown(meta, transcript), encoding="utf-8")
    (entry_dir / "index.html").write_text(render_html(meta, transcript), encoding="utf-8")

    if audio_path and audio_path.exists() and audio_path.parent != entry_dir:
        target = entry_dir / "audio.m4a"
        audio_path.rename(target)

    return entry_dir