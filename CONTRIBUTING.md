# Contributing

This is a living methodology document — it's meant to be improved as tools and techniques evolve.

## Good contributions

- New consistency techniques that fix a specific, reproducible drift problem
- Corrections to existing techniques based on your own production testing
- Additional rows for the "Common Mistakes and Fixes" table
- Improvements to `scripts/shot_list_generator.py`
- Tool-agnostic alternatives to anything currently written for a specific platform

## What to avoid

- Vendor-specific marketing language — describe what a technique achieves, not why a specific product is the best
- Untested theory — if you haven't actually produced something with the technique, note that clearly in the PR description
- Breaking the existing doc structure without discussion — open an issue first for structural changes

## How to submit

1. Fork the repo
2. Make your change in a new branch
3. If you're adding a technique, include a short real-world example the way the existing docs do
4. Open a PR describing what problem this solves and how you verified it works

## Reporting issues

Use the issue templates in `.github/ISSUE_TEMPLATE/` for bug reports against the script tool, or open a blank issue for methodology discussion.
