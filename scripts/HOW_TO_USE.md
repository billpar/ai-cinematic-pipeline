# How to Use This Script (Beginner Guide)

This guide assumes you've never used Python or a terminal before. It walks through everything from scratch.

**Note:** this requires a computer (Windows, Mac, or Linux) — it cannot be run from a phone.

---

## Step 1 — Check if Python is already installed

**On Mac or Linux:**
1. Open the **Terminal** app (search for "Terminal" in your applications)
2. Type `python3 --version` and press Enter
3. If you see something like `Python 3.11.4`, you already have it — skip to Step 3

**On Windows:**
1. Open **Command Prompt** (search for "cmd" in the Start menu)
2. Type `python --version` and press Enter
3. If you see something like `Python 3.11.4`, you already have it — skip to Step 3

If instead you get an error like "command not found" or "not recognized," continue to Step 2.

---

## Step 2 — Install Python (only if Step 1 showed an error)

1. Go to [python.org/downloads](https://www.python.org/downloads/)
2. Click the big download button for your operating system
3. Run the installer
   - **Important on Windows:** check the box that says **"Add Python to PATH"** before clicking Install
4. Once installed, repeat Step 1 to confirm it worked

---

## Step 3 — Download this repo to your computer

1. On the GitHub repo page, click the green **"Code"** button
2. Click **"Download ZIP"**
3. Find the downloaded ZIP file (usually in your Downloads folder) and extract/unzip it

---

## Step 4 — Write your scene breakdown

1. Open any plain text editor (Notepad on Windows, TextEdit on Mac — set to plain text mode)
2. Write your scenes using this exact format:

```
SCENE: 1
SETTING: Your location name
LIGHTING: Your lighting description

BEAT: First thing that happens.
BEAT: Second thing that happens.
BEAT: Character says, "Dialogue line here."
```

3. Save the file as `my_script.txt` — save it inside the `scripts` folder of the repo you downloaded, so it's easy to find

---

## Step 5 — Run the script

1. Open Terminal (Mac/Linux) or Command Prompt (Windows)
2. Navigate to the `scripts` folder. Type `cd ` (with a space after it), then drag the `scripts` folder from your file browser into the terminal window — it will paste the correct path automatically — then press Enter
3. Run this command (Mac/Linux):
```
python3 shot_list_generator.py my_script.txt my_shotlist.csv
```
   Or on Windows:
```
python shot_list_generator.py my_script.txt my_shotlist.csv
```

---

## Step 6 — Open your result

You'll now have a new file called `my_shotlist.csv` in the same folder. Open it with Excel, Google Sheets, or Numbers — your scenes are already broken into rows, with setting, lighting, and dialogue filled in automatically.

Fill in the remaining columns (shot type, lens, expression, camera notes) yourself, using [`templates/prompt-template.md`](../templates/prompt-template.md) and [`templates/shot-preset-library.md`](../templates/shot-preset-library.md) as a reference.

---

## Common problems

| Problem | Likely fix |
|---|---|
| "command not found" / "not recognized" | Python isn't installed correctly — redo Step 2, and on Windows make sure "Add to PATH" was checked |
| "No such file or directory" | You're not in the right folder — redo Step 5, point 2 |
| The CSV file looks empty or wrong | Check your input file matches the exact format in Step 4 — `SCENE:`, `SETTING:`, `LIGHTING:`, `BEAT:` must be spelled exactly like that |

If you're stuck, open an issue on the repo and describe what happened — happy to help troubleshoot.
