# Octave Ladder — README (Spec v1.2)

This folder contains the 2^n shell scaffold used in the **Flavor + Membrane** validation.

## Files
- `octave_shrinking_ladder.csv` — ladder table with k=0..11, Δφ_k, f_k=(1/45)·2^k, and optional radius ratio R/R0=2^(k/3).
- `octave_dphi_sweep.png` — Δφ_k vs k.
- `freq_ratio_vs_k.png` — frequency ratio vs k (log scale).
- `ladder_polar_map.png` — polar scatter of gate angles θ=Δφ_k.

## Quick interpretation
- **Triplet cadence (k mod 3):**
  - Class **A (k≡0 mod 3)**: k={0,3,6,9}. Radius law hits exact powers 2^(k/3) ∈ {1, 2, 4, 8} → “anchor shells” (smooth radii).
  - Class **B (k≡1 mod 3)**: k={1,4,7,10}. Your eye caught these as “smooth” too: they ride one cube‑root up (≈×1.26, ×2.52, ×5.04, ×10.08), often looking regular in polar because Δφ_k lands near stable octants (16°, 128°, 304°, 272°).
  - Class **C (k≡2 mod 3)**: k={2,5,8,11}. These are the complementary cube‑root‑squared steps.

- **Pairing inside each triplet:** (k, k+1) behave like **clockwise/anticlockwise** companions once projected in polar (Δφ around/beyond 180°). The third (k+2) “resets” the local phase relation before the next triplet.

- **Frequency ladder:** `f_k = (1/45)·2^k` exposes neat terminal decimals at k={1,4,7,10} and their companions; you can re‑parameterize with `1/33` or `1/7` without changing the dyadic structure. That swap only rescales the **y‑axis** and may align with alternative normalizations (e.g., 33/7 cadence).

- **13th shell (k=12):** adding one more step gives a “leap” shell consistent with your **leap‑year / 13 gate** narrative. In our table we cap at 12 by design; k=12 would repeat mod‑360° but continue frequency ×2.

## Suggested next probes
1. **Base normalization sweep:** regenerate the ladder with `f0∈{1/45, 1/33, 1/7}` and compare fits (RMSE/AIC/BIC).
2. **Clockwise/anticlockwise split:** for each triplet, test a sign flip in the membrane term to emulate the observed handedness in Δφ_k.
3. **13th “flux gate”:** include k=12 in the phase grid and check closure vs your 13↔31 metric (429 constant context).

---

*Maintainer:* Scarabæus1033 • *Spec:* v1.2 • *Notes generated:* auto‑README
