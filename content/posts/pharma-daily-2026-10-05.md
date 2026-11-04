---
title: "Pharma Daily — October 5, 2026"
date: 2026-10-05
description: "One pipeline, five first-hand sources: 3 deals, 0 FDA approvals and 12 upcoming readouts, collected and charted without an LLM."
tags: ["pharma", "biotech", "daily-brief", "data-pipeline"]
kind: note
canonicalPath: /blog/pharma-daily-2026-10-05.html
videoId: fEcND0h4Zv4
audioPath: /audio/pharma-daily-2026-10-05.mp3
---

Daily pharma news is mostly second-hand aggregation. This post is the output of a pipeline that skips the aggregators and reads only first-hand sources: regulator databases, trial registries and company wire releases.

> **TL;DR** — A small Python pipeline pulled 11 items from SEC EDGAR, openFDA, ClinicalTrials.gov and two wire feeds for Oct 4–October 5, 2026: 3 deal events, 0 FDA approvals and 12 Phase 2/3 readouts due within 90 days. Everything below is extracted heuristically — regex and keyword rules, no LLM — and every row links back to the original filing or press release.

## Today's Deals

| Company | Type | Upfront | Total (incl. milestones) | Source |
|---|---|---|---|---|
| Sensible Bio | financing | undisclosed | $47M | [filing / release](https://endpoints.news/sensible-bio-secures-47m-series-a-for-mrna-therapy-manufacturing-platform/) |
| — | collaboration | $355M | $1.20B | [filing / release](https://endpoints.news/csl-to-pay-355m-upfront-to-co-develop-alentis-kidney-and-liver-drug/) |
| Jasper Therapeutics, Inc. | license | undisclosed | undisclosed | [filing / release](https://www.sec.gov/Archives/edgar/data/1788028/000121390026106574/ea030760201ex99-3.htm) |

*Table 1: Deal events in the collection window, sorted by disclosed total value.*

Deal-comp context: across 2 deals with disclosed values in the window, the median total is $624M; the largest is $47M (Sensible Bio). Milestone-heavy structures dominate, so headline totals overstate near-term cash.

![Horizontal bar chart of disclosed deal values in US$ millions](/figures/pharma-daily-2026-10-05-deal-sizes.png)

*Figure 1: Disclosed total deal values collected this window.*

## FDA & Approvals

No new approvals surfaced in openFDA for this window.

## Readout Calendar

| Primary completion | Phase | Sponsor | Study |
|---|---|---|---|
| 2026-10-30 | Phase 3 | Vertex Pharmaceuticals… | [A Study Evaluating the Long-term Safety and Efficacy of VX-121…](https://clinicaltrials.gov/study/NCT05444257) |
| 2026-12-31 | Phase 3 | University of Birmingham | [Preventing Pulmonary Complications in Surgical Patients at Risk of…](https://clinicaltrials.gov/study/NCT04386070) |
| 2026-12-16 | Phase 3 | Hoffmann-La Roche | [A Study to Evaluate the Efficacy, Safety, Pharmacokinetics (PK), and…](https://clinicaltrials.gov/study/NCT05503264) |
| 2026-12 | Phase 3 | University of Birmingham | [CompARE: Escalating Treatment of Intermediate and High-risk…](https://clinicaltrials.gov/study/NCT04116047) |
| 2026-10-31 | Phase 3 | Annexon, Inc. | [A Study Investigating the Efficacy and Safety of Intravitreal (IVT)…](https://clinicaltrials.gov/study/NCT06510816) |
| 2026-10-31 | Phase 3 | Olema Pharmaceuticals, Inc. | [OP-1250 (Palazestrant) vs. Standard of Care for the Treatment of…](https://clinicaltrials.gov/study/NCT06016738) |
| 2026-10-26 | Phase 3 | Galderma R&D | [A Long-term Study of Nemolizumab (CD14152) in Participants With…](https://clinicaltrials.gov/study/NCT04204616) |
| 2026-12 | Phase 3 | Vanda Pharmaceuticals | [Study to Evaluate the Efficacy and Safety of VQW-765 for the…](https://clinicaltrials.gov/study/NCT07221578) |
| 2026-12-31 | Phase 3 | University of Minnesota | [Evaluation of a Disability-Focused Sexual and Reproductive Health…](https://clinicaltrials.gov/study/NCT07772778) |
| 2026-12 | Phase 3 | University Hospital… | [Evaluation of the Efficacy of an inTerdialytic "Ethanol 40% v/v -…](https://clinicaltrials.gov/study/NCT03083184) |

*Table 3: Phase 2/3 studies on ClinicalTrials.gov with primary completion dates in the next 90 days (major sponsors prioritized, ranked by enrollment).*

## Sources

- [Sensible Bio secures $47M Series A for mRNA therapy manufacturing platform](https://endpoints.news/sensible-bio-secures-47m-series-a-for-mrna-therapy-manufacturing-platform/)
- [CSL to pay $355M upfront to co-develop Alentis’ kidney and liver drug](https://endpoints.news/csl-to-pay-355m-upfront-to-co-develop-alentis-kidney-and-liver-drug/)
- [Jasper Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1788028/000121390026106574/ea030760201ex99-3.htm)
- [A Study Evaluating the Long-term Safety and Efficacy of VX-121 Combination Therapy](https://clinicaltrials.gov/study/NCT05444257)
- [Preventing Pulmonary Complications in Surgical Patients at Risk of COVID-19](https://clinicaltrials.gov/study/NCT04386070)
- [A Study to Evaluate the Efficacy, Safety, Pharmacokinetics (PK), and Pharmacodynamics (PD)](https://clinicaltrials.gov/study/NCT05503264)
- [CompARE: Escalating Treatment of Intermediate and High-risk Oropharyngeal Cancer (OPC)](https://clinicaltrials.gov/study/NCT04116047)
- [A Study Investigating the Efficacy and Safety of Intravitreal (IVT) Injections of Vonaprum](https://clinicaltrials.gov/study/NCT06510816)
- [OP-1250 (Palazestrant) vs. Standard of Care for the Treatment of ER+/HER2- Advanced Breast](https://clinicaltrials.gov/study/NCT06016738)
- [A Long-term Study of Nemolizumab (CD14152) in Participants With Prurigo Nodularis (PN)](https://clinicaltrials.gov/study/NCT04204616)
- [Study to Evaluate the Efficacy and Safety of VQW-765 for the On-Demand Treatment of Social](https://clinicaltrials.gov/study/NCT07221578)
- [Evaluation of a Disability-Focused Sexual and Reproductive Health Curriculum for Health St](https://clinicaltrials.gov/study/NCT07772778)
- [Evaluation of the Efficacy of an inTerdialytic "Ethanol 40% v/v - enoxapaRin 1000 U/mL" Lo](https://clinicaltrials.gov/study/NCT03083184)
- [Efficacy and Safety oF FErric CarboxymalTose in Patients With Advanced Gastric Cancer(EFFE](https://clinicaltrials.gov/study/NCT05226169)
- [A Study of 2nd-line FOLFIRI ± Bevacizumab vs. Irinotecan ± Bevacizumab in mCRC](https://clinicaltrials.gov/study/NCT03303495)

All items above are drawn from first-hand public sources — SEC filings, trial registries, and company releases. The same source-first discipline is what I apply to [LLM agents in regulated programming](/blog/why-llm-agents-fail-regulated-programming.html).
