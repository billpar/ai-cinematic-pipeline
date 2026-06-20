# 02 — Character, Setting & Prop Asset Creation

Everything downstream depends on these assets being locked *before* you generate a single video clip. Treat this stage as building your "visual bible."

## Character reference sheets

Use a photorealistic image model capable of consistent multi-angle output. Build a **7-panel turnaround**:

**Top row — 4 panels, full body:**
- Front view (0°)
- Right side profile (90°)
- Left side profile (-90°)
- Back view (180°)

**Bottom row — 3 panels, head close-ups:**
- 3/4 portrait, slight left
- Front-facing portrait
- 3/4 portrait, slight right

**Rules:**
- Neutral grey background, every panel
- Identical lighting across all 7 panels
- Zero variation in clothing, hair, skin tone, or proportions between panels
- For background/anonymous characters: use a face covering (mask, goggles, helmet) — this sidesteps face-consistency problems entirely
- Lock the character's text description and reuse it **verbatim** in every single prompt for the rest of production

**Generic structure for a locked character anchor:**
```
[Character Name] — [skin tone], [hair description], [eye color],
[distinguishing marks], [hand/accessory details], [clothing top layer],
[clothing bottom layer], [footwear]. Default expression: [physical
micro-detail, not an emotion word].
```

Reuse this string exactly, every time, for every shot featuring this character.

## Setting reference images

Generate in **16:9 wide format** — it gives the video model more spatial information to work from than square or vertical crops.

**Rules:**
- Asymmetric composition (e.g. heavier object/structure on one side, open space on the other) — avoid dead-center symmetry
- At least one visible light source in frame — this locks the lighting logic for every subsequent shot in that location
- Avoid heavy fog or haze — it hides spatial information the model needs
- Slightly reduce contrast before feeding it into the video model — acts like a pseudo-LOG image, giving the model more dynamic range to work with
- Always include: floor texture, wall texture, a light source, and visible depth

**Generic structure for a setting key-elements list:**
```
[Lighting type and color temperature], [main central object/furniture
and its condition], [one structural detail — door, wall feature,
window], [surface/texture description], [overall mood detail —
ceiling height, openness, enclosure].
```

## Prop assets

For any object appearing in more than one shot, generate a standalone photorealistic reference image and give it a clear scale description so the model doesn't lose proportion.

**Generic structure:**
```
[Object type], [shape], approximately the size of [a familiar
reference object] — [hand-held / tabletop / room-sized, as
applicable]. [Material and wear condition], [distinguishing
surface details].
```

## Once locked, don't touch them

The single biggest cause of visual drift across an episode is regenerating "improved" versions of a character or setting mid-production. Lock these assets early and treat them as source plates for the rest of the shoot.

---

Next: [`03-prompt-writing-guide.md`](03-prompt-writing-guide.md)
