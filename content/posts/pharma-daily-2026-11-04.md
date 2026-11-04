---
title: "Pharma Daily — November 4, 2026"
date: 2026-11-04
description: "One pipeline, five first-hand sources: 9 deals, 0 FDA approvals and 12 upcoming readouts, collected and charted without an LLM."
tags: ["pharma", "biotech", "daily-brief", "data-pipeline"]
kind: note
canonicalPath: /blog/pharma-daily-2026-11-04.html
---

Daily pharma news is mostly second-hand aggregation. This post is the output of a pipeline that skips the aggregators and reads only first-hand sources: regulator databases, trial registries and company wire releases.

> **TL;DR** — A small Python pipeline pulled 30 items from SEC EDGAR, openFDA, ClinicalTrials.gov and two wire feeds for Nov 3–November 4, 2026: 9 deal events, 0 FDA approvals and 12 Phase 2/3 readouts due within 90 days. Everything below is extracted heuristically — regex and keyword rules, no LLM — and every row links back to the original filing or press release.

## Today's Deals

| Company | Type | Upfront | Total (incl. milestones) | Source |
|---|---|---|---|---|
| IDEAYA Biosciences, Inc. | license | undisclosed | $1.15B | [filing / release](https://www.sec.gov/Archives/edgar/data/1676725/000119312526444225/idya-ex99_1.htm) |
| Nuvectis Pharma, Inc. | license | $30M | $140M | [filing / release](https://www.sec.gov/Archives/edgar/data/1875558/000110465926122360/tm2628939d1_ex99-1.htm) |
| Harmony Biosciences Holdings, Inc. | license | undisclosed | $1.04B | [filing / release](https://www.sec.gov/Archives/edgar/data/1802665/000110465926122377/hrmy-ex99d1.htm) |
| NewAmsterdam Pharma Co N.V. | license | undisclosed | $643M | [filing / release](https://www.sec.gov/Archives/edgar/data/1936258/000119312526446219/nams-ex99_1.htm) |
| Aquestive Therapeutics, Inc. | license | $13M | $48M | [filing / release](https://www.sec.gov/Archives/edgar/data/1398733/000139873326000073/q32026-ex991earningsrelease.htm) |
| — | other | undisclosed | $7B | [filing / release](https://endpoints.news/boehringer-ingelheim-strikes-7b-backloaded-adc-tce-cancer-deal-with-chinas-sino/) |
| — | license | undisclosed | $1.47B | [filing / release](https://endpoints.news/abbvie-bets-up-to-1-47b-on-nxeras-gut-targeting-ibd-program/) |
| Ultragenyx Pharmaceutical Inc. | license | undisclosed | $210M | [filing / release](https://www.sec.gov/Archives/edgar/data/1515673/000119312526445342/rare-20261030.htm) |
| — | other | undisclosed | $1.50B | [filing / release](https://endpoints.news/serviers-1-5b-bet-on-edgewise-drug-fails-five-months-in/) |

*Table 1: Deal events in the collection window, sorted by disclosed total value.*

Deal-comp context: across 9 deals with disclosed values in the window, the median total is $1.04B; the largest is $1.15B (IDEAYA Biosciences, Inc.). Milestone-heavy structures dominate, so headline totals overstate near-term cash.

![Horizontal bar chart of disclosed deal values in US$ millions](/figures/pharma-daily-2026-11-04-deal-sizes.png)

*Figure 1: Disclosed total deal values collected this window.*

## FDA & Approvals

No new approvals surfaced in openFDA for this window.

## Readout Calendar

| Primary completion | Phase | Sponsor | Study |
|---|---|---|---|
| 2026-12-31 | Phase 3 | Boehringer Ingelheim | [EASi-KIDNEY™ (The Studies of Heart & Kidney Protection With BI 690517…](https://clinicaltrials.gov/study/NCT06531824) |
| 2026-12 | Phase 3 | Chia Tai Tianqing… | [A Phase III Clinical Trial of AK105 Injection Combined With Anlotinib…](https://clinicaltrials.gov/study/NCT04344158) |
| 2026-11-30 | Phase 3 | Zhejiang Wenda Pharma… | [A Multicenter, Randomized, Double-Blind, Placebo-Controlled Phase Ⅲ…](https://clinicaltrials.gov/study/NCT07672561) |
| 2026-12-31 | Phase 3 | Tasly Pharmaceutical Group… | [A Study of Lianxiaxiaopi Granules in the Treatment of Postprandial…](https://clinicaltrials.gov/study/NCT06696261) |
| 2026-12-31 | Phase 3 | Second Affiliated Hospital… | [Intravenous Thrombolysis and NOAC](https://clinicaltrials.gov/study/NCT06749834) |
| 2026-12-14 | Phase 2 | Novo Nordisk A/S | [A Research Study on How Well Different Doses of the Medicine…](https://clinicaltrials.gov/study/NCT07184632) |
| 2027-02 | Phase 2 | Eli Lilly and Company | [A Study of Brenipatide in Adults Who Quit Smoking Cigarettes and Want…](https://clinicaltrials.gov/study/NCT07223840) |
| 2026-12-31 | Phase 3 | Clarity Pharmaceuticals Ltd | [64Cu-SAR-bisPSMA Positron Emission Tomography: A Phase 3 Study of…](https://clinicaltrials.gov/study/NCT06970847) |
| 2026-12 | Phase 3 | Sun Yat-sen University | [Chemoradiotherapy Plus Anti-PD1 in Recurrent NPC: A Multicenter…](https://clinicaltrials.gov/study/NCT05340491) |
| 2026-12-31 | Phase 3 | Tianjin Medical University… | [Modified Zipper Therapy for AQP4-IgG Positive Neuromyelitis Optica…](https://clinicaltrials.gov/study/NCT07420296) |

*Table 3: Phase 2/3 studies on ClinicalTrials.gov with primary completion dates in the next 90 days (major sponsors prioritized, ranked by enrollment).*

## Sources

- [IDEAYA Biosciences, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1676725/000119312526444225/idya-ex99_1.htm)
- [Nuvectis Pharma, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1875558/000110465926122360/tm2628939d1_ex99-1.htm)
- [Harmony Biosciences Holdings, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1802665/000110465926122377/hrmy-ex99d1.htm)
- [NewAmsterdam Pharma Co N.V. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1936258/000119312526446219/nams-ex99_1.htm)
- [Aquestive Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1398733/000139873326000073/q32026-ex991earningsrelease.htm)
- [Boehringer Ingelheim strikes $7B backloaded ADC, TCE cancer deal with China's Sino](https://endpoints.news/boehringer-ingelheim-strikes-7b-backloaded-adc-tce-cancer-deal-with-chinas-sino/)
- [AbbVie bets up to $1.47B on Nxera's gut-targeting IBD program](https://endpoints.news/abbvie-bets-up-to-1-47b-on-nxeras-gut-targeting-ibd-program/)
- [Ultragenyx Pharmaceutical Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1515673/000119312526445342/rare-20261030.htm)
- [Servier's $1.5B bet on Edgewise drug fails five months in](https://endpoints.news/serviers-1-5b-bet-on-edgewise-drug-fails-five-months-in/)
- [EASi-KIDNEY™ (The Studies of Heart & Kidney Protection With BI 690517 in Combination With ](https://clinicaltrials.gov/study/NCT06531824)
- [A Phase III Clinical Trial of AK105 Injection Combined With Anlotinib Hydrochloride Capsul](https://clinicaltrials.gov/study/NCT04344158)
- [A Multicenter, Randomized, Double-Blind, Placebo-Controlled Phase Ⅲ Study to Evaluate the ](https://clinicaltrials.gov/study/NCT07672561)
- [A Study of Lianxiaxiaopi Granules in the Treatment of Postprandial Distress Syndrome](https://clinicaltrials.gov/study/NCT06696261)
- [Intravenous Thrombolysis and NOAC](https://clinicaltrials.gov/study/NCT06749834)
- [A Research Study on How Well Different Doses of the Medicine NNC0662-0419 Help People Livi](https://clinicaltrials.gov/study/NCT07184632)

All items above are drawn from first-hand public sources — SEC filings, trial registries, and company releases. The same source-first discipline is what I apply to [LLM agents in regulated programming](/blog/why-llm-agents-fail-regulated-programming.html).
