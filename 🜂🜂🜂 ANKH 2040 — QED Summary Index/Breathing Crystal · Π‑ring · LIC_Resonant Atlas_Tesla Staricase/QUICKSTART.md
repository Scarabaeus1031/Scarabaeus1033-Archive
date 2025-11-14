# LANG-ALGO • Quick Ops

## Render vendessimal prime overlays
```bash
python -m lang_algo.viz --mode overlays --cfg config.yaml --out visuals/
```

## Synthesize LIC field from text
```bash
python -m lang_algo.synth \
  --input "LIC LOGIC LIGHT" \
  --cfg config.yaml \
  --phonemes phoneme_map.yaml \
  --out out/lic_field.wav
```

## Breathing Crystal sequence (7→9→12→17)
```bash
python -m lang_algo.breathe --cfg config.yaml --preview out/breathe_timeline.png
```

## Notes
- Vowels use η-band centers: [0.429, 0.456, 0.487].
- Consonants act as gates; adjust hardness/sustain in `phoneme_map.yaml`.
- Rails √5 / √2 route spectral energy; step factors ×63/×65/×68 handle macro-shifts.
