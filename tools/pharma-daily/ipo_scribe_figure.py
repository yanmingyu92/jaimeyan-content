"""One-off figure for the Scribe Therapeutics IPO deep-dive (ipo-scribe-2026):
SCTX documented closes Jul 24 – Sep 4, 2026 — a Phase 1 CRISPR platform that
nearly doubled vs offer on insider anchoring and analyst initiations, with no
post-IPO clinical data. Dashed segments connect documented closes, NOT a full
daily series. The Jul 24 debut close (~$21.65) is DERIVED from Jul 27's
-12.38% d/d change (no public feed carries the Jul 24 bar).
Data: stockanalysis.com / Yahoo Finance daily series via research; offer per
424B4; events per 10-Q and 8-K exhibits.
Not DB-driven — one-shot analysis figure.
"""
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

INK, INK_SOFT, INK_MUTE = "#1c1917", "#44403c", "#78716c"
PAPER, LINE = "#fbfaf8", "#e7e5e4"
TEAL, RED = "#0f766e", "#b91c1c"

OFFER = 15.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-07-24", 21.65, "Debut close ~\\$21.65\n(+44.3%, derived)", 4, 10),
    ("2026-07-27", 18.97, "Jul 27: \\$18.97", -6, -10),
    ("2026-07-28", 18.06, "Jul 28: \\$18.06 — lowest close", 12, -18),
    ("2026-08-05", 23.80, "Aug 5: \\$23.80", 6, -26),
    ("2026-08-18", 27.11, "Aug 18: \\$27.11 (+27.9% d/d,\nno company disclosure)", -10, 12),
    ("2026-08-24", 37.25, "Aug 24: \\$37.25\nhighest close (+148.3%)", -10, 10),
    ("2026-09-02", 30.90, "Sep 2: \\$30.90\n(Q2 print, +6.6% d/d)", -12, 8),
    ("2026-09-04", 28.67, "Sep 4: \\$28.67\n(+91.1% vs offer)", -10, -28),
]

dates = [dt.date.fromisoformat(p[0]) for p in PTS]
prices = [p[1] for p in PTS]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.065, 0.11, 0.865, 0.66])
ax.set_facecolor(PAPER)

ax.plot(dates, prices, color=TEAL, lw=1.6, ls=(0, (4, 3)), marker="o", ms=5,
        markerfacecolor=TEAL, markeredgecolor=TEAL, alpha=0.9)
ax.axhline(OFFER, color=INK_MUTE, lw=1.0, ls=(0, (5, 3)))
ax.text(dates[0], OFFER - 1.8, "\\$15.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(11, 44)
ax.set_xlim(dates[0] - dt.timedelta(days=5), dates[-1] + dt.timedelta(days=5))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "A platform story that got paid: SCTX nearly doubled",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "vs offer with no post-IPO clinical data",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "SCTX key closes vs the \\$15.00 offer, Jul 24 – Sep 4, 2026 · dashed = checkpoints",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: stockanalysis.com / Yahoo Finance daily series (SCTX); offer per 424B4; events per 10-Q and 8-K (Sep 2, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-scribe-2026-platform.png"
fig.savefig(out, dpi=160)
print("wrote", out)
