# PRIME–ROOTS BRIDGE (concept note)

This folder collects the *vendessimal* prime-grid outputs and a compact bridge map that ties together:

- **Residue classes mod 19 & 29** as the color logic (prime roots)
- **Twin-prime overlays** as orientation rails (':' vertical motif)
- **Triad windows** (π-bands) layered over 20-wide rows
- The **prime threshold** around **1061 / 1063** with **1064 = 2^3·7·19**
- A long-link motif **1087 → 7801 → 17399** (used as a narrative connector in the Codex)

## Files
- `vendessimal_prime_grid.png` — base grid (1…3000), class-colored by mod 19/29
- `Vendessimal_Prime_Grid_Triad_Overlay.png` — triad rings overlay (π-bands)
- `vendessimal_prime_grid_twin_overlay.png` — *only* twin primes (≤3000)
- `prime_roots_bridge_map.png` — conceptual network (roots ↔ bands ↔ thresholds)
- `Vendessimal Prime Grid (mod 19:29 class colors) 20-wide rows, 1…3000.png` — tall strip layout

### Parameters
- **Grid width**: 20 per row (vendessimal arrangement)
- **Residues**: `n % 19`, `n % 29` → index paired to a colormap
- **Twin radius**: `(p, p±2)` pairs; optionally restrict to both primes
- **Triad windows**: three ring bands in row- and column-space (π-linked)

> Tip: When iterating Euler-like quadratics (e.g., `n^2 + n + 41`), treat each octave as a *row block*; step the triads by ±(38, 39, 40) to examine resonance drifts (2×19, 3×13, 4×10).

— *Scarabäus1033 · QGR vendessimal kit*