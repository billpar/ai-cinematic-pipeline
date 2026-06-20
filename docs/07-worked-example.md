# 07 — Worked Example (Start to Finish)

Every other doc in this repo explains one piece of the pipeline on its own. This doc walks through **one small scene, start to finish** — so you can see how the pieces connect in practice.

We'll use a short, generic scene: a character enters a room and has a brief, tense exchange with someone already there.

---

## Step 1 — Raw scene idea

Before anything else, here's the scene in plain narrative form, the way you might first write it:

> A character walks into a dimly lit room. Someone is already there, waiting, and doesn't seem surprised to see them. A short, loaded exchange follows.

This is a starting point, not something you'd ever put into a prompt directly — too vague, too narrative.

---

## Step 2 — Break it into a beat sheet

Following [`01-pipeline-overview.md`](01-pipeline-overview.md), we convert the scene into a structured input file (the same format used by [`scripts/shot_list_generator.py`](../scripts/shot_list_generator.py)):

```
SCENE: 1
SETTING: Dim interior room
LIGHTING: Single overhead light, heavy shadow

BEAT: Wide shot of the empty room before anyone enters.
BEAT: Character A opens the door and steps inside, scanning the room.
BEAT: Character B is already seated, watching the door, unmoving.
BEAT: Character A says, "I didn't expect you to be here already."
BEAT: Character B says, "I know."
```

Notice each beat is a small, physical unit — not a paragraph of narrative description.

---

## Step 3 — Run the shot list generator

Following the steps in [`scripts/HOW_TO_USE.md`](../scripts/HOW_TO_USE.md):

```
python3 shot_list_generator.py my_scene.txt my_shotlist.csv
```

This produces a scaffolded CSV with `scene`, `setting`, `immutable_lighting`, `action`, and `dialogue` already filled in for each beat — see [`templates/shot-list-template.csv`](../templates/shot-list-template.csv) for the column structure.

---

## Step 4 — Fill in the remaining columns by hand

The generator can't decide your camera language or expressions for you — that's the creative part. Using [`templates/shot-preset-library.md`](../templates/shot-preset-library.md), we assign a preset to each beat:

| Beat | Preset used | Why |
|---|---|---|
| 1 (empty room) | Establishing Wide | Sets the location before anyone enters |
| 2 (A enters) | Tracking Follow | Follows A's movement into the space |
| 3 (B already seated) | Tension Static | Stillness signals B was waiting |
| 4 (A's line) | Over-the-Shoulder Dialogue | Standard two-character coverage |
| 5 (B's line) | Intimate Close-Up | The short reply lands harder in close-up |

---

## Step 5 — Write the full prompts

Using [`templates/prompt-template.md`](../templates/prompt-template.md) and the rules in [`docs/03-prompt-writing-guide.md`](03-prompt-writing-guide.md), here are two of the five beats fully written out:

**Beat 3 — Tension Static:**
```
[00:04 - 00:06]

Locked-off medium shot, 50mm, f/2.0.
Camera completely static, no movement of any kind.

@Character_B sits facing the door, hands resting still in their lap.
No blinking, no shift in weight, no reaction as the door opens.
Expression: jaw relaxed, eyes fixed on the doorway.

Audio: faint ambient room tone, no music.

@Dim_interior_room
```

**Beat 5 — Intimate Close-Up:**
```
[00:09 - 00:11]

Close-up shot, 85mm, f/1.8.
Slow push-in, shallow depth of field.

@Character_B says, "I know." Beat before: stillness, no warning shift.
Beat after: faint, controlled exhale, expression otherwise unchanged.
Expression: right corner of mouth lifts slightly, eyes unchanged.

Audio: the line itself, quiet, no ambient swell underneath.

@Dim_interior_room
```

---

## Step 6 — Generation and continuity

Following [`docs/04-consistency-techniques.md`](04-consistency-techniques.md), beat 4 and beat 5 happen in the same physical moment — so the last frame of beat 4's generated clip would be exported and used as the start frame for beat 5, keeping Character B's position and the room's lighting fully consistent between the two shots.

---

## Step 7 — Audio post

Per [`docs/05-audio-post-production.md`](05-audio-post-production.md), the two dialogue lines stay on a separate dialogue track from the ambient room tone, with no music layered underneath — consistent with the "less is more" principle for tense, quiet scenes.

---

## The point of this example

Five beats, five presets, two fully written prompts, one continuity link between them. That's the entire loop — every doc in this repo is a deeper dive into one piece of what you just saw end to end here.

---

Back to [`README.md`](../README.md)
