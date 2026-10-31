# Instructions for future project chats and agents

Scope: this project directory only. Keep public documentation in English. Use normal relative Markdown links so the same tree works in GitHub and Obsidian.

1. Read README.md, STATE.md, CORRECTIONS.md and the relevant topic before editing or advising on hardware.
2. Separate source-file facts, owner reports, recovered firmware analysis, proposed actions and actual measurements. Never infer that a planned move has happened.
3. Physical board: R2.0. Factory state: Samsung 32 GB, 0110. Target: Samsung K3KLALA0DM-MGCU ×8, 1110. Proposed move: R0715 → R0744 only. Check current STATE before repeating these facts.
4. SEL3/SEL2 are BOTTOM (APU face); SEL1/SEL0 are TOP. Native X must be reflected to match the reference BOTTOM photograph. A different photo rotation requires a new alignment.
5. Never generate/redraw/reconstruct a PCB photograph for pad identification. Use original pixels and deterministic overlays. Cross-check several neighbouring components and the electrical nets. Do not rehabilitate withdrawn images.
6. Update the affected Markdown, machine-readable data, STATE and CHANGELOG together. Add source IDs, date, exact values and uncertainty. Keep contradictory evidence with an explicit correction; do not silently erase it.
7. Run `python3 scripts/check_reference.py` after changing mapping or pad data. This tests documentation consistency, not hardware. Before a new physical instruction, recheck the relevant source and request/record actual measurements where needed.
8. Do not invent missing firmware versions, offsets, hashes, supplier prices, video transcripts, test results, tool purchases or thermal profiles. Leave unknowns explicit.
9. Keep raw commercial board files, firmware, credentials, personal contacts, invoices, private chats and image EXIF location out of the public tree. Do not assign a licence to third-party material.
10. Before updating GitHub, read the current branch/files. Use an isolated project path; do not overwrite unrelated profile/repository work. Record the actual commit and verify the published files. Before replacing Obsidian notes, make a private backup and check for concurrent edits.
11. Obsidian and GitHub copies are not automatically synchronised. State exactly which copy was written. Do not claim future chats will update files without access and a successful write.

## Update record

```text
Date:
New fact / result:
Evidence type:
Source file, hash, image, URL or private reference:
Exact measurement / observed behaviour:
What it changes:
What remains unknown:
Files updated:
Validation run:
GitHub commit / Obsidian sync status:
```
