import itertools
import math

# ----------------------------
# Small numeric utilities
# ----------------------------

EPS = 1e-9

def almost_equal(a, b, tol=1e-9):
    return abs(a - b) <= tol

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

# ----------------------------
# Convex hull (monotone chain)
# ----------------------------

def cross(o, a, b):
    return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

def convex_hull(points):
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

    # drop last point of each (repeats start)
    return lower[:-1] + upper[:-1]

# ----------------------------
# Integer allocations on x+y+z=h
# ----------------------------

def integer_allocations(h):
    out = []
    for x in range(h+1):
        for y in range(h+1-x):
            z = h - x - y
            out.append((x, y, z))
    return out

# ----------------------------
# Hamilton S-piece inequalities
# We work in (x,y) with z = h - x - y
# Each inequality is of form: A*x + B*y <= C
# ----------------------------

def add_ineq(ineqs, A, B, C):
    ineqs.append((float(A), float(B), float(C)))

def eval_ineq(ineq, x, y):
    A, B, C = ineq
    return A*x + B*y - C  # should be <= 0 if feasible

def piece_inequalities(m, S, h):
    """
    Build inequalities for P(m,S) (closed form) on plane x+y+z=h, x,y,z>=0.

    m: tuple (m1,m2,m3) sum h
    S: subset of {0,1,2} getting the surplus seats
    floors l_i = m_i-1 if i in S else m_i

    Constraints:
      - x,y,z >= 0
      - slab: l_i <= q_i <= l_i+1 for each i
      - remainder order: for i in S, j not in S:
            (q_i - l_i) >= (q_j - l_j)
    """
    S = set(S)
    l = [m[i]-1 if i in S else m[i] for i in range(3)]
    if any(li < 0 for li in l):
        return None  # impossible

    ineqs = []

    # Nonnegativity and simplex boundary:
    # x >= 0  -> -x <= 0
    add_ineq(ineqs, -1,  0, 0)
    # y >= 0  -> -y <= 0
    add_ineq(ineqs,  0, -1, 0)
    # z = h-x-y >= 0  -> x+y <= h
    add_ineq(ineqs,  1,  1, h)

    # Slabs for x and y:
    # l0 <= x <= l0+1
    add_ineq(ineqs, -1,  0, -l[0])      # x >= l0
    add_ineq(ineqs,  1,  0,  l[0]+1)    # x <= l0+1
    # l1 <= y <= l1+1
    add_ineq(ineqs,  0, -1, -l[1])      # y >= l1
    add_ineq(ineqs,  0,  1,  l[1]+1)    # y <= l1+1

    # Slab for z: l2 <= z <= l2+1, i.e.
    # l2 <= h-x-y <= l2+1  <=>  h-(l2+1) <= x+y <= h-l2
    add_ineq(ineqs, -1, -1, -(h-(l[2]+1)))  # x+y >= h-(l2+1)
    add_ineq(ineqs,  1,  1,  (h-l[2]))      # x+y <= h-l2

    # Remainder comparisons: (q_i - l_i) >= (q_j - l_j)
    # Rearranged: q_j - q_i <= l_j - l_i
    # Substitute q = (x, y, h-x-y).

    def q_expr(idx):
        # returns coefficients (ax, by, const) for q_idx in terms of (x,y):
        # q0 = x
        # q1 = y
        # q2 = h - x - y
        if idx == 0:
            return (1, 0, 0)
        if idx == 1:
            return (0, 1, 0)
        if idx == 2:
            return (-1, -1, h)
        raise ValueError

    for i in range(3):
        for j in range(3):
            if i in S and j not in S:
                aix, aiy, aic = q_expr(i)
                ajx, ajy, ajc = q_expr(j)
                # q_j - q_i <= l_j - l_i
                A = (ajx - aix)
                B = (ajy - aiy)
                C = (l[j] - l[i]) - (ajc - aic)
                add_ineq(ineqs, A, B, C)

    return ineqs, tuple(l)

# ----------------------------
# Compute polygon vertices from inequalities
# ----------------------------

def intersect_lines(L1, L2):
    """
    L: (A,B,C) meaning A*x + B*y = C
    returns (x,y) or None if parallel.
    """
    A1, B1, C1 = L1
    A2, B2, C2 = L2
    det = A1*B2 - A2*B1
    if abs(det) < 1e-12:
        return None
    x = (C1*B2 - C2*B1) / det
    y = (A1*C2 - A2*C1) / det
    return (x, y)

