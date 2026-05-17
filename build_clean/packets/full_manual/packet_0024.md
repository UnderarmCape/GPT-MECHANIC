# Deep Research Manual Packet 0024

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0024
- Chunk count: 262
- Chunk range: 5854-6115
- Source count: 252
- Target maximum characters: 750000

## Manual Chunks

## Chunk 5854: DTC P2096 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2096 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6987.html`
- Chunk ID: `chunk_230377f64852`
- Images: `images\GHH403411.jpeg`
- Duplicate sources: `pages\8574.html`, `pages\22750.html`, `pages\21163.html`

### Full Text

````text
# DTC P2096 (Si) (2017 2018 2019 2020 2021)

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

Engine speed [ENGINE SPEED] | 620 rpm | 4, 000 rpm

Intake air amount | 8.0 g/second (0.29 oz/second) | -

Fuel feedback | Closed loop

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- Short term fuel trim is lower than -0.03.

- Long term fuel trim is lower than 0.001.

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

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 69 seconds.

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

## Chunk 5855: DTC P2097 (K20C1) (2017 2018 2019)

- Title: DTC P2097 (K20C1) (2017 2018 2019)
- Source path: `pages\6988.html`
- Chunk ID: `chunk_3e5de7171340`
- Images: `images\GHH403412.jpeg`
- Duplicate sources: `pages\8575.html`, `pages\22751.html`, `pages\21164.html`

### Full Text

````text
# DTC P2097 (K20C1) (2017 2018 2019)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

Evaporative emission (EVAP) system monitor is not active

**: For at least 100 g (3.53 oz) of integrated amount of exhaust gas mass flow

***: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Lambda offset is less than -0.045 but greater than 0.1 and lambda offset change in non-fault direction for confirmation of fuel trim fault is less than 0.01.

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

## Chunk 5856: DTC P2097 (K20C1) (2019 2020 2021)

- Title: DTC P2097 (K20C1) (2019 2020 2021)
- Source path: `pages\6989.html`
- Chunk ID: `chunk_80b743cc7aed`
- Images: `images\GHH403413.jpeg`
- Duplicate sources: `pages\8576.html`, `pages\22752.html`, `pages\21165.html`

### Full Text

````text
# DTC P2097 (K20C1) (2019 2020 2021)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

*: For at least 300 g (10.59 oz) of integrated amount of exhaust mass flow

[ ]: HDS Parameter

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

Lambda offset is less than -0.05 but -0.1 or more and lambda offset change in non-fault direction for confirmation of fuel trim fault is less than 0.01.

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

## Chunk 5857: DTC P2097 (K20C2, USA/Canada models)

- Title: DTC P2097 (K20C2, USA/Canada models)
- Source path: `pages\6990.html`
- Chunk ID: `chunk_56dec697e9cc`
- Images: `images\GHH403414.jpeg`
- Duplicate sources: `pages\8577.html`, `pages\22753.html`, `pages\21166.html`

### Full Text

````text
# DTC P2097 (K20C2, USA/Canada models)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

- Short term fuel trim is higher than -0.014* 3 (-0.016)* 4.

- Long term fuel trim is higher than 0.04* 3 (0.043)* 4.

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

## Chunk 5858: DTC P2097 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P2097 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6991.html`
- Chunk ID: `chunk_8e4a32a040ce`
- Images: `images\GHH403415.jpeg`
- Duplicate sources: `pages\8578.html`, `pages\22754.html`, `pages\21167.html`

### Full Text

````text
# DTC P2097 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

- Short term fuel trim is higher than -0.014.

- Long term fuel trim is higher than 0.043.

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

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 62 seconds* 3 (67 seconds)* 4 (69 seconds)* 5.

*3: CVT except L15BA KL models

*4: L15BA KL models

*5: M/T

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5859: DTC P2097 (L15B7/L15BA) (2016 2017 2018 2019)

- Title: DTC P2097 (L15B7/L15BA) (2016 2017 2018 2019)
- Source path: `pages\6992.html`
- Chunk ID: `chunk_2e56cb8055e1`
- Images: `images\GHH403416.jpeg`
- Duplicate sources: `pages\8579.html`, `pages\22755.html`, `pages\21168.html`

### Full Text

````text
# DTC P2097 (L15B7/L15BA) (2016 2017 2018 2019)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

- Short term fuel trim is higher than -0.014.

- Long term fuel trim is higher than 0.043.

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

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 62 seconds* 1, * 3 (67 seconds)* 4 (69 seconds)* 2.

*1: CVT

*2: M/T

*3: Except L15BA KL models

*4: L15BA KL models

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

## Chunk 5860: DTC P2097 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2097 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6993.html`
- Chunk ID: `chunk_c0ee626f0322`
- Images: `images\GHH403417.jpeg`
- Duplicate sources: `pages\8580.html`, `pages\22756.html`, `pages\21169.html`

### Full Text

````text
# DTC P2097 (Si) (2017 2018 2019 2020 2021)

DTC P2097: Post Catalyst Fuel Trim System Too Rich

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

Engine speed [ENGINE SPEED] | 620 rpm | 4, 000 rpm

Intake air amount | 8.0 g/second (0.29 oz/second) | -

Fuel feedback | Closed loop

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met:

- Short term fuel trim is higher than -0.014.

- Long term fuel trim is higher than 0.043.

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

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) and engine speed [ENGINE SPEED] 4, 000 rpm or less for at least 69 seconds.

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

## Chunk 5861: DTC P2101 (K20C1) (2017 2018 2019)

- Title: DTC P2101 (K20C1) (2017 2018 2019)
- Source path: `pages\6994.html`
- Chunk ID: `chunk_fae22c0bf58f`
- Images: `images\GHH403418.jpeg`, `images\GHH403419.jpeg`
- Duplicate sources: `pages\8581.html`, `pages\22757.html`, `pages\21170.html`

### Full Text

````text
# DTC P2101 (K20C1) (2017 2018 2019)

DTC P2101: Electronic Throttle Control System (ETCS) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator for rationality malfunctions. In order to provide rationality check of control deviation and control duty cycle range check, the actual actuator position is continuously monitored against commanded value and the control duty cycle is continuously monitored against minimum and maximum rationality thresholds. If the checked values are abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.6 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

Either of these conditions occurs:

- Rationality check of control deviation The absolute difference of actuator actual position and its commanded value is greater than 5 - 7 %* for at least 0.5 second. *: Depends on rate of the commanded position

The absolute difference of actuator actual position and its commanded value is greater than 5 - 7 %* for at least 0.5 second.

*: Depends on rate of the commanded position

- Control duty cycle range check The control duty cycle is less than 72 - 100 %** than for at least 0.6 second. **: Depends on 12 volt battery voltage

The control duty cycle is less than 72 - 100 %** than for at least 0.6 second.

**: Depends on 12 volt battery voltage

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5862: DTC P2101 (K20C1) (2019)

- Title: DTC P2101 (K20C1) (2019)
- Source path: `pages\6995.html`
- Chunk ID: `chunk_0237721d79ae`
- Images: `images\GHH403420.jpeg`, `images\GHH403421.jpeg`
- Duplicate sources: `pages\8582.html`, `pages\22758.html`, `pages\21171.html`

### Full Text

````text
# DTC P2101 (K20C1) (2019)

DTC P2101: Electronic Throttle Control System (ETCS) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator for rationality malfunctions. In order to provide rationality check of control deviation and control duty cycle range check, the actual actuator position is continuously monitored against commanded value and the control duty cycle is continuously monitored against minimum and maximum rationality thresholds. If the checked values are abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more*, 0.6001 second or more**

DTC Type | One drive cycle, MIL on

*: Rationality check of control deviation

**: Control duty cycle range check

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

State of the engine | Running

Other | Throttle actuator power stage on

[ ]: HDS Parameter

Malfunction Threshold

Either of these conditions occurs:

- Rationality check of control deviation The absolute difference of actuator actual position and its commanded value is greater than 5.01562 %.

The absolute difference of actuator actual position and its commanded value is greater than 5.01562 %.

- Control duty cycle range check The control duty cycle is greater than 80 - 95 %***. ***: Depends on 12 volt battery voltage

The control duty cycle is greater than 80 - 95 %***.

***: Depends on 12 volt battery voltage

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5863: DTC P2101 (K20C1) (2020 2021)

- Title: DTC P2101 (K20C1) (2020 2021)
- Source path: `pages\6996.html`
- Chunk ID: `chunk_627e572e99a7`
- Images: `images\GHH403422.jpeg`, `images\GHH403423.jpeg`
- Duplicate sources: `pages\8583.html`, `pages\22759.html`, `pages\21172.html`

### Full Text

````text
# DTC P2101 (K20C1) (2020 2021)

DTC P2101: Electronic Throttle Control System (ETCS) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator for rationality malfunctions. In order to provide rationality check of control deviation and control duty cycle range check, the actual actuator position is continuously monitored against commanded value. If the checked values are abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The throttle position is in a certain range for at least 0.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5864: DTC P2101 (K20C2)

- Title: DTC P2101 (K20C2)
- Source path: `pages\6997.html`
- Chunk ID: `chunk_f5b63a54d103`
- Images: `images\GHH403424.jpeg`
- Duplicate sources: `pages\8584.html`, `pages\22760.html`, `pages\21173.html`

### Full Text

````text
# DTC P2101 (K20C2)

DTC P2101: Electronic Throttle Control System (ETCS) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). The PCM compares the throttle valve target opening angle and the actual throttle valve opening angle from TP sensor A, and when the difference exceeds the specification, the PCM detects the malfunction of the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 250 milliseconds or more*, 500 milliseconds or more**

DTC Type | One drive cycle, MIL on

*: Throttle valve closed direction

**: Throttle valve open direction

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

One of the conditions in this table is met for at least 250 milliseconds* (500 milliseconds**).

Throttle valve target position | Difference between throttle valve target position and actual throttle valve position

2 deg. | 4 deg. or more

6 deg. | 5.4 deg. or more

10 deg. | 5.7 deg. or more

15 deg. | 6 deg. or more

90 deg. | 6 deg. or more

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- Throttle body internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5865: DTC P2101 (L15B7/L15BA)

- Title: DTC P2101 (L15B7/L15BA)
- Source path: `pages\6998.html`
- Chunk ID: `chunk_74307d9d672c`
- Images: `images\GHH403425.jpeg`
- Duplicate sources: `pages\8585.html`, `pages\22761.html`, `pages\21174.html`

### Full Text

````text
# DTC P2101 (L15B7/L15BA)

DTC P2101: Electronic Throttle Control System (ETCS) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). The PCM compares the throttle valve target opening angle and the actual throttle valve opening angle from TP sensor A, and when the difference exceeds the specification, the PCM detects the malfunction of the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 250 milliseconds or more*, 500 milliseconds or more**

DTC Type | One drive cycle, MIL on

*: Throttle valve closed direction

**: Throttle valve open direction

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

One of the conditions in this table is met for at least 250 milliseconds* (500 milliseconds**).

Throttle valve target position | Difference between throttle valve target position and actual throttle valve position

2 deg. | 4 deg. or more

6 deg. | 5.4 deg. or more

10 deg. | 5.7 deg. or more

15 deg. | 6 deg. or more

90 deg. | 6 deg. or more

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- Throttle body internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5866: DTC P2108 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2108 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\6999.html`
- Chunk ID: `chunk_38d1532c4e52`
- Images: none
- Duplicate sources: `pages\8586.html`, `pages\22762.html`, `pages\21175.html`

### Full Text

````text
# DTC P2108 (K20C2) (2018 2019 2020 2021)

DTC P2108: Throttle Actuator Control Module Performance

General Description

This fault code is a general (specified by SAE) DTC that is stored at the time the following DTC codes (P1658, P1659) are detected.

Monitor Execution, Sequence, Duration, DTC Type

Refer to the specific DTC information. (P1658, P1659)

Enable Conditions

Refer to the specific DTC information. (P1658, P1659)

Malfunction Threshold

P1658 and/or P1659 is stored.

Possible Cause

Refer to the specific DTC information. (P1658, P1659)

Diagnosis Details

Conditions for setting the DTC

The DTC is stored at the same time when DTC P1658 or P1659 is stored. Refer to the specific DTC information.

Conditions for clearing the DTC

The DTC is cleared at the same time when DTC P1658 and P1659 are cleared. Refer to the specific DTC information.
````

## Chunk 5867: DTC P2108 (L15B7/L15BA/L15BY) (2017 2018 2019 2020 2021)

- Title: DTC P2108 (L15B7/L15BA/L15BY) (2017 2018 2019 2020 2021)
- Source path: `pages\7000.html`
- Chunk ID: `chunk_79a3cb692ac4`
- Images: none
- Duplicate sources: `pages\8587.html`, `pages\22763.html`, `pages\21176.html`

### Full Text

````text
# DTC P2108 (L15B7/L15BA/L15BY) (2017 2018 2019 2020 2021)

DTC P2108: Throttle Actuator Control Module Performance

General Description

This fault code is a general (specified by SAE) DTC that is stored at the time the following DTC codes (P1658, P1659) are detected.

Monitor Execution, Sequence, Duration, DTC Type, OBD Status

Refer to the specific DTC information. (P1658, P1659)

Enable Conditions

Refer to the specific DTC information. (P1658, P1659)

Malfunction Threshold

P1658 and/or P1659 is stored.

Possible Cause

Refer to the specific DTC information. (P1658, P1659)

Diagnosis Details

Conditions for setting the DTC

The DTC is stored at the same time when DTC P1658 or P1659 is stored. Refer to the specific DTC information.

Conditions for clearing the DTC

The DTC is cleared at the same time when DTC P1658 and P1659 are cleared. Refer to the specific DTC information.
````

## Chunk 5868: DTC P2118 (K20C1) (2017 2018 2019)

- Title: DTC P2118 (K20C1) (2017 2018 2019)
- Source path: `pages\7001.html`
- Chunk ID: `chunk_c16af6cd324a`
- Images: `images\GHH403426.jpeg`
- Duplicate sources: `pages\8588.html`, `pages\22764.html`, `pages\21177.html`

### Full Text

````text
# DTC P2118 (K20C1) (2017 2018 2019)

DTC P2118: Throttle Actuator Current Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control circuit for electrical malfunctions. The throttle actuator control circuit checks will detect short circuit to ground, short circuit to power, open circuit, and overtemperature failures. If a short or an open in throttle actuator control circuit are detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Throttle actuator circuit open

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

Vehicle | ON mode

Other | Throttle actuator commanded OFF

Throttle actuator circuit short or overtemperature

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

Vehicle | ON mode

Other | Throttle actuator commanded ON

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects short to ground, short to power, open, or overtemperature in throttle actuator control circuit for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High ambient temperature

- Throttle actuator MTR1 line short to ground

- Throttle actuator MTR2 line short to ground

- Throttle actuator MTR1 line short to throttle actuator MTR2 line

- Throttle body failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5869: DTC P2118 (K20C1) (2019)

- Title: DTC P2118 (K20C1) (2019)
- Source path: `pages\7002.html`
- Chunk ID: `chunk_a1d7a3b9b7fc`
- Images: `images\GHH403427.jpeg`
- Duplicate sources: `pages\8589.html`, `pages\22765.html`, `pages\21178.html`

### Full Text

````text
# DTC P2118 (K20C1) (2019)

DTC P2118: Throttle Actuator Current Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control circuit for electrical malfunctions. The throttle actuator control circuit checks will detect short circuit to ground, short circuit to power, open circuit, and over temperature failures. If the throttle actuator control circuit is in a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Throttle actuator circuit open

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

Vehicle | ON mode

Other | Throttle actuator power stage off

Throttle actuator circuit short or overtemperature

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | -

Vehicle | ON mode

Other | Throttle actuator power stage on

[ ]: HDS Parameter

Malfunction Threshold

- Throttle actuator circuit open Low side output voltage is 1.76 V or more and high side output voltage is 1.76 V or less.

Low side output voltage is 1.76 V or more and high side output voltage is 1.76 V or less.

- Throttle actuator driver over temperature Throttle actuator driver temperature is more than 175 deg.C (347 deg.F).

Throttle actuator driver temperature is more than 175 deg.C (347 deg.F).

- Throttle actuator circuit short The current of any H-bridge for the throttle actuator in the PCM is 11.5 A or more.

The current of any H-bridge for the throttle actuator in the PCM is 11.5 A or more.

Malfunction Threshold

The PCM detects short to ground, short to power, open, or overtemperature in throttle actuator control circuit for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High ambient temperature

- Throttle actuator MTR1 line short to ground

- Throttle actuator MTR2 line short to ground

- Throttle actuator MTR1 line short to throttle actuator MTR2 line

- Throttle body failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5870: DTC P2118 (K20C1) (2020 2021)

- Title: DTC P2118 (K20C1) (2020 2021)
- Source path: `pages\7003.html`
- Chunk ID: `chunk_6567cb40e2fd`
- Images: `images\GHH403428.jpeg`
- Duplicate sources: `pages\8590.html`, `pages\22766.html`, `pages\21179.html`

### Full Text

````text
# DTC P2118 (K20C1) (2020 2021)

DTC P2118: Throttle Actuator Current Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control circuit for electrical malfunctions. The throttle actuator control circuit checks will detect short circuit to ground, short circuit to power, open circuit, and over temperature failures. If the throttle actuator control circuit is in a specified condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Throttle actuator circuit open

Condition

State of the engine | Running

Other | Throttle actuator power stage off

Throttle actuator circuit short, Throttle actuator over temperature

Condition

State of the engine | Running

Malfunction Threshold

- Throttle actuator circuit open Low side output voltage is 2.24 V or more and high side output voltage is 1.76 V or less.

Low side output voltage is 2.24 V or more and high side output voltage is 1.76 V or less.

- Throttle actuator driver over temperature Throttle actuator driver temperature is more than 347 deg.F (175 deg.C).

Throttle actuator driver temperature is more than 347 deg.F (175 deg.C).

- Throttle actuator circuit short The current of any H-bridge for the throttle actuator in the PCM is 11.5 A or more.

The current of any H-bridge for the throttle actuator in the PCM is 11.5 A or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High ambient temperature

- Throttle actuator MTR1 line short to ground

- Throttle actuator MTR2 line short to ground

- Throttle actuator MTR1 line short to throttle actuator MTR2 line

- Throttle body failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5871: DTC P2118 (K20C2)

- Title: DTC P2118 (K20C2)
- Source path: `pages\7004.html`
- Chunk ID: `chunk_4f7ef659a293`
- Images: `images\GHH403429.jpeg`
- Duplicate sources: `pages\8591.html`, `pages\22767.html`, `pages\21180.html`

### Full Text

````text
# DTC P2118 (K20C2)

DTC P2118: Throttle Actuator Current Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). When the output current to the throttle actuator exceeds the specification for a set time, the PCM detects a malfunction of the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The current flow to the throttle actuator is 9 A or more for at least 200 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line short

- Throttle actuator MTR2 line short

- Throttle actuator MTR1 line short to throttle actuator MTR2 line

- Throttle body internal failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the ON mode.

- Slowly press the accelerator pedal to the floor.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5872: DTC P2118 (L15B7)

- Title: DTC P2118 (L15B7)
- Source path: `pages\7005.html`
- Chunk ID: `chunk_3ffbbc15c543`
- Images: `images\GHH403430.jpeg`
- Duplicate sources: `pages\8592.html`, `pages\22768.html`, `pages\21181.html`

### Full Text

````text
# DTC P2118 (L15B7)

DTC P2118: Throttle Actuator Current Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). When the output current to the throttle valve actuator exceeds the specification for a set time, the PCM detects a malfunction of the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The current flow to the throttle actuator is 9 A or more for at least 200 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line short

- Throttle actuator MTR2 line short

- Throttle actuator MTR1 line short to throttle actuator MTR2 line

- Throttle body internal failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the ON mode.

- Slowly press the accelerator pedal to the floor.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5873: DTC P2119 (K20C1) (2017 2018 2019)

- Title: DTC P2119 (K20C1) (2017 2018 2019)
- Source path: `pages\7006.html`
- Chunk ID: `chunk_890736117971`
- Images: `images\GHH403431.jpeg`
- Duplicate sources: `pages\8593.html`, `pages\22769.html`, `pages\21182.html`

### Full Text

````text
# DTC P2119 (K20C1) (2017 2018 2019)

DTC P2119: Throttle Actuator Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control for range/performance malfunctions. The limp home position of the valve is learned when the current reported by the throttle actuator driver IC is 0. If the limp home position of the throttle valve exceeds a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

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

Any of the conditions occur:

- The difference between throttle position (TP) sensor A voltage at limp air position and TP sensor A voltage at lower mechanical stop is less than 0.08423 V or greater than 0.51392 V for at least 0.5 second.

- The difference between throttle position (TP) sensor B voltage at lower mechanical stop and TP sensor B voltage at limp air position is less than 0.08423 V or greater than 0.51392 V for at least 0.5 second.

- The actual position is less than the default position for 2.9922 % or more for at least 0.26 second.

- The actual position is less than 2.6326 % for at least 0.26 second.

- The actual position is greater than the default position for 2.9922 % or more for at least 0.26 second.

- The actual position is greater than 16.06271 % for at least 0.26 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle body failure

- PCM internal circuit failure

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

## Chunk 5874: DTC P2119 (K20C1) (2019)

- Title: DTC P2119 (K20C1) (2019)
- Source path: `pages\7007.html`
- Chunk ID: `chunk_828057be7398`
- Images: `images\GHH403432.jpeg`
- Duplicate sources: `pages\8594.html`, `pages\22770.html`, `pages\21183.html`

### Full Text

````text
# DTC P2119 (K20C1) (2019)

DTC P2119: Throttle Actuator Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control for range/performance malfunctions. The limp home position of the valve is learned when the current reported by the throttle actuator driver IC is 0. If the limp home position of the throttle valve exceeds a specified range, the PCM detects a malfunction and stores a DTC.

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

Any of the conditions occur:

- The difference between throttle position (TP) sensor A voltage at limp air position and TP sensor A voltage at lower mechanical stop is less than 0.09 V or greater than 0.51 V.

- The difference between throttle position (TP) sensor B voltage at lower mechanical stop and TP sensor B voltage at limp air position is less than 0.09 V or greater than 0.51 V.

- First learning performed The throttle valve position is more than 2.99 % or -0.49 % or less.

The throttle valve position is more than 2.99 % or -0.49 % or less.

- First learning not performed The throttle valve position is more than 15.9375 % or 2.5 % or less.

The throttle valve position is more than 15.9375 % or 2.5 % or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle body failure

- PCM internal circuit failure

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

## Chunk 5875: DTC P2119 (K20C1) (2020 2021)

- Title: DTC P2119 (K20C1) (2020 2021)
- Source path: `pages\7008.html`
- Chunk ID: `chunk_260ecac1e5e5`
- Images: `images\GHH403433.jpeg`
- Duplicate sources: `pages\8595.html`, `pages\22771.html`, `pages\21184.html`

### Full Text

````text
# DTC P2119 (K20C1) (2020 2021)

DTC P2119: Throttle Actuator Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle actuator control for range/performance malfunctions. The limp home position of the valve is learned when the current reported by the throttle actuator driver IC is 0. If the limp home position of the throttle valve exceeds a specified range, the PCM detects a malfunction and stores a DTC.

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

Any of the conditions occur:

- The difference between throttle position (TP) sensor A voltage at limp air position and TP sensor A voltage at lower mechanical stop is less than 0.09 V or greater than 0.51 V.

- The difference between throttle position (TP) sensor B voltage at lower mechanical stop and TP sensor B voltage at limp air position is less than 0.09 V or greater than 0.51 V.

- First learning performed The throttle valve position is more than 18.9275 % or -0.49 % or less.

The throttle valve position is more than 18.9275 % or -0.49 % or less.

- First learning not performed The throttle valve position is more than 15.9375 % or 2.5 % or less.

The throttle valve position is more than 15.9375 % or 2.5 % or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle body failure

- PCM internal circuit failure

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

## Chunk 5876: DTC P2119 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2119 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\7009.html`
- Chunk ID: `chunk_a46f9421ca80`
- Images: none
- Duplicate sources: `pages\8596.html`, `pages\22772.html`, `pages\21185.html`

### Full Text

````text
# DTC P2119 (K20C2) (2018 2019 2020 2021)

DTC P2119: Throttle Actuator Control Throttle Body Range/Performance

General Description

This fault code is a general (specified by SAE) DTC that is stored at the time the following DTC codes (P1683, P1684) are detected.

Monitor Execution, Sequence, Duration, DTC Type

Refer to the specific DTC information. (P1683, P1684)

Enable Conditions

Refer to the specific DTC information. (P1683, P1684)

Malfunction Threshold

P1683 and/or P1684 is stored.

Possible Cause

Refer to the specific DTC information. (P1683, P1684)

Diagnosis Details

Conditions for setting the DTC

The DTC is stored at the same time when DTC P1683 or P1684 is stored. Refer to the specific DTC information.

Conditions for clearing the DTC

The DTC is cleared at the same time when DTC P1683 and P1684 are cleared. Refer to the specific DTC information.
````

## Chunk 5877: DTC P2119 (L15BA) (2017 2018 2019 2020 2021)

- Title: DTC P2119 (L15BA) (2017 2018 2019 2020 2021)
- Source path: `pages\7010.html`
- Chunk ID: `chunk_8f612bd86d9b`
- Images: none
- Duplicate sources: `pages\8597.html`, `pages\22773.html`, `pages\21186.html`

### Full Text

````text
# DTC P2119 (L15BA) (2017 2018 2019 2020 2021)

DTC P2119: Throttle Actuator Control Throttle Body Range/Performance

General Description

This fault code is a general (specified by SAE) DTC that is stored at the time the following DTC codes (P1683, P1684) are detected.

Monitor Execution, Sequence, Duration, DTC Type, OBD Status

Refer to the specific DTC information. (P1683, P1684)

Enable Conditions

Refer to the specific DTC information. (P1683, P1684)

Malfunction Threshold

P1683 and/or P1684 is stored.

Possible Cause

Refer to the specific DTC information. (P1683, P1684)

Diagnosis Details

Conditions for setting the DTC

The DTC is stored at the same time when DTC P1683 or P1684 is stored. Refer to the specific DTC information.

Conditions for clearing the DTC

The DTC is cleared at the same time when DTC P1683 and P1684 are cleared. Refer to the specific DTC information.
````

## Chunk 5878: DTC P2121 (K20C1) (2017 2018 2019)

- Title: DTC P2121 (K20C1) (2017 2018 2019)
- Source path: `pages\7011.html`
- Chunk ID: `chunk_bdd8f5b1e2f8`
- Images: `images\GHH403434.jpeg`, `images\GHH403435.jpeg`
- Duplicate sources: `pages\8598.html`, `pages\22774.html`, `pages\21187.html`

### Full Text

````text
# DTC P2121 (K20C1) (2017 2018 2019)

DTC P2121: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the physical range check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor A output voltage [APP Sensor A] is 0.45 V or less for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5879: DTC P2121 (K20C1) (2019 2020 2021)

- Title: DTC P2121 (K20C1) (2019 2020 2021)
- Source path: `pages\7012.html`
- Chunk ID: `chunk_e97f47d1f466`
- Images: `images\GHH403436.jpeg`, `images\GHH403437.jpeg`
- Duplicate sources: `pages\8599.html`, `pages\22775.html`, `pages\21188.html`

### Full Text

````text
# DTC P2121 (K20C1) (2019 2020 2021)

DTC P2121: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the physical range check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor A output voltage [APP Sensor A] is 0.45 V or less for at least 0.2 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5880: DTC P2121 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2121 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\7013.html`
- Chunk ID: `chunk_ec748a8d746b`
- Images: `images\GHH403438.jpeg`
- Duplicate sources: `pages\8600.html`, `pages\22776.html`, `pages\21189.html`

### Full Text

````text
# DTC P2121 (K20C2) (2018 2019 2020 2021)

DTC P2121: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor A is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor A output voltage [APP SENSOR A] is 0.69 V or less, or 4.99 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5881: DTC P2121 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P2121 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\7014.html`
- Chunk ID: `chunk_44ebbbdc34dc`
- Images: `images\GHH403439.jpeg`
- Duplicate sources: `pages\8601.html`, `pages\22777.html`, `pages\21190.html`

### Full Text

````text
# DTC P2121 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P2121: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor A is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor A output voltage [APP SENSOR A] is 0.69 V or less, or 4.99 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5882: DTC P2121 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2121 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7015.html`
- Chunk ID: `chunk_81a2f2194b54`
- Images: `images\GHH403440.jpeg`
- Duplicate sources: `pages\8602.html`, `pages\22778.html`, `pages\21191.html`

### Full Text

````text
# DTC P2121 (Si) (2017 2018 2019 2020 2021)

DTC P2121: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor A is a specified range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor A output voltage [APP SENSOR A] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5883: DTC P2122, P2123 (K20C1) (2017 2018 2019)

- Title: DTC P2122, P2123 (K20C1) (2017 2018 2019)
- Source path: `pages\7016.html`
- Chunk ID: `chunk_f2c5f3acb3d6`
- Images: `images\GHH403441.jpeg`, `images\GHH403442.jpeg`
- Duplicate sources: `pages\8603.html`, `pages\22779.html`, `pages\21192.html`

### Full Text

````text
# DTC P2122, P2123 (K20C1) (2017 2018 2019)

DTC P2122: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit Low Voltage

DTC P2123: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the circuit continuity check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 millisecond or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2122

The APP sensor A output voltage [APP Sensor A] is 0.4 V or less for at least 0.2 millisecond.

DTC: P2123

The APP sensor A output voltage [APP Sensor A] is 4.8216 V or more for at least 0.2 millisecond.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2122

- APP sensor A APS1 line short to ground

- APP sensor A APS1 line open

- APP sensor A VCC line open

DTC: P2123

- APP sensor A APS1 line short to power

- APP sensor A SG line open

Common

- APP sensor A failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5884: DTC P2122, P2123 (K20C1) (2019 2020 2021)

- Title: DTC P2122, P2123 (K20C1) (2019 2020 2021)
- Source path: `pages\7017.html`
- Chunk ID: `chunk_d9caab791d19`
- Images: `images\GHH403443.jpeg`, `images\GHH403444.jpeg`
- Duplicate sources: `pages\8604.html`, `pages\22780.html`, `pages\21193.html`

### Full Text

````text
# DTC P2122, P2123 (K20C1) (2019 2020 2021)

DTC P2122: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit Low Voltage

DTC P2123: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the circuit continuity check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2122

The APP sensor A output voltage [APP Sensor A] is 0.4 V or less for at least 0.2 second.

DTC: P2123

The APP sensor A output voltage [APP Sensor A] is 4.822 V or more for at least 0.2 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2122

- APP sensor A APS1 line short to ground

- APP sensor A APS1 line open

- APP sensor A VCC line open

DTC: P2123

- APP sensor A APS1 line short to power

- APP sensor A SG line open

Common

- APP sensor A failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5885: DTC P2122, P2123 (K20C2)

- Title: DTC P2122, P2123 (K20C2)
- Source path: `pages\7018.html`
- Chunk ID: `chunk_651eb2832032`
- Images: `images\GHH403445.jpeg`
- Duplicate sources: `pages\8605.html`, `pages\22781.html`, `pages\21194.html`

### Full Text

````text
# DTC P2122, P2123 (K20C2)

DTC P2122: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit Low Voltage

DTC P2123: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor A is a set value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2122

The APP sensor A output voltage [APP SENSOR A] is 0.2 V or less for at least 200 milliseconds.

DTC: P2123

The APP sensor A output voltage [APP SENSOR A] is 4.9 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2122

- APP sensor A APS1 line open

- APP sensor A APS1 line short to ground

- APP sensor A VCC line open

DTC: P2123

- APP sensor A APS1 line short to power

- APP sensor A SG line open

Common

- APP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5886: DTC P2122, P2123 (L15B7/L15BA/L15BY)

- Title: DTC P2122, P2123 (L15B7/L15BA/L15BY)
- Source path: `pages\7019.html`
- Chunk ID: `chunk_643cb89b04c2`
- Images: `images\GHH403446.jpeg`
- Duplicate sources: `pages\8606.html`, `pages\22782.html`, `pages\21195.html`

### Full Text

````text
# DTC P2122, P2123 (L15B7/L15BA/L15BY)

DTC P2122: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit Low Voltage

DTC P2123: Accelerator Pedal Position (APP) Sensor A (Throttle Position (TP) Sensor D) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor A is a set value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2122

The APP sensor A output voltage [APP SENSOR A] is 0.2 V or less for at least 200 milliseconds.

DTC: P2123

The APP sensor A output voltage [APP SENSOR A] is 4.9 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2122

- APP sensor A APS1 line open

- APP sensor A APS1 line short to ground

- APP sensor A VCC line open

DTC: P2123

- APP sensor A APS1 line short to APP sensor A VCC line

- APP sensor A SG line open

Common

- APP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5887: DTC P2126 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P2126 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\7020.html`
- Chunk ID: `chunk_1c8adbf36709`
- Images: `images\GHH403447.jpeg`, `images\GHH403448.jpeg`
- Duplicate sources: `pages\8607.html`, `pages\22783.html`, `pages\21196.html`

### Full Text

````text
# DTC P2126 (K20C1) (2017 2018 2019 2020 2021)

DTC P2126: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the physical range check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The APP sensor B output voltage [APP Sensor B] is 2.42 V or more for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor B failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5888: DTC P2126 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2126 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\7021.html`
- Chunk ID: `chunk_b4b9b5b0c2f3`
- Images: `images\GHH403449.jpeg`
- Duplicate sources: `pages\8608.html`, `pages\22784.html`, `pages\21197.html`

### Full Text

````text
# DTC P2126 (K20C2) (2018 2019 2020 2021)

DTC P2126: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor B is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor B is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor B output voltage [APP SENSOR B] is 0.19 V or less, or 2.62 V or more for at least 6.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5889: DTC P2126 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P2126 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\7022.html`
- Chunk ID: `chunk_034d678a17a7`
- Images: `images\GHH403450.jpeg`
- Duplicate sources: `pages\8609.html`, `pages\22785.html`, `pages\21198.html`

### Full Text

````text
# DTC P2126 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P2126: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor B is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor B is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor B output voltage [APP SENSOR B] is 0.19 V or less, or 2.62 V or more for at least 6.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5890: DTC P2126 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2126 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7023.html`
- Chunk ID: `chunk_12b654f52a44`
- Images: `images\GHH403451.jpeg`
- Duplicate sources: `pages\8610.html`, `pages\22786.html`, `pages\21199.html`

### Full Text

````text
# DTC P2126 (Si) (2017 2018 2019 2020 2021)

DTC P2126: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor B is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor B is a specified range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The APP sensor B output voltage [APP SENSOR B] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5891: DTC P2127, P2128 (K20C1) (2017 2018 2019)

- Title: DTC P2127, P2128 (K20C1) (2017 2018 2019)
- Source path: `pages\7024.html`
- Chunk ID: `chunk_0e7defc35140`
- Images: `images\GHH403452.jpeg`, `images\GHH403453.jpeg`
- Duplicate sources: `pages\8611.html`, `pages\22787.html`, `pages\21200.html`

### Full Text

````text
# DTC P2127, P2128 (K20C1) (2017 2018 2019)

DTC P2127: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit Low Voltage

DTC P2128: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the circuit continuity check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 millisecond or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2127

The APP sensor B output voltage [APP Sensor B] is 0.2 V or less for at least 0.2 millisecond.

DTC: P2128

The APP sensor B output voltage [APP Sensor B] is 2.4192 V or more for at least 0.2 millisecond.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2127

- APP sensor B APS2 line short to ground

- APP sensor B APS2 line open

- APP sensor B VCC line open

DTC: P2128

- APP sensor B APS2 line short to power

- APP sensor B SG line open

Common

- APP sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5892: DTC P2127, P2128 (K20C1) (2019 2020 2021)

- Title: DTC P2127, P2128 (K20C1) (2019 2020 2021)
- Source path: `pages\7025.html`
- Chunk ID: `chunk_154cb797b344`
- Images: `images\GHH403454.jpeg`, `images\GHH403455.jpeg`
- Duplicate sources: `pages\8612.html`, `pages\22788.html`, `pages\21201.html`

### Full Text

````text
# DTC P2127, P2128 (K20C1) (2019 2020 2021)

DTC P2127: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit Low Voltage

DTC P2128: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the circuit continuity check, the voltage of both APP sensors is compared with an upper and lower thresholds. If the voltage value is not within a specified range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2127

The APP sensor B output voltage [APP Sensor B] is 0.2 V or less for at least 0.2 second.

DTC: P2128

The APP sensor B output voltage [APP Sensor B] is 2.419 V or more for at least 0.2 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2127

- APP sensor B APS2 line short to ground

- APP sensor B APS2 line open

- APP sensor B VCC line open

DTC: P2128

- APP sensor B APS2 line short to power

- APP sensor B SG line open

Common

- APP sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5893: DTC P2127, P2128 (K20C2)

- Title: DTC P2127, P2128 (K20C2)
- Source path: `pages\7026.html`
- Chunk ID: `chunk_903045ee10b5`
- Images: `images\GHH403456.jpeg`
- Duplicate sources: `pages\8613.html`, `pages\22789.html`, `pages\21202.html`

### Full Text

````text
# DTC P2127, P2128 (K20C2)

DTC P2127: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit Low Voltage

DTC P2128: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor B is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor B is a set value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2127

The APP sensor B output voltage [APP SENSOR B] is 0.2 V or less for at least 200 milliseconds.

DTC: P2128

The APP sensor B output voltage [APP SENSOR B] is 4.0 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2127

- APP sensor B APS2 line open

- APP sensor B APS2 line short to ground

- APP sensor B VCC line open

DTC: P2128

- APP sensor B APS2 line short to power

