# 05 — Audio Post-Production

## Track layout

Separate audio into distinct tracks in your DAW:

1. **Dialogue** — spoken lines generated natively by the video model
2. **Voiceover** — internal monologue / narration, generated separately
3. **Sound effects** — ambient and action sounds, native or added
4. **Music** — composed or licensed, added in post
5. **Foley** — hand-crafted sound detail layered on top

## Removing unwanted native audio

AI video models with native audio generation will sometimes produce dialogue, music, or speech you didn't ask for — especially in silent scenes where a character's voice profile is still bound to an active element.

Use a stem-separation tool (e.g. iZotope RX's Music Rebalance module, or equivalent) to isolate and remove unwanted music or speech without damaging the rest of the mix.

**Voice element rules to prevent this at the source:**
- Once a voice profile is bound to a character element, it stays active whenever native audio generation is on
- For scenes with no dialogue, the bound voice can still trigger speech randomly
- Fix: bind voice profiles only when you're actively generating a dialogue scene; for silent scenes, let the model generate ambient sound effects naturally and clean up any stray speech afterward

## Voice expression tagging

If your voice tool supports expression tags, use bracketed tags inline to control delivery:

```
[quiet internal monologue, completely calm]Footsteps outside the door.
[slight pause]Been there eleven minutes.
[dry, almost amused]Thinks I don't know.
```

Common useful tags: dramatic, quiet, calm, tense, dry, amused, cold, intense, soft, matter-of-fact, with pause, taking time. Available tags vary by tool — check your provider's documentation for the current list.

## Sound design principle

Less is more, especially for slower or dialogue-driven scenes: ambient hum + precise, intentional sound effects + genuine silence. Music should be additive, not constant underneath everything. The silence between sounds carries as much narrative weight as the sounds themselves.

---

Next: [`06-platform-recommendations.md`](06-platform-recommendations.md)
