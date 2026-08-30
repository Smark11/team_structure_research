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
  ("case-studies", "Case Studies", "How eight streaming and media companies organize data",
   "Eight companies, 2012–2026. Every one keeps the platform central; every new hub got a capability, not a domain.",
   "Comparative case studies of Netflix, Spotify, Google/YouTube, Amazon, Disney, WBD, NBCU/Peacock and Paramount, with evidence tags."),
  ("foundations", "Foundations", "The canon, and where it contradicts itself",
   "Nine bodies of work reduced to the claims that matter for a second site — and the places they disagree.",
   "Galbraith, Mintzberg, Conway, Team Topologies, span of control, Larson, Accelerate, the data-org literature and distance research, synthesized."),
  ("applying-it", "Applying It Here", "Mapping it onto a 140-person org",
   "Three tests, fourteen units of work, one ownership table.",
   "The frameworks and evidence applied to a ~140-person data organization and its domains."),
  ("charter-evidence", "Charter Evidence", "What the India evidence rules out",
   "Base rates, eight reference sites and the conversion failure modes. The evidence rules out shared ownership and says nothing about which domain.",
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
n_cited = len(order)
for s in SRC:
    if id(s) not in num:
        order.append(s); num[id(s)] = len(order)

TAGCLS = {"documented": "tag-doc", "inferred": "tag-inf", "folklore": "tag-folk"}
def qualifier(s):
    note = (s.get("note", "") or "").lower()
    for word, label in (("tertiary", "tertiary"), ("wikipedia", "tertiary"), ("vendor", "vendor"), ("marketing", "vendor"), ("secondary", "secondary"), ("search index", "index only"), ("search-index", "index only"), ("excerpt", "excerpt only"), ("403", "blocked; title-level"), ("metadata", "metadata only"), ("summary", "summary only"), ("recruiting", "recruiting copy"), ("via ", "via secondary"), ("scanned", "abstract only")):
        if word in note: return label
    return ""

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
    q = qualifier(s)
    return (f'<li id="s-{n}"><span class="id">{n}</span><div>'
            f'<span class="t"><a href="{url}">{title}</a></span><br><span class="who">{meta}</span>'
            f'{(" <span class=&quot;who&quot;>— " + note + "</span>") if note else ""}'
            f'<a class="url" href="{url}">{url}</a><span class="acc">accessed {acc}</span></div>'
            f'<span class="tg"><span class="tag {TAGCLS[tag]}">{tag}</span>{("<span class=&quot;q&quot;>" + q + "</span>") if q else ""}</span></li>')
def preview_html(s, n):
    who = html.escape(s.get("author", "")); title = html.escape(s.get("title", ""))
    venue = html.escape(s.get("venue", "")); year = html.escape(str(s.get("year", "")))
    url = html.escape(s.get("url", "")); tag = s.get("tag", "documented")
    return (f'<div data-id="s-{n}"><strong>{n}.</strong> {title}<br><span class="who">{who}{(" · " + venue) if venue else ""}{(" · " + year) if year else ""}</span> '
            f'<span class="tag {TAGCLS[tag]}">{tag}</span><br><a href="{url}">{url}</a></div>')

SUPRUN = re.compile(r'(?:<sup class="c">(?:<a href="sources\.html#s-\d+">\d+</a>)+</sup>\s*){2,}|<sup class="c">(?:<a href="sources\.html#s-\d+">\d+</a>){2,}</sup>')
def collapse_sups(html_text):
    def rep(m):
        nums = sorted({int(x) for x in re.findall(r'#s-(\d+)"', m.group(0))})
        # build ranges
        out, i = [], 0
        while i < len(nums):
            j = i
            while j + 1 < len(nums) and nums[j+1] == nums[j] + 1: j += 1
            if j - i >= 2:
                out.append(f'<a href="sources.html#s-{nums[i]}">{nums[i]}</a><a href="sources.html#s-{nums[j]}" class="r">{nums[j]}</a>')
            else:
                out.extend(f'<a href="sources.html#s-{n}">{n}</a>' for n in nums[i:j+1])
            i = j + 1
        return '<sup class="c">' + ''.join(out) + '</sup>'
    return SUPRUN.sub(rep, html_text)

H2 = re.compile(r'<h2 id="([^"]+)">(.*?)</h2>', re.S)
def number_sections(html_text, sec):
    heads = H2.findall(html_text)
    toc = '<ul class="toc">' + ''.join(f'<li><a href="#{i}"><span class="n">{sec}.{k+1}</span>{re.sub(r"<[^>]+>", "", t)}</a></li>' for k, (i, t) in enumerate(heads)) + '</ul>'
    if re.search(r'<ul class="toc">', html_text):
        html_text = re.sub(r'<ul class="toc">.*?</ul>', toc, html_text, count=1, flags=re.S)
    else:
        # insert after the tag key if present, else at the top
        if '<div class="tag-key' in html_text:
            html_text = re.sub(r'(<div class="tag-key[^>]*>.*?</div>)', lambda m: m.group(1) + "\n" + toc, html_text, count=1, flags=re.S)
        else:
            html_text = toc + "\n" + html_text
    k = [0]
    def rep(m):
        k[0] += 1
        return f'<h2 id="{m.group(1)}"><span class="n">{sec}.{k[0]}</span>{m.group(2)}</h2>'
    return H2.sub(rep, html_text)

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
        intro = (f'<p data-cite="none">{n_cited} sources cited on the site, {len(order)} verified in total. Evidence tags describe the source itself: '
                 f'<span class="tag tag-doc">documented</span> primary source, engineering blog, talk or credible reporting ({counts["documented"]}); '
                 f'<span class="tag tag-inf">inferred</span> a reasonable read of public signals, or a page seen only through a search excerpt ({counts["inferred"]}); '
                 f'<span class="tag tag-folk">folklore</span> widely repeated, weakly sourced ({counts["folklore"]}). '
                 f'Every URL was verified on the access date shown. Where a page blocked automated fetching, the note says so.</p>')
        body = intro + '<ol class="src wide">' + "".join(entry_html(s, i+1) for i, s in enumerate(order[:n_cited])) + "</ol>"
        if n_cited < len(order):
            body += (f'<h2 id="consulted">Consulted in the research, not cited on the site</h2>'
                     f'<p data-cite="none">{len(order) - n_cited} sources verified during the research phase whose claims did not survive editing onto the site. Listed so the record is complete; numbered after the cited entries.</p>'
                     '<ol class="src wide" start="' + str(n_cited + 1) + '">' + "".join(entry_html(s, n_cited + i + 1) for i, s in enumerate(order[n_cited:])) + "</ol>")
        render(name, section, h1, dek, desc, body, idx, set())
        continue
    if name not in frags: continue
    cited = set()
    def sub(m):
        n = number_for(m.group(1)); cited.add(n)
        return f'<a href="sources.html#s-{n}">{n}</a>'
    content = CITE.sub(sub, frags[name])
    content = collapse_sups(content)
    content = number_sections(content, idx + 1)
    render(name, section, h1, dek, desc, content, idx, cited)

print(f"sources numbered: {len(order)}")
sys.exit(subprocess.call([sys.executable, str(ROOT / "tools/check-citations.py"), "--warn-only"]))
