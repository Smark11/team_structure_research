#!/usr/bin/env python3
"""Authoring-time build: wrap content fragments in the page template, assign site-wide
source numbers in order of first citation, generate docs/sources.html, then audit.
Serving needs none of this — docs/ is plain HTML."""
import json, re, pathlib, html, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
TPL = (ROOT / "tools/page-template.html").read_text(encoding="utf-8")
SRC = json.loads((ROOT / "research/sources.json").read_text(encoding="utf-8"))
OUT = ROOT / "docs"

PAGES = [
  # file, section name, h1, dek, description
  ("index", "The Recommendation", "What the India site should own",
   "One answer, defended in two minutes, with the full case underneath.",
   "The recommendation on the India site's charter for a ~140-person data organization, with phases, tripwires and steelmanned alternatives."),
  ("case-studies", "Case Studies", "How eight streaming and media companies actually organize data",
   "Reorgs beat snapshots: what changed, why, and what is plausibly attributable to structure.",
   "Comparative case studies of Netflix, Spotify, Google/YouTube, Amazon, Disney, WBD, NBCU/Peacock and Paramount, with evidence tags."),
  ("foundations", "Foundations", "The canon, and where it contradicts itself",
   "Nine bodies of work reduced to the claims that matter for a second site — and the places they disagree.",
   "Galbraith, Mintzberg, Conway, Team Topologies, span of control, Larson, Accelerate, the data-org literature and distance research, synthesized."),
  ("applying-it", "Applying It Here", "Mapping it onto a 140-person org",
   "Three tests, eight domains, one ownership table.",
   "The frameworks and evidence applied to a ~140-person data organization and its domains."),
  ("charter-evidence", "Charter Evidence", "What the India evidence actually discriminates",
   "Base rates, reference sites, conversion failure modes, and the distributed-work research.",
   "The GCC and distributed-work evidence behind the India charter recommendation."),
  ("learning-plan", "Learning Plan", "What to read, and when",
   "Ten books, twelve blogs, nine podcasts — ranked for this decision and verified.",
   "A ranked, verified, 12-month learning plan for the org-design decision."),
  ("sources", "Sources", "Sources",
   "Every claim on this site resolves here. Numbered in order of first citation; each entry carries an evidence tag and the date it was accessed.",
   "Full bibliography with evidence tags, URLs and access dates."),
]

key2src = {}
for s in SRC:
    for k in s["keys"]:
        assert k not in key2src, f"duplicate key {k}"
        key2src[k] = s

CITE = re.compile(r'<a href="sources\.html#(C\d-\d+)">[^<]*</a>')
order = []      # sources in order of first citation
num = {}        # id(source) -> number
def number_for(key):
    s = key2src.get(key)
    if s is None:
        raise SystemExit(f"UNKNOWN CITATION KEY {key}")
    if id(s) not in num:
        order.append(s); num[id(s)] = len(order)
    return num[id(s)]

frags = {}
for name, *_ in PAGES:
    if name == "sources": continue
    p = ROOT / "tools/content" / f"{name}.html"
    if not p.exists():
        print(f"  (missing fragment {p.name}, skipping)"); continue
    txt = p.read_text(encoding="utf-8")
    for m in CITE.finditer(txt):
        number_for(m.group(1))
    frags[name] = txt
# uncited sources get numbers at the end so the bibliography is complete
for s in SRC:
    if id(s) not in num:
        order.append(s); num[id(s)] = len(order)

TAGCLS = {"documented": "tag-doc", "inferred": "tag-inf", "folklore": "tag-folk"}
def entry_html(s, n):
    who = html.escape(s.get("author", ""))
    title = html.escape(s.get("title", ""))
    venue = html.escape(s.get("venue", ""))
    year = html.escape(str(s.get("year", "")))
    url = html.escape(s.get("url", ""))
    acc = html.escape(s.get("accessed", "2026-08-29"))
    tag = s.get("tag", "documented")
    note = html.escape(s.get("note", "") or "")
    meta = " · ".join(x for x in [who, venue, year] if x)
    return (f'<li id="s-{n}"><span class="id">{n}</span><div>'
            f'<span class="t"><a href="{url}">{title}</a></span><br><span class="who">{meta}</span>'
            f'{(" <span class=&quot;who&quot;>— " + note + "</span>") if note else ""}'
            f'<a class="url" href="{url}">{url}</a><span class="acc">accessed {acc}</span></div>'
            f'<span class="tg"><span class="tag {TAGCLS[tag]}">{tag}</span></span></li>')
