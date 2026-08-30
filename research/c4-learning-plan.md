# C4 — Ranked, Verified Learning Plan for the Data-Org Redesign and India Site Decision

**Audience:** senior data executive, ~140-person data org inside a large media/streaming company, redesigning the org and standing up an India engineering site (contractor-to-FTE conversion; deciding whether the site owns domains, owns platform capabilities, or graduates from extension to ownership).

**Verification standard:** every book, blog, podcast, and episode below was checked on 2026-08-29 against a publisher page, author site, podcast feed page, or episode page. Anything that could not be confirmed is listed in "Dropped / could not verify" at the end, not silently included.

**Assumed milestones (used throughout):**

| Milestone | Approximate month |
|---|---|
| Charter decision (what the India site is *for*; domain vs platform vs extension) | Month 2 |
| First India leadership hire (site lead / senior EM) | Month 4 |
| Contractor-to-FTE conversion wave and first team handover | Month 6 |
| First graduation review (extension → ownership) | Month 9 |
| Org-wide review | Month 12 |

---

## Section 1 — Top 10 books, ranked

The ranking is for *this* decision, not for general management self-improvement. Books that are excellent but at the wrong altitude (first-line management, IC career) are ranked low or dropped.

### 1. *Team Topologies*, 2nd edition — Matthew Skelton & Manuel Pais (IT Revolution, 2025) [C4-1]

**Essential. Read in month 1, before any org chart is drawn.** This is the only book on the list with a vocabulary precise enough to settle the India question. "Does the site own domains, platform capabilities, or is it an extension?" translates directly into: are India teams *stream-aligned* (domain-owning), *platform* (self-serve capability owners), or *enabling*? The book's interaction modes (collaboration / X-as-a-service / facilitating) are exactly the levers you will use to design a graduation path: a team that starts in *collaboration* mode with a US team and moves to owning an *X-as-a-service* boundary has, by definition, graduated. The second edition (September 2025) adds cross-industry case studies; buy that one, not the 2019 first edition (ISBN 9781942788812). Read it before *An Elegant Puzzle* so Larson's sizing heuristics land inside a structural frame. The Conway's Law chapter should be read alongside Fowler's bliki entry [C4-15].

### 2. *An Elegant Puzzle: Systems of Engineering Management* — Will Larson (Stripe Press, 2019) [C4-2]

**Essential. Read in month 1, alongside Team Topologies.** The "sizing teams" and "staying on the path to high-performing teams" chapters are the most practical text available on how many people a team and a manager should carry, when to split, and why moving people between teams during a reorg destroys more than it creates. Larson's rule that you should fix one team at a time rather than spreading thin is the single most useful check against a "big bang" India transition. The chapter on running a reorg ("organizational design" section) is short and blunt and should be reread at month 8 before the graduation review. Skip the career-ladder appendices for this purpose.

### 3. *The Culture Map: Breaking Through the Invisible Boundaries of Global Business* — Erin Meyer (PublicAffairs, 2014) [C4-3]

**Essential for the India site. Read in month 3, before the first India leadership hire interview loop.** Most US–India engineering failures are not skill failures; they are *scaling* failures on Meyer's eight dimensions, especially communicating (low- vs high-context), evaluating (direct vs indirect negative feedback), leading (egalitarian vs hierarchical), and deciding (consensual vs top-down). The reason this matters for the *structure* decision: an "extension" model where India teams take tickets from US leads bakes in the hierarchical/indirect pattern that later makes ownership graduation feel like a jump rather than a step. Read it to design interview questions for the site lead (you want someone who can bridge both maps) and to set explicit feedback and decision norms in the charter. Overrated part: the anecdotes about French vs. Dutch meetings; skim those.

### 4. *The Engineering Executive's Primer: Impactful Technical Leadership* — Will Larson (O'Reilly, 2024) [C4-4]

**Essential. Read in months 1–2, before the charter is finalized.** Where *An Elegant Puzzle* is about teams, the *Primer* is about the executive's own operating system: writing an engineering strategy, running planning, measuring an engineering org, and (critically) managing your relationship with the CEO/CFO who will ask why India headcount is cheaper on paper but not yet faster in practice. The chapters on "Writing an engineering strategy" and "Measuring engineering organizations" give you the structure for the charter document and the graduation criteria respectively. Drafts of most chapters remain on lethain.com [C4-11], so you can preview before buying.

### 5. *Designing Organizations: Strategy, Structure, and Process at the Business Unit and Enterprise Levels*, 3rd edition — Jay R. Galbraith (Jossey-Bass/Wiley, 2014) [C4-5]

