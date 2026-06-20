![Cover](assets/cover.png)
# AI Cinematic Pipeline

> A production-tested methodology and template kit for making narrative short films and episodic series entirely with AI generation tools.

This repo documents a real end-to-end pipeline — script → character/setting assets → shot-by-shot prompts → video generation → consistency techniques → audio post — built from actual solo production work, not theory. It's tool-agnostic where it can be, and names specific tools where they matter.

If you're trying to make something that looks *directed*, not just generated, this is for you.

## Why this exists

Most AI video guides stop at "type a prompt, get a clip." That's not filmmaking — it's slot machine generation. This pipeline treats every shot like a director would: physical blocking, locked visual continuity, micro-expression control, and frame-to-frame chaining so consecutive clips don't visually drift.

## What's inside

| Folder | Contents |
|---|---|
| [`docs/`](docs) | The full written methodology, split by production stage |
| [`templates/`](templates) | Reusable templates: character sheets, shot lists, prompt structure |
| [`scripts/`](scripts) | A small Python tool to turn a script breakdown into a structured shot list |

## Pipeline at a glance

1. **Script breakdown** — identify every character, setting, and prop
2. **Character assets** — locked 7-panel turnaround reference sheets
3. **Setting assets** — wide reference images per location
4. **Prop assets** — standalone references for recurring objects
5. **Voice assets** — one voice profile per character
6. **Shot planning** — break scenes into 2–3 second beats
7. **Prompt writing** — one beat = one prompt, immutable vs mutable elements
8. **Generation** — video model with correct element/reference tagging
9. **Frame chaining** — last frame of clip A becomes start frame of clip B
10. **Audio post** — dialogue, voiceover, SFX, music, foley as separate tracks
11. **Edit** — assemble, color grade, caption

Full detail for each stage lives in [`docs/`](docs).

## Quick start

1. Read [`docs/01-pipeline-overview.md`](docs/01-pipeline-overview.md) for the full picture.
2. Copy [`templates/shot-list-template.csv`](templates/shot-list-template.csv) and break your script into beats.
3. Use [`scripts/shot_list_generator.py`](scripts/shot_list_generator.py) to scaffold the shot list automatically from a simple script file.
4. Follow [`docs/03-prompt-writing-guide.md`](docs/03-prompt-writing-guide.md) for prompt structure per beat.
5. Apply [`docs/04-consistency-techniques.md`](docs/04-consistency-techniques.md) — especially start/end frame chaining — to avoid drift between clips.

## Philosophy

- **Direct, don't describe.** Physical blocking beats narrative prose every time. "Right corner of mouth lifts slightly, eyes unchanged" generates better than "faintly amused."
- **Lock your visual bible before generating anything.** Character sheets, setting plates, and color palette per location should never be regenerated mid-production.
- **Stillness is direction too.** Explicitly describing non-movement creates as much tension as movement.
- **Less is more in audio.** Ambient hum + precise SFX + silence beats constant music underneath everything.

This is tool-agnostic methodology first. Where specific tools are mentioned (in [`docs/06-platform-recommendations.md`](docs/06-platform-recommendations.md)), treat them as one working setup, not the only one — swap in whatever your current AI generation, voice, and DAW tools are.

## Contributing

Found a technique that works better? PRs welcome — see [`CONTRIBUTING.md`](CONTRIBUTING.md).

## License

MIT — see [`LICENSE`](LICENSE). Use this methodology freely in your own productions.
