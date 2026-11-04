"""One-off figure for the Odyssey Therapeutics IPO deep-dive (ipo-odyssey-2026):
ODTX documented closes May 8 – Sep 4, 2026 — broke on debut, then re-rated
on the Q1 and Q2 earnings prints, not on new clinical data. Dashed segments
connect documented closes, NOT a full daily series.
Data: Yahoo Finance daily series via research; offer per 424B4.
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

OFFER = 18.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-05-08", 16.42, "Debut close \\$16.42 (-8.8%)", 4, -24),
    ("2026-06-16", 17.87, None, 0, 0),
    ("2026-06-18", 19.07, "Jun 18: \\$19.07 (+6.7% over 2 days\non Q1 print)", 8, 6),
    ("2026-07-08", 15.56, "Jul 8: \\$15.56 — lowest close", 6, -26),
    ("2026-08-03", 18.13, None, 0, 0),
    ("2026-08-06", 21.55, "Aug 6: \\$21.55 (+18.8% over 3 sessions\non Q2 print)", -14, 8),
    ("2026-08-28", 24.36, "Aug 28: \\$24.36", 8, -20),
    ("2026-09-04", 28.76, "Sep 4: \\$28.76 (+59.8% vs offer)\nhighest close", -8, 10),
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
ax.text(dt.date(2026, 7, 20), OFFER + 0.5, "\\$18.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(12.5, 32)
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

fig.text(0.03, 0.965, "Broke on debut, up 59.8% by September: ODTX",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "re-rated on earnings prints, not new clinical data",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "ODTX key closes vs the 18.00 offer, May 8 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (ODTX); offer per Odyssey 424B4; events per company 8-K exhibits (Jun 17, Aug 4, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-odyssey-2026-rebound.png"
fig.savefig(out, dpi=160)
print("wrote", out)
