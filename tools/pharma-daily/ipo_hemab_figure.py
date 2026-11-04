"""One-off figure for the Hemab IPO deep-dive (ipo-hemab-2026):
COAG documented closes May 1 – Sep 4, 2026 — a staircase of disclosed
events. Dashed segments connect documented closes, NOT a daily series.
Data: Yahoo Finance + stock_finance_data series via research; offer per
pricing PR. Not DB-driven — one-shot analysis figure.
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
    ("2026-05-01", 34.00, "Debut close \\$34.00 (+88.9%)", 8, 4),
    ("2026-06-12", 24.98, "Jun 12: \\$24.98\nlowest close", 6, -26),
    ("2026-06-29", 36.73, "Jun 29: \\$36.73 (+13.5%)\nISTH presentations announced", 4, 10),
    ("2026-07-14", 43.31, "Jul 14: \\$43.31 (+9.6%)\nISTH sutacimig data", -150, -6),
    ("2026-08-14", 54.94, "Aug 14: \\$54.94 — highest close\n(Aug 11: HMB-002 data + FDA Ph3 nod)", -14, 8),
    ("2026-09-04", 44.41, "Sep 4: \\$44.41 (+146.7% vs offer)", -30, -42),
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
ax.text(dates[0], OFFER - 2.6, "\\$18.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(12, 64)
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

fig.text(0.03, 0.965, "Every leg up came with a data print:",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "COAG's +147% is a staircase of disclosed events",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "COAG key closes vs the 18.00 offer, May 1 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance and stock_finance_data daily series (COAG); offer per Hemab pricing release; events per company releases.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-hemab-2026-stairs.png"
fig.savefig(out, dpi=160)
print("wrote", out)
