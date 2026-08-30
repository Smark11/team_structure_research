# Cycle 1 — responses to all four reviewers

**Date:** 2026-08-30. Every numbered item from `cycle-1-red-team.md` (A1–A27), `cycle-1-fact-check.md` (B1–B43), `cycle-1-editor.md` (C1–C35) and `cycle-1-design.md` (D1–D34) is listed with its disposition. **Accepted** = applied as proposed; **Modified** = applied with a stated change; **Rejected** = not applied, with the one-line reason. The recommendation memo moved from v1 to v2 (`research/recommendation.md`); the site was rebuilt against it.

## What changed in the recommendation (summary)

1. The first domain is **quality of experience**, not "sessions and QoE": sessionization and engagement metrics stay central because the session fact table fails the separability test (A6).
2. Phase 1 transfers **two** components (telemetry ingestion; experimentation engine), not three; data-quality tooling moves in Phase 2, staffed during Phase 1 (A10). Staffing arithmetic is shown.
3. The experimentation interface is drawn as a **versioned metric-definition contract**: India owns computation including the implementation of definitions; the US owns semantic definitions, the catalog and the review gate (A19).
4. The "27% graduate within five years" statistic is retired as a base rate; the 56/44 snapshot is used, and Zinnov's own 27% claim appears once, attributed, with the method-unpublished caveat (A3, B1 verified the number exists on Zinnov's page).
5. Gates name the **measurement system and owner**; DORA's four metrics are replaced by contract breaches, P1 incidents and backfill hours; thresholds are "baseline plus its own variance" (A11, A12).
6. Attrition gate raised to **≤ 25% regretted, not rising** — the market base rate (A13).
7. **Twelve tripwires** (T1–T12); fallbacks narrow instead of returning work to dissolved teams (A14, A16).
8. A **cost table**, a **sensitivity table** (20/40/60 contractors, concentration), a **fraud-first steelman**, an **ads-measurement** candidate, and a **Phase 0 legal/PII review** were added (A8, A17, A20, A21, A22).
9. The platform-drift claim is downgraded to judgment; option B's rebuttal is rewritten as "a hedge, not a documented necessity"; tripwire T5's landing is reconciled with it (A18).
10. The memo states plainly that it graduates and that its criteria are invented (A2).

---

## Reviewer A — red team

