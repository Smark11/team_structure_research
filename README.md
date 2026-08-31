# team_structure_research

A decision-support site, and the complete research record behind it, on one question: **what charter should a new India engineering site have inside a ~140-person data organization at a large streaming/media company — full domain ownership, platform/capability ownership, a graduating extension, or a hybrid — and what does the answer do to the rest of the org?**

The published site (GitHub Pages, from `main:/docs`) is genericized: it never names the company. The full-context memo lives only in this repo, at [`decision-memo.md`](decision-memo.md).

## The answer, in one sentence

Charter the India site as the accountable owner of whole platform components — telemetry ingestion and the experimentation engine first, data-quality and contracts tooling next — and of one domain, quality of experience, with sessionization and the metrics catalog staying central; graduate a second domain (fraud and paid sharing, or ads measurement) on a criteria-gated decision; and keep commerce, experimentation analysis, browse, search and conversion funnels anchored in the US.

## Ten findings the site rests on

1. Every company studied that runs data at scale keeps the platform central and puts the *people* near the domain; nobody runs per-domain metric definitions or per-domain A/B stacks, and the two public counter-examples (Spotify's squads hand-negotiating experiment buckets, Amazon finance's 25 databases) were fixed by building central platforms after the fact.
2. Remote engineering sites chartered as new hubs by a parent — Netflix Warsaw, Spotify London, Amazon Hyderabad, Prime Video Bengaluru, WBD India — hold capability charters, not data-domain ownership; the exceptions grew in over ~18 years (Google Zurich), were origin sites (Sky/Peacock), acquisitions (Spotify Boston), or home-market products (Hotstar).
3. Distance does not measurably degrade quality; diffuse ownership and coupled work do. Cross-site work items took ~2.5× as long at Lucent because more people were needed per item; Microsoft found no quality penalty for distributed components once ownership was site-level and tooling shared.
4. Diffuse ownership is the best-replicated defect predictor in the software-engineering literature (~86% precision on Windows Vista) — which is what a "graduating extension" is, structurally, during its extension phase.
5. The India-centre market picture is a snapshot, not a graduation rate: 56% of centres sit in Zinnov's two execution tiers. The two celebrated graduations (Target, Lowe's) took ten to twenty years and had product management and managers in India by the time ownership was theirs.
6. The India organizations that owned a consumer domain end-to-end (Hotstar, Google Pay) were India-first products with local P&L — no verified case exists of a global consumer domain handed to a new centre on day one and succeeding.
7. Every data reorg at the four legacy-media companies studied was triggered by a P&L question, never a data question, and the 2026 moves pulled product data platforms toward ad monetization — so the charter is designed to survive being re-homed.
8. Conversion economics: the vendor controls who is released; centres pay 25–40% over IT-services bands; AI/cloud roles run 18–25% attrition. On the assumed baseline the site costs $1.7–3.5M a year more than an MSA-offshore vendor mix — it is not cheaper; it is a different thing.
9. The plan transfers ownership by whole units on written gates, with the calendar phase-relative (a late start moves every later date), twelve tripwires with executable fallbacks, and a first-domain test that costs something to pass (the US decommissions its own QoE computation) and something to fail (the domain claim is withdrawn, costed).
10. Attribution is weak everywhere — no company publishes outcome data tying structure to results — so the recommendation rests on avoiding documented failure modes more than on copying documented successes.

## Repo map

| Path | What it is |
|---|---|
| `/docs` | The published site: seven hand-authored static pages, no framework, no build step needed to serve. 200 numbered citations resolving to a Sources page with evidence tags (documented / inferred / folklore) and access dates; judgment calls visibly labeled. |
| `/research` | The research record: five parallel research reports (`c1`–`c5`: streaming-native cases, legacy-media cases, the academic canon, a verified learning plan, India GCC evidence), `synthesis.md` (cross-cutting findings and tensions), `recommendation.md` (the memo, v3.1; v1–v2 in git history), `sources.json` (217 verified sources), `source-map.md`. |
| `/reviews` | Three full review cycles plus a verification round, four reviewers each (red team, fact-checker with URL sweeps, editor, design critic with rendered screenshots), every numbered critique answered item-by-item in `cycle-N-responses.md`; `final-report.md` tells the story. |
| `/decision-memo.md` | The full-context memo (repo only). |
| `/site-plan.md` | The site's information architecture and design system (two-hue ownership colour, Newsreader/Archivo/JetBrains Mono, reading column with marginalia rail). |
| `/tools` | Authoring-time build: `build.py` (wraps content fragments, numbers sources site-wide in citation order, collapses citation runs, sets smart quotes, generates the Sources page), `check-citations.py` (every paragraph and list item must carry a citation or a judgment label), the page template and component guide. |

## How it was built

Five research agents ran in parallel, each verifying every source by fetch before citing it (things that could not be verified are flagged, not cited — the reports carry explicit "could not verify" lists). A synthesis reconciled their disagreements — including a genuine three-way split on which domain India should own first — and a decision memo took positions with labeled judgment. The site was then designed and built, and put through review cycles in which a red-team VP attacked the recommendation, a fact-checker re-fetched sources and audited every claim's citation and evidence tag, an editor enforced one argument and a constants table across pages, and a design critic rendered every page at desktop and mobile in both themes. The memo was rewritten twice under that pressure (v1 → v2 → v3): the first domain narrowed, the schedule became phase-relative, the cost table was rebuilt from the vendor rate up, and the claim it could not defend — a graduation base rate — was retired. The full evolution is in `reviews/final-report.md`.

## Serving

GitHub Pages serves `main:/docs` as-is. Locally: `cd docs && python3 -m http.server` — there is no build step to serve; `tools/build.py` is authoring-time only.
