
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

# ---------------- helpers ----------------
def rot2d(xy, deg):
    th = np.deg2rad(deg)
    R = np.array([[np.cos(th), -np.sin(th)],
                  [np.sin(th),  np.cos(th)]])
    return R @ xy

def circle(r, n=1024):
    t = np.linspace(0, 2*np.pi, n)
    return r*np.cos(t), r*np.sin(t)

def plot_mercury_gradient(ax, path_xy, lw=1.6):
    """Mercury path with Gold→Yellow→Silver gradient (phi/Io split)."""
    x, y = path_xy
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segs = np.concatenate([points[:-1], points[1:]], axis=1)
    s = np.linspace(0.0, 1.0, len(x)-1)
    cmap = LinearSegmentedColormap.from_list(
        "phi_io_mercury",
        ["#f59e0b", "#fde047", "#c0c0c0"], N=256
    )
    lc = LineCollection(segs, cmap=cmap, array=s, linewidth=lw, alpha=0.95)
    ax.add_collection(lc)

def copper_parchment(ax, size=1200, amp=0.06, rot_deg=18):
    """
    Draws a subtle copper-etch/engraving texture:
    - low-frequency sinusoidal 'paper grain'
    - faint radial and hatch lines reminiscent of old scientific plates
    """
    # synthetic parchment via smooth sinusoid mix
    xs = np.linspace(-1.2, 1.2, size)
    ys = np.linspace(-1.2, 1.2, size)
    X, Y = np.meshgrid(xs, ys)
    R = np.sqrt(X*X + Y*Y)
    # smooth large-scale grain
    tex = (np.sin(1.3*X) + np.sin(1.7*Y) + 0.6*np.sin(0.9*(X+Y))) / 3.0
    # normalize and tint toward copper
    tex = (tex - tex.min()) / (tex.max() - tex.min())
    # alpha mask: stronger grain outside center
    mask = np.clip((R - 0.2)/1.2, 0, 1)
    alpha = 0.12*mask  # subtle
    # copper tone blend
    base = np.ones((*tex.shape, 3))
    copper = np.array([245, 213, 182])/255.0  # light copper
    img = (1-amp)*base + amp*tex[...,None]*copper
    ax.imshow(img, extent=(-1.2,1.2,-1.2,1.2), origin="lower", alpha=alpha, zorder=0)

    # faint engraving lines: concentric & hatched
    # concentric
    for r in np.linspace(0.12, 1.06, 60):
        x, y = circle(r, n=720)
        ax.plot(x, y, color="#b08968", linewidth=0.2, alpha=0.08, zorder=1)
    # hatched (rotated lines across the plate)
    th = np.deg2rad(rot_deg)
    c, s = np.cos(th), np.sin(th)
    for u in np.linspace(-1.2, 1.2, 50):
        x0, y0 = -1.3, u
        x1, y1 =  1.3, u
        # rotate
        x0r, y0r = c*x0 - s*y0, s*x0 + c*y0
        x1r, y1r = c*x1 - s*y1, s*x1 + c*y1
        ax.plot([x0r, x1r], [y0r, y1r], color="#9c6644", linewidth=0.25, alpha=0.06, zorder=1)

