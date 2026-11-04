"""One-off figure for the Vogenx IPO deep-dive (ipo-vogenx-2026):
VOGX documented closes Aug 12 – Sep 4, 2026 — a +161% climb on zero
company disclosures; the only dated event was the greenshoe close.
Dashed segments connect documented closes, NOT a full daily series.
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

OFFER = 13.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-08-12", 13.00, "Debut close \\$13.00 (0.0%)", 8, 6),
    ("2026-08-18", 19.75, "Aug 18: \\$19.75", -10, 10),
    ("2026-08-19", 23.16, "Aug 19: \\$23.16 — greenshoe\nclosed (full 15%)", 10, -4),
    ("2026-08-28", 33.96, "Aug 28: \\$33.96 (+161.2%)", 8, -40),
    ("2026-08-31", 34.00, "Aug 31: \\$34.00 — highest close", -10, 12),
    ("2026-09-04", 31.73, "Sep 4: \\$31.73 (+144.1% vs offer)", -8, -32),
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
ax.text(dates[0], OFFER - 1.6, "\\$13.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(9, 40)
ax.set_xlim(dates[0] - dt.timedelta(days=2), dates[-1] + dt.timedelta(days=3))
ax.xaxis.set_major_locator(mdates.WeekdayLocator(byweekday=0))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "No news, just float: VOGX tripled in under four",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "weeks on zero company disclosures",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "VOGX key closes vs the \\$13.00 offer, Aug 12 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (VOGX); offer per Vogenx 424B4; greenshoe close per company 8-K (Aug 19, 2026).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-vogenx-2026-float.png"
fig.savefig(out, dpi=160)
print("wrote", out)
