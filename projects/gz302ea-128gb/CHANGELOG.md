# Changelog

## 2026-11-01 — owner-reported continuity checks passed

- Recorded the owner's report that all three multimeter checks passed with direct continuity: T1 R0715.2–R0744.1, T2 R0715.1–C0704.2 and T3 R0744.2–R0726.2.
- Updated the measurement procedure/log and machine-readable results; retained null numerical Ω values, shorted-lead reference and missing instrument/test-condition metadata. No zero-ohm values were inferred.
- Added source S8 and updated README, STATE and the historical corrections to distinguish an owner-reported physical test from source-file verification and runtime validation.
- Preserved the existing pad coordinates, photographs, resistor mapping and nine recovered firmware profiles. Earlier generated guides remain withdrawn.
- Kept resistor relocation, DRAM replacement, 128 GB POST and stability tests pending. Passing same-net continuity checks is not a complete short-circuit test or a successful-upgrade report.
- The record date is the documentation date; the exact physical test timestamp was not supplied.

## 2026-10-31 — consolidated reference

- Re-read the original FZ; matched its SHA-256 and rechecked the strap nets, coordinates, faces and BOM.
- Added the three unpowered continuity checks, precise pad identities, annotated original-photo points and blank measurement records.
- Retained the nine-row APCB table and all conversion moves; separated firmware-table provenance from source-file and runtime verification.
- Corrected the physical revision to R2.0 despite SMBIOS 1.0; documented the BOTTOM reflection and split between board faces.
- Explicitly withdrew the incorrect generated diagrams, wrong-side overview and overconfident confirmation language.
- Recorded the current disassembled/masked but unmodified state, procurement evidence, equipment history, donor-board incident and validation gates.
- Added maintenance instructions and a reference consistency checker. No hardware change, BIOS flash or measurement is implied by this documentation update.
