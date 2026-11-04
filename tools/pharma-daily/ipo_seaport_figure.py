"""One-off figure for the Seaport IPO deep-dive (ipo-seaport-2026):
SPTX documented closes May 1 – Sep 4, 2026 — below offer for two weeks,
then re-rated on GlyphAgo data and the Q2 print; the biggest single-day
jump (Aug 26) has no disclosed catalyst. Dashed segments connect
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

OFFER = 18.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-05-01", 19.84, "Debut close \\$19.84 (+10.2%)", 8, 6),
    ("2026-05-11", 15.25, "May 11: \\$15.25 — lowest close\n(-15.3% vs offer)", 10, -26),
    ("2026-06-09", 17.66, "Jun 9: \\$17.66 (+9.0% on\nGlyphAgo MAD + Q1 8-K)", 8, -30),
    ("2026-08-04", 21.43, "Aug 4: \\$21.43 (post-Q2 print,\nrunway into 2029)", -12, 10),
    ("2026-08-26", 27.84, "Aug 26: \\$27.84 — highest close\n(+12.1%, no disclosed catalyst)", -10, 8),
    ("2026-08-28", 24.04, "", 0, 0),
    ("2026-09-04", 24.86, "Sep 4: \\$24.86\n(+38.1% vs offer)", -8, -46),
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
ax.text(dt.date(2026, 5, 22), OFFER + 0.5, "\\$18.00 offer",
        fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(11, 32)
ax.set_xlim(dates[0] - dt.timedelta(days=6), dates[-1] + dt.timedelta(days=8))
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "Back above water: SPTX rebuilt a +38% gain on data,",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "but its biggest daily jump had no disclosed catalyst",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "SPTX key closes vs the \\$18.00 offer, May 1 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (SPTX); offer per Seaport 424B4; events per company 8-K exhibits (Jun 8, Aug 3, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-seaport-2026-tape.png"
fig.savefig(out, dpi=160)
print("wrote", out)
