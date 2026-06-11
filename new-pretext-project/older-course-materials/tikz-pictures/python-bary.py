import itertools
import numpy as np

from scipy.spatial import HalfspaceIntersection, ConvexHull

# ----------------------------
# Helpers for the simplex plane
# ----------------------------

def integer_allocations(h=15, n=3):
    """All integer m >=0 with sum m_i = h."""
    if n != 3:
        raise NotImplementedError("This helper currently assumes n=3.")
    out = []
    for m1 in range(h + 1):
        for m2 in range(h + 1 - m1):
            m3 = h - m1 - m2
            out.append((m1, m2, m3))
    return out

def q_from_xy(xy, h):
    """Map (x,y) -> (x,y,z) on plane x+y+z=h."""
    x, y = xy
    return np.array([x, y, h - x - y], dtype=float)

def remainder_ineq(i, j, l):
    """
    Inequality: (q_i - l_i) >= (q_j - l_j).
    In terms of (x,y), with z = h - x - y baked later.
    We'll return coefficients for ax + by <= c form after substitution.
    """
    # We'll build this in full (q0,q1,q2) first, then substitute z.
    # For now return a vector in q-space:
    # q_j - q_i <= l_j - l_i
    # => (-e_i + e_j) · q <= l_j - l_i
    a = np.zeros(3)
    a[j] = 1.0
    a[i] = -1.0
    b = float(l[j] - l[i])
    return a, b  # a·q <= b

def slab_ineq(i, lower, upper):
    """
    lower <= q_i <= upper  (closed)
    returns two inequalities a·q <= b
    """
    a1 = np.zeros(3); a1[i] = -1.0  # -q_i <= -lower  <=> q_i >= lower
    b1 = -float(lower)
    a2 = np.zeros(3); a2[i] =  1.0  #  q_i <= upper
    b2 =  float(upper)
    return [(a1,b1),(a2,b2)]

def nonneg_ineq(i):
    """q_i >= 0 -> -q_i <= 0"""
    a = np.zeros(3); a[i] = -1.0
    b = 0.0
    return a, b

def to_halfspaces_xy(ineqs_q, h):
    """
    Convert inequalities in q-space: a·q <= b
    into inequalities in xy-space: A*[x,y] + c <= 0 format for HalfspaceIntersection.
    Using q = (x, y, h - x - y).
    """
    halfspaces = []
    for a, b in ineqs_q:
        # a0*x + a1*y + a2*(h-x-y) <= b
        # (a0 - a2)*x + (a1 - a2)*y <= b - a2*h
        A = (a[0] - a[2])
        B = (a[1] - a[2])
        rhs = b - a[2]*h
        # HalfspaceIntersection expects: [A, B, C] meaning A*x + B*y + C <= 0
        # so set C = -rhs
        halfspaces.append([A, B, -rhs])
    return np.array(halfspaces, dtype=float)

def find_interior_point(halfspaces, tries=20000, seed=0):
    """
    Randomly search for a point strictly inside all halfspaces.
    (Good enough for small problems; avoids LP setup.)
    """
    rng = np.random.default_rng(seed)
    # sample inside the simplex x>=0,y>=0,x+y<=h by rejection
    # but note: regions may be smaller than simplex.
    for _ in range(tries):
        # sample uniform-ish in simplex triangle
        r1, r2 = rng.random(), rng.random()
        if r1 + r2 > 1:
            r1, r2 = 1 - r1, 1 - r2
        x = r1 * 4.0
        y = r2 * (4.0 - x)
        p = np.array([x, y], dtype=float)
        vals = halfspaces[:, 0]*p[0] + halfspaces[:, 1]*p[1] + halfspaces[:, 2]
        if np.all(vals < -1e-7):
            return p
    return None

