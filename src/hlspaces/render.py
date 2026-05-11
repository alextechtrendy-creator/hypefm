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
<title>{title} — hype.fm</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
  :root {{
    --bg: #fafaf7;
    --bg-card: #ffffff;
    --fg: #222;
    --fg-muted: #666;
    --fg-faint: #999;
    --accent: #c0682c;
    --border: #e5e5e0;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: Verdana, Geneva, sans-serif;
    background: var(--bg); color: var(--fg);
    margin: 0; line-height: 1.5; -webkit-font-smoothing: antialiased;
  }}
  .container {{ max-width: 720px; margin: 0 auto; padding: 1.75rem 1.25rem 4rem; }}
  .back {{ font-size: 11px; color: var(--fg-faint); text-decoration: none; }}
  .back:hover {{ color: var(--accent); }}
  h1 {{
    font-size: 18px; font-weight: 500; line-height: 1.3;
    margin: 0.75rem 0 0.5rem; letter-spacing: -0.01em;
  }}
  .description {{
    font-size: 13px; color: #555; margin: 0 0 0.75rem; line-height: 1.5;
  }}
  .meta {{
    font-size: 11px; color: var(--fg-muted); margin: 0 0 1rem;
  }}
  .meta .tag {{ color: var(--accent); }}
  audio {{
    width: 100%; height: 38px; margin-bottom: 1.25rem;
  }}
  .audio-unavailable {{
    font-size: 12px; color: var(--fg-muted); font-style: italic;
    padding: 0.6rem 0.8rem; background: var(--bg-card);
    border: 1px solid var(--border); border-radius: 4px;
    margin-bottom: 1.25rem;
  }}
  .section-label {{
    font-size: 11px; color: var(--fg-faint); margin: 0 0 0.5rem;
    text-transform: uppercase; letter-spacing: 0.05em;
  }}
  .moments {{ display: flex; flex-direction: column; gap: 6px; margin-bottom: 1.5rem; }}
  .moment {{
    display: flex; gap: 12px; padding: 8px 10px;
    background: var(--bg-card); border: 1px solid var(--border);
    border-radius: 4px; cursor: pointer; transition: border-color 0.1s;
  }}
  .moment:hover {{ border-color: #ccc; }}
  .moment-ts {{
    font-size: 11px; color: var(--accent); font-weight: 500;
    min-width: 48px; font-variant-numeric: tabular-nums;
  }}
  .moment-label {{ font-size: 12px; margin: 0; line-height: 1.4; color: #333; }}
  .transcript-toggle {{
    border-top: 1px solid var(--border); padding-top: 1rem; margin-top: 1.5rem;
    font-size: 12px; color: var(--accent); cursor: pointer;
    background: none; border-left: none; border-right: none; border-bottom: none;
    padding-left: 0; padding-right: 0; font-family: inherit;
  }}
  .transcript-toggle:hover {{ text-decoration: underline; }}
  #transcript {{ display: none; margin-top: 1rem; }}
  #transcript.visible {{ display: block; }}
  .chunk {{
    padding: 0.6rem 0.75rem; margin-bottom: 0.4rem; background: var(--bg-card);
    border: 1px solid var(--border); border-radius: 4px; cursor: pointer;
    transition: border-color 0.1s;
  }}
  .chunk:hover {{ border-color: #ccc; }}
  .chunk-header {{
    display: flex; gap: 0.6rem; font-size: 11px; margin-bottom: 0.25rem;
    color: var(--fg-muted);
  }}
  .chunk-ts {{
    color: var(--accent); font-variant-numeric: tabular-nums; font-weight: 500;
  }}
  .chunk-speaker {{ font-weight: 500; }}
  .chunk-text {{ color: #333; font-size: 12px; line-height: 1.5; }}
  .footer {{
    margin-top: 2.5rem; padding-top: 1rem; border-top: 1px solid var(--border);
    color: var(--fg-faint); font-size: 11px; text-align: center;
  }}
  .footer a {{ color: var(--fg-muted); text-decoration: none; }}
</style>
</head>
<body>
<div class="container">

<a href="../../index.html" class="back">← back to hype.fm</a>

<h1>{title}</h1>
{description_html}
<p class="meta">{meta_html}</p>

{audio_section}

{moments_section}

{transcript_section}

<div class="footer">
  <a href="https://hypefm.xyz">hype.fm</a> &nbsp;·&nbsp;
  <a href="{space_url}" target="_blank" rel="noopener">view on x</a>
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
      toggle.textContent = visible ? '− hide full transcript' : '+ show full transcript';
    }});
  }}
</script>
</body>
</html>
"""


def render_html(meta: SpaceMetadata, transcript: Transcript, audio_filename: str = "audio.m4a") -> str:
    # Use R2 URL if available, fall back to local file
    audio_url = f"https://pub-09a0dd3dd2e44d25b3f0948f1c3d2b33.r2.dev/{meta.space_id}/audio.m4a"
    title = meta.summary_title or meta.title or "Untitled Space"

    description_html = ""
    if meta.summary_description:
        description_html = f'<p class="description">{_escape(meta.summary_description)}</p>'

    meta_parts = []
    if meta.host_username:
        meta_parts.append(f"@{_escape(meta.host_username)}")
    if meta.started_at:
        meta_parts.append(meta.started_at.strftime("%b %d, %Y").lower())
    if transcript.duration_seconds:
        meta_parts.append(_format_timestamp(transcript.duration_seconds))
    meta_html = " &nbsp;·&nbsp; ".join(meta_parts)
    if meta.topic_tags:
        tag_html = " · ".join(f'<span class="tag">{_escape(t)}</span>' for t in meta.topic_tags)
        meta_html += f" &nbsp;·&nbsp; {tag_html}"

    if meta.audio_captured:
        audio_section = f'<audio controls preload="metadata" src="{audio_url}"></audio>'
    else:
        reason = meta.capture_failure_reason or "Audio not available."
        audio_section = f'<div class="audio-unavailable">{_escape(reason)}</div>'

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
        meta_html=meta_html,
        audio_section=audio_section,
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