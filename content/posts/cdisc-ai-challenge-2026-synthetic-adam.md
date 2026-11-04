---
title: "The 2026 CDISC AI Challenge: Winners, Open Code, and a Synthetic ADaM Showdown"
date: 2026-10-05
description: "The 2026 CDISC AI Innovation Challenge winners present today in Denver. None published code — except one adjacent R package. We read synadam's source and compare it to our own synthetic ADaM pipeline."
tags: ["cdisc", "synthetic-data", "adam", "llm", "standards"]
kind: deep-dive
paperRef: phuse-2025-ml12
canonicalPath: /blog/cdisc-ai-challenge-2026-synthetic-adam.html
videoId: LRwwfo4zuUE
---

The 2026 CDISC AI Innovation Challenge results landed days ago, and the winners are presenting at the CDISC US Interchange in Denver today, October 5th. Fifty submissions from 30 organizations — more than double the 22 from 2025 — across three use cases: AI-enabled synthetic data for automation testing, AI-driven SAP generation, and AI-driven TFL generation. If you care about where AI and clinical data standards actually meet in production, this is the closest thing to a survey of the state of the art.

I did two things with the results: read everything public about the six winning and runner-up solutions, and then went looking for code. That second search turned up exactly one installable artifact adjacent to the winners — Novartis's open-source `synadam` R package — so I read its source too. What follows is a practitioner read on all of it.

> **TL;DR** — The 2026 winners validate directions we took in our PhUSE 2025 ML12 paper: standards-native generation, ARS as the intermediate layer, evidence records over agent counts. The open-source pickings are thin — none of the six solutions published code. The one package that exists, `synadam`, is *not* the winning Syn2Real; it's a much simpler de-identification tool with a "glimpse-then-simulate" mechanism that preserves ranges but not distributions. synadam vs. our ML12 pipeline is an apples-to-oranges comparison — and making it precisely is the useful part.

## The 2026 winners at a glance

