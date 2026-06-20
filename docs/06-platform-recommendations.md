# 06 — Platform Recommendations & Common Mistakes

## Tool categories

This methodology is tool-agnostic by design — the techniques matter more than the specific app. That said, here's a working category breakdown so you know what to look for in each slot of the pipeline:

| Task | What to look for |
|---|---|
| Character assets | Photorealistic image model with strong multi-angle/turnaround consistency |
| Setting images | Photorealistic image model with strong environmental/spatial coherence |
| Video generation | Model supporting image-to-video (start frame) and multi-element reference binding |
| Voice generation | TTS model with expression/delivery tagging support |
| Audio post | DAW with stem separation capability |
| Title cards / text effects | A model that preserves text consistency from video input (most models do **not** preserve text consistency when generating titles from scratch — animate the title separately first, then feed it in as a video reference) |
| Image inpainting | Generative fill / inpainting tool for fixing specific regions of a reference plate |
| Video upscaling | Any upscaler that preserves detail without introducing new artifacts |

Tools in this space change fast — treat any specific product name as a snapshot, not a permanent recommendation, and re-check current options periodically.

## Common mistakes and fixes

| Problem | Cause | Fix |
|---|---|---|
| Character appears in wrong position | No start-frame chaining | Export last frame, use as start frame of the next clip |
| Character speaks randomly | Voice bound to element while native audio is on, in a silent scene | Remove stray speech in post with stem separation |
| Prop appears the wrong scale | Too many competing prompt instructions, scale lost | Reduce prompt complexity, rely on the reference image for scale |
| Character in the wrong pose | Narrative description instead of physical direction | State body position, facing direction, hand position explicitly |
| Lighting shifts between clips | Immutable elements described inconsistently | Lock the lighting description, reuse the same setting reference every time |
| Unwanted character appears in frame | Element attached in the UI but not needed for that beat | Only attach elements that actually appear in that specific beat |
| Model ignores half the prompt | Over-specification | One instruction per category — one camera note, one action, one lighting note |

---

Back to [`README.md`](../README.md)
