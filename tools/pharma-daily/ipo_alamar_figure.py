"""One-off figure for the Alamar IPO deep-dive (ipo-alamar-2026):
ALMR documented closes Apr 17 – Sep 4, 2026 — the +30.7% one-day re-rate
came on the Q2 print (82% revenue growth, first FY guidance), not on any
clinical event; the company has no drug pipeline. Dashed segments connect
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

OFFER = 17.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-04-17", 22.00, "Debut close \\$22.00\n(+29.4% vs offer)", 8, -32),
    ("2026-05-08", 23.96, "May 8: \\$23.96 — Q1:\nrevenue +99% Y/Y", 10, 8),
    ("2026-05-26", 19.09, "May 26: \\$19.09 — lowest close", 8, -30),
    ("2026-08-10", 27.99, "Aug 10: \\$27.99 (pre-print)", -16, 10),
    ("2026-08-11", 36.57, "Aug 11: \\$36.57 — highest close\n(+30.7% on Q2: +82% rev, FY guide)", -14, 10),
    ("2026-09-04", 30.80, "Sep 4: \\$30.80 (+81.2% vs offer)", -8, -55),
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
ax.text(dates[0], OFFER - 1.6, "\\$17.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(13, 44)
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

fig.text(0.03, 0.965, "The Q2 print, not the courtroom: ALMR re-rated",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "+30.7% in one session on 82% revenue growth",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "ALMR key closes vs the \\$17.00 offer, Apr 17 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (ALMR); offer per Alamar 424B4; events per company 8-Ks (May 8, Aug 10, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-alamar-2026-rerate.png"
fig.savefig(out, dpi=160)
print("wrote", out)