**Essential, and the one your peers in the business will recognize. Read in month 2, before the charter decision.** Galbraith's Star Model (strategy, structure, processes, rewards, people) is the frame a CFO, CHRO, or COO expects. Its most useful lesson for a data org is that structure is the *least* powerful lever; lateral processes (how domains and platforms coordinate) and reward systems (are India teams measured on tickets closed or on outcomes owned?) decide whether a structure works. Use it to write the two or three pages of the charter that the non-technical executives will read. It is dry and dated in examples; read the Star Model chapters and the chapters on lateral processes and matrix organizations, skip the rest.

### 6. *Scaling People: Tactics for Management and Company Building* — Claire Hughes Johnson (Stripe Press, 2023) [C4-6]

**Read in months 3–4, before the India leadership hire and the contractor-to-FTE conversion.** This is the operational manual for the people side of the transition: hiring and onboarding at scale, writing operating principles, running performance and compensation cycles, and building the "operating cadence" a new site needs so it is not dependent on a US manager's calendar. Her material on foundational documents (mission, principles, operating cadence) is exactly what a new site charter needs so that autonomy is *designed*, not hoped for. Hughes Johnson ran Stripe's international expansion, so the advice translates. It is long; the hiring, onboarding, and operating-cadence sections are the load-bearing parts for this decision.

### 7. *Data Mesh: Delivering Data-Driven Value at Scale* — Zhamak Dehghani (O'Reilly, 2022) [C4-7]

**Read in month 2, with skepticism, before deciding domain ownership.** You do not need to adopt data mesh to benefit from its vocabulary: *domain ownership*, *data as a product*, *self-serve platform*, and *federated computational governance* map cleanly onto Team Topologies' stream-aligned / platform / enabling teams. The book's real contribution to the India decision is its argument that domain ownership only works when the platform makes ownership cheap, which is a strong argument for giving India *platform capabilities* first and *domains* second. What is overrated: the governance chapters are aspirational and the implementation guidance is thin. What is essential: Part II (principles) and the chapter on organizing teams. Do not let anyone use this book to justify a full decentralization of a 140-person org in year one.

### 8. *The Art of Action: How Leaders Close the Gaps Between Plans, Actions, and Results* — Stephen Bungay (Nicholas Brealey, 2011; 10th-anniversary edition 2022) [C4-8]

**Read in months 5–6, before the first team handover.** Bungay's "mission command" (Auftragstaktik) is the best available model for what a *graduated* India team should look like: leaders state intent and constraints, teams decide how. The three gaps (knowledge, alignment, effects) explain most remote-site dysfunction better than time-zone arguments do. Use it to write the "briefing" for the first handover: what outcome, what boundaries, what you will and will not ask them to escalate. Its military history is the reason people skip it; do not, it is the argument. This book is why "extension → ownership" should be framed as widening the scope of intent given, not as a change in reporting lines.

### 9. *Accelerate: The Science of Lean Software and DevOps* — Nicole Forsgren, Jez Humble & Gene Kim (IT Revolution, 2018) [C4-9]

**Read in months 6–7, before you write the graduation criteria.** Overrated as a general management book (it is a research summary), but essential for one purpose: it gives you defensible, outcome-based delivery metrics (lead time, deployment frequency, change failure rate, time to restore) that do not depend on where a team sits. A graduation review that uses these plus a data-quality/SLA measure is harder to game and harder for a US team to block on "they're not ready yet." Also read the chapter on organizational culture (Westrum typology); the "generative vs bureaucratic" distinction is a fair description of the difference between an owning site and a ticket-taking one. Skip the statistical methodology appendix.

### 10. *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* — Ron Kohavi, Diane Tang & Ya Xu (Cambridge University Press, 2020) [C4-10]

**Read in month 8, before the graduation review, if experimentation is a candidate platform capability for India.** In a streaming business, the experimentation platform is one of the most likely "platform capability" candidates to hand to a new site: well-bounded, high-leverage, mostly independent of content-domain context. Kohavi's book makes the case that trustworthy experimentation is a *platform* discipline (metrics governance, guardrails, institutional memory), not a set of analysts, which is the argument you need to make it an India-owned capability rather than a service desk. Part I is written for executives and takes an evening. Only necessary if experimentation is in scope; otherwise it drops to optional.

### Verified but not in the top 10 (and why)

