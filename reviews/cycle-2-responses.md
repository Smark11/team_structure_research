# Cycle 2 — responses to all four reviewers

**Date:** 2026-08-30. Every numbered item from `cycle-2-red-team.md` (A2-1–A2-24), `cycle-2-fact-check.md` (B2-1–B2-25), `cycle-2-editor.md` (C2-1–C2-34) and `cycle-2-design.md` (D2-1–D2-25) with its disposition. The recommendation moved from v2 to **v3** (`research/recommendation.md`); the site was rebuilt against it.

## What changed in the recommendation (v2 → v3)

1. **The calendar is phase-relative.** Every date is an offset from G0 (Gate 0 passes; target month 3, no later than 6) or G1 (the first quarter boundary after G0 + 6). The US QoE dissolution is announced at G1 − 3 and retention runs to G1 + 3, so a late Phase 1 can no longer leave a US team in notice for a transfer that has not happened. Two calendars are shown (A2-2, A2-18).
2. **Gate 0 no longer requires managers started**; it requires two engineering-manager searches open with shortlists, and Gate 1 requires both started. The Phase 1 arrangement (site head runs two teams through tech leads, span rule suspended) is now consistent with the gate. "Engineering manager" is defined; "second-line manager" is glossed where the India-centre literature is quoted (A2-1).
3. **The experimentation line moved**: India owns the runtime *and* the metric-definition schema with a change process and SLAs; the US analysis function files requests and keeps the semantic catalog and the review gate. Three quarterly changes are walked through on Applying It with hand-off counts; the gate measures P1 hours-to-resolve; the QoE team is the engine's on-site customer (A2-6, A2-3 for T4).
4. **QoE is scored under the decision rights it would have** (India decides definitions, engineering consulted → pass with consultation), and its test now bites: Gate 2 requires playback engineering to *decommission* its own QoE computation and at least three India-authored definition changes adopted; failure withdraws the domain claim at the next annual review and is costed. NBCU's "equally accountable" phrasing is cited as a case, not adopted as the template (A2-4).
5. **T4 and T6 fallbacks narrow instead of returning**; T6 explicitly refuses re-transfer to the duplicating team (A2-3).
6. **The cost table is rebuilt from the vendor rate up**: loaded conversion cost derived from bill rate, margin and premium; today's line as a range by contractor mix; backfill, wage inflation, retention (conversion and US QoE), double-running (with the T12 path) and severance added; the US offset shown as a scenario with an owner and a decision date; the CFO sentence rewritten to "+$1.5–3M a year before the offset; not cheaper than the vendor" (A2-7, A2-8, A2-9).
7. **A month-3 re-decision point**: if counsel clears fraud and the contractors sit in commerce, Phase 2 is fraud (A2-15). The 60-in-commerce sensitivity row has an else-branch (commerce-source ingestion as a component) and the 20-contractor row states the decision (a 15–20-person platform-only site) (A2-10, A2-11).
8. **Ads measurement**: the fifth criterion — robustness to a P&L-driven re-homing — is named and applied to all four candidates (QoE scores worst); the precondition that ad-tech first transfers the data into this org is stated (A2-16).
9. **Phase 0 plan** with owners, lead times and the critical path; the wanted list is frozen at site head + 30 days or month 4 with the head holding a veto (A2-17, A2-24).
10. **A stated transfer mechanism** for QoE (facilitating mode G1 − 3 to G1 + 3) as a named exception to the half-ownership rule; DQ tooling is a transfer of the US team's existing checks plus a build-out, with the India ingestion and QoE teams as first customers (A2-18, A2-19).
11. **"Not an extension" is qualified** ("after Gate 0"); Phase 1 is named as execution under US standards with the unilateral-decisions list shown (A2-20).
12. Five new hubs in the constants; the graduation clock added to the constants; QoE team 8–10 with two analytics partner seats (C2-6, C2-7, C2-8).

---

## Reviewer A — red team (cycle 2)

