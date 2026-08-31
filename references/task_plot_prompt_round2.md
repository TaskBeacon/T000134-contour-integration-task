Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean scientific task-flow timeline, landscape1800×1000. Use the supplied grayscale Gabor images as actual visual appearance references in image snapshots. The first supplied image is SIGNAL and second is NULL; they are reference assets, not a canvas to edit.

Task: Contour Integration Task
Construct: contour integration
Rows/conditions:
- Path first: first image contains the path, second image is the null.
- Path second: first image is null, second image contains the path.

Timeline phases:
- Path first: Fixation (500 ms; no response; gray screen with black+) -> First image (1000 ms; no response; SIGNAL reference array) -> Gap (1000 ms; no response; blank gray) -> Second image (1000 ms; no response; NULL reference array) -> Report (4000 ms max; response ends screen; gray screen with Chinese question 哪一幅包含连续的弯曲路径？) -> Intertrial (300 ms; blank gray).
- Path second: Fixation (500 ms; no response; gray screen with black+) -> First image (1000 ms; no response; NULL reference array) -> Gap (1000 ms; no response; blank gray) -> Second image (1000 ms; no response; SIGNAL reference array) -> Report (4000 ms max; response ends screen; gray screen with Chinese question 哪一幅包含连续的弯曲路径？) -> Intertrial (300 ms; blank gray).

Visual requirements:
- White background, crisp dark readable text, restrained blue/teal row accent; one horizontal row per representative trial type.
- Exactly six participant-screen snapshots perrow, connected by thin arrows; consistent gray screen boxes and subtle row separators. Timing below each screen, short phase label above.
- Arrays must show dense small sinusoidal Gabor patches at many orientations as in the supplied references. Do not turn patches into dots or plain line dashes. Signal and null arrays have identical positions and density, not different element counts. No drawn path lines, arrows pointing to the target, colored patches, enlarged elements, or path outlines inside any screen.
- Put row labels atleft. Chinese report text may wrap into3short lines within its screen; preserve every Chinese character exactly.
- Leave the entire top18%blank white for the later fixed title/subtitle/logo. Do not draw any title, subtitle, watermark, logo or TaskBeacon text yourself.
- Below rows, place the concise explanatory notes: Bend:15° /30° /45° /60° /75°; F=first • J=second; 2 blocks×50trials; No feedback. These notes are outside participant screens.
- Collapse equivalent bend conditions into these two representative rows. All six timings and both interval orders must be unambiguous. Large enough text for normal document viewing; avoid cramped labels.

Accuracy constraints:
- No invented phases, stimuli, keys, rewards, timings, equipment, people or decoration.
- Preserve exact short terms: Path first, Path second, Fixation, First image, Gap, Second image, Report, Intertrial, 500 ms,1000 ms,4000 ms max,300 ms.
- Only draw timeline content below the blankheaderband.

Style: TaskBeacon scientific infographic, gray participant screens, restrained accents, subtle arrows, clean raster layout, generous spacing.

Round2 targeted revision (supersedes previous six-square-screen layout only):
- Correct screen geometry. Each actual participant screen is landscape16:10,1280×800. Image array is a CENTERED SQUARE512×512, exactly40%screen width and64%screen height, surrounded by gray margins. NEVER fill the whole screen with the array.
- For legibility use exactly THREE larger16:10participant-screen snapshots perrow: First image, Second image, Report. Two representative rows remain Path first/Path second. Merge minor phases into clear timeline annotations (not fake screen snapshots): BEFORE first image show “Fixation+500 ms”; arrow fromfirst tosecond labeled “Gray gap1000 ms”; AFTER report show “Gray intertrial300 ms”. First/second snapshots each1000ms; Report4000ms max.
- In each Report snapshot, the exact Chinesequestion “哪一幅包含连续的弯曲路径？” is a SINGLE centered line, as in actual1280×800native screen. It occupies about26%ofscreen width; no enlarged/wrapped three-line question. EnglishReportlabeloutside is large andreadable.
- Make the three screen snapshots large, e.g.each480×300within a2048-widecanvas. Center Gabor arrays about192×192inside the480×300frames. Keep all screenboxes the SAME16:10shape and gray background. Two rows plusfooter and blanktop18%header.
- Preserve both intervalorders, signal/null reference appearance and all timing/key/bend/count/no-feedbacknotes. No colored or enlarged target elements, no pathoutline, no internal labels in the arrays. Only explanatorylabelsoutside actualscreens.
