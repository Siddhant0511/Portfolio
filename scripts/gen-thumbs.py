"""Render one thumbnail per case file from that project's real data.

Every mark is drawn from numbers that already appear in the case study, in the
site palette (neutral marks plus a single accent on the point of the chart), so
the grid reads as one system instead of nine borrowed screenshots.
"""
import io, json, os

W, H = 800, 640
PAD = 76
# The tile prints the file ID and year over the top of the thumbnail, so the
# drawing keeps clear of this band. 165/640 of the height is ~65px at 317px wide,
# comfortably past the 50px the overlay occupies.
TOP = 165
BG = "#fbfbf9"
LINE = "#dcdcd6"
LINE_STRONG = "#bdbdb6"
INK = "#121315"
ACCENT = "#e4561b"

OUT = "public/thumbs"
os.makedirs(OUT, exist_ok=True)


def wrap(body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img">'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>'
    )


def save(name, body):
    p = os.path.join(OUT, f"{name}.svg")
    io.open(p, "w", encoding="utf-8").write(wrap(body))
    print(f"{name:26} {len(wrap(body)):6} bytes")


# --- 1. quantum trial: train recall vs test recall, the overfit collapse ------
def quantum_trial():
    rows = [
        ("L1 logistic regression", 58.3, 36.8, True),
        ("Random Forest", 72.9, 5.3, False),
        ("Random Forest + SMOTE", 23.2, 2.6, False),
        ("XGBoost", 82.8, 23.7, False),
        ("XGBoost + SMOTE", 5.3, 0.0, False),
    ]
    x0, x1 = PAD, W - PAD
    span = x1 - x0
    step = (H - TOP - PAD) / (len(rows) - 1)
    s = []
    for i, (_, a, b, hl) in enumerate(rows):
        y = TOP + i * step
        ax, bx = x0 + span * (a / 100), x0 + span * (b / 100)
        col = ACCENT if hl else LINE_STRONG
        s.append(f'<line x1="{x0}" y1="{y}" x2="{x1}" y2="{y}" stroke="{LINE}" stroke-width="1.5"/>')
        s.append(f'<line x1="{bx}" y1="{y}" x2="{ax}" y2="{y}" stroke="{col}" stroke-width="6"/>')
        s.append(f'<circle cx="{bx}" cy="{y}" r="9" fill="{BG}" stroke="{col}" stroke-width="5"/>')
        s.append(f'<circle cx="{ax}" cy="{y}" r="9" fill="{INK if hl else LINE_STRONG}"/>')
    return "".join(s)


