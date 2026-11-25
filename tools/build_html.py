#!/usr/bin/env python3
"""Build a stand-alone HTML slide deck from a LiaScript presentation (Pxx_*.md).

  python3 tools/build_html.py                 every AI_in_TVET_II_WiSe_2026_2027/*/P*.md
  python3 tools/build_html.py path/P03_X.md   only these files

The HTML file is written next to the .md file. Visual style: HTML decks of AI in TVET I (OVGU colours,
top/bottom bar, step-by-step builds, speaker notes, overview, document mode). LiaScript features are
translated: quizzes and gap texts can be checked, surveys can be clicked (local only), Mermaid diagrams are
rendered with mermaid.js, embedded websites and videos load only after a click. JavaScript playgrounds
(<script>…</script>) cannot run outside LiaScript – they become a card that opens the same slide in the
LiaScript version.
"""
import html
import re
import sys
from pathlib import Path

import markdown

REPO = Path(__file__).resolve().parent.parent
GH_RAW = "https://raw.githubusercontent.com/OVGU-VET-TechEd/AI_in_TVET_II_WiSe_2026_2027/main/"
LIA = "https://liascript.github.io/course/?"
COURSE = "AI in TVET II"

MID = [0]  # running id for radio groups of matrix quizzes
FENCE = re.compile(r"^\s*(```+|~~~+)")
NARR = re.compile(r"^\s*--\{\{(\d+)\}\}--\s*$")
FRAG = re.compile(r"^\s*\{\{(\d+)\}\}\s*$")
STARS = re.compile(r"^\s*\*{40}\s*$")


# ---------------------------------------------------------------- placeholders
class Store:
    def __init__(self):
        self.items = []

    def put(self, h):
        self.items.append(h)
        return f"⁣PH{len(self.items) - 1}⁣"

    def restore(self, text):
        for _ in range(4):
            new = re.sub(r"<p>\s*⁣PH(\d+)⁣\s*</p>", lambda m: self.items[int(m.group(1))], text)
            new = re.sub(r"⁣PH(\d+)⁣", lambda m: self.items[int(m.group(1))], new)
            if new == text:
                break
            text = new
        return text


def esc(s):
    return html.escape(s, quote=True)


def inline_md(s, store):
    """Render one line of Markdown without the surrounding <p>."""
    s = convert_inline(s, store)
    out = markdown.markdown(s)
    out = re.sub(r"^<p>(.*)</p>$", r"\1", out.strip(), flags=re.S)
    return store.restore(out)


# ---------------------------------------------------------------- inline LiaScript
def convert_inline(s, store):
    # protect inline code
    codes = []

    def keep(m):
        codes.append(m.group(0))
        return f"⁤C{len(codes) - 1}⁤"

    s = s.replace(">`@input`</script>", ">@input</script>")  # quoted input scripts (text/select)
    s = re.sub(r"`[^`]+`", keep, s)
    # inline input scripts → value chip
    def inp(m):
        attrs = m.group(1)
        val = re.search(r'value="([^"]*)"', attrs)
        kind = re.search(r'input="([^"]*)"', attrs)
        v = val.group(1) if val else ""
        if kind and kind.group(1) == "range":
            mn = re.search(r'min="([^"]*)"', attrs); mx = re.search(r'max="([^"]*)"', attrs)
            st = re.search(r'step="([^"]*)"', attrs)
            return store.put(f'<input class="rng" type="range" min="{esc(mn.group(1) if mn else "0")}" max="{esc(mx.group(1) if mx else "10")}" step="{esc(st.group(1) if st else "1")}" value="{esc(v)}" aria-label="slider"><output class="rngv">{esc(v)}</output>')
        if kind and kind.group(1) == "select":
            opts = re.search(r'options="([^"]*)"', attrs)
            o = "".join(f'<option{" selected" if x == v else ""}>{esc(x)}</option>' for x in (opts.group(1).split("|" if "|" in opts.group(1) else ",") if opts else [v]))
            return store.put(f'<select class="gap">{o}</select>')
        return store.put(f'<input class="txt" type="text" value="{esc(v)}" aria-label="input">')
    s = re.sub(r"<script([^>]*input=[^>]*)>`?@input`?</script>", inp, s)
    # images, videos, embeds
    s = re.sub(r"\?\?\[([^\]]*)\]\(([^)\s]+)[^)]*\)", lambda m: store.put(embed(m.group(1), m.group(2))), s)
    s = re.sub(r"!\?\[([^\]]*)\]\(([^)\s]+)[^)]*\)", lambda m: store.put(video(m.group(1), m.group(2))), s)
    # gaps: drag & drop and selection
    def sel(m):
        opts = [o.strip() for o in m.group(1).split("|")]
        ans = next((o[1:-1] for o in opts if o.startswith("(") and o.endswith(")")), "")
        clean = [o[1:-1] if o.startswith("(") and o.endswith(")") else o for o in opts]
        o = '<option value="">…</option>' + "".join(f"<option>{esc(x)}</option>" for x in clean)
        return store.put(f'<select class="gap" data-answer="{esc(ans)}">{o}</select>')
    s = re.sub(r"\[->\[([^\]]+)\]\]", sel, s)
    s = re.sub(r"\[\[([^\]\[]*\|[^\]\[]*)\]\]", sel, s)
    # text answers (not ___ surveys, not hints, not X)
    def txt(m):
        a = m.group(1).strip()
        if set(a) <= set("_ ") or a in ("?", "X", "x", ""):
            return m.group(0)
        return store.put(f'<input class="gap txt" type="text" data-answer="{esc(a)}" size="{max(6, len(a) + 2)}" aria-label="answer">')
    s = re.sub(r"\[\[([^\]\[]+)\]\]", txt, s)
    s = re.sub(r"⁤C(\d+)⁤", lambda m: codes[int(m.group(1))], s)
    return s


