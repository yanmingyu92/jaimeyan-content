---
title: "Validation as a Release Gate: Building a GxP Governance Layer for Shiny at Kardigan"
date: 2026-09-28
description: "How I designed the governance and validation layer for ClinVista, an internal Shiny data-review platform — and why it survived the decision to replace the platform itself."
tags: ["shiny", "gxp", "validation", "clinical-programming", "r", "governance"]
kind: deep-dive
paperRef: pharmasug-2026-ai-201
canonicalPath: /blog/clinvista-gxp-shiny-governance.html
videoId: rdYYKhNtlwM
---

In mid-2026, Kardigan's statistical programming team faced a familiar small-biotech problem. We were adopting R and Shiny for clinical data review, our reviewers largely worked only in SAS, and every dashboard that touched a clinical decision needed to survive a simple question from QA: who validated this, and how do you know?

I built ClinVista to answer that question — a containerized Shiny platform behind corporate SSO, serving nine applications, with a vendor data service as the system of record. This post is not about the platform. It is about the governance and validation layer I designed around it, because that layer turned out to be the durable asset: when the company later decided to move the platform layer to Posit Connect, the governance framework had no replacement and carried over intact.

> **TL;DR** — I split validation into a platform layer (validated once, impact-assessed on change) and an application layer (per app, re-validated when data logic changes), made GxP classification a declared metadata field so validation depth scales with risk, and made a completed validation memo a hard release gate. The framework is GAMP 5 Category 4 thinking applied to Shiny, and it is the process counterpart to my QC research on double programming and AI-assisted validation.

## The problem

A small biotech does not have a validation department. It has a handful of programmers, a QA function that (rightly) asks hard questions, and a regulatory clock. The failure mode I was designing against was not a bad dashboard — it was the two ways teams usually respond to GxP pressure on Shiny apps: validate everything like it is submission-grade and drown in re-validation churn, or validate nothing and hope nobody asks. Neither survives contact with a real program.

The design constraint that shaped everything else: our users authorize against a vendor data service, and our reviewers think in SAS datasets and PROC COMPARE, not in R session logs. The governance layer had to meet both facts where they were.

## Design decisions worth defending

Each of these is stated as a decision plus the rationale, because the rationale is the part that transfers.

**Split validation into platform-level and application-level.** The platform — authentication enforcement, the data-access channel, deployment and rollback mechanics, logging, backups — is validated once and re-validated only by impact assessment when a listed trigger changes (auth flow, data channel, network exposure, deployment mechanics, infrastructure). Each application is validated separately, by its own maintainer, and re-validated whenever its data logic changes. The rationale: platform assurance stays stable instead of churning with every dashboard release, and correctness of numbers becomes personally owned by the person who wrote the derivations. Platform controls are referenced by app validations, never repeated.

![Two-layer validation split: one platform IQ/OQ report validated once, per-app validation memos scaled by GxP tier](/figures/clinvista-gxp-shiny-governance-validation-split.svg)

*Figure 1: The validation split. The platform layer is validated once and maintained by impact assessment; each application is validated at a depth set by its declared GxP tier.*

**Declare GxP classification in app metadata.** Every app carries a `classification` field — `exploratory`, `gxp-support`, or `gxp-critical` — in its metadata file, proposed by the app author, approved by the platform maintainer, and enforced by CI so only legal values survive a merge. Validation depth follows the tier: exploratory needs code review and passing tests; gxp-support adds a validation memo, an RTM, and an independent second-person re-check of key numbers; gxp-critical adds independent double programming with dual sign-off. Upgrades are always allowed; downgrades require a written rationale in the memo. The rationale: validation effort scales with declared risk instead of with whoever shouted loudest, and the decision tree takes thirty seconds to apply.

| Tier | Declaration means | Evidence required before release |
|---|---|---|
| `exploratory` | No clinical decisions depend on the output | Code review and passing tests |
| `gxp-support` | Internal clinical or scientific decisions rely on it | Validation memo, RTM, and an independent second-person re-check of key numbers |
| `gxp-critical` | Regulated submission or decision input | The above, plus independent double programming with dual sign-off |

*Table 1: Validation depth follows the declared GxP tier. Upgrades are always allowed; downgrades require a written rationale in the memo.*

![GxP classification decision tree: regulated submission or decision leads to gxp-critical, internal clinical or scientific decisions to gxp-support, otherwise exploratory](/figures/clinvista-gxp-shiny-governance-classification-tree.svg)

*Figure 2: The classification decision tree. Two questions assign every app to a tier, and the tier fixes the required evidence before development starts.*

**No memo, no release.** Validation is a release gate, not after-the-fact paperwork. Merging code exposes nothing by itself; an application becomes reachable only through an explicit whitelist action, and a gxp-support or gxp-critical app is not whitelisted until its validation memo is complete, signed, and reviewed. The rationale: if the gate is the paperwork, the paperwork cannot be skipped — and an auditor can reconstruct any release decision from records that already exist.

![Four control gates between a code change and a production user, with the release whitelist checking for a completed validation memo](/figures/clinvista-gxp-shiny-governance-release-gates.svg)

*Figure 3: Four gates between a code change and a user. Merging code is not a release; visibility is a separate act that checks the validation memo first.*