# --- 2. V-Guard: the duck curve from 15-minute national grid data -------------
def vguard():
    d = json.load(open("src/data/vguard-nldc.json"))["Q1"]
    total, solar = d["total"], d["solar"]
    n = len(total)
    x0, x1 = PAD, W - PAD
    y0, y1 = TOP, H - PAD
    ymax = 260.0

    def pt(i, v):
        return (x0 + (x1 - x0) * i / (n - 1), y1 - (y1 - y0) * (v / ymax))

    s = []
    for g in range(1, 4):
        y = y0 + (y1 - y0) * g / 4
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>')
    area = " ".join(f"{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}" for i, v in enumerate(solar))
    s.append(f'<polygon points="{x0},{y1} {area} {x1},{y1}" fill="{ACCENT}" fill-opacity="0.16"/>')
    s.append(f'<polyline points="{area}" fill="none" stroke="{ACCENT}" stroke-width="4" stroke-linejoin="round"/>')
    tot = " ".join(f"{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}" for i, v in enumerate(total))
    s.append(f'<polyline points="{tot}" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
    s.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{LINE_STRONG}" stroke-width="1.5"/>')
    return "".join(s)


# --- 3. Finception: default rate by purpose and loan bucket -------------------
def finception():
    vals = [
        [16.3, 18.75, 37.5, None], [10.42, 12.78, 14.29, 26.32],
        [12.35, 14.88, 15.59, 16.94], [8.86, 10.88, 12.2, 18.18],
        [8.39, 8.16, 11.79, 5.88], [7.97, 8.22, 10.53, 5.75],
        [7.19, 6.47, 7.71, 13.16], [7.17, 7.57, 7.92, 7.47],
        [5.86, 7.36, 11.54, 3.57], [5.63, 5.64, 5.56, 5.55],
        [5.05, 6.03, 5.03, 6.11], [5.25, 5.29, 6.85, 4.82],
        [4.39, 4.29, 5.4, 6.25], [4.21, 4.1, 3.69, 3.43],
    ]
    rows, cols, thr, mx = len(vals), 4, 14.0, 37.5
    gw, gh = W - 2 * PAD, H - TOP - PAD
    cw, ch = gw / cols, gh / rows
    gap = 2.5
    s = []
    for r in range(rows):
        for c in range(cols):
            v = vals[r][c]
            x, y = PAD + c * cw, TOP + r * ch
            if v is None:
                s.append(f'<rect x="{x+gap:.1f}" y="{y+gap:.1f}" width="{cw-2*gap:.1f}" '
                         f'height="{ch-2*gap:.1f}" fill="none" stroke="{LINE}" stroke-width="1"/>')
                continue
            if v >= thr:
                t = (v - thr) / (mx - thr)
                fill, op = ACCENT, 0.42 + 0.58 * t
            else:
                fill, op = LINE_STRONG, 0.22 + 0.62 * (v / thr)
            s.append(f'<rect x="{x+gap:.1f}" y="{y+gap:.1f}" width="{cw-2*gap:.1f}" '
                     f'height="{ch-2*gap:.1f}" fill="{fill}" fill-opacity="{op:.2f}"/>')
    return "".join(s)


# --- 4. StreamMax: fatigue rate against days since the last session -----------
def streammax():
    d = json.load(open("src/data/streammax.json"))["daysSince"]
    x0, x1, y0, y1 = PAD, W - PAD, TOP, H - PAD
    n = len(d)
    slot = (x1 - x0) / n
    bw = slot * 0.62
    mx = 84.0
    s = []
    for g in range(1, 4):
        y = y0 + (y1 - y0) * g / 4
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>')
    for i, row in enumerate(d):
        h = (y1 - y0) * (row["rate"] / mx)
        x = x0 + i * slot + (slot - bw) / 2
        col = ACCENT if row["x"] >= 6 else LINE_STRONG
        s.append(f'<rect x="{x:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{col}"/>')
    s.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{LINE_STRONG}" stroke-width="1.5"/>')
    return "".join(s)


# --- 5. TezCredit: the six-step borrower journey ------------------------------
def tezcredit():
    n = 6
    x0, y0, y1 = PAD, TOP, H - PAD
    step = (y1 - y0) / (n - 1)
    bw, bh = 300, 52
    s = []
    for i in range(n):
        y = y0 + i * step - bh / 2
        x = x0 + i * ((W - 2 * PAD - bw) / (n - 1))
        last = i == n - 1
        fill = ACCENT if last else BG
        stroke = ACCENT if last else LINE_STRONG
        if i < n - 1:
            ny = y0 + (i + 1) * step - bh / 2
            nx = x0 + (i + 1) * ((W - 2 * PAD - bw) / (n - 1))
            s.append(f'<path d="M {x+28} {y+bh} L {x+28} {ny-14} L {nx+28} {ny-14} L {nx+28} {ny}" '
                     f'fill="none" stroke="{LINE_STRONG}" stroke-width="2"/>')
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{bh}" fill="{fill}" '
                 f'stroke="{stroke}" stroke-width="2.5"/>')
        dot = BG if last else ACCENT
        s.append(f'<rect x="{x+18:.1f}" y="{y+bh/2-5:.1f}" width="10" height="10" fill="{dot}"/>')
    return "".join(s)


# --- 6. VitalChain: hash, chain, consensus ------------------------------------
def vitalchain():
    s = []
    gap = 44
    bw = (W - 2 * PAD - 2 * gap) / 3
    bh = 300
    y = (H - bh) / 2
    for i in range(3):
        x = PAD + i * (bw + gap)
        last = i == 2
        stroke = ACCENT if last else LINE_STRONG
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{bh}" fill="{BG}" '
                 f'stroke="{stroke}" stroke-width="3.5"/>')
        # hash lines: the block's fingerprint
        for k in range(6):
            ly = y + 48 + k * 42
            w = bw - 68 - (k % 3) * 30
            col = ACCENT if (last and k == 3) else LINE_STRONG
            s.append(f'<line x1="{x+34:.1f}" y1="{ly}" x2="{x+34+w:.1f}" y2="{ly}" stroke="{col}" stroke-width="7"/>')
        if i < 2:
            s.append(f'<line x1="{x+bw}" y1="{y+bh/2}" x2="{x+bw+gap}" y2="{y+bh/2}" '
                     f'stroke="{LINE_STRONG}" stroke-width="3"/>')
            cx = x + bw + gap / 2
            s.append(f'<rect x="{cx-7}" y="{y+bh/2-7}" width="14" height="14" fill="{ACCENT}" '
                     f'transform="rotate(45 {cx} {y+bh/2})"/>')
    return "".join(s)


