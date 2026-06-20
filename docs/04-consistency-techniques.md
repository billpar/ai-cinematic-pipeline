# 04 — Consistency Techniques

How to stop your characters, lighting, and spatial logic from drifting clip to clip.

## Technique 1 — Start/end frame chaining (most important)

This is how to get seamless continuity between consecutive clips.

**Process:**
1. Generate clip A.
2. Export the very last frame as a still image.
3. Upload that frame as the **start frame** of clip B.
4. The model interpolates forward from that exact frame — character position, lighting, and spatial relationships carry over.

**This solves:** characters appearing in the wrong position, lighting shifts between clips, spatial jumps between angles.

In most image-to-video tools this is the "image-to-video" or "first frame" mode — upload the exported last frame as the reference image, then generate the next clip from it.

This technique is especially effective across cliffhanger or cut-sensitive sequences, where even a one-frame discontinuity reads as a jump cut error.

## Technique 2 — Seed parity

Most generation tools use a seed value that controls how the model "thinks" about an image. Reusing the same seed with similar prompts keeps facial structure and scene geometry consistent across generations.

**How to use it:** note the seed of a successful generation. When generating a follow-up shot of the same character, reuse that seed. Works best combined with the same character reference image.

**Practical tip:** keep a running log of seed numbers per character and per scene — see [`templates/shot-list-template.csv`](../templates/shot-list-template.csv), which has a seed column.

## Technique 3 — Prompt anchoring (immutable vs. mutable)

Split every prompt into two layers.

**Immutable — never changes within a scene:**
- Character tag and reference image
- Setting tag and reference image
- Lighting style description
- Overall film style (grain, color treatment, genre tone)

**Mutable — changes every beat:**
- Camera angle and shot type
- Character action and movement
- Character expression
- Audio description

**Rule:** never describe an immutable element differently between two consecutive shots of the same scene. Inconsistent lighting description between shots is the most common cause of visible drift.

## Technique 4 — The visual bible

Before generating anything, lock all visual decisions:
- Character reference sheets
- Setting reference images
- Color palette per location (e.g. warm tones = Location A, cool tones = Location B)
- Prop reference images

Once locked, treat these as source plates. Do not regenerate them mid-production, even if you spot something you'd improve — regenerating breaks continuity with every shot already produced from the original.

---

Next: [`05-audio-post-production.md`](05-audio-post-production.md)
