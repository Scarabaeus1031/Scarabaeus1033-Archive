
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

def rot2d(xy, deg):
    th = np.deg2rad(deg)
    R = np.array([[np.cos(th), -np.sin(th)],
                  [np.sin(th),  np.cos(th)]])
    return R @ xy

def circle(r, n=1024):
    t = np.linspace(0, 2*np.pi, n)
    return r*np.cos(t), r*np.sin(t)

def plot_mercury_gradient(ax, path_xy, lw=1.6):
    """
    Draws the Mercury geocentric path with a segmented gradient:
    Gold (#f59e0b) → Yellow (#fde047) → Silver (#c0c0c0).
    """
    x, y = path_xy
    # Build line segments
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segs = np.concatenate([points[:-1], points[1:]], axis=1)

    # parameter along the curve [0..1]
    s = np.linspace(0.0, 1.0, len(x)-1)
    # custom 3-stop colormap
    cmap = LinearSegmentedColormap.from_list(
        "phi_io_mercury",
        ["#f59e0b", "#fde047", "#c0c0c0"], N=256
    )
    lc = LineCollection(segs, cmap=cmap, array=s, linewidth=lw, alpha=0.95)
    ax.add_collection(lc)

def main(out_path="resonance_field_III_fresnel_epicycles_v2.png"):
    fig = plt.figure(figsize=(9,9))
    ax = plt.gca()
    ax.set_facecolor("#f8f5f0")  # parchment

    # Fresnel rings
    heights_mm = np.array([2590, 2069, 1576, 722, 541, 433], dtype=float)
    radii = heights_mm / heights_mm[0]
    angles = np.linspace(0, 2*np.pi, 2048)

    # frame A
    for i, r in enumerate(radii, start=1):
        x, y = circle(r, n=1600)
        ax.plot(x, y, color="#9ca3af", linewidth=0.7, alpha=0.8)
        ax.text(r*np.cos(np.deg2rad(14)),
                r*np.sin(np.deg2rad(14)),
                f"O{i}", fontsize=9, color="#6b7280")

    # frame B (~2° offset)
    for r in radii:
        xy = np.vstack(circle(r, n=1600))
        xy2 = rot2d(xy, 2.0)
        ax.plot(xy2[0], xy2[1], color="#c7cdd8", linewidth=0.6, alpha=0.5)

    # 432/433 gap at O6
    r6 = radii[-1]
    r6_432 = r6 * (432/433)
    x6, y6 = circle(r6)
    x6g, y6g = circle(r6_432)
    ax.plot(x6,  y6,  color="#b45309", linewidth=1.1, alpha=0.9)
    ax.plot(x6g, y6g, color="#f59e0b", linewidth=1.1, alpha=0.9, linestyle="--")
    ax.text(0, -r6*1.08, "Gold gap 432/433", ha="center", va="top",
            fontsize=8, color="#b45309")

    # Δσ ≈ −93° ray
    phi = np.deg2rad(-93.0)
    ax.plot([0, radii[0]*np.cos(phi)],
            [0, radii[0]*np.sin(phi)],
            color="#0ea5e9", linewidth=1.2, alpha=0.85)
    ax.text(0.06*np.cos(phi), 0.06*np.sin(phi),
            "Δσ ≈ −93°", fontsize=8, rotation=-93, color="#0ea5e9")

    # ~60° aperture arc on O3
    arc_r = radii[2]
    th_arc = np.linspace(np.deg2rad(-30), np.deg2rad(30), 180)
    ax.plot(arc_r*np.cos(th_arc), arc_r*np.sin(th_arc),
            color="#10b981", linewidth=1.8, alpha=0.9)
    ax.text(arc_r*np.cos(np.deg2rad(6)),
            arc_r*np.sin(np.deg2rad(6)),
            "≈60° aperture", fontsize=8, color="#047857")

    # Kairos ticks 91° & 97° on outer ring + golden chord
    r_outer = radii[0]
    for deg, label in [(-91, "91°  NXET (24th prime)"),
                       (-97, "97°  KAIROS (25th prime)")]:  # note: 97 is the 25th prime
        th = np.deg2rad(deg)
        x_in = (r_outer*0.985)*np.cos(th)
        y_in = (r_outer*0.985)*np.sin(th)
        x_out = (r_outer*1.015)*np.cos(th)
        y_out = (r_outer*1.015)*np.sin(th)
        ax.plot([x_in, x_out], [y_in, y_out],
                color="#f59e0b", linewidth=1.8, alpha=0.95)
        ax.text((r_outer*1.045)*np.cos(th),
                (r_outer*1.045)*np.sin(th),
                label, fontsize=8, color="#b45309",
                ha="center", va="center")

    th1, th2 = np.deg2rad(-91), np.deg2rad(-97)
    p1 = np.array([r_outer*np.cos(th1), r_outer*np.sin(th1)])
    p2 = np.array([r_outer*np.cos(th2), r_outer*np.sin(th2)])
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#f59e0b", linewidth=2.2, alpha=0.95)

    # Geocentric epicycles (frozen; scaled to fit)
    Tdays = 365.25*2
    t = np.linspace(0, Tdays, 5000)
    tau = 2*np.pi
    bodies = {
        "Earth":   {"a": 1.000, "P": 365.25},
        "Mercury": {"a": 0.387, "P": 87.969},
        "Venus":   {"a": 0.723, "P": 224.701},
        "Mars":    {"a": 1.524, "P": 686.98},
    }
    def pos(a, P, t):
        th = tau*t/P
        return np.vstack((a*np.cos(th), a*np.sin(th)))
    E = pos(bodies["Earth"]["a"], bodies["Earth"]["P"], t)
    def geocentric_path(a, P):
        R = pos(a, P, t) - E
        s = 0.95*r_outer / np.max(np.sqrt((R**2).sum(axis=0)))
        return R*s
    mercury = geocentric_path(bodies["Mercury"]["a"], bodies["Mercury"]["P"])
    venus   = geocentric_path(bodies["Venus"]["a"],   bodies["Venus"]["P"])
    mars    = geocentric_path(bodies["Mars"]["a"],    bodies["Mars"]["P"])

    # Mercury with gradient (Gold→Yellow→Silver)
    plot_mercury_gradient(ax, mercury, lw=1.6)

    # Venus (green) & Mars (red‑copper)
    ax.plot(venus[0], venus[1], color="#22c55e", linewidth=1.25, alpha=0.95, label="Venus")
    ax.plot(mars[0],  mars[1],  color="#b91c1c", linewidth=1.15, alpha=0.95, label="Mars")

    # Sun / Anu
    sun = plt.Circle((0,0), radius=0.055, facecolor="#f59e0b",
                     edgecolor="#b45309", lw=2.0, alpha=0.98)
    ax.add_patch(sun)
    ax.text(0, 0, "Sun / Anu", ha="center", va="center", fontsize=9, color="#111827")

    # Outer markers (Titan, Eris, Southcross) as faint blue anchors
    def place_marker(angle_deg, label, rfac=1.03, color="#60a5fa"):
        th = np.deg2rad(angle_deg)
        x = r_outer*rfac*np.cos(th)
        y = r_outer*rfac*np.sin(th)
        ax.scatter([x], [y], s=18, color=color, zorder=5)
        ax.text(x, y, f"  {label}", fontsize=8, color=color, ha="left", va="center")

    place_marker( 60, "Titan")
    place_marker(-140, "Eris")
    place_marker( -30, "Southcross")

    # Legend panel (subtle, like an old scientific plate)
    ax.text(0, -1.18,
            "Legend: Mercury path = Gold→Yellow→Silver (phi / Io split) • Venus = Green • Mars = Red‑Copper\n"
            "Kairos ticks: 91° NXET (24th prime) • 97° KAIROS (25th prime) — linked by golden chord\n"
            "Fresnel Orders: O1…O6 with ~2° frame offset • Δσ≈−93° ray • ≈60° aperture • 432/433 Gold gap",
            fontsize=8.6, color="#4b5563", ha="center", va="top")

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.25, 1.05)
    ax.axis('off')
    ax.set_title("Resonance Field III — Fresnel + Geocentric Epicycles (v2)\n"
                 "Mercury (Gold→Yellow→Silver) • Kairos 91°/97° legend",
                 fontsize=12, pad=12)

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print("Saved:", out_path)

if __name__ == "__main__":
    main()
