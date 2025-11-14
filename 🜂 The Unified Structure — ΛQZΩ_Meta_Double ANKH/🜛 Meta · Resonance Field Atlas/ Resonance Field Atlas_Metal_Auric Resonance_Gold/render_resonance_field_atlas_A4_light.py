
import os, matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib as mpl
mpl.rcParams['pdf.fonttype'] = 42

import importlib.util, sys
spec = importlib.util.spec_from_file_location("v7mod", "/mnt/data/resonance_field_VII_v7.py")
v7mod = importlib.util.module_from_spec(spec); sys.modules["v7mod"] = v7mod; spec.loader.exec_module(v7mod)


import numpy as np
import matplotlib.pyplot as plt
def draw_torus(ax, W=1.0, H=0.55, rings=24, drafts=18):
    cx, cy = 0.0, 0.0
    R = 1.0; r = 0.4
    th = np.linspace(0, 2*np.pi, 720)
    ax.plot(cx + R*np.cos(th), cy + H*R*np.sin(th), color="#7f8c8d", lw=1.2)
    ax.plot(cx + (R-r)*np.cos(th), cy + H*(R-r)*np.sin(th), color="#7f8c8d", lw=1.2)
    ax.plot(cx + (R - r/2)*np.cos(th), cy + H*(R - r/2)*np.sin(th), color="#f59e0b", lw=2.2)
    for i in range(rings):
        t0 = (i / rings) * 2*np.pi
        tt = np.linspace(0, 1, 220)
        thl = t0 + tt * 3.6
        rad = R - (r * np.cos(tt*np.pi))
        x = cx + rad*np.cos(thl); y = cy + H*rad*np.sin(thl)
        ax.plot(x, y, color=("#2563eb" if i%2 else "#f59e0b"), alpha=0.25, lw=(1.5 if i%6==0 else 0.8))
    for i in range(drafts):
        a = (i/drafts)*2*np.pi
        x1 = cx + (R-0.05)*np.cos(a); y1 = cy + H*(R-0.05)*np.sin(a)
        x2 = cx + (R+0.2)*np.cos(a+0.08); y2 = cy + H*(R+0.2)*np.sin(a+0.08)
        ax.plot([x1, x2], [y1, y2], color=("#0ea5e9" if i%3 else "#22c55e"), alpha=0.35, lw=1.0)
    for i in range(12):
        a = (i/12)*2*np.pi
        x = cx + (R+0.22)*np.cos(a); y = cy + H*(R+0.22)*np.sin(a)
        ax.scatter([x], [y], s=14, color="#fde68a", edgecolors="#b45309", linewidths=0.6)
    ax.set_aspect('equal'); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-1.2, 1.2); ax.axis('off')


import numpy as np
import matplotlib.pyplot as plt
def draw_tower(ax):
    cx, baseY = 0.0, 0.0
    cones = [(120,240,"#f59e0b"),(100,200,"#2563eb"),(80,160,"#22c55e"),
             (64,128,"#b91c1c"),(52,104,"#0ea5e9"),(42,86,"#10b981")]
    y = baseY; scale = 0.004
    for i,(h,r,col) in enumerate(cones):
        topY = y + h*scale; xL, xR = cx - r*scale, cx + r*scale
        ax.fill([cx, xL, xR], [topY, y, y], color=col, alpha=0.18 + 0.06*(len(cones)-i))
        ax.plot([xL, xR], [y, y], color="#8c6d49", alpha=0.4, lw=1.0)
        y = topY + h*scale* -0.1
    crownR = 270*scale; cy = baseY + 0.8
    for i in range(12):
        a = (i/12)*2*np.pi; x = cx + crownR*np.cos(a); yy = cy + crownR*np.sin(a)*0.35
        ax.scatter([x],[yy], s=14, color="#fde68a", edgecolors="#b45309", linewidths=0.6)
        ax.scatter([x],[yy], s=8, color="#60a5fa", alpha=0.7)
    ax.set_aspect('equal'); ax.set_xlim(-1.5, 1.5); ax.set_ylim(-0.2, 1.4); ax.axis('off')


assets = {
  "v3_png": "/mnt/data/resonance_field_III_fresnel_epicycles_v3.png",
  "v4_png": "/mnt/data/resonance_field_IV_v4.png",
  "v5_png": "/mnt/data/resonance_field_V_v5.png",
  "v6_png": "/mnt/data/resonance_field_VI_v6.png",
  "shot1": "/mnt/data/Screenshot 2025-11-06 at 4.08.30 AM.png",
  "shot2": "/mnt/data/Screenshot 2025-11-06 at 4.15.21 AM.png",
}