def polygon_vertices_from_halfspaces(halfspaces, interior_point):
    """
    Compute intersection polygon vertices in xy-plane.
    Returns ordered vertices (xy) or None if empty/unbounded.
    """
    hs = np.array(halfspaces, dtype=float)
    try:
        hs_int = HalfspaceIntersection(hs, interior_point)
    except Exception:
        return None
    pts = hs_int.intersections
    if pts is None or len(pts) < 3:
        return None
    # order them via convex hull
    hull = ConvexHull(pts)
    return pts[hull.vertices]

# ----------------------------
# Hamilton S-piece construction
# ----------------------------

def hamilton_piece_halfspaces(m, S, h=4, closed=True):
    """
    Build inequalities defining the S-piece for output m under Hamilton:
      - let l_i = m_i-1 if i in S else m_i
      - slab: l_i <= q_i <= l_i+1
      - simplex nonneg: q_i >= 0
      - remainder order: for i in S, j not in S: (q_i - l_i) >= (q_j - l_j)
    Returns halfspaces in xy format (A,B,C) for A*x + B*y + C <= 0,
    or None if immediately impossible (e.g., some l_i < 0).
    """
    n = 3
    S = set(S)
    l = [m[i] - 1 if i in S else m[i] for i in range(n)]
    if any(li < 0 for li in l):
        return None

    ineqs_q = []

    # nonnegativity
    for i in range(n):
        ineqs_q.append(nonneg_ineq(i))

    # slab constraints (closed)
    for i in range(n):
        lower = l[i]
        upper = l[i] + 1
        ineqs_q.extend(slab_ineq(i, lower, upper))

    # remainder comparisons
    for i in range(n):
        for j in range(n):
            if i in S and j not in S:
                a, b = remainder_ineq(i, j, l)
                ineqs_q.append((a, b))

    # Note: the plane constraint x+y+z=h is enforced by z = h-x-y substitution.

    return to_halfspaces_xy(ineqs_q, h=h), l

def all_hamilton_pieces(h=4):
    """
    For each integer m with sum h, compute all nonempty S-pieces.
    Returns dict: m -> list of pieces, where each piece is
      { "S": tuple, "l": floor vector, "xy_vertices": array, "q_vertices": array }
    """
    results = {}
    ms = integer_allocations(h=h, n=3)
    for m in ms:
        pieces = []
        # surplus seats = |S| must equal h - sum(l) = h - (sum(m)-|S|) = |S|
        # So any S is arithmetically compatible; geometry will decide emptiness.
        for k in range(0, 3):  # size of S could be 0,1,2 (k=3 would require floors sum 1, impossible with sum 4)
            for S in itertools.combinations(range(3), k):
                halfspaces_and_l = hamilton_piece_halfspaces(m, S, h=h)
                if halfspaces_and_l is None:
                    continue
                halfspaces, l = halfspaces_and_l
                ip = find_interior_point(halfspaces, seed=hash((m, S)) & 0xffffffff)
                if ip is None:
                    continue
                xy_poly = polygon_vertices_from_halfspaces(halfspaces, ip)
                if xy_poly is None:
                    continue
                q_poly = np.array([q_from_xy(p, h=h) for p in xy_poly])
                pieces.append({
                    "S": tuple(S),
                    "l": tuple(l),
                    "xy_vertices": xy_poly,
                    "q_vertices": q_poly
                })
        if pieces:
            results[m] = pieces
    return results

# ----------------------------
# Run it for h=15 and print summary
# ----------------------------

if __name__ == "__main__":
    res = all_hamilton_pieces(h=15)

    print(f"Integer allocations m with sum 15: {len(integer_allocations(15,3))} (should be 15)")
    print(f"m's that actually have at least one nonempty S-piece: {len(res)}")

    for m in sorted(res.keys()):
        print(f"\nm = {m}")
        for piece in res[m]:
            S = piece["S"]
            l = piece["l"]
            verts = piece["q_vertices"]
            print(f"  S={S}  floors l={l}  #verts={len(verts)}")
            # show vertices rounded for readability
            for v in verts:
                print("    ", tuple(np.round(v, 6)))