"""One-off figure for the Aktis Oncology IPO deep-dive (ipo-aktis-2026):
AKTS documented closes from debut to Sep 4, 2026 — the 2026 opener set
the class playbook: top-of-range, strategic anchor, full greenshoe.
Dashed segments connect documented closes, NOT a full daily series.
Data: stock_finance_data daily bars (debut detail) + Yahoo Finance
daily series via research; offer per pricing PR. One-shot figure.
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
    ("2026-01-09", 22.40, "Debut: opened \\$27.00 (+50%),\nclosed \\$22.40 (+24.4%)", 10, 6),
    ("2026-03-27", 15.19, "Mar 27: \\$15.19 — lowest close\n(−15.6% vs offer)", 10, -22),
    ("2026-06-30", 32.23, "Jun 30: \\$32.23 — highest close,\nASCO window re-rate", -12, 8),
    ("2026-08-28", 25.78, "Aug 28: \\$25.78", -60, -26),
    ("2026-09-04", 27.05, "Sep 4: \\$27.05 (+50.3% vs offer)", -6, 12),
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
ax.text(dates[0], OFFER - 1.6, "\\$18.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(11, 37)
ax.set_xlim(dates[0] - dt.timedelta(days=8), dates[-1] + dt.timedelta(days=8))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "The 2026 opener wrote the playbook:",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "top of range, a Lilly anchor, and a pop that held",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "AKTS key closes vs the 18.00 offer, Jan 9 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: stock_finance_data and Yahoo Finance daily series (AKTS); offer per Aktis pricing release; Lilly tranche per Lilly Schedule 13D.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-aktis-2026-playbook.png"
fig.savefig(out, dpi=160)
print("wrote", out)
