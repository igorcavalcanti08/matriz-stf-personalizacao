import csv, math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

rows = list(csv.DictReader(open('figura1_dados.csv', encoding='utf-8')))
lanes = ['STF', 'Congresso', 'Constituinte', 'Outro']          # de cima para baixo
lane_y = {l: len(lanes) - 1 - i for i, l in enumerate(lanes)}
CAT = 'Efeito sobre os poderes individuais'
style = {
    'Ampliação forte': ('#b2182b', 3),
    'Ampliação forte com restrição (mista)': ('#ef8a62', 3),
    'Ampliação leve': ('#f4b183', 2),
    'Restrição': ('#2166ac', 3),
    'Sem efeito sobre os poderes individuais': ('#c8c8c8', 1),
}
order = list(style)

W_IN, H_IN = 6.7, 4.2
x0, x1 = 1885, 2028
fig, ax = plt.subplots(figsize=(W_IN, H_IN), dpi=300)
plt.rcParams['font.family'] = 'DejaVu Sans'

# beeswarm simples: posição em mm para evitar sobreposição
ax_w_mm = W_IN * 25.4 * 0.80
mm_per_year = ax_w_mm / (x1 - x0)
D = 2.1            # diâmetro do ponto em mm
lane_h_mm = 13.0   # altura útil de cada faixa em mm
placed = {l: [] for l in lanes}
raw = []
rows.sort(key=lambda r: (style[r[CAT]][1], int(r['Ano'])), reverse=True)
for r in rows:
    l = r['Autor formal']; xm = (int(r['Ano']) - x0) * mm_per_year
    off = 0.0; k = 0
    while not all((xm - px) ** 2 + (off - py) ** 2 >= D ** 2 for px, py in placed[l]):
        k += 1; off = ((k + 1) // 2) * (D * 0.5) * (1 if k % 2 else -1)
    placed[l].append((xm, off)); raw.append((int(r['Ano']), l, off, r[CAT]))
ext = {l: max([abs(o) for _, o in placed[l]] + [0]) for l in lanes}
centers = {}; ycur = 0.0; PAD = 2.6
for l in reversed(lanes):
    ycur += max(ext[l], 1.2) + PAD; centers[l] = ycur; ycur += max(ext[l], 1.2)
YTOP = ycur + PAD
pts = [(a, centers[l] + o, c) for a, l, o, c in raw]
for cat in reversed(order):
    xs = [p[0] for p in pts if p[2] == cat]; ys = [p[1] for p in pts if p[2] == cat]
    ax.scatter(xs, ys, s=(D * 2.83) ** 2 * 0.62, c=style[cat][0], edgecolors='white', linewidths=0.4, zorder=3 if cat != order[-1] else 2)
for l in lanes:
    ax.axhline(centers[l], color='#e6e6e6', lw=0.6, zorder=1)
for yr, lab in [(1970, 'Regimento\nde 1970'), (1988, 'Constituição\nde 1988')]:
    ax.axvline(yr, color='#7f7f7f', lw=0.6, ls=(0, (3, 2)), zorder=1)
    ax.text(yr - 1.2, YTOP - 0.3, lab, ha='right', va='top', fontsize=6.3, color='#555555', linespacing=1.1)

ax.set_yticks([centers[l] for l in lanes])
ax.set_yticklabels(lanes, fontsize=8)
ax.set_xlim(x0, x1); ax.set_ylim(0, YTOP + 3.5)
ax.set_xticks([1890, 1910, 1930, 1950, 1970, 1990, 2010, 2023])
ax.tick_params(axis='x', labelsize=7.5, length=2.5, color='#999999')
ax.tick_params(axis='y', length=0)
for s in ['top', 'right', 'left']: ax.spines[s].set_visible(False)
ax.spines['bottom'].set_color('#999999'); ax.spines['bottom'].set_linewidth(0.6)
ax.set_xlabel('Ano da norma', fontsize=7.5, color='#333333')

handles = [Line2D([0], [0], marker='o', color='w', markerfacecolor=style[c][0], markeredgecolor='white', markersize=5.5, label=c) for c in order]
fig.legend(handles=handles, loc='upper center', ncol=3, fontsize=6.6, frameon=False, bbox_to_anchor=(0.53, 1.0), handletextpad=0.2, columnspacing=1.0)
fig.subplots_adjust(left=0.13, right=0.97, top=0.84, bottom=0.14)
fig.savefig('figura1.png', dpi=300)
print('ok')