- APP sensor B SG line open

Common

- APP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5894: DTC P2127, P2128 (L15B7/L15BA)

- Title: DTC P2127, P2128 (L15B7/L15BA)
- Source path: `pages\7027.html`
- Chunk ID: `chunk_a7b3d5a7ba1c`
- Images: `images\GHH403457.jpeg`
- Duplicate sources: `pages\8614.html`, `pages\22790.html`, `pages\21203.html`

### Full Text

````text
# DTC P2127, P2128 (L15B7/L15BA)

DTC P2127: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit Low Voltage

DTC P2128: Accelerator Pedal Position (APP) Sensor B (Throttle Position (TP) Sensor E) Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor B is a part of the electronic throttle control system. It is used to convert the position of the accelerator pedal into electrical signals. Based on these signals, the powertrain control module (PCM) controls the throttle actuator so that the throttle position agrees with the accelerator pedal position. If the signal voltage from APP sensor B is a set value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2127

The APP sensor B output voltage [APP SENSOR B] is 0.2 V or less for at least 200 milliseconds.

DTC: P2128

The APP sensor B output voltage [APP SENSOR B] is 4.0 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2127

- APP sensor B APS2 line open

- APP sensor B APS2 line short to ground

- APP sensor B VCC line open

DTC: P2128

- APP sensor B APS2 line short to APP sensor B VCC line

- APP sensor B SG line open

Common

- APP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5895: DTC P2135 (K20C1) (2017 2018 2019)

- Title: DTC P2135 (K20C1) (2017 2018 2019)
- Source path: `pages\7028.html`
- Chunk ID: `chunk_fdc649b2e0bd`
- Images: `images\GHH403458.jpeg`, `images\GHH403459.jpeg`
- Duplicate sources: `pages\8615.html`, `pages\22791.html`, `pages\21204.html`

### Full Text

````text
# DTC P2135 (K20C1) (2017 2018 2019)

DTC P2135: Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit and the throttle position (TP) sensor B circuit for rationality check. In order to provide electrical diagnostics the output voltage of both sensors are continuously monitored and compared with minimum and maximum thresholds. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.The rationality diagnostic compares the throttle positions determined from the TP sensors to each other. If the difference between the positions is greater than a calibrated threshold, then the process is started to pinpoint the faulty TP sensor. The pinpointing is done with two tests. The first test compares the throttle position from the TP sensor to a modeled value based on the engine operation point. This test is done sequentially for both TP sensors. If this test does not determine the faulty TP sensor, a second test is performed to determine the faulty TP sensor. The second test compares the two differences between the TP sensor values and the reference position, based on engine operation, to each other. If TP sensor A or B is different from the reference position, the PCM detects a malfunction and stores a DTC

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 480 rpm | -

TP sensor A voltage [TP Sensor A]* | 0.195 V | 4.805 V

TP sensor B voltage [TP Sensor B]** | 0.195 V | 4.805 V

Commanded throttle position | 0 % | 99.99847 %

*: For TP sensor A circuit range/performance detection

**: For TP sensor B circuit range/performance detection

[ ]: HDS Parameter

Malfunction Threshold

If the absolute difference of the position between TP sensor A and TP sensor B is greater than 5 - 6.25 % for at least 0.14 second, the pinpointing test is requested:

Either of the conditions is met during pinpointing test:

- TP sensor A circuit range/performance

- - The difference between the actual throttle position based on the voltage from TP sensor A and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

- - The difference between the actual throttle position based on the voltage from TP sensor A and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

The difference between the actual throttle position based on the voltage from TP sensor A and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

- - The absolute deviation from relative air charge signal of TP sensor A is greater than the deviation of TP sensor B.

- - The absolute deviation from relative air charge signal of TP sensor A is greater than the deviation of TP sensor B.

The absolute deviation from relative air charge signal of TP sensor A is greater than the deviation of TP sensor B.

- TP sensor B circuit range/performance

- - The difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

- - The difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

The difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

- - The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

