
# Vendessimal Prime Toolkit
# Usage: import vendessimal_prime_toolkit as vpt
import math, numpy as np
import matplotlib.pyplot as plt

def primes_upto(n):
    if n < 2: return []
    sieve = np.ones(n+1, dtype=bool)
    sieve[:2] = False
    for p in range(2, int(n**0.5)+1):
        if sieve[p]: sieve[p*p:n+1:p] = False
    return np.flatnonzero(sieve).tolist()

def grid_xy(n, width=20):
    n0 = n-1
    return n0//width, n0%width

def to_flat_index(row,col,width=20):
    return row*width+col+1

def triad_mask(rows, width=20, centers=(3.5,10,16.5), sigma=2.2, delta=2.0, mode='gauss'):
    X = np.tile(np.arange(width)[None,:], (rows,1))
    M = np.zeros((rows, width), dtype=float)
    for c in centers:
        if mode=='gauss':
            M += np.exp(-0.5*((X-c)/sigma)**2)
        else:
            M += (np.abs(X-c) <= delta).astype(float)
    return M/ M.max() if M.max()>0 else M

def twin_primes_upto(n):
    ps = primes_upto(n+2); s=set(ps)
    return [p for p in ps if p+2 in s]

def rail_membership(rows, width, slope, b_list, tau=0.6):
    members=set()
    for r in range(rows):
        for b in b_list:
            pred = (slope*r + b) % width
            for c in range(width):
                d = min((c-pred)%width, (pred-c)%width)
                if d<=tau:
                    n = to_flat_index(r,c,width)
                    members.add(n)
    return members

def euler_41_trace(N):
    vals=[]; n=0
    while True:
        v=n*n+n+41
        if v>N: break
        vals.append(v); n+=1
    return vals

def plot_extended(N=3000, width=20, mod_pair=(19,29),
                  triad_cfg=dict(centers=(3.5,10,16.5), sigma=2.2, delta=2.0, mode='gauss'),
                  rails_tau=0.55,
                  outpath="vendessimal_extended.png"):
    rows=(N+width-1)//width
    A=np.zeros((rows,width))
    for n in range(1, rows*width+1):
        r,c=grid_xy(n,width)
        a=n%mod_pair[0]; b=n%mod_pair[1]
        A[r,c]=a + b*mod_pair[0]
    M=triad_mask(rows,width,**triad_cfg)
    fig=plt.figure(figsize=(14,8)); ax=plt.gca()
    img=ax.imshow(A, cmap='viridis', origin='upper', interpolation='nearest', aspect='auto')
    ax.imshow(np.ones_like(M), cmap='gray', alpha=1-M*0.65, origin='upper', interpolation='nearest', aspect='auto')
    # overlays
    twins=twin_primes_upto(N)
    xs=[]; ys=[]
    for p in twins:
        r,c=grid_xy(p,width); xs.append(c); ys.append(r)
    ax.scatter(xs, ys, s=10, marker='s', edgecolor='gold', facecolor='none', linewidths=0.8, label='twin primes')
    rails2=rail_membership(rows,width, math.sqrt(2), [0,5,10,15], tau=rails_tau)
    rails5=rail_membership(rows,width, math.sqrt(5), [0,5,10,15], tau=rails_tau)
    for sset,col in [(rails2,'white'), (rails5,'orange')]:
        xs=[]; ys=[]
        for n in sset:
            if n<=N:
                r,c=grid_xy(n,width); xs.append(c); ys.append(r)
        ax.scatter(xs, ys, s=4, color=col, alpha=0.8, label=f'rail {"√2" if col=="white" else "√5"}')
    e41=euler_41_trace(N)
    xs=[]; ys=[]
    for v in e41:
        r,c=grid_xy(v,width); xs.append(c); ys.append(r)
    ax.scatter(xs, ys, s=24, marker='P', color='#ffdd55', edgecolor='black', linewidths=0.3, label='Euler n²+n+41')
    # 1061/1063/1064
    for value, txt, col in [(1061,'1061 (prime)','lime'), (1063,'1063 (prime)','lime'), (1064,'1064 = 2³·7·19','red')]:
        r,c=grid_xy(value,width); ax.scatter([c],[r], s=100, marker='o', color='none', edgecolor=col, linewidths=2.0)
        ax.text(c+0.3, r-0.3, txt, color=col, fontsize=8, weight='bold')
    ax.set_title(f"Vendessimal Prime Grid (1…{N}) — extended overlays")
    ax.set_xlabel("Column (×20)"); ax.set_ylabel("Row")
    ax.set_xlim(-0.5, width-0.5); ax.set_ylim(rows-0.5, -0.5)
    ax.grid(True, color='w', alpha=0.15, ls=':', lw=0.5)
    cbar=plt.colorbar(img, ax=ax, fraction=0.025, pad=0.02); cbar.set_label("Residue index")
    ax.legend(loc='upper right', fontsize=8, framealpha=0.85)
    plt.tight_layout(); fig.savefig(outpath, dpi=180); plt.close(fig); return outpath
