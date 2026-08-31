# Validation scope

All evidence uses synthetic identity/responses. No human pilot or clinical calibration was performed.

The five native gates (standard, TAPS, PsychoPy QA, scripted simulation, sampler simulation) passed. `gate_report.json` retains commands and original outputs. Ten-trial diagnostic configurations cover all five bends and both target intervals with unchanged timing. `check_semantics.py` independently checks all100 materials,99 subject plans and six executions of the actual trial body. `native_visual.py` exercised ordinary human startup with synthetic identity, real initialization and visible stimuli; its limited interception avoids claiming actual participant recruitment or a real human data run.

`check_outputs.py` checks three actual native CSV files, and `check_frame_budget.py` explains the measured report-window timing from recorded frame estimates. Original failures and repairs remain in `initial_failures.md`. Source/generator/cue restrictions and no-pilot limits are in the reference audit and README.

The final flow image is built-in ImageGen round4 with the official branding script, accepted after parent actual visual review. Rounds1–3 remain preserved as rejected evidence. The final diagram explicitly shows independently enlarged crops, not full-screen layouts or physical scale.

The paired source-only web repository archives real ten-trial browser downloads, 200 actual production PNG HTTP checks, exact native scheduling/scoring parity, scoped TypeScript including all owned tests and the full research recorder fixture. No shared framework source changes were required.