def embed(title, url):
    return (f'<div class="embed card"><div class="embed-head"><b>🧪 {esc(title)}</b>'
            f'<a class="btn small" href="{esc(url)}" target="_blank" rel="noopener">Open in new tab ↗</a></div>'
            f'<button class="btn small load" data-src="{esc(url)}">Load here</button></div>')


def video(title, url):
    yt = re.search(r"(?:youtu\.be/|v=)([\w-]{6,})", url)
    src = f"https://www.youtube-nocookie.com/embed/{yt.group(1)}" if yt else url
    return (f'<div class="embed card video"><div class="embed-head"><b>🎬 {esc(title)}</b>'
            f'<a class="btn small" href="{esc(url)}" target="_blank" rel="noopener">Watch on the website ↗</a></div>'
            f'<button class="btn small load" data-src="{esc(src)}">Load video here</button></div>')


# ---------------------------------------------------------------- block LiaScript
def convert_quiz(lines, store, playground_link):
    """lines: option lines (+ hints + solution). Returns HTML."""
    opts, hints, sol, i = [], [], [], 0
    while i < len(lines):
        ln = lines[i]
        if re.match(r"^\s*\[\[\?\]\]", ln):
            hints.append(ln.split("]]", 1)[1].strip())
        elif ln.strip() == "***":
            j = i + 1
            while j < len(lines) and lines[j].strip() != "***":
                sol.append(lines[j]); j += 1
            i = j
        elif ln.strip():
            opts.append(ln)
        i += 1
    m0 = re.match(r"^- \[([(\[])(.*?)[)\]]\]", opts[0])
    multi = m0.group(1) == "["
    labels = [re.match(r"^- \[[(\[](.*?)[)\]]\]", o).group(1) for o in opts]
    texts = [inline_md(re.sub(r"^- \[[(\[].*?[)\]]\]\s*", "", o), store) for o in opts]
    is_quiz = all(l.strip() in ("X", "x", "") for l in labels)
    if not is_quiz:  # survey
        cls = "poll multi" if multi else "poll"
        b = "".join(f'<button class="opt" aria-pressed="false">{t}</button>' for t in texts)
        return f'<div class="{cls}">{b}<p class="small muted">Survey – your choice stays in this browser. Live results: classroom in the LiaScript version.</p></div>'
    correct = [i for i, l in enumerate(labels) if l.strip() in ("X", "x")]
    b = "".join(f'<button class="opt" data-ok="{1 if i in correct else 0}" aria-pressed="false">{t}</button>' for i, t in enumerate(texts))
    h = "".join(f'<p class="hint" hidden>💡 {inline_md(x, store)}</p>' for x in hints)
    s = ""
    if sol:
        s = f'<div class="sol" hidden>{store.restore(markdown.markdown(convert_inline(chr(10).join(sol), store)))}</div>'
    kind = "multi" if multi else "single"
    btn = '<button class="btn small check">Check</button>' if multi else ""
    return f'<div class="quiz" data-kind="{kind}"><div class="opts">{b}</div><div class="row-actions">{btn}<span class="fb" aria-live="polite"></span></div>{h}{s}</div>'


