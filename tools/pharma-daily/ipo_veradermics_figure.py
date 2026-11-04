"""One-off figure for the Veradermics IPO deep-dive (ipo-veradermics-2026):
MANE documented closes from debut to Sep 4, 2026 — the +479% was built
on two clinical data days. Dashed segments connect documented closes,
they are NOT a full daily series.
Data: Yahoo Finance daily series via research + stock_finance_data bars;
offer per pricing PR. Not DB-driven — one-shot analysis figure.
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
    ("2026-02-04", 37.75, "Debut close \\$37.75 (+122.1%)", 8, 4),
    ("2026-04-24", 67.84, "Apr 24: \\$67.84", -12, -20),
    ("2026-04-27", 100.10, "Apr 27: \\$100.10 (+47.6% in one day)\nStudy '302 male Ph2/3 topline", -14, -34),
    ("2026-04-29", 106.55, "Apr 29: follow-on\npriced at \\$100.00", 16, -46),
    ("2026-07-14", 110.17, "Jul 14: \\$110.17", 12, 14),
    ("2026-07-15", 123.70, "Jul 15: \\$123.70 (+12.3%)\nStudy '207 female cohort", -170, 12),
    ("2026-09-04", 98.51, "Sep 4: \\$98.51 (+479.5% vs offer)", -10, -22),
]

dates = [dt.date.fromisoformat(p[0]) for p in PTS]
prices = [p[1] for p in PTS]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.07, 0.11, 0.86, 0.66])
ax.set_facecolor(PAPER)

ax.plot(dates, prices, color=TEAL, lw=1.6, ls=(0, (4, 3)), marker="o", ms=5,
        markerfacecolor=TEAL, markeredgecolor=TEAL, alpha=0.9)
ax.axhline(OFFER, color=INK_MUTE, lw=1.0, ls=(0, (5, 3)))
ax.text(dates[0], OFFER - 6, "\\$17.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(0, 150)
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

fig.text(0.03, 0.965, "Two data days built the class's best tape:",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "MANE's +479% is catalysts, not momentum",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "MANE key closes vs the 17.00 offer, Feb 4 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series and stock_finance_data bars (MANE); offer and readouts per Veradermics releases (SEC EDGAR).",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-veradermics-2026-catalysts.png"
fig.savefig(out, dpi=160)
print("wrote", out)
