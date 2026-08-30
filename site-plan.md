# Site plan — "The Second Site"

Working title for the published site: **The Second Site** (a decision record on what an India engineering site should own, and what that does to the org around it). Identifying details are genericized on the site: "a large streaming/media company," "a ~140-person data organization." The full-context memo lives only in `/decision-memo.md`.

## 1. Job of the site
One reader, one job: a senior data executive who must choose an India-site charter and defend it. The site must let them (a) read the recommendation in two minutes, (b) drill into the defense, (c) check any claim back to a source. Everything else is subordinate.

## 2. Information architecture (fixed by the brief)
| # | Page | File | Job |
|---|------|------|-----|
| 1 | The Recommendation | `index.html` | The memo. One-sentence answer, 2-minute read, drill-down to full defense, phases, tripwires, steelmen. |
| 2 | Case Studies | `case-studies.html` | Eight companies compared; evidence tags visible in UI; reorg timelines. |
| 3 | Foundations | `foundations.html` | The canon, its durable principles, and where it contradicts itself. |
| 4 | Applying It Here | `applying-it.html` | Frameworks mapped to the ~140-person org and its domains (genericized). |
| 5 | Charter Evidence | `charter-evidence.html` | India/GCC findings behind the recommendation. |
| 6 | Learning Plan | `learning-plan.html` | Ranked, annotated, 12-month calendar. |
| 7 | Sources | `sources.html` | Numbered bibliography: author, title, URL, access date, evidence tag. |

Global numbered citations: one master list in `docs/sources.html`; every page cites `<sup><a href="sources.html#s-N">N</a></sup>`. Numbering is site-wide, not per-page, so a source keeps its number everywhere. A checker script (`tools/check-citations.py`) verifies every cited number exists and every source is cited at least once, and that every paragraph carrying a factual claim has a citation or a `[judgment]` label.

## 3. Design direction

**Register:** private decision memo produced with annual-report care. Not a marketing site. Reference points: Stripe Press (typographic confidence, restraint), The Pudding (diagrams that explain), high-end annual reports (numbers set with dignity, generous margins).

**The one aesthetic risk:** the site's colour system *is* the argument. Two hues stand for the two sites — a steel blue for the US org, a marigold for India — and every org-topology diagram, phase path, and decision tree is drawn in those two hues, so "what India owns" is legible as colour before the reader reads a word. Overlap (shared ownership, the time-zone overlap window) is drawn as the two hues interleaved, never blended into a third colour, because blended ownership is the failure mode the memo argues against.

**Ground:** cool paper, not warm cream. Neutrals are biased slightly green-grey toward the ink. No pure grey.

### Tokens
```
--paper:      #F4F5F1   page ground (light)
--paper-2:    #EAECE6   recessed panels, table stripes
--ink:        #16211F   text, rules (green-black)
--ink-2:      #4A5552   secondary text
--ink-3:      #8A938F   captions, hairlines
--us:         #2E4B6B   US org — steel blue
--us-soft:    #D7E0EA
--in:         #C27A1E   India site — marigold (desaturated)
--in-soft:    #F1E1C7
--accent:     var(--us)  links + focus ring use the US blue; India marigold is reserved for diagrams and India-specific callouts so it keeps meaning
Dark theme: --paper #121716, --paper-2 #1A211F, --ink #E8EBE7, --ink-2 #AEB6B2, --ink-3 #6E7773, --us #8FB0D4, --us-soft #23364A, --in #E0A24E, --in-soft #4A3417
```
Evidence tags are encoded by **shape + text, not colour alone**: `[documented]` solid chip, `[inferred]` outlined chip, `[folklore]` dashed-outline chip. All three are ink-on-paper so they read in both themes and to colour-blind readers.

### Type
- **Display & running text:** *Newsreader* (Google Fonts, variable, optical sizes). Display at opsz 72 for page titles and the one-sentence recommendation; text at opsz 16 for body. Italic for pull-quotes and steelman headers. Fallback: Georgia, "Times New Roman", serif.
- **Utility (nav, labels, tables, chips, diagram text):** *Archivo* — slightly condensed grotesk, reads as "annotation" against the serif. Uppercase labels at 11–12px with 0.08em tracking. Fallback: "Helvetica Neue", Arial, sans-serif.
- **Citations & figures:** *JetBrains Mono* for superscript citation numbers, source IDs, and tabular numbers in tables (`font-variant-numeric: tabular-nums`). Fallback: ui-monospace, Menlo, monospace.
- **Scale (1.25 major third, base 18px):** 12 / 14 / 18 / 22.5 / 28 / 35 / 44 / 55. Line-height 1.55 body, 1.1 display. Measure 66ch.

### Layout
- A **reading column with a marginalia rail**: on ≥1100px the body column is 66ch left-of-centre and a right rail carries evidence tags, "why this matters here" asides, and figure captions, the way an annotated report is set. Below 1100px the rail content folds inline as small labelled blocks. No sidebar nav; a slim sticky top bar with the seven sections and a progress hairline.
- Each page opens with an **eyebrow (section number + name)**, a title in Newsreader display, and a one-paragraph "what this page settles" dek. No hero imagery.
- Section numbering is used because the seven pages *are* a sequence (answer → evidence → theory → application → site-specific evidence → what to read → sources); it encodes reading order, not decoration.
- Diagrams are inline SVG, hand-designed, in the two-hue system with Archivo labels; each has a `<figcaption>` and an accessible `<title>/<desc>`. Planned figures:
  1. **Org topologies** (index / applying-it): four charter models drawn side-by-side as the same 140-person org with ownership colour-coded.
  2. **The phased charter path** (index): a horizontal path with graduation gates; the India hue grows in area across phases.
  3. **Decision tree** (index): which charter under which conditions; the reader's branch highlighted.
  4. **Reorg timelines** (case-studies): a compact timeline per company, tick marks at reorgs.
  5. **Time-zone overlap** (charter-evidence): a 24-hour band showing Pacific/Eastern vs. IST and the working overlap window.
  6. **Framework disagreement map** (foundations): frameworks as nodes, tensions as edges.
- Motion: none beyond a 150ms hover/focus transition and the progress hairline. `prefers-reduced-motion` respected. The page is a document; it should not perform.

### Accessibility & performance
- Semantic landmarks (`header/nav/main/aside/footer`), one `h1` per page, skip link, visible focus ring (2px, `--us`), all diagrams with text alternatives, contrast ≥ 4.5:1 for text in both themes (checked).
- No JS required to read anything. JS used only for: theme respects OS (CSS-only), progress hairline, citation hover previews (progressive enhancement), and the drill-down `<details>` elements which work without JS.
- Budget: < 120KB HTML+CSS per page excluding fonts; three font families, ≤ 6 weight/style files, `display=swap`. No frameworks, no images except inline SVG.

## 4. Build approach (no build step for serving)
Hand-authored HTML per page sharing one `docs/assets/site.css` and `docs/assets/site.js`. A small authoring-time script (`tools/check-citations.py`, Python stdlib) validates citations; it is not needed to serve the site. Sources master list authored once in `docs/sources.html`; research reports' local keys (`[C1-3]` etc.) are mapped to global numbers in `research/source-map.md`.

## 5. Content mapping (filled after Phase 1 research)
_To be completed._
