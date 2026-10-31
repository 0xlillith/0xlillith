# Hardware baseline and firmware evidence

## Baseline

| Item | Recorded information | Evidence |
|---|---|---|
| Machine | ASUS ROG Flow Z13 (2025), GZ302EA | Owner's project |
| Physical PCB | `GZ302EA MAIN BOARD R2.0` | Owner's board photograph |
| SMBIOS board version | `1.0` | Earlier software report; not the physical revision |
| Platform | AMD Strix Halo; reference BOM lists AI MAX+-395 | BoardView/BOM and project record |
| Factory DRAM | Samsung `K3KL8L80DM-MGCU`, 8 × 4 GB | Project memory report and source BOM |
| Factory package | FBGA315; source BOM: LPD5X 8533 1024M×32 1.05 V DD | Source BOM |
| Software-reported speeds | `Speed=8533`, `ConfiguredClockSpeed=8000` | Earlier Windows report; not independently measured bus timing |
| Target | Eight Samsung `K3KLALA0DM-MGCU`, 128 GB total | Purchased/chosen project parts |
| Current physical intervention | Disassembly and masking only | Owner's latest explicit report |

The eight package positions in the reference file are U1401, U1402, U1501, U1502, U1601, U1602, U1701 and U1702. Software memory-device entries alone do not establish physical package count or channel topology; the BoardView independently identifies those eight package sites. Do not derive die count, rank topology or ball diameter from the Windows table.

## APCB findings and their limit

The recovered table associates nine DRAM configurations with APCB instances 1–9 and BoardMasks 0x0002–0x0200. It includes three named 128 GB configurations. The factory Samsung 32 GB row (`0110`, instance 5, mask 0x0020, K3KL8L80DM-MGCU) is consistent with the source BOM and strap population.

This consistency supports the interpretation, but does not replace a reproducible firmware extraction. The original BIOS/APCB binary is not part of this publication. These identifiers remain **unknown**:

| Required record | Status |
|---|---|
| Analysed ASUS BIOS version | Not recovered |
| SHA-256 of analysed image | Not recovered |
| Currently installed BIOS version | Not recorded here |
| APCB block offsets / extraction command / tool version | Not recovered |
| Selector implementation mapping raw bits to a profile | Not independently reproduced here |

The most defensible current conclusion is: **the recovered firmware table includes profiles for the proposed parts; stock-firmware operation is plausible, but not guaranteed**. Do not claim that every stock BIOS version supports them, that any 16 GB BGA315 device is interchangeable, or that a successful 128 GB boot has already occurred.

Earlier chats mentioned independent mods and video reports without BIOS modification. Their exact links/transcripts were not recovered for this edition, so they are not treated as independently checked evidence.

## Before rework

Record the installed BIOS version when safe access to the assembled system is available, retain any already-made backup, and recover the original analysis image, hash and extraction steps. Do not flash an arbitrary BIOS or reassemble merely to satisfy a documentation checkbox without assessing the hardware state. Preserve recovery keys and data backups before future firmware or hardware changes.

Source register: [S1–S3 and S6](../SOURCES.md).
