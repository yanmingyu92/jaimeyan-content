"""One-off figure for the Attovia IPO deep-dive (ipo-attovia-2026):
ATTO documented closes Aug 5 – Sep 4, 2026 — the stock never closed below
its $17.00 offer; the September leg followed the Q2 print and the runway
extension into 2030. Dashed segments connect documented closes, NOT a full
daily series.
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

OFFER = 17.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-08-05", 21.90, "Debut close \\$21.90 (+28.8%)", 8, 6),
    ("2026-08-06", 20.38, "Aug 6: \\$20.38 — full\ngreenshoe closed", 10, -30),
    ("2026-08-12", 18.06, "Aug 12: \\$18.06 — lowest close (+6.2%)", 0, -38),
    ("2026-09-01", 22.22, "Sep 1: \\$22.22", -6, -26),
    ("2026-09-02", 23.13, "Sep 2: \\$23.13 — Q2 print,\nrunway into 2030 (+4.1%)", -78, 6),
    ("2026-09-04", 25.55, "Sep 4: \\$25.55 — highest close\n(+50.3% vs offer)", -10, 8),
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
ax.text(dates[0], OFFER - 0.7, "\\$17.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(15.5, 28.5)
ax.set_xlim(dates[0] - dt.timedelta(days=3), dates[-1] + dt.timedelta(days=3))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0, interval=1))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "Never below offer: ATTO's Phase 1b itch data",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "held the premium into a runway-extension print",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "ATTO key closes vs the \\$17.00 offer, Aug 5 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (ATTO); offer per Attovia 424B4; events per company PRs and 8-K exhibits (Aug 6, Sep 2, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-attovia-2026-aftermarket.png"
fig.savefig(out, dpi=160)
print("wrote", out)
