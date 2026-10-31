# Corrections and withdrawn material

These corrections supersede earlier chat illustrations and the initial Obsidian README. They are retained explicitly so a later agent cannot revive an incorrect instruction.

| Earlier claim / material | Correction | Basis |
|---|---|---|
| SMBIOS `Version 1.0` meant the project PCB was Rev 1.0 | The physical board is marked R2.0. SMBIOS does not override that marking. Genuine R1.0 boards remain outside this map. | Owner's PCB photograph |
| The relevant region was above the upper-right RAM in the overview | In the owner's overview orientation, it is above the **upper-left** RAM, below the upper-left APU mounting hole. | Corrected mirror interpretation and matching nearby components |
| Native BoardView X could be displayed unchanged against the BOTTOM photograph | This photo requires horizontal reflection of native coordinates. | Coordinate matching |
| Photo-like generated graphics identified the pads | Those graphics altered component appearance/placement and even labelled multi-pin parts as resistors. **All such generated guides are withdrawn.** | Comparison with original photographs |
| All eight strap footprints could be marked on the APU-side macro | SEL3/SEL2 are BOTTOM; SEL1/SEL0 are TOP. | FZ `SYM_MIRROR` and source reader |
| The empty footprint above the destination was another valid destination | It is R2848, connected to SPI nets, not R0744. | Source nets |
| All +1.8 V-labelled rails could be treated as interchangeable | +1.8VS and +1.8VSUS are distinct nets. The upper pad of C0704 is GND. | Source nets |
| Existing APCB entries guaranteed stock-BIOS operation | The recovered table is useful but its original binary provenance has not been recovered. Runtime success remains unproven. | Evidence audit |
| “Confirmed” implied the owner had measured the board | Source-file verification, photographic matching, continuity measurements and runtime tests are separate evidence levels. | No physical readings supplied |

## Withdrawn filenames

Do not use the following old outputs for pad location, even if an earlier chat called them verified:

- `mapa_de_resistencias_gz302ea_128_gb.png`
- `GZ302EA_Samsung_128GB_straps.png` and its early SVG/preview (unreflected physical map)
- `GZ302EA_R2_foto_real_zona_straps.png` (old right-side zone)
- `guía_de_cambio_de_straps_gz302ea.png`
- `guía_visual_de_mod_de_placa_asus_gz302ea.png`
- `guía_de_cambio_de_strap_samsung_128_gb.png`

They are not included as active references. The current diagram is an annotation of the original microscope photograph, with pad locations traceable through `data/probe-checks.json`. The original full-resolution Spanish measurement guides may be retained privately as a historical reference, but new edits must use the source photograph rather than repainting it.

The owner explicitly stated that **nothing had been desoldered** after the erroneous directions. Do not invent a repair, a damaged component or a successfully completed move.
