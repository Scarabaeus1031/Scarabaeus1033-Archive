
#!/usr/bin/env python3
import argparse, math, os, sys, json, random
import numpy as np
import matplotlib.pyplot as plt

def is_prime(n:int)->bool:
    if n<2: return False
    if n%2==0: return n==2
    r = int(n**0.5)
    f = 3
    while f<=r:
        if n%f==0: return False
        f += 2
    return True

def twin_pairs_upto(N):
    out=set()
    for p in range(3, N-1, 2):
        if is_prime(p) and is_prime(p+2):
            out.add(p); out.add(p+2)
    return out

def euler41_values(N):
    vals=[]
    n=0
    while True:
        v = n*n + n + 41
        if v>N: break
        vals.append(v)
        n+=1
    return vals

def grid_coords(x, width=20):
    # 1-based x → (row, col) zero-based for imshow-like layouts
    x0 = x-1
    row = x0 // width
    col = x0 % width
    return row, col

def triad_mask(cols, centers, sigma, mode, delta):
    mask = np.zeros(cols.shape, dtype=float)
    for c in centers:
        if mode=='gauss':
            mask += np.exp(-0.5*((cols-c)/sigma)**2)
        else:
            mask += (np.abs(cols-c)<=delta).astype(float)
    mask = mask / mask.max() if mask.max()>0 else mask
    return mask

def rails_mask(rows, cols, tau=0.55):
    # √2 and √5 rails (two diagonal families): we approximate by modding the slope patterns
    # Normalize rows/cols to [0,1] to be scale-agnostic, then form two linear families.
    R = (rows - rows.min())/(rows.max()-rows.min()+1e-9)
    C = (cols - cols.min())/(cols.max()-cols.min()+1e-9)
    # slope sqrt(2): c ≈ r * s  (mod 1) and sqrt(5): c ≈ r / s
    s2 = math.sqrt(2.0)
    s5 = math.sqrt(5.0)
    d1 = np.minimum(np.abs(C - (R*s2 % 1.0)), 1 - np.abs(C - (R*s2 % 1.0)))
    d2 = np.minimum(np.abs(C - (R/s2 % 1.0)), 1 - np.abs(C - (R/s2 % 1.0)))
    d3 = np.minimum(np.abs(C - (R*s5 % 1.0)), 1 - np.abs(C - (R*s5 % 1.0)))
    d4 = np.minimum(np.abs(C - (R/s5 % 1.0)), 1 - np.abs(C - (R/s5 % 1.0)))
    rail = (d1<tau) | (d2<tau) | (d3<tau) | (d4<tau)
    return rail.astype(float)