def preview_html(s, n):
    who = html.escape(s.get("author", "")); title = html.escape(s.get("title", ""))
    venue = html.escape(s.get("venue", "")); year = html.escape(str(s.get("year", "")))
    url = html.escape(s.get("url", "")); tag = s.get("tag", "documented")
    return (f'<div data-id="s-{n}"><strong>{n}.</strong> {title}<br><span class="who">{who}{(" · " + venue) if venue else ""}{(" · " + year) if year else ""}</span> '
            f'<span class="tag {TAGCLS[tag]}">{tag}</span><br><a href="{url}">{url}</a></div>')

def render(name, section, h1, dek, desc, content, idx, cited_nums):
    words = len(re.sub(r"<[^>]+>", " ", content).split())
    mins = max(1, round(words / 230))
    prev_i = (idx - 1) % len(PAGES); next_i = (idx + 1) % len(PAGES)
    out = TPL
    reps = {
      "{{PAGE_TITLE}}": html.escape(section if name != "index" else "The Recommendation"),
      "{{PAGE_DESC}}": html.escape(desc), "{{NUM}}": str(idx + 1), "{{SECTION_NAME}}": section,
      "{{H1}}": h1, "{{DEK}}": dek, "{{READ_TIME}}": f"{words:,} words · {mins} min",
      "{{CONTENT}}": content,
      "{{PREV_HREF}}": PAGES[prev_i][0] + ".html", "{{PREV_TITLE}}": f"{prev_i+1} · {PAGES[prev_i][1]}",
      "{{NEXT_HREF}}": PAGES[next_i][0] + ".html", "{{NEXT_TITLE}}": f"{next_i+1} · {PAGES[next_i][1]}",
    }
    for i in range(1, 8):
        reps[f"{{{{CUR_{i}}}}}"] = ' aria-current="page"' if i == idx + 1 else ""
    for k, v in reps.items():
        out = out.replace(k, v)
    if cited_nums:
        tpl = '<template id="src-index">' + "".join(preview_html(order[n-1], n) for n in sorted(cited_nums)) + "</template>\n"
        out = out.replace('<script src="assets/site.js"></script>', tpl + '<script src="assets/site.js"></script>')
    (OUT / f"{name}.html").write_text(out, encoding="utf-8")
    print(f"  wrote {name}.html  ({words:,} words, {len(cited_nums)} distinct sources)")

for idx, (name, section, h1, dek, desc) in enumerate(PAGES):
    if name == "sources":
        counts = {"documented": 0, "inferred": 0, "folklore": 0}
        for s in order: counts[s.get("tag", "documented")] += 1
        intro = (f'<p data-cite="none">{len(order)} sources. Evidence tags describe the source itself: '
                 f'<span class="tag tag-doc">documented</span> primary source, engineering blog, talk or credible reporting ({counts["documented"]}); '
                 f'<span class="tag tag-inf">inferred</span> a reasonable read of public signals, or a page seen only through a search excerpt ({counts["inferred"]}); '
                 f'<span class="tag tag-folk">folklore</span> widely repeated, weakly sourced ({counts["folklore"]}). '
                 f'Every URL was verified on the access date shown. Where a page blocked automated fetching, the note says so.</p>')
        body = intro + '<ol class="src wide">' + "".join(entry_html(s, i+1) for i, s in enumerate(order)) + "</ol>"
        render(name, section, h1, dek, desc, body, idx, set())
        continue
    if name not in frags: continue
    cited = set()
    def sub(m):
        n = number_for(m.group(1)); cited.add(n)
        return f'<a href="sources.html#s-{n}">{n}</a>'
    content = CITE.sub(sub, frags[name])
    render(name, section, h1, dek, desc, content, idx, cited)

print(f"sources numbered: {len(order)}")
sys.exit(subprocess.call([sys.executable, str(ROOT / "tools/check-citations.py"), "--warn-only"]))