def convert_blocks(text, store, playground_link):
    """Convert block-level LiaScript constructs in a Markdown chunk; returns Markdown with placeholders."""
    lines = text.split("\n")
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        fm = FENCE.match(ln)
        if fm:
            fence = fm.group(1)
            info = ln.strip()[len(fence):].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith(fence):
                body.append(lines[i]); i += 1
            i += 1
            code = "\n".join(body)
            if info.startswith("mermaid"):
                out.append(store.put(f'<div class="mermaid-box"><pre class="mermaid">{esc(code)}</pre></div>'))
            else:
                lang = info.split()[0] if info else ""
                runnable = i < len(lines) and re.match(r"^\s*<script>\s*@input", lines[i] or "")
                note = ""
                if runnable:
                    while i < len(lines) and "</script>" not in lines[i]:
                        i += 1
                    i += 1
                    note = f'<p class="small"><a href="{playground_link}" target="_blank" rel="noopener">▶ Run this code in the LiaScript version ↗</a></p>'
                out.append(store.put(f'<pre class="code"><code class="lang-{esc(lang)}">{esc(code)}</code></pre>{note}'))
            continue
        # multi-line script (playground output) → card
        if re.match(r"^\s*<script(?![^>]*input=)", ln):
            while i < len(lines) and "</script>" not in lines[i]:
                i += 1
            i += 1
            out.append(store.put(f'<div class="card pg"><b>▶ Interactive playground</b><p>This part computes live in LiaScript (sliders, inputs, charts).</p><a class="btn primary small" href="{playground_link}" target="_blank" rel="noopener">Open this slide in LiaScript ↗</a></div>'))
            continue
        # HTML comments
        if re.match(r"^\s*<!--.*-->\s*$", ln):
            i += 1
            continue
        # alerts
        am = re.match(r"^>\s*\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]\s*(.*)$", ln)
        if am:
            body = []
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                body.append(lines[i][1:].strip()); i += 1
            kind = {"NOTE": "main", "TIP": "", "IMPORTANT": "crit", "WARNING": "crit", "CAUTION": "crit"}[am.group(1)]
            inner = store.restore(markdown.markdown(convert_inline("\n".join(body), store)))
            out.append(store.put(f'<div class="callout {kind}"><span class="lab">{esc(am.group(2) or am.group(1).title())}</span>{inner}</div>'))
            continue
        # task list
        if re.match(r"^- \[ \] ", ln):
            items = []
            while i < len(lines) and re.match(r"^- \[ \] ", lines[i]):
                items.append(inline_md(lines[i][6:], store)); i += 1
            out.append(store.put('<ul class="tasks">' + "".join(f'<li><label><input type="checkbox"> <span>{t}</span></label></li>' for t in items) + "</ul>"))
            continue
        # quiz / survey options
        if re.match(r"^- \[[(\[][^\]]*[)\]]\]", ln):
            block = []
            while i < len(lines) and (re.match(r"^- \[[(\[][^\]]*[)\]]\]", lines[i]) or re.match(r"^\s*\[\[\?\]\]", lines[i])):
                block.append(lines[i]); i += 1
            if i < len(lines) and lines[i].strip() == "***":
                block.append("***"); i += 1
                while i < len(lines) and lines[i].strip() != "***":
                    block.append(lines[i]); i += 1
                block.append("***"); i += 1
            out.append(store.put(convert_quiz(block, store, playground_link)))
            continue
        # matrix quiz/survey header  [(a) (b)]
        if re.match(r"^\[\s*\(.+\)\s*\]\s*$", ln):
            MID[0] += 1
            heads = re.findall(r"\(([^)]*)\)", ln)
            rows = []
            i += 1
            while i < len(lines) and lines[i].startswith("["):
                m = re.match(r"^\[(.*?)\]\s*(.*)$", lines[i])
                marks = re.findall(r"\((.)\)", m.group(1))
                rows.append(([x == "X" for x in marks], m.group(2))); i += 1
            body = "".join(
                "<tr><td>" + inline_md(t, store) + "</td>" + "".join(
                    f'<td><input type="radio" name="m{MID[0]}_{r}" data-ok="{1 if ok else 0}"></td>' for ok in marks) + "</tr>"
                for r, (marks, t) in enumerate(rows))
            out.append(store.put(f'<div class="quiz matrix"><table class="t"><tr><th></th>{"".join(f"<th>{esc(h)}</th>" for h in heads)}</tr>{body}</table><div class="row-actions"><button class="btn small check">Check</button><span class="fb"></span></div></div>'))
            continue
        # free text survey
        if re.match(r"^\s*\[\[_+( _+)*\]\]\s*$", ln):
            n = ln.count("_") // 3
            out.append(store.put(f'<textarea class="free" rows="{max(1, min(n, 4))}" placeholder="Your answer (stays in this browser)"></textarea>'))
            i += 1
            continue
        out.append(convert_inline(ln, store))
        i += 1
    return "\n".join(out)


def render_md(text, store, playground_link):
    md = convert_blocks(text, store, playground_link)
    h = markdown.markdown(md, extensions=["tables", "sane_lists"])
    h = re.sub(r"<table>(.*?)</table>", r'<div class="table-scroll"><table class="t">\1</table></div>', h, flags=re.S)
    h = store.restore(h)
    h = h.replace('<a href="http', '<a target="_blank" rel="noopener" href="http')
    return h


# ---------------------------------------------------------------- slide parsing
def split_slides(body):
    slides, cur, in_code = [], None, False
    for ln in body.split("\n"):
        if FENCE.match(ln):
            in_code = not in_code
        m = None if in_code else re.match(r"^(#{1,2})\s+(.*)$", ln)
        if m:
            cur = {"level": len(m.group(1)), "title": m.group(2).strip(), "lines": []}
            slides.append(cur)
        elif cur is not None:
            cur["lines"].append(ln)
    return slides


def segment(lines):
    """Split slide lines into (step, markdown) segments and collect narration."""
    segs, notes, i, buf = [], {}, 0, []
    in_code = False

    def flush():
        if any(x.strip() for x in buf):
            segs.append((0, "\n".join(buf)))
        buf.clear()

    while i < len(lines):
        ln = lines[i]
        if FENCE.match(ln):
            in_code = not in_code
            buf.append(ln); i += 1
            continue
        if in_code:
            buf.append(ln); i += 1
            continue
        nm = NARR.match(ln)
        if nm:
            n = int(nm.group(1)); i += 1
            txt = []
            while i < len(lines) and lines[i].strip():
                txt.append(lines[i].strip()); i += 1
            notes.setdefault(n, []).append(" ".join(txt))
            continue
        fm = FRAG.match(ln)
        if fm:
            flush()
            n = int(fm.group(1)); i += 1
            while i < len(lines) and not lines[i].strip():
                i += 1
            chunk = []
            if i < len(lines) and STARS.match(lines[i]):
                i += 1
                while i < len(lines) and not STARS.match(lines[i]):
                    chunk.append(lines[i]); i += 1
                i += 1
            elif i < len(lines) and lines[i].strip() == "<section>":
                i += 1
                while i < len(lines) and lines[i].strip() != "</section>":
                    chunk.append(lines[i]); i += 1
                i += 1
            else:
                code = False
                while i < len(lines):
                    if FENCE.match(lines[i]):
                        code = not code
                    if not code and not lines[i].strip() and chunk and not chunk[-1].lstrip().startswith("<!--"):
                        break
                    chunk.append(lines[i]); i += 1
            segs.append((n, "\n".join(chunk)))
            continue
        if ln.strip() in ("<section>", "</section>"):
            i += 1
            continue
        buf.append(ln); i += 1
    flush()
    return segs, notes