def main(out_path="resonance_field_III_fresnel_epicycles_v3.png"):
    fig = plt.figure(figsize=(9,9))
    ax = plt.gca()
    ax.set_facecolor("#f8f5f0")  # parchment base

    # Copper/engraving background
    copper_parchment(ax)

    # Fresnel rings
    heights_mm = np.array([2590, 2069, 1576, 722, 541, 433], dtype=float)
    radii = heights_mm / heights_mm[0]
    angles = np.linspace(0, 2*np.pi, 2048)

    # frame A
    for i, r in enumerate(radii, start=1):
        x, y = circle(r, n=1600)
        ax.plot(x, y, color="#7f8c8d", linewidth=0.7, alpha=0.9, zorder=5)
        ax.text(r*np.cos(np.deg2rad(14)),
                r*np.sin(np.deg2rad(14)),
                f"O{i}", fontsize=9, color="#6b7280", zorder=8)

    # frame B (~2° offset)
    for r in radii:
        xy = np.vstack(circle(r, n=1600))
        xy2 = rot2d(xy, 2.0)
        ax.plot(xy2[0], xy2[1], color="#c7cdd8", linewidth=0.6, alpha=0.55, zorder=4)

    # 432/433 gap at O6
    r6 = radii[-1]
    r6_432 = r6 * (432/433)
    x6, y6 = circle(r6)
    x6g, y6g = circle(r6_432)
    ax.plot(x6,  y6,  color="#b45309", linewidth=1.15, alpha=0.95, zorder=6)
    ax.plot(x6g, y6g, color="#f59e0b", linewidth=1.15, alpha=0.95, linestyle="--", zorder=6)
    ax.text(0, -r6*1.08, "Gold gap 432/433", ha="center", va="top",
            fontsize=8, color="#b45309", zorder=8)

    # Δσ ≈ −93° ray
    phi = np.deg2rad(-93.0)
    ax.plot([0, radii[0]*np.cos(phi)],
            [0, radii[0]*np.sin(phi)],
            color="#0ea5e9", linewidth=1.2, alpha=0.9, zorder=7)
    ax.text(0.06*np.cos(phi), 0.06*np.sin(phi),
            "Δσ ≈ −93°", fontsize=8, rotation=-93, color="#0ea5e9", zorder=8)

    # ~60° aperture arc on O3
    arc_r = radii[2]
    th_arc = np.linspace(np.deg2rad(-30), np.deg2rad(30), 180)
    ax.plot(arc_r*np.cos(th_arc), arc_r*np.sin(th_arc),
            color="#10b981", linewidth=1.9, alpha=0.95, zorder=7)
    ax.text(arc_r*np.cos(np.deg2rad(6)),
            arc_r*np.sin(np.deg2rad(6)),
            "≈60° aperture", fontsize=8, color="#047857", zorder=8)

    # Kairos ticks 91° & 97° + golden chord on O1
    r_outer = radii[0]
    for deg, label in [(-91, "91°  NXET (24th prime)"),
                       (-97, "97°  KAIROS (25th prime)")]:
        th = np.deg2rad(deg)
        x_in = (r_outer*0.985)*np.cos(th)
        y_in = (r_outer*0.985)*np.sin(th)
        x_out = (r_outer*1.015)*np.cos(th)
        y_out = (r_outer*1.015)*np.sin(th)
        ax.plot([x_in, x_out], [y_in, y_out],
                color="#f59e0b", linewidth=1.9, alpha=0.98, zorder=9)
        ax.text((r_outer*1.045)*np.cos(th),
                (r_outer*1.045)*np.sin(th),
                label, fontsize=8, color="#b45309",
                ha="center", va="center", zorder=10)

    th1, th2 = np.deg2rad(-91), np.deg2rad(-97)
    p1 = np.array([r_outer*np.cos(th1), r_outer*np.sin(th1)])
    p2 = np.array([r_outer*np.cos(th2), r_outer*np.sin(th2)])
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#f59e0b", linewidth=2.3, alpha=0.98, zorder=9)

    # Geocentric epicycles (frozen)
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

    # Mercury with gradient
    plot_mercury_gradient(ax, mercury, lw=1.65)
    # Venus & Mars
    ax.plot(venus[0], venus[1], color="#22c55e", linewidth=1.25, alpha=0.97, zorder=9, label="Venus")
    ax.plot(mars[0],  mars[1],  color="#b91c1c", linewidth=1.15, alpha=0.97, zorder=9, label="Mars")

    # Sun / Anu
    sun = plt.Circle((0,0), radius=0.055, facecolor="#f59e0b",
                     edgecolor="#b45309", lw=2.0, alpha=0.99, zorder=10)
    ax.add_patch(sun)
    ax.text(0, 0, "Sun / Anu", ha="center", va="center", fontsize=9, color="#111827", zorder=11)

    # Outer markers (Titan, Eris, Southcross)
    def place_marker(angle_deg, label, rfac=1.03, color="#60a5fa"):
        th = np.deg2rad(angle_deg)
        x = r_outer*rfac*np.cos(th)
        y = r_outer*rfac*np.sin(th)
        ax.scatter([x], [y], s=18, color=color, zorder=12)
        ax.text(x, y, f"  {label}", fontsize=8, color=color, ha="left", va="center", zorder=12)

    place_marker( 60, "Titan")
    place_marker(-140, "Eris")
    place_marker( -30, "Southcross")

    # Legend (subtle)
    ax.text(0, -1.18,
            "Legend: Mercury = Gold→Yellow→Silver (phi/Io split) • Venus = Green • Mars = Red‑Copper\n"
            "Kairos ticks: 91° NXET (24th prime) • 97° KAIROS (25th prime) — golden chord\n"
            "Fresnel: O1…O6 (≈2° offset) • Δσ≈−93° • ≈60° aperture • 432/433 gap • Copper‑etch texture",
            fontsize=8.6, color="#4b5563", ha="center", va="top", zorder=13)

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.15, 1.15)
    ax.set_ylim(-1.25, 1.05)
    ax.axis('off')
    ax.set_title("Resonance Field III — Fresnel + Geocentric Epicycles (v3)\n"
                 "Copper‑Etch Texture • Mercury Gradient • Kairos Legend",
                 fontsize=12, pad=12)

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print("Saved:", out_path)

if __name__ == "__main__":
    main()