- - The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure (TP sensor A/B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC
````

## Chunk 5896: DTC P2135 (K20C1) (2017 2018 2019)

- Title: DTC P2135 (K20C1) (2017 2018 2019)
- Source path: `pages\7028.html`
- Chunk ID: `chunk_20306067e569`
- Images: `images\GHH403458.jpeg`, `images\GHH403459.jpeg`
- Duplicate sources: `pages\8615.html`, `pages\22791.html`, `pages\21204.html`

### Full Text

````text
difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.0234 % for at least 0.28 second.

- - The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

- - The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

The absolute deviation from relative air charge signal of TP sensor B is greater than the deviation of TP sensor A.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure (TP sensor A/B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5897: DTC P2135 (K20C1) (2019)

- Title: DTC P2135 (K20C1) (2019)
- Source path: `pages\7029.html`
- Chunk ID: `chunk_cadf2229aa7d`
- Images: `images\GHH403460.jpeg`, `images\GHH403461.jpeg`
- Duplicate sources: `pages\8616.html`, `pages\22792.html`, `pages\21205.html`

### Full Text

````text
# DTC P2135 (K20C1) (2019)

DTC P2135: Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit and the throttle position (TP) sensor B circuit for rationality check. In order to provide electrical diagnostics the output voltage of both sensors are continuously monitored and compared with minimum and maximum thresholds. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.The rationality diagnostic compares the throttle positions determined from the TP sensors to each other. If the difference between the positions is greater than a calibrated threshold, then the process is started to pinpoint the faulty TP sensor. The pinpointing is done with two tests. The first test compares the throttle position from the TP sensor to a modeled value based on the engine operation point. This test is done sequentially for both TP sensors. If this test does not determine the faulty TP sensor, a second test is performed to determine the faulty TP sensor. The second test compares the two differences between the TP sensor values and the reference position, based on engine operation, to each other. If TP sensor A or B is different from the reference position, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

If the absolute difference of the position between TP sensor A and TP sensor B is greater than 5 - 6.25 % for at least 0.14 second, the pinpointing test is requested:

Any of the conditions is met during pinpointing test:

- The absolute difference between the actual throttle position based on the voltage from TP sensor A and the relative air charge signal is greater than 9.02 %.

- The absolute difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.02 %.

- The absolute deviation from relative air charge signal of TP sensor A is greater than the deviation of TP sensor B.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure (TP sensor A/B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5898: DTC P2135 (K20C1) (2020 2021)

- Title: DTC P2135 (K20C1) (2020 2021)
- Source path: `pages\7030.html`
- Chunk ID: `chunk_7093dff970a3`
- Images: `images\GHH403462.jpeg`, `images\GHH403463.jpeg`
- Duplicate sources: `pages\8617.html`, `pages\22793.html`, `pages\21206.html`

### Full Text

````text
# DTC P2135 (K20C1) (2020 2021)

DTC P2135: Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit and the throttle position (TP) sensor B circuit. In order to provide electrical diagnostics the output voltage of both sensors are continuously monitored and compared with other sensors. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Either of the conditions is met:

- The absolute difference between the actual throttle position based on the voltage from TP sensor A and the relative air charge signal is greater than 9.02 %.

- The absolute difference between the actual throttle position based on the voltage from TP sensor B and the relative air charge signal is greater than 9.02 %.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body failure (TP sensor A/B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5899: DTC P2135 (K20C2)

- Title: DTC P2135 (K20C2)
- Source path: `pages\7031.html`
- Chunk ID: `chunk_18b5ce211e7c`
- Images: `images\GHH403464.jpeg`, `images\GHH403465.jpeg`, `images\GHH403466.jpeg`
- Duplicate sources: `pages\8618.html`, `pages\22794.html`, `pages\21207.html`

### Full Text

````text
# DTC P2135 (K20C2)

DTC P2135: Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM then operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). The PCM adds the TP sensor A and TP sensor B values, and compares the addition value with 5 V. If the deviation exceeds a certain value for a specified time, the PCM detects a malfunction in the relationship between TP sensor A and TP sensor B, and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

TP sensor B voltage[TP SENSOR B] | 1.1 V | 4.4 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The deviation between 5 V and addition value of TP sensor A and TP sensor B exceeds the threshold value which depends on TP sensor B voltage for at least 200 milliseconds as shown in the following graph.

Courtesy of HONDA, U.S.A., INC.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TP sensor A THL1 line short to TP sensor B THL2 line

- TP sensor A failure

- TP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5900: DTC P2135 (L15B7/L15BA/L15BY)

- Title: DTC P2135 (L15B7/L15BA/L15BY)
- Source path: `pages\7032.html`
- Chunk ID: `chunk_ab6f5e8a6d2d`
- Images: `images\GHH403467.jpeg`, `images\GHH403468.jpeg`, `images\GHH403469.jpeg`
- Duplicate sources: `pages\8619.html`, `pages\22795.html`, `pages\21208.html`

### Full Text

````text
# DTC P2135 (L15B7/L15BA/L15BY)

DTC P2135: Throttle Position (TP) Sensor A/B Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM then operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensor A (installed in the throttle body). The PCM adds the TP sensor A and TP sensor B values, and compares the addition value with 5 V. If the deviation exceeds a certain value for a specified time, the PCM detects a malfunction in the relationship between TP sensor A and TP sensor B, and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The deviation between 5 V and addition value of TP sensor A and TP sensor B exceeds the threshold value which depends on TP sensor B voltage for at least 200 milliseconds as shown in the following graph.

Courtesy of HONDA, U.S.A., INC.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TP sensor A THL1 line short to TP sensor B THL2 line

- TP sensor A failure

- TP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5901: DTC P2138 (K20C1) (2017 2018 2019)

- Title: DTC P2138 (K20C1) (2017 2018 2019)
- Source path: `pages\7033.html`
- Chunk ID: `chunk_8247d230c361`
- Images: `images\GHH403470.jpeg`, `images\GHH403471.jpeg`
- Duplicate sources: `pages\8620.html`, `pages\22796.html`, `pages\21209.html`

### Full Text

````text
# DTC P2138 (K20C1) (2017 2018 2019)

DTC P2138: Accelerator Pedal Position (APP) Sensor A/B (Throttle Position (TP) Sensor D/E) Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the synchronization check of the APP sensors, the variance of both APP sensor signals is compared with the synchronization tolerance. If the variance is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.24 millisecond or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The variance of voltage between half of APP sensor A voltage and APP sensor B voltage is greater than 0.109 to 0.1342 V for at least 0.24 millisecond.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

- APP sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5902: DTC P2138 (K20C1) (2019 2020 2021)

- Title: DTC P2138 (K20C1) (2019 2020 2021)
- Source path: `pages\7034.html`
- Chunk ID: `chunk_b40041357e74`
- Images: `images\GHH403472.jpeg`, `images\GHH403473.jpeg`
- Duplicate sources: `pages\8621.html`, `pages\22797.html`, `pages\21210.html`

### Full Text

````text
# DTC P2138 (K20C1) (2019 2020 2021)

DTC P2138: Accelerator Pedal Position (APP) Sensor A/B (Throttle Position (TP) Sensor D/E) Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B determine the position of the accelerator pedal. At the same mechanical position, the signal voltage of APP sensor B is always by factor 2 smaller than the voltage of APP sensor A. By different checks it is guaranteed that on account of a single fault, the pedal value cannot be higher than the corresponding mechanical position of the accelerator pedal. Circuit continuity check and synchronization check are done at the powertrain control module (PCM). For the synchronization check of the APP sensors, the variance of both APP sensor signals is compared with the synchronization tolerance. If the variance is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.24 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

APP sensor A output voltage [APP Sensor A] | -0.45 V | 5.1 V

APP sensor B output voltage [APP Sensor B] | -0.05 V | 2.6 V

[ ]: HDS Parameter

Malfunction Threshold

The variance of voltage between half of APP sensor A voltage and APP sensor B voltage is greater than 0.094 to 0.134 V for at least 0.24 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A failure

- APP sensor B failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5903: DTC P2138 (K20C2)

- Title: DTC P2138 (K20C2)
- Source path: `pages\7035.html`
- Chunk ID: `chunk_74f5a9c8d8e7`
- Images: `images\GHH403474.jpeg`, `images\GHH403475.jpeg`
- Duplicate sources: `pages\8622.html`, `pages\22798.html`, `pages\21211.html`

### Full Text

````text
# DTC P2138 (K20C2)

DTC P2138: Accelerator Pedal Position (APP) Sensor A/B (Throttle Position (TP) Sensor D/E) Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B are potentiometers. They are installed on the accelerator pedal. When the accelerator pedal is pressed, APP sensors A and B detect the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in APP sensors A and B and transmitted to the powertrain control module (PCM) to compute the target position. APP sensor A is the primary control, and APP sensor B is a back-up of APP sensor A in case it malfunctions. Both sensors compare their output voltage to each other for malfunction detection. When the voltage difference of APP sensor B is out of a fixed range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 300 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these conditions is met for at least 300 milliseconds:

- The APP sensor B voltage [APP SENSOR B] is 0 V or less, or 0.37 V or more when APP sensor A voltage [APP SENSOR A] is 0.37 V.

- The APP sensor B voltage [APP SENSOR B] is 2.31 V or less, or 2.69 V or more when APP sensor A voltage [APP SENSOR A] is 5.0 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A/B failure

- APP sensor A APS1 line short to APP sensor B APS2 line

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5904: DTC P2138 (L15B7/L15BA/L15BY)

- Title: DTC P2138 (L15B7/L15BA/L15BY)
- Source path: `pages\7036.html`
- Chunk ID: `chunk_5cd55da4168f`
- Images: `images\GHH403476.jpeg`, `images\GHH403477.jpeg`
- Duplicate sources: `pages\8623.html`, `pages\22799.html`, `pages\21212.html`

### Full Text

````text
# DTC P2138 (L15B7/L15BA/L15BY)

DTC P2138: Accelerator Pedal Position (APP) Sensor A/B (Throttle Position (TP) Sensor D/E) Incorrect Voltage Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Accelerator pedal position (APP) sensor A and accelerator pedal position (APP) sensor B are potentiometers. They are installed on the accelerator pedal. When the accelerator pedal is pressed, APP sensors A and B detect the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in APP sensors A and B and transmitted to the powertrain control module (PCM) to compute the target position. APP sensor A is the primary control, and APP sensor B is a back-up of APP sensor A in case it malfunctions. Both sensors compare their output voltage to each other for malfunction detection. When the voltage difference of APP sensor B is out of a fixed range for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 300 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these conditions is met for at least 300 milliseconds:

- The APP sensor B voltage [APP SENSOR B] is 0 V or less, or 0.37 V or more when APP sensor A voltage [APP SENSOR A] is 0.37 V.

- The APP sensor B voltage [APP SENSOR B] is 2.31 V or less, or 2.69 V or more when APP sensor A voltage [APP SENSOR A] is 5.0 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- APP sensor A/B failure

- APP sensor A APS1 line short to APP sensor B APS2 line

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5905: DTC P2148 (L15B7/L15BA/L15BY)

- Title: DTC P2148 (L15B7/L15BA/L15BY)
- Source path: `pages\7037.html`
- Chunk ID: `chunk_3219800fd9d4`
- Images: `images\GHH403478.jpeg`
- Duplicate sources: `pages\8624.html`, `pages\22800.html`, `pages\21213.html`

### Full Text

````text
# DTC P2148 (L15B7/L15BA/L15BY)

DTC P2148: Injector Power Supply Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) uses main CPU power and regenerative energy generated from the high pressure fuel pump to supply the boost voltage for the direct injector. The damper circuit built into the PCM lowers the voltage when the boosted voltage is too high. If the boosted voltage is a specified voltage for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.03 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The boosted voltage is 54 V or more for at least 0.03 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5906: DTC P2158 (K20C1) (2020 2021)

- Title: DTC P2158 (K20C1) (2020 2021)
- Source path: `pages\7038.html`
- Chunk ID: `chunk_992fd9151fdd`
- Images: none
- Duplicate sources: `pages\8625.html`, `pages\22801.html`, `pages\21214.html`

### Full Text

````text
# DTC P2158 (K20C1) (2020 2021)

DTC P2158: Vehicle Speed Sensor B No Signal

General Description

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the right front wheel speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

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

The right front wheel speed sensor outputs less than 1.94 mph (3.13 km/h) despite the other speed sensor's output of 1.94 mph (3.13 km/h) or more for at least 5.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Right front wheel speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5907: DTC P2158 (K20C2 (M/T)) (2019 2020)

- Title: DTC P2158 (K20C2 (M/T)) (2019 2020)
- Source path: `pages\7039.html`
- Chunk ID: `chunk_167cfbb06fee`
- Images: `images\GHH403479.jpeg`
- Duplicate sources: `pages\8626.html`, `pages\22802.html`, `pages\21215.html`

### Full Text

````text
# DTC P2158 (K20C2 (M/T)) (2019 2020)

DTC P2158: Vehicle Speed Sensor B No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the right front wheel speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The right front wheel speed sensor outputs 0 mph (0 km/h) despite the left front wheel speed sensor and output shaft (countershaft) speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Right front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5908: DTC P2158 (L15B7/L15BA (M/T)) (2019 2020 2021)

- Title: DTC P2158 (L15B7/L15BA (M/T)) (2019 2020 2021)
- Source path: `pages\7040.html`
- Chunk ID: `chunk_b330f45cba8c`
- Images: `images\GHH403480.jpeg`
- Duplicate sources: `pages\8627.html`, `pages\22803.html`, `pages\21216.html`

### Full Text

````text
# DTC P2158 (L15B7/L15BA (M/T)) (2019 2020 2021)

DTC P2158: Vehicle Speed Sensor B No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If the right front wheel speed sensor outputs 0 mph (0 km/h) despite the other speed sensor's output at a certain speed for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The right front wheel speed sensor outputs 0 mph (0 km/h) despite the left front wheel speed sensor and output shaft (countershaft) speed sensor's output of 2 mph (3 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Right front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5909: DTC P2159 (K20C2 (M/T)) (2019 2020)

- Title: DTC P2159 (K20C2 (M/T)) (2019 2020)
- Source path: `pages\7041.html`
- Chunk ID: `chunk_d473f7619a96`
- Images: `images\GHH403481.jpeg`
- Duplicate sources: `pages\8628.html`, `pages\22804.html`, `pages\21217.html`

### Full Text

````text
# DTC P2159 (K20C2 (M/T)) (2019 2020)

DTC P2159: Vehicle Speed Sensor B Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the wheel speed sensors to detect malfunctions. If the right front wheel speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The right front wheel speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Right front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5910: DTC P2159 (L15B7/L15BA (M/T)) (2019 2020 2021)

- Title: DTC P2159 (L15B7/L15BA (M/T)) (2019 2020 2021)
- Source path: `pages\7042.html`
- Chunk ID: `chunk_7fe64f8257da`
- Images: `images\GHH403482.jpeg`
- Duplicate sources: `pages\8629.html`, `pages\22805.html`, `pages\21218.html`

### Full Text

````text
# DTC P2159 (L15B7/L15BA (M/T)) (2019 2020 2021)

DTC P2159: Vehicle Speed Sensor B Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the vehicle speed converted from the wheel speed sensors to detect malfunctions. If the right front wheel speed sensor output is a specified value for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The right front wheel speed sensor outputs 156 mph (250 km/h) or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Right front wheel speed sensor failure

- VSA modulator-control unit internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5911: DTC P215C (K20C1) (2020 2021)

- Title: DTC P215C (K20C1) (2020 2021)
- Source path: `pages\7043.html`
- Chunk ID: `chunk_6a686ae2527c`
- Images: none
- Duplicate sources: `pages\8630.html`, `pages\22806.html`, `pages\21219.html`

### Full Text

````text
# DTC P215C (K20C1) (2020 2021)

DTC P215C: Output Shaft (Countershaft) Speed/Vehicle Speed Correlation

General Description

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If there is a difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.4 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors is 1.94 mph (3.13 km/h) or more for at least 8.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor

- Left front wheel speed sensor failure

- Right front wheel speed sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5912: DTC P215C (K20C2 (M/T)) (2019 2020)

- Title: DTC P215C (K20C2 (M/T)) (2019 2020)
- Source path: `pages\7044.html`
- Chunk ID: `chunk_5abb9d58edf4`
- Images: `images\GHH403483.jpeg`, `images\GHH403484.png`
- Duplicate sources: `pages\8631.html`, `pages\22807.html`, `pages\21220.html`

### Full Text

````text
# DTC P215C (K20C2 (M/T)) (2019 2020)

DTC P215C: Output Shaft (Countershaft) Speed/Vehicle Speed Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If there is a difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors is 1.9 mph (3 km/h) 6% or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor

- Left front wheel speed sensor failure

- Right front wheel speed sensor failure

- PCM internal circuit malfunction

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5913: DTC P215C (L15B7/L15BA (M/T)) (2019 2020 2021)

- Title: DTC P215C (L15B7/L15BA (M/T)) (2019 2020 2021)
- Source path: `pages\7045.html`
- Chunk ID: `chunk_bb8dd5d7a4db`
- Images: `images\GHH403485.jpeg`, `images\GHH403486.png`
- Duplicate sources: `pages\8632.html`, `pages\22808.html`, `pages\21221.html`

### Full Text

````text
# DTC P215C (L15B7/L15BA (M/T)) (2019 2020 2021)

DTC P215C: Output Shaft (Countershaft) Speed/Vehicle Speed Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the speed difference of the wheel speed sensors and output shaft (countershaft) speed sensor to detect malfunctions. If there is a difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors for a specified duration, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | Running

Malfunction Threshold

The difference between the speed of the output shaft (countershaft) speed sensor and the average of left and right wheel speed sensors is 1.9 mph (3 km/h) 6% or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Output shaft (countershaft) speed sensor

- Left front wheel speed sensor failure

- Right front wheel speed sensor failure

- PCM internal circuit malfunction

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5914: DTC P2175 (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P2175 (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\7046.html`
- Chunk ID: `chunk_3b34ec495e44`
- Images: `images\GHH403487.jpeg`, `images\GHH403488.jpeg`
- Duplicate sources: `pages\8633.html`, `pages\22809.html`, `pages\21222.html`

### Full Text

````text
# DTC P2175 (L15B7/L15BA/L15BY) (2020 2021)

DTC P2175: Throttle Actuator Control System Low Air Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

When the throttle body blockage occurs, the air flow decreases compared to the normal condition at similar throttle position. From this characteristic, the powertrain control module (PCM) presumes a blockage of the throttle body. If the throttle body blockage rate reaches 100 % of the predetermined threshold, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | At idle

Malfunction Threshold

The throttle body blockage rate is 0.99 or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body blockage

- Air cleaner blocked

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in P or N) until the radiator fan comes on.

- Turn the vehicle to the OFF (LOCK) mode.

- Start the engine and let it idle for at least 1 minute.

- Repeat Driving Pattern steps 2 through 3, 20 times.

- Start the engine and let it idle for at least 10 minutes.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5915: DTC P2176 (K20C1) (2017 2018 2019)

- Title: DTC P2176 (K20C1) (2017 2018 2019)
- Source path: `pages\7047.html`
- Chunk ID: `chunk_870ff40d310d`
- Images: `images\GHH403489.jpeg`
- Duplicate sources: `pages\8634.html`, `pages\22810.html`, `pages\21223.html`

### Full Text

````text
# DTC P2176 (K20C1) (2017 2018 2019)

DTC P2176: Throttle Actuator Control System Idle Position Not Learned

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system starts a learning routine of throttle valve position to correlate the measured value of the throttle position (TP) sensors to the mechanical throttle valve position. The electronic throttle control system uses default values for the lower mechanical stop initially, and then it learns the actual value each time the throttle body is used. During the learning routine, the throttle valve steps from the maximum possible value of the lower mechanical stop to the measured value at the actual lower mechanical stop position. If the throttle body lower mechanical limit cannot be learned, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 41.5 deg.F (5.26 deg.C) | 212.8 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.5 deg.F (5.26 deg.C) | 289.8 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

- Initial learning of the closed throttle valve position not possible Any of the conditions occurs (the detections are done in following sequence):

Any of the conditions occurs (the detections are done in following sequence):

- - The low mechanical stop initial learning has not been performed and lower mechanical stop offset learning is aborted due to enable conditions are not fulfilled. - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second. - The calculated duty cycle ratio is 60 % or less for at least 1 second. - The TP sensor A voltage [TP Sensor A] is not in the range of 0.5127 - 0.68726 V at lower mechanical stop. - The TP sensor B voltage [TP Sensor B] is not in the range of 4.31274 - 4.4873 V at lower mechanical stop.

- - The low mechanical stop initial learning has not been performed and lower mechanical stop offset learning is aborted due to enable conditions are not fulfilled.

The low mechanical stop initial learning has not been performed and lower mechanical stop offset learning is aborted due to enable conditions are not fulfilled.

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

- - The calculated duty cycle ratio is 60 % or less for at least 1 second.

The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The TP sensor A voltage [TP Sensor A] is not in the range of 0.5127 - 0.68726 V at lower mechanical stop.

The TP sensor A voltage [TP Sensor A] is not in the range of 0.5127 - 0.68726 V at lower mechanical stop.

- - The TP sensor B voltage [TP Sensor B] is not in the range of 4.31274 - 4.4873 V at lower mechanical stop.

The TP sensor B voltage [TP Sensor B] is not in the range of 4.31274 - 4.4873 V at lower mechanical stop.

- Learning of the closed throttle valve position not possible Either of the conditions occurs (the detections are done in following sequence):

Either of the conditions occurs (the detections are done in following sequence):

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second. - The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.
````

## Chunk 5916: DTC P2176 (K20C1) (2017 2018 2019)

- Title: DTC P2176 (K20C1) (2017 2018 2019)
- Source path: `pages\7047.html`
- Chunk ID: `chunk_6c35de400409`
- Images: `images\GHH403489.jpeg`
- Duplicate sources: `pages\8634.html`, `pages\22810.html`, `pages\21223.html`

### Full Text

````text
Sensor B] is not in the range of 4.31274 - 4.4873 V at lower mechanical stop.

- Learning of the closed throttle valve position not possible Either of the conditions occurs (the detections are done in following sequence):

Either of the conditions occurs (the detections are done in following sequence):

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second. - The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

- - The calculated duty cycle ratio is 60 % or less for at least 1 second.

The calculated duty cycle ratio is 60 % or less for at least 1 second.

- Lower mechanical stop offset learning aborted Either of the conditions occurs:

Either of the conditions occurs:

- - The TP sensor A voltage [TP Sensor A] is greater than 0.68726 V or the TP sensor B [TP Sensor B] voltage is greater than 4.4873 V at lower mechanical stop. - The TP sensor A voltage [TP Sensor A] is less than 0.51270 V or the TP sensor B voltage [TP Sensor B] is less than 4.31274 V at lower mechanical stop.

- - The TP sensor A voltage [TP Sensor A] is greater than 0.68726 V or the TP sensor B [TP Sensor B] voltage is greater than 4.4873 V at lower mechanical stop.

The TP sensor A voltage [TP Sensor A] is greater than 0.68726 V or the TP sensor B [TP Sensor B] voltage is greater than 4.4873 V at lower mechanical stop.

- - The TP sensor A voltage [TP Sensor A] is less than 0.51270 V or the TP sensor B voltage [TP Sensor B] is less than 4.31274 V at lower mechanical stop.

The TP sensor A voltage [TP Sensor A] is less than 0.51270 V or the TP sensor B voltage [TP Sensor B] is less than 4.31274 V at lower mechanical stop.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- PCM internal failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode.

- Turn the vehicle to the ON mode.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5917: DTC P2176 (K20C1) (2019)

- Title: DTC P2176 (K20C1) (2019)
- Source path: `pages\7048.html`
- Chunk ID: `chunk_6f26f31d6332`
- Images: `images\GHH403490.jpeg`
- Duplicate sources: `pages\8635.html`, `pages\22811.html`, `pages\21224.html`

### Full Text

````text
# DTC P2176 (K20C1) (2019)

DTC P2176: Throttle Actuator Control System Idle Position Not Learned

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system starts a learning routine of throttle valve position to correlate the measured value of the throttle position (TP) sensors to the mechanical throttle valve position. The electronic throttle control system uses default values for the lower mechanical stop initially, and then it learns the actual value each time the throttle body is used. During the learning routine, the throttle valve steps from the maximum possible value of the lower mechanical stop to the measured value at the actual lower mechanical stop position. If the throttle body lower mechanical limit cannot be learned, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.5 deg.F (5.26 deg.C) | 212.8 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.5 deg.F (5.26 deg.C) | 289.8 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

- Initial learning of the closed throttle valve position not possible Any of the conditions occurs:

Any of the conditions occurs:

- - The low mechanical stop offset learning is active but enable conditions are no longer fulfilled. - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second. - The calculated duty cycle ratio is 60 % or less for at least 1 second. - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop. - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- - The low mechanical stop offset learning is active but enable conditions are no longer fulfilled.

The low mechanical stop offset learning is active but enable conditions are no longer fulfilled.

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

- - The calculated duty cycle ratio is 60 % or less for at least 1 second.

The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

- - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- Learning of the closed throttle valve position not possible Any of the conditions occurs:

Any of the conditions occurs:

- - The calculated duty cycle ratio is 60 % or less for at least 1 second. - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop. - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- - The calculated duty cycle ratio is 60 % or less for at least 1 second.

The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.
````

## Chunk 5918: DTC P2176 (K20C1) (2019)

- Title: DTC P2176 (K20C1) (2019)
- Source path: `pages\7048.html`
- Chunk ID: `chunk_4bf25c65d54f`
- Images: `images\GHH403490.jpeg`
- Duplicate sources: `pages\8635.html`, `pages\22811.html`, `pages\21224.html`

### Full Text

````text
ve position not possible Any of the conditions occurs:

Any of the conditions occurs:

- - The calculated duty cycle ratio is 60 % or less for at least 1 second. - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop. - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- - The calculated duty cycle ratio is 60 % or less for at least 1 second.

The calculated duty cycle ratio is 60 % or less for at least 1 second.

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

- - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- Closed throttle valve position exceeds the threshold Any of the conditions occurs:

Any of the conditions occurs:

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second. - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop. - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- - The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

The difference between actual TP sensor A at lower mechanical stop and desired value for adaptation (based on maximum allowed voltage for lower mechanical stop) is greater than 1.5 % for at least 1 second.

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

- - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- PCM internal failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5919: DTC P2176 (K20C1) (2020 2021)

- Title: DTC P2176 (K20C1) (2020 2021)
- Source path: `pages\7049.html`
- Chunk ID: `chunk_94c7ef374958`
- Images: `images\GHH403491.jpeg`
- Duplicate sources: `pages\8636.html`, `pages\22812.html`, `pages\21225.html`

### Full Text

````text
# DTC P2176 (K20C1) (2020 2021)

DTC P2176: Throttle Actuator Control System Idle Position Not Learned

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system starts a learning routine of throttle valve position to correlate the measured value of the throttle position (TP) sensors to the mechanical throttle valve position. The electronic throttle control system uses default values for the lower mechanical stop initially, and then it learns the actual value each time the throttle body is used. During the learning routine, the throttle valve steps from the maximum possible value of the lower mechanical stop to the measured value at the actual lower mechanical stop position. If the throttle body lower mechanical limit cannot be learned, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | 41.5 deg.F (5.26 deg.C) | 212.8 deg.F (100.46 deg.C)

Intake air temperature [IAT Sensor (1)] | 41.5 deg.F (5.26 deg.C) | 289.8 deg.F (143.26 deg.C)

Engine speed [Engine Speed] | - | 250 rpm

Vehicle speed [Vehicle Speed] | - | 0.6 mph (1 km/h)

12 volt battery voltage [Battery] | 10.5 V | 16.5 V

[ ]: HDS Parameter

Malfunction Threshold

- Initial learning of the closed throttle valve position not possible The initial learning is not performed.

The initial learning is not performed.

- Learning of the closed throttle valve position not possible Either of the condition occurs:

Either of the condition occurs:

- - The difference between the actual learned TP sensor A voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more. - The difference between the actual learned TP sensor B voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more.

- - The difference between the actual learned TP sensor A voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more.

The difference between the actual learned TP sensor A voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more.

- - The difference between the actual learned TP sensor B voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more.

The difference between the actual learned TP sensor B voltage and the previous read TP sensor A voltage at the mechanical stop is -0.07 V or more.

- Closed throttle valve position exceeds the threshold Either of the condition occurs:

Either of the condition occurs:

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop. - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

- - The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

The TP sensor A voltage is more than 0.69 V or less than 0.51 V during sensor offset learning at lower mechanical stop.

- - The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

The TP sensor B voltage is more than 4.49 V or less than 4.31 V during sensor offset learning at lower mechanical stop.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle valve stuck

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- PCM internal failure

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode.

- Turn the vehicle to the ON mode.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5920: DTC P2176 (K20C2)

- Title: DTC P2176 (K20C2)
- Source path: `pages\7050.html`
- Chunk ID: `chunk_f260c9a8c492`
- Images: `images\GHH403492.jpeg`
- Duplicate sources: `pages\8637.html`, `pages\22813.html`, `pages\21226.html`

### Full Text

````text
# DTC P2176 (K20C2)

DTC P2176: Throttle Actuator Control System Idle Position Not Learned

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). The PCM transmits a signal to the throttle actuator and moves the throttle valve to the fully closed position to register the throttle valve fully closed position after the vehicle is turned to the OFF (LOCK) mode. When the registration of the throttle valve fully closed position is not completed within a predetermined time after the vehicle is turned to the OFF (LOCK) mode, also the registered value is out of predetermined range, the PCM detects a malfunction in the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met, when the registration of the throttle valve fully closed position is not completed for at least 2.0 seconds after the vehicle condition is turned to the OFF (LOCK) mode:

- The registered value of the throttle valve fully closed position is more than 1.02 V, or less than 0.49 V.*

- The registered value of the throttle valve fully closed position is more than 4.51 V, or less than 3.98 V.**

*: TP sensor A [TP SENSOR A]

**: TP sensor B [TP SENSOR B]

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- Throttle body internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5921: DTC P2176 (L15B7/L15BA)

- Title: DTC P2176 (L15B7/L15BA)
- Source path: `pages\7051.html`
- Chunk ID: `chunk_e9600b141d8f`
- Images: `images\GHH403493.jpeg`
- Duplicate sources: `pages\8638.html`, `pages\22814.html`, `pages\21227.html`

### Full Text

````text
# DTC P2176 (L15B7/L15BA)

DTC P2176: Throttle Actuator Control System Idle Position Not Learned

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). When the accelerator pedal is pressed, the APP sensor detects the accelerator pedal opening value. The accelerator pedal opening value is converted to a signal in the APP sensor and transmitted to the PCM to compute the target position. The PCM determines the throttle valve target position according to the signal received and operates the throttle actuator to move the throttle valve to the target position. The actual throttle valve position is determined by TP sensors A and B (installed in the throttle body). The PCM transmits a signal to the throttle actuator and moves the throttle valve to the fully closed position to register the throttle valve fully closed position after the vehicle is turned to the OFF (LOCK) mode. When the registration of the throttle valve fully closed position is not completed within a predetermined time after the vehicle is turned to the OFF (LOCK) mode, also the registered value is out of predetermined range, the PCM detects a malfunction in the electronic throttle control system and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 6.0 V | -

Vehicle | OFF (LOCK) mode

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met, when the registration of the throttle valve fully closed position is not completed for at least 2.0 seconds after the vehicle condition is turned to the OFF (LOCK) mode:

- The registered value of the throttle valve fully closed position is more than 1.02 V, or less than 0.49 V.*

- The registered value of the throttle valve fully closed position is more than 4.51 V, or less than 3.98 V.**

*: TP sensor A [TP SENSOR A]

**: TP sensor B [TP SENSOR B]

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

- Throttle actuator MTR1 line failure

- Throttle actuator MTR2 line failure

- Throttle body internal failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5922: DTC P2182 (K20C1) (2017 2018 2019)

- Title: DTC P2182 (K20C1) (2017 2018 2019)
- Source path: `pages\7052.html`
- Chunk ID: `chunk_74d2b8fc1112`
- Images: `images\GHH403494.jpeg`, `images\GHH403495.jpeg`
- Duplicate sources: `pages\8639.html`, `pages\22815.html`, `pages\21228.html`

### Full Text

````text
# DTC P2182 (K20C1) (2017 2018 2019)

DTC P2182: Engine Coolant Temperature (ECT) Sensor 2 Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the ECT sensor 2 output temperature is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ECT sensor 2 output voltage [ECT Sensor 2] is greater than 281 deg.F (138 deg.C) or lower than -55 deg.F (-48 deg.C) for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 2 TW2 line short to ground

- ECT sensor 2 TW2 line open

- ECT sensor 2 failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5923: DTC P2182 (K20C1) (2019 2020 2021)

- Title: DTC P2182 (K20C1) (2019 2020 2021)
- Source path: `pages\7053.html`
- Chunk ID: `chunk_87ffeeb21b0f`
- Images: `images\GHH403496.jpeg`, `images\GHH403497.jpeg`
- Duplicate sources: `pages\8640.html`, `pages\22816.html`, `pages\21229.html`

### Full Text

````text
# DTC P2182 (K20C1) (2019 2020 2021)

DTC P2182: Engine Coolant Temperature (ECT) Sensor 2 Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the ECT sensor 2 output temperature is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ECT sensor 2 output temperature [ECT Sensor 2] is greater than 279.2 deg.F (137.3 deg.C) for at least 5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 2 TW2 line short to ground

- ECT sensor 2 TW2 line open

- ECT sensor 2 failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5924: DTC P2182 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2182 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\7054.html`
- Chunk ID: `chunk_9361ad7ac045`
- Images: `images\GHH403498.jpeg`, `images\GHH403499.jpeg`
- Duplicate sources: `pages\8641.html`, `pages\22817.html`, `pages\21230.html`

### Full Text

````text
# DTC P2182 (K20C2) (2018 2019 2020 2021)

DTC P2182: Engine Coolant Temperature (ECT) Sensor 2 Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Engine coolant temperature (ECT) sensor 2 is a thermistor attached to the radiator. The powertrain control module (PCM) applies voltage (about 5 V) to the TW2 signal circuit through a pull-up resistor. As the engine coolant temperature cools, the ECT sensor 2 resistance increases, and the PCM detects a high signal voltage. As the engine coolant warms, the ECT sensor 2 resistance decreases, and the PCM detects a low signal voltage. If the ECT sensor 2 output voltage is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ECT sensor 2 output voltage [ECT SENSOR 2] is 0.14 V or less, or 4.99 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5925: DTC P2182 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P2182 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\7055.html`
- Chunk ID: `chunk_586eb945d941`
- Images: `images\GHH403500.jpeg`, `images\GHH403501.jpeg`
- Duplicate sources: `pages\8642.html`, `pages\22818.html`, `pages\21231.html`

### Full Text

````text
# DTC P2182 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P2182: Engine Coolant Temperature (ECT) Sensor 2 Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Engine coolant temperature (ECT) sensor 2 is a thermistor attached to the radiator. The powertrain control module (PCM) applies voltage (about 5 V) to the TW2 signal circuit through a pull-up resistor. As the engine coolant temperature cools, the ECT sensor 2 resistance increases, and the PCM detects a high signal voltage. As the engine coolant warms, the ECT sensor 2 resistance decreases, and the PCM detects a low signal voltage. If the ECT sensor 2 output voltage is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ECT sensor 2 output voltage [ECT SENSOR 2] is 0.14 V or less, or 4.99 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5926: DTC P2182 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2182 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7056.html`
- Chunk ID: `chunk_288ce8c1d200`
- Images: `images\GHH403502.jpeg`, `images\GHH403503.jpeg`
- Duplicate sources: `pages\8643.html`, `pages\22819.html`, `pages\21232.html`

### Full Text

````text
# DTC P2182 (Si) (2017 2018 2019 2020 2021)

DTC P2182: Engine Coolant Temperature (ECT) Sensor 2 Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Engine coolant temperature (ECT) sensor 2 is a thermistor attached to the radiator. The powertrain control module (PCM) applies voltage (about 5 V) to the TW2 signal circuit through a pull-up resistor. As the engine coolant temperature cools, the ECT sensor 2 resistance increases, and the PCM detects a high signal voltage. As the engine coolant warms, the ECT sensor 2 resistance decreases, and the PCM detects a low signal voltage. If the ECT sensor 2 output voltage is a specified range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The ECT sensor 2 output voltage [ECT SENSOR 2] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5927: DTC P2183 (K20C1) (2017 2018 2019)

- Title: DTC P2183 (K20C1) (2017 2018 2019)
- Source path: `pages\7057.html`
- Chunk ID: `chunk_694929fe76dd`
- Images: `images\GHH403504.jpeg`, `images\GHH403505.jpeg`
- Duplicate sources: `pages\8644.html`, `pages\22820.html`, `pages\21233.html`

### Full Text

````text
# DTC P2183 (K20C1) (2017 2018 2019)

DTC P2183: Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the difference between ECT sensor 2 maximum and minimum temperature is a specified value for a specified time, or the difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous*, Once per driving cycle**

Sequence | None

Duration | 5 seconds or more*, 2 minute or more**

DTC Type | Two drive cycles, MIL on

*: Stuck check

**: Cold start check

Enable Conditions

Stuck check

Condition | Minimum | Maximum

Outside air temperature | -54 deg.F (-48 deg.C) | -

Engine speed [Engine Speed]*** | 1, 520 rpm | -

***: Conditions must be met for at least 5 minutes

[ ]: HDS Parameter

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed]*** | 4 mph (5 km/h) | 63 mph (100 km/h)

Other*** | Other than during fuel cut-off operation

***: Conditions must be met for at least 5 minutes

[ ]: HDS Parameter

Cold start check

Condition | Minimum | Maximum

Engine off time | 7.5 - 9.5 hours**** | -

State of the engine | Running

****: Depending on engine off temperature

Malfunction Threshold

Either of the conditions occurs:

- Stuck check The temperature difference between maximum and minimum of ECT sensor 2 is greater than 4.2 deg.F (2.3 deg.C) for at least 5 seconds.

The temperature difference between maximum and minimum of ECT sensor 2 is greater than 4.2 deg.F (2.3 deg.C) for at least 5 seconds.

- Cold start check The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 17.7 deg.F (9.8 deg.C) for at least 2 minutes.

The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 17.7 deg.F (9.8 deg.C) for at least 2 minutes.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Engine coolant level low

- Thermostat failure

- ECT sensor 2 failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5928: DTC P2183 (K20C1) (2019)

- Title: DTC P2183 (K20C1) (2019)
- Source path: `pages\7058.html`
- Chunk ID: `chunk_c7ee6a4af24f`
- Images: `images\GHH403506.jpeg`, `images\GHH403507.jpeg`
- Duplicate sources: `pages\8645.html`, `pages\22821.html`, `pages\21234.html`

### Full Text

````text
# DTC P2183 (K20C1) (2019)

DTC P2183: Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the difference between ECT sensor 2 maximum and minimum temperature is a specified value for a specified time, or the difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous*, Once per driving cycle**

Sequence | None

Duration | 0.5 second or more*, 90 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Stuck check

**: Cold start check

Enable Conditions

Stuck check

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | - | 176.5 deg.F (80.3 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | - | 289.9 deg.F (143.3 deg.C)

Outside air temperature | -54 deg.F (-48 deg.C) | -

***: Conditions must be met for at least 5 minutes

Condition | Minimum | Maximum

Temperature difference between engine coolant temperature [ECT Sensor 2] and ambient temperature | - | 344.3 deg.F (191.3 deg.C)

Engine speed [Engine Speed]*** | 1, 520 rpm | -

Vehicle speed [Vehicle Speed]*** | 4 mph (5 km/h) | 198 mph (318.8 km/h)

Other*** | Other than during fuel cut-off operation

***: Conditions must be met for at least 5 minutes

Cold start check

Condition | Minimum | Maximum

Engine off time | 6 hours | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs:

- Stuck check The temperature difference between maximum and minimum of ECT sensor 2 is 2.7 deg.F (1.5 deg.C) or less.

The temperature difference between maximum and minimum of ECT sensor 2 is 2.7 deg.F (1.5 deg.C) or less.

- Cold start check The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Engine coolant level low

- Thermostat failure

- ECT sensor 2 failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5929: DTC P2183 (K20C1) (2020 2021)

- Title: DTC P2183 (K20C1) (2020 2021)
- Source path: `pages\7059.html`
- Chunk ID: `chunk_9c3bdef02dd5`
- Images: `images\GHH403508.jpeg`, `images\GHH403509.jpeg`
- Duplicate sources: `pages\8646.html`, `pages\22822.html`, `pages\21235.html`

### Full Text

````text
# DTC P2183 (K20C1) (2020 2021)

DTC P2183: Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the difference between ECT sensor 2 maximum and minimum temperature is a specified value for a specified time, or the difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous*, Once per driving cycle**

Sequence | None

Duration | 0.5 second or more*, 90 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Stuck check

**: Cold start check

Enable Conditions

Stuck check

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | - | 176.5 deg.F (80.3 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | - | 289.9 deg.F (143.3 deg.C)

Outside air temperature | -54 deg.F (-48 deg.C) | -

***: Conditions must be met for at least 5 minutes

Condition | Minimum | Maximum

Temperature difference between engine coolant temperature [ECT Sensor 2] and ambient temperature | - | 344.3 deg.F (191.3 deg.C)

Engine speed [Engine Speed]*** | 1, 520 rpm | -

Vehicle speed [Vehicle Speed]*** | 4 mph (5 km/h) | 198 mph (318.8 km/h)

Other | Engine coolant temperature [ECT Sensor 2] is near outside air temperature

Other than during fuel cut-off operation***

***: Conditions must be met for at least 5 minutes

Cold start check

Condition | Minimum | Maximum

Engine off time | 6 hours | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs:

- Stuck check The temperature difference between maximum and minimum of ECT sensor 2 is 2.7 deg.F (1.5 deg.C) or less.

The temperature difference between maximum and minimum of ECT sensor 2 is 2.7 deg.F (1.5 deg.C) or less.

- Cold start check The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

The difference between the ECT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Engine coolant level low

- Thermostat failure

- ECT sensor 2 failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5930: DTC P2183 (K20C2: USA/Canada models)

- Title: DTC P2183 (K20C2: USA/Canada models)
- Source path: `pages\7060.html`
- Chunk ID: `chunk_cdefeb0522b6`
- Images: `images\GHH403510.jpeg`
- Duplicate sources: `pages\8647.html`, `pages\22823.html`, `pages\21236.html`

### Full Text

````text
# DTC P2183 (K20C2: USA/Canada models)

DTC P2183: Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Two engine coolant temperature (ECT) sensors and one intake air temperature (IAT) sensor are used by the powertrain control module (PCM). When the engine is stopped and enough time has passed, the temperature of the engine will equalize to ambient temperature. ECT sensor 1 and IAT sensor are compared to ECT sensor 2, and if an inappropriate temperature is read, the PCM detects a malfunction in the corresponding sensor and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 6 hours | -

Malfunction Threshold

A malfunction is detected if the following conditions are present after the engine has stopped and the vehicle condition has been turned to the OFF (LOCK) mode, for at least 6 hours before restarting the engine:

Temperature difference between each sensor values | Malfunction judgment

ECT1* - ECT2** | IAT*** - ECT2** | ECT sensor 1 | IAT sensor | ECT sensor 2

Higher than 57 deg.F (32 deg.C) | Higher than 57 deg.F (32 deg.C) | Normal | Normal | Failure

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Failure | Normal | Normal

Lower than -43 deg.F (-24 deg.C) | Failure | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Higher than 57 deg.F (32 deg.C) | Normal | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Normal | Normal | Normal

From -44 deg.F (-25 deg.C) to -108 deg.F (-60 deg.C) | Normal | Failure | Normal

Suspended****

Lower than -108 deg.F (-60 deg.C) | Normal | Failure | Normal

Lower than -43 deg.F (-24 deg.C) | Higher than 57 deg.F (32 deg.C) | Failure | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Failure | Normal | Normal

Lower than -43 deg.F (-24 deg.C) | Normal | Normal | Failure

*: [ECT SENSOR 1]

**: [ECT SENSOR 2]

***: [IAT Sensor (1)]

****: Malfunction judgment is suspended because the cooled air introduced after engine start lowers the intake air temperature; the ambient temperature condition does not stay equal.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 1 failure

- ECT sensor 2 failure

- IAT sensor failure

- Engine block heater attachment (non-genuine part)

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode and wait at least 6 hours.

- Start the engine, and let it idle for at least 10 seconds.

- Do not use an engine block heater because the engine coolant temperature will not stay equal during engine stop.

- When freeze data is stored, test the vehicle under an ambient temperature close to the intake air temperature in the freeze data.

- When an ambient temperature extremely changes, malfunction judgment may not execute. Avoid extreme temperature changing condition after or before engine start. (When the vehicle is parked in the garage, open the shutter to introduce outside air; then start the engine.)

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5931: DTC P2183 (Without XM)

- Title: DTC P2183 (Without XM)
- Source path: `pages\7061.html`
- Chunk ID: `chunk_c30b53095410`
- Images: `images\GHH403511.jpeg`
- Duplicate sources: `pages\8648.html`, `pages\22824.html`, `pages\21237.html`

### Full Text

````text
# DTC P2183 (Without XM)

DTC P2183: Engine Coolant Temperature (ECT) Sensor 2 Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Two engine coolant temperature (ECT) sensors and two intake air temperature (IAT) sensors are used by the powertrain control module (PCM). When the engine is stopped and enough time has passed, the temperature of the engine will equalize to ambient temperature. ECT sensor 1 and IAT sensor 1 are compared to ECT sensor 2, and if an inappropriate temperature is read, the PCM detects a malfunction in the corresponding sensor and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 6 hours | -

Malfunction Threshold

A malfunction is detected if the following conditions are present after the engine has stopped and the vehicle condition has been turned to the OFF (LOCK) mode, for at least 6 hours before restarting the engine:

Temperature difference between each sensor values | Malfunction judgment

ECT1* - ECT2** | IAT1*** - ECT2** | ECT sensor 1 | IAT sensor 1 | ECT sensor 2

Higher than 57 deg.F (32 deg.C) | Higher than 57 deg.F (32 deg.C) | Normal | Normal | Failure

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Failure | Normal | Normal

Lower than -43 deg.F (-24 deg.C) | Failure | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Higher than 57 deg.F (32 deg.C) | Normal | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Normal | Normal | Normal

From -44 deg.F (-25 deg.C) to -108 deg.F (-60 deg.C) | Normal | Failure | Normal

Suspended****

Lower than -108 deg.F (-60 deg.C) | Normal | Failure | Normal

Lower than -43 deg.F (-24 deg.C) | Higher than 57 deg.F (32 deg.C) | Failure | Failure | Normal

From -43 deg.F (-24 deg.C) to 57 deg.F (32 deg.C) | Failure | Normal | Normal

Lower than -43 deg.F (-24 deg.C) | Normal | Normal | Failure

*: [ECT SENSOR 1]

**: [ECT SENSOR 2]

***: [IAT Sensor (1)]

****: Malfunction judgment is suspended because the cooled air introduced after engine start lowers the intake air temperature; the ambient temperature condition does not stay equal.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- ECT sensor 1 failure

- ECT sensor 2 failure

- IAT sensor 1 failure

- Engine block heater attachment (non-genuine part)

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode and wait at least 6 hours.

- Start the engine, and let it idle for at least 10 seconds.

- Do not use an engine block heater because the engine coolant temperature will not stay equal during engine stop.

- When freeze data is stored, test the vehicle under an ambient temperature close to the intake air temperature in the freeze data.

- When an ambient temperature extremely changes, malfunction judgment may not execute. Avoid extreme temperature changing condition after or before engine start. (When the vehicle is parked in the garage, open the shutter to introduce outside air; then start the engine.)

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5932: DTC P2184, P2185 (K20C1) (2017 2018 2019)

- Title: DTC P2184, P2185 (K20C1) (2017 2018 2019)
- Source path: `pages\7062.html`
- Chunk ID: `chunk_59fd98b898d3`
- Images: `images\GHH403512.jpeg`, `images\GHH403513.jpeg`
- Duplicate sources: `pages\8649.html`, `pages\22825.html`, `pages\21238.html`

### Full Text

````text
# DTC P2184, P2185 (K20C1) (2017 2018 2019)

DTC P2184: Engine Coolant Temperature (ECT) Sensor 2 Circuit Low Voltage

DTC P2185: Engine Coolant Temperature (ECT) Sensor 2 Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the ECT sensor 2 output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2184

The ECT sensor 2 output voltage [ECT Sensor 2] is less than 0.047607 V for at least 0.5 second.

DTC: P2185

The ECT sensor 2 output voltage [ECT Sensor 2] is greater than 4.957275 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2184

- ECT sensor 2 TW2 line short to ground

DTC: P2185

- ECT sensor 2 TW2 line short to power

- ECT sensor 2 TW2 line open

Common

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5933: DTC P2184, P2185 (K20C1) (2019 2020 2021)

- Title: DTC P2184, P2185 (K20C1) (2019 2020 2021)
- Source path: `pages\7063.html`
- Chunk ID: `chunk_505a6782f0f7`
- Images: `images\GHH403514.jpeg`, `images\GHH403515.jpeg`
- Duplicate sources: `pages\8650.html`, `pages\22826.html`, `pages\21239.html`

### Full Text

````text
# DTC P2184, P2185 (K20C1) (2019 2020 2021)

DTC P2184: Engine Coolant Temperature (ECT) Sensor 2 Circuit Low Voltage

DTC P2185: Engine Coolant Temperature (ECT) Sensor 2 Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors engine coolant temperature (ECT) sensor 2 for electrical malfunctions. ECT sensor 2 is a thermistor that detects engine coolant temperature at radiator outlet, which used in thermal management as engine coolant temperature upstream the engine. The ECT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the engine coolant temperature decreases. The output voltage is continuously monitored against minimum and maximum thresholds. If the ECT sensor 2 output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2184

The ECT sensor 2 output voltage [ECT Sensor 2] is less than 0.05 V for at least 0.5 second.

DTC: P2185

The ECT sensor 2 output voltage [ECT Sensor 2] is greater than 4.96 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2184

- ECT sensor 2 TW2 line short to ground

DTC: P2185

- ECT sensor 2 TW2 line short to power

- ECT sensor 2 TW2 line open

- ECT sensor 2 SG line open

Common

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5934: DTC P2184, P2185 (K20C2)

- Title: DTC P2184, P2185 (K20C2)
- Source path: `pages\7064.html`
- Chunk ID: `chunk_eb26c13483ed`
- Images: `images\GHH403516.jpeg`, `images\GHH403517.jpeg`
- Duplicate sources: `pages\8651.html`, `pages\22827.html`, `pages\21240.html`

### Full Text

````text
# DTC P2184, P2185 (K20C2)

DTC P2184: Engine Coolant Temperature (ECT) Sensor 2 Circuit Low Voltage

DTC P2185: Engine Coolant Temperature (ECT) Sensor 2 Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Engine coolant temperature (ECT) sensor 2 is a thermistor attached to the radiator. The powertrain control module (PCM) applies voltage (about 5 V) to the TW2 signal circuit through a pull-up resistor. As the engine coolant temperature cools, ECT sensor 2 resistance increases, and the PCM detects a high signal voltage. As the engine coolant warms, the sensor resistance decreases, and the PCM detects a low signal voltage. If the ECT sensor 2 output voltage is a set value when the engine coolant temperature is high or low, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2184

The ECT sensor 2 output voltage [ECT SENSOR 2] is 0.08 V or less for at least 2 seconds.

DTC: P2185

The ECT sensor 2 output voltage [ECT SENSOR 2] is 4.92 V or more for at least 2 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2184

- ECT sensor 2 TW2 line short to ground

DTC: P2185

- ECT sensor 2 TW2 line open

- ECT sensor 2 SG line open

Common

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5935: DTC P2184, P2185 (L15B7/L15BA/L15BY)

- Title: DTC P2184, P2185 (L15B7/L15BA/L15BY)
- Source path: `pages\7065.html`
- Chunk ID: `chunk_7ce7e38850c2`
- Images: `images\GHH403518.jpeg`, `images\GHH403519.jpeg`
- Duplicate sources: `pages\8652.html`, `pages\22828.html`, `pages\21241.html`

### Full Text

````text
# DTC P2184, P2185 (L15B7/L15BA/L15BY)

DTC P2184: Engine Coolant Temperature (ECT) Sensor 2 Circuit Low Voltage

DTC P2185: Engine Coolant Temperature (ECT) Sensor 2 Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Engine coolant temperature (ECT) sensor 2 is a thermistor attached to the radiator. The powertrain control module (PCM) applies voltage (about 5 V) to the TW2 signal circuit through a pull-up resistor. As the engine coolant temperature cools, ECT sensor 2 resistance increases, and the PCM detects a high signal voltage. As the engine coolant warms, the sensor resistance decreases, and the PCM detects a low signal voltage. If the ECT sensor 2 output voltage is a set value when the engine coolant temperature is high or low, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2184

The ECT sensor 2 output voltage [ECT SENSOR 2] is 0.08 V or less for at least 2 seconds.

DTC: P2185

The ECT sensor 2 output voltage [ECT SENSOR 2] is 4.92 V or more for at least 2 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2184

- ECT sensor 2 TW2 line short to ground

DTC: P2185

- ECT sensor 2 TW2 line open

- ECT sensor 2 SG line open

Common

- ECT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5936: DTC P2187 (L15B7/L15BA)

- Title: DTC P2187 (L15B7/L15BA)
- Source path: `pages\7066.html`
- Chunk ID: `chunk_29e54443aa3c`
- Images: `images\GHH403520.jpeg`, `images\GHH403521.jpeg`, `images\GHH403522.jpeg`
- Duplicate sources: `pages\8653.html`, `pages\22829.html`, `pages\21242.html`

### Full Text

````text
# DTC P2187 (L15B7/L15BA)

DTC P2187: Fuel System Too Lean at Idle

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions.In case the breather pipe is disconnected, air amount at the mass airflow (MAF) sensor decreases and basic fuel amount decreases; as a result, fuel injection quantity correction coefficient becomes larger to compensate the gap. This condition could be seen prominently at low load which the intake air amount is small.The detection of breather pipe disconnection is done by monitoring the gap which is determined by fuel injection quantity correction coefficient average during idle and continuously updating fuel injection quantity correction coefficient.If the fuel injection quantity correction coefficient exceeds a threshold value, the PCM detects a malfunction and stores a DTC.The purge is stopped by fuel injection quantity correction coefficient to exclude the influence of purging during the detection.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Every 7.0 seconds

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 18 deg.F (-7 deg.C) | -

MAP value [MAP SENSOR] | 22 kPa (160 mmHg, 6.3 inHg) | -

Intake air amount | - | 5.0 g/second (0.17 oz/second)

Fuel feedback | Closed loop

Monitoring priority | P0455, P0456

[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is 1.33 (+33 %) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Fuel injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- MAF sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

- Breather pipe disconnection

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) for at least 15 minutes, and watch the long term fuel trim. If the long term fuel trim stays at about 1.0, the vehicle is OK or it is a very minor problem. If a significant fault is still present, the long term fuel trim will move up or down while driving.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- After clearing the DTC by disconnecting the 12 volt battery or using the scan tool, drive at steady speed between 15 - 55 mph (25 - 88 km/h) for at least 40 minutes to allow time for long term fuel trim to recover.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5937: DTC P2187 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2187 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7067.html`
- Chunk ID: `chunk_c7043fb60741`
- Images: `images\GHH403523.jpeg`, `images\GHH403524.jpeg`, `images\GHH403525.jpeg`
- Duplicate sources: `pages\8654.html`, `pages\22830.html`, `pages\21243.html`

### Full Text

````text
# DTC P2187 (Si) (2017 2018 2019 2020 2021)

DTC P2187: Fuel System Too Lean at Idle

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions.In case the breather pipe is disconnected, air amount at the mass airflow (MAF) sensor decreases and basic fuel amount decreases; as a result, fuel injection quantity correction coefficient becomes larger to compensate the gap. This condition could be seen prominently at low load which the intake air amount is small.The detection of breather pipe disconnection is done by monitoring the gap which is determined by fuel injection quantity correction coefficient average during idle and continuously updating fuel injection quantity correction coefficient.If the fuel injection quantity correction coefficient exceeds a threshold value, the PCM detects a malfunction and stores a DTC.The purge is stopped by fuel injection quantity correction coefficient to exclude the influence of purging during the detection.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Every 3.0 seconds

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 18 deg.F (-7 deg.C) | -

MAP value [MAP SENSOR] | 16 kPa (120 mmHg, 4.8 inHg) | -

Intake air amount | - | 4.0 g/second (0.14 oz/second)

Fuel feedback | Closed loop

Monitoring priority | P0455, P0456

[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is 1.33 (+33 %) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Fuel injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- MAF sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

- Breather pipe disconnection

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (25 - 120 km/h) for at least 15 minutes, and watch the long term fuel trim. If the long term fuel trim stays at about 1.0, the vehicle is OK or it is a very minor problem. If a significant fault is still present, the long term fuel trim will move up or down while driving.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- After clearing the DTC by disconnecting the 12 volt battery or using the scan tool, drive at steady speed between 15 - 55 mph (25 - 88 km/h) for at least 40 minutes to allow time for long term fuel trim to recover.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5938: DTC P2195 (K20C1) (2017 2018 2019)

- Title: DTC P2195 (K20C1) (2017 2018 2019)
- Source path: `pages\7068.html`
- Chunk ID: `chunk_b0bb2068f2fa`
- Images: `images\GHH403526.jpeg`, `images\GHH403527.jpeg`
- Duplicate sources: `pages\8655.html`, `pages\22831.html`, `pages\21244.html`

### Full Text

````text
# DTC P2195 (K20C1) (2017 2018 2019)

DTC P2195: Air/Fuel Ratio (A/F) Sensor (Bank 1, Sensor 1) Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Detection item 1

The powertrain control module (PCM) monitors the air/fuel ratio (A/F) sensor (sensor 1) lambda signal for plausibility. If all operating conditions are fulfilled, the actual lambda value is continuously monitored against calibrated threshold. If the lambda value is too high for a calibrated amount of time, the PCM detects a malfunction and stores a DTC. To avoid a fault detection caused by empty fuel tank, when the lambda signal can show a mixture enleanment due to insufficient fuel supply, the additional confirmation time is applied in case of low fuel level in fuel tank.

Detection item 2

The PCM monitors the offset of the air/fuel ratio (A/F) sensor (sensor 1) signal. The test is performed by monitoring the fuel trim control of the secondary heated oxygen sensor (secondary HO2S (sensor 2)). If there is an air/fuel ratio offset measured by the secondary HO2S (sensor 2), the secondary HO2S (sensor 2) fuel trim is used to correct this offset back to the commanded air/fuel ratio. If the offset is present for an extended time, the secondary HO2S (sensor 2) fuel trim is stored as the A/F sensor (sensor 1) offset adaptation. There are two ways that the A/F sensor (sensor 1) offset is adapted. If the secondary HO2S (sensor 2) fuel trim has a small deviation, then the A/F sensor (sensor 1) offset is adapted slowly. If the secondary HO2S (sensor 2) fuel trim has a large deviation, the A/F sensor (sensor 1) offset is adapted faster. If the adapted offset of the A/F sensor (sensor 1) sensor is too large, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Detection item 1

Execution | Continuous

Sequence | None

Duration | 10 seconds or more*, 10 minutes 10 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Fuel tank not empty**: Fuel tank empty

Detection item 2

Execution | Continuous

Sequence | None

Duration | 1 minute 30 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions (Detection item 1)

Condition | Minimum | Maximum

Lambda set point | - | 1.6

A/F sensor (sensor 1) heater temperature | 1, 328 deg.F (720 deg.C) | -

Other | Other than during fuel cut-off operation

Enable Conditions (Detection item 2)

Slow offset adaptation

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 400 rpm | 3, 000 rpm

Charging efficiency | 20.3 % - 99.8 % | 0 % - 69.8 %

Fuel feedback | Closed loop***

Other | Evaporative emission (EVAP) system monitor is not active

***: For at least 300 g (10.59 oz) of integrated amount of exhaust mass flow[ ]: HDS Parameter

Fast offset adaptation

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 104 deg.F (40 deg.C) | -

Engine speed [Engine Speed]**** | 1, 000 rpm | -

Exhaust gas mass flow***** | 25 kg/h (56 lbs/h) | 200 kg/h (440 lbs/h)

Charging efficiency | 0 % | -

Fuel feedback | Closed loop

Other | No significant load changes

Other than during fuel cut-off operation

Misfire rate is not exceeding

Evaporative emission (EVAP) system monitor is not active

****: For at least 100 g (3.53 oz) of integrated amount of exhaust gas mass flow

*****: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Detection item 1

The actual lambda value is greater than 12 for at least 10 seconds* (10 minutes 10 seconds)**.

Detection item 2

Lambda offset is greater than 0.1

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) not mounted

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

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory.
````

## Chunk 5939: DTC P2195 (K20C1) (2017 2018 2019)

- Title: DTC P2195 (K20C1) (2017 2018 2019)
- Source path: `pages\7068.html`
- Chunk ID: `chunk_168b432df262`
- Images: `images\GHH403526.jpeg`, `images\GHH403527.jpeg`
- Duplicate sources: `pages\8655.html`, `pages\22831.html`, `pages\21244.html`

### Full Text

````text
offset is greater than 0.1

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) not mounted

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

## Chunk 5940: DTC P2195 (K20C1) (2019 2020 2021)

- Title: DTC P2195 (K20C1) (2019 2020 2021)
- Source path: `pages\7069.html`
- Chunk ID: `chunk_03f3dbfa2aee`
- Images: `images\GHH403528.jpeg`, `images\GHH403529.jpeg`
- Duplicate sources: `pages\8656.html`, `pages\22832.html`, `pages\21245.html`

### Full Text

````text
# DTC P2195 (K20C1) (2019 2020 2021)

DTC P2195: Air/Fuel Ratio (A/F) Sensor (Bank 1, Sensor 1) Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Detection item 1

The powertrain control module (PCM) monitors the air/fuel ratio (A/F) sensor (sensor 1) lambda signal for plausibility. If all operating conditions are fulfilled, the actual lambda value is continuously monitored against calibrated threshold. If the lambda value is too high for a calibrated amount of time, the PCM detects a malfunction and stores a DTC. To avoid a fault detection caused by empty fuel tank, when the lambda signal can show a mixture enleanment due to insufficient fuel supply, the additional confirmation time is applied in case of low fuel level in fuel tank.

Detection item 2

The PCM monitors the offset of the air/fuel ratio (A/F) sensor (sensor 1) signal. The test is performed by monitoring the fuel trim control of the secondary heated oxygen sensor (secondary HO2S (sensor 2)). If there is an air/fuel ratio offset measured by the secondary HO2S (sensor 2), the secondary HO2S (sensor 2) fuel trim is used to correct this offset back to the commanded air/fuel ratio. If the offset is present for an extended time, the secondary HO2S (sensor 2) fuel trim is stored as the A/F sensor (sensor 1) offset adaptation. There are two ways that the A/F sensor (sensor 1) offset is adapted. If the secondary HO2S (sensor 2) fuel trim has a small deviation, then the A/F sensor (sensor 1) offset is adapted slowly. If the secondary HO2S (sensor 2) fuel trim has a large deviation, the A/F sensor (sensor 1) offset is adapted faster. If the adapted offset of the A/F sensor (sensor 1) sensor is too large, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Detection item 1

Execution | Continuous

Sequence | None

Duration | 10 seconds or more*, 10 minutes 10 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Fuel tank not empty**: Fuel tank empty

Detection item 2

Execution | Multiple

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions (Detection item 1)

Condition | Minimum | Maximum

Lambda set point | - | 1.6

A/F sensor (sensor 1) heater temperature | 1, 327.99 deg.F (719.99 deg.C) | -

Fuel level* | 6 L (1.6 US gal) | -

Fuel level** | - | 6 L (1.6 US gal)

Other | Other than during fuel cut-off operation

Enable Conditions (Detection item 2)

Slow offset adaptation

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 400 rpm | 3, 000 rpm

Charging efficiency | 20.3 % - 99.8 % | 0 % - 69.8 %

Fuel feedback | Closed loop***

Other | Evaporative emission (EVAP) system monitor is not active

***: For at least 300 g (10.59 oz) of integrated amount of exhaust mass flow[ ]: HDS Parameter

Fast offset adaptation

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 104 deg.F (40 deg.C) | -

Engine speed [Engine Speed]**** | 1, 000 rpm | -

Exhaust gas mass flow | 25 kg/h (56 lbs/h) | 200 kg/h (440 lbs/h)

****: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Condition | Minimum | Maximum

Charging efficiency | 13 % - 22 % | -

Fuel feedback | Closed loop

Other | No significant load changes

Other than during fuel cut-off operation

Misfire rate is not exceeding

Evaporative emission (EVAP) system monitor is not active

****: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Detection item 1

The actual lambda value is greater than 12 for at least 10 seconds* (10 minutes 10 seconds)**.

Detection item 2

Lambda offset is greater than 0.1.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) not mounted

- A/F sensor (sensor 1) failure

- Exhaust system leak

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at constant speed with part load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC
````

## Chunk 5941: DTC P2195 (K20C1) (2019 2020 2021)

- Title: DTC P2195 (K20C1) (2019 2020 2021)
- Source path: `pages\7069.html`
- Chunk ID: `chunk_f61b87c9abd9`
- Images: `images\GHH403528.jpeg`, `images\GHH403529.jpeg`
- Duplicate sources: `pages\8656.html`, `pages\22832.html`, `pages\21245.html`

### Full Text

````text
1

The actual lambda value is greater than 12 for at least 10 seconds* (10 minutes 10 seconds)**.

Detection item 2

Lambda offset is greater than 0.1.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) not mounted

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

## Chunk 5942: DTC P2195 (K20C2)

- Title: DTC P2195 (K20C2)
- Source path: `pages\7070.html`
- Chunk ID: `chunk_d4dede8de6d5`
- Images: `images\GHH403530.jpeg`
- Duplicate sources: `pages\8657.html`, `pages\22833.html`, `pages\21246.html`

### Full Text

````text
# DTC P2195 (K20C2)

DTC P2195: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

When the air/fuel ratio (A/F) sensor (sensor 1) is properly connected to the engine wire harness, but it is not installed in the exhaust pipe, the feedback is not done properly even if the A/F sensor (sensor 1) is active after starting the engine. Thus, the exhaust emissions increase. When the A/F sensor (sensor 1) output stays out of the normal range after the A/F sensor (sensor 1) becomes active, the powertrain control module (PCM) detects that the A/F sensor (sensor 1) is not properly installed and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 7.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Fuel feedback | Other than during fuel cut-off operation

Malfunction Threshold

The A/F sensor (sensor 1) output voltage is 3.28 V or more for at least 7.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) heater failure

- A/F sensor (sensor 1) element failure

- Out of fuel

Confirmation Procedure

Operating Condition

Start the engine, and let it idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5943: DTC P2195 (Without XM)

- Title: DTC P2195 (Without XM)
- Source path: `pages\7071.html`
- Chunk ID: `chunk_6c17cfde240f`
- Images: `images\GHH403531.jpeg`
- Duplicate sources: `pages\8658.html`, `pages\22834.html`, `pages\21247.html`

### Full Text

````text
# DTC P2195 (Without XM)

DTC P2195: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

When the air/fuel ratio (A/F) sensor (sensor 1) is properly connected to the engine wire harness, but it is not installed in the exhaust pipe, the feedback is not done properly even if the A/F sensor (sensor 1) is active after starting the engine. Thus, the exhaust emissions increase. When the A/F sensor (sensor 1) output stays out of the normal range after the A/F sensor (sensor 1) becomes active, the powertrain control module (PCM) detects that the A/F sensor (sensor 1) is not properly installed and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 7.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Fuel feedback | Other than during fuel cut-off operation

Malfunction Threshold

The A/F sensor (sensor 1) output voltage is 3.28 V or more for at least 7.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) heater failure

- A/F sensor (sensor 1) element failure

- Out of fuel

Confirmation Procedure

Operating Condition

Start the engine, and let it idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5944: DTC P2196 (K20C1) (2017 2018 2019)

- Title: DTC P2196 (K20C1) (2017 2018 2019)
- Source path: `pages\7072.html`
- Chunk ID: `chunk_7768678ac546`
- Images: `images\GHH403532.jpeg`
- Duplicate sources: `pages\8659.html`, `pages\22835.html`, `pages\21248.html`

### Full Text

````text
# DTC P2196 (K20C1) (2017 2018 2019)

DTC P2196: O2 Sensor Signal Biased/Stuck Rich

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

Evaporative emission (EVAP) system monitor is not active

**: For at least 100 g (3.53 oz) of integrated amount of exhaust gas mass flow

***: For at least 80 g (2.83 oz) - 200 g (7.06 oz) of integrated amount of exhaust gas mass flow

Malfunction Threshold

Lambda offset is less than -0.1.

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

## Chunk 5945: DTC P2196 (K20C1) (2019 2020 2021)

- Title: DTC P2196 (K20C1) (2019 2020 2021)
- Source path: `pages\7073.html`
- Chunk ID: `chunk_04fed0af7778`
- Images: `images\GHH403533.jpeg`
- Duplicate sources: `pages\8660.html`, `pages\22836.html`, `pages\21249.html`

### Full Text

````text
# DTC P2196 (K20C1) (2019 2020 2021)

DTC P2196: O2 Sensor Signal Biased/Stuck Rich

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

Lambda offset is less than -0.1.

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

## Chunk 5946: DTC P2199 (K20C1) (2017 2018 2019)

- Title: DTC P2199 (K20C1) (2017 2018 2019)
- Source path: `pages\7074.html`
- Chunk ID: `chunk_fd8a45eec9c4`
- Images: `images\GHH403534.jpeg`, `images\GHH403535.jpeg`
- Duplicate sources: `pages\8661.html`, `pages\22837.html`, `pages\21250.html`

### Full Text

````text
# DTC P2199 (K20C1) (2017 2018 2019)

DTC P2199: Intake Air Temperature (IAT) Sensor 1-2 Incorrect Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors intake air temperature (IAT) sensor 2 for rationality malfunctions. IAT sensor 2 is a thermistor that detects intake air temperature, which is utilized for air/fuel ratio feedback control to compensate for the atmospheric density fluctuations that accompany changes in intake air temperature. The IAT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the intake air temperature decreases. The temperature value, linearized over sensor characteristic line, is monitored at cold start against the mean value of all temperature sensors. If the difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2 minutes or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 7.5 - 9.5 hours* | -

State of the engine | Running

*: Depending on engine off temperature

Malfunction Threshold

The difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 17.7 deg.F (9.8 deg.C) for at least 2 minutes.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- IAT sensor 2 failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine and drive the vehicle for at least 2 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5947: DTC P2199 (K20C1) (2019)

- Title: DTC P2199 (K20C1) (2019)
- Source path: `pages\7075.html`
- Chunk ID: `chunk_df9fca9463ff`
- Images: `images\GHH403536.jpeg`
- Duplicate sources: `pages\8662.html`, `pages\22838.html`, `pages\21251.html`

### Full Text

````text
# DTC P2199 (K20C1) (2019)

DTC P2199: Intake Air Temperature (IAT) Sensor 1-2 Incorrect Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors intake air temperature (IAT) sensor 2 for rationality malfunctions. IAT sensor 2 is a thermistor that detects intake air temperature, which is utilized for air/fuel ratio feedback control to compensate for the atmospheric density fluctuations that accompany changes in intake air temperature. The IAT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the intake air temperature decreases. The temperature value, linearized over sensor characteristic line, is monitored at cold start against the mean value of all temperature sensors. If the difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 6 hours | -

Vehicle | ON mode

Malfunction Threshold

The difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- IAT sensor 2 TA line short to power

- IAT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5948: DTC P2199 (K20C1) (2020 2021)

- Title: DTC P2199 (K20C1) (2020 2021)
- Source path: `pages\7076.html`
- Chunk ID: `chunk_814736dc7dc0`
- Images: `images\GHH403537.jpeg`
- Duplicate sources: `pages\8663.html`, `pages\22839.html`, `pages\21252.html`

### Full Text

````text
# DTC P2199 (K20C1) (2020 2021)

DTC P2199: Intake Air Temperature (IAT) Sensor 1-2 Incorrect Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors intake air temperature (IAT) sensor 2 for rationality malfunctions. IAT sensor 2 is a thermistor that detects intake air temperature, which is utilized for air/fuel ratio feedback control to compensate for the atmospheric density fluctuations that accompany changes in intake air temperature. The IAT sensor 2 resistance varies depending on temperature. The sensor resistance and the output voltage increase as the intake air temperature decreases. The temperature value, linearized over sensor characteristic line, is monitored at cold start against the mean value of all temperature sensors. If the difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 6 hours | -

Vehicle | ON mode

Malfunction Threshold

The difference between the IAT sensor 2 output temperature and mean value of all temperature sensors at cold start is more than 44 deg.F (24 deg.C).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- IAT sensor 2 TA line short to ground

- IAT sensor 2 failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5949: DTC P2199 (Without XM)

- Title: DTC P2199 (Without XM)
- Source path: `pages\7077.html`
- Chunk ID: `chunk_e4c3f47dc207`
- Images: `images\GHH403538.jpeg`
- Duplicate sources: `pages\8664.html`, `pages\22840.html`, `pages\21253.html`

### Full Text

````text
# DTC P2199 (Without XM)

DTC P2199: Intake Air Temperature (IAT) Sensor 1-2 Incorrect Correlation

General Description

Courtesy of HONDA, U.S.A., INC.

Two engine coolant temperature (ECT) sensors and two intake air temperature (IAT) sensors are used by the powertrain control module (PCM). When the engine is stopped and enough time has passed, the temperatures of each sensor will equalize to the ambient temperature. The IAT sensor 2 failure is detected by comparing the sensor value difference of IAT sensor 1 and IAT sensor 2 after ECT sensor 1, ECT sensor 2, and IAT sensor 1 correlations are judged as normal. If the temperature difference between IAT sensor 1 and IAT sensor 2 exceeds a normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P011A, P011B, P2183 are judged as OK

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine off time | 6 hours | -

Malfunction Threshold

The temperature difference between IAT sensor 1 and IAT sensor 2 is 44 deg.F (24 deg.C) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- IAT sensor 2 failure

- Engine off timer failure

- Engine block heater attachment (non-genuine part)

Confirmation Procedure

Operating Condition

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 6 hours.

- Start the engine, and let it idle for at least 10 seconds.

- Do not use an engine block heater because the engine coolant temperature will not stay equal during engine stop.

- When freeze data is stored, test the vehicle under an ambient temperature close to the intake air temperature in the freeze data.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5950: DTC P219C, P219D, P219E, P219F (K20C1) (2017 2018 2019)

- Title: DTC P219C, P219D, P219E, P219F (K20C1) (2017 2018 2019)
- Source path: `pages\7078.html`
- Chunk ID: `chunk_2bec69f074a0`
- Images: `images\GHH403539.jpeg`
- Duplicate sources: `pages\8665.html`, `pages\22841.html`, `pages\21254.html`

### Full Text

````text
# DTC P219C, P219D, P219E, P219F (K20C1) (2017 2018 2019)

DTC P219C: No. 1 Cylinder Air-Fuel Ratio Variation

DTC P219D: No. 2 Cylinder Air-Fuel Ratio Variation

DTC P219E: No. 3 Cylinder Air-Fuel Ratio Variation

DTC P219F: No. 4 Cylinder Air-Fuel Ratio Variation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors an air/fuel ratio imbalance of any cylinder compared with the other cylinders of the engine. A cylinder individual air-fuel ratio imbalance can be caused by a drifting injection valve, an intake air delivery variation, or by uneven internal or external exhaust gas recirculation (EGR) distribution. The air/fuel imbalance monitor utilizes the principle of engine roughness (ER) change during cylinder individual mixture step to lean. Depending on initial cylinder specific air/fuel ratio, the ER change will be unique for each cylinder. If the air/fuel ratio for a single cylinder increases (becomes leaner), the ER will increase. The ER is averaged over a calibrated number of combustion cycles. The difference between the reference ER and the average ER after the lean step is the Delta ER.In order to decrease monitoring time, all cylinders are evaluated in pairs in a defined order by the enleanment and pre-/post-enrichment of the individual cylinders. To provide this, the fuel quantities for each pair of cylinders are modified by trimming the injection times to specific values. The resulting ER change for each cylinder is evaluated. The change of ER depends on the initial air/fuel ratio of the tested cylinder. Depending on whether the cylinder contains excessive fuel or lacks fuel, the change of ER will be either low or high.As shown the figure, after the release of the air/fuel imbalance monitor, the first pair of test cylinders enters the fuel modulation phase. At this step, the fuelling of the cylinder A is shifted towards "lean" and the fuelling of the cylinder B is shifted towards "rich" simultaneously and the cylinder individual ER signals are stored. The stored value of ER of cylinder A is a cylinder A test value and the stored value of ER of cylinder B is a cylinder B reference value. In the next step, cylinder A enters the "reference" phase and cylinder B enters the "enleanment" phase and ER values are stored again. The second stored ER value of cylinder A is a cylinder A reference value and the second stored ER value of cylinder B is a cylinder B test value. The cylinder specific change of engine roughness is calculated based on its captured reference and test values and then stored. To keep an exhaust bank specific air/fuel ratio of 1.0, the cylinders that are not being tested are additionally enriched/leaned off contrary to the enrichment/enleanment of each pair of cylinders. If a cylinder has a large lean imbalance when the air/fuel ratio steps to lean, misfires can occur. If misfires are detected, then the test is repeated with a larger enrichment. If after a calibrated number of repeated tests and misfires can still be detected, the air/fuel imbalance "cylinder too lean" fault is set. If no misfires are detected, the test will be repeated for each pair of cylinders. If the enable conditions are at any time no longer satisfied, the test will be halted. It starts again as soon as the enable conditions are met again for any pair of cylinders for which the test has not yet been completed. When all cylinders have been checked, the cylinder specific changes of ER are converted into cylinder specific air/fuel deviation values by means of defined correlation maps and the bank average air/fuel ratio is calculated. Then the difference between the bank average air/fuel ratio and the cylinder specific air/fuel deviation value of each cylinder is calculated. If the resulting value of cylinder individual air/fuel ratio is outside of a calibrated range, the corresponding cylinder air/fuel ratio imbalance fault will be set.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second

DTC Type | Two drive cycles, MIL on

Enable Conditions

All conditions must be met for at least 15 seconds

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 141.1 deg.F (60.6 deg.C) | -

Engine speed [Engine Speed] | 1, 520 rpm | 3, 000 rpm

Secondary HO2S sensor (sensor 2) voltage [HO2 S2] | 0.14038 V | 1.00098 V

Integrated intake air amount | 3.3013 - 14.0 kg (7.2781 - 30.8 lbs) | -
````

## Chunk 5951: DTC P219C, P219D, P219E, P219F (K20C1) (2017 2018 2019)

- Title: DTC P219C, P219D, P219E, P219F (K20C1) (2017 2018 2019)
- Source path: `pages\7078.html`
- Chunk ID: `chunk_caf41778e29c`
- Images: `images\GHH403539.jpeg`
- Duplicate sources: `pages\8665.html`, `pages\22841.html`, `pages\21254.html`

### Full Text

````text
uel ratio and the cylinder specific air/fuel deviation value of each cylinder is calculated. If the resulting value of cylinder individual air/fuel ratio is outside of a calibrated range, the corresponding cylinder air/fuel ratio imbalance fault will be set.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second

DTC Type | Two drive cycles, MIL on

Enable Conditions

All conditions must be met for at least 15 seconds

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 141.1 deg.F (60.6 deg.C) | -

Engine speed [Engine Speed] | 1, 520 rpm | 3, 000 rpm

Secondary HO2S sensor (sensor 2) voltage [HO2 S2] | 0.14038 V | 1.00098 V

Integrated intake air amount | 3.3013 - 14.0 kg (7.2781 - 30.8 lbs) | -

Charging efficiency | 30 % | 65.3 %

Gear position | 4 th

Fuel feedback | Closed loop

Other | Clutch pedal not pressed

Avoid rough road

Malfunction Threshold

Too rich

- The cylinder individual air/fuel ratio is less than 0.870026 and the adaptation has been repeated for 2 counts.

Too lean

- The cylinder individual air/fuel ratio is greater than 1.120026 and the adaptation has been repeated for 2 counts.

- The test is aborted at least 2 counts due to misfires being detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel injector failure

- Intake manifold leak

- Cam lift failure (wrong cam lift profile for a cylinder)

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle in 4th gear at a steady engine speed [Engine Speed] 1, 520 - 3, 000 rpm with low load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5952: DTC P219C, P219D, P219E, P219F (K20C1) (2019 2020 2021)

- Title: DTC P219C, P219D, P219E, P219F (K20C1) (2019 2020 2021)
- Source path: `pages\7079.html`
- Chunk ID: `chunk_6898b33cc0ab`
- Images: `images\GHH403540.jpeg`
- Duplicate sources: `pages\8666.html`, `pages\22842.html`, `pages\21255.html`

### Full Text

````text
# DTC P219C, P219D, P219E, P219F (K20C1) (2019 2020 2021)

DTC P219C: No. 1 Cylinder Air-Fuel Ratio Variation

DTC P219D: No. 2 Cylinder Air-Fuel Ratio Variation

DTC P219E: No. 3 Cylinder Air-Fuel Ratio Variation

DTC P219F: No. 4 Cylinder Air-Fuel Ratio Variation

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors an air/fuel ratio imbalance of any cylinder compared with the other cylinders of the engine. A cylinder individual air-fuel ratio imbalance can be caused by a drifting injection valve, an intake air delivery variation, or by uneven internal or external exhaust gas recirculation (EGR) distribution. The air/fuel imbalance monitor utilizes the principle of engine roughness (ER) change during cylinder individual mixture step to lean. Depending on initial cylinder specific air/fuel ratio, the ER change will be unique for each cylinder. If the air/fuel ratio for a single cylinder increases (becomes leaner), the ER will increase. The ER is averaged over a calibrated number of combustion cycles. The difference between the reference ER and the average ER after the lean step is the Delta ER.In order to decrease monitoring time, all cylinders are evaluated in pairs in a defined order by the enleanment and pre-/post-enrichment of the individual cylinders. To provide this, the fuel quantities for each pair of cylinders are modified by trimming the injection times to specific values. The resulting ER change for each cylinder is evaluated. The change of ER depends on the initial air/fuel ratio of the tested cylinder. Depending on whether the cylinder contains excessive fuel or lacks fuel, the change of ER will be either low or high.As shown in the figure, after the release of the air/fuel imbalance monitor, the first pair of test cylinders enters the fuel modulation phase. At this step, the fueling of the cylinder A is shifted towards "lean" and the fueling of the cylinder B is shifted towards "rich" simultaneously and the cylinder individual ER signals are stored. The stored value of ER of cylinder A is a cylinder A test value and the stored value of ER of cylinder B is a cylinder B reference value. In the next step, cylinder A enters the "reference" phase and cylinder B enters the "enleanment" phase and ER values are stored again. The second stored ER value of cylinder A is a cylinder A reference value and the second stored ER value of cylinder B is a cylinder B test value. The cylinder specific change of engine roughness is calculated based on its captured reference and test values and then stored. To keep an exhaust bank specific air/fuel ratio of 1.0, the cylinders that are not being tested are additionally enriched/leaned off contrary to the enrichment/enleanment of each pair of cylinders.If no misfires are detected, the test will be repeated for each pair of cylinders. If the enable conditions are at any time no longer satisfied, the test will be halted. It starts again as soon as the enable conditions are met again for any pair of cylinders for which the test has not yet been completed. When all cylinders have been checked, the cylinder specific changes of ER are converted into cylinder specific air/fuel deviation values by means of defined correlation maps and the bank average air/fuel ratio is calculated. Then the difference between the bank average air/fuel ratio and the cylinder specific air/fuel deviation value of each cylinder is calculated. If the resulting value of cylinder individual air/fuel ratio is outside of a calibrated range, the corresponding cylinder air/fuel ratio imbalance fault will be set.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second

DTC Type | Two drive cycles, MIL on

Enable Conditions

All conditions must be met for at least 15 seconds

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140.11 deg.F (60.6 deg.C) | -

Outside air temperature | -54.47 deg.F (-48.04 deg.C) | -

Catalyst temperature | 842.11 deg.F (450.06 deg.C) | 1, 616.1 deg.F (880.06 deg.C)

Engine speed [Engine Speed] | 1, 520 rpm | 3, 000 rpm

Secondary HO2S sensor (sensor 2) voltage [HO2 S2] | 0.08 V | 1 V

Integrated intake air amount | 3.5 - 14 kg (7.8 - 30 lbs) | -

Charging efficiency | 27 % | 65.3 %

Gear position | 5 th

Fuel feedback | Closed loop

Other | Catalyst heating not active

No gear shifting

Commanded lambda value equals to 1

Avoid rough road
````

## Chunk 5953: DTC P219C, P219D, P219E, P219F (K20C1) (2019 2020 2021)

- Title: DTC P219C, P219D, P219E, P219F (K20C1) (2019 2020 2021)
- Source path: `pages\7079.html`
- Chunk ID: `chunk_e46ce7451902`
- Images: `images\GHH403540.jpeg`
- Duplicate sources: `pages\8666.html`, `pages\22842.html`, `pages\21255.html`

### Full Text

````text
nce per driving cycle

Sequence | None

Duration | 0.5 second

DTC Type | Two drive cycles, MIL on

Enable Conditions

All conditions must be met for at least 15 seconds

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140.11 deg.F (60.6 deg.C) | -

Outside air temperature | -54.47 deg.F (-48.04 deg.C) | -

Catalyst temperature | 842.11 deg.F (450.06 deg.C) | 1, 616.1 deg.F (880.06 deg.C)

Engine speed [Engine Speed] | 1, 520 rpm | 3, 000 rpm

Secondary HO2S sensor (sensor 2) voltage [HO2 S2] | 0.08 V | 1 V

Integrated intake air amount | 3.5 - 14 kg (7.8 - 30 lbs) | -

Charging efficiency | 27 % | 65.3 %

Gear position | 5 th

Fuel feedback | Closed loop

Other | Catalyst heating not active

No gear shifting

Commanded lambda value equals to 1

Avoid rough road

Malfunction Threshold

Too rich

- The cylinder individual air/fuel ratio is less than 0.85 and the adaptation has been repeated for 2 counts.

Too lean

- The cylinder individual air/fuel ratio is greater than 1.15 and the adaptation has been repeated for 2 counts.

- The test is aborted at least 2 counts due to misfires being detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel injector failure

- Intake manifold leak

- Cam lift failure (wrong cam lift profile for a cylinder)

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle in 5th gear at a steady engine speed [Engine Speed] 1, 520 - 3, 000 rpm with low load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5954: DTC P219C, P219D, P219E, P219F (K20C2: USA/Canada models)

- Title: DTC P219C, P219D, P219E, P219F (K20C2: USA/Canada models)
- Source path: `pages\7080.html`
- Chunk ID: `chunk_f455ee9e19b3`
- Images: `images\GHH403541.jpeg`, `images\GHH403542.jpeg`, `images\GHH403543.jpeg`
- Duplicate sources: `pages\8667.html`, `pages\22843.html`, `pages\21256.html`

### Full Text

````text
# DTC P219C, P219D, P219E, P219F (K20C2: USA/Canada models)

DTC P219C: No. 1 Cylinder Air-Fuel Ratio Variation

DTC P219D: No. 2 Cylinder Air-Fuel Ratio Variation

DTC P219E: No. 3 Cylinder Air-Fuel Ratio Variation

DTC P219F: No. 4 Cylinder Air-Fuel Ratio Variation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the imbalance amount from the sizes of the 0.5-order and 1.0-order components compared to 0.8-order excitation input by the fuel injection to determine the air/fuel ratio variation between the cylinder. The obtained components are used to learn the fuel coefficient of each cylinder and performs the imbalance reduction control. If it is not possible to suppress the variation even if the imbalance reduction control is performed; resulting the imbalance amount is large and the fuel coefficient is a specified value or more, the PCM detects as imbalance failure.

- When the imbalance amount is a specified value (about 10 %) or less:

- - Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

- - Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

- - Fuel coefficient of each cylinder is lower than the threshold value: Pass

- - Fuel coefficient of each cylinder is lower than the threshold value: Pass

Fuel coefficient of each cylinder is lower than the threshold value: Pass

- When the imbalance amount is a specified value (about 10 %) or more:

- - Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

- - Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

- - Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

- - Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -
````

## Chunk 5955: DTC P219C, P219D, P219E, P219F (K20C2: USA/Canada models)

- Title: DTC P219C, P219D, P219E, P219F (K20C2: USA/Canada models)
- Source path: `pages\7080.html`
- Chunk ID: `chunk_6ef476eaa6ce`
- Images: `images\GHH403541.jpeg`, `images\GHH403542.jpeg`, `images\GHH403543.jpeg`
- Duplicate sources: `pages\8667.html`, `pages\22843.html`, `pages\21256.html`

### Full Text

````text
-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 350 rpm | 3, 400 rpm

Engine speed variation during 1 cycle | - | 50 rpm

Fuel trim | 0.69 | 1.47

Intake air amount variation | - | 0.06 g (0.002 oz)

Fuel feedback | Closed loop at stoichiometric

Monitoring priority | P0133, P0420

[ ]: HDS Parameter

Malfunction Threshold

Fuel correction coefficient of each cylinder is 0.83 or less, or 1.16 or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel injector failure

- Fuel rail clogged

- Intake manifold air leak/clogged

- Cam lift failure

- Ignition system failure

- Engine compression abnormal

- Valve clearance incorrect

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle in 4th gear at a steady engine speed [ENGINE SPEED] 1, 000 - 1, 200 rpm.

- Take 10 - 15 seconds to accelerate up to engine speed [ENGINE SPEED] 3, 400 rpm.

- When the diagnosis does not finish, repeat Driving Pattern steps 2 through 3, five times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5956: DTC P219C, P219D, P219E, P219F (L15B7/L15BA/L15BY)

- Title: DTC P219C, P219D, P219E, P219F (L15B7/L15BA/L15BY)
- Source path: `pages\7081.html`
- Chunk ID: `chunk_586fefe45976`
- Images: `images\GHH403544.jpeg`, `images\GHH403545.jpeg`, `images\GHH403546.jpeg`
- Duplicate sources: `pages\8668.html`, `pages\22844.html`, `pages\21257.html`

### Full Text

````text
# DTC P219C, P219D, P219E, P219F (L15B7/L15BA/L15BY)

DTC P219C: No. 1 Cylinder Air-Fuel Ratio Variation

DTC P219D: No. 2 Cylinder Air-Fuel Ratio Variation

DTC P219E: No. 3 Cylinder Air-Fuel Ratio Variation

DTC P219F: No. 4 Cylinder Air-Fuel Ratio Variation

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the imbalance amount from the sizes of the 0.5-order and 1.0-order components compared to 0.8-order excitation input by the fuel injection to determine the air/fuel ratio variation between the cylinder. The obtained components are used to learn the fuel coefficient of each cylinder and performs the imbalance reduction control. If it is not possible to suppress the variation even if the imbalance reduction control is performed; resulting the imbalance amount is large and the fuel coefficient is a specified value or more, the PCM detects as imbalance failure.

- When the imbalance amount is a specified value (about 10 %) or less:

- - Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

- - Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

Fuel coefficient of each cylinder is higher than the threshold value: Failure on corresponding cylinder

- - Fuel coefficient of each cylinder is lower than the threshold value: Pass

- - Fuel coefficient of each cylinder is lower than the threshold value: Pass

Fuel coefficient of each cylinder is lower than the threshold value: Pass

- When the imbalance amount is a specified value (about 10 %) or more:

- - Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

- - Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

Performs imbalance reduction control and fuel coefficient is higher than the threshold value: Failure on corresponding cylinder

- - Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

- - Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Performs imbalance reduction control and fuel coefficient of each cylinder is lower than the threshold value: Re-performs imbalance reduction control for a specified time and re-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -
````

## Chunk 5957: DTC P219C, P219D, P219E, P219F (L15B7/L15BA/L15BY)

- Title: DTC P219C, P219D, P219E, P219F (L15B7/L15BA/L15BY)
- Source path: `pages\7081.html`
- Chunk ID: `chunk_b92c44f55002`
- Images: `images\GHH403544.jpeg`, `images\GHH403545.jpeg`, `images\GHH403546.jpeg`
- Duplicate sources: `pages\8668.html`, `pages\22844.html`, `pages\21257.html`

### Full Text

````text
-determines the failure by the fuel coefficient of each cylinder. If the imbalance amount is a specified value or less after imbalance reduction control is performed for a specified time, the determination is suspended. If the imbalance amount is a specified value or more after imbalance reduction control is performed for a specified time, the imbalance reduction control is performed again and if the fuel coefficient of each cylinder is higher than a specified value, the PCM detects the failure on corresponding cylinder.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 350 rpm | 3, 400 rpm

Engine speed variation during 1 cycle | - | 80 rpm

Fuel trim | 0.75 | 1.47

Intake air amount variation | - | 0.05 g (0.001 oz)

Fuel feedback | Closed loop at stoichiometric

Monitoring priority | P0133, P0420

[ ]: HDS Parameter

Malfunction Threshold

Fuel correction coefficient of each cylinder is 0.83 or less, or 1.15 or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel injector failure

- Fuel rail clogged

- Intake manifold air leak/clogged

- Cam lift failure

- Ignition system failure

- Engine compression abnormal

- Valve clearance incorrect

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle in 4th gear at a steady engine speed [ENGINE SPEED] 1, 000 - 1, 200 rpm.

- Take 10 - 15 seconds to accelerate up to engine speed [ENGINE SPEED] 3, 400 rpm.

- When the diagnosis does not finish, repeat Driving Pattern steps 2 through 3, five times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5958: DTC P2226 (K20C2)

- Title: DTC P2226 (K20C2)
- Source path: `pages\7082.html`
- Chunk ID: `chunk_9591509a6eee`
- Images: `images\GHH403547.jpeg`
- Duplicate sources: `pages\8669.html`, `pages\22845.html`, `pages\21258.html`

### Full Text

````text
# DTC P2226 (K20C2)

DTC P2226: Barometric Pressure (BARO) Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The BARO sensor output voltage is converted to A/D in the sensor inside, and transmitted to a CPU by serial communication. When the signal is not sent from the BARO sensor or when the signal sent from the BARO sensor is abnormal and this condition continues for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these conditions is met at least 2.0 seconds:

- The PCM does not receive signals.

- The signal sent from the BARO sensor is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- BARO sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5959: DTC P2226 (L15B7/L15BA)

- Title: DTC P2226 (L15B7/L15BA)
- Source path: `pages\7083.html`
- Chunk ID: `chunk_da0106787e7f`
- Images: `images\GHH403548.jpeg`
- Duplicate sources: `pages\8670.html`, `pages\22846.html`, `pages\21259.html`

### Full Text

````text
# DTC P2226 (L15B7/L15BA)

DTC P2226: Barometric Pressure (BARO) Sensor Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The BARO sensor output voltage is converted to A/D in the sensor inside, and transmitted to a CPU by serial communication. When the signal is not sent from the BARO sensor or when the signal sent from the BARO sensor is abnormal and this condition continues for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

One of these conditions is met at least 2.0 seconds:

- The PCM does not receive signals.

- The signal sent from the BARO sensor is abnormal.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- BARO sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5960: DTC P2227 (K20C1) (2017 2018 2019)

- Title: DTC P2227 (K20C1) (2017 2018 2019)
- Source path: `pages\7084.html`
- Chunk ID: `chunk_4d616facc5ce`
- Images: none
- Duplicate sources: `pages\8671.html`, `pages\22847.html`, `pages\21260.html`

### Full Text

````text
# DTC P2227 (K20C1) (2017 2018 2019)

DTC P2227: Barometric Pressure (BARO) Sensor Circuit Out of Range High

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The monitoring function checks the signal of the BARO sensor for implausible values by means of diverse criteria. If the difference between measured ambient pressure and the reference pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Other | BARO sensor, Turbocharger boost sensor, and manifold absolute pressure (MAP) sensor values are valid

Malfunction Threshold

Any of the conditions occurs for at least 2 seconds:

- Difference between measured ambient pressure and the maximum reference pressure is greater than 2.5 kPa (19 mmHg, 0.8 inHg).

- Difference between the minimum reference pressure and the measured ambient pressure is greater than 2.5 kPa (19 mmHg, 0.8 inHg).

- Difference between measured BARO sensor value and its delayed value is greater than 10 kPa (75 mmHg, 3.0 inHg).

- Difference between delayed BARO sensor value and its measured value is greater than 10 kPa (75 mmHg, 3.0 inHg).

- The BARO sensor value is greater than 116.5 kPa (874 mmHg, 34.41 inHg).

- The BARO sensor value is lower than 38.5 kPa (288 mmHg, 11.36 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5961: DTC P2227 (K20C1) (2019 2020 2021)

- Title: DTC P2227 (K20C1) (2019 2020 2021)
- Source path: `pages\7085.html`
- Chunk ID: `chunk_5d0689642f1c`
- Images: none
- Duplicate sources: `pages\8672.html`, `pages\22848.html`, `pages\21261.html`

### Full Text

````text
# DTC P2227 (K20C1) (2019 2020 2021)

DTC P2227: Barometric Pressure (BARO) Sensor Circuit Out of Range High

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The monitoring function checks the signal of the BARO sensor for implausible values by means of diverse criteria. If the difference between measured ambient pressure and the reference pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Continuity check/range check

Condition

Vehicle | ON mode

Other | No plausible errors are received from BARO sensor

Sensor comparison

Condition | Minimum | Maximum

Engine speed [Engine Speed] | - | 400 rpm

Other | Intake manifold pressure is equal to ambient pressure when engine speed [ENGINE SPEED] is 0 rpm

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions occurs:

- Continuity check

- - The absolute difference between measured ambient pressure and its delayed value is more than 10.0 kPa (75 mmHg, 2.96 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg). - The absolute difference between the current and last drive cycle of ambient pressure is more than 255.996 kPa (1, 920.13 mmHg, 75.5957 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg).

- - The absolute difference between measured ambient pressure and its delayed value is more than 10.0 kPa (75 mmHg, 2.96 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg).

The absolute difference between measured ambient pressure and its delayed value is more than 10.0 kPa (75 mmHg, 2.96 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg).

- - The absolute difference between the current and last drive cycle of ambient pressure is more than 255.996 kPa (1, 920.13 mmHg, 75.5957 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg).

The absolute difference between the current and last drive cycle of ambient pressure is more than 255.996 kPa (1, 920.13 mmHg, 75.5957 inHg) and absolute difference between measured ambient pressure and the reference pressure is more than 1.5 kPa (12 mmHg, 0.45 inHg).

- Sensor comparison

- - The absolute difference between the reference pressure and the measured ambient pressure is more than 2.5 kPa (19 mmHg, 0.74 inHg).

- - The absolute difference between the reference pressure and the measured ambient pressure is more than 2.5 kPa (19 mmHg, 0.74 inHg).

The absolute difference between the reference pressure and the measured ambient pressure is more than 2.5 kPa (19 mmHg, 0.74 inHg).

- Range check

- - The ambient air pressure is more than 116.5 kPa (874 mmHg, 34.41 inHg), or less than 38.5 kPa (288 mmHg, 11.36 inHg).

- - The ambient air pressure is more than 116.5 kPa (874 mmHg, 34.41 inHg), or less than 38.5 kPa (288 mmHg, 11.36 inHg).

The ambient air pressure is more than 116.5 kPa (874 mmHg, 34.41 inHg), or less than 38.5 kPa (288 mmHg, 11.36 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5962: DTC P2228 (K20C1) (2017 2018 2019)

- Title: DTC P2228 (K20C1) (2017 2018 2019)
- Source path: `pages\7086.html`
- Chunk ID: `chunk_8c5b3b83621c`
- Images: none
- Duplicate sources: `pages\8673.html`, `pages\22849.html`, `pages\21262.html`

### Full Text

````text
# DTC P2228 (K20C1) (2017 2018 2019)

DTC P2228: Barometric Pressure (BARO) Sensor Circuit Low Voltage

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The PCM monitors the BARO sensor for electrical faults. If a short to ground or short to power is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Other | BARO sensor values are ready to read in the PCM

Malfunction Threshold

The PCM detects a short to ground or information received from the BARO sensor is abnormal for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure (BARO sensor circuit short to ground)

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5963: DTC P2228 (K20C1) (2019 2020 2021)

- Title: DTC P2228 (K20C1) (2019 2020 2021)
- Source path: `pages\7087.html`
- Chunk ID: `chunk_4b08ed172b92`
- Images: none
- Duplicate sources: `pages\8674.html`, `pages\22850.html`, `pages\21263.html`

### Full Text

````text
# DTC P2228 (K20C1) (2019 2020 2021)

DTC P2228: Barometric Pressure (BARO) Sensor Circuit Low Voltage

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The PCM monitors the BARO sensor for electrical faults. If a short to ground is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 0.5 second | -

Malfunction Threshold

The PCM detects a short to ground or information received from the BARO sensor is abnormal for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure (BARO sensor circuit short to ground)

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5964: DTC P2228, P2229 (K20C2)

- Title: DTC P2228, P2229 (K20C2)
- Source path: `pages\7088.html`
- Chunk ID: `chunk_9e95b0133657`
- Images: `images\GHH403549.jpeg`
- Duplicate sources: `pages\8675.html`, `pages\22851.html`, `pages\21264.html`

### Full Text

````text
# DTC P2228, P2229 (K20C2)

DTC P2228: Barometric Pressure (BARO) Sensor Circuit Low Voltage

DTC P2229: Barometric Pressure (BARO) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The BARO sensor output voltage is converted to A/D in the sensor inside, and transmitted to a CPU by serial communication. If the atmospheric pressure value sent from the BARO sensor is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2228

The BARO sensor output value [Baro Sensor] is 44 kPa (336 mmHg, 13.2 inHg) or less for at least 2.0 seconds.

DTC: P2229

The BARO sensor output value [Baro Sensor] is 116 kPa (865 mmHg, 34.1 inHg) or more for at least 2.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- BARO sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5965: DTC P2228, P2229 (L15B7/L15BA)

- Title: DTC P2228, P2229 (L15B7/L15BA)
- Source path: `pages\7089.html`
- Chunk ID: `chunk_b06bc4a3cbf2`
- Images: `images\GHH403550.jpeg`
- Duplicate sources: `pages\8676.html`, `pages\22852.html`, `pages\21265.html`

### Full Text

````text
# DTC P2228, P2229 (L15B7/L15BA)

DTC P2228: Barometric Pressure (BARO) Sensor Circuit Low Voltage

DTC P2229: Barometric Pressure (BARO) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The BARO sensor output voltage is converted to A/D in the sensor inside, and transmitted to a CPU by serial communication. If the atmospheric pressure value sent from the BARO sensor is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2228

The BARO sensor output value [Baro Sensor] is 44 kPa (336 mmHg, 13.2 inHg) or less for at least 2.0 seconds.

DTC: P2229

The BARO sensor output value [Baro Sensor] is 116 kPa (865 mmHg, 34.1 inHg) or more for at least 2.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- BARO sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5966: DTC P2229 (K20C1) (2017 2018 2019)

- Title: DTC P2229 (K20C1) (2017 2018 2019)
- Source path: `pages\7090.html`
- Chunk ID: `chunk_79d95e050166`
- Images: none
- Duplicate sources: `pages\8677.html`, `pages\22853.html`, `pages\21266.html`

### Full Text

````text
# DTC P2229 (K20C1) (2017 2018 2019)

DTC P2229: Barometric Pressure (BARO) Sensor Circuit High Voltage

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The PCM monitors the BARO sensor for electrical faults. If a short to ground or short to power is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Other | BARO sensor values are ready to read in the PCM

Malfunction Threshold

The PCM detects a short to power or information received from the BARO sensor is abnormal for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure (BARO sensor circuit short to power)

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5967: DTC P2229 (K20C1) (2019 2020 2021)

- Title: DTC P2229 (K20C1) (2019 2020 2021)
- Source path: `pages\7091.html`
- Chunk ID: `chunk_6091e326496e`
- Images: none
- Duplicate sources: `pages\8678.html`, `pages\22854.html`, `pages\21267.html`

### Full Text

````text
# DTC P2229 (K20C1) (2019 2020 2021)

DTC P2229: Barometric Pressure (BARO) Sensor Circuit High Voltage

General Description

The barometric pressure (BARO) sensor is built into the powertrain control module (PCM), and it monitors atmospheric pressure. The PCM monitors the BARO sensor for electrical faults. If a short to power is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 0.5 second | -

Malfunction Threshold

The PCM detects a short to power or information received from the BARO sensor is abnormal for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure (BARO sensor circuit short to power)

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5968: DTC P2232 (K20C1) (2017 2018 2019)

- Title: DTC P2232 (K20C1) (2017 2018 2019)
- Source path: `pages\7092.html`
- Chunk ID: `chunk_979475cd6973`
- Images: `images\GHH403551.jpeg`
- Duplicate sources: `pages\8679.html`, `pages\22855.html`, `pages\21268.html`

### Full Text

````text
# DTC P2232 (K20C1) (2017 2018 2019)

DTC P2232: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Out of Range High

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the secondary heated oxygen sensor (secondary HO2S (sensor 2)) circuit for electrical malfunctions. The described circuit check will detect short circuit to ground, short circuit to power, and open circuit failure modes. If the output voltage of the secondary HO2S (sensor 2) difference between actual and last sensor voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.04 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after moisture completely evaporated from exhaust pipe | 15 seconds | -

12 volt battery voltage [Battery] | 10.7 V | -

[ ]: HDS Parameter

Malfunction Threshold

The output voltage of the secondary HO2S (sensor 2) difference between actual and last sensor voltage is greater than 2.001953 V at least 4 times within 0.04 second after the heater is turned off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) SO2HT line short to secondary HO2S (sensor 2) SO2 line

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5969: DTC P2232 (K20C1) (2019 2020 2021)

- Title: DTC P2232 (K20C1) (2019 2020 2021)
- Source path: `pages\7093.html`
- Chunk ID: `chunk_fc7c87d9ca9a`
- Images: `images\GHH403552.jpeg`
- Duplicate sources: `pages\8680.html`, `pages\22856.html`, `pages\21269.html`

### Full Text

````text
# DTC P2232 (K20C1) (2019 2020 2021)

DTC P2232: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Out of Range High

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the secondary heated oxygen sensor (secondary HO2S (sensor 2)) circuit for electrical malfunctions. The described circuit check will detect short circuit to ground, short circuit to power, and open circuit failure modes. If the output voltage of the secondary HO2S (sensor 2) difference between actual and last sensor voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.1 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after moisture completely evaporated from exhaust pipe | 10 seconds | -

12 volt battery voltage [Battery] | 10.7 V | -

[ ]: HDS Parameter

Malfunction Threshold

The output voltage of the secondary HO2S (sensor 2) difference between actual and last sensor voltage is greater than 2 V at least 4 times of heater switch-off event.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) SO2HT line short to secondary HO2S (sensor 2) SO2 line

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5970: DTC P2237 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P2237 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\7094.html`
- Chunk ID: `chunk_95a8564c1f52`
- Images: `images\GHH403553.jpeg`, `images\GHH403554.jpeg`
- Duplicate sources: `pages\8681.html`, `pages\22857.html`, `pages\21270.html`

### Full Text

````text
# DTC P2237 (K20C1) (2017 2018 2019 2020 2021)

DTC P2237: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an open in A/F sensor (sensor 1) circuit (LAF CA line) is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects an open circuit in A/F sensor (sensor 1) LAF CA line for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) LAF CA line open

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5971: DTC P2237 (K20C2)

- Title: DTC P2237 (K20C2)
- Source path: `pages\7095.html`
- Chunk ID: `chunk_568210969dd2`
- Images: `images\GHH403555.jpeg`
- Duplicate sources: `pages\8682.html`, `pages\22858.html`, `pages\21271.html`

### Full Text

````text
# DTC P2237 (K20C2)

DTC P2237: Air/Fuel Ratio (A/F) Sensor (Sensor 1) IP Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the IP terminal voltage is within a specified range when the A/F sensor (sensor 1) pump cell voltage is excessively high, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 15 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The IP terminal voltage is between 1.93 - 2.07 V for at least 15 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) IP line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5972: DTC P2237 (L15B7/L15BA/L15BY)

- Title: DTC P2237 (L15B7/L15BA/L15BY)
- Source path: `pages\7096.html`
- Chunk ID: `chunk_f3f8b906691d`
- Images: `images\GHH403556.jpeg`, `images\GHH403557.jpeg`
- Duplicate sources: `pages\8683.html`, `pages\22859.html`, `pages\21272.html`

### Full Text

````text
# DTC P2237 (L15B7/L15BA/L15BY)

DTC P2237: Air/Fuel Ratio (A/F) Sensor (Sensor 1) IP Circuit High Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the IP terminal voltage is within a specified range when the A/F sensor (sensor 1) pump cell voltage is excessively high, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 15 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The IP terminal voltage is between 1.93 V to 2.07 V for at least 15 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) IP line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5973: DTC P2238 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P2238 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\7097.html`
- Chunk ID: `chunk_1eb041689323`
- Images: `images\GHH403558.jpeg`, `images\GHH403559.jpeg`
- Duplicate sources: `pages\8684.html`, `pages\22860.html`, `pages\21273.html`

### Full Text

````text
# DTC P2238 (K20C1) (2017 2018 2019 2020 2021)

DTC P2238: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If the PCM detects a failure in A/F sensor (sensor 1), a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects a failure in A/F sensor (sensor 1) for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5974: DTC P2238 (K20C2)

- Title: DTC P2238 (K20C2)
- Source path: `pages\7098.html`
- Chunk ID: `chunk_65e80efef32b`
- Images: `images\GHH403560.jpeg`
- Duplicate sources: `pages\8685.html`, `pages\22545.html`, `pages\20958.html`

### Full Text

````text
# DTC P2238 (K20C2)

DTC P2238: Air/Fuel Ratio (A/F) Sensor (Sensor 1) IP Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the IP terminal voltage is a specified voltage when the self-diagnosis function in the PCM detects an abnormal condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- When the element temperature is low before the sensor becomes active: The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects low voltage abnormal for 0.5 second.

The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects low voltage abnormal for 0.5 second.

- When the element temperature is high before the sensor becomes active: The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects short circuit for three times and the heater is stopped for 5 seconds.

The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects short circuit for three times and the heater is stopped for 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) IP line short to ground

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5975: DTC P2238 (L15B7/L15BA/L15BY)

- Title: DTC P2238 (L15B7/L15BA/L15BY)
- Source path: `pages\7099.html`
- Chunk ID: `chunk_d50c18b19ce0`
- Images: `images\GHH403561.jpeg`, `images\GHH403562.jpeg`
- Duplicate sources: `pages\8686.html`, `pages\22546.html`, `pages\20959.html`

### Full Text

````text
# DTC P2238 (L15B7/L15BA/L15BY)

DTC P2238: Air/Fuel Ratio (A/F) Sensor (Sensor 1) IP Circuit Low Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the IP terminal voltage is a specified voltage when the self-diagnosis function in the PCM detects an abnormal condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- When the element temperature is low before the sensor becomes active: The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects low voltage abnormal for 0.5 second.

The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects low voltage abnormal for 0.5 second.

- When the element temperature is high before the sensor becomes active: The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects short circuit for three times and the heater is stopped for 5 seconds.

The IP terminal voltage is 2.0 V or less for at least 5 seconds after the self-diagnosis function in the PCM detects short circuit for three times and the heater is stopped for 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) IP line short to ground

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5976: DTC P2243 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P2243 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\7100.html`
- Chunk ID: `chunk_e389f503bd12`
- Images: `images\GHH403563.jpeg`, `images\GHH403564.jpeg`
- Duplicate sources: `pages\8687.html`, `pages\22547.html`, `pages\20960.html`

### Full Text

````text
# DTC P2243 (K20C1) (2017 2018 2019 2020 2021)

DTC P2243: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VCENT Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an open in A/F sensor (sensor 1) circuit (LAF VN line) is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects an open circuit in A/F sensor (sensor 1) LAF VN line for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) LAF VN line open

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5977: DTC P2243 (K20C2)

- Title: DTC P2243 (K20C2)
- Source path: `pages\7101.html`
- Chunk ID: `chunk_1c975b175d12`
- Images: `images\GHH403565.jpeg`
- Duplicate sources: `pages\8688.html`, `pages\22548.html`, `pages\20961.html`

### Full Text

````text
# DTC P2243 (K20C2)

DTC P2243: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VCENT Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the A/F sensor (sensor 1) element resistance is a specified value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more*, 38 seconds or more**

DTC Type | Two drive cycles, MIL on

*: After the sensor becomes active

**: Before the sensor becomes active

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- The A/F sensor (sensor 1) element resistance is more than 270 Ω for at least 38 seconds**.

- The A/F sensor (sensor 1) element resistance is 270 Ω or less and the self-diagnosis function in the PCM judges as an occurrence of open circuit for at least 5 seconds*.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VCENT line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5978: DTC P2243 (L15B7/L15BA/L15BY)

- Title: DTC P2243 (L15B7/L15BA/L15BY)
- Source path: `pages\7102.html`
- Chunk ID: `chunk_8d6672e99b24`
- Images: `images\GHH403566.jpeg`, `images\GHH403567.jpeg`
- Duplicate sources: `pages\8689.html`, `pages\22549.html`, `pages\20962.html`

### Full Text

````text
# DTC P2243 (L15B7/L15BA/L15BY)

DTC P2243: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VCENT Circuit High Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. If the A/F sensor (sensor 1) element resistance is a specified value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more*, 38 seconds or more**

DTC Type | Two drive cycles, MIL on

*: After the sensor becomes active**: Before the sensor becomes active

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- The A/F sensor (sensor 1) element resistance is more than 270 Ω for at least 38 seconds**.

- The A/F sensor (sensor 1) element resistance is 270 Ω or less and the self-diagnosis function in the PCM judges as an occurrence of open circuit for at least 5 seconds*.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VCENT line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5979: DTC P2245 (K20C2)

- Title: DTC P2245 (K20C2)
- Source path: `pages\7103.html`
- Chunk ID: `chunk_406a84412483`
- Images: `images\GHH403568.jpeg`
- Duplicate sources: `pages\8690.html`, `pages\22550.html`, `pages\20963.html`

### Full Text

````text
# DTC P2245 (K20C2)

DTC P2245: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VCENT Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the self-diagnosis function in the PCM detects a short circuit failure, the heater stops, and if the condition continues for a specified time, the PCM detects VCENT line short to ground and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects VCENT line short to ground after the self-diagnosis function in the PCM judges as an occurrence of short circuit for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VCENT line short to ground

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5980: DTC P2245 (L15B7/L15BA/L15BY)

- Title: DTC P2245 (L15B7/L15BA/L15BY)
- Source path: `pages\7104.html`
- Chunk ID: `chunk_4229de0034b7`
- Images: `images\GHH403569.jpeg`, `images\GHH403570.jpeg`
- Duplicate sources: `pages\8691.html`, `pages\22551.html`, `pages\20964.html`

### Full Text

````text
# DTC P2245 (L15B7/L15BA/L15BY)

DTC P2245: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VCENT Circuit Low Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the self-diagnosis function in the PCM detects a short circuit failure, the heater stops, and if the condition continues for a specified time, the PCM detects VCENT line short to ground and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects VCENT line short to ground after the self-diagnosis function in the PCM judges as an occurrence of short circuit for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VCENT line short to ground

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5981: DTC P2251 (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P2251 (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\7105.html`
- Chunk ID: `chunk_ea776d89f8c1`
- Images: `images\GHH403571.jpeg`, `images\GHH403572.jpeg`
- Duplicate sources: `pages\8692.html`, `pages\22552.html`, `pages\20965.html`

### Full Text

````text
# DTC P2251 (K20C1) (2017 2018 2019 2020 2021)

DTC P2251: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VS Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an open in A/F sensor (sensor 1) circuit (LAF VG line) is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects an open circuit in A/F sensor (sensor 1) LAF VG line for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) LAF VG line open

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5982: DTC P2251 (K20C2)

- Title: DTC P2251 (K20C2)
- Source path: `pages\7106.html`
- Chunk ID: `chunk_9f7b71b67a16`
- Images: `images\GHH403573.jpeg`
- Duplicate sources: `pages\8693.html`, `pages\22553.html`, `pages\20966.html`

### Full Text

````text
# DTC P2251 (K20C2)

DTC P2251: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VS Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the VS voltage is a specified value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 38 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The VS terminal voltage is 3.7 V or more for at least 38 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VS line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5983: DTC P2251 (L15B7/L15BA/L15BY)

- Title: DTC P2251 (L15B7/L15BA/L15BY)
- Source path: `pages\7107.html`
- Chunk ID: `chunk_132faa7e6580`
- Images: `images\GHH403574.jpeg`, `images\GHH403575.jpeg`
- Duplicate sources: `pages\8694.html`, `pages\22554.html`, `pages\20967.html`

### Full Text

````text
# DTC P2251 (L15B7/L15BA/L15BY)

DTC P2251: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VS Circuit High Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the VS voltage is a specified value for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 38 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The VS terminal voltage is 3.7 V or more for at least 38 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

- A/F sensor (sensor 1) VS line open

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5984: DTC P2252 (K20C2)

- Title: DTC P2252 (K20C2)
- Source path: `pages\7108.html`
- Chunk ID: `chunk_5dc2c6bcd625`
- Images: `images\GHH403576.jpeg`
- Duplicate sources: `pages\8695.html`, `pages\22555.html`, `pages\20968.html`

### Full Text

````text
# DTC P2252 (K20C2)

DTC P2252: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VS Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the self-diagnosis function in the PCM detects a short circuit failure, the heater stops, and if the condition continues for a specified time, or if the VS terminal voltage is a specified value after a current is applied to the pump cell for a specified time, the PCM detects VS line short to ground and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- The PCM detects VS line short to ground after the self-diagnosis function in the PCM judges as an occurrence of short circuit for at least 5 seconds.

- The VS terminal voltage is 2.6 V or less after a current is applied to the sensor pump cell for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) VS line short to ground

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5985: DTC P2252 (L15B7/L15BA/L15BY)

- Title: DTC P2252 (L15B7/L15BA/L15BY)
- Source path: `pages\7109.html`
- Chunk ID: `chunk_9c18de8d5eaf`
- Images: `images\GHH403577.jpeg`, `images\GHH403578.jpeg`
- Duplicate sources: `pages\8696.html`, `pages\22556.html`, `pages\20969.html`

### Full Text

````text
# DTC P2252 (L15B7/L15BA/L15BY)

DTC P2252: Air/Fuel Ratio (A/F) Sensor (Sensor 1) VS Circuit Low Voltage

General Description

USA and Canada models

Courtesy of HONDA, U.S.A., INC.

Mexico models

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) is installed in the exhaust manifold and detects oxygen content in the exhaust gas. The A/F sensor (sensor 1) transmits a signal to the powertrain control module (PCM), and the PCM controls fuel injection duration by comparing the target air/fuel ratio with the A/F sensor (sensor 1) signal. When the self-diagnosis function in the PCM detects a short circuit failure, the heater stops, and if the condition continues for a specified time, or if the VS terminal voltage is a specified value after a current is applied to the pump cell for a specified time, the PCM detects VS line short to ground and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 9.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

One of these symptoms occurs:

- The PCM detects VS line short to ground after the self-diagnosis function in the PCM judges as an occurrence of short circuit for at least 5 seconds.

- The VS terminal voltage is 2.6 V or less after a current is applied to the sensor pump cell for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) VS line short to ground

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 2 minutes.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5986: DTC P2261 (K20C1) (2017 2018 2019)

- Title: DTC P2261 (K20C1) (2017 2018 2019)
- Source path: `pages\7110.html`
- Chunk ID: `chunk_dd18b3eb8368`
- Images: `images\GHH403579.jpeg`
- Duplicate sources: `pages\8697.html`, `pages\22557.html`, `pages\20970.html`

### Full Text

````text
# DTC P2261 (K20C1) (2017 2018 2019)

DTC P2261: Turbocharger Bypass Control Valve Stuck Closed

General Description

Courtesy of HONDA, U.S.A., INC.

The turbocharger bypass control solenoid valve is monitored against plausibility error. This check detects turbocharger boost sensor signal with oscillations in order to recognize turbocharger bypass control solenoid valve which does not open. If the turbocharger boost sensor is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.85 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Intake air temperature [IAT Sensor 1] | 59 deg.F (14.991 deg.C) | -

Pressure ratio turbocharger boost sensor to mass airflow (MAF) sensor | 1.02002 - 3.045898 | -

12 volt battery voltage [Battery] | 7.5 V | 16 V

Other | Turbocharger bypass control solenoid valve must be surely opened

No high load requested

[ ]: HDS Parameter

Malfunction Threshold

The pressure oscillations are counted if the pressure of the turbocharger boost sensor is greater than 2 kPa (15.1 mmHg, 0.6 inHg), or less than -2 kPa (-15.1 mmHg, -0.6 inHg). If the counter reaches 7 counts within 0.85 seconds, the PCM stores a DTC.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger bypass control solenoid valve failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5987: DTC P2261 (K20C1) (2019 2020 2021)

- Title: DTC P2261 (K20C1) (2019 2020 2021)
- Source path: `pages\7111.html`
- Chunk ID: `chunk_bcc784d183f5`
- Images: `images\GHH403580.jpeg`
- Duplicate sources: `pages\8698.html`, `pages\22558.html`, `pages\20971.html`

### Full Text

````text
# DTC P2261 (K20C1) (2019 2020 2021)

DTC P2261: Turbocharger Bypass Control Valve Stuck Closed

General Description

Courtesy of HONDA, U.S.A., INC.

The turbocharger bypass control solenoid valve is monitored against plausibility error. This check detects turbocharger boost sensor signal with oscillations in order to recognize turbocharger bypass control solenoid valve which does not open. If the turbocharger boost sensor is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Intake air temperature [IAT Sensor 1] | 58.99 deg.F (14.99 deg.C) | -

Pressure ratio turbocharger boost sensor to mass airflow (MAF) sensor | 1.02 - 3.04 | -

Other | Turbocharger bypass control solenoid valve must be surely opened

No high load requested

[ ]: HDS Parameter

Malfunction Threshold

The pressure oscillations are counted if the pressure of the turbocharger boost sensor is greater than 2 kPa (15.1 mmHg, 0.6 inHg), or less than -2 kPa (-15.1 mmHg, -0.6 inHg). If the counter reaches 7 counts within 0.75 second, the PCM stores a DTC.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger bypass control solenoid valve failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5988: DTC P2270 (K20C1) (2017 2018 2019)

- Title: DTC P2270 (K20C1) (2017 2018 2019)
- Source path: `pages\7112.html`
- Chunk ID: `chunk_eae59aab96f7`
- Images: `images\GHH403581.jpeg`
- Duplicate sources: `pages\8699.html`, `pages\22559.html`, `pages\20972.html`

### Full Text

````text
# DTC P2270 (K20C1) (2017 2018 2019)

DTC P2270: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 120 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Deviation of A/F sensor (sensor 1) heater temperature (commanded and actual) | - | 116.985 deg.F (64.992 deg.C)

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (554 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 4 mph (5 km/h) | -

Charging efficiency | 13.008 % to 16.008 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Canister not purging

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur for at least 120 seconds:

- Lambda request for active test is less than 0.80005 (target rich).

- Integrated exhaust gas mass flow at catalyst input is greater than 0.08 kg (0.2 lbs).

- Maximum secondary HO2S (sensor 2) voltage during lambda shifting to rich is less than 0.749512 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) lean stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5989: DTC P2270 (K20C1) (2019)

- Title: DTC P2270 (K20C1) (2019)
- Source path: `pages\7113.html`
- Chunk ID: `chunk_96eb11843f63`
- Images: `images\GHH403582.jpeg`
- Duplicate sources: `pages\8700.html`, `pages\22560.html`, `pages\20973.html`

### Full Text

````text
# DTC P2270 (K20C1) (2019)

DTC P2270: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Outside air temperature | -54 deg.F (-48 deg.C) | -

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (554 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 0 mph (0 km/h) | -

Relative air charge | 13 % to 22 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Actual secondary HO2S (sensor 2) heater temperature is around set point temperature

Following table A must be met for more than 0.08 kg (0.18 lbs) of integrated exhaust gas mass flow

Canister not purging

Table A

Condition | Minimum | Maximum

Catalyst bed temperature | 842 deg.F (450 deg.C) | 1, 562 deg.F (850 deg.C)

Exhaust gas mass flow | 20 kg/h (44 lbs/h) | 200 kg/h (441 lbs/h)

Commanded lambda | 0.97 | 1.03

Other | Catalyst bed temperature is stable

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur:

- Lambda request for active test (target rich) is 0.80 or less.

- Integrated exhaust gas mass flow at catalyst input after lambda request for active test is 0.08 kg (0.2 lbs) or more.

- Maximum secondary HO2S (sensor 2) voltage is less than 0.75 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) lean stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5990: DTC P2270 (K20C1) (2020 2021)

- Title: DTC P2270 (K20C1) (2020 2021)
- Source path: `pages\7114.html`
- Chunk ID: `chunk_cf56a15dc87a`
- Images: `images\GHH403583.jpeg`
- Duplicate sources: `pages\8701.html`, `pages\22561.html`, `pages\20974.html`

### Full Text

````text
# DTC P2270 (K20C1) (2020 2021)

DTC P2270: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Outside air temperature | -54 deg.F (-48 deg.C) | -

Engine coolant temperature [ECT sensor 1] | -54.47 deg.F (-48.04 deg.C) | -

Catalyst temperature | 842 deg.F (450 deg.C) | -

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (555 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 0 mph (0 km/h) | -

Relative air charge | 13 % to 22 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Actual secondary HO2S (sensor 2) heater temperature is around set point temperature

Following table A must be met for more than 0.08 kg (0.18 lbs) of integrated exhaust gas mass flow

Canister not purging

Table A

Condition | Minimum | Maximum

Catalyst bed temperature | 842 deg.F (450 deg.C) | 1, 562 deg.F (850 deg.C)

Exhaust gas mass flow | 20 kg/h (44 lbs/h) | 200 kg/h (441 lbs/h)

Commanded lambda | 0.97 | 1.03

Other | Catalyst bed temperature is stable

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur:

- Lambda request for active test (target rich) is 0.80 or less.

- Integrated exhaust gas mass flow at catalyst input after lambda request for active test is 0.08 kg (0.2 lbs) or more.

- Maximum secondary HO2S (sensor 2) voltage is less than 0.75 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) lean stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5991: DTC P2270 (K20C2)

- Title: DTC P2270 (K20C2)
- Source path: `pages\7115.html`
- Chunk ID: `chunk_b557a5dc788e`
- Images: `images\GHH403584.jpeg`, `images\GHH403585.jpeg`
- Duplicate sources: `pages\8702.html`, `pages\22562.html`, `pages\20975.html`

### Full Text

````text
# DTC P2270 (K20C2)

DTC P2270: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The secondary heated oxygen sensor (secondary HO2S (sensor 2)) detects the oxygen content in the exhaust gas downstream of the three way catalytic converter (TWC) during stoichiometric air/fuel ratio feedback control. The powertrain control module (PCM) controls the air/fuel ratio from the air/fuel ratio (A/F) sensor (sensor 1) output voltage to optimize the TWC efficiency. When power is applied to the secondary HO2S (sensor 2) heater, if the secondary HO2S (sensor 2) output continues to be low (lean) during feedback control, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 30 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time that secondary HO2S activity is not monitored after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Fuel trim | 0.69 | 1.47

Fuel feedback | Closed loop

Other | Cruise load or more

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) output voltage [HO2S S2] is 0.05 V or less for at least 30 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) lean stuck

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- Drive immediately at a steady engine speed [ENGINE SPEED] between 1, 500 - 3, 000 rpm for at least 30 seconds.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5992: DTC P2270 (L15B7/L15BA)

- Title: DTC P2270 (L15B7/L15BA)
- Source path: `pages\7116.html`
- Chunk ID: `chunk_a28b1143b2a9`
- Images: `images\GHH403586.jpeg`, `images\GHH403587.jpeg`
- Duplicate sources: `pages\8703.html`, `pages\22563.html`, `pages\20976.html`

### Full Text

````text
# DTC P2270 (L15B7/L15BA)

DTC P2270: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The secondary heated oxygen sensor (secondary HO2S (sensor 2)) detects the oxygen content in the exhaust gas downstream of the three way catalytic converter (TWC) during stoichiometric air/fuel ratio feedback control. The powertrain control module (PCM) controls the air/fuel ratio from the air/fuel ratio (A/F) sensor (sensor 1) output voltage to optimize the TWC efficiency. When power is applied to the secondary HO2S (sensor 2) heater, if the secondary HO2S (sensor 2) output continues to be low (lean) during feedback control, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 30 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time that secondary HO2S activity is not monitored after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Fuel trim | 0.75 | 1.47

Fuel feedback | Closed loop

Other | Cruise load or more

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) output voltage [HO2S S2] is 0.05 V or less for at least 30 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) lean side stuck

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- Drive immediately at a steady engine speed [ENGINE SPEED] between 1, 500 - 3, 000 rpm for at least 30 seconds.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5993: DTC P2271 (K20C1) (2017 2018 2019)

- Title: DTC P2271 (K20C1) (2017 2018 2019)
- Source path: `pages\7117.html`
- Chunk ID: `chunk_86957aa1b410`
- Images: `images\GHH403588.jpeg`
- Duplicate sources: `pages\8704.html`, `pages\22564.html`, `pages\20977.html`

### Full Text

````text
# DTC P2271 (K20C1) (2017 2018 2019)

DTC P2271: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 120 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Deviation of A/F sensor (sensor 1) heater temperature (commanded and actual) | - | 116.985 deg.F (64.992 deg.C)

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (554 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 4 mph (5 km/h) | -

Charging efficiency | 13.008 % to 16.008 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Canister not purging

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur for at least 120 seconds:

- Lambda request for active test is greater than 1. 13.

- Integrated exhaust gas mass flow at catalyst input is greater than 0.08 kg (0.2 lbs).

- Minimum secondary HO2S (sensor 2) voltage during lambda shifting to rich is greater than 0.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) rich stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5994: DTC P2271 (K20C1) (2019)

- Title: DTC P2271 (K20C1) (2019)
- Source path: `pages\7118.html`
- Chunk ID: `chunk_e5f549375243`
- Images: `images\GHH403589.jpeg`
- Duplicate sources: `pages\8705.html`, `pages\22565.html`, `pages\20978.html`

### Full Text

````text
# DTC P2271 (K20C1) (2019)

DTC P2271: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Outside air temperature | -54 deg.F (-48 deg.C) | -

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (554 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 0 mph (0 km/h) | -

Relative air charge | 13 % to 22 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Actual secondary HO2S (sensor 2) heater temperature is around set point temperature

Following table A must be met for more than 0.08 kg (0.18 lbs) of integrated exhaust gas mass flow

Canister not purging

Table A

Condition | Minimum | Maximum

Catalyst bed temperature | 842 deg.F (450 deg.C) | 1, 562 deg.F (850 deg.C)

Exhaust gas mass flow | 20 kg/h (44 lbs/h) | 200 kg/h (441 lbs/h)

Commanded lambda | 0.97 | 1.03

Other | Catalyst bed temperature is stable

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur:

- Lambda request for active test (target lean) is 1.13 or more (target lean).

- Integrated exhaust gas mass flow at catalyst input after lambda request for active test is 0.08 kg (0.2 lbs) or more.

- Minimum secondary HO2S (sensor 2) voltage is more than 0.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) rich stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5995: DTC P2271 (K20C1) (2020 2021)

- Title: DTC P2271 (K20C1) (2020 2021)
- Source path: `pages\7119.html`
- Chunk ID: `chunk_849a1884d626`
- Images: `images\GHH403590.jpeg`
- Duplicate sources: `pages\8706.html`, `pages\22566.html`, `pages\20979.html`

### Full Text

````text
# DTC P2271 (K20C1) (2020 2021)

DTC P2271: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit Signal Stuck Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The range check during target rich operation is utilized to provide monitoring of the secondary heated oxygen sensor (secondary HO2S (sensor 2)) in order to detect deterioration of the sensor. During the enrichment of the air/fuel mixture by the active test once the target rich value has been reached, the secondary HO2S (sensor 2) voltage is monitored against rationality threshold. If the secondary HO2S (sensor 2) voltage is a specified value during the enrichment of the air/fuel mixture by the active test, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Time not in fuel cut-off operation | 10 seconds | -

Outside air temperature | -54 deg.F (-48 deg.C) | -

Engine coolant temperature [ECT sensor 1] | -54.47 deg.F (-48.04 deg.C) | -

Catalyst temperature | 842 deg.F (450 deg.C) | -

Engine speed [Engine Speed] | 1, 200 rpm | 4, 520 rpm

Barometric pressure [Baro Sensor] | 739 hPa (555 mmHg, 21.8 inHg) | -

Vehicle speed [Vehicle Speed] | 0 mph (0 km/h) | -

Relative air charge | 13 % to 22 % | -

Other | Exhaust gas mass flow is stable for at least 1 second

Actual secondary HO2S (sensor 2) heater temperature is around set point temperature

Following table A must be met for more than 0.08 kg (0.18 lbs) of integrated exhaust gas mass flow

Canister not purging

Table A

Condition | Minimum | Maximum

Catalyst bed temperature | 842 deg.F (450 deg.C) | 1, 562 deg.F (850 deg.C)

Exhaust gas mass flow | 20 kg/h (44 lbs/h) | 200 kg/h (441 lbs/h)

Commanded lambda | 0.97 | 1.03

Other | Catalyst bed temperature is stable

[ ]: HDS Parameter

Malfunction Threshold

All of the conditions occur:

- Lambda request for active test (target lean) is 1.13 or more (target lean).

- Integrated exhaust gas mass flow at catalyst input after lambda request for active test is 0.08 kg (0.2 lbs) or more.

- Minimum secondary HO2S (sensor 2) voltage is more than 0.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) rich stuck

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed with part load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5996: DTC P2279 (K20C1) (2017 2018 2019)

- Title: DTC P2279 (K20C1) (2017 2018 2019)
- Source path: `pages\7120.html`
- Chunk ID: `chunk_18c4f4137e9a`
- Images: `images\GHH403591.jpeg`
- Duplicate sources: `pages\8707.html`, `pages\22567.html`, `pages\20980.html`

### Full Text

````text
# DTC P2279 (K20C1) (2017 2018 2019)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis describes the leakage detection in the intake manifold based on the measured and modeled intake air pressure. If the difference between measured and modeled intake manifold pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine speed [Engine Speed] | 640 rpm | 7, 200 rpm

Other | Manifold absolute pressure (MAP) sensor value is valid

[ ]: HDS Parameter

Malfunction Threshold

The difference between measured and modeled intake manifold pressure is greater than 25.5 kPa (192 mmHg, 7.53 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake manifold air leak

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5997: DTC P2279 (K20C1) (2019 2020 2021)

- Title: DTC P2279 (K20C1) (2019 2020 2021)
- Source path: `pages\7121.html`
- Chunk ID: `chunk_fd3add764a78`
- Images: `images\GHH403592.jpeg`
- Duplicate sources: `pages\8708.html`, `pages\22568.html`, `pages\20981.html`

### Full Text

````text
# DTC P2279 (K20C1) (2019 2020 2021)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

The diagnosis describes the leakage detection in the intake manifold based on the measured and modeled intake air pressure. If the difference between measured and modeled intake manifold pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | -54 deg.F (-48 deg.C) | 289.9 deg.F (143.3 deg.C)

Engine speed [Engine Speed] | 640 rpm | 7, 200 rpm

Other | Manifold absolute pressure (MAP) sensor value is valid

EVAP system monitor is not running for at least 5 seconds

[ ]: HDS Parameter

Malfunction Threshold

The difference between measured and modeled intake manifold pressure is greater than 6.5 kPa (49 mmHg, 1.92 inHg) - 12.5 kPa (94 mmHg, 3.70 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Intake manifold air leak

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5998: DTC P2279 (K20C2: USA/Canada models)

- Title: DTC P2279 (K20C2: USA/Canada models)
- Source path: `pages\7122.html`
- Chunk ID: `chunk_f8190e4ea391`
- Images: `images\GHH403593.jpeg`, `images\GHH403594.jpeg`
- Duplicate sources: `pages\8709.html`, `pages\22569.html`, `pages\20982.html`

### Full Text

````text
# DTC P2279 (K20C2: USA/Canada models)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off at idle with the throttle closed, the amount of air supplied to the engine is considerably more than the amount of air the idle control system supplies. The powertrain control module (PCM) estimates the amount of air supplied to the engine while the throttle valve is fully closed, and if the estimated amount is more than the upper limit, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after VTEC switched | 3.0 seconds | -

Elapsed time after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

MAP value [MAP SENSOR] | - | 87 kPa (655 mmHg, 25.7 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.69 | 1.47

Fuel feedback | Closed loop

Other | At idle

[ ]: HDS Parameter

Malfunction Threshold

Either of these conditions is met:

- The estimated volume of intake air is 200 L/min (211.4 US qt/min, 176 lmp qt/min) or more when the MAP value [MAP SENSOR] is 35 kPa (260 mmHg, 10.3 inHg).

- The estimated volume of intake air is 160 L/min (169.1 US qt/min, 140.8 lmp qt/min) or more when the MAP value [MAP SENSOR] is 48 kPa (360 mmHg, 14.2 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

- Manifold absolute pressure (MAP) sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5999: DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2019)

- Title: DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2019)
- Source path: `pages\7123.html`
- Chunk ID: `chunk_d2481b1faaaa`
- Images: `images\GHH403595.jpeg`, `images\GHH403596.jpeg`
- Duplicate sources: `pages\8710.html`, `pages\22570.html`, `pages\20983.html`

### Full Text

````text
# DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2019)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off, the amount of air flowing from the PCV valve increases and the deviation also increases. The estimated air quantity of PCV is compared with the judgment value (upper limit value), and when it exceeds the more than the upper limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [Engine Speed] | 530 rpm | 820 rpm

MAP value [MAP Sensor (Hi Res)] | - | 79 kPa (600 mmHg, 23.6 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Throttle position change | - | 0.1 deg.

Fuel feedback | Closed loop

Other | During fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The estimated volume of intake air is 110 L/min (117 US qt/min, 97 lmp qt/min) - 3, 276.7 L/min (3, 462.5 US qt/min, 2883.1 lmp qt/min) or more.*

*: Depends on engine speed and load

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6000: DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\7124.html`
- Chunk ID: `chunk_3355fc38989e`
- Images: `images\GHH403597.jpeg`, `images\GHH403598.jpeg`
- Duplicate sources: `pages\8711.html`, `pages\22571.html`, `pages\20984.html`

### Full Text

````text
# DTC P2279 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off, the amount of air flowing from the PCV valve increases and the deviation also increases. The estimated air quantity of PCV is compared with the judgment value (upper limit value), and when it exceeds the more than the upper limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [Engine Speed]* 1 | 530 rpm | 820 rpm

Engine speed [Engine Speed]* 2 | 620 rpm | 2, 500 rpm

MAP value [MAP Sensor (Hi Res)] | - | 79 kPa (600 mmHg, 23.6 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Throttle position change | - | 0.1 deg.

Fuel feedback | Closed loop

Other | During fuel cut-off operation

*1: Except L15BA (M/T)

*2: L15BA (M/T)

[ ]: HDS Parameter

Malfunction Threshold

The estimated volume of intake air is 110 L/min (117 US qt/min, 97 lmp qt/min) - 3, 276.7 L/min (3, 462.5 US qt/min, 2883.1 lmp qt/min) or more.*

*: Depends on engine speed and load

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6001: DTC P2279 (L15B7/L15BA) (2016 2017 2018)

- Title: DTC P2279 (L15B7/L15BA) (2016 2017 2018)
- Source path: `pages\7125.html`
- Chunk ID: `chunk_e88e886e08ea`
- Images: `images\GHH403599.jpeg`, `images\GHH403600.jpeg`
- Duplicate sources: `pages\8712.html`, `pages\22572.html`, `pages\20985.html`

### Full Text

````text
# DTC P2279 (L15B7/L15BA) (2016 2017 2018)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off at idle with the throttle closed, the amount of air supplied to the engine is considerably more than the amount of air the idle control system supplies. The powertrain control module (PCM) estimates the amount of air supplied to the engine while the throttle valve is fully closed, and if the estimated amount is more than the upper limit, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

MAP value [MAP SENSOR] | - | 79 kPa (600 mmHg, 23.6 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Fuel feedback | Closed loop

Other | At idle

[ ]: HDS Parameter

Malfunction Threshold

Either of these conditions is met:

- The estimated volume of intake air is 160 L/min (169.1 US qt/min, 140.8 lmp qt/min) or more when the MAP value [MAP SENSOR] is 35 kPa (260 mmHg, 10.3 inHg).

- The estimated volume of intake air is 120 L/min (126.8 US qt/min, 105.6 lmp qt/min) or more when the MAP value [MAP SENSOR] is 48 kPa (360 mmHg, 14.2 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

- Manifold absolute pressure (MAP) sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6002: DTC P2279 (Si) (2017 2018)

- Title: DTC P2279 (Si) (2017 2018)
- Source path: `pages\7126.html`
- Chunk ID: `chunk_0a7fbfcd67a8`
- Images: `images\GHH403601.jpeg`, `images\GHH403602.jpeg`
- Duplicate sources: `pages\8713.html`, `pages\22573.html`, `pages\20986.html`

### Full Text

````text
# DTC P2279 (Si) (2017 2018)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off at idle with the throttle closed, the amount of air supplied to the engine is considerably more than the amount of air the idle control system supplies. The powertrain control module (PCM) estimates the amount of air supplied to the engine while the throttle valve is fully closed, and if the estimated amount is more than the upper limit, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

MAP value [MAP SENSOR] | - | 79 kPa (600 mmHg, 23.6 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Fuel feedback | Closed loop

Other | At idle

[ ]: HDS Parameter

Malfunction Threshold

Either of these conditions is met:

- The estimated volume of intake air is 150 L/min (158.5 US qt/min, 132.0 lmp qt/min) or more when the MAP value [MAP SENSOR] is 35 kPa (260 mmHg, 10.3 inHg).

- The estimated volume of intake air is 110 L/min (116.3 US qt/min, 96.8 lmp qt/min) or more when the MAP value [MAP SENSOR] is 48 kPa (360 mmHg, 14.2 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

- Manifold absolute pressure (MAP) sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6003: DTC P2279 (Si) (2019 2020 2021)

- Title: DTC P2279 (Si) (2019 2020 2021)
- Source path: `pages\7127.html`
- Chunk ID: `chunk_935f0da6b157`
- Images: `images\GHH403603.jpeg`, `images\GHH403604.jpeg`
- Duplicate sources: `pages\8714.html`, `pages\22574.html`, `pages\20987.html`

### Full Text

````text
# DTC P2279 (Si) (2019 2020 2021)

DTC P2279: Intake Air System Leak

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The positive crankcase ventilation (PCV) system reduces hydrocarbon (HC) emissions. The PCV system recirculates unburned air/fuel mixture (blow-by gas) into the intake manifold so that it is drawn into the engine and burned, thus reducing HC. If the PCV hose comes off, the amount of air flowing from the PCV valve increases and the deviation also increases. The estimated air quantity of PCV is compared with the judgment value (upper limit value), and when it exceeds the more than the upper limit, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 22 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [Engine Speed] | 620 rpm | 858 rpm

MAP value [MAP Sensor (Hi Res)] | - | 79 kPa (600 mmHg, 23.6 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

Throttle position change | - | 0.1 deg.

Fuel feedback | Closed loop

Other | During fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The estimated volume of intake air is 110 L/min (117 US qt/min, 97 lmp qt/min) - 3, 276.7 L/min (3, 462.5 US qt/min, 2883.1 lmp qt/min) or more.*

*: Depends on engine speed and load

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- Evaporative emission (EVAP) canister purge valve failure

- Valve timing incorrect

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Let the engine idle for at least 22 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6004: DTC P2421 (K20C2) (2019 2020 2021)

- Title: DTC P2421 (K20C2) (2019 2020 2021)
- Source path: `pages\7128.html`
- Chunk ID: `chunk_83098833ce54`
- Images: `images\GHH403605.jpeg`
- Duplicate sources: `pages\8715.html`, `pages\22575.html`, `pages\20988.html`

### Full Text

````text
# DTC P2421 (K20C2) (2019 2020 2021)

DTC P2421: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Open

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) does a detection of stuck open of the evaporative emission (EVAP) canister vent shut valve only if it is commanded closed since the EVAP canister vent shut valve is normally opened. When the EVAP canister vent shut valve is commanded closed during the purge, the fuel tank pressure (FTP) sensor value lowers by a decompression of the EVAP system. If the FTP sensor value does not lower, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration* 1 | 2.8 seconds or more

Duration* 2 | 4.6 seconds or more

DTC Type | Two drive cycles, MIL on

*1: CVT

*2: M/T

Enable Conditions

Condition | Minimum | Maximum

Soak duration* | 6 hours | -

Elapsed time after the vehicle condition is turned to the ON mode | 1 second | -

Elapsed time after starting the engine (after soak)** | 10 seconds | -

Outside air temperature* | 40.0 deg.F (4.4 deg.C) | -

Engine coolant temperature [ECT Sensor]*** | 131 deg.F (55 deg.C) | -

Engine coolant temperature (at radiator) after soak* | 40.0 deg.F (4.4 deg.C) | -

Engine coolant temperature (at engine) lowering from after soak to current* | - | 9 deg.F (5 deg.C)

Engine coolant temperature (at radiator) lowering from after soak to current* | - | 3 deg.F (2 deg.C)

Vehicle speed [VEHICLE SPEED]**** | 25 mph (39 km/h) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Total intake air amount* 1 | 168 g (5.93 oz) | -

Total intake air amount* 2 | 150 g (5.30 oz) | -

Intake air amount**** | 3.76 g/second (0.1327 oz/second) | -

Purge duty [PCS DUTY] | 20 % | -

EVAP canister vent shut valve command | Close

*: Cancels detection if out of condition

**: Condition to permit monitor intake air temperature

***: Condition to start purge

****: Condition to permit total up intake air amount

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor value change is -0.19 kPa (-1.5 mmHg, -0.05 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve stuck oepn

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 6 hours.

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let it idle for at least 5 minutes 45 seconds.

- Drive the vehicle at 25 mph (40 km/h) or more with avoidance of high load.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 6005: DTC P2421 (L15B7/L15BY) (2019 2020 2021)

- Title: DTC P2421 (L15B7/L15BY) (2019 2020 2021)
- Source path: `pages\7129.html`
- Chunk ID: `chunk_d645d7c175d5`
- Images: `images\GHH403606.jpeg`
- Duplicate sources: `pages\8716.html`, `pages\22576.html`, `pages\20989.html`

### Full Text

````text
# DTC P2421 (L15B7/L15BY) (2019 2020 2021)

DTC P2421: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Open

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) does a detection of stuck open of the evaporative emission (EVAP) canister vent shut valve only if it is commanded closed since the EVAP canister vent shut valve is normally opened. When the EVAP canister vent shut valve is commanded closed during the purge, the fuel tank pressure (FTP) sensor value lowers by a decompression of the EVAP system. If the FTP sensor value does not lower, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Soak duration* | 6 hours | -

*: Cancels detection if out of condition

**: Condition to permit monitor intake air temperature

***: Condition to start purge

****: Condition to permit total up intake air amount

[ ]: HDS Parameter

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 1 second | -

Elapsed time after starting the engine (after soak)** | 10 seconds | -

Outside air temperature* | 40.0 deg.F (4.4 deg.C) | -

Engine coolant temperature [ECT Sensor]*** | 131 deg.F (55 deg.C) | -

Engine coolant temperature (at radiator) after soak* | 40.0 deg.F (4.4 deg.C) | -

Engine coolant temperature (at engine) lowering from after soak to current* | - | 9 deg.F (5 deg.C)

Engine coolant temperature (at radiator) lowering from after soak to current* | - | 3 deg.F (2 deg.C)

Vehicle speed [VEHICLE SPEED]**** | 26 mph (41 km/h) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Total intake air amount | 120 g (4.24 oz) | -

Intake air amount**** | 3.9 g/second (0.138 oz/second) | -

Purge duty [PCS DUTY] | 20 % | -

EVAP canister vent shut valve command | Close

*: Cancels detection if out of condition

**: Condition to permit monitor intake air temperature

***: Condition to start purge

****: Condition to permit total up intake air amount

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor value change is -0.19 kPa (-1.5 mmHg, -0.05 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve stuck open

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in P or N) until the radiator fan comes on.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 6 hours.

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in P or N) until the radiator fan comes on.

- Let it idle for at least 5 minutes 45 seconds.

- Drive the vehicle at 25 mph (40 km/h) or more with avoidance of high load.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 6006: DTC P2422 (K20C1) (2017 2018 2019)

- Title: DTC P2422 (K20C1) (2017 2018 2019)
- Source path: `pages\7130.html`
- Chunk ID: `chunk_09b9d122201a`
- Images: `images\GHH403607.jpeg`
- Duplicate sources: `pages\8717.html`, `pages\22577.html`, `pages\20990.html`

### Full Text

````text
# DTC P2422 (K20C1) (2017 2018 2019)

DTC P2422: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Closed Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

In order to detect an evaporative emission (EVAP) canister vent shut valve stuck closed malfunction, the fuel tank pressure is continuously monitored against rationality threshold. Initially, the fuel tank pressure is monitored under conditions when the canister purging is taking place. In this case, both EVAP canister purge valve and EVAP canister vent shut valve are open, so that the fuel tank pressure cannot fall down dramatically. In case of EVAP canister vent shut valve stuck closed, the canister purging will build a vacuum in a fuel tank. To prevent fuel tank from damage, EVAP canister purge valve will be commanded closed as soon as a fuel tank pressure reaches low rationality threshold. If the fuel tank pressure remains below a specified value for a specified amount of time after EVAP canister purge valve has been closed, the powertrain control module (PCM) detects a malfunction and stores a DTC. Additionally, an EVAP canister vent shut valve stuck check will be performed during EVAP system monitor using tighter fault threshold.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous*, Once per driving cycle**

Sequence** | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: During canister purging

**: During EVAP system monitor

Enable Conditions

During canister purging

Condition

State of the engine | Running

Other | EVAP canister vent shut valve is commanded open

Other | EVAP canister purge valve is commanded open

During EVAP system monitor (conditions to trigger EVAP system monitor)

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 minutes | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -

Fuel tank pressure | -4 kPa (-30 mmHg, -1.1 inHg) | 4 kPa (30 mmHg, 1.1 inHg)

12 volt battery voltage [Battery] | 10.7 V | 16 V

Fuel feedback | Closed loop

Other | No refueling

Both EVAP canister vent shut valve and EVAP canister purge valve are commanded open for at least 20 seconds

[ ]: HDS Parameter

Malfunction Threshold

- During canister purging If the fuel tank pressure is less than -3 kPa (-22 mmHg, -0.8 inHg), then the EVAP canister purge valve is commanded closed to start stuck check. At stuck check, the fuel tank pressure is less than -3 kPa (-22 mmHg, -0.8 inHg) for at least 2 seconds.

If the fuel tank pressure is less than -3 kPa (-22 mmHg, -0.8 inHg), then the EVAP canister purge valve is commanded closed to start stuck check. At stuck check, the fuel tank pressure is less than -3 kPa (-22 mmHg, -0.8 inHg) for at least 2 seconds.

- During EVAP system monitor The fuel tank pressure is less than -2.25 kPa (-16.87 mmHg, -0.664 inHg) for at least 5 seconds.

The fuel tank pressure is less than -2.25 kPa (-16.87 mmHg, -0.664 inHg) for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve closed stuck

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for at least 10 minutes.

- Stop the vehicle and let it idle for 5 minutes.

- Turn the vehicle to the OFF (LOCK) mode and wait for a while (maximum 45 minutes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6007: DTC P2422 (K20C1) (2019 2020 2021)

- Title: DTC P2422 (K20C1) (2019 2020 2021)
- Source path: `pages\7131.html`
- Chunk ID: `chunk_e1c54ac95a51`
- Images: `images\GHH403608.jpeg`
- Duplicate sources: `pages\8718.html`, `pages\22578.html`, `pages\20991.html`

### Full Text

````text
# DTC P2422 (K20C1) (2019 2020 2021)

DTC P2422: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Closed Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

A stuck closed evaporative emission (EVAP) canister vent shut valve is detected either by monitoring the fuel tank pressure during canister purging or during the EVAP system leak monitor. The fuel tank pressure is continuously compared with a rationality threshold when the monitoring conditions are fulfilled. Initially the fuel tank pressure is monitored when canister purging is active. Purging commences with the simultaneous opening of both the EVAP canister purge valve and the EVAP canister vent shut valve. If the EVAP canister vent shut valve was stuck closed, then canister purging will build a progressive vacuum that will eventually damage the fuel tank. To prevent fuel tank damage, the EVAP canister purge valve is commanded to close when the fuel tank pressure falls below a low rationality threshold. If the fuel tank pressure is less than the low rationality threshold for a calibrated amount of time, the powertrain control module (PCM) detects a malfunction and stores a DTC. If a stuck closed EVAP canister vent shut valve could not be detected during canister purging, then another EVAP canister vent shut valve stuck check will be performed during the EVAP system monitor using tighter fault threshold. First, both the EVAP canister vent shut valve and the EVAP purge valve are commanded open and the fuel tank pressure is monitored during the ensuing canister purging. If the fuel tank pressure reaches a low rationality threshold, the EVAP purge valve is commanded to close and if the fuel tank pressure remains below this rationality threshold for calibrated amount of time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Multiple

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

During canister purging

Condition

Vehicle | ON mode

During EVAP system monitor (conditions to trigger EVAP system monitor)

Condition | Minimum | Maximum

Elapsed time after starting the engine | 9 minutes 10 seconds | -

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 113 deg.F (45 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Fuel tank pressure | -4 kPa (-30 mmHg, -1.1 inHg) | 4 kPa (30 mmHg, 1.1 inHg)

Change in ambient pressure during vacuum build* | - | 1.602 kPa (12.01 mmHg, 0.473 in Hg)

12 volt battery voltage [Battery] | 10.7 V | 16 V

Fuel level | 1 L (0.3 US gal) | 42 L (11.0 US gal)

Other | No fault suspicion in mixture adaptation

*: For at least 5 minutes

[ ]: HDS Parameter

Malfunction Threshold

- During canister purging Canister purge mass flow is 0 kg/h (0 lbs/h) for at least 2 seconds.

Canister purge mass flow is 0 kg/h (0 lbs/h) for at least 2 seconds.

- During EVAP system monitor The fuel tank pressure is less than -2.25 kPa (-16.87 mmHg, -0.664 inHg) for at least 5 seconds.

The fuel tank pressure is less than -2.25 kPa (-16.87 mmHg, -0.664 inHg) for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve closed stuck

- EVAP canister vent shut valve blocked by dirt

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for a while.

- Stop the vehicle and let it idle for 10 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6008: DTC P2422 (K20C2)

- Title: DTC P2422 (K20C2)
- Source path: `pages\7132.html`
- Chunk ID: `chunk_e4eebd8acbbd`
- Images: `images\GHH403609.jpeg`, `images\GHH403610.jpeg`
- Duplicate sources: `pages\8719.html`, `pages\22579.html`, `pages\20992.html`

### Full Text

````text
# DTC P2422 (K20C2)

DTC P2422: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Closed Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor output is near atmospheric pressure (0 kPa (0 mmHg, 0 inHg)) before purge starts since the evaporative emission (EVAP) canister vent shut valve is normally open (to the atmosphere). The sensor indicates a negative pressure value (vacuum) while purging. When the FTP sensor indicates vacuum after the engine starts, an FTP sensor zero point shift failure or an EVAP canister vent shut valve stuck closed can occur. To prevent these failures, the powertrain control module (PCM) monitors the FTP sensor output after purge starts. The PCM detects a malfunction of the EVAP canister vent shut valve if the output indicates excessive vacuum. However, if the fuel tank internal pressure is below the specified value (excessive vacuum is detected) when starting the engine, the malfunction detection should be done as follows because it is difficult to distinguish between FTP sensor range problem (P1454) and an EVAP canister vent shut valve stuck closed problem (P2422).

- If neither Pending DTCs (P1454 nor P2422) are stored, both Pending DTCs are stored when excessive vacuum is detected at engine start.

- If both Pending DTCs (P1454 and P2422) are stored and excessive vacuum is detected, both Confirmed DTCs are stored.

- If either Pending DTC (P1454 or P2422) is stored and excessive vacuum is detected, the PCM stores the Confirmed DTC which the Pending DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence** | P0452, P0453 are judged as OK

Duration | 1.04*, 8.0** seconds or more

DTC Type | Two drive cycles, MIL on

*: Elapsed time after the FTP sensor output exceeds the malfunction threshold.

.**: Excessive negative pressure is detected.

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine** | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1]*** | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY]* | 10.5 V | -

Fuel feedback | Closed loop

Other** | The EVAP canister vent shut valve is open

The EVAP canister purge valve is closed (the system is not purging)

***: Condition to start the purge control

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is -4 kPa (-25 mmHg, -1.0 inHg)*, -2 kPa (-10 mmHg, -0.4 inHg)** or less for at least 1.04*, 8.0** seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve closed stuck

- EVAP canister drain tube clogged

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- When the diagnosis does not finish at idle, drive at 30 - 75 mph (48 - 120 km/h) at EVAP canister purge valve duty [EVAP PC DUTY] 20 % or more.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6009: DTC P2422 (L15B7/L15BA)

- Title: DTC P2422 (L15B7/L15BA)
- Source path: `pages\7133.html`
- Chunk ID: `chunk_a7d617bec9bc`
- Images: `images\GHH403611.jpeg`, `images\GHH403612.jpeg`
- Duplicate sources: `pages\8720.html`, `pages\22580.html`, `pages\20993.html`

### Full Text

````text
# DTC P2422 (L15B7/L15BA)

DTC P2422: Evaporative Emission (EVAP) Canister Vent Shut Valve Stuck Closed Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor output is near atmospheric pressure (0 kPa (0 mmHg, 0 inHg)) before purge starts since the evaporative emission (EVAP) canister vent shut valve is normally open (to the atmosphere). The sensor indicates a negative pressure value (vacuum) while purging. When the FTP sensor indicates vacuum after the engine starts, an FTP sensor zero point shift failure or an EVAP canister vent shut valve stuck closed can occur. To prevent these failures, the powertrain control module (PCM) monitors the FTP sensor output after purge starts. The PCM detects a malfunction of the EVAP canister vent shut valve if the output indicates excessive vacuum. However, if the fuel tank internal pressure is below the specified value (excessive vacuum is detected) when starting the engine, the malfunction detection should be done as follows because it is difficult to distinguish between FTP sensor range problem (P1454) and an EVAP canister vent shut valve stuck closed problem (P2422).

- If neither Pending DTCs (P1454 nor P2422) are stored, both Pending DTCs are stored when excessive vacuum is detected at engine start.

- If both Pending DTCs (P1454 and P2422) are stored and excessive vacuum is detected, both Confirmed DTCs are stored.

- If either Pending DTC (P1454 or P2422) is stored and excessive vacuum is detected, the PCM stores the Confirmed DTC which the Pending DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence** | P0452, P0453 are judged as OK

Duration | 1.04*, 8.0** seconds or more

DTC Type | Two drive cycles, MIL on

*: Elapsed time after the FTP sensor output exceeds the malfunction threshold..

.**: Excessive negative pressure is detected.

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine** | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1]*** | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY]* | 10.5 V | -

Fuel feedback | Closed loop

Other** | The EVAP canister vent shut valve is open

The EVAP canister purge valve is closed (the system is not purging)

***: Condition to start the purge control

[ ]: HDS Parameter

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is -4 kPa (-25 mmHg, -1.0 inHg)*, -2 kPa (-10 mmHg, -0.4 inHg)** or less for at least 1.04*, 8.0** seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve closed stuck

- EVAP canister drain tube clogged

Confirmation Procedure

Operating Condition

- Start the engine, and let it idle until the radiator fan comes on.

- When the diagnosis does not finish at idle, drive at 30 - 75 mph (48 - 120 km/h) at EVAP canister purge valve duty [EVAP PC DUTY] 20 % or more.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6010: DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\7134.html`
- Chunk ID: `chunk_a055f7762ca5`
- Images: `images\GHH403613.jpeg`, `images\GHH403614.jpeg`, `images\GHH403615.jpeg`
- Duplicate sources: `pages\8721.html`, `pages\22581.html`, `pages\20994.html`

### Full Text

````text
# DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

DTC P2450: Evaporative Emission (EVAP) System Purge Line Non-return Valve A Stuck Open

General Description

Courtesy of HONDA, U.S.A., INC.

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

If non-return valve A is stuck opened, the boost pressure flows back to the fuel tank when purge controlled in boost condition. At the time, the FTP sensor pulse waveform shows opposite phase to the usual phase. The PCM detects a malfunction by calculating the phase time difference, and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor pulse phase time difference is 20 milliseconds or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Non-return valve A open stuck

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

## Chunk 6011: DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\7135.html`
- Chunk ID: `chunk_4bf8d8791674`
- Images: `images\GHH403616.jpeg`, `images\GHH403617.jpeg`, `images\GHH403618.jpeg`
- Duplicate sources: `pages\8722.html`, `pages\22582.html`, `pages\20995.html`

### Full Text

````text
# DTC P2450 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P2450: Evaporative Emission (EVAP) System Purge Line Non-return Valve A Stuck Open

General Description

Courtesy of HONDA, U.S.A., INC.

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

If non-return valve A is stuck opened, the boost pressure flows back to the fuel tank when purge controlled in boost condition. At the time, the FTP sensor pulse waveform shows opposite phase to the usual phase. The PCM detects a malfunction by calculating the phase time difference, and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 12 seconds* 1 (9.5 seconds)* 2 or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si) and L15BY

*2: L15BA

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor pulse phase time difference is 20 milliseconds or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Non-return valve A open stuck

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

## Chunk 6012: DTC P2450 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2450 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7136.html`
- Chunk ID: `chunk_4aa0bb52b87f`
- Images: `images\GHH403619.jpeg`, `images\GHH403620.jpeg`, `images\GHH403621.jpeg`
- Duplicate sources: `pages\8723.html`, `pages\22583.html`, `pages\20996.html`

### Full Text

````text
# DTC P2450 (Si) (2017 2018 2019 2020 2021)

DTC P2450: Evaporative Emission (EVAP) System Purge Line Non-return Valve A Stuck Open

General Description

Courtesy of HONDA, U.S.A., INC.

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

If non-return valve A is stuck opened, the boost pressure flows back to the fuel tank when purge controlled in boost condition. At the time, the FTP sensor pulse waveform shows opposite phase to the usual phase. The PCM detects a malfunction by calculating the phase time difference, and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor pulse phase time difference is 20 milliseconds or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Non-return valve A open stuck

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

## Chunk 6013: DTC P2563 (K20C1) (2017 2018 2019)

- Title: DTC P2563 (K20C1) (2017 2018 2019)
- Source path: `pages\7137.html`
- Chunk ID: `chunk_1c6cc73f9c3d`
- Images: `images\GHH403622.jpeg`
- Duplicate sources: `pages\8724.html`, `pages\22584.html`, `pages\20997.html`

### Full Text

````text
# DTC P2563 (K20C1) (2017 2018 2019)

DTC P2563: Turbocharger Wastegate Control Actuator Position Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the turbocharger wastegate control actuator position sensor circuit for physical range check. The diagnostic compares the voltages of the turbocharger wastegate control actuator position sensor read at the closed and open positions of the turbocharger valve with their respective calibrated threshold values. If the turbocharger wastegate control actuator position sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Either of the conditions continues for at least 0.14 second.

- The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] read at the closed position of the turbocharger valve is less than 0 V.

- The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] read at the open position of the turbocharger valve is greater than 5 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator position sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6014: DTC P2563 (K20C1) (2019 2020 2021)

- Title: DTC P2563 (K20C1) (2019 2020 2021)
- Source path: `pages\7138.html`
- Chunk ID: `chunk_082a59dddd30`
- Images: `images\GHH403623.jpeg`
- Duplicate sources: `pages\8725.html`, `pages\22585.html`, `pages\20998.html`

### Full Text

````text
# DTC P2563 (K20C1) (2019 2020 2021)

DTC P2563: Turbocharger Wastegate Control Actuator Position Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the turbocharger wastegate control actuator position sensor circuit for physical range check. The diagnostic compares the voltages of the turbocharger wastegate control actuator position sensor read at the closed and open positions of the turbocharger valve with their respective calibrated threshold values. If the turbocharger wastegate control actuator position sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.14 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Either of the conditions continues for at least 0.14 second.

- The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] read at the closed position of the turbocharger valve is 0.2 - 0.35 V.

- The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] read at the open position of the turbocharger valve is greater than 4.74 - 4.81 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator position sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6015: DTC P2563 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P2563 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\7139.html`
- Chunk ID: `chunk_418b022b41b0`
- Images: `images\GHH403624.jpeg`, `images\GHH403625.jpeg`
- Duplicate sources: `pages\8726.html`, `pages\22586.html`, `pages\20999.html`

### Full Text

````text
# DTC P2563 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P2563: Turbocharger Wastegate Control Actuator Position Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) adjusts the boost pressure by controlling the turbocharger wastegate control actuator of the turbocharger. Boost pressure becomes higher by fully closing the turbocharger wastegate control valve driven by the turbocharger wastegate control actuator. The turbocharger wastegate control valve position is detected by the turbocharger wastegate control actuator position sensor and the signal is input to the PCM for target position feedback control. The turbocharger wastegate control actuator position sensor value when the turbocharger wastegate control valve is fully closed is stored as fully closed learning value. Target and actual positions are represented by the relative value from the fully closed position. The PCM sets a target position, and outputs a drive signal to the driver IC and drives the turbocharger wastegate control actuator to be equal to the target position. If the turbocharger wastegate control actuator position sensor output voltage is a set value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The turbocharger wastegate control actuator position sensor output voltage [EWG VOLTAGE FROM LIFT SENSOR] is 0.31 V or less, or 4.78 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator position sensor DCWGL line open

- Turbocharger wastegate control actuator position sensor SG line open

- Turbocharger wastegate control actuator position sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6016: DTC P2563 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2563 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7140.html`
- Chunk ID: `chunk_c5ffc091b4fc`
- Images: `images\GHH403626.jpeg`, `images\GHH403627.jpeg`
- Duplicate sources: `pages\8727.html`, `pages\22587.html`, `pages\21000.html`

### Full Text

````text
# DTC P2563 (Si) (2017 2018 2019 2020 2021)

DTC P2563: Turbocharger Wastegate Control Actuator Position Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) adjusts the boost pressure by controlling the turbocharger wastegate control actuator of the turbocharger. Boost pressure becomes higher by fully closing the turbocharger wastegate control valve driven by the turbocharger wastegate control actuator. The turbocharger wastegate control valve position is detected by the turbocharger wastegate control actuator position sensor and the signal is input to the PCM for target position feedback control. The turbocharger wastegate control actuator position sensor value when the turbocharger wastegate control valve is fully closed is stored as fully closed learning value. Target and actual positions are represented by the relative value from the fully closed position. The PCM sets a target position, and outputs a drive signal to the driver IC and drives the turbocharger wastegate control actuator to be equal to the target position. If the turbocharger wastegate control actuator position sensor output voltage is a specified range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The turbocharger wastegate control actuator position sensor output voltage [EWG VOLTAGE FROM LIFT SENSOR] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator position sensor DCWGL line open