def parse_header(src):
    m = re.match(r"\s*<!--(.*?)-->", src, re.S)
    head = {}
    if m:
        for ln in m.group(1).split("\n"):
            km = re.match(r"^(\w+):\s*(.*)$", ln.strip())
            if km:
                head[km.group(1)] = km.group(2).strip()
        src = src[m.end():]
    return head, src


def build(md_path):
    md_path = md_path.resolve()
    rel = md_path.relative_to(REPO).as_posix()
    lia_url = LIA + GH_RAW + rel
    up = "../" * (len(Path(rel).parts) - 1)
    src = md_path.read_text(encoding="utf-8")
    head, body = parse_header(src)
    slides = split_slides(body)
    sections, section = [], ""
    for idx, sl in enumerate(slides):
        store = Store()
        link = f"{lia_url}#{idx + 1}"
        segs, notes = segment(sl["lines"])
        title_html = inline_md(re.sub(r"^(\d+)\.", r"\1\\.", sl["title"]), store)
        nm = re.match(r"^(\d+)\.\s+(.*)$", sl["title"])
        if nm:
            label = re.sub(r"[^\w\s,:;&()–-]", "", nm.group(2)).strip()
            section = f"Part {nm.group(1)} · {label}"
        parts = []
        for n, chunk in segs:
            h = render_md(chunk, store, link)
            parts.append(f'<div class="frag" data-f="{n}">{h}</div>' if n else h)
        note = " ".join(" ".join(notes[k]) for k in sorted(notes))
        plain_title = re.sub(r"<[^>]+>", "", title_html)
        if sl["level"] == 1:
            inner = (f'<div class="hero-grid"><div><p class="kicker">{COURSE} · OVGU Magdeburg</p><h1>{title_html}</h1>'
                     f'{"".join(parts)}'
                     f'<div class="row-actions"><a class="btn primary" href="{lia_url}" target="_blank" rel="noopener">LiaScript version · classroom polls ↗</a></div>'
                     f'<p class="keys hide-scroll"><kbd>←</kbd> <kbd>→</kbd> or <kbd>Space</kbd> navigate · <kbd>O</kbd> overview · <kbd>N</kbd> notes · <kbd>S</kbd> document mode · <kbd>F</kbd> full screen</p></div>'
                     f'<div class="hero-badge" aria-hidden="true">{esc(md_path.stem[:3])}</div></div>')
            cls = "slide hero"
        else:
            kick = f'<p class="kicker">{esc(section)}</p>' if section else ""
            refs = " refs" if sl["title"].lower().startswith("references") else ""
            inner = f'{kick}<h2>{title_html}</h2><div class="body{refs}">{"".join(parts)}</div>'
            cls = "slide"
        sections.append(f'<section class="{cls}" data-title="{esc(plain_title.strip())}">\n<div class="inner">{inner}</div>\n'
                        f'<aside class="notes">{esc(note)}</aside>\n</section>')
    title = head.get("title", md_path.stem)
    deck_title = re.sub(r"\s*\(Session slides\)\s*$", "", title)
    page = TEMPLATE.format(
        title=esc(deck_title), desc=esc(head.get("comment", "")), up=up, course=COURSE,
        slides="\n\n".join(sections), lia=esc(lia_url), deck=esc(deck_title))
    out = md_path.with_suffix(".html")
    out.write_text(page, encoding="utf-8")
    print(f"wrote {out.relative_to(REPO)} ({len(slides)} slides)")