def polygon_from_halfplanes(ineqs):
    """
    ineqs: list of (A,B,C) with A*x + B*y <= C
    Returns hull vertices in CCW order, or None if empty.
    """
    # candidate points: all pairwise intersections of boundary lines
    candidates = []
    lines = [(A,B,C) for (A,B,C) in ineqs]
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            p = intersect_lines(lines[i], lines[j])
            if p is None:
                continue
            x, y = p
            # feasibility check
            ok = True
            for ineq in ineqs:
                if eval_ineq(ineq, x, y) > 1e-9:
                    ok = False
                    break
            if ok and math.isfinite(x) and math.isfinite(y):
                candidates.append((x, y))

    candidates = uniq_points(candidates)
    if len(candidates) < 3:
        return None

    hull = convex_hull(candidates)
    if len(hull) < 3:
        return None
    return hull

# ----------------------------
# Map (x,y) to barycentric equilateral triangle coords
# with vertices A=(h,0,0), B=(0,h,0), C=(0,0,h)
# in 2D: A=(0,0), B=(S,0), C=(S/2, S*sqrt(3)/2)
# point = (x/h)*A + (y/h)*B + (z/h)*C
# ----------------------------

def barycentric_to_2d(q, h, side_len):
    x, y, z = q
    A = (0.0, 0.0)
    B = (side_len, 0.0)
    C = (side_len/2.0, side_len*math.sqrt(3)/2.0)
    w1 = x / h
    w2 = y / h
    w3 = z / h
    X = w1*A[0] + w2*B[0] + w3*C[0]
    Y = w1*A[1] + w2*B[1] + w3*C[1]
    return (X, Y)

def q_from_xy(xy, h):
    x, y = xy
    return (x, y, h - x - y)

# ----------------------------
# Produce TikZ
# ----------------------------

def tikz_for_pieces(h=8, side_len=16.0, draw_lattice=True):
    ms = integer_allocations(h)
    tikz_lines = []
    tikz_lines.append(r"\begin{tikzpicture}[scale=1.0, line cap=round, line join=round]")
    tikz_lines.append(rf"  \def\N{{{h}}}")
    tikz_lines.append(rf"  \def\S{{{side_len}}}")
    tikz_lines.append(r"  \coordinate (A) at (0,0);")
    tikz_lines.append(r"  \coordinate (B) at (\S,0);")
    tikz_lines.append(r"  \coordinate (C) at ({\S/2},{\S*sqrt(3)/2});")
    tikz_lines.append(r"  \draw[thick] (A)--(B)--(C)--cycle;")
    tikz_lines.append(r"  \node[below left] at (A) {$(\N,0,0)$};")
    tikz_lines.append(r"  \node[below right] at (B) {$(0,\N,0)$};")
    tikz_lines.append(r"  \node[above] at (C) {$(0,0,\N)$};")

    if draw_lattice:
        tikz_lines.append(r"  % lattice points")
        for a in range(h+1):
            for b in range(h+1-a):
                c = h-a-b
                X, Y = barycentric_to_2d((a,b,c), h, side_len)
                tikz_lines.append(rf"  \fill[white] ({X:.6f},{Y:.6f}) circle (1.05pt);")
                tikz_lines.append(rf"  \fill[black] ({X:.6f},{Y:.6f}) circle (0.75pt);")

    tikz_lines.append(r"  % Hamilton S-pieces")
    tikz_lines.append(r"  \tikzset{piece/.style={thick, dashed}}")

    for m in ms:
        # try all subsets S of {0,1,2}
        for k in range(0, 3):
            for S in itertools.combinations(range(3), k):
                built = piece_inequalities(m, S, h)
                if built is None:
                    continue
                ineqs, floors = built
                poly_xy = polygon_from_halfplanes(ineqs)
                if poly_xy is None:
                    continue

                # convert polygon vertices to q then to 2D barycentric
                poly_pts = []
                for xy in poly_xy:
                    q = q_from_xy(xy, h)
                    X, Y = barycentric_to_2d(q, h, side_len)
                    poly_pts.append((X, Y))

                # draw polygon
                path = " -- ".join([f"({X:.6f},{Y:.6f})" for (X,Y) in poly_pts])
                tikz_lines.append(rf"  % m={m}, S={S}, floors={floors}")
                tikz_lines.append(rf"  \draw[piece] {path} -- cycle;")

    tikz_lines.append(r"\end{tikzpicture}")
    return "\n".join(tikz_lines)

def main():
    tex = tikz_for_pieces(h=8, side_len=17.0, draw_lattice=True)
    with open("hamilton_h4.tex", "w", encoding="utf-8") as f:
        f.write("% Auto-generated by hamilton_pieces_to_tikz.py\n")
        f.write("% Requires: \\usepackage{tikz}\n")
        f.write("% Optional: \\usetikzlibrary{calc}\n\n")
        f.write(tex)
        f.write("\n")
    print("Wrote hamilton_h4.tex")

if __name__ == "__main__":
    main()
