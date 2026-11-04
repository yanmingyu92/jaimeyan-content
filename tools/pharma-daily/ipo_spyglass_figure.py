"""One-off figure for the SpyGlass IPO deep-dive (ipo-spyglass-2026):
SGP documented closes Feb 6 – Sep 4, 2026 — the pop held, a June scare
nearly round-tripped to the offer, then a quiet grind back.
Dashed segments connect documented closes, NOT a full daily series.
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

OFFER = 16.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-02-06", 26.40, "Debut close \\$26.40 (+65.0%)", 6, 6),
    ("2026-02-19", 29.68, "Feb 19: \\$29.68 — highest close", 8, 8),
    ("2026-06-16", 17.56, "Jun 16: \\$17.56 — lowest close,\n+9.8% above offer", 8, -10),
    ("2026-08-28", 26.42, "Aug 28: \\$26.42", -30, -28),
    ("2026-09-04", 28.94, "Sep 4: \\$28.94 (+80.9% vs offer)", -6, 10),
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
ax.text(dates[0], OFFER - 1.7, "\\$16.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(12, 34)
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

fig.text(0.03, 0.965, "The pop held, the June scare came within",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "10% of the offer — and the tape ground back",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "SGP key closes vs the 16.00 offer, Feb 6 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance and stock_finance_data daily series (SGP); offer per SpyGlass pricing release (Feb 5, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-spyglass-2026-grind.png"
fig.savefig(out, dpi=160)
print("wrote", out)