- *High Output Management* — Andrew S. Grove (Vintage, 1995) [C4-27]. Still the best primer on managerial leverage and "task-relevant maturity," which is a useful lens on graduation; but it is at first/second-line altitude for this decision. Optional, month 10.
- *Team of Teams* — Stanley McChrystal et al. (Portfolio, 2015) [C4-28]. Good on shared consciousness across a distributed organization; weak on how to structure it. Bungay covers the same ground with more rigor.
- *Structure in Fives: Designing Effective Organizations* — Henry Mintzberg (Prentice Hall, 1983) [C4-29]. Verified and foundational, but Galbraith gives you the same executive vocabulary with less 1980s baggage. Overrated for practitioners.
- *Fundamentals of Data Engineering* — Joe Reis & Matt Housley (O'Reilly, 2022) [C4-30]. Verified and good. Not for you; it is the book to hand the India site lead and every converted FTE in month 5 as a shared lifecycle vocabulary.

---

## Section 2 — Blogs and newsletters, ranked (12)

All checked live on 2026-08-29. "Read first" is the specific entry point.

### 1. Will Larson — *Irrational Exuberance* (lethain.com) [C4-11]
Active (posts dated August 2026: "Roadmap decisions rather than dates," "Middle management roles are also a trap"). The most consistently useful writing on engineering strategy, org sizing, and executive operation. **Read first:** the "executive" tag (draft chapters of the *Primer*), then his posts on sizing teams and on running reorgs.

### 2. Team Topologies news/blog (teamtopologies.com/news) [C4-12]
Active (August 2026 post on agentic-AI readiness). It is a vendor blog, so filter the consulting pitches; the value is the case studies and the ongoing refinement of team types and interaction modes. **Read first:** the book page and the case-study posts; the 2026 AI-readiness posts are less relevant to your decision than the earlier material on platform teams and cognitive load.

### 3. Gergely Orosz — *The Pragmatic Engineer* (newsletter.pragmaticengineer.com) [C4-13]
Active (weekly, 1.1M+ subscribers; July 2026 AMA on engineering organizations). Best for "how do real companies actually structure this" reporting rather than theory. **Read first:** search the archive for platform-teams and reorg pieces; the deep dives on how specific companies run engineering are worth the paid tier during a redesign year.

### 4. Camille Fournier — *Elided Branches* (elidedbranches.com) [C4-14]
Active (May 2026, "Guidelines for Respectful Use of AI"; November 2025, "Revisiting Manager READMEs"; June 2025, "Dude, Where's My Strategy?"). Her Medium mirror (skamille.medium.com) exists but blocks automated fetches, so cite the primary site. Fournier is the sharpest available writer on platform engineering as an organizational (not technical) problem. **Read first:** "Dude, Where's My Strategy?" then her platform-engineering posts.

### 5. Martin Fowler — bliki: *Conway's Law* (martinfowler.com/bliki/ConwaysLaw.html) [C4-15]
Updated October 2022; still the canonical short statement of the Inverse Conway Maneuver. Not a newsletter, a reference page. **Read first:** the page itself, ten minutes, in month 1; it is the intellectual basis for the claim that "extension teams" produce extension-shaped architecture.

### 6. Chad Sanderson — *Data Products* (dataproducts.substack.com) [C4-16]
Active (July 2026, "The Shift Left Manifesto v2"). The most practical writing on data contracts and producer-side ownership, which is the mechanism by which a domain-owning team in India can be trusted by a consuming team in the US. **Read first:** "The Rise of Data Contracts," then "Shift Left Manifesto v2."

### 7. Benn Stancil — *benn.substack* (benn.substack.com) [C4-17]
Active (weekly; July 2026 "Be a winner, or join one?"). Increasingly about AI and the industry rather than data-team design, which is why it ranks here and not higher. Still the best skeptic on data-org orthodoxy. **Read first:** "Disband the analytics team" (the argument against a standalone central analytics function) before you decide what stays central.

### 8. Netflix Technology Blog (netflixtechblog.com) [C4-18]
Active (August 2026, "A Tale of Two Flink Autoscalers"; May 2026, "Data Projects: Managing Data Assets at Netflix Scale"). Direct-competitor relevance: how a streaming company draws the platform/domain line for data. **Read first:** "Data Projects: Managing Data Assets at Netflix Scale" (May 2026) for how a platform team defines ownership units.

### 9. Tristan Handy — *The Analytics Engineering Roundup* (roundup.getdbt.com) [C4-19]
Active (weekly roundups through August 2026; also hosts the podcast). Curated links plus editorial; the roundups on "data teams in the AI era" are the relevant thread. **Read first:** the podcast feed (Section 3) rather than the roundups.

### 10. Charity Majors — *charity.wtf* (charity.wtf) [C4-20]
Active on Substack (posts through 2026; the site's older WordPress archive URLs 404). Most relevant to a data org for her writing on the engineer/manager pendulum and on why management is not a promotion, which matters when you convert senior contractors and must decide who becomes a lead. **Read first:** "The Engineer/Manager Pendulum" (2017, still cited weekly).

### 11. Spotify Engineering (engineering.atspotify.com) [C4-21]
Active (August 2026, "When Can LLMs Replace Humans in A/B Tests?"; July 2026 data-lake indexing post). Relevant for experimentation-platform and data-lake ownership patterns in a media company. The "Spotify model" org posts are old and overrated; ignore them. **Read first:** the 2026 experimentation and data-lake posts.

### 12. LeadDev (leaddev.com) [C4-22]
Active (2025–2026 articles: "How to redesign a broken delivery flow," "Engineering leadership in 2025"). Broad, sometimes shallow, but reliable for practitioner accounts of reorgs and managing managers. The site's podcast page 404s (see Dropped). **Read first:** the "reporting" section's 2025 engineering-leadership pieces.

### Flagged, not ranked
- **Locally Optimistic** (locallyoptimistic.com) [C4-23] — still up, but the most recent post is August 2025. Its archive on data-team structure is good; treat it as a reference, not a subscription.
- **Kohavi** — his current writing is on LinkedIn (not verifiable as a stable URL); the book's companion site experimentguide.com [C4-24] is live and lists his quarterly classes.

---

## Section 3 — Podcasts, ranked (9)

Each show verified live with 2024–2026 episodes; each episode URL fetched on 2026-08-29.

### 1. *Engineering Enablement* — DX (Abi Noda, Brian Houck, Justin Reock) (getdx.com/podcast) [C4-31]
The best show for this decision: short, research-anchored, and focused on org design and platform teams rather than tools.
- "Designing the AI-native engineering organization with 1Password, Microsoft and Atlassian" (June 2026) — how three orgs are restructuring teams and hiring. [C4-32]
- "Adopting the product operating model at Priceline" (Ep. 111, July 2026) — a project-to-product reorg driven by developer-experience data, with explicit discussion of handoffs and silos. The closest analogue to your graduation review. [C4-33]

### 2. *The Pragmatic Engineer Podcast* — Gergely Orosz (Apple Podcasts / newsletter.pragmaticengineer.com) [C4-34]
Weekly, long-form, with senior guests; high signal on how real orgs work.
- "The Pragmatic Engineer AMA" (July 8, 2026) — includes questions on engineering organizations and hiring. [C4-35]
- "Stop being skeptical about AI for development with Charity Majors" (August 12, 2026) — relevant to how you size teams post-2025 rather than to India directly. [C4-36]

### 3. *The Analytics Engineering Podcast* — Tristan Handy, dbt Labs (roundup.getdbt.com/s/the-analytics-engineering-podcast) [C4-37]
The only data-specific show on this list with current leadership content.
- "The scarce resource is consensus (Ian Macomber, Ramp)" (July 16, 2026) — the argument that when analysis is cheap, a data team's job is company-wide agreement; this reframes what a *central* team should still own. [C4-38]
- "Data lessons from inside Meta (Shridhar Iyer)" (July 30, 2026) — organizational changes required in a very large data org. [C4-39]

### 4. *Lenny's Podcast* — Lenny Rachitsky (lennysnewsletter.com/podcast) [C4-40]
Mostly product; three episodes are directly useful and all three guests are on the book list.
- "Lessons from scaling Stripe | Claire Hughes Johnson" (March 5, 2023). [C4-41]
- "The engineering mindset | Will Larson" (January 7, 2024). [C4-42]
- "The things engineers are desperate for PMs to understand | Camille Fournier" (September 15, 2024). [C4-43]

### 5. Team Topologies author episodes (two shows) [C4-44] [C4-45]
Not a single show, but the two most current long interviews with the authors, both post-second-edition thinking.
- Thoughtworks Technology Podcast, "Organizational design and Team Topologies after AI" (September 4, 2025). [C4-44]
- Software Engineering Radio 646, "Matthew Skelton on Team Topologies" (December 11, 2024) — when to adopt, keys to implementation, common mistakes. [C4-45]

### 6. *Data Engineering Podcast* — Tobias Macey (dataengineeringpodcast.com) [C4-46]
Active (E515, August 27, 2026), but recent episodes are tool- and AI-centric. The org-design episodes are older and still the best available on the specific question of data platform teams in large companies.
- "Building And Managing Data Teams And Data Platforms In Large Organizations With Ashish Mrig" (E257, January 23, 2022) — Wayfair's platform/team design. [C4-47]
- "Revisiting The Technical And Social Benefits Of The Data Mesh" (E250, December 27, 2021) — Dehghani on what actually happened when clients tried it. [C4-48]

### 7. *Dev Interrupted* — LinearB (linearb.io/dev-interrupted) [C4-49]
Weekly; uneven, vendor-adjacent, but with a few genuinely relevant episodes.
- "Team Topologies: Organizing Business & Technology Teams w/ Matthew Skelton & Manuel Pais" (March 21, 2023). [C4-50]
- "The End of Specialization? How AI Shapes Modern Dev Teams" (May 6, 2025, Lee Robinson) — relevant to whether India teams should be built as full-stack product teams or specialist pools. [C4-51]

### 8. *Software Engineering Daily* (softwareengineeringdaily.com) [C4-52]
Active daily, but overwhelmingly tooling and AI in 2026. Skippable for this decision; one episode earns a listen.
- "Sleuth and the Future of Engineering Teams with Dylan Etkin" (October 30, 2024). [C4-53]

### 9. *The Data Stack Show* — RudderStack (datastackshow.com) [C4-54]
Flagged: every 2026 episode is a re-air. Treat as an archive. One older episode is worth it:
- "A Decade of Change in the Data Space with Benn Stancil" (September 14, 2022). [C4-55]

---

## Section 4 — 12-month reading calendar

| Month | Milestone | Books | Blogs / newsletters | Podcasts |
|---|---|---|---|---|
| 1 | Diagnose; start charter draft | *Team Topologies* 2e [C4-1]; *An Elegant Puzzle* [C4-2] (sizing, reorg chapters); start *Engineering Executive's Primer* [C4-4] | Fowler, *Conway's Law* [C4-15]; lethain "executive" tag [C4-11]; subscribe to Pragmatic Engineer [C4-13] and Data Products [C4-16] | Thoughtworks, "Org design and Team Topologies after AI" [C4-44]; SE Radio 646 [C4-45] |
| 2 | **Charter decision** (domain vs platform vs extension) | Finish *Primer* [C4-4]; *Designing Organizations* [C4-5] (Star Model, lateral processes); *Data Mesh* [C4-7] Part II only | Benn Stancil, "Disband the analytics team" [C4-17]; Netflix "Data Projects" [C4-18] | DX, "Adopting the product operating model at Priceline" [C4-33]; Lenny, Will Larson [C4-42] |
| 3 | Design India leadership role; interview loop | *The Culture Map* [C4-3] | Camille Fournier, "Dude, Where's My Strategy?" [C4-14] | Analytics Engineering, Ian Macomber "consensus" [C4-38] |
| 4 | **First India leadership hire** | *Scaling People* [C4-6] (hiring, onboarding, operating cadence) | Charity Majors, "Engineer/Manager Pendulum" [C4-20] | Lenny, Claire Hughes Johnson [C4-41]; DX, "AI-native engineering organization" [C4-32] |
| 5 | Contractor-to-FTE conversion planning | Hand *Fundamentals of Data Engineering* [C4-30] to the site lead and converted FTEs | Sanderson, "Rise of Data Contracts" [C4-16] | Data Engineering Podcast, Ashish Mrig [C4-47] |
| 6 | **First team handover** | *The Art of Action* [C4-8]; begin *Accelerate* [C4-9] | Team Topologies case studies [C4-12] | Dev Interrupted, Team Topologies authors [C4-50] |
| 7 | Define graduation criteria | Finish *Accelerate* [C4-9] (metrics, Westrum culture) | Pragmatic Engineer archive on platform teams [C4-13] | Pragmatic Engineer AMA [C4-35]; Dev Interrupted, "End of Specialization?" [C4-51] |
| 8 | Pre-review; decide experimentation ownership | *Trustworthy Online Controlled Experiments* [C4-10] Part I; reread *Elegant Puzzle* reorg chapter [C4-2] | Spotify 2026 experimentation posts [C4-21]; experimentguide.com [C4-24] | Analytics Engineering, Shridhar Iyer / Meta [C4-39] |
| 9 | **First graduation review** | Reread *Team Topologies* interaction-modes chapter [C4-1] | Lenny, Camille Fournier [C4-43]; LeadDev reorg pieces [C4-22] | Data Engineering Podcast, Dehghani revisit [C4-48] |
| 10 | Second-wave planning | Optional: *High Output Management* [C4-27] (task-relevant maturity) | dbt Roundup "data teams in the AI era" [C4-19] | Pragmatic Engineer, Charity Majors [C4-36] |
| 11 | Retrospective inputs | Optional: *Team of Teams* [C4-28] if cross-site shared consciousness is the gap | Locally Optimistic archive on team structure [C4-23] | SED, Dylan Etkin [C4-53] (skippable) |
| 12 | **Org-wide review** | Reread *Designing Organizations* [C4-5] rewards/processes chapters; *Primer* measurement chapter [C4-4] | Sanderson, "Shift Left Manifesto v2" [C4-16] | Data Stack Show, Benn Stancil [C4-55] (archive) |

**Blunt priorities if time is short:** months 1–2 books (Team Topologies, Elegant Puzzle, Primer, Galbraith) plus *The Culture Map* in month 3 are the non-negotiables. Everything else is supporting material.

---

## Dropped / could not verify

- **Monday Morning Data Chat** (Joe Reis & Matt Housley) — show confirmed to have ended; no 2025–2026 episodes. Dropped.
- **LeadDev podcast** — leaddev.com/podcast returns 404. The successor, *LeadDev's PriorityZero* (Apple Podcasts), has no episode after January 13, 2025. Dropped as a podcast; leaddev.com kept as a site.
- **Camille Fournier on Medium** (skamille.medium.com) — exists but returns HTTP 403 to fetches; replaced with her primary site elidedbranches.com, which was verified.
- **Kohavi's experimentation posts** — no stable, fetchable URL for his current LinkedIn writing; represented by the verified book and companion site only.
- **"The Data Leaders"-type newsletters** — no specific title could be verified; dropped rather than guessed.
- **Not evaluated in this pass (deprioritized before verification, so not cited):** *The Manager's Path* (wrong altitude for an executive redesign), *Staff Engineer* (IC-track), *Working Backwards*, *No Rules Rules* (tempting for a streaming company, but a culture memoir, not structural), *Remote: Office Not Required* / *Distributed Teams*, *Software Engineering at Google*, *Leading Effective Engineering Teams*, *Turn the Ship Around!*, and Mintzberg's *The Structuring of Organizations* (the *Structure in Fives* condensation was verified instead). These may well exist as described; they were not verified here and are not recommended in this plan.

---

## Sources

All accessed 2026-08-29.

- [C4-1] Skelton, M. & Pais, M. *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, 2nd ed. IT Revolution, 2025. ISBN 9781966280002. https://itrevolution.com/product/team-topologies-second-edition/ (1st ed. 2019, ISBN 9781942788812, https://teamtopologies.com/book)
- [C4-2] Larson, W. *An Elegant Puzzle: Systems of Engineering Management*. Stripe Press, 2019. ISBN 9781732265189. https://press.stripe.com/an-elegant-puzzle
- [C4-3] Meyer, E. *The Culture Map: Breaking Through the Invisible Boundaries of Global Business*. PublicAffairs, 2014. ISBN 9781610392501. https://www.hachettebookgroup.com/titles/erin-meyer/the-culture-map/9781610392501/
- [C4-4] Larson, W. *The Engineering Executive's Primer: Impactful Technical Leadership*. O'Reilly Media, 2024. ISBN 9781098149482. https://www.oreilly.com/library/view/the-engineering-executives/9781098149475/
- [C4-5] Galbraith, J. R. *Designing Organizations: Strategy, Structure, and Process at the Business Unit and Enterprise Levels*, 3rd ed. Jossey-Bass (Wiley), 2014. ISBN 9781118409954. https://www.wiley.com/en-us/designing-organizations-strategy-structure-and-process-at-the-business-unit-and-enterprise-levels-3rd-edition-p-9781118409954
- [C4-6] Hughes Johnson, C. *Scaling People: Tactics for Management and Company Building*. Stripe Press, 2023. ISBN 9781953953216. https://press.stripe.com/scaling-people
- [C4-7] Dehghani, Z. *Data Mesh: Delivering Data-Driven Value at Scale*. O'Reilly Media, 2022. ISBN 9781492092391. https://www.oreilly.com/library/view/data-mesh/9781492092384/
- [C4-8] Bungay, S. *The Art of Action: How Leaders Close the Gaps Between Plans, Actions, and Results*. Nicholas Brealey, 2011 (ISBN 9781857885590); 10th-anniversary ed. 2022 (ISBN 9781529376968). https://www.hachette.co.uk/titles/stephen-bungay/the-art-of-action/9781857885590/
- [C4-9] Forsgren, N., Humble, J. & Kim, G. *Accelerate: The Science of Lean Software and DevOps*. IT Revolution, 2018. ISBN 9781942788331. https://www.simonandschuster.com/books/Accelerate/Nicole-Forsgren-PhD/9781942788331
- [C4-10] Kohavi, R., Tang, D. & Xu, Y. *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*. Cambridge University Press, 2020. ISBN 9781108724265. https://www.cambridge.org/core/books/trustworthy-online-controlled-experiments/BFFD7CC0B7325B5DCEEFFB1DD9401F7E
- [C4-11] Larson, W. *Irrational Exuberance* (blog). Active August 2026. https://lethain.com/
- [C4-12] Team Topologies news/blog. Active August 2026. https://teamtopologies.com/news
- [C4-13] Orosz, G. *The Pragmatic Engineer* (newsletter). Active 2026. https://newsletter.pragmaticengineer.com/
- [C4-14] Fournier, C. *Elided Branches* (blog). Active May 2026. https://www.elidedbranches.com/
- [C4-15] Fowler, M. "Conway's Law." martinfowler.com bliki, updated October 20, 2022. https://martinfowler.com/bliki/ConwaysLaw.html
- [C4-16] Sanderson, C. *Data Products* (newsletter). Active July 2026. https://dataproducts.substack.com/ ("The Shift Left Manifesto – v2," https://dataproducts.substack.com/p/the-shift-left-manifesto-v2; "The Rise of Data Contracts," https://dataproducts.substack.com/p/the-rise-of-data-contracts)
- [C4-17] Stancil, B. *benn.substack* (newsletter). Active July 2026. https://benn.substack.com/ ("Disband the analytics team," https://benn.substack.com/p/disband-the-analytics-team)
- [C4-18] Netflix Technology Blog. Active August 2026. https://netflixtechblog.com/ ("Data Projects: Managing Data Assets at Netflix Scale," May 2026, https://netflixtechblog.com/data-projects-managing-data-assets-at-netflix-scale-7ca25888591e)
- [C4-19] Handy, T. *The Analytics Engineering Roundup*. dbt Labs. Active August 2026. https://roundup.getdbt.com/
- [C4-20] Majors, C. *charity.wtf* (Substack). Active 2026. https://charity.wtf/ ("The Engineer/Manager Pendulum," 2017, https://charity.wtf/p/the-engineer-manager-pendulum)
- [C4-21] Spotify Engineering blog. Active August 2026. https://engineering.atspotify.com/
- [C4-22] LeadDev. Active 2025–2026. https://leaddev.com/
- [C4-23] Locally Optimistic. Last post August 18, 2025. https://locallyoptimistic.com/
- [C4-24] Kohavi, R. et al. *Experiment Guide* (book companion site). https://experimentguide.com/
- [C4-27] Grove, A. S. *High Output Management*. Vintage, 1995. ISBN 9780679762881. https://www.penguinrandomhouse.com/books/72467/high-output-management-by-andrew-s-grove-former-chairman-and-ceo-of-intel/
- [C4-28] McChrystal, S., Collins, T., Silverman, D. & Fussell, C. *Team of Teams: New Rules of Engagement for a Complex World*. Portfolio, 2015. ISBN 9781591847489. https://www.penguinrandomhouse.com/books/317066/team-of-teams-by-general-stanley-mcchrystal-tantum-collins-david-silverman-and-chris-fussell/
- [C4-29] Mintzberg, H. *Structure in Fives: Designing Effective Organizations*. Prentice Hall, 1983. ISBN 9780138543495. https://books.google.com/books/about/Structure_in_Fives.html?id=nR5HAAAAMAAJ
- [C4-30] Reis, J. & Housley, M. *Fundamentals of Data Engineering: Plan and Build Robust Data Systems*. O'Reilly Media, 2022. ISBN 9781098108304. https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- [C4-31] DX. *Engineering Enablement* podcast (hosts Abi Noda, Brian Houck, Justin Reock). Active 2026. https://getdx.com/podcast/
- [C4-32] "Designing the AI-native engineering organization with 1Password, Microsoft and Atlassian." *Engineering Enablement*, June 2026. https://getdx.com/podcast/designing-the-ai-native-engineering-organization/
- [C4-33] "Adopting the product operating model at Priceline" (Ep. 111). *Engineering Enablement*, July 2026. https://getdx.com/podcast/adopting-the-product-operating-model-at-priceline/
- [C4-34] Orosz, G. *The Pragmatic Engineer Podcast*. Active August 2026. https://podcasts.apple.com/us/podcast/the-pragmatic-engineer/id1769051199
- [C4-35] "The Pragmatic Engineer AMA." *The Pragmatic Engineer Podcast*, July 8, 2026. https://newsletter.pragmaticengineer.com/p/the-pragmatic-engineer-ama
- [C4-36] "Stop being skeptical about AI for development with Charity Majors." *The Pragmatic Engineer Podcast*, August 12, 2026. https://newsletter.pragmaticengineer.com/p/stop-being-skeptical-about-ai-for
- [C4-37] Handy, T. *The Analytics Engineering Podcast*. dbt Labs. Active August 2026. https://roundup.getdbt.com/s/the-analytics-engineering-podcast
- [C4-38] "The scarce resource is consensus (Ian Macomber)." *The Analytics Engineering Podcast*, July 16, 2026. https://roundup.getdbt.com/p/the-scarce-resource-is-consensus
- [C4-39] "Data lessons from inside Meta (Shridhar Iyer)." *The Analytics Engineering Podcast*, July 30, 2026. https://roundup.getdbt.com/p/data-lessons-from-inside-meta-shridhar
- [C4-40] Rachitsky, L. *Lenny's Podcast*. https://www.lennysnewsletter.com/podcast
- [C4-41] "Lessons from scaling Stripe | Claire Hughes Johnson." *Lenny's Podcast*, March 5, 2023. https://www.lennysnewsletter.com/p/lessons-from-scaling-stripe-tactics
- [C4-42] "The engineering mindset | Will Larson." *Lenny's Podcast*, January 7, 2024. https://www.lennysnewsletter.com/p/the-engineering-mindset-will-larson
- [C4-43] "The things engineers are desperate for PMs to understand | Camille Fournier." *Lenny's Podcast*, September 15, 2024. https://www.lennysnewsletter.com/p/engineering-leadership-camille-fournier
- [C4-44] "Organizational design and Team Topologies after AI" (Skelton & Pais). *Thoughtworks Technology Podcast*, September 4, 2025. https://www.thoughtworks.com/insights/podcasts/technology-podcasts/organizational-design-team-topologies-ai
- [C4-45] "SE Radio 646: Matthew Skelton on Team Topologies." *Software Engineering Radio*, December 11, 2024. https://se-radio.net/2024/12/se-radio-646-matthew-skelton-on-team-topologies/ (verified via https://matthewskelton.com/all-videos-and-podcast-episodes/software-engineering-radio-646-matthew-skelton-on-team-topologies)
- [C4-46] Macey, T. *Data Engineering Podcast*. Active August 2026 (E515). https://www.dataengineeringpodcast.com/
- [C4-47] "Building And Managing Data Teams And Data Platforms In Large Organizations With Ashish Mrig" (E257). *Data Engineering Podcast*, January 23, 2022. https://www.dataengineeringpodcast.com/episodepage/building-and-managing-data-teams-and-data-platforms-in-large-organizations-with-ashish-mrig
- [C4-48] "Revisiting The Technical And Social Benefits Of The Data Mesh" (E250, Zhamak Dehghani). *Data Engineering Podcast*, December 27, 2021. https://www.dataengineeringpodcast.com/episodepage/revisiting-the-technical-and-social-benefits-of-the-data-mesh
- [C4-49] LinearB. *Dev Interrupted* podcast. Active 2025–2026. https://linearb.io/dev-interrupted
- [C4-50] "Team Topologies: Organizing Business & Technology Teams w/ authors Matthew Skelton & Manuel Pais." *Dev Interrupted*, March 21, 2023. https://linearb.io/dev-interrupted/podcast/team-topologies-organizing-business-technology-teams
- [C4-51] "The End of Specialization? How AI Shapes Modern Dev Teams" (Lee Robinson). *Dev Interrupted*, May 6, 2025. https://linearb.io/dev-interrupted/podcast/the-end-of-specialization-how-ai-shapes-modern-dev-teams
- [C4-52] *Software Engineering Daily*. Active August 2026. https://softwareengineeringdaily.com/
- [C4-53] "Sleuth and the Future of Engineering Teams with Dylan Etkin." *Software Engineering Daily*, October 30, 2024. https://softwareengineeringdaily.com/podcasts/sleuth-and-the-future-of-engineering-teams-with-dylan-etkin/
- [C4-54] RudderStack. *The Data Stack Show*. 2026 episodes are re-airs. https://datastackshow.com/
- [C4-55] "A Decade of Change in the Data Space with Benn Stancil of Mode." *The Data Stack Show*, September 14, 2022. https://datastackshow.com/podcast/a-decade-of-change-in-the-data-space-with-benn-stancil-of-mode/
