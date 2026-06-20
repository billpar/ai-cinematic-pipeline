#!/usr/bin/env python3
"""
shot_list_generator.py

Turns a simple scene/beat script file into a scaffolded shot list CSV,
matching templates/shot-list-template.csv columns.

Input file format (plain text):

    SCENE: 1
    SETTING: Location A
    LIGHTING: Warm overhead light

    BEAT: Wide establishing shot of the location, no characters yet.
    BEAT: Character A kneels beside an object, performing a small task.
    BEAT: Character A says, "Line of dialogue here."

    SCENE: 2
    SETTING: Location B
    LIGHTING: Cool overhead light

    BEAT: Character B stands at a central table studying an object.

Usage:
    python3 shot_list_generator.py input_script.txt output_shotlist.csv
"""

import csv
import sys
import re

COLUMNS = [
    "scene", "beat", "timestamp", "shot_type", "lens",
    "characters_in_frame", "setting", "immutable_lighting", "action",
    "expression_physical", "dialogue", "voiceover", "audio_notes",
    "elements_attached", "seed", "start_frame_source", "status", "notes",
]


def parse_script(path):
    scenes = []
    current_scene = None

    with open(path, "r", encoding="utf-8") as f:
        for raw_line in f:
            line = raw_line.strip()
            if not line:
                continue

            if line.upper().startswith("SCENE:"):
                if current_scene:
                    scenes.append(current_scene)
                current_scene = {
                    "scene": line.split(":", 1)[1].strip(),
                    "setting": "",
                    "lighting": "",
                    "beats": [],
                }
            elif line.upper().startswith("SETTING:") and current_scene:
                current_scene["setting"] = line.split(":", 1)[1].strip()
            elif line.upper().startswith("LIGHTING:") and current_scene:
                current_scene["lighting"] = line.split(":", 1)[1].strip()
            elif line.upper().startswith("BEAT:") and current_scene:
                current_scene["beats"].append(line.split(":", 1)[1].strip())

        if current_scene:
            scenes.append(current_scene)

    return scenes


def extract_dialogue(beat_text):
    """Pull out a quoted line if present, return (action_text, dialogue_text)."""
    match = re.search(r'"([^"]+)"', beat_text)
    if match:
        dialogue = match.group(1)
        action = beat_text.replace(f'"{dialogue}"', "").strip()
        action = re.sub(r"\bsays,?\s*$", "", action).strip().rstrip(",")
        return action, dialogue
    return beat_text, ""


def build_rows(scenes):
    rows = []
    for scene in scenes:
        for i, beat_text in enumerate(scene["beats"], start=1):
            action, dialogue = extract_dialogue(beat_text)
            row = {
                "scene": scene["scene"],
                "beat": i,
                "timestamp": "",
                "shot_type": "",
                "lens": "",
                "characters_in_frame": "",
                "setting": scene["setting"],
                "immutable_lighting": scene["lighting"],
                "action": action,
                "expression_physical": "",
                "dialogue": dialogue,
                "voiceover": "",
                "audio_notes": "",
                "elements_attached": "",
                "seed": "",
                "start_frame_source": "",
                "status": "planned",
                "notes": "",
            }
            rows.append(row)
    return rows


def write_csv(rows, out_path):
    with open(out_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 shot_list_generator.py input_script.txt output_shotlist.csv")
        sys.exit(1)

    input_path, output_path = sys.argv[1], sys.argv[2]
    scenes = parse_script(input_path)

    if not scenes:
        print("No scenes found. Check your input file format — see the docstring at the top of this script.")
        sys.exit(1)

    rows = build_rows(scenes)
    write_csv(rows, output_path)

    total_beats = sum(len(s["beats"]) for s in scenes)
    print(f"Scaffolded {len(scenes)} scene(s), {total_beats} beat(s) -> {output_path}")
    print("Fill in shot_type, lens, expression, elements_attached, and seed columns per beat before generating.")


if __name__ == "__main__":
    main()
