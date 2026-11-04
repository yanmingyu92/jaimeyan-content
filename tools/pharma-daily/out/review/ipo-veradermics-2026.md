# Review — `content/posts/ipo-veradermics-2026.md`

Adversarial fact-check against the article's linked sources (no data pack provided).
Report-only per instruction; the draft was not modified.

## Violations

1. **Study '306 enrollment — draft says n=552; a cited source says 556.**
   - Draft: "Study '306 (Phase 2/3, females; NCT07146022, n=552)".
   - Evidence: the linked Q2 2026 results release (EX-99.1) says "a 556 participant,
     registration-directed trial" and "in 556 female participants" (enrollment complete).
     The registry NCT07146022 reports `enrollmentInfo.count = 552` but typed `ESTIMATED`
     — the original target, not the completed enrollment.
   - The draft uses the stale registry target while the company's own most-recent
     filing (also cited in the draft) says 556. Should be 556, or explicitly note
     the registry's 552 is the pre-completion estimate.

2. **Study '302 headline n — 480 in body, 519 in FAQ, no reconciliation.**
   - Draft body: "n=480 per registry". Draft FAQ: "a 519-patient male Phase 2/3".
   - Evidence: registry NCT06724614 = 480 `ESTIMATED`; the April 27 8-K and 424B4 =
     "Study '302 enrolled 519 patients". The actual enrolled count is 519; 480 is the
     registry estimate. Presenting 480 in the body while the FAQ uses 519 is internally
     inconsistent and understates the real trial size.

3. **Study '304 enrollment — draft says n=480; the 424B4 says 498.**
   - Draft: "Study '304 (Phase 3, males; NCT06972264, n=480)".
   - Evidence: registry NCT06972264 = 480 `ESTIMATED`; the linked 424B4 says the
     confirmatory Phase 3 is "targeting the enrollment of 498 male patients". Same
     stale-registry-vs-filing conflict as above.

4. **Study '207 mischaracterized as "female Phase 2".**
   - Draft: "The open-label female Phase 2 (Study '207)".
   - Evidence: the July 15 8-K "About Study '207" describes it as a Phase 2 open-label
     study in "21 adult male and 28 adult female" patients; registry NCT06527365 title
     is "Males and Females With AGA". The July 15 results are the female cohort only.
     "female Phase 2" reads as a female-only study.

## Notes (lower severity, no rewrite applied)

5. **Follow-on share count.** The table lists 4,420,358 shares without noting that this
   includes the 576,568-share greenshoe; the base per the May 1 8-K was 3,843,790 shares.
   The $442.0M is correct (base + full greenshoe, confirmed in the Q2 10-Q), but the row
   lacks the "greenshoe included" annotation the IPO rows carry.

6. **VDMN wording.** 424B4 says "dissolvable microarray patch"; draft says "microneedle
   patch". Close but not verbatim.

7. **Price/volume figures are not traceable to any linked URL.** First-day close $37.75,
   the Apr 24/27, Jul 14/15/16, Aug 28 closes, the Sep 4 close $98.51, volume 363,236,
   and the derived +479.5% / +47.6% / +12.3% / −20% all cite "Yahoo Finance daily series"
   and the "stock_finance_data feed" in the provenance footer rather than a fetchable
   source. Internal arithmetic is consistent; the raw closes could not be re-verified
   against the linked evidence base.

## Clean checks

- Voice/QC: `scripts/blog-qc.mjs` reports 0 errors / 0 warnings; no banned phrases.
- Internal `/blog/` links (biotech-ipo-class, ipo-eikon-2026, ipo-kailera-2026) all target
  published posts (no `draft: true`); the Aktis/Lilly ~$100M cross-reference matches the
  parent post.
- Verified against sources: IPO 15,077,647 sh @ $17.00 = $256.3M; greenshoe full →
  17,339,294 sh, $294.8M gross / $269.1M net; range 13,350,000 sh @ $14–16; Lilly anchor
  ≤4.9%; follow-on $442.0M gross / ≈$414.3M net; placement 300,000 @ $99.99999 = $30.0M
  ("Montanova Capital (formerly known as Suvretta Capital)"); syndicate Jefferies/Leerink/
  Citigroup/Cantor; Study '302 +30.3/+33.0 vs +7.3 (p<0.0001), 48.4%/62.9% vs 13.4%,
  Month-2 separation, no TRSAEs/no cardiac AESIs; Study '207 +22.7/+23.3 and 88.9%/90.0%;
  cash $819.9M at Jun 30, Q2 net loss $23.5M on $18.6M R&D, runway into 2030; founded 2019
  by dermatologists Reid Waldman and Tim Durso; patent 2043; pipeline (wart patch,
  molluscum antiviral gel, alopecia areata topical).

VERDICT: needs-human