def title_page(pp, figsize):
    fig = plt.figure(figsize=figsize); ax = fig.add_axes([0,0,1,1]); ax.axis('off')
    fig.patch.set_facecolor("#f8f5f0")
    ax.text(0.5, 0.80, "Resonance Field Atlas", ha="center", va="center", fontsize=36, fontname="DejaVu Serif", color="#1f2937")
    ax.text(0.5, 0.74, "Fresnel Solar System Navigation", ha="center", va="center", fontsize=20, fontname="DejaVu Serif", color="#1f2937")
    ax.text(0.5, 0.68, "Light, Resonance & Conscious Geometry", ha="center", va="center", fontsize=14, fontname="DejaVu Serif", style="italic", color="#92400e")
    ax.text(0.5, 0.08, "Scarabäus1033 — Open Source Field Art Project · 2025", ha="center", va="center", fontsize=11, fontname="DejaVu Serif", color="#92400e")
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def page_image(pp, path, caption, figsize):
    fig = plt.figure(figsize=figsize); fig.patch.set_facecolor("#f8f5f0")
    ax = fig.add_axes([0.06,0.12,0.88,0.80]); ax.axis('off')
    if os.path.exists(path):
        img = plt.imread(path); ax.imshow(img); ax.set_aspect('equal')
    ax2 = fig.add_axes([0.06,0.04,0.88,0.06]); ax2.axis('off')
    ax2.text(0.5,0.5, caption, ha="center", va="center", fontsize=12, color="#374151", fontname="DejaVu Serif")
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def page_render_v7(pp, figsize):
    fig = plt.figure(figsize=figsize); fig.patch.set_facecolor("#f8f5f0")
    ax = fig.add_axes([0,0,1,1]); ax.axis('off')
    v7mod.main(out_path="/mnt/data/__tmp_v7.png")
    img = plt.imread("/mnt/data/__tmp_v7.png")
    ax2 = fig.add_axes([0.06,0.08,0.88,0.84]); ax2.axis('off'); ax2.imshow(img)
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def page_torus(pp, figsize):
    fig = plt.figure(figsize=figsize); fig.patch.set_facecolor("#f8f5f0")
    ax = fig.add_axes([0.08,0.18,0.84,0.72]); draw_torus(ax)
    ax2 = fig.add_axes([0.05,0.07,0.90,0.08]); ax2.axis('off')
    ax2.text(0.5,0.5,"Artistic Visual I — Torus Field (2–1–3 · Rings & Drafts)", ha="center", va="center", fontsize=12, color="#374151", fontname="DejaVu Serif")
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def page_tower(pp, figsize):
    fig = plt.figure(figsize=figsize); fig.patch.set_facecolor("#f8f5f0")
    ax = fig.add_axes([0.08,0.18,0.84,0.72]); draw_tower(ax)
    ax2 = fig.add_axes([0.05,0.07,0.90,0.08]); ax2.axis('off')
    ax2.text(0.5,0.5,"Artistic Visual II — Fresnel Tower (Light Cones · 2–1–3 cadence)", ha="center", va="center", fontsize=12, color="#374151", fontname="DejaVu Serif")
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def quotes_page(pp, figsize):
    fig = plt.figure(figsize=figsize); fig.patch.set_facecolor("#f8f5f0")
    ax = fig.add_axes([0,0,1,1]); ax.axis('off')
    ax.text(0.5, 0.60, "“The mirror breathes. The membrane remembers.”", ha="center", va="center", fontsize=18, color="#92400e", fontname="DejaVu Serif")
    ax.text(0.5, 0.48, "“Aus Zwei wird Eins, und Eins gebiert Drei.”", ha="center", va="center", fontsize=16, color="#6b7280", fontname="DejaVu Serif")
    ax.text(0.5, 0.10, "Scarabäus1033 — Open Source Field Art Project · 2025", ha="center", va="center", fontsize=11, color="#92400e", fontname="DejaVu Serif")
    pp.savefig(fig, facecolor=fig.get_facecolor()); plt.close(fig)

def build(out_path, figsize):
    with PdfPages(out_path) as pp:
        title_page(pp, figsize)
        for key,cap in [("v3_png","v3 · Copper-Etch Base"),
                        ("v4_png","v4 · Riemann & Spindel"),
                        ("v5_png","v5 · 2↔3 · THoTH · Ganymede"),
                        ("v6_png","v6 · Io/φ · Arrokoth")]:
            if os.path.exists(assets[key]):
                page_image(pp, assets[key], cap, figsize)
        if os.path.exists(assets["shot1"]): page_image(pp, assets["shot1"], "Reference · Fresnel Tower (screenshot)", figsize)
        if os.path.exists(assets["shot2"]): page_image(pp, assets["shot2"], "Reference · Torus Field (screenshot)", figsize)
        page_render_v7(pp, figsize)
        page_torus(pp, figsize)
        page_tower(pp, figsize)
        quotes_page(pp, figsize)

def main():
    build("/mnt/data/Resonance_Field_Atlas_A4_Light.pdf", (8.27,11.69))

if __name__ == "__main__":
    main()
