"""One-off figure for the BlossomHill IPO deep-dive (ipo-blossomhill-2026):
BLSM documented closes Aug 7 – Sep 4, 2026 — a flat debut, then a four-week
grind to +37.6% on thin float; the biggest up-day (Aug 25) had no disclosed
catalyst. Dashed segments connect documented closes, NOT a full daily series.
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
    ("2026-08-07", 16.00, "Debut close \\$16.00 (0.0%;\nopened \\$15.75, below offer)", 8, 6),
    ("2026-08-18", None, None, 0, 0),  # placeholder removed below
    ("2026-08-20", 15.80, "Aug 20: \\$15.80 — lowest close\n(two days after Fast Track PR)", 6, -30),
    ("2026-08-25", 18.42, "Aug 25: \\$18.42 (+14.9% d/d,\nno disclosed catalyst)", -8, 12),
    ("2026-08-28", 19.56, "Aug 28:\n\\$19.56 (+22.25%)", 10, -38),
    ("2026-09-04", 22.01, "Sep 4: \\$22.01 (+37.6% vs offer)\n— highest close", -10, 8),
]
PTS = [p for p in PTS if p[1] is not None]

dates = [dt.date.fromisoformat(p[0]) for p in PTS]
prices = [p[1] for p in PTS]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.065, 0.11, 0.865, 0.66])
ax.set_facecolor(PAPER)

ax.plot(dates, prices, color=TEAL, lw=1.6, ls=(0, (4, 3)), marker="o", ms=5,
        markerfacecolor=TEAL, markeredgecolor=TEAL, alpha=0.9)
ax.axhline(OFFER, color=INK_MUTE, lw=1.0, ls=(0, (5, 3)))
ax.text(dates[0], OFFER - 0.55, "\\$16.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(14, 24.5)
ax.set_xlim(dates[0] - dt.timedelta(days=3), dates[-1] + dt.timedelta(days=3))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "A flat debut, then a quiet grind: BLSM added",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "+37.6% in four weeks on thin float",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "BLSM key closes vs the \\$16.00 offer, Aug 7 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (BLSM); offer per BlossomHill 424B4; Fast Track PR (Aug 18, 2026) per company release.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-blossomhill-2026-grind.png"
fig.savefig(out, dpi=160)
print("wrote", out)
