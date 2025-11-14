
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from matplotlib.colors import LinearSegmentedColormap

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
    # zeta zero marks (first 15, decorative mapping)
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
    """
    Draws a gentle logarithmic spiral r = a * exp(b*theta), theta in [0, 2π*turns]
    rotated by rot_deg. Used to evoke counter-rotation flows.
    """
    th = np.linspace(0, 2*np.pi*turns, 2000)
    r = a * np.exp(b*th)
    x = r*np.cos(th); y = r*np.sin(th)
    xy = np.vstack((x,y))
    if rot_deg != 0:
        xy = rot2d(xy, rot_deg)
    ax.plot(xy[0], xy[1], color=color, linewidth=lw, alpha=alpha, zorder=z)

def framed_inscription(ax, text, y=-1.24, width=1.9):
    # simple frame line and centered text
    ax.plot([-width/2, width/2], [y+0.02, y+0.02], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.plot([-width/2, width/2], [y-0.18, y-0.18], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.text(0, y-0.08, text, ha="center", va="center", fontsize=8.2, color="#4b5563", zorder=15)

# ---------- main ----------
def main(out_path="resonance_field_V_v5.png"):
    fig = plt.figure(figsize=(9,9))
    ax = plt.gca()
    ax.set_facecolor("#f8f5f0")

    # background
    copper_parchment(ax)

    # Fresnel rings
    heights_mm = np.array([2590, 2069, 1576, 722, 541, 433], dtype=float)
    radii = heights_mm / heights_mm[0]
    angles = np.linspace(0, 2*np.pi, 2048)

    # frame A & labels
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

    # Kairos ticks 91/97 + chord
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

    plot_mercury_gradient(ax, merc, lw=1.65, z=9)
    ax.plot(vene[0], vene[1], color="#22c55e", linewidth=1.25, alpha=0.97, zorder=9)
    ax.plot(mars[0], mars[1], color="#b91c1c", linewidth=1.15, alpha=0.97, zorder=9)

    # Sun / Anu
    sun = plt.Circle((0,0), radius=0.055, facecolor="#f59e0b",
                     edgecolor="#b45309", lw=2.0, alpha=0.99, zorder=10)
    ax.add_patch(sun)
    ax.text(0, 0, "Sun / Anu", ha="center", va="center", fontsize=9, color="#111827", zorder=11)

    # Uranus–Neptune spindle
    ax.plot([0,0], [-1.1, 1.1], color="#60a5fa", linewidth=2.2, alpha=0.18, zorder=3)
    ax.plot([0,0], [-1.1, 1.1], color="#60a5fa", linewidth=0.9, alpha=0.55, zorder=11)
    ax.text(0, 1.12,  "Uranus", fontsize=8.5, color="#3b82f6", ha="center", va="bottom", zorder=12)
    ax.text(0,-1.12, "Neptune", fontsize=8.5, color="#3b82f6", ha="center", va="top", zorder=12)

    # outer markers (Titan/Eris/Southcross + Ganymede @ ~23:00 ≈ 330°)
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
    place_marker( 330, "Ganymede", align="right")  # ≈ 23:00

    # counter-rotating spirals (2 ↔ 3), faint
    spiral(ax, a=0.10, b=0.23, turns=2.7, rot_deg= 25, color="#2563eb", lw=1.3, alpha=0.28, z=8)  # HIIC side (blue)
    spiral(ax, a=0.10, b=0.23, turns=2.7, rot_deg=-25, color="#f59e0b", lw=1.3, alpha=0.28, z=8)  # HIIO side (gold)

    # labels for streams
    ax.text(-0.72,  0.32, "HIIC  /  HIICVI", color="#1e3a8a", fontsize=8.5, zorder=12)
    ax.text( 0.72, -0.32, "HIIIC /  HIIO",   color="#b45309", fontsize=8.5, ha="right", zorder=12)

    # THoTH knot at center (small double ring + label)
    thoth_outer = plt.Circle((0,0), radius=0.085, edgecolor="#374151", facecolor="none", lw=0.8, alpha=0.6, zorder=12)
    thoth_inner = plt.Circle((0,0), radius=0.035, edgecolor="#374151", facecolor="none", lw=0.8, alpha=0.6, zorder=12)
    ax.add_patch(thoth_outer); ax.add_patch(thoth_inner)
    ax.text(0, 0.10, "THoTH", fontsize=8.5, color="#374151", ha="center", va="bottom", zorder=13)

    # decorative Riemann scale on halo
    decorative_riemann(ax, r_outer)

    # inscription
    ins = ("Neutrino‑Lunge: Aus‑ und Einatmen des Feldes (ν ↔ γ) • 2–1–3: Gegenrotationen treffen im Goldring (Erde)\n"
           "THoTH‑Zyklus: AM ↔ VM ↔ PM • Kairos‑Lock 91°/97° • Ganymed–Titan als Wasser/Methan‑Spiegel • Arrokoth–Chiron–Pluto Achse")
    # frame lines + text
    ax.plot([-0.95, 0.95], [-1.22, -1.22], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.plot([-0.95, 0.95], [-1.38, -1.38], color="#8c6d49", linewidth=0.8, alpha=0.6, zorder=14)
    ax.text(0, -1.305, ins, ha="center", va="center", fontsize=8.1, color="#4b5563", zorder=15)

    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.4, 1.08)
    ax.axis('off')
    ax.set_title("Resonance Field V — Counter‑Rotation 2↔3 • THoTH Knot • Ganymede (v5)",
                 fontsize=12, pad=12)

    plt.savefig(out_path, dpi=300, bbox_inches="tight")
    print("Saved:", out_path)

if __name__ == "__main__":
    main()
