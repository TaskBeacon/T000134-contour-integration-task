# Parameter Mapping
## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| array | stimuli.* | 512×512 pixels | field1993 | Methods p176 | direct | No visual-angle calibration |
| gabors | assets/manifest.json | 256 elements; sigma4; period8; amplitude.95 | field1993 | Methods pp176/179, Fig5 | direct | No photometric contrast claim |
| path | task.conditions | 12 elements, bends15/30/45/60/75° | field1993 | ExptI p179 | direct | Geometric angles, not visual angles |
| perturbation | scripts/generate_assets.py | ±10° bend perturbation | field1993 | Methods p179 vs Fig5±5 discrepancy | direct | Explicit conflict resolved in favor of body text |
| interval | timing.array_duration | 1s each | field1993 | Methods p176 | direct | Natural gaze shifts allowed |
| gap | timing.gap_duration | 1s | field1993 | p176 short-duration condition | adapted | Used for full1s condition here |
| other timing | timing | .5s fixation,4s report,.3s ITI | field1993 | No matching original parameters | inferred | No feedback |
| counts | task.total_trials | 100unique pairs,2×50 | field1993 | Original4×250 | adapted | Accuracy only, no threshold fit |
| control | assets/manifest.json | paired positions and orientation histogram | field1993 | Density control pp176/179 | adapted | Null is global permutation; original used random arrays |
| response | task.report_keys | F first/J second | field1993 | Original mouse2AFC | adapted | Omission retained |
| packing | scripts/generate_assets.py | min18px, bounded patches, no path crossings | field1993 | Separation/grid principle | adapted | Finite authored bank not human piloted |