| # | Sev | Disposition | Note |
|---|---|---|---|
| A1 | blocking | **Accepted** | "Three of five tracks named QoE" removed everywhere; replaced with the honest summary (C3 fraud; C5 telemetry capability; C1/C2 graduating QoE/sessions, C2 fraud first) and the choice labelled as the memo's judgment. |
| A2 | major | **Modified** | The memo now says it graduates and that its criteria are invented. The one-sentence recommendation keeps "not an extension" in the narrow sense stated: no phase in which India contributes to work the US owns. The "undocumented criteria" argument against option C is dropped. |
| A3 | blocking | **Modified** | "27% / 73% / within five years" retired as a base rate everywhere (index, Fig 1.1, steelmen, charter evidence, applying-it). Reviewer B then verified the sentence "27% reach Portfolio Hub in 5 years" is on Zinnov's page, so it is cited **once** on Charter Evidence and once on the index drill-down as Zinnov's claim with "method not published" — never as a rate the memo stands on. |
| A4 | major | **Accepted** | Hotstar tagged `inferred, single trade source` everywhere; reframed as "follows its market's P&L, true of any charter"; no longer the lead example in the two-minute section. |
| A5 | major | **Accepted** | "Every remote site" replaced with the precise statement (new hubs: Warsaw, Bengaluru, WBD India; Zurich ~18 years; Sky origin site; Boston acquired; Hotstar home-market). |
| A6 | blocking | **Accepted** | QoE scored on the page against its real stakeholders (playback, client, CDN/live ops, device certification) and the session fact's dependents. Result: Test 1 partial, Test 3 pass only with sessionization excluded — so sessionization stays central and the domain is QoE alone. Matrix rescored; experimentation engine and QoE now consistent on Test 3. |
| A7 | minor | **Accepted** | Fig 4.1 desc, prose and marks reconciled (applying-it agent). |
| A8 | major | **Accepted** | "Why not fraud first" paragraph added to memo §1 and index 1.2e with the compact scoring table; the honest reason stated: lower risk over higher relevance. |
| A9 | major | **Accepted** | "India PM" replaced by a staff-level QoE analytics lead who owns the roadmap and is the named decision-maker for metric-definition changes; Target/Lowe's PM citations no longer used to justify the role. |
| A10 | major | **Accepted** | Phase 1 reduced to two components; per-component converted/net-new math shown; Gate 0 requires one engineering manager *started* per Phase 1 component. |
| A11 | major | **Accepted** | DORA metrics replaced by contract breaches, P1 incidents, backfill hours; baseline captured in Phase 0 as a precondition; C3 §7 cited honestly; 30% replaced by baseline-plus-variance. |
| A12 | blocking | **Accepted** | Every numeric gate names its system, owner and start; the wanted list is frozen in writing at month 1; the 30% gate carries the anti-gaming check (no rise in contract breaches). |
| A13 | major | **Accepted** | Gate ≤ 25% regretted and not rising; retention grant at months 18/30; expected turnover arithmetic on Charter Evidence. |
| A14 | major | **Accepted** | T9 sponsor leaves, T10 site head leaves, T11 hiring freeze, T12 vendor blocks release added; US QoE dissolution announced at month 6 with retention through month 12. |
| A15 | minor | **Accepted** | T7 now says "no structural fallback; at the new executive's discretion"; the mitigation is leverage (telemetry; ads measurement if chosen). |
| A16 | blocking | **Accepted** | T3 and T5 fallbacks rewritten to narrow, not return; transfer-back only after a US team is re-formed. |
| A17 | major | **Accepted** | Sensitivity table (20/40/60; platform+QoE vs commerce concentration); "±30%" claim deleted; "if contractors sit in commerce, re-run the decision" stated. |
| A18 | major | **Accepted** | Drift claim downgraded to judgment; §5B rewritten as "why we add one domain anyway: a hedge"; T5's landing ("the site is option B") reconciled. |
| A19 | blocking | **Accepted** | Experimentation line redrawn (option 1 in the critique): India owns computation incl. definition implementation via a versioned schema; US owns semantics, catalog, review gate; T4 covers the contract failing. |
| A20 | blocking | **Accepted** | Three-year cost table with ranges and the CFO sentence; all assumption-flagged. |
| A21 | major | **Accepted** | Legal/PII review moved to Phase 0 with a named owner (privacy counsel); Phase 3 fraud conditional on it; QoE telemetry PII noted at Phase 2. |
| A22 | major | **Accepted** | Ads measurement scored (row in the memo table and Fig 4.1); named as a Phase 3 alternative; "no ads tier" handled in the baseline and sensitivity. |
| A23 | minor | **Accepted** | One rule: Phase 1 starts when Gate 0 passes, target month 3, no later than 6 (T1 at 6); sourcing plan for the site head stated. |
| A24 | major | **Accepted** | Phase 1 management arrangement stated: site head runs the teams directly with two tech leads; the ≤ 8 rule is suspended until managers land. |
| A25 | minor | **Accepted** | "Herbsleb 2.5× applied to 1:1s" deleted; remote directs banned as judgment without the citation; overlap figures unified. |
| A26 | minor | **Accepted** | Two-minute section tagged at drill-down granularity; "hired before ownership moved" → "had by the time ownership was described as theirs; sequence not documented". |
| A27 | minor | **Accepted** | T6 detection added: quarterly duplicate-pipeline audit by the metrics-catalog function. |

## Reviewer B — fact-check and citation audit

