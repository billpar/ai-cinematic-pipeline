# Shot Preset Library

A set of named, reusable camera and blocking presets. Instead of writing camera direction from scratch for every beat, pick a preset, plug in your character and setting tags, and adjust only what's different about that specific shot.

This is genre-flexible — the presets below lean toward dramatic/tension-driven scenes since that's a common use case, but the structure applies to any narrative genre. Add your own presets at the bottom as you find combinations that work well with your specific tools.

## How to use a preset

Each preset gives you the **camera block** pre-written. You still fill in:
- Character tag(s) and their physical action
- Expression (physical, not emotional — see [`docs/03-prompt-writing-guide.md`](../docs/03-prompt-writing-guide.md))
- Setting tag
- Dialogue/audio, if any

---

## 1. Intimate Close-Up

**Use for:** quiet emotional beats, internal moments, confessions, eye contact.

```
Close-up shot, 85mm, f/1.8.
Slow push-in, shallow depth of field, background softly out of focus.
```

---

## 2. Power Dynamic

**Use for:** establishing dominance, intimidation, status imbalance between two characters.

```
Low angle shot, 35mm, f/2.8.
Slight upward tilt, subtle camera drift, character framed to appear
larger in frame relative to the other.
```

---

## 3. Tension Static

**Use for:** standoffs, held silences, moments where stillness carries the weight.

```
Locked-off medium shot, 50mm, f/2.0.
Camera completely static, no movement of any kind.
```

---

## 4. Emotional Break

**Use for:** a character's composure cracking, a sudden shift in emotional state.

```
Medium close-up, 50mm, f/2.0.
Handheld feel, very slight natural camera jitter, no deliberate movement.
```

---

## 5. Distance Wide

**Use for:** isolation, loneliness, a character dwarfed by their environment.

```
Wide shot, 24mm, f/4.
Static or very slow drift, character small in frame, generous negative
space around them.
```

---

## 6. Establishing Wide

**Use for:** opening a scene, introducing a new location.

```
Wide establishing shot, 24-35mm, f/4-5.6.
Static or slow lateral drift across the space.
```

---

## 7. Tracking Follow

**Use for:** a character moving through a space with purpose — walking, searching, approaching.

```
Medium shot, 35mm, f/2.8.
Camera tracks alongside or slightly behind the character at a
matched pace.
```

---

## 8. Reveal Pull-Back

**Use for:** revealing new information in frame — a second character, an object, a changed environment.

```
Starts close, 50mm, f/2.0.
Slow pull-back to wider framing, revealing additional context as the
shot progresses.
```

---

## 9. Over-the-Shoulder Dialogue

**Use for:** standard two-character conversation coverage.

```
Medium shot, 50mm, f/2.2.
Camera positioned just behind one character's shoulder, other
character in clear focus facing camera.
```

---

## 10. Macro Detail

**Use for:** insert shots — hands, objects, small but narratively important details.

```
Macro/close-up shot, 100mm, f/2.8.
Static, extremely shallow depth of field, subject sharply isolated
from background.
```

---

## Combining presets into a scene

A scene is usually built from 3-5 shots in sequence. Example structure for a two-character dialogue scene:

1. **Establishing Wide** — set the location
2. **Over-the-Shoulder Dialogue** — main coverage
3. **Intimate Close-Up** — on the emotional turn of the scene
4. **Macro Detail** — insert on a relevant object or gesture, if useful
5. **Tension Static** or **Emotional Break** — for the scene's final beat

## Add your own presets

| Name | Use case | Camera block |
|---|---|---|
| | | |
| | | |

---

See [`prompt-template.md`](prompt-template.md) for how to plug a preset's camera block into a full beat prompt.
