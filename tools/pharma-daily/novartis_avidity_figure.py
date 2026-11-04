"""One-off figure for the Novartis-Avidity deal retrospective
(novartis-avidity-adc-2026): the $72.00 offer against the unaffected close and
30-day VWAP, with the three-program scorecard six months after closing.
Data: Avidity 8-K/10-K, Novartis releases. Not DB-driven — one-shot figure.
"""
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

INK, INK_SOFT, INK_MUTE = "#1c1917", "#44403c", "#78716c"
PAPER, LINE = "#fbfaf8", "#e7e5e4"
TEAL, RED, GOLD = "#0f766e", "#b91c1c", "#b45309"

BARS = [
    ("30-day VWAP", 44.42, INK_MUTE, ""),
    ("Unaffected close", 49.15, INK_SOFT, "Oct 24, 2025"),
    ("Novartis cash offer", 72.00, TEAL, "+46% vs close · +62% vs VWAP"),
]

SCORECARD = [
    ("del-zota · DMD44", "Filed; FDA priority review", TEAL),
    ("del-brax · FSHD", "Phase 1/2 biomarker win (Jun '26)", TEAL),
    ("del-desiran · DM1", "HARBOR Phase 3 miss (Sep 8 '26)", RED),
]

fig = plt.figure(figsize=(7.5, 5.0))  # 1200x800 @160dpi
fig.patch.set_facecolor(PAPER)

# Left panel: price ladder
ax = fig.add_axes([0.16, 0.16, 0.30, 0.58])
ax.set_facecolor(PAPER)
labels = [b[0] for b in BARS]
vals = [b[1] for b in BARS]
colors = [b[2] for b in BARS]
ypos = [0, 1, 2]
ax.barh(ypos, vals, height=0.52, color=colors, alpha=0.92)
for y, v, b in zip(ypos, vals, BARS):
    ax.text(v + 1.2, y, f"${v:.2f}", va="center", fontsize=9.5,
            color=INK, fontweight="bold")
    if b[3]:
        ax.text(v + 1.2, y - 0.26, b[3], va="center", fontsize=8.0, color=TEAL)
ax.set_yticks(ypos)
ax.set_yticklabels(labels, fontsize=8.5, color=INK_SOFT)
ax.set_xlim(0, 92)
ax.set_ylim(-0.55, 2.55)
ax.invert_yaxis()
ax.tick_params(axis="x", labelsize=8.0, colors=INK_MUTE, length=0)
ax.tick_params(axis="y", length=0)
for s in ("top", "right"):
    ax.spines[s].set_visible(False)
for s in ("left", "bottom"):
    ax.spines[s].set_color(LINE)
ax.grid(axis="x", color=LINE, lw=0.6)
ax.set_axisbelow(True)
ax.set_xlabel("USD per Avidity (RNA) share", fontsize=8.5, color=INK_MUTE)

# Right panel: scorecard
ax2 = fig.add_axes([0.545, 0.16, 0.42, 0.58])
ax2.set_facecolor(PAPER)
ax2.set_xlim(0, 1)
ax2.set_ylim(0, 1)
ax2.axis("off")
ax2.text(0.02, 0.97, "Six months after closing", fontsize=10, fontweight="bold",
         color=INK, va="top")
rows = [
    ("del-zota · DMD44", "Filed; FDA priority review", TEAL),
    ("del-brax · FSHD", "Phase 1/2 biomarker win (Jun '26)", TEAL),
    ("del-desiran · DM1", "HARBOR Phase 3 miss (Sep 8 '26)", RED),
]
y0 = 0.78
for name, status, c in rows:
    ax2.text(0.02, y0, name, fontsize=9, color=INK, fontweight="bold", va="top")
    ax2.text(0.06, y0 - 0.16, status, fontsize=8.5, color=c, va="top")
    ax2.plot([0.02, 0.98], [y0 - 0.30, y0 - 0.30], color=LINE, lw=0.6)
    y0 -= 0.36
ax2.text(0.02, 0.06, "NVS Sep 8 close $137.81, −13.9% vs Sep 4\nJefferies: failed program ≈ ⅓ of deal value",
         fontsize=8.0, color=INK_MUTE, va="bottom")

fig.text(0.03, 0.965, "A 46% premium bought three shots;",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.928, "six months in, two stand",
         fontsize=13, fontweight="bold", color=INK, ha="left", va="top")
fig.text(0.03, 0.892, "Novartis–Avidity: $72.00/share, ~$12.0B fully diluted · signed Oct 25, 2025 · closed Feb 27, 2026",
         fontsize=9.5, color=INK_MUTE, ha="left", va="top")
fig.text(0.03, 0.018, "Source: Avidity 8-K (Oct 27, 2025) and completion 8-K (Feb 27, 2026); FY2025 10-K; Novartis releases; NVS close per Yahoo Finance.",
         fontsize=7.5, color=INK_MUTE, ha="left", va="bottom")
fig.text(0.97, 0.052, "Pharma Daily · jaimeyan.com", fontsize=7.5, color=TEAL,
         ha="right", va="bottom", fontweight="bold")

out = "public/figures/novartis-avidity-adc-2026-deal.png"
fig.savefig(out, dpi=160)
print("wrote", out)