**Separation of duties.** The person who writes an app cannot approve its release to users. Classification approval, release decisions, and whitelist changes are platform-maintainer actions, distinct from authorship; gxp-critical work requires a QC programmer who must be a different person than the production programmer. On a small team this is the decision people push back on, and it is the one I would defend first: self-approval is where small-team GxP programs quietly die.

**No shadow authorization.** The platform keeps no permission database of its own. Per-user data authorization is enforced server-side by the system of record, so revoking someone's access takes effect without any platform-side change, and there is exactly one place where access decisions live. The rationale: every shadow ACL is a future audit finding, because it will drift from the real one.

**Disclosure-tiered documentation.** Implementation and operational detail stays in privately maintained documents; the shared application repository carries what app teams need; the governance repository contains no code, no secrets, and is safe for stakeholder reading — its architecture document states up front what it deliberately does not contain. The rationale: governance documents that are safe to read get read, and the ones that get read get followed.

## What I would do differently

I would buy the platform layer and keep the governance layer. That is now the plan of record at Kardigan — Posit Connect for hosting, an internal R package for team tooling — and it is the right call, not a retreat.

The engineering judgment is this: the platform layer (SSO wiring, container orchestration, routing, process management) is undifferentiated work that a vendor does better and patches faster, and every hour I spent on it was an hour not spent on the layer where the actual risk lives. The governance layer is the opposite. No commercial product ships your classification rubric, your memo gates, your independence rules for QC programming, or your Part 11 story, because those are decisions about *your* risk appetite and *your* data flows. A hosting platform gives you audit logs and access controls as primitives; deciding what they must guarantee, and proving it, remains yours.

If I were starting today, I would write the governance framework first, platform-agnostic from day one, and treat whatever sits underneath it — bespoke containers or Posit Connect — as an implementation detail the framework references but does not depend on. That is also why the Part 11 mapping in the open-source template derived from this work is written for both hosting models.

## The research program connection

This governance framework did not come out of nowhere, and it is not separate from my published work — it is the process layer of the same program.

The double-programming rules I applied to gxp-critical apps — the QC programmer works from the specification alone, comparison happens on the datasets behind the numbers rather than on screenshots, independence is a property you protect rather than assume — are the same independence constraints I studied in our [PharmaSUG 2026 AI-201 paper](/papers/pharmasug-2026-ai-201.html) on AI-assisted QC code generation ([companion post](/blog/eliminating-qc-programming-duplication.html)). That paper asks whether an LLM can generate *independent* QC code without the usual duplication cost; the governance framework is where that question stops being academic, because the framework defines what "independent" must mean before any tool, AI or human, is allowed to claim it.

[CAVE-Onc](/papers/cave-onc.html) (PLOS One, 2026) is the other side of the same coin: deterministic, machine-checkable validation rules catching cross-domain contradictions that manual review misses. The classification rubric and RTM machinery in this framework are how that kind of automated checking gets a mandated seat in a release process instead of remaining an optional extra.

Read together, the three threads — AI-assisted QC, deterministic validation, and governance-as-release-gate — are one research program: how a small team gets regulatory-grade confidence out of modern tooling without enterprise headcount.

## Where this honestly stands

What the record shows: nine Shiny applications on the platform architecture; the application repository's onboarding pipeline exercised end-to-end with its first app at the gxp-support tier; and the platform validation report still in draft when the platform decision arrived. I am not going to dress up adoption numbers I cannot back — if I add metrics here later (apps validated per tier, users served, effort saved), each will carry its source. The framework's value is not in a deployment count — it is that when the platform underneath was swapped, not one governance decision had to be revisited.

## Key takeaways

- Split validation into a stable platform layer and a per-app layer, or every dashboard release becomes a platform re-validation.
- Put GxP classification in machine-readable metadata, and let CI refuse anything else — policy that is not enforced at merge time is a suggestion.
- Make the validation memo the release gate. Paperwork that gates deployment cannot be skipped; paperwork that follows it will be.
- Keep no shadow permissions. One system of record for authorization, enforced server-side, makes revocation free and audits short.
- Buy the platform, keep the governance. Vendors sell hosting primitives; your validation story is yours to design and to defend.

## FAQ

### Is ClinVista open source?

No. The platform and its code remain private. What I have released separately is [shiny-gxp-governance](https://github.com/yanmingyu92/shiny-gxp-governance), a generic, company-neutral governance and validation template — the methodology, rewritten for any small biotech — containing no company code, configuration, or documents.

### Does this apply if we already use Posit Connect?

Yes, and that is the point of the "what I would do differently" section. The framework treats the hosting platform as a replaceable layer: Connect gives you authentication, audit logs, and content versioning as primitives, and the governance framework defines what those primitives must guarantee and how you evidence it. The template's Part 11 mapping is written for both hosting models.

### How does this relate to the R Validation Hub?

It complements their published scope. The Hub's risk-based framework covers R *packages* and explicitly leaves infrastructure validation and environment governance to each organization. This framework covers the adjacent layer — application-level validation and platform governance — and assumes package risk assessment per the Hub's approach as an input.

---

*No employer code, configuration, data, or operational detail appears in this article. Architectural descriptions are at the methodology level; the governance documents referenced follow the same disclosure discipline described above. The open-source template derived from this work is a framework, not validated software — adopting it does not by itself confer compliance, and its outputs require independent qualified review.*
