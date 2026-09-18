"""Render one thumbnail per case file from that project's real data.

Every mark comes from numbers that already appear in the case study, and every
chart carries the project's own vocabulary, so the tile reads as that project
rather than as an abstract shape. Palette is the site's: neutral marks plus a
single accent on the point of the chart.

Text uses a generic monospace stack. These SVGs are loaded through <img>, so no
web font is available to them, and system mono is the closest match to the site's
Geist Mono labels.

Run after changing a case file's numbers:  python scripts/gen-thumbs.py
"""
import io, json, os

W, H = 800, 640
PAD = 76
# The tile prints the file ID and year over the top of the thumbnail, so the
# drawing keeps clear of this band.
TOP = 165

BG = "#fbfbf9"
LINE = "#dcdcd6"
LINE_STRONG = "#bdbdb6"
INK = "#121315"
MUTED = "#62666d"
ACCENT = "#e4561b"
ACCENT_INK = "#b0400b"

MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"
OUT = "public/thumbs"
os.makedirs(OUT, exist_ok=True)


def esc(t):
    return t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def label(x, y, text, size=27, fill=MUTED, anchor="start", weight="400", spacing=0.06):
    return (
        f'<text x="{x:.1f}" y="{y:.1f}" font-family="{MONO}" font-size="{size}" '
        f'fill="{fill}" text-anchor="{anchor}" font-weight="{weight}" '
        f'letter-spacing="{spacing}em">{esc(text)}</text>'
    )


def wrap(body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" '
        f'width="{W}" height="{H}" role="img">'
        f'<rect width="{W}" height="{H}" fill="{BG}"/>{body}</svg>'
    )


def save(name, body):
    io.open(os.path.join(OUT, f"{name}.svg"), "w", encoding="utf-8").write(wrap(body))
    print(f"{name:26} {len(wrap(body)):6} bytes")


# --- CC-01 V-Guard: a day of national generation, and the solar bell ----------
def vguard():
    d = json.load(open("src/data/vguard-nldc.json"))["Q1"]
    total, solar = d["total"], d["solar"]
    n = len(total)
    x0, x1 = PAD, W - PAD
    y0, y1 = TOP + 40, H - PAD - 46
    ymax = 260.0

    def pt(i, v):
        return (x0 + (x1 - x0) * i / (n - 1), y1 - (y1 - y0) * (v / ymax))

    s = []
    for g in range(1, 4):
        y = y0 + (y1 - y0) * g / 4
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>')
    area = " ".join(f"{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}" for i, v in enumerate(solar))
    s.append(f'<polygon points="{x0},{y1} {area} {x1},{y1}" fill="{ACCENT}" fill-opacity="0.16"/>')
    s.append(f'<polyline points="{area}" fill="none" stroke="{ACCENT}" stroke-width="4.5" stroke-linejoin="round"/>')
    tot = " ".join(f"{pt(i,v)[0]:.1f},{pt(i,v)[1]:.1f}" for i, v in enumerate(total))
    s.append(f'<polyline points="{tot}" fill="none" stroke="{INK}" stroke-width="3.5" stroke-linejoin="round"/>')
    s.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{LINE_STRONG}" stroke-width="1.5"/>')
    s.append(label(x0, TOP + 22, "NATIONAL GRID, 15 MIN", 27, MUTED))
    s.append(label(x0 + 14, pt(0, total[0])[1] - 22, "TOTAL", 28, INK, weight="600"))
    peak = max(range(n), key=lambda i: solar[i])
    s.append(label(pt(peak, solar[peak])[0], pt(peak, solar[peak])[1] - 24, "SOLAR", 28, ACCENT_INK,
                   anchor="middle", weight="600"))
    s.append(label(x0, H - PAD - 8, "00:00", 26, MUTED))
    s.append(label(x1, H - PAD - 8, "24:00", 26, MUTED, anchor="end"))
    return "".join(s)


