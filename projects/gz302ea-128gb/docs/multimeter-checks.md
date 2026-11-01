# Unpowered continuity checks before the Samsung strap change

Status: **T1, T2 and T3 passed with direct continuity, as reported by the owner.** Recorded 2026-11-01; the exact measurement timestamp and numerical resistance readings were not supplied. These checks support the pad identification; they do not certify the upgrade. See [S8](../SOURCES.md#s8--owners-continuity-test-report).

![Probe locations](../assets/probe-points.webp)

## Preparation

Disconnect the battery, charger, USB devices and other powered connections. The board must be de-energised before continuity/resistance measurements. Use the meter's instructions to confirm residual voltage has fallen safely; do not discharge components by shorting them. Black lead goes in COM; red lead goes in V/Ω, not A/mA. Select continuity or resistance. Record the reading with the probe tips touching before probing the board. Use fine tips under magnification without scraping or bridging adjacent pads. General meter safety: [Fluke](https://www.fluke.com/en/learn/blog/maintenance-monitoring/how-to-use-a-multimeter-guide).

All directions below refer to the photograph above. Do not reuse them after rotating or mirroring an image.

## Contact points

| Label | Reference | Pad | In this photograph | BoardView net |
|---|---|---:|---|---|
| A | R0715 | 2 | Upper end of the mounted vertical resistor | `DIMM_SEL3` |
| B | R0744 | 1 | Left pad of the empty horizontal destination | `DIMM_SEL3` |
| C | R0715 | 1 | Lower end of that same mounted resistor | `GND` |
| D | C0704 | 2 | Upper end of the capacitor below R0715 | `GND` |
| E | R0744 | 2 | Right pad of the empty horizontal destination | `+1.8VS` |
| F | R0726 | 2 | Left end of the second mounted horizontal resistor at upper right | `+1.8VS` |

The horizontal resistor above R0726 is **R0733**, not another strap. The empty horizontal footprint above R0744 is **R2848**, not the destination. C0704 is a capacitor: its **upper pad 2 is GND**, while its lower pad 1 is **+1.8VSUS**, not +1.8VS. Do not substitute the screw ring as a ground reference without verifying it.

## Three measurements

| Test | Red | Black | Expected | Owner-reported result |
|---|---|---|---|---|
| T1 — SEL3 connection | A | B | Low, stable resistance close to the shorted-lead reading | PASS — direct continuity |
| T2 — ground connection | C | D | Same | PASS — direct continuity |
| T3 — pull-up rail connection | E | F | Same | PASS — direct continuity |

These are same-net checks. **10 kΩ is not the expected reading**: none measures across both ends of R0715. The name `+1.8VS` is not an expected voltage during this procedure; do not power the board for T3.

Use the numerical resistance reading as well as the beeper. There is no universal beeper threshold or fixed acceptance value specified here. If a result is OL, kiloohms, unstable, or materially above the shorted-lead reference, check tip contact, mode and component identification. Do not desolder until the discrepancy is resolved.

Passing these three checks supports the pad identification, but is not a complete short-circuit test: a fault shorting nets together could also produce continuity. It does not isolate the resistor's value, prove every rail is healthy, validate the DRAM part, or establish BIOS compatibility. Those are separate checks.

## Recorded results

Evidence: the owner explicitly reported completing all three multimeter checks successfully, with direct continuity. This is an owner-reported physical test, not an assistant measurement or a software-check result. No meter display photographs, numerical readings or shorted-lead reference were supplied; unknown values remain unreported rather than being filled with zero or expected values.

| Field | Recorded value |
|---|---|
| Record date / operator | 2026-11-01 / board owner |
| Exact measurement timestamp | Not supplied |
| Instrument | Multimeter; model and selected mode not supplied |
| Battery / charger / powered peripherals disconnected | Required by the procedure; not separately confirmed in the result message |
| Residual voltage check | Not separately reported |
| Shorted-lead reference, Ω | Not supplied |
| T1 A–B result / Ω | PASS — direct continuity; numerical Ω not supplied |
| T2 C–D result / Ω | PASS — direct continuity; numerical Ω not supplied |
| T3 E–F result / Ω | PASS — direct continuity; numerical Ω not supplied |
| Any discrepancy / corrective action | None reported for these three checks |
| Consequence | Physical test report supports the identified SEL3, ground and pull-up-rail connections |
| Rework / 128 GB operation | Not reported as performed; still pending |

Update this table and [probe-checks.json](../data/probe-checks.json) together when further results are supplied. The source records retain original photo coordinates and BoardView coordinates. The continuity result does not change the documented resistor positions or prove that any resistor has been moved.

## After the eventual move

The copper connections tested above do not change when the resistor is moved, so passing them again does **not** prove that the new resistor was soldered correctly. Inspect both solder joints at R0744 and confirm R0715 is empty. Check for bridges and displaced adjacent parts. An in-circuit resistance reading may be affected by other paths and is not automatically an isolated 10 kΩ measurement.

Sources: [S1 and S2](../SOURCES.md) for pad identities and the photograph, [S5](../SOURCES.md#s5--meter-handling) for meter handling, and [S8](../SOURCES.md#s8--owners-continuity-test-report) for the reported results. Numerical resistance readings, rework and modified-board runtime validation remain unreported.
