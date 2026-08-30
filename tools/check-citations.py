#!/usr/bin/env python3
"""Authoring-time citation audit for docs/. Not needed to serve the site.

Checks:
  1. Every <sup class="c"><a href="sources.html#s-N"> points at an existing <li id="s-N"> in docs/sources.html.
  2. Every source entry is cited at least once somewhere in docs/.
  3. Coverage: every <p> inside <main> that is not marked data-kind="judgment"/"nav"/"meta" and is not inside
     an element with class "judgment" carries at least one citation, OR contains a [judgment] tag, OR is
     explicitly opted out with data-cite="none" (for pure structural/transitional text). Reports each miss.
Exit code 1 on any hard failure (1, 2) or any coverage miss unless --warn-only.
"""
import re, sys, pathlib, html

ROOT = pathlib.Path(__file__).resolve().parents[1] / "docs"
pages = sorted(p for p in ROOT.glob("*.html"))
src_html = (ROOT / "sources.html").read_text(encoding="utf-8")
source_ids = set(re.findall(r'<li[^>]*\bid="(s-\d+)"', src_html))

cite_re = re.compile(r'<sup class="c">(.*?)</sup>', re.S)
href_re = re.compile(r'href="sources\.html#(s-\d+)"')
p_re = re.compile(r'<p\b([^>]*)>(.*?)</p>', re.S)
main_re = re.compile(r'<main\b.*?</main>', re.S)

bad_refs, cited, misses = [], set(), []
for page in pages:
    txt = page.read_text(encoding="utf-8")
    for m in href_re.finditer(txt):
        cited.add(m.group(1))
        if m.group(1) not in source_ids:
            bad_refs.append((page.name, m.group(1)))
    if page.name == "sources.html":
        continue
    mm = main_re.search(txt)
    body = mm.group(0) if mm else txt
    # strip regions exempt from coverage
    body = re.sub(r'<(figure|nav|aside|table|details class="drill">\s*<summary|summary)\b.*?</\1>', '', body, flags=re.S)
    body = re.sub(r'<div class="[^"]*\bjudgment\b[^"]*">.*?</div>', '', body, flags=re.S)
    for pm in p_re.finditer(body):
        attrs, inner = pm.group(1), pm.group(2)
        if 'data-cite="none"' in attrs: continue
        if re.search(r'class="[^"]*\b(dek|thesis|muted|by|fb|small|co)\b', attrs): continue
        if 'sources.html#s-' in inner: continue
        if 'tag-judg' in inner or '[judgment]' in inner: continue
        plain = re.sub(r'<[^>]+>', '', inner).strip()
        if len(plain) < 40: continue  # transitional fragment
        misses.append((page.name, html.unescape(plain)[:110]))

uncited = sorted(source_ids - cited, key=lambda s: int(s.split('-')[1]))
warn_only = "--warn-only" in sys.argv
print(f"pages: {len(pages)}  sources: {len(source_ids)}  cited ids: {len(cited)}")
if bad_refs:
    print("\nDANGLING CITATIONS:"); [print(f"  {p}: {i}") for p, i in bad_refs]
if uncited:
    print("\nUNCITED SOURCES:"); print("  " + ", ".join(uncited))
if misses:
    print(f"\nPARAGRAPHS WITHOUT CITATION OR JUDGMENT LABEL ({len(misses)}):")
    for p, t in misses: print(f"  {p}: {t}…")
ok = not bad_refs and not uncited and (warn_only or not misses)
print("\nRESULT:", "OK" if ok else "FAIL")
sys.exit(0 if ok else 1)
