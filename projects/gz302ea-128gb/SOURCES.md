# Evidence and sources

Updated: 2026-10-31. Different evidence types must remain distinct.

## S1 — Original BoardView, privately held

File: `GZ302EA Rev 2.0 BoardView .fz`.

SHA-256: `b87c91f10ef4163c7129db8a7e1eedea4f2d148d829fb911e5b05c15f6824944`.

A fresh read during this documentation update confirmed the eight strap designators, their pad nets/coordinates, face fields and BOM population. The source identifies GZ302EA 2.0 / 60NR0JY0-MB4000, reference 32 GB MAX+-395 board. The minimal extract is stored in `data/boardview-extract.json`.

This verifies what the file contains, not the electrical state of every physical board. The raw commercial file and its viewer are not redistributed.

## S2 — Owner's photographs

`1000075585.jpg`: overall board photograph; physical `GZ302EA MAIN BOARD R2.0` marking. `1000075612.jpg`: final microscope view of the corrected region, 1536 × 1157 pixels. The latter's SHA-256 and exact pixel contact coordinates are stored in `data/probe-checks.json`.

Published image processing is limited to cropping, rotation where stated, resizing/compression, and marker overlays. No components or pads are generated. The reference photograph still shows the factory state; it is not an “after” image. No EXIF location or private file paths are required for these published derivatives.

## S3 — Recovered BIOS/APCB table

The nine-row table was pasted back into the project conversation by the owner, then preserved in the Obsidian README. It records P/N, capacity, instance, BoardMask and SEL3..0.

**Missing:** original analysed binary, BIOS version, SHA-256, APCB offsets and extraction-tool provenance. It has not been independently re-extracted in this documentation pass. The source's internal consistency and agreement with the 32 GB Samsung BOM are useful but not equivalent to a runtime trace.

## S4 — FZ face interpretation

[OpenBoardView FZFile.cpp](https://github.com/OpenBoardView/OpenBoardView/blob/master/src/openboardview/FileFormats/FZFile.cpp), read on 2026-10-31. Its treatment of `smirror` provides the reference for YES/BOTTOM and NO/TOP. No OpenBoardView source is copied into this project. The local checking script supports only the unencrypted layout of the identified source file; it is not a generic BoardView tool.

## S5 — Meter handling

[Fluke: How to Use a Multimeter](https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide), accessed 2026-10-31. Used for general continuity/resistance mode and de-energised testing precautions, **not** for the ASUS-specific pad identities, which come from S1.

## S6 — Project conversation record

Recorded by the owner: purchase/receipt of Samsung DRAM; available tools; preference for solder paste; donor-board practice; board disassembly and masking; no desoldering yet; work postponed because of wind. The current [STATE](STATE.md) reflects the latest explicit hardware report, not a planned operation.

Relevant historical chat entries include chip-model confirmation (2026-09-18), supplier inspection video (2026-09-22), reported chip arrival (2026-09-29), and MX300 wick/pad incident (2026-10-10). Dates from older chat summaries are historical pointers, not a reconstructed tool-execution log.

## S7 — Private Obsidian purchase note

Existing `Compras.md`, read 2026-10-31. Records Samsung ×8 and the Coolmod thermal-material order: EUR 19.95 + EUR 32.95 = EUR 52.90 before unrecorded shipping. Some equipment checkboxes predate later purchases; newer observations are kept separately rather than silently treating every unchecked box as still missing.

The original note is retained privately. Public procurement notes omit personal messages, addresses, account details and unneeded commercial/private data.

## Sources not recovered

The original Chinese modification-video URLs/transcripts; the supplier video's full technical transcript; Lucy/Tina RFQ quotations; Taobao/Superbuy exact offers; and BIOS extraction output beyond the table were not recovered. Mention of these investigations is preserved as a retrieval task, not as technical proof or an attributable quotation. No “best offer” ranking is published without those records.

## Evidence labels

- **Source-verified:** checked in a file or image named here.
- **Owner-reported:** explicitly stated in the project history.
- **Recovered analysis:** preserved result whose original calculation/binary has not been rechecked.
- **Planned / expected:** work or behaviour not yet observed.
- **Measured / tested:** only after actual results are recorded; currently no continuity or modified-board results exist.

Public release does not grant rights to the withheld BoardView, vendor materials or firmware. No third-party licence is inferred from possession of a source file.
