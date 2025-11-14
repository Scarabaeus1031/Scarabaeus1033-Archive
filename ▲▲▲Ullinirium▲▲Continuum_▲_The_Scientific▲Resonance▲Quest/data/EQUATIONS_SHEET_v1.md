# EQUATIONS_SHEET_v1 — NEXAH · Scientific Verification Starter

This sheet collects *testable* formulas and the **exact procedures** we will use to evaluate them against public data (JPL/NASA/USGS etc.).

---

## 0. Units & Constants (reference)

- 1 AU = 149,597,870.700 km (IAU 2012, exact)
- 1 ly ≈ 9,460,730,472,580.801 km
- 1 mile = 1.609344 km (international mile)
- Royal cubit (canonical) ≈ 0.5235 m (historical range ~0.523–0.525 m)

A full conversion table is provided in `units_reference_table.csv`.

---

## 1. Gravity Shell Model (g_n)

**Model form:**  
\[ g(n; \theta, \varphi, \phi) = g_c \cdot n^{-\phi} \cdot \cos(n\,\theta + \varphi) \]

- Baseline: \( g_c = 9.81\,\mathrm{m/s^2} \)
- Parameters to fit from data: \(\theta\) (deg), phase \(\varphi\) (deg), exponent \(\phi\) (dimensionless)
- Prior from scans (Titan “Grey Elevator”):  
  • Local extremum near **n ≈ 1.099–1.100** at **θ ≈ 106°**, **phase ≈ 25°**.  
  • See: `theta_phase_grid_scan_extremum.csv`, `gn_curve_best_extremum_near_1p1.png`.

**Test protocol:**
1. Select planetary sample with measured surface gravity.  
2. Fit (θ, phase, φ) by minimizing RMSE between model and observed g under integer / quasi-integer shell indices n.  
3. Report RMSE, MAE, R²; plot residuals; leave-one-out validation.  
4. **Pass:** beats constant baseline and simple radius power-law.

Artifacts: `planetary_gravity_codex_mapping.csv` (present), residual charts.

---

## 2. Lunar Elemental–Albedo Relation

**Data:** `lunar_elemental_panel.csv` (+ `_extended.csv`) with: name, elemental_axis ∈ [0,1], albedo ∈ [0,1].

**Null:** linear fit y = a + b x  
**Alt:** logistic or monotone spline y = σ(a + b x + c x²)  
**Diagnostics:** R², Spearman ρ, Cook’s distance.  
**Pass:** AIC/BIC improvement and stability under 1-out cross-val.

Charts: scatter + fit band; residual vs fitted.

---

## 3. Phase Scan (θ, phase) Reproducibility

**Input:** `theta_phase_grid_scan_extremum.csv`, `theta_phase_grid_distance_heatmap.png`  
**Procedure:** grid search, cubic interp for extremum; perturb sampling.  
**Pass:** optimum stable within ±1° (θ) and ±2° (phase).

---

## 4. Stellar Cross Consistency

Validate spherical intersection of axes using RA/Dec (J2000) for key stars (Sirius, Vega, Orion region, etc.).  
**Pass:** bearings reproduce the designed cross within ±0.5°.

---

## 5. Provenance & Reproducibility

Sources: JPL Horizons/SBDB, NASA PDS, USGS Astrogeology, SIMBAD/VizieR (placeholders).  
Freeze scripts, seeds; export all intermediate CSVs in `/data/` with README.

---

### Deliverables checklist
- [x] `units_reference_table.csv`  
- [ ] Planetary gravity residuals  
- [ ] Lunar elemental–albedo fits  
- [ ] Phase-scan top-3 parameter sets  
- [ ] `EQUATIONS_SHEET_v1.md` (this file) + gallery links