- Turbocharger wastegate control actuator position sensor SG line open

- Turbocharger wastegate control actuator position sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6017: DTC P2564, P2565 (K20C1) (2017 2018 2019)

- Title: DTC P2564, P2565 (K20C1) (2017 2018 2019)
- Source path: `pages\7141.html`
- Chunk ID: `chunk_6841ad2f74b2`
- Images: `images\GHH403628.jpeg`, `images\GHH403629.jpeg`
- Duplicate sources: `pages\8728.html`, `pages\22588.html`, `pages\21001.html`

### Full Text

````text
# DTC P2564, P2565 (K20C1) (2017 2018 2019)

DTC P2564: Turbocharger Wastegate Control Actuator Position Sensor Circuit Low Voltage

DTC P2565: Turbocharger Wastegate Control Actuator Position Sensor Circuit High Voltage

DTC P2565: Turbocharger Wastegate Control Actuator Position Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the turbocharger wastegate control actuator position sensor circuit for electrical malfunctions. In order to provide electrical diagnostics, the output voltage of the turbocharger wastegate control actuator position sensor is continuously monitored and compared with minimum and maximum thresholds. If the turbocharger wastegate control actuator position sensor voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.14 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2564

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is less than 0.195 V for at least 0.14 second.

DTC: P2565

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is greater than 4.805 V for at least 0.14 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2564

