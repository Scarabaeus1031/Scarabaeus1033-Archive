# Vendessimal Prime Toolkit — Extended Overlays

This drop adds:
- **Triad band parameters** (`centers`, `sigma`, `delta`, `mode`)
- **Twin‑Prime layer** (p & p+2 both prime)
- **√2 / √5 rail buckets** (diagonal families with slopes √2 and √5)
- **Euler‑41 trace** (values of n²+n+41 ≤ N)
- **1061–1064 prime‑threshold inset**

## Quickstart

```python
import vendessimal_prime_toolkit as vpt
vpt.plot_extended(N=3000, outpath="vendessimal_extended.png",
                  triad_cfg=dict(centers=(2.5,10,17.5), sigma=2.1, mode='gauss'),
                  rails_tau=0.55)
```

Artifacts generated now:
- `vendessimal_extended.png`
- `vendessimal_twin_layer.png`
- `prime_threshold_1061_1064.png`

Generated: 2025-11-01T13:20:53.865209Z