def plot_extended(N=3000, mod_pair=(19,29),
                  centers=(3,10,17), sigma=2.4, mode='gauss', delta=2.0,
                  rails_tau=0.55, twin_alpha=0.75,
                  breath_sec=6, timeline=(7,9,12,17),
                  outpath="vendessimal_extended.png",
                  twin_only=False, threshold_inset=False):

    W=20
    rows = N//W + (1 if N%W else 0)
    R = np.arange(rows)[:,None] * np.ones((1,W))
    C = np.ones((rows,1)) * np.arange(W)[None,:]

    # Base data: residue index combining mod 19/29 for color
    idx = np.zeros((rows, W), dtype=int)
    for x in range(1, N+1):
        r,c = grid_coords(x, width=W)
        i19 = x % mod_pair[0]
        i29 = x % mod_pair[1]
        idx[r,c] = i19*mod_pair[1] + i29

    fig = plt.figure(figsize=(16,9), dpi=150)
    ax = plt.gca()
    im = ax.imshow(idx, cmap='viridis', aspect='auto', interpolation='nearest')
    ax.set_xlabel("Column (×20)"); ax.set_ylabel("Row")
    cb = plt.colorbar(im, ax=ax)
    cb.set_label("Residue index (mod 19 / mod 29)")

    # Triad overlay
    cols = C.copy()
    tmask = triad_mask(cols, centers, sigma, mode, delta)
    ax.imshow(tmask, cmap='autumn', alpha=0.18, aspect='auto', interpolation='nearest')

    # Rails overlay
    rmask = rails_mask(R, C, tau=rails_tau)
    ax.imshow(rmask, cmap='cool', alpha=0.12, aspect='auto', interpolation='nearest')

    # Twins
    twins = twin_pairs_upto(N)
    Y = []
    X = []
    for p in twins:
        r,c = grid_coords(p, width=W)
        Y.append(r); X.append(c)
    ax.scatter(X, Y, s=8, c='yellow', alpha=twin_alpha, marker='s', edgecolor='k', linewidths=0.2)

    # Euler-41
    e41 = euler41_values(N)
    if e41:
        Ye, Xe = [], []
        for v in e41:
            r,c = grid_coords(v, width=W)
            Ye.append(r); Xe.append(c)
        ax.scatter(Xe, Ye, s=14, facecolors='none', edgecolors='white', linewidths=0.8, label='Euler(n^2+n+41)')

    # 1061–1064
    for val, col, lab in [(1061,'lime','1061'), (1063,'orange','1063 (prime)'), (1064,'red','1064=2^3·7·19')]:
        if 1<=val<=N:
            r,c = grid_coords(val, width=W)
            ax.scatter([c],[r], s=120, facecolors='none', edgecolors=col, linewidths=1.8)
            ax.text(c+0.25, r-0.25, lab, color=col, fontsize=8, ha='left', va='bottom')

    title = f"Vendessimal Prime Grid (1…{N}) — triad σ={sigma}, rails τ={rails_tau} | timeline {timeline} × {breath_sec}s"
    ax.set_title(title)

    if twin_only:
        # redo as black background with only twins
        plt.clf()
        fig = plt.figure(figsize=(8,10), dpi=150)
        ax = plt.gca()
        ax.set_facecolor('k')
        ax.scatter(X, Y, s=10, c='#ffee99', alpha=1.0, marker='s')
        ax.set_xlim(-1, W)
        ax.set_ylim(rows, -1)
        ax.set_title(f"Vendessimal Prime Grid — Twin Primes Overlay (≤{N})")
        ax.set_xlabel("Column (1–20)"); ax.set_ylabel("Row (step of 20)")
        outpath = outpath if outpath else "vendessimal_twin_layer.png"
        plt.tight_layout()
        plt.savefig(outpath, bbox_inches='tight')
        return outpath

    if threshold_inset:
        # Minimal inset image focusing 1061–1064 numbers in a small canvas
        plt.clf()
        fig = plt.figure(figsize=(6,3), dpi=150)
        ax = plt.gca()
        for i,val in enumerate([1061,1062,1063,1064]):
            ax.text(i+1, 1, str(val), fontsize=20, fontweight='bold',
                    color=('lime' if val==1061 else 'orange' if val==1063 else 'red' if val==1064 else 'w'))
        ax.set_xlim(0.5, 4.5); ax.set_ylim(0.5, 1.5)
        ax.axis('off')
        ax.set_title("Prime‑Schwelle: 1061 | 1062 | 1063 (prime) | 1064 = 2³·7·19")
        outpath = outpath if outpath else "prime_threshold_1061_1064.png"
        plt.tight_layout()
        plt.savefig(outpath, bbox_inches='tight')
        return outpath

    plt.tight_layout()
    if not outpath: outpath = "vendessimal_extended.png"
    plt.savefig(outpath, bbox_inches='tight')
    return outpath

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--N", type=int, default=3000)
    ap.add_argument("--mod-pair", nargs=2, type=int, default=[19,29])
    ap.add_argument("--centers", nargs=3, type=float, default=[3.0,10.0,17.0])
    ap.add_argument("--sigma", type=float, default=2.4)
    ap.add_argument("--mode", choices=["gauss","hard"], default="gauss")
    ap.add_argument("--delta", type=float, default=2.0)
    ap.add_argument("--rails-tau", type=float, default=0.55)
    ap.add_argument("--twin-alpha", type=float, default=0.75)
    ap.add_argument("--breath-sec", type=float, default=6.0)
    ap.add_argument("--timeline", nargs=4, type=int, default=[7,9,12,17])
    ap.add_argument("--twin-only", action="store_true")
    ap.add_argument("--threshold-inset", action="store_true")
    ap.add_argument("--out", type=str, default="vendessimal_extended.png")
    args = ap.parse_args()

    plot_extended(
        N=args.N, mod_pair=tuple(args["mod-pair"]) if isinstance(args.__dict__.get("mod-pair"), list) else tuple(args.mod_pair),
        centers=tuple(args.centers), sigma=args.sigma, mode=args.mode, delta=args.delta,
        rails_tau=args.rails_tau, twin_alpha=args.twin_alpha,
        breath_sec=args.breath_sec, timeline=tuple(args.timeline),
        twin_only=args.twin_only, threshold_inset=args.threshold_inset,
        outpath=args.out
    )

if __name__=="__main__":
    main()
