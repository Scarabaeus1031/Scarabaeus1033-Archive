
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.patches import Ellipse

# ---------- helpers ----------
def rot2d(xy, deg):
    th = np.deg2rad(deg)
    R = np.array([[np.cos(th), -np.sin(th)],
                  [np.sin(th),  np.cos(th)]])
    return R @ xy

def circle(r, n=1024):
    t = np.linspace(0, 2*np.pi, n)
    return r*np.cos(t), r*np.sin(t)

def plot_mercury_gradient(ax, path_xy, lw=1.6, z=9):
    x, y = path_xy
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segs = np.concatenate([points[:-1], points[1:]], axis=1)
    s = np.linspace(0.0, 1.0, len(x)-1)
    cmap = LinearSegmentedColormap.from_list(
        "phi_io_mercury",
        ["#f59e0b", "#fde047", "#c0c0c0"], N=256
    )
    lc = LineCollection(segs, cmap=cmap, array=s, linewidth=lw, alpha=0.97, zorder=z)
    ax.add_collection(lc)

def copper_parchment(ax, size=1200, amp=0.06, rot_deg=18):
    xs = np.linspace(-1.2, 1.2, size)
    ys = np.linspace(-1.2, 1.2, size)
    X, Y = np.meshgrid(xs, ys)
    R = np.sqrt(X*X + Y*Y)
    tex = (np.sin(1.3*X) + np.sin(1.7*Y) + 0.6*np.sin(0.9*(X+Y))) / 3.0
    tex = (tex - tex.min()) / (tex.max() - tex.min())
    mask = np.clip((R - 0.2)/1.2, 0, 1)
    alpha = 0.12*mask
    base = np.ones((*tex.shape, 3))
    copper = np.array([245, 213, 182])/255.0
    img = (1-amp)*base + amp*tex[...,None]*copper
    ax.imshow(img, extent=(-1.2,1.2,-1.2,1.2), origin="lower", alpha=alpha, zorder=0)

    # micro-engraving
    for r in np.linspace(0.12, 1.06, 60):
        x, y = circle(r, n=720)
        ax.plot(x, y, color="#b08968", linewidth=0.2, alpha=0.08, zorder=1)

    # hatch
    th = np.deg2rad(rot_deg)
    c, s = np.cos(th), np.sin(th)
    for u in np.linspace(-1.2, 1.2, 50):
        x0, y0 = -1.3, u
        x1, y1 =  1.3, u
        x0r, y0r = c*x0 - s*y0, s*x0 + c*y0
        x1r, y1r = c*x1 - s*y1, s*x1 + c*y1
        ax.plot([x0r, x1r], [y0r, y1r], color="#9c6644", linewidth=0.25, alpha=0.06, zorder=1)

def decorative_riemann(ax, r_outer):
    # ticks
    for deg in range(0, 360, 5):
        th = np.deg2rad(deg)
        L = 0.012 if deg % 30 == 0 else 0.007
        rin = r_outer*(1.03)
        rout = r_outer*(1.03+L)
        ax.plot([rin*np.cos(th), rout*np.cos(th)],
                [rin*np.sin(th), rout*np.sin(th)],
                color="#8c6d49", linewidth=0.6 if deg % 30 else 0.9, alpha=0.7, zorder=10)
    # zeta zero marks (decorative)
    zeta_zeros = np.array([
        14.134725, 21.022040, 25.010858, 30.424876, 32.935062,
        37.586178, 40.918719, 43.327073, 48.005150, 49.773832,
        52.970322, 56.446247, 59.347044, 60.831779, 65.112545
    ])
    angs = (zeta_zeros - zeta_zeros.min())/(zeta_zeros.max()-zeta_zeros.min())*360.0
    for a in angs:
        th = np.deg2rad(a)
        xh = r_outer*1.085*np.cos(th)
        yh = r_outer*1.085*np.sin(th)
        ax.scatter([xh], [yh], s=8, color="#ffffff", zorder=13, edgecolors="#f59e0b", linewidths=0.5)
        ax.plot([r_outer*1.06*np.cos(th), r_outer*1.09*np.cos(th)],
                [r_outer*1.06*np.sin(th), r_outer*1.09*np.sin(th)],
                color="#f59e0b", linewidth=0.8, alpha=0.9, zorder=12)

def spiral(ax, a=0.12, b=0.18, turns=2.5, rot_deg=0, color="#60a5fa", lw=1.0, alpha=0.35, z=8):
    th = np.linspace(0, 2*np.pi*turns, 2000)
    r = a * np.exp(b*th)
    x = r*np.cos(th); y = r*np.sin(th)
    xy = np.vstack((x,y))
    if rot_deg != 0:
        xy = rot2d(xy, rot_deg)
    ax.plot(xy[0], xy[1], color=color, linewidth=lw, alpha=alpha, zorder=z)

