# Planetary g — Flavor+Membrane Validation — Run A (Default Priors)

**Phi-flavors (Greek Φ index ~21):** {1:1.38, 2:1.45, 3:1.52, 4:1.59, 5:1.618}
**Theta prior:** bimodal at 51°/53°, gate allowed at 106° (Grey Elevator)
**Membrane:** double-circle product; Δ_membrane ∈ [0°, 7°]

## Inputs
- g_obs: standard planetary surface gravities
- n_p windows: [k-0.2, k+0.2] for k=1..8 (heliocentric order)
- flavor map: planet_moon_flavor_assignment.csv (planets used; moons reserved for transfer test)
- priors: phi_set as above; Theta prior; Δ_membrane prior

## Optimize
- Variables: {phi_1..phi_5, Theta, Phi0, Δ_membrane, {n_p}}
- Loss: RMSE + λ_Theta * min((Θ-51)^2,(Θ-53)^2,(Θ-106)^2) + λ_mem * (Δ_membrane/7)^2

## Baselines
- mean model; r^-2 powerlaw; single-cos no-membrane

## Outputs
- gravity_fit_flavormix_summary.csv
- planet_flavor_assignment.csv (this file)
- gravity_fit_vs_obs_flavormix.png
- gravity_residuals_flavormix.png