| # | Sev | Disposition | Note |
|---|---|---|---|
| A2-1 | blocking | **Accepted (option b)** | Gate 0 = searches with shortlists; Gate 1 = both started; the player-coach period stated; vocabulary defined. |
| A2-2 | blocking | **Accepted** | Phase-relative schedule everywhere (memo, index phases, Fig 1.2 axis "months after Gate 0" with two calendar rows, Applying It, Learning Plan). Two-quarter minimum stated in G1's definition. |
| A2-3 | blocking | **Accepted** | T4: facilitating quarter, then fold assignment/exposure into telemetry and return computation to a re-formed US team on a six-month hire, interim named. T6: dissolve the duplicate; re-transfer to the duplicating team excluded. |
| A2-4 | blocking | **Accepted (option b)** | Domain kept; decision right India's, US consulted; Test 1 rescored on that basis and said so; Gate 2 = decommissioning + three adopted changes; failure named and costed; "equally accountable" dropped as the template. The lead's role is designed so both outcomes are real jobs (platform product owner if the bet fails). |
| A2-5 | major | **Accepted** | Ingestion owns raw events to the landing schema; QoE owns downstream. In the memo, index 1.2e and the ownership table. |
| A2-6 | blocking | **Accepted** | Line redrawn (India owns schema and runtime; US files requests); three walk-throughs on Applying It; gate measures P1 hours; on-site customer named. |
| A2-7 | major | **Accepted** | Conversion cost derived from the vendor rate; today's line as a range by mix; the direction of the step-up stated for both mixes. |
| A2-8 | major | **Accepted** | Offset is a scenario with owner (data executive) and date (G1); base case leads with +$1.5–3M; "roughly the same as today" removed from the two-minute section. |
| A2-9 | major | **Accepted** | Backfill, wage inflation, retention (both), double-running, severance, site-head LTI added; year-3 delta restated. |
| A2-10 | major | **Accepted** | Else-branch: commerce-source ingestion as a component when legal fails; costs stated; "usually sit" deleted. |
| A2-11 | major | **Accepted** | 20-contractor row states the decision (platform-only 15–20; vendor-stay alternative); "robust" reworded. |
| A2-12 | major | **Accepted** | T9: enforcer above the sponsor signs the cost line; 60-day continue/freeze/unwind decision; phase-relative announcements; "base case is a platform site" stated. |
| A2-13 | major | **Accepted** | T11: announcement withdrawn and US team re-confirmed if the freeze lands in the window (costed); sub-five teams get a facilitating engineer. |
| A2-14 | major | **Accepted** | T12: named negotiators from month 0; +12–18 months; double-running and recruiting in the one-time table; runbook contingency budgeted. |
| A2-15 | major | **Accepted** | Month-3 re-decision point in Gate 0; fraud scored under India-decides-within-bands rights; QoE-first justified on the assumed baseline only, and said so. |
| A2-16 | major | **Accepted** | Fifth criterion named and applied to all four; ads-ownership precondition stated; "leverage" removed as a selection reason. |
| A2-17 | major | **Accepted** | Phase 0 plan table with owners, lead times and critical path; Gate 0 does not wait for the managers; wanted-list freeze at head + 30 days or month 4. |
| A2-18 | major | **Accepted** | Facilitating-mode window as a stated exception; retention in the cost table; announcement tied to G1. |
| A2-19 | major | **Accepted** | Baseline assumption: the US runs basic checks today; Phase 2(c) is a transfer plus build-out; the US engineers' seats in the offset scenario; on-site customers named. |
| A2-20 | major | **Accepted** | "After Gate 0" qualifier; "decides unilaterally in Phase 1" column; Phase 1 named as execution under US standards. |
| A2-21 | minor | **Accepted** | 27% removed from the two-minute section; once on the index drill-down, once on Charter Evidence. |
| A2-22 | minor | **Accepted** | Cohort gates in heads (≥ 10 of 16; ≤ 2 departures); the 50–60% gap closed (T2 fires below 60% by month 6). |
| A2-23 | minor | **Accepted** | Successor named at G1 (interim), confirmed at Gate 3. |
| A2-24 | minor | **Accepted** | Decision-log field owned by the US platform director in Phase 0 with a written definition; gate in relative form ("halved between the G0 + 3 and G0 + 6 readings"). |

