import itertools
import math

# ----------------------------
# Numerics + geometry helpers
# ----------------------------

EPS = 1e-10

def uniq_points(points, tol=1e-8):
    out = []
    for p in points:
        ok = True
        for q in out:
            if abs(p[0]-q[0]) < tol and abs(p[1]-q[1]) < tol:
                ok = False
                break
        if ok:
            out.append(p)
    return out

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
    """Monotone chain convex hull; returns vertices CCW without repeating first."""
    pts = sorted(points)
    if len(pts) <= 1:
        return pts

    lower = []
    for p in pts:
        while len(lower) >= 2 and cross(lower[-2], lower[-1], p) <= 1e-12:
            lower.pop()
        lower.append(p)

    upper = []
    for p in reversed(pts):
        while len(upper) >= 2 and cross(upper[-2], upper[-1], p) <= 1e-12:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

# Half-plane format: A*x + B*y <= C
def eval_ineq(ineq, x, y):
    A, B, C = ineq
    return A*x + B*y - C

def intersect_lines(L1, L2):
    """L: (A,B,C) meaning A*x + B*y = C"""
    A1, B1, C1 = L1
    A2, B2, C2 = L2
    det = A1*B2 - A2*B1
    if abs(det) < 1e-12:
        return None
    x = (C1*B2 - C2*B1) / det
    y = (A1*C2 - A2*C1) / det
    if not (math.isfinite(x) and math.isfinite(y)):
        return None
    return (x, y)

def polygon_from_halfplanes(ineqs):
    """Return polygon hull vertices (x,y) or None if empty."""
    # candidates = all pairwise boundary intersections that satisfy all inequalities
    candidates = []
    for i in range(len(ineqs)):
        for j in range(i+1, len(ineqs)):
            p = intersect_lines(ineqs[i], ineqs[j])
            if p is None:
                continue
            x, y = p
            if all(eval_ineq(ineq, x, y) <= 1e-9 for ineq in ineqs):
                candidates.append((x, y))

    candidates = uniq_points(candidates)
    if len(candidates) < 3:
        return None

    hull = convex_hull(candidates)
    if len(hull) < 3:
        return None
    return hull

# ----------------------------
# Simplex + barycentric embedding
# ----------------------------

def integer_allocations(h):
    """All integer m >=0 with sum h."""
    out = []
    for m1 in range(h+1):
        for m2 in range(h+1-m1):
            m3 = h - m1 - m2
            out.append((m1, m2, m3))
    return out

def q_from_xy(x, y, h):
    """On plane x+y+z=h"""
    return (x, y, h - x - y)

def bary_2d(q, h, side_len):
    """
    Equilateral triangle vertices:
      A=(h,0,0) -> (0,0)
      B=(0,h,0) -> (S,0)
      C=(0,0,h) -> (S/2, S*sqrt(3)/2)
    and q maps by weights q_i/h.
    """
    x, y, z = q
    A = (0.0, 0.0)
    B = (side_len, 0.0)
    C = (side_len/2.0, side_len*math.sqrt(3)/2.0)
    w1, w2, w3 = x/h, y/h, z/h
    X = w1*A[0] + w2*B[0] + w3*C[0]
    Y = w1*A[1] + w2*B[1] + w3*C[1]
    return (X, Y)

# ----------------------------
# Webster divisor-cell inequalities on Δ_h (n=3)
# ----------------------------

def webster_cell_inequalities_xy(m, h):
    """
    Build linear inequalities A*x + B*y <= C in (x,y) chart (z=h-x-y)
    describing the Webster cell of allocation m.

    Condition: exists t>0 such that round(t*q_i)=m_i for all i.
    Equivalent (pairwise) halfspaces on q:
        (m_i - 1/2) q_j <= (m_j + 1/2) q_i   for all i,j
    plus simplex constraints q>=0, x+y<=h.
    """
    m1, m2, m3 = m

    # simplex constraints in xy:
    # x >= 0  -> -x <= 0
    # y >= 0  -> -y <= 0
    # z >= 0  -> x+y <= h
    ineqs = [(-1, 0, 0), (0, -1, 0), (1, 1, h)]

    # express q0=x, q1=y, q2=h-x-y
    def q_expr(idx):
        # returns (A,B,const) for q_idx = A*x + B*y + const
        if idx == 0:  # x
            return (1.0, 0.0, 0.0)
        if idx == 1:  # y
            return (0.0, 1.0, 0.0)
        if idx == 2:  # z = h-x-y
            return (-1.0, -1.0, float(h))
        raise ValueError

    ms = [float(m1), float(m2), float(m3)]

    # Pairwise inequalities:
    # (m_i - 1/2) q_j <= (m_j + 1/2) q_i
    # Move all to LHS:
    # (m_i - 1/2) q_j - (m_j + 1/2) q_i <= 0
    for i in range(3):
        for j in range(3):
            if i == j:
                continue
            mi = ms[i]
            mj = ms[j]
            Ai, Bi, Ci = q_expr(i)
            Aj, Bj, Cj = q_expr(j)

            coef = (mi - 0.5)
            coef2 = (mj + 0.5)

            A = coef*Aj - coef2*Ai
            B = coef*Bj - coef2*Bi
            C = -(coef*Cj - coef2*Ci)  # bring constant to RHS: A*x+B*y <= C

            ineqs.append((A, B, C))

    return ineqs