TEMPLATE = """<!doctype html>
<html lang="en" class="present-root">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="icon" href="{up}assets/ovgu_logo.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,500;0,600;1,400&family=Barlow+Semi+Condensed:wght@500;600&display=swap" rel="stylesheet">
<style>
:root {{ color-scheme: light; --main:#7a003f; --main-dark:#5c002f; --second:#bc7f9f; --third:#f5ebf0; --ink:#111; --ink-2:#3e3f40; --ink-3:#5f6163;
  --line:#cfd3d6; --soft:#e7e9ea; --bg:#fff; --bg-2:#f8f8f8; --s1:#2a78d6; --good:#0ca30c; --good-bg:#e2f4e2; --crit:#d03b3b; --crit-bg:#fbe3e3; --warn:#fab219; --hb:3.1rem; --fb:3rem; }}
* {{ box-sizing: border-box; }}
html {{ font-size: 16px; }}
html.present-root {{ font-size: clamp(13px, min(1.1vw, 2.05vh), 30px); }}
body {{ margin:0; background:var(--bg); color:var(--ink); font-family:"Barlow","Helvetica Neue",Arial,sans-serif; line-height:1.45; overflow-wrap:anywhere; }}
a {{ color:var(--main); }} a:hover {{ color:var(--main-dark); }}
h1,h2,h3 {{ font-family:"Barlow Semi Condensed","Barlow",sans-serif; font-weight:600; line-height:1.12; }}
button,input,textarea,select {{ font:inherit; }}
:focus-visible {{ outline:3px solid var(--s1); outline-offset:2px; }}
small,.small {{ font-size:.82em; }} .muted {{ color:var(--ink-3); }}
.topbar {{ position:fixed; top:0; left:0; right:0; height:var(--hb); z-index:30; display:flex; align-items:center; gap:.9rem; padding:0 1.1rem; background:#fff; border-bottom:1px solid var(--line); }}
.topbar img {{ height:2.1rem; display:block; }}
.topbar .deck-title {{ font-family:"Barlow Semi Condensed",sans-serif; font-weight:600; color:var(--main); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; }}
.topbar .lia-link {{ margin-left:auto; font-size:.85rem; white-space:nowrap; }}
.botbar {{ position:fixed; left:0; right:0; bottom:0; height:var(--fb); z-index:30; display:flex; align-items:center; gap:.5rem; padding:0 1rem; background:#fff; border-top:1px solid var(--line); }}
.progress {{ position:absolute; top:-1px; left:0; height:3px; background:var(--main); transition:width .3s; }}
.counter {{ font-variant-numeric:tabular-nums; font-size:.9rem; color:var(--ink-2); min-width:4.2rem; text-align:center; }}
.steps {{ display:flex; gap:.25rem; }} .steps i {{ width:.45rem; height:.45rem; border-radius:50%; background:var(--soft); display:block; }} .steps i.on {{ background:var(--main); }}
.spacer {{ flex:1; }} .stitle {{ font-size:.85rem; color:var(--ink-3); white-space:nowrap; overflow:hidden; text-overflow:ellipsis; max-width:40vw; }}
.cbtn {{ border:1px solid var(--line); background:#fff; color:var(--ink); border-radius:.35rem; padding:.25rem .6rem; font-size:.85rem; cursor:pointer; white-space:nowrap; }}
.cbtn:hover {{ border-color:var(--main); color:var(--main); }} .cbtn[aria-pressed="true"] {{ background:var(--main); color:#fff; border-color:var(--main); }}
#deck {{ position:fixed; top:var(--hb); bottom:var(--fb); left:0; right:0; }}
.slide {{ position:absolute; inset:0; display:none; }} .slide.active {{ display:block; }}
body.prerender .slide {{ display:block; visibility:hidden; }}
.slide > .inner {{ height:100%; overflow-y:auto; max-width:80rem; margin:0 auto; padding:1.3rem 2.6rem 1.8rem; }}
.slide .notes {{ display:none; }}
.notes-panel {{ position:fixed; left:0; right:0; bottom:var(--fb); z-index:25; max-height:32vh; overflow:auto; background:#fffdf2; border-top:3px solid var(--warn); padding:.7rem 1.4rem; font-size:.95rem; display:none; }}
.notes-panel.open {{ display:block; }} .notes-panel h4 {{ margin:0 0 .3rem; font-size:.8rem; letter-spacing:.08em; text-transform:uppercase; color:var(--ink-3); }}
.overview {{ position:fixed; inset:0; z-index:60; background:rgba(255,255,255,.98); overflow:auto; padding:1.4rem 2rem 2rem; display:none; }}
.overview.open {{ display:block; }} .ov-head {{ display:flex; justify-content:space-between; align-items:center; margin-bottom:1rem; }} .overview h2 {{ margin:0; color:var(--main); }}
.ov-grid {{ display:grid; grid-template-columns:repeat(auto-fill,minmax(min(15rem,100%),1fr)); gap:.7rem; }}
.ov-item {{ text-align:left; border:1px solid var(--line); border-top:4px solid var(--second); background:#fff; border-radius:.3rem; padding:.55rem .7rem; cursor:pointer; font-size:.9rem; }}
.ov-item:hover,.ov-item.cur {{ border-top-color:var(--main); box-shadow:0 2px 8px rgba(122,0,63,.15); }} .ov-item b {{ display:block; color:var(--ink-3); font-size:.75rem; font-weight:500; }}
.frag {{ opacity:0; visibility:hidden; transform:translateY(.35rem); transition:opacity .35s, transform .35s, visibility .35s; }}
.frag.on {{ opacity:1; visibility:visible; transform:none; }}
@media (prefers-reduced-motion: reduce) {{ .frag,.progress {{ transition:none; }} }}
body.scroll .topbar {{ position:sticky; }} body.scroll #deck {{ position:static; }}
body.scroll .slide {{ position:static; display:block; border-bottom:8px solid var(--third); }}
body.scroll .slide > .inner {{ height:auto; overflow:visible; padding:1.4rem 16px 2.2rem; }}
body.scroll .frag {{ opacity:1; visibility:visible; transform:none; }}
body.scroll .botbar, body.scroll .notes-panel, body.scroll .hide-scroll {{ display:none; }}
body.scroll .slide .notes {{ display:block; max-width:80rem; margin:0 auto 1.2rem; font-size:.9rem; color:var(--ink-3); border-left:3px solid var(--warn); padding:.3rem .8rem; background:#fffdf2; }}
body.scroll .slide .notes:empty {{ display:none; }}
body.scroll .slide .notes::before {{ content:"Speaker notes · "; font-weight:600; }}
.kicker {{ font-family:"Barlow Semi Condensed",sans-serif; font-weight:600; text-transform:uppercase; letter-spacing:.08em; font-size:.82rem; color:var(--main); margin:0 0 .25rem; }}
.slide h2 {{ margin:0 0 .8rem; font-size:2.05rem; color:var(--main); }}
.slide p {{ margin:0 0 .7rem; }} .slide ul,.slide ol {{ margin:0 0 .7rem; padding-left:1.3rem; }} .slide li {{ margin:.2rem 0; }}
.body > * + *, .frag > * + * {{ margin-top:.2rem; }}
.card {{ border:1px solid var(--line); background:#fff; border-radius:.4rem; padding:.85rem 1rem; margin:.4rem 0 .8rem; }}
.card.pg {{ border-left:5px solid var(--main); background:var(--third); }} .card.pg p {{ margin:.3rem 0 .5rem; }}
.callout {{ border-left:5px solid var(--s1); background:#f1f6fd; padding:.7rem .95rem; border-radius:0 .4rem .4rem 0; margin:.5rem 0 .8rem; }}
.callout.main {{ border-left-color:var(--main); background:var(--third); }} .callout.crit {{ border-left-color:var(--crit); background:#fdf1f1; }}
.callout .lab {{ font-weight:600; display:block; margin-bottom:.2rem; }} .callout > :last-child {{ margin-bottom:0; }}
.table-scroll {{ overflow-x:auto; margin:0 0 .8rem; }}
table.t {{ width:100%; border-collapse:collapse; font-size:.95rem; }}
table.t th {{ text-align:left; background:var(--soft); padding:.4rem .6rem; font-weight:600; }}
table.t td {{ padding:.45rem .6rem; border-bottom:1px solid var(--soft); vertical-align:top; }}
code {{ background:var(--bg-2); border:1px solid var(--soft); border-radius:.25rem; padding:0 .25rem; font-size:.9em; }}
pre.code {{ background:#1f1f24; color:#f4f4f5; padding:.8rem 1rem; border-radius:.4rem; overflow:auto; font-size:.85rem; line-height:1.4; margin:.3rem 0 .8rem; white-space:pre-wrap; }}
pre.code code {{ background:none; border:0; color:inherit; padding:0; }}
.mermaid-box {{ margin:.4rem 0 .9rem; text-align:center; }} .mermaid-box svg {{ max-width:100%; height:auto; max-height:52vh; }}
body.scroll .mermaid-box svg {{ max-height:none; }}
.btn {{ border:1px solid var(--main); background:#fff; color:var(--main); border-radius:.35rem; padding:.35rem .85rem; cursor:pointer; font-weight:600; text-decoration:none; display:inline-flex; align-items:center; gap:.35rem; }}
.btn:hover {{ background:var(--third); }} .btn.primary {{ background:var(--main); color:#fff; }} .btn.primary:hover {{ background:var(--main-dark); }} .btn.small {{ padding:.2rem .6rem; font-size:.85rem; }}
.row-actions {{ display:flex; flex-wrap:wrap; gap:.5rem; align-items:center; margin:.4rem 0 .6rem; }}
.quiz, .poll {{ margin:.3rem 0 .9rem; }}
.opts, .poll {{ display:flex; flex-direction:column; gap:.35rem; align-items:flex-start; }}
.opt {{ text-align:left; border:1px solid var(--line); background:#fff; border-radius:.4rem; padding:.35rem .8rem; cursor:pointer; min-width:min(28rem,100%); }}
.opt:hover {{ border-color:var(--main); }} .opt[aria-pressed="true"] {{ border-color:var(--main); background:var(--third); }}
.opt.right {{ border-color:var(--good); background:var(--good-bg); }} .opt.wrong {{ border-color:var(--crit); background:var(--crit-bg); }}
.fb {{ font-weight:600; }} .fb.ok {{ color:var(--good); }} .fb.no {{ color:var(--crit); }}
.hint {{ font-size:.9rem; background:#fff8e1; padding:.3rem .6rem; border-radius:.3rem; }}
.sol {{ border-left:4px solid var(--good); background:var(--good-bg); padding:.4rem .8rem; border-radius:0 .3rem .3rem 0; font-size:.92rem; }}
.gap {{ border:1px solid var(--line); border-radius:.3rem; padding:.1rem .35rem; background:#fff; }}
.gap.right {{ border-color:var(--good); background:var(--good-bg); }} .gap.wrong {{ border-color:var(--crit); background:var(--crit-bg); }}
textarea.free {{ width:min(40rem,100%); border:1px solid var(--line); border-radius:.35rem; padding:.4rem .6rem; display:block; margin:.2rem 0 .8rem; }}
ul.tasks {{ list-style:none; padding-left:0; }} ul.tasks input {{ accent-color:var(--main); }}
input.rng {{ accent-color:var(--main); vertical-align:middle; }} .rngv {{ display:inline-block; min-width:1.5rem; text-align:center; font-weight:600; color:var(--main); }}
input.txt {{ border:1px solid var(--line); border-radius:.3rem; padding:.1rem .4rem; min-width:14rem; }}
.embed-head {{ display:flex; flex-wrap:wrap; gap:.6rem; align-items:center; justify-content:space-between; margin-bottom:.4rem; }}
.embed iframe {{ width:100%; height:58vh; border:0; border-radius:.3rem; }}
.refs {{ font-size:.82rem; }} .refs ul {{ columns:2 22rem; column-gap:1.6rem; }} .refs li {{ break-inside:avoid; }}
.slide.hero {{ background:var(--main); color:#fff; }} .slide.hero a {{ color:#fff; }}
.hero-grid {{ display:grid; grid-template-columns:1.6fr 1fr; gap:2rem; align-items:center; min-height:100%; }}
.hero h1 {{ font-size:3.1rem; margin:.2rem 0 .8rem; }} .hero .kicker {{ color:#fff; opacity:.85; }}
.hero .btn {{ border-color:#fff; color:#fff; background:transparent; }} .hero .btn.primary {{ background:#fff; color:var(--main); }}
.hero .keys {{ margin-top:1.4rem; font-size:.85rem; opacity:.85; }}
.hero-badge {{ justify-self:center; width:min(18rem,30vw); aspect-ratio:1; border-radius:50%; border:3px dashed rgba(255,255,255,.55); display:grid; place-items:center; font-family:"Barlow Semi Condensed",sans-serif; font-size:clamp(3rem,7vw,7rem); font-weight:600; background:rgba(255,255,255,.08); }}
kbd {{ font-family:inherit; font-size:.85em; border:1px solid var(--line); border-bottom-width:2px; border-radius:.25rem; padding:0 .35rem; background:var(--bg-2); }}
.hero kbd {{ background:rgba(255,255,255,.15); border-color:rgba(255,255,255,.4); color:#fff; }}
@media (max-width:820px) {{ .hero-grid {{ grid-template-columns:1fr; }} .hero-badge {{ display:none; }} .hero h1 {{ font-size:2.2rem; }} .slide h2 {{ font-size:1.6rem; }} .slide > .inner {{ padding:1rem 1rem 1.6rem; }} .stitle {{ display:none; }} }}
@media print {{ html.present-root {{ font-size:12px; }} .topbar,.botbar,.notes-panel,.overview {{ display:none !important; }} #deck {{ position:static; }}
  .slide {{ position:static !important; display:block !important; page-break-after:always; }} .slide > .inner {{ height:auto; overflow:visible; }}
  .frag {{ opacity:1 !important; visibility:visible !important; transform:none !important; }} .slide.hero {{ -webkit-print-color-adjust:exact; print-color-adjust:exact; }} }}
</style>
</head>
<body class="prerender">
<header class="topbar">
  <a href="{up}index.html" title="Course website"><img src="{up}assets/ovgu_logo.svg" alt="Otto von Guericke University Magdeburg – back to the course website"></a>
  <span class="deck-title">{course} · {deck}</span>
  <a class="lia-link" href="{lia}" target="_blank" rel="noopener">LiaScript version ↗</a>
</header>
<main id="deck" aria-roledescription="slide deck">
{slides}
</main>
<div class="notes-panel" id="notesPanel" aria-live="polite"><h4>Speaker notes</h4><div id="notesText"></div></div>
<div class="overview" id="overview" role="dialog" aria-label="Slide overview"><div class="ov-head"><h2>Overview</h2><button class="cbtn" id="ovClose">Close (Esc)</button></div><div class="ov-grid" id="ovGrid"></div></div>
<nav class="botbar" aria-label="Slide navigation">
  <div class="progress" id="progress"></div>
  <button class="cbtn" id="prev" aria-label="Previous">←</button>
  <span class="counter" id="count"></span>
  <button class="cbtn" id="next" aria-label="Next">→</button>
  <span class="steps" id="steps"></span>
  <span class="stitle" id="stitle"></span>
  <span class="spacer"></span>
  <button class="cbtn" id="ovBtn" title="Overview (O)">Overview</button>
  <button class="cbtn" id="notesBtn" aria-pressed="false" title="Speaker notes (N)">Notes</button>
  <button class="cbtn" id="scrollBtn" aria-pressed="false" title="Document mode (S)">Document</button>
  <button class="cbtn" id="fsBtn" title="Full screen (F)">⛶</button>
</nav>
<script type="module">
import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
mermaid.initialize({{ startOnLoad:false, securityLevel:"loose", theme:"base", fontFamily:"Barlow, Arial, sans-serif",
  themeVariables:{{ primaryColor:"#f7eef2", primaryBorderColor:"#7a003f", lineColor:"#3e3f40", fontSize:"15px" }} }});
try {{ await mermaid.run({{ querySelector:".mermaid" }}); }} catch (e) {{ console.warn(e); }}
document.body.classList.remove("prerender");
window.dispatchEvent(new Event("deck-ready"));
</script>
<script>
(() => {{
  const $ = (s, r = document) => r.querySelector(s), $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const slides = $$(".slide");
  let cur = 0, step = 0;
  const maxStep = s => Math.max(0, ...$$(".frag", s).map(e => +e.dataset.f || 0));
  function render() {{
    slides.forEach((s, i) => s.classList.toggle("active", i === cur));
    const s = slides[cur];
    $$(".frag", s).forEach(e => e.classList.toggle("on", (+e.dataset.f || 0) <= step));
    $("#count").textContent = `${{cur + 1}} / ${{slides.length}}`;
    $("#stitle").textContent = s.dataset.title || "";
    $("#progress").style.width = `${{(cur / Math.max(1, slides.length - 1)) * 100}}%`;
    $("#steps").innerHTML = Array.from({{ length: maxStep(s) }}, (_, k) => `<i class="${{k < step ? "on" : ""}}"></i>`).join("");
    $("#notesText").textContent = ($(".notes", s) || {{}}).textContent || "";
    history.replaceState(null, "", `#${{cur + 1}}`);
  }}
  function go(i, atEnd) {{ cur = Math.max(0, Math.min(slides.length - 1, i)); step = atEnd ? maxStep(slides[cur]) : 0; $(".inner", slides[cur]).scrollTop = 0; render(); }}
  function next() {{ if (step < maxStep(slides[cur])) {{ step++; render(); }} else if (cur < slides.length - 1) go(cur + 1); }}
  function prev() {{ if (step > 0) {{ step--; render(); }} else if (cur > 0) go(cur - 1, true); }}
  $("#next").onclick = next; $("#prev").onclick = prev;
  const toggleNotes = () => {{ const p = $("#notesPanel"); p.classList.toggle("open"); $("#notesBtn").setAttribute("aria-pressed", p.classList.contains("open")); }};
  const toggleScroll = () => {{ document.body.classList.toggle("scroll"); $("#scrollBtn").setAttribute("aria-pressed", document.body.classList.contains("scroll")); if (!document.body.classList.contains("scroll")) go(cur); }};
  const fs = () => document.fullscreenElement ? document.exitFullscreen() : document.documentElement.requestFullscreen?.();
  const ov = $("#overview");
  $("#ovGrid").innerHTML = slides.map((s, i) => `<button class="ov-item" data-i="${{i}}"><b>${{i + 1}}</b>${{s.dataset.title}}</button>`).join("");
  $$(".ov-item").forEach(b => b.onclick = () => {{ ov.classList.remove("open"); go(+b.dataset.i); }});
  const toggleOv = () => {{ ov.classList.toggle("open"); $$(".ov-item").forEach(b => b.classList.toggle("cur", +b.dataset.i === cur)); }};
  $("#ovBtn").onclick = toggleOv; $("#ovClose").onclick = toggleOv;
  $("#notesBtn").onclick = toggleNotes; $("#scrollBtn").onclick = toggleScroll; $("#fsBtn").onclick = fs;
  document.addEventListener("keydown", e => {{
    if (e.target.closest("textarea, input, select") || e.metaKey || e.ctrlKey || e.altKey) return;
    if (e.key === "Escape") {{ ov.classList.remove("open"); return; }}
    if (document.body.classList.contains("scroll") && !"sS".includes(e.key)) return;
    if (["ArrowRight", "PageDown", " "].includes(e.key)) {{ e.preventDefault(); next(); }}
    else if (["ArrowLeft", "PageUp"].includes(e.key)) {{ e.preventDefault(); prev(); }}
    else if (e.key === "Home") go(0); else if (e.key === "End") go(slides.length - 1);
    else if ("nN".includes(e.key)) toggleNotes(); else if ("fF".includes(e.key)) fs();
    else if ("oO".includes(e.key)) toggleOv(); else if ("sS".includes(e.key)) toggleScroll();
  }});
  let tx = null;
  $("#deck").addEventListener("touchstart", e => {{ tx = e.touches[0].clientX; }}, {{ passive: true }});
  $("#deck").addEventListener("touchend", e => {{ if (tx === null) return; const dx = e.changedTouches[0].clientX - tx; if (Math.abs(dx) > 70 && !e.target.closest("textarea, input, iframe")) (dx < 0 ? next : prev)(); tx = null; }});
  if (window.matchMedia("(max-width: 600px)").matches) toggleScroll();

  /* quizzes */
  $$(".quiz[data-kind]").forEach(q => {{
    const opts = $$(".opt", q), fb = $(".fb", q), single = q.dataset.kind === "single";
    let tries = 0;
    const show = ok => {{
      fb.textContent = ok ? "✔ Correct" : "✘ Not yet – try again"; fb.className = "fb " + (ok ? "ok" : "no");
      tries += ok ? 0 : 1;
      if (tries >= 1) $$(".hint", q).forEach(h => h.hidden = false);
      if (ok || tries >= 2) {{ const s = $(".sol", q); if (s) s.hidden = false; }}
      if (ok || tries >= 2) opts.forEach(o => o.classList.toggle("right", o.dataset.ok === "1"));
    }};
    opts.forEach(o => o.onclick = () => {{
      if (single) {{ opts.forEach(x => {{ x.setAttribute("aria-pressed", x === o); x.classList.remove("wrong"); }}); if (o.dataset.ok !== "1") o.classList.add("wrong"); show(o.dataset.ok === "1"); }}
      else o.setAttribute("aria-pressed", o.getAttribute("aria-pressed") !== "true");
    }});
    const c = $(".check", q);
    if (c) c.onclick = () => show(opts.every(o => (o.getAttribute("aria-pressed") === "true") === (o.dataset.ok === "1")));
  }});
  $$(".quiz.matrix").forEach(q => $(".check", q).onclick = () => {{
    const rows = $$("tr", q).slice(1);
    const ok = rows.every(r => $$("input", r).every(i => i.checked === (i.dataset.ok === "1")));
    const fb = $(".fb", q); fb.textContent = ok ? "✔ Correct" : "✘ Not yet"; fb.className = "fb " + (ok ? "ok" : "no");
  }});
  $$(".poll").forEach(p => {{ const multi = p.classList.contains("multi"); $$(".opt", p).forEach(b => b.onclick = () => {{
    if (multi) b.setAttribute("aria-pressed", b.getAttribute("aria-pressed") !== "true"); else $$(".opt", p).forEach(x => x.setAttribute("aria-pressed", x === b)); }}); }});
  $$(".gap[data-answer]").forEach(g => g.addEventListener("change", () => {{
    if (!g.dataset.answer) return;
    const ok = g.value.trim().toLowerCase() === g.dataset.answer.trim().toLowerCase();
    g.classList.toggle("right", ok); g.classList.toggle("wrong", !ok);
  }}));
  $$("input.rng").forEach(r => r.addEventListener("input", () => {{ r.nextElementSibling.textContent = r.value; }}));
  $$("button.load").forEach(b => b.onclick = () => {{
    const f = document.createElement("iframe"); f.src = b.dataset.src; f.loading = "lazy"; f.allowFullscreen = true;
    f.title = b.parentElement.querySelector("b").textContent; b.replaceWith(f);
  }});
  const start = () => go((parseInt(location.hash.slice(1)) || 1) - 1);
  start();
  window.addEventListener("deck-ready", () => render());
}})();
</script>
</body>
</html>
"""


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted(REPO.glob("AI_in_TVET_II_WiSe_2026_2027/*/P*.md"))
    for f in files:
        build(f)


if __name__ == "__main__":
    main()
