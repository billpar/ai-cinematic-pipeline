# 01 — Pipeline Overview

The full workflow, in order. Each stage is detailed in its own doc.

## 1. Script breakdown
Read the script once for story, then again purely as a director: list every character, every setting, every prop that recurs across more than one shot. This list becomes your asset list.

## 2. Character assets
Build a locked 7-panel turnaround reference sheet per character (front, two profiles, back, three head angles). See [`02-character-asset-creation.md`](02-character-asset-creation.md).

## 3. Setting assets
Wide reference images per location, generated with enough spatial and lighting information that the video model doesn't have to guess. See [`02-character-asset-creation.md`](02-character-asset-creation.md) (covers settings and props too).

## 4. Prop assets
Any object appearing in more than one shot gets its own standalone reference image with a clear scale description.

## 5. Voice assets
One voice profile per speaking character, generated ahead of time so dialogue scenes stay consistent.

## 6. Shot planning
Break every scene into beats of roughly 2–3 seconds. One beat is the smallest unit the video model should be asked to generate in a single pass. Use [`templates/shot-list-template.csv`](../templates/shot-list-template.csv).

## 7. Prompt writing
One beat = one prompt. Every prompt separates immutable elements (character, setting, lighting style) from mutable ones (camera, action, expression). Full structure in [`03-prompt-writing-guide.md`](03-prompt-writing-guide.md).

## 8. Generation
Run the prompt through your video model with the correct reference elements attached — only the elements that actually appear in that beat.

## 9. Frame chaining
Export the last frame of each generated clip and feed it back in as the start frame of the next. This is the single highest-leverage technique for visual continuity. See [`04-consistency-techniques.md`](04-consistency-techniques.md).

## 10. Audio post
Separate tracks: dialogue, voiceover, sound effects, music, foley. See [`05-audio-post-production.md`](05-audio-post-production.md).

## 11. Edit
Assemble clips in order, sync audio, color grade, add captions, export.

---

Next: [`02-character-asset-creation.md`](02-character-asset-creation.md)