# --- CC-02 Attrition copilot: recall collapses from train to test -------------
def quantum_trial():
    rows = [
        ("L1 LOGISTIC", 58.3, 36.8, True),
        ("RANDOM FOREST", 72.9, 5.3, False),
        ("RF + SMOTE", 23.2, 2.6, False),
        ("XGBOOST", 82.8, 23.7, False),
        ("XGB + SMOTE", 5.3, 0.0, False),
    ]
    gutter = 250
    x0, x1 = PAD + gutter, W - PAD
    span = x1 - x0
    y0, y1 = TOP + 56, H - PAD - 30
    step = (y1 - y0) / (len(rows) - 1)
    s = [label(PAD, TOP + 22, "RECALL %", 27, MUTED)]
    s.append(label(x1, TOP + 22, "TRAIN", 26, MUTED, anchor="end"))
    for i, (name, a, b, hl) in enumerate(rows):
        y = y0 + i * step
        ax, bx = x0 + span * (a / 100), x0 + span * (b / 100)
        col = ACCENT if hl else LINE_STRONG
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1.5"/>')
        s.append(f'<line x1="{bx:.1f}" y1="{y:.1f}" x2="{ax:.1f}" y2="{y:.1f}" stroke="{col}" stroke-width="6"/>')
        s.append(f'<circle cx="{bx:.1f}" cy="{y:.1f}" r="9" fill="{BG}" stroke="{col}" stroke-width="5"/>')
        s.append(f'<circle cx="{ax:.1f}" cy="{y:.1f}" r="9" fill="{INK if hl else LINE_STRONG}"/>')
        s.append(label(PAD, y + 9, name, 26, ACCENT_INK if hl else MUTED,
                       weight="600" if hl else "400"))
    s.append(label(x0, H - PAD + 4, "TEST", 26, MUTED))
    return "".join(s)


# --- CC-03 Digital lending: default rate by purpose and ticket size -----------
def finception():
    rows = [
        ("EDUCATIONAL", [16.3, 18.75, 37.5, None]),
        ("SMALL BUSINESS", [12.35, 14.88, 15.59, 16.94]),
        ("WEDDING", [10.42, 12.78, 14.29, 26.32]),
        ("RENEWABLE", [8.86, 10.88, 12.2, 18.18]),
        ("MOVING", [8.39, 8.16, 11.79, 5.88]),
        ("MEDICAL", [7.19, 6.47, 7.71, 13.16]),
        ("CREDIT CARD", [4.21, 4.1, 3.69, 3.43]),
    ]
    cols = ["0-10K", "10-20K", "20-30K", "30-40K"]
    thr, mx = 14.0, 37.5
    gutter = 258
    gx0, gx1 = PAD + gutter, W - PAD
    gy0, gy1 = TOP + 62, H - PAD - 28
    cw, ch = (gx1 - gx0) / 4, (gy1 - gy0) / len(rows)
    gap = 2.5
    s = [label(PAD, TOP + 22, "DEFAULT RATE %", 27, MUTED)]
    for c, cl in enumerate(cols):
        s.append(label(gx0 + c * cw + cw / 2, gy0 - 14, cl, 23, MUTED, anchor="middle"))
    for r, (name, vals) in enumerate(rows):
        y = gy0 + r * ch
        s.append(label(PAD, y + ch / 2 + 8, name, 24, MUTED))
        for c, v in enumerate(vals):
            x = gx0 + c * cw
            if v is None:
                s.append(f'<rect x="{x+gap:.1f}" y="{y+gap:.1f}" width="{cw-2*gap:.1f}" '
                         f'height="{ch-2*gap:.1f}" fill="none" stroke="{LINE}" stroke-width="1"/>')
                continue
            if v >= thr:
                fill, op = ACCENT, 0.42 + 0.58 * ((v - thr) / (mx - thr))
            else:
                fill, op = LINE_STRONG, 0.22 + 0.62 * (v / thr)
            s.append(f'<rect x="{x+gap:.1f}" y="{y+gap:.1f}" width="{cw-2*gap:.1f}" '
                     f'height="{ch-2*gap:.1f}" fill="{fill}" fill-opacity="{op:.2f}"/>')
    s.append(label(gx0, H - PAD + 6, "LOAN SIZE", 24, MUTED))
    return "".join(s)


