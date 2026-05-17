# Deep Research Manual Packet 0023

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0023
- Chunk count: 267
- Chunk range: 5587-5853
- Source count: 248
- Target maximum characters: 750000

## Manual Chunks

## Chunk 5587: DTC P04DF (K20C2) (2016 2017 2018)

- Title: DTC P04DF (K20C2) (2016 2017 2018)
- Source path: `pages\6739.html`
- Chunk ID: `chunk_9ec3f733d5cc`
- Images: `images\GHH403115.jpeg`
- Duplicate sources: `pages\8326.html`, `pages\23130.html`, `pages\21543.html`

### Full Text

````text
# DTC P04DF (K20C2) (2016 2017 2018)

DTC P04DF: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is 0.3 kPa (2 mmHg, 0.08 inHg) or more for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5588: DTC P04DF (K20C2) (2019 2020 2021)

- Title: DTC P04DF (K20C2) (2019 2020 2021)
- Source path: `pages\6740.html`
- Chunk ID: `chunk_11bacfe5e0e8`
- Images: `images\GHH403116.jpeg`
- Duplicate sources: `pages\8327.html`, `pages\23131.html`, `pages\21544.html`

### Full Text

````text
# DTC P04DF (K20C2) (2019 2020 2021)

DTC P04DF: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is 0.3 kPa (2 mmHg, 0.08 inHg) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5589: DTC P04DF (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P04DF (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\6741.html`
- Chunk ID: `chunk_15acb2a6b5b8`
- Images: `images\GHH403117.jpeg`, `images\GHH403118.jpeg`
- Duplicate sources: `pages\8328.html`, `pages\23132.html`, `pages\21545.html`

### Full Text

````text
# DTC P04DF (L15B7 (except Si)/L15BA/L15BY)

DTC P04DF: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of negative pressure side:

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is 0.3 kPa (2 mmHg, 0.08 inHg) or more for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5590: DTC P04DF(Si) (2017 2018 2019 2020 2021)

- Title: DTC P04DF(Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6742.html`
- Chunk ID: `chunk_51c1a27a80f0`
- Images: `images\GHH403119.jpeg`, `images\GHH403120.jpeg`
- Duplicate sources: `pages\8329.html`, `pages\23133.html`, `pages\21546.html`

### Full Text

````text
# DTC P04DF(Si) (2017 2018 2019 2020 2021)

DTC P04DF: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of negative pressure side:

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is 0.3 kPa (2 mmHg, 0.08 inHg) or more for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5591: DTCP04F0 (K20C1) (2017 2018 2019)

- Title: DTCP04F0 (K20C1) (2017 2018 2019)
- Source path: `pages\6743.html`
- Chunk ID: `chunk_32d9782c6455`
- Images: `images\GHH403121.jpeg`
- Duplicate sources: `pages\8330.html`, `pages\23134.html`, `pages\21547.html`

### Full Text

````text
# DTCP04F0 (K20C1) (2017 2018 2019)

DTC P04F0: Evaporative Emission (EVAP) System Incorrect Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors second purge line which is used for regeneration of evaporative emission (EVAP) canister at full load (boost condition) for stuck closed detection. Second purge line has a mechanical non-return valve which prevents back purging of EVAP canister with boost pressure. The described test will detect low purge flow fault, which can be caused by non-return valve stuck closed malfunction. The second purge line monitoring will be performed in boost mode, when canister purging is performed using second purge line. As soon as enable conditions are fulfilled, the EVAP canister purge valve will be stimulated with the special pattern. In order to detect second purge line stuck closed fault, the fuel tank pressure oscillations are monitored during stimulation cycle of the EVAP canister purge valve. If no fuel tank pressure oscillations can be observed during EVAP canister purge valve open phase, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | -

Engine speed [Engine Speed] | 2, 000 rpm | 6, 000 rpm

Boost pressure | 10 kPa (75 mmHg, 3.0 inHg) | -

12 volt battery voltage [Battery] | 10.7 V | -

Charging efficiency | 80 % | -

Fuel feedback | Closed loop

[ ]: HDS Parameter

Malfunction Threshold

The pressure oscillation is less than 0.1875 kPa (1.406 mmHg, 0.05536 inHg) at least 3 times during the open phase of EVAP canister purge valve stimulation cycle.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve stuck closed

- EVAP canister purge valve stuck open

- Purge line not connected

- Non-return valve B stuck closed

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle at engine speed [Engine Speed] 2, 000 rpm or more with full load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5592: DTC P04F0 (K20C1) (2019 2020 2021)

- Title: DTC P04F0 (K20C1) (2019 2020 2021)
- Source path: `pages\6744.html`
- Chunk ID: `chunk_ca817e2bc271`
- Images: `images\GHH403122.jpeg`
- Duplicate sources: `pages\8331.html`, `pages\23135.html`, `pages\21548.html`

### Full Text

````text
# DTC P04F0 (K20C1) (2019 2020 2021)

DTC P04F0: Evaporative Emission (EVAP) System Incorrect Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors second purge line which is used for regeneration of evaporative emission (EVAP) canister at full load (boost condition) for stuck closed detection. Second purge line has a mechanical non-return valve which prevents back purging of EVAP canister with boost pressure. The described test will detect low purge flow fault, which can be caused by non-return valve stuck closed malfunction. The second purge line monitoring will be performed in boost mode, when canister purging is performed using second purge line. As soon as enable conditions are fulfilled, the EVAP canister purge valve will be stimulated with the special pattern. In order to detect second purge line stuck closed fault, the fuel tank pressure oscillations are monitored during stimulation cycle of the EVAP canister purge valve. If no fuel tank pressure oscillations can be observed during EVAP canister purge valve open phase, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | -

Engine coolant temperature [ECT Sensor 1] | 140 deg.F (60 deg.C) | -

Engine speed [Engine Speed] | 2, 000 rpm | 6, 000 rpm

Boost pressure | 10 kPa (75 mmHg, 3.0 inHg) | -

12 volt battery voltage [Battery] | 10.7 V | -

Charging efficiency | 80.02 % | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Integrated purge mass flow after a longer purge stop | 0.49 g (0.0173 oz) | -

Integrated mass flow at repeating EVAP canister purge valve diagnosis | 0 g (0 oz) | -

Fuel feedback | Closed loop

[ ]: HDS Parameter

Malfunction Threshold

Both conditions occur:

- Mass flow during diagnosis second purge line is 0 - 2.5 kg/h (0 - 5.5 lbs/h)*.

- The pressure oscillation is less than 0.1875 kPa (1.406 mmHg, 0.05536 inHg) at least 3 times during the open phase of EVAP canister purge valve stimulation cycle.

*: Depending on diagnosis duration

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve stuck closed

- EVAP canister purge valve stuck open

- Purge line not connected

- Non-return valve B stuck closed

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle at engine speed [Engine Speed] between 2, 000 - 6, 000 rpm with full load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5593: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\6745.html`
- Chunk ID: `chunk_8be98ef59a01`
- Images: `images\GHH403123.jpeg`, `images\GHH403124.jpeg`
- Duplicate sources: `pages\8332.html`, `pages\23136.html`, `pages\21549.html`

### Full Text

````text
# DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

DTC P04F0: Evaporative Emission (EVAP) System Incorrect Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P145D is judged as NG

Duration | 11 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

P145D is determined as NG and P04DF is determined as OK.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor output stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5594: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\6745.html`
- Chunk ID: `chunk_1d7de02f3941`
- Images: `images\GHH403123.jpeg`, `images\GHH403124.jpeg`
- Duplicate sources: `pages\8332.html`, `pages\23136.html`, `pages\21549.html`

### Full Text

````text
Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5595: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6746.html`
- Chunk ID: `chunk_b8bb8f483295`
- Images: `images\GHH403125.jpeg`, `images\GHH403126.jpeg`
- Duplicate sources: `pages\8333.html`, `pages\23137.html`, `pages\21550.html`

### Full Text

````text
# DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P04F0: Evaporative Emission (EVAP) System Incorrect Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P145D is judged as NG

Duration | 11 seconds* 1 (9.5 seconds)* 2 or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si) and L15BY

*2: L15BA

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

P145D is determined as NG and P04DF is determined as OK.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor output stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.
````

## Chunk 5596: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P04F0 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6746.html`
- Chunk ID: `chunk_8c76010ad617`
- Images: `images\GHH403125.jpeg`, `images\GHH403126.jpeg`
- Duplicate sources: `pages\8333.html`, `pages\23137.html`, `pages\21550.html`

### Full Text

````text
nstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5597: DTC P04F0 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P04F0 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6747.html`
- Chunk ID: `chunk_f01e90b1fa03`
- Images: `images\GHH403127.jpeg`, `images\GHH403128.jpeg`
- Duplicate sources: `pages\8334.html`, `pages\23138.html`, `pages\21551.html`

### Full Text

````text
# DTC P04F0 (Si) (2017 2018 2019 2020 2021)

DTC P04F0: Evaporative Emission (EVAP) System Incorrect Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P145D is judged as NG

Duration | 9.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

P145D is determined as NG and P04DF is determined as OK.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor output stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.
````

## Chunk 5598: DTC P04F0 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P04F0 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6747.html`
- Chunk ID: `chunk_0b21f567440f`
- Images: `images\GHH403127.jpeg`, `images\GHH403128.jpeg`
- Duplicate sources: `pages\8334.html`, `pages\23138.html`, `pages\21551.html`

### Full Text

````text
the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5599: DTC P04F1 (K20C1) (2019 2020 2021)

- Title: DTC P04F1 (K20C1) (2019 2020 2021)
- Source path: `pages\6748.html`
- Chunk ID: `chunk_f81d27610d89`
- Images: `images\GHH403129.jpeg`
- Duplicate sources: `pages\8335.html`, `pages\23139.html`, `pages\21552.html`

### Full Text

````text
# DTC P04F1 (K20C1) (2019 2020 2021)

DTC P04F1: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air. Several steps are taken to detect for leakage in the fuel supply system. If no pressure decrease has been detected during vacuum build-up, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

General enable conditions to trigger EVAP system monitor

Condition | Minimum | Maximum

Elapsed time after starting the engine | 9 minutes 10 seconds | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 113 deg.F (45 deg.C)

Condition | Minimum | Maximum

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Fuel tank pressure | -4 kPa (-30 mmHg, -1.1 inHg) | 4 kPa (30 mmHg, 1.1 inHg)

12 volt battery voltage [Battery] | 10.7 V | 16 V

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Fuel feedback | Closed loop

Other | No refueling

Both EVAP canister vent shut valve and EVAP canister purge valve are commanded open for at least 20 seconds

No excessive ambient pressure change for at least 5 minutes

Canister purging

Condition

Other | Both EVAP canister vent shut valve and EVAP canister purge valve are commanded open

EVAP canister vent shut valve stuck check

Condition

Other | EVAP canister vent shut valve stuck in closed position has not been detected

EVAP canister vent shut valve is commanded open and EVAP canister purge valve is commanded closed

Pressure stabilization after purging

Condition

Other | Fuel tank pressure has stabilized after purging for at least 3 seconds within 10 seconds

Phase A: Compensation gradient determination

Condition

Other | EVAP canister vent shut valve is commanded closed

EVAP canister purge valve stuck in open position has not been detected

No high evaporation condition

No condensation condition

Phase B: Vacuum build-up

Condition

Other | EVAP canister purge valve is commanded open

EVAP canister vent shut valve remains commanded closed

No large leakage fault was detected while vacuum build-up

[ ]: HDS Parameter

Malfunction Threshold

The difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -0.05 kPa (-0.4 mmHg, -0.015 inHg) (no significant pressure decrease has been detected) or integrated purge mass flow has reached 0.35 g (0.0124 oz).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for a while.

- Stop the vehicle and let it idle for 10 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5600: DTC P04F1 (K20C2) (2016 2017 2018)

- Title: DTC P04F1 (K20C2) (2016 2017 2018)
- Source path: `pages\6749.html`
- Chunk ID: `chunk_47de69aa6e12`
- Images: `images\GHH403130.jpeg`
- Duplicate sources: `pages\8336.html`, `pages\23140.html`, `pages\21553.html`

### Full Text

````text
# DTC P04F1 (K20C2) (2016 2017 2018)

DTC P04F1: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than 0.2 kPa (2 mmHg, 0.07 inHg) for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5601: DTC P04F1 (K20C2) (2019 2020 2021)

- Title: DTC P04F1 (K20C2) (2019 2020 2021)
- Source path: `pages\6750.html`
- Chunk ID: `chunk_adad60cd8192`
- Images: `images\GHH403131.jpeg`
- Duplicate sources: `pages\8337.html`, `pages\23141.html`, `pages\21554.html`

### Full Text

````text
# DTC P04F1 (K20C2) (2019 2020 2021)

DTC P04F1: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than 0.2 kPa (2 mmHg, 0.07 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

- EVAP canister purge valve open stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5602: DTC P04F1 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P04F1 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\6751.html`
- Chunk ID: `chunk_db0aae323f65`
- Images: `images\GHH403132.jpeg`, `images\GHH403133.jpeg`
- Duplicate sources: `pages\8338.html`, `pages\23142.html`, `pages\21555.html`

### Full Text

````text
# DTC P04F1 (L15B7 (except Si)/L15BA/L15BY)

DTC P04F1: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of negative pressure side:

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than 0.3 kPa (2 mmHg, 0.08 inHg) for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5603: DTC P04F1 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P04F1 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6752.html`
- Chunk ID: `chunk_7b8019012424`
- Images: `images\GHH403134.jpeg`, `images\GHH403135.jpeg`
- Duplicate sources: `pages\8339.html`, `pages\23143.html`, `pages\21556.html`

### Full Text

````text
# DTC P04F1 (Si) (2017 2018 2019 2020 2021)

DTC P04F1: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of negative pressure side:

<STEP 1>

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P0441 OK)

- P04F1 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P0441 NG)

- Either purge flow P04F1 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, classify the failed part according to <STEP 2>

<STEP 2>

If there is no pulse, it is determined as either no purge flow or the EVAP canister purge valve is stuck OPEN:

When the FTP sensor fluctuates from negative pressure to atmospheric pressure after the vehicle condition is turned to the OFF (LOCK) mode: P04DF EVAP canister purge valve stuck OPEN

When there is no fluctuation of the FTP sensor: P04F1 purge flow NG

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0441 is judged as NG

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Wait for stability after the vehicle condition is turned to the OFF (LOCK) mode | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than 0.3 kPa (2 mmHg, 0.08 inHg) for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5604: DTC P0500 (K20C1) (2020 2021)

- Title: DTC P0500 (K20C1) (2020 2021)
- Source path: `pages\6753.html`
- Chunk ID: `chunk_e9f16cd8eefb`
- Images: none
- Duplicate sources: `pages\8340.html`, `pages\23144.html`, `pages\21557.html`

### Full Text

````text
# DTC P0500 (K20C1) (2020 2021)

DTC P0500: Vehicle Speed Sensor A No Signal

General Description

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the left front wheel speed sensor outputs less than a specified speed despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.4 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The left front wheel speed sensor outputs less than 1.94 mph (3.13 km/h) despite the other speed sensor's output of 1.94 mph (3.13 km/h) or more for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Left front wheel speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5605: DTC P0500 (K20C2) (2019 2020 2021)

- Title: DTC P0500 (K20C2) (2019 2020 2021)
- Source path: `pages\6754.html`
- Chunk ID: `chunk_80ca573dd105`
- Images: `images\GHH403136.jpeg`
- Duplicate sources: `pages\8341.html`, `pages\23145.html`, `pages\21558.html`

### Full Text

````text
# DTC P0500 (K20C2) (2019 2020 2021)

DTC P0500: Vehicle Speed Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the left front wheel speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The left front wheel speed sensor outputs 0 mph (0 km/h) despite the right front wheel speed sensor and output shaft (countershaft) speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Left front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5606: DTC P0500 (L15B7/L15BA) (2019 2020 2021)

- Title: DTC P0500 (L15B7/L15BA) (2019 2020 2021)
- Source path: `pages\6755.html`
- Chunk ID: `chunk_152710b60fd1`
- Images: `images\GHH403137.jpeg`
- Duplicate sources: `pages\8342.html`, `pages\23146.html`, `pages\21559.html`

### Full Text

````text
# DTC P0500 (L15B7/L15BA) (2019 2020 2021)

DTC P0500: Vehicle Speed Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the left front wheel speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The left front wheel speed sensor outputs 0 mph (0 km/h) despite the right front wheel speed sensor and output shaft (countershaft) speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Left front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5607: DTC P0501 (K20C1 (PGM-FI System)) (2017 2018 2019)

- Title: DTC P0501 (K20C1 (PGM-FI System)) (2017 2018 2019)
- Source path: `pages\6756.html`
- Chunk ID: `chunk_ed44912d1841`
- Images: none
- Duplicate sources: `pages\8343.html`, `pages\23147.html`, `pages\21560.html`

### Full Text

````text
# DTC P0501 (K20C1 (PGM-FI System)) (2017 2018 2019)

DTC P0501: Output Shaft Speed Sensor Circuit Out of Range High

General Description

The powertrain control module (PCM) monitors the output speed sensor for electrical malfunctions. If the output shaft speed sensor outputs a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The output shaft speed sensor output speed is greater than 203.6 mph (327.6 km/h) or 0 mph (0 km/h) or less for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5608: DTC P0501 (K20C1 (PGM-FI System)) (2019 2020 2021)

- Title: DTC P0501 (K20C1 (PGM-FI System)) (2019 2020 2021)
- Source path: `pages\6757.html`
- Chunk ID: `chunk_2743c960c9c8`
- Images: none
- Duplicate sources: `pages\8344.html`, `pages\23148.html`, `pages\21561.html`

### Full Text

````text
# DTC P0501 (K20C1 (PGM-FI System)) (2019 2020 2021)

DTC P0501: Output Shaft Speed Sensor Circuit Out of Range High

General Description

The powertrain control module (PCM) monitors the output speed sensor for electrical malfunctions. If the output shaft speed sensor outputs a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The output shaft speed sensor output speed is greater than 196 mph (315 km/h) or less than 0 mph (0 km/h) for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5609: DTC P0501 (K20C2) (2019 2020 2021)

- Title: DTC P0501 (K20C2) (2019 2020 2021)
- Source path: `pages\6758.html`
- Chunk ID: `chunk_7a8636d02082`
- Images: `images\GHH403138.jpeg`
- Duplicate sources: `pages\8345.html`, `pages\23149.html`, `pages\21562.html`

### Full Text

````text
# DTC P0501 (K20C2) (2019 2020 2021)

DTC P0501: Vehicle Speed Sensor A Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the wheel speed sensors to detect malfunctions. If the left front wheel speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The left front wheel speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Left front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5610: DTC P0501 (L15B7/L15BA) (2019 2020 2021)

- Title: DTC P0501 (L15B7/L15BA) (2019 2020 2021)
- Source path: `pages\6759.html`
- Chunk ID: `chunk_bad1d0cbadc1`
- Images: `images\GHH403139.jpeg`
- Duplicate sources: `pages\8346.html`, `pages\23150.html`, `pages\21563.html`

### Full Text

````text
# DTC P0501 (L15B7/L15BA) (2019 2020 2021)

DTC P0501: Vehicle Speed Sensor A Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the wheel speed sensors to detect malfunctions. If the left front wheel speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The left front wheel speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Left front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5611: DTC P0506 (K20C1) (2017 2018 2019)

- Title: DTC P0506 (K20C1) (2017 2018 2019)
- Source path: `pages\6760.html`
- Chunk ID: `chunk_f1f068f3901a`
- Images: `images\GHH403140.jpeg`
- Duplicate sources: `pages\8347.html`, `pages\23151.html`, `pages\21564.html`

### Full Text

````text
# DTC P0506 (K20C1) (2017 2018 2019)

DTC P0506: Idle Control System RPM Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 13.1 deg.F (-10.5 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -23.4 deg.F (-30.8 deg.C) | -

Engine speed [Engine Speed] | - | 4, 000 rpm

Other | Vehicle stopped

Engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The current idle speed is 100 rpm less than the set point idle speed for at least 0.5 second and the idle speed controller integrator is in maximum control range.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5612: DTC P0506 (K20C1) (2019)

- Title: DTC P0506 (K20C1) (2019)
- Source path: `pages\6761.html`
- Chunk ID: `chunk_dca5627d2b7b`
- Images: `images\GHH403141.jpeg`
- Duplicate sources: `pages\8348.html`, `pages\23152.html`, `pages\21565.html`

### Full Text

````text
# DTC P0506 (K20C1) (2019)

DTC P0506: Idle Control System RPM Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | Vehicle stopped

Malfunction Threshold

The set point idle speed minus the current idle speed is higher than 100 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5613: DTC P0506 (K20C1) (2020 2021)

- Title: DTC P0506 (K20C1) (2020 2021)
- Source path: `pages\6762.html`
- Chunk ID: `chunk_c57d36159573`
- Images: `images\GHH403142.jpeg`
- Duplicate sources: `pages\8349.html`, `pages\23153.html`, `pages\21566.html`

### Full Text

````text
# DTC P0506 (K20C1) (2020 2021)

DTC P0506: Idle Control System RPM Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | -4.5 deg.F (-20.3 deg.C) | 289.85 deg.F (143.25 deg.C)

Intake air temperature [IAT Sensor (1)] | -23.4 deg.F (-30.8 deg.C) | -

Other | Vehicle speed [Vehicle Speed] is at 0 mph (0 km/h)

[ ]: HDS Parameter

Malfunction Threshold

The set point idle speed minus the current idle speed is higher than 100 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5614: DTC P0506 (K20C2, KA/KC models)

- Title: DTC P0506 (K20C2, KA/KC models)
- Source path: `pages\6763.html`
- Chunk ID: `chunk_695e8a5bf9cd`
- Images: `images\GHH403143.jpeg`, `images\GHH403144.jpeg`
- Duplicate sources: `pages\8350.html`, `pages\23154.html`, `pages\21567.html`

### Full Text

````text
# DTC P0506 (K20C2, KA/KC models)

DTC P0506: Idle Control System RPM Lower than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A target idle speed that meets the engine operating conditions (coolant temperature, A/C ON or OFF, etc.) is stored in the powertrain control module (PCM). The PCM monitors and controls the idle speed so that the actual idle speed is equal to the target idle speed. If the actual idle speed varies beyond a specified value from the target speed over a certain period of time, the PCM detects a malfunction in the idle speed control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.69 | 1.47

Throttle position | Fully closed

Fuel feedback | Closed loop

Other | The engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The actual idle speed is 100 rpm less than the target idle speed for at least 20 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 20 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5615: DTC P0506 (L15B7/L15BA)

- Title: DTC P0506 (L15B7/L15BA)
- Source path: `pages\6764.html`
- Chunk ID: `chunk_91a2cdbf6dde`
- Images: `images\GHH403145.jpeg`, `images\GHH403146.jpeg`
- Duplicate sources: `pages\8351.html`, `pages\23155.html`, `pages\21568.html`

### Full Text

````text
# DTC P0506 (L15B7/L15BA)

DTC P0506: Idle Control System RPM Lower than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A target idle speed that meets the engine operating conditions (coolant temperature, A/C ON or OFF, etc.) is stored in the powertrain control module (PCM). The PCM monitors and controls the idle speed so that the actual idle speed is equal to the target idle speed. If the actual idle speed varies beyond a specified value from the target speed over a certain period of time, the PCM detects a malfunction in the idle speed control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Throttle position | Fully closed

Fuel feedback | Closed loop

Other | The engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The actual idle speed is 100 rpm less than the target idle speed for at least 20 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 20 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5616: DTC P0507 (K20C1) (2017 2018 2019)

- Title: DTC P0507 (K20C1) (2017 2018 2019)
- Source path: `pages\6765.html`
- Chunk ID: `chunk_94b97df0f694`
- Images: `images\GHH403147.jpeg`
- Duplicate sources: `pages\8352.html`, `pages\23156.html`, `pages\21569.html`

### Full Text

````text
# DTC P0507 (K20C1) (2017 2018 2019)

DTC P0507: Idle Control System RPM Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 13.1 deg.F (-10.5 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -23.4 deg.F (-30.8 deg.C) | -

Engine speed [Engine Speed] | - | 4, 000 rpm

Other | Vehicle stopped

Engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The current idle speed is 200 rpm greater than the set point idle speed for at least 0.5 second and the idle speed controller integrator is in minimum control range.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- Evaporative emission (EVAP) system air leak

- EVAP system failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5617: DTC P0507 (K20C1) (2019)

- Title: DTC P0507 (K20C1) (2019)
- Source path: `pages\6766.html`
- Chunk ID: `chunk_c517b761a165`
- Images: `images\GHH403148.jpeg`
- Duplicate sources: `pages\8353.html`, `pages\23157.html`, `pages\21570.html`

### Full Text

````text
# DTC P0507 (K20C1) (2019)

DTC P0507: Idle Control System RPM Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | Vehicle stopped

Malfunction Threshold

The set point idle speed minus the current idle speed is less than -200 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- Evaporative emission (EVAP) system air leak

- EVAP system failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5618: DTC P0507 (K20C1) (2020 2021)

- Title: DTC P0507 (K20C1) (2020 2021)
- Source path: `pages\6767.html`
- Chunk ID: `chunk_ce352816a38a`
- Images: `images\GHH403149.jpeg`
- Duplicate sources: `pages\8354.html`, `pages\23158.html`, `pages\21571.html`

### Full Text

````text
# DTC P0507 (K20C1) (2020 2021)

DTC P0507: Idle Control System RPM Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | -4.5 deg.F (-20.3 deg.C) | 289.85 deg.F (143.25 deg.C)

Intake air temperature [IAT Sensor (1)] | -23.4 deg.F (-30.8 deg.C) | -

Other | Vehicle speed [Vehicle Speed] is at 0 mph (0 km/h)

[ ]: HDS Parameter

Malfunction Threshold

The set point idle speed minus the current idle speed is less than -200 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

- Evaporative emission (EVAP) system air leak

- EVAP system failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for a while.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5619: DTC P0507 (K20C2)

- Title: DTC P0507 (K20C2)
- Source path: `pages\6768.html`
- Chunk ID: `chunk_6619c262b580`
- Images: `images\GHH403150.jpeg`, `images\GHH403151.jpeg`
- Duplicate sources: `pages\8355.html`, `pages\22861.html`, `pages\21274.html`

### Full Text

````text
# DTC P0507 (K20C2)

DTC P0507: Idle Control System RPM Higher than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A target idle speed that meets the engine operating conditions (coolant temperature, A/C ON or OFF, etc.) is stored in the powertrain control module (PCM). The PCM monitors and controls the idle speed so that the actual idle speed is equal to the target idle speed. If the actual idle speed varies beyond a specified value from the target speed over a certain period of time, the PCM detects a malfunction in the idle speed control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.69 | 1.47

Throttle position | Fully closed

Fuel feedback | Closed loop

Other | The engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The actual idle speed is 200 rpm greater than the target idle speed for at least 20 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 20 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5620: DTC P0507 (Without XM)

- Title: DTC P0507 (Without XM)
- Source path: `pages\6769.html`
- Chunk ID: `chunk_9b51870cf346`
- Images: `images\GHH403152.jpeg`, `images\GHH403153.jpeg`
- Duplicate sources: `pages\8356.html`, `pages\22862.html`, `pages\21275.html`

### Full Text

````text
# DTC P0507 (Without XM)

DTC P0507: Idle Control System RPM Higher than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A target idle speed that meets the engine operating conditions (coolant temperature, A/C ON or OFF, etc.) is stored in the powertrain control module (PCM). The PCM monitors and controls the idle speed so that the actual idle speed is equal to the target idle speed. If the actual idle speed varies beyond a specified value from the target speed over a certain period of time, the PCM detects a malfunction in the idle speed control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Throttle position | Fully closed

Fuel feedback | Closed loop

Other | The engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

The actual idle speed is 200 rpm greater than the target idle speed for at least 20 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body air leak

- Intake manifold air leak

- Intake air system air leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 20 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5621: DTC P050A (K20C1) (2017 2018 2019)

- Title: DTC P050A (K20C1) (2017 2018 2019)
- Source path: `pages\6770.html`
- Chunk ID: `chunk_a21ab749bf05`
- Images: `images\GHH403154.jpeg`
- Duplicate sources: `pages\8357.html`, `pages\22863.html`, `pages\21276.html`

### Full Text

````text
# DTC P050A (K20C1) (2017 2018 2019)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs during catalyst heating, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | - | 4, 000 rpm

Other | Catalyst heating is active

Vehicle stopped

Engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs:

- The current idle speed is 100 rpm less than the set point idle speed for at least 0.5 second during catalyst heating and the idle speed controller integrator is in maximum control range.

- The current idle speed is 200 rpm greater than the set point idle speed for at least 0.5 second during catalyst heating and the idle speed controller integrator is in minimum control range.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Throttle body failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5622: DTC P050A (K20C1) (2019 2020 2021)

- Title: DTC P050A (K20C1) (2019 2020 2021)
- Source path: `pages\6771.html`
- Chunk ID: `chunk_1de9c08b7357`
- Images: `images\GHH403155.jpeg`
- Duplicate sources: `pages\8358.html`, `pages\22864.html`, `pages\21277.html`

### Full Text

````text
# DTC P050A (K20C1) (2019 2020 2021)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The idle speed control system matches desired and current engine idle speed. Therefore, an integral action controller is used. In case of a permanent difference between desired and current engine idle speed, the diagnosis checks if this difference is out of a calibrated range with the integral action controller. If current engine speed deviation occurs during catalyst heating, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | -4.5 deg.F (-20.3 deg.C) | 179.2 deg.F (81.8 deg.C)

Difference of desired idle speed during catalyst heating and idle speed setpoint without catalyst heating | -1 rpm | -

Other | Catalyst heating is active

Vehicle stopped

Engine is under no load

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs:

- The deviation of idle speed (set point minus current engine speed) is more than 100 rpm.

- The deviation of idle speed (set point minus current engine speed) is less than -200 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Throttle body failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5623: DTC P050A (K20C2) (2019 2020 2021)

- Title: DTC P050A (K20C2) (2019 2020 2021)
- Source path: `pages\6772.html`
- Chunk ID: `chunk_f82878c8a6aa`
- Images: `images\GHH403156.jpeg`, `images\GHH403157.jpeg`
- Duplicate sources: `pages\8359.html`, `pages\22865.html`, `pages\21278.html`

### Full Text

````text
# DTC P050A (K20C2) (2019 2020 2021)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual amount of air is less than the target amount, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 20 seconds

Engine coolant temperature [ECT SENSOR 1] | 32 deg.F (0 deg.C) | 140 deg.F (60 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The total airflow is decreased by a factor of 0.4 for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Intake air temperature (IAT) sensor failure

- Engine coolant temperature (ECT) sensor 1 failure

- Ignition system failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 140 deg.F (60 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5624: DTC P050A (K20C2, USA/Canada models) (2016 2017 2018)

- Title: DTC P050A (K20C2, USA/Canada models) (2016 2017 2018)
- Source path: `pages\6773.html`
- Chunk ID: `chunk_3edcd6566cc1`
- Images: `images\GHH403158.jpeg`, `images\GHH403159.jpeg`
- Duplicate sources: `pages\8360.html`, `pages\22866.html`, `pages\21279.html`

### Full Text

````text
# DTC P050A (K20C2, USA/Canada models) (2016 2017 2018)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual amount of air is less than the target amount, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 20 seconds

Engine coolant temperature [ECT SENSOR 1] | 32 deg.F (0 deg.C) | 140 deg.F (60 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The total airflow is decreased by a factor of 0.552 for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Intake air temperature (IAT) sensor failure

- Engine coolant temperature (ECT) sensor 1 failure

- Ignition system failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 140 deg.F (60 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5625: DTC P050A (L15B7/L15BA/L15BY) (2019)

- Title: DTC P050A (L15B7/L15BA/L15BY) (2019)
- Source path: `pages\6774.html`
- Chunk ID: `chunk_782780c90924`
- Images: `images\GHH403160.jpeg`, `images\GHH403161.jpeg`
- Duplicate sources: `pages\8361.html`, `pages\22867.html`, `pages\21280.html`

### Full Text

````text
# DTC P050A (L15B7/L15BA/L15BY) (2019)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual amount of air is less than the target amount, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The total airflow is decreased by a factor of 0.42* 1 (0.56)* 2 for at least 10 seconds.

*1: L15B7 (except Si)

*2: Si, L15BA, L15BY

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Intake air temperature (IAT) sensor 1 failure

- Engine coolant temperature (ECT) sensor 1 failure

- Ignition system failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5626: DTC P050A (L15B7/L15BY) (2020 2021)

- Title: DTC P050A (L15B7/L15BY) (2020 2021)
- Source path: `pages\6775.html`
- Chunk ID: `chunk_56d508232a0d`
- Images: `images\GHH403162.jpeg`, `images\GHH403163.jpeg`
- Duplicate sources: `pages\8362.html`, `pages\22868.html`, `pages\21281.html`

### Full Text

````text
# DTC P050A (L15B7/L15BY) (2020 2021)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual amount of air is less than the target amount, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The total airflow is decreased by a factor of 0.42* 1 (0.39)* 2 for at least 10 seconds.

*1: L15B7 (except Si)

*2: Si

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Intake air temperature (IAT) sensor 1 failure

- Engine coolant temperature (ECT) sensor 1 failure

- Ignition system failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5627: DTC P050A (L15BA) (2020 2021)

- Title: DTC P050A (L15BA) (2020 2021)
- Source path: `pages\6776.html`
- Chunk ID: `chunk_6ed226e16af5`
- Images: `images\GHH403164.jpeg`, `images\GHH403165.jpeg`, `images\GHH403166.jpeg`
- Duplicate sources: `pages\8363.html`, `pages\22869.html`, `pages\21282.html`

### Full Text

````text
# DTC P050A (L15BA) (2020 2021)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm system increases air flow and retards ignition timing to accelerate the warm-up of the catalyst on cold engine start. If the actual air flow is insufficient or excessive compared to the target air flow, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle valve | Fully closed

Accelerator pedal position | Released

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The ratio of integrated air flow difference between actual and target by integrated target air flow is 0.44* 1 (0.39)* 2 or more, or -0.44 or less.

*1: CVT*2: M/T

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Throttle body clogged

- Intake air system clogged

- Mass airflow (MAF) sensor failure

- Intake air temperature (IAT) sensor failure

- Engine coolant temperature (ECT) sensor 1 failure

- Air fuel ratio too rich

- Air fuel ratio too lean

- Ignition system failure

Confirmation Procedure

Operating Condition

- Leave the vehicle until the engine coolant temperature [ECT SENSOR 1] lowers to 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5628: DTC P050A (Without XM) (2016 2017 2018)

- Title: DTC P050A (Without XM) (2016 2017 2018)
- Source path: `pages\6777.html`
- Chunk ID: `chunk_8173d6091658`
- Images: `images\GHH403167.jpeg`, `images\GHH403168.jpeg`
- Duplicate sources: `pages\8364.html`, `pages\22870.html`, `pages\21283.html`

### Full Text

````text
# DTC P050A (Without XM) (2016 2017 2018)

DTC P050A: Cold Start Idle Air Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual amount of air is less than the target amount, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The total airflow is decreased by a factor of 0.56 for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

- Intake air system clogged

- Intake air temperature (IAT) sensor 1 failure

- Engine coolant temperature (ECT) sensor 1 failure

- Ignition system failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5629: DTC P050B (K20C1) (2017 2018)

- Title: DTC P050B (K20C1) (2017 2018)
- Source path: `pages\6778.html`
- Chunk ID: `chunk_3187a669e366`
- Images: none
- Duplicate sources: `pages\8365.html`, `pages\22871.html`, `pages\21284.html`

### Full Text

````text
# DTC P050B (K20C1) (2017 2018)

DTC P050B: Cold Start Ignition Timing Control System Performance Problem

General Description

The powertrain control module (PCM) monitors the ignition timing during the catalyst heating. To increase the energy within the exhaust system, the ignition timing must be shifted to retard. The task of the diagnosis function is to monitor the retard of the ignition timing. If the deviation of actual ignition efficiency comparing to the desired catalyst heating ignition efficiency is a specified value for a specified time during catalyst heating, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | - | 400 rpm

Charging efficiency | - | 49.992 %

Other | Catalyst heating is active

Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The deviation of actual ignition efficiency comparing to the desired catalyst heating ignition efficiency is greater than 0.5 for at least 5 seconds during catalyst heating.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition timing incorrect

- Injection timing incorrect

- Ignition coil failure

- Injector failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5630: DTC P050B (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P050B (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\6779.html`
- Chunk ID: `chunk_7a01688d1a21`
- Images: `images\GHH403169.jpeg`, `images\GHH403170.jpeg`, `images\GHH403171.jpeg`
- Duplicate sources: `pages\8366.html`, `pages\22872.html`, `pages\21285.html`

### Full Text

````text
# DTC P050B (L15B7/L15BA/L15BY) (2020 2021)

DTC P050B: Cold Start Ignition Timing Control System Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm system increases air flow and retards ignition timing to accelerate the warm-up of the catalyst on cold engine start. If the ignition timing is excessively advanced, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration* 1 | 6.0 seconds or more

Duration* 2 | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

*1: CVT

*2: M/T

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Fuel feedback | Closed loop

Throttle valve | Fully closed

Accelerator pedal position | Released

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The ignition timing is excessively advanced.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Throttle body clogged

- Intake air system clogged

- Mass airflow (MAF) sensor failure

- Intake air temperature (IAT) sensor failure

- Engine coolant temperature (ECT) sensor 1 failure

- Air fuel ratio too rich

- Air fuel ratio too lean

- Ignition system failure

Confirmation Procedure

Operating Condition

- Leave the vehicle until the engine coolant temperature [ECT SENSOR 1] lowers to 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 6 seconds* 1 (5 seconds)* 2.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5631: DTC P050D (K20C1) (2019 2020 2021)

- Title: DTC P050D (K20C1) (2019 2020 2021)
- Source path: `pages\6780.html`
- Chunk ID: `chunk_d065dbee71f2`
- Images: none
- Duplicate sources: `pages\8367.html`, `pages\22873.html`, `pages\21286.html`

### Full Text

````text
# DTC P050D (K20C1) (2019 2020 2021)

DTC P050D: Cold Start Ignition Timing Control System Performance Problem

General Description

The powertrain control module (PCM) monitors the ignition timing during the catalyst heating. To increase the energy within the exhaust system, the ignition timing must be shifted to retard. The task of the diagnosis function is to monitor the retard of the ignition timing. If the deviation of actual ignition efficiency comparing to the desired catalyst heating ignition efficiency is a specified value for a specified time during catalyst heating, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Absolute difference of current and filtered engine speed | - | 400 rpm

Charging efficiency | - | 49.992 %

Other | Catalyst heating is active

Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The deviation of actual ignition efficiency comparing to the desired catalyst heating ignition efficiency is greater than 0.2 for at least 5 seconds during catalyst heating.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition timing incorrect

- Injection timing incorrect

- Ignition coil failure

- Injector failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5632: DTC P050D (K20C2) (2019 2020 2021)

- Title: DTC P050D (K20C2) (2019 2020 2021)
- Source path: `pages\6781.html`
- Chunk ID: `chunk_bfa6eb397866`
- Images: `images\GHH403172.jpeg`, `images\GHH403173.jpeg`
- Duplicate sources: `pages\8368.html`, `pages\22874.html`, `pages\21287.html`

### Full Text

````text
# DTC P050D (K20C2) (2019 2020 2021)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual engine speed is a specified fast idle value, and it continues for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.5 seconds | -

Duration of quick warm-up system operation after engine start-up | - | 20 seconds

Engine coolant temperature [ECT SENSOR 1] | 32 deg.F (0 deg.C) | 140 deg.F (60 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The engine speed [ENGINE SPEED] is 2, 200 rpm or more for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 140 deg.F (60 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5633: DTC P050D (K20C2, USA/Canada models) (2016 2017 2018)

- Title: DTC P050D (K20C2, USA/Canada models) (2016 2017 2018)
- Source path: `pages\6782.html`
- Chunk ID: `chunk_218e9e0af2fc`
- Images: `images\GHH403174.jpeg`, `images\GHH403175.jpeg`
- Duplicate sources: `pages\8369.html`, `pages\22875.html`, `pages\21288.html`

### Full Text

````text
# DTC P050D (K20C2, USA/Canada models) (2016 2017 2018)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual engine speed is a specified fast idle value, and it continues for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.5 seconds | -

Duration of quick warm-up system operation after engine start-up | - | 20 seconds

Engine coolant temperature [ECT SENSOR 1] | 32 deg.F (0 deg.C) | 140 deg.F (60 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The engine speed [ENGINE SPEED] is 2, 400 rpm or more for at least 3.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 140 deg.F (60 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5634: DTC P050D (L15B7/L15BA) (2016 2017 2018)

- Title: DTC P050D (L15B7/L15BA) (2016 2017 2018)
- Source path: `pages\6783.html`
- Chunk ID: `chunk_95cdac2964e2`
- Images: `images\GHH403176.jpeg`, `images\GHH403177.jpeg`
- Duplicate sources: `pages\8370.html`, `pages\22876.html`, `pages\21289.html`

### Full Text

````text
# DTC P050D (L15B7/L15BA) (2016 2017 2018)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual engine speed is a specified fast idle value, and it continues for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.5 seconds | -

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The engine speed [ENGINE SPEED] is 2, 400 rpm or more for at least 3.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5635: DTC P050D (L15B7/L15BA/L15BY) (2019)

- Title: DTC P050D (L15B7/L15BA/L15BY) (2019)
- Source path: `pages\6784.html`
- Chunk ID: `chunk_94f30270ad17`
- Images: `images\GHH403178.jpeg`, `images\GHH403179.jpeg`
- Duplicate sources: `pages\8371.html`, `pages\22877.html`, `pages\21290.html`

### Full Text

````text
# DTC P050D (L15B7/L15BA/L15BY) (2019)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual engine speed is a specified fast idle value, and it continues for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

*1: L15B7 (except Si)

*2: Si, L15BA, L15BY

Duration* 1 | 5.0 seconds or more

Duration* 2 | 3.5 seconds or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si)

*2: Si, L15BA, L15BY

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.5 seconds | -

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The engine speed [ENGINE SPEED] is 2, 300 rpm* 1 (2, 400 rpm)* 2 or more for at least 5.0 seconds* 1 (3.5 seconds)* 2.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5636: DTC P050D (L15B7/L15BY) (2020 2021)

- Title: DTC P050D (L15B7/L15BY) (2020 2021)
- Source path: `pages\6785.html`
- Chunk ID: `chunk_e8eacc63883e`
- Images: `images\GHH403180.jpeg`, `images\GHH403181.jpeg`
- Duplicate sources: `pages\8372.html`, `pages\22878.html`, `pages\21291.html`

### Full Text

````text
# DTC P050D (L15B7/L15BY) (2020 2021)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm-up system supplies additional air and retards the ignition timing when the engine is cold to activate the catalytic converter as quickly as possible. When the actual engine speed is a specified fast idle value, and it continues for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

*1: L15B7 (except Si)

*2: Si

Duration* 1 | 5.0 seconds or more

Duration* 2 | 3.5 seconds or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si)

*2: Si

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.5 seconds | -

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle position | Fully closed

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The engine speed [ENGINE SPEED] is 2, 300 rpm* 1 (2, 200 rpm)* 2 or more for at least 5.0 seconds* 1 (3.5 seconds)* 2.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Mass airflow (MAF) sensor failure

Confirmation Procedure

Operating Condition

- Allow the engine to cool to an ambient engine coolant temperature [ECT SENSOR 1] of 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5637: DTC P050D (L15BA) (2020 2021)

- Title: DTC P050D (L15BA) (2020 2021)
- Source path: `pages\6786.html`
- Chunk ID: `chunk_c4b02df5eefc`
- Images: `images\GHH403182.jpeg`, `images\GHH403183.jpeg`, `images\GHH403184.jpeg`
- Duplicate sources: `pages\8373.html`, `pages\22879.html`, `pages\21292.html`

### Full Text

````text
# DTC P050D (L15BA) (2020 2021)

DTC P050D: Cold Start Idle Speed Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The quick warm system increases air flow and retards ignition timing to accelerate the warm-up of the catalyst on cold engine start. If the actual engine speed is insufficient or excessive compared to the target engine speed, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Duration of quick warm-up system operation after engine start-up | - | 40 seconds

Engine coolant temperature [ECT SENSOR 1] | 50 deg.F (10 deg.C) | 122 deg.F (50 deg.C)

Throttle valve | Fully closed

Accelerator pedal position | Released

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The average of difference between the actual engine speed and the target engine speed is 700 rpm or more, or -650 rpm or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake air duct breakage

- Intake air duct misinstalled

- Air cleaner breakage

- Air cleaner damage

- Air cleaner clogged

- Throttle body clogged

- Intake air system clogged

- Mass airflow (MAF) sensor failure

- Intake air temperature (IAT) sensor failure

- Engine coolant temperature (ECT) sensor 1 failure

- Air fuel ratio too rich

- Air fuel ratio too lean

- Ignition system failure

Confirmation Procedure

Operating Condition

- Leave the vehicle until the engine coolant temperature [ECT SENSOR 1] lowers to 122 deg.F (50 deg.C) or less.

- Start the engine, and let it idle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5638: DTC P0522, P0523 (K20C1) (2017 2018 2019)

- Title: DTC P0522, P0523 (K20C1) (2017 2018 2019)
- Source path: `pages\6787.html`
- Chunk ID: `chunk_f715108d3713`
- Images: `images\GHH403185.jpeg`
- Duplicate sources: `pages\8374.html`, `pages\22880.html`, `pages\21293.html`

### Full Text

````text
# DTC P0522, P0523 (K20C1) (2017 2018 2019)

DTC P0522: Rocker Arm Oil Pressure Sensor Circuit Low Voltage

DTC P0523: Rocker Arm Oil Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The rocker arm oil pressure sensor detects engine oil pressure in the system. When the voltage from the rocker arm oil pressure sensor is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0522

The rocker arm oil pressure sensor output voltage [Rocker Arm Oil Pressure Sensor] is under 0 V for at least 0.5 second.

DTC: P0523

The rocker arm oil pressure sensor output voltage [Rocker Arm Oil Pressure Sensor] is over 5 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0522

- Rocker arm oil pressure sensor OPSEN line short to ground

- Rocker arm oil pressure sensor VCC line open

DTC: P0523

- Rocker arm oil pressure sensor OPSEN line open

- Rocker arm oil pressure sensor SG line open

Common

- Rocker arm oil pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5639: DTC P0522, P0523 (K20C1) (2019 2020 2021)

- Title: DTC P0522, P0523 (K20C1) (2019 2020 2021)
- Source path: `pages\6788.html`
- Chunk ID: `chunk_39da09b1e6c2`
- Images: `images\GHH403186.jpeg`
- Duplicate sources: `pages\8375.html`, `pages\22881.html`, `pages\21294.html`

### Full Text

````text
# DTC P0522, P0523 (K20C1) (2019 2020 2021)

DTC P0522: Rocker Arm Oil Pressure Sensor Circuit Low Voltage

DTC P0523: Rocker Arm Oil Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The rocker arm oil pressure sensor detects engine oil pressure in the system. When the voltage from the rocker arm oil pressure sensor is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0522

The rocker arm oil pressure sensor output voltage [Rocker Arm Oil Pressure Sensor] is less than 0.24 V for at least 0.5 second.

DTC: P0523

The rocker arm oil pressure sensor output voltage [Rocker Arm Oil Pressure Sensor] is more than 4.73 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0522

- Rocker arm oil pressure sensor OPSEN line short to ground

- Rocker arm oil pressure sensor VCC line open

DTC: P0523

- Rocker arm oil pressure sensor OPSEN line open

- Rocker arm oil pressure sensor SG line open

Common

- Rocker arm oil pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5640: DTC P0532, P0533 (K20C1) (2017 2018 2019)

- Title: DTC P0532, P0533 (K20C1) (2017 2018 2019)
- Source path: `pages\6789.html`
- Chunk ID: `chunk_32567470a3f0`
- Images: `images\GHH403187.jpeg`
- Duplicate sources: `pages\8376.html`, `pages\22882.html`, `pages\21295.html`

### Full Text

````text
# DTC P0532, P0533 (K20C1) (2017 2018 2019)

DTC P0532: A/C Pressure Sensor Circuit Low Voltage

DTC P0533: A/C Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the A/C pressure sensor. The A/C refrigerant pressure is read from the A/C pressure sensor through the analog digital (A/D) converter. This is a value corresponding to the physical value of the pressure. The signal is transformed into a physical value by a transformation curve. If the A/C pressure sensor output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Outside air temperature | -40.07 deg.F (-40.04 deg.C) | -

State of the engine | Running

Malfunction Threshold

DTC: P0532

The A/C pressure sensor output voltage [A/C Pressure Sensor] is less than 0.142 V for at least 0.5 second.

DTC: P0533

The A/C pressure sensor output voltage [A/C Pressure Sensor] is greater than 4.845 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0532

- A/C pressure sensor PD SENSOR line short to ground

- A/C pressure sensor VCC line open

DTC: P0533

- Rocker arm oil pressure sensor PD SENSOR line open

- Rocker arm oil pressure sensor SG line open

Common

- A/C pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5641: DTC P0532, P0533 (K20C1) (2019 2020 2021)

- Title: DTC P0532, P0533 (K20C1) (2019 2020 2021)
- Source path: `pages\6790.html`
- Chunk ID: `chunk_eb106800776d`
- Images: `images\GHH403188.jpeg`
- Duplicate sources: `pages\8377.html`, `pages\22883.html`, `pages\21296.html`

### Full Text

````text
# DTC P0532, P0533 (K20C1) (2019 2020 2021)

DTC P0532: A/C Pressure Sensor Circuit Low Voltage

DTC P0533: A/C Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the A/C pressure sensor. The A/C refrigerant pressure is read from the A/C pressure sensor through the analog digital (A/D) converter. This is a value corresponding to the physical value of the pressure. The signal is transformed into a physical value by a transformation curve. If the A/C pressure sensor output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Outside air temperature | -40.07 deg.F (-40.04 deg.C) | -

State of the engine | Running

Malfunction Threshold

DTC: P0532

The A/C pressure sensor output voltage [A/C Pressure Sensor] is less than 0.14 V for at least 0.5 second.

DTC: P0533

The A/C pressure sensor output voltage [A/C Pressure Sensor] is greater than 4.85 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0532

- A/C pressure sensor PD SENSOR line short to ground

- A/C pressure sensor VCC line open

DTC: P0533

- Rocker arm oil pressure sensor PD SENSOR line open

- Rocker arm oil pressure sensor SG line open

Common

- A/C pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5642: DTC P0532, P0533 (K20C2)

- Title: DTC P0532, P0533 (K20C2)
- Source path: `pages\6791.html`
- Chunk ID: `chunk_73042df002dd`
- Images: `images\GHH403189.jpeg`, `images\GHH403190.jpeg`
- Duplicate sources: `pages\8378.html`, `pages\22884.html`, `pages\21297.html`

### Full Text

````text
# DTC P0532, P0533 (K20C2)

DTC P0532: A/C Pressure Sensor Circuit Low Voltage

DTC P0533: A/C Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The A/C pressure sensor measures the change in the pressure of the air conditioning refrigerant. The signal from the A/C pressure sensor is low voltage at low pressure (when the air conditioning load is low) and high voltage at high pressure (when the air conditioning load is high). The powertrain control module (PCM) compares the expected voltage to the A/C pressure sensor output voltage. When the A/C pressure sensor output voltage is lower or higher than the expected voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0532

The A/C pressure sensor output voltage [A/C PRESSURE SENSOR] is 0.24 V or less for at least 10 seconds.

DTC: P0533

The A/C pressure sensor output voltage [A/C PRESSURE SENSOR] is 4.76 V or more for at least 10 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0532

- A/C pressure sensor PD SENSOR line short to ground

- A/C pressure sensor VCC line open

DTC: P0533

- A/C pressure sensor PD SENSOR line open

- A/C pressure sensor SG line open

Common

- A/C pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5643: DTC P0532, P0533 (L15B7/L15BA/L15BY)

- Title: DTC P0532, P0533 (L15B7/L15BA/L15BY)
- Source path: `pages\6792.html`
- Chunk ID: `chunk_1d6cdc09561c`
- Images: `images\GHH403191.jpeg`, `images\GHH403192.jpeg`
- Duplicate sources: `pages\8379.html`, `pages\22885.html`, `pages\21298.html`

### Full Text

````text
# DTC P0532, P0533 (L15B7/L15BA/L15BY)

DTC P0532: A/C Pressure Sensor Circuit Low Voltage

DTC P0533: A/C Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The A/C pressure sensor measures the change in the pressure of the air conditioning refrigerant. The signal from the A/C pressure sensor is low voltage at low pressure (when the air conditioning load is low) and high voltage at high pressure (when the air conditioning load is high). The powertrain control module (PCM) compares the expected voltage to the A/C pressure sensor output voltage. When the A/C pressure sensor output voltage is lower or higher than the expected voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0532

The A/C pressure sensor output voltage [A/C PRESSURE SENSOR] is 0.24 V or less for at least 10 seconds.

DTC: P0533

The A/C pressure sensor output voltage [A/C PRESSURE SENSOR] is 4.76 V or more for at least 10 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0532

- A/C pressure sensor PD SENSOR line short to ground

- A/C pressure sensor VCC line open

DTC: P0533

- A/C pressure sensor PD SENSOR line open

- A/C pressure sensor SG line open

Common

- A/C pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5644: DTC P053F (K20C1) (2017 2018 2019)

- Title: DTC P053F (K20C1) (2017 2018 2019)
- Source path: `pages\6793.html`
- Chunk ID: `chunk_0521a2e4e663`
- Images: `images\GHH403193.jpeg`
- Duplicate sources: `pages\8380.html`, `pages\22886.html`, `pages\21299.html`

### Full Text

````text
# DTC P053F (K20C1) (2017 2018 2019)

DTC P053F: Fuel Rail Pressure Performance

General Description

Courtesy of HONDA, U.S.A., INC.

The high pressure fuel system consists of a fuel rail, a fuel rail pressure sensor, a high pressure fuel pump with a built-in fuel control solenoid. In dependence of torque demand and engine speed, high pressure has to be adjusted. Therefore the fuel pressure in the rail is measured and controlled with help of the fuel control solenoid. If the difference between the desired and measured fuel rail pressure is too large, combustion and emissions can be influenced. The powertrain control module (PCM) monitors the high pressure fuel control system. The diagnosis checks the plausibility of the high pressure controller output if the activation of the fuel control solenoid extremely deviates from the pre-control. If the pressure deviation at controller output is a specified value during catalyst heating is active, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 3 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Relative fuel mass quantity | 5.016 % | 190.031 - 250.031 %

Other | Catalyst heating is active

Fuel rail pressure control is active

Malfunction Threshold

Either of the conditions occurs for at least 3 seconds:

- The positive pressure deviation at controller output is greater than 1, 500 kPa (15.30 kgf/cm 2, 217.6 psi) during catalyst heating.

- The negative pressure deviation at controller output is less than -1, 500 MPa (-15.30 kgf/cm 2, -217.6 psi) during catalyst heating.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- High pressure fuel pump failure (pressure relief valve defection)

- Fuel pump low flow

- High pressure fuel pipe leakage

- Fuel injector contamination

- Fuel rail pressure sensor drifting

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5645: DTC P053F (K20C1) (2019 2020 2021)

- Title: DTC P053F (K20C1) (2019 2020 2021)
- Source path: `pages\6794.html`
- Chunk ID: `chunk_c6612bd4a08f`
- Images: `images\GHH403194.jpeg`
- Duplicate sources: `pages\8381.html`, `pages\22887.html`, `pages\21300.html`

### Full Text

````text
# DTC P053F (K20C1) (2019 2020 2021)

DTC P053F: Fuel Rail Pressure Performance

General Description

Courtesy of HONDA, U.S.A., INC.

The high pressure fuel system consists of a fuel rail, a fuel rail pressure sensor, a high pressure fuel pump with a built-in fuel control solenoid. In dependence of torque demand and engine speed, high pressure has to be adjusted. Therefore the fuel pressure in the rail is measured and controlled with help of the fuel control solenoid. If the difference between the desired and measured fuel rail pressure is too large, combustion and emissions can be influenced. The powertrain control module (PCM) monitors the high pressure fuel control system. The diagnosis checks the plausibility of the high pressure controller output if the activation of the fuel control solenoid extremely deviates from the pre-control. If the pressure deviation at controller output is a specified value during catalyst heating is active, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 3 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2 seconds | -

Relative fuel mass quantity | 5.02 % | 320.02 %

Other | Catalyst heating is active

Catalyst heating request by cold engine

High pressure regulation flag is switched on

Malfunction Threshold

Either of the conditions occurs for at least 3 seconds:

- The positive pressure deviation at controller output is greater than 1, 500 kPa (15.30 kgf/cm 2, 217.6 psi) during catalyst heating.

- The negative pressure deviation at controller output is less than -1, 500 kPa (-15.30 kgf/cm 2, -217.6 psi) during catalyst heating.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- High pressure fuel pump failure (pressure relief valve defection)

- Fuel pump low flow

- High pressure fuel pipe leakage

- Fuel injector contamination

- Fuel rail pressure sensor drifting

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5646: DTC P0560 (K20C1) (2017 2018 2019)

- Title: DTC P0560 (K20C1) (2017 2018 2019)
- Source path: `pages\6795.html`
- Chunk ID: `chunk_67aab238bbd0`
- Images: `images\GHH403195.jpeg`
- Duplicate sources: `pages\8382.html`, `pages\22888.html`, `pages\21301.html`

### Full Text

````text
# DTC P0560 (K20C1) (2017 2018 2019)

DTC P0560: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors permanent power supply line of the PCM. If the permanent power supply line for the PCM is interrupted for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The power supply for the PCM is interrupted for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM +B BACKUP FI-ECU line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5647: DTC P0560 (K20C1) (2019 2020 2021)

- Title: DTC P0560 (K20C1) (2019 2020 2021)
- Source path: `pages\6796.html`
- Chunk ID: `chunk_240f26eb2b6f`
- Images: `images\GHH403196.jpeg`
- Duplicate sources: `pages\8383.html`, `pages\22889.html`, `pages\21302.html`

### Full Text

````text
# DTC P0560 (K20C1) (2019 2020 2021)

DTC P0560: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the standby power supply line of the PCM for open circuit. The diagnosis works only once in every initialization of the PCM. If there is an interruption in the power supply line, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The power supply for the PCM is interrupted.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit FI MAIN RLY OUT line short to ground

- PGM-FI main relay 1 circuit FI MAIN RLY OUT line open

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line open

- Loss of energy

- Fuse blown

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5648: DTC P0562 (K20C1) (2017 2018 2019)

- Title: DTC P0562 (K20C1) (2017 2018 2019)
- Source path: `pages\6797.html`
- Chunk ID: `chunk_4aeaafbe6692`
- Images: `images\GHH403197.jpeg`
- Duplicate sources: `pages\8384.html`, `pages\22890.html`, `pages\21303.html`

### Full Text

````text
# DTC P0562 (K20C1) (2017 2018 2019)

DTC P0562: Charging System Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. If the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 11 V or less for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil open, stator coil open, regulator failure)

- Alternator poor or loose connection

- Alternator side B terminal disconnection

- Battery terminal fuse box side B terminal disconnection

- 12 volt battery voltage low

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5649: DTC P0562 (K20C1) (2019 2020 2021)

- Title: DTC P0562 (K20C1) (2019 2020 2021)
- Source path: `pages\6798.html`
- Chunk ID: `chunk_7797bd5800cf`
- Images: `images\GHH403198.jpeg`
- Duplicate sources: `pages\8385.html`, `pages\22891.html`, `pages\21304.html`

### Full Text

````text
# DTC P0562 (K20C1) (2019 2020 2021)

DTC P0562: Charging System Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. If the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is less than 11 V for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil open, stator coil open, voltage regulator failure)

- Alternator poor or loose connection

- Alternator side B terminal disconnection

- Battery terminal fuse box side B terminal disconnection

- 12 volt battery voltage low

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5650: DTC P0562 (K20C2)

- Title: DTC P0562 (K20C2)
- Source path: `pages\6799.html`
- Chunk ID: `chunk_1467552ab6e0`
- Images: `images\GHH403199.jpeg`
- Duplicate sources: `pages\8386.html`, `pages\22892.html`, `pages\21305.html`

### Full Text

````text
# DTC P0562 (K20C2)

DTC P0562: Charging System Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. If the FI MAIN RLY OUT terminal voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 11.0 V or less for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil open, stator coil open, regulator failure)

- Alternator stopped by over temperature

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5651: DTC P0562 (L15B7/L15BA/L15BY)

- Title: DTC P0562 (L15B7/L15BA/L15BY)
- Source path: `pages\6800.html`
- Chunk ID: `chunk_9624920ea670`
- Images: `images\GHH403200.jpeg`
- Duplicate sources: `pages\8387.html`, `pages\22893.html`, `pages\21306.html`

### Full Text

````text
# DTC P0562 (L15B7/L15BA/L15BY)

DTC P0562: Charging System Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. If the FI MAIN RLY OUT terminal voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 11.0 V or less for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil open, stator coil open, regulator failure)

- Alternator stopped by over temperature

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5652: DTC P0563 (K20C2)

- Title: DTC P0563 (K20C2)
- Source path: `pages\6801.html`
- Chunk ID: `chunk_4e5109fa40c7`
- Images: `images\GHH403201.jpeg`, `images\GHH403202.jpeg`
- Duplicate sources: `pages\8388.html`, `pages\22894.html`, `pages\21307.html`

### Full Text

````text
# DTC P0563 (K20C2)

DTC P0563: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

If there is a short to ground in the harness between the powertrain control module (PCM) and PGM-FI main relay 1 circuit, PGM-FI main relay 1 circuit stays ON even if the vehicle is turned to the OFF (LOCK) mode, and the PCM remains active. However, the engine is not running because power for the gauges, the ignition, and the fuel pump is turned OFF by the ignition switch. When the PCM operates for a set time after the vehicle is turned to the OFF (LOCK) mode, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] (FI MAIN RLY OUT terminal of PCM) | 10.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM operates for at least 5 seconds after the vehicle is turned to the OFF (LOCK) mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit stuck on failure

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5653: DTC P0563 (L15B7/L15BA)

- Title: DTC P0563 (L15B7/L15BA)
- Source path: `pages\6802.html`
- Chunk ID: `chunk_0b743a9cec35`
- Images: `images\GHH403203.jpeg`, `images\GHH403204.jpeg`
- Duplicate sources: `pages\8389.html`, `pages\22895.html`, `pages\21308.html`

### Full Text

````text
# DTC P0563 (L15B7/L15BA)

DTC P0563: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

If there is a short to ground in the harness between the powertrain control module (PCM) and PGM-FI main relay 1 circuit, PGM-FI main relay 1 circuit stays ON even if the vehicle is turned to the OFF (LOCK) mode, and the PCM remains active. However, the engine is not running because power for the gauges, the ignition, and the fuel pump is turned OFF by the ignition switch. When the PCM operates for a set time after the vehicle is turned to the OFF (LOCK) mode, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] (FI MAIN RLY OUT terminal of PCM) | 10.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM operates for at least 5 seconds after the vehicle is turned to the OFF (LOCK) mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit stuck on failure

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5654: DTC P0571 (K20C1) (2017 2018 2019)

- Title: DTC P0571 (K20C1) (2017 2018 2019)
- Source path: `pages\6803.html`
- Chunk ID: `chunk_beca83edad01`
- Images: `images\GHH403205.jpeg`
- Duplicate sources: `pages\8390.html`, `pages\22896.html`, `pages\21309.html`

### Full Text

````text
# DTC P0571 (K20C1) (2017 2018 2019)

DTC P0571: Brake Pedal Position Switch Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of these conditions occurs:

- When the brake pedal position switch (STOP SW line) outputs ON to the PCM during accelerator pedal position is more than 0 % for 2.0 seconds or more, the detection counter is incremented. If the detection counter reaches to 15, 000 counts or more, the PCM stores a DTC.

- When the brake pedal position switch (STOP SW line) outputs OFF to the PCM while the vehicle is decelerated (to 0 mph (0 km/h)) from vehicle speed [Vehicle Speed] over 25 mph (40 km/h) for 2.0 seconds or more, the detection counter is incremented. If the detection counter reaches to more than 3 counts, the PCM stores a DTC.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch STOP SW line open

- Brake pedal position switch STOP SW line short to power

- Brake pedal position switch STOP SW line short to ground

- Brake pedal position switch failure

Confirmation Procedure

Operating Condition

- Start the engine, and drive the vehicle at 25 mph (40 km/h) or more.

- Decelerate without pressing the brake pedal for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5655: DTC P0571 (K20C1) (2019 2020 2021)

- Title: DTC P0571 (K20C1) (2019 2020 2021)
- Source path: `pages\6804.html`
- Chunk ID: `chunk_b86cb2a2e6a7`
- Images: `images\GHH403206.jpeg`
- Duplicate sources: `pages\8391.html`, `pages\22897.html`, `pages\21310.html`

### Full Text

````text
# DTC P0571 (K20C1) (2019 2020 2021)

DTC P0571: Brake Pedal Position Switch Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring the signals from the brake pedal position switch. If the PCM continuously inputs an abnormal signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of these conditions occurs:

- When the brake pedal position switch (STOP SW line) is closed during accelerator pedal position is more than 0 % for 2 seconds or more, the detection counter is incremented. If the detection counter reaches to 15, 000 counts or more, the PCM stores a DTC.

- When the brake pedal position switch (STOP SW line) is open while the vehicle is decelerated (to 0 mph (0 km/h)) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h), the detection counter is incremented. If the detection counter reaches to more than 3 counts, the PCM stores a DTC.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch STOP SW line open

- Brake pedal position switch STOP SW line short to power

- Brake pedal position switch STOP SW line short to ground

- Brake pedal position switch failure

Confirmation Procedure

Operating Condition

- Start the engine, and drive the vehicle at 25 mph (40 km/h) or more.

- Decelerate without pressing the brake pedal for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5656: DTC P0571 (K20C2)

- Title: DTC P0571 (K20C2)
- Source path: `pages\6805.html`
- Chunk ID: `chunk_46bda6316e6b`
- Images: `images\GHH403207.jpeg`, `images\GHH403208.jpeg`
- Duplicate sources: `pages\8392.html`, `pages\22898.html`, `pages\21311.html`

### Full Text

````text
# DTC P0571 (K20C2)

DTC P0571: Brake Pedal Position Switch Circuit Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 minutes or more*, Depending on driving conditions**

DTC Type | Two drive cycles, MIL off

*: Symptom 1

**: Symptom 2

Enable Conditions

Condition

Vehicle | ON mode

Other* | Accelerator pedal pressed

Malfunction Threshold

- Symptom 1 The PCM inputs an ON signal from the brake pedal position switch (STOP SW line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

The PCM inputs an ON signal from the brake pedal position switch (STOP SW line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

- Symptom 2 The PCM inputs an OFF signal from the brake pedal position switch (STOP SW line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

The PCM inputs an OFF signal from the brake pedal position switch (STOP SW line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch stuck

- Brake pedal position switch STOP SW line open (includes poor or loose connection)

- Brake pedal position switch STOP SW line short to power

- Brake pedal position switch STOP SW line short to ground

- Brake pedal position switch failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5657: DTC P0571 (L15B7/L15BA/L15BY)

- Title: DTC P0571 (L15B7/L15BA/L15BY)
- Source path: `pages\6806.html`
- Chunk ID: `chunk_415a64b038d3`
- Images: `images\GHH403209.jpeg`, `images\GHH403210.jpeg`
- Duplicate sources: `pages\8393.html`, `pages\22899.html`, `pages\21312.html`

### Full Text

````text
# DTC P0571 (L15B7/L15BA/L15BY)

DTC P0571: Brake Pedal Position Switch Circuit Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 minutes or more*, Depending on driving conditions**

DTC Type | Two drive cycles, MIL off

*: Symptom 1

**: Symptom 2

Enable Conditions

Condition

Vehicle | ON mode

Other* | Accelerator pedal pressed

Malfunction Threshold

Either of these conditions occurs:

- Symptom 1 The PCM inputs an ON signal from the brake pedal position switch (STOP SW line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

The PCM inputs an ON signal from the brake pedal position switch (STOP SW line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

- Symptom 2 The PCM inputs an OFF signal from the brake pedal position switch (STOP SW line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

The PCM inputs an OFF signal from the brake pedal position switch (STOP SW line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch stuck

- Brake pedal position switch STOP SW line open (includes poor or loose connection)

- Brake pedal position switch STOP SW line short to power

- Brake pedal position switch STOP SW line short to ground

- Brake pedal position switch failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5658: DTC P0600 (K20C2 (PGM-FI System))

- Title: DTC P0600 (K20C2 (PGM-FI System))
- Source path: `pages\6807.html`
- Chunk ID: `chunk_81c62244269c`
- Images: `images\GHH403211.jpeg`
- Duplicate sources: `pages\8394.html`, `pages\22900.html`, `pages\21313.html`

### Full Text

````text
# DTC P0600 (K20C2 (PGM-FI System))

DTC P0600: Powertrain Control Module (PCM) Serial Communication Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The driver IC which has diagnostic function and the CPU are built into the powertrain control module (PCM). If the CPU cannot receive diagnostic information from the driver IC for a specified duration due to occurrence of communication abnormality between the driver IC and the CPU, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs for at least 5 seconds:

- The CPU does not receive signal from the driver IC via the communication lines.

- The signal sent from the driver IC is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5659: DTC P0600 (L15B7 (PGM-FI System))

- Title: DTC P0600 (L15B7 (PGM-FI System))
- Source path: `pages\6808.html`
- Chunk ID: `chunk_6ab13a40c6de`
- Images: `images\GHH403212.jpeg`
- Duplicate sources: `pages\8395.html`, `pages\22901.html`, `pages\21314.html`

### Full Text

````text
# DTC P0600 (L15B7 (PGM-FI System))

DTC P0600: Powertrain Control Module (PCM) Serial Communication Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The driver IC which has diagnostic function and the CPU are built into the powertrain control module (PCM). If the CPU cannot receive diagnostic information from the driver IC for a specified duration due to occurrence of communication abnormality between the driver IC and the CPU, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs for at least 5 seconds:

- The CPU does not receive signal from the driver IC via the communication lines.

- The signal sent from the driver IC is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5660: DTC P0602 (K20C2 (PGM-FI System))

- Title: DTC P0602 (K20C2 (PGM-FI System))
- Source path: `pages\6809.html`
- Chunk ID: `chunk_fa7d505e4ab0`
- Images: `images\GHH403213.jpeg`
- Duplicate sources: `pages\8396.html`, `pages\22902.html`, `pages\21315.html`

### Full Text

````text
# DTC P0602 (K20C2 (PGM-FI System))

DTC P0602: Powertrain Control Module (PCM) Programming Error

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with an update program to update its control program. The programs in the CPU of the PCM are classified as a PCM program (update-capable program) and a program for the update function (non-updatable program). The program update only updates the PCM program. When the PCM power is turned off during an update, the power for the update function is lost, and the update process stops. When the program update is stopped before it is completed, the PCM stores a DTC that indicates the update is not finished.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or less

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM program update stops 1 second before it is finished.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM program unwritten

Diagnosis Details

Conditions for setting the DTC

When the PCM program is not written in the PCM, the MIL comes on and a Pending DTC and a Confirmed DTC are stored in the PCM memory.

Conditions for clearing the DTC

The MIL, the Pending DTC, and the Confirmed DTC are cleared when the PCM program update is completed.
````

## Chunk 5661: DTC P0602 (L15B7 (PGM-FI System))

- Title: DTC P0602 (L15B7 (PGM-FI System))
- Source path: `pages\6810.html`
- Chunk ID: `chunk_5f6f20cc4c98`
- Images: `images\GHH403214.jpeg`
- Duplicate sources: `pages\8397.html`, `pages\22903.html`, `pages\21316.html`

### Full Text

````text
# DTC P0602 (L15B7 (PGM-FI System))

DTC P0602: Powertrain Control Module (PCM) Programming Error

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with an update program to update its control program. The programs in the CPU of the PCM are classified as a PCM program (update-capable program) and a program for the update function (non-updatable program). The program update only updates the PCM program. When the PCM power is turned off during an update, the power for the update function is lost, and the update process stops. When the program update is stopped before it is completed, the PCM stores a DTC that indicates the update is not finished.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or less

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM program update stops 1 second before it is finished.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM program unwritten

Diagnosis Details

Conditions for setting the DTC

When the PCM program is not written in the PCM, the MIL comes on and a Pending DTC and a Confirmed DTC are stored in the PCM memory.

Conditions for clearing the DTC

The MIL, the Pending DTC, and the Confirmed DTC are cleared when the PCM program update is completed.
````

## Chunk 5662: DTC P0606 (K20C1) (2017 2018 2019)

- Title: DTC P0606 (K20C1) (2017 2018 2019)
- Source path: `pages\6811.html`
- Chunk ID: `chunk_603d98eb446c`
- Images: none
- Duplicate sources: `pages\8398.html`, `pages\22904.html`, `pages\21317.html`

### Full Text

````text
# DTC P0606 (K20C1) (2017 2018 2019)

DTC P0606: Powertrain Control Module (PCM) Processor Malfunction

General Description

DTC P0606 is stored if the internal failures of the powertrain control module (PCM) are detected:

- Knock sensor signal check The PCM tests to diagnose the evaluation of the knock detection signal from the knock sensor. A knock sensor (piezo-ceramic acceleration sensor) acquires the combustion noise and converts it into electrical signals. The signal is processed in the microcontroller CPU (knock sensor processor) of the PCM. The number of sampled signals, the position and the length of the measuring window are constantly (combustion synchronized) monitored for rationality faults. If these values are abnormal, the PCM detects a malfunction and stores a DTC.

The PCM tests to diagnose the evaluation of the knock detection signal from the knock sensor. A knock sensor (piezo-ceramic acceleration sensor) acquires the combustion noise and converts it into electrical signals. The signal is processed in the microcontroller CPU (knock sensor processor) of the PCM. The number of sampled signals, the position and the length of the measuring window are constantly (combustion synchronized) monitored for rationality faults. If these values are abnormal, the PCM detects a malfunction and stores a DTC.

- EEPROM read/write error The read and write access to EEPROM is permanently monitored by the EEPROM hardware abstraction layer. If a data block could not be read from or write to the EEPROM, the PCM detects a malfunction and stores a DTC.

The read and write access to EEPROM is permanently monitored by the EEPROM hardware abstraction layer. If a data block could not be read from or write to the EEPROM, the PCM detects a malfunction and stores a DTC.

- A/F sensor (sensor 1) driver IC error The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the PCM. The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an error occurs at the driver IC, the PCM detects a malfunction and stores a DTC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the PCM. The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an error occurs at the driver IC, the PCM detects a malfunction and stores a DTC.

- CVO signal not plausible The powertrain control module (PCM) diagnoses the controlled valve operation (CVO) that corrects the injection time of every injector to get a correct fuel quantity. The PCM converts the injector voltage signals to digital CVO signals. If the CVO signal is abnormal, the PCM detects a malfunction and stores a DTC.

The powertrain control module (PCM) diagnoses the controlled valve operation (CVO) that corrects the injection time of every injector to get a correct fuel quantity. The PCM converts the injector voltage signals to digital CVO signals. If the CVO signal is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Knock sensor signal check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

EEPROM read/write error

Condition

Vehicle | ON mode

A/F sensor (sensor 1) driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

CVO signal not plausible

Condition

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

- Knock sensor signal check Either of the symptoms occurs:

Either of the symptoms occurs:
````

## Chunk 5663: DTC P0606 (K20C1) (2017 2018 2019)

- Title: DTC P0606 (K20C1) (2017 2018 2019)
- Source path: `pages\6811.html`
- Chunk ID: `chunk_dc6547f5ada9`
- Images: none
- Duplicate sources: `pages\8398.html`, `pages\22904.html`, `pages\21317.html`

### Full Text

````text
If the CVO signal is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Knock sensor signal check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

EEPROM read/write error

Condition

Vehicle | ON mode

A/F sensor (sensor 1) driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

CVO signal not plausible

Condition

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

- Knock sensor signal check Either of the symptoms occurs:

Either of the symptoms occurs:

- - Absolute difference between number of estimated and number measured sampled signals within observation period (400 crankshaft revolutions) is greater than 30 counts for at least 24 counts. - Number of signal evaluation errors (position and length of measuring window) within observation period (approximately 3 seconds) is greater than 2 counts.

- - Absolute difference between number of estimated and number measured sampled signals within observation period (400 crankshaft revolutions) is greater than 30 counts for at least 24 counts.

Absolute difference between number of estimated and number measured sampled signals within observation period (400 crankshaft revolutions) is greater than 30 counts for at least 24 counts.

- - Number of signal evaluation errors (position and length of measuring window) within observation period (approximately 3 seconds) is greater than 2 counts.

Number of signal evaluation errors (position and length of measuring window) within observation period (approximately 3 seconds) is greater than 2 counts.

- EEPROM read/write error Either of the symptoms occurs:

Either of the symptoms occurs:

- - A data block cannot be read or a read order of data blocks is not successfully accomplished. - A data block cannot be written.

- - A data block cannot be read or a read order of data blocks is not successfully accomplished.

A data block cannot be read or a read order of data blocks is not successfully accomplished.

- - A data block cannot be written.

A data block cannot be written.

- A/F sensor (sensor 1) driver IC error An error is detected during communication with the driver IC for at least 2 seconds.

An error is detected during communication with the driver IC for at least 2 seconds.

- CVO signal not plausible Either of the symptoms occurs for at least 100 counts:

Either of the symptoms occurs for at least 100 counts:

- - Measured buffer CVO signal at beginning is more than 15, 000. - Measured buffer CVO signal at end is less than 5, 000.

- - Measured buffer CVO signal at beginning is more than 15, 000.

Measured buffer CVO signal at beginning is more than 15, 000.

- - Measured buffer CVO signal at end is less than 5, 000.

Measured buffer CVO signal at end is less than 5, 000.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle at engine speed [Engine Speed] 1, 000 rpm or more for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5664: DTC P0606 (K20C1) (2019 2020 2021)

- Title: DTC P0606 (K20C1) (2019 2020 2021)
- Source path: `pages\6812.html`
- Chunk ID: `chunk_d1923718eda1`
- Images: none
- Duplicate sources: `pages\8399.html`, `pages\22905.html`, `pages\21318.html`

### Full Text

````text
# DTC P0606 (K20C1) (2019 2020 2021)

DTC P0606: Powertrain Control Module (PCM) Processor Malfunction

General Description

DTC P0606 is stored if the internal failures of the powertrain control module (PCM) are detected:

- Knock sensor signal check The PCM tests to diagnose the evaluation of the knock detection signal from the knock sensor. A knock sensor (piezo-ceramic acceleration sensor) acquires the combustion noise and converts it into electrical signals. The signal is processed in the microcontroller CPU (knock sensor processor) of the PCM. The number of sampled signals, the position and the length of the measuring window are constantly (combustion synchronized) monitored for rationality faults. If these values are abnormal, the PCM detects a malfunction and stores a DTC.

The PCM tests to diagnose the evaluation of the knock detection signal from the knock sensor. A knock sensor (piezo-ceramic acceleration sensor) acquires the combustion noise and converts it into electrical signals. The signal is processed in the microcontroller CPU (knock sensor processor) of the PCM. The number of sampled signals, the position and the length of the measuring window are constantly (combustion synchronized) monitored for rationality faults. If these values are abnormal, the PCM detects a malfunction and stores a DTC.

- Electrically erasable programmable read-only memory (EEPROM) read/write error The read and write access to EEPROM is permanently monitored by the EEPROM hardware abstraction layer. If a data block could not be read from or write to the EEPROM, the PCM detects a malfunction and stores a DTC.

The read and write access to EEPROM is permanently monitored by the EEPROM hardware abstraction layer. If a data block could not be read from or write to the EEPROM, the PCM detects a malfunction and stores a DTC.

- Air/fuel ratio (A/F) sensor (sensor 1) driver IC error The driver IC for A/F sensor (sensor 1) is built into the PCM. The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an error occurs at the driver IC, the PCM detects a malfunction and stores a DTC.

The driver IC for A/F sensor (sensor 1) is built into the PCM. The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an error occurs at the driver IC, the PCM detects a malfunction and stores a DTC.

- Controlled valve operation (CVO) signal not plausible The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, error reactions will be activated such as triggering a new base adaptation or locking the defective injector for the CVO. If the CVO signal is not plausible, the PCM detects a malfunction and stores a DTC.

The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, error reactions will be activated such as triggering a new base adaptation or locking the defective injector for the CVO. If the CVO signal is not plausible, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous or multiple*

Sequence | None

Duration | Depending on error

DTC Type | Two drive cycles, MIL on

*: Depending on error

Enable Conditions

Knock sensor signal check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

EEPROM read/write error

Condition

Vehicle | ON mode

A/F sensor (sensor 1) driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

CVO signal not plausible

Condition

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

- Knock sensor signal check Either of the symptoms occurs:
````

## Chunk 5665: DTC P0606 (K20C1) (2019 2020 2021)

- Title: DTC P0606 (K20C1) (2019 2020 2021)
- Source path: `pages\6812.html`
- Chunk ID: `chunk_4435c48e1dff`
- Images: none
- Duplicate sources: `pages\8399.html`, `pages\22905.html`, `pages\21318.html`

### Full Text

````text
VO signal is not plausible, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous or multiple*

Sequence | None

Duration | Depending on error

DTC Type | Two drive cycles, MIL on

*: Depending on error

Enable Conditions

Knock sensor signal check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

EEPROM read/write error

Condition

Vehicle | ON mode

A/F sensor (sensor 1) driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

CVO signal not plausible

Condition

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

- Knock sensor signal check Either of the symptoms occurs:

Either of the symptoms occurs:

- - The absolute difference of estimated and measured sampled signals in the measuring window is more than 30 at least 100 counts within 400 of observation period. - Number of signal evaluation errors (position and length of measuring window) within observation period is greater than 2 counts.

- - The absolute difference of estimated and measured sampled signals in the measuring window is more than 30 at least 100 counts within 400 of observation period.

The absolute difference of estimated and measured sampled signals in the measuring window is more than 30 at least 100 counts within 400 of observation period.

- - Number of signal evaluation errors (position and length of measuring window) within observation period is greater than 2 counts.

Number of signal evaluation errors (position and length of measuring window) within observation period is greater than 2 counts.

- EEPROM read/write error A data block cannot be read/written or a read order of data blocks is not successfully accomplished at least 3 events.

A data block cannot be read/written or a read order of data blocks is not successfully accomplished at least 3 events.

- A/F sensor (sensor 1) driver IC error Either of the symptoms occurs:

Either of the symptoms occurs:

- - A/F sensor (sensor 1) driver IC error in the PCM is detected during transmission of diagnostic register, data register, or RAM data. - The driver IC initialization was not successful, slow response, or no values found in diagnosis register.

- - A/F sensor (sensor 1) driver IC error in the PCM is detected during transmission of diagnostic register, data register, or RAM data.

A/F sensor (sensor 1) driver IC error in the PCM is detected during transmission of diagnostic register, data register, or RAM data.

- - The driver IC initialization was not successful, slow response, or no values found in diagnosis register.

The driver IC initialization was not successful, slow response, or no values found in diagnosis register.

- CVO signal not plausible Either of the symptoms occurs for at least 100 counts:

Either of the symptoms occurs for at least 100 counts:

- - Measured buffer CVO signal at beginning is more than 15, 000. - Measured buffer CVO signal at end is less than 5, 000.

- - Measured buffer CVO signal at beginning is more than 15, 000.

Measured buffer CVO signal at beginning is more than 15, 000.

- - Measured buffer CVO signal at end is less than 5, 000.

Measured buffer CVO signal at end is less than 5, 000.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle at engine speed [Engine Speed] 1, 000 rpm or more for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5666: DTC P0607 (K20C1) (2017 2018 2019)

- Title: DTC P0607 (K20C1) (2017 2018 2019)
- Source path: `pages\6813.html`
- Chunk ID: `chunk_9a52dea07e6e`
- Images: none
- Duplicate sources: `pages\8400.html`, `pages\22906.html`, `pages\21319.html`

### Full Text

````text
# DTC P0607 (K20C1) (2017 2018 2019)

DTC P0607: Powertrain Control Module (PCM) Internal Circuit Malfunction

General Description

DTC P0607 is stored if the internal failures of the powertrain control module (PCM) are detected:

- Starter relay driver IC disturbance The driver IC for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

The driver IC for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

- System basic IC for powertrain control error The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

- PCM internal communication error The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

- Peripheral device error The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

- Throttle actuator driver IC error The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on
````

## Chunk 5667: DTC P0607 (K20C1) (2017 2018 2019)

- Title: DTC P0607 (K20C1) (2017 2018 2019)
- Source path: `pages\6813.html`
- Chunk ID: `chunk_77317d7f84cc`
- Images: none
- Duplicate sources: `pages\8400.html`, `pages\22906.html`, `pages\21319.html`

### Full Text

````text
control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

- Starter relay driver IC disturbance Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

- System basic IC for powertrain control error Either of the symptoms occurs:

Either of the symptoms occurs:

- - System basic IC receives a different check byte value. - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- - System basic IC receives a different check byte value.

System basic IC receives a different check byte value.

- - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- PCM internal communication error The error counter exceeds 5 counts.

The error counter exceeds 5 counts.

- Peripheral device error Peripheral monitoring function reports an error for at least 0.1 second.

Peripheral monitoring function reports an error for at least 0.1 second.

- Throttle actuator driver IC error Any of the errors are reported:

Any of the errors are reported:

- - Throttle actuator driver IC communication error - Throttle actuator driver IC time out error - Throttle actuator driver IC identification error

- - Throttle actuator driver IC communication error

Throttle actuator driver IC communication error

- - Throttle actuator driver IC time out error

Throttle actuator driver IC time out error

- - Throttle actuator driver IC identification error

Throttle actuator driver IC identification error

- Turbocharger wastegate control actuator driver IC error Any of the errors are reported:

Any of the errors are reported:

- - Turbocharger wastegate control actuator driver IC communication error - Turbocharger wastegate control actuator driver IC time out error - Turbocharger wastegate control actuator driver IC identification error

- - Turbocharger wastegate control actuator driver IC communication error

Turbocharger wastegate control actuator driver IC communication error

- - Turbocharger wastegate control actuator driver IC time out error

Turbocharger wastegate control actuator driver IC time out error

- - Turbocharger wastegate control actuator driver IC identification error

Turbocharger wastegate control actuator driver IC identification error

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5668: DTC P0607 (K20C1) (2019)

- Title: DTC P0607 (K20C1) (2019)
- Source path: `pages\6814.html`
- Chunk ID: `chunk_f7b36de9bcba`
- Images: none
- Duplicate sources: `pages\8401.html`, `pages\22907.html`, `pages\21320.html`

### Full Text

````text
# DTC P0607 (K20C1) (2019)

DTC P0607: Powertrain Control Module (PCM) Internal Circuit Malfunction

General Description

DTC P0607 is stored if the internal failures of the powertrain control module (PCM) are detected:

- Starter control module disturbance The starter control module for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

The starter control module for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

- System basic IC for powertrain control error The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

- PCM internal communication error The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

- Peripheral device error The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

- Throttle actuator driver IC error The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error

DTC Type | One drive cycle, MIL on
````

## Chunk 5669: DTC P0607 (K20C1) (2019)

- Title: DTC P0607 (K20C1) (2019)
- Source path: `pages\6814.html`
- Chunk ID: `chunk_ad0ad4049490`
- Images: none
- Duplicate sources: `pages\8401.html`, `pages\22907.html`, `pages\21320.html`

### Full Text

````text
control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error

DTC Type | One drive cycle, MIL on

Enable Conditions

Starter control module disturbance, System basic IC for powertrain control error, PCM internal communication error, peripheral device error

Condition

Vehicle | ON mode

Throttle actuator driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

State of the engine | Running

Other | Other than fuel cut operation

Throttle actuator power stage on

Turbocharger wastegate control actuator driver IC error

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

State of the engine | Running

Other | Turbocharger wastegate control actuator power stage on

[ ]: HDS Parameter

Malfunction Threshold

- Starter control module disturbance Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

- System basic IC for powertrain control error Either of the symptoms occurs:

Either of the symptoms occurs:

- - System basic IC receives a different check byte value. - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- - System basic IC receives a different check byte value.

System basic IC receives a different check byte value.

- - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- PCM internal communication error All of the symptoms occur:

All of the symptoms occur:

- - The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller. - During communication between the monitoring function and the function controller. - The malfunction detection counter in the function controller exceeds 5 counts.

- - The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller.

The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller.

- - During communication between the monitoring function and the function controller.

During communication between the monitoring function and the function controller.

- - The malfunction detection counter in the function controller exceeds 5 counts.

The malfunction detection counter in the function controller exceeds 5 counts.

- Peripheral device error Peripheral monitoring function reports an error.

Peripheral monitoring function reports an error.

- Throttle actuator driver IC error Throttle actuator driver IC reports an error.

Throttle actuator driver IC reports an error.

- Turbocharger wastegate control actuator driver IC error Turbocharger wastegate control actuator driver IC reports an error.

Turbocharger wastegate control actuator driver IC reports an error.

Malfunction Threshold

- Starter relay driver IC disturbance Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

- System basic IC for powertrain control error Either of the symptoms occurs:

Either of the symptoms occurs:

- - System basic IC receives a different check byte value. - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- - System basic IC receives a different check byte value.

System basic IC receives a different check byte value.

- - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.
````

## Chunk 5670: DTC P0607 (K20C1) (2019)

- Title: DTC P0607 (K20C1) (2019)
- Source path: `pages\6814.html`
- Chunk ID: `chunk_a22b811b40b8`
- Images: none
- Duplicate sources: `pages\8401.html`, `pages\22907.html`, `pages\21320.html`

### Full Text

````text
IC reports an error.

Malfunction Threshold

- Starter relay driver IC disturbance Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

- System basic IC for powertrain control error Either of the symptoms occurs:

Either of the symptoms occurs:

- - System basic IC receives a different check byte value. - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- - System basic IC receives a different check byte value.

System basic IC receives a different check byte value.

- - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- PCM internal communication error The error counter exceeds 5 counts.

The error counter exceeds 5 counts.

- Peripheral device error Peripheral monitoring function reports an error for at least 0.1 second.

Peripheral monitoring function reports an error for at least 0.1 second.

- Throttle actuator driver IC error Any of the errors are reported:

Any of the errors are reported:

- - Throttle actuator driver IC communication error - Throttle actuator driver IC time out error - Throttle actuator driver IC identification error

- - Throttle actuator driver IC communication error

Throttle actuator driver IC communication error

- - Throttle actuator driver IC time out error

Throttle actuator driver IC time out error

- - Throttle actuator driver IC identification error

Throttle actuator driver IC identification error

- Turbocharger wastegate control actuator driver IC error Any of the errors are reported:

Any of the errors are reported:

- - Turbocharger wastegate control actuator driver IC communication error - Turbocharger wastegate control actuator driver IC time out error - Turbocharger wastegate control actuator driver IC identification error

- - Turbocharger wastegate control actuator driver IC communication error

Turbocharger wastegate control actuator driver IC communication error

- - Turbocharger wastegate control actuator driver IC time out error

Turbocharger wastegate control actuator driver IC time out error

- - Turbocharger wastegate control actuator driver IC identification error

Turbocharger wastegate control actuator driver IC identification error

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5671: DTC P0607 (K20C1) (2020 2021)

- Title: DTC P0607 (K20C1) (2020 2021)
- Source path: `pages\6815.html`
- Chunk ID: `chunk_dab1f23c5476`
- Images: none
- Duplicate sources: `pages\8402.html`, `pages\22908.html`, `pages\21321.html`

### Full Text

````text
# DTC P0607 (K20C1) (2020 2021)

DTC P0607: Powertrain Control Module (PCM) Internal Circuit Malfunction

General Description

DTC P0607 is stored if the internal failures of the powertrain control module (PCM) are detected:

- Starter control module disturbance The starter control module for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

The starter control module for starter relays in the PCM provides two low side switches for the control of a starter relays in automotive applications. This error is a result of a hardware failure/disturbance, therefore the detection strategy is similar to the hardware monitoring of the PCM monitoring software used mainly to filter disturbances. If a disturbance is detected, the PCM stores a DTC.

- System basic IC for powertrain control error The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

The system basic driver IC for powertrain control controls the hardware functions of the application specific integrated circuit (ASIC). The driver IC features the communication with the monitoring unit (external watchdog), the acquisition of ON reset, control of the PGM-FI main relay, the wakeup control, and the diagnosis of the sensor supplies. If the values or communications are abnormal, the PCM detects a malfunction and stores a DTC.

- PCM internal communication error The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

The PCM reciprocally monitors the function controller and monitoring module using the query-response communication. The status of the error counter in the monitoring module is transferred together with the query and stored in the function controller. If the error counter reaches a specified value, the PCM detects a malfunction and stores a DTC.

- Peripheral device error The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

The PCM monitors peripheral devices to determine proper working of the peripheral devices. The peripheral monitoring device (PMD) in the PCM monitors errors in communication between peripheral device and controller, and also partial resets. If any peripheral monitoring function reports an error, the PCM detects a malfunction and stores a DTC.

- Throttle actuator driver IC error The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error
````

## Chunk 5672: DTC P0607 (K20C1) (2020 2021)

- Title: DTC P0607 (K20C1) (2020 2021)
- Source path: `pages\6815.html`
- Chunk ID: `chunk_8c940e29e4d6`
- Images: none
- Duplicate sources: `pages\8402.html`, `pages\22908.html`, `pages\21321.html`

### Full Text

````text
PCM monitors the throttle actuator control circuit for communication malfunctions. If any errors in the throttle actuator control circuit are detected, the PCM stores a DTC.

- Turbocharger wastegate control actuator driver IC error The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

The PCM monitors the turbocharger wastegate control actuator control circuit for communication malfunctions. If any errors in the turbocharger wastegate control actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error

DTC Type | One drive cycle, MIL on

Enable Conditions

Starter control module disturbance, System basic IC for powertrain control error, PCM internal communication error, peripheral device error

Condition

Vehicle | ON mode

Throttle actuator driver IC error, Turbocharger wastegate control actuator driver IC error

Condition

State of the engine | Running

Malfunction Threshold

- Starter control module disturbance Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

Electromagnetic interference (EMI) disturbance is detected for at least 0.5 second.

- System basic IC for powertrain control error Either of the symptoms occurs:

Either of the symptoms occurs:

- - System basic IC receives a different check byte value. - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- - System basic IC receives a different check byte value.

System basic IC receives a different check byte value.

- - Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

Serial peripheral interface (SPI) driver does not accept a command-prompt sequence.

- PCM internal communication error All of the symptoms occur:

All of the symptoms occur:

- - The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller. - During communication between the monitoring function and the function controller. - The malfunction detection counter in the function controller exceeds 5 counts.

- - The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller.

The error counter is within 5 counts during confirmation of communication between the monitoring module and the function controller.

- - During communication between the monitoring function and the function controller.

During communication between the monitoring function and the function controller.

- - The malfunction detection counter in the function controller exceeds 5 counts.

The malfunction detection counter in the function controller exceeds 5 counts.

- Peripheral device error Peripheral monitoring function reports an error.

Peripheral monitoring function reports an error.

- Throttle actuator driver IC error Throttle actuator driver IC reports an error.

Throttle actuator driver IC reports an error.

- Turbocharger wastegate control actuator driver IC error Turbocharger wastegate control actuator driver IC reports an error.

Turbocharger wastegate control actuator driver IC reports an error.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5673: DTC P060A (K20C2)

- Title: DTC P060A (K20C2)
- Source path: `pages\6816.html`
- Chunk ID: `chunk_bffa52fb1d10`
- Images: `images\GHH403215.jpeg`
- Duplicate sources: `pages\8403.html`, `pages\22909.html`, `pages\21322.html`

### Full Text

````text
# DTC P060A (K20C2)

DTC P060A: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

When a malfunction occurs in the communication line between the main CPU and the sub CPU in the powertrain control module (PCM), no monitor signals from the sub CPU for a set time, or abnormal signals are detected for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these symptoms occurs for at least 2.0 seconds:

- No sub CPU monitor signals are detected.

- Sub CPU monitor signals are abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5674: DTC P060A (L15B7/L15BA)

- Title: DTC P060A (L15B7/L15BA)
- Source path: `pages\6817.html`
- Chunk ID: `chunk_a0216a6a6354`
- Images: `images\GHH403216.jpeg`
- Duplicate sources: `pages\8404.html`, `pages\22910.html`, `pages\21323.html`

### Full Text

````text
# DTC P060A (L15B7/L15BA)

DTC P060A: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

When a malfunction occurs in the communication line between the main CPU and the sub CPU in the powertrain control module (PCM), no monitor signals from the sub CPU for a set time, or abnormal signals are detected for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these symptoms occurs for at least 2.0 seconds:

- No sub CPU monitor signals are detected.

- Sub CPU monitor signals are abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5675: DTC P060C (K20C1) (2017 2018 2019)

- Title: DTC P060C (K20C1) (2017 2018 2019)
- Source path: `pages\6818.html`
- Chunk ID: `chunk_ed5dddb47802`
- Images: none
- Duplicate sources: `pages\8405.html`, `pages\22911.html`, `pages\21324.html`

### Full Text

````text
# DTC P060C (K20C1) (2017 2018 2019)

DTC P060C: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

DTC P060C is stored if the internal failures of the powertrain control module (PCM) are detected:

- Engine torque limitation failure The engine torque is limited to a maximum value that is defined according to the current constraints. If the engine speed exceeds the maximum engine speed, the engine torque is reduced. In normal circumstances, this intervention in torque limiting is done only for short times. If the limitation is active for a longer time, the PCM detects a malfunction and stores a DTC.

The engine torque is limited to a maximum value that is defined according to the current constraints. If the engine speed exceeds the maximum engine speed, the engine torque is reduced. In normal circumstances, this intervention in torque limiting is done only for short times. If the limitation is active for a longer time, the PCM detects a malfunction and stores a DTC.

- PCM internal calculation error The PCM monitors itself whether the PCM internal calculations are correct. Therefore control values are compared with monitoring values. If the injection cut-off pattern does not fit to the injection mode or the desired injection pattern is not equal to the actual injection pattern, the PCM detects a malfunction and stores a DTC. The fault leads to an injection quantity limitation.

The PCM monitors itself whether the PCM internal calculations are correct. Therefore control values are compared with monitoring values. If the injection cut-off pattern does not fit to the injection mode or the desired injection pattern is not equal to the actual injection pattern, the PCM detects a malfunction and stores a DTC. The fault leads to an injection quantity limitation.

- Fuel correction error The cylinder individual fuel correction monitoring consists of an injection valve pin lift rationality check, and a signal range check of the calculated cylinder individual fuel mass. If the checked fuel corrections are out of a specified range, the PCM detects a malfunction and stores a DTC. Faults recognized by the monitoring functions lead to limp home modes.

The cylinder individual fuel correction monitoring consists of an injection valve pin lift rationality check, and a signal range check of the calculated cylinder individual fuel mass. If the checked fuel corrections are out of a specified range, the PCM detects a malfunction and stores a DTC. Faults recognized by the monitoring functions lead to limp home modes.

- Charging efficiency deviation The PCM monitors the deviation of the predicted charging efficiency from the calculated charging efficiency. If the absolute deviation is greater than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

The PCM monitors the deviation of the predicted charging efficiency from the calculated charging efficiency. If the absolute deviation is greater than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

- APP sensor signal plausibility check The accelerator pedal position monitoring consists of the signal plausibility check and the sensor supply voltage check. The PCM determines the accelerator pedal position based on two redundant accelerator pedal position (APP) sensors. For safety reasons, the two APP sensor signals are compared for synchronism. If the difference between the two APP sensor signals exceeds a specified value or if the APP sensor supply voltage is out of a specified range, the PCM detects a malfunction and stores a DTC.

The accelerator pedal position monitoring consists of the signal plausibility check and the sensor supply voltage check. The PCM determines the accelerator pedal position based on two redundant accelerator pedal position (APP) sensors. For safety reasons, the two APP sensor signals are compared for synchronism. If the difference between the two APP sensor signals exceeds a specified value or if the APP sensor supply voltage is out of a specified range, the PCM detects a malfunction and stores a DTC.

- Engine speed check The monitoring function of the PCM calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed.
````

## Chunk 5676: DTC P060C (K20C1) (2017 2018 2019)

- Title: DTC P060C (K20C1) (2017 2018 2019)
- Source path: `pages\6818.html`
- Chunk ID: `chunk_6dd63b8725d3`
- Images: none
- Duplicate sources: `pages\8405.html`, `pages\22911.html`, `pages\21324.html`

### Full Text

````text
PCM detects a malfunction and stores a DTC.

The accelerator pedal position monitoring consists of the signal plausibility check and the sensor supply voltage check. The PCM determines the accelerator pedal position based on two redundant accelerator pedal position (APP) sensors. For safety reasons, the two APP sensor signals are compared for synchronism. If the difference between the two APP sensor signals exceeds a specified value or if the APP sensor supply voltage is out of a specified range, the PCM detects a malfunction and stores a DTC.

- Engine speed check The monitoring function of the PCM calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed. If the difference between the two engine speeds is a specified value, the PCM detects a malfunction and stores a DTC.

The monitoring function of the PCM calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed. If the difference between the two engine speeds is a specified value, the PCM detects a malfunction and stores a DTC.

- Monitoring of mixture correction factor and relative fuel mass The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring. The function checks the plausibility of the mixture control and secures the calculated fuel mass. If the relative fuel mass or the mixture correction factor is abnormal, the PCM detects a malfunction and stores a DTC.

The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring. The function checks the plausibility of the mixture control and secures the calculated fuel mass. If the relative fuel mass or the mixture correction factor is abnormal, the PCM detects a malfunction and stores a DTC.

- Monitoring of injection cut-off and ignition cut-off The PCM monitors the injection cut-off above a first engine speed threshold and ignition cut off above a second engine speed threshold. If the monitored reactions are abnormal, the PCM detects a malfunction and stores a DTC.

The PCM monitors the injection cut-off above a first engine speed threshold and ignition cut off above a second engine speed threshold. If the monitored reactions are abnormal, the PCM detects a malfunction and stores a DTC.

- Lambda value check The PCM monitors the desired lambda value by means of plausibility check against operating modes. If the desired lambda is out of range, the PCM detects a malfunction and stores a DTC. Faults recognized by the monitoring functions lead to limp home modes.

The PCM monitors the desired lambda value by means of plausibility check against operating modes. If the desired lambda is out of range, the PCM detects a malfunction and stores a DTC. Faults recognized by the monitoring functions lead to limp home modes.

- Starter driver IC check The PCM monitors the plausibility check of the status of starter driver and redundancy control side start permission. If the starter driver are activated but redundancy control side does not permit engine start, the PCM detects a malfunction and stores a DTC.

The PCM monitors the plausibility check of the status of starter driver and redundancy control side start permission. If the starter driver are activated but redundancy control side does not permit engine start, the PCM detects a malfunction and stores a DTC.

- Engine torque check The PCM monitors the engine torque. The current engine torque is compared with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

The PCM monitors the engine torque. The current engine torque is compared with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

- Ignition angle check The PCM monitors the ignition angle. The ignition angle check detects implausible values by comparing the ignition angle output value with a verification value. If the ignition angle value and the complement of the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

The PCM monitors the ignition angle.
````

## Chunk 5677: DTC P060C (K20C1) (2017 2018 2019)

- Title: DTC P060C (K20C1) (2017 2018 2019)
- Source path: `pages\6818.html`
- Chunk ID: `chunk_04081b06eee9`
- Images: none
- Duplicate sources: `pages\8405.html`, `pages\22911.html`, `pages\21324.html`

### Full Text

````text
red with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

The PCM monitors the engine torque. The current engine torque is compared with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

- Ignition angle check The PCM monitors the ignition angle. The ignition angle check detects implausible values by comparing the ignition angle output value with a verification value. If the ignition angle value and the complement of the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

The PCM monitors the ignition angle. The ignition angle check detects implausible values by comparing the ignition angle output value with a verification value. If the ignition angle value and the complement of the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Engine torque limitation failure/Starter driver IC check

Condition

State of the engine | Running

PCM internal calculation error/Charging efficiency deviation/Monitoring of mixture correction factor and relative fuel mass

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 200 rpm | -

Other | Condition in steady engine load and engine speed

Fuel correction error

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 200 rpm | -

12 volt battery voltage [Battery] | 7 V | -

Other | Condition in steady engine load and engine speed

APP sensor signal plausibility check/Ignition angle check/Engine torque check

Condition

Vehicle | ON mode

Engine speed check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 520 rpm | -

Monitoring of injection cut-off and ignition cut-off

Condition

Vehicle | ON mode

Other | Injection cut-off is commanded

Lambda value check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 200 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

- Engine torque limitation failure The desired engine torque is limited for at least 10 seconds.

The desired engine torque is limited for at least 10 seconds.

- PCM internal calculation error Either of the symptoms occurs:

Either of the symptoms occurs:

- - Injection cut-off pattern is not equal to the injection mode. - Desired injection pattern is not equal to the actual injection pattern.

- - Injection cut-off pattern is not equal to the injection mode.

Injection cut-off pattern is not equal to the injection mode.

- - Desired injection pattern is not equal to the actual injection pattern.

Desired injection pattern is not equal to the actual injection pattern.

- Fuel correction error Either of the symptoms occurs:

Either of the symptoms occurs:

- - Correction factor tolerance-compensation is greater than 1.27. - Calculated cylinder individual relative fuel mass is out of range.

- - Correction factor tolerance-compensation is greater than 1.27.

Correction factor tolerance-compensation is greater than 1.27.

- - Calculated cylinder individual relative fuel mass is out of range.

Calculated cylinder individual relative fuel mass is out of range.

- Charging efficiency deviation The absolute deviation of the predicted charging efficiency from the calculated charging efficiency is greater than 11.3 % for at least 360 milliseconds.

The absolute deviation of the predicted charging efficiency from the calculated charging efficiency is greater than 11.3 % for at least 360 milliseconds.

- APP sensor signal plausibility check Either of the symptoms occurs:

Either of the symptoms occurs:

- - The difference between the two APP sensor signals is greater than 0.2832 V. - The difference between the two APP sensor signals is greater than 0.2686 V and the APP sensor supply voltage is 1.1621 V or more.

- - The difference between the two APP sensor signals is greater than 0.2832 V.

The difference between the two APP sensor signals is greater than 0.2832 V.

- - The difference between the two APP sensor signals is greater than 0.2686 V and the APP sensor supply voltage is 1.1621 V or more.
````

## Chunk 5678: DTC P060C (K20C1) (2017 2018 2019)

- Title: DTC P060C (K20C1) (2017 2018 2019)
- Source path: `pages\6818.html`
- Chunk ID: `chunk_0538729a820f`
- Images: none
- Duplicate sources: `pages\8405.html`, `pages\22911.html`, `pages\21324.html`

### Full Text

````text
.3 % for at least 360 milliseconds.

The absolute deviation of the predicted charging efficiency from the calculated charging efficiency is greater than 11.3 % for at least 360 milliseconds.

- APP sensor signal plausibility check Either of the symptoms occurs:

Either of the symptoms occurs:

- - The difference between the two APP sensor signals is greater than 0.2832 V. - The difference between the two APP sensor signals is greater than 0.2686 V and the APP sensor supply voltage is 1.1621 V or more.

- - The difference between the two APP sensor signals is greater than 0.2832 V.

The difference between the two APP sensor signals is greater than 0.2832 V.

- - The difference between the two APP sensor signals is greater than 0.2686 V and the APP sensor supply voltage is 1.1621 V or more.

The difference between the two APP sensor signals is greater than 0.2686 V and the APP sensor supply voltage is 1.1621 V or more.

- Engine speed check The difference between the two engine speeds is 320 rpm or more when the engine speed is 15, 000 rpm or less.

The difference between the two engine speeds is 320 rpm or more when the engine speed is 15, 000 rpm or less.

- Monitoring of mixture correction factor and relative fuel mass One of these symptoms occurs:

One of these symptoms occurs:

- - Maximum permissible factor lambda control in monitoring function is greater than 1.265625. - Maximum permissible lambda adaption in monitoring function is greater than 1.335938. - Maximum permissible value of additive air fuel adaption at monitoring function is greater than 8.3 %. - Maximum after start adaption value in function monitoring is greater than 1.01563. - Minimum permitted value of evaporating fuel at high engine speeds in function monitoring is less than -0.094 %. - The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- - Maximum permissible factor lambda control in monitoring function is greater than 1.265625.

Maximum permissible factor lambda control in monitoring function is greater than 1.265625.

- - Maximum permissible lambda adaption in monitoring function is greater than 1.335938.

Maximum permissible lambda adaption in monitoring function is greater than 1.335938.

- - Maximum permissible value of additive air fuel adaption at monitoring function is greater than 8.3 %.

Maximum permissible value of additive air fuel adaption at monitoring function is greater than 8.3 %.

- - Maximum after start adaption value in function monitoring is greater than 1.01563.

Maximum after start adaption value in function monitoring is greater than 1.01563.

- - Minimum permitted value of evaporating fuel at high engine speeds in function monitoring is less than -0.094 %.

Minimum permitted value of evaporating fuel at high engine speeds in function monitoring is less than -0.094 %.

- - The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- Monitoring of injection cut-off and ignition cut-off Either of the symptoms occurs:

Either of the symptoms occurs:

- - The engine speed exceeds a calibrated limit and the injection cut-off delay counter is counted 2 times and error counter is counted is counted 4 times. - The engine speed exceeds a calibrated limit and the ignition cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

- - The engine speed exceeds a calibrated limit and the injection cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

The engine speed exceeds a calibrated limit and the injection cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

- - The engine speed exceeds a calibrated limit and the ignition cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

The engine speed exceeds a calibrated limit and the ignition cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

- Lambda value check The desired lambda value is less than 0.69949, or greater than 1.20044.

The desired lambda value is less than 0.69949, or greater than 1.20044.
````

## Chunk 5679: DTC P060C (K20C1) (2017 2018 2019)

- Title: DTC P060C (K20C1) (2017 2018 2019)
- Source path: `pages\6818.html`
- Chunk ID: `chunk_5e9150f5c7fd`
- Images: none
- Duplicate sources: `pages\8405.html`, `pages\22911.html`, `pages\21324.html`

### Full Text

````text
unted 4 times.

- - The engine speed exceeds a calibrated limit and the injection cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

The engine speed exceeds a calibrated limit and the injection cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

- - The engine speed exceeds a calibrated limit and the ignition cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

The engine speed exceeds a calibrated limit and the ignition cut-off delay counter is counted 2 times and error counter is counted is counted 4 times.

- Lambda value check The desired lambda value is less than 0.69949, or greater than 1.20044.

The desired lambda value is less than 0.69949, or greater than 1.20044.

- Starter driver IC check The starter driver are activated but redundancy control side does not permit engine start at least 5 events.

The starter driver are activated but redundancy control side does not permit engine start at least 5 events.

- Engine torque check The current engine torque is greater than the maximum allowed engine torque at least 13 times.

The current engine torque is greater than the maximum allowed engine torque at least 13 times.

- Ignition angle check The ignition angle value and the complement of the ignition angle value are not identical.

The ignition angle value and the complement of the ignition angle value are not identical.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5680: DTC P060C (K20C1) (2019 2020 2021)

- Title: DTC P060C (K20C1) (2019 2020 2021)
- Source path: `pages\6819.html`
- Chunk ID: `chunk_4e66098d31e2`
- Images: none
- Duplicate sources: `pages\8406.html`, `pages\22912.html`, `pages\21325.html`

### Full Text

````text
# DTC P060C (K20C1) (2019 2020 2021)

DTC P060C: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

DTC P060C is stored if the internal failures of the powertrain control module (PCM) are detected:

- Engine torque limitation failure The engine torque is limited to a maximum value that is defined according to the current constraints. If the engine speed exceeds the maximum engine speed, the engine torque is reduced. In normal circumstances, this intervention in torque limiting is done only for short times. If the limitation is active for a longer time, the PCM detects a malfunction and stores a DTC.

The engine torque is limited to a maximum value that is defined according to the current constraints. If the engine speed exceeds the maximum engine speed, the engine torque is reduced. In normal circumstances, this intervention in torque limiting is done only for short times. If the limitation is active for a longer time, the PCM detects a malfunction and stores a DTC.

- PCM internal calculation error The PCM monitors itself whether the PCM internal calculations are correct. Therefore control values are compared with monitoring values. If the injection cut-off pattern does not fit to the injection mode or the desired injection pattern is not equal to the actual injection pattern, the PCM detects a malfunction and stores a DTC. The fault leads to an injection quantity limitation.

The PCM monitors itself whether the PCM internal calculations are correct. Therefore control values are compared with monitoring values. If the injection cut-off pattern does not fit to the injection mode or the desired injection pattern is not equal to the actual injection pattern, the PCM detects a malfunction and stores a DTC. The fault leads to an injection quantity limitation.

- Charging efficiency deviation The PCM monitors the deviation of the predicted charging efficiency from the calculated charging efficiency. If the absolute deviation is greater than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

The PCM monitors the deviation of the predicted charging efficiency from the calculated charging efficiency. If the absolute deviation is greater than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

- Accelerator pedal position (APP) sensor signal plausibility check The accelerator pedal position monitoring consists of the signal plausibility check and the sensor supply voltage check. The PCM determines the accelerator pedal position based on two redundant APP sensors. For safety reasons, the two APP sensor signals are compared for synchronism. If the difference between the two APP sensor signals exceeds a specified value, the PCM detects a malfunction and stores a DTC.

The accelerator pedal position monitoring consists of the signal plausibility check and the sensor supply voltage check. The PCM determines the accelerator pedal position based on two redundant APP sensors. For safety reasons, the two APP sensor signals are compared for synchronism. If the difference between the two APP sensor signals exceeds a specified value, the PCM detects a malfunction and stores a DTC.

- Engine speed check The monitoring function of the PCM calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed. If the difference between the two engine speeds is a specified value, the PCM detects a malfunction and stores a DTC.

The monitoring function of the PCM calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed. If the difference between the two engine speeds is a specified value, the PCM detects a malfunction and stores a DTC.

- Monitoring of mixture correction factor and relative fuel mass The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring. The function checks the plausibility of the mixture control and secures the calculated fuel mass. If the relative fuel mass or the mixture correction factor is abnormal, the PCM detects a malfunction and stores a DTC.

The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring.
````

## Chunk 5681: DTC P060C (K20C1) (2019 2020 2021)

- Title: DTC P060C (K20C1) (2019 2020 2021)
- Source path: `pages\6819.html`
- Chunk ID: `chunk_f726ca8f3429`
- Images: none
- Duplicate sources: `pages\8406.html`, `pages\22912.html`, `pages\21325.html`

### Full Text

````text
calculates the engine speed based on information from the related sensor. For safety reasons, the calculated engine speed of the monitoring function is compared with the measured engine speed. If the difference between the two engine speeds is a specified value, the PCM detects a malfunction and stores a DTC.

- Monitoring of mixture correction factor and relative fuel mass The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring. The function checks the plausibility of the mixture control and secures the calculated fuel mass. If the relative fuel mass or the mixture correction factor is abnormal, the PCM detects a malfunction and stores a DTC.

The PCM monitors the relative fuel mass and the mixture correction factor of the function monitoring. The function checks the plausibility of the mixture control and secures the calculated fuel mass. If the relative fuel mass or the mixture correction factor is abnormal, the PCM detects a malfunction and stores a DTC.

- Monitoring of injection cut-off and ignition cut-off The PCM monitors the injection cut-off above a first engine speed threshold and ignition cut off above a second engine speed threshold. If the monitored reactions are abnormal, the PCM detects a malfunction and stores a DTC.

The PCM monitors the injection cut-off above a first engine speed threshold and ignition cut off above a second engine speed threshold. If the monitored reactions are abnormal, the PCM detects a malfunction and stores a DTC.

- Lambda value check The PCM monitors the desired lambda value by means of plausibility check against operating modes. If the desired lambda is out of range, the PCM detects a malfunction and stores a DTC. The faults recognized by the monitoring functions lead to limp home modes.

The PCM monitors the desired lambda value by means of plausibility check against operating modes. If the desired lambda is out of range, the PCM detects a malfunction and stores a DTC. The faults recognized by the monitoring functions lead to limp home modes.

- Starter driver IC check The PCM monitors the plausibility check of the status of starter driver and redundancy control side start permission. If the starter driver is activated but redundancy control side does not permit engine start, the PCM detects a malfunction and stores a DTC.

The PCM monitors the plausibility check of the status of starter driver and redundancy control side start permission. If the starter driver is activated but redundancy control side does not permit engine start, the PCM detects a malfunction and stores a DTC.

- Engine torque check The PCM monitors the engine torque. The current engine torque is compared with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

The PCM monitors the engine torque. The current engine torque is compared with the maximum allowed engine torque. If the current engine torque is greater than the maximum allowed engine torque, the PCM detects a malfunction and stores a DTC.

- Ignition angle check The PCM monitors the ignition angle. The ignition angle check detects implausible values by comparing the ignition angle output value with a verification value. If the ignition angle value and the complement of the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

The PCM monitors the ignition angle. The ignition angle check detects implausible values by comparing the ignition angle output value with a verification value. If the ignition angle value and the complement of the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

- Overvoltage detection This function defines the reaction of the PCM in case of shut-off of the power stage via the watchdog output and supply voltage monitoring of power stages lines. If the overvoltage is detected, the PCM detects a malfunction and stores a DTC.

This function defines the reaction of the PCM in case of shut-off of the power stage via the watchdog output and supply voltage monitoring of power stages lines. If the overvoltage is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error

DTC Type | One drive cycle, MIL on

Enable Conditions
````

## Chunk 5682: DTC P060C (K20C1) (2019 2020 2021)

- Title: DTC P060C (K20C1) (2019 2020 2021)
- Source path: `pages\6819.html`
- Chunk ID: `chunk_509b0596e11d`
- Images: none
- Duplicate sources: `pages\8406.html`, `pages\22912.html`, `pages\21325.html`

### Full Text

````text
the ignition angle value are not identical for a specified time, the PCM detects a malfunction and stores a DTC.

- Overvoltage detection This function defines the reaction of the PCM in case of shut-off of the power stage via the watchdog output and supply voltage monitoring of power stages lines. If the overvoltage is detected, the PCM detects a malfunction and stores a DTC.

This function defines the reaction of the PCM in case of shut-off of the power stage via the watchdog output and supply voltage monitoring of power stages lines. If the overvoltage is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on error

DTC Type | One drive cycle, MIL on

Enable Conditions

Engine torque limitation failure/Engine torque check/Overvoltage detection

Condition

State of the engine | Running

Charging efficiency deviation/Fuel correction error/PCM internal calculation error/Lambda value check/Monitoring of mixture correction factor and relative fuel mass

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 200 rpm | -

Other | Injection cut-off is not commanded

APP sensor signal plausibility check

Condition | Minimum | Maximum

APP sensor 1 output voltage | 1.18 V | -

APP sensor 2 output voltage | 1.18 V | -

Engine speed check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 520 rpm | -

Starter driver IC check/Ignition angle check

Condition

Vehicle | ON mode

Monitoring of injection cut-off and ignition cut-off

Condition

Vehicle | ON mode

Other | Injection cut-off is commanded

[ ]: HDS Parameter

Malfunction Threshold

- Engine torque limitation failure The desired engine torque is limited for at least 10 seconds.

The desired engine torque is limited for at least 10 seconds.

- PCM internal calculation error Either of the symptoms occurs:

Either of the symptoms occurs:

- - Injection cut-off pattern is not equal to the injection mode. - Desired injection pattern is not equal to the actual injection pattern.

- - Injection cut-off pattern is not equal to the injection mode.

Injection cut-off pattern is not equal to the injection mode.

- - Desired injection pattern is not equal to the actual injection pattern.

Desired injection pattern is not equal to the actual injection pattern.

- Charging efficiency deviation The absolute deviation of the predicted charging efficiency from the calculated charging efficiency is greater than 11.3 %.

The absolute deviation of the predicted charging efficiency from the calculated charging efficiency is greater than 11.3 %.

- APP sensor signal plausibility check Either of the symptoms occurs:

Either of the symptoms occurs:

- - The difference between the two APP sensor signals is more than 0.28 V at full load. - The difference between the two APP sensor signals is more than 0.27 V at part load.

- - The difference between the two APP sensor signals is more than 0.28 V at full load.

The difference between the two APP sensor signals is more than 0.28 V at full load.

- - The difference between the two APP sensor signals is more than 0.27 V at part load.

The difference between the two APP sensor signals is more than 0.27 V at part load.

- Engine speed check The difference between the two engine speeds is 320 rpm or more and the counter counts at least 8 times.

The difference between the two engine speeds is 320 rpm or more and the counter counts at least 8 times.

- Monitoring of mixture correction factor and relative fuel mass Either of the symptoms occurs:

Either of the symptoms occurs:

- - Mixture correction factor is more than 1.27. - The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- - Mixture correction factor is more than 1.27.

Mixture correction factor is more than 1.27.

- - The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- Monitoring of injection cut-off and ignition cut-off The engine speed is too high during injection cut off or ignition cut off.

The engine speed is too high during injection cut off or ignition cut off.
````

## Chunk 5683: DTC P060C (K20C1) (2019 2020 2021)

- Title: DTC P060C (K20C1) (2019 2020 2021)
- Source path: `pages\6819.html`
- Chunk ID: `chunk_5c7c58c55cfb`
- Images: none
- Duplicate sources: `pages\8406.html`, `pages\22912.html`, `pages\21325.html`

### Full Text

````text
- The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- - Mixture correction factor is more than 1.27.

Mixture correction factor is more than 1.27.

- - The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

The reference value of the relative fuel mass of the function monitoring is less than a minimum calibrated threshold or greater than maximum calibrated threshold.

- Monitoring of injection cut-off and ignition cut-off The engine speed is too high during injection cut off or ignition cut off.

The engine speed is too high during injection cut off or ignition cut off.

- Lambda value check The desired lambda value is less than 0.7, or greater than 1. 2.

The desired lambda value is less than 0.7, or greater than 1. 2.

- Starter driver IC check The starter driver are activated but redundancy control side does not permit engine start.

The starter driver are activated but redundancy control side does not permit engine start.

- Engine torque check The current engine torque is greater than the maximum allowed engine torque at least 13 times.

The current engine torque is greater than the maximum allowed engine torque at least 13 times.

- Ignition angle check The ignition angle value and the complement of the ignition angle value are not identical at least 16 times.

The ignition angle value and the complement of the ignition angle value are not identical at least 16 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5684: DTC P060D (K20C1) (2017 2018 2019)

- Title: DTC P060D (K20C1) (2017 2018 2019)
- Source path: `pages\6820.html`
- Chunk ID: `chunk_9377883a5a95`
- Images: none
- Duplicate sources: `pages\8407.html`, `pages\22913.html`, `pages\21326.html`

### Full Text

````text
# DTC P060D (K20C1) (2017 2018 2019)

DTC P060D: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

The powertrain control module (PCM) monitors the analog digital (A/D) converter of the microcontroller. The monitoring of the A/D converter is done by means of a low voltage test impulse and a voltage test out of range. If the A/D converter voltage is out of normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.15 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Low voltage test impulse

Condition

Vehicle | ON mode

Other | A/D converter input forced to low level

Voltage test out of range

Condition

Vehicle | ON mode

Malfunction Threshold

- Low voltage test impulse The converted A/D value is greater than 0.215 V for at least 0.15 second.

The converted A/D value is greater than 0.215 V for at least 0.15 second.

- Voltage test out of range The A/D converter test voltage is greater than 4.8291 V, or less than 4.7266 V for at least 0.15 second.

The A/D converter test voltage is greater than 4.8291 V, or less than 4.7266 V for at least 0.15 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5685: DTC P060D (K20C1) (2019 2020 2021)

- Title: DTC P060D (K20C1) (2019 2020 2021)
- Source path: `pages\6821.html`
- Chunk ID: `chunk_9dfe18bd81f7`
- Images: none
- Duplicate sources: `pages\8408.html`, `pages\22914.html`, `pages\21327.html`

### Full Text

````text
# DTC P060D (K20C1) (2019 2020 2021)

DTC P060D: Powertrain Control Module (PCM) Internal Control Module Malfunction

General Description

The powertrain control module (PCM) monitors the analog digital (A/D) converter of the microcontroller. The monitoring of the A/D converter is done by means of a low voltage test impulse and a voltage test out of range. If the A/D converter voltage is out of normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more*, 0.15 second or more**

DTC Type | One drive cycle, MIL on

*: Case 1

**: Case 2

Enable Conditions

Case 1

Condition

Vehicle | ON mode

Other | A/D converter input forced to low level

Case 2

Condition

Vehicle | ON mode

Malfunction Threshold

- Case 1 The measured voltage at the A/D converter for accelerator pedal position (APP) sensor 2 signal is greater than 0.22 V.

The measured voltage at the A/D converter for accelerator pedal position (APP) sensor 2 signal is greater than 0.22 V.

- Case 2 The A/D converter test voltage is greater than 4.83 V, or less than 4.73 V.

The A/D converter test voltage is greater than 4.83 V, or less than 4.73 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5686: DTC P0615 (K20C1) (2017 2018 2019)

- Title: DTC P0615 (K20C1) (2017 2018 2019)
- Source path: `pages\6822.html`
- Chunk ID: `chunk_521c69d616aa`
- Images: `images\GHH403217.jpeg`
- Duplicate sources: `pages\8409.html`, `pages\22915.html`, `pages\21328.html`

### Full Text

````text
# DTC P0615 (K20C1) (2017 2018 2019)

DTC P0615: Starter Cut Relay Diagnosis Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. If the voltage of starter cut relay diagnostic line is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) output voltage [Starter Cut Relay] is between 2.14 V to 3.01 V for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line open

- Starter cut relay 1 circuit failure

- Starter cut relay 2 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5687: DTC P0615 (K20C1) (2019 2020 2021)

- Title: DTC P0615 (K20C1) (2019 2020 2021)
- Source path: `pages\6823.html`
- Chunk ID: `chunk_4ba5b5a81e73`
- Images: `images\GHH403218.jpeg`
- Duplicate sources: `pages\8410.html`, `pages\22916.html`, `pages\21329.html`

### Full Text

````text
# DTC P0615 (K20C1) (2019 2020 2021)

DTC P0615: Starter Cut Relay Diagnosis Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. The testing of starter cut relay circuit fault is done when both relays are powered during start. If the voltage of starter cut relay diagnostic line is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

Starter cut relay 1 circuit power stage | Active

Starter cut relay 2 circuit power stage | Active

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) input voltage [Starter Cut Relay] is between 2.14 V to 3.01 V for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line open

- Starter cut relay 1 circuit failure

- Starter cut relay 2 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5688: DTC P0615 (K20C2: With Keyless Access System)

- Title: DTC P0615 (K20C2: With Keyless Access System)
- Source path: `pages\6824.html`
- Chunk ID: `chunk_6b93f70050f2`
- Images: `images\GHH403219.jpeg`
- Duplicate sources: `pages\8411.html`, `pages\22917.html`, `pages\21330.html`

### Full Text

````text
# DTC P0615 (K20C2: With Keyless Access System)

DTC P0615: Starter Cut Relay Diagnosis Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) input does not exceed the upper and lower limits for a specified duration when the starter is ON (STS ON), the PCM detects an OPEN malfunction of the diagnosis line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is between 2.4 V to 2.6 V for at least 0.3 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY 1 TO 2 line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5689: DTC P0615 (L15B7/L15BA)

- Title: DTC P0615 (L15B7/L15BA)
- Source path: `pages\6825.html`
- Chunk ID: `chunk_c5f2d24d209f`
- Images: `images\GHH403220.jpeg`
- Duplicate sources: `pages\8412.html`, `pages\22918.html`, `pages\21331.html`

### Full Text

````text
# DTC P0615 (L15B7/L15BA)

DTC P0615: Starter Cut Relay Diagnosis Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) input does not exceed the upper and lower limits for a specified duration when the starter is ON (STS ON), the PCM detects an OPEN malfunction of the diagnosis line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is between 2.4 V to 2.6 V for at least 0.3 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay ST RLY 1 TO 2 line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5690: DTC P0616 (K20C1) (2017 2018 2019)

- Title: DTC P0616 (K20C1) (2017 2018 2019)
- Source path: `pages\6826.html`
- Chunk ID: `chunk_ba3fe1d1910d`
- Images: `images\GHH403221.jpeg`
- Duplicate sources: `pages\8413.html`, `pages\22919.html`, `pages\21332.html`

### Full Text

````text
# DTC P0616 (K20C1) (2017 2018 2019)

DTC P0616: Starter Cut Relay Diagnosis Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. If the voltage of starter cut relay diagnostic line is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) output voltage [Starter Cut Relay] is 2.14 V or less for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line short to ground

- Starter cut relay 2 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5691: DTC P0616 (K20C1) (2019 2020 2021)

- Title: DTC P0616 (K20C1) (2019 2020 2021)
- Source path: `pages\6827.html`
- Chunk ID: `chunk_9e4962734d08`
- Images: `images\GHH403222.jpeg`
- Duplicate sources: `pages\8414.html`, `pages\22920.html`, `pages\21333.html`

### Full Text

````text
# DTC P0616 (K20C1) (2019 2020 2021)

DTC P0616: Starter Cut Relay Diagnosis Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. The testing of stuck starter cut relays are done by measuring the voltage at the starter cut relays when the starter is not active. If the voltage of starter cut relay diagnostic line is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

Starter cut relay 1 circuit power stage | Active

Starter cut relay 2 circuit power stage | Active

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) input voltage [Starter Cut Relay] is 2.14 V or less for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line short to ground

- Starter cut relay 2 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5692: DTC P0616 (K20C2: With Keyless Access System)

- Title: DTC P0616 (K20C2: With Keyless Access System)
- Source path: `pages\6828.html`
- Chunk ID: `chunk_6613fb261e97`
- Images: `images\GHH403223.jpeg`
- Duplicate sources: `pages\8415.html`, `pages\22921.html`, `pages\21334.html`

### Full Text

````text
# DTC P0616 (K20C2: With Keyless Access System)

DTC P0616: Starter Cut Relay Diagnosis Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) is a specified voltage for a set time when the starter is OFF (STS OFF), the PCM detects an ON malfunction of starter cut relay 2 circuit and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is less than 2.2 V for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ON failure

- Starter cut relay circuit ST RLY 1 TO 2 line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5693: DTC P0616 (L15B7/L15BA)

- Title: DTC P0616 (L15B7/L15BA)
- Source path: `pages\6829.html`
- Chunk ID: `chunk_9173169f028d`
- Images: `images\GHH403224.jpeg`
- Duplicate sources: `pages\8416.html`, `pages\22922.html`, `pages\21335.html`

### Full Text

````text
# DTC P0616 (L15B7/L15BA)

DTC P0616: Starter Cut Relay Diagnosis Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) is a specified voltage for a set time when the starter is OFF (STS OFF), the PCM detects an ON malfunction of starter cut relay 2 circuit and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is 2.2 V or less for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ON failure

- Starter cut relay circuit ST RLY 1 TO 2 line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5694: DTC P0617 (K20C1) (2017 2018 2019)

- Title: DTC P0617 (K20C1) (2017 2018 2019)
- Source path: `pages\6830.html`
- Chunk ID: `chunk_12b570d10967`
- Images: `images\GHH403225.jpeg`
- Duplicate sources: `pages\8417.html`, `pages\22923.html`, `pages\21336.html`

### Full Text

````text
# DTC P0617 (K20C1) (2017 2018 2019)

DTC P0617: Starter Cut Relay Diagnosis Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. If the voltage of starter cut relay diagnostic line is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) output voltage [Starter Cut Relay] is 3.01 V or more for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line short to power

- Starter cut relay 1 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5695: DTC P0617 (K20C1) (2019 2020 2021)

- Title: DTC P0617 (K20C1) (2019 2020 2021)
- Source path: `pages\6831.html`
- Chunk ID: `chunk_55a54b9eef92`
- Images: `images\GHH403226.jpeg`
- Duplicate sources: `pages\8418.html`, `pages\22924.html`, `pages\21337.html`

### Full Text

````text
# DTC P0617 (K20C1) (2019 2020 2021)

DTC P0617: Starter Cut Relay Diagnosis Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis of the starter cut relays are done at the engine starting operation with enable conditions for the diagnosis are fulfilled. To check both starter cut relays, the switching off sequence of the driver ICs are changed at the end of every starter operation. The testing of stuck starter cut relays are done by measuring the voltage at the starter cut relays when the starter is not active. If the voltage of starter cut relay diagnostic line is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8.0 V | -

State of the engine | Running

Starter cut relay 1 circuit power stage | Active

Starter cut relay 2 circuit power stage | Active

[ ]: HDS Parameter

Malfunction Threshold

The diagnosis line (ST RLY1 TO 2) input voltage [Starter Cut Relay] is 3.01 V or more for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay circuit ST RLY1 TO 2 line short to power

- Starter cut relay 1 circuit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5696: DTC P0617 (K20C2: USA/Canada models with Keyless Access System)

- Title: DTC P0617 (K20C2: USA/Canada models with Keyless Access System)
- Source path: `pages\6832.html`
- Chunk ID: `chunk_ea67a7acb2e5`
- Images: `images\GHH403227.jpeg`
- Duplicate sources: `pages\8419.html`, `pages\22925.html`, `pages\21338.html`

### Full Text

````text
# DTC P0617 (K20C2: USA/Canada models with Keyless Access System)

DTC P0617: Starter Cut Relay Diagnosis Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) is a specified voltage for a set time when the starter is OFF (STS OFF), the PCM detects an ON malfunction of starter cut relay 1 circuit and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is more than 3.20 V for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ON failure

- Starter cut relay circuit ST RLY 1 TO 2 line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5697: DTC P0617 (L15B7/L15BA)

- Title: DTC P0617 (L15B7/L15BA)
- Source path: `pages\6833.html`
- Chunk ID: `chunk_d7339451a217`
- Images: `images\GHH403228.jpeg`
- Duplicate sources: `pages\8420.html`, `pages\22926.html`, `pages\21339.html`

### Full Text

````text
# DTC P0617 (L15B7/L15BA)

DTC P0617: Starter Cut Relay Diagnosis Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the voltage of the diagnosis line (ST RLY 1 TO 2) is a specified voltage for a set time when the starter is OFF (STS OFF), the PCM detects an ON malfunction of starter cut relay 1 circuit and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The diagnosis line (ST RLY 1 TO 2) input voltage [STARTER CUT RELAY] is 3.20 V or more for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ON failure

- Starter cut relay circuit ST RLY 1 TO 2 line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5698: DTC P061B (K20C2)

- Title: DTC P061B (K20C2)
- Source path: `pages\6834.html`
- Chunk ID: `chunk_50b3c96f3ad4`
- Images: `images\GHH403229.jpeg`, `images\GHH403230.jpeg`, `images\GHH403231.jpeg`
- Duplicate sources: `pages\8421.html`, `pages\22927.html`, `pages\21340.html`

### Full Text

````text
# DTC P061B (K20C2)

DTC P061B: Powertrain Control Module (PCM) Internal Malfunction (Torque Calculation)

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) calculates the target torque from the accelerator pedal inputs, external demands, and auxiliary load information, and calculates the allowable torque of up to acceleration state leads to hazardous event for the target torque. Abnormal accelerations are detected by the relations of the target torque, the allowable torque, and the torque estimated from engine output command. There are two methods to detect abnormal accelerations; time judgment method and integration judgment method. If both of the methods are judged abnormal, the PCM detects a malfunction and stores a DTC.

- Time judgment method: Malfunction is established if the estimated torque is higher than the target torque for a specified time. The allowable time changes depending on the difference width between the estimated torque and the allowable torque.

- Integration judgment method: Malfunction is established if the integration value of torque difference exceeds a threshold.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on the driving conditions

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 1, 600 rpm | -

Accelerator pedal position | - | 0.2 %

[ ]: HDS Parameter

Malfunction Threshold

Both of the conditions occur:

- The estimated torque is higher than the target torque.

- Integration value of difference between the estimated torque and target torque exceeds a threshold.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle under Enable Conditions (see "Engine speed [ENGINE SPEED]"and "Accelerator pedal position").

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5699: DTC P061B (Si) (2017 2018 2019 2020 2021)

- Title: DTC P061B (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6835.html`
- Chunk ID: `chunk_c8e386f6b2a3`
- Images: `images\GHH403232.jpeg`, `images\GHH403233.jpeg`, `images\GHH403234.jpeg`
- Duplicate sources: `pages\8422.html`, `pages\22928.html`, `pages\21341.html`

### Full Text

````text
# DTC P061B (Si) (2017 2018 2019 2020 2021)

DTC P061B: Powertrain Control Module (PCM) Internal Malfunction (Torque Calculation)

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) calculates the target torque from the accelerator pedal inputs, external demands, and auxiliary load information, and calculates the allowable torque of up to acceleration state leads to hazardous event for the target torque. Abnormal accelerations are detected by the relations of the target torque, the allowable torque, and the torque estimated from engine output command. There are two methods to detect abnormal accelerations; time judgment method and integration judgment method. If both of the methods are judged abnormal, the PCM detects a malfunction and stores a DTC.

- Time judgment method: Malfunction is established if the estimated torque is higher than the target torque for a specified time. The allowable time changes depending on the difference width between the estimated torque and the allowable torque.

- Integration judgment method: Malfunction is established if the integration value of torque difference exceeds a threshold.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on the driving conditions

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 1, 900 rpm | -

Accelerator pedal position | - | 0.2 %

[ ]: HDS Parameter

Malfunction Threshold

Both of the conditions occur:

- The estimated torque is higher than the target torque.

- Integration value of difference between the estimated torque and target torque exceeds a threshold.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle under Enable Conditions (see "Engine speed [ENGINE SPEED]"and "Accelerator pedal position").

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5700: DTC P061B (Without XM)

- Title: DTC P061B (Without XM)
- Source path: `pages\6836.html`
- Chunk ID: `chunk_67903f58004b`
- Images: `images\GHH403235.jpeg`, `images\GHH403236.jpeg`, `images\GHH403237.jpeg`
- Duplicate sources: `pages\8423.html`, `pages\22929.html`, `pages\21342.html`

### Full Text

````text
# DTC P061B (Without XM)

DTC P061B: Powertrain Control Module (PCM) Internal Malfunction (Torque Calculation)

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) calculates the target torque from the accelerator pedal inputs, external demands, and auxiliary load information, and calculates the allowable torque of up to acceleration state leads to hazardous event for the target torque. Abnormal accelerations are detected by the relations of the target torque, the allowable torque, and the torque estimated from engine output command. There are two methods to detect abnormal accelerations; time judgment method and integration judgment method. If both of the methods are judged abnormal, the PCM detects a malfunction and stores a DTC.

- Time judgment method: Malfunction is established if the estimated torque is higher than the target torque for a specified time. The allowable time changes depending on the difference width between the estimated torque and the allowable torque.

- Integration judgment method: Malfunction is established if the integration value of torque difference exceeds a threshold.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Depending on the driving conditions

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Accelerator pedal position | - | 0.2 %

[ ]: HDS Parameter

Malfunction Threshold

Both of the conditions occur:

- The estimated torque is higher than the target torque.

- Integration value of difference between the estimated torque and target torque exceeds a threshold.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle under Enable Conditions (see "Engine speed [ENGINE SPEED]"and "Accelerator pedal position").

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5701: DTC P062B (L15B7/L15BA/L15BY)

- Title: DTC P062B (L15B7/L15BA/L15BY)
- Source path: `pages\6837.html`
- Chunk ID: `chunk_fd93d25299f0`
- Images: `images\GHH403238.jpeg`
- Duplicate sources: `pages\8424.html`, `pages\22930.html`, `pages\21343.html`

### Full Text

````text
# DTC P062B (L15B7/L15BA/L15BY)

DTC P062B: Powertrain Control Module (PCM) Internal Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The injector supplies fuel to the engine and its fuel pressure is adjusted by high pressure fuel pump output duty cycle, and controlled by the powertrain control module (PCM) ON/OFF command. In the PCM, the injector driver receives commands from the CPU and drives injectors and solenoids. Also, the CPU sets current to drive injectors and solenoids, and transmits the current to the injector driver. If an abnormal communication occurs in the PCM, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 7 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The CPU cannot communicate with injector driver at least 100 times (counts once per 30 deg. camshaft angle).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5702: DTC P062F(K20C2 (PGM-FI System))

- Title: DTC P062F(K20C2 (PGM-FI System))
- Source path: `pages\6838.html`
- Chunk ID: `chunk_4f5e35656aa0`
- Images: `images\GHH403239.jpeg`
- Duplicate sources: `pages\8425.html`, `pages\22931.html`, `pages\21344.html`

### Full Text

````text
# DTC P062F(K20C2 (PGM-FI System))

DTC P062F: Powertrain Control Module (PCM) Internal Control Module Keep Alive Memory (KAM) Error

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with an electrically erasable programmable read-only memory (EEPROM). The data (control learn data, etc.) for powertrain control and information (vehicle identification number (VIN), etc.) related to the vehicle control is stored in the EEPROM, so that it can be maintained even when power is not supplied to the PCM, such as when the 12 volt battery is disconnected. When powered up, the CPU retrieves the stored information from the EEPROM, as well as writes data to the EEPROM (control related data is written when the vehicle is turned to the ON mode, and vehicle information when commanded from the HDS). When the data retrieval or data writing process is not finished normally, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

A malfunction is detected whenever the EEPROM data retrieval and writing process is not completed normally.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5703: DTC P062F (L15B7 (PGM-FI System))

- Title: DTC P062F (L15B7 (PGM-FI System))
- Source path: `pages\6839.html`
- Chunk ID: `chunk_704a4d51eb09`
- Images: `images\GHH403240.jpeg`
- Duplicate sources: `pages\8426.html`, `pages\22932.html`, `pages\21345.html`

### Full Text

````text
# DTC P062F (L15B7 (PGM-FI System))

DTC P062F: Powertrain Control Module (PCM) Internal Control Module Keep Alive Memory (KAM) Error

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with an electrically erasable programmable read-only memory (EEPROM). The data (control learn data, etc.) for powertrain control and information (vehicle identification number (VIN), etc.) related to the vehicle control is stored in the EEPROM, so that it can be maintained even when power is not supplied to the PCM, such as when the 12 volt battery is disconnected. When powered up, the CPU retrieves the stored information from the EEPROM, as well as writes data to the EEPROM (control related data is written when the vehicle is turned to the ON mode, and vehicle information when commanded from the HDS). When the data retrieval or data writing process is not finished normally, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

A malfunction is detected whenever the EEPROM data retrieval and writing process is not completed normally.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5704: DTC P0630 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P0630 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\6840.html`
- Chunk ID: `chunk_5a729b6b9a59`
- Images: none
- Duplicate sources: `pages\8427.html`, `pages\22933.html`, `pages\21346.html`

### Full Text

````text
# DTC P0630 (K20C1) (2017 2018 2019 2020 2021)

DTC P0630: VIN Not Programmed or Mismatch

General Description

The DTC P0630 is set before vehicle identification number (VIN) is written and resets after VIN is written. Testing is done by carrying out the VIN write process. This test can be done only after EEPROM first initialization is performed. If the VIN is not registered or incompatible, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Other | EEPROM first initialization has been performed

Malfunction Threshold

The VIN is not registered or incompatible.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VIN not registered in the PCM

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

When the VIN registration is completed, the MIL is cleared.
````

## Chunk 5705: DTC P0630 (K20C2)

- Title: DTC P0630 (K20C2)
- Source path: `pages\6841.html`
- Chunk ID: `chunk_106d9b61aeef`
- Images: `images\GHH403241.jpeg`
- Duplicate sources: `pages\8428.html`, `pages\22934.html`, `pages\21347.html`

### Full Text

````text
# DTC P0630 (K20C2)

DTC P0630: VIN Not Programmed or Mismatch

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) stores a vehicle identification number (VIN) in the electrically erasable programmable read-only memory (EEPROM) and outputs the VIN according to commands from the HDS. The VIN for each vehicle is registered to the PCM using the HDS. The registered VIN is read by the CPU from the EEPROM after the vehicle is turned to the ON mode or after the Clear command is executed. If the VIN is not registered in the EEPROM when the vehicle is turned to the ON mode or when the Clear command is executed, the PCM detects a VIN unregistered condition and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or less

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The VIN is not registered in the EEPROM in the PCM.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VIN not registered in the PCM EEPROM

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

When the VIN registration is completed, the MIL is cleared.
````

## Chunk 5706: DTC P0630 (L15B7/L15BA)

- Title: DTC P0630 (L15B7/L15BA)
- Source path: `pages\6842.html`
- Chunk ID: `chunk_88d4fab28464`
- Images: `images\GHH403242.jpeg`
- Duplicate sources: `pages\8429.html`, `pages\22935.html`, `pages\21348.html`

### Full Text

````text
# DTC P0630 (L15B7/L15BA)

DTC P0630: VIN Not Programmed or Mismatch

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) stores a vehicle identification number (VIN) in the electrically erasable programmable read-only memory (EEPROM) and outputs the VIN according to commands from the HDS. The VIN for each vehicle is registered to the PCM using the HDS. The registered VIN is read by the CPU from the EEPROM after the vehicle is turned to the ON mode or after the Clear command is executed. If the VIN is not registered in the EEPROM when the vehicle is turned to the ON mode or when the Clear command is executed, the PCM detects a VIN unregistered condition and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or less

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The VIN is not registered in the EEPROM in the PCM.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VIN not registered in the PCM EEPROM

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

When the VIN registration is completed, the MIL is cleared.
````

## Chunk 5707: DTC P0641 (K20C1 (PGM-FI System)) (2017 2018 2019 2020 2021)

- Title: DTC P0641 (K20C1 (PGM-FI System)) (2017 2018 2019 2020 2021)
- Source path: `pages\6843.html`
- Chunk ID: `chunk_2910b97d14b6`
- Images: none
- Duplicate sources: `pages\8430.html`, `pages\22936.html`, `pages\21349.html`

### Full Text

````text
# DTC P0641 (K20C1 (PGM-FI System)) (2017 2018 2019 2020 2021)

DTC P0641: Sensor Reference Voltage A Malfunction

General Description

The powertrain control module (PCM) provides power supply voltages for the sensors. The monitoring function checks this sensor supply voltages (outputs) and compares it with minimum and maximum thresholds. The PCM contains a linear voltage regulator (5V) to provide a reference voltage. The monitoring function checks the provided sensor supply voltages against the reference voltage. If the sensor power supply voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.15 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power supply voltage is less than 4.8 V, or greater than 5.2 V for at least 0.15 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel rail pressure sensor VCC line short to power

- Crankshaft position (CKP) sensor VCC line short to power

- Camshaft position (CMP) sensor B VCC line short to power

- Neutral position sensor VCC line short to power

- Mass airflow (MAF) sensor/intake air temperature (IAT) sensor 1 VCC line short to power

- Throttle body VCC line short to power

- Acceleration pedal position (APP) sensor VCC line short to power

- Camshaft position (CMP) sensor A VCC line short to power

- Input shaft (mainshaft) speed sensor VCC line short to power

- Output shaft (countershaft) speed sensor VCC line short to power

- Turbocharger boost sensor VCC line short to power

- Manifold absolute pressure (MAP) sensor/intake air temperature (IAT) sensor 2 VCC line short to power

- Rocker arm oil pressure sensor VCC line short to power

- Turbocharger VCC line short to power

- A/C pressure sensor VCC line short to power

- Fuel tank pressure (FTP) sensor VCC line short to power* 1

- Fuel rail pressure sensor VCC line short to ground

- CKP sensor VCC line short to ground

- CMP sensor B VCC line short to ground

- Neutral position sensor VCC line short to ground

- MAF sensor/IAT sensor 1 VCC line short to ground

- Throttle body VCC line short to ground

- APP sensor VCC line short to ground

- CMP sensor A VCC line short to ground

- Input shaft (mainshaft) speed sensor VCC line short to ground

- Output shaft (countershaft) speed sensor VCC line short to ground

- Turbocharger boost sensor VCC line short to ground

- MAP sensor/IAT sensor 2 VCC line short to ground

- Rocker arm oil pressure sensor VCC line short to ground

- Turbocharger VCC line short to ground

- A/C pressure sensor VCC line short to ground

- FTP sensor VCC line short to ground* 1

- PCM internal circuit failure

*1: USA/Canada

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5708: DTC P0641 (K20C2 (PGM-FI System))

- Title: DTC P0641 (K20C2 (PGM-FI System))
- Source path: `pages\6844.html`
- Chunk ID: `chunk_84f584f68d15`
- Images: `images\GHH403243.jpeg`
- Duplicate sources: `pages\8431.html`, `pages\22937.html`, `pages\21350.html`

### Full Text

````text
# DTC P0641 (K20C2 (PGM-FI System))

DTC P0641: Sensor Reference Voltage A Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with a voltage monitor (5 V power source) to supply a stable 5 V to each sensor as reference voltage. The correct voltage for the sensors are loaded in the CPU of the PCM (A/D input) and when the sensor power voltage is a set value (high or low) for a certain time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power voltage is 6.00 V or more, or 3.99 V or less, for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Manifold absolute pressure (MAP) sensor VCC line short to power

- Output shaft (countershaft) speed sensor VCC line short to power* 1

- Crankshaft position (CKP) sensor VCC line short to power

- Throttle body VCC line short to power

- Accelerator pedal position (APP) sensor VCC line short to power

- MAP sensor VCC line short to ground

- Output shaft (countershaft) speed sensor VCC line short to ground* 1

- CKP sensor VCC line short to ground

- Throttle body VCC line short to ground

- APP sensor VCC line short to ground

- PCM internal circuit failure

*1: M/T model

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5709: DTC P0641 (L15B7/L15BA/L15BY (PGM-FI System))

- Title: DTC P0641 (L15B7/L15BA/L15BY (PGM-FI System))
- Source path: `pages\6845.html`
- Chunk ID: `chunk_51289fce3e45`
- Images: `images\GHH403244.jpeg`
- Duplicate sources: `pages\8432.html`, `pages\22938.html`, `pages\21351.html`

### Full Text

````text
# DTC P0641 (L15B7/L15BA/L15BY (PGM-FI System))

DTC P0641: Sensor Reference Voltage A Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with a voltage monitor (5 V power source) to supply a stable 5 V to each sensor as reference voltage. The correct voltage for the sensors are loaded in the CPU of the PCM (A/D input) and when the sensor power voltage is a set value (high or low) for a certain time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power voltage is 6.00 V or more, or 3.99 V or less, for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Manifold absolute pressure (MAP) sensor VCC line short to power

- Fuel rail pressure sensor VCC line short to power

- Crankshaft position (CKP) sensor VCC line short to power

- Throttle body VCC line short to power

- Accelerator pedal position (APP) sensor VCC line short to power

- Output shaft (countershaft) speed sensor VCC line short to power* 1

- MAP sensor VCC line short to ground

- Fuel rail pressure sensor VCC line short to ground

- CKP sensor VCC line short to ground

- Throttle body VCC line short to ground

- APP sensor VCC line short to ground

- Output shaft (countershaft) speed sensor VCC line short to ground* 1

- PCM internal circuit failure

*1: M/T model

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5710: DTC P0651 (K20C2 (PGM-FI System))

- Title: DTC P0651 (K20C2 (PGM-FI System))
- Source path: `pages\6846.html`
- Chunk ID: `chunk_f4ec60204042`
- Images: `images\GHH403245.jpeg`
- Duplicate sources: `pages\8433.html`, `pages\22939.html`, `pages\21352.html`

### Full Text

````text
# DTC P0651 (K20C2 (PGM-FI System))

DTC P0651: Sensor Reference Voltage B Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with a voltage monitor (5 V power source) to supply a stable 5 V to each sensor as reference voltage. The correct voltage for the sensors are loaded in the CPU of the PCM (A/D input) and when the sensor power voltage is a set value (high or low) for a certain time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power voltage is 6.00 V or more, or 3.99 V or less, for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/C pressure sensor VCC line short to power* 1

- Accelerator pedal position (APP) sensor VCC line short to power

- Mass airflow (MAF) sensor/intake air temperature (IAT) sensor VCC line short to power

- Neutral position sensor VCC line short to power* 2

- Fuel tank pressure (FTP) sensor VCC line short to power* 3

- Camshaft position (CMP) sensor A VCC line short to power

- Camshaft position (CMP) sensor B VCC line short to power

- A/C pressure sensor VCC line short to ground* 1

- APP sensor VCC line short to ground

- MAF sensor/IAT sensor VCC line short to ground

- Neutral position sensor VCC line short to ground* 2

- FTP sensor VCC line short to ground* 3

- CMP sensor A VCC line short to ground

- CMP sensor B VCC line short to ground

- PCM internal circuit failure

*1: With A/C

*2: M/T model

*3: USA and Canada models

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5711: DTC P0651 (L15B7 (except Si)/L15BA/L15BY (PGM-FI System))

- Title: DTC P0651 (L15B7 (except Si)/L15BA/L15BY (PGM-FI System))
- Source path: `pages\6847.html`
- Chunk ID: `chunk_f484bde10986`
- Images: `images\GHH403246.jpeg`
- Duplicate sources: `pages\8434.html`, `pages\22940.html`, `pages\21353.html`

### Full Text

````text
# DTC P0651 (L15B7 (except Si)/L15BA/L15BY (PGM-FI System))

DTC P0651: Sensor Reference Voltage B Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with a voltage monitor (5 V power source) to supply a stable 5 V to each sensor as reference voltage. The correct voltage for the sensors are loaded in the CPU of the PCM (A/D input) and when the sensor power voltage is a set value (high or low) for a certain time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power voltage is 6.00 V or more, or 3.99 V or less, for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/C pressure sensor VCC line short to power

- Accelerator pedal position (APP) sensor VCC line short to power

- Turbocharger VCC line short to power

- Turbocharger boost sensor VCC line short to power

- Camshaft position (CMP) sensor A VCC line short to power

- Camshaft position (CMP) sensor B VCC line short to power

- Fuel tank pressure (FTP) sensor VCC line short to power* 1

- Neutral position sensor VCC line short to power* 2

- A/C pressure sensor VCC line short to ground

- APP sensor VCC line short to ground

- Turbocharger VCC line short to ground

- Turbocharger boost sensor VCC line short to ground

- CMP sensor A VCC line short to ground

- CMP sensor B VCC line short to ground

- FTP sensor VCC line short to ground* 1

- Neutral position sensor VCC line short to ground* 2

- PCM internal circuit failure

*1: USA and Canada models

*2: M/T model

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5712: DTC P0651 (Si (PGM-FI System)) (2017 2018 2019 2020 2021)

- Title: DTC P0651 (Si (PGM-FI System)) (2017 2018 2019 2020 2021)
- Source path: `pages\6848.html`
- Chunk ID: `chunk_b123c13a19dc`
- Images: `images\GHH403247.jpeg`
- Duplicate sources: `pages\8435.html`, `pages\22941.html`, `pages\21354.html`

### Full Text

````text
# DTC P0651 (Si (PGM-FI System)) (2017 2018 2019 2020 2021)

DTC P0651: Sensor Reference Voltage B Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) is equipped with a voltage monitor (5 V power source) to supply a stable 5 V to each sensor as reference voltage. The correct voltage for the sensors are loaded in the CPU of the PCM (A/D input) and when the sensor power voltage is a set value (high or low) for a certain time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The sensor power voltage is 6.00 V or more, or 3.99 V or less, for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/C pressure sensor VCC line short to power

- Accelerator pedal position (APP) sensor VCC line short to power

- Turbocharger VCC line short to power

- Turbocharger boost sensor VCC line short to power

- Camshaft position (CMP) sensor A VCC line short to power

- Camshaft position (CMP) sensor B VCC line short to power

- Fuel tank pressure (FTP) sensor VCC line short to power

- Neutral position sensor VCC line short to power

- Mass airflow (MAF) sensor/intake air temperature (IAT) sensor 1 VCC line short to power

- A/C pressure sensor VCC line short to ground

- APP sensor VCC line short to ground

- Turbocharger VCC line short to ground

- Turbocharger boost sensor VCC line short to ground

- CMP sensor A VCC line short to ground

- CMP sensor B VCC line short to ground

- FTP sensor VCC line short to ground

- Neutral position sensor VCC line short to ground

- MAF sensor/IAT sensor 1 VCC line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5713: DTC P0657 (K20C2)

- Title: DTC P0657 (K20C2)
- Source path: `pages\6849.html`
- Chunk ID: `chunk_7fd5ca13a34e`
- Images: `images\GHH403248.jpeg`, `images\GHH403249.jpeg`
- Duplicate sources: `pages\8436.html`, `pages\22942.html`, `pages\21355.html`

### Full Text

````text
# DTC P0657 (K20C2)

DTC P0657: Powertrain Control Module (PCM) Power Supply Circuit Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

Main CPU and driver ICs are built into the powertrain control module (PCM). The main CPU receives drive commands and driver IC drives each corresponding devices. Power for the main CPU is provided from +B BACKUP FI-ECU line via CPU power supply, and power for the driver ICs are provided from FI MAIN RLY OUT line via PGM-FI main relay 1 circuit. If the FI MAIN RLY OUT voltage is a specified voltage for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

FI MAIN RLY OUT voltage is 6.0 V or less for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit failure

- Fuse blown

- PGM-FI main relay 1 circuit FI MAIN RLY OUT line open

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5714: DTC P0657 (L15B7/L15BA)

- Title: DTC P0657 (L15B7/L15BA)
- Source path: `pages\6850.html`
- Chunk ID: `chunk_094134f964d3`
- Images: `images\GHH403250.jpeg`, `images\GHH403251.jpeg`
- Duplicate sources: `pages\8437.html`, `pages\22943.html`, `pages\21356.html`

### Full Text

````text
# DTC P0657 (L15B7/L15BA)

DTC P0657: Powertrain Control Module (PCM) Power Supply Circuit Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

Main CPU and driver ICs are built into the powertrain control module (PCM). The main CPU receives drive commands and driver IC drives each corresponding devices. Power for the main CPU is provided from +B BACKUP FI-ECU line via CPU power supply, and power for the driver ICs are provided from FI MAIN RLY OUT line via PGM-FI main relay 1 circuit. If the FI MAIN RLY OUT voltage is a specified voltage for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

FI MAIN RLY OUT voltage is 6.0 V or less for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit failure

- Fuse blown

- PGM-FI main relay 1 circuit FI MAIN RLY OUT line open

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5715: DTC P065A (K20C1) (2017 2018 2019)

- Title: DTC P065A (K20C1) (2017 2018 2019)
- Source path: `pages\6851.html`
- Chunk ID: `chunk_c973380ab22d`
- Images: `images\GHH403252.jpeg`
- Duplicate sources: `pages\8438.html`, `pages\22944.html`, `pages\21357.html`

### Full Text

````text
# DTC P065A (K20C1) (2017 2018 2019)

DTC P065A: ACG No Charging Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The voltage regulator in the alternator self-diagnoses itself, and by the PCM demands, the results are transmitted via the LIN line. If mechanical or electrical error is reported from the alternator, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The alternator reports mechanical or electrical error to the PCM via the LIN for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator internal failure (voltage regulator failure)

- Alternator rotation defection

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5716: DTC P065A (K20C1) (2019 2020 2021)

- Title: DTC P065A (K20C1) (2019 2020 2021)
- Source path: `pages\6852.html`
- Chunk ID: `chunk_6796a4b1e1f2`
- Images: `images\GHH403253.jpeg`
- Duplicate sources: `pages\8439.html`, `pages\22945.html`, `pages\21358.html`

### Full Text

````text
# DTC P065A (K20C1) (2019 2020 2021)

DTC P065A: ACG No Charging Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) continuously monitors the alternator via the local interconnect network (LIN) line. If the PCM receives information during the engine is running that the alternator is not generating a power nor rotating, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Electrical or mechanical fault of the alternator is reported via the LIN.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5717: DTC P065A (K20C2)

- Title: DTC P065A (K20C2)
- Source path: `pages\6853.html`
- Chunk ID: `chunk_6b966267d442`
- Images: `images\GHH403254.jpeg`
- Duplicate sources: `pages\8440.html`, `pages\22946.html`, `pages\21359.html`

### Full Text

````text
# DTC P065A (K20C2)

DTC P065A: ACG No Charging Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The voltage regulator in the alternator self-diagnoses itself, and by the PCM demands, the results are transmitted via the LIN line. If the self-diagnosed results are judged as generation unable or alternator rotation stop, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 60 seconds:

- B terminal voltage is regulated voltage or more, and F terminal voltage is HIGH.

- B terminal voltage is 10 V or less (when the alternator speed is 3, 000 rpm or less), or 11 V or less (when the alternator speed is 3, 000 rpm or more).

- P terminal voltage is 2 V or less (when the alternator speed is 3, 000 rpm or less), or 6 V or less (when the alternator speed is 3, 000 rpm or more).

- Alternator speed is 400 rpm or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator internal failure (voltage regulator failure)

- Alternator rotation defection

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5718: DTC P065A (L15B7/L15BA)

- Title: DTC P065A (L15B7/L15BA)
- Source path: `pages\6854.html`
- Chunk ID: `chunk_f3bb231df846`
- Images: `images\GHH403255.jpeg`
- Duplicate sources: `pages\8441.html`, `pages\22947.html`, `pages\21360.html`

### Full Text

````text
# DTC P065A (L15B7/L15BA)

DTC P065A: ACG No Charging Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The voltage regulator in the alternator self-diagnoses itself, and by the PCM demands, the results are transmitted via the LIN line. If the self-diagnosed results are judged as generation unable or alternator rotation stop, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 60 seconds:

- B terminal voltage is regulated voltage or more, and F terminal voltage is HIGH.

- B terminal voltage is 10 V or less (when the alternator speed is 3, 000 rpm or less), or 11 V or less (when the alternator speed is 3, 000 rpm or more).

- P terminal voltage is 2 V or less (when the alternator speed is 3, 000 rpm or less), or 6 V or less (when the alternator speed is 3, 000 rpm or more).

- Alternator speed is 400 rpm or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator internal failure (voltage regulator failure)

- Alternator rotation defection

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5719: DTC P0685 (K20C1) (2017 2018 2019)

- Title: DTC P0685 (K20C1) (2017 2018 2019)
- Source path: `pages\6855.html`
- Chunk ID: `chunk_05c9d4405b53`
- Images: `images\GHH403256.jpeg`
- Duplicate sources: `pages\8442.html`, `pages\22948.html`, `pages\21361.html`

### Full Text

````text
# DTC P0685 (K20C1) (2017 2018 2019)

DTC P0685: A/F Sensor (Sensor 1) Heater Power Source Circuit Open

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the A/F sensor (sensor 1) heater output voltage is within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | OFF

[ ]: HDS Parameter

Malfunction Threshold

The A/F sensor (sensor 1) heater output voltage is within a range of 3 V to 5 V while the A/F sensor (sensor 1) heater is switched off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) heater failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5720: DTC P0685 (K20C1) (2019 2020 2021)

- Title: DTC P0685 (K20C1) (2019 2020 2021)
- Source path: `pages\6856.html`
- Chunk ID: `chunk_f15a3ff0daa4`
- Images: `images\GHH403257.jpeg`
- Duplicate sources: `pages\8443.html`, `pages\22949.html`, `pages\21362.html`

### Full Text

````text
# DTC P0685 (K20C1) (2019 2020 2021)

DTC P0685: A/F Sensor (Sensor 1) Heater Power Source Circuit Open

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the FI SUB RLY CL- voltage is within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | OFF

[ ]: HDS Parameter

Malfunction Threshold

The FI SUB RLY CL- voltage is within a range of 3.26 V to 4.70 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit FI SUB RLY CL- line open

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5721: DTC P0686 (K20C1) (2017 2018 2019)

- Title: DTC P0686 (K20C1) (2017 2018 2019)
- Source path: `pages\6857.html`
- Chunk ID: `chunk_245975afd20c`
- Images: `images\GHH403258.jpeg`
- Duplicate sources: `pages\8444.html`, `pages\22950.html`, `pages\21363.html`

### Full Text

````text
# DTC P0686 (K20C1) (2017 2018 2019)

DTC P0686: A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the A/F sensor (sensor 1) heater output voltage is a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | OFF

[ ]: HDS Parameter

Malfunction Threshold

The A/F sensor (sensor 1) heater output voltage is less than 3 V while the A/F sensor (sensor 1) heater is switched off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) heater failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5722: DTC P0686 (K20C1) (2019 2020 2021)

- Title: DTC P0686 (K20C1) (2019 2020 2021)
- Source path: `pages\6858.html`
- Chunk ID: `chunk_79e9e8570ff1`
- Images: `images\GHH403259.jpeg`
- Duplicate sources: `pages\8445.html`, `pages\22951.html`, `pages\21364.html`

### Full Text

````text
# DTC P0686 (K20C1) (2019 2020 2021)

DTC P0686: A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the FI SUB RLY CL- voltage is a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | OFF

[ ]: HDS Parameter

Malfunction Threshold

The FI SUB RLY CL- voltage is 2.74 or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit FI SUB RLY CL- line short to ground

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5723: DTC P0687 (K20C1) (2017 2018 2019)

- Title: DTC P0687 (K20C1) (2017 2018 2019)
- Source path: `pages\6859.html`
- Chunk ID: `chunk_0b835612086a`
- Images: `images\GHH403260.jpeg`
- Duplicate sources: `pages\8446.html`, `pages\22952.html`, `pages\21365.html`

### Full Text

````text
# DTC P0687 (K20C1) (2017 2018 2019)

DTC P0687: A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the A/F sensor (sensor 1) heater output voltage is a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | ON

[ ]: HDS Parameter

Malfunction Threshold

The A/F sensor (sensor 1) heater output voltage is greater than 0.5 A while the A/F sensor (sensor 1) heater is switched on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) heater failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5724: DTC P0687 (K20C1) (2019 2020 2021)

- Title: DTC P0687 (K20C1) (2019 2020 2021)
- Source path: `pages\6860.html`
- Chunk ID: `chunk_78b08f641633`
- Images: `images\GHH403261.jpeg`
- Duplicate sources: `pages\8447.html`, `pages\22953.html`, `pages\21366.html`

### Full Text

````text
# DTC P0687 (K20C1) (2019 2020 2021)

DTC P0687: A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the sensor element is embedded in the air/fuel ratio (A/F) sensor (sensor 1), and it is controlled and monitored by the powertrain control module (PCM). It is activated and heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the FI SUB RLY CL- current is a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Command to A/F sensor (sensor 1) heater relay | ON

[ ]: HDS Parameter

Malfunction Threshold

The FI SUB RLY CL- current is greater than 2 A.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit FI SUB RLY CL- line short to power

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5725: DTC P068A (K20C1) (2017 2018 2019)

- Title: DTC P068A (K20C1) (2017 2018 2019)
- Source path: `pages\6861.html`
- Chunk ID: `chunk_3467477d846d`
- Images: `images\GHH403262.jpeg`
- Duplicate sources: `pages\8448.html`, `pages\22954.html`, `pages\21367.html`

### Full Text

````text
# DTC P068A (K20C1) (2017 2018 2019)

DTC P068A: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors PGM-FI main relay 1 for electrical malfunctions. The early opening of PGM-FI main relay 1 is monitored by recording whether PGM-FI main relay 1 is switched off correctly at the last driving cycle. If the power supply for the PCM is interrupted for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Other | PCM switched OFF, diagnosis is running

Malfunction Threshold

The power supply for the PCM is interrupted at least 3 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 FI MAIN RLY OUT line short to ground

- PGM-FI main relay 1 FI MAIN RLY OUT line open

- PGM-FI main relay 1 FI MAIN RLY CL- line open

- Loss of energy

- Fuse blown

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5726: DTC P068A (K20C1) (2019)

- Title: DTC P068A (K20C1) (2019)
- Source path: `pages\6862.html`
- Chunk ID: `chunk_e5d1fd8761ad`
- Images: `images\GHH403263.jpeg`
- Duplicate sources: `pages\8449.html`, `pages\22955.html`, `pages\21368.html`

### Full Text

````text
# DTC P068A (K20C1) (2019)

DTC P068A: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors PGM-FI main relay 1 circuit for electrical malfunctions. The early opening of PGM-FI main relay 1 circuit is monitored by recording whether PGM-FI main relay 1 circuit is switched off correctly at the last driving cycle. If the PGM-FI main relay 1 circuit was opened without command, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle/two drive cycles*, MIL on

*: The detection drive cycle may change depending on the vehicle condition when the fault is detected.

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PGM-FI main relay 1 circuit was opened without command.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 FI MAIN RLY OUT line short to ground

- PGM-FI main relay 1 FI MAIN RLY OUT line open

- PGM-FI main relay 1 FI MAIN RLY CL- line open

- Loss of energy

- Fuse blown

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC (for one drive cycle)

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for setting the DTC (for two drive cycles)

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5727: DTC P068A (K20C1) (2020 2021)

- Title: DTC P068A (K20C1) (2020 2021)
- Source path: `pages\6863.html`
- Chunk ID: `chunk_e88f1b0bc4e6`
- Images: `images\GHH403264.jpeg`
- Duplicate sources: `pages\8450.html`, `pages\22956.html`, `pages\21369.html`

### Full Text

````text
# DTC P068A (K20C1) (2020 2021)

DTC P068A: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors PGM-FI main relay 1 circuit for electrical malfunctions. The early opening of PGM-FI main relay 1 circuit is monitored by recording whether PGM-FI main relay 1 circuit is switched off correctly at the last driving cycle. If the PGM-FI main relay 1 circuit was opened without command, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off/two drive cycles, MIL on*

*: The detection drive cycle and the MIL may change depending on the vehicle condition when the fault is detected.

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PGM-FI main relay 1 circuit was opened without command.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 FI MAIN RLY OUT line short to ground

- PGM-FI main relay 1 FI MAIN RLY OUT line open

- PGM-FI main relay 1 FI MAIN RLY CL- line open

- Loss of energy

- Fuse blown

- PCM internal circuit failure

Diagnosis Details (for one drive cycle, MIL off)

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.

Diagnosis Details (for two drive cycles, MIL on)

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5728: DTC P068B (K20C1) (2017 2018 2019)

- Title: DTC P068B (K20C1) (2017 2018 2019)
- Source path: `pages\6864.html`
- Chunk ID: `chunk_c8f0ec00bbf3`
- Images: `images\GHH403265.jpeg`
- Duplicate sources: `pages\8451.html`, `pages\22957.html`, `pages\21370.html`

### Full Text

````text
# DTC P068B (K20C1) (2017 2018 2019)

DTC P068B: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the PGM-FI main relay 1 circuit for electrical malfunctions. The driver IC of the PGM-FI main relay 1 circuit is monitored for a specified number of test pulses. If a stuck or a short to ground in the PGM-FI main relay 1 circuit is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more*, 75 milliseconds or more**

DTC Type | Two drive cycles, MIL off

*: Short to ground

**: Stuck

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Other** | PCM switched OFF, diagnosis is running

Malfunction Threshold

- Short to ground A short to ground in the PGM-FI main relay 1 circuit is detected for at least 3 test pulses.

A short to ground in the PGM-FI main relay 1 circuit is detected for at least 3 test pulses.

- Stuck A stuck in the PGM-FI main relay 1 circuit is detected for at least 75 milliseconds after the PCM commanded OFF.

A stuck in the PGM-FI main relay 1 circuit is detected for at least 75 milliseconds after the PCM commanded OFF.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit stuck on failure

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line short to ground

- Fuse blown

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5729: DTC P068B (K20C1) (2019 2020 2021)

- Title: DTC P068B (K20C1) (2019 2020 2021)
- Source path: `pages\6865.html`
- Chunk ID: `chunk_e690a8d280d4`
- Images: `images\GHH403266.jpeg`
- Duplicate sources: `pages\8452.html`, `pages\22958.html`, `pages\21371.html`

### Full Text

````text
# DTC P068B (K20C1) (2019 2020 2021)

DTC P068B: Powertrain Control Module (PCM) Power Source Circuit Unexpected Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the PGM-FI main relay 1 circuit for electrical malfunctions. The driver IC of the PGM-FI main relay 1 circuit is monitored for a specified number of test pulses. If a stuck or a short to ground in the PGM-FI main relay 1 circuit is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous*, once per driving cycle**

Sequence | None

Duration | 0.5 second or more*, 75 milliseconds or more**

DTC Type | Two drive cycles, MIL off

*: Short to ground**: Stuck

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Malfunction Threshold

- Short to ground A short to ground in the PGM-FI main relay 1 circuit is detected for at least 3 test pulses.

A short to ground in the PGM-FI main relay 1 circuit is detected for at least 3 test pulses.

- Stuck A stuck in the PGM-FI main relay 1 circuit is detected for at least 75 milliseconds after the PCM commanded OFF.

A stuck in the PGM-FI main relay 1 circuit is detected for at least 75 milliseconds after the PCM commanded OFF.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 1 circuit stuck on failure

- PGM-FI main relay 1 circuit FI MAIN RLY CL- line short to ground

- Fuse blown

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5730: DTC P06A8 (K20C2 (PGM-FI System))

- Title: DTC P06A8 (K20C2 (PGM-FI System))
- Source path: `pages\6866.html`
- Chunk ID: `chunk_d5627d2e16fd`
- Images: `images\GHH403267.jpeg`, `images\GHH403268.jpeg`
- Duplicate sources: `pages\8453.html`, `pages\22959.html`, `pages\21372.html`

### Full Text

````text
# DTC P06A8 (K20C2 (PGM-FI System))

DTC P06A8: Internal VCC Power Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Main CPU and sub CPU are built into the powertrain control module (PCM). The main CPU supplies 3.3 V power voltage to the sub CPU. The sub CPU converts (A/D conversion) the supplied power voltage and outputs the A/D converted value to the main CPU via serial communication. The main CPU monitors the PCM internal 5 V power supply by comparing with the received value (comparison power supply voltage (3.3 V)) from the sub CPU. When the 5 V power supply is normal, the comparison power supply voltage (3.3 V) falls within a normal area. If the 5 V power supply malfunctions, the comparison power supply voltage (3.3 V) exceeds the range of normal area. If the comparison power supply voltage is out of permissible range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM internal comparison power supply voltage is 3.10 V or less, 3.51 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM (internal 5 V power supply circuit) failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5731: DTC P06A8 (L15B7 (PGM-FI System))

- Title: DTC P06A8 (L15B7 (PGM-FI System))
- Source path: `pages\6867.html`
- Chunk ID: `chunk_16eea191f4f4`
- Images: `images\GHH403269.jpeg`, `images\GHH403270.jpeg`
- Duplicate sources: `pages\8454.html`, `pages\22960.html`, `pages\21373.html`

### Full Text

````text
# DTC P06A8 (L15B7 (PGM-FI System))

DTC P06A8: Internal VCC Power Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Main CPU and sub CPU are built into the powertrain control module (PCM). The main CPU supplies 3.3 V power voltage to the sub CPU. The sub CPU converts (A/D conversion) the supplied power voltage and outputs the A/D converted value to the main CPU via serial communication. The main CPU monitors the PCM internal 5 V power supply by comparing with the received value (comparison power supply voltage (3.3 V)) from the sub CPU. When the 5 V power supply is normal, the comparison power supply voltage (3.3 V) falls within a normal area. If the 5 V power supply malfunctions, the comparison power supply voltage (3.3 V) exceeds the range of normal area. If the comparison power supply voltage is out of permissible range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM internal comparison power supply voltage is 3.10 V or less, 3.51 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM (internal 5 V power supply circuit) failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5732: DTC P0703 (K20C1) (2017 2018 2019)

- Title: DTC P0703 (K20C1) (2017 2018 2019)
- Source path: `pages\6868.html`
- Chunk ID: `chunk_1ed3205787b1`
- Images: `images\GHH403271.jpeg`
- Duplicate sources: `pages\8455.html`, `pages\22961.html`, `pages\21374.html`

### Full Text

````text
# DTC P0703 (K20C1) (2017 2018 2019)

DTC P0703: Brake Pedal Position Switch (NC) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of these conditions occurs:

- When the brake pedal position switch (BKSWNC line) outputs ON to the PCM during the vehicle speed [Vehicle Speed] at more than 13 mph (20 km/h) with accelerator pedal position at more than 0 % for 2.0 seconds or more, the detection counter is incremented. If the detection counter reaches to 15, 000 counts or more, the PCM stores a DTC.

- When the brake pedal position switch (BKSWNC line) outputs OFF to the PCM while the vehicle is decelerated (to 0 mph (0 km/h)) from vehicle speed [Vehicle Speed] over 25 mph (40 km/h) for 2.0 seconds or more, the detection counter is incremented. If the detection counter reaches to more than 3 counts, the PCM stores a DTC.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch BKSWNC line open

- Brake pedal position switch BKSWNC line short to power

- Brake pedal position switch BKSWNC line short to ground

- Brake pedal position switch failure

Confirmation Procedure

Operating Condition

- Start the engine, and drive the vehicle at 25 mph (40 km/h) or more.

- Decelerate without pressing the brake pedal for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5733: DTC P0703 (K20C1) (2019 2020 2021)

- Title: DTC P0703 (K20C1) (2019 2020 2021)
- Source path: `pages\6869.html`
- Chunk ID: `chunk_02a69018939f`
- Images: `images\GHH403272.jpeg`
- Duplicate sources: `pages\8456.html`, `pages\22962.html`, `pages\21375.html`

### Full Text

````text
# DTC P0703 (K20C1) (2019 2020 2021)

DTC P0703: Brake Pedal Position Switch (NC) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring the signals from the brake pedal position switch. If the PCM continuously inputs an abnormal signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of these conditions occurs:

- When the brake pedal position switch (BKSWNC line) is open during the vehicle speed [VEHICLE SPEED] at more than 13 mph (20 km/h) with accelerator pedal position at more than 0 % for 2 seconds or more, the detection counter is incremented. If the detection counter reaches to 15, 000 counts or more, the PCM stores a DTC.

- When the brake pedal position switch (BKSWNC line) is closed while the vehicle is decelerated (to 0 mph (0 km/h)) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h), the detection counter is incremented. If the detection counter reaches to more than 3 counts, the PCM stores a DTC.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch BKSWNC line open

- Brake pedal position switch BKSWNC line short to power

- Brake pedal position switch BKSWNC line short to ground

- Brake pedal position switch failure

Confirmation Procedure

Operating Condition

- Start the engine, and drive the vehicle at 25 mph (40 km/h) or more.

- Decelerate without pressing the brake pedal for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5734: DTC P0703 (K20C2)

- Title: DTC P0703 (K20C2)
- Source path: `pages\6870.html`
- Chunk ID: `chunk_95fd41b4d5e8`
- Images: `images\GHH403273.jpeg`, `images\GHH403274.jpeg`
- Duplicate sources: `pages\8457.html`, `pages\22963.html`, `pages\21376.html`

### Full Text

````text
# DTC P0703 (K20C2)

DTC P0703: Brake Pedal Position Switch (NC) Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 minutes or more*, Depending on driving conditions**

DTC Type | Two drive cycles, MIL off

*: Symptom 1

**: Symptom 2

Enable Conditions

Condition

Vehicle | ON mode

Other* | Accelerator pedal pressed

Malfunction Threshold

- Symptom 1 The PCM inputs an ON signal from the brake pedal position switch (BKSWNC line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

The PCM inputs an ON signal from the brake pedal position switch (BKSWNC line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

- Symptom 2 The PCM inputs an OFF signal from the brake pedal position switch (BKSWNC line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

The PCM inputs an OFF signal from the brake pedal position switch (BKSWNC line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch stuck

- Brake pedal position switch BKSWNC line open (includes poor or loose connection)

- Brake pedal position switch BKSWNC line short to power

- Brake pedal position switch BKSWNC line short to ground

- Brake pedal position switch failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5735: DTC P0703 (L15B7/L15BA)

- Title: DTC P0703 (L15B7/L15BA)
- Source path: `pages\6871.html`
- Chunk ID: `chunk_7210044743fd`
- Images: `images\GHH403275.jpeg`, `images\GHH403276.jpeg`
- Duplicate sources: `pages\8458.html`, `pages\22964.html`, `pages\21377.html`

### Full Text

````text
# DTC P0703 (L15B7/L15BA)

DTC P0703: Brake Pedal Position Switch (NC) Malfunction

General Description

Without Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System:

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects a brake pedal position switch malfunction by monitoring ON/OFF signals from the brake pedal position switch. If the PCM continuously inputs an ON or OFF signal from brake pedal position switch for a specified time during a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 minutes or more*, Depending on driving conditions**

DTC Type | Two drive cycles, MIL off

*: Symptom 1

**: Symptom 2

Enable Conditions

Condition

Vehicle | ON mode

Other* | Accelerator pedal pressed

Malfunction Threshold

Either of these conditions occurs:

- Symptom 1 The PCM inputs an ON signal from the brake pedal position switch (BKSWNC line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

The PCM inputs an ON signal from the brake pedal position switch (BKSWNC line) for at least 5 minutes when the vehicle speed [VEHICLE SPEED] is at 13 mph (20 km/h) or more.

- Symptom 2 The PCM inputs an OFF signal from the brake pedal position switch (BKSWNC line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

The PCM inputs an OFF signal from the brake pedal position switch (BKSWNC line) for three cycles when the vehicle is stopped (or decelerated to 1 mph (3 km/h) or less) from vehicle speed [VEHICLE SPEED] over 25 mph (40 km/h).

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Brake pedal position switch stuck

- Brake pedal position switch BKSWNC line open (includes poor or loose connection)

- Brake pedal position switch BKSWNC line short to power

- Brake pedal position switch BKSWNC line short to ground

- Brake pedal position switch failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5736: DTC P0715 (K20C1) (2017 2018 2019)

- Title: DTC P0715 (K20C1) (2017 2018 2019)
- Source path: `pages\6872.html`
- Chunk ID: `chunk_6d1a7b03354e`
- Images: `images\GHH403277.jpeg`
- Duplicate sources: `pages\8459.html`, `pages\22965.html`, `pages\21378.html`

### Full Text

````text
# DTC P0715 (K20C1) (2017 2018 2019)

DTC P0715: Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the input (mainshaft) speed sensor for rationality faults. The mainshaft speed is calculated from the PWM signal received from the input (mainshaft) speed sensor. Based on the time period of the PWM signal received, which indicates the time period of each tooth of mainshaft, the mainshaft speed will be calculated. The mainshaft speed is continuously monitored against engine speed in order to detect rationality faults. If the absolute difference between the mainshaft speed and the engine speed is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Time the clutch pedal is not pressed | 5 seconds | -

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | -

Other | Gear is engaged

[ ]: HDS Parameter

Malfunction Threshold

The absolute difference between the mainshaft speed [M SHAFT SPD] and the engine speed [Engine Speed] is greater than 500 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Input (mainshaft) speed sensor NM line short to ground

- Input (mainshaft) speed sensor NM line open

- Input (mainshaft) speed sensor VCC line open

- Input (mainshaft) speed sensor SG line open

- Input (mainshaft) speed sensor connector disconnection

- Input (mainshaft) speed sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at speed over 10 mph (15 km/h) for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5737: DTC P0715 (K20C1) (2019 2020 2021)

- Title: DTC P0715 (K20C1) (2019 2020 2021)
- Source path: `pages\6873.html`
- Chunk ID: `chunk_08de2e7a675d`
- Images: `images\GHH403278.jpeg`
- Duplicate sources: `pages\8460.html`, `pages\22966.html`, `pages\21379.html`

### Full Text

````text
# DTC P0715 (K20C1) (2019 2020 2021)

DTC P0715: Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the input (mainshaft) speed sensor for rationality faults. The mainshaft speed is calculated from the PWM signal received from the input (mainshaft) speed sensor. The mainshaft speed is continuously monitored against engine speed in order to detect rationality faults. If the absolute difference between the mainshaft speed and the engine speed is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Time the clutch pedal is not pressed | 5 seconds | -

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | -

Other | Gear is engaged

[ ]: HDS Parameter

Malfunction Threshold

The absolute difference between the mainshaft speed [M SHAFT SPD] and the engine speed [Engine Speed] is greater than 500 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Input (mainshaft) speed sensor NM line short to ground

- Input (mainshaft) speed sensor NM line open

- Input (mainshaft) speed sensor VCC line open

- Input (mainshaft) speed sensor SG line open

- Input (mainshaft) speed sensor connector disconnection

- Input (mainshaft) speed sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at speed over 10 mph (15 km/h) for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5738: DTC P0720 (K20C1) (2017 2018 2019)

- Title: DTC P0720 (K20C1) (2017 2018 2019)
- Source path: `pages\6874.html`
- Chunk ID: `chunk_e3f67940bf37`
- Images: `images\GHH403279.jpeg`
- Duplicate sources: `pages\8461.html`, `pages\22967.html`, `pages\21380.html`

### Full Text

````text
# DTC P0720 (K20C1) (2017 2018 2019)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The monitoring function is checking the speed information received from the output (countershaft) speed sensor during fuel cut-off operation. If the vehicle speed is a specified value during certain driving condition, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 68 deg.F (19.96 deg.C) | -

Engine speed [Engine Speed] | 1, 500 rpm | 4, 500 rpm

Other | During fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The vehicle speed [Vehicle Speed] is less than 3 mph (5 km/h) during above enable conditions for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor defection

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle for a while and decelerate with the throttle valve fully closed.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5739: DTC P0720 (K20C1) (2019)

- Title: DTC P0720 (K20C1) (2019)
- Source path: `pages\6875.html`
- Chunk ID: `chunk_b17178d4d80f`
- Images: `images\GHH403280.jpeg`
- Duplicate sources: `pages\8462.html`, `pages\22968.html`, `pages\21381.html`

### Full Text

````text
# DTC P0720 (K20C1) (2019)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The monitoring function is checking the speed information received from the output (countershaft) speed sensor during fuel cut-off operation. If the vehicle speed is a specified value during certain driving condition, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 68 deg.F (19.96 deg.C) | -

Engine speed [Engine Speed] | 1, 500 rpm | 4, 500 rpm

Other | During fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The vehicle speed [Vehicle Speed] is less than 3 mph (5 km/h) during above enable conditions for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor defection

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle for a while and decelerate with the throttle valve fully closed.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5740: DTC P0720 (K20C1) (2020 2021)

- Title: DTC P0720 (K20C1) (2020 2021)
- Source path: `pages\6876.html`
- Chunk ID: `chunk_5d22005c8283`
- Images: none
- Duplicate sources: `pages\8463.html`, `pages\22969.html`, `pages\21382.html`

### Full Text

````text
# DTC P0720 (K20C1) (2020 2021)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor outputs less than a specified speed despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.4 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs less than 1.94 mph (31.13 km/h) despite the other speed sensor's output of 1.94 mph (3.13 km/h) or more for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5741: DTC P0720 (K20C2 (M/T) USA/Canada models) (2019 2020)

- Title: DTC P0720 (K20C2 (M/T) USA/Canada models) (2019 2020)
- Source path: `pages\6877.html`
- Chunk ID: `chunk_f9bffa618311`
- Images: `images\GHH403281.jpeg`
- Duplicate sources: `pages\8464.html`, `pages\22970.html`, `pages\21383.html`

### Full Text

````text
# DTC P0720 (K20C2 (M/T) USA/Canada models) (2019 2020)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs 0 mph (0 km/h) despite the wheel speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5742: DTC P0720 (K20C2 (M/T)) (2016 2017 2018)

- Title: DTC P0720 (K20C2 (M/T)) (2016 2017 2018)
- Source path: `pages\6878.html`
- Chunk ID: `chunk_4cc65ce5be33`
- Images: `images\GHH403282.jpeg`
- Duplicate sources: `pages\8465.html`, `pages\22971.html`, `pages\21384.html`

### Full Text

````text
# DTC P0720 (K20C2 (M/T)) (2016 2017 2018)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The output shaft (countershaft) speed sensor is attached to the transmission housing to sense output shaft (countershaft) revolutions. The powertrain control module (PCM) determines the vehicle speed according to the signal from the output shaft (countershaft) speed sensor for the control units. If no signal from the output shaft (countershaft) speed sensor is received for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 4, 000 rpm | -

12 volt battery voltage [BATTERY] | 10.0 V | -

Other | During fuel cut-off operation for deceleration

[ ]: HDS Parameter

Malfunction Threshold

No signal from the output shaft (countershaft) speed sensor is detected for at least 5 seconds during deceleration with the engine speed [ENGINE SPEED] at 4, 000 rpm or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor NC line short to ground

- Output shaft (countershaft) speed sensor NC line open

- Output shaft (countershaft) speed sensor connector disconnection

- Output shaft (countershaft) speed sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5743: DTC P0720 (L15B7/L15BA) (2017 2018)

- Title: DTC P0720 (L15B7/L15BA) (2017 2018)
- Source path: `pages\6879.html`
- Chunk ID: `chunk_68c82fdf3e9e`
- Images: `images\GHH403283.jpeg`
- Duplicate sources: `pages\8466.html`, `pages\22972.html`, `pages\21385.html`

### Full Text

````text
# DTC P0720 (L15B7/L15BA) (2017 2018)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The output shaft (countershaft) speed sensor is attached to the transmission housing to sense output shaft (countershaft) revolutions. The powertrain control module (PCM) determines the vehicle speed according to the signal from the output shaft (countershaft) speed sensor for the control units. If no signal from the output shaft (countershaft) speed sensor is received for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 4, 000 rpm | -

12 volt battery voltage [BATTERY] | 10.0 V | -

Other | During fuel cut-off operation for deceleration

[ ]: HDS Parameter

Malfunction Threshold

No signal from the output shaft (countershaft) speed sensor is detected for at least 5 seconds during deceleration with the engine speed [ENGINE SPEED] at 4, 000 rpm or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor NC line short to ground

- Output shaft (countershaft) speed sensor NC line open

- Output shaft (countershaft) speed sensor connector disconnection

- Output shaft (countershaft) speed sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5744: DTC P0720 (L15B7/L15BA: USA/Canada models) (2019 2020 2021)

- Title: DTC P0720 (L15B7/L15BA: USA/Canada models) (2019 2020 2021)
- Source path: `pages\6880.html`
- Chunk ID: `chunk_8a1f459eb03a`
- Images: `images\GHH403284.jpeg`
- Duplicate sources: `pages\8467.html`, `pages\22973.html`, `pages\21386.html`

### Full Text

````text
# DTC P0720 (L15B7/L15BA: USA/Canada models) (2019 2020 2021)

DTC P0720: Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs 0 mph (0 km/h) despite the wheel speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5745: DTC P0721 (K20C1) (2020 2021)

- Title: DTC P0721 (K20C1) (2020 2021)
- Source path: `pages\6881.html`
- Chunk ID: `chunk_6a211ca86f5a`
- Images: none
- Duplicate sources: `pages\8468.html`, `pages\22974.html`, `pages\21387.html`

### Full Text

````text
# DTC P0721 (K20C1) (2020 2021)

DTC P0721: Output Shaft (Countershaft) Speed Sensor Out of Range

General Description

The powertrain control module (PCM) monitors the vehicle speed converted from the output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs 199 mph (320 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5746: DTC P0721 (K20C2 (M/T)) (2019 2020)

- Title: DTC P0721 (K20C2 (M/T)) (2019 2020)
- Source path: `pages\6882.html`
- Chunk ID: `chunk_57f3e0431666`
- Images: `images\GHH403285.jpeg`
- Duplicate sources: `pages\8469.html`, `pages\22975.html`, `pages\21388.html`

### Full Text

````text
# DTC P0721 (K20C2 (M/T)) (2019 2020)

DTC P0721: Output Shaft (Countershaft) Speed Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5747: DTC P0721 (L15B7/L15BA (M/T)) (2019 2020 2021)

- Title: DTC P0721 (L15B7/L15BA (M/T)) (2019 2020 2021)
- Source path: `pages\6883.html`
- Chunk ID: `chunk_a8a747173420`
- Images: `images\GHH403286.jpeg`
- Duplicate sources: `pages\8470.html`, `pages\22976.html`, `pages\21389.html`

### Full Text

````text
# DTC P0721 (L15B7/L15BA (M/T)) (2019 2020 2021)

DTC P0721: Output Shaft (Countershaft) Speed Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the output shaft (countershaft) speed sensor to detect malfunctions. If the output shaft (countershaft) speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The output shaft (countershaft) speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5748: DTC P0831 (K20C1) (2017 2018 2019)

- Title: DTC P0831 (K20C1) (2017 2018 2019)
- Source path: `pages\6884.html`
- Chunk ID: `chunk_b7968645810f`
- Images: `images\GHH403287.jpeg`
- Duplicate sources: `pages\8471.html`, `pages\22977.html`, `pages\21390.html`

### Full Text

````text
# DTC P0831 (K20C1) (2017 2018 2019)

DTC P0831: Clutch Pedal Position Switch A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the clutch pedal position switch A for rationality faults. When the PCM cannot detect release status from clutch pedal position switch A (CLUTCH SW(SA)) under certain driving conditions, the detection continues after the vehicle is turned to the OFF (LOCK) mode. If the malfunction continues for a set time after the vehicle is turned to the OFF (LOCK) mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 500 rpm | -

Vehicle speed [Vehicle Speed] | 19 mph (30 km/h) | -

Other | Monitoring after the vehicle is turned to the OFF (LOCK) mode may take maximum 15 minutes

[ ]: HDS Parameter

Malfunction Threshold

When the PCM cannot detect NOT PRESSED status from clutch pedal position switch A (CLUTCH SW(SA)) under enable conditions, the detection continues after the vehicle is turned to the OFF (LOCK) mode.The PCM cannot detect NOT PRESSED status from clutch pedal position switch A (CLUTCH SW(SA)) for at least 400 milliseconds after the vehicle is turned to the OFF (LOCK) mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Clutch pedal position switch A stuck ON failure

- Clutch pedal position switch A CLUTCH SW(SA) line short to ground

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Drive the vehicle for a while at engine speed [Engine Speed] above 1, 500 rpm.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 15 minutes.

- Turn the vehicle to the ON mode.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5749: DTC P0831 (K20C1) (2019 2020 2021)

- Title: DTC P0831 (K20C1) (2019 2020 2021)
- Source path: `pages\6885.html`
- Chunk ID: `chunk_6260289e0936`
- Images: `images\GHH403288.jpeg`
- Duplicate sources: `pages\8472.html`, `pages\22978.html`, `pages\21391.html`

### Full Text

````text
# DTC P0831 (K20C1) (2019 2020 2021)

DTC P0831: Clutch Pedal Position Switch A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the clutch pedal position switch A for rationality faults. When the PCM cannot detect release status from clutch pedal position switch A (CLUTCH SW(SA)) under certain driving conditions, the detection continues after the vehicle is turned to the OFF (LOCK) mode. If the malfunction continues for a set time after the vehicle is turned to the OFF (LOCK) mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle/two drive cycles*, MIL off

*: The detection drive cycle may change depending upon the vehicle condition when the fault is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 500 rpm | -

Vehicle speed [Vehicle Speed] | 19 mph (30 km/h) | -

Other | Leave 15 minutes in vehicle OFF (LOCK) mode after the vehicle is driven at above condition.

[ ]: HDS Parameter

Malfunction Threshold

The clutch pedal position switch A (CLUTCH SW(SA)) is ON despite the released clutch pedal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Clutch pedal position switch A stuck ON failure

- Clutch pedal position switch A CLUTCH SW(SA) line short to ground

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Drive the vehicle for a while at engine speed [Engine Speed] above 1, 500 rpm.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 15 minutes.

- Turn the vehicle to the ON mode.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC (for one drive cycle)

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for setting the DTC (for two drive cycles)

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5750: DTC P0831 (K20C2 (M/T) with Keyless Access System) (2016 2017 2018 2019 2020)

- Title: DTC P0831 (K20C2 (M/T) with Keyless Access System) (2016 2017 2018 2019 2020)
- Source path: `pages\6886.html`
- Chunk ID: `chunk_fd0ed04f6b15`
- Images: `images\GHH403289.jpeg`
- Duplicate sources: `pages\8473.html`, `pages\22979.html`, `pages\21392.html`

### Full Text

````text
# DTC P0831 (K20C2 (M/T) with Keyless Access System) (2016 2017 2018 2019 2020)

DTC P0831: Clutch Pedal Position Switch A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the clutch pedal position switch A signal to switch the starting system from auto control mode to manual mode when it malfunctions. When the PCM cannot detect an OFF signal from clutch pedal position switch A while the clutch pedal is released, the detection continues after the vehicle is turned to the OFF (LOCK) mode. If the malfunction continues for a set time after the vehicle is turned to the OFF (LOCK) mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5 minutes or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Vehicle speed[VEHICLE SPEED] | 19 mph (30 km/h) | -

Other | Malfunction judgment executes after the vehicle is turned to the OFF (LOCK) mode if PCM cannot detect OFF signal from clutch pedal position switch A while clutch pedal is released under above conditions

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot detect an OFF signal from clutch pedal position switch A for at least 5 minutes after the vehicle is turned to the OFF (LOCK) mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Clutch pedal position switch A stuck ON failure

- Clutch pedal position switch A CLUTCH SW(SA) line short to ground

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5751: DTC P0831(L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

- Title: DTC P0831(L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)
- Source path: `pages\6887.html`
- Chunk ID: `chunk_5a718604f475`
- Images: `images\GHH403290.jpeg`
- Duplicate sources: `pages\8474.html`, `pages\22980.html`, `pages\21393.html`

### Full Text

````text
# DTC P0831(L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

DTC P0831: Clutch Pedal Position Switch A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the clutch pedal position switch A signal to switch the starting system from auto control mode to manual mode when it malfunctions. When the PCM cannot detect an OFF signal from clutch pedal position switch A while the clutch pedal is released, the detection continues after the vehicle is turned to the OFF (LOCK) mode. If the malfunction continues for a set time after the vehicle is turned to the OFF (LOCK) mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5 minutes or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Vehicle speed[VEHICLE SPEED] | 19 mph (30 km/h) | -

Other | Malfunction judgment executes after the vehicle is turned to the OFF (LOCK) mode if PCM cannot detect OFF signal from clutch pedal position switch A while clutch pedal is released under above conditions

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot detect an OFF signal from clutch pedal position switch A for at least 5 minutes after the vehicle is turned to the OFF (LOCK) mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Clutch pedal position switch A stuck ON failure

- Clutch pedal position switch A CLUTCH SW(SA) line short to ground

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5752: DTC P0850 (K20C1) (2017 2018 2019)

- Title: DTC P0850 (K20C1) (2017 2018 2019)
- Source path: `pages\6888.html`
- Chunk ID: `chunk_b1bf7154071a`
- Images: `images\GHH403291.jpeg`
- Duplicate sources: `pages\8475.html`, `pages\22981.html`, `pages\21394.html`

### Full Text

````text
# DTC P0850 (K20C1) (2017 2018 2019)

DTC P0850: Neutral Position Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the variance of both sensor signals neutral position sensor A and neutral position sensor B is compared with the synchronization tolerance. If the variance of the neutral position sensors is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Neutral position sensor A output voltage [Neutral Position Sensor 1] | 0.4914 V | 4.0306 V

Neutral position sensor B output voltage [Neutral Position Sensor 2] | 0.2434 V | 3.263 V

Malfunction Threshold

The variance of both sensor signals (absolute difference between signal voltage of neutral position sensor A multiplicated by correction factor and signal voltage of neutral position sensor B) is greater than 0.17 - 0.62 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Neutral position sensor A NSS1 line short to neutral position sensor B NSS2 line

- Neutral position sensor A failure

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5753: DTC P0850 (K20C1) (2019 2020 2021)

- Title: DTC P0850 (K20C1) (2019 2020 2021)
- Source path: `pages\6889.html`
- Chunk ID: `chunk_10fa6bc853a2`
- Images: `images\GHH403292.jpeg`
- Duplicate sources: `pages\8476.html`, `pages\22982.html`, `pages\21395.html`

### Full Text

````text
# DTC P0850 (K20C1) (2019 2020 2021)

DTC P0850: Neutral Position Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the variance of both sensor signals neutral position sensor A and neutral position sensor B are compared with the synchronization tolerance. If the variance of the neutral position sensors is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Neutral position sensor A output voltage [Neutral Position Sensor 1] | 0.49 V | 4.03 V

Neutral position sensor B output voltage [Neutral Position Sensor 2] | 0.24 V | 3.26 V

Malfunction Threshold

The variance of both sensor signals (absolute difference between signal voltage of neutral position sensor A multiplicated by correction factor and signal voltage of neutral position sensor B) is greater than 0.17 - 0.62 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Neutral position sensor A NSS1 line short to neutral position sensor B NSS2 line

- Neutral position sensor A failure

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5754: DTC P0850 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

- Title: DTC P0850 (K20C2 (M/T)) (2016 2017 2018 2019 2020)
- Source path: `pages\6890.html`
- Chunk ID: `chunk_07084f7802fc`
- Images: `images\GHH403293.jpeg`
- Duplicate sources: `pages\8477.html`, `pages\22983.html`, `pages\21396.html`

### Full Text

````text
# DTC P0850 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

DTC P0850: Neutral Position Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the voltage correlation of neutral position sensor A and neutral position sensor B is out of a specified range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.1 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The neutral position sensor correlation allowed voltage in the Table B is specified value or more for at least 2.1 seconds.

Table B: The neutral position sensor A voltage and the neutral position sensor B voltage correlation

Neutral position sensor A output voltage | 0.92 V or less | 1.06 V | 3.49 V

Sensor correlation allowed voltage | 0.20 V | 0.43 V | 0.87 V

The neutral position sensor correlation allowed voltage calculate expression: Neutral position sensor A voltage/2 - Neutral position sensor B voltage

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Neutral position sensor A NSS1 line short to neutral position sensor B NSS2 line

- Neutral position sensor A failure

- Neutral position sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the ON mode.

- Shift the transmission to all driving position/mode, then move it to the neutral position/mode.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5755: DTC P0850 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

- Title: DTC P0850 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)
- Source path: `pages\6891.html`
- Chunk ID: `chunk_5442ce1ddb4a`
- Images: `images\GHH403294.jpeg`
- Duplicate sources: `pages\8478.html`, `pages\22984.html`, `pages\21397.html`

### Full Text

````text
# DTC P0850 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

DTC P0850: Neutral Position Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the voltage correlation of neutral position sensor A and neutral position sensor B is out of a specified range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.1 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The neutral position sensor correlation allowed voltage in the Table B is specified value or more for at least 2.1 seconds.

Table B: The neutral position sensor A voltage and the neutral position sensor B voltage correlation

Neutral position sensor A output voltage | 0.92 V or less | 1.06 V | 3.49 V

Sensor correlation allowed voltage | 0.20 V | 0.43 V | 0.87 V

The neutral position sensor correlation allowed voltage calculate expression: Neutral position sensor A voltage/2 - Neutral position sensor B voltage

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Neutral position sensor A NSS1 line short to neutral position sensor B NSS2 line

- Neutral position sensor A failure

- Neutral position sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the ON mode.

- Shift the transmission to all driving position/mode, then move it to the neutral position/mode.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5756: DTC P0851, P0852 (K20C1) (2017 2018 2019)

- Title: DTC P0851, P0852 (K20C1) (2017 2018 2019)
- Source path: `pages\6892.html`
- Chunk ID: `chunk_f5709db0ecc8`
- Images: `images\GHH403295.jpeg`
- Duplicate sources: `pages\8479.html`, `pages\22985.html`, `pages\21398.html`

### Full Text

````text
# DTC P0851, P0852 (K20C1) (2017 2018 2019)

DTC P0851: Neutral Position Sensor A Circuit Low Voltage

DTC P0852: Neutral Position Sensor A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the neutral position sensor A output voltage is continuously monitored and compared with minimum and maximum thresholds. If the neutral position sensor A output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0851

The neutral position sensor A output voltage [Neutral Position Sensor 1] is less than 0.4914 V for at least 0.5 second.

DTC: P0852

The neutral position sensor A output voltage [Neutral Position Sensor 1] is greater than 4.0306 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0851

- Neutral position sensor A VCC line open

- Neutral position sensor A NSS1 line short to ground

- Neutral position sensor A NSS1 line open

DTC: P0852

- Neutral position sensor A NSS1 line short to power

- Neutral position sensor A SG line open

Common

- Neutral position sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5757: DTC P0851, P0852 (K20C1) (2019 2020 2021)

- Title: DTC P0851, P0852 (K20C1) (2019 2020 2021)
- Source path: `pages\6893.html`
- Chunk ID: `chunk_c32e6930e7f3`
- Images: `images\GHH403296.jpeg`
- Duplicate sources: `pages\8480.html`, `pages\22986.html`, `pages\21399.html`

### Full Text

````text
# DTC P0851, P0852 (K20C1) (2019 2020 2021)

DTC P0851: Neutral Position Sensor A Circuit Low Voltage

DTC P0852: Neutral Position Sensor A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the neutral position sensor A output voltage is continuously monitored and compared with minimum and maximum thresholds. If the neutral position sensor A output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0851

The neutral position sensor A output voltage [Neutral Position Sensor 1] is less than 0.49 V for at least 0.5 second.

DTC: P0852

The neutral position sensor A output voltage [Neutral Position Sensor 1] is greater than 4.0306 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0851

- Neutral position sensor A VCC line open

- Neutral position sensor A NSS1 line short to ground

- Neutral position sensor A NSS1 line open

DTC: P0852

- Neutral position sensor A NSS1 line short to power

- Neutral position sensor A SG line open

Common

- Neutral position sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5758: DTC P0851, P0852 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

- Title: DTC P0851, P0852 (K20C2 (M/T)) (2016 2017 2018 2019 2020)
- Source path: `pages\6894.html`
- Chunk ID: `chunk_9d5f69574dbb`
- Images: `images\GHH403297.jpeg`
- Duplicate sources: `pages\8481.html`, `pages\22987.html`, `pages\21400.html`

### Full Text

````text
# DTC P0851, P0852 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

DTC P0851: Neutral Position Sensor A Circuit Low Voltage

DTC P0852: Neutral Position Sensor A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the neutral position sensor A output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0851

The neutral position sensor A output voltage is 0.15 V or less for at least 2.0 seconds.

DTC: P0852

The neutral position sensor A output voltage is 3.5 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0851

- Neutral position sensor A VCC line open

- Neutral position sensor A NSS1 line short to ground

DTC: P0852

- Neutral position sensor A SG line open

- Neutral position sensor A NSS1 line short to power

Common

- Neutral position sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5759: DTC P0851, P0852 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

- Title: DTC P0851, P0852 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)
- Source path: `pages\6895.html`
- Chunk ID: `chunk_edafff0cff5d`
- Images: `images\GHH403298.jpeg`
- Duplicate sources: `pages\8482.html`, `pages\22988.html`, `pages\21401.html`

### Full Text

````text
# DTC P0851, P0852 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

DTC P0851: Neutral Position Sensor A Circuit Low Voltage

DTC P0852: Neutral Position Sensor A Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the neutral position sensor A output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0851

The neutral position sensor A output voltage is 0.15 V or less for at least 2.0 seconds.

DTC: P0852

The neutral position sensor A output voltage is 3.5 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0851

- Neutral position sensor A VCC line open

- Neutral position sensor A NSS1 line short to ground

DTC: P0852

- Neutral position sensor A SG line open

- Neutral position sensor A NSS1 line short to power

Common

- Neutral position sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5760: DTC P0864 (K20C2) (2019 2020 2021)

- Title: DTC P0864 (K20C2) (2019 2020 2021)
- Source path: `pages\6896.html`
- Chunk ID: `chunk_1265b39a407d`
- Images: `images\GHH403299.jpeg`
- Duplicate sources: `pages\8483.html`, `pages\22989.html`, `pages\21402.html`

### Full Text

````text
# DTC P0864 (K20C2) (2019 2020 2021)

DTC P0864: PT-CAN Malfunction (Powertrain Control Module (PCM)-Transmission Control Module (TCM))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (TM-CAN_H and TM-CAN_L). When the information is not sent from the transmission control module (TCM) via the TM-CAN lines and this condition continues for a specified time or when the information sent from the TCM is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the TCM via the TM-CAN lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- TM-CAN circuit TM-CAN_H line open

- TM-CAN circuit TM-CAN_L line open

- TM-CAN circuit TM-CAN_H line short to ground

- TM-CAN circuit TM-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5761: DTC P0864 (L15B7/L15BA/L15BY) (2019 2020 2021)

- Title: DTC P0864 (L15B7/L15BA/L15BY) (2019 2020 2021)
- Source path: `pages\6897.html`
- Chunk ID: `chunk_ad7f7c4e096b`
- Images: `images\GHH403300.jpeg`
- Duplicate sources: `pages\8484.html`, `pages\22990.html`, `pages\21403.html`

### Full Text

````text
# DTC P0864 (L15B7/L15BA/L15BY) (2019 2020 2021)

DTC P0864: PT-CAN Malfunction (Powertrain Control Module (PCM)-Transmission Control Module (TCM))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (TM-CAN_H and TM-CAN_L). When the information is not sent from the transmission control module (TCM) via the TM-CAN lines and this condition continues for a specified time or when the information sent from the TCM is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the TCM via the TM-CAN lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- TM-CAN circuit TM-CAN_H line open

- TM-CAN circuit TM-CAN_L line open

- TM-CAN circuit TM-CAN_H line short to ground

- TM-CAN circuit TM-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5762: DTC P1009 (K20C2)

- Title: DTC P1009 (K20C2)
- Source path: `pages\6898.html`
- Chunk ID: `chunk_2dab78be1d75`
- Images: `images\GHH403301.jpeg`
- Duplicate sources: `pages\8485.html`, `pages\22991.html`, `pages\21404.html`

### Full Text

````text
# DTC P1009 (K20C2)

DTC P1009: Variable Valve Timing Control (VTC) A Advance Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The variable valve timing control (VTC) system controls the phase of the intake camshaft and exhaust camshaft. It uses oil pressure to operate the VTC actuator A so the valve timing is optimized depending on driving conditions. The powertrain control module (PCM) monitors the phase control command value and the actual phase value of intake camshaft using the camshaft position (CMP) sensor A. When an over-advanced camshaft phase angle, which the over-advanced angle is predetermined value greater than the commanded values, continues to exist while the VTC is either active or inactive or an advanced phase angle of the intake camshaft is greater than the predetermined value while the VTC is inactive, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.1 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting (or stalled) the engine | 10 seconds | -

Other | In the case the engine was stalled, the intake camshaft angle must be 10 deg. or more for at least 2 seconds after restarting the engine

Malfunction Threshold

Either one of the condition is met for at least 4.1 seconds:

- The controlling value of an advanced intake camshaft phase angle is 58.8 deg. greater than the commanded value while the VTC is either active or inactive.

- The controlling value of an advanced intake camshaft phase angle is 20.0 deg. greater than the commanded value which is 0 deg. while the VTC is inactive.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator A advanced angle side stuck

- Cam chain elongation

- VTC oil control solenoid valve A advanced angle side stuck

- VTC oil control solenoid valve A short

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5763: DTC P1009 (Without XM)

- Title: DTC P1009 (Without XM)
- Source path: `pages\6899.html`
- Chunk ID: `chunk_b09616e7d4a5`
- Images: `images\GHH403302.jpeg`
- Duplicate sources: `pages\8486.html`, `pages\22992.html`, `pages\21405.html`

### Full Text

````text
# DTC P1009 (Without XM)

DTC P1009: Variable Valve Timing Control (VTC) A Advance Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The variable valve timing control (VTC) system controls the phase of the intake camshaft and exhaust camshaft. It uses oil pressure to operate the VTC actuator A so the valve timing is optimized depending on driving conditions. The powertrain control module (PCM) monitors the phase control command value and the actual phase value of intake camshaft using the camshaft position (CMP) sensor A. When an over-advanced camshaft phase angle, which the over-advanced angle is predetermined value greater than the commanded values, continues to exist while the VTC is either active or inactive or an advanced phase angle of the intake camshaft is greater than the predetermined value while the VTC is inactive, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.1 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting (or stalled) the engine | 10 seconds | -

Other | In the case the engine was stalled, the intake camshaft angle must be 10 deg. or more for at least 2 seconds after restarting the engine

Malfunction Threshold

Either one of the condition is met for at least 4.1 seconds:

- The controlling value of an advanced intake camshaft phase angle is 61.7 deg. greater than the commanded value while the VTC is either active or inactive.

- The controlling value of an advanced intake camshaft phase angle is 20.0 deg. greater than the commanded value which is 0 deg. while the VTC is inactive.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator A advanced angle side stuck

- Cam chain elongation

- VTC oil control solenoid valve A advanced angle side stuck

- VTC oil control solenoid valve A short

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5764: DTC P101A (K20C2)

- Title: DTC P101A (K20C2)
- Source path: `pages\6900.html`
- Chunk ID: `chunk_78a027f93414`
- Images: `images\GHH403303.jpeg`
- Duplicate sources: `pages\8487.html`, `pages\22993.html`, `pages\21406.html`

### Full Text

````text
# DTC P101A (K20C2)

DTC P101A: Variable Valve Timing Control (VTC) B Advance Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The variable valve timing control (VTC) system controls the phase of the intake camshaft and exhaust camshaft. It uses oil pressure to operate the VTC actuator B so the valve timing is optimized depending on driving conditions. The powertrain control module (PCM) monitors the phase control command value and the actual phase value of exhaust camshaft using the camshaft position (CMP) sensor B. When an over-retarded camshaft phase angle, which the over-retarded angle is predetermined value greater than the commanded values, continues to exist while the VTC is either active or inactive or a retarded phase angle of the exhaust camshaft is greater than the predetermined value while the VTC is inactive, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.1 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting (or stalled) the engine | 0.5 second | -

Other | In the case the engine was stalled, the exhaust camshaft angle must be 10 deg. or more for at least 2 seconds after restarting the engine

Malfunction Threshold

Either one of the condition is met for at least 4.1 seconds:

- The controlling value of a retarded exhaust camshaft phase angle is 48.8 deg. greater than the commanded value while the VTC is either active or inactive.

- The controlling value of a retarded exhaust camshaft phase angle is 20.0 deg. greater than the commanded value which is 0 deg. while the VTC is inactive.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator B abnormal retarded phase angle

- VTC oil control solenoid valve B stuck

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5765: DTC P101A (Without XM)

- Title: DTC P101A (Without XM)
- Source path: `pages\6901.html`
- Chunk ID: `chunk_880dc0f06448`
- Images: `images\GHH403304.jpeg`
- Duplicate sources: `pages\8488.html`, `pages\22994.html`, `pages\21407.html`

### Full Text

````text
# DTC P101A (Without XM)

DTC P101A: Variable Valve Timing Control (VTC) B Advance Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The variable valve timing control (VTC) system controls the phase of the intake camshaft and exhaust camshaft. It uses oil pressure to operate the VTC actuator B so the valve timing is optimized depending on driving conditions. The powertrain control module (PCM) monitors the phase control command value and the actual phase value of exhaust camshaft using the camshaft position (CMP) sensor B. When an over-retarded camshaft phase angle, which the over-retarded angle is predetermined value greater than the commanded values, continues to exist while the VTC is either active or inactive or a retarded phase angle of the exhaust camshaft is greater than the predetermined value while the VTC is inactive, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.1 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting (or stalled) the engine | 0.5 second | -

Other | In the case the engine was stalled, the exhaust camshaft angle must be 10 deg. or more for at least 2 seconds after restarting the engine

Malfunction Threshold

Either one of the condition is met for at least 4.1 seconds:

- The controlling value of a retarded exhaust camshaft phase angle is 41.7 deg. greater than the commanded value while the VTC is either active or inactive.

- The controlling value of a retarded exhaust camshaft phase angle is 20.0 deg. greater than the commanded value which is 0 deg. while the VTC is inactive.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator B abnormal retarded phase angle

- VTC oil control solenoid valve B stuck

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5766: DTC P1172 (K20C2: USA/Canada models)

- Title: DTC P1172 (K20C2: USA/Canada models)
- Source path: `pages\6902.html`
- Chunk ID: `chunk_ea8379baf8cb`
- Images: `images\GHH403305.jpeg`
- Duplicate sources: `pages\8489.html`, `pages\22995.html`, `pages\21408.html`

### Full Text

````text
# DTC P1172 (K20C2: USA/Canada models)

DTC P1172: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Out of Range High

General Description

Courtesy of HONDA, U.S.A., INC.

If a malfunction causes the air/fuel ratio (A/F) sensor (sensor 1) signal to the powertrain control module (PCM) to deviate from the normal control area, the A/F sensor (sensor 1) may still become active after the engine starts, but the air/fuel feedback does not start normally and the emissions deteriorate. When the A/F sensor (sensor 1) output is out of the normal area, and this condition continues after the A/F sensor (sensor 1) is active, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 7.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

A malfunction is detected when the A/F sensor (sensor 1) output voltage is 4.7 V or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

- Air/fuel ratio feedback is started while idling, hold for at least 7 seconds.

[ ]: HDS Parameter

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5767: DTC P1172 (L15B7/L15BA)

- Title: DTC P1172 (L15B7/L15BA)
- Source path: `pages\6903.html`
- Chunk ID: `chunk_d0572b45788c`
- Images: `images\GHH403306.jpeg`
- Duplicate sources: `pages\8490.html`, `pages\22996.html`, `pages\21409.html`

### Full Text

````text
# DTC P1172 (L15B7/L15BA)

DTC P1172: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Out of Range High

General Description

Courtesy of HONDA, U.S.A., INC.

If a malfunction causes the air/fuel ratio (A/F) sensor (sensor 1) signal to the powertrain control module (PCM) to deviate from the normal control area, the A/F sensor (sensor 1) may still become active after the engine starts, but the air/fuel feedback does not start normally and the emissions deteriorate. When the A/F sensor (sensor 1) output is out of the normal area, and this condition continues after the A/F sensor (sensor 1) is active, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 7.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

A malfunction is detected when the A/F sensor (sensor 1) output voltage is 4.7 V or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

- Air/fuel ratio feedback is started while idling, hold for at least 7 seconds.

[ ]: HDS Parameter

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5768: DTC P134B (K20C1) (2017 2018 2019)

- Title: DTC P134B (K20C1) (2017 2018 2019)
- Source path: `pages\6904.html`
- Chunk ID: `chunk_84e8b3a7d24b`
- Images: `images\GHH403307.jpeg`
- Duplicate sources: `pages\8491.html`, `pages\22997.html`, `pages\21410.html`

### Full Text

````text
# DTC P134B (K20C1) (2017 2018 2019)

DTC P134B: Crankshaft Signal Diagnose

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) checks for crankshaft signal loss and crankshaft signal disturbances. It also performs a rationality check of the crankshaft position (CKP) sensor signal. If the following failures are detected, the PCM stores a DTC:

- Loss of crankshaft signal

- Noisy crankshaft signal

- Pulse length of CKP sensor signal is out of tolerance

- Engine stop position calculated from the CKP sensor signal deviates too much from the real engine position

- Implausible reverse pulses detected since the PCM was switched on is too high

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, Continuous**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

*: Start position check

**: Pulse length check and implausible reverse rotation check

Enable Conditions

Malfunction detection starts if any conditions is met:

Check of signal pulse length

Condition

State of engine | Running

Check of engine stop position

Condition

Vehicle | ON mode

Check of implausible reverse rotation

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

- Check of signal pulse length Implausible pulse length of the CKP sensor signal is detected at least 10 times.

Implausible pulse length of the CKP sensor signal is detected at least 10 times.

- Check of engine stop position The absolute difference of the engine stop position calculated from the CKP sensor signal from the real engine position is 9 deg. or more at least 10 times.

The absolute difference of the engine stop position calculated from the CKP sensor signal from the real engine position is 9 deg. or more at least 10 times.

- Check of implausible reverse rotation Implausible reverse pulses are detected at least 10 times since the PCM was switched on.

Implausible reverse pulses are detected at least 10 times since the PCM was switched on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor loose connection or poor contact

- Noise disturbance by starter

- Noise disturbance during stop phase

- Pulse plate defection

- CKP sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and drive the vehicle at engine speed [Engine Speed] 4, 000 rpm or more.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5769: DTC P134B (K20C1) (2019 2020 2021)

- Title: DTC P134B (K20C1) (2019 2020 2021)
- Source path: `pages\6905.html`
- Chunk ID: `chunk_96696c10098d`
- Images: `images\GHH403308.jpeg`
- Duplicate sources: `pages\8492.html`, `pages\22998.html`, `pages\21411.html`

### Full Text

````text
# DTC P134B (K20C1) (2019 2020 2021)

DTC P134B: Crankshaft Signal Diagnose

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) checks for crankshaft signal loss and crankshaft signal disturbances. It also performs a rationality check of the crankshaft position (CKP) sensor signal. If the following failures are detected, the PCM stores a DTC:

- Loss of crankshaft signal

- Noisy crankshaft signal

- Pulse length of CKP sensor signal is out of tolerance

- Engine stop position calculated from the CKP sensor signal deviates too much from the real engine position

- Implausible reverse pulses detected since the PCM was switched on is too high

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

- Check of signal pulse length Implausible pulse length of the CKP sensor signal is detected at least 10 times.

Implausible pulse length of the CKP sensor signal is detected at least 10 times.

- Check of engine stop position The engine stop position calculated from the CKP sensor signal deviates too much from the real engine position at least 10 times.

The engine stop position calculated from the CKP sensor signal deviates too much from the real engine position at least 10 times.

- Check of implausible reverse rotation Implausible reverse pulses are detected at least 10 times since the PCM was switched on.

Implausible reverse pulses are detected at least 10 times since the PCM was switched on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor loose connection or poor contact

- Noise disturbance by starter

- Noise disturbance during stop phase

- Pulse plate defection

- CKP sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and drive the vehicle at engine speed [Engine Speed] 4, 000 rpm or more.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5770: DTC P1454 (K20C2)

- Title: DTC P1454 (K20C2)
- Source path: `pages\6906.html`
- Chunk ID: `chunk_a8a3914d209f`
- Images: `images\GHH403309.jpeg`, `images\GHH403310.jpeg`
- Duplicate sources: `pages\8493.html`, `pages\22999.html`, `pages\21412.html`

### Full Text

````text
# DTC P1454 (K20C2)

DTC P1454: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure is about 0 kPa (0 mmHg, 0 inHg) when starting a cold engine. When the fuel tank pressure (FTP) sensor output value is out of a specified range and the powertrain control module (PCM) judges that there's no other cause [no evaporative emission (EVAP) canister vent shut valve failure, etc.] for the FTP sensor zero point shift, the PCM detects an FTP sensor malfunction. However, if the FTP sensor output when starting the engine, is a prescribed negative value or less (excessive negative pressure is detected), the malfunction judgment should be done as follows because it is difficult to distinguish the FTP sensor zero point shift (P1454) from the EVAP canister vent shut valve failure (P2422).

- If neither Pending DTCs (P1454 nor P2422) are stored, both Pending DTCs are stored when excessive vacuum is detected at engine start.

- If both Pending DTCs (P1454 and P2422) are stored and excessive vacuum is detected, both Confirmed DTCs are stored.

- If either Pending DTC (P1454 or P2422) is stored and excessive vacuum is detected, the PCM stores the Confirmed DTC which the Pending DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0452, P0453 are judged as OK

Duration | 8.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Other | The EVAP canister vent shut valve is open

The EVAP canister purge valve is closed (the system is not purging)

Malfunction Threshold

- The FTP sensor output fluctuates by 0.7 kPa (5 mmHg, 0.2 inHg) or more, or -0.7 kPa (-5 mmHg, -0.2 inHg) or less, for at least 8.0 seconds.

- The FTP sensor output [FTP SENSOR] value is -1.4 kPa (-10 mmHg, -0.4 inHg) or less for at least 8.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- When the diagnosis does not finish at idle, drive at 30 - 75 mph (48 - 120 km/h) at EVAP canister purge valve duty [EVAP PC DUTY] 20 % or more.

- Drive the vehicle in the manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5771: DTC P1454 (L15B7, USA/Canada models)

- Title: DTC P1454 (L15B7, USA/Canada models)
- Source path: `pages\6907.html`
- Chunk ID: `chunk_d85b655097c3`
- Images: `images\GHH403311.jpeg`, `images\GHH403312.jpeg`
- Duplicate sources: `pages\8494.html`, `pages\23000.html`, `pages\21413.html`

### Full Text

````text
# DTC P1454 (L15B7, USA/Canada models)

DTC P1454: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure is about 0 kPa (0 mmHg, 0 inHg) when starting a cold engine. When the fuel tank pressure (FTP) sensor output value is out of a specified range and the powertrain control module (PCM) judges that there's no other cause [no evaporative emission (EVAP) canister vent shut valve failure, etc.] for the FTP sensor zero point shift, the PCM detects an FTP sensor malfunction. However, if the FTP sensor output when starting the engine, is a prescribed negative value or less (excessive negative pressure is detected), the malfunction judgment should be done as follows because it is difficult to distinguish the FTP sensor zero point shift (P1454) from the EVAP canister vent shut valve failure (P2422).

- If neither Pending DTCs (P1454 nor P2422) are stored, both Pending DTCs are stored when excessive vacuum is detected at engine start.

- If both Pending DTCs (P1454 and P2422) are stored and excessive vacuum is detected, both Confirmed DTCs are stored.

- If either Pending DTC (P1454 or P2422) is stored and excessive vacuum is detected, the PCM stores the Confirmed DTC which the Pending DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0452, P0453 are judged as OK

Duration | 8.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Other | The EVAP canister vent shut valve is open

The EVAP canister purge valve is closed (the system is not purging)

Malfunction Threshold

- The FTP sensor output fluctuates by 0.7 kPa (5 mmHg, 0.2 inHg) or more, or -0.7 kPa (-5 mmHg, -0.2 inHg) or less, for at least 8.0 seconds.

- The FTP sensor output [FTP SENSOR] value is -1.4 kPa (-10 mmHg, -0.4 inHg) or less for at least 8.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- When the diagnosis does not finish at idle, drive at 30 - 75 mph (48 - 120 km/h) at EVAP canister purge valve duty [EVAP PC DUTY] 20 % or more.

- Drive the vehicle in the manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5772: DTC P1458 (K20C2)

- Title: DTC P1458 (K20C2)
- Source path: `pages\6908.html`
- Chunk ID: `chunk_c4b6dc7ac795`
- Images: `images\GHH403313.jpeg`, `images\GHH403314.jpeg`, `images\GHH403315.jpeg`
- Duplicate sources: `pages\8495.html`, `pages\23001.html`, `pages\21414.html`

### Full Text

````text
# DTC P1458 (K20C2)

DTC P1458: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Detection of atmospheric pressure failure

Judgment 2: Flickering of the FTP sensor

<Judgments 1 and 2 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect atmospheric pressure, after keeping the canister vent opened for a specified duration to stabilize the pressure inside the fuel tank.

- If the pressure inside the fuel tank after a specified duration has not reached a specified value from the sensor zero point, a canister vent blockage is detected.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect FTP sensor electrical noise failure, after keeping the canister vent opened for a specified time to stabilize the pressure inside the fuel tank.

- If the difference of pressure inside the fuel tank and an average value after a specified duration has exceeded a specified value for a specified duration, an FTP sensor electrical noise failure is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 50 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 2] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Malfunction Threshold

- The misalignment of zero point pressure inside the fuel tank is 0.6 kPa (5 mmHg, 0.1 inHg) or more.

- The output from the FTP sensor is flickering 10 seconds or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor output stuck

- FTP sensor line electrical noise overlapped

- FTP sensor line open

- FTP sensor line short

- EVAP canister vent shut valve full closed stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 28 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5773: DTC P1458 (K20C2)

- Title: DTC P1458 (K20C2)
- Source path: `pages\6908.html`
- Chunk ID: `chunk_24cfc5def862`
- Images: `images\GHH403313.jpeg`, `images\GHH403314.jpeg`, `images\GHH403315.jpeg`
- Duplicate sources: `pages\6909.html`, `pages\8495.html`, `pages\8496.html`, `pages\23001.html`, `pages\23002.html`, `pages\21414.html`, `pages\21415.html`

### Full Text

````text
ecutes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5774: DTC P1458 (L15B7/L15BA)

- Title: DTC P1458 (L15B7/L15BA)
- Source path: `pages\6909.html`
- Chunk ID: `chunk_3a3f8802bf55`
- Images: `images\GHH403316.jpeg`, `images\GHH403317.jpeg`, `images\GHH403318.jpeg`
- Duplicate sources: `pages\8496.html`, `pages\23002.html`, `pages\21415.html`

### Full Text

````text
# DTC P1458 (L15B7/L15BA)

DTC P1458: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Detection of atmospheric pressure failure

Judgment 2: Flickering of the FTP sensor

<Judgments 1 and 2 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect atmospheric pressure, after keeping the canister vent opened for a specified duration to stabilize the pressure inside the fuel tank.

- If the pressure inside the fuel tank after a specified duration has not reached a specified value from the sensor zero point, a canister vent blockage is detected.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect FTP sensor electrical noise failure, after keeping the canister vent opened for a specified time to stabilize the pressure inside the fuel tank.

- If the difference of pressure inside the fuel tank and an average value after a specified duration has exceeded a specified value for a specified duration, an FTP sensor electrical noise failure is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 50 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 2] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Malfunction Threshold

- The misalignment of zero point pressure inside the fuel tank is 0.6 kPa (5 mmHg, 0.1 inHg) or more.

- The output from the FTP sensor is flickering 10 seconds or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor output stuck

- FTP sensor line electrical noise overlapped

- FTP sensor line open

- FTP sensor line short

- EVAP canister vent shut valve full closed stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 25 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5775: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\6910.html`
- Chunk ID: `chunk_ac824121cc68`
- Images: `images\GHH403319.jpeg`, `images\GHH403320.jpeg`
- Duplicate sources: `pages\8497.html`, `pages\23003.html`, `pages\21416.html`

### Full Text

````text
# DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

DTC P145D: Evaporative Emission (EVAP) System Purge Flow Malfunction at turbocharging

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 11 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 11 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5776: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6911.html`
- Chunk ID: `chunk_1bd04c56412a`
- Images: `images\GHH403321.jpeg`, `images\GHH403322.jpeg`
- Duplicate sources: `pages\8498.html`, `pages\23004.html`, `pages\21417.html`

### Full Text

````text
# DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P145D: Evaporative Emission (EVAP) System Purge Flow Malfunction at turbocharging

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 11 seconds* 1 (9.5 seconds)* 2 or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si) and L15BY*2: L15BA

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 11 seconds* 1 (9.5 seconds)* 2.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5777: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P145D (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6911.html`
- Chunk ID: `chunk_c928609ebfac`
- Images: `images\GHH403321.jpeg`, `images\GHH403322.jpeg`
- Duplicate sources: `pages\8498.html`, `pages\23004.html`, `pages\21417.html`

### Full Text

````text
- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5778: DTC P145D (Si) (2017 2018 2019)

- Title: DTC P145D (Si) (2017 2018 2019)
- Source path: `pages\6912.html`
- Chunk ID: `chunk_bb9ecd722db0`
- Images: `images\GHH403323.jpeg`, `images\GHH403324.jpeg`
- Duplicate sources: `pages\8499.html`, `pages\23005.html`, `pages\21418.html`

### Full Text

````text
# DTC P145D (Si) (2017 2018 2019)

DTC P145D: Evaporative Emission (EVAP) System Purge Flow Malfunction at turbocharging

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 9.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 10 % or less for at least 9.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5779: DTC P145D (Si) (2020 2021)

- Title: DTC P145D (Si) (2020 2021)
- Source path: `pages\6913.html`
- Chunk ID: `chunk_74dcda850142`
- Images: `images\GHH403325.jpeg`, `images\GHH403326.jpeg`
- Duplicate sources: `pages\8500.html`, `pages\23006.html`, `pages\21419.html`

### Full Text

````text
# DTC P145D (Si) (2020 2021)

DTC P145D: Evaporative Emission (EVAP) System Purge Flow Malfunction at turbocharging

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Flowing | Flowing | OK | Purge line normal, EVAP canister purge valve normal

Flowing | Flowing | NG (P2450) | Non-return valve A abnormal

Negative side purge flow | Boost side purge flow | Purge back-flow (P2450) | Condition

Not flowing | Flowing | - | Negative side purge line abnormal

Flowing | Not flowing | - | Boost side purge line abnormal

Not flowing | Not flowing | - | Purge line abnormal, EVAP canister purge valve open

The fuel vapor in the fuel tank is temporarily stored in the evaporative emission (EVAP) canister and drawn into the engine through the EVAP canister purge valve. The powertrain control module (PCM) controls the amount of vapor introduced into the engine by varying the duty cycle of the EVAP canister purge valve according to the condition of the engine.

The PCM checks the purge flow conditions on both negative and boost pressure sides. If either side of the purge flow is detected as abnormal, it is determined that there is a clog or disconnection on the abnormal side of the purge line. If both sides of the purge flow are detected as abnormal, it is determined that the purge lines are abnormal or the EVAP canister purge valve is stuck opened.

Purge flow check of boost pressure side:

The EVAP canister purge valve opens normally (EVAP canister purge valve OPEN OK) and detects that the purge flow is normal when the pulse of the EVAP canister purge valve duty cycle is transmitted to the fuel tank pressure (FTP) sensor during purge flow (pulse method).

OK determination: Pulse exists (P145D OK)

- P04F0 Purge flow OK

- P04DF EVAP canister purge valve stuck Open OK

NG determination: No pulse (P145D NG)

- Either purge flow P04F0 abnormality or P04DF EVAP canister purge valve OPEN failure

- In this case, if purge flow check of negative pressure side P0441 is determined as OK or P04DF is determined as OK by the check after the vehicle condition is turned to the OFF (LOCK) mode after P0441 is determined as NG, the purge flow check of boost pressure side P04F0 is determined as NG

When P04DF is determined as OK after the vehicle condition is turned to the OFF (LOCK) mode, P04F0 is also determined after the vehicle condition is turned to the OFF (LOCK) mode.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 9.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | 115 kPa (860 mmHg, 33.9 inHg) | -

Boost pressure | 14 kPa (100 mmHg, 4 inHg) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

[ ]: HDS Parameter

Condition | Minimum | Maximum

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 9.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

- EVAP canister purge valve open stuck

- FTP sensor stuck

- EVAP system line clogged

- EVAP system line misinstalled

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5780: DTC P145D (Si) (2020 2021)

- Title: DTC P145D (Si) (2020 2021)
- Source path: `pages\6913.html`
- Chunk ID: `chunk_4966f2907e44`
- Images: `images\GHH403325.jpeg`, `images\GHH403326.jpeg`
- Duplicate sources: `pages\8500.html`, `pages\23006.html`, `pages\21419.html`

### Full Text

````text
Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 55 seconds.

- Drive the vehicle at high load for total of at least 9.5 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5781: DTC P1549 (K20C1) (2017 2018 2019)

- Title: DTC P1549 (K20C1) (2017 2018 2019)
- Source path: `pages\6914.html`
- Chunk ID: `chunk_9e624d70dfb0`
- Images: `images\GHH403327.jpeg`
- Duplicate sources: `pages\8501.html`, `pages\23007.html`, `pages\21420.html`

### Full Text

````text
# DTC P1549 (K20C1) (2017 2018 2019)

DTC P1549: Charging System High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity to supply necessary power to the electrical system and to charge the 12 volt battery. The alternator voltage target values from 12.5 V to 14.5 V are achieved by switching the alternator control mode (controlled by the powertrain control module (PCM)). The alternator output signal is sent to the PCM, and it varies according to the 12 volt battery's state of charge, the electrical load, and the engine speed. When the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 16 V or more for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (voltage regulator failure)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5782: DTC P1549 (K20C1) (2019 2020 2021)

- Title: DTC P1549 (K20C1) (2019 2020 2021)
- Source path: `pages\6915.html`
- Chunk ID: `chunk_b1b93e99bb45`
- Images: `images\GHH403328.jpeg`
- Duplicate sources: `pages\8502.html`, `pages\23008.html`, `pages\21421.html`

### Full Text

````text
# DTC P1549 (K20C1) (2019 2020 2021)

DTC P1549: Charging System High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity to supply necessary power to the electrical system and to charge the 12 volt battery. The alternator voltage target values from 12.5 V to 14.5 V are achieved by switching the alternator control mode (controlled by the powertrain control module (PCM)). The alternator output signal is sent to the PCM, and it varies according to the 12 volt battery's state of charge, the electrical load, and the engine speed. When the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is more than 16 V for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (voltage regulator failure)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5783: DTC P1549 (K20C2)

- Title: DTC P1549 (K20C2)
- Source path: `pages\6916.html`
- Chunk ID: `chunk_b7d2d624805f`
- Images: `images\GHH403329.jpeg`
- Duplicate sources: `pages\8503.html`, `pages\23009.html`, `pages\21422.html`

### Full Text

````text
# DTC P1549 (K20C2)

DTC P1549: Charging System High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity to supply the necessary power to the electrical system and to charge the 12 volt battery. The alternator voltage target values from 12.5 V to 14.5 V are achieved by switching the alternator control mode (controlled by the powertrain control module (PCM)). The alternator output signal is sent to the PCM, and it varies according to the 12 volt battery's state of charge, the electrical load, and the engine speed. When the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 16.0 V or more for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil E side short to ground, regulator failure)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5784: DTC P1549 (L15B7/L15BA)

- Title: DTC P1549 (L15B7/L15BA)
- Source path: `pages\6917.html`
- Chunk ID: `chunk_5b5d24feb987`
- Images: `images\GHH403330.jpeg`
- Duplicate sources: `pages\8504.html`, `pages\23010.html`, `pages\21423.html`

### Full Text

````text
# DTC P1549 (L15B7/L15BA)

DTC P1549: Charging System High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity to supply the necessary power to the electrical system and to charge the 12 volt battery. The alternator voltage target values from 12.5 V to 14.5 V are achieved by switching the alternator control mode (controlled by the powertrain control module (PCM)). The alternator output signal is sent to the PCM, and it varies according to the 12 volt battery's state of charge, the electrical load, and the engine speed. When the FI MAIN RLY OUT terminal voltage is a set value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 16.0 V or more for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure (field coil E side short to ground, regulator failure)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5785: DTC P154A (K20C1) (2017 2018 2019)

- Title: DTC P154A (K20C1) (2017 2018 2019)
- Source path: `pages\6918.html`
- Chunk ID: `chunk_3651399aa811`
- Images: `images\GHH403331.jpeg`
- Duplicate sources: `pages\8505.html`, `pages\23011.html`, `pages\21424.html`

### Full Text

````text
# DTC P154A (K20C1) (2017 2018 2019)

DTC P154A: Battery Sensor Internal Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The 12 volt battery sensor is the central component of the electronic energy management. The 12 volt battery sensor records battery quantities as current, voltage, and temperature. With the measured values, the integrated software monitors current and anticipate battery states. If the PCM detects a 12 volt battery sensor hardware failure for a specified time, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Other | LIN communication is established for at least 3 seconds

Malfunction Threshold

The PCM detects a 12 volt battery sensor hardware failure for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5786: DTC P154A (K20C1) (2019 2020 2021)

- Title: DTC P154A (K20C1) (2019 2020 2021)
- Source path: `pages\6919.html`
- Chunk ID: `chunk_ccb2d27db966`
- Images: `images\GHH403332.jpeg`
- Duplicate sources: `pages\8506.html`, `pages\23012.html`, `pages\21425.html`

### Full Text

````text
# DTC P154A (K20C1) (2019 2020 2021)

DTC P154A: Battery Sensor Internal Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The 12 volt battery sensor is the central component of the electronic energy management. The 12 volt battery sensor records battery quantities as current, voltage, and temperature. With the measured values, the integrated software monitors current and anticipate battery states. If the PCM detects a 12 volt battery sensor hardware failure for a specified time, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Other | LIN communication is established for at least 3 seconds

Malfunction Threshold

The PCM detects a 12 volt battery sensor hardware failure for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5787: DTC P154A (K20C2)

- Title: DTC P154A (K20C2)
- Source path: `pages\6920.html`
- Chunk ID: `chunk_54778914885e`
- Images: `images\GHH403333.jpeg`
- Duplicate sources: `pages\8507.html`, `pages\23013.html`, `pages\21426.html`

### Full Text

````text
# DTC P154A (K20C2)

DTC P154A: Battery Sensor Internal Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The 12 volt battery sensor is connected between the 12 volt battery and ground. The 12 volt battery sensor measures the 12 volt battery's current, voltage, and temperature. The measured value is sent to the powertrain control module (PCM) via the local interconnect network (LIN) line by the request of the PCM. The 12 volt battery sensor has a self diagnostic function and sends the results to the PCM via the LIN line. If the diagnostic results are outside the normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either one of the conditions is met for at least 10 seconds:

- Internal current detection circuit open or A/D conversion circuit abnormal

- Internal voltage detection circuit open/short or A/D conversion circuit abnormal

- Internal temperature detection circuit open/short or A/D conversion circuit abnormal

- Calibration data abnormal

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5788: DTC P154A (Without XM)

- Title: DTC P154A (Without XM)
- Source path: `pages\6921.html`
- Chunk ID: `chunk_6033f2d9e20e`
- Images: `images\GHH403334.jpeg`
- Duplicate sources: `pages\8508.html`, `pages\23014.html`, `pages\21427.html`

### Full Text

````text
# DTC P154A (Without XM)

DTC P154A: Battery Sensor Internal Failure

General Description

Courtesy of HONDA, U.S.A., INC.

The 12 volt battery sensor is connected between the 12 volt battery and ground. The 12 volt battery sensor measures the 12 volt battery's current, voltage, and temperature. The measured value is sent to the powertrain control module (PCM) via the local interconnect network (LIN) line by the request of the PCM. The 12 volt battery sensor has a self diagnostic function and sends the results to the PCM via the LIN line. If the diagnostic results are outside the normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either one of the conditions is met for at least 10 seconds:

- Internal current detection circuit open or A/D conversion circuit abnormal

- Internal voltage detection circuit open/short or A/D conversion circuit abnormal

- Internal temperature detection circuit open/short or A/D conversion circuit abnormal

- Calibration data abnormal

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5789: DTC P154B (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P154B (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\6922.html`
- Chunk ID: `chunk_3fc5aae6d055`
- Images: `images\GHH403335.jpeg`
- Duplicate sources: `pages\8509.html`, `pages\23015.html`, `pages\21428.html`

### Full Text

````text
# DTC P154B (K20C1) (2017 2018 2019 2020 2021)

DTC P154B: Battery Sensor Characteristic Abnormal

General Description

Courtesy of HONDA, U.S.A., INC.

The 12 volt battery sensor is connected between the 12 volt battery and ground. The 12 volt battery sensor measures the 12 volt battery's current, voltage, and temperature. The measured value is sent to the powertrain control module (PCM) via local interconnect network (LIN) on demand from the PCM. If the PCM receives an invalid value from the 12 volt battery sensor, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Other | LIN communication is established for at least 3 seconds

Malfunction Threshold

The PCM receives an invalid value from the 12 volt battery sensor for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5790: DTC P1658 (K20C2)

- Title: DTC P1658 (K20C2)
- Source path: `pages\6923.html`
- Chunk ID: `chunk_093dfe68b722`
- Images: `images\GHH403336.jpeg`
- Duplicate sources: `pages\8510.html`, `pages\23016.html`, `pages\21429.html`

### Full Text

````text
# DTC P1658 (K20C2)

DTC P1658: Electronic Throttle Control System (ETCS) Control Relay ON Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). When the voltage is applied from the PGM-FI subrelay circuit to the FI SUB RLY OUT terminal for a set time after the PGM-FI subrelay circuit is turned off, the PCM detects a malfunction in the PGM-FI subrelay circuit power switch and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Malfunction Threshold

The communication signal is input from the PCM for at least 2.0 seconds after the PGM-FI subrelay circuit is turned off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit failure

- PGM-FI subrelay circuit FI SUB RLY CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5791: DTC P1658 (L15B7/L15BA/L15BY)

- Title: DTC P1658 (L15B7/L15BA/L15BY)
- Source path: `pages\6924.html`
- Chunk ID: `chunk_6fa771265683`
- Images: `images\GHH403337.jpeg`
- Duplicate sources: `pages\8511.html`, `pages\23017.html`, `pages\21430.html`

### Full Text

````text
# DTC P1658 (L15B7/L15BA/L15BY)

DTC P1658: Electronic Throttle Control System (ETCS) Control Relay ON Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). When the voltage is applied from the PGM-FI subrelay circuit to the FI SUB RLY OUT terminal for a set time after the PGM-FI subrelay circuit is turned off, the PCM detects a malfunction in the PGM-FI subrelay circuit power switch and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Malfunction Threshold

The communication signal is input from the PCM for at least 2.0 seconds after the PGM-FI subrelay circuit is turned off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit failure

- PGM-FI subrelay circuit FI SUB RLY CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5792: DTC P1659 (K20C2)

- Title: DTC P1659 (K20C2)
- Source path: `pages\6925.html`
- Chunk ID: `chunk_2c34b7559fb8`
- Images: `images\GHH403338.jpeg`
- Duplicate sources: `pages\8512.html`, `pages\23018.html`, `pages\21431.html`

### Full Text

````text
# DTC P1659 (K20C2)

DTC P1659: Electronic Throttle Control System (ETCS) Control Relay OFF Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). When the voltage from the PGM-FI subrelay circuit is not input for a set time after the PGM-FI subrelay circuit is turned on when the vehicle is turned to the ON mode, the PCM detects a malfunction in the PGM-FI subrelay circuit power switch and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The power supply voltage is not applied from the PGM-FI subrelay circuit for at least 200 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit failure

- Fuse failure

- PGM-FI subrelay circuit FI SUB RLY OUT line open

- PGM-FI subrelay circuit FI SUB RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5793: DTC P1659 (L15B7/L15BA)

- Title: DTC P1659 (L15B7/L15BA)
- Source path: `pages\6926.html`
- Chunk ID: `chunk_0fe8a8f22c56`
- Images: `images\GHH403339.jpeg`
- Duplicate sources: `pages\8513.html`, `pages\23019.html`, `pages\21432.html`

### Full Text

````text
# DTC P1659 (L15B7/L15BA)

DTC P1659: Electronic Throttle Control System (ETCS) Control Relay OFF Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). When the voltage from the PGM-FI subrelay circuit is not input for a set time after the PGM-FI subrelay circuit is turned on when the vehicle is turned to the ON mode, the PCM detects a malfunction in the PGM-FI subrelay circuit power switch and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The power supply voltage is not applied from the PGM-FI subrelay circuit for at least 200 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI subrelay circuit failure

- Fuse failure

- PGM-FI subrelay circuit FI SUB RLY OUT line open

- PGM-FI subrelay circuit FI SUB RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5794: DTC P1683 (K20C1) (2017 2018 2019)

- Title: DTC P1683 (K20C1) (2017 2018 2019)
- Source path: `pages\6927.html`
- Chunk ID: `chunk_09522da9fe08`
- Images: `images\GHH403340.jpeg`
- Duplicate sources: `pages\8514.html`, `pages\23020.html`, `pages\21433.html`

### Full Text

````text
# DTC P1683 (K20C1) (2017 2018 2019)

DTC P1683: Throttle Valve Default Position Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The opening motion forced by the default position spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.26 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the ON mode* | 29 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

*: Malfunction detection executes after the vehicle is turned to the OFF (LOCK) mode[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met for at least 0.26 second:

- If the default position learning has been performed The actual position is less than the default position for 2.9922 % or more.

The actual position is less than the default position for 2.9922 % or more.

- If the default position learning has not been performed The actual position is less than 2.6326 %.

The actual position is less than 2.6326 %.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5795: DTC P1683 (K20C1) (2019)

- Title: DTC P1683 (K20C1) (2019)
- Source path: `pages\6928.html`
- Chunk ID: `chunk_3045f8d2d2cf`
- Images: `images\GHH403341.jpeg`
- Duplicate sources: `pages\8515.html`, `pages\23021.html`, `pages\21434.html`

### Full Text

````text
# DTC P1683 (K20C1) (2019)

DTC P1683: Throttle Valve Default Position Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The opening motion forced by the default position spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.26 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- First learning performed The throttle valve position is 12.9475 % or less.

The throttle valve position is 12.9475 % or less.

- First learning not performed The throttle valve position is 2.5 % or less.

The throttle valve position is 2.5 % or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5796: DTC P1683 (K20C1) (2020 2021)

- Title: DTC P1683 (K20C1) (2020 2021)
- Source path: `pages\6929.html`
- Chunk ID: `chunk_66ab73a49129`
- Images: `images\GHH403342.jpeg`
- Duplicate sources: `pages\8516.html`, `pages\23022.html`, `pages\21435.html`

### Full Text

````text
# DTC P1683 (K20C1) (2020 2021)

DTC P1683: Throttle Valve Default Position Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The opening motion forced by the default position spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.26 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- First learning performed The throttle valve position is -0.49 % or less.

The throttle valve position is -0.49 % or less.

- First learning not performed The throttle valve position is 2.5 % or less.

The throttle valve position is 2.5 % or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5797: DTC P1683 (K20C2)

- Title: DTC P1683 (K20C2)
- Source path: `pages\6930.html`
- Chunk ID: `chunk_89153b53456b`
- Images: `images\GHH403343.jpeg`
- Duplicate sources: `pages\8517.html`, `pages\23023.html`, `pages\21436.html`

### Full Text

````text
# DTC P1683 (K20C2)

DTC P1683: Throttle Valve Default Position Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). The throttle valve default position spring is attached to the throttle valve gear. It opens the throttle valve to improve starting performance in cold conditions, or to retain minimum running performance in case of an electronic throttle control system failure. To confirm that the throttle valve is operating normally, and if the detecting condition meets, the throttle valve moves to a fully closed position and opens to the target position by the throttle valve default position spring. If the throttle valve does not move to the target position range, the PCM detects a throttle valve default position spring malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 158 deg.F (70 deg.C) | -

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The throttle valve position is 5 deg. or more from the fully closed position, or 3 deg. or less from the fully closed position, for at least 2.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve default position spring abnormal

- Throttle valve friction increase (poor action)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5798: DTC P1683 (L15B7/L15BA/L15BY)

- Title: DTC P1683 (L15B7/L15BA/L15BY)
- Source path: `pages\6931.html`
- Chunk ID: `chunk_2c2973c12ce4`
- Images: `images\GHH403344.jpeg`
- Duplicate sources: `pages\8518.html`, `pages\23024.html`, `pages\21437.html`

### Full Text

````text
# DTC P1683 (L15B7/L15BA/L15BY)

DTC P1683: Throttle Valve Default Position Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). The throttle valve default position spring is attached to the throttle valve gear. It opens the throttle valve to improve starting performance in cold conditions, or to retain minimum running performance in case of an electronic throttle control system failure. To confirm that the throttle valve is operating normally, and if the detecting condition meets, the throttle valve moves to a fully closed position and opens to the target position by the throttle valve default position spring. If the throttle valve does not move to the target position range, the PCM detects a throttle valve default position spring malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 158 deg.F (70 deg.C) | -

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The throttle valve position is 5 deg. or more from the fully closed position, or 3 deg. or less from the fully closed position, for at least 2.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve default position spring abnormal

- Throttle valve friction increase (poor action)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5799: DTC P1684 (K20C1) (2017 2018 2019)

- Title: DTC P1684 (K20C1) (2017 2018 2019)
- Source path: `pages\6932.html`
- Chunk ID: `chunk_826fdc78daef`
- Images: `images\GHH403345.jpeg`
- Duplicate sources: `pages\8519.html`, `pages\23025.html`, `pages\21438.html`

### Full Text

````text
# DTC P1684 (K20C1) (2017 2018 2019)

DTC P1684: Throttle Valve Return Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The return motion forced by the return spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.36 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the ON mode* | 29 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

*: Malfunction detection executes after the vehicle is turned to the OFF (LOCK) mode[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- If the default position learning has been performed The actual position is greater than the default position for 2.9922 % or more for at least 0.36 second.

The actual position is greater than the default position for 2.9922 % or more for at least 0.36 second.

- If the default position learning has not been performed The actual position is greater than 16.06271 %.

The actual position is greater than 16.06271 %.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5800: DTC P1684 (K20C1) (2019)

- Title: DTC P1684 (K20C1) (2019)
- Source path: `pages\6933.html`
- Chunk ID: `chunk_b5216acd1288`
- Images: `images\GHH403346.jpeg`
- Duplicate sources: `pages\8520.html`, `pages\23026.html`, `pages\21439.html`

### Full Text

````text
# DTC P1684 (K20C1) (2019)

DTC P1684: Throttle Valve Return Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The return motion forced by the return spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.36 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- First learning performed The throttle valve position is more than 2.99 %.

The throttle valve position is more than 2.99 %.

- First learning not performed The throttle valve position is more than 15.9375 %.

The throttle valve position is more than 15.9375 %.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5801: DTC P1684 (K20C1) (2020 2021)

- Title: DTC P1684 (K20C1) (2020 2021)
- Source path: `pages\6934.html`
- Chunk ID: `chunk_44db0b6a6af0`
- Images: `images\GHH403347.jpeg`
- Duplicate sources: `pages\8521.html`, `pages\23027.html`, `pages\21440.html`

### Full Text

````text
# DTC P1684 (K20C1) (2020 2021)

DTC P1684: Throttle Valve Return Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the electronic throttle control system for functionality failures. The return motion forced by the return spring is checked. If the actual position exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.36 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 41.47 deg.F (5.26 deg.C) | 212.82 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.47 deg.F (5.26 deg.C) | 289.86 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- First learning performed The throttle valve position is more than 18.9275 %.

The throttle valve position is more than 18.9275 %.

- First learning not performed The throttle valve position is more than 15.9375 %.

The throttle valve position is more than 15.9375 %.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 30 seconds.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5802: DTC P1684 (K20C2)

- Title: DTC P1684 (K20C2)
- Source path: `pages\6935.html`
- Chunk ID: `chunk_e1922db44981`
- Images: `images\GHH403348.jpeg`
- Duplicate sources: `pages\8522.html`, `pages\22698.html`, `pages\21111.html`

### Full Text

````text
# DTC P1684 (K20C2)

DTC P1684: Throttle Valve Return Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). The throttle valve return spring is attached to the throttle valve gear to return the throttle valve to the default position. To confirm that the throttle valve is operating normally, and if the detecting condition meets, the throttle valve moves to a specified position and closes to the target position by the throttle valve return spring. If the throttle valve does not move to the target position range, the PCM detects a throttle valve return spring malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 158 deg.F (70 deg.C) | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The throttle valve opening angle is 17 deg. or more, 11 deg. or less, for at least 2.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve return spring failure

- Throttle valve friction increase (poor action)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5803: DTC P1684 (L15B7/L15BA)

- Title: DTC P1684 (L15B7/L15BA)
- Source path: `pages\6936.html`
- Chunk ID: `chunk_ffcad1953a2d`
- Images: `images\GHH403349.jpeg`
- Duplicate sources: `pages\8523.html`, `pages\22699.html`, `pages\21112.html`

### Full Text

````text
# DTC P1684 (L15B7/L15BA)

DTC P1684: Throttle Valve Return Spring Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). The throttle valve return spring is attached to the throttle valve gear to return the throttle valve to the default position. To confirm that the throttle valve is operating normally, and if the detecting condition meets, the throttle valve moves to a specified position and closes to the target position by the throttle valve return spring. If the throttle valve does not move to the target position range, the PCM detects a throttle valve return spring malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 158 deg.F (70 deg.C) | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

The throttle valve opening angle is 17 deg. or more, 11 deg. or less, for at least 2.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve return spring failure

- Throttle valve friction increase (poor action)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

- Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5804: DTC P16BB (K20C1) (2017 2018 2019)

- Title: DTC P16BB (K20C1) (2017 2018 2019)
- Source path: `pages\6937.html`
- Chunk ID: `chunk_003fc4080007`
- Images: `images\GHH403350.jpeg`
- Duplicate sources: `pages\8524.html`, `pages\22700.html`, `pages\21113.html`

### Full Text

````text
# DTC P16BB (K20C1) (2017 2018 2019)

DTC P16BB: Alternator B Terminal Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the battery's state of charge, the electrical load, and the engine speed. If the FI MAIN RLY OUT terminal voltage and the alternator output are out of a specified value for a set time while the PCM commands a target generating voltage to 14.5 V at a specified engine speed, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

Alternator control mode | 14 V

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 12.0 V or less, and the alternator duty cycle is within 5 % to 50 % for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- Alternator internal failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Maintain an engine speed [Engine Speed] of 500 rpm or more.

- Turn on the headlights (high beam) and rear window defogger.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5805: DTC P16BB (K20C1) (2019 2020 2021)

- Title: DTC P16BB (K20C1) (2019 2020 2021)
- Source path: `pages\6938.html`
- Chunk ID: `chunk_8167af00e476`
- Images: `images\GHH403351.jpeg`
- Duplicate sources: `pages\8525.html`, `pages\22701.html`, `pages\21114.html`

### Full Text

````text
# DTC P16BB (K20C1) (2019 2020 2021)

DTC P16BB: Alternator B Terminal Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the battery's state of charge, the electrical load, and the engine speed. If the FI MAIN RLY OUT terminal voltage and the alternator output are out of a specified value for a set time while the request voltage to the alternator is 14 V at a specified engine speed, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The 12 volt battery voltage is less than 11 V when the alternator request voltage is more than 14 V, and the alternator power generation amount is within 5 % to 50 % for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- Alternator internal failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Maintain an engine speed [Engine Speed] of 500 rpm or more.

- Turn on the headlights (high beam) and rear window defogger.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5806: DTC P16BB (K20C2)

- Title: DTC P16BB (K20C2)
- Source path: `pages\6939.html`
- Chunk ID: `chunk_01d2ed077d59`
- Images: `images\GHH403352.jpeg`
- Duplicate sources: `pages\8526.html`, `pages\22702.html`, `pages\21115.html`

### Full Text

````text
# DTC P16BB (K20C2)

DTC P16BB: Alternator B Terminal Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the 12 volt battery's state of charge, the electrical load, and the engine speed. If the FI MAIN RLY OUT terminal voltage and the alternator output are out of a specified value for a set time while the PCM commands a target generating voltage to 14.5 V at a specified engine speed, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 500 rpm | 3, 000 rpm

Alternator control mode | 14.5 V mode

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 12.0 V or less, and the alternator power generation amount is within 1.0 % to 50.0 % for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- Alternator internal failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Maintain an engine speed [ENGINE SPEED] of 500 rpm to 3, 000 rpm.

- Turn on the headlights (high beam) and rear window defogger.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5807: DTC P16BB (L15B7/L15BA/L15BY)

- Title: DTC P16BB (L15B7/L15BA/L15BY)
- Source path: `pages\6940.html`
- Chunk ID: `chunk_7c9c234c2ff1`
- Images: `images\GHH403353.jpeg`
- Duplicate sources: `pages\8527.html`, `pages\22703.html`, `pages\21116.html`

### Full Text

````text
# DTC P16BB (L15B7/L15BA/L15BY)

DTC P16BB: Alternator B Terminal Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the 12 volt battery's state of charge, the electrical load, and the engine speed. If the FI MAIN RLY OUT terminal voltage and the alternator output are out of a specified value for a set time while the PCM commands a target generating voltage to 14.5 V at a specified engine speed, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 500 rpm | 3, 000 rpm

Alternator control mode | 14.5 V mode

[ ]: HDS Parameter

Malfunction Threshold

The FI MAIN RLY OUT terminal voltage is 12.0 V or less, and the alternator power generation amount is within 1.0 % to 50.0 % for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator side B terminal disconnection

- Under-hood fuse/relay box side B terminal disconnection

- Alternator internal failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Maintain an engine speed [ENGINE SPEED] of 500 rpm to 3, 000 rpm.

- Turn on the headlights (high beam) and rear window defogger.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5808: DTC P16E2 (K20C1) (2017 2018 2019)

- Title: DTC P16E2 (K20C1) (2017 2018 2019)
- Source path: `pages\6941.html`
- Chunk ID: `chunk_eb54acdd67e7`
- Images: `images\GHH403354.jpeg`
- Duplicate sources: `pages\8528.html`, `pages\22704.html`, `pages\21117.html`

### Full Text

````text
# DTC P16E2 (K20C1) (2017 2018 2019)

DTC P16E2: PGM-FI-ACG LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) transmits/receives signals to/from the alternator. If the powertrain control module (PCM) receives incorrect information from the alternator, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Non Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1.5 seconds:

- Checksum error There is a mismatch in the checksum.

There is a mismatch in the checksum.

- Frame error There is a deviation in the LIN frame.

There is a deviation in the LIN frame.

- Header timeout error There is a fault in the LIN line caused by problems with the physical layer connection.

There is a fault in the LIN line caused by problems with the physical layer connection.

- Message timeout error The slave node is unable to respond as an acknowledgment to the header frame from the master node.

The slave node is unable to respond as an acknowledgment to the header frame from the master node.

- Overrun error LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator LIN line open

- Alternator LIN line short to ground

- Alternator failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5809: DTC P16E2 (K20C1) (2019 2020 2021)

- Title: DTC P16E2 (K20C1) (2019 2020 2021)
- Source path: `pages\6942.html`
- Chunk ID: `chunk_ccf4be740dc1`
- Images: `images\GHH403355.jpeg`
- Duplicate sources: `pages\8529.html`, `pages\22705.html`, `pages\21118.html`

### Full Text

````text
# DTC P16E2 (K20C1) (2019 2020 2021)

DTC P16E2: PGM-FI-ACG LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) transmits/receives signals to/from the alternator. If the powertrain control module (PCM) receives incorrect information from the alternator, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the ON mode | 3 seconds | -

12 volt battery voltage [Battery]* | 10.04 V | -

*: For at least 5 seconds[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1.5 seconds:

- Checksum error There is a mismatch in the checksum.

There is a mismatch in the checksum.

- Frame error There is a deviation in the LIN frame.

There is a deviation in the LIN frame.

- Header timeout error There is a fault in the LIN line caused by problems with the physical layer connection.

There is a fault in the LIN line caused by problems with the physical layer connection.

- Message timeout error The slave node is unable to respond as an acknowledgment to the header frame from the master node.

The slave node is unable to respond as an acknowledgment to the header frame from the master node.

- Overrun error LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator LIN line open

- Alternator LIN line short to ground

- Alternator failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5810: DTC P16E2 (K20C2)

- Title: DTC P16E2 (K20C2)
- Source path: `pages\6943.html`
- Chunk ID: `chunk_5e3c872e1736`
- Images: `images\GHH403356.jpeg`
- Duplicate sources: `pages\8530.html`, `pages\22706.html`, `pages\21119.html`

### Full Text

````text
# DTC P16E2 (K20C2)

DTC P16E2: PGM-FI-ACG LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) line connects the alternator and the powertrain control module (PCM). The LIN uses a master/slave protocol to send and receive data to the different components on the line. The PCM is the master unit, which controls the engine electrical system. The 12 volt battery sensor and the alternator are the slaves. The alternator receives data from the PCM and provides feedback to the PCM, which allows the PCM to operate the engine electrical system efficiently. When the PCM does not receive signals from the alternator within its specified amount of time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5 seconds:

- The PCM cannot receive any information via the LIN line.

- The information sent from the alternator is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure

- Alternator LIN(BATT SENSOR) line open

- Alternator LIN(BATT SENSOR) line short

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5811: DTC P16E2 (Without XM)

- Title: DTC P16E2 (Without XM)
- Source path: `pages\6944.html`
- Chunk ID: `chunk_af4646ee0739`
- Images: `images\GHH403357.jpeg`
- Duplicate sources: `pages\8531.html`, `pages\22707.html`, `pages\21120.html`

### Full Text

````text
# DTC P16E2 (Without XM)

DTC P16E2: PGM-FI-ACG LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) line connects the alternator and the powertrain control module (PCM). The LIN uses a master/slave protocol to send and receive data to the different components on the line. The PCM is the master unit, which controls the engine electrical system. The 12 volt battery sensor and the alternator are the slaves. The alternator receives data from the PCM and provides feedback to the PCM, which allows the PCM to operate the engine electrical system efficiently. When the PCM does not receive signals from the alternator within its specified amount of time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5 seconds:

- The PCM cannot receive any information via the LIN line.

- The information sent from the alternator is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator failure

- Alternator LIN(BATT SENSOR) line open

- Alternator LIN(BATT SENSOR) line short

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5812: DTC P16E3 (K20C1) (2017 2018 2019)

- Title: DTC P16E3 (K20C1) (2017 2018 2019)
- Source path: `pages\6945.html`
- Chunk ID: `chunk_ffa8b0f56a14`
- Images: `images\GHH403358.jpeg`
- Duplicate sources: `pages\8532.html`, `pages\22708.html`, `pages\21121.html`

### Full Text

````text
# DTC P16E3 (K20C1) (2017 2018 2019)

DTC P16E3: PGM-FI-Battery Sensor LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) transmits/receives signals to/from the 12 volt battery sensor. If the powertrain control module (PCM) receives incorrect information from the 12 volt battery sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Non Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1.5 seconds:

- Checksum error There is a mismatch in the checksum.

There is a mismatch in the checksum.

- Frame error There is a deviation in the LIN frame.

There is a deviation in the LIN frame.

- Header timeout error There is a fault in the LIN line caused by problems with the physical layer connection.

There is a fault in the LIN line caused by problems with the physical layer connection.

- Message timeout error The slave node is unable to respond as an acknowledgment to the header frame from the master node.

The slave node is unable to respond as an acknowledgment to the header frame from the master node.

- Overrun error LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

- No start communication error There is no wake-up request.

There is no wake-up request.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor LIN line open

- 12 volt battery sensor LIN line short to ground

- 12 volt battery sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5813: DTC P16E3 (K20C1) (2019 2020 2021)

- Title: DTC P16E3 (K20C1) (2019 2020 2021)
- Source path: `pages\6946.html`
- Chunk ID: `chunk_5c8a3b8c8df3`
- Images: `images\GHH403359.jpeg`
- Duplicate sources: `pages\8533.html`, `pages\22709.html`, `pages\21122.html`

### Full Text

````text
# DTC P16E3 (K20C1) (2019 2020 2021)

DTC P16E3: PGM-FI-Battery Sensor LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) transmits/receives signals to/from the 12 volt battery sensor. If the powertrain control module (PCM) receives incorrect information from the 12 volt battery sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the ON mode | 3 seconds | -

12 volt battery voltage [Battery]* | 10.04 V | -

*: For at least 5 seconds[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1.5 seconds:

- Checksum error There is a mismatch in the checksum.

There is a mismatch in the checksum.

- Frame error There is a deviation in the LIN frame.

There is a deviation in the LIN frame.

- Header timeout error There is a fault in the LIN line caused by problems with the physical layer connection.

There is a fault in the LIN line caused by problems with the physical layer connection.

- Message timeout error The slave node is unable to respond as an acknowledgment to the header frame from the master node.

The slave node is unable to respond as an acknowledgment to the header frame from the master node.

- Overrun error LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

LIN frame has been overwritten in the receive buffer by another frame before the previous frame was read.

- No start communication error There is no wake-up request.

There is no wake-up request.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor LIN line open

- 12 volt battery sensor LIN line short to ground

- 12 volt battery sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5814: DTC P16E3 (K20C2)

- Title: DTC P16E3 (K20C2)
- Source path: `pages\6947.html`
- Chunk ID: `chunk_37aa35beb6a0`
- Images: `images\GHH403360.jpeg`
- Duplicate sources: `pages\8534.html`, `pages\22710.html`, `pages\21123.html`

### Full Text

````text
# DTC P16E3 (K20C2)

DTC P16E3: PGM-FI-Battery Sensor LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) line is connects the 12 volt battery sensor and the powertrain control module (PCM). The LIN uses a master/slave protocol to send and receive data to the different components on the line. The PCM is the master unit, which controls the engine electrical system. The 12 volt battery sensor and the alternator are the slaves. The 12 volt battery sensor receives data from the PCM and provides feedback to the PCM, which allows the PCM to operate the engine electrical system efficiently. When the PCM does not receive signals from the 12 volt battery sensor within its specified amount of time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5 seconds:

- The PCM cannot receive any information via the LIN line.

- The information sent from the 12 volt battery sensor is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor LIN(BATT SENSOR) line open

- 12 volt battery sensor LIN(BATT SENSOR) line short

- 12 volt battery sensor failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5815: DTC P16E3 (L15B7/L15BA/L15BY)

- Title: DTC P16E3 (L15B7/L15BA/L15BY)
- Source path: `pages\6948.html`
- Chunk ID: `chunk_fde5c9a488b8`
- Images: `images\GHH403361.jpeg`
- Duplicate sources: `pages\8535.html`, `pages\22711.html`, `pages\21124.html`

### Full Text

````text
# DTC P16E3 (L15B7/L15BA/L15BY)

DTC P16E3: PGM-FI-Battery Sensor LIN Communication Error

General Description

Courtesy of HONDA, U.S.A., INC.

The local interconnect network (LIN) line is connects the 12 volt battery sensor and the powertrain control module (PCM). The LIN uses a master/slave protocol to send and receive data to the different components on the line. The PCM is the master unit, which controls the engine electrical system. The 12 volt battery sensor and the alternator are the slaves. The 12 volt battery sensor receives data from the PCM and provides feedback to the PCM, which allows the PCM to operate the engine electrical system efficiently. When the PCM does not receive signals from the 12 volt battery sensor within its specified amount of time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5 seconds:

- The PCM cannot receive any information via the LIN line.

- The information sent from the 12 volt battery sensor is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- 12 volt battery sensor LIN(BATT SENSOR) line open

- 12 volt battery sensor LIN(BATT SENSOR) line short

- 12 volt battery sensor failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5816: DTC P16E4 (K20C1) (2017 2018 2019)

- Title: DTC P16E4 (K20C1) (2017 2018 2019)
- Source path: `pages\6949.html`
- Chunk ID: `chunk_93e418437c70`
- Images: `images\GHH403362.jpeg`
- Duplicate sources: `pages\8536.html`, `pages\22712.html`, `pages\21125.html`

### Full Text

````text
# DTC P16E4 (K20C1) (2017 2018 2019)

DTC P16E4: ACG High-temperature

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according the battery's state of charge, the electrical load, and the engine speed. The voltage regulator in the alternator runs a self-diagnostic function by PCM command, the results are transmitted via the LIN line. If the self-diagnosed results are judged that the alternator temperature is too high, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

High temperature of the alternator is reported for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ambient temperature extreme increase

- Alternator internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5817: DTC P16E4 (K20C1) (2019 2020 2021)

- Title: DTC P16E4 (K20C1) (2019 2020 2021)
- Source path: `pages\6950.html`
- Chunk ID: `chunk_a07778f2550e`
- Images: `images\GHH403363.jpeg`
- Duplicate sources: `pages\8537.html`, `pages\22713.html`, `pages\21126.html`

### Full Text

````text
# DTC P16E4 (K20C1) (2019 2020 2021)

DTC P16E4: ACG High-temperature

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) continuously monitors the alternator via the local interconnect network (LIN) lines. If the PCM receives a high temperature information of the alternator, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 500 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM receives a high temperature information of the alternator for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Alternator internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5818: DTC P16E4 (K20C2)

- Title: DTC P16E4 (K20C2)
- Source path: `pages\6951.html`
- Chunk ID: `chunk_1c139a80702b`
- Images: `images\GHH403364.jpeg`
- Duplicate sources: `pages\8538.html`, `pages\22714.html`, `pages\21127.html`

### Full Text

````text
# DTC P16E4 (K20C2)

DTC P16E4: ACG High-temperature

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the 12 volt battery's state of charge, the electrical load, and the engine speed. The voltage regulator in the alternator runs a self-diagnostic function by PCM command, the results are transmitted via the LIN line. If the self-diagnosed results are judged that the alternator temperature is too high, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The alternator internal temperature is 320 deg.F (160 deg.C) or more, for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ambient temperature extreme increase

- Alternator internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5819: DTC P16E4 (L15B7/L15BA/L15BY)

- Title: DTC P16E4 (L15B7/L15BA/L15BY)
- Source path: `pages\6952.html`
- Chunk ID: `chunk_c034f17f0794`
- Images: `images\GHH403365.jpeg`
- Duplicate sources: `pages\8539.html`, `pages\22715.html`, `pages\21128.html`

### Full Text

````text
# DTC P16E4 (L15B7/L15BA/L15BY)

DTC P16E4: ACG High-temperature

General Description

Courtesy of HONDA, U.S.A., INC.

Driven by the engine, the alternator generates electricity according to the commands from the powertrain control module (PCM). The local interconnect network (LIN) line is connected to the alternator and transmits/receives information to/from the PCM. The PCM sets a target generating voltage in the range of 12.5 V to 14.5 V and commands the alternator via the LIN line. The alternator output signal (duty signal) is sent to the PCM, and is varied according to the 12 volt battery's state of charge, the electrical load, and the engine speed. The voltage regulator in the alternator runs a self-diagnostic function by PCM command, the results are transmitted via the LIN line. If the self-diagnosed results are judged that the alternator temperature is too high, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 60 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The alternator internal temperature is 320 deg.F (160 deg.C) or more, for at least 60 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ambient temperature extreme increase

- Alternator internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5820: DTC P16E6 (K20C2 (CVT) with Keyless Access System)

- Title: DTC P16E6 (K20C2 (CVT) with Keyless Access System)
- Source path: `pages\6953.html`
- Chunk ID: `chunk_ffa1fd304cc9`
- Images: `images\GHH403366.jpeg`
- Duplicate sources: `pages\8540.html`, `pages\22716.html`, `pages\21129.html`

### Full Text

````text
# DTC P16E6 (K20C2 (CVT) with Keyless Access System)

DTC P16E6: Transmission Range Switch START Switch Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode, or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ATP ST terminal is high for a specified time when the shift position is in other than P or N during the vehicle is in ON mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Shift lever position/mode | Other than P or N

Malfunction Threshold

ATP ST terminal is high for at least 5 seconds when the shift position is in other than P or N position/mode during the vehicle is in ON mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Transmission range switch ATP ST line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5821: DTC P16E6 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P16E6 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\6954.html`
- Chunk ID: `chunk_1aeab91fdf4a`
- Images: `images\GHH403367.jpeg`
- Duplicate sources: `pages\8541.html`, `pages\22717.html`, `pages\21130.html`

### Full Text

````text
# DTC P16E6 (L15B7/L15BA/L15BY (CVT))

DTC P16E6: Transmission Range Switch START Switch Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode, or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ATPST terminal is high for a specified time when the shift position is in other than P or N during the vehicle is in ON mode, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Shift lever position/mode | Other than P or N

Malfunction Threshold

ATPST terminal is high for at least 5 seconds when the shift position is in other than P or N position/mode during the vehicle is in ON mode.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Transmission range switch ATPST line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5822: DTC P16F3 (K20C1) (2017 2018 2019)

- Title: DTC P16F3 (K20C1) (2017 2018 2019)
- Source path: `pages\6955.html`
- Chunk ID: `chunk_cfb060d4370b`
- Images: `images\GHH403368.jpeg`
- Duplicate sources: `pages\8542.html`, `pages\22718.html`, `pages\21131.html`

### Full Text

````text
# DTC P16F3 (K20C1) (2017 2018 2019)

DTC P16F3: Starter Cut Relay 1 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the starter control system. Open load and short circuit to ground can be detected only if starter cut relay driver IC is not active. If the PCM detects a short to ground or an open in the starter cut relay 1 circuit, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short to ground or an open in the starter cut relay 1 circuit for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line open

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5823: DTC P16F3 (K20C1) (2019 2020 2021)

- Title: DTC P16F3 (K20C1) (2019 2020 2021)
- Source path: `pages\6956.html`
- Chunk ID: `chunk_458a9a274e79`
- Images: `images\GHH403369.jpeg`
- Duplicate sources: `pages\8543.html`, `pages\22719.html`, `pages\21132.html`

### Full Text

````text
# DTC P16F3 (K20C1) (2019 2020 2021)

DTC P16F3: Starter Cut Relay 1 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the starter control system. Open load and short circuit to ground can be detected only if starter cut relay driver IC is not active. If the PCM detects a short to ground or an open in the starter cut relay 1 circuit, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short to ground or an open in the starter cut relay 1 circuit for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line open

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5824: DTC P16F3 (K20C2: With Keyless Access System)

- Title: DTC P16F3 (K20C2: With Keyless Access System)
- Source path: `pages\6957.html`
- Chunk ID: `chunk_ba119ae4372e`
- Images: `images\GHH403370.jpeg`
- Duplicate sources: `pages\8544.html`, `pages\22720.html`, `pages\21133.html`

### Full Text

````text
# DTC P16F3 (K20C2: With Keyless Access System)

DTC P16F3: Starter Cut Relay 1 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY1 CL- return signal is LOW for a specified time when the starter is OFF (STS OFF), the PCM detects an open or a short to ground of the ST CUT RLY1 CL- and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ST CUT RLY1 CL- return signal is LOW for at least 5 seconds when the starter is OFF (STS OFF).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to ground

- Starter cut relay 1 circuit ST CUT RLY1 CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5825: DTC P16F3 (L15B7/L15BA)

- Title: DTC P16F3 (L15B7/L15BA)
- Source path: `pages\6958.html`
- Chunk ID: `chunk_8475e87e29d4`
- Images: `images\GHH403371.jpeg`
- Duplicate sources: `pages\8545.html`, `pages\22721.html`, `pages\21134.html`

### Full Text

````text
# DTC P16F3 (L15B7/L15BA)

DTC P16F3: Starter Cut Relay 1 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY1 CL- return signal is LOW for a specified time when the starter is OFF (STS OFF), the PCM detects an open or a short to ground of the ST CUT RLY1 CL- and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ST CUT RLY1 CL- return signal is LOW for at least 5 seconds when the starter is OFF (STS OFF).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to ground

- Starter cut relay 1 circuit ST CUT RLY1 CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5826: DTC P16F4 (K20C1) (2017 2018 2019)

- Title: DTC P16F4 (K20C1) (2017 2018 2019)
- Source path: `pages\6959.html`
- Chunk ID: `chunk_bfb62dacd754`
- Images: `images\GHH403372.jpeg`
- Duplicate sources: `pages\8546.html`, `pages\22722.html`, `pages\21135.html`

### Full Text

````text
# DTC P16F4 (K20C1) (2017 2018 2019)

DTC P16F4: Starter Cut Relay 2 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the starter control system. Open load and short circuit to ground can be detected only if starter cut relay driver IC is not active. If the PCM detects a short to ground or an open in the starter cut relay 2 circuit, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short to ground or an open in the starter cut relay 2 circuit for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line open

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5827: DTC P16F4 (K20C1) (2019 2020 2021)

- Title: DTC P16F4 (K20C1) (2019 2020 2021)
- Source path: `pages\6960.html`
- Chunk ID: `chunk_c98d1da83a90`
- Images: `images\GHH403373.jpeg`
- Duplicate sources: `pages\8547.html`, `pages\22723.html`, `pages\21136.html`

### Full Text

````text
# DTC P16F4 (K20C1) (2019 2020 2021)

DTC P16F4: Starter Cut Relay 2 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the starter control system. Open load and short circuit to ground can be detected only if starter cut relay driver IC is not active. If the PCM detects a short to ground or an open in the starter cut relay 2 circuit, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short to ground or an open in the starter cut relay 2 circuit for at least 0.3 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line open

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5828: DTC P16F4 (K20C2: With Keyless Access System)

- Title: DTC P16F4 (K20C2: With Keyless Access System)
- Source path: `pages\6961.html`
- Chunk ID: `chunk_5ee3165a7036`
- Images: `images\GHH403374.jpeg`
- Duplicate sources: `pages\8548.html`, `pages\22724.html`, `pages\21137.html`

### Full Text

````text
# DTC P16F4 (K20C2: With Keyless Access System)

DTC P16F4: Starter Cut Relay 2 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY2 CL- return signal is LOW for a specified time when the starter is OFF (STS OFF), the PCM detects an open or a short to ground of the ST CUT RLY2 CL- and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ST CUT RLY2 CL- return signal is LOW for at least 5 seconds when the starter is OFF (STS OFF).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to ground

- Starter cut relay 2 circuit ST CUT RLY2 CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5829: DTC P16F4 (L15B7/L15BA/L15BY)

- Title: DTC P16F4 (L15B7/L15BA/L15BY)
- Source path: `pages\6962.html`
- Chunk ID: `chunk_d6e6ae31c42d`
- Images: `images\GHH403375.jpeg`
- Duplicate sources: `pages\8549.html`, `pages\22725.html`, `pages\21138.html`

### Full Text

````text
# DTC P16F4 (L15B7/L15BA/L15BY)

DTC P16F4: Starter Cut Relay 2 Control Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY2 CL- return signal is LOW for a specified time when the starter is OFF (STS OFF), the PCM detects an open or a short to ground of the ST CUT RLY2 CL- and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ST CUT RLY2 CL- return signal is LOW for at least 5 seconds when the starter is OFF (STS OFF).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to ground

- Starter cut relay 2 circuit ST CUT RLY2 CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5830: DTC P16F5 (K20C1) (2017 2018 2019)

- Title: DTC P16F5 (K20C1) (2017 2018 2019)
- Source path: `pages\6963.html`
- Chunk ID: `chunk_1553bf0cf6ae`
- Images: `images\GHH403376.jpeg`
- Duplicate sources: `pages\8550.html`, `pages\22726.html`, `pages\21139.html`

### Full Text

````text
# DTC P16F5 (K20C1) (2017 2018 2019)

DTC P16F5: Starter Cut Relay 1 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The short to power in starter cut relay circuit can be detected only if the starter driver is active. The monitoring is done by the powertrain control module (PCM). To check both starter relays, the sequence of switching starter driver off (means which starter driver has to be switched off first) is changed at every start. The switch off sequence for starter driver is changed at the end of every starter operation. If the PCM detects a short circuit to power at starter cut relay 1, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.26 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery]* | 8 V | -

State of the engine* | Running

Other | Starter operation is finished

*: Conditions are met for at least 2.2 seconds[ ]: HDS Parameter

Malfunction Threshold

The PCM detects a short circuit to power at starter cut relay 1 circuit for at least 0.26 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to power

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5831: DTC P16F5 (K20C1) (2019 2020 2021)

- Title: DTC P16F5 (K20C1) (2019 2020 2021)
- Source path: `pages\6964.html`
- Chunk ID: `chunk_2993fc7e3c8e`
- Images: `images\GHH403377.jpeg`
- Duplicate sources: `pages\8551.html`, `pages\22727.html`, `pages\21140.html`

### Full Text

````text
# DTC P16F5 (K20C1) (2019 2020 2021)

DTC P16F5: Starter Cut Relay 1 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The short to power in starter cut relay circuit can be detected only if the starter driver is active. The monitoring is done by the powertrain control module (PCM). To check both starter relays, the sequence of switching starter driver off (means which starter driver has to be switched off first) is changed at every start. The switch off sequence for starter driver is changed at the end of every starter operation. If the PCM detects a short circuit to power at starter cut relay 1, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.26 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short circuit to power at starter cut relay 1 circuit for at least 0.26 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5832: DTC P16F5 (K20C2: With Keyless Access System)

- Title: DTC P16F5 (K20C2: With Keyless Access System)
- Source path: `pages\6965.html`
- Chunk ID: `chunk_61fa07dca232`
- Images: `images\GHH403378.jpeg`
- Duplicate sources: `pages\8552.html`, `pages\22728.html`, `pages\21141.html`

### Full Text

````text
# DTC P16F5 (K20C2: With Keyless Access System)

DTC P16F5: Starter Cut Relay 1 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY1 CL- return signal is HIGH for a specified time when the starter is ON (STS ON), the PCM detects a short to power of the ST CUT RLY1 CL- line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The ST CUT RLY1 CL- return signal is HIGH for at least 0.3 second when the starter is ON (STS ON).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5833: DTC P16F5 (L15B7/L15BA)

- Title: DTC P16F5 (L15B7/L15BA)
- Source path: `pages\6966.html`
- Chunk ID: `chunk_69d2bf7b901c`
- Images: `images\GHH403379.jpeg`
- Duplicate sources: `pages\8553.html`, `pages\22729.html`, `pages\21142.html`

### Full Text

````text
# DTC P16F5 (L15B7/L15BA)

DTC P16F5: Starter Cut Relay 1 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY1 CL- return signal is HIGH for a specified time when the starter is ON (STS ON), the PCM detects a short to power of the ST CUT RLY1 CL- line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The ST CUT RLY1 CL- return signal is HIGH for at least 0.3 second when the starter is ON (STS ON).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 1 circuit ST CUT RLY1 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5834: DTC P16F6 (K20C1) (2017 2018 2019)

- Title: DTC P16F6 (K20C1) (2017 2018 2019)
- Source path: `pages\6967.html`
- Chunk ID: `chunk_d6c7cec8a801`
- Images: `images\GHH403380.jpeg`
- Duplicate sources: `pages\8554.html`, `pages\22730.html`, `pages\21143.html`

### Full Text

````text
# DTC P16F6 (K20C1) (2017 2018 2019)

DTC P16F6: Starter Cut Relay 2 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The short to power in starter cut relay circuit can be detected only if the starter driver is active. The monitoring is done by the powertrain control module (PCM). To check both starter relays, the sequence of switching starter driver off (means which starter driver has to be switched off first) is changed at every start. The switch off sequence for starter driver is changed at the end of every starter operation. If the PCM detects a short circuit to power at starter cut relay 2, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.26 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery]* | 8 V | -

State of the engine* | Running

Other | Starter operation is finished

*: Conditions are met for at least 2.2 seconds[ ]: HDS Parameter

Malfunction Threshold

The PCM detects a short circuit to power at starter cut relay 2 circuit for at least 0.26 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to power

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5835: DTC P16F6 (K20C1) (2019 2020 2021)

- Title: DTC P16F6 (K20C1) (2019 2020 2021)
- Source path: `pages\6968.html`
- Chunk ID: `chunk_7e84a8a108f8`
- Images: `images\GHH403381.jpeg`
- Duplicate sources: `pages\8555.html`, `pages\22731.html`, `pages\21144.html`

### Full Text

````text
# DTC P16F6 (K20C1) (2019 2020 2021)

DTC P16F6: Starter Cut Relay 2 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The short to power in starter cut relay circuit can be detected only if the starter driver is active. The monitoring is done by the powertrain control module (PCM). To check both starter relays, the sequence of switching starter driver off (means which starter driver has to be switched off first) is changed at every start. The switch off sequence for starter driver is changed at the end of every starter operation. If the PCM detects a short circuit to power at starter cut relay 2, a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.26 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The PCM detects a short circuit to power at starter cut relay 2 circuit for at least 0.26 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5836: DTC P16F6 (K20C2: USA/Canada models with Keyless Access System)

- Title: DTC P16F6 (K20C2: USA/Canada models with Keyless Access System)
- Source path: `pages\6969.html`
- Chunk ID: `chunk_b396e6584f53`
- Images: `images\GHH403382.jpeg`
- Duplicate sources: `pages\8556.html`, `pages\22732.html`, `pages\21145.html`

### Full Text

````text
# DTC P16F6 (K20C2: USA/Canada models with Keyless Access System)

DTC P16F6: Starter Cut Relay 2 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY2 CL- return signal is HIGH for a specified time when the starter is ON (STS ON), the PCM detects a short to power of the ST CUT RLY2 CL- line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The ST CUT RLY2 CL- return signal is HIGH for at least 0.3 second when the starter is ON (STS ON).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5837: DTC P16F6 (L15B7/L15BA)

- Title: DTC P16F6 (L15B7/L15BA)
- Source path: `pages\6970.html`
- Chunk ID: `chunk_8b5c8273078d`
- Images: `images\GHH403383.jpeg`
- Duplicate sources: `pages\8557.html`, `pages\22733.html`, `pages\21146.html`

### Full Text

````text
# DTC P16F6 (L15B7/L15BA)

DTC P16F6: Starter Cut Relay 2 Control Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The starter control system prevents the starter from accidentally activating when the shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T), or when the engine is running. If the vehicle is turned mistakenly while shift position is not in P or N position/mode (CVT) or the clutch pedal is released (M/T) or while the engine is running, the powertrain control module (PCM) will stop power to the starter cut relay circuits. However, cranking to return from auto idle stop does not correspond to this (if equipped). In this system, two starter cut relay circuits are connected in series (starter cut relay 1 circuit, starter cut relay 2 circuit) to prevent the starter from running continuously due to a starter cut relay circuit malfunction. Also a diagnosis line (ST RLY 1 TO 2) is connected to monitor the voltage between the starter cut relay 1 circuit and starter cut relay 2 circuit. Based on the diagnosis line signals, the PCM detects an OPEN malfunction of diagnosis line, an ON malfunction of starter cut relay 1 circuit, and an ON malfunction of starter cut relay 2 circuit. The PCM also equips with return signal circuits of starter cut relay 1 circuit and starter cut relay 2 circuit to detect an OFF malfunction. If the ST CUT RLY2 CL- return signal is HIGH for a specified time when the starter is ON (STS ON), the PCM detects a short to power of the ST CUT RLY2 CL- line and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.3 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Starter | ON

Malfunction Threshold

The ST CUT RLY2 CL- return signal is HIGH for at least 0.3 second when the starter is ON (STS ON).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Starter cut relay 2 circuit ST CUT RLY2 CL- line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command by disconnecting the 12 volt battery.
````

## Chunk 5838: DTC P1701 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P1701 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\6971.html`
- Chunk ID: `chunk_dfc2a29f97c7`
- Images: `images\GHH403384.jpeg`
- Duplicate sources: `pages\8558.html`, `pages\22734.html`, `pages\21147.html`

### Full Text

````text
# DTC P1701 (K20C1) (2017 2018 2019 2020 2021)

DTC P1701: Back-Up Light Switch Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the back-up light switch for rationality faults. The back-up light switch signal is used to detect whether the vehicle is running in reverse. If the back-up light switch is stayed ON for a certain distance, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.5 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The back-up light switch stayed ON for at least 100 milliseconds while the vehicle is driven for 2 miles (2 km) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Back-up light switch BACK LT line short to power

- Back-up light switch stuck on

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5839: DTC P1707, P1708 (K20C1) (2017 2018 2019)

- Title: DTC P1707, P1708 (K20C1) (2017 2018 2019)
- Source path: `pages\6972.html`
- Chunk ID: `chunk_b30c47f3a013`
- Images: `images\GHH403385.jpeg`
- Duplicate sources: `pages\8559.html`, `pages\22735.html`, `pages\21148.html`

### Full Text

````text
# DTC P1707, P1708 (K20C1) (2017 2018 2019)

DTC P1707: Neutral Position Sensor B Circuit Low Voltage

DTC P1708: Neutral Position Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the neutral position sensor B output voltage is continuously monitored and compared with minimum and maximum thresholds. If the neutral position sensor B output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P1707

The neutral position sensor B output voltage [Neutral Position Sensor 2] is less than 0.2434 V for at least 0.5 second.

DTC: P1708

The neutral position sensor B output voltage [Neutral Position Sensor 2] is greater than 3.263 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P1707

- Neutral position sensor B VCC line open

- Neutral position sensor B NSS2 line short to ground

DTC: P1708

- Neutral position sensor B NSS2 line short to power

- Neutral position sensor B NSS2 line open

- Neutral position sensor B SG line open

Common

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5840: DTC P1707, P1708 (K20C1) (2019 2020 2021)

- Title: DTC P1707, P1708 (K20C1) (2019 2020 2021)
- Source path: `pages\6973.html`
- Chunk ID: `chunk_cd27fe8936f2`
- Images: `images\GHH403386.jpeg`
- Duplicate sources: `pages\8560.html`, `pages\22736.html`, `pages\21149.html`

### Full Text

````text
# DTC P1707, P1708 (K20C1) (2019 2020 2021)

DTC P1707: Neutral Position Sensor B Circuit Low Voltage

DTC P1708: Neutral Position Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors neutral position sensors for electrical malfunctions. The function is checking if the gear is in the neutral position or not. In order to provide diagnostics, the neutral position sensor B output voltage is continuously monitored and compared with minimum and maximum thresholds. If the neutral position sensor B output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P1707

The neutral position sensor B output voltage [Neutral Position Sensor 2] is less than 0.24 V for at least 0.5 second.

DTC: P1708

The neutral position sensor B output voltage [Neutral Position Sensor 2] is greater than 3.26 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P1707

- Neutral position sensor B VCC line open

- Neutral position sensor B NSS2 line short to ground

DTC: P1708

- Neutral position sensor B NSS2 line short to power

- Neutral position sensor B NSS2 line open

- Neutral position sensor B SG line open

Common

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5841: DTC P1707, P1708 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

- Title: DTC P1707, P1708 (K20C2 (M/T)) (2016 2017 2018 2019 2020)
- Source path: `pages\6974.html`
- Chunk ID: `chunk_6992404f6f62`
- Images: `images\GHH403387.jpeg`
- Duplicate sources: `pages\8561.html`, `pages\22737.html`, `pages\21150.html`

### Full Text

````text
# DTC P1707, P1708 (K20C2 (M/T)) (2016 2017 2018 2019 2020)

DTC P1707: Neutral Position Sensor B Circuit Low Voltage

DTC P1708: Neutral Position Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the neutral position sensor B output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P1707

The neutral position sensor B output voltage is 0.15 V or less for at least 2.0 seconds.

DTC: P1708

The neutral position sensor B output voltage is 3.5 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P1707

- Neutral position sensor B VCC line open

- Neutral position sensor B NSS2 line short to ground

DTC: P1708

- Neutral position sensor B SG line open

- Neutral position sensor B NSS2 line short to power

Common

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5842: DTC P1707, P1708 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

- Title: DTC P1707, P1708 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)
- Source path: `pages\6975.html`
- Chunk ID: `chunk_3eb144b7c7d5`
- Images: `images\GHH403388.jpeg`
- Duplicate sources: `pages\8562.html`, `pages\22738.html`, `pages\21151.html`

### Full Text

````text
# DTC P1707, P1708 (L15B7/L15BA (M/T)) (2017 2018 2019 2020 2021)

DTC P1707: Neutral Position Sensor B Circuit Low Voltage

DTC P1708: Neutral Position Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Table A: Neutral position sensor output voltage

NSS1 voltage | NSS2 voltage

Neutral | 2.7 - 3.0 V | 1.35 - 1.5 V

Neutral position sensor A and neutral position sensor B are semiconductor type that output different voltage characteristics. Each neutral position sensor outputs a voltage which depends on the condition is shown in Table A. The powertrain control module (PCM) judges whether it is in neutral or not from the neutral position sensor output voltage, and uses the information for various controls and auto idle stop system control (if equipped). Neutral position sensor A is for judging the neutral, and neutral position sensor B compares their output voltage to each other for malfunction detection. When the neutral position sensor B output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P1707

The neutral position sensor B output voltage is 0.15 V or less for at least 2.0 seconds.

DTC: P1708

The neutral position sensor B output voltage is 3.5 V or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P1707

- Neutral position sensor B VCC line open

- Neutral position sensor B NSS2 line short to ground

DTC: P1708

- Neutral position sensor B SG line open

- Neutral position sensor B NSS2 line short to power

Common

- Neutral position sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5843: DTC P2073 (K20C2)

- Title: DTC P2073 (K20C2)
- Source path: `pages\6976.html`
- Chunk ID: `chunk_42bb09f9d85e`
- Images: `images\GHH403389.jpeg`, `images\GHH403390.jpeg`, `images\GHH403391.jpeg`
- Duplicate sources: `pages\8563.html`, `pages\22739.html`, `pages\21152.html`

### Full Text

````text
# DTC P2073 (K20C2)

DTC P2073: Manifold Absolute Pressure (MAP) Sensor Signal Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The manifold absolute pressure (MAP) sensor senses manifold absolute pressure (vacuum) and converts it into electrical signals. The MAP sensor outputs low signal voltage at high vacuum (throttle valve closed) and high signal voltage at low vacuum (throttle valve wide open). The powertrain control module (PCM) compares a predetermined MAP value at a given throttle position and manifold absolute pressure to the output voltage value of the MAP sensor. If the MAP sensor outputs high voltage during fuel cut-off operation for deceleration with the throttle valve fully closed, which should make the manifold absolute pressure lower, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after VTEC switched | 3.0 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 200 rpm | 6, 600 rpm

Vehicle speed [VEHICLE SPEED] | 15 mph (24 km/h) | -

Throttle position | Fully closed | -

Fuel feedback | During deceleration | -

[ ]: HDS Parameter

Malfunction Threshold

The MAP sensor output [MAP SENSOR] is 54 kPa (400 mmHg, 15.8 inHg) or more for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal high

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

- Intake air system air leak

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a steady speed between 55 - 75 mph (88 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5844: DTC P2073 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P2073 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\6977.html`
- Chunk ID: `chunk_877be7bc17c4`
- Images: `images\GHH403392.jpeg`, `images\GHH403393.jpeg`, `images\GHH403394.jpeg`
- Duplicate sources: `pages\8564.html`, `pages\22740.html`, `pages\21153.html`

### Full Text

````text
# DTC P2073 (L15B7 (except Si)/L15BA/L15BY)

DTC P2073: Manifold Absolute Pressure (MAP) Sensor Signal Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor, the manifold absolute pressure (MAP) sensor, and the turbocharger boost sensor are equipped to the vehicle to detect air pressure conditions to the engine. The BARO sensor value and the turbocharger boost sensor value shows similar value at range "A" such as in idle conditions, and the turbocharger boost sensor value and MAP sensor value shows similar value at range "B" such as in high throttle position.

Malfunction determinations are done by the powertrain control module (PCM) in two ranges by comparing the pressure sensor values.

- At range "A": BARO sensor or turbocharger boost sensor is abnormal if the difference of the two pressure sensor values are specified or more (P00CF)

- At range "B": Turbocharger boost sensor or MAP sensor is abnormal if the difference of the two pressure sensor values are specified or more (P023D)

- Range "A" determined as abnormal and range "B" determined as normal: BARO sensor abnormal (P0069)

- Both ranges "A" and "B" determined as abnormal: Turbocharger boost sensor abnormal (P0236)

- Turbocharger boost sensor or MAP sensor values do not change when throttle position is transited from ranges "A" to "B": Determined as turbocharger boost sensor output stuck (P0236) or MAP sensor output stuck (P2073 or P2074)

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3.0 seconds | -

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 2, 000 rpm | 36.3 deg. | -

4, 000 rpm | 42.2 deg. | -

Intake air amount | - | 7.0 g/second (0.24 oz/second)

[ ]: HDS Parameter

Malfunction Threshold

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P2073 if either conditions occur:

- The variation of the MAP sensor value measured during range "A" determination and range "B" determination is 0.7 kPa (5 mmHg, 0.2 inHg) or less when range "A" determination and range "B" determination are determined as normal and the difference of the BARO sensor value measured during range "A" determination and range "B" determination is 5.4 kPa (40 mmHg, 1.6 inHg) or less.

- The MAP sensor value is higher than the turbocharger boost sensor value for 27 kPa (200 mmHg, 7.9 inHg) or more* when range "A" determination is determined as normal and range "B" determination is determined as abnormal. *: Threshold value changes depending on throttle position.

*: Threshold value changes depending on throttle position.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal high

- MAP sensor output stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 5 seconds.

- Drive the vehicle at engine speed [ENGINE SPEED] 1, 700 rpm or more with throttle position 42.2 deg. or more for at least 6 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5845: DTC P2073 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2073 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6978.html`
- Chunk ID: `chunk_26d7bd5a86a7`
- Images: `images\GHH403395.jpeg`, `images\GHH403396.jpeg`, `images\GHH403397.jpeg`
- Duplicate sources: `pages\8565.html`, `pages\22741.html`, `pages\21154.html`

### Full Text

````text
# DTC P2073 (Si) (2017 2018 2019 2020 2021)

DTC P2073: Manifold Absolute Pressure (MAP) Sensor Signal Higher Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor, the manifold absolute pressure (MAP) sensor, and the turbocharger boost sensor are equipped to the vehicle to detect air pressure conditions to the engine. The BARO sensor value and the turbocharger boost sensor value shows similar value at range "A" such as in idle conditions, and the turbocharger boost sensor value and MAP sensor value shows similar value at range "B" such as in high throttle position.

Malfunction determinations are done by the powertrain control module (PCM) in two ranges by comparing the pressure sensor values.

- At range "A": BARO sensor or turbocharger boost sensor is abnormal if the difference of the two pressure sensor values are specified or more (P00CF)

- At range "B": Turbocharger boost sensor or MAP sensor is abnormal if the difference of the two pressure sensor values are specified or more (P023D)

- Range "A" determined as abnormal and range "B" determined as normal: BARO sensor abnormal (P0069)

- Both ranges "A" and "B" determined as abnormal: Turbocharger boost sensor abnormal (P0236)

- Turbocharger boost sensor or MAP sensor values do not change when throttle position is transited from ranges "A" to "B": Determined as turbocharger boost sensor output stuck (P0236) or MAP sensor output stuck (P2073 or P2074)

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3.0 seconds | -

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 1, 700 rpm | 34.9 deg. | -

2, 500 rpm | 31.4 deg. | -

Intake air amount | - | 7.0 g/second (0.24 oz/second)

[ ]: HDS Parameter

Malfunction Threshold

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P2073 if either conditions occur:

- The variation of the MAP sensor value measured during range "A" determination and range "B" determination is 0.7 kPa (5 mmHg, 0.2 inHg) or less when range "A" determination and range "B" determination are determined as normal and the difference of the BARO sensor value measured during range "A" determination and range "B" determination is 5.4 kPa (40 mmHg, 1.6 inHg) or less.

- The MAP sensor value is higher than the turbocharger boost sensor value for 27 kPa (200 mmHg, 7.9 inHg) or more* when range "A" determination is determined as normal and range "B" determination is determined as abnormal. *: Threshold value changes depending on throttle position.

*: Threshold value changes depending on throttle position.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal high

- MAP sensor output stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 5 seconds.

- Drive the vehicle at engine speed [ENGINE SPEED] 1, 700 rpm or more with throttle position 34.9 deg. or more for at least 6 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5846: DTC P2074 (K20C2)

- Title: DTC P2074 (K20C2)
- Source path: `pages\6979.html`
- Chunk ID: `chunk_1a32afa44e4c`
- Images: `images\GHH403398.jpeg`, `images\GHH403399.jpeg`
- Duplicate sources: `pages\8566.html`, `pages\22742.html`, `pages\21155.html`

### Full Text

````text
# DTC P2074 (K20C2)

DTC P2074: Manifold Absolute Pressure (MAP) Sensor Signal Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The manifold absolute pressure (MAP) sensor senses manifold absolute pressure (vacuum) and converts it into electrical signals. The MAP sensor outputs low signal voltage at high vacuum (throttle valve closed) and high signal voltage at low vacuum (throttle valve wide open). The powertrain control module (PCM) compares a predetermined MAP value at a given throttle position and manifold absolute pressure to the output voltage value of the MAP sensor. If the MAP sensor outputs lower voltage than expected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after VTEC switched | 3 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 200 rpm | -

Vehicle speed [VEHICLE SPEED] | 15 mph (24 km/h) | -

Throttle position | 1, 000 rpm | 12.0 deg. | -

4, 000 rpm | 30.7 deg. | -

Other | Other than during fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The MAP sensor output [MAP SENSOR] is 54 kPa (406 mmHg, 15.9 inHg) or less for at least 2.0 seconds when atmospheric pressure [BARO SENSOR] is 103 kPa (776 mmHg, 30.6 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal low

- Intake air system clogged

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed of 15 mph (24 km/h) or more under Enable Conditions (see "Throttle position" and "Engine speed [ENGINE SPEED]") for at least 2 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5847: DTC P2074 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P2074 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\6980.html`
- Chunk ID: `chunk_59d6cb559261`
- Images: `images\GHH403400.jpeg`, `images\GHH403401.jpeg`, `images\GHH403402.jpeg`
- Duplicate sources: `pages\8567.html`, `pages\22743.html`, `pages\21156.html`

### Full Text

````text
# DTC P2074 (L15B7 (except Si)/L15BA/L15BY)

DTC P2074: Manifold Absolute Pressure (MAP) Sensor Signal Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor, the manifold absolute pressure (MAP) sensor, and the turbocharger boost sensor are equipped to the vehicle to detect air pressure conditions to the engine. The BARO sensor value and the turbocharger boost sensor value shows similar value at range "A" such as in idle conditions, and the turbocharger boost sensor value and MAP sensor value shows similar value at range "B" such as in high throttle position.

Malfunction determinations are done by the powertrain control module (PCM) in two ranges by comparing the pressure sensor values.

- At range "A": BARO sensor or turbocharger boost sensor is abnormal if the difference of the two pressure sensor values are specified or more (P00CF)

- At range "B": Turbocharger boost sensor or MAP sensor is abnormal if the difference of the two pressure sensor values are specified or more (P023D)

- Range "A" determined as abnormal and range "B" determined as normal: BARO sensor abnormal (P0069)

- Both ranges "A" and "B" determined as abnormal: Turbocharger boost sensor abnormal (P0236)

- Turbocharger boost sensor or MAP sensor values do not change when throttle position is transited from ranges "A" to "B": Determined as turbocharger boost sensor output stuck (P0236) or MAP sensor output stuck (P2073 or P2074)

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3.0 seconds | -

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 2, 000 rpm | 36.3 deg. | -

4, 000 rpm | 42.2 deg. | -

Intake air amount | - | 7.0 g/second (0.24 oz/second)

[ ]: HDS Parameter

Malfunction Threshold

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P2073 if the MAP sensor value is lower than the turbocharger boost sensor value for 27 kPa (200 mmHg, 7.9 inHg) or more* when range "A" determination is determined as normal and range "B" determination is determined as abnormal.

*: Threshold value changes depending on throttle position.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal low

- MAP sensor output stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 5 seconds.

- Drive the vehicle at engine speed [ENGINE SPEED] 1, 700 rpm or more with throttle position 42.2 deg. or more for at least 6 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5848: DTC P2074 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2074 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6981.html`
- Chunk ID: `chunk_52720a1293c9`
- Images: `images\GHH403403.jpeg`, `images\GHH403404.jpeg`, `images\GHH403405.jpeg`
- Duplicate sources: `pages\8568.html`, `pages\22744.html`, `pages\21157.html`

### Full Text

````text
# DTC P2074 (Si) (2017 2018 2019 2020 2021)

DTC P2074: Manifold Absolute Pressure (MAP) Sensor Signal Lower Than Expected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor, the manifold absolute pressure (MAP) sensor, and the turbocharger boost sensor are equipped to the vehicle to detect air pressure conditions to the engine. The BARO sensor value and the turbocharger boost sensor value shows similar value at range "A" such as in idle conditions, and the turbocharger boost sensor value and MAP sensor value shows similar value at range "B" such as in high throttle position.

Malfunction determinations are done by the powertrain control module (PCM) in two ranges by comparing the pressure sensor values.

- At range "A": BARO sensor or turbocharger boost sensor is abnormal if the difference of the two pressure sensor values are specified or more (P00CF)

- At range "B": Turbocharger boost sensor or MAP sensor is abnormal if the difference of the two pressure sensor values are specified or more (P023D)

- Range "A" determined as abnormal and range "B" determined as normal: BARO sensor abnormal (P0069)

- Both ranges "A" and "B" determined as abnormal: Turbocharger boost sensor abnormal (P0236)

- Turbocharger boost sensor or MAP sensor values do not change when throttle position is transited from ranges "A" to "B": Determined as turbocharger boost sensor output stuck (P0236) or MAP sensor output stuck (P2073 or P2074)

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3.0 seconds | -

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 1, 700 rpm | 34.9 deg. | -

2, 500 rpm | 31.9 deg. | -

Intake air amount | - | 7.0 g/second (0.24 oz/second)

[ ]: HDS Parameter

Malfunction Threshold

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P2074 if the MAP sensor value is lower than the turbocharger boost sensor value for 27 kPa (200 mmHg, 7.9 inHg) or more* when range "A" determination is determined as normal and range "B" determination is determined as abnormal.

*: Threshold value changes depending on throttle position.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output signal low

- MAP sensor output stuck

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 5 seconds.

- Drive the vehicle at engine speed [ENGINE SPEED] 1, 700 rpm or more with throttle position 34.9 deg. or more for at least 6 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5849: DTC P2096 (K20C1) (2017 2018 2019)

- Title: DTC P2096 (K20C1) (2017 2018 2019)
- Source path: `pages\6982.html`
- Chunk ID: `chunk_8cbe9b63fa8a`
- Images: `images\GHH403406.jpeg`
- Duplicate sources: `pages\8569.html`, `pages\22745.html`, `pages\21158.html`

### Full Text

````text
# DTC P2096 (K20C1) (2017 2018 2019)

DTC P2096: Post Catalyst Fuel Trim System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The PCM monitors the offset of the air/fuel ratio (A/F) sensor (sensor 1) signal. The test is performed by monitoring the fuel trim control of the secondary heated oxygen sensor (secondary HO2S (sensor 2)). If there is an air/fuel ratio offset measured by the secondary HO2S (sensor 2), the secondary HO2S (sensor 2) fuel trim is used to correct this offset back to the commanded air/fuel ratio. If the offset is present for an extended time, the secondary HO2S (sensor 2) fuel trim is stored as the A/F sensor (sensor 1) offset adaptation. There are two ways that the A/F sensor (sensor 1) offset is adapted. If the secondary HO2S (sensor 2) fuel trim has a small deviation, then the A/F sensor (sensor 1) offset is adapted slowly. If the secondary HO2S (sensor 2) fuel trim has a large deviation, the A/F sensor (sensor 1) offset is adapted faster. If the adapted offset of the A/F sensor (sensor 1) sensor is too large, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 minute 30 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Slow offset adaptation

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 400 rpm | 3, 000 rpm

Charging efficiency | 20.3 % - 99.8 % | 0 % - 69.8 %

Fuel feedback | Closed loop*

Other | Evaporative emission (EVAP) system monitor is not active

*: For at least 300 g (10.59 oz) of integrated amount of exhaust mass flow[ ]: HDS Parameter

Fast offset adaptation

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 104 deg.F (40 deg.C) | -

Engine speed [Engine Speed]** | 1, 000 rpm | -

Exhaust gas mass flow*** | 25 kg/h (56 lbs/h) | 200 kg/h (440 lbs/h)

**: For at least 100 g (3.53 oz) of integrated amount of exhaust gas mass flow

***: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Condition | Minimum | Maximum

Charging efficiency | 0 % | -

Fuel feedback | Closed loop

Other | No significant load changes

Other than during fuel cut-off operation

Misfire rate is not exceeding

EVAP system monitor is not active

**: For at least 100 g (3.53 oz) of integrated amount of exhaust gas mass flow

***: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Lambda offset is greater than 0.045 but less than 0.1 and lambda offset change in non-fault direction for confirmation of fuel trim fault is less than 0.01.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- Exhaust system leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at constant speed with part load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5850: DTC P2096 (K20C1) (2019 2020 2021)

- Title: DTC P2096 (K20C1) (2019 2020 2021)
- Source path: `pages\6983.html`
- Chunk ID: `chunk_186c2f1b74b5`
- Images: `images\GHH403407.jpeg`
- Duplicate sources: `pages\8570.html`, `pages\22746.html`, `pages\21159.html`

### Full Text

````text
# DTC P2096 (K20C1) (2019 2020 2021)

DTC P2096: Post Catalyst Fuel Trim System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The PCM monitors the offset of the air/fuel ratio (A/F) sensor (sensor 1) signal. The test is performed by monitoring the fuel trim control of the secondary heated oxygen sensor (secondary HO2S (sensor 2)). If there is an air/fuel ratio offset measured by the secondary HO2S (sensor 2), the secondary HO2S (sensor 2) fuel trim is used to correct this offset back to the commanded air/fuel ratio. If the offset is present for an extended time, the secondary HO2S (sensor 2) fuel trim is stored as the A/F sensor (sensor 1) offset adaptation. There are two ways that the A/F sensor (sensor 1) offset is adapted. If the secondary HO2S (sensor 2) fuel trim has a small deviation, then the A/F sensor (sensor 1) offset is adapted slowly. If the secondary HO2S (sensor 2) fuel trim has a large deviation, the A/F sensor (sensor 1) offset is adapted faster. If the adapted offset of the A/F sensor (sensor 1) sensor is too large, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Multiple

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Slow offset adaptation

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 400 rpm | 3, 000 rpm

Charging efficiency | 20.3 % - 99.8 % | 0 % - 69.8 %

Fuel feedback | Closed loop*

Other | Evaporative emission (EVAP) system monitor is not active

*: For at least 300 g (10.59 oz) of integrated amount of exhaust mass flow[ ]: HDS Parameter

Fast offset adaptation

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 104 deg.F (40 deg.C) | -

Engine speed [Engine Speed]** | 1, 000 rpm | -

Exhaust gas mass flow | 25 kg/h (56 lbs/h) | 200 kg/h (440 lbs/h)

**: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Condition | Minimum | Maximum

Charging efficiency | 13 % - 22 % | -

Fuel feedback | Closed loop

Other | No significant load changes

Other than during fuel cut-off operation

Misfire rate is not exceeding

EVAP system monitor is not active

**: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Lambda offset is greater than 0.05 but 0.1 or less and lambda offset change in non-fault direction for confirmation of fuel trim fault is less than 0.01.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- Exhaust system leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at constant speed with part load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5851: DTC P2096 (K20C2: USA/Canada models)

- Title: DTC P2096 (K20C2: USA/Canada models)
- Source path: `pages\6984.html`
- Chunk ID: `chunk_cb0c724c3984`
- Images: `images\GHH403408.jpeg`
- Duplicate sources: `pages\8571.html`, `pages\22747.html`, `pages\21160.html`

### Full Text

````text
# DTC P2096 (K20C2: USA/Canada models)

DTC P2096: Post Catalyst Fuel Trim System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects oxygen content in the exhaust gas by the air/fuel ratio (A/F) sensor (sensor 1), and it uses feedback control before the three way catalytic converter (TWC) to bring the air/fuel ratio close to the target air/fuel ratio. The target air/fuel ratio is adjusted by the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output so that the air/fuel ratio in the TWC is optimized. When the A/F sensor (sensor 1) cannot measure air/fuel ratio in the exhaust gas normally, a gap occurs to the actual air/fuel ratio. As a result, the gap causes a deviation in target air/fuel ratio control (after TWC) which is determined by the secondary HO2S (sensor 2). If the deviation exceeds a limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Depending on the driving conditions

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED]* 1 | 550 rpm | 4, 000 rpm

Engine speed [ENGINE SPEED]* 2 | 650 rpm | 4, 000 rpm

Intake air amount* 1 | 7.0 g/second (0.25 oz/second) | -

Intake air amount* 2 | 6.0 g/second (0.22 oz/second) | -

Fuel feedback | Closed loop

*1: CVT model

*2: M/T model

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- Short term fuel trim is lower than -0.03* 3 (-0.032)* 4.

- Long term fuel trim is lower than 0.001.

*3: Except KL models

*4: KL models

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) malfunction/slow response

- A/F sensor (sensor 1) circuit range/performance

- Fuel system too lean

- Fuel system too rich

- Secondary HO2S (sensor 2) circuit signal stuck lean

- Secondary HO2S (sensor 2) circuit open

- Secondary HO2S (sensor 2) slow response

- Misfire

- Air/fuel ratio variation between cylinders

- Exhaust system failure (exhaust gas leak)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 72 seconds* 1 (84 seconds)* 2.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5852: DTC P2096 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P2096 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6985.html`
- Chunk ID: `chunk_85aea3669973`
- Images: `images\GHH403409.jpeg`
- Duplicate sources: `pages\8572.html`, `pages\22748.html`, `pages\21161.html`

### Full Text

````text
# DTC P2096 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P2096: Post Catalyst Fuel Trim System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects oxygen content in the exhaust gas by the air/fuel ratio (A/F) sensor (sensor 1), and it uses feedback control before the three way catalytic converter (TWC) to bring the air/fuel ratio close to the target air/fuel ratio. The target air/fuel ratio is adjusted by the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output so that the air/fuel ratio in the TWC is optimized. When the A/F sensor (sensor 1) cannot measure air/fuel ratio in the exhaust gas normally, a gap occurs to the actual air/fuel ratio. As a result, the gap causes a deviation in target air/fuel ratio control (after TWC) which is determined by the secondary HO2S (sensor 2). If the deviation exceeds a limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Depending on the driving conditions

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED] | 530 rpm | 4, 000 rpm

Intake air amount* 1 | 9.0 g/second (0.32 oz/second) | -

Intake air amount* 2 | 8.0 g/second (0.29 oz/second) | -

Fuel feedback | Closed loop

*1: Except L15BA (M/T)

*2: L15BA (M/T)

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- Short term fuel trim is lower than -0.03* 3 (-0.0537)* 4.

- Long term fuel trim is lower than 0.001.

*3: Except L15BA KL models

*4: L15BA KL models

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) malfunction/slow response

- A/F sensor (sensor 1) circuit range/performance

- Fuel system too lean

- Fuel system too rich

- Secondary HO2S (sensor 2) circuit signal stuck lean

- Secondary HO2S (sensor 2) circuit open

- Secondary HO2S (sensor 2) slow response

- Misfire

- Air/fuel ratio variation between cylinders

- Exhaust system failure (exhaust gas leak)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 62 seconds* 5 (67 seconds)* 4 (69 seconds)* 6.

*5: CVT except L15BA KL models

*6: M/T

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5853: DTC P2096 (L15B7/L15BA) (2016 2017 2018 2019)

- Title: DTC P2096 (L15B7/L15BA) (2016 2017 2018 2019)
- Source path: `pages\6986.html`
- Chunk ID: `chunk_43742f4bf7fe`
- Images: `images\GHH403410.jpeg`
- Duplicate sources: `pages\8573.html`, `pages\22749.html`, `pages\21162.html`

### Full Text

````text
# DTC P2096 (L15B7/L15BA) (2016 2017 2018 2019)

DTC P2096: Post Catalyst Fuel Trim System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects oxygen content in the exhaust gas by the air/fuel ratio (A/F) sensor (sensor 1), and it uses feedback control before the three way catalytic converter (TWC) to bring the air/fuel ratio close to the target air/fuel ratio. The target air/fuel ratio is adjusted by the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output so that the air/fuel ratio in the TWC is optimized. When the A/F sensor (sensor 1) cannot measure air/fuel ratio in the exhaust gas normally, a gap occurs to the actual air/fuel ratio. As a result, the gap causes a deviation in target air/fuel ratio control (after TWC) which is determined by the secondary HO2S (sensor 2). If the deviation exceeds a limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Depending on the driving conditions

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED] | 530 rpm | 4, 000 rpm

Intake air amount | 9.0 g/second (0.32 oz/second) | -

Fuel feedback | Closed loop

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- Short term fuel trim is lower than -0.03* 1 (-0.0537)* 2.

- Long term fuel trim is lower than 0.001.

*1: Except L15BA KL models

*2: L15BA KL models

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) malfunction/slow response

- A/F sensor (sensor 1) circuit range/performance

- Fuel system too lean

- Fuel system too rich

- Secondary HO2S (sensor 2) circuit signal stuck lean

- Secondary HO2S (sensor 2) circuit open

- Secondary HO2S (sensor 2) slow response

- Misfire

- Air/fuel ratio variation between cylinders

- Exhaust system failure (exhaust gas leak)

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 62 seconds* 3 (67 seconds)* 2 (69 seconds)* 4.

*3: CVT except L15BA KL models

*4: M/T

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Sources Used

- `pages\6739.html`
- `pages\6740.html`
- `pages\6741.html`
- `pages\6742.html`
- `pages\6743.html`
- `pages\6744.html`
- `pages\6745.html`
- `pages\6746.html`
- `pages\6747.html`
- `pages\6748.html`
- `pages\6749.html`
- `pages\6750.html`
- `pages\6751.html`
- `pages\6752.html`
- `pages\6753.html`
- `pages\6754.html`
- `pages\6755.html`
- `pages\6756.html`
- `pages\6757.html`
- `pages\6758.html`
- `pages\6759.html`
- `pages\6760.html`
- `pages\6761.html`
- `pages\6762.html`
- `pages\6763.html`
- `pages\6764.html`
- `pages\6765.html`
- `pages\6766.html`
- `pages\6767.html`
- `pages\6768.html`
- `pages\6769.html`
- `pages\6770.html`
- `pages\6771.html`
- `pages\6772.html`
- `pages\6773.html`
- `pages\6774.html`
- `pages\6775.html`
- `pages\6776.html`
- `pages\6777.html`
- `pages\6778.html`
- `pages\6779.html`
- `pages\6780.html`
- `pages\6781.html`
- `pages\6782.html`
- `pages\6783.html`
- `pages\6784.html`
- `pages\6785.html`
- `pages\6786.html`
- `pages\6787.html`
- `pages\6788.html`
- `pages\6789.html`
- `pages\6790.html`
- `pages\6791.html`
- `pages\6792.html`
- `pages\6793.html`
- `pages\6794.html`
- `pages\6795.html`
- `pages\6796.html`
- `pages\6797.html`
- `pages\6798.html`
- `pages\6799.html`
- `pages\6800.html`
- `pages\6801.html`
- `pages\6802.html`
- `pages\6803.html`
- `pages\6804.html`
- `pages\6805.html`
- `pages\6806.html`
- `pages\6807.html`
- `pages\6808.html`
- `pages\6809.html`
- `pages\6810.html`
- `pages\6811.html`
- `pages\6812.html`
- `pages\6813.html`
- `pages\6814.html`
- `pages\6815.html`
- `pages\6816.html`
- `pages\6817.html`
- `pages\6818.html`
- `pages\6819.html`
- `pages\6820.html`
- `pages\6821.html`
- `pages\6822.html`
- `pages\6823.html`
- `pages\6824.html`
- `pages\6825.html`
- `pages\6826.html`
- `pages\6827.html`
- `pages\6828.html`
- `pages\6829.html`
- `pages\6830.html`
- `pages\6831.html`
- `pages\6832.html`
- `pages\6833.html`
- `pages\6834.html`
- `pages\6835.html`
- `pages\6836.html`
- `pages\6837.html`
- `pages\6838.html`
- `pages\6839.html`
- `pages\6840.html`
- `pages\6841.html`
- `pages\6842.html`
- `pages\6843.html`
- `pages\6844.html`
- `pages\6845.html`
- `pages\6846.html`
- `pages\6847.html`
- `pages\6848.html`
- `pages\6849.html`
- `pages\6850.html`
- `pages\6851.html`
- `pages\6852.html`
- `pages\6853.html`
- `pages\6854.html`
- `pages\6855.html`
- `pages\6856.html`
- `pages\6857.html`
- `pages\6858.html`
- `pages\6859.html`
- `pages\6860.html`
- `pages\6861.html`
- `pages\6862.html`
- `pages\6863.html`
- `pages\6864.html`
- `pages\6865.html`
- `pages\6866.html`
- `pages\6867.html`
- `pages\6868.html`
- `pages\6869.html`
- `pages\6870.html`
- `pages\6871.html`
- `pages\6872.html`
- `pages\6873.html`
- `pages\6874.html`
- `pages\6875.html`
- `pages\6876.html`
- `pages\6877.html`
- `pages\6878.html`
- `pages\6879.html`
- `pages\6880.html`
- `pages\6881.html`
- `pages\6882.html`
- `pages\6883.html`
- `pages\6884.html`
- `pages\6885.html`
- `pages\6886.html`
- `pages\6887.html`
- `pages\6888.html`
- `pages\6889.html`
- `pages\6890.html`
- `pages\6891.html`
- `pages\6892.html`
- `pages\6893.html`
- `pages\6894.html`
- `pages\6895.html`
- `pages\6896.html`
- `pages\6897.html`
- `pages\6898.html`
- `pages\6899.html`
- `pages\6900.html`
- `pages\6901.html`
- `pages\6902.html`
- `pages\6903.html`
- `pages\6904.html`
- `pages\6905.html`
- `pages\6906.html`
- `pages\6907.html`
- `pages\6908.html`
- `pages\6909.html`
- `pages\6910.html`
- `pages\6911.html`
- `pages\6912.html`
- `pages\6913.html`
- `pages\6914.html`
- `pages\6915.html`
- `pages\6916.html`
- `pages\6917.html`
- `pages\6918.html`
- `pages\6919.html`
- `pages\6920.html`
- `pages\6921.html`
- `pages\6922.html`
- `pages\6923.html`
- `pages\6924.html`
- `pages\6925.html`
- `pages\6926.html`
- `pages\6927.html`
- `pages\6928.html`
- `pages\6929.html`
- `pages\6930.html`
- `pages\6931.html`
- `pages\6932.html`
- `pages\6933.html`
- `pages\6934.html`
- `pages\6935.html`
- `pages\6936.html`
- `pages\6937.html`
- `pages\6938.html`
- `pages\6939.html`
- `pages\6940.html`
- `pages\6941.html`
- `pages\6942.html`
- `pages\6943.html`
- `pages\6944.html`
- `pages\6945.html`
- `pages\6946.html`
- `pages\6947.html`
- `pages\6948.html`
- `pages\6949.html`
- `pages\6950.html`
- `pages\6951.html`
- `pages\6952.html`
- `pages\6953.html`
- `pages\6954.html`
- `pages\6955.html`
- `pages\6956.html`
- `pages\6957.html`
- `pages\6958.html`
- `pages\6959.html`
- `pages\6960.html`
- `pages\6961.html`
- `pages\6962.html`
- `pages\6963.html`
- `pages\6964.html`
- `pages\6965.html`
- `pages\6966.html`
- `pages\6967.html`
- `pages\6968.html`
- `pages\6969.html`
- `pages\6970.html`
- `pages\6971.html`
- `pages\6972.html`
- `pages\6973.html`
- `pages\6974.html`
- `pages\6975.html`
- `pages\6976.html`
- `pages\6977.html`
- `pages\6978.html`
- `pages\6979.html`
- `pages\6980.html`
- `pages\6981.html`
- `pages\6982.html`
- `pages\6983.html`
- `pages\6984.html`
- `pages\6985.html`
- `pages\6986.html`
