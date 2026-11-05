---
title: "Pharma Daily — November 5, 2026"
date: 2026-11-05
description: "One pipeline, five first-hand sources: 23 deals, 0 FDA approvals and 12 upcoming readouts, collected and charted without an LLM."
tags: ["pharma", "biotech", "daily-brief", "data-pipeline"]
kind: note
canonicalPath: /blog/pharma-daily-2026-11-05.html
---

Daily pharma news is mostly second-hand aggregation. This post is the output of a pipeline that skips the aggregators and reads only first-hand sources: regulator databases, trial registries and company wire releases.

> **TL;DR** — A small Python pipeline pulled 50 items from SEC EDGAR, openFDA, ClinicalTrials.gov and two wire feeds for Nov 4–November 5, 2026: 23 deal events, 0 FDA approvals and 12 Phase 2/3 readouts due within 90 days. Everything below is extracted heuristically — regex and keyword rules, no LLM — and every row links back to the original filing or press release.

## Today's Deals

| Company | Type | Upfront | Total (incl. milestones) | Source |
|---|---|---|---|---|
| Zenas BioPharma, Inc. | license | $35M | $647M | [filing / release](https://www.sec.gov/Archives/edgar/data/1953926/000110465926123035/tm2628936d1_ex99-1.htm) |
| OPKO HEALTH, INC. | license | undisclosed | $722M | [filing / release](https://www.sec.gov/Archives/edgar/data/944809/000119312526447357/opk-ex99_1.htm) |
| Summit Therapeutics Inc. | collaboration | undisclosed | $2B | [filing / release](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/a2026_prx1105xq32026earn.htm) |
| Monte Rosa Therapeutics, Inc. | license | undisclosed | $583M | [filing / release](https://www.sec.gov/Archives/edgar/data/1826457/000119312526448527/glue-ex99_1.htm) |
| Climb Bio, Inc. | license | undisclosed | $228M | [filing / release](https://www.sec.gov/Archives/edgar/data/1768446/000119312526448556/clym-ex99_1.htm) |
| Aclaris Therapeutics, Inc. | license | undisclosed | $205M | [filing / release](https://www.sec.gov/Archives/edgar/data/1557746/000110465926123039/acrs-ex99d1.htm) |
| Nuvectis Pharma, Inc. | license | $30M | $140M | [filing / release](https://www.sec.gov/Archives/edgar/data/1875558/000110465926122360/tm2628939d1_ex99-1.htm) |
| Korro Bio, Inc. | collaboration | undisclosed | $125M | [filing / release](https://www.sec.gov/Archives/edgar/data/1703647/000119312526448532/krro-ex99_1.htm) |
| Harmony Biosciences Holdings, Inc. | license | undisclosed | $1.04B | [filing / release](https://www.sec.gov/Archives/edgar/data/1802665/000110465926122377/hrmy-ex99d1.htm) |
| C4 Therapeutics, Inc. | collaboration | undisclosed | $11M | [filing / release](https://www.sec.gov/Archives/edgar/data/1662579/000162828026070560/exhibit991q32026earnings.htm) |

*Table 1: Deal events in the collection window, sorted by disclosed total value.*

Deal-comp context: across 17 deals with disclosed values in the window, the median total is $288M; the largest is $647M (Zenas BioPharma, Inc.). Milestone-heavy structures dominate, so headline totals overstate near-term cash.

![Horizontal bar chart of disclosed deal values in US$ millions](/figures/pharma-daily-2026-11-05-deal-sizes.png)

*Figure 1: Disclosed total deal values collected this window.*

## FDA & Approvals

No new approvals surfaced in openFDA for this window.

## Readout Calendar

| Primary completion | Phase | Sponsor | Study |
|---|---|---|---|
| 2027-01-11 | Phase 3 | AstraZeneca | [A Study to Investigate the Efficacy and Safety of Dato-DXd With or…](https://clinicaltrials.gov/study/NCT06417814) |
| 2027-01-31 | Phase 3 | Merck Sharp & Dohme LLC | [Efficacy and Safety of Pembrolizumab (MK-3475) in Combination With…](https://clinicaltrials.gov/study/NCT04241185) |
| 2026-12 | Phase 3 | Chia Tai Tianqing… | [Clinical Study on Adjuvant Therapy of TQB3616 Combined With Endocrine…](https://clinicaltrials.gov/study/NCT05780567) |
| 2027-01 | Phase 3 | Universität Münster | [Reducing Cardiac-surgery Associated Acute Kidney Injury Occurence by…](https://clinicaltrials.gov/study/NCT06615102) |
| 2027-01 | Phase 3 | Shanghai Huilun… | [A Phase III Clinical Study of H077 Sustained-Release Tablets Compared…](https://clinicaltrials.gov/study/NCT07146386) |
| 2027-01-04 | Phase 3 | MoonLake Immunotherapeutics AG | [Evaluation of Sonelokimab in Patients With Active Psoriatic Arthritis…](https://clinicaltrials.gov/study/NCT06641089) |
| 2026-12-31 | Phase 3 | Ginger Yang | [Teen Driving Translation Study (NIH)](https://clinicaltrials.gov/study/NCT05696353) |
| 2026-12-31 | Phase 3 | Hangzhou Highlightll… | [A Long-term Extension Clinical Study of TLL-018 in Patients With…](https://clinicaltrials.gov/study/NCT06887127) |
| 2027-01 | Phase 3 | Telix Pharmaceuticals… | [PSMA PET Combined With MRI for the Detection of PCa](https://clinicaltrials.gov/study/NCT07052214) |
| 2026-12-01 | Phase 3 | Kind Pharmaceuticals LLC | [A Study of AND017 to Evaluate Efficacy and Safety in Patients With…](https://clinicaltrials.gov/study/NCT07487727) |

*Table 3: Phase 2/3 studies on ClinicalTrials.gov with primary completion dates in the next 90 days (major sponsors prioritized, ranked by enrollment).*

## Sources

- [Zenas BioPharma, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1953926/000110465926123035/tm2628936d1_ex99-1.htm)
- [OPKO HEALTH, INC. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/944809/000119312526447357/opk-ex99_1.htm)
- [Summit Therapeutics Inc. 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/1599298/000159929826000088/a2026_prx1105xq32026earn.htm)
- [Monte Rosa Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1826457/000119312526448527/glue-ex99_1.htm)
- [Climb Bio, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1768446/000119312526448556/clym-ex99_1.htm)
- [Aclaris Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1557746/000110465926123039/acrs-ex99d1.htm)
- [Nuvectis Pharma, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1875558/000110465926122360/tm2628939d1_ex99-1.htm)
- [Korro Bio, Inc. 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/1703647/000119312526448532/krro-ex99_1.htm)
- [Harmony Biosciences Holdings, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1802665/000110465926122377/hrmy-ex99d1.htm)
- [C4 Therapeutics, Inc. 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/1662579/000162828026070560/exhibit991q32026earnings.htm)
- [NewAmsterdam Pharma Co N.V. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1936258/000119312526446219/nams-ex99_1.htm)
- [Arcus Biosciences, Inc. 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/1724521/000172452126000056/a2026q38kexhibit991.htm)
- [Dogwood Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1818844/000110465926123095/dwtx-ex99d1.htm)
- [Korro Bio, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1703647/000119312526448532/krro-20261103.htm)
- [Boehringer Ingelheim strikes $7B backloaded ADC, TCE cancer deal with China's Sino](https://endpoints.news/boehringer-ingelheim-strikes-7b-backloaded-adc-tce-cancer-deal-with-chinas-sino/)

All items above are drawn from first-hand public sources — SEC filings, trial registries, and company releases. The same source-first discipline is what I apply to [LLM agents in regulated programming](/blog/why-llm-agents-fail-regulated-programming.html).
