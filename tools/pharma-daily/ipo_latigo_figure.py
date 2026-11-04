"""One-off figure for the Latigo IPO deep-dive (ipo-latigo-2026):
LTGO documented closes Aug 7 – Sep 4, 2026 — a +1.4% debut, then a 29.5%
climb (Aug 19 -> Aug 27) on no disclosed company catalyst. Dashed segments
connect documented closes, NOT a full daily series.
Data: Yahoo Finance daily series via research; offer per 424B4; events per
company 8-K exhibits and the Q2 2026 10-Q.
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
    ("2026-08-07", 18.25, "Debut close \\$18.25 (+1.4%)\n— also the lowest close", 4, -24),
    ("2026-08-19", 19.30, "Aug 19: \\$19.30 — last close\nbefore the run", -8, 10),
    ("2026-08-27", 25.00, "Aug 27: \\$25.00 — highest close (+38.9%)\nno disclosed catalyst", -6, 10),
    ("2026-08-31", 22.02, "Aug 31: \\$22.02", -10, -18),
    ("2026-09-03", 22.48, "Sep 3: \\$22.48 — Q2 print\nrunway into 2029", 8, -24),
    ("2026-09-04", 23.04, "Sep 4: \\$23.04\n(+28.0% vs offer)", 8, 6),
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
ax.text(dates[-1] + dt.timedelta(days=5), OFFER - 0.9, "\\$18.00 offer",
        fontsize=8.5, color=INK_MUTE, ha="right")

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(15.5, 27.5)
ax.set_xlim(dates[0] - dt.timedelta(days=2), dates[-1] + dt.timedelta(days=6))
ax.xaxis.set_major_locator(mdates.DayLocator(interval=7))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))
ax.tick_params(labelsize=8.5, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)

fig.text(0.03, 0.965, "A quiet debut, then a 29.5% six-session climb",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "with no disclosed company catalyst",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "LTGO documented closes vs the \\$18.00 offer, Aug 7 – Sep 4, 2026 · checkpoints, not a daily series",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (LTGO); offer per 424B4; greenshoe and runway per Q2 2026 10-Q / Sep 3, 2026 release.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-latigo-2026-rally.png"
fig.savefig(out, dpi=160)
print("wrote", out)