# --- AC-01 StreamMax: fatigue against days away ------------------------------
def streammax():
    d = json.load(open("src/data/streammax.json"))["daysSince"]
    x0, x1 = PAD, W - PAD
    y0, y1 = TOP + 54, H - PAD - 40
    n = len(d)
    slot = (x1 - x0) / n
    bw = slot * 0.6
    mx = 88.0
    s = [label(PAD, TOP + 22, "% FATIGUED", 27, MUTED)]
    for g in range(1, 4):
        y = y0 + (y1 - y0) * g / 4
        s.append(f'<line x1="{x0}" y1="{y:.1f}" x2="{x1}" y2="{y:.1f}" stroke="{LINE}" stroke-width="1"/>')
    for i, row in enumerate(d):
        h = (y1 - y0) * (row["rate"] / mx)
        x = x0 + i * slot + (slot - bw) / 2
        hot = row["x"] >= 6
        s.append(f'<rect x="{x:.1f}" y="{y1-h:.1f}" width="{bw:.1f}" height="{h:.1f}" '
                 f'fill="{ACCENT if hot else LINE_STRONG}"/>')
    s.append(f'<line x1="{x0}" y1="{y1}" x2="{x1}" y2="{y1}" stroke="{LINE_STRONG}" stroke-width="1.5"/>')
    top = d[-1]
    s.append(label(x1, y1 - (y1 - y0) * (top["rate"] / mx) - 16, f'{top["rate"]:.0f}%', 28,
                   ACCENT_INK, anchor="end", weight="600"))
    s.append(label(x0, H - PAD - 6, "0", 25, MUTED))
    s.append(label(x1, H - PAD - 6, "10+", 25, MUTED, anchor="end"))
    s.append(label((x0 + x1) / 2, H - PAD + 22, "DAYS SINCE LAST SESSION", 25, MUTED, anchor="middle"))
    return "".join(s)


# --- AC-02 TezCredit: the borrower journey -----------------------------------
def tezcredit():
    steps = ["ONBOARD", "VERIFY", "UNDERSTAND", "DECIDE", "SIGN", "DISBURSE"]
    n = len(steps)
    x0 = PAD
    y0, y1 = TOP + 44, H - PAD - 20
    step = (y1 - y0) / (n - 1)
    bw, bh = 330, 50
    xspan = (W - 2 * PAD - bw) / (n - 1)
    s = [label(PAD, TOP + 14, "MINUTES, END TO END", 27, MUTED)]
    for i, name in enumerate(steps):
        y = y0 + i * step - bh / 2
        x = x0 + i * xspan
        last = i == n - 1
        if i < n - 1:
            ny = y0 + (i + 1) * step - bh / 2
            nx = x0 + (i + 1) * xspan
            s.append(f'<path d="M {x+26:.1f} {y+bh:.1f} L {x+26:.1f} {ny-12:.1f} '
                     f'L {nx+26:.1f} {ny-12:.1f} L {nx+26:.1f} {ny:.1f}" '
                     f'fill="none" stroke="{LINE_STRONG}" stroke-width="2"/>')
        s.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{bw}" height="{bh}" '
                 f'fill="{ACCENT if last else BG}" stroke="{ACCENT if last else LINE_STRONG}" stroke-width="2.5"/>')
        s.append(f'<rect x="{x+16:.1f}" y="{y+bh/2-5:.1f}" width="10" height="10" '
                 f'fill="{BG if last else ACCENT}"/>')
        s.append(label(x + 42, y + bh / 2 + 9, name, 26, BG if last else INK,
                       weight="600" if last else "400"))
    return "".join(s)


