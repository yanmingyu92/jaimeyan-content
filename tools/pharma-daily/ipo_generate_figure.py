"""One-off figure for the Generate Biomedicines IPO deep-dive (ipo-generate-2026):
GENB documented closes from debut to Sep 4, 2026 — the class's worst debut
repaired on execution, then an ERS poster-leak spike and instant retrace.
Dashed segments connect documented closes, NOT a full daily series.
Data: Yahoo Finance daily series via research; offer per pricing PR.
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
    ("2026-02-27", 12.65, "Debut close \\$12.65 (−20.9%)\nworst first day of 2026", 8, 6),
    ("2026-03-06", 11.21, "Mar 6: \\$11.21 — lowest close", 10, -20),
    ("2026-06-26", 16.47, "Jun 26: \\$16.47\nback above offer", -10, -30),
    ("2026-08-13", 15.03, "Aug 13: \\$15.03", -80, -30),
    ("2026-08-25", 20.38, "Aug 25: \\$20.38 (+15.0%)\nERS posters posted early", -10, 10),
    ("2026-08-28", 15.33, "Aug 28: \\$15.33", -14, -36),
    ("2026-09-04", 16.39, "Sep 4: \\$16.39 (+2.4% vs offer)", -8, 16),
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
ax.text(dates[0], OFFER + 0.3, "\\$16.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(9, 23)
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

fig.text(0.03, 0.965, "The worst debut of 2026 repaired itself on",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "execution — and the ERS spike did not hold",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "GENB key closes vs the 16.00 offer, Feb 27 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (GENB); offer per Generate Biomedicines pricing release (Feb 26, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-generate-2026-repair.png"
fig.savefig(out, dpi=160)
print("wrote", out)
