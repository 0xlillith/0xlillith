# Rework preparation, materials and validation

**No rework has been performed on this GZ302EA board in the recorded state.** This is a preparation record, not a validated thermal recipe.

## Equipment and materials in the project record

| Item | Recorded state | Limitation |
|---|---|---|
| Yihua 862BD+ hot-air / soldering station | Reported available | Display settings do not establish pad temperature |
| PCB preheater | Available / used for practice | Exact model and calibrated board profile not recorded |
| UNI-T UT320D / thermocouple setup | Reported available | Probe placement and contact method must be recorded |
| TOMLOV digital microscope | Visible in the supplied photographs | Do not describe it as the earlier proposed stereo trinocular |
| Eight Samsung K3KLALA0DM-MGCU | Purchase and receipt reported | Electrical test and exact incoming package condition pending |
| Amtech NC-559 flux | Project consumable | Exact formulation, authenticity, shelf life and lot not verified here |
| SAC305 solder paste | Planned/available in project history | User chose paste rather than loose balls; paste grade, stencil and process remain to be matched |
| Desoldering wick | Used in practice; replacement procurement discussed | Appropriate width, wetting and heat delivery still need practice validation |
| Kapton/foil masking | Board shown masked | Appearance does not demonstrate a safe thermal profile or electrical isolation |
| Thermal interface materials | Recorded Coolmod order | See procurement; reassembly coverage must follow the original assembly |

A stencil matching the actual package/pitch, correct orientation references, suitable soldering tips, ESD handling, stable PCB support, cleaning supplies and fume extraction remain part of the preparation checklist. A photograph cannot establish all are ready. Do not assign an unconfirmed ball diameter, paste deposit volume or baking schedule.

## Practice incident — separate MX300 donor board

On 2026-10-10 the owner described removing an IC from a faulty MX300 SSD, then having the copper wick stick during pad cleaning. Extra flux and heat were used; some pads lifted. Reported settings/readings included roughly 400 °C on the iron display, around 150 °C at the heater and around 60 °C at the PCB. Hot-air display was also reported around 400 °C, with removal taking roughly one or two minutes.

These are **an incident record, not recommended settings and not a measured reflow profile**. The thermocouple attachment and spatial temperature distribution were not recorded sufficiently to derive a safe GZ302EA process. Practice must address heat transfer and non-forced release of the wick before cleaning this motherboard's BGA pads. Do not pull solidified wick or pry a package from unmolten joints.

## Preparation gates

1. Photograph the physical PCB revision, package orientation and original population. Back up data and recovery material when the machine is safely operable. Keep batteries and all external power disconnected during unpowered handling.
2. Resolve the three [continuity checks](multimeter-checks.md); record numbers rather than expected values. Confirm the actual incoming chips and their compatibility separately.
3. Provide stable support without loading components on the opposite face. Ensure masking and any metallic shielding cannot short pads or move under airflow. Review the APU/thermal-interface area and residual conductive material before heating.
4. Establish a repeatable profile using the actual equipment, thermocouple contact and a suitable practice board. Record heater setting, measured board/package temperatures, airflow, nozzle, distance and time. No generic “400 °C for N seconds” recipe is authorised by these notes.
5. Only then perform controlled package removal, pad preparation and replacement, with inspection between stages. Reball only when the incoming condition/process requires it; flux is not solder and solder paste contains both alloy and flux. Do not add an uncontrolled paste deposit to an already-balled package.
6. For the selected Samsung set, move the documented 10 kΩ resistor R0715 to R0744. Retain the same value; do not bridge the footprint. Confirm R0715 is empty and R0726/R0728/R0705 are unchanged.
7. Inspect for bridges, lifted pads, missing nearby parts and wrong orientation. Re-establish the thermal assembly correctly before normal powered testing.

This outline records the intended work sequence; it does not certify temperature limits, incoming parts, moisture handling or completion. Stop if the process becomes uncontrolled. The owner postponed hot-air work because of outdoor wind and the lack of a suitable indoor soldering location; waiting does not change project status.

## Planned validation — all results pending

| Gate | Record required |
|---|---|
| Pre-power inspection | Photos of all replaced packages and both SEL3 footprints; electrical discrepancies resolved |
| First POST | Installed BIOS version, observed boot/training behaviour, capacity reported |
| Operating system | Total physical memory, hardware-reserved memory and graphics allocation; distinguish installed from usable RAM |
| Memory integrity | Test tool/version, passes, duration, address coverage and error count, including high addresses |
| Boot repeatability | Multiple cold starts and warm restarts |
| Load | CPU/RAM and iGPU/shared-memory workloads; logs and temperatures |
| Power states | Suspend/resume and relevant AC/battery transitions |
| Stability | WHEA/system errors, crashes, corruption and sustained testing |

A first boot is not proof of reliable operation. Report actual tests, failures and limits rather than “works perfectly”. The iGPU uses shared system memory, so graphics load belongs in the planned test coverage. Sources: [S6 project record](../SOURCES.md); all process steps above are an unvalidated project plan.
