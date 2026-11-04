"""One-off figure for the ivonescimab OS deep-dive (summit-ivonescimab-os-2026):
SMMT daily closes Apr 2025 - Sep 8, 2026 — the 2025 OS air pocket (-36% on the
interim 'trend', -30.5% on the global PFS win) and the 2026 OS significance
ruling (+17.3%). Data: Yahoo Finance daily series; events per Summit 8-Ks.
Not DB-driven — one-shot analysis figure.
"""
import datetime as dt

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

INK, INK_SOFT, INK_MUTE = "#1c1917", "#44403c", "#78716c"
PAPER, LINE = "#fbfaf8", "#e7e5e4"
TEAL, RED = "#0f766e", "#b91c1c"

df = pd.read_csv(
    r"C:/Users/yanmi/Downloads/NIW/portfolio/portfolio/portfolio/.tmp_research/summit-ivonescimab-os-2026/smmt_daily.csv",
    parse_dates=["Date"], index_col="Date",
)
df = df.dropna(subset=["Close"])
dates = df.index.to_pydatetime()
closes = df["Close"].astype(float).to_numpy()

EVENTS = [
    ("2025-04-24", 36.70, "Apr 24 '25: \\$36.70 — pre-interim-OS close", 6, 6),
    ("2025-04-25", 23.47, "Apr 25 '25: −36.0%\ninterim OS = 'trend' only", 12, -40),
    ("2025-05-30", 18.22, "May 30 '25: −30.5%\nglobal PFS win, OS open", 12, -30),
    ("2026-07-22", None, "Jul 22 '26: HARMONi OS\nupdate HR 0.76", -10, 44),
    ("2026-09-03", 17.13, "Sep 3 '26: +17.3%, 2.7x volume\nOS significance; HR undisclosed", -120, 8),
    ("2026-09-08", 17.64, "Sep 8: \\$17.64\nstill −52% vs Apr '25", -8, -32),
]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)
ax = fig.add_axes([0.065, 0.11, 0.865, 0.66])
ax.set_facecolor(PAPER)

ax.plot(dates, closes, color=TEAL, lw=1.2, alpha=0.95)
ax.fill_between(dates, closes, closes.min() * 0.92, color=TEAL, alpha=0.07)

for d_str, y, lab, dx, dy in EVENTS:
    d = pd.Timestamp(d_str)
    if y is None:
        y = float(df.loc[:d_str, "Close"].iloc[-1])
    ax.plot([d], [y], marker="o", ms=5, color=TEAL, markeredgecolor=TEAL, zorder=5)
    ha = "right" if dx < 0 else "left"
    ax.annotate(lab, xy=(d, y), xytext=(dx, dy), textcoords="offset points",
                fontsize=8.0, color=INK_SOFT, ha=ha,
                arrowprops=dict(arrowstyle="-", color=INK_MUTE, lw=0.6))

ax.set_ylim(10, 40)
ax.set_xlim(dates[0] - dt.timedelta(days=10), dates[-1] + dt.timedelta(days=14))
ax.xaxis.set_major_locator(mdates.MonthLocator(interval=3))
ax.xaxis.set_major_formatter(mdates.DateFormatter("%b\n%Y"))
ax.tick_params(labelsize=8.0, colors=INK_MUTE, length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="y", color=LINE, lw=0.6)
ax.set_axisbelow(True)
ax.set_ylabel("SMMT close (USD)", fontsize=8.5, color=INK_MUTE)

fig.text(0.03, 0.965, "The OS question cost Summit 52%; the answer bought back 21%",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "SMMT daily closes, Apr 2025 – Sep 8, 2026 · HARMONi-2 interim 'trend' (Apr '25) vs OS significance (Sep '26)",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Yahoo Finance daily series (SMMT); events per Summit Therapeutics 8-K filings. Moves are close-to-close; Sep 8, 2026 marked.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/summit-ivonescimab-os-2026-tape.png"
fig.savefig(out, dpi=160)
print("wrote", out)
