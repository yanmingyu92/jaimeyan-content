"""One-off figure for the Apnimed IPO deep-dive (ipo-apnimed-2026):
APMD documented closes Jul 31 - Sep 4, 2026 — a +56% debut and a doubled
peak with no disclosed company news; the stock trades on the Feb 2027 PDUFA.
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

OFFER = 16.00
# (date, close, label, dx, dy)
PTS = [
    ("2026-07-31", 25.00, "Debut close \\$25.00 (+56.3%)", 8, 4),
    ("2026-08-11", 24.87, "Aug 11: \\$24.87 — lowest close", -6, -30),
    ("2026-08-17", 32.55, "Aug 17: \\$32.55 — highest close", -4, 10),
    ("2026-08-20", 28.55, "Aug 20: \\$28.55\n(−10.2%, no disclosed news)", 2, -32),
    ("2026-08-31", 26.25, "Aug 31: \\$26.25 (−11.6% day,\nno disclosed news)", 10, -30),
    ("2026-09-04", 27.45, "Sep 4: \\$27.45\n(+71.6% vs offer)", -8, 12),
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
ax.text(dates[0], OFFER - 1.6, "\\$16.00 offer", fontsize=8.5, color=INK_MUTE)

for (d, p, lab, dx, dy), x, y in zip(PTS, dates, prices):
    if lab:
        ha = "right" if dx < 0 else "left"
        ax.annotate(lab, xy=(x, y), xytext=(dx, dy), textcoords="offset points",
                    fontsize=8.5, color=INK_SOFT, ha=ha)

ax.set_ylim(12, 38)
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

fig.text(0.03, 0.965, "A +56% debut and a doubled peak on no news:",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "APMD trades on a February 2027 PDUFA date",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "APMD key closes vs the \\$16.00 offer, Jul 31 – Sep 4, 2026 · dashed = documented checkpoints, not daily",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (APMD); offer per Apnimed 424B4; EDGAR shows no company news around the Aug swings.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/ipo-apnimed-2026-pdufa.png"
fig.savefig(out, dpi=160)
print("wrote", out)
