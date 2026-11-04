"""One-off figure for the Eikon IPO deep-dive (ipo-eikon-2026):
documented EIKN price checkpoints vs the $18 offer, Feb–Sep 2026.
The decline was gradual (no single catalyst); dashed segments connect
documented closes, they are NOT a full daily series.
Data: Yahoo Finance daily series via research (key closes/highs/lows);
offer per pricing release. Not DB-driven — one-shot analysis figure.
"""
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

INK, INK_SOFT, INK_MUTE = "#1c1917", "#44403c", "#78716c"
PAPER, LINE = "#fbfaf8", "#e7e5e4"
TEAL, RED = "#0f766e", "#b91c1c"

OFFER = 18.00
# (date, price, label, dx, dy)
PTS = [
    ("2026-02-05", 15.00, "Debut close \\$15.00 (−16.7%)", 8, 6),
    ("2026-02-18", 16.26, "Feb 18: \\$16.26 — highest close,\nnever above offer", 8, 8),
    ("2026-04-28", 8.56, "Apr 28: \\$8.56 close,\nintraday trough \\$7.90", 6, -24),
    ("2026-06-10", 8.36, "Jun 10: \\$8.36 — lowest close", 10, -16),
    ("2026-08-03", 9.15, "Aug 3: \\$9.15 — lockup expiry\n(32.9M shares unlocked)", -6, 14),
    ("2026-08-28", 10.98, None, 0, 0),
    ("2026-09-04", 10.86, "Sep 4: \\$10.86 (−39.7%)", -4, 12),
]

dates = [dt.date.fromisoformat(p[0]) for p in PTS]
prices = [p[1] for p in PTS]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.065, 0.11, 0.865, 0.66])
ax.set_facecolor(PAPER)

ax.plot(dates, prices, color=RED, lw=1.6, ls=(0, (4, 3)), marker="o", ms=5,
        markerfacecolor=RED, markeredgecolor=RED, alpha=0.85)
ax.axhline(OFFER, color=INK_MUTE, lw=1.0, ls=(0, (5, 3)))
ax.text(dates[0], OFFER + 0.4, "\\$18.00 offer (top of range)", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "left" if dx >= 0 else "right"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(5, 21)
ax.set_xlim(dates[0] - dt.timedelta(days=6), dates[-1] + dt.timedelta(days=6))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "Priced at the top of range —",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "and EIKN never saw the offer price again",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "EIKN documented levels vs the 18.00 offer, Feb 5 – Sep 4, 2026 · dashed = checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (EIKN); offer per Eikon pricing release (Feb 4, 2026); lockup per Q2 2026 10-Q.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-eikon-2026-bleed.png"
fig.savefig(out, dpi=160)
print("wrote", out)
