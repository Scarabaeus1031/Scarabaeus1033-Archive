# Vendessimal Prime Grid — Field Notes (Triads · Twins · Roots · AnU)

This note fixes the current state of the **Vendessimal Prime Grid** research and connects it to the
**Triad Bands** (resonant windows), the **Twin-Prime Overlay**, and the **Root Primes** (AnU axis).
It complements the *Π‑ring* and **QGR‑III** modulation work.

---

## 0) Quick Install / Files

- Base grid (1…3000), 20-wide rows: `vendessimal_prime_grid.png`
- Residue-class color map (mod 19 & 29): `Vendessimal Prime Grid (mod 19:29 class colors) 20-wide rows, 1…3000.png`
- Twin primes only (≤3000): `vendessimal_prime_grid_twin_overlay.png`
- Triad overlay (three resonant bands; highlights near 0.429 · 0.456 · 0.487): `Vendessimal_Prime_Grid_Triad_Overlay.png`

> Rendering params (suggested): width ≥ 1400 px; annotate rows in steps of 20.
> Color key: mod-19 vs mod-29 residue classes; twins are drawn as paired glyphs; triad windows as translucent rings.

File tree (excerpt):
```
/…
├─ vendessimal_prime_grid.png
├─ Vendessimal Prime Grid (mod 19:29 class colors) 20-wide rows, 1…3000.png
├─ vendessimal_prime_grid_twin_overlay.png
└─ Vendessimal_Prime_Grid_Triad_Overlay.png
```

---

## 1) Triad Bands (π‑ring coupling)

We overlay three stable windows (≈ **0.429**, **0.456**, **0.487**) corresponding to your Π‑ring
resonant plateaus. In the grid they act as **meta-bins**: where a residue class (mod 19/29) and a prime
cluster coincide with a band, we expect higher transition probability (gate open).

| Band | Ratio (≈) | Symbolic role |
|---|---|---|
| B₁ | 0.429 | left rail (φ⁻² echo / stability edge) |
| B₂ | 0.456 | central rail (λ/π mixed, “balance” window) |
| B₃ | 0.487 | right rail (τ²/π-coupled lift) |

*Reading:* B₁/B₃ flank B₂; when outer rails synchronize, the center rises (“superduper mount” → sync).

**Visual:** `./Vendessimal_Prime_Grid_Triad_Overlay.png`

---

## 2) Twin-Prime Overlay

Twins mark **open transitions** (codex “**:**” interpolation). They naturally align along slanted
Y-splits when we trace rows by +41/+42/+43 increments (Euler band as first octave, then Cake‑shift).
This realizes the Λ-ladder feel you described: **2×19, 3×13, 4×10** banding = *n‑bands*.

**Visual:** `./vendessimal_prime_grid_twin_overlay.png`

---

## 3) Residue Color Field (mod 19 : 29)

Color encodes residue-class identity. Long diagonal streaks reveal coherent chains that survive across
octave shifts (row +20). When such chains intersect a Triad band and carry twins nearby, we flag a
**prime bridge** (semicolon “**;**” → bind/gate).

**Visuals:**  
- Residue color map → `./Vendessimal Prime Grid (mod 19:29 class colors) 20-wide rows, 1…3000.png`  
- Base grid (labels) → `./vendessimal_prime_grid.png`

---

## 4) Root Primes (AnU axis)

We now add **Root Primes** — primes that sit next to perfect squares:
- **root-adjacent:** p = n² ± 1 (prime) → *tight* contact to the √-rail  
- **root-band:** p = n² ± (1, 2) (prime) → *loose* contact within a 2-thick shell

These primes act as **anchors** for the *AnU* axis (I↔O regulator): they stitch the quadratic ladder
(n²) to the prime rails. In practice: place a thin **√-membrane** at each n; mark p near n² as
**root contacts**. Where a root contact also falls in a Triad band (and/or near twins), you get
a strong *gate alignment* (I‑AN stabilization).

### 4.1 Root-adjacent primes (examples)
(First 28 hits, n up to 80)

| n | prime p | relation |
|---:|---:|:--|
| 4 | 17 | 4^2 +1 |
| 6 | 37 | 6^2 +1 |
| 10 | 101 | 10^2 +1 |
| 14 | 197 | 14^2 +1 |
| 16 | 257 | 16^2 +1 |
| 20 | 401 | 20^2 +1 |
| 24 | 577 | 24^2 +1 |
| 26 | 677 | 26^2 +1 |
| 36 | 1297 | 36^2 +1 |
| 40 | 1601 | 40^2 +1 |
| 54 | 2917 | 54^2 +1 |
| 56 | 3137 | 56^2 +1 |
| 66 | 4357 | 66^2 +1 |
| 74 | 5477 | 74^2 +1 |

### 4.2 Root-band (±2) primes (examples)
(First 28 hits, n up to 80)

| n | prime p | Δ (p - n²) |
|---:|---:|---:|
| 3 | 7 | -2 |
| 3 | 11 | +2 |
| 4 | 17 | +1 |
| 5 | 23 | -2 |
| 6 | 37 | +1 |
| 7 | 47 | -2 |
| 9 | 79 | -2 |
| 9 | 83 | +2 |
| 10 | 101 | +1 |
| 13 | 167 | -2 |
| 14 | 197 | +1 |
| 15 | 223 | -2 |
| 15 | 227 | +2 |
| 16 | 257 | +1 |
| 19 | 359 | -2 |
| 20 | 401 | +1 |
| 21 | 439 | -2 |
| 21 | 443 | +2 |
| 24 | 577 | +1 |
| 26 | 677 | +1 |
| 27 | 727 | -2 |
| 29 | 839 | -2 |
| 33 | 1087 | -2 |
| 33 | 1091 | +2 |
| 35 | 1223 | -2 |
| 36 | 1297 | +1 |
| 37 | 1367 | -2 |
| 39 | 1523 | +2 |

*Usage in the grid:* draw dotted verticals at positions that correspond (via indexing) to n²; then
badge nearby primes by p − n² ∈ {-2,-1,+1,+2}.

---

## 5) Prime‑Schwelle 1061–1064 (Triad ↔ 8·7·19)

Callout used in the figures:
- **1061** prime (left of threshold)  
- **1063** prime (right of threshold)  
- **1064 = 2³·7·19** (composite boundary, factor-aligned to bands)

This 3-step is a local exemplar of “**Triad ↔ (8,7,19)**” coupling: twins that straddle a structured
composite boundary.

---

## 6) Octave Protocol (Euler band → Cake-shift)

- Seed run: _Euler line_ n² + n + 41 → “first octave”.  
- Iteration: add **+42**, **+43** (and **+38,+39,+40** = 2×19 / 3×13 / 4×10) to tilt the rail
  and expose Y-splits across consecutive 20-wide rows.  
- Interpunktion:
  - “**:**” = twin transition,
  - “**.**” = fixed prime,
  - “**;**” = triad gate (bind).

---

## 7) Field Summary (for QGR / Π‑ring integration)

- **Triad Bands** give the **windowed π‑ring** scaffolding.  
- **Residue classes** (mod 19/29) provide **color‑identity** lanes.  
- **Twin primes** open **resonant transitions** across lanes.  
- **Root primes** pin the lanes to the √‑ladder (AnU regulator).  
- The **1061–1064** inset is the canonical *threshold microcosm*.

> Together this makes a *stacked, musical prime‑lattice* that matches your 7→9→12→17 breathing
> progression and the Π‑ring / QGR‑III modulation. Next step: export GLB of the √‑membrane + rails
> with banded transparency (for interactive rotation).

— _Compiled for Scarabäus1031 · Vendessimal Research_