| # | Sev | Disposition | Note |
|---|---|---|---|
| B1 | blocking | **Accepted** | Charter Evidence §5.1 rewritten to "about 110 between early 2024 and late 2025; more than 120 since January 2023 — roughly 50 a year; 35% of mid-market centres". |
| B2 | blocking | **Accepted** | 25–40% everywhere; constants table updated; the 15–40% figure noted as unsupported in C5. |
| B3 | blocking | **Accepted** | Cambridge URL replaced (DOI added to note). |
| B4 | blocking | **Modified** | Primary URL switched to the McKinsey article page; the archetype ranges recorded in the source note so the claim survives link rot. Browser confirmation deferred to cycle 2's fact-checker. |
| B5 | blocking | **Accepted** | Concurrency numbers removed from index 1.2a; Charter Evidence card cites C2-17 (ByteByteGo) for ~60M (2023). |
| B6 | blocking | **Accepted** | Fig 2.2 caption cites Hotstar to C2-15/C2-16 (case-studies agent). |
| B7 | blocking | **Accepted** | Sky sentence rewritten to the Desk's figures (3,000 since 2023; 2,000 call-centre; 600 tech, Sept 2025) with the exact quotation. |
| B8 | blocking | **Accepted** | Paramount quotations paraphrased or replaced with the Desk's actual wording. |
| B9 | blocking | **Accepted** | Attribution corrected to EY via VARINDIA; quotation marks removed; Zinnov's 7:1–8:1 kept separately. |
| B10 | blocking | **Accepted** | Stancil "delegated" clause deleted. |
| B11 | blocking | **Accepted** | sources.json author → Filippova, A.; sentence rewritten without the quotation. |
| B12 | major | **Accepted** | Zurich analytics clause → `inferred`. |
| B13 | major | **Accepted** | Paramount CTO non-replacement → `inferred`. |
| B14 | major | **Accepted** | HBO Max timing rewritten to the sources' dates; `inferred` beyond them. |
| B15 | major | **Accepted** | Hotstar drain → `inferred` on Charter Evidence (both places). |
| B16 | major | **Accepted** | D'Amaro name dropped from the documented sentence. |
| B17 | major | **Accepted** | Cummings, Ramasubbu and Carmel sentences tagged `inferred` (findings via search summary) on Charter Evidence and Foundations. |
| B18 | major | **Accepted** | Bryar & Carr sentence cited to C1-31 (the page actually read) and tagged accordingly. |
| B19 | major | **Accepted** | Olli placement → `inferred`; Warsaw sentence left visibly unsourced (no citation) with `inferred`. |
| B20 | major | **Modified** | Rather than a fourth pill state, the Sources page now renders a visible qualifier under the tag ("tertiary", "vendor", "secondary", "index only", "blocked; title-level", "via secondary") derived from the source note. Page-level claims resting only on Wikipedia keep `documented` where the underlying primary is a press release the Wikipedia entry cites; Hotstar-only-via-Wikipedia claims on index are now limited to what the entry supports. |
| B21 | major | **Accepted** | Larson quotations cited to the book (C3-22) where not in the 2018 post; "three to five" attributed to the book. |
| B22 | major | **Accepted** | DORA platform-engineering clause deleted. |
| B23 | major | **Accepted** | "roughly a third" → "significantly" for Cataldo. |
| B24 | major | **Accepted** | Urwick disclosure cited to Nickols (C3-17); quotation marked as quoted in secondary sources. |
| B25 | major | **Accepted** | "Via" notes on Thompson and Urwick entries (rendered as the qualifier). |
| B26 | major | **Accepted** | Target: 2005 cited to ANSR (C5-23); "over roughly two decades"; "ten to twenty years". |
| B27 | major | **Accepted** | JPMorgan quotation cited to C5-26. |
| B28 | major | **Accepted** | "$2B synergy target" deleted; ">95% cloud-native" verified-or-deleted by the case-studies agent. |
| B29 | major | **Modified** | The Spotify locations page is not in sources.json; rather than add an unverified entry, the sentence is reduced to what C1-21 supports (hub list) and the India offices clause is dropped. |
| B30 | major | **Accepted** | Google job-title specifics removed from quotation marks; sentence kept as `inferred` without specifics. |
| B31 | minor | **Accepted** | All three quotations corrected to the source wording. |
| B32 | minor | **Accepted** | "Global Networks (later renamed Discovery Global)". |
| B33 | minor | **Accepted** | "AI and cloud roles — the closest published proxy for data roles". |
| B34 | minor | **Accepted** | Learning-plan "dropped" list marked `data-cite="none"` deliberately; "after a decade" removed from the Citi sentence. |
| B35 | minor | **Accepted** | "An order of magnitude larger" everywhere (also C3). |
| B36 | minor | **Accepted** | "as of its 2020–2022 posts". |
| B37 | minor | **Accepted** | Mode 2015 / Corthell attribution; dated anchor added. |
| B38 | minor | **Accepted** | "(page undated, accessed 2026-08-29)" in the source notes for the two careers pages; "undated (c. 2018)" for the Spotify post. |
| B39 | minor | **Accepted** | The build now collapses adjacent citations into a sorted, deduplicated run. |
| B40 | minor | **Accepted** | C1-6 added to the "first engineering hub" sentence. |
| B41 | minor | **Accepted** | Fowler bliki (C4-15) added for Leroy and Simons. |
| B42 | minor | **Accepted** | "7,000 cuts" figure dropped or cited to the Disney release by the case-studies agent. |
| B43 | minor | **Accepted** | Herbsleb DOI recorded in the note; verification claim corrected. |