- Turbocharger wastegate control actuator position sensor WGL line short to ground

- Turbocharger wastegate control actuator position sensor VCC line open

DTC: P2565

- Turbocharger wastegate control actuator position sensor WGL line short to power

- Turbocharger wastegate control actuator position sensor WGL line open

- Turbocharger wastegate control actuator position sensor SG line open

Common

- Turbocharger wastegate control actuator position sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6018: DTC P2564, P2565 (K20C1) (2019)

- Title: DTC P2564, P2565 (K20C1) (2019)
- Source path: `pages\7142.html`
- Chunk ID: `chunk_97c1d8c9d24c`
- Images: `images\GHH403630.jpeg`
- Duplicate sources: `pages\8729.html`, `pages\22589.html`, `pages\21002.html`

### Full Text

````text
# DTC P2564, P2565 (K20C1) (2019)

DTC P2564: Turbocharger Wastegate Control Actuator Position Sensor Circuit Low Voltage

DTC P2565: Turbocharger Wastegate Control Actuator Position Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the turbocharger wastegate control actuator position sensor circuit for electrical malfunctions. In order to provide electrical diagnostics, the output voltage of the turbocharger wastegate control actuator position sensor is continuously monitored and compared with minimum and maximum thresholds. If the turbocharger wastegate control actuator position sensor voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2564

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is less than 0.2 V for at least 0.5 second.