# --- AC-03 VitalChain: hash, chain, consensus --------------------------------
def vitalchain():
    names = ["HASH", "CHAIN", "CONSENSUS"]
    gap = 40
    bw = (W - 2 * PAD - 2 * gap) / 3
    bh = 250
    y = TOP + 60
    s = [label(PAD, TOP + 16, "TAMPER-EVIDENT RECORD", 27, MUTED)]
    for i, name in enumerate(names):
        x = PAD + i * (bw + gap)
        last = i == 2
        stroke = ACCENT if last else LINE_STRONG
        s.append(f'<rect x="{x:.1f}" y="{y}" width="{bw:.1f}" height="{bh}" fill="{BG}" '
                 f'stroke="{stroke}" stroke-width="3.5"/>')
        for k in range(4):
            ly = y + 46 + k * 38
            wd = bw - 64 - (k % 3) * 28
            col = ACCENT if (last and k == 2) else LINE_STRONG
            s.append(f'<line x1="{x+32:.1f}" y1="{ly}" x2="{x+32+wd:.1f}" y2="{ly}" '
                     f'stroke="{col}" stroke-width="7"/>')
        s.append(label(x + bw / 2, y + bh + 38, name, 26, ACCENT_INK if last else MUTED,
                       anchor="middle", weight="600" if last else "400"))
        if i < 2:
            s.append(f'<line x1="{x+bw:.1f}" y1="{y+bh/2}" x2="{x+bw+gap:.1f}" y2="{y+bh/2}" '
                     f'stroke="{LINE_STRONG}" stroke-width="3"/>')
            cx = x + bw + gap / 2
            s.append(f'<rect x="{cx-7:.1f}" y="{y+bh/2-7}" width="14" height="14" fill="{ACCENT}" '
                     f'transform="rotate(45 {cx:.1f} {y+bh/2})"/>')
    return "".join(s)


# --- AC-04 Butterfly valves: Kraljic positioning -----------------------------
def butterfly():
    x0, x1 = PAD + 40, W - PAD
    y0, y1 = TOP + 56, H - PAD - 44
    mx, my = (x0 + x1) / 2, (y0 + y1) / 2
    s = [label(PAD, TOP + 20, "KRALJIC POSITIONING", 27, MUTED)]
    s.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="none" '
             f'stroke="{LINE_STRONG}" stroke-width="2"/>')
    s.append(f'<line x1="{mx}" y1="{y0}" x2="{mx}" y2="{y1}" stroke="{LINE}" stroke-width="1.5"/>')
    s.append(f'<line x1="{x0}" y1="{my}" x2="{x1}" y2="{my}" stroke="{LINE}" stroke-width="1.5"/>')
    quad = [("BOTTLENECK", x0 + 16, y0 + 34), ("STRATEGIC", mx + 16, y0 + 34),
            ("NON-CRITICAL", x0 + 16, y1 - 16), ("LEVERAGE", mx + 16, y1 - 16)]
    for name, qx, qy in quad:
        s.append(label(qx, qy, name, 23, MUTED))
    for px, py, hl in [(74, 30, False), (74, 76, True)]:
        cx, cy = x0 + (x1 - x0) * px / 100, y1 - (y1 - y0) * py / 100
        if hl:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="62" fill="{ACCENT}" fill-opacity="0.13"/>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="30" fill="{ACCENT}"/>')
        else:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="30" fill="{BG}" stroke="{INK}" stroke-width="5"/>')
    s.append(label((x0 + x1) / 2, H - PAD + 4, "PROFIT IMPACT", 24, MUTED, anchor="middle"))
    s.append(f'<text x="{PAD - 4}" y="{(y0+y1)/2}" font-family="{MONO}" font-size="24" fill="{MUTED}" '
             f'text-anchor="middle" letter-spacing="0.06em" '
             f'transform="rotate(-90 {PAD-4} {(y0+y1)/2})">SUPPLY RISK</text>')
    return "".join(s)


