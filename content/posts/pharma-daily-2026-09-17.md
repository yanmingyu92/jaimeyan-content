---
title: "Pharma Daily — September 17, 2026"
date: 2026-09-17
description: "One pipeline, five first-hand sources: 32 deals, 25 FDA approvals and 12 upcoming readouts, collected and charted without an LLM."
tags: ["pharma", "biotech", "daily-brief", "data-pipeline"]
kind: note
canonicalPath: /blog/pharma-daily-2026-09-17.html
videoId: cwBrBt4MTmk
audioPath: /audio/pharma-daily-2026-09-17.mp3
---

Daily pharma news is mostly second-hand aggregation. This post is the output of a pipeline that skips the aggregators and reads only first-hand sources: regulator databases, trial registries and company wire releases.

> **TL;DR** — A small Python pipeline pulled 116 items from SEC EDGAR, openFDA, ClinicalTrials.gov and two wire feeds for Sep 10–September 17, 2026: 32 deal events, 25 FDA approvals and 12 Phase 2/3 readouts due within 90 days. Everything below is extracted heuristically — regex and keyword rules, no LLM — and every row links back to the original filing or press release.

## Today's Deals

| Company | Type | Upfront | Total (incl. milestones) | Source |
|---|---|---|---|---|
| Yarrow Bioscience, Inc. | license | undisclosed | $150M | [filing / release](https://www.sec.gov/Archives/edgar/data/1566044/000110465926106699/tm2624937d1_ex99-2.htm) |
| Connect Biopharma Holdings Ltd | collaboration | undisclosed | $99M | [filing / release](https://www.sec.gov/Archives/edgar/data/1835268/000183526826000034/exhibit991.htm) |
| Tempest Therapeutics, Inc. | license | undisclosed | undisclosed | [filing / release](https://www.sec.gov/Archives/edgar/data/1544227/000119312526394492/d185404dex991.htm) |
| Roche / Dualitas | other | undisclosed | $1B | [filing / release](https://www.fiercebiotech.com/biotech/roche-pays-dualitas-365m-pair-big-bispecific-screening-drive) |
| Cardiff Oncology, Inc. | license | undisclosed | undisclosed | [filing / release](https://www.sec.gov/Archives/edgar/data/1213037/000149315226042506/ex99-1.htm) |
| Perspective Therapeutics, Inc. | collaboration | undisclosed | undisclosed | [filing / release](https://www.sec.gov/Archives/edgar/data/728387/000119312526389785/catx-ex99_1.htm) |
| Sling | other | undisclosed | $123M | [filing / release](https://endpoints.news/sling-gets-123m-for-phase-3-trial-of-ex-astellas-drug-in-thyroid-eye-disease/) |
| — | other | undisclosed | $100M | [filing / release](https://endpoints.news/bristol-myers-scraps-orum-partnered-cancer-drug/) |
| — | other | undisclosed | $750M | [filing / release](https://www.fiercebiotech.com/biotech/gsk-doubles-down-chimagen-750m-multiple-myeloma-wager) |
| — | financing | undisclosed | $123M | [filing / release](https://www.fiercebiotech.com/biotech/sling-reels-123m-series-c-funding-its-oral-tepezza-rival-eye-disease) |

*Table 1: Deal events in the collection window, sorted by disclosed total value.*

Deal-comp context: across 17 deals with disclosed values in the window, the median total is $180M; the largest is $150M (Yarrow Bioscience, Inc.). Milestone-heavy structures dominate, so headline totals overstate near-term cash.

![Horizontal bar chart of disclosed deal values in US$ millions](/figures/pharma-daily-2026-09-17-deal-sizes.png)

*Figure 1: Disclosed total deal values collected this window.*

## FDA & Approvals

| Product (sponsor) | Date | Link |
|---|---|---|
| EPINEPHRINE (Zydus Pharms) | 2026-09-14 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=219832) |
| IMDELLTRA (Amgen Inc) | 2026-09-11 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=761344) |
| LISDEXAMFETAMINE DIMESYLATE (Ascent Pharms Inc) | 2026-09-10 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=217442) |
| ASENAPINE MALEATE (Alembic) | 2026-09-10 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=206098) |
| SPIRONOLACTONE AND HYDROCHLOROTHIAZIDE (Rubicon Research) | 2026-09-10 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=220884) |
| ITRACONAZOLE (Apotex) | 2026-09-11 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=208481) |
| GABAPENTIN (Invagen Pharms) | 2026-09-11 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=090705) |
| COLISTIMETHATE SODIUM (Sagent Pharms Inc) | 2026-09-14 | [Drugs@FDA](https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm?event=overview.process&ApplNo=201365) |

*Table 2: Approvals recorded in openFDA's Drugs@FDA feed this window.*

## Readout Calendar

| Primary completion | Phase | Sponsor | Study |
|---|---|---|---|
| 2026-11-18 | Phase 3 | Bristol-Myers Squibb | [A Study to Evaluate the Efficacy and Safety of Deucravacitinib in…](https://clinicaltrials.gov/study/NCT05946941) |
| 2026-09-30 | Phase 3 | AstraZeneca | [A Study to Investigate the Efficacy and Safety of Dato-DXd With or…](https://clinicaltrials.gov/study/NCT06417814) |
| 2026-10 | Phase 3 | University of Oxford | [A Randomized Trial Assessing the Effects of Inclisiran on Clinical…](https://clinicaltrials.gov/study/NCT03705234) |
| 2026-11-13 | Phase 3 | Hoffmann-La Roche | [A Study Evaluating the Efficacy and Safety of Inavolisib Plus…](https://clinicaltrials.gov/study/NCT05646862) |
| 2026-12-02 | Phase 3 | Pfizer | [A Study to Learn About Medicine Called Ritlecitinib in Children Aged…](https://clinicaltrials.gov/study/NCT07029711) |
| 2026-12 | Phase 3 | Second Affiliated Hospital… | [The Impact of Fexofenadine Hydrochloride on the Prognosis of Patients…](https://clinicaltrials.gov/study/NCT07381803) |
| 2026-12 | Phase 3 | The Cleveland Clinic | [Total Intravenous Anesthesia and Recurrence Free Survival](https://clinicaltrials.gov/study/NCT04513808) |
| 2026-11 | Phase 3 | Gustave Roussy, Cancer… | [High-Risk Neuroblastoma Study 2 of SIOP-Europa-Neuroblastoma (SIOPEN)](https://clinicaltrials.gov/study/NCT04221035) |
| 2026-09-23 | Phase 3 | ANRS, Emerging Infectious… | [Intensified Tuberculosis Treatment to Reduce the Mortality of…](https://clinicaltrials.gov/study/NCT04145258) |
| 2026-12 | Phase 3 | Mabscale, LLC | [A Safety and Efficacy Study of Bevacizumab, Paclitaxel, Carboplatin…](https://clinicaltrials.gov/study/NCT05654454) |

*Table 3: Phase 2/3 studies on ClinicalTrials.gov with primary completion dates in the next 90 days (major sponsors prioritized, ranked by enrollment).*

## Sources

- [Yarrow Bioscience, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1566044/000110465926106699/tm2624937d1_ex99-2.htm)
- [Connect Biopharma Holdings Ltd 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/1835268/000183526826000034/exhibit991.htm)
- [Tempest Therapeutics, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1544227/000119312526394492/d185404dex991.htm)
- [Roche signs $1B deal with Dualitas to pair up on big bispecific screening drive](https://www.fiercebiotech.com/biotech/roche-pays-dualitas-365m-pair-big-bispecific-screening-drive)
- [Cardiff Oncology, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1213037/000149315226042506/ex99-1.htm)
- [Perspective Therapeutics, Inc. 8-K mentioning collaboration agreement](https://www.sec.gov/Archives/edgar/data/728387/000119312526389785/catx-ex99_1.htm)
- [Sling gets $123M for Phase 3 trial of ex-Astellas drug in thyroid eye disease](https://endpoints.news/sling-gets-123m-for-phase-3-trial-of-ex-astellas-drug-in-thyroid-eye-disease/)
- [Bristol Myers scraps $100M Orum-partnered cancer drug](https://endpoints.news/bristol-myers-scraps-orum-partnered-cancer-drug/)
- [GSK doubles down on Chimagen with $750M multiple myeloma wager](https://www.fiercebiotech.com/biotech/gsk-doubles-down-chimagen-750m-multiple-myeloma-wager)
- [Sling reels in $123M series C to fund oral Tepezza rival through phase 3 trial](https://www.fiercebiotech.com/biotech/sling-reels-123m-series-c-funding-its-oral-tepezza-rival-eye-disease)
- [Korsana Biosciences, Inc. 8-K mentioning license agreement](https://www.sec.gov/Archives/edgar/data/1755237/000119312526389318/d178159dex993.htm)
- [Newly formed Jaguar acquires Afib device assets from J&amp;J](https://www.fiercebiotech.com/medtech/newly-formed-jaguar-acquires-afib-device-assets-jj)
- [Novo partners with Orbis, deepening investment in oral peptide drugs](https://www.biopharmadive.com/news/novo-orbis-macrocyclic-peptides-oral-obesity-drugs/830645/)
- [SK pens $315M pact with fellow South Korean company for Parkinson’s prospect](https://www.fiercebiotech.com/biotech/sk-pens-315m-pact-fellow-south-korean-company-parkinsons-prospect)
- [Novo walks away from $285M pact to develop monthly GLP-1 obesity drug with Ascendis](https://www.fiercebiotech.com/biotech/novo-walks-away-285m-pact-develop-monthly-glp-1-ascendis)

All items above are drawn from first-hand public sources — SEC filings, trial registries, and company releases. The same source-first discipline is what I apply to [LLM agents in regulated programming](/blog/why-llm-agents-fail-regulated-programming.html).