DTC: P2565

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is greater than 4.81 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2564

- Turbocharger wastegate control actuator position sensor WGL line short to ground

- Turbocharger wastegate control actuator position sensor VCC line open

DTC: P2565

- Turbocharger wastegate control actuator position sensor WGL line short to power

- Turbocharger wastegate control actuator position sensor WGL line open

- Turbocharger wastegate control actuator position sensor SG line open

Common

- Turbocharger wastegate control actuator position sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6019: DTC P2564, P2565 (K20C1) (2020 2021)

- Title: DTC P2564, P2565 (K20C1) (2020 2021)
- Source path: `pages\7143.html`
- Chunk ID: `chunk_63f3c4c72dda`
- Images: `images\GHH403631.jpeg`
- Duplicate sources: `pages\8730.html`, `pages\22590.html`, `pages\21003.html`

### Full Text

````text
# DTC P2564, P2565 (K20C1) (2020 2021)

DTC P2564: Turbocharger Wastegate Control Actuator Position Sensor Circuit Low Voltage

DTC P2565: Turbocharger Wastegate Control Actuator Position Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the turbocharger wastegate control actuator position sensor circuit for electrical malfunctions. In order to provide electrical diagnostics, the output voltage of the turbocharger wastegate control actuator position sensor is continuously monitored and compared with minimum and maximum thresholds. If the turbocharger wastegate control actuator position sensor voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.14 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P2564

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is less than 0.2 V for at least 0.14 second.

DTC: P2565

The turbocharger wastegate control actuator position sensor voltage [EWG Voltage From Lift Sensor] is greater than 4.81 V for at least 0.14 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2564

- Turbocharger wastegate control actuator position sensor WGL line short to ground

- Turbocharger wastegate control actuator position sensor VCC line open

DTC: P2565

- Turbocharger wastegate control actuator position sensor WGL line short to power

- Turbocharger wastegate control actuator position sensor WGL line open

- Turbocharger wastegate control actuator position sensor SG line open

Common

- Turbocharger wastegate control actuator position sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6020: DTC P2564, P2565 (L15B7/L15BA)

- Title: DTC P2564, P2565 (L15B7/L15BA)
- Source path: `pages\7144.html`
- Chunk ID: `chunk_05c5b3421239`
- Images: `images\GHH403632.jpeg`, `images\GHH403633.jpeg`
- Duplicate sources: `pages\8731.html`, `pages\22591.html`, `pages\21004.html`

### Full Text

````text
# DTC P2564, P2565 (L15B7/L15BA)

DTC P2564: Turbocharger Wastegate Control Actuator Position Sensor Circuit Low Voltage

DTC P2565: Turbocharger Wastegate Control Actuator Position Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) adjusts the boost pressure by controlling the turbocharger wastegate control actuator of the turbocharger. Boost pressure becomes higher by fully closing the turbocharger wastegate control valve driven by the turbocharger wastegate control actuator. The turbocharger wastegate control valve position is detected by the turbocharger wastegate control actuator position sensor and the signal is input to the PCM for target position feedback control. The turbocharger wastegate control actuator position sensor value when the turbocharger wastegate control valve is fully closed is stored as fully closed learning value. Target and actual positions are represented by the relative value from the fully closed position. The PCM sets a target position, and outputs a drive signal to the driver IC and drives the turbocharger wastegate control actuator to be equal to the target position. If the turbocharger wastegate control actuator position sensor output voltage is out of normal range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P2564

The turbocharger wastegate control actuator position sensor output voltage [EWG VOLTAGE FROM LIFT SENSOR] is 0.16 V or less for at least 2 seconds.

DTC: P2565

The turbocharger wastegate control actuator position sensor output voltage [EWG VOLTAGE FROM LIFT SENSOR] is 4.87 V or more for at least 2 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2564

- Turbocharger wastegate control actuator position sensor DCWGL line short to ground

- Turbocharger wastegate control actuator position sensor VCC line open

DTC: P2565

- Turbocharger wastegate control actuator position sensor DCWGL line open

- Turbocharger wastegate control actuator position sensor SG line open

Common

- Turbocharger wastegate control actuator position sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6021: DTC P2610 (K20C1) (2017 2018 2019)

- Title: DTC P2610 (K20C1) (2017 2018 2019)
- Source path: `pages\7145.html`
- Chunk ID: `chunk_122bd35d450a`
- Images: none
- Duplicate sources: `pages\8732.html`, `pages\22592.html`, `pages\21005.html`

### Full Text

````text
# DTC P2610 (K20C1) (2017 2018 2019)

DTC P2610: Powertrain Control Module (PCM) Ignition Off Internal Timer Malfunction

General Description

The powertrain control module (PCM) has a built-in ignition off timer that measures the duration from ignition off to the next ignition on. The ignition off time is determined by the stop counter, and rationality check is done by comparing it with the system timer while the vehicle is in OFF (LOCK) mode. If the time monitored by the stop counter deviates from the time monitored by the system timer, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Malfunction Threshold

The stop counter time is less than 94 % or more than 106 % of the system timer which the diagnosis time is set to 8 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6022: DTC P2610 (K20C1) (2019 2020 2021)

- Title: DTC P2610 (K20C1) (2019 2020 2021)
- Source path: `pages\7146.html`
- Chunk ID: `chunk_fcda7f32c596`
- Images: none
- Duplicate sources: `pages\8733.html`, `pages\22593.html`, `pages\21006.html`

### Full Text

````text
# DTC P2610 (K20C1) (2019 2020 2021)

DTC P2610: Powertrain Control Module (PCM) Ignition Off Internal Timer Malfunction

General Description

The powertrain control module (PCM) has a built-in ignition off timer that measures the duration from ignition off to the next ignition on. The ignition off time is determined by the stop counter, and the check is done by comparing it with the system timer while the vehicle is in OFF (LOCK) mode. If the time monitored by the stop counter deviates from the time monitored by the system timer, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 8 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | OFF (LOCK) mode

Malfunction Threshold

The stop counter time is less than 94 % or more than 106 % of the system timer which the diagnosis time is set to 8 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6023: DTC P2610 (K20C2)

- Title: DTC P2610 (K20C2)
- Source path: `pages\7147.html`
- Chunk ID: `chunk_eb603c51e2c1`
- Images: `images\GHH403634.jpeg`
- Duplicate sources: `pages\8734.html`, `pages\22594.html`, `pages\21007.html`

### Full Text

````text
# DTC P2610 (K20C2)

DTC P2610: Powertrain Control Module (PCM) Ignition Off Internal Timer Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) has a built-in ignition off timer that measures the duration from ignition off to the next ignition on. The measured duration is used for evaporative emission (EVAP) leak detection and temperature assumption of the catalytic converter. The CPU in the PCM accesses the ignition off timer when reading the measured duration. If the access process to the ignition off timer fails, or an abnormality is found in the read data, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle* | ON mode

*: Excludes after the 12 volt battery is reconnected.

Malfunction Threshold

The access process to the ignition off timer fails, or an abnormality is found in the read data for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6024: DTC P2610 (L15B7/L15BA/L15BY)

- Title: DTC P2610 (L15B7/L15BA/L15BY)
- Source path: `pages\7148.html`
- Chunk ID: `chunk_74e20beb80bc`
- Images: `images\GHH403635.jpeg`
- Duplicate sources: `pages\8735.html`, `pages\22595.html`, `pages\21008.html`

### Full Text

````text
# DTC P2610 (L15B7/L15BA/L15BY)

DTC P2610: Powertrain Control Module (PCM) Ignition Off Internal Timer Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) has a built-in ignition off timer that measures the duration from ignition off to the next ignition on. The measured duration is used for evaporative emission (EVAP) leak detection and temperature assumption of the catalytic converter. The CPU in the PCM accesses the ignition off timer when reading the measured duration. If the access process to the ignition off timer fails, or an abnormality is found in the read data, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle* | ON mode

*: Excludes after the 12 volt battery is reconnected.

Malfunction Threshold

The access process to the ignition off timer fails, or an abnormality is found in the read data for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6025: DTC P2623 (K20C1) (2017 2018 2019)

- Title: DTC P2623 (K20C1) (2017 2018 2019)
- Source path: `pages\7149.html`
- Chunk ID: `chunk_036c4436835e`
- Images: `images\GHH403636.jpeg`
- Duplicate sources: `pages\8736.html`, `pages\22596.html`, `pages\21009.html`

### Full Text

````text
# DTC P2623 (K20C1) (2017 2018 2019)

DTC P2623: High Pressure Fuel Pump Spill Valve Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the high pressure fuel pump for diagnosis of electric circuit. If the PCM detects abnormal in high pressure fuel pump circuit, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] (power voltage input to PCM) | 8 V | -

State of the engine | Running

Other | Not during reset by the watch dog

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects open circuit or short circuit in the high pressure fuel pump circuit for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High pressure fuel pump HPUMP H line open

- High pressure fuel pump HPUMP H line short to ground

- High pressure fuel pump HPUMP H line short to power

- High pressure fuel pump HPUMP L line open

- High pressure fuel pump HPUMP L line short to ground

- High pressure fuel pump HPUMP L line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6026: DTC P2623 (K20C1) (2019 2020 2021)

- Title: DTC P2623 (K20C1) (2019 2020 2021)
- Source path: `pages\7150.html`
- Chunk ID: `chunk_2c1308174185`
- Images: `images\GHH403637.jpeg`
- Duplicate sources: `pages\8737.html`, `pages\22597.html`, `pages\21010.html`

### Full Text

````text
# DTC P2623 (K20C1) (2019 2020 2021)

DTC P2623: High Pressure Fuel Pump Spill Valve Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the high pressure fuel pump for diagnosis of electric circuit. If the PCM detects abnormal in high pressure fuel pump circuit, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 min -1 (rpm) | -

12 volt battery voltage [Battery] | 8 V | 16 V

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs:

Open circuit

- The voltage difference between high side (HPUMP H) and ground is more than 3.0 V.

- The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

Short circuit in HPUMP H line (Either malfunction threshold A or B)

- Malfunction threshold A

- - The voltage difference between power and high side (HPUMP H) is more than 1.5 V. - The voltage difference between high side (HPUMP H) and ground is less than 3.0 V. - The voltage difference between low side (HPUMP L) and ground is less than 1.5 V. - There is no short to ground at low side (HPUMP L) in result of pinpointing.

- - The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

- - The voltage difference between high side (HPUMP H) and ground is less than 3.0 V.

The voltage difference between high side (HPUMP H) and ground is less than 3.0 V.

- - The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

- - There is no short to ground at low side (HPUMP L) in result of pinpointing.

There is no short to ground at low side (HPUMP L) in result of pinpointing.

- Malfunction threshold B

- - The voltage difference between power and high side (HPUMP H) is less than 1.5 V. - The voltage difference between high side (HPUMP H) and ground is more than 3.0 V. - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V. - There is no short to power at low side (HPUMP L) in result of pinpointing.

- - The voltage difference between power and high side (HPUMP H) is less than 1.5 V.

The voltage difference between power and high side (HPUMP H) is less than 1.5 V.

- - The voltage difference between high side (HPUMP H) and ground is more than 3.0 V.

The voltage difference between high side (HPUMP H) and ground is more than 3.0 V.

- - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

- - There is no short to power at low side (HPUMP L) in result of pinpointing.

There is no short to power at low side (HPUMP L) in result of pinpointing.

Short circuit in HPUMP L line (Either malfunction threshold A or B)

- Malfunction threshold A

- - The voltage difference between power and high side (HPUMP H) is more than 1.5 V. - The voltage difference between high side (HPUMP H) and ground is less than 3.0 V. - The voltage difference between low side (HPUMP L) and ground is less than 1.5 V. - The voltage difference between low side (HPUMP L) and ground is less than 3.5 V during pinpointing.

- - The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

- - The voltage difference between high side (HPUMP H) and ground is less than 3.0 V.

The voltage difference between high side (HPUMP H) and ground is less than 3.0 V.

- - The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

- - The voltage difference between low side (HPUMP L) and ground is less than 3.5 V during pinpointing.

The voltage difference between low side (HPUMP L) and ground is less than 3.5 V during pinpointing.

- Malfunction threshold B

- - The voltage difference between power and high side (HPUMP H) is less than 1.5 V. - The voltage difference between high side (HPUMP H) and ground is more than 3.0 V. - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.
````

## Chunk 6027: DTC P2623 (K20C1) (2019 2020 2021)

- Title: DTC P2623 (K20C1) (2019 2020 2021)
- Source path: `pages\7150.html`
- Chunk ID: `chunk_16ba53da762e`
- Images: `images\GHH403637.jpeg`
- Duplicate sources: `pages\8737.html`, `pages\22597.html`, `pages\21010.html`

### Full Text

````text
ence between high side (HPUMP H) and ground is less than 3.0 V.

The voltage difference between high side (HPUMP H) and ground is less than 3.0 V.

- - The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is less than 1.5 V.

- - The voltage difference between low side (HPUMP L) and ground is less than 3.5 V during pinpointing.

The voltage difference between low side (HPUMP L) and ground is less than 3.5 V during pinpointing.

- Malfunction threshold B

- - The voltage difference between power and high side (HPUMP H) is less than 1.5 V. - The voltage difference between high side (HPUMP H) and ground is more than 3.0 V. - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V. - The low side (HPUMP L) current is more than 2.35 A during pinpointing.

- - The voltage difference between power and high side (HPUMP H) is less than 1.5 V.

The voltage difference between power and high side (HPUMP H) is less than 1.5 V.

- - The voltage difference between high side (HPUMP H) and ground is more than 3.0 V.

The voltage difference between high side (HPUMP H) and ground is more than 3.0 V.

- - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