# --- AC-05 PrintCraft: order to cash across the functions --------------------
def printcraft():
    lanes = [
        ("SALES", [("QUOTE", 0.00, 0.26), ("ORDER", 0.34, 0.26)]),
        ("MANUFACTURING", [("JOB SPEC", 0.10, 0.30), ("PRESS", 0.48, 0.24), ("QC", 0.78, 0.22)]),
        ("FINANCE", [("INVOICE", 0.30, 0.30), ("COLLECT", 0.68, 0.32)]),
    ]
    hl = (1, 1)
    gutter = 240
    x0, x1 = PAD + gutter, W - PAD
    y0, y1 = TOP + 40, H - PAD
    lane_h = (y1 - y0) / 3
    bh = 54
    s = [label(PAD, TOP + 12, "ORDER TO CASH", 27, MUTED)]
    for li, (lane, boxes) in enumerate(lanes):
        ly = y0 + li * lane_h
        cy = ly + lane_h / 2
        if li:
            s.append(f'<line x1="{PAD}" y1="{ly:.1f}" x2="{x1}" y2="{ly:.1f}" stroke="{LINE}" stroke-width="1.5"/>')
        s.append(label(PAD, cy + 8, lane, 24, MUTED))
        s.append(f'<line x1="{x0}" y1="{cy:.1f}" x2="{x1}" y2="{cy:.1f}" stroke="{LINE}" stroke-width="1"/>')
        for bi, (name, sx, sw) in enumerate(boxes):
            bx = x0 + (x1 - x0) * sx
            bwid = (x1 - x0) * sw
            on = (li, bi) == hl
            s.append(f'<rect x="{bx:.1f}" y="{cy-bh/2:.1f}" width="{bwid:.1f}" height="{bh}" '
                     f'fill="{ACCENT if on else BG}" stroke="{ACCENT if on else LINE_STRONG}" stroke-width="2.5"/>')
            s.append(label(bx + bwid / 2, cy + 9, name, 23, BG if on else INK, anchor="middle",
                           weight="600" if on else "400"))
    return "".join(s)


# --- AC-06 NovaTel: one spine instead of standalone systems ------------------
def novatel():
    nodes = {
        "KYC": (0.09, 0.16), "PROVISION": (0.09, 0.84),
        "BILLING": (0.46, 0.16), "TICKETS": (0.46, 0.84),
        "ERP": (0.80, 0.50),
    }
    edges = [("KYC", "BILLING"), ("PROVISION", "TICKETS"), ("KYC", "PROVISION"),
             ("BILLING", "ERP"), ("TICKETS", "ERP"), ("BILLING", "TICKETS")]
    x0, x1 = PAD + 30, W - PAD - 30
    y0, y1 = TOP + 60, H - PAD - 30

    def pos(k):
        px, py = nodes[k]
        return x0 + (x1 - x0) * px, y0 + (y1 - y0) * py

    s = [label(PAD, TOP + 22, "ONE SPINE, FIVE FLOWS", 27, MUTED)]
    for a, b in edges:
        ax, ay = pos(a)
        bx, by = pos(b)
        on = b == "ERP"
        s.append(f'<line x1="{ax:.1f}" y1="{ay:.1f}" x2="{bx:.1f}" y2="{by:.1f}" '
                 f'stroke="{ACCENT if on else LINE_STRONG}" stroke-width="{3.5 if on else 2}"/>')
    for k in nodes:
        cx, cy = pos(k)
        core = k == "ERP"
        if core:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="56" fill="{ACCENT}" fill-opacity="0.13"/>')
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="34" fill="{ACCENT}"/>')
            s.append(label(cx, cy + 9, k, 25, BG, anchor="middle", weight="600"))
        else:
            s.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="17" fill="{BG}" stroke="{INK}" stroke-width="3.5"/>')
            below = cy > (y0 + y1) / 2
            s.append(label(cx, cy + (44 if below else -30), k, 24, MUTED, anchor="middle"))
    return "".join(s)


for name, fn in [
    ("quantum-trial", quantum_trial), ("vguard-bess", vguard),
    ("finception-credit-risk", finception), ("streammax-fatigue", streammax),
    ("tezcredit", tezcredit), ("vitalchain", vitalchain),
    ("butterfly-valves", butterfly), ("printcraft-erp", printcraft),
    ("novatel-erp", novatel),
]:
    save(name, fn())