## Reviewer B — fact-check (cycle 2)

| # | Sev | Disposition | Note |
|---|---|---|---|
| B2-1 | blocking | **Accepted** | Target card quotation corrected to "resting with". |
| B2-2 | blocking | **Accepted** | Applying It Larson sentence corrected (6–8 people-focused from the post; 3–5 hands-on from the book). |
| B2-3 | blocking | **Accepted** | `data-cite="none"` on the dropped list; the audit script now covers `<li>` items too, so the exemption is deliberate. |
| B2-4 | blocking | **Accepted** | 200k/110k pair deleted; the 510,000+ / 63% / 54% statement cited to HRKatha and the EY release. |
| B2-5 | blocking | **Accepted** | Retrospective described accurately; DOI in the source note. |
| B2-6 | blocking | **Accepted** | Citi row rewritten to the sourced facts. |
| B2-7 | blocking | **Accepted** | No citations and no documented chip on the summary of the site's own tracks; C3-42 kept on the canon clause only. |
| B2-8 | major | **Accepted** | New tertiary source (C2-51, Wikipedia WBD) added to sources.json and cited for the two 2022 rows; recorded in source-map.md. |
| B2-9 | major | **Accepted** | Thoughtworks retrospective characterized by its named failure modes; the "thick central platform" conclusion labelled judgment. |
| B2-10 | major | **Accepted** | T11 rewritten to "cut headcount" with the four companies' sources. |
| B2-11 | major | **Accepted** | Disney/Paramount sentence softened to what the sources say. |
| B2-12 | major | **Accepted** | Hotstar full-stack claim and Sky origin-site claim tagged inferred; index "Why this shape" run keeps `documented` for the five hubs and describes Sky as "where Peacock's platform came from" (C2-28's AWS study supports joint NBCU/Sky teams building it). |
| B2-13 | major | **Accepted** | Chip split on the index: 2.5× documented, time-zone finding inferred. |
| B2-14 | major | **Accepted** | Graduation clock standardized to ten to twenty years; card "over roughly two decades". |
| B2-15 | major | **Accepted** | Explicit `qualifier` field in sources.json; Disney Streaming blog no qualifier; Working Backwards "retail page only"; Storyboard18 "secondary". |
| B2-16 | minor | **Accepted** | Zurich sentence rewritten. |
| B2-17 | minor | **Accepted** | Alt-table row reads "Global Networks (later Discovery Global)". |
| B2-18 | minor | **Accepted** | C5-3 added. |
| B2-19 | minor | **Accepted** | Caveat cell rewritten; cites HRKatha only. |
| B2-20 | minor | **Accepted** | Row label "AI / cloud roles (proxy for data roles)". |
| B2-21 | minor | **Accepted** | "the minimal-collaboration interaction mode Team Topologies calls X-as-a-service". |
| B2-22 | minor | **Accepted** | C3-9 added to Fig 3.1's caption. |
| B2-23 | minor | **Accepted** | The build now recomputes cited/uncited on every run; s-107 falls into the consulted list automatically after the case-studies cut. |
| B2-24 | minor | **Accepted** | McKinsey note records the typo and the browser verification. |
| B2-25 | minor | **Accepted** | Forrester 2011 row split: models documented, "no documented follow-up" inferred. |

## Reviewer C — editor (cycle 2)

| # | Sev | Disposition | Note |
|---|---|---|---|
| C2-1 | blocking | **Accepted** | 27% out of the two-minute section. |
| C2-2 | blocking | **Accepted** | Zinnov quotation in full only on Charter Evidence; index 1.2e carries the clause. |
| C2-3 | blocking | **Accepted** | Charter Evidence §5.4 reduced to Fig 5.2 plus the one accepted sentence. |
| C2-4 | blocking | **Accepted** | Charter Evidence Phase 3 wording matches the memo (ads measurement or ML-platform expansion; neither a fallback). |
| C2-5 | blocking | **Accepted** | Foundations pointer names both candidates and the legal review. |
| C2-6 | blocking | **Accepted** | Five new hubs, four different cases — in the constants, the memo, the index and Case Studies. |
| C2-7 | blocking | **Accepted** | QoE team 8–10 with two analytics partner seats everywhere. |
| C2-8 | blocking | **Accepted** | Graduation clock in the constants ("ten to twenty years"); every page updated. |
| C2-9 | blocking | **Accepted** | Learning Plan Primer entry: "a site that costs more than the vendor did". |
| C2-10 | major | **Accepted** | Cross-references corrected (§4.7, §2.1, §1.1–1.3). |
| C2-11 | major | **Accepted** | Fig 1.3: experimentation analysis exits at "many deciders"; the question-3 "no" exit says no current unit exits there. |
| C2-12 | major | **Accepted** | Answer block carries "while sessionization and the metrics catalog stay central" and names both second-domain candidates. |
| C2-13 | major | **Accepted** | Every self-referential "first draft / earlier version / and we say so" line removed from the site; the memo's status line carries the version history. |
| C2-14 | minor | **Accepted** | "does not pretend" cut everywhere; Applying It keeps one plain sentence ("The site is not cheaper than the vendor; it is a different thing"). |
| C2-15 | minor | **Accepted** | "leverage", "hedge", "landing", "load-bearing" removed from the site (the memo keeps "hedge" in §5B's heading, as the reviewer allowed). |
| C2-16 | minor | **Accepted** | "actually" removed (the one inside Kniberg's quotation stays). |
| C2-17 | minor | **Accepted** | "this memo" on index and Applying It, "this site" on evidence pages, no "we" outside quotations. |
| C2-18 | major | **Modified** | Two-minute section restructured per the proposed text with v3 content: the cost sentence is the v3 one (+$1.5–3M, not "roughly the same"), the Sky clause is worded to what the sources support, and a month-3 re-decision clause is added because the red team required it. ≈ 430 prose words plus the rail and the pull quote. |
| C2-19 | major | **Accepted** | §1.6 folded into §1.2: each drill-down opens with the strongest case, then the rebuttal; the hybrid steelman is 1.2d; whole-components and QoE are 1.2e and 1.2f. |
| C2-20 | major | **Accepted** | 1.2f post-table prose reduced to the three-sentence verdict plus the re-decision clause; T5 and the Disney/Paramount sentence removed from it. |
| C2-21 | major | **Accepted** | Applying It judgment box opens at the verdict. |
| C2-22 | major | **Accepted** | Fig 4.1/4.2/4.3 descriptions are one sentence; the alt tables are the accessible alternative. |
| C2-23 | major | **Accepted** | Applying It §4.5 span/floor paragraphs reduced to one sentence with pointers. |
| C2-24 | minor | **Accepted** | "Not fitted" once (the rail); Galbraith paragraph reduced to its last clause. |
| C2-25 | major | **Accepted** | §4.6 reduced to three short paragraphs with pointers. |
| C2-26 | minor | **Accepted** | "12h" rail cut. |
| C2-27 | minor | **Accepted** | Cost intro reduced to the "finance replaces every number" sentence. |
| C2-28 | minor | **Accepted** | Stancil, Dev Interrupted and the milestone row rewritten. |
| C2-29 | major | **Accepted** | Fig 1.2 caption names the two written exceptions. |
| C2-30 | major | **Accepted in part** | Applying It lands at 6,489 by the build's count, not ≈5,000: the cut list was applied in full, but the red team's mandated additions (Phase 0 plan table, three walk-throughs, unilateral-decisions column, the fuller cost and sensitivity tables, the fifth criterion) add ≈1,200 words, twice what the target assumed. The page is the working-out; the memo chose completeness over the target. Case Studies prose now ≈ 5,000 words excluding figure tables (page count 6,979 including two accessibility tables); Foundations 4,483 — the agent stopped short of the last ~200 words rather than drop cited claims, which is the right call. |
| C2-31 | minor | **Accepted** | "Follows its market's P&L" kept on index 1.2a and the Charter Evidence card only. |
| C2-32 | minor | **Accepted** | Index Phase 2 points to Applying It §4.3 for the decision-rights table. |
| C2-33 | minor | **Accepted** | Mega-centre-heads clause removed from index Phase 0. |
| C2-34 | pass | — | Genericization: pass. |

## Reviewer D — design critic (cycle 2)

| # | Sev | Disposition | Note |
|---|---|---|---|
| D2-1 | blocking | **Accepted** | Figs 1.1, 1.2, 1.3 wrapped in `figure.wide.scroll` with the cue; alt tables on 1.1 (fourteen units) and 1.3 (four questions); the phases ledger is 1.2's alternative. |
| D2-2 | blocking | **Accepted** | ≤ 640px: numbers only, `flex-start`, `overflow: visible`; verified at 390 (all seven numbers visible). |
| D2-3 | blocking | **Accepted** | Collapse regex rewritten to leave trailing whitespace; regression check `</sup>[A-Za-z"(]` = 0 on every page. |
| D2-4 | blocking | **Accepted** | Number-only breakpoint at 1140px; hidden-scrollbar rules deleted. |
| D2-5 | major | **Accepted** | All eight foundations rails moved to directly after their section's h2; `clear: both` removed from h2. |
| D2-6 | major | **Accepted** | Full-chip rules restored for `.src`, `td` and `.tag-key` with `::before` suppressed. |
| D2-7 | major | **Accepted** | The build enforces one order: period, citation run, space, chip. |
| D2-8 | major | **Accepted** | `min-width: 800px`; Fig 5.1 wrapped in the scroll figure. |
| D2-9 | major | **Accepted** | Dark `--ink-3` #8A938F; inline judgment chip text in ink-2 with the marigold glyph; glyphs at 11px. |
| D2-10 | major | **Accepted** | Smart-quotes pass in the build on text nodes (skipping code); `hanging-punctuation: first` on `.pull` and `blockquote`. |
| D2-11 | major | **Accepted** | Attribution reduced to "Target's India president, 2026"; the hedge moved into the prose; `.pull` restyled with the marigold opening mark and no rule. One pull per essay page is deferred to cycle 3 for Case Studies and Foundations. |
| D2-12 | major | **Accepted** | SVG data-URI favicon (the marigold square). |
| D2-13 | minor | **Accepted** | Both overrunning labels shortened. |
| D2-14 | minor | **Accepted** | Qualifier shown once (explicit field; note text no longer duplicated by the derivation). |
| D2-15 | minor | **Accepted** | Sources h2s numbered 7.1 and 7.2. |
| D2-16 | minor | **Deferred** | Fig 5.2 into the rail — a rail-bars component now exists in the CSS; applying it on Charter Evidence is queued for cycle 3 with the other figure polish. |
| D2-17 | minor | **Accepted** | h2 fluid (`clamp`). |
| D2-18 | minor | **Accepted** | Fig 1.3 legend line: solid = US owns · tint = never transfers · marigold = the QoE path. |
| D2-19 | minor | **Accepted** | Tag key shows the inline glyph next to each chip. |
| D2-20 | minor | **Accepted** | "Section N of 7 · Sources accessed" replaces the word count. |
| D2-21 | minor | **Deferred** | Fig 3.1 alt table — cycle 3. |
| D2-22 | minor | **Accepted in part** | Fig 1.1's key moved inside the SVG; captions on the index are ≤ 3 lines. Other pages' captions are trimmed where the agents touched them; a full pass is cycle 3. |
| D2-23 | minor | **Accepted** | Citation padding removed; comma margin .1em. |
| D2-24 | minor | **Accepted** | `figure + h2` margin rule. |
| D2-25 | pass | — | Keyboard note recorded; `aria-describedby` present. |

## Carried to cycle 3

- One pull quote on Case Studies and Foundations (D2-11); Fig 5.2 into the rail (D2-16); Fig 3.1 alt table (D2-21); caption length pass on pages 2–5 (D2-22).
- Case Studies and Foundations remaining word cuts (C2-30) if the editor still wants them after the cycle-2 additions.
- Re-verify every v3 constant across pages (the schedule is now phase-relative on every page; the Learning Plan's calendar states the happy path).