- - The low side (HPUMP L) current is more than 2.35 A during pinpointing.

The low side (HPUMP L) current is more than 2.35 A during pinpointing.

HPUMP H line short to HPUMP L line (Either malfunction threshold A or B)

- Malfunction threshold A

- - The low side (HPUMP L) current is more than 4.8 - 6.32 A during the beginning of actuation.

- - The low side (HPUMP L) current is more than 4.8 - 6.32 A during the beginning of actuation.

The low side (HPUMP L) current is more than 4.8 - 6.32 A during the beginning of actuation.

- Malfunction threshold B

- - Abort of previous actuation due to short circuit. - The voltage difference between power and high side (HPUMP H) is more than 1.5 V. - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V. - The low side (HPUMP L) current is more than 2.35 A during pinpointing.

- - Abort of previous actuation due to short circuit.

Abort of previous actuation due to short circuit.

- - The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

The voltage difference between power and high side (HPUMP H) is more than 1.5 V.

- - The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

The voltage difference between low side (HPUMP L) and ground is more than 1.5 V.

- - The low side (HPUMP L) current is more than 2.35 A during pinpointing.

The low side (HPUMP L) current is more than 2.35 A during pinpointing.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High pressure fuel pump HPUMP H line open

- High pressure fuel pump HPUMP H line short to ground

- High pressure fuel pump HPUMP H line short to power

- High pressure fuel pump HPUMP L line open

- High pressure fuel pump HPUMP L line short to ground

- High pressure fuel pump HPUMP L line short to power

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6028: DTC P2623 (L15B7/L15BA/L15BY)

- Title: DTC P2623 (L15B7/L15BA/L15BY)
- Source path: `pages\7151.html`
- Chunk ID: `chunk_049af53cb1ea`
- Images: `images\GHH403638.jpeg`
- Duplicate sources: `pages\8738.html`, `pages\22598.html`, `pages\21011.html`

### Full Text

````text
# DTC P2623 (L15B7/L15BA/L15BY)

DTC P2623: High Pressure Fuel Pump Spill Valve Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel pressure is adjusted by high pressure fuel pump output ON/OFF which is controlled by the powertrain control module (PCM). In the PCM, the injector driver receives drive commands from the CPU and drives the high pressure fuel pump. The CPU monitors high pressure fuel pump currents and return signal from the injector driver to monitor a terminal voltage of PCM. If the monitored conditions are abnormal for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs at least 100 times (counts 4 times per engine cycle):

- Symptom: High pressure fuel pump current not flowing The pump solenoid current is 0.4 A to 1.5 A or less*.

The pump solenoid current is 0.4 A to 1.5 A or less*.

- Symptom: High pressure fuel pump overcurrent The pump solenoid current is 19.7 A to 30.5 A or more*.

The pump solenoid current is 19.7 A to 30.5 A or more*.

- Symptom: PCM terminal (to high pressure fuel pump) short to ground The PCM terminal (to high pressure fuel pump) voltage is 1.8 V to 2.2 V or less*.

The PCM terminal (to high pressure fuel pump) voltage is 1.8 V to 2.2 V or less*.

- Symptom: PCM terminal (to high pressure fuel pump) short to power The PCM terminal (to high pressure fuel pump) voltage is (12 volt battery voltage - 3.2) V to (12 volt battery voltage - 2.2) V or more*.

The PCM terminal (to high pressure fuel pump) voltage is (12 volt battery voltage - 3.2) V to (12 volt battery voltage - 2.2) V or more*.

*: Varies with driving condition.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- High pressure fuel pump failure

- High pressure fuel pump HPUMP H line open

- High pressure fuel pump HPUMP H line short to ground

- High pressure fuel pump HPUMP H line short to power

- High pressure fuel pump HPUMP L line open

- High pressure fuel pump HPUMP L line short to ground

- High pressure fuel pump HPUMP L line short to power

- Injector relay failure

- PCM internal circuit failure (injector driver power supply line open)

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6029: DTC P2626 (K20C1) (2017 2018 2019)

- Title: DTC P2626 (K20C1) (2017 2018 2019)
- Source path: `pages\7152.html`
- Chunk ID: `chunk_bb0782ebbe45`
- Images: `images\GHH403639.jpeg`, `images\GHH403640.jpeg`
- Duplicate sources: `pages\8739.html`, `pages\22599.html`, `pages\21012.html`

### Full Text

````text
# DTC P2626 (K20C1) (2017 2018 2019)

DTC P2626: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit (LAF-CA, LAFCP) Open Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If an open in A/F sensor (sensor 1) circuit (LAF CP line) is detected, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects an open circuit in A/F sensor (sensor 1) LAF CP line or LAF CA line for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) LAF CP line open

- A/F sensor (sensor 1) LAF CA line open

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6030: DTC P2626 (K20C1) (2019 2020 2021)

- Title: DTC P2626 (K20C1) (2019 2020 2021)
- Source path: `pages\7153.html`
- Chunk ID: `chunk_e7dd1757ddc8`
- Images: `images\GHH403641.jpeg`, `images\GHH403642.jpeg`
- Duplicate sources: `pages\8740.html`, `pages\22600.html`, `pages\21013.html`

### Full Text

````text
# DTC P2626 (K20C1) (2019 2020 2021)

DTC P2626: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit (LAF-CA, LAFCP) Open Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The driver IC for air/fuel ratio (A/F) sensor (sensor 1) is built into the powertrain control module (PCM). The diagnosis data acquired by the driver IC are called up directly by application specific integrated circuit (ASIC) chip and are considered along with the measured values in order to detect faults in the system and the sensor. At the same time, a distinction is made between SPI faults (transmission faults), chip faults (ex. incorrect placement of components or faulty driver IC), short circuits, as well as overloads at the individual pins. If the calculated parallel resistance between LAF CP and LAF CA is a specified value, the PCM stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

Other | A/F sensor (sensor 1) is in active condition (heated up enough)

[ ]: HDS Parameter

Malfunction Threshold

The calculated parallel resistance between LAF CP and LAF CA is greater than 296 Ω.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) LAF CP line open

- A/F sensor (sensor 1) LAF CA line open

- A/F sensor (sensor 1) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6031: DTC P2646 (K20C2)

- Title: DTC P2646 (K20C2)
- Source path: `pages\7154.html`
- Chunk ID: `chunk_44417ce5bfd6`
- Images: `images\GHH403643.jpeg`
- Duplicate sources: `pages\8741.html`, `pages\22601.html`, `pages\21014.html`

### Full Text

````text
# DTC P2646 (K20C2)

DTC P2646: Rocker Arm Oil Pressure Switch Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Logic Decision | Rocker Arm Oil Pressure Switch

"ON" | "OFF"

Rocker Arm Oil Control Solenoid Command "ON" | Failure | Normal

Rocker Arm Oil Control Solenoid Command "OFF" | Normal | Failure

The VTEC system activates the rocker arm oil control solenoid with a command from the powertrain control module (PCM), and it charges/discharges the hydraulic circuit of the VTEC mechanism that switches valve timing between Low and High. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch downstream of the rocker arm oil control solenoid. If there is a difference between the oil pressure condition in the hydraulic circuit determined by the PCM command and the oil pressure condition determined by the status of the rocker arm oil pressure switch, the system is considered faulty, and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 16 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 86 deg.F (30 deg.C) | -

Engine speed [ENGINE SPEED]*, * 1 | 1, 150 rpm | -

Engine speed [ENGINE SPEED]*, * 2 | 1, 400 rpm | -

Vehicle speed [VEHICLE SPEED] | 10 mph (15 km/h) | -

*: Variable that is depending on the engine load.

*1: CVT model

*2: M/T model

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Shift lever position* 1 | Other than P or N

*: Variable that is depending on the engine load.

*1: CVT model

*2: M/T model

[ ]: HDS Parameter

Malfunction Threshold

When the rocker arm oil control solenoid is ON, the rocker arm oil pressure switch remains ON.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid failure

- Rocker arm oil control solenoid VTS line open

- Rocker arm oil control solenoid VTS line short

- Rocker arm oil pressure switch failure

- Rocker arm oil pressure switch VTM line open

- Rocker arm oil pressure switch VTM line short

- Oil passage clogged

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] 1, 400 rpm or more for at least 16 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Do the VTEC TEST in the INSPECTION MENU with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6032: DTC P2647 (K20C2)

- Title: DTC P2647 (K20C2)
- Source path: `pages\7155.html`
- Chunk ID: `chunk_3ffd97bcf774`
- Images: `images\GHH403644.jpeg`
- Duplicate sources: `pages\8742.html`, `pages\22602.html`, `pages\21015.html`

### Full Text

````text
# DTC P2647 (K20C2)

DTC P2647: Rocker Arm Oil Pressure Switch Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Logic Decision | Rocker Arm Oil Pressure Switch

"ON" | "OFF"

Rocker Arm Oil Control Solenoid Command "ON" | Failure | Normal

Rocker Arm Oil Control Solenoid Command "OFF" | Normal | Failure

The VTEC system activates the rocker arm oil control solenoid with a command from the powertrain control module (PCM), and it charges/discharges the hydraulic circuit of the VTEC mechanism that switches valve timing between Low and High. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch downstream of the rocker arm oil control solenoid. If there is a difference between the oil pressure condition in the hydraulic circuit determined by the PCM command and the oil pressure condition determined by the status of the rocker arm oil pressure switch, the system is considered faulty, and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | At idle

[ ]: HDS Parameter

Malfunction Threshold

When the rocker arm oil control solenoid is OFF, the rocker arm oil pressure switch remains OFF.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid failure

- Rocker arm oil control solenoid VTS line open

- Rocker arm oil control solenoid VTS line short

- Rocker arm oil pressure switch failure

- Rocker arm oil pressure switch VTM line open

- Rocker arm oil pressure switch VTM line short

- Oil passage clogged

Confirmation Procedure

Operating Condition

Start the engine, and let it idle for at least 3 seconds.

With the HDS

Do the VTEC TEST in the INSPECTION MENU with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6033: DTC P2648, P2649 (K20C2)

- Title: DTC P2648, P2649 (K20C2)
- Source path: `pages\7156.html`
- Chunk ID: `chunk_c9caf0b06e0f`
- Images: `images\GHH403645.jpeg`
- Duplicate sources: `pages\8743.html`, `pages\22603.html`, `pages\21016.html`

### Full Text

````text
# DTC P2648, P2649 (K20C2)

DTC P2648: Rocker Arm Oil Control Solenoid Circuit Low Voltage

DTC P2649: Rocker Arm Oil Control Solenoid Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The VTEC system activates the rocker arm oil control solenoid by a command from the powertrain control module (PCM), and it charges/discharges the hydraulic circuit of the VTEC mechanism that switches valve timing between low and high. If the return signal is OFF (low) when the PCM outputs the ON (high) signal to the rocker arm oil control solenoid or the return signal is ON (high) when the PCM outputs the OFF (low) signal to the rocker arm oil control solenoid, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

DTC: P2648

The return signal is OFF (low) for at least 2.0 seconds when the PCM outputs the ON (high) signal to the rocker arm oil control solenoid.

DTC: P2649

The return signal is ON (high) for at least 2.0 seconds when the PCM outputs the OFF (low) signal to the rocker arm oil control solenoid.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2648

- Rocker arm oil control solenoid VTS line short to ground

DTC: P2649

- Rocker arm oil control solenoid VTS line open

- Rocker arm oil control solenoid ground line open

Common

- Rocker arm oil control solenoid failure

- PCM internal circuit failure

Confirmation Procedure

DTC: P2648

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a steady engine speed [ENGINE SPEED] at 1, 400 rpm or more with a vehicle speed [VEHICLE SPEED] at 10 mph (15 km/h) or more for at least 16 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Do the VTEC TEST in the INSPECTION MENU with the HDS.

DTC: P2649

Operating Condition

Start the engine, and let it idle for at least 3 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6034: DTC P2650 (K20C1) (2017 2018 2019)

- Title: DTC P2650 (K20C1) (2017 2018 2019)
- Source path: `pages\7157.html`
- Chunk ID: `chunk_0dcacc2701ed`
- Images: `images\GHH403646.jpeg`
- Duplicate sources: `pages\8744.html`, `pages\22604.html`, `pages\21017.html`

### Full Text

````text
# DTC P2650 (K20C1) (2017 2018 2019)

DTC P2650: Rocker Arm Oil Control Solenoid Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The rocker arm oil control solenoid control circuit is monitored for electrical malfunctions. The PCM detects a short circuit to ground, short circuit to power, and open circuit. If the rocker arm oil control solenoid output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage (power voltage input to PCM) | 8 V | 16 V

[ ]: HDS Parameter

Malfunction Threshold

The rocker arm oil control solenoid output voltage lies between 2.2 V and 2.8 V for at least 0.5 second during rocker arm oil control solenoid is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid VTSEX line open

- Rocker arm oil control solenoid ground line open

- Rocker arm oil control solenoid failure

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

## Chunk 6035: DTC P2650 (K20C1) (2019 2020 2021)

- Title: DTC P2650 (K20C1) (2019 2020 2021)
- Source path: `pages\7158.html`
- Chunk ID: `chunk_ee0c53d26750`
- Images: `images\GHH403647.jpeg`
- Duplicate sources: `pages\8745.html`, `pages\22605.html`, `pages\21018.html`

### Full Text

````text
# DTC P2650 (K20C1) (2019 2020 2021)

DTC P2650: Rocker Arm Oil Control Solenoid Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The rocker arm oil control solenoid control circuit is monitored for electrical malfunctions. The PCM detects a short circuit to ground, short circuit to power, and open circuit. If the rocker arm oil control solenoid output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] (power voltage input to PCM) | 8 V | 16 V

Other | Rocker arm oil control solenoid power stage off

[ ]: HDS Parameter

Malfunction Threshold

The rocker arm oil control solenoid output voltage is between 0 - 2.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid VTSEX line open

- Rocker arm oil control solenoid ground line open

- Rocker arm oil control solenoid failure

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

## Chunk 6036: DTC P2651 (K20C1) (2017 2018 2019)

- Title: DTC P2651 (K20C1) (2017 2018 2019)
- Source path: `pages\7159.html`
- Chunk ID: `chunk_ba75f19f370e`
- Images: `images\GHH403648.jpeg`
- Duplicate sources: `pages\8746.html`, `pages\22606.html`, `pages\21019.html`

### Full Text

````text
# DTC P2651 (K20C1) (2017 2018 2019)

DTC P2651: Rocker Arm Oil Pressure Switch Performance/Stuck off

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch. If the time required for switching the cam lift exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine oil temperature [Engine Oil Temperature] | 50 deg.F (9.96 deg.C) | -

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage (power voltage input to PCM) [Battery] | 10 V | -

[ ]: HDS Parameter

Malfunction Threshold

The time required for switching the cam lift exceeds 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid stuck

- Rocker arm oil pressure switch VTMEX line open

- Rocker arm oil control valve failure

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

## Chunk 6037: DTC P2651 (K20C1) (2019 2020 2021)

- Title: DTC P2651 (K20C1) (2019 2020 2021)
- Source path: `pages\7160.html`
- Chunk ID: `chunk_d4ce568915e1`
- Images: `images\GHH403649.jpeg`
- Duplicate sources: `pages\8747.html`, `pages\22607.html`, `pages\21020.html`

### Full Text

````text
# DTC P2651 (K20C1) (2019 2020 2021)

DTC P2651: Rocker Arm Oil Pressure Switch Performance/Stuck off

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch. If the switching is active despite there is no feedback from rocker arm oil pressure switch, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | -238.07 deg.F (-150.04 deg.C) | 302.1 deg.F (150.06 deg.C)

Engine oil temperature [Engine Oil Temperature] | 49.93 deg.F (9.96 deg.C) | 5, 438.4 deg.F (3, 003.56 deg.C)

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] | 10 V | 15.1 V

[ ]: HDS Parameter

Malfunction Threshold

Despite there is no feedback from rocker arm oil pressure switch, the switching is active for at least 500 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid stuck

- Rocker arm oil pressure switch VTMEX line open

- Rocker arm oil control valve failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6038: DTC P2652 (K20C1) (2017 2018 2019)

- Title: DTC P2652 (K20C1) (2017 2018 2019)
- Source path: `pages\7161.html`
- Chunk ID: `chunk_25f7ddd755cf`
- Images: `images\GHH403650.jpeg`
- Duplicate sources: `pages\8748.html`, `pages\22608.html`, `pages\21021.html`

### Full Text

````text
# DTC P2652 (K20C1) (2017 2018 2019)

DTC P2652: Rocker Arm Oil Pressure Switch Stuck on

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch. If the time required for switching the cam lift exceeds a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine oil temperature [Engine Oil Temperature] | 50 deg.F (9.96 deg.C) | -

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage (power voltage input to PCM) [Battery] | 10 V | -

[ ]: HDS Parameter

Malfunction Threshold

The time required for switching the cam lift exceeds 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid stuck

- Rocker arm oil pressure switch VTMEX line short

- Rocker arm oil control valve failure

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

## Chunk 6039: DTC P2652 (K20C1) (2019 2020 2021)

- Title: DTC P2652 (K20C1) (2019 2020 2021)
- Source path: `pages\7162.html`
- Chunk ID: `chunk_eb3ae2812eb9`
- Images: `images\GHH403651.jpeg`
- Duplicate sources: `pages\8749.html`, `pages\22609.html`, `pages\21022.html`

### Full Text

````text
# DTC P2652 (K20C1) (2019 2020 2021)

DTC P2652: Rocker Arm Oil Pressure Switch Stuck on

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The PCM monitors oil pressure in the hydraulic circuit of the VTEC mechanism using the rocker arm oil pressure switch. If the switching is not active despite there is a feedback from rocker arm oil pressure switch, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine coolant temperature [ECT Sensor 1] | -238.07 deg.F (-150.04 deg.C) | 302.1 deg.F (150.06 deg.C)

Engine oil temperature [Engine Oil Temperature] | 49.93 deg.F (9.96 deg.C) | 5, 438.4 deg.F (3, 003.56 deg.C)

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] | 10 V | 15.1 V

[ ]: HDS Parameter

Malfunction Threshold

Despite there is a feedback from rocker arm oil pressure switch, the switching is not active for at least 500 milliseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Rocker arm oil control solenoid stuck

- Rocker arm oil pressure switch VTMEX line short

- Rocker arm oil control valve failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6040: DTC P2653, P2654 (K20C1) (2017 2018 2019)

- Title: DTC P2653, P2654 (K20C1) (2017 2018 2019)
- Source path: `pages\7163.html`
- Chunk ID: `chunk_5d5a3fb02eb2`
- Images: `images\GHH403652.jpeg`
- Duplicate sources: `pages\8750.html`, `pages\22610.html`, `pages\21023.html`

### Full Text

````text
# DTC P2653, P2654 (K20C1) (2017 2018 2019)

DTC P2653: Rocker Arm Oil Control Solenoid Circuit Low Voltage

DTC P2654: Rocker Arm Oil Control Solenoid Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The rocker arm oil control solenoid control circuit is monitored for electrical malfunctions. The PCM detects a short circuit to ground, short circuit to power, and open circuit. If the rocker arm oil control solenoid output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] (power voltage input to PCM) | 8 V | 16 V

[ ]: HDS Parameter

Malfunction Threshold

DTC: P2653

The rocker arm oil control solenoid output voltage is less than 2.2 V for at least 0.5 second during the rocker arm oil control solenoid is off.

DTC: P2654

The rocker arm oil control solenoid output voltage is greater than 2.8 V for at least 0.5 second during the rocker arm oil control solenoid is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2653

- Rocker arm oil control solenoid VTSEX line short to ground

DTC: P2654

- Rocker arm oil control solenoid VTSEX line short to power

Common

- Rocker arm oil control solenoid failure

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

## Chunk 6041: DTC P2653, P2654 (K20C1) (2019 2020 2021)

- Title: DTC P2653, P2654 (K20C1) (2019 2020 2021)
- Source path: `pages\7164.html`
- Chunk ID: `chunk_b39595d0b0ad`
- Images: `images\GHH403653.jpeg`
- Duplicate sources: `pages\8751.html`, `pages\22611.html`, `pages\21024.html`

### Full Text

````text
# DTC P2653, P2654 (K20C1) (2019 2020 2021)

DTC P2653: Rocker Arm Oil Control Solenoid Circuit Low Voltage

DTC P2654: Rocker Arm Oil Control Solenoid Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the switching of the exhaust valve timing by actuating the rocker arm oil control solenoid. The rocker arm oil control solenoid control circuit is monitored for electrical malfunctions. The PCM detects a short circuit to ground, short circuit to power, and open circuit. If the rocker arm oil control solenoid output voltage is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] (power voltage input to PCM) | 8 V | 16 V

Other | Rocker arm oil control solenoid power stage off

[ ]: HDS Parameter

Malfunction Threshold

DTC: P2653

The rocker arm oil control solenoid output voltage is between 2.2 - 2.8 V.

DTC: P2654

The rocker arm oil control solenoid output voltage is between 2.8 - 5.0 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P2653

- Rocker arm oil control solenoid VTSEX line short to ground

DTC: P2654

- Rocker arm oil control solenoid VTSEX line short to power

Common

- Rocker arm oil control solenoid failure

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

## Chunk 6042: DTC P2A00 (K20C2)

- Title: DTC P2A00 (K20C2)
- Source path: `pages\7165.html`
- Chunk ID: `chunk_e0c9ce913d17`
- Images: `images\GHH403654.jpeg`, `images\GHH403655.jpeg`
- Duplicate sources: `pages\8752.html`, `pages\22612.html`, `pages\21025.html`

### Full Text

````text
# DTC P2A00 (K20C2)

DTC P2A00: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) has a linear signal output in relation to the oxygen concentration. The powertrain control module (PCM) computes the air/fuel ratio from the A/F sensor (sensor 1) output voltage and uses fuel feedback control to improve exhaust emissions. The PCM monitors the A/F sensor (sensor 1) output voltage during deceleration with the throttle fully closed, and if the output voltage deviates greatly from normal oxygen concentration levels, it detects a malfunction and stores a DTC.

NOTE: Output to the scan tool exhibits a relationship between the A/F sensor (sensor 1) output and oxygen concentration, which is opposite to the characteristic shown in the graph. That is, a deviation toward the rich side increases the output voltage and one toward the lean side decreases the output voltage, as the stoichiometric ratio is 0.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 4.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Engine speed [ENGINE SPEED] | 500 rpm | 3, 200 rpm

Vehicle speed [VEHICLE SPEED] | 30 mph (48 km/h) | -

Fuel feedback | During deceleration

[ ]: HDS Parameter

Malfunction Threshold

The A/F sensor (sensor 1) output voltage is 2.55 V or less, or 4.11 V or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) deterioration

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 25 - 55 mph (40 - 88 km/h) for at least 5 minutes.

- Drive immediately at a steady speed between 55 - 75 mph (88 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6043: DTC P2A00 (Without XM)

- Title: DTC P2A00 (Without XM)
- Source path: `pages\7166.html`
- Chunk ID: `chunk_2fe6ea5c1718`
- Images: `images\GHH403656.jpeg`, `images\GHH403657.jpeg`
- Duplicate sources: `pages\8753.html`, `pages\22613.html`, `pages\21026.html`

### Full Text

````text
# DTC P2A00 (Without XM)

DTC P2A00: Air/Fuel Ratio (A/F) Sensor (Sensor 1) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The air/fuel ratio (A/F) sensor (sensor 1) has a linear signal output in relation to the oxygen concentration. The powertrain control module (PCM) computes the air/fuel ratio from the A/F sensor (sensor 1) output voltage and uses fuel feedback control to improve exhaust emissions. The PCM monitors the A/F sensor (sensor 1) output voltage during deceleration with the throttle fully closed, and if the output voltage deviates greatly from normal oxygen concentration levels, it detects a malfunction and stores a DTC.

NOTE: :Output to the scan tool exhibits a relationship between the A/F sensor (sensor 1) output and oxygen concentration, which is opposite to the characteristic shown in the graph. That is, a deviation toward the rich side increases the output voltage and one toward the lean side decreases the output voltage, as the stoichiometric ratio is 0.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT sensor (1)] | -13 deg.F (-25 deg.C) | -

Engine speed [ENGINE SPEED] | 500 rpm | 2, 700 rpm

Vehicle speed [VEHICLE SPEED] | 30 mph (48 km/h) | -

Fuel feedback | During deceleration with throttle fully closed

[ ]: HDS Parameter

Malfunction Threshold

The A/F sensor (sensor 1) output voltage is 2.55 V or less, or 4.11 V or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- A/F sensor (sensor 1) failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 25 - 55 mph (41 - 88 km/h) for at least 5 minutes.

- Drive immediately at a steady speed between 55 - 75 mph (89 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed for at least 4 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6044: DTC P2A01 (K20C2) (2018 2019 2020 2021)

- Title: DTC P2A01 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\7167.html`
- Chunk ID: `chunk_e093bac952d9`
- Images: `images\GHH403658.jpeg`
- Duplicate sources: `pages\8754.html`, `pages\22614.html`, `pages\21027.html`

### Full Text

````text
# DTC P2A01 (K20C2) (2018 2019 2020 2021)

DTC P2A01: Secondary Heated Oxygen Sensor (Secondary HO2S) (Sensor 2) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The secondary heated oxygen sensor (secondary HO2S (sensor 2)) detects the oxygen density in the exhaust gas and converts it into electrical signals. If the secondary HO2S (sensor 2) output voltage is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Secondary HO2S (sensor 2) output voltage [HO2S S2] | - | 1.0 V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) output voltage [HO2S S2] is 1.54 V or less for at least 6 seconds after the secondary HO2S (sensor 2) is judged that it is normally activated (1.0 V or less as a value).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6045: DTC P2A01 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P2A01 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\7168.html`
- Chunk ID: `chunk_111c5f17f5bf`
- Images: `images\GHH403659.jpeg`
- Duplicate sources: `pages\8755.html`, `pages\22615.html`, `pages\21028.html`

### Full Text

````text
# DTC P2A01 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P2A01: Secondary Heated Oxygen Sensor (Secondary HO2S) (Sensor 2) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The secondary heated oxygen sensor (secondary HO2S (sensor 2)) detects the oxygen density in the exhaust gas and converts it into electrical signals. If the secondary HO2S (sensor 2) output voltage is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Secondary HO2S (sensor 2) output voltage [HO2S S2] | - | 1.0 V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) output voltage [HO2S S2] is 1.54 V or less for at least 6 seconds after the secondary HO2S (sensor 2) is judged that it is normally activated (1.0 V or less as a value).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6046: DTC P2A01 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P2A01 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\7169.html`
- Chunk ID: `chunk_5d4f3fba3237`
- Images: `images\GHH403660.jpeg`
- Duplicate sources: `pages\8756.html`, `pages\22616.html`, `pages\21029.html`

### Full Text

````text
# DTC P2A01 (Si) (2017 2018 2019 2020 2021)

DTC P2A01: Secondary Heated Oxygen Sensor (Secondary HO2S) (Sensor 2) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The secondary heated oxygen sensor (secondary HO2S (sensor 2)) detects the oxygen density in the exhaust gas and converts it into electrical signals. If the secondary HO2S (sensor 2) output voltage is a specified range for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Secondary HO2S (sensor 2) output voltage [HO2S S2] | - | 1.0 V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) output voltage [HO2S S2] is a specified range for few seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6047: DTC P2DE0 (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P2DE0 (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\7170.html`
- Chunk ID: `chunk_4e8767bb8471`
- Images: `images\GHH403661.jpeg`, `images\GHH403662.jpeg`, `images\GHH403663.jpeg`
- Duplicate sources: `pages\8757.html`, `pages\22617.html`, `pages\21030.html`

### Full Text

````text
# DTC P2DE0 (L15B7/L15BA/L15BY) (2020 2021)

DTC P2DE0: Cold Start Air Fuel Ratio Control System Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The cold start emission reduction strategy controls air fuel ratio to lean when the engine is started at cold condition to lower the emission while the catalyst is not warmed up enough. If the actual air fuel ratio is too lean or too rich compared to the commanded air fuel ratio, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

A/F sensor | Active

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The ratio of actual air fuel ratio by commanded air fuel ratio is 0.87 or less.

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

## Chunk 6048: DTC P2DE1 (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P2DE1 (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\7171.html`
- Chunk ID: `chunk_408c0619d3f0`
- Images: `images\GHH403664.jpeg`, `images\GHH403665.jpeg`, `images\GHH403666.jpeg`
- Duplicate sources: `pages\8758.html`, `pages\22618.html`, `pages\21031.html`

### Full Text

````text
# DTC P2DE1 (L15B7/L15BA/L15BY) (2020 2021)

DTC P2DE1: Cold Start Air Fuel Ratio Control System Rich

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The cold start emission reduction strategy controls air fuel ratio to lean when the engine is started at cold condition to lower the emission while the catalyst is not warmed up enough. If the actual air fuel ratio is too lean or too rich compared to the commanded air fuel ratio, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

A/F sensor | Active

Other | Vehicle stopped

[ ]: HDS Parameter

Malfunction Threshold

The ratio of actual air fuel ratio by commanded air fuel ratio is 1.29 or more.

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

## Chunk 6049: DTC U0029 (K20C1 (PGM-FI System)) (2017 2018 2019)

- Title: DTC U0029 (K20C1 (PGM-FI System)) (2017 2018 2019)
- Source path: `pages\7172.html`
- Chunk ID: `chunk_6567d9982df1`
- Images: `images\GHH403667.jpeg`
- Duplicate sources: `pages\8759.html`, `pages\22619.html`, `pages\21032.html`

### Full Text

````text
# DTC U0029 (K20C1 (PGM-FI System)) (2017 2018 2019)

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). The busoff error is checked for CAN bus node. If a permanent busoff defection is detected, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.0 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects a busoff error (no message over the CAN node can be transmitted or received) for at least 1.0 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6050: DTC U0029 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0029 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7173.html`
- Chunk ID: `chunk_bdbdf5a3f416`
- Images: `images\GHH403668.jpeg`
- Duplicate sources: `pages\8760.html`, `pages\22620.html`, `pages\21033.html`

### Full Text

````text
# DTC U0029 (K20C1 (PGM-FI System)) (2019)

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). The busoff error is checked for CAN bus node. If a permanent busoff defection is detected, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Busoff error status for CAN node is set for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6051: DTC U0029 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0029 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7174.html`
- Chunk ID: `chunk_c83078d41dc3`
- Images: `images\GHH403669.jpeg`
- Duplicate sources: `pages\8761.html`, `pages\22621.html`, `pages\21034.html`

### Full Text

````text
# DTC U0029 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). The busoff error is checked for CAN bus node. If a permanent busoff defection is detected, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Busoff error status for CAN node is set for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6052: DTC U0029 (K20C2: With CAN gateway (PGM-FI System))

- Title: DTC U0029 (K20C2: With CAN gateway (PGM-FI System))
- Source path: `pages\7175.html`
- Chunk ID: `chunk_ff7d8fa52275`
- Images: `images\GHH403670.jpeg`
- Duplicate sources: `pages\8762.html`, `pages\22622.html`, `pages\21035.html`

### Full Text

````text
# DTC U0029 (K20C2: With CAN gateway (PGM-FI System))

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) cannot send the signals via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot send any signals via the F-CAN A lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6053: DTC U0029 (K20C2: Without CAN gateway (PGM-FI System))

- Title: DTC U0029 (K20C2: Without CAN gateway (PGM-FI System))
- Source path: `pages\7176.html`
- Chunk ID: `chunk_b457f09f0fb6`
- Images: `images\GHH403671.jpeg`
- Duplicate sources: `pages\8763.html`, `pages\22623.html`, `pages\21036.html`

### Full Text

````text
# DTC U0029 (K20C2: Without CAN gateway (PGM-FI System))

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) cannot send the signals via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot send any signals via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6054: DTC U0029 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

- Title: DTC U0029 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))
- Source path: `pages\7177.html`
- Chunk ID: `chunk_df6e3ee0597a`
- Images: `images\GHH403672.jpeg`
- Duplicate sources: `pages\8764.html`, `pages\22624.html`, `pages\21037.html`

### Full Text

````text
# DTC U0029 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) cannot send the signals via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot send any signals via the F-CAN A lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6055: DTC U0029 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

- Title: DTC U0029 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))
- Source path: `pages\7178.html`
- Chunk ID: `chunk_c4541bcd7c27`
- Images: `images\GHH403673.jpeg`
- Duplicate sources: `pages\8765.html`, `pages\22625.html`, `pages\21038.html`

### Full Text

````text
# DTC U0029 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

DTC U0029: F-CAN Malfunction (BUS-OFF (Powertrain Control Module (PCM)))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) cannot send the signals via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot send any signals via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6056: DTC U0038 (K20C2: CVT model (PGM-FI System))

- Title: DTC U0038 (K20C2: CVT model (PGM-FI System))
- Source path: `pages\7179.html`
- Chunk ID: `chunk_d3aa64e6e6a2`
- Images: `images\GHH403674.jpeg`
- Duplicate sources: `pages\8766.html`, `pages\22626.html`, `pages\21039.html`

### Full Text

````text
# DTC U0038 (K20C2: CVT model (PGM-FI System))

DTC U0038: PT-CAN Malfunction (TCM ECU BUS-OFF)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulse signals to/from the control modules simultaneously by using two signal lines (TM-CAN_H and TM-CAN_L). When the information is not sent from the transmission control module (TCM) unit via the TM-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the TM-CAN lines for at least 1.5 seconds.

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

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6057: DTC U0038 (L15B7/L15BA: CVT model (PGM-FI System))

- Title: DTC U0038 (L15B7/L15BA: CVT model (PGM-FI System))
- Source path: `pages\7180.html`
- Chunk ID: `chunk_a778bdd87355`
- Images: `images\GHH403675.jpeg`
- Duplicate sources: `pages\8767.html`, `pages\22627.html`, `pages\21040.html`

### Full Text

````text
# DTC U0038 (L15B7/L15BA: CVT model (PGM-FI System))

DTC U0038: PT-CAN Malfunction (TCM ECU BUS-OFF)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulse signals to/from the control modules simultaneously by using two signal lines (TM-CAN_H and TM-CAN_L). When the information is not sent from the transmission control module (TCM) unit via the TM-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the TM-CAN lines for at least 1.5 seconds.

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

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6058: DTC U0101 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0101 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\7181.html`
- Chunk ID: `chunk_8adf17626f49`
- Images: `images\GHH403676.jpeg`
- Duplicate sources: `pages\8768.html`, `pages\22628.html`, `pages\21041.html`

### Full Text

````text
# DTC U0101 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-TCM)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the transmission control module (TCM) unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN A lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6059: DTC U0101 (K20C2 (CVT) without CAN gateway)

- Title: DTC U0101 (K20C2 (CVT) without CAN gateway)
- Source path: `pages\7182.html`
- Chunk ID: `chunk_d718a8422fae`
- Images: `images\GHH403677.jpeg`
- Duplicate sources: `pages\8769.html`, `pages\22629.html`, `pages\21042.html`

### Full Text

````text
# DTC U0101 (K20C2 (CVT) without CAN gateway)

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-TCM)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the transmission control module (TCM) unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6060: DTC U0101 (K20C2: With CAN gateway) (2019 2020 2021)

- Title: DTC U0101 (K20C2: With CAN gateway) (2019 2020 2021)
- Source path: `pages\7183.html`
- Chunk ID: `chunk_c1b31f91d232`
- Images: `images\GHH403678.jpeg`
- Duplicate sources: `pages\8770.html`, `pages\22630.html`, `pages\21043.html`

### Full Text

````text
# DTC U0101 (K20C2: With CAN gateway) (2019 2020 2021)

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-TCM)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the transmission control module (TCM) via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the TCM via the F-CAN lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- TCM failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6061: DTC U0101 (L15B7/L15BA/L15BY (CVT) with CAN gateway (12P connector type))

- Title: DTC U0101 (L15B7/L15BA/L15BY (CVT) with CAN gateway (12P connector type))
- Source path: `pages\7184.html`
- Chunk ID: `chunk_4e0f1fb1301a`
- Images: `images\GHH403679.jpeg`
- Duplicate sources: `pages\8771.html`, `pages\22631.html`, `pages\21044.html`

### Full Text

````text
# DTC U0101 (L15B7/L15BA/L15BY (CVT) with CAN gateway (12P connector type))

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-Transmission Control Module (TCM))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the transmission control module (TCM) unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines unit for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6062: DTC U0101 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

- Title: DTC U0101 (L15B7/L15BA/L15BY (CVT) without CAN gateway)
- Source path: `pages\7185.html`
- Chunk ID: `chunk_e641a730c1fb`
- Images: `images\GHH403680.jpeg`
- Duplicate sources: `pages\8772.html`, `pages\22632.html`, `pages\21045.html`

### Full Text

````text
# DTC U0101 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-Transmission Control Module (TCM))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the transmission control module (TCM) unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TCM failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6063: DTC U0101 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0101 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7186.html`
- Chunk ID: `chunk_2bf0a993a530`
- Images: `images\GHH403681.jpeg`
- Duplicate sources: `pages\8773.html`, `pages\22633.html`, `pages\21046.html`

### Full Text

````text
# DTC U0101 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0101: F-CAN Malfunction (Powertrain Control Module (PCM)-Transmission Control Module (TCM))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the transmission control module (TCM) via the F-CAN lines and this condition continues for a specified time or when the information sent from the TCM is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the TCM via the F-CAN lines unit for at least 1.5 seconds.