Per the [CDISC challenge page](https://www.cdisc.org/events/ai-innovation-challenge), judging weights standards integration and traceability most heavily — a signal worth remembering.

| Use case | Winner | Runner-up | One-line approach |
|---|---|---|---|
| 1. Synthetic data for automation testing | **Syn2Real** (Novartis + AWS) | **Leova** (BioInformatiCo) | Syn2Real: standards-native framework generating synthetic SDTM/ADaM from a study's USDM definition. Leova: protocol → USDM → synthetic "rule-breaker" patients robot-entered into an EDC to verify edit checks — closed-loop protocol-to-analysis testing (2nd of 19 submissions; [details](https://www.bioinformatico.com/resources/2026/cdisc-ai-innovation-challenge-2026-runner-up/)). |
| 2. AI-driven SAP generation | **Smart ClinSAP** (Saama) | **SAP-Genie** (Jazz) | Smart ClinSAP: protocol interpretation → executable SAS/R. SAP-Genie: protocol → ARS-conformant SAP plus a traceable CDISC package. |
| 3. AI-driven TFL generation | **PAIR** (Novartis + AWS) | **TLFGenix** (Zifo) | PAIR: agentic workflow from SAP + ADaM specs + TFL shells → complete reporting packages. TLFGenix: six-agent pipeline with human approval gates and per-TLF evidence records ([Zifo's release](https://www.prnewswire.com/news-releases/zifos-ai-powered-clinical-reporting-solution-named-runner-up-in-the-2026-cdisc-ai-innovation-challenge-302890189.html)). |

*Table 1: 2026 CDISC AI Innovation Challenge results by use case.*

TLFGenix's architecture deserves one more sentence because it's the most fully described: SAP digitization → ADaM profiling → ARS-aligned analysis spec → R driver scripts → network-isolated sandbox execution → schema/consistency checks. Statisticians approve the spec before any codegen and sign off each TLF; a lineage graph enables selective regeneration when the spec changes; every TLF ships an evidence record.

## Where is the code?

Nowhere, mostly. I checked the GitHub API today: of the six 2026 solutions, none has public code. SAP-Genie, TLFGenix, Syn2Real, PAIR, Leova — no repos. Smart ClinSAP has only a 19 KB documentation repo.

The single installable artifact adjacent to the winners is [`Novartis/synadam`](https://github.com/Novartis/synadam): an open-source R package on CRAN, MIT-licensed, created June 2026, roughly two stars at time of writing. **Important: synadam is not Syn2Real.** Syn2Real is the USDM-driven, standards-native framework that won Use Case 1; synadam is a separate, much simpler Novartis package in the same problem family. Conflating them would be a mistake, so I'll keep them strictly apart here.

One channel worth watching: COSA, the CDISC Open-Source Alliance. The 2025 open-source winners were invited to contribute through it, and CDISC's own [cdisc-org](https://github.com/cdisc-org) repos — including the Analysis Results Standard — are already open. If any 2026 code surfaces publicly, that's where it will likely land.

## synadam under the hood

Since synadam is the only thing you can actually `install.packages()` today, I read the R source. The mechanism is "glimpse-then-simulate": a family of `glimpse*()` functions extracts per-column summaries from *real* ADaM data, and `simulate*()` draws synthetic values from those summaries.

```r
library(synadam)

# Scan real ADaM datasets, build a YAML study config (seed included)
yaml_path <- generate_study_config(
  adam_dir   = "path/to/adam",
  output_dir = "./syn_data",
  seed       = 42
)

# Deterministic simulation; syn_*.rds files land in output_dir
simulate_study(yaml_path)
```

*Listing 1: synadam quickstart. The zero-config scan plus seeded simulation is the whole workflow.*

What it preserves:

- **Structure and ranges.** Numeric and date columns are sampled uniformly between the observed min and max.
- **NA positions**, if you ask it to mirror them; IDs are regenerated sequentially.
- **Exact treatment + flag combination counts**, and Y/N proportions on flag columns.
- **User-declared joint combinations** via `ordered_col_sets` (e.g. REGION1/REGION1N stay paired).
- **A BDS spine**: per-subject PARAM/visit profiles are resampled and crossed with synthetic ADSL rows — ADSL-first propagation, so cross-dataset joins work.

What it does not preserve:

- **Marginal distributions.** `runif` between min and max means a bimodal or skewed lab value becomes flat. Only the range survives.
- **Category frequencies.** Character columns are uniformly resampled over unique values — an 80/20 sex split drifts toward 50/50.
- **Cross-PARAMCD plausibility.** AVAL min/max is computed across *all* PARAMCDs mixed together, so a lab test can draw values from another test's range.
- **Correlations and clinical constraints.** Nothing enforces AVAL vs. BASE vs. CHG coherence or AESTDY ≤ AEENDY unless you manually declare the relationships. There is no clinical-constraint layer at all.
- **No built-in fidelity evaluation** — no KS tests, chi-square, or divergence metrics to tell you how far off you drifted.
- **A privacy caveat**: the observed min/max are embedded in the summary, so the extremes of your real data leak into the synthetic output.

To be fair: for its actual use case — **de-identification, when you have real ADaM and cannot share it** — this trade-off is defensible. You're not asking it to invent a plausible trial; you're asking it to scramble one you already have. And the engineering is clean: S3 dispatch, checkmate input validation, seeds for determinism, YAML study configs, a version attribute on outputs, CRAN distribution. No LLM cost, no nondeterminism.

## synadam vs. our ML12 pipeline

Our [PhUSE US Connect 2025 paper ML12](/papers/phuse-2025-ml12.html) ("A Novel Pipeline for Generating Realistic Synthetic CDISC ADaM Datasets Using Large Language Models and Knowledge Graphs", Yan & Su, 2025; [PDF](/papers/PAP_ML12.pdf)) attacks the opposite problem: you have **no real data yet** — study-build testing, pipeline development before first patient in — and must generate from the spec alone. Spec → JSON schema → knowledge-graph enrichment (protocol/SAP/CRF queried block-by-block to inject ranges, derivations, allowed values) plus rule-based restructuring into ADSL/BDS/OCCDS → Faker-based, ADSL-first generation → formal evaluation via a composite Q score over ~13 sub-metrics (KS tests, chi-square, JS divergence on AEDECOD, AVAL–CHG correlation, temporal validity, cross-dataset USUBJID consistency).

| Dimension | synadam | ML12 pipeline |
|---|---|---|
| Goal | De-identify real ADaM you can't share | Spec-first generation when no real data exists |
| Input | Real ADaM datasets | ADaM spec + protocol/SAP/CRF |
| Method | Glimpse-then-simulate (uniform resampling) | KG-enriched schema + Faker templates |
| Marginal distributions | Not preserved (uniform min–max) | Injected from documentation knowledge |
| Category frequencies | Not preserved (~uniform) | Chi-square-validated against reference |
| Cross-variable relations | Only manually declared combos | Modeled (BDS blocks); weakest metric (0.38–0.65) |
| Clinical constraints | None enforced | Temporal validity checked; still only 50–65% in OCCDS |
| Built-in validation | None | Composite Q score, ~13 sub-metrics |
| Stack | R, CRAN, checkmate, YAML | Python, LLM, Faker, knowledge graph |
| Determinism / cost | Seeded, zero LLM cost | LLM-dependent, needs curated input documents |

*Table 2: synadam vs. our ML12 pipeline. Same problem family, opposite starting conditions.*

Two honest observations. First, the shared design: both systems independently arrived at **ADSL-first generation with subject propagation** into BDS/OCCDS. When two teams with opposite inputs converge on the same spine, that's probably a real constraint of the data model, not a coincidence. Second, the candid side: synadam cannot do clinical realism or self-validation — it was never meant to. And ML12's relationship score is its own weakest metric at every level (0.38 direct / 0.58 KG-enhanced / 0.65 template), temporal validity in OCCDS sat at 50–65%, and the whole thing degrades if the input documents are thin. Neither tool is a synthetic-data panacea; they bracket the problem from opposite ends.

## What the challenge means for our pipeline

Four concrete takeaways for our own stack:

1. **ARS is the emerging industry intermediate layer.** SAP-Genie emits ARS-conformant SAPs; TLFGenix builds ARS-aligned analysis specs; PAIR consumes the same standards chain; and CDISC's ARS repo is actually open. Our [Mock Shell Generator](/tools/mock-generator/) already exports cards-style ARD and tfrmt JSON — but ARD is not ARS. An ARS-conformant export for our spec/binding layer is now on the roadmap, not the wishlist.
2. **Borrow TLFGenix's evidence record + lineage graph.** Human approval of the spec before codegen, sign-off per TLF, and selective regeneration when the spec changes via a lineage graph — that is exactly the pattern a spec-change impact analysis needs, and it maps directly onto our deterministic-IR design.
3. **Leova's adversarial patients are the most transferable idea.** Synthetic "rule-breaker" records pushed through an EDC to verify edit checks is closed-loop testing in its purest form. We can generate boundary-violating records — AESTDY after AEENDY, out-of-range AVALs, orphaned USUBJIDs — specifically to stress our own data-readiness checks. Offense testing your own defense.
4. **Deterministic + human-gate remains defensible.** TLFGenix has six agents; agent count is not the metric that matters. The judges weighted traceability highest, and the runner-up in every use case had explicit human gates. Our Mock Shell Generator's confirm queue (BYO-key LLM suggests, never auto-writes) and the gxptlf engine's locked-reference replay with independent recompute sit squarely on the right side of that line.

## Key takeaways

- The 2026 CDISC AI Challenge drew 50 submissions from 30 organizations; winners present today in Denver. Standards integration and traceability were the top judging criteria.
- None of the six winning/runner-up solutions published code. The only installable artifact nearby is `Novartis/synadam` — which is *not* the winning Syn2Real.
- synadam's glimpse-then-simulate mechanism preserves structure, ranges, NA patterns, declared joint combos, and exact treatment counts — but not marginal distributions, category frequencies, cross-PARAMCD plausibility, correlations, or clinical constraints, and it embeds real min/max values (a privacy caveat). For de-identification, that's a defensible trade with clean engineering behind it.
- synadam and our ML12 pipeline solve opposite problems — de-identify data you have vs. generate data you don't — yet both converged on ADSL-first subject propagation. Each is weakest exactly where the other doesn't try: synadam has no fidelity metrics; ML12's relationship score is its own lowest component.
- ARS is the de facto intermediate layer of the 2026 winners; TLFGenix's evidence-record-plus-lineage-graph and Leova's adversarial rule-breaker patients are the two patterns worth borrowing now.