# --- 7. Butterfly valves: Kraljic positioning --------------------------------
def butterfly():
    x0, x1, y0, y1 = PAD, W - PAD, TOP, H - PAD
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    s = [f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" stroke="{LINE_STRONG}" stroke-width="2"/>']
    s.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{y1}" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(f'<line x1="{x0}" y1="{my}" x2="{x1}" y2="{my}" stroke="{LINE}" stroke-width="1.5"/>')
    # The two playbooks the strategy splits the category into.
    items = [(74, 30, False), (74, 76, True)]
    for px, py, hl in items:
        cx, cy = x0 + (x1 - x0) * px / 100, y1 - (y1 - y0) * py / 100
        if hl:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="74" fill="{ACCENT}" fill-opacity="0.13"/>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="36" fill="{ACCENT}"/>')
        else:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="36" fill="{BG}" stroke="{INK}" stroke-width="5"/>')
    return "".join(s)


# --- 8. PrintCraft: order to cash across three lanes --------------------------
def printcraft():
    lanes = [
        [(0.00, 0.20), (0.30, 0.22), (0.66, 0.34)],
        [(0.12, 0.26), (0.46, 0.30), (0.82, 0.18)],
        [(0.04, 0.18), (0.36, 0.26), (0.70, 0.30)],
    ]
    hl = (1, 1)
    x0, x1, y0, y1 = PAD, W - PAD, PAD, H - PAD
    lane_h = (y1 - y0) / 3
    bh = 56
    s = []
    for li, boxes in enumerate(lanes):
        ly = y0 + li * lane_h
        cy = ly + lane_h / 2
        if li:
            s.append(f'<line x1="{x0}" y1="{ly:.1f}" x2="{x1}" y2="{ly:.1f}" stroke="{LINE}" stroke-width="1.5"/>')
        s.append(f'<line x1="{x0}" y1="{cy:.1f}" x2="{x1}" y2="{cy:.1f}" stroke="{LINE}" stroke-width="1"/>')
        for bi, (sx, sw) in enumerate(boxes):
            bx = x0 + (x1 - x0) * sx
            bwid = (x1 - x0) * sw
            on = (li, bi) == hl
            s.append(f'<rect x="{bx:.1f}" y="{cy-bh/2:.1f}" width="{bwid:.1f}" height="{bh}" '
                     f'fill="{ACCENT if on else BG}" stroke="{ACCENT if on else LINE_STRONG}" stroke-width="2.5"/>')
    return "".join(s)


# --- 9. Novatel: the process network across functions -------------------------
def novatel():
    nodes = {
        "a": (0.10, 0.50), "b": (0.34, 0.18), "c": (0.34, 0.50),
        "d": (0.34, 0.82), "e": (0.63, 0.32), "f": (0.63, 0.68),
        "g": (0.90, 0.50),
    }
    edges = [("a", "b"), ("a", "c"), ("a", "d"), ("b", "e"), ("c", "e"),
             ("c", "f"), ("d", "f"), ("e", "g"), ("f", "g")]
    x0, x1, y0, y1 = PAD, W - PAD, PAD, H - PAD

    def pos(k):
        px, py = nodes[k]
        return x0 + (x1 - x0) * px, y0 + (y1 - y0) * py

    s = []
    for a, b in edges:
        ax, ay = pos(a)
        bx, by = pos(b)
        on = b == "g"
        s.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                 f'stroke="{ACCENT if on else LINE_STRONG}" stroke-width="{3 if on else 2}"/>')
    for k in nodes:
        cx, cy = pos(k)
        if k == "g":
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="42" fill="{ACCENT}" fill-opacity="0.14"/>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="24" fill="{ACCENT}"/>')
        else:
            r = 24 if k == "a" else 19
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r}" fill="{BG}" stroke="{INK}" stroke-width="3.5"/>')
    return "".join(s)


for name, fn in [
    ("quantum-trial", quantum_trial), ("vguard-bess", vguard),
    ("finception-credit-risk", finception), ("streammax-fatigue", streammax),
    ("tezcredit", tezcredit), ("vitalchain", vitalchain),
    ("butterfly-valves", butterfly), ("printcraft-erp", printcraft),
    ("novatel-erp", novatel),
]:
    save(name, fn())
