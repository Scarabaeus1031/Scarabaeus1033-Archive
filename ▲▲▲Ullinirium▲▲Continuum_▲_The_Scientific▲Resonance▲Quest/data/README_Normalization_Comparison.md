# Normalization Comparison — Octave Ladder (1/45 vs 1/33 vs 1/7)

This note helps compare the three base frequency normalizations used in the **2^n shell ladder**.

## 0) Artefacts

**Baseline (f0 = 1/45)**
- CSV: `octave_shrinking_ladder.csv`
- Plots: `octave_dphi_sweep.png`, `freq_ratio_vs_k.png`, `ladder_polar_map.png`

**Alt A (f0 = 1/33)**
- CSV: `octave_shrinking_ladder_f0_33.csv`
- Plots: `octave_dphi_sweep_f0_33.png`, `freq_ratio_vs_k_f0_33.png`, `ladder_polar_map_f0_33.png`

**Alt B (f0 = 1/7)**
- CSV: `octave_shrinking_ladder_f0_7.csv`
- Plots: `octave_dphi_sweep_f0_7.png`, `freq_ratio_vs_k_f0_7.png`, `ladder_polar_map_f0_7.png`

## 1) Metric Definitions

- **RMSE** — root mean square error vs. chosen reference (e.g., planetary g residuals, phase-lock target angles).
- **AIC** — Akaike Information Criterion for model selection on the same target set.
- **BIC** — Bayesian Information Criterion for the same fit.

> *Important:* Use the *same targets* (and identical data splits) across all three normalizations.

## 2) Results Table (fill-in)

| Normalization | RMSE (↓) | AIC (↓) | BIC (↓) | Notes |
|---|---:|---:|---:|---|
| f0 = 1/45 | — | — | — | baseline (Spec v1.2) |
| f0 = 1/33 | — | — | — | 33-cadence; check #1/#4/#7/#10 smoothness |
| f0 = 1/7  | — | — | — | 7-cadence; check pair symmetry + terminals |

## 3) Visual Cues

- **Polar pairing:** verify “clockwise/anticlockwise” within each triplet (k,k+1,k+2).
- **Smooth shells:** check k={1,4,7,10} in each normalization for visual regularity.
- **Terminal decimals:** inspect `freq_ratio` columns (end digits and repeating patterns).

## 4) Decision Notes

- Pick the normalization that minimizes (RMSE, AIC, BIC) **and** preserves the intended symbolic constraints:
  - triplet cadence (k mod 3),
  - 13th leap shell behavior (k=12),
  - visual stability of #1/#4/#7/#10.
- Record the rationale here:

> **Chosen f0:** …  
> **Why:** …

---
Maintainer: Scarabæus1033 · Template v1.0