# ---------- main ----------
def main(out_path="resonance_field_VII_v7.png"):
    fig = plt.figure(figsize=(9,9))
    ax = plt.gca()
    ax.set_aspect('equal', adjustable='box')
    ax.set_facecolor("#f8f5f0")

    # background
    copper_parchment(ax)

    # Fresnel rings
    heights_mm = np.array([2590, 2069, 1576, 722, 541, 433], dtype=float)
    radii = heights_mm / heights_mm[0]
    angles = np.linspace(0, 2*np.pi, 2048)

    # frames
    for i, r in enumerate(radii, start=1):
        x, y = circle(r, n=1600)
        ax.plot(x, y, color="#7f8c8d", linewidth=0.7, alpha=0.9, zorder=5)
        ax.text(r*np.cos(np.deg2rad(14)), r*np.sin(np.deg2rad(14)), f"O{i}", fontsize=9, color="#6b7280", zorder=8)
    for r in radii:
        xy = np.vstack(circle(r, n=1600))
        xy2 = rot2d(xy, 2.0)
        ax.plot(xy2[0], xy2[1], color="#c7cdd8", linewidth=0.6, alpha=0.55, zorder=4)

    # 432/433 gap at O6
    r6 = radii[-1]
    r6_432 = r6 * (432/433)
    x6, y6 = circle(r6); x6g, y6g = circle(r6_432)
    ax.plot(x6,  y6,  color="#b45309", linewidth=1.15, alpha=0.95, zorder=6)
    ax.plot(x6g, y6g, color="#f59e0b", linewidth=1.15, alpha=0.95, linestyle="--", zorder=6)
    ax.text(0, -r6*1.08, "Gold gap 432/433", ha="center", va="top", fontsize=8, color="#b45309", zorder=8)

    # Δσ and aperture
    phi = np.deg2rad(-93.0)
    ax.plot([0, radii[0]*np.cos(phi)], [0, radii[0]*np.sin(phi)], color="#0ea5e9", linewidth=1.2, alpha=0.9, zorder=7)
    ax.text(0.06*np.cos(phi), 0.06*np.sin(phi), "Δσ ≈ −93°", fontsize=8, rotation=-93, color="#0ea5e9", zorder=8)
    arc_r = radii[2]
    th_arc = np.linspace(np.deg2rad(-30), np.deg2rad(30), 180)
    ax.plot(arc_r*np.cos(th_arc), arc_r*np.sin(th_arc), color="#10b981", linewidth=1.9, alpha=0.95, zorder=7)
    ax.text(arc_r*np.cos(np.deg2rad(6)), arc_r*np.sin(np.deg2rad(6)), "≈60° aperture", fontsize=8, color="#047857", zorder=8)

    # Kairos ticks and chord
    r_outer = radii[0]
    for deg, label in [(-91, "91°  NXET (24th)"), (-97, "97°  KAIROS (25th)")]:
        th = np.deg2rad(deg)
        x_in = (r_outer*0.985)*np.cos(th); y_in = (r_outer*0.985)*np.sin(th)
        x_out= (r_outer*1.015)*np.cos(th); y_out= (r_outer*1.015)*np.sin(th)
        ax.plot([x_in, x_out], [y_in, y_out], color="#f59e0b", linewidth=1.9, alpha=0.98, zorder=9)
        ax.text((r_outer*1.045)*np.cos(th), (r_outer*1.045)*np.sin(th),
                label, fontsize=8, color="#b45309", ha="center", va="center", zorder=10)
    th1, th2 = np.deg2rad(-91), np.deg2rad(-97)
    p1 = np.array([r_outer*np.cos(th1), r_outer*np.sin(th1)])
    p2 = np.array([r_outer*np.cos(th2), r_outer*np.sin(th2)])
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], color="#f59e0b", linewidth=2.3, alpha=0.98, zorder=9)

    # geocentric epicycles (frozen)
    Tdays = 365.25*2
    t = np.linspace(0, Tdays, 5000)
    tau = 2*np.pi
    bodies = {"Earth":{"a":1.0,"P":365.25},
              "Mercury":{"a":0.387,"P":87.969},
              "Venus":{"a":0.723,"P":224.701},
              "Mars":{"a":1.524,"P":686.98}}
    def pos(a,P,t):
        th = tau*t/P
        return np.vstack((a*np.cos(th), a*np.sin(th)))
    E = pos(bodies["Earth"]["a"], bodies["Earth"]["P"], t)
    def geocentric(a,P):
        R = pos(a,P,t) - E
        s = 0.95*r_outer / np.max(np.sqrt((R**2).sum(axis=0)))
        return R*s
    merc = geocentric(bodies["Mercury"]["a"], bodies["Mercury"]["P"])
    vene = geocentric(bodies["Venus"]["a"],   bodies["Venus"]["P"])
    mars = geocentric(bodies["Mars"]["a"],    bodies["Mars"]["P"])

    # Mercury path (gradient) + Io/phi marker
    points = np.array([merc[0], merc[1]]).T.reshape(-1, 1, 2)
    segs = np.concatenate([points[:-1], points[1:]], axis=1)
    s = np.linspace(0.0, 1.0, len(merc[0])-1)
    cmap = LinearSegmentedColormap.from_list("phi_io_mercury", ["#f59e0b", "#fde047", "#c0c0c0"], N=256)
    lc = LineCollection(segs, cmap=cmap, array=s, linewidth=1.7, alpha=0.97, zorder=9)
    ax.add_collection(lc)
    idx = int(0.40*(merc.shape[1]-1))
    x_io, y_io = merc[0, idx], merc[1, idx]
    io = plt.Circle((x_io, y_io), radius=0.014, facecolor="#f472b6", edgecolor="#fca5a5", lw=0.8, alpha=0.95, zorder=12)
    ax.add_patch(io)

    # Venus & Mars
    ax.plot(vene[0], vene[1], color="#22c55e", linewidth=1.25, alpha=0.97, zorder=9)
    ax.plot(mars[0], mars[1], color="#b91c1c", linewidth=1.15, alpha=0.97, zorder=9)

    # Sun / Anu
    sun = plt.Circle((0,0), radius=0.055, facecolor="#f59e0b",
                     edgecolor="#b45309", lw=2.0, alpha=0.99, zorder=10)
    ax.add_patch(sun)
    ax.text(0, 0, "Sun / Anu", ha="center", va="center", fontsize=9, color="#111827", zorder=11)

    # Uranus–Neptune spindle (with pink heartline)
    ax.plot([0,0], [-1.1, 1.1], color="#60a5fa", linewidth=2.2, alpha=0.18, zorder=3)
    ax.plot([0,0], [-1.1, 1.1], color="#60a5fa", linewidth=0.9, alpha=0.55, zorder=11)
    ax.plot([0,0], [0.0, 1.08], color="#f472b6", linewidth=1.2, alpha=0.20, zorder=11)

    # outer markers (Titan/Eris/Southcross/Ganymede)
    def place_marker(angle_deg, label, rfac=1.03, color="#60a5fa", align="left"):
        th = np.deg2rad(angle_deg)
        x = r_outer*rfac*np.cos(th); y = r_outer*rfac*np.sin(th)
        ax.scatter([x], [y], s=20, color=color, zorder=12)
        ha = "left" if align=="left" else "right"
        dx = 0.0 if align=="center" else (0.01 if ha=="left" else -0.01)
        ax.text(x+dx, y, f"  {label}" if ha=="left" else f"{label}  ",
                fontsize=8, color=color, ha=ha, va="center", zorder=12)

    place_marker( 60,  "Titan")
    place_marker(-140, "Eris")
    place_marker( -30, "Southcross")
    place_marker( 330, "Ganymede", align="right")

    # counter-rotating spirals (faint)
    def spiral(ax, a=0.10, b=0.23, turns=2.7, rot_deg= 25, color="#2563eb", lw=1.3, alpha=0.28, z=8):
        th = np.linspace(0, 2*np.pi*turns, 2000)
        r = a * np.exp(b*th)
        x = r*np.cos(th); y = r*np.sin(th)
        xy = np.vstack((x,y))
        if rot_deg != 0:
            xy = rot2d(xy, rot_deg)
        ax.plot(xy[0], xy[1], color=color, linewidth=lw, alpha=alpha, zorder=z)

    spiral(ax, a=0.10, b=0.23, turns=2.7, rot_deg= 25, color="#2563eb", lw=1.3, alpha=0.28, z=8)
    spiral(ax, a=0.10, b=0.23, turns=2.7, rot_deg=-25, color="#f59e0b", lw=1.3, alpha=0.28, z=8)

    # labels for streams
    ax.text(-0.72,  0.32, "HIIC  /  HIICVI", color="#1e3a8a", fontsize=8.5, zorder=12)
    ax.text( 0.72, -0.32, "HIIIC /  HIIO",   color="#b45309", fontsize=8.5, ha="right", zorder=12)

    # symbolic Arrokoth (double shell) at spindle top
    rA = r_outer*1.085
    xA, yA = 0.0, rA
    e1 = Ellipse((xA-0.03, yA), width=0.10, height=0.06, angle=0,
                 edgecolor="#ec4899", facecolor="#f472b6", alpha=0.5, lw=1.0, zorder=13)
    e2 = Ellipse((xA+0.03, yA), width=0.10, height=0.06, angle=0,
                 edgecolor="#ec4899", facecolor="#f472b6", alpha=0.5, lw=1.0, zorder=13)
    ax.add_patch(e1); ax.add_patch(e2)
    ax.plot([xA-0.04, xA+0.04], [yA, yA], color="#ec4899", linewidth=1.2, alpha=0.8, zorder=14)

    # decorative Riemann scale
    decorative_riemann(ax, r_outer)

    # 2^n scale (inner ring): small ticks and labels around a compact radius
    r_inner = 0.22
    x_inn, y_inn = circle(r_inner, n=1200)
    ax.plot(x_inn, y_inn, color="#c0c0c0", linewidth=0.6, alpha=0.7, zorder=6)
    ns = list(range(-3, 9))  # n = -3..8
    for i, n in enumerate(ns):
        th = 2*np.pi * (i / len(ns))  # evenly spaced for aesthetics
        # alternating gold/silver ticks
        col = "#f59e0b" if i % 2 == 0 else "#c0c0c0"
        ax.plot([r_inner*0.98*np.cos(th), r_inner*1.02*np.cos(th)],
                [r_inner*0.98*np.sin(th), r_inner*1.02*np.sin(th)],
                color=col, linewidth=1.0, alpha=0.9, zorder=7)
        ax.text(r_inner*1.06*np.cos(th), r_inner*1.06*np.sin(th),
                f"2^{n}", fontsize=7.5, color="#6b7280",
                ha="center", va="center", zorder=8)

    # Jupiter–Saturn axis (V–6) horizontal with belts
    ax.plot([-1.08, 1.08], [0, 0], color="#a3a3a3", linewidth=0.7, alpha=0.7, zorder=3)  # base
    # soft gold halo left (Jupiter), dark grey right (Saturn)
    ax.plot([-1.08, -0.10], [0,0], color="#f59e0b", linewidth=1.8, alpha=0.25, zorder=7)
    ax.plot([ 0.10,  1.08], [0,0], color="#111827", linewidth=1.8, alpha=0.25, zorder=7)
    ax.text(-1.10, 0.03, "Jupiter (V)", fontsize=8, color="#b45309", ha="left", zorder=8)
    ax.text( 1.10, 0.03, "Saturn (6)",  fontsize=8, color="#374151", ha="right", zorder=8)
    # Black Sun near Saturn
    ax.add_patch(plt.Circle((0.88, 0.0), radius=0.05, facecolor="#0b0f19", edgecolor="#374151", lw=0.8, alpha=0.75, zorder=8))

    # faint belts (asteroid & kuiper) as translucent annuli
    for rB, aB in [(0.48, 0.06), (1.00, 0.04)]:
        xB, yB = circle(rB)
        ax.plot(xB, yB, color="#8c6d49", linewidth=1.0, alpha=0.10, zorder=2)
        # subtle blur via multiple offsets
        for k in range(1,4):
            xBo, yBo = circle(rB + k*0.006)
            ax.plot(xBo, yBo, color="#8c6d49", linewidth=0.6, alpha=0.05, zorder=2)

    # inscription with Visoko note
    ins = ("Neutrino‑Lunge: ν↔γ • 2–1–3 Gegenrotationen im Goldring • Kairos 91°/97° • "
           "Ganymede–Titan–Arrokoth Trias • Uranus–Neptun Spindel • Jupiter–Saturn V–6 Achse • "
           "Visoko — Double Breathing Crystal")
    ax.plot([-0.95, 0.95], [-1.22, -1.22], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.plot([-0.95, 0.95], [-1.38, -1.38], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.text(0, -1.305, ins, ha="center", va="center", fontsize=8.1, color="#4b5563", zorder=15)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.4, 1.08)
    ax.axis('off')
    ax.set_title("Resonance Field VII — 2^n Mercury Scale • V–6 Axis • Belts • Visoko (v7)",
                 fontsize=12, pad=12)

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print("Saved:", out_path)

if __name__ == "__main__":
    main()
