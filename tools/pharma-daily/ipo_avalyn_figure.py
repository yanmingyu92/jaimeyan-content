"""One-off figure for the Avalyn IPO deep-dive (ipo-avalyn-2026):
AVLN documented closes Apr 30 – Sep 4, 2026 — execution milestones, not
newsflow, carried the stock past +100%. Dashed segments connect documented
closes, NOT a full daily series.
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
    ("2026-04-30", 29.49, "Debut close \\$29.49 (+63.8%)", 8, 4),
    ("2026-06-17", 29.31, "Jun 17: \\$29.31 — MIST\nenrollment completed (398 pts)", 8, -34),
    ("2026-06-18", 31.45, "Jun 18: \\$31.45 (+7.3%)", 8, 4),
    ("2026-07-16", 25.68, "Jul 16: \\$25.68 — lowest close", 6, -24),
    ("2026-08-14", 39.25, "Aug 14: \\$39.25 — highest close\n(Q2 print, runway into 2029)", -14, 8),
    ("2026-08-28", 34.69, "Aug 28: \\$34.69", -70, -28),
    ("2026-09-04", 37.39, "Sep 4: \\$37.39 (+107.7% vs offer)", -8, 10),
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
ax.text(dates[0], OFFER - 2.2, "\\$18.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(13, 46)
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

fig.text(0.03, 0.965, "Execution, not newsflow: AVLN doubled on",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "enrollment completed and a runway extension",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "AVLN key closes vs the 18.00 offer, Apr 30 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (AVLN); offer per Avalyn 424B4; events per company 8-K exhibits (Jun 17, Aug 12, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-avalyn-2026-execution.png"
fig.savefig(out, dpi=160)
print("wrote", out)