def webster_cell_polygon_q(m, h):
    """Return polygon vertices as q=(x,y,z) tuples, or None."""
    ineqs = webster_cell_inequalities_xy(m, h)
    poly_xy = polygon_from_halfplanes(ineqs)
    if poly_xy is None:
        return None
    poly_q = [q_from_xy(x, y, h) for (x, y) in poly_xy]
    return poly_q

# ----------------------------
# TikZ writer
# ----------------------------

def tikz_picture_for_webster(h=15, side_len=6.0, draw_lattice=True, label_vertices=False):
    ms = integer_allocations(h)

    lines = []
    lines.append(r"\begin{tikzpicture}[line cap=round,line join=round]")
    lines.append(rf"  \def\N{{{h}}}")
    lines.append(rf"  \def\S{{{side_len}}}")
    lines.append(r"  \coordinate (A) at (0,0);")
    lines.append(r"  \coordinate (B) at (\S,0);")
    lines.append(r"  \coordinate (C) at ({\S/2},{\S*sqrt(3)/2});")
    lines.append(r"  \draw[thick] (A)--(B)--(C)--cycle;")
    lines.append(r"  \node[below left] at (A) {$(\N,0,0)$};")
    lines.append(r"  \node[below right] at (B) {$(0,\N,0)$};")
    lines.append(r"  \node[above] at (C) {$(0,0,\N)$};")
    lines.append("")

    if draw_lattice:
        lines.append(r"  % lattice points (integer triples summing to N)")
        for a in range(h+1):
            for b in range(h+1-a):
                c = h - a - b
                X, Y = bary_2d((a,b,c), h, side_len)
                lines.append(rf"  \fill[white] ({X:.6f},{Y:.6f}) circle (1.05pt);")
                lines.append(rf"  \fill[black] ({X:.6f},{Y:.6f}) circle (0.75pt);")
        lines.append("")

    lines.append(r"  % Webster divisor-method cells")
    lines.append(r"  \tikzset{cell/.style={thick, dashed}}")
    lines.append("")

    for m in ms:
        poly_q = webster_cell_polygon_q(m, h)
        if poly_q is None:
            continue

        pts = [bary_2d(q, h, side_len) for q in poly_q]
        path = " -- ".join([f"({X:.6f},{Y:.6f})" for (X,Y) in pts])

        lines.append(rf"  % m = {m}")
        lines.append(rf"  \draw[cell] {path} -- cycle;")

        if label_vertices:
            # place label near the lattice point for m
            Xc, Yc = bary_2d(m, h, side_len)
            lines.append(rf"  \node[font=\scriptsize] at ({Xc:.6f},{Yc:.6f}) {{$({m[0]},{m[1]},{m[2]})$}};")

        lines.append("")

    lines.append(r"\end{tikzpicture}")
    return "\n".join(lines)

def main():
    h = 15
    tex = []
    tex.append("% Auto-generated Webster divisor-method cells on x+y+z = N")
    tex.append("% Compile with: \\usepackage{tikz}")
    tex.append("%")
    tex.append(tikz_picture_for_webster(h=h, side_len=6.8, draw_lattice=True, label_vertices=False))
    outname = "webster_h4.tex"
    with open(outname, "w", encoding="utf-8") as f:
        f.write("\n".join(tex))
        f.write("\n")
    print(f"Wrote {outname}")

if __name__ == "__main__":
    main()
