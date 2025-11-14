# Vendessimal Prime Grid — Extended (Triad, Rails, Thresholds)

This pack implements the **Breathing Crystal Mechanism** on a 20‑wide vendessimal grid:
- **Residue colors** mod 19/29 (class index).
- **Triad overlay** (three harmonic bands) with Gaussian or hard windows.
- **Twin‑prime layer** (overlay only the (p, p+2) constellation).
- **√2 / √5 rails** (diagonal prime families with tolerance τ).
- **Euler‑41 trace**: points of *n² + n + 41* (until N).
- **Prime threshold inset 1061–1064**: marks 1061, 1063 (prime) and 1064 = 2³·7·19.

> **Breathing timeline** (defaults): 1 breath = 6 s. We treat 7→9→12→17 as ordered phases.
{
  "stages": [
    {
      "name": "7\u2011Gate (Heptagon seed)",
      "breaths": 7,
      "seconds": 42
    },
    {
      "name": "9\u2011Gate (Triadic bloom)",
      "breaths": 9,
      "seconds": 54
    },
    {
      "name": "12\u2011Gate (Harmonic ring)",
      "breaths": 12,
      "seconds": 72
    },
    {
      "name": "17\u2011Gate (Gauss\u2011Gauss bridge)",
      "breaths": 17,
      "seconds": 102
    }
  ],
  "note": "One full macro\u2011cycle = 7+9+12+17 = 45 breaths = 270 s."
}

## Quickstart

```bash
python3 vendessimal_prime_toolkit.py --N 3000 --out vendessimal_extended.png
```

Twin‑only poster:
```bash
python3 vendessimal_prime_toolkit.py --twin-only --out vendessimal_twin_layer.png
```

Mini‑spicker 1061–1064:
```bash
python3 vendessimal_prime_toolkit.py --threshold-inset --out prime_threshold_1061_1064.png
```

## Key Parameters

- `--mod-pair 19 29` : residue color classes (default 19/29).
- `--centers 3 10 17` : triad band centers on 20‑grid columns (≈ thirds).
- `--sigma 2.4` : Gaussian σ (column units). Use `--mode hard --delta 2.0` for box bands.
- `--rails-tau 0.55` : tolerance for √2/√5 diagonal rail buckets.
- `--twin-alpha 0.75` : alpha for twin‑prime overlay.
- `--timeline 7 9 12 17` and `--breath-sec 6` : breathing phase mapping for titles/exports.

> Defaults are tuned to **σ = 2.4**, centers **(3, 10, 17)**, rails **τ = 0.55**, breath **6 s**.

## File tree
```
prime_suite/
  vendessimal_prime_toolkit.py
  README_EXTENDED.md
  vendessimal_extended.png           # full overlay (if generated)
  vendessimal_twin_layer.png         # twin-only (if generated)
  prime_threshold_1061_1064.png      # mini-inset (if generated)
```