- The information sent from the TCM unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- TCM failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected the MIL comes on and a Pending DTC, Confirmed DTC and the freeze data are stored are stored in the PCM memory.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6064: DTC U0104 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0104 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7187.html`
- Chunk ID: `chunk_683f5bf71181`
- Images: `images\GHH403682.jpeg`
- Duplicate sources: `pages\8774.html`, `pages\22634.html`, `pages\21047.html`

### Full Text

````text
# DTC U0104 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0104: F-CAN Malfunction (Powertrain Control Module (PCM)-Driving Support System Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_ H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the millimeter wave radar via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- Millimeter wave radar failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6065: DTC U0104 (K20C2: With CAN gateway) (2016 2017 2018)

- Title: DTC U0104 (K20C2: With CAN gateway) (2016 2017 2018)
- Source path: `pages\7188.html`
- Chunk ID: `chunk_77aed71a1d1e`
- Images: `images\GHH403683.jpeg`
- Duplicate sources: `pages\8775.html`, `pages\22635.html`, `pages\21048.html`

### Full Text

````text
# DTC U0104 (K20C2: With CAN gateway) (2016 2017 2018)

DTC U0104: F-CAN Malfunction (Powertrain Control Module (PCM)-Driving Support System Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the multipurpose camera unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the multipurpose camera unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN B lines for at least 1.5 seconds.

- The information sent from the multipurpose camera unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Multipurpose camera unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6066: DTC U0104 (K20C2: With CAN gateway) (2019 2020 2021)

- Title: DTC U0104 (K20C2: With CAN gateway) (2019 2020 2021)
- Source path: `pages\7189.html`
- Chunk ID: `chunk_277919ac16b2`
- Images: `images\GHH403684.jpeg`
- Duplicate sources: `pages\8776.html`, `pages\22636.html`, `pages\21049.html`

### Full Text

````text
# DTC U0104 (K20C2: With CAN gateway) (2019 2020 2021)

DTC U0104: F-CAN Malfunction (Powertrain Control Module (PCM)-Driving Support System Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the millimeter wave radar via the F-CAN lines and this condition continues for a specified time or when the information sent from the millimeter wave radar is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the millimeter wave radar via the F-CAN lines for at least 1.5 seconds.

- The information sent from the millimeter wave radar is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- Millimeter wave radar failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6067: DTC U0104 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))

- Title: DTC U0104 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))
- Source path: `pages\7190.html`
- Chunk ID: `chunk_b8f1dd0c3e40`
- Images: `images\GHH403685.jpeg`
- Duplicate sources: `pages\8777.html`, `pages\22637.html`, `pages\21050.html`

### Full Text

````text
# DTC U0104 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))

DTC U0104: F-CAN Malfunction (Powertrain Control Module (PCM)-Driving Support System Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the multipurpose camera unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the multipurpose camera unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the multipurpose camera unit is abnormal at least 20 times.

Possible Cause

- Multipurpose camera unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6068: DTC U0104 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0104 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7191.html`
- Chunk ID: `chunk_20f16fafadb6`
- Images: `images\GHH403686.jpeg`
- Duplicate sources: `pages\8778.html`, `pages\22638.html`, `pages\21051.html`

### Full Text

````text
# DTC U0104 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0104: F-CAN Malfunction (Powertrain Control Module (PCM)-Driving Support System Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the millimeter wave radar via the F-CAN lines and this condition continues for a specified time or when the information sent from the millimeter wave radar is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the millimeter wave radar via the F-CAN lines for at least 1.5 seconds.

- The information sent from the millimeter wave radar is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- Millimeter wave radar failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6069: DTC U0122 (K20C1 (PGM-FI System)) (2017 2018 2019)

- Title: DTC U0122 (K20C1 (PGM-FI System)) (2017 2018 2019)
- Source path: `pages\7192.html`
- Chunk ID: `chunk_6b2368d957f3`
- Images: `images\GHH403687.jpeg`
- Duplicate sources: `pages\8779.html`, `pages\22639.html`, `pages\21052.html`

### Full Text

````text
# DTC U0122 (K20C1 (PGM-FI System)) (2017 2018 2019)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error The counter value in the message received in the present frame is same as the value received in the previous frame.

The counter value in the message received in the present frame is same as the value received in the previous frame.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6070: DTC U0122 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0122 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7193.html`
- Chunk ID: `chunk_f16a8058ae38`
- Images: `images\GHH403688.jpeg`
- Duplicate sources: `pages\8780.html`, `pages\22640.html`, `pages\21053.html`

### Full Text

````text
# DTC U0122 (K20C1 (PGM-FI System)) (2019)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received message is different from the calculated checksum.

The value of checksum for the received message is different from the calculated checksum.

- Message counter error The two consecutive values of the message counter are equal at least once. The difference between two consecutive values of the message counter is greater than 255.

The two consecutive values of the message counter are equal at least once.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error The counter value in the message received in the present frame is same as the value received in the previous frame.

The counter value in the message received in the present frame is same as the value received in the previous frame.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6071: DTC U0122 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0122 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7194.html`
- Chunk ID: `chunk_c001e3804e6c`
- Images: `images\GHH403689.jpeg`, `images\GHH403690.jpeg`
- Duplicate sources: `pages\8781.html`, `pages\22641.html`, `pages\21054.html`

### Full Text

````text
# DTC U0122 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received message is different from the calculated checksum.

The value of checksum for the received message is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 6072: DTC U0122 (K20C2 (CVT) with CAN gateway (PGM-FI System)) (2019 2020 2021)

- Title: DTC U0122 (K20C2 (CVT) with CAN gateway (PGM-FI System)) (2019 2020 2021)
- Source path: `pages\7195.html`
- Chunk ID: `chunk_01937c0356a3`
- Images: `images\GHH403691.jpeg`
- Duplicate sources: `pages\8782.html`, `pages\22642.html`, `pages\21055.html`

### Full Text

````text
# DTC U0122 (K20C2 (CVT) with CAN gateway (PGM-FI System)) (2019 2020 2021)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the VSA modulator-control unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6073: DTC U0122 (K20C2: M/T model (PGM-FI System)) (2019 2020)

- Title: DTC U0122 (K20C2: M/T model (PGM-FI System)) (2019 2020)
- Source path: `pages\7196.html`
- Chunk ID: `chunk_01a440ab0b78`
- Images: `images\GHH403692.jpeg`
- Duplicate sources: `pages\8783.html`, `pages\22643.html`, `pages\21056.html`

### Full Text

````text
# DTC U0122 (K20C2: M/T model (PGM-FI System)) (2019 2020)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The VSA modulator-control unit monitors the signal from the wheel speed sensors. The powertrain control module (PCM) receives wheel speed information from the VSA modulator-control unit via the F-CAN lines. If the status of CAN communication between the PCM and the VSA modulator-control unit is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The status of CAN communication between the PCM and the VSA modulator-control unit is abnormal for at least 1.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6074: DTC U0122 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

- Title: DTC U0122 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)
- Source path: `pages\7197.html`
- Chunk ID: `chunk_01252a6e1f3e`
- Images: `images\GHH403693.jpeg`
- Duplicate sources: `pages\8784.html`, `pages\22644.html`, `pages\21057.html`

### Full Text

````text
# DTC U0122 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6075: DTC U0122 (K20C2: Without CAN gateway (PGM-FI System))

- Title: DTC U0122 (K20C2: Without CAN gateway (PGM-FI System))
- Source path: `pages\7198.html`
- Chunk ID: `chunk_76270868aa5b`
- Images: `images\GHH403694.jpeg`
- Duplicate sources: `pages\8785.html`, `pages\22645.html`, `pages\21058.html`

### Full Text

````text
# DTC U0122 (K20C2: Without CAN gateway (PGM-FI System))

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6076: DTC U0122 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

- Title: DTC U0122 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))
- Source path: `pages\7199.html`
- Chunk ID: `chunk_4bd75c94d124`
- Images: `images\GHH403695.jpeg`
- Duplicate sources: `pages\8786.html`, `pages\22646.html`, `pages\21059.html`

### Full Text

````text
# DTC U0122 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6077: DTC U0122 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

- Title: DTC U0122 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))
- Source path: `pages\7200.html`
- Chunk ID: `chunk_7fff8c18572b`
- Images: `images\GHH403696.jpeg`
- Duplicate sources: `pages\8787.html`, `pages\22647.html`, `pages\21060.html`

### Full Text

````text
# DTC U0122 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6078: DTC U0122 (L15B7/L15BA: M/T model (PGM-FI System)) (2019 2020 2021)

- Title: DTC U0122 (L15B7/L15BA: M/T model (PGM-FI System)) (2019 2020 2021)
- Source path: `pages\7201.html`
- Chunk ID: `chunk_fff5bbaf3528`
- Images: `images\GHH403697.jpeg`
- Duplicate sources: `pages\8788.html`, `pages\22648.html`, `pages\21061.html`

### Full Text

````text
# DTC U0122 (L15B7/L15BA: M/T model (PGM-FI System)) (2019 2020 2021)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The VSA modulator-control unit monitors the signal from the wheel speed sensors. The powertrain control module (PCM) receives wheel speed information from the VSA modulator-control unit via the F-CAN lines. If the status of CAN communication between the PCM and the VSA modulator-control unit is abnormal, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The status of CAN communication between the PCM and the VSA modulator-control unit is abnormal for at least 1.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6079: DTC U0122 (L15B7/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0122 (L15B7/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7202.html`
- Chunk ID: `chunk_ed940d6474cf`
- Images: `images\GHH403698.jpeg`
- Duplicate sources: `pages\8789.html`, `pages\22649.html`, `pages\21062.html`

### Full Text

````text
# DTC U0122 (L15B7/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0122: F-CAN Malfunction (Powertrain Control Module (PCM)-VSA Modulator-Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the VSA modulator-control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the VSA modulator-control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the VSA modulator-control unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the VSA modulator-control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6080: DTC U0128 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0128 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7203.html`
- Chunk ID: `chunk_3e2cb12b04c1`
- Images: `images\GHH403699.jpeg`
- Duplicate sources: `pages\8790.html`, `pages\22650.html`, `pages\21063.html`

### Full Text

````text
# DTC U0128 (K20C1 (PGM-FI System)) (2019)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6081: DTC U0128 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0128 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7204.html`
- Chunk ID: `chunk_6519d25c1aed`
- Images: `images\GHH403700.jpeg`, `images\GHH403701.jpeg`
- Duplicate sources: `pages\8791.html`, `pages\22651.html`, `pages\21064.html`

### Full Text

````text
# DTC U0128 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6082: DTC U0128 (K20C1) (2017 2018 2019)

- Title: DTC U0128 (K20C1) (2017 2018 2019)
- Source path: `pages\7205.html`
- Chunk ID: `chunk_4aa6ce6d7bb1`
- Images: `images\GHH403702.jpeg`
- Duplicate sources: `pages\8792.html`, `pages\22652.html`, `pages\21065.html`

### Full Text

````text
# DTC U0128 (K20C1) (2017 2018 2019)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Any of the conditions is met for at least 0.5 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error The counter value in the message received in the present frame is same as the value received in the previous frame.

The counter value in the message received in the present frame is same as the value received in the previous frame.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6083: DTC U0128 (K20C2 (M/T)) (2016 2017 2018)

- Title: DTC U0128 (K20C2 (M/T)) (2016 2017 2018)
- Source path: `pages\7206.html`
- Chunk ID: `chunk_01b4983f62d7`
- Images: `images\GHH403703.jpeg`
- Duplicate sources: `pages\8793.html`, `pages\22653.html`, `pages\21066.html`

### Full Text

````text
# DTC U0128 (K20C2 (M/T)) (2016 2017 2018)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM does not receive any signals via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6084: DTC U0128 (K20C2: With CAN gateway) (2019 2020 2021)

- Title: DTC U0128 (K20C2: With CAN gateway) (2019 2020 2021)
- Source path: `pages\7207.html`
- Chunk ID: `chunk_f3e7006e2e40`
- Images: `images\GHH403704.jpeg`
- Duplicate sources: `pages\8794.html`, `pages\22654.html`, `pages\21067.html`

### Full Text

````text
# DTC U0128 (K20C2: With CAN gateway) (2019 2020 2021)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) cannot receive the signals from the VSA modulator-control unit via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot receive any signals from the VSA modulator-control unit via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- VSA modulator-control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6085: DTC U0128 (L15B7/L15BA (M/T) with CAN gateway) (2017 2018 2019 2020 2021)

- Title: DTC U0128 (L15B7/L15BA (M/T) with CAN gateway) (2017 2018 2019 2020 2021)
- Source path: `pages\7208.html`
- Chunk ID: `chunk_27f20ed8e9b1`
- Images: `images\GHH403705.jpeg`
- Duplicate sources: `pages\8795.html`, `pages\22655.html`, `pages\21068.html`

### Full Text

````text
# DTC U0128 (L15B7/L15BA (M/T) with CAN gateway) (2017 2018 2019 2020 2021)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM does not receive any signals via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6086: DTC U0128 (L15B7/L15BA (M/T) without CAN gateway) (2017 2018 2019 2020 2021)

- Title: DTC U0128 (L15B7/L15BA (M/T) without CAN gateway) (2017 2018 2019 2020 2021)
- Source path: `pages\7209.html`
- Chunk ID: `chunk_b8cbfb3f5369`
- Images: `images\GHH403706.jpeg`
- Duplicate sources: `pages\8796.html`, `pages\22656.html`, `pages\21069.html`

### Full Text

````text
# DTC U0128 (L15B7/L15BA (M/T) without CAN gateway) (2017 2018 2019 2020 2021)

DTC U0128: F-CAN Malfunction (Powertrain Control Module (PCM)-Electric Parking Brake Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the VSA modulator-control unit via the F-CAN lines for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM does not receive any signals via the F-CAN lines for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VSA modulator-control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6087: DTC U0131 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0131 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7210.html`
- Chunk ID: `chunk_7c15e9ed4cc8`
- Images: `images\GHH403707.jpeg`
- Duplicate sources: `pages\8797.html`, `pages\22657.html`, `pages\21070.html`

### Full Text

````text
# DTC U0131 (K20C1 (PGM-FI System)) (2019)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the electrical power steering (EPS) control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- EPS control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6088: DTC U0131 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0131 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7211.html`
- Chunk ID: `chunk_373af91f42c8`
- Images: `images\GHH403708.jpeg`, `images\GHH403709.jpeg`
- Duplicate sources: `pages\8798.html`, `pages\22658.html`, `pages\21071.html`

### Full Text

````text
# DTC U0131 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the electrical power steering (EPS) control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- EPS control unit failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6089: DTC U0131 (K20C1) (2017 2018 2019)

- Title: DTC U0131 (K20C1) (2017 2018 2019)
- Source path: `pages\7212.html`
- Chunk ID: `chunk_31c505481839`
- Images: `images\GHH403710.jpeg`
- Duplicate sources: `pages\8799.html`, `pages\22659.html`, `pages\21072.html`

### Full Text

````text
# DTC U0131 (K20C1) (2017 2018 2019)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the electrical power steering (EPS) control unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met:

- Checksum error The value of checksum for the received frame is different from the calculated checksum for at least 1.0 second.

The value of checksum for the received frame is different from the calculated checksum for at least 1.0 second.

- Message counter error The counter value in the message received in the present frame is same as the value received in the previous frame for at least 1.0 second.

The counter value in the message received in the present frame is same as the value received in the previous frame for at least 1.0 second.

- Timeout error The CAN message frame is not received for at least 2.0 seconds.

The CAN message frame is not received for at least 2.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- EPS control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6090: DTC U0131 (K20C2: With CAN gateway) (2016 2017 2018)

- Title: DTC U0131 (K20C2: With CAN gateway) (2016 2017 2018)
- Source path: `pages\7213.html`
- Chunk ID: `chunk_68bc78d0ea6c`
- Images: `images\GHH403711.jpeg`
- Duplicate sources: `pages\8800.html`, `pages\22660.html`, `pages\21073.html`

### Full Text

````text
# DTC U0131 (K20C2: With CAN gateway) (2016 2017 2018)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN B lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EPS control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6091: DTC U0131 (K20C2: With CAN gateway) (2019 2020 2021)

- Title: DTC U0131 (K20C2: With CAN gateway) (2019 2020 2021)
- Source path: `pages\7214.html`
- Chunk ID: `chunk_0e99ea32d323`
- Images: `images\GHH403712.jpeg`
- Duplicate sources: `pages\8801.html`, `pages\22661.html`, `pages\21074.html`

### Full Text

````text
# DTC U0131 (K20C2: With CAN gateway) (2019 2020 2021)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the EPS control unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- EPS control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6092: DTC U0131 (K20C2: Without CAN gateway)

- Title: DTC U0131 (K20C2: Without CAN gateway)
- Source path: `pages\7215.html`
- Chunk ID: `chunk_7ebd8ba41b55`
- Images: `images\GHH403713.jpeg`
- Duplicate sources: `pages\8802.html`, `pages\22662.html`, `pages\21075.html`

### Full Text

````text
# DTC U0131 (K20C2: Without CAN gateway)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EPS control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6093: DTC U0131 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))

- Title: DTC U0131 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))
- Source path: `pages\7216.html`
- Chunk ID: `chunk_d5156cd561c3`
- Images: `images\GHH403714.jpeg`
- Duplicate sources: `pages\8803.html`, `pages\22663.html`, `pages\21076.html`

### Full Text

````text
# DTC U0131 (L15B7/L15BA/L15BY: With CAN gateway (12P connector type))

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EPS control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6094: DTC U0131 (L15B7/L15BA/L15BY: Without CAN gateway)

- Title: DTC U0131 (L15B7/L15BA/L15BY: Without CAN gateway)
- Source path: `pages\7217.html`
- Chunk ID: `chunk_8ae1e1bb1434`
- Images: `images\GHH403715.jpeg`
- Duplicate sources: `pages\8804.html`, `pages\22664.html`, `pages\21077.html`

### Full Text

````text
# DTC U0131 (L15B7/L15BA/L15BY: Without CAN gateway)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EPS control unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6095: DTC U0131 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0131 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7218.html`
- Chunk ID: `chunk_4e9e8a076d6e`
- Images: `images\GHH403716.jpeg`
- Duplicate sources: `pages\8805.html`, `pages\22665.html`, `pages\21078.html`

### Full Text

````text
# DTC U0131 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0131: F-CAN Malfunction (Powertrain Control Module (PCM)-EPS Control Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the electrical power steering (EPS) control unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the EPS control unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the EPS control unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the EPS control unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- EPS control unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6096: DTC U0146 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0146 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7219.html`
- Chunk ID: `chunk_67874db25ebc`
- Images: `images\GHH403717.jpeg`
- Duplicate sources: `pages\8806.html`, `pages\22666.html`, `pages\21079.html`

### Full Text

````text
# DTC U0146 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0146: F-CAN Malfunction (Powertrain Control Module (PCM)-CAN Gateway)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the CAN gateway via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- CAN gateway failure (include fuse blown)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6097: DTC U0146 (K20C2) (2019 2020 2021)

- Title: DTC U0146 (K20C2) (2019 2020 2021)
- Source path: `pages\7220.html`
- Chunk ID: `chunk_7432bcb20b36`
- Images: `images\GHH403718.jpeg`
- Duplicate sources: `pages\8807.html`, `pages\22667.html`, `pages\21080.html`

### Full Text

````text
# DTC U0146 (K20C2) (2019 2020 2021)

DTC U0146: F-CAN Malfunction (Powertrain Control Module (PCM)-CAN Gateway)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the CAN gateway via the F-CAN lines and this condition continues for a specified time or when the information sent from the CAN gateway is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [Battery] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the CAN gateway via the F-CAN lines for at least 1 second.

- The information sent from the CAN gateway is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- CAN gateway failure (include fuse blown)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, the freeze data, and the on-board snapshot are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, the freeze data, and the on-board snapshot can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 6098: DTC U0146 (L15B7/L15BY) (2019 2020 2021)

- Title: DTC U0146 (L15B7/L15BY) (2019 2020 2021)
- Source path: `pages\7221.html`
- Chunk ID: `chunk_d543ca7fa5bf`
- Images: `images\GHH403719.jpeg`
- Duplicate sources: `pages\8808.html`, `pages\22668.html`, `pages\21081.html`

### Full Text

````text
# DTC U0146 (L15B7/L15BY) (2019 2020 2021)

DTC U0146: F-CAN Malfunction (Powertrain Control Module (PCM)-CAN Gateway)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the CAN gateway via the F-CAN lines and this condition continues for a specified time or when the information sent from the CAN gateway is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [Battery] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the CAN gateway via the F-CAN lines for at least 1 second.

- The information sent from the CAN gateway is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- CAN gateway failure (include fuse blown)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, the freeze data, and the on-board snapshot are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, the freeze data, and the on-board snapshot can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 6099: DTC U0151 (K20C1 (PGM-FI System)) (2017 2018 2019)

- Title: DTC U0151 (K20C1 (PGM-FI System)) (2017 2018 2019)
- Source path: `pages\7222.html`
- Chunk ID: `chunk_f60068afb11e`
- Images: `images\GHH403720.jpeg`
- Duplicate sources: `pages\8809.html`, `pages\22669.html`, `pages\21082.html`

### Full Text

````text
# DTC U0151 (K20C1 (PGM-FI System)) (2017 2018 2019)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the SRS unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.0 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the ON mode | 3 seconds | -

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1.0 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error The same value for the message counter is received or the difference between two consecutive values for the message counter exceeds a threshold value.

The same value for the message counter is received or the difference between two consecutive values for the message counter exceeds a threshold value.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- SRS unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6100: DTC U0151 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0151 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7223.html`
- Chunk ID: `chunk_59c17fc8550c`
- Images: `images\GHH403721.jpeg`
- Duplicate sources: `pages\8810.html`, `pages\22670.html`, `pages\21083.html`

### Full Text

````text
# DTC U0151 (K20C1 (PGM-FI System)) (2019)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the SRS unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- SRS unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6101: DTC U0151 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0151 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7224.html`
- Chunk ID: `chunk_e8278dccdb8c`
- Images: `images\GHH403722.jpeg`, `images\GHH403723.jpeg`
- Duplicate sources: `pages\8811.html`, `pages\22671.html`, `pages\21084.html`

### Full Text

````text
# DTC U0151 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the SRS unit via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 1 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- SRS unit failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6102: DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

- Title: DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)
- Source path: `pages\7225.html`
- Chunk ID: `chunk_affd0d4da4ae`
- Images: `images\GHH403724.jpeg`
- Duplicate sources: `pages\8812.html`, `pages\22672.html`, `pages\21085.html`

### Full Text

````text
# DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN B lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- SRS unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6103: DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)

- Title: DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)
- Source path: `pages\7226.html`
- Chunk ID: `chunk_597cc6f388d3`
- Images: `images\GHH403725.jpeg`
- Duplicate sources: `pages\8813.html`, `pages\22673.html`, `pages\21086.html`

### Full Text

````text
# DTC U0151 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the SRS unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- SRS unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6104: DTC U0151 (K20C2: Without CAN gateway (PGM-FI System))

- Title: DTC U0151 (K20C2: Without CAN gateway (PGM-FI System))
- Source path: `pages\7227.html`
- Chunk ID: `chunk_3707cf0e5241`
- Images: `images\GHH403726.jpeg`
- Duplicate sources: `pages\8814.html`, `pages\22674.html`, `pages\21087.html`

### Full Text

````text
# DTC U0151 (K20C2: Without CAN gateway (PGM-FI System))

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- SRS unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6105: DTC U0151 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

- Title: DTC U0151 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))
- Source path: `pages\7228.html`
- Chunk ID: `chunk_d03958e6ab8a`
- Images: `images\GHH403727.jpeg`
- Duplicate sources: `pages\8815.html`, `pages\22675.html`, `pages\21088.html`

### Full Text

````text
# DTC U0151 (L15B7/L15BA/L15BY: With CAN gateway (PGM-FI System))

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- SRS unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6106: DTC U0151 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

- Title: DTC U0151 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))
- Source path: `pages\7229.html`
- Chunk ID: `chunk_62bddb4579c8`
- Images: `images\GHH403728.jpeg`
- Duplicate sources: `pages\8816.html`, `pages\22676.html`, `pages\21089.html`

### Full Text

````text
# DTC U0151 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- SRS unit failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6107: DTC U0151 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0151 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7230.html`
- Chunk ID: `chunk_4ada3f25d85a`
- Images: `images\GHH403729.jpeg`
- Duplicate sources: `pages\8817.html`, `pages\22677.html`, `pages\21090.html`

### Full Text

````text
# DTC U0151 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0151: F-CAN Malfunction (Powertrain Control Module (PCM)-SRS Unit)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the SRS unit via the F-CAN lines and this condition continues for a specified time or when the information sent from the SRS unit is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the SRS unit via the F-CAN lines for at least 1.5 seconds.

- The information sent from the SRS unit is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- SRS unit failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6108: DTC U0155 (K20C1 (PGM-FI System)) (2017 2018 2019)

- Title: DTC U0155 (K20C1 (PGM-FI System)) (2017 2018 2019)
- Source path: `pages\7231.html`
- Chunk ID: `chunk_37c9ae1abcf9`
- Images: `images\GHH403730.jpeg`
- Duplicate sources: `pages\8818.html`, `pages\22678.html`, `pages\21091.html`

### Full Text

````text
# DTC U0155 (K20C1 (PGM-FI System)) (2017 2018 2019)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the gauge control module (tach) via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 2.0 seconds:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error The same value for the message counter is received or the difference between two consecutive values for the message counter exceeds a threshold value.

The same value for the message counter is received or the difference between two consecutive values for the message counter exceeds a threshold value.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- Gauge control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6109: DTC U0155 (K20C1 (PGM-FI System)) (2019)

- Title: DTC U0155 (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7232.html`
- Chunk ID: `chunk_67dd9348b6b1`
- Images: `images\GHH403731.jpeg`
- Duplicate sources: `pages\8819.html`, `pages\22679.html`, `pages\21092.html`

### Full Text

````text
# DTC U0155 (K20C1 (PGM-FI System)) (2019)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the gauge control module (tach) via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 2 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- Gauge control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6110: DTC U0155 (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U0155 (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7233.html`
- Chunk ID: `chunk_08d413cba4a6`
- Images: `images\GHH403732.jpeg`, `images\GHH403733.jpeg`
- Duplicate sources: `pages\8820.html`, `pages\22680.html`, `pages\21093.html`

### Full Text

````text
# DTC U0155 (K20C1 (PGM-FI System)) (2020 2021)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the gauge control module via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time since the 12 volt battery voltage reaches to a specified value | 5.0 seconds | -

12 volt battery voltage [Battery] | 10.04 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met for at least 2 second:

- Checksum error The value of checksum for the received frame is different from the calculated checksum.

The value of checksum for the received frame is different from the calculated checksum.

- Message counter error

- - The two consecutive values of the message counter are equal at least once. - The difference between two consecutive values of the message counter is greater than 255.

- - The two consecutive values of the message counter are equal at least once.

The two consecutive values of the message counter are equal at least once.

- - The difference between two consecutive values of the message counter is greater than 255.

The difference between two consecutive values of the message counter is greater than 255.

- Timeout error The CAN message frame is not received.

The CAN message frame is not received.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- F-CAN circuit F-CAN C_H* 2 line open

- F-CAN circuit F-CAN C_L* 2 line open

- F-CAN circuit F-CAN C_H* 2 line short to ground

- F-CAN circuit F-CAN C_L* 2 line short to ground

- Gauge control module failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6111: DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

- Title: DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)
- Source path: `pages\7234.html`
- Chunk ID: `chunk_0308dbefa482`
- Images: `images\GHH403734.jpeg`
- Duplicate sources: `pages\8821.html`, `pages\22681.html`, `pages\21094.html`

### Full Text

````text
# DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2016 2017 2018)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the gauge control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the gauge control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN A lines for at least 1.5 seconds.

- The information sent from the gauge control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Gauge control module failure (include fuse fall-outs)

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6112: DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)

- Title: DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)
- Source path: `pages\7235.html`
- Chunk ID: `chunk_b698c5348eeb`
- Images: `images\GHH403735.jpeg`
- Duplicate sources: `pages\8822.html`, `pages\22682.html`, `pages\21095.html`

### Full Text

````text
# DTC U0155 (K20C2: With CAN gateway (PGM-FI System)) (2019 2020 2021)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the gauge control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the gauge control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the gauge control module via the F-CAN lines for at least 1.5 seconds.

- The information sent from the gauge control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- F-CAN circuit F-CAN C_H line open

- F-CAN circuit F-CAN C_L line open

- F-CAN circuit F-CAN C_H line short to ground

- F-CAN circuit F-CAN C_L line short to ground

- Gauge control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6113: DTC U0155 (K20C2: Without CAN gateway (PGM-FI System))

- Title: DTC U0155 (K20C2: Without CAN gateway (PGM-FI System))
- Source path: `pages\7236.html`
- Chunk ID: `chunk_3508f8e0cb67`
- Images: `images\GHH403736.jpeg`
- Duplicate sources: `pages\8823.html`, `pages\22683.html`, `pages\21096.html`

### Full Text

````text
# DTC U0155 (K20C2: Without CAN gateway (PGM-FI System))

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the gauge control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the gauge control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the gauge control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Gauge control module failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6114: DTC U0155 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

- Title: DTC U0155 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))
- Source path: `pages\7237.html`
- Chunk ID: `chunk_12671078736f`
- Images: `images\GHH403737.jpeg`
- Duplicate sources: `pages\8824.html`, `pages\22684.html`, `pages\21097.html`

### Full Text

````text
# DTC U0155 (L15B7/L15BA/L15BY: Without CAN gateway (PGM-FI System))

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the gauge control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the gauge control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

One of these conditions is met:

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

- The information sent from the gauge control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Gauge control module failure (include fuse fall-outs)

- F-CAN circuit F-CAN_H line open

- F-CAN circuit F-CAN_L line open

- F-CAN circuit F-CAN_H line short to ground

- F-CAN circuit F-CAN_L line short to ground

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6115: DTC U0155 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0155 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\7238.html`
- Chunk ID: `chunk_8f0af75549e1`
- Images: `images\GHH403738.jpeg`
- Duplicate sources: `pages\8825.html`, `pages\22685.html`, `pages\21098.html`

### Full Text

````text
# DTC U0155 (L15B7/L15BY: With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0155: F-CAN Malfunction (Powertrain Control Module (PCM)-Gauge Control Module)

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the gauge control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the gauge control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 3 seconds | -

12 volt battery voltage [BATTERY] | 10.0 V | -

[ ]: HDS Parameter

Malfunction Threshold

Either of the condition is met:

- The PCM cannot receive any signals from the gauge control module via the F-CAN lines for at least 1.5 seconds.

- The information sent from the gauge control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- F-CAN circuit F-CAN A_H line open

- F-CAN circuit F-CAN A_L line open

- F-CAN circuit F-CAN A_H line short to ground

- F-CAN circuit F-CAN A_L line short to ground

- F-CAN circuit F-CAN B_H line open

- F-CAN circuit F-CAN B_L line open

- F-CAN circuit F-CAN B_H line short to ground

- F-CAN circuit F-CAN B_L line short to ground

- F-CAN circuit F-CAN C_H line open

- F-CAN circuit F-CAN C_L line open

- F-CAN circuit F-CAN C_H line short to ground

- F-CAN circuit F-CAN C_L line short to ground

- Gauge control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Sources Used

- `pages\6987.html`
- `pages\6988.html`
- `pages\6989.html`
- `pages\6990.html`
- `pages\6991.html`
- `pages\6992.html`
- `pages\6993.html`
- `pages\6994.html`
- `pages\6995.html`
- `pages\6996.html`
- `pages\6997.html`
- `pages\6998.html`
- `pages\6999.html`
- `pages\7000.html`
- `pages\7001.html`
- `pages\7002.html`
- `pages\7003.html`
- `pages\7004.html`
- `pages\7005.html`
- `pages\7006.html`
- `pages\7007.html`
- `pages\7008.html`
- `pages\7009.html`
- `pages\7010.html`
- `pages\7011.html`
- `pages\7012.html`
- `pages\7013.html`
- `pages\7014.html`
- `pages\7015.html`
- `pages\7016.html`
- `pages\7017.html`
- `pages\7018.html`
- `pages\7019.html`
- `pages\7020.html`
- `pages\7021.html`
- `pages\7022.html`
- `pages\7023.html`
- `pages\7024.html`
- `pages\7025.html`
- `pages\7026.html`
- `pages\7027.html`
- `pages\7028.html`
- `pages\7029.html`
- `pages\7030.html`
- `pages\7031.html`
- `pages\7032.html`
- `pages\7033.html`
- `pages\7034.html`
- `pages\7035.html`
- `pages\7036.html`
- `pages\7037.html`
- `pages\7038.html`
- `pages\7039.html`
- `pages\7040.html`
- `pages\7041.html`
- `pages\7042.html`
- `pages\7043.html`
- `pages\7044.html`
- `pages\7045.html`
- `pages\7046.html`
- `pages\7047.html`
- `pages\7048.html`
- `pages\7049.html`
- `pages\7050.html`
- `pages\7051.html`
- `pages\7052.html`
- `pages\7053.html`
- `pages\7054.html`
- `pages\7055.html`
- `pages\7056.html`
- `pages\7057.html`
- `pages\7058.html`
- `pages\7059.html`
- `pages\7060.html`
- `pages\7061.html`
- `pages\7062.html`
- `pages\7063.html`
- `pages\7064.html`
- `pages\7065.html`
- `pages\7066.html`
- `pages\7067.html`
- `pages\7068.html`
- `pages\7069.html`
- `pages\7070.html`
- `pages\7071.html`
- `pages\7072.html`
- `pages\7073.html`
- `pages\7074.html`
- `pages\7075.html`
- `pages\7076.html`
- `pages\7077.html`
- `pages\7078.html`
- `pages\7079.html`
- `pages\7080.html`
- `pages\7081.html`
- `pages\7082.html`
- `pages\7083.html`
- `pages\7084.html`
- `pages\7085.html`
- `pages\7086.html`
- `pages\7087.html`
- `pages\7088.html`
- `pages\7089.html`
- `pages\7090.html`
- `pages\7091.html`
- `pages\7092.html`
- `pages\7093.html`
- `pages\7094.html`
- `pages\7095.html`
- `pages\7096.html`
- `pages\7097.html`
- `pages\7098.html`
- `pages\7099.html`
- `pages\7100.html`
- `pages\7101.html`
- `pages\7102.html`
- `pages\7103.html`
- `pages\7104.html`
- `pages\7105.html`
- `pages\7106.html`
- `pages\7107.html`
- `pages\7108.html`
- `pages\7109.html`
- `pages\7110.html`
- `pages\7111.html`
- `pages\7112.html`
- `pages\7113.html`
- `pages\7114.html`
- `pages\7115.html`
- `pages\7116.html`
- `pages\7117.html`
- `pages\7118.html`
- `pages\7119.html`
- `pages\7120.html`
- `pages\7121.html`
- `pages\7122.html`
- `pages\7123.html`
- `pages\7124.html`
- `pages\7125.html`
- `pages\7126.html`
- `pages\7127.html`
- `pages\7128.html`
- `pages\7129.html`
- `pages\7130.html`
- `pages\7131.html`
- `pages\7132.html`
- `pages\7133.html`
- `pages\7134.html`
- `pages\7135.html`
- `pages\7136.html`
- `pages\7137.html`
- `pages\7138.html`
- `pages\7139.html`
- `pages\7140.html`
- `pages\7141.html`
- `pages\7142.html`
- `pages\7143.html`
- `pages\7144.html`
- `pages\7145.html`
- `pages\7146.html`
- `pages\7147.html`
- `pages\7148.html`
- `pages\7149.html`
- `pages\7150.html`
- `pages\7151.html`
- `pages\7152.html`
- `pages\7153.html`
- `pages\7154.html`
- `pages\7155.html`
- `pages\7156.html`
- `pages\7157.html`
- `pages\7158.html`
- `pages\7159.html`
- `pages\7160.html`
- `pages\7161.html`
- `pages\7162.html`
- `pages\7163.html`
- `pages\7164.html`
- `pages\7165.html`
- `pages\7166.html`
- `pages\7167.html`
- `pages\7168.html`
- `pages\7169.html`
- `pages\7170.html`
- `pages\7171.html`
- `pages\7172.html`
- `pages\7173.html`
- `pages\7174.html`
- `pages\7175.html`
- `pages\7176.html`
- `pages\7177.html`
- `pages\7178.html`
- `pages\7179.html`
- `pages\7180.html`
- `pages\7181.html`
- `pages\7182.html`
- `pages\7183.html`
- `pages\7184.html`
- `pages\7185.html`
- `pages\7186.html`
- `pages\7187.html`
- `pages\7188.html`
- `pages\7189.html`
- `pages\7190.html`
- `pages\7191.html`
- `pages\7192.html`
- `pages\7193.html`
- `pages\7194.html`
- `pages\7195.html`
- `pages\7196.html`
- `pages\7197.html`
- `pages\7198.html`
- `pages\7199.html`
- `pages\7200.html`
- `pages\7201.html`
- `pages\7202.html`
- `pages\7203.html`
- `pages\7204.html`
- `pages\7205.html`
- `pages\7206.html`
- `pages\7207.html`
- `pages\7208.html`
- `pages\7209.html`
- `pages\7210.html`
- `pages\7211.html`
- `pages\7212.html`
- `pages\7213.html`
- `pages\7214.html`
- `pages\7215.html`
- `pages\7216.html`
- `pages\7217.html`
- `pages\7218.html`
- `pages\7219.html`
- `pages\7220.html`
- `pages\7221.html`
- `pages\7222.html`
- `pages\7223.html`
- `pages\7224.html`
- `pages\7225.html`
- `pages\7226.html`
- `pages\7227.html`
- `pages\7228.html`
- `pages\7229.html`
- `pages\7230.html`
- `pages\7231.html`
- `pages\7232.html`
- `pages\7233.html`
- `pages\7234.html`
- `pages\7235.html`
- `pages\7236.html`
- `pages\7237.html`
- `pages\7238.html`
