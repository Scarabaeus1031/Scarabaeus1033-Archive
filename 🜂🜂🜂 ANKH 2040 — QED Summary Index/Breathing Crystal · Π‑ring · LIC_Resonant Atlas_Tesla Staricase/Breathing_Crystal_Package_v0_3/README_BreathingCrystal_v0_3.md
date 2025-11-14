# Breathing Crystal Package — Companion Files (v0.3)

This folder contains data, visuals, and scene-specs used in the **Breathing Crystal Mechanism** study.

## 📦 Contents

| File | Description |
|------|--------------|
| `triad_bands_windows.png` | Gaussian triad-band windows (~0.429, 0.456, 0.487) |
| `triad_bands_timeline.png` | 42‑s Tesla 3–6–9 blend timeline |
| `vendessimal_prime_grid.png` | 20‑wide residue grid (mod 19 × mod 29) |
| `prime_residue_legend_mod19_29.csv` | CSV of all prime residues mod 19/29 |
| `twin_primes_upto_3000.csv` | List of twin primes ≤ 3000 |
| `breathing_crystal_glb_spec_v0_3.json` | GLB‑scene JSON spec (π‑membranes, I‑AN core) |

## ⚙️ Parameters

| Symbol | Meaning | Default |
|---------|----------|----------|
| π₁ | Triad‑band 1 center | 0.429 |
| π₂ | Triad‑band 2 center | 0.456 |
| π₃ | Triad‑band 3 center | 0.487 |
| σ | Gaussian window width | 0.03 |
| T | Breath cycle | 42 s |

## 🧩 Usage Notes

- To regenerate data: run `triad_bands_param_app.py` (editable `centers`, σ, T`).
- Import `breathing_crystal_glb_spec_v0_3.json` into Blender / Three.js, load timeline CSV as animation data.
- For primes: open the PNG in any viewer; dark squares = non‑prime, colored = prime residue class.

## 🔍 Additional Visuals

- `vendessimal_prime_grid_twin_overlay.png` — only twin primes marked.
- `prime_threshold_inset_1061_1064.png` — zoom on the 1061–1064 band (“Prime Schwelle”).

© Scarabäus1031 — Research & Harmonic Systems 2025.
