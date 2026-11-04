"""One-off figure for the AgomAb IPO deep-dive (ipo-agomab-2026):
AGMB documented closes Feb 6 - Sep 4, 2026 — a -39.9% trough and an 85%
rally with no clinical data anywhere in the window. Dashed segments connect
documented closes, NOT a full daily series.
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

OFFER = 16.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-02-06", 14.65, "Debut close \\$14.65 (-8.4%)", 8, 4),
    ("2026-03-26", 11.87, "Mar 26: \\$11.87 — AGMB-447\npatent PR day (-7.7%)", -10, -42),
    ("2026-06-12", 9.61, "Jun 12: \\$9.61 — lowest close (-39.9%)", -6, -26),
    ("2026-06-29", 17.82, "Jun 29: \\$17.82 — highest close (+11.4%)\n+85% in 17 days, no company news", -10, 10),
    ("2026-08-06", 13.50, "Aug 6: \\$13.50 (H1)", 10, -26),
    ("2026-08-28", 13.17, "Aug 28: \\$13.17 (-17.7%)", -6, -28),
    ("2026-09-04", 15.78, "Sep 4: \\$15.78 (-1.4% vs offer)", -6, 10),
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
ax.text(dates[0], OFFER + 0.25, "\\$16.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(8, 20.5)
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

fig.text(0.03, 0.965, "An 85% rally with no data behind it: AGMB's",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "round trip from -39.9% to near par",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "AGMB key closes vs the \\$16.00 offer, Feb 6 - Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (AGMB); offer per AgomAb 424B4; events per company 6-K exhibits and IR releases (2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-agomab-2026-roundtrip.png"
fig.savefig(out, dpi=160)
print("wrote", out)
