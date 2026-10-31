# Other configurations — reference only

The selected project build is Samsung 128 GB. This page retains the other eight profiles without suggesting that they have been tested.

All moves below start from **Samsung 32 GB `0110`**, with **R0715, R0726, R0728, R0705** fitted. They are not incremental instructions from one row to the next. Use matching DRAM packages; changing straps alone does not add capacity.

| Target | SEL3..0 | BOTTOM / photographed face | TOP / opposite face | Final populated positions, SEL3 to SEL0 |
|---|:---:|---|---|---|
| 32 GB SK hynix | `0100` | None | `R0728 → R0727` | R0715, R0726, R0727, R0705 |
| 32 GB Samsung | `0110` | None | None | R0715, R0726, R0728, R0705 |
| 32 GB Micron | `0111` | None | `R0705 → R0739` | R0715, R0726, R0728, R0739 |
| 64 GB SK hynix | `0000` | `R0726 → R0719` | `R0728 → R0727` | R0715, R0719, R0727, R0705 |
| 64 GB Samsung | `0001` | `R0726 → R0719` | `R0728 → R0727`; `R0705 → R0739` | R0715, R0719, R0727, R0739 |
| 64 GB Micron | `0011` | `R0726 → R0719` | `R0705 → R0739` | R0715, R0719, R0728, R0739 |
| 128 GB SK hynix | `1100` | `R0715 → R0744` | `R0728 → R0727` | R0744, R0726, R0727, R0705 |
| 128 GB Samsung | `1110` | `R0715 → R0744` | None | R0744, R0726, R0728, R0705 |
| 128 GB Micron | `1111` | `R0715 → R0744` | `R0705 → R0739` | R0744, R0726, R0728, R0739 |

Each row leaves exactly one resistor in each pair. The two unchanged bottom-face straps in the Samsung upgrade are R0726 (fitted) and R0719 (empty). Both TOP-face pairs remain untouched for Samsung 128 GB.

SK hynix 128 GB needs the additional **TOP-face R0728 → R0727** move. Micron 128 GB needs **TOP-face R0705 → R0739**. Their positions cannot be marked on the APU-face photograph because they are on the other side.

Part numbers, APCB instances and BoardMasks are in the [master table](../README.md#complete-dram--apcb--strap-table). Electrical pairs and sides were read from the BoardView; the firmware association is the recovered project table, not a new firmware extraction. No alternative profile has a recorded runtime test in this project.
