# Task Logic Audit

Written from Field, Hayes & Hess (1993), Methods pp176â€“179 and Experiment I, before task implementation. Primary full text: https://redwood.berkeley.edu/wp-content/uploads/2020/08/field-etal93.pdf . No unrelated task logic reused.

## 1. Paradigm Intent

Temporal two-alternative contour detection using orientation relationships among twelve Gabor elements embedded in256. Manipulate successive path bend magnitude15/30/45/60/75 degrees; measure accuracy and response RT by bend, retaining omissions. This is a pixel-defined behavioral adaptation, not a calibrated physical threshold or exact replication.

## 2. Block/Trial Workflow

Two blocks of50 trials (100 total), ten observations for each bendÃ—target interval cell. This reduced research protocol is an explicit adaptation to an authored100-pair stimulus bank, not the article's four250-trial blocks. Each pair is presented once. Built-in BlockUnit schedules immutable scalar item labels; a task-specific preplan pairs five bends,20 unique exemplars each, with exactly ten first/ten second targets. Within each bend, shuffle interval assignments using random.Random(overall_seed+numeric subject_id); then shuffle all labels with the same RNG before splitting blocks. The paired asset identity and interval factor must be assigned before run_trial. Web uses public PythonRandom for identical scheduling. No random factors in run_trial.

Trial: fixation500ms (+) â†’ interval_one1000ms (512Ã—512 Gabor array) â†’ gap1000ms (mean gray) â†’ interval_two1000ms (paired array) â†’ report up to4000ms (which image had the path?) â†’ intertrial300ms (mean gray). Only report captures F=first/J=second. Response terminates report. Omission advances at deadline. No outcome feedback or reward. Instructions and between-block rests wait for space. Timing is identical in diagnostic profiles; only item counts differ (all five bends and both target intervals retained).

## 3. Condition Semantics

Conditions bend_15, bend_30, bend_45, bend_60, bend_75 denote unsigned successive backbone turn magnitudes, with random sign and uniformÂ±10Â° perturbation. These are path curvature factors, not orientation-jitter thresholds. Twelve elements are centered on consecutive backbone segments. Every image has exactly one element per32Ã—32 cell. Both intervals in a pair share all positions and exactly the same orientation multiset; null orientation assignment is a random permutation across all256 positions. This strengthens density/global orientation control relative to independent original arrays. Both arrays change many orientations, preventing a lone changed element from marking the path. A finite bank does not prove absence of every possible visual shortcut; human pilot data are absent.

All participant text resides in config stimuli. Arrays are mathematically generated PNGs with retained geometry/orientation manifests, never imagegen or drawing placeholders. No path highlight or internal condition token is visible during trials.

## 4. Response and Scoring Rules

Config-defined F/J map to1/2. Correct iff valid chosen interval equals preplanned target interval. Timeout has choice=null. Omitted rows remain in total denominator; report accuracy_all=correct/total and accuracy_valid=correct/valid with denominators explicitly recorded. RT is only the report-stage software RT; it is not from first-array onset. No adaptive controller and no threshold fit.

## 5. Stimulus Layout Plan

512Ã—512 grayscale image centered at[0,0], native units pix; corresponding512 CSSpx web size. No superimposed text during either image or gap. Circular Gaussian sigma4px and cosine period8px; carrier normal is tangent+90Â°, so visible bars align with backbone. Contrast numerical amplitude0.95, mean grayscale128; no luminance/gamma claim. Generator constrains patch support to image bounds, enforces minimum interelement separation18px and no backbone self intersections. These constraints and paired position/orientation permutation are declared adaptations. Fixation24px; report/instructions SimHei24px, explicit newlines and wrapWidth1100, centered, window1280Ã—800. User must not resize during session; browser/native scale is uncalibrated and viewing distance uncontrolled. Render checks inspect actual screenshots and asset-level stats.

## 6. Trigger Plan

Mock behavioral markers: experiment1/99; fixation10; interval_one20; gap30; interval_two40; report50; first51; second52; omission59; intertrial60. StimUnit owns phase/response/timeout events and trial context; next_trial_id owns native identity. Markers are software events, not EEG hardware timing evidence.

## 7. Architecture Decisions (Auditability)

Simple mode-aware main, native BlockUnit and StimBank, thin run_trial. utils handles scalar plan encoding/decoding, exact preplanning, scoring and denominator-preserving summary. Asset generator is an offline reproducible scientific material tool, distinct from the mandatory imagegen task-flow plot. No controller, compatibility layer, custom display loop, or private framework APIs. Ordinary human branch will also be smoke checked independently of QA.

## 8. Inference Log

Source anchors: Methods p176 establishes two sequential1s images; pp176/179 and Fig5 establish512Â² pixels,256 elements in16Â² cells,12 path elements, sigma4, period8; Experiment I p179 establishes15/30/45/60/75Â° bends. Textp179 specifiesÂ±10Â° turn variation whereas Fig5 caption saysÂ±5Â°; use Methods textÂ±10Â° and disclose this disagreement. All fixation/gap/report/ITI timing, F/J/space mapping, two50-trial blocks, paired density/histogram control, no feedback, bounded placement, validation profiles, seed policy and Chinese copy are inferred adaptations. No physical visual-angle, photometric calibration, eye tracking, human pilot, normative or clinical validation is claimed. The bank samples a contour-integration manipulation and is not a psychometric threshold instrument.

Observation policy: prefixation is central; during each1s image observers may look naturally around the array (Field1993p179 expressly permits2â€“3 fixation shifts). No eye tracking or fixation-invalid key is used.

Independent material verification: paired mean grayscale differs at most0.002381/255 and pixel SD at most0.003238/255; no clipped pixels. A conservative local alignment graph (18–50px edges, both bars≤25°from chord) finds maximum null component11elements, so no12-element chain under this proxy. This proxy misses strongly bent accidental contours; it is not human validation or proof of zero shortcuts.
Post-build timing audit: actual missing-response close3.94878–4.05132s for nominal4s due to framebudget based on estimatedperiod. Native239/238-style budgets closeafter(nframes−1) intervals; exactrecorded settings and one-recorded-frame consistencycheck in native_frame_budget.json. No protocoltiming was changed. Native/web retain nominaldeadlines; measureddeadline equality is not claimed.
