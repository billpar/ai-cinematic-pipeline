# 03 — Prompt Writing Guide

## The director mindset — the most important rule in this whole repo

When reading a script for AI generation, ignore the narrative prose. The script tells you what the story *means*. Your job is to translate that into physical reality — where bodies are, what hands are doing, what the camera sees.

**Wrong (narrative):**
> The character realizes someone has been watching them and feels confident because they already knew.

**Right (director):**
> Character A sits facing away from the door. Hands continue a small repetitive task. They do not turn around. Expression: unhurried, faintly amused.

## Translating script language into physical direction

Scripts use figurative language. Convert it:

| Script says | Translate to |
|---|---|
| "something shifts underneath it" | subtle change in eye focus, jaw slightly less tight |
| "the ghost of something not quite a smile" | one corner of mouth moves 2mm upward, eyes unchanged |
| "shoulders drop one half-inch" | keep verbatim — it's already physical |

## Facial expression system — micro-muscle control

Never describe emotions directly. Describe the physical state that produces them.

| Emotion (don't write this) | Physical direction (write this) |
|---|---|
| faintly amused | right corner of mouth lifts slightly, eyes unchanged |
| suspicious | lower eyelids tighten subtly, blink rate reduced |
| calculating | eyes move slightly left then back, jaw still |
| shock | all facial movement stops completely for one beat |
| controlled anger | jaw tightens, lips press together, no movement elsewhere |

The more specific the physical instruction, the more psychological realism the model produces.

## Negative space direction

Describe stillness explicitly — it's a directorial tool, not a default state.

**Wrong:** `Character stands still.`

**Right:** `Character stands completely still — no hand movement, no blinking, no shift in weight, no reaction.`

Video models generally respect constraints. Absence of movement creates tension equal to movement itself.

## Voiceover vs. spoken dialogue

This distinction matters for what goes in the prompt vs. what's added in post:

- `CHARACTER (VOICEOVER):` → **do not** put in the generation prompt. Add separately in post-production via your voice tool.
- `CHARACTER:` (no voiceover tag) → put in the prompt as spoken dialogue, generated with the clip.

## Spatial blocking for multi-character shots

Before writing a prompt with 2+ characters in frame, lock their physical positions first. Models will hallucinate spatial relationships unless they're declared in absolute terms.

**Always declare:**
- Where each character stands relative to the other (distance in meters)
- Which direction each is facing
- Who occludes whom
- Where key props sit relative to characters
- Camera position relative to the scene

**Wrong:** `Character A and Character B stand facing each other in the room.`

**Right:** `Character A stands 2 meters from the central object, facing the entrance. Character B stands on the far side of the object, 3 meters from Character A, facing them — object partially occludes their lower body. Camera at eye height, positioned behind Character A's left shoulder.`

## Camera coverage pattern

For a typical dialogue or reveal beat:
1. Establish or hold on character face
2. Pull back slightly to show context
3. Cutaway to environmental detail
4. Return to character face

## Quick-reference checklist

Before generating each beat, confirm:

- [ ] Timestamp format correct, e.g. `[00:00 - 00:02]`
- [ ] Shot type stated first, with lens (e.g. 85mm/50mm/35mm) and aperture
- [ ] Camera behavior matches the character's emotional beat
- [ ] Element tag used every time that element performs an action
- [ ] Character position stated: sitting/standing, facing direction, distance from others
- [ ] Expression described physically (micro-muscle), never emotionally
- [ ] Dialogue written as `Character says, "text"` with pre/during/post-line beats noted
- [ ] No voiceover lines inside the prompt
- [ ] Audio/ambience line included
- [ ] Setting tag included
- [ ] Only the elements that actually appear in this beat are attached
- [ ] No negative prompts
- [ ] No aspect ratio text inside the prompt
- [ ] Spatial blocking declared for any multi-character shot

See [`templates/prompt-template.md`](../templates/prompt-template.md) for a fill-in-the-blanks version of this structure.

---

Next: [`04-consistency-techniques.md`](04-consistency-techniques.md)