## Reviewer C — editor

| # | Sev | Disposition | Note |
|---|---|---|---|
| C1 | blocking | **Accepted** | Learning Plan intro, milestone table, calendar and the Kohavi/Bungay/Accelerate/Fundamentals/Team Topologies entries re-keyed to the v2 gates (months 3/9/18/30; Phase 1 two components; Phase 2 QoE + DQ). |
| C2 | blocking | **Accepted** | 45–50 everywhere. |
| C3 | blocking | **Accepted** | "An order of magnitude larger." |
| C4 | blocking | **Accepted** | "The twelve-hour gap"; range 9.5–13.5 stated once in Fig 4.3's caption. |
| C5 | blocking | **Accepted** | Charter Evidence overlap sentence uses the Fig 4.3 constants; "worst case in the Cummings data" dropped. |
| C6 | blocking | **Modified** | Standardized on **25–40%**, not 15–40%: Reviewer B showed the cited source says 25–40 and no source says 15–40. |
| C7 | blocking | **Accepted** | Foundations span sentence → "seven to eight for standardized work; five to seven for domain teams; nothing at ten". |
| C8 | blocking | **Modified** | Neither "every" nor "7 of 9": the precise statement (new hubs vs origin/acquired/home-market sites) from A5 is used on both pages; Fig 2.2 caption matches. |
| C9 | blocking | **Accepted** | Hotstar drain `inferred` on Charter Evidence. |
| C10 | blocking | **Accepted** | Both sentences rewritten with the judgment label ("Half-ownership is diffuse ownership by design. [judgment]"). |
| C11 | blocking | **Accepted** | "56% … still execution shops" + judgment. |
| C12 | blocking | **Accepted** | Rewritten: what the owners had (documented) vs. what this site lacks on the assumed baseline. |
| C13 | blocking | **Modified** | Pointer appended to Foundations §3.9 with v2's reasoning (fraud loses on legal exposure and decision latency, not standardization; QoE first; fraud gated). |
| C14 | blocking | **Accepted** | Principle numbers added to the three tests and the gate on Applying It. |
| C15 | blocking | **Accepted** | "Peer relevance". |
| C16 | major | **Accepted** | Distance research in full only on Foundations §3.10; Charter Evidence keeps Fig 5.2 (now an inline rail figure) and one summary sentence; Applying It keeps one derivation sentence per test. |
| C17 | major | **Accepted** | Hotstar in full only on Case Studies; index and Charter Evidence carry the short versions supplied. |
| C18 | major | **Modified** | Went further: the 27% is removed as a base rate everywhere and appears once as Zinnov's attributed claim (see A3/B1). |
| C19 | major | **Accepted** | Foundations §3.11 case-studies H3 cut to the judgment box. |
| C20 | major | **Accepted** | Target quote in full on index (as the page's pull quote) and on the Target card; §1.6d references it. |
| C21 | major | **Accepted** | Full "US stops doing" list on Applying It; index §1.4 cut to the two-paragraph version; rewards paragraph deduplicated. |
| C22 | major | **Modified** | Index 1.2e is not reduced to four sentences — the red team required the scoring to be shown where the claim is made — but it now carries the compact four-row table and links to the full matrix; Applying It keeps the full judgment box. |
| C23 | major | **Accepted** | Zinnov/Forrester quotations in full only on Charter Evidence §5.3; clauses elsewhere. |
| C24 | major | **Accepted** | Month 9 everywhere (dissolved at the transfer; announced at month 6). |
| C25 | major | **Accepted** | T1–T12 numbering; Applying It references "tripwire T6". |
| C26 | major | **Accepted** | Case Studies cut list applied (case-studies agent); target ~5,500. |
| C27 | major | **Accepted** | Foundations cut list applied (foundations agent); target ~4,000. |
| C28 | minor | **Accepted** | Throat-clearing lines cut; "actually" ×5 cut; "binding constraint" reduced. |
| C29 | minor | **Accepted** | Deks and H1s updated in the build's page table; Fig 2.1 caption prefix; Fig 5.1 caption (without the 27%); §3.6 heading. |
| C30 | minor | **Modified** | Two-minute section restructured with "the US stops owning them" second and Fig 1.1 moved to the top of §1.2, per the proposed text — with the 27% sentence replaced and the evidence tags added (A26). It is ~480 words: the red team's tagging requirement and the cost line add length the editor's draft did not carry. |
| C31 | minor | **Accepted** | Disney "exactly why" softened to the sequence the source supports. |
| C32 | minor | **Superseded** | The "three of five" claim was removed entirely (A1). |
| C33 | minor | **Accepted** | Evidence-collection notes moved out of the argument pages; they live in the source notes. |
| C34 | minor | **Accepted** | Foundations figures renumbered in page order. |
| C35 | minor | **Accepted** | "There is no clean resolution" cut; Charter Evidence "one gap" paragraph reduced to a clause. |

## Reviewer D — design critic

| # | Sev | Disposition | Note |
|---|---|---|---|
| D1 | blocking | **Accepted** | Fig 4.2 redrawn at 960×560 with the note block moved right of the spine, headers on solid fills in paper, boxes widened, "cross this line" relocated (applying-it agent). |
| D2 | blocking | **Modified** | Base label sizes raised (fig-t 13, fig-t2 12, fig-l 11, fig-m 11.5); dense figures get a `figure.scroll` wrapper (min-width 720px, "scroll →" cue) and a `details.alt` text-alternative table; simple charts (5.1, 5.2) are redrawn at ≤ 720 viewBox with ≥ 12px text. Mobile-specific second SVGs were **not** built for 1.1/3.2 — the scroll wrapper plus alt table gives the same legibility at lower maintenance cost. |
| D3 | blocking | **Accepted** | Hues reserved for site ownership on every figure: 2.1 marks are ink dots/rings with marigold only on India sites; 2.2 flat rectangles with a marigold left rule for India sites; 3.1/3.2 no hue; 4.1 marks in ink with hue only on the owner pill; 5.1 two-category encoding (execution = ink tints, ownership = marigold, justified as India-site ownership); 5.2 ink bars. |
| D4 | major | **Accepted** | Fig 4.3 bars as soft fills with a solid top rule and ink text; overlap as an interleaved `<pattern>` of the two hues; wrap-around stub labelled. |
| D5 | major | **Accepted** | Paper halo via `paint-order` on all figure text classes; edges re-routed around labels; figures renumbered. |
| D6 | major | **Accepted** | Fig 2.2 pills replaced by flat rectangles; Sky/Peacock text on two lines. |
| D7 | minor | **Accepted** | Fig 1.3 edges orthogonal; marigold only on the QoE path. |
| D8 | minor | **Accepted** | Fig 1.2 single legend; phase names in the header row; phase 0 labelled in the row gutter; chart aligned to x=0. |
| D9 | minor | **Accepted** | Fig 4.1 legend left, footnote as a second ≤ 66ch line. |
| D10 | minor | **Accepted** | Fig 2.1 widened, 3-level stagger with leader ticks. |
| D11 | minor | **Accepted** | Plain-sentence titles on all figures. |
| D12 | blocking | **Accepted** | Rail is now float-into-padding (Tufte pattern); `.wide` clears and spans; no rail takes a row. |
| D13 | blocking | **Accepted** | `.rank li > * { grid-column: 2 }` and the number spans rows. |
| D14 | major | **Accepted** | Tagline hidden ≤ 1500px; tracking .06em; padding .45rem; verified all seven items fit at 1440. |
| D15 | major | **Modified** | ≤ 900px the nav shows section numbers with only the current section's name — the plan's own navigation grammar — instead of a details menu. |
| D16 | major | **Accepted** | One right edge: `.page`, header and footer capped at 72rem; wide elements span the reading column plus rail. |
| D17 | major | **Accepted** | Footer inner padded with the same gutter. |
| D18 | minor | **Accepted** | `.k` right-aligned with `margin-left: auto`. |
| D19 | minor | **Accepted** | Running numbers injected into every h2 by the build, and the TOC generated from the same list so they cannot drift. |
| D20 | pass | — | Italic display voice added: one `.pull` quotation per page (index: Target). |
| D21 | major | **Accepted** | Build collapses adjacent citations into sorted, deduplicated runs with ranges ("10–15"); digits in ink-2, not blue. |
| D22 | minor | **Accepted** | `--ink-3` darkened to #68726E (light); `.judgment .label` and `.rank .when` in ink-2 with a marigold rule. |
| D23 | pass | — | — |
| D24 | blocking | **Modified** | `documented` is **not** made invisible: the brief requires a visible tag on every case-study claim, and an unmarked default is indistinguishable from an untagged claim. Instead all inline chips are glyph-first, unfilled annotations in ink-3/ink-2 (● documented, ◐ inferred, ○ folklore, ◆ judgment), which removes the solid blocks and the white bars in dark mode; full chips remain in tables, keys and the Sources list. |
| D25 | pass | **Modified** | `aria-describedby` on the citation link while its preview is open is added in `site.js` in cycle 2 (deferred; no reader-facing regression). |
| D26 | major | **Accepted** | `overflow-wrap: anywhere` on source-list children; `overflow-x: clip` on main. |
| D27 | minor | **Accepted** | Page-head padding reduced ≤ 640px. |
| D28 | pass | **Accepted** | Font stylesheet preloaded; budget note added to the plan (the two long pages are justified and gzip < 32KB). |
| D29 | major | **Modified** | Items 1, 2, 5, 6, 7, 8 applied (rail numerals, flat rectangles, inline Fig 5.2, running numbers, citation runs, pull quotes). Item 3 handled per D24. Item 4 — removing the per-page key/TOC — **rejected**: the key is what makes the tags interpretable on every page a reader may land on, and the TOC is now generated and numbered. Fig 1.1 is not bled to full width: the page's single right edge (D16) is the stronger rule. |
| D30 | minor | **Accepted** | Pager top rule 3px to pair with the answer block. |
| D31 | minor | **Accepted** | En-dash markers on unclassed lists. |
| D32 | minor | **Accepted** | `.judgment` is a left-rule block, no fill. |
| D33 | minor | **Accepted** | Fig 5.1 two-category encoding with hatching. |
| D34 | minor | **Accepted** | "Analysts report to". |

## Items carried to cycle 2

- B4: confirm the McKinsey article page opens in a browser (automated clients time out).
- D25: `aria-describedby` on citation previews.
- Re-verify every figure at 390px after the size bump and the scroll wrappers (design critic).
- Re-check the case-studies and foundations word counts against the editor's targets.
