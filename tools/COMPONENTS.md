# Component guide for page authors (docs/*.html)

Pages are hand-authored HTML sharing `docs/assets/site.css`. Write ONLY the inner content that goes inside `<div class="body"> … </div>` (see `tools/page-template.html`); the build script wraps it. Use the components below and nothing else — no inline styles, no new classes, no emoji, no images.

## Grid
`.body` is a two-column grid: main reading column (66ch) + right rail. Every direct child sits in the main column unless it has class `rail` (goes to the right rail, next to the preceding block) or `wide` (spans both columns — use for tables, figures, card grids).

```html
<h2 id="slug">Section title</h2>
<p>Body text…<sup class="c"><a href="sources.html#C1-3">C1-3</a></sup></p>
<aside class="rail"><span class="label">Why it matters here</span><p>Short marginal note in the rail.</p></aside>
<div class="tbl-wrap wide"><table>…</table></div>
```

## Citations — MANDATORY on every factual claim
`<sup class="c"><a href="sources.html#C1-3">C1-3</a></sup>` — use the research report's local key (C1-3, C2-12, C3-43, C4-1, C5-22). The build script converts keys to site-wide numbers and verifies each key exists; a wrong key fails the build. Two citations: two adjacent `<sup>`s. Put the citation at the end of the sentence or clause it supports. A paragraph with a factual claim and no citation fails the audit UNLESS it carries a judgment tag (below).

## Evidence & judgment tags
- `<span class="tag tag-doc">documented</span>` — engineering blog, talk, credible reporting, primary source
- `<span class="tag tag-inf">inferred</span>` — reasonable read of public signals
- `<span class="tag tag-folk">folklore</span>` — widely repeated, weakly sourced
- `<span class="tag tag-judg">judgment</span>` — an opinion/position, not a sourced fact

Every case-study claim gets one of the first three, placed right after the claim (inside the sentence or at its end, before the citation). Judgment paragraphs open or close with the judgment tag.
Put a tag key at the top of any page that uses tags:
```html
<div class="tag-key wide"><span><span class="tag tag-doc">documented</span> primary source or credible reporting</span><span><span class="tag tag-inf">inferred</span> reasonable read of public signals</span><span><span class="tag tag-folk">folklore</span> widely repeated, weakly sourced</span><span><span class="tag tag-judg">judgment</span> our position, not a sourced fact</span></div>
```

## Text components
- `<h2 id="…">` sections, `<h3>` subsections, `<h4>` small-caps labels.
- `<p>`, `<ul>`, `<ol>`, `<blockquote>` (for a real quotation; cite it).
- `<div class="note"><span class="label">Label</span><p>…</p></div>` — callout; add class `in` for an India-specific callout.
- `<div class="judgment"><span class="label">Judgment</span><p>…</p></div>` — a boxed position statement (paragraphs inside are exempt from the citation audit).
- `<details class="drill"><summary>Title <span class="k">optional key</span></summary><div class="in">…</div></details>` — drill-down; the memo's "read in 2 minutes, drill for the defense" pattern.
- `<ul class="toc">` with `<li><a href="#slug"><span class="n">2.1</span>Title</a></li>` — page table of contents right after the page head.

## Data components
- Tables: always wrap `<div class="tbl-wrap wide"><table><thead>…</thead><tbody>…</tbody></table></div>`; numeric cells `class="num"`.
- Case cards: `<div class="cases wide"><article class="case"><div class="co">Netflix</div><h3>Title</h3><p>…</p></article>…</div>`
- Ranked list (learning plan): `<ol class="rank"><li><h3>Title</h3><div class="by">Author · Publisher, Year</div><p>…</p><span class="when">Read: month 1</span></li></ol>`
- Phases: `<ol class="phases"><li><div class="ph">Months 0–3</div><div><h3>Phase 0 — Foundation</h3><p>…</p><p class="gate"><strong>Gate</strong> criteria…</p></div></li></ol>`
- Tripwires: `<ol class="tripwires"><li><div><span class="label">Tripwire</span><p>…</p></div><div class="fb"><span class="label">Fallback</span><p>…</p></div></li></ol>`

## Figures
`<figure class="wide"><svg viewBox="0 0 960 420" role="img" aria-labelledby="f1t f1d"><title id="f1t">…</title><desc id="f1d">…</desc>…</svg><figcaption><span class="fig">Fig. 2.1</span>Caption.</figcaption></figure>`
Diagrams are drawn in the two-hue system: US = `class="fig-us"` (fill) / `fig-stroke-us`, India = `fig-in` / `fig-stroke-in`, soft variants `fig-us-soft` / `fig-in-soft`; neutral ink `fig-ink`, `fig-ink2`, `fig-ink3`, `fig-paper`, `fig-paper2`, rules `fig-rule`. Text classes: `fig-t` (12px), `fig-t2` (11px secondary), `fig-l` (10px uppercase label), `fig-m` (mono). Never hard-code colours. Keep strokes 1–1.5px. The lead author draws the main diagrams; page authors may add small ones (timelines) following this system.

## Voice
Blunt private-memo voice. Take positions; label them. No filler, no "in today's fast-paced world," no restating the other pages. The reader's employer is never named: "a large streaming/media company," "the ~140-person org," "the India site."
