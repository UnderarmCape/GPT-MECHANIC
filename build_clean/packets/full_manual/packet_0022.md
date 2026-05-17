# Deep Research Manual Packet 0022

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0022
- Chunk count: 238
- Chunk range: 5349-5586
- Source count: 197
- Target maximum characters: 750000

## Manual Chunks

## Chunk 5349: DTC P0140 (K20C1) (2019 2020 2021)

- Title: DTC P0140 (K20C1) (2019 2020 2021)
- Source path: `pages\6542.html`
- Chunk ID: `chunk_4b13e6f3d182`
- Images: `images\GHH402824.jpeg`
- Duplicate sources: `pages\8129.html`, `pages\23200.html`, `pages\21613.html`

### Full Text

````text
# DTC P0140 (K20C1) (2019 2020 2021)

DTC P0140: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Circuit No Activity

General Description

Courtesy of HONDA, U.S.A., INC.

In order to ensure a constant and appropriate operating temperature of the secondary heated oxygen sensor (secondary HO2S (sensor 2)), a heater is integrated and it is controlled and monitored by the powertrain control module (PCM). The PCM monitors the correlation between the ceramics temperature and internal resistance. In case of defective sensor heating, the ceramics temperature usually is lower compared to a faultless sensor and as a consequence the internal resistance of the sensor is considerably higher compared to a regularly heated sensor. If the secondary HO2S (sensor 2) internal resistance exceeds a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 minutes or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine stop time | 2 minutes | -

Intake air temperature [IAT Sensor (1)] | 18.5 deg.F (-7.5 deg.C) | -

Exhaust gas temperature | 392.02 deg.F (200.01 deg.C) | 1, 111.98 deg.F (599.99 deg.C)

12 volt battery voltage [Battery] | 10.7 V | 16.1 V

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) internal resistance exceeds 1, 026 ' - 22, 320 '*.

*: Depends on operating condition

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) resistance high

- Secondary HO2S (sensor 2) failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5350: DTC P0141 (K20C1) (2017 2018 2019)

- Title: DTC P0141 (K20C1) (2017 2018 2019)
- Source path: `pages\6543.html`
- Chunk ID: `chunk_147ce0711327`
- Images: `images\GHH402825.jpeg`
- Duplicate sources: `pages\8130.html`, `pages\23201.html`, `pages\21614.html`

### Full Text

````text
# DTC P0141 (K20C1) (2017 2018 2019)

DTC P0141: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Heater Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

In order to ensure a constant and appropriate operating temperature of the secondary heated oxygen sensor (secondary HO2S (sensor 2)), a heater is integrated and it is controlled and monitored by the powertrain control module (PCM). When the heater is activated, it heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the secondary HO2S (sensor 2) heater current or output voltage is other than a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] | 8 V | 16 V

[ ]: HDS Parameter

Malfunction Threshold

- Short circuit to power The secondary HO2S (sensor 2) heater output current is higher than 3 A for at least 0.5 second.

The secondary HO2S (sensor 2) heater output current is higher than 3 A for at least 0.5 second.

- Short circuit to ground The secondary HO2S (sensor 2) heater output voltage is lower than 2 V for at least 0.5 second.

The secondary HO2S (sensor 2) heater output voltage is lower than 2 V for at least 0.5 second.

- Open circuit The secondary HO2S (sensor 2) heater output voltage is between 3 V and 5 V for at least 0.5 second.

The secondary HO2S (sensor 2) heater output voltage is between 3 V and 5 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) SO2HT line open

- Secondary HO2S (sensor 2) SO2HT line short to ground

- Secondary HO2S (sensor 2) SO2HT line short to power

- Secondary HO2S (sensor 2) failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5351: DTC P0141 (K20C1) (2019 2020 2021)

- Title: DTC P0141 (K20C1) (2019 2020 2021)
- Source path: `pages\6544.html`
- Chunk ID: `chunk_e72108258cb8`
- Images: `images\GHH402826.jpeg`
- Duplicate sources: `pages\8131.html`, `pages\23202.html`, `pages\21615.html`

### Full Text

````text
# DTC P0141 (K20C1) (2019 2020 2021)

DTC P0141: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Heater Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

In order to ensure a constant and appropriate operating temperature of the secondary heated oxygen sensor (secondary HO2S (sensor 2)), a heater is integrated and it is controlled and monitored by the powertrain control module (PCM). When the heater is activated, it heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the secondary HO2S (sensor 2) heater current or output voltage is other than a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | - | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

- Short circuit to power The secondary HO2S (sensor 2) heater output current is 12.5 A or more for at least 0.5 second.

The secondary HO2S (sensor 2) heater output current is 12.5 A or more for at least 0.5 second.

- Short circuit to ground The secondary HO2S (sensor 2) heater output voltage is 2.74 V or less for at least 0.5 second.

The secondary HO2S (sensor 2) heater output voltage is 2.74 V or less for at least 0.5 second.

- Open circuit The secondary HO2S (sensor 2) heater output voltage is between 3.26 - 4.7 V for at least 0.5 second.

The secondary HO2S (sensor 2) heater output voltage is between 3.26 - 4.7 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) SO2HT line open

- Secondary HO2S (sensor 2) SO2HT line short to ground

- Secondary HO2S (sensor 2) SO2HT line short to power

- Secondary HO2S (sensor 2) failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5352: DTC P0141 (K20C2)

- Title: DTC P0141 (K20C2)
- Source path: `pages\6545.html`
- Chunk ID: `chunk_1460dc56b63b`
- Images: `images\GHH402827.jpeg`
- Duplicate sources: `pages\8132.html`, `pages\23203.html`, `pages\21616.html`

### Full Text

````text
# DTC P0141 (K20C2)

DTC P0141: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Heater Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the zirconia element is embedded in the secondary heated oxygen sensor (secondary HO2S (sensor 2)), and it is controlled by the powertrain control module (PCM). When activated, it heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the secondary HO2S (sensor 2) heater draws other than a specified amperage, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 41 deg.F (5 deg.C) | -

12 volt battery voltage [BATTERY] (FI MAIN RLY OUT terminal of PCM) | 4.67 V | -

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) heater output is 0.38 A or less, or 3.33 A or more, for at least 5.0 seconds when the heater is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) heater failure

- Secondary HO2S (sensor 2) SO2HT line open

- Secondary HO2S (sensor 2) SO2HT line short to ground

- Secondary HO2S (sensor 2) heater power supply line open (includes fuse blown)

- Poor ignition switch

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5353: DTC P0141 (L15B7/L15BA/L15BY)

- Title: DTC P0141 (L15B7/L15BA/L15BY)
- Source path: `pages\6546.html`
- Chunk ID: `chunk_865ee0bb5e1f`
- Images: `images\GHH402828.jpeg`
- Duplicate sources: `pages\8133.html`, `pages\23204.html`, `pages\21617.html`

### Full Text

````text
# DTC P0141 (L15B7/L15BA/L15BY)

DTC P0141: Secondary Heated Oxygen Sensor (Secondary HO2S (Sensor 2)) Heater Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

A heater for the zirconia element is embedded in the secondary heated oxygen sensor (secondary HO2S (sensor 2)), and it is controlled by the powertrain control module (PCM). When activated, it heats the sensor to stabilize and speed up the detection of oxygen content when the exhaust gas temperature is cold. If the secondary HO2S (sensor 2) heater draws other than a specified amperage, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature[ECT SENSOR 1] | 41 deg.F (5 deg.C) | -

12 volt battery voltage [BATTERY] (FI MAIN RLY OUT terminal of PCM) | 4.67 V | -

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) heater output is 0.38 A or less, or 3.33 A or more, for at least 5.0 seconds when the heater is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Secondary HO2S (sensor 2) heater failure

- Secondary HO2S (sensor 2) SO2HT line open

- Secondary HO2S (sensor 2) SO2HT line short to ground

- Secondary HO2S (sensor 2) heater power supply line open (includes fuse blown)

- Secondary HO2S (sensor 2) heater internal circuit open

- Poor ignition switch

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5354: DTC P0171 (K20C1) (2017 2018 2019)

- Title: DTC P0171 (K20C1) (2017 2018 2019)
- Source path: `pages\6547.html`
- Chunk ID: `chunk_5d9c1d9c8707`
- Images: `images\GHH402829.jpeg`
- Duplicate sources: `pages\8134.html`, `pages\23205.html`, `pages\21618.html`

### Full Text

````text
# DTC P0171 (K20C1) (2017 2018 2019)

DTC P0171: Fuel System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel mixture adaption system. The fuel mixture adaptation system corrects fuel mixture deviations from the fuel control system with the following error compensation terms:

The multiplicative correction term FRA: dominates the total fuel correction at higher engine speeds and loads.

The additive correction term ORA: dominates the total fuel correction at idle.

This is only possible when closed loop fuel control is active and during homogeneous operation with stoichiometric ratio. If the multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is greater than a specified value, the PCM detects a malfunction and stores a DTC. The PCM also monitors the short term fuel trim value. If the short trim fuel trim value is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Long term fuel trim

Condition

Other | Multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is enabled

Excessive fuel must not be contained in engine oil

Short term fuel trim

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140 deg.F (60 deg.C) | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Fuel injection time | 1, 560 times | -

Fuel feedback | Closed loop

Other | Evaporative emission (EVAP) canister not purging

Excessive fuel must not be contained in engine oil

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met:

- Monitor for multiplicative part of long term fuel trim The multiplicative part of long term fuel trim change is within 2.0 % for 10 seconds after the multiplicative part of long term fuel trim reached 1.299988.

The multiplicative part of long term fuel trim change is within 2.0 % for 10 seconds after the multiplicative part of long term fuel trim reached 1.299988.

- Monitor for additive part of long term fuel trim The additive part of long term fuel trim change is within 1, 535.953 % for 10 seconds after the additive part of long term fuel trim reached 5.484.

The additive part of long term fuel trim change is within 1, 535.953 % for 10 seconds after the additive part of long term fuel trim reached 5.484.

- Monitor for short term fuel trim The deviation of the short trim fuel trim mean value from 1.0 is higher than 0.23999 for at least 10 seconds.

The deviation of the short trim fuel trim mean value from 1.0 is higher than 0.23999 for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Exhaust gas leak

- Mass airflow (MAF) sensor failure

- Fuel injector failure

- Fuel control system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at high engine speed and high load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5355: DTC P0171 (K20C1) (2019 2020 2021)

- Title: DTC P0171 (K20C1) (2019 2020 2021)
- Source path: `pages\6548.html`
- Chunk ID: `chunk_b40148e0b483`
- Images: `images\GHH402830.jpeg`
- Duplicate sources: `pages\8135.html`, `pages\23206.html`, `pages\21619.html`

### Full Text

````text
# DTC P0171 (K20C1) (2019 2020 2021)

DTC P0171: Fuel System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel mixture adaptation system. The fuel mixture adaptation system corrects fuel mixture deviations from the fuel control system with the following error compensation terms:

The multiplicative correction term FRA: dominates the total fuel correction at higher engine speeds and loads.

The additive correction term ORA: dominates the total fuel correction at idle.

This is only possible when closed loop fuel control is active and during homogeneous operation with stoichiometric ratio. If the multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is greater than a specified value, the PCM detects a malfunction and stores a DTC. The PCM also monitors the short term fuel trim value. If the short trim fuel trim value is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Multiple*, Continuous**

Sequence | None

Duration | 0.5 second or more*, 100 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Long term fuel trim

**: Short term fuel trim

Enable Conditions

Long term fuel trim

Condition

Other | Multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is enabled

Excessive fuel must not be contained in engine oil

Multiplicative part is stable for at least 10 seconds***

***: Monitor for additive part

Short term fuel trim

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140 deg.F (60 deg.C) | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Fuel injection time | 1, 560 times | -

Fuel feedback | Closed loop

Other | Evaporative emission (EVAP) canister not purging for at least 10 seconds

Excessive fuel must not be contained in engine oil

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met:

- Monitor for multiplicative part of long term fuel trim The multiplicative part of long term fuel trim is more than 1.30 for at least 10 seconds.

The multiplicative part of long term fuel trim is more than 1.30 for at least 10 seconds.

- Monitor for additive part of long term fuel trim The additive part of long term fuel trim is more than 5.48 % for at least 10 seconds.

The additive part of long term fuel trim is more than 5.48 % for at least 10 seconds.

- Monitor for short term fuel trim The deviation of the short trim fuel trim mean value from 1.0 is higher than 0.24.

The deviation of the short trim fuel trim mean value from 1.0 is higher than 0.24.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Exhaust gas leak

- Mass airflow (MAF) sensor failure

- Fuel injector failure

- Fuel control system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at high engine speed and high load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5356: DTC P0171 (K20C2)

- Title: DTC P0171 (K20C2)
- Source path: `pages\6549.html`
- Chunk ID: `chunk_c6becb4c75cf`
- Images: `images\GHH402831.jpeg`
- Duplicate sources: `pages\8136.html`, `pages\23207.html`, `pages\21620.html`

### Full Text

````text
# DTC P0171 (K20C2)

DTC P0171: Fuel System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions. Long term fuel trim is computed from short term fuel trim and is used to regulate long term deviation from the stoichiometric air/fuel ratio, which occurs when fuel metering components deteriorate with age or system failures occur. In addition, long term fuel trim is stored in the PCM memory and is used to determine when fuel metering components malfunction. When long term fuel trim is higher than normal, which is about 1.0 (0 %), the amount of injected fuel must be increased, and when lower than normal, it must be decreased. If long term fuel trim is higher than normal (too lean), the PCM detects a malfunction in the fuel metering components and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | Every 3.0 seconds

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED]* 1 | 550 rpm | 4, 000 rpm

Engine speed [ENGINE SPEED]* 2 | 650 rpm | 4, 000 rpm

MAP value [MAP SENSOR]* 1 | 19 kPa (140 mmHg, 5.6 inHg) | -

MAP value [MAP SENSOR]* 2 | 18 kPa (130 mmHg, 5.2 inHg) | -

Fuel feedback | Closed loop

Monitoring priority | P0133, P0420, P219C, P219D, P219E, P219F

*1: CVT model

*2: M/T model[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is higher than 1.32 (+32 %).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- Mass airflow (MAF) sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (24 - 120 km/h) for at least 15 minutes, and watch the long term fuel trim. If the long term fuel trim stays at about 1.0, the vehicle is OK or it is a very minor problem. If a significant fault is still present, the long term fuel trim will move up or down while driving.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- After clearing the DTC by disconnecting the 12 volt battery or using the scan tool, drive at a steady speed between 15 - 55 mph (24 - 88km/h) for at least 40 minutes or longer to allow time for long term fuel trim to recover.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5357: DTC P0171 (L15B7/L15BA/L15BY)

- Title: DTC P0171 (L15B7/L15BA/L15BY)
- Source path: `pages\6550.html`
- Chunk ID: `chunk_4443e1353533`
- Images: `images\GHH402832.jpeg`
- Duplicate sources: `pages\8137.html`, `pages\23208.html`, `pages\21621.html`

### Full Text

````text
# DTC P0171 (L15B7/L15BA/L15BY)

DTC P0171: Fuel System Too Lean

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions. Long term fuel trim is computed from short term fuel trim and is used to regulate long term deviation from the stoichiometric air/fuel ratio, which occurs when fuel metering components deteriorate with age or system failures occur. In addition, long term fuel trim is stored in the PCM memory and is used to determine when fuel metering components malfunction. When long term fuel trim is higher than normal, which is about 1.0 (0 %), the amount of injected fuel must be increased, and when lower than normal, it must be decreased. If long term fuel trim is normal (too lean) or more, the PCM detects a malfunction in the fuel metering components and stores a DTC.

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

Engine speed [ENGINE SPEED]* 1 | 530 rpm | 4, 000 rpm

Engine speed [ENGINE SPEED]* 2 | 620 rpm | 4, 000 rpm

MAP value [MAP SENSOR] | 16 kPa (120 mmHg, 4.8 inHg) | -

Fuel feedback | Closed loop

Monitoring priority | P0133, P0420, P219C, P219D, P219E, P219F

*1: CVT

*2: M/T[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is 1.33 (+33 %) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Fuel injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- Mass airflow (MAF) sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

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

## Chunk 5358: DTC P0172 (K20C1) (2017 2018 2019)

- Title: DTC P0172 (K20C1) (2017 2018 2019)
- Source path: `pages\6551.html`
- Chunk ID: `chunk_b11e2587b744`
- Images: `images\GHH402833.jpeg`
- Duplicate sources: `pages\8138.html`, `pages\23209.html`, `pages\21622.html`

### Full Text

````text
# DTC P0172 (K20C1) (2017 2018 2019)

DTC P0172: Fuel System Too Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel mixture adaption system. The fuel mixture adaptation system corrects fuel mixture deviations from the fuel control system with the following error compensation terms:

The multiplicative correction term FRA: dominates the total fuel correction at higher engine speeds and loads.

The additive correction term ORA: dominates the total fuel correction at idle.

This is only possible when closed loop fuel control is active and during homogeneous operation with stoichiometric ratio. If the multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is less than a specified value, the PCM detects a malfunction and stores a DTC. The PCM also monitors the short term fuel trim value. If the short trim fuel trim value is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Long term fuel trim

Condition

Other | Multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is enabled

Excessive fuel must not be contained in engine oil

Short term fuel trim

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140 deg.F (60 deg.C) | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Fuel injection time | 1, 560 times | -

Fuel feedback | Closed loop

Other | Evaporative emission (EVAP) canister not purging

Excessive fuel must not be contained in engine oil

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met:

- Monitor for multiplicative part of long term fuel trim The multiplicative part of long term fuel trim change is within 2.0 % for 10 seconds after the multiplicative part of long term fuel trim reached 0.700012.

The multiplicative part of long term fuel trim change is within 2.0 % for 10 seconds after the multiplicative part of long term fuel trim reached 0.700012.

- Monitor for additive part of long term fuel trim The additive part of long term fuel trim change is within 1535.953 % for 10 seconds after the additive part of long term fuel trim reached -5.484.

The additive part of long term fuel trim change is within 1535.953 % for 10 seconds after the additive part of long term fuel trim reached -5.484.

- Monitor for short term fuel trim The deviation of the short trim fuel trim mean value from 1.0 is lower than 0.23999 for at least 10 seconds.

The deviation of the short trim fuel trim mean value from 1.0 is lower than 0.23999 for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Exhaust gas leak

- Mass airflow (MAF) sensor failure

- Fuel injector failure

- Fuel control system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at high engine speed and high load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5359: DTC P0172 (K20C1) (2019 2020 2021)

- Title: DTC P0172 (K20C1) (2019 2020 2021)
- Source path: `pages\6552.html`
- Chunk ID: `chunk_ecb93579b7b7`
- Images: `images\GHH402834.jpeg`
- Duplicate sources: `pages\8139.html`, `pages\23210.html`, `pages\21623.html`

### Full Text

````text
# DTC P0172 (K20C1) (2019 2020 2021)

DTC P0172: Fuel System Too Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel mixture adaptation system. The fuel mixture adaptation system corrects fuel mixture deviations from the fuel control system with the following error compensation terms:

The multiplicative correction term FRA: dominates the total fuel correction at higher engine speeds and loads.

The additive correction term ORA: dominates the total fuel correction at idle.

This is only possible when closed loop fuel control is active and during homogeneous operation with stoichiometric ratio. If the multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is less than a specified value, the PCM detects a malfunction and stores a DTC. The PCM also monitors the short term fuel trim value. If the short trim fuel trim value is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Multiple*, Continuous**

Sequence | None

Duration | 0.5 second or more*, 100 seconds or more**

DTC Type | Two drive cycles, MIL on

*: Long term fuel trim**: Short term fuel trim

Enable Conditions

Long term fuel trim

Condition

Other | Multiplicative part of the long term fuel trim or the additive part of the long term fuel trim is enabled

Excessive fuel must not be contained in engine oil

Multiplicative part is stable for at least 10 seconds***

***: Monitor for additive part

Short term fuel trim

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 140 deg.F (60 deg.C) | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Fuel injection time | 1, 560 times | -

Fuel feedback | Closed loop

Other | Evaporative emission (EVAP) canister not purging for at least 10 seconds

Excessive fuel must not be contained in engine oil

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met:

- Monitor for multiplicative part of long term fuel trim The multiplicative part of long term fuel trim is lower than 0.70 for at least 10 seconds.

The multiplicative part of long term fuel trim is lower than 0.70 for at least 10 seconds.

- Monitor for additive part of long term fuel trim The additive part of long term fuel trim is lower than -5.48 % for at least 10 seconds.

The additive part of long term fuel trim is lower than -5.48 % for at least 10 seconds.

- Monitor for short term fuel trim The deviation of the short trim fuel trim mean value from 1.0 is lower than -0.24.

The deviation of the short trim fuel trim mean value from 1.0 is lower than -0.24.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Exhaust gas leak

- Mass airflow (MAF) sensor failure

- Fuel injector failure

- Fuel control system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at high engine speed and high load for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5360: DTC P0172 (K20C2)

- Title: DTC P0172 (K20C2)
- Source path: `pages\6553.html`
- Chunk ID: `chunk_7c33b4b4a8fc`
- Images: `images\GHH402835.jpeg`
- Duplicate sources: `pages\8140.html`, `pages\23211.html`, `pages\21624.html`

### Full Text

````text
# DTC P0172 (K20C2)

DTC P0172: Fuel System Too Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions. Long term fuel trim is computed from short term fuel trim and is used to regulate long term deviation from the stoichiometric air/fuel ratio, which occurs when fuel metering components deteriorate with age or system failures occur. In addition, long term fuel trim is stored in the PCM memory and is used to determine when fuel metering components malfunction. When long term fuel trim is higher than normal, which is about 1.0 (0 %), the amount of injected fuel must be increased, and when lower than normal, it must be decreased. If long term fuel trim is lower than normal (too rich), the PCM detects a malfunction in the fuel metering components and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 19 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED]* 1 | 550 rpm | 4, 000 rpm

Engine speed [ENGINE SPEED]* 2 | 650 rpm | 4, 000 rpm

MAP value [MAP SENSOR]* 1 | 19 kPa (140 mmHg, 5.6 inHg) | -

MAP value [MAP SENSOR]* 2 | 18 kPa (130 mmHg, 5.2 inHg) | -

Fuel feedback | Closed loop

Monitoring priority | P0133, P0420, P219C, P219D, P219E, P219F

*1: CVT model

*2: M/T model[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is lower than 0.79 (-21 %).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- Mass airflow (MAF) sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at a steady speed between 15 - 75 mph (24 - 120 km/h) for at least 15 minutes, and watch the long term fuel trim. If the long term fuel trim stays at about 1.0, the vehicle is OK or it is a very minor problem. If a significant fault is still present, the long term fuel trim will move up or down while driving.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2.

- After clearing the DTC by disconnecting the 12 volt battery or using the scan tool, drive at a steady speed between 15 - 55 mph (24 - 88km/h) for at least 40 minutes or longer to allow time for long term fuel trim to recover.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5361: DTC P0172 (L15B7/L15BA)

- Title: DTC P0172 (L15B7/L15BA)
- Source path: `pages\6554.html`
- Chunk ID: `chunk_e6720ce8cd31`
- Images: `images\GHH402836.jpeg`
- Duplicate sources: `pages\8141.html`, `pages\23212.html`, `pages\21625.html`

### Full Text

````text
# DTC P0172 (L15B7/L15BA)

DTC P0172: Fuel System Too Rich

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) detects the oxygen content in the exhaust gas from the air/fuel ratio (A/F) sensor (sensor 1) signal voltage, and it uses fuel feedback control to maintain the optimal air/fuel ratio. The air/fuel ratio coefficient for correcting the amount of injected fuel is the short term fuel trim. The PCM varies short term fuel trim continuously to keep the air/fuel ratio close to the stoichiometric ratio for all driving conditions. Long term fuel trim is computed from short term fuel trim and is used to regulate long term deviation from the stoichiometric air/fuel ratio, which occurs when fuel metering components deteriorate with age or system failures occur. In addition, long term fuel trim is stored in the PCM memory and is used to determine when fuel metering components malfunction. When long term fuel trim is higher than normal, which is about 1.0 (0 %), the amount of injected fuel must be increased, and when lower than normal, it must be decreased. If long term fuel trim is normal (too rich) or less, the PCM detects a malfunction in the fuel metering components and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*

Sequence | None

Duration | 20 seconds or more

DTC Type | Two drive cycles, MIL on

*: The malfunction judgment is cleared when it is judged as normal under the same driving conditions in which the malfunction is detected.

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | 18 deg.F (-7 deg.C) | -

Engine speed [ENGINE SPEED]* 1 | 530 rpm | 4, 000 rpm

Engine speed [ENGINE SPEED]* 2 | 620 rpm | 4, 000 rpm

MAP value [MAP SENSOR] | 16 kPa (120 mmHg, 4.8 inHg) | -

Fuel feedback | Closed loop

Monitoring priority | P0133, P0420, P219C, P219D, P219E, P219F

*1: CVT

*2: M/T[ ]: HDS Parameter

Malfunction Threshold

Long term fuel trim is 0.79 (-21 %) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel pump failure

- Fuel injector failure

- Fuel pressure regulator failure

- Fuel line failure

- Fuel supply system failure

- Mass airflow (MAF) sensor range/performance problem

- Manifold absolute pressure (MAP) sensor range/performance problem

- A/F sensor (sensor 1) failure

- Secondary HO2S (sensor 2) failure

- Vacuum hose misinstalled

- Throttle body air leak

- Intake manifold air leak

- EVAP canister purge valve failure

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

## Chunk 5362: DTC P0190 (K20C1) (2017 2018 2019)

- Title: DTC P0190 (K20C1) (2017 2018 2019)
- Source path: `pages\6555.html`
- Chunk ID: `chunk_adf12d93d86a`
- Images: `images\GHH402837.jpeg`
- Duplicate sources: `pages\8142.html`, `pages\23213.html`, `pages\21626.html`

### Full Text

````text
# DTC P0190 (K20C1) (2017 2018 2019)

DTC P0190: Fuel Rail Pressure Sensor Circuit Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor for out of range malfunctions. If the fuel rail pressure sensor is within a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of the conditions is met:

- Out of range high The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 4.74701 V to 4.82666 V for at least 1 second.

The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 4.74701 V to 4.82666 V for at least 1 second.

- Out of range low The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 0.24170 V to 0.35675 V for at least 1 second.

The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 0.24170 V to 0.35675 V for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Fuel rail pressure sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5363: DTC P0190 (K20C1) (2019 2020 2021)

- Title: DTC P0190 (K20C1) (2019 2020 2021)
- Source path: `pages\6556.html`
- Chunk ID: `chunk_d4d662ff50fa`
- Images: `images\GHH402838.jpeg`
- Duplicate sources: `pages\8143.html`, `pages\23214.html`, `pages\21627.html`

### Full Text

````text
# DTC P0190 (K20C1) (2019 2020 2021)

DTC P0190: Fuel Rail Pressure Sensor Circuit Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor for out of range malfunctions. If the fuel rail pressure sensor is within a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

Either of the conditions is met:

- Out of range high The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 4.75 V to 4.83 V for at least 1 second.

The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 4.75 V to 4.83 V for at least 1 second.

- Out of range low The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 0.24 V to 0.36 V for at least 1 second.

The fuel rail pressure sensor voltage [Fuel Pressure Converted From PF Sensor] is in the range of 0.24 V to 0.36 V for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Fuel rail pressure sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5364: DTC P0191 (K20C1) (2017 2018 2019)

- Title: DTC P0191 (K20C1) (2017 2018 2019)
- Source path: `pages\6557.html`
- Chunk ID: `chunk_6fbc2df3b06b`
- Images: `images\GHH402839.jpeg`
- Duplicate sources: `pages\8144.html`, `pages\23215.html`, `pages\21628.html`

### Full Text

````text
# DTC P0191 (K20C1) (2017 2018 2019)

DTC P0191: Fuel Rail Pressure Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor. Failures in function caused by an open or a short circuits in the electrical circuit can be detected with a pull-up resistor. If the fuel rail pressure sensor is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Range/performance check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 120 rpm | 4, 520 rpm

Fuel rail pressure | 1, 000 kPa (10.2 kgf/cm 2, 145 psi) | -

Fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] | - | 4.40002 V

Relative fuel mass | 5.016 % | -

Injection counter | 4 | -

Other | Fuel rail pressure sensor voltage is valid

[ ]: HDS Parameter

Offset check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3 minutes | -

Fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor]* | 0.24170 V | 4.82666 V

*: Condition is met for at least 0.7 second

Malfunction Threshold

Any of the conditions is met:

- Range/performance check The fuel rail pressure sensor voltage difference between minimum and maximum value over one cycle is 0.0049 V or less for at least 2 seconds.

The fuel rail pressure sensor voltage difference between minimum and maximum value over one cycle is 0.0049 V or less for at least 2 seconds.

- Offset check

- - The error suspicion is set if the fuel rail pressure is below 130 kPa (1.32 kgf/cm 2, 18.8 psi) for at least 0.05 second or greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi). The PCM stores a DTC if the multiplicative correction is below 0.720001 or the additive correction is below -5.016 % of the mixture adaptation. - The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi) and the difference between the pressure before and after the fuel pump is driven is greater than 250 kPa (2.55 kgf/cm 2, 36.3 psi).

- - The error suspicion is set if the fuel rail pressure is below 130 kPa (1.32 kgf/cm 2, 18.8 psi) for at least 0.05 second or greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi). The PCM stores a DTC if the multiplicative correction is below 0.720001 or the additive correction is below -5.016 % of the mixture adaptation.

The error suspicion is set if the fuel rail pressure is below 130 kPa (1.32 kgf/cm 2, 18.8 psi) for at least 0.05 second or greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi). The PCM stores a DTC if the multiplicative correction is below 0.720001 or the additive correction is below -5.016 % of the mixture adaptation.

- - The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi) and the difference between the pressure before and after the fuel pump is driven is greater than 250 kPa (2.55 kgf/cm 2, 36.3 psi).

The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi) and the difference between the pressure before and after the fuel pump is driven is greater than 250 kPa (2.55 kgf/cm 2, 36.3 psi).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Fuel rail pressure low

- Fuel rail pressure high

- Vacuum leaks

- Fuel rail pressure sensor PF line open

- Fuel rail pressure sensor PF line short to ground

- Fuel rail pressure sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5365: DTC P0191 (K20C1) (2019 2020 2021)

- Title: DTC P0191 (K20C1) (2019 2020 2021)
- Source path: `pages\6558.html`
- Chunk ID: `chunk_bad5b846e97e`
- Images: `images\GHH402840.jpeg`
- Duplicate sources: `pages\8145.html`, `pages\23216.html`, `pages\21629.html`

### Full Text

````text
# DTC P0191 (K20C1) (2019 2020 2021)

DTC P0191: Fuel Rail Pressure Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor. Failures in function caused by an open or a short circuits in the electrical circuit can be detected with a pull-up resistor. If the fuel rail pressure sensor is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more*, 0.5 second or more**

DTC Type | One drive cycle, MIL on

*: Signal stuck check

**: Offset check

Enable Conditions

Signal stuck check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 120 rpm | 4, 520 rpm

Fuel rail pressure | 1, 000 kPa (10.2 kgf/cm 2, 145 psi) | -

Fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] | - | 4.4 V

Relative fuel mass | 5.02 % | -

Injection counter | 4 | -

[ ]: HDS Parameter

Offset check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 3 minutes | -

Malfunction Threshold

Any of the conditions is met:

- Signal stuck check The fuel rail pressure sensor voltage difference between minimum and maximum value over one cycle is 0 V or less.

The fuel rail pressure sensor voltage difference between minimum and maximum value over one cycle is 0 V or less.

- Offset check The error suspicion is set if the fuel rail pressure is below 130 kPa (1.32 kgf/cm 2, 18.8 psi) for at least 0.05 second or greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi). The PCM confirms the failure if any of the following conditions occur:

The error suspicion is set if the fuel rail pressure is below 130 kPa (1.32 kgf/cm 2, 18.8 psi) for at least 0.05 second or greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi). The PCM confirms the failure if any of the following conditions occur:

- - The multiplicative correction is 0.72 or less or the additive correction is -5.02 % or less of the mixture adaptation. - The multiplicative correction is 1.28 or more or the additive correction is 5.02 % or more of the mixture adaptation. - The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi).

- - The multiplicative correction is 0.72 or less or the additive correction is -5.02 % or less of the mixture adaptation.

The multiplicative correction is 0.72 or less or the additive correction is -5.02 % or less of the mixture adaptation.

- - The multiplicative correction is 1.28 or more or the additive correction is 5.02 % or more of the mixture adaptation.

The multiplicative correction is 1.28 or more or the additive correction is 5.02 % or more of the mixture adaptation.

- - The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi).

The fuel rail pressure is greater than 1, 300 kPa (13.26 kgf/cm 2, 188.6 psi).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Fuel rail pressure low

- Fuel rail pressure high

- Vacuum leaks

- Fuel rail pressure sensor PF line open

- Fuel rail pressure sensor PF line short to ground

- Fuel rail pressure sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5366: DTC P0191 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0191 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6559.html`
- Chunk ID: `chunk_d1a7abee08ae`
- Images: `images\GHH402841.jpeg`, `images\GHH402842.jpeg`
- Duplicate sources: `pages\8146.html`, `pages\23217.html`, `pages\21630.html`

### Full Text

````text
# DTC P0191 (Si) (2017 2018 2019 2020 2021)

DTC P0191: Fuel Rail Pressure Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel rail pressure sensor senses fuel pressure and converts it into electrical signals. The powertrain control module (PCM) adjusts to a specified fuel pressure by controlling the high pressure fuel pump solenoid based on the fuel rail pressure sensor output signal. The fuel rail pressure sensor outputs low signal voltage at low fuel pressure and high signal voltage at high fuel pressure. If the fuel rail pressure sensor output voltage is a specified range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The fuel rail pressure sensor output voltage [FUEL PRESSURE CONVERTED FROM PF SENSOR] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel rail pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5367: DTC P0192, P0193 (K20C1) (2017 2018 2019)

- Title: DTC P0192, P0193 (K20C1) (2017 2018 2019)
- Source path: `pages\6560.html`
- Chunk ID: `chunk_5f7381f102d7`
- Images: `images\GHH402843.jpeg`
- Duplicate sources: `pages\8147.html`, `pages\23218.html`, `pages\21631.html`

### Full Text

````text
# DTC P0192, P0193 (K20C1) (2017 2018 2019)

DTC P0192: Fuel Rail Pressure Sensor Circuit Low Voltage

DTC P0193: Fuel Rail Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor. Failures in function caused by an open or short circuits in the electrical circuit can be detected with a pull-up resistor. If the fuel rail pressure sensor output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0192

The fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] is less than 0.2417 V for at least 0.5 second.

DTC: P0193

The fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] is greater than 4.82666 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0192

- Fuel rail pressure sensor PF line short to power

DTC: P0193

- Fuel rail pressure sensor PF line short to power

- Fuel rail pressure sensor PF line open

- Fuel rail pressure sensor SG line open

Common

- Fuel rail pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5368: DTC P0192, P0193 (K20C1) (2019 2020 2021)

- Title: DTC P0192, P0193 (K20C1) (2019 2020 2021)
- Source path: `pages\6561.html`
- Chunk ID: `chunk_381eae503587`
- Images: `images\GHH402844.jpeg`
- Duplicate sources: `pages\8148.html`, `pages\23219.html`, `pages\21632.html`

### Full Text

````text
# DTC P0192, P0193 (K20C1) (2019 2020 2021)

DTC P0192: Fuel Rail Pressure Sensor Circuit Low Voltage

DTC P0193: Fuel Rail Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the sensor signal of the fuel rail pressure sensor. Failures in function caused by an open or short circuits in the electrical circuit can be detected with a pull-up resistor. If the fuel rail pressure sensor output voltage is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0192

The fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] is less than 0.24 V for at least 0.5 second.

DTC: P0193

The fuel rail pressure sensor output voltage [Fuel Pressure Converted From PF Sensor] is greater than 4.83 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0192

- Fuel rail pressure sensor PF line short to power

- Fuel rail pressure sensor VCC line open

DTC: P0193

- Fuel rail pressure sensor PF line short to power

- Fuel rail pressure sensor PF line open

- Fuel rail pressure sensor SG line open

Common

- Fuel rail pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5369: DTC P0192, P0193 (L15B7/L15BA/L15BY)

- Title: DTC P0192, P0193 (L15B7/L15BA/L15BY)
- Source path: `pages\6562.html`
- Chunk ID: `chunk_06165ef15cda`
- Images: `images\GHH402845.jpeg`, `images\GHH402846.jpeg`
- Duplicate sources: `pages\8149.html`, `pages\23220.html`, `pages\21633.html`

### Full Text

````text
# DTC P0192, P0193 (L15B7/L15BA/L15BY)

DTC P0192: Fuel Rail Pressure Sensor Circuit Low Voltage

DTC P0193: Fuel Rail Pressure Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel rail pressure sensor senses fuel pressure and converts it into electrical signals. The powertrain control module (PCM) adjusts to a specified fuel pressure by controlling the high pressure fuel pump solenoid based on the fuel rail pressure sensor output signal. The fuel rail pressure sensor outputs low signal voltage at low fuel pressure and high signal voltage at high fuel pressure. If the fuel rail pressure sensor output voltage is out of a specified range for predetermined time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.5 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0192

The fuel rail pressure sensor output voltage [FUEL PRESSURE CONVERTED FROM PF SENSOR] is 0.31 V or less for at least 1.5 seconds.

DTC: P0193

The fuel rail pressure sensor output voltage [FUEL PRESSURE CONVERTED FROM PF SENSOR] is 4.89 V or more for at least 1.5 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0192

- Fuel rail pressure sensor VCC line open

- Fuel rail pressure sensor PF line short to ground

DTC: P0193

- Fuel rail pressure sensor SG line open

- Fuel rail pressure sensor PF line open

Common

- Fuel rail pressure sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5370: DTC P0201, P0202, P0203, P0204 (K20C1) (2017 2018 2019)

- Title: DTC P0201, P0202, P0203, P0204 (K20C1) (2017 2018 2019)
- Source path: `pages\6563.html`
- Chunk ID: `chunk_51a0956e9415`
- Images: `images\GHH402847.jpeg`
- Duplicate sources: `pages\8150.html`, `pages\23221.html`, `pages\21634.html`

### Full Text

````text
# DTC P0201, P0202, P0203, P0204 (K20C1) (2017 2018 2019)

DTC P0201: No. 1 Cylinder Injector Circuit Malfunction

DTC P0202: No. 2 Cylinder Injector Circuit Malfunction

DTC P0203: No. 3 Cylinder Injector Circuit Malfunction

DTC P0204: No. 4 Cylinder Injector Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the injector driver for electrical malfunctions. The driver of the injector is continuously monitored until the fault counter reaches a defined threshold. If the PCM detects abnormal conditions for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.06 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects short (short to ground, short to power, or short to another line) or an open in injector circuits for at least 0.06 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0201

- No. 1 injector INJ H1 line open

- No. 1 injector INJ H1 line short to power

- No. 1 injector INJ H1 line short to ground

- No. 1 injector INJ L1 line open

- No. 1 injector INJ L1 line short to power

- No. 1 injector INJ L1 line short to ground

- No. 1 injector INJ H1 line short to No. 1 injector INJ L1 line

- No. 1 injector failure

DTC: P0202

- No. 2 injector INJ H2 line open

- No. 2 injector INJ H2 line short to power

- No. 2 injector INJ H2 line short to ground

- No. 2 injector INJ L2 line open

- No. 2 injector INJ L2 line short to power

- No. 2 injector INJ L2 line short to ground

- No. 2 injector INJ H2 line short to No. 2 injector INJ L2 line

- No. 2 injector failure

DTC: P0203

- No. 3 injector INJ H3 line open

- No. 3 injector INJ H3 line short to power

- No. 3 injector INJ H3 line short to ground

- No. 3 injector INJ L3 line open

- No. 3 injector INJ L3 line short to power

- No. 3 injector INJ L3 line short to ground

- No. 3 injector INJ H3 line short to No. 3 injector INJ L3 line

- No. 3 injector failure

DTC: P0204

- No. 4 injector INJ H4 line open

- No. 4 injector INJ H4 line short to power

- No. 4 injector INJ H4 line short to ground

- No. 4 injector INJ L4 line open

- No. 4 injector INJ L4 line short to power

- No. 4 injector INJ L4 line short to ground

- No. 4 injector INJ H4 line short to No. 4 injector INJ L4 line

- No. 4 injector failure

Common

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5371: DTC P0201, P0202, P0203, P0204 (K20C1) (2019 2020 2021)

- Title: DTC P0201, P0202, P0203, P0204 (K20C1) (2019 2020 2021)
- Source path: `pages\6564.html`
- Chunk ID: `chunk_cf228fc1d44b`
- Images: `images\GHH402848.jpeg`
- Duplicate sources: `pages\8151.html`, `pages\23222.html`, `pages\21635.html`

### Full Text

````text
# DTC P0201, P0202, P0203, P0204 (K20C1) (2019 2020 2021)

DTC P0201: No. 1 Cylinder Injector Circuit Malfunction

DTC P0202: No. 2 Cylinder Injector Circuit Malfunction

DTC P0203: No. 3 Cylinder Injector Circuit Malfunction

DTC P0204: No. 4 Cylinder Injector Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the injector driver for electrical malfunctions. The driver of the injector is continuously monitored until the fault counter reaches a defined threshold. If the PCM detects abnormal conditions for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects short (short to ground, short to power, or short to another line) or an open in injector circuits at least 3 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0201

- No. 1 injector INJ H1 line open

- No. 1 injector INJ H1 line short to power

- No. 1 injector INJ H1 line short to ground

- No. 1 injector INJ L1 line open

- No. 1 injector INJ L1 line short to power

- No. 1 injector INJ L1 line short to ground

- No. 1 injector INJ H1 line short to No. 1 injector INJ L1 line

- No. 1 injector failure

DTC: P0202

- No. 2 injector INJ H2 line open

- No. 2 injector INJ H2 line short to power

- No. 2 injector INJ H2 line short to ground

- No. 2 injector INJ L2 line open

- No. 2 injector INJ L2 line short to power

- No. 2 injector INJ L2 line short to ground

- No. 2 injector INJ H2 line short to No. 2 injector INJ L2 line

- No. 2 injector failure

DTC: P0203

- No. 3 injector INJ H3 line open

- No. 3 injector INJ H3 line short to power

- No. 3 injector INJ H3 line short to ground

- No. 3 injector INJ L3 line open

- No. 3 injector INJ L3 line short to power

- No. 3 injector INJ L3 line short to ground

- No. 3 injector INJ H3 line short to No. 3 injector INJ L3 line

- No. 3 injector failure

DTC: P0204

- No. 4 injector INJ H4 line open

- No. 4 injector INJ H4 line short to power

- No. 4 injector INJ H4 line short to ground

- No. 4 injector INJ L4 line open

- No. 4 injector INJ L4 line short to power

- No. 4 injector INJ L4 line short to ground

- No. 4 injector INJ H4 line short to No. 4 injector INJ L4 line

- No. 4 injector failure

Common

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5372: DTC P0201, P0202, P0203, P0204 (K20C2)

- Title: DTC P0201, P0202, P0203, P0204 (K20C2)
- Source path: `pages\6565.html`
- Chunk ID: `chunk_ffe076664462`
- Images: `images\GHH402849.jpeg`
- Duplicate sources: `pages\8152.html`, `pages\23223.html`, `pages\21636.html`

### Full Text

````text
# DTC P0201, P0202, P0203, P0204 (K20C2)

DTC P0201: No. 1 Cylinder Injector Circuit Malfunction

DTC P0202: No. 2 Cylinder Injector Circuit Malfunction

DTC P0203: No. 3 Cylinder Injector Circuit Malfunction

DTC P0204: No. 4 Cylinder Injector Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The injector supplies fuel to the engine and is controlled by the powertrain control module (PCM) ON/OFF command. In the PCM, the injector driver receives a drive commands from the CPU and drives the injector. The CPU monitors a terminal voltage of PCM by the return signal circuit. If the return signal from the injector does not change for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more (at idle)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

State of the engine | Running

Other | Other than during fuel cut-off operation

[ ]: HDS Parameter

Malfunction Threshold

The return signal from the injector does not change at least 30 times (counts once per engine cycle).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0201

- No. 1 injector failure

- No. 1 injector INJ1 line open

- No. 1 injector line INJ1 short to ground

- No. 1 injector line INJ1 short to power

- No. 1 injector power supply line open

DTC: P0202

- No. 2 injector failure

- No. 2 injector INJ2 line open

- No. 2 injector INJ2 line short to ground

- No. 2 injector INJ2 line short to power

- No. 2 injector power supply line open

DTC: P0203

- No. 3 injector failure

- No. 3 injector INJ3 line open

- No. 3 injector INJ3 line short to ground

- No. 3 injector INJ3 line short to power

- No. 3 injector power supply line open

DTC: P0204

- No. 4 injector failure

- No. 4 injector INJ4 line open

- No. 4 injector INJ4 line short to ground

- No. 4 injector INJ4 line short to power

- No. 4 injector power supply line open

Common

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5373: DTC P0201, P0202, P0203, P0204 (L15B7/L15BA/L15BY)

- Title: DTC P0201, P0202, P0203, P0204 (L15B7/L15BA/L15BY)
- Source path: `pages\6566.html`
- Chunk ID: `chunk_2cb6d232e3eb`
- Images: `images\GHH402850.jpeg`
- Duplicate sources: `pages\8153.html`, `pages\23224.html`, `pages\21637.html`

### Full Text

````text
# DTC P0201, P0202, P0203, P0204 (L15B7/L15BA/L15BY)

DTC P0201: No. 1 Cylinder Injector Circuit Malfunction

DTC P0202: No. 2 Cylinder Injector Circuit Malfunction

DTC P0203: No. 3 Cylinder Injector Circuit Malfunction

DTC P0204: No. 4 Cylinder Injector Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The injector supplies fuel to the engine and is controlled by the powertrain control module (PCM) ON/OFF command. In the PCM, the injector driver receives a drive commands from the CPU and drives the injector. The CPU monitors injector currents and return signal from the injector driver to monitor a terminal voltage of PCM. If the monitored conditions are abnormal for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10 V | -

State of the engine | Running

Crankshaft position (CKP) sensor | Normal

Camshaft position (CMP) sensor | Normal

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs at least 30 times (counts once per engine cycle):

- Symptom: Injector current not flowing The injector current is 0.2 A to 1 A or less*.

The injector current is 0.2 A to 1 A or less*.

- Symptom: Injector over current The injector current is 12 A to 20 A or more*.

The injector current is 12 A to 20 A or more*.

- Symptom: PCM terminal (to injector) short to ground The PCM terminal (to injector) voltage is 1 V to 1.3 V or less*.

The PCM terminal (to injector) voltage is 1 V to 1.3 V or less*.

- Symptom: PCM terminal (to injector) short to power The PCM terminal (to injector) voltage is 4.6 V to 5 V or more*.

The PCM terminal (to injector) voltage is 4.6 V to 5 V or more*.

- Symptom: Return signal abnormal The return signal does not change.

The return signal does not change.

*: Varies with driving condition.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0201

- No. 1 injector failure

- No. 1 injector line open

- No. 1 injector line short to ground

- No. 1 injector line short to power

- No. 4 injector line short to ground

DTC: P0202

- No. 2 injector failure

- No. 2 injector line open

- No. 2 injector line short to ground

- No. 2 injector line short to power

- No. 3 injector line short to ground

DTC: P0203

- No. 3 injector failure

- No. 3 injector line open

- No. 3 injector line short to ground

- No. 3 injector line short to power

- No. 2 injector line short to ground

DTC: P0204

- No. 4 injector failure

- No. 4 injector line open

- No. 4 injector line short to ground

- No. 4 injector line short to power

- No. 1 injector line short to ground

Common

- Injector relay failure

- PCM internal circuit failure (injector driver power supply line open)

- High pressure fuel pump failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5374: DTC P0221 (K20C1) (2017 2018 2019)

- Title: DTC P0221 (K20C1) (2017 2018 2019)
- Source path: `pages\6567.html`
- Chunk ID: `chunk_4020ab0684bd`
- Images: `images\GHH402851.jpeg`, `images\GHH402852.jpeg`
- Duplicate sources: `pages\8154.html`, `pages\23225.html`, `pages\21638.html`

### Full Text

````text
# DTC P0221 (K20C1) (2017 2018 2019)

DTC P0221: Throttle Position (TP) Sensor B Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit for physical range check. The diagnostic compares the voltages of the throttle position sensor A read at the closed and open positions of the throttle valve with their respective calibrated threshold values. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

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

- The TP sensor B output voltage [TP Sensor B] read at the closed position of the throttle valve is greater than 4.58252 V.

- The TP sensor B output voltage [TP Sensor B] read at the open position of the throttle valve is less than 0.62012 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TP sensor B contact resistance changed

- Throttle body failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5375: DTC P0221 (K20C1) (2019 2020 2021)

- Title: DTC P0221 (K20C1) (2019 2020 2021)
- Source path: `pages\6568.html`
- Chunk ID: `chunk_39608ebd50f5`
- Images: `images\GHH402853.jpeg`, `images\GHH402854.jpeg`
- Duplicate sources: `pages\8155.html`, `pages\23226.html`, `pages\21639.html`

### Full Text

````text
# DTC P0221 (K20C1) (2019 2020 2021)

DTC P0221: Throttle Position (TP) Sensor B Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit for physical range check. The diagnostic compares the voltages of the throttle position sensor A read at the closed and open positions of the throttle valve with their respective calibrated threshold values. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

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

- The TP sensor B output voltage [TP Sensor B] read at the closed position of the throttle valve is 4.8 V or less, or more than 4.58 V.

- The TP sensor B output voltage [TP Sensor B] read at the open position of the throttle valve is 0.2 V or more, or less than 0.62 V.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TP sensor B contact resistance changed

- Throttle body failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5376: DTC P0221 (K20C2) (2018 2019 2020 2021)

- Title: DTC P0221 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\6569.html`
- Chunk ID: `chunk_e278b956c675`
- Images: `images\GHH402855.jpeg`
- Duplicate sources: `pages\8156.html`, `pages\23227.html`, `pages\21640.html`

### Full Text

````text
# DTC P0221 (K20C2) (2018 2019 2020 2021)

DTC P0221: Throttle Position (TP) Sensor B Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). TP sensor B is a semiconductor type, and it is attached to the throttle body and shaft to determine throttle valve position. The throttle valve position signal from TP sensor B is transmitted to the PCM for target position feedback control. If the signal voltage from TP sensor B is a set value for a specified time, the PCM detects a TP sensor B malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The TP sensor B output voltage [TP SENSOR B] is 0.48 V or less, or 4.61 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body internal failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5377: DTC P0221 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P0221 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\6570.html`
- Chunk ID: `chunk_39c1484c6951`
- Images: `images\GHH402856.jpeg`
- Duplicate sources: `pages\8157.html`, `pages\23228.html`, `pages\21641.html`

### Full Text

````text
# DTC P0221 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P0221: Throttle Position (TP) Sensor B Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). TP sensor B is a semiconductor type, and it is attached to the throttle body and shaft to determine throttle valve position. The throttle valve position signal from TP sensor B is transmitted to the PCM for target position feedback control. If the signal voltage from TP sensor B is a set value for a specified time, the PCM detects a TP sensor B malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The TP sensor B output voltage [TP SENSOR B] is 0.48 V or less, or 4.61 V or more for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body internal failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5378: DTC P0221 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0221 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6571.html`
- Chunk ID: `chunk_0208ceb88445`
- Images: `images\GHH402857.jpeg`
- Duplicate sources: `pages\8158.html`, `pages\23229.html`, `pages\21642.html`

### Full Text

````text
# DTC P0221 (Si) (2017 2018 2019 2020 2021)

DTC P0221: Throttle Position (TP) Sensor B Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). TP sensor B is a semiconductor type, and it is attached to the throttle body and shaft to determine throttle valve position. The throttle valve position signal from TP sensor B is transmitted to the PCM for target position feedback control. If the signal voltage from TP sensor B is a specified range for a specified time, the PCM detects a TP sensor B malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The TP sensor B output voltage [TP SENSOR B] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Throttle body internal failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5379: DTC P0222, P0223 (K20C1) (2017 2018 2019)

- Title: DTC P0222, P0223 (K20C1) (2017 2018 2019)
- Source path: `pages\6572.html`
- Chunk ID: `chunk_c23dbade5cae`
- Images: `images\GHH402858.jpeg`, `images\GHH402859.jpeg`
- Duplicate sources: `pages\8159.html`, `pages\23230.html`, `pages\21643.html`

### Full Text

````text
# DTC P0222, P0223 (K20C1) (2017 2018 2019)

DTC P0222: Throttle Position (TP) Sensor B Circuit Low Voltage

DTC P0223: Throttle Position (TP) Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit and the throttle position (TP) sensor B circuit for electrical malfunctions. In order to provide electrical diagnostics the output voltage of both sensors are continuously monitored and compared with minimum and maximum thresholds. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.14 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P0222

The TP sensor B output voltage [TP Sensor B] is less than 0.195 V for at least 0.14 second.

DTC: P0223

The TP sensor B output voltage [TP Sensor B] is greater than 4.805 V for at least 0.14 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0222

- TP sensor B THL2 line short to ground

- TP sensor B VCC line open

DTC: P0223

- TP sensor B THL2 line short to power

- TP sensor B THL2 line open

- TP sensor B SG line open

Common

- Throttle body failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5380: DTC P0222, P0223 (K20C1) (2019 2020 2021)

- Title: DTC P0222, P0223 (K20C1) (2019 2020 2021)
- Source path: `pages\6573.html`
- Chunk ID: `chunk_7343c708fc6e`
- Images: `images\GHH402860.jpeg`, `images\GHH402861.jpeg`
- Duplicate sources: `pages\8160.html`, `pages\23231.html`, `pages\21644.html`

### Full Text

````text
# DTC P0222, P0223 (K20C1) (2019 2020 2021)

DTC P0222: Throttle Position (TP) Sensor B Circuit Low Voltage

DTC P0223: Throttle Position (TP) Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the throttle position (TP) sensor A circuit and the throttle position (TP) sensor B circuit for electrical malfunctions. In order to provide electrical diagnostics the output voltage of both sensors are continuously monitored and compared with minimum and maximum thresholds. If the TP sensor B output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.14 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P0222

The TP sensor B output voltage [TP Sensor B] is less than 0.2 V for at least 0.14 second.

DTC: P0223

The TP sensor B output voltage [TP Sensor B] is greater than 4.8 V for at least 0.14 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0222

- TP sensor B THL2 line short to ground

- TP sensor B VCC line open

DTC: P0223

- TP sensor B THL2 line short to power

- TP sensor B THL2 line open

- TP sensor B SG line open

Common

- Throttle body failure (TP sensor B)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5381: DTC P0222, P0223 (K20C2)

- Title: DTC P0222, P0223 (K20C2)
- Source path: `pages\6574.html`
- Chunk ID: `chunk_c8ffefe75274`
- Images: `images\GHH402862.jpeg`
- Duplicate sources: `pages\8161.html`, `pages\23232.html`, `pages\21645.html`

### Full Text

````text
# DTC P0222, P0223 (K20C2)

DTC P0222: Throttle Position (TP) Sensor B Circuit Low Voltage

DTC P0223: Throttle Position (TP) Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). TP sensor B is a semiconductor type, and it is attached to the throttle body and shaft to determine throttle valve position. The throttle valve position signal from TP sensor B is transmitted to the PCM for target position feedback control. If the signal from TP sensor B is a fixed value for a set time, the PCM detects a TP sensor B malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0222

The TP sensor B output voltage [TP SENSOR B] is 0.3 V or less for at least 200 milliseconds.

DTC: P0223

The TP sensor B output voltage [TP SENSOR B] is 4.8 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0222

- TP sensor B THL2 line short to ground

- TP sensor B VCC (DBW) line open

DTC: P0223

- TP sensor B THL2 line open

- TP sensor B SG (DBW) line open

Common

- TP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5382: DTC P0222, P0223 (L15B7/L15BA/L15BY)

- Title: DTC P0222, P0223 (L15B7/L15BA/L15BY)
- Source path: `pages\6575.html`
- Chunk ID: `chunk_a6046cf2ea42`
- Images: `images\GHH402863.jpeg`
- Duplicate sources: `pages\8162.html`, `pages\23233.html`, `pages\21646.html`

### Full Text

````text
# DTC P0222, P0223 (L15B7/L15BA/L15BY)

DTC P0222: Throttle Position (TP) Sensor B Circuit Low Voltage

DTC P0223: Throttle Position (TP) Sensor B Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The electronic throttle control system controls the throttle valve opening. The system includes the throttle actuator, the throttle valve, throttle position (TP) sensors A and B, the PGM-FI subrelay circuit, the accelerator pedal position (APP) sensor, and the powertrain control module (PCM). TP sensor B is a semiconductor type, and it is attached to the throttle body and shaft to determine throttle valve position. The throttle valve position signal from TP sensor B is transmitted to the PCM for target position feedback control. If the signal from TP sensor B is a fixed value for a set time, the PCM detects a TP sensor B malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 200 milliseconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0222

The TP sensor B output voltage [TP SENSOR B] is 0.3 V or less for at least 200 milliseconds.

DTC: P0223

The TP sensor B output voltage [TP SENSOR B] is 4.8 V or more for at least 200 milliseconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0222

- TP sensor B THL2 line short to ground

- TP sensor B VCC line open

DTC: P0223

- TP sensor B THL2 line open

- TP sensor B SG line open

Common

- TP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5383: DTC P0230 (K20C1) (2017 2018 2019)

- Title: DTC P0230 (K20C1) (2017 2018 2019)
- Source path: `pages\6576.html`
- Chunk ID: `chunk_9c7ccaeb95bc`
- Images: `images\GHH402864.jpeg`
- Duplicate sources: `pages\8163.html`, `pages\23234.html`, `pages\21647.html`

### Full Text

````text
# DTC P0230 (K20C1) (2017 2018 2019)

DTC P0230: Fuel Pump Primary Circuit

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel pump control circuit for electrical malfunctions. The diagnosis is disabled under certain battery voltage conditions. The described diagnosis will detect short circuits and open circuit. If the PCM detects any of these circuit faults, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.1 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The fuel pump driver reports open, short to ground, or short to power for at least 0.1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 2 FUEL PUMP RLY CL- line short to power

- PGM-FI main relay 2 FUEL PUMP RLY CL- line short to ground

- PGM-FI main relay 2 FUEL PUMP RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5384: DTC P0230 (K20C1) (2019 2020 2021)

- Title: DTC P0230 (K20C1) (2019 2020 2021)
- Source path: `pages\6577.html`
- Chunk ID: `chunk_c805ca73e6e4`
- Images: `images\GHH402865.jpeg`
- Duplicate sources: `pages\8164.html`, `pages\23235.html`, `pages\21648.html`

### Full Text

````text
# DTC P0230 (K20C1) (2019 2020 2021)

DTC P0230: Fuel Pump Primary Circuit

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the fuel pump control circuit for electrical malfunctions. The diagnosis is disabled under certain 12 volt battery voltage conditions. The described diagnosis will detect short circuits and open circuit. If the PGM-FI main relay 2 output voltage or current is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.1 second or more

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

- Open circuit The PGM-FI main relay 2 output voltage is between 3.26 - 4.7 V when the PGM-FI main relay 2 power stage is off.

The PGM-FI main relay 2 output voltage is between 3.26 - 4.7 V when the PGM-FI main relay 2 power stage is off.

- Short circuit to power The PGM-FI main relay 2 output current is 2 A or more when the PGM-FI main relay 2 power stage is on.

The PGM-FI main relay 2 output current is 2 A or more when the PGM-FI main relay 2 power stage is on.

- Short circuit to ground The PGM-FI main relay 2 output voltage is 2.74 V or less when the PGM-FI main relay 2 power stage is off.

The PGM-FI main relay 2 output voltage is 2.74 V or less when the PGM-FI main relay 2 power stage is off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PGM-FI main relay 2 FUEL PUMP RLY CL- line short to power

- PGM-FI main relay 2 FUEL PUMP RLY CL- line short to ground

- PGM-FI main relay 2 FUEL PUMP RLY CL- line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5385: DTC P0234 (K20C1) (2017 2018 2019)

- Title: DTC P0234 (K20C1) (2017 2018 2019)
- Source path: `pages\6578.html`
- Chunk ID: `chunk_cff2188f9053`
- Images: `images\GHH402866.jpeg`
- Duplicate sources: `pages\8165.html`, `pages\23236.html`, `pages\21649.html`

### Full Text

````text
# DTC P0234 (K20C1) (2017 2018 2019)

DTC P0234: Turbocharger Overboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The boost pressure control monitor is utilized to detect possible errors of the turbocharger system. The turbocharger consists of two elements, a turbine and a compressor, which are connected by a single shaft. The boost control apparatus consists of turbocharger wastegate control actuator that is connected to the turbocharger wastegate control valve passing through the turbine housing. The electronically controlled turbocharger wastegate control valve delivers the resulting boost pressure. In order to provide boost pressure control diagnosis, the actual boost pressure upstream of the throttle valve is monitored against desired boost pressure under certain conditions. There are two types of boost pressure control deviation errors distinguished. If either of the following errors is detected, the PCM detects a malfunction and stores a DTC.

- Overcharging error: Negative boost pressure control deviation. The actual boost pressure exceeds the desired boost pressure value.

- Undercharging error: Positive boost pressure control deviation. The desired boost pressure exceeds the actual boost pressure value.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Other | Turbocharger boost sensor value is valid

Malfunction Threshold

The difference between measured pressure upstream throttle valve and desired pressure upstream throttle valve is 20 kPa (150.2 mmHg, 6 inHg) - 100 kPa (750.7 mmHg, 30 inHg) or more for at least 2 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator stuck

- Leakage in turbocharger system

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at engine speed [Engine Speed] 3, 200 rpm or more with high load.

[ ]: HDS Parameter

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5386: DTC P0234 (K20C1) (2019 2020 2021)

- Title: DTC P0234 (K20C1) (2019 2020 2021)
- Source path: `pages\6579.html`
- Chunk ID: `chunk_49f156b78af3`
- Images: `images\GHH402867.jpeg`
- Duplicate sources: `pages\8166.html`, `pages\23237.html`, `pages\21650.html`

### Full Text

````text
# DTC P0234 (K20C1) (2019 2020 2021)

DTC P0234: Turbocharger Overboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The boost pressure control monitor is utilized to detect possible errors of the turbocharger system. The turbocharger consists of two elements, a turbine and a compressor, which are connected by a single shaft. The boost control apparatus consists of turbocharger wastegate control actuator that is connected to the turbocharger wastegate control valve passing through the turbine housing. The electronically controlled turbocharger wastegate control valve delivers the resulting boost pressure. In order to provide boost pressure control diagnosis, the actual boost pressure upstream of the throttle valve is monitored against desired boost pressure under certain conditions. There are two types of boost pressure control deviation errors distinguished. If either of the following errors is detected, the PCM detects a malfunction and stores a DTC.

- Overcharging error: Negative boost pressure control deviation. The actual boost pressure exceeds the desired boost pressure value.

- Undercharging error: Positive boost pressure control deviation. The desired boost pressure exceeds the actual boost pressure value.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed] | 2 mph (3 km/h) | -

[ ]: HDS Parameter

Malfunction Threshold

The difference between commanded pressure upstream throttle valve and measured pressure upstream throttle valve is 20 kPa (150 mmHg, 5.9 inHg) - 100 kPa (750 mmHg, 29.6 inHg) or more for at least 2 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator stuck

- Leakage in turbocharger system

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at engine speed [Engine Speed] 3, 200 rpm or more with high load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5387: DTC P0234 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)

- Title: DTC P0234 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)
- Source path: `pages\6580.html`
- Chunk ID: `chunk_1ae9e2428749`
- Images: `images\GHH402868.jpeg`, `images\GHH402869.jpeg`
- Duplicate sources: `pages\8167.html`, `pages\23238.html`, `pages\21651.html`

### Full Text

````text
# DTC P0234 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)

DTC P0234: Turbocharger Overboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger boost pressure so that the boost pressure to the engine does not exceed the set upper pressure limit. When the boost pressure increases abnormally, a malfunction of the turbocharger control system is determined and fuel cut and throttle restriction control is done to protect the powertrain.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.0 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Other | No change of boost pressure upper limit

[ ]: HDS Parameter

Malfunction Threshold

Either one of conditions is met for at least 1.0 second, and fuel cut-off is operated for engine protection.

- The boost pressure is 148 - 305 kPa (1, 109 - 2, 291 mmHg, 43.7 - 90.1 inHg) or more*

- The intake air pressure is 216 - 305 kPa (1, 614 - 2, 291 mmHg, 63.6 - 90.1 inHg) or more*

*: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck close failure

- Turbocharger wastegate control actuator stuck close failure

- Turbocharger wastegate control valve bypass clogged

- PCM internal circuit failure (BARO sensor)

- Turbocharger boost sensor internal failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at engine speed [ENGINE SPEED] at 1, 200 rpm or more for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5388: DTC P0234 (L15B7 (except Si)/L15BY) (2019 2020 2021)

- Title: DTC P0234 (L15B7 (except Si)/L15BY) (2019 2020 2021)
- Source path: `pages\6581.html`
- Chunk ID: `chunk_4e0d0c060094`
- Images: `images\GHH402870.jpeg`, `images\GHH402871.jpeg`
- Duplicate sources: `pages\8168.html`, `pages\23239.html`, `pages\21652.html`

### Full Text

````text
# DTC P0234 (L15B7 (except Si)/L15BY) (2019 2020 2021)

DTC P0234: Turbocharger Overboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger boost pressure so that the boost pressure to the engine does not exceed the set upper pressure limit. When the boost pressure increases abnormally, a malfunction of the turbocharger control system is determined and fuel cut and throttle restriction control is done to protect the powertrain.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.0 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Other | No change of boost pressure upper limit

[ ]: HDS Parameter

Malfunction Threshold

Either one of conditions is met for at least 1.0 second, and fuel cut-off is operated for engine protection.

- The boost pressure is 147.8 - 300 kPa (1, 108.4 - 2, 250 mmHg, 43.67 - 88.7 inHg)* 1 (148 - 305 kPa (1, 109 - 2, 291 mmHg, 43.7 - 90.1 inHg))* 2 or more*

- The intake air pressure is 216 - 305 kPa (1, 614 - 2, 291 mmHg, 63.6 - 90.1 inHg) or more*

*1: L15B7*2: L15BA, L15BY*: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck close failure

- Turbocharger wastegate control actuator stuck close failure

- Turbocharger wastegate control valve bypass clogged

- PCM internal circuit failure (BARO sensor)

- Turbocharger boost sensor internal failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive at engine speed [ENGINE SPEED] at 1, 200 rpm or more for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5389: DTC P0234 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0234 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6582.html`
- Chunk ID: `chunk_620b32c3429c`
- Images: `images\GHH402872.jpeg`, `images\GHH402873.jpeg`
- Duplicate sources: `pages\8169.html`, `pages\23240.html`, `pages\21653.html`

### Full Text

````text
# DTC P0234 (Si) (2017 2018 2019 2020 2021)

DTC P0234: Turbocharger Overboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger boost pressure so that the boost pressure to the engine does not exceed the set upper pressure limit. When the boost pressure increases abnormally, a malfunction of the turbocharger control system is determined and fuel cut and throttle restriction control is done to protect the powertrain.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.0 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Other | No change of boost pressure upper limit

[ ]: HDS Parameter

Malfunction Threshold

Either one of conditions is met for at least 1.0 second, and fuel cut-off is operated for engine protection.

- The boost pressure is 148 - 300 kPa (1, 109 - 2, 250 mmHg, 43.7 - 88.6 inHg) or more*

- The intake air pressure is 260 - 292 kPa (1, 948 - 2, 192 mmHg, 76.8 - 86.3 inHg) or more*

*: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck close failure

- Turbocharger wastegate control actuator stuck close failure

- Turbocharger wastegate control valve bypass clogged

- PCM internal circuit failure (BARO sensor)

- Turbocharger boost sensor internal failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive at engine speed [ENGINE SPEED] at 1, 200 rpm or more for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5390: DTC P0235 (L15BA) (2018 2019 2020 2021)

- Title: DTC P0235 (L15BA) (2018 2019 2020 2021)
- Source path: `pages\6583.html`
- Chunk ID: `chunk_aed3c2438adf`
- Images: `images\GHH402874.jpeg`, `images\GHH402875.jpeg`
- Duplicate sources: `pages\8170.html`, `pages\23241.html`, `pages\21654.html`

### Full Text

````text
# DTC P0235 (L15BA) (2018 2019 2020 2021)

DTC P0235: Turbocharger Boost Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The turbocharger boost sensor senses turbocharger boost pressure (vacuum) and converts it into electrical signals. The turbocharger boost sensor outputs low signal voltage at high-vacuum (throttle valve closed) and high signal voltage at low-vacuum (throttle valve wide open). If the signal voltage from the turbocharger boost sensor is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The turbocharger boost sensor output voltage [TC BOOST PRESSURE SENSOR] is 0.37 V or less for at least 6 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5391: DTC P0235 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0235 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6584.html`
- Chunk ID: `chunk_9de9ab137f88`
- Images: `images\GHH402876.jpeg`, `images\GHH402877.jpeg`
- Duplicate sources: `pages\8171.html`, `pages\23242.html`, `pages\21655.html`

### Full Text

````text
# DTC P0235 (Si) (2017 2018 2019 2020 2021)

DTC P0235: Turbocharger Boost Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The turbocharger boost sensor senses turbocharger boost pressure (vacuum) and converts it into electrical signals. The turbocharger boost sensor outputs low signal voltage at high-vacuum (throttle valve closed) and high signal voltage at low-vacuum (throttle valve wide open). If the signal voltage from the turbocharger boost sensor is a specified range for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Few seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The turbocharger boost sensor output voltage [TC BOOST PRESSURE SENSOR] is a specified range for few seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5392: DTC P0236 (K20C1) (2017 2018 2019)

- Title: DTC P0236 (K20C1) (2017 2018 2019)
- Source path: `pages\6585.html`
- Chunk ID: `chunk_2844b4bbacef`
- Images: `images\GHH402878.jpeg`
- Duplicate sources: `pages\8172.html`, `pages\23243.html`, `pages\21656.html`

### Full Text

````text
# DTC P0236 (K20C1) (2017 2018 2019)

DTC P0236: Turbocharger Boost Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the pressure signal of the turbocharger boost sensor. During the range check, the turbocharger booster sensor will be monitored if it is within a physically possible range. If the turbocharger boost sensor output pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Other | Turbocharger boost sensor value is valid

Malfunction Threshold

The turbocharger boost sensor output pressure is greater than 406.29 kPa (3, 047.5 mmHg, 119.978 inHg), or less than 30 kPa (225 mmHg, 8.8 inHg) for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5393: DTC P0236 (K20C1) (2019 2020 2021)

- Title: DTC P0236 (K20C1) (2019 2020 2021)
- Source path: `pages\6586.html`
- Chunk ID: `chunk_8eaa83894350`
- Images: `images\GHH402879.jpeg`
- Duplicate sources: `pages\8173.html`, `pages\23244.html`, `pages\21657.html`

### Full Text

````text
# DTC P0236 (K20C1) (2019 2020 2021)

DTC P0236: Turbocharger Boost Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the pressure signal of the turbocharger boost sensor. During the range check, the turbocharger booster sensor will be monitored if it is within a physically possible range. If the turbocharger boost sensor output pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.2 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Continuous check

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

Turbocharger boost sensor output voltage [TC Boost Pressure Voltage] | 0.16 V | 4.91 V

Other | Above enable conditions are met for at least 0.2 second

Check in post drive

Condition | Minimum | Maximum

Engine speed [Engine Speed] | - | 400 rpm

[ ]: HDS Parameter

Malfunction Threshold

- Continuous check The turbocharger boost sensor output pressure is greater than 406.297 kPa (3, 047.48 mmHg, 119.9795 inHg), or less than 30 kPa (225 mmHg, 8.8 inHg).

The turbocharger boost sensor output pressure is greater than 406.297 kPa (3, 047.48 mmHg, 119.9795 inHg), or less than 30 kPa (225 mmHg, 8.8 inHg).

- Check in post drive The turbocharger boost sensor output pressure is greater than 511.992 kPa (3, 840.25 mmHg, 151.1912 inHg).

The turbocharger boost sensor output pressure is greater than 511.992 kPa (3, 840.25 mmHg, 151.1912 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5394: DTC P0236 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0236 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\6587.html`
- Chunk ID: `chunk_cceb49a8c573`
- Images: `images\GHH402880.jpeg`, `images\GHH402881.jpeg`, `images\GHH402882.jpeg`
- Duplicate sources: `pages\8174.html`, `pages\23245.html`, `pages\21658.html`

### Full Text

````text
# DTC P0236 (L15B7 (except Si)/L15BA/L15BY)

DTC P0236: Turbocharger Boost Sensor Circuit Range/Performance Problem

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

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P0236 if either conditions occur:

- Range "A" determination (P00CF) and range "B" determination (P023D) are determined as abnormal.

- The variation of the turbocharger boost sensor value measured during range "A" determination and range "B" determination is 0.7 kPa (5 mmHg, 0.2 inHg) or less when range "A" determination and range "B" determination are determined as normal and the difference of the BARO sensor value measured during range "A" determination and range "B" determination is 5.4 kPa (40 mmHg, 1.6 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor output range/performance problem

- Turbocharger boost sensor output stuck

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

## Chunk 5395: DTC P0236 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0236 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6588.html`
- Chunk ID: `chunk_e2aab4c47317`
- Images: `images\GHH402883.jpeg`, `images\GHH402884.jpeg`, `images\GHH402885.jpeg`
- Duplicate sources: `pages\8175.html`, `pages\23246.html`, `pages\21659.html`

### Full Text

````text
# DTC P0236 (Si) (2017 2018 2019 2020 2021)

DTC P0236: Turbocharger Boost Sensor Circuit Range/Performance Problem

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

Both range "A" (P00CF) and range "B" (P023D) determinations must be completed. The PCM stores DTC P0236 if either conditions occur:

- Range "A" determination (P00CF) and range "B" determination (P023D) are determined as abnormal.

- The variation of the turbocharger boost sensor value measured during range "A" determination and range "B" determination is 0.7 kPa (5 mmHg, 0.2 inHg) or less when range "A" determination and range "B" determination are determined as normal and the difference of the BARO sensor value measured during range "A" determination and range "B" determination is 5.4 kPa (40 mmHg, 1.6 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger boost sensor output range/performance problem

- Turbocharger boost sensor output stuck

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

## Chunk 5396: DTC P0237, P0238 (K20C1) (2017 2018 2019)

- Title: DTC P0237, P0238 (K20C1) (2017 2018 2019)
- Source path: `pages\6589.html`
- Chunk ID: `chunk_53f7a7aa795b`
- Images: `images\GHH402886.jpeg`
- Duplicate sources: `pages\8176.html`, `pages\23247.html`, `pages\21660.html`

### Full Text

````text
# DTC P0237, P0238 (K20C1) (2017 2018 2019)

DTC P0237: Turbocharger Boost Sensor Circuit Low Voltage

DTC P0238: Turbocharger Boost Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The turbocharger boost sensor converts the measured pressure upstream of the throttle valve (boost pressure). The monitoring function checks the voltage range of the turbocharger boost sensor. If the turbocharger boost sensor output voltage is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0237

The turbocharger boost sensor output voltage [TC Boost Pressure Sensor] is less than 0.161 V for at least 0.5 second.

DTC: P0238

The turbocharger boost sensor output voltage [TC Boost Pressure Sensor] is greater than 4.91 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0237

- Turbocharger boost sensor P3 line short to ground

DTC: P0238

- Turbocharger boost sensor P3 line short to power

- Turbocharger boost sensor P3 line open

Common

- Turbocharger boost sensor failure

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

## Chunk 5397: DTC P0237, P0238 (K20C1) (2019 2020 2021)

- Title: DTC P0237, P0238 (K20C1) (2019 2020 2021)
- Source path: `pages\6590.html`
- Chunk ID: `chunk_5581ac0ff93c`
- Images: `images\GHH402887.jpeg`
- Duplicate sources: `pages\8177.html`, `pages\23248.html`, `pages\21661.html`

### Full Text

````text
# DTC P0237, P0238 (K20C1) (2019 2020 2021)

DTC P0237: Turbocharger Boost Sensor Circuit Low Voltage

DTC P0238: Turbocharger Boost Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The turbocharger boost sensor converts the measured pressure upstream of the throttle valve (boost pressure). The monitoring function checks the voltage range of the turbocharger boost sensor. If the turbocharger boost sensor output voltage is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0237

The turbocharger boost sensor output voltage [TC Boost Pressure Sensor] is less than 0.16 V for at least 0.5 second.

DTC: P0238

The turbocharger boost sensor output voltage [TC Boost Pressure Sensor] is greater than 4.91 V for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0237

- Turbocharger boost sensor P3 line short to ground

DTC: P0238

- Turbocharger boost sensor P3 line short to power

- Turbocharger boost sensor P3 line open

Common

- Turbocharger boost sensor failure

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

## Chunk 5398: DTC P0237, P0238 (L15B7)

- Title: DTC P0237, P0238 (L15B7)
- Source path: `pages\6591.html`
- Chunk ID: `chunk_2a222993299e`
- Images: `images\GHH402888.jpeg`, `images\GHH402889.jpeg`
- Duplicate sources: `pages\8178.html`, `pages\23249.html`, `pages\21662.html`

### Full Text

````text
# DTC P0237, P0238 (L15B7)

DTC P0237: Turbocharger Boost Sensor Circuit Low Voltage

DTC P0238: Turbocharger Boost Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The turbocharger boost sensor senses turbocharger boost pressure (vacuum) and converts it into electrical signals. The turbocharger boost sensor outputs low signal voltage at high-vacuum (throttle valve closed) and high signal voltage at low-vacuum (throttle valve wide open). If the signal voltage from the turbocharger boost sensor is a set value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0237

The turbocharger boost sensor output voltage [TC BOOST PRESSURE SENSOR] is 0.23 V or less for at least 2 seconds.

DTC: P0238

The turbocharger boost sensor output voltage [TC BOOST PRESSURE SENSOR] is 4.49 V or more for at least 2 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0237

- Turbocharger boost sensor P3 line short to ground

- Turbocharger boost sensor VCC line open

DTC: P0238

- Turbocharger boost sensor P3 line open

- Turbocharger boost sensor SG line open

Common

- Turbocharger boost sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5399: DTC P023D (L15B7/L15BA)

- Title: DTC P023D (L15B7/L15BA)
- Source path: `pages\6592.html`
- Chunk ID: `chunk_7b6f87f74992`
- Images: `images\GHH402890.jpeg`, `images\GHH402891.jpeg`, `images\GHH402892.jpeg`
- Duplicate sources: `pages\8179.html`, `pages\23250.html`, `pages\21663.html`

### Full Text

````text
# DTC P023D (L15B7/L15BA)

DTC P023D: Turbocharger Boost Sensor/Manifold Absolute Pressure (MAP) Sensor Incorrect Correlation

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

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 2, 000 rpm | 36.3 deg. | -

4, 000 rpm | 42.2 deg. | -

[ ]: HDS Parameter

Malfunction Threshold

The difference between the MAP sensor value and the turbocharger boost pressure value is 27 kPa (200 mmHg, 7.9 inHg) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output range/performance problem

- Turbocharger boost sensor output range/performance problem

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

## Chunk 5400: DTC P023D (Si) (2017 2018 2019 2020 2021)

- Title: DTC P023D (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6593.html`
- Chunk ID: `chunk_e5f2b1beca1d`
- Images: `images\GHH402893.jpeg`, `images\GHH402894.jpeg`, `images\GHH402895.jpeg`
- Duplicate sources: `pages\8180.html`, `pages\23251.html`, `pages\21664.html`

### Full Text

````text
# DTC P023D (Si) (2017 2018 2019 2020 2021)

DTC P023D: Turbocharger Boost Sensor/Manifold Absolute Pressure (MAP) Sensor Incorrect Correlation

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

Engine speed [ENGINE SPEED] | 1, 700 rpm | -

Throttle position | 1, 700 rpm | 34.9 deg. | -

2, 500 rpm | 31.4 deg. | -

[ ]: HDS Parameter

Malfunction Threshold

The difference between the MAP sensor value and the turbocharger boost pressure value is 27 kPa (200 mmHg, 7.9 inHg) or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- MAP sensor output range/performance problem

- Turbocharger boost sensor output range/performance problem

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

## Chunk 5401: DTC P026B (K20C1) (2017 2018 2019 2020 2021)

- Title: DTC P026B (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\6594.html`
- Chunk ID: `chunk_f4a7bc54feaa`
- Images: none
- Duplicate sources: `pages\8181.html`, `pages\23252.html`, `pages\21665.html`

### Full Text

````text
# DTC P026B (K20C1) (2017 2018 2019 2020 2021)

DTC P026B: Injector Performance Problem

General Description

This fault code is a general (specified by SAE) DTC that is stored at the time the following DTC codes (P02CC, P02CD, P02CE, P02CF, P02D0, P02D1, P02D2, P02D3) are detected.
````

## Chunk 5402: DTC P027E (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P027E (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\6595.html`
- Chunk ID: `chunk_99ae6d068a19`
- Images: `images\GHH402896.jpeg`, `images\GHH402897.jpeg`, `images\GHH402898.jpeg`
- Duplicate sources: `pages\8182.html`, `pages\23253.html`, `pages\21666.html`

### Full Text

````text
# DTC P027E (L15B7/L15BA/L15BY) (2020 2021)

DTC P027E: Cold Start Air Fuel Ratio Control System Command Lean

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The cold start emission reduction strategy controls air fuel ratio to lean when the engine is started at cold condition to lower the emission while the catalyst is not warmed up enough. If the commanded air fuel ratio is too lean or too rich compared to the target air fuel ratio, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

The ratio of commanded air fuel ratio by target air fuel ratio is 0.87 or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

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

## Chunk 5403: DTC P027F (L15B7/L15BA/L15BY) (2020 2021)

- Title: DTC P027F (L15B7/L15BA/L15BY) (2020 2021)
- Source path: `pages\6596.html`
- Chunk ID: `chunk_e99499a91f51`
- Images: `images\GHH402899.jpeg`, `images\GHH402900.jpeg`, `images\GHH402901.jpeg`
- Duplicate sources: `pages\8183.html`, `pages\23254.html`, `pages\21667.html`

### Full Text

````text
# DTC P027F (L15B7/L15BA/L15BY) (2020 2021)

DTC P027F: Cold Start Air Fuel Ratio Control System Command Rich

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The cold start emission reduction strategy controls air fuel ratio to lean when the engine is started at cold condition to lower the emission while the catalyst is not warmed up enough. If the commanded air fuel ratio is too lean or too rich compared to the target air fuel ratio, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

The ratio of commanded air fuel ratio by target air fuel ratio is 1.29 or more.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM internal circuit failure

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

## Chunk 5404: DTC P0299 (K20C1) (2017 2018 2019)

- Title: DTC P0299 (K20C1) (2017 2018 2019)
- Source path: `pages\6597.html`
- Chunk ID: `chunk_eeda03a2ed9d`
- Images: `images\GHH402902.jpeg`
- Duplicate sources: `pages\8184.html`, `pages\23255.html`, `pages\21668.html`

### Full Text

````text
# DTC P0299 (K20C1) (2017 2018 2019)

DTC P0299: Turbocharger Underboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The boost pressure control monitor is utilized to detect possible errors of the turbocharger system. The turbocharger consists of two elements, a turbine and a compressor, which are connected by a single shaft. The boost control apparatus consists of turbocharger wastegate control actuator that is connected to the turbocharger wastegate control valve passing through the turbine housing. The electronically controlled turbocharger wastegate control valve delivers the resulting boost pressure. In order to provide boost pressure control diagnosis, the actual boost pressure upstream of the throttle valve is monitored against desired boost pressure under certain conditions. There are two types of boost pressure control deviation errors distinguished. If either of the following errors is detected, the PCM detects a malfunction and stores a DTC.

- Overcharging error: Negative boost pressure control deviation. The actual boost pressure exceeds the desired boost pressure value.

- Undercharging error: Positive boost pressure control deviation. The desired boost pressure exceeds the actual boost pressure value.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

The following conditions must be met for at least 2 seconds.

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 3, 200 - 3, 800 rpm | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Difference between commanded pressure upstream throttle valve and minimum pressure after air cleaner | 2 kPa (15.1 mmHg, 0.6 inHg) | -

Difference between measured boost pressure upstream throttle valve and ambient air pressure | 35 kPa (262.6 mmHg, 10.4 inHg) | -

Difference between commanded pressure upstream throttle valve and base boost pressure | 10 kPa (75.1 mmHg, 3 inHg) | -

Vehicle speed [Vehicle Speed] | 2 mph (3 km/h) | -

Exhaust gas mass flow | 250 kg/h (551.2 lbs/h) | -

Other | Throttle valve limp home mode is not active

Wide open throttle

[ ]: HDS Parameter

Malfunction Threshold

The difference between desired pressure upstream throttle valve and measured pressure upstream throttle valve is 20 kPa (150.2 mmHg, 6 inHg) or more for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator stuck

- Leakage in turbocharger system

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at engine speed [Engine Speed] 3, 200 rpm or more with high load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5405: DTC P0299 (K20C1) (2019 2020 2021)

- Title: DTC P0299 (K20C1) (2019 2020 2021)
- Source path: `pages\6598.html`
- Chunk ID: `chunk_6938ac1f653e`
- Images: `images\GHH402903.jpeg`
- Duplicate sources: `pages\8185.html`, `pages\23256.html`, `pages\21669.html`

### Full Text

````text
# DTC P0299 (K20C1) (2019 2020 2021)

DTC P0299: Turbocharger Underboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The boost pressure control monitor is utilized to detect possible errors of the turbocharger system. The turbocharger consists of two elements, a turbine and a compressor, which are connected by a single shaft. The boost control apparatus consists of turbocharger wastegate control actuator that is connected to the turbocharger wastegate control valve passing through the turbine housing. The electronically controlled turbocharger wastegate control valve delivers the resulting boost pressure. In order to provide boost pressure control diagnosis, the actual boost pressure upstream of the throttle valve is monitored against desired boost pressure under certain conditions. There are two types of boost pressure control deviation errors distinguished. If either of the following errors is detected, the PCM detects a malfunction and stores a DTC.

- Overcharging error: Negative boost pressure control deviation. The actual boost pressure exceeds the desired boost pressure value.

- Undercharging error: Positive boost pressure control deviation. The desired boost pressure exceeds the actual boost pressure value.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

The following conditions must be met for at least 2 seconds.

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 3, 200 - 3, 800 rpm | -

Vehicle speed [Vehicle Speed] | 2 mph (3 km/h) | -

[ ]: HDS Parameter

Condition | Minimum | Maximum

Barometric pressure (BARO) sensor [Baro] | 70 kPa (525 mmHg, 20.7 inHg) | -

[ ]: HDS Parameter

Malfunction Threshold

The difference between commanded pressure upstream throttle valve and measured pressure upstream throttle valve is 20 kPa (150 mmHg, 5.9 inHg) or more for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Turbocharger wastegate control actuator stuck

- Leakage in turbocharger system

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

- Drive the vehicle at engine speed [Engine Speed] 3, 200 rpm or more with high load.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5406: DTC P0299 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)

- Title: DTC P0299 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)
- Source path: `pages\6599.html`
- Chunk ID: `chunk_bff31b275c67`
- Images: `images\GHH402904.jpeg`, `images\GHH402905.jpeg`
- Duplicate sources: `pages\8186.html`, `pages\23257.html`, `pages\21670.html`

### Full Text

````text
# DTC P0299 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018)

DTC P0299: Turbocharger Underboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger control system to control boost pressure. When the difference between the target boost pressure and actual boost pressure is at a specified value for a predetermined time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 3, 000 rpm | -

Other | No change of boost pressure upper limit

[ ]: HDS Parameter

Malfunction Threshold

The difference between the target boost pressure and actual boost pressure is 6 kPa (43.6 mmHg, 1.8 inHg) or more and the boost pressure is 53 - 239 kPa (400 - 1, 796 mmHg, 15.7 - 70.7 inHg) or less* for at least 6.0 seconds.

*: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck open failure

- Turbocharger bypass control valve open/close failure

- Turbine damage or seizure

- Exhaust pipe clogged

- Air cleaner element clogged

- Air tube between compressor and intercooler damage/leakage

- Turbocharger boost sensor range/performance problem

- BARO sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] at 3, 000 rpm or more for at least 7 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5407: DTC P0299 (L15B7 (except Si)/L15BY) (2019 2020 2021)

- Title: DTC P0299 (L15B7 (except Si)/L15BY) (2019 2020 2021)
- Source path: `pages\6600.html`
- Chunk ID: `chunk_d45eab365afb`
- Images: `images\GHH402906.jpeg`, `images\GHH402907.jpeg`
- Duplicate sources: `pages\8187.html`, `pages\23258.html`, `pages\21671.html`

### Full Text

````text
# DTC P0299 (L15B7 (except Si)/L15BY) (2019 2020 2021)

DTC P0299: Turbocharger Underboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger control system to control boost pressure. When the difference between the target boost pressure and actual boost pressure is at a specified value for a predetermined time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions (L15B7)

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 156 deg.F (69 deg.C) | -

Engine speed [Engine Speed] | 54 kPa (400 mmHg, 15.8 inHg)* | 4, 500 rpm | -

71 kPa (530 mmHg, 20.9 inHg)* | 3, 700 rpm | -

84 kPa (624 mmHg, 24.6 inHg)* | 3, 000 rpm | -

95 kPa (714 mmHg, 28.1 inHg)* | 2, 350 rpm | -

102 kPa (760 mmHg, 30.0 inHg)* | 2, 350 rpm | -

Other | No change of boost pressure upper limit

*: Barometric pressure [Baro Sensor]

[ ]: HDS Parameter

Enable Conditions (L15BA, L15BY)

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 1, 000 rpm | -

Other | No change of boost pressure upper limit

Malfunction Threshold

The difference between the target boost pressure and actual boost pressure is 6 kPa (43.6 mmHg, 1.8 inHg) or more and the boost pressure is 53 - 239 kPa (400 - 1, 796 mmHg, 15.7 - 70.7 inHg) or less* for at least 6.0 seconds.

*: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck open failure

- Turbocharger bypass control valve open/close failure

- Turbine damage or seizure

- Exhaust pipe clogged

- Air cleaner element clogged

- Air tube between compressor and intercooler damage/leakage

- Turbocharger boost sensor range/performance problem

- BARO sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] at 2, 350 rpm* 1 (3, 000 rpm)* 2 or more for at least 6 seconds* 1 (7 seconds)* 2.

*1: L15B7*2: L15BA, L15BY

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5408: DTC P0299 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0299 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6601.html`
- Chunk ID: `chunk_6afa0a69c8ff`
- Images: `images\GHH402908.jpeg`, `images\GHH402909.jpeg`
- Duplicate sources: `pages\8188.html`, `pages\23259.html`, `pages\21672.html`

### Full Text

````text
# DTC P0299 (Si) (2017 2018 2019 2020 2021)

DTC P0299: Turbocharger Underboost Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) controls the turbocharger control system to control boost pressure. When the difference between the target boost pressure and actual boost pressure is at a specified value for a predetermined time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Engine speed [ENGINE SPEED] | 71 kPa (530 mmHg, 20.9 inHg)* | 3, 900 rpm | -

102 kPa (760 mmHg, 30.0 inHg)* | 2, 500 rpm | -

Other | No change of boost pressure upper limit

*: Barometric pressure [BARO SENSOR]

[ ]: HDS Parameter

Malfunction Threshold

The difference between the target boost pressure and actual boost pressure is 54 - 240 kPa (400 - 1, 796 mmHg, 15.8 - 70.8 inHg) or more** for at least 6.0 seconds.

**: Varies with driving conditions.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes

- Turbocharger wastegate control valve stuck open failure

- Turbocharger bypass control valve open/close failure

- Turbine damage or seizure

- Exhaust pipe clogged

- Air cleaner element clogged

- Air tube between compressor and charge air cooler damage/leakage

- Turbocharger boost sensor range/performance problem

- BARO sensor range/performance problem

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Accelerate the vehicle at an engine speed [ENGINE SPEED] at 2, 500 rpm or more with wide open throttle for at least 6 seconds.

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

## Chunk 5409: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2017 2018 2019)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2017 2018 2019)
- Source path: `pages\6602.html`
- Chunk ID: `chunk_07a7650444a9`
- Images: `images\GHH402910.jpeg`
- Duplicate sources: `pages\8189.html`, `pages\23260.html`, `pages\21673.html`

### Full Text

````text
# DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2017 2018 2019)

DTC P02CC: No. 1 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02CE: No. 2 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D0: No. 3 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D2: No. 4 Cylinder Injector Offset Learning Exceeds Minimum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module monitors the controlled valve operation (CVO) of each injector. The CVO corrects the injection time of every injector to get a correct fuel quantity. After base adaption is finished in every injection the current injection time variation will be checked against a diagnosis threshold. If the result exceeds a threshold, error counter is incremented. If the error counter exceeds a specified count, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The error counter exceeds 100 counts.*

*: The error count is incremented to the counter if the current injection time variation is less than -200 microseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Injector failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle for a while with certain loads.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5410: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)
- Source path: `pages\6603.html`
- Chunk ID: `chunk_138fea9e164b`
- Images: `images\GHH402911.jpeg`
- Duplicate sources: `pages\8190.html`, `pages\23261.html`, `pages\21674.html`

### Full Text

````text
# DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)

DTC P02CC: No. 1 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02CE: No. 2 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D0: No. 3 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D2: No. 4 Cylinder Injector Offset Learning Exceeds Minimum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

Controlled valve operation (CVO) is a function of the powertrain control module (PCM) to determine the actual open time of injection valves. The function utilizes different signal processing algorithms to calculate rising delay and closing delay out of executed measurements. The algorithms are divided in two parts. The first part is the base adaptation and requires special injector energizing time for the measurement. The second part based on learning during normal engine operation. The needle opening duration is controlled and energizing time (feed-forward control) is adapted to the injector individually. The control variable is 'topen' and the corresponding correcting variable is the energizing time 'ti' as shown in the figure. The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, corresponding error reactions will be activated such as triggering a new base adaptation or locking the defective injector for CVO. The diagnostic utilizes different monitors in order to detect the minimum CVO errors.

- Monitor 1: Rationality check of opening delay time 'tantot' The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 3: Rationality check of plateau correction height The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 4: Rationality check of the total calculated injection time correction value The calculated injection time correction is checked by the diagnostic function depending on the current working point. 4.1: In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC. 4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

4.1: In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 6: Detection of "full-lift" closing time This diagnostic monitors if the "full-lift" closing time can be detected or not.
````

## Chunk 5411: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)
- Source path: `pages\6603.html`
- Chunk ID: `chunk_ec3a26c282ca`
- Images: `images\GHH402911.jpeg`
- Duplicate sources: `pages\8190.html`, `pages\23261.html`, `pages\21674.html`

### Full Text

````text
pe of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 6: Detection of "full-lift" closing time This diagnostic monitors if the "full-lift" closing time can be detected or not. If the "full-lift' closing time 'tab' cannot be detected for number of times, the PCM detects a malfunction and stores a DTC.

This diagnostic monitors if the "full-lift" closing time can be detected or not. If the "full-lift' closing time 'tab' cannot be detected for number of times, the PCM detects a malfunction and stores a DTC.

- Monitor 7: Rationality check of the ballistic correction at the adjustment-point As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Common

Condition

State of the engine | Running

Monitor 1, 3, and 6

Condition

Other | During CVO basic adaptation

Monitor 4.1

Condition

Other | Not during CVO basic adaptation

Pulse type of current injection is not in "transition"

"Ballistic" injection active

Monitor 4.2

Condition

Other | Not during CVO basic adaptation

Pulse type of current injection is not in "transition"

"Full-lift" injection active

Monitor 7

Condition

Other | During CVO basic adaptation

Pulse type of current injection is "ballistic"

Malfunction Threshold

- Monitor 1 Either of the conditions is met:

Either of the conditions is met:

- - Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds. - The system cannot detect 'tantot' value.

- - Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds.

Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds.

- - The system cannot detect 'tantot' value.

The system cannot detect 'tantot' value.

- Monitor 3 All conditions are met:

All conditions are met:

- - The current plateau value is less than -150 μseconds. - The total 'topen' adaptation value is out of minimum tolerance range at least 2 counts.

- - The current plateau value is less than -150 μseconds.

The current plateau value is less than -150 μseconds.

- - The total 'topen' adaptation value is out of minimum tolerance range at least 2 counts.

The total 'topen' adaptation value is out of minimum tolerance range at least 2 counts.

- Monitor 4.1 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "ballistic". - The total calculated injection time correction is less than -50 μseconds. - The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- - The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- - The total calculated injection time correction is less than -50 μseconds.

The total calculated injection time correction is less than -50 μseconds.

- - The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- Monitor 4.2 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "full-lift".
````

## Chunk 5412: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2019)
- Source path: `pages\6603.html`
- Chunk ID: `chunk_51b601f80c93`
- Images: `images\GHH402911.jpeg`
- Duplicate sources: `pages\8190.html`, `pages\23261.html`, `pages\21674.html`

### Full Text

````text
l calculated injection time correction is less than -50 μseconds. - The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- - The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- - The total calculated injection time correction is less than -50 μseconds.

The total calculated injection time correction is less than -50 μseconds.

- - The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

The total "ballistic" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- Monitor 4.2 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "full-lift". - The total calculated injection time correction is less than -200 μseconds. - The total "full-lift" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- - The pulse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- - The total calculated injection time correction is less than -200 μseconds.

The total calculated injection time correction is less than -200 μseconds.

- - The total "full-lift" calculated injection time correction is out of minimum tolerance range at least 100 counts.

The total "full-lift" calculated injection time correction is out of minimum tolerance range at least 100 counts.

- Monitor 5 All conditions are met:

All conditions are met:

- - The measured "full-lift" closing time is more than 580 μseconds. - The current "full-lift" closing time 'tab' is out of minimum tolerance range at least 100 counts.

- - The measured "full-lift" closing time is more than 580 μseconds.

The measured "full-lift" closing time is more than 580 μseconds.

- - The current "full-lift" closing time 'tab' is out of minimum tolerance range at least 100 counts.

The current "full-lift" closing time 'tab' is out of minimum tolerance range at least 100 counts.

- Monitor 6 All conditions are met:

All conditions are met:

- - There is a faulty in CVO controller. - The "full-lift" closing time 'tab' not been found at least 100 counts.

- - There is a faulty in CVO controller.

There is a faulty in CVO controller.

- - The "full-lift" closing time 'tab' not been found at least 100 counts.

The "full-lift" closing time 'tab' not been found at least 100 counts.

- Monitor 7 The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Improper fuel injection amount control operation

- Poor connection of injector

- Injector failure

- Improper cylinder compression

- Cylinder injection pipe collapsed

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5413: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)
- Source path: `pages\6604.html`
- Chunk ID: `chunk_4b9728c7b7ec`
- Images: `images\GHH402912.jpeg`
- Duplicate sources: `pages\8191.html`, `pages\23262.html`, `pages\21675.html`

### Full Text

````text
# DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)

DTC P02CC: No. 1 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02CE: No. 2 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D0: No. 3 Cylinder Injector Offset Learning Exceeds Minimum Limit

DTC P02D2: No. 4 Cylinder Injector Offset Learning Exceeds Minimum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

Controlled valve operation (CVO) is a function of the powertrain control module (PCM) to determine the actual open time of injection valves. The function utilizes different signal processing algorithms to calculate rising delay and closing delay out of executed measurements. The algorithms are divided in two parts. The first part is the base adaptation and requires special injector energizing time for the measurement. The second part based on learning during normal engine operation. The needle opening duration is controlled and energizing time (feed-forward control) is adapted to the injector individually. The control variable is 'topen' and the corresponding correcting variable is the energizing time 'ti' as shown in the figure. The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, corresponding error reactions will be activated such as triggering a new base adaptation or locking the defective injector for CVO. The diagnostic utilizes different monitors in order to detect the minimum CVO errors.

- Monitor 1: Rationality check of opening delay time 'tantot' The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 3: Rationality check of plateau correction height The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 4: Rationality check of the total calculated injection time correction value The calculated injection time correction is checked by the diagnostic function depending on the current working point. In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC. In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 6: Detection of "full-lift" closing time This diagnostic monitors if the "full-lift" closing time can be detected or not.
````

## Chunk 5414: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)
- Source path: `pages\6604.html`
- Chunk ID: `chunk_5a5ec22d9322`
- Images: `images\GHH402912.jpeg`
- Duplicate sources: `pages\8191.html`, `pages\23262.html`, `pages\21675.html`

### Full Text

````text
pe of the current injection is "full-lift" and the total calculated injection time correction is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is greater than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 6: Detection of "full-lift" closing time This diagnostic monitors if the "full-lift" closing time can be detected or not. If the "full-lift' closing time 'tab' cannot be detected for number of times, the PCM detects a malfunction and stores a DTC.

This diagnostic monitors if the "full-lift" closing time can be detected or not. If the "full-lift' closing time 'tab' cannot be detected for number of times, the PCM detects a malfunction and stores a DTC.

- Monitor 7: Rationality check of the ballistic correction at the adjustment-point As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Common

Condition

State of the engine | Running

Monitor 1 and 3

Condition

Other | Base adaptation is active

Monitor 4

Condition

Other | Base adaptation is finished

Monitor 7

Condition

Other | Base adaptation is active

The controller is stable during base adaption

Pulse type of current injection is "ballistic"

Malfunction Threshold

- Monitor 1 Either of the conditions is met at least 1 time:

Either of the conditions is met at least 1 time:

- - Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds. - The system cannot detect 'tantot' value.

- - Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds.

Difference between current opening time delay 'tantot' and its default value is less than -150 μseconds.

- - The system cannot detect 'tantot' value.

The system cannot detect 'tantot' value.

- Monitor 3 The current plateau value is less than -150 μseconds at least 2 times.

The current plateau value is less than -150 μseconds at least 2 times.

- Monitor 4 A and B, or C and D is met at least 100 times:

A and B, or C and D is met at least 100 times:

- A. The pulse type of current injection is "ballistic". B. The total calculated injection time correction is less than -50 μseconds. C. The pulse type of current injection is "full-lift". D. The total calculated injection time correction is less than -200 μseconds.

- A. The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- B. The total calculated injection time correction is less than -50 μseconds.

The total calculated injection time correction is less than -50 μseconds.

- C. The pulse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- D. The total calculated injection time correction is less than -200 μseconds.

The total calculated injection time correction is less than -200 μseconds.

- Monitor 5 The measured "full-lift" closing time is more than 580 μseconds at least 100 times.

The measured "full-lift" closing time is more than 580 μseconds at least 100 times.

- Monitor 6 There is a faulty in CVO controller at least 100 times.

There is a faulty in CVO controller at least 100 times.

- Monitor 7 The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.
````

## Chunk 5415: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)

- Title: DTC P02CC, P02CE, P02D0, P02D2 (K20C1) (2020 2021)
- Source path: `pages\6604.html`
- Chunk ID: `chunk_280f42561ae9`
- Images: `images\GHH402912.jpeg`
- Duplicate sources: `pages\8191.html`, `pages\23262.html`, `pages\21675.html`

### Full Text

````text
lse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- D. The total calculated injection time correction is less than -200 μseconds.

The total calculated injection time correction is less than -200 μseconds.

- Monitor 5 The measured "full-lift" closing time is more than 580 μseconds at least 100 times.

The measured "full-lift" closing time is more than 580 μseconds at least 100 times.

- Monitor 6 There is a faulty in CVO controller at least 100 times.

There is a faulty in CVO controller at least 100 times.

- Monitor 7 The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction is stable during the base adaptation for at least -50 μseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Improper fuel injection amount control operation

- Poor connection of injector

- Injector failure

- Improper cylinder compression

- Cylinder injection pipe collapsed

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5416: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2017 2018 2019)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2017 2018 2019)
- Source path: `pages\6605.html`
- Chunk ID: `chunk_14a87f3012b8`
- Images: `images\GHH402913.jpeg`
- Duplicate sources: `pages\8192.html`, `pages\23263.html`, `pages\21676.html`

### Full Text

````text
# DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2017 2018 2019)

DTC P02CD: No. 1 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02CF: No. 2 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D1: No. 3 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D3: No. 4 Cylinder Injector Offset Learning Exceeds Maximum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module monitors the controlled valve operation (CVO) of each injector. The CVO corrects the injection time of every injector to get a correct fuel quantity. After base adaption is finished in every injection the current injection time variation will be checked against a diagnosis threshold. If the result exceeds a threshold, error counter is incremented. If the error counter exceeds a specified count, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The error counter exceeds 100 counts.*

*: The error count is incremented to the counter if the current injection time variation is more than 200 microseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Injector failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle for a while with certain loads.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5417: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)
- Source path: `pages\6606.html`
- Chunk ID: `chunk_5533f799de43`
- Images: `images\GHH402914.jpeg`
- Duplicate sources: `pages\8193.html`, `pages\23264.html`, `pages\21677.html`

### Full Text

````text
# DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)

DTC P02CD: No. 1 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02CF: No. 2 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D1: No. 3 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D3: No. 4 Cylinder Injector Offset Learning Exceeds Maximum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

Controlled valve operation (CVO) is a function of the powertrain control module (PCM) to determine the actual open time of injection valves. The function utilizes different signal processing algorithms to calculate rising delay and closing delay out of executed measurements. The algorithms are divided in two parts. The first part is the base adaptation and requires special injector energizing time for the measurement. The second part based on learning during normal engine operation. The needle opening duration is controlled and energizing time (feed-forward control) is adapted to the injector individually. The control variable is 'topen' and the corresponding correcting variable is the energizing time 'ti' as shown in the figure. The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, corresponding error reactions will be activated such as triggering a new base adaptation or locking the defective injector for CVO. The diagnostic utilizes different monitors in order to detect the minimum CVO errors.

- Monitor 1: Rationality check of opening delay time 'tantot' The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 2: CVO controller stability check CVO controller is checked for stability during CVO basic adaptation. If the opening time of the last iteration step comparing to the previous iteration step is more than a threshold within a monitoring window, the PCM detects a malfunction and stores a DTC.

CVO controller is checked for stability during CVO basic adaptation. If the opening time of the last iteration step comparing to the previous iteration step is more than a threshold within a monitoring window, the PCM detects a malfunction and stores a DTC.

- Monitor 3: Rationality check of plateau correction height The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 4: Rationality check of the total calculated injection time correction value The calculated injection time correction is checked by the diagnostic function depending on the current working point. 4.1: In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC. 4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

4.1: In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.
````

## Chunk 5418: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)
- Source path: `pages\6606.html`
- Chunk ID: `chunk_0049045fd107`
- Images: `images\GHH402914.jpeg`
- Duplicate sources: `pages\8193.html`, `pages\23264.html`, `pages\21677.html`

### Full Text

````text
brated threshold, the PCM detects a malfunction and stores a DTC. 4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

4.1: In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

4.2: In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 7: Rationality check of the ballistic correction at the adjustment-point As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Common

Condition

State of the engine | Running

Monitor 1, 2, and 3

Condition

Other | During CVO basic adaptation

Monitor 4.1

Condition

Other | Not during CVO basic adaptation

Pulse type of current injection is not in "transition"

"Ballistic" injection active

Monitor 4.2

Condition

Other | Not during CVO basic adaptation

Pulse type of current injection is not in "transition"

"Full-lift" injection active

Monitor 7

Condition

Other | During CVO basic adaptation

Other | Pulse type of current injection is "ballistic"

Malfunction Threshold

- Monitor 1 Difference between current opening time delay 'tantot' and its default value is more than 150 μseconds.

Difference between current opening time delay 'tantot' and its default value is more than 150 μseconds.

- Monitor 2 Difference between calculated and desired opening time of the last measurement is more than 30 μseconds at least 7 counts.

Difference between calculated and desired opening time of the last measurement is more than 30 μseconds at least 7 counts.

- Monitor 3 All conditions are met:

All conditions are met:

- - The current plateau value is more than 90 μseconds. - The total 'topen' adaptation value is out of maximum tolerance range at least 2 counts.

- - The current plateau value is more than 90 μseconds.

The current plateau value is more than 90 μseconds.

- - The total 'topen' adaptation value is out of maximum tolerance range at least 2 counts.

The total 'topen' adaptation value is out of maximum tolerance range at least 2 counts.

- Monitor 4.1 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "ballistic". - The total calculated injection time correction is more than 80 μseconds. - The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.

- - The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- - The total calculated injection time correction is more than 80 μseconds.

The total calculated injection time correction is more than 80 μseconds.

- - The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.

The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.
````

## Chunk 5419: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2019)
- Source path: `pages\6606.html`
- Chunk ID: `chunk_1c93d53696ae`
- Images: `images\GHH402914.jpeg`
- Duplicate sources: `pages\8193.html`, `pages\23264.html`, `pages\21677.html`

### Full Text

````text
or 4.1 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "ballistic". - The total calculated injection time correction is more than 80 μseconds. - The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.

- - The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- - The total calculated injection time correction is more than 80 μseconds.

The total calculated injection time correction is more than 80 μseconds.

- - The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.

The total "ballistic" calculated injection time correction is out of maximum tolerance range at least 100 counts.

- Monitor 4.2 All conditions are met:

All conditions are met:

- - The pulse type of current injection is "full-lift". - The total calculated injection time correction is more than 200 μseconds. - The total "full-lift" calculated injection time correction is out of maximum tolerance range at least 100 counts.

- - The pulse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- - The total calculated injection time correction is more than 200 μseconds.

The total calculated injection time correction is more than 200 μseconds.

- - The total "full-lift" calculated injection time correction is out of maximum tolerance range at least 100 counts.

The total "full-lift" calculated injection time correction is out of maximum tolerance range at least 100 counts.

- Monitor 5 All conditions are met:

All conditions are met:

- - The measured "full-lift" closing time is less than 200 μseconds. - The current "full-lift" closing time 'tab' is out of maximum tolerance range at least 100 counts.

- - The measured "full-lift" closing time is less than 200 μseconds.

The measured "full-lift" closing time is less than 200 μseconds.

- - The current "full-lift" closing time 'tab' is out of maximum tolerance range at least 100 counts.

The current "full-lift" closing time 'tab' is out of maximum tolerance range at least 100 counts.

- Monitor 7 The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Improper fuel injection amount control operation

- Poor connection of injector

- Injector failure

- Improper cylinder compression

- Cylinder injection pipe collapsed

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5420: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)
- Source path: `pages\6607.html`
- Chunk ID: `chunk_ae1e27a6790d`
- Images: `images\GHH402915.jpeg`
- Duplicate sources: `pages\8194.html`, `pages\23265.html`, `pages\21678.html`

### Full Text

````text
# DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)

DTC P02CD: No. 1 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02CF: No. 2 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D1: No. 3 Cylinder Injector Offset Learning Exceeds Maximum Limit

DTC P02D3: No. 4 Cylinder Injector Offset Learning Exceeds Maximum Limit

General Description

Courtesy of HONDA, U.S.A., INC.

Controlled valve operation (CVO) is a function of the powertrain control module (PCM) to determine the actual open time of injection valves. The function utilizes different signal processing algorithms to calculate rising delay and closing delay out of executed measurements. The algorithms are divided in two parts. The first part is the base adaptation and requires special injector energizing time for the measurement. The second part based on learning during normal engine operation. The needle opening duration is controlled and energizing time (feed-forward control) is adapted to the injector individually. The control variable is 'topen' and the corresponding correcting variable is the energizing time 'ti' as shown in the figure. The monitoring function verifies the calculated adjustment values of the CVO function. In case of an error, corresponding error reactions will be activated such as triggering a new base adaptation or locking the defective injector for CVO. The diagnostic utilizes different monitors in order to detect the minimum CVO errors.

- Monitor 1: Rationality check of opening delay time 'tantot' The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The 'tantot' value is continuously monitored against a default value. If the difference between current opening time delay (tantot) and its default value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 2: CVO controller stability check CVO controller is checked for stability during CVO basic adaptation. If the opening time of the last iteration step comparing to the previous iteration step is more than a threshold within a monitoring window, the PCM detects a malfunction and stores a DTC.

CVO controller is checked for stability during CVO basic adaptation. If the opening time of the last iteration step comparing to the previous iteration step is more than a threshold within a monitoring window, the PCM detects a malfunction and stores a DTC.

- Monitor 3: Rationality check of plateau correction height The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The ballistic slope correction includes a slope correction and a plateau correction parts. The measured height of the plateau correction is continuously monitored against an expected value. If the current plateau value is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 4: Rationality check of the total calculated injection time correction value The calculated injection time correction is checked by the diagnostic function depending on the current working point. In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC. In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.
````

## Chunk 5421: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)
- Source path: `pages\6607.html`
- Chunk ID: `chunk_abdd30245dcf`
- Images: `images\GHH402915.jpeg`
- Duplicate sources: `pages\8194.html`, `pages\23265.html`, `pages\21678.html`

### Full Text

````text
ore than a calibrated threshold, the PCM detects a malfunction and stores a DTC. In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

The calculated injection time correction is checked by the diagnostic function depending on the current working point.

In case the pulse type of the current injection is "ballistic" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

In case the pulse type of the current injection is "full-lift" and the total calculated injection time correction is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 5: Rationality check of the "full-lift" closing time This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

This diagnostic compares the "full-lift" closing time with an expected value. If the current "full-lift" closing time 'tab' is less than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

- Monitor 7: Rationality check of the ballistic correction at the adjustment-point As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

As soon as the controller is stable at the ballistic adjustment-point, the current value of ballistic correction is transmitted to the diagnostic function. If the integrated value during base adaptation is more than a calibrated threshold, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Common

Condition

State of the engine | Running

Monitor 1 and 3

Condition

Other | Base adaptation is active

Monitor 2

Condition

Other | Base adaptation is active

The controller is not stable

Monitor 4

Condition

Other | Base adaptation is finished

Monitor 7

Condition

Other | Base adaptation is active

The controller is stable during base adaption

Pulse type of current injection is "ballistic"

Malfunction Threshold

- Monitor 1 Difference between current opening time delay 'tantot' and its default value is more than 150 μseconds at least 1 time.

Difference between current opening time delay 'tantot' and its default value is more than 150 μseconds at least 1 time.

- Monitor 2 The controller cannot stabilize within 7 times of allowed measurements.

The controller cannot stabilize within 7 times of allowed measurements.

- Monitor 3 The current plateau value is more than 90 μseconds at least 2 times.

The current plateau value is more than 90 μseconds at least 2 times.

- Monitor 4 A and B, or C and D is met at least 100 times:

A and B, or C and D is met at least 100 times:

- A. The pulse type of current injection is "ballistic". B. The total calculated injection time correction is more than 80 μseconds. C. The pulse type of current injection is "full-lift". D. The total calculated injection time correction is more than 200 μseconds.

- A. The pulse type of current injection is "ballistic".

The pulse type of current injection is "ballistic".

- B. The total calculated injection time correction is more than 80 μseconds.

The total calculated injection time correction is more than 80 μseconds.

- C. The pulse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- D. The total calculated injection time correction is more than 200 μseconds.

The total calculated injection time correction is more than 200 μseconds.

- Monitor 5 The measured "full-lift" closing time is less than 200 μseconds at least 100 times.

The measured "full-lift" closing time is less than 200 μseconds at least 100 times.

- Monitor 7 The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

Possible Cause
````

## Chunk 5422: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)

- Title: DTC P02CD, P02CF, P02D1, P02D3 (K20C1) (2020 2021)
- Source path: `pages\6607.html`
- Chunk ID: `chunk_e7e47dbeb183`
- Images: `images\GHH402915.jpeg`
- Duplicate sources: `pages\8194.html`, `pages\23265.html`, `pages\21678.html`

### Full Text

````text
lated injection time correction is more than 80 μseconds.

- C. The pulse type of current injection is "full-lift".

The pulse type of current injection is "full-lift".

- D. The total calculated injection time correction is more than 200 μseconds.

The total calculated injection time correction is more than 200 μseconds.

- Monitor 5 The measured "full-lift" closing time is less than 200 μseconds at least 100 times.

The measured "full-lift" closing time is less than 200 μseconds at least 100 times.

- Monitor 7 The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

The total calculated injection time correction after the controller is stable during the base adaptation for at least -50 μseconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Improper fuel injection amount control operation

- Poor connection of injector

- Injector failure

- Improper cylinder compression

- Cylinder injection pipe collapsed

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5423: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2017 2018 2019)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2017 2018 2019)
- Source path: `pages\6608.html`
- Chunk ID: `chunk_42dbf56f2b05`
- Images: none
- Duplicate sources: `pages\8195.html`, `pages\23266.html`, `pages\21679.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2017 2018 2019)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

The basic operating principle of the engine misfire detection monitor is based on the calculated angular acceleration of the engine crankshaft during each individual combustion event. In case of a lack of combustion, or insufficient combustion in any cylinder, the CKP pulse plate which is attached to the crankshaft requires a longer time to pass the crankshaft position (CKP) sensor. The associated acceleration value will overshoot a calibrated threshold (indicating a large deceleration) which will then lead to a misfire event being detected by the system. There are two types of misfire detection:

- Catalyst damaging misfire Misfire events are counted within intervals of 200 crankshaft revolutions. Dependant on the current engine speed and load, a weighted fault counter will increment with each new misfire event. Catalyst damaging misfire events are evaluated bank specifically. A fault entry will occur anytime the weighted misfire counters exceed a calibrated threshold for a given engine bank. With this condition, the powertrain control module (PCM) stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.

Misfire events are counted within intervals of 200 crankshaft revolutions. Dependant on the current engine speed and load, a weighted fault counter will increment with each new misfire event. Catalyst damaging misfire events are evaluated bank specifically. A fault entry will occur anytime the weighted misfire counters exceed a calibrated threshold for a given engine bank. With this condition, the powertrain control module (PCM) stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.

- Emission relevant misfire Misfire events are counted during 1, 000 crankshaft revolution intervals after engine start. At the end of each 1, 000 crankshaft revolution period, the total number of detected misfire events is compared to a fault threshold. If the number of detected events exceeds a threshold, a fault counter will be incremented. After exceeding the emissions relevant fault threshold for the fourth occurrence, the PCM stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.

Misfire events are counted during 1, 000 crankshaft revolution intervals after engine start. At the end of each 1, 000 crankshaft revolution period, the total number of detected misfire events is compared to a fault threshold. If the number of detected events exceeds a threshold, a fault counter will be incremented. After exceeding the emissions relevant fault threshold for the fourth occurrence, the PCM stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | 15 seconds

Type 2 | 8 minutes

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 450 rpm | 7, 000 rpm

Engine torque | 3.52 to 12.11 % | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

[ ]: HDS Parameter

Malfunction Threshold

- Catalyst damaging misfire Misfire occurs 5, 000 times. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

Misfire occurs 5, 000 times. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

- Emission relevant misfire If the misfire occurs 94 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

If the misfire occurs 94 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

Possible Cause
````

## Chunk 5424: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2017 2018 2019)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2017 2018 2019)
- Source path: `pages\6608.html`
- Chunk ID: `chunk_25c487458725`
- Images: none
- Duplicate sources: `pages\8195.html`, `pages\23266.html`, `pages\21679.html`

### Full Text

````text
es. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

Misfire occurs 5, 000 times. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

- Emission relevant misfire If the misfire occurs 94 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

If the misfire occurs 94 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed for at least 2 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Catalyst damaging misfire:

- If a catalyst damaging misfire occurs, the MIL will blink in each interval that catalyst damaging misfire is detected. The MIL will cease from blinking after an interval passes where no catalyst damaging misfire is detected. After this point, the MIL will either be extinguished or will remain illuminated. This behavior depends on whether catalyst damaging misfire has been detected in one drive cycle (one occurrence) or in two drive cycles (two occurrences).

Emission relevant misfire:

- If an emission relevant misfire occurs during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5425: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2019 2020 2021)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2019 2020 2021)
- Source path: `pages\6609.html`
- Chunk ID: `chunk_abd8868502e4`
- Images: none
- Duplicate sources: `pages\8196.html`, `pages\23267.html`, `pages\21680.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2019 2020 2021)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

The basic operating principle of the engine misfire detection monitor is based on the calculated angular acceleration of the engine crankshaft during each individual combustion event. In case of a lack of combustion, or insufficient combustion in any cylinder, the CKP pulse plate which is attached to the crankshaft requires a longer time to pass the crankshaft position (CKP) sensor. The associated acceleration value will overshoot a calibrated threshold (indicating a large deceleration) which will then lead to a misfire event being detected by the system. There are two types of misfire detection:

- Catalyst damaging misfire Misfire events are counted within intervals of 200 crankshaft revolutions. Dependant on the current engine speed and load, a weighted fault counter will increment with each new misfire event. Catalyst damaging misfire events are evaluated bank specifically. A fault entry will occur anytime the weighted misfire counters exceed a calibrated threshold for a given engine bank. With this condition, the powertrain control module (PCM) stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.

Misfire events are counted within intervals of 200 crankshaft revolutions. Dependant on the current engine speed and load, a weighted fault counter will increment with each new misfire event. Catalyst damaging misfire events are evaluated bank specifically. A fault entry will occur anytime the weighted misfire counters exceed a calibrated threshold for a given engine bank. With this condition, the powertrain control module (PCM) stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.

- Emission relevant misfire Misfire events are counted during 1, 000 crankshaft revolution intervals after engine start. At the end of each 1, 000 crankshaft revolution period, the total number of detected misfire events is compared to a fault threshold. If the number of detected events exceeds a threshold, a fault counter will be incremented. After exceeding the emissions relevant fault threshold for the fourth occurrence, the PCM stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.

Misfire events are counted during 1, 000 crankshaft revolution intervals after engine start. At the end of each 1, 000 crankshaft revolution period, the total number of detected misfire events is compared to a fault threshold. If the number of detected events exceeds a threshold, a fault counter will be incremented. After exceeding the emissions relevant fault threshold for the fourth occurrence, the PCM stores a DTC. A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | -30 deg.F (-22 deg.C) | -

Engine speed [Engine Speed] | 450 rpm | 7, 000 rpm

Engine torque | 3.13 to 12.89 % | -

Fuel feedback | Other than during fuel cut-off operation

Other | ABS/VSA not active

Test-drive on a flat road to avoid misdetection

[ ]: HDS Parameter

Malfunction Threshold

- Catalyst damaging misfire Misfire rate is more than 5 - 19.84 %*. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.) *: Depending on engine speed and load

Misfire rate is more than 5 - 19.84 %*. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

*: Depending on engine speed and load

- Emission relevant misfire If the misfire occurs 100 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

If the misfire occurs 100 times during 1, 000 crankshaft revolutions, a fault counter is incremented.
````

## Chunk 5426: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2019 2020 2021)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C1) (2019 2020 2021)
- Source path: `pages\6609.html`
- Chunk ID: `chunk_c108f56b338a`
- Images: none
- Duplicate sources: `pages\8196.html`, `pages\23267.html`, `pages\21680.html`

### Full Text

````text
eshold

- Catalyst damaging misfire Misfire rate is more than 5 - 19.84 %*. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.) *: Depending on engine speed and load

Misfire rate is more than 5 - 19.84 %*. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 25 % of the total misfire.)

*: Depending on engine speed and load

- Emission relevant misfire If the misfire occurs 100 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

If the misfire occurs 100 times during 1, 000 crankshaft revolutions, a fault counter is incremented. The condition occurs 4 events. (A cylinder specific DTC will be recorded for each cylinder that contributes at least 10 % of the total misfire.)

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at constant vehicle speed for at least 2 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

Catalyst damaging misfire:

- If a catalyst damaging misfire occurs, the MIL will blink in each interval that catalyst damaging misfire is detected. The MIL will cease from blinking after an interval passes where no catalyst damaging misfire is detected. After this point, the MIL will either be extinguished or will remain illuminated. This behavior depends on whether catalyst damaging misfire has been detected in one drive cycle (one occurrence) or in two drive cycles (two occurrences).

Emission relevant misfire:

- If an emission relevant misfire occurs during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5427: DTC P0300, P0301, P0302, P0303, P0304 (K20C2)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C2)
- Source path: `pages\6610.html`
- Chunk ID: `chunk_aa553e6bf956`
- Images: `images\GHH402916.jpeg`, `images\GHH402917.jpeg`
- Duplicate sources: `pages\8197.html`, `pages\23268.html`, `pages\21681.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (K20C2)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED]* 1, * 3 | 500 rpm | 6, 700 rpm

Engine speed [ENGINE SPEED]* 1, * 4 | 600 rpm | 6, 700 rpm

Engine speed [ENGINE SPEED]* 2, * 3 | 500 rpm | 4, 500 rpm

Engine speed [ENGINE SPEED]* 2, * 4 | 600 rpm | 4, 500 rpm

MAP value [MAP SENSOR]*, * 3 | 500 rpm** | 24 kPa (176 mmHg, 7.0 inHg) | -

2, 250 rpm** | 22 kPa (163 mmHg, 6.5 inHg) | -

500 rpm*** | 37 kPa (277 mmHg, 11.0 inHg) | -

2, 750 rpm*** | 29 kPa (212 mmHg, 8.4 inHg) | -

MAP value [MAP SENSOR]*, * 4 | 500 rpm** | 24 kPa (176 mmHg, 7.0 inHg) | -

2, 250 rpm** | 22 kPa (163 mmHg, 6.5 inHg) | -

500 rpm*** | 36 kPa (269 mmHg, 10.6 inHg) | -

2, 750 rpm*** | 28 kPa (208 mmHg, 8.2 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: USA and Canada models

*2: Mexico models

*3: CVT model

*4: M/T model

*: Varies with driving conditions.

**: Rocker arm oil control solenoid: OFF

****: Rocker arm oil control solenoid: ON[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 17 - 89 times****

Misfire Type 2 (Light) | Per 1, 000 revolutions | 38 times* 5 (28 times)* 6 (84 times)* 2

*5: KA, KC models

*6: KL models

****: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (24 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:
````

## Chunk 5428: DTC P0300, P0301, P0302, P0303, P0304 (K20C2)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (K20C2)
- Source path: `pages\6610.html`
- Chunk ID: `chunk_07e42fbf9cd5`
- Images: `images\GHH402916.jpeg`, `images\GHH402917.jpeg`
- Duplicate sources: `pages\8197.html`, `pages\23268.html`, `pages\21681.html`

### Full Text

````text
ating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (24 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM*****. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM*****.

***** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5429: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA) (2016 2017)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA) (2016 2017)
- Source path: `pages\6611.html`
- Chunk ID: `chunk_cebc8d2fa3f7`
- Images: `images\GHH402918.jpeg`, `images\GHH402919.jpeg`
- Duplicate sources: `pages\8198.html`, `pages\23269.html`, `pages\21682.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA) (2016 2017)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 480 rpm | 6, 500 rpm

MAP value [MAP SENSOR]*, * 1 | 500 rpm | 28 kPa (205 mmHg, 8.1 inHg) | -

2, 500 rpm | 24 kPa (175 mmHg, 6.9 inHg) | -

MAP value [MAP SENSOR]*, * 2 | 700 rpm** | 21 kPa (156 mmHg, 6.2 inHg) | -

2, 500 rpm** | 23 kPa (167 mmHg, 6.6 inHg) | -

700 rpm*** | 38 kPa (280 mmHg, 11.1 inHg) | -

2, 650 rpm*** | 24 kPa (176 mmHg, 7.0 inHg) | -

MAP value [MAP SENSOR]*, * 3 | 500 rpm | 22 kPa (163 mmHg, 6.5 inHg) | -

2, 250 rpm | 22 kPa (159 mmHg, 6.3 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: CVT

*2: L15B7 M/T

*3: L15BA M/T

*: Varies with driving conditions.

**: Rocker arm oil control solenoid: OFF

***: Rocker arm oil control solenoid: ON[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 17 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts.
````

## Chunk 5430: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA) (2016 2017)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA) (2016 2017)
- Source path: `pages\6611.html`
- Chunk ID: `chunk_4cb437711c2f`
- Images: `images\GHH402918.jpeg`, `images\GHH402919.jpeg`
- Duplicate sources: `pages\8198.html`, `pages\23269.html`, `pages\21682.html`

### Full Text

````text
h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM***.

*** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5431: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2018)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2018)
- Source path: `pages\6612.html`
- Chunk ID: `chunk_d0f9bb4a5055`
- Images: `images\GHH402920.jpeg`, `images\GHH402921.jpeg`
- Duplicate sources: `pages\8199.html`, `pages\23270.html`, `pages\21683.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2018)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 480 rpm | 6, 500 rpm

MAP value [MAP SENSOR]*, * 1 | 500 rpm | 28 kPa (205 mmHg, 8.1 inHg) | -

2, 500 rpm | 24 kPa (175 mmHg, 6.9 inHg) | -

MAP value [MAP SENSOR]*, * 2 | 500 rpm | 22 kPa (163 mmHg, 6.5 inHg) | -

2, 250 rpm | 22 kPa (159 mmHg, 6.3 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: CVT

*2: M/T

*: Varies with driving conditions.[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 17 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.
````

## Chunk 5432: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2018)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2018)
- Source path: `pages\6612.html`
- Chunk ID: `chunk_8d4be5a88bc6`
- Images: `images\GHH402920.jpeg`, `images\GHH402921.jpeg`
- Duplicate sources: `pages\6613.html`, `pages\8199.html`, `pages\8200.html`, `pages\23270.html`, `pages\23271.html`, `pages\21683.html`, `pages\21684.html`

### Full Text

````text
ating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM***.

*** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5433: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2019)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2019)
- Source path: `pages\6613.html`
- Chunk ID: `chunk_e6d2e51d08f6`
- Images: `images\GHH402922.jpeg`, `images\GHH402923.jpeg`
- Duplicate sources: `pages\8200.html`, `pages\23271.html`, `pages\21684.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2019)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 480 rpm | 6, 500 rpm

MAP value [MAP SENSOR]*, * 1 | 500 rpm | 28 kPa (205 mmHg, 8.1 inHg) | -

2, 500 rpm | 24 kPa (175 mmHg, 6.9 inHg) | -

MAP value [MAP SENSOR]*, * 2 | 500 rpm | 22 kPa (163 mmHg, 6.5 inHg) | -

2, 250 rpm | 22 kPa (159 mmHg, 6.3 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: CVT*2: M/T*: Varies with driving conditions.[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 20 - 89 times**, * 1 (17 - 89 times)**, * 2

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.
````

## Chunk 5434: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2020 2021)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2020 2021)
- Source path: `pages\6614.html`
- Chunk ID: `chunk_f1ccaff07759`
- Images: `images\GHH402924.jpeg`, `images\GHH402925.jpeg`
- Duplicate sources: `pages\8201.html`, `pages\23272.html`, `pages\21685.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2020 2021)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected No. 4 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 480 rpm | 6, 500 rpm

MAP value [MAP SENSOR]*, * 1 | 500 rpm | 28 kPa (205 mmHg, 8.1 inHg) | -

2, 500 rpm | 24 kPa (175 mmHg, 6.9 inHg) | -

MAP value [MAP SENSOR]*, * 2 | 500 rpm | 22 kPa (163 mmHg, 6.5 inHg) | -

2, 250 rpm | 22 kPa (159 mmHg, 6.3 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: CVT*2: M/T*: Varies with driving conditions.[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 20 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.
````

## Chunk 5435: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2020 2021)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7 (except Si)/L15BA/L15BY: USA/Canada models) (2020 2021)
- Source path: `pages\6614.html`
- Chunk ID: `chunk_682cb0dd28b1`
- Images: `images\GHH402924.jpeg`, `images\GHH402925.jpeg`
- Duplicate sources: `pages\8201.html`, `pages\23272.html`, `pages\21685.html`

### Full Text

````text
ave difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM***.

*** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5436: DTC P0300, P0301, P0302, P0303, P0304 (L15B7/L15BA)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7/L15BA)
- Source path: `pages\6615.html`
- Chunk ID: `chunk_45b8d596116a`
- Images: `images\GHH402926.jpeg`, `images\GHH402927.jpeg`
- Duplicate sources: `pages\8202.html`, `pages\23273.html`, `pages\21686.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (L15B7/L15BA)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 480 rpm | 6, 500 rpm

MAP value [MAP SENSOR]*, * 1 | 500 rpm | 28 kPa (205 mmHg, 8.1 inHg) | -

2, 500 rpm | 24 kPa (175 mmHg, 6.9 inHg) | -

MAP value [MAP SENSOR]*, * 2 | 700 rpm** | 21 kPa (156 mmHg, 6.2 inHg) | -

2, 500 rpm** | 23 kPa (167 mmHg, 6.6 inHg) | -

700 rpm*** | 38 kPa (280 mmHg, 11.1 inHg) | -

2, 650 rpm*** | 24 kPa (176 mmHg, 7.0 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*1: CVT

*2: M/T

*: Varies with driving conditions.

**: Rocker arm oil control solenoid: OFF

***: Rocker arm oil control solenoid: ON[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 17 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.
````

## Chunk 5437: DTC P0300, P0301, P0302, P0303, P0304 (L15B7/L15BA)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (L15B7/L15BA)
- Source path: `pages\6615.html`
- Chunk ID: `chunk_51f2b58f02c7`
- Images: `images\GHH402926.jpeg`, `images\GHH402927.jpeg`
- Duplicate sources: `pages\8202.html`, `pages\23273.html`, `pages\21686.html`

### Full Text

````text
e data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM***.

*** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5438: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2017 2018)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2017 2018)
- Source path: `pages\6616.html`
- Chunk ID: `chunk_b01bc3f857bb`
- Images: `images\GHH402928.jpeg`, `images\GHH402929.jpeg`
- Duplicate sources: `pages\8203.html`, `pages\23274.html`, `pages\21687.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (Si) (2017 2018)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 500 rpm | 6, 500 rpm

MAP value [MAP SENSOR]* | 500 rpm | 24 kPa (174 mmHg, 6.9 inHg) | -

2, 750 rpm | 23 kPa (172 mmHg, 6.8 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*: Varies with driving conditions.[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 17 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.
````

## Chunk 5439: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2017 2018)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2017 2018)
- Source path: `pages\6616.html`
- Chunk ID: `chunk_c1ce95a07352`
- Images: `images\GHH402928.jpeg`, `images\GHH402929.jpeg`
- Duplicate sources: `pages\6617.html`, `pages\8203.html`, `pages\8204.html`, `pages\23274.html`, `pages\23275.html`, `pages\21687.html`, `pages\21688.html`

### Full Text

````text
ng the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.

- If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Misfire Type 2:

- If a type 2 misfire (emission-related but not severe enough to immediately damage the catalyst) occurs, a Pending DTC is stored, but the MIL does not come on or blink. If a type 2 misfire occurs during a second drive cycle, the MIL comes on and stays on unless the Pending DTC has been cleared by the PCM***.

*** The Pending DTC is erased if either of these conditions is met:

- The vehicle is operated at least once under the same driving conditions as the first misfire detection, and no misfire is detected.

- 80 drive cycles, regardless of driving conditions, are completed with no misfire detected.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive drive cycles in which the engine conditions are similar to the first time the malfunction was detected. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5440: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2019 2020 2021)

- Title: DTC P0300, P0301, P0302, P0303, P0304 (Si) (2019 2020 2021)
- Source path: `pages\6617.html`
- Chunk ID: `chunk_56379459e9f3`
- Images: `images\GHH402930.jpeg`, `images\GHH402931.jpeg`
- Duplicate sources: `pages\8204.html`, `pages\23275.html`, `pages\21688.html`

### Full Text

````text
# DTC P0300, P0301, P0302, P0303, P0304 (Si) (2019 2020 2021)

DTC P0300: Random Misfire Detected

DTC P0301: No. 1 Cylinder Misfire Detected

DTC P0302: No. 2 Cylinder Misfire Detected

DTC P0303: No. 3 Cylinder Misfire Detected

DTC P0304: No. 4 Cylinder Misfire Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft vibrates slightly when each cylinder fires. If a misfire occurs, the crankshaft rotation speed changes rapidly. The powertrain control module (PCM) monitors the crankshaft rotation speed based on the output pulses from the crankshaft position (CKP) sensor. By monitoring changes in the crankshaft rotation speed, the PCM counts the number of misfires and determines which cylinder is misfiring.

- P0300: If more than one DTC from P0301 through P0304 has been stored while misfires in multiple cylinders are detected, a malfunction is detected and a DTC is stored.

- P0301, P0302, P0303, P0304: If a misfire is detected, a DTC is stored.

There are two types of misfire detection:

- Type 1: When the number of misfires per 200 engine revolutions reaches the level that can damage the three way catalyst (TWC), a DTC is stored and the MIL blinks.

- Type 2: When the number of misfires per 1, 000 engine revolutions reaches the level that affects FTP mode exhaust emissions, a DTC is stored and the MIL comes on.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | Type 1 | Per 200 revolutions

Type 2 | Per 1, 000 revolutions

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after monitor finishing condition except immediate starting the engine | 1.0 second | -

Engine coolant temperature [ECT SENSOR 1] | None, unless the initial engine coolant temperature [ECT SENSOR 1] is 14 deg.F (-10 deg.C) or less, in which case the monitor will not run until the engine coolant temperature [ECT SENSOR 1] reaches 68 deg.F (20 deg.C)

Engine speed [ENGINE SPEED] | 500 rpm | 6, 500 rpm

MAP value [MAP SENSOR]* | 500 rpm | 24 kPa (174 mmHg, 6.9 inHg) | -

2, 750 rpm | 23 kPa (172 mmHg, 6.8 inHg) | -

Fuel feedback | Other than during fuel cut-off operation

Other | Test-drive on a flat road to avoid misdetection

*: Varies with driving conditions.[ ]: HDS Parameter

Malfunction Threshold

The number of misfires versus engine revolutions is equal to or greater than the values in the table.

Misfire Type | The number of engine revolutions | The number of misfires

Misfire Type 1 (Severe) | Per 200 revolutions | 20 - 89 times**

Misfire Type 2 (Light) | Per 1, 000 revolutions | 77 times

**: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Ignition system failure

- Fuel supply system failure

- Intake air system failure

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 15 - 75 mph (25 - 120 km/h) for at least 3 minutes.

- Stop the vehicle, and let the engine idle for at least 3 minutes.

- When freeze data is stored, drive the vehicle under those conditions instead of Driving Pattern step 2 or 3.

- When you have difficulty duplicating the DTC because of road conditions and traffic situations, repeat the driving pattern several times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

Misfire Type 1:

- If a type 1 misfire (catalyst damaging) occurs once, the MIL blinks once per second, a Pending DTC is stored, and the high rpm fuel injection stop system activates. The fuel injection stops, at high rpm only, on the cylinder that has the highest misfire counts. The MIL then continues to blink and the fuel injection stays off at high rpm, until the drive is completed.

- If a type 1 misfire occurs during a second drive cycle, the MIL and fuel injection behave the same and a Confirmed DTC is stored.

- After a type 1 misfire has been detected during two drive cycles, the MIL comes on and stays on beginning with the third drive cycle, unless the Pending DTC has been cleared by the PCM***. Even if the MIL is on, it will start blinking if a type 1 misfire occurs.
````

## Chunk 5441: DTC P0326 (K20C1) (2017 2018 2019)

- Title: DTC P0326 (K20C1) (2017 2018 2019)
- Source path: `pages\6618.html`
- Chunk ID: `chunk_3924b30ecd2b`
- Images: `images\GHH402932.jpeg`
- Duplicate sources: `pages\8205.html`, `pages\23276.html`, `pages\21689.html`

### Full Text

````text
# DTC P0326 (K20C1) (2017 2018 2019)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the knock sensor for rationality faults. The knock sensor is attached to the cylinder block. The knock sensor transforms the structure borne vibrations into electrical signals which can be evaluated by the PCM. The knock sensor signal is evaluated according to intensity and spectral information of knocking and non-knocking combustions. The diagnostic strategy is identical for all cylinders. It starts by calculating a normalized reference level of knock control based on the knock sensor's signal. This reference signal represents the basic noise of the current cylinder being analyzed. The normalized reference level of knock control is continuously monitored against minimum rationality threshold. If the normalized reference level of knock control is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine coolant temperature [ECT Sensor 1] | 122.6 deg.F (50.3 deg.C) | -

Engine speed [Engine Speed] | 1, 920 rpm | -

Charging efficiency | 43.008 % | -

Other | Crankshaft (CKP) sensor and camshaft (CMP) sensors output signals are valid

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met for at least 30 counts:

- Normalized reference voltage of the knock sensor is less than 0.2002 V - 1.2012 V*.

- Normalized reference voltage of the knock sensor is greater than 13.8477 V - 230 V*.

*: Depends on engine speed

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor loose connection or poor contact

- Excessively high engine noise

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [Engine Speed] 2, 000 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5442: DTC P0326 (K20C1) (2019 2020 2021)

- Title: DTC P0326 (K20C1) (2019 2020 2021)
- Source path: `pages\6619.html`
- Chunk ID: `chunk_1f216de25918`
- Images: `images\GHH402933.jpeg`
- Duplicate sources: `pages\8206.html`, `pages\23277.html`, `pages\21690.html`

### Full Text

````text
# DTC P0326 (K20C1) (2019 2020 2021)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the knock sensor for rationality faults. The knock sensor is attached to the cylinder block. The knock sensor transforms the structure borne vibrations into electrical signals which can be evaluated by the PCM. The knock sensor signal is evaluated according to intensity and spectral information of knocking and non-knocking combustions. The diagnostic strategy is identical for all cylinders. It starts by calculating a normalized reference level of knock control based on the knock sensor's signal. This reference signal represents the basic noise of the current cylinder being analyzed. The normalized reference level of knock control is continuously monitored against minimum rationality threshold. If the normalized reference level of knock control is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 920 rpm | -

Other | Condition in steady engine load and engine speed

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions is met for at least 30 counts:

- Normalized reference voltage of the knock sensor is less than 0.2002 V - 1.2012 V*.

- Normalized reference voltage of the knock sensor is greater than 13.85 V - 230 V*.

*: Depends on engine speed

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor loose connection or poor contact

- Excessively high engine noise

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [Engine Speed] 2, 000 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5443: DTC P0326 (K20C2)

- Title: DTC P0326 (K20C2)
- Source path: `pages\6620.html`
- Chunk ID: `chunk_e28ba77988b9`
- Images: `images\GHH402934.jpeg`, `images\GHH402935.jpeg`
- Duplicate sources: `pages\8207.html`, `pages\23278.html`, `pages\21691.html`

### Full Text

````text
# DTC P0326 (K20C2)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A nonresonant type of knock sensor is used, and it is mounted on the cylinder block to detect engine knocking. Vibration from engine combustion causes the torus-shaped weight to compress the ceramic element in the nonresonant knock sensor, and converts it into electrical signals. The powertrain control module (PCM) controls the ignition timing according to the electrical signal level. If the signal level from the knock sensor drops for a set time because of a poor connection at the knock sensor, or a bad sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5.0 seconds | -

Engine speed [ENGINE SPEED] | 1, 750 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5.0 seconds:

- The knock sensor output signal strength is 42 or less at the engine speed [ENGINE SPEED] of 1, 750 rpm.

- The knock sensor output signal strength is 62 or less at the engine speed [ENGINE SPEED] of 2, 500 rpm.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor misinstalled

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] 1, 750 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5444: DTC P0326 (L15B7 (except Si)/L15BA/L15BY) (2019 2020 2021)

- Title: DTC P0326 (L15B7 (except Si)/L15BA/L15BY) (2019 2020 2021)
- Source path: `pages\6621.html`
- Chunk ID: `chunk_c37d9b78ab6b`
- Images: `images\GHH402936.jpeg`, `images\GHH402937.jpeg`
- Duplicate sources: `pages\8208.html`, `pages\23279.html`, `pages\21692.html`

### Full Text

````text
# DTC P0326 (L15B7 (except Si)/L15BA/L15BY) (2019 2020 2021)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A nonresonant type of knock sensor is used, and it is mounted on the cylinder block to detect engine knocking. Vibration from engine combustion causes the torus-shaped weight to compress the ceramic element in the nonresonant knock sensor, and converts it into electrical signals. The powertrain control module (PCM) controls the ignition timing according to the electrical signal level. If the signal level from the knock sensor drops for a set time because of a poor connection at the knock sensor, or a bad sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5.0 seconds | -

Engine speed [ENGINE SPEED] | 2, 000 rpm | -

[ ]: HDS Parameter

Malfunction Threshold (CVT)

Either one of the conditions is met for at least 5.0 seconds.

- The knock sensor output signal strength is 55 or less at the engine speed [ENGINE SPEED] of 1, 500 rpm*.

- The knock sensor output signal strength is 95 or less at the engine speed [ENGINE SPEED] of 2, 500 rpm*.

*: Depending on engine speed and load.

Malfunction Threshold (M/T)

Either one of the conditions is met for at least 5.0 seconds.

- The knock sensor output signal strength is 44 or less at the engine speed [ENGINE SPEED] of 1, 500 rpm*.

- The knock sensor output signal strength is 77 or less at the engine speed [ENGINE SPEED] of 2, 500 rpm*.

*: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor misinstalled

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] 2, 000 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5445: DTC P0326 (L15B7/L15BA/L15BY) (2016 2017 2018)

- Title: DTC P0326 (L15B7/L15BA/L15BY) (2016 2017 2018)
- Source path: `pages\6622.html`
- Chunk ID: `chunk_8ffbeb240e0a`
- Images: `images\GHH402938.jpeg`, `images\GHH402939.jpeg`
- Duplicate sources: `pages\8209.html`, `pages\23280.html`, `pages\21693.html`

### Full Text

````text
# DTC P0326 (L15B7/L15BA/L15BY) (2016 2017 2018)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A nonresonant type of knock sensor is used, and it is mounted on the cylinder block to detect engine knocking. Vibration from engine combustion causes the torus-shaped weight to compress the ceramic element in the nonresonant knock sensor, and converts it into electrical signals. The powertrain control module (PCM) controls the ignition timing according to the electrical signal level. If the signal level from the knock sensor drops for a set time because of a poor connection at the knock sensor, or a bad sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5.0 seconds | -

Engine speed [ENGINE SPEED] | 2, 000 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5.0 seconds.

- The knock sensor output signal strength is 60 or less at the engine speed [ENGINE SPEED] of 1, 250 rpm*.

- The knock sensor output signal strength is 111 or less at the engine speed [ENGINE SPEED] of 2, 500 rpm*.

*: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor misinstalled

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] 2, 000 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5446: DTC P0326 (Si) (2019 2020 2021)

- Title: DTC P0326 (Si) (2019 2020 2021)
- Source path: `pages\6623.html`
- Chunk ID: `chunk_39b10769155a`
- Images: `images\GHH402940.jpeg`, `images\GHH402941.jpeg`
- Duplicate sources: `pages\8210.html`, `pages\23281.html`, `pages\21694.html`

### Full Text

````text
# DTC P0326 (Si) (2019 2020 2021)

DTC P0326: Knock Sensor Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

A nonresonant type of knock sensor is used, and it is mounted on the cylinder block to detect engine knocking. Vibration from engine combustion causes the torus-shaped weight to compress the ceramic element in the nonresonant knock sensor, and converts it into electrical signals. The powertrain control module (PCM) controls the ignition timing according to the electrical signal level. If the signal level from the knock sensor drops for a set time because of a poor connection at the knock sensor, or a bad sensor, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 5.0 seconds | -

Engine speed [ENGINE SPEED] | 2, 000 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Either one of the conditions is met for at least 5.0 seconds.

- The knock sensor output signal strength is 47 or less at the engine speed [ENGINE SPEED] of 1, 250 rpm*.

- The knock sensor output signal strength is 90 or less at the engine speed [ENGINE SPEED] of 2, 500 rpm*.

*: Depending on engine speed and load.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Knock sensor misinstalled

- Knock sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at an engine speed [ENGINE SPEED] 2, 000 rpm or more for at least 5 seconds.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5447: DTC P0327, P0328 (K20C1) (2017 2018 2019)

- Title: DTC P0327, P0328 (K20C1) (2017 2018 2019)
- Source path: `pages\6624.html`
- Chunk ID: `chunk_361f974ef90c`
- Images: `images\GHH402942.jpeg`
- Duplicate sources: `pages\8211.html`, `pages\23282.html`, `pages\21695.html`

### Full Text

````text
# DTC P0327, P0328 (K20C1) (2017 2018 2019)

DTC P0327: Knock Sensor Circuit Low Voltage

DTC P0328: Knock Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

A piezo sensitive knock sensor is mounted on cylinder block. The powertrain control module (PCM) monitors the knock sensor for electrical malfunctions. The knock sensor transforms the structure borne vibrations into electrical signals which can be evaluated by the PCM. The knock sensor signal is evaluated according to intensity and spectral information of knocking and non-knocking combustions. The output voltage of the knock sensor is continuously monitored against minimum and maximum thresholds. If the knock sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0327

The knock sensor output voltage is less than -0.700021 V at least 3 events.

DTC: P0328

The knock sensor output voltage is greater than 1.000031 V at least 3 events.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0327

- Knock sensor KS POS line short to ground

- Knock sensor KS NEG line short to ground

DTC: P0328

- Knock sensor KS POS line short to power

- Knock sensor KS NEG line short to power

Common

- Knock sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, hold the engine speed [Engine Speed] over 1, 000 rpm.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5448: DTC P0327, P0328 (K20C1) (2019 2020 2021)

- Title: DTC P0327, P0328 (K20C1) (2019 2020 2021)
- Source path: `pages\6625.html`
- Chunk ID: `chunk_cf4bf22b85c9`
- Images: `images\GHH402943.jpeg`
- Duplicate sources: `pages\8212.html`, `pages\23283.html`, `pages\21696.html`

### Full Text

````text
# DTC P0327, P0328 (K20C1) (2019 2020 2021)

DTC P0327: Knock Sensor Circuit Low Voltage

DTC P0328: Knock Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

A piezo sensitive knock sensor is mounted on cylinder block. The powertrain control module (PCM) monitors the knock sensor for electrical malfunctions. The knock sensor transforms the structure borne vibrations into electrical signals which can be evaluated by the PCM. The knock sensor signal is evaluated according to intensity and spectral information of knocking and non-knocking combustions. The output voltage of the knock sensor is continuously monitored against minimum and maximum thresholds. If the knock sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 000 rpm | -

Other | Condition in steady engine load and engine speed

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0327

The knock sensor output voltage is less than -0.7 V at least 3 events.

DTC: P0328

The knock sensor output voltage is greater than 1 V at least 3 events.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0327

- Knock sensor KS POS line short to ground

- Knock sensor KS NEG line short to ground

DTC: P0328

- Knock sensor KS POS line short to power

- Knock sensor KS NEG line short to power

Common

- Knock sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, hold the engine speed [Engine Speed] over 1, 000 rpm.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5449: DTC P0327, P0328 (K20C2)

- Title: DTC P0327, P0328 (K20C2)
- Source path: `pages\6626.html`
- Chunk ID: `chunk_4dbd8fcd0b4c`
- Images: `images\GHH402944.jpeg`
- Duplicate sources: `pages\8213.html`, `pages\23284.html`, `pages\21697.html`

### Full Text

````text
# DTC P0327, P0328 (K20C2)

DTC P0327: Knock Sensor Circuit Low Voltage

DTC P0328: Knock Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The knock sensor is mounted on the engine block and detects engine knocking. The vibrations caused by the knocking are converted into electrical signals through the piezo ceramic element. The powertrain control module (PCM) controls the ignition timing based on the electrical signal. If the signal from the knock sensor is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0327

The knock sensor output voltage is 0.50 V or less for at least 2 seconds.

DTC: P0328

The knock sensor output voltage is 4.50 V or more for at least 2 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0327

- Knock sensor KNOCK line short to ground

DTC: P0328

- Knock sensor KNOCK line open

- Knock sensor KS GND line open

Common

- Knock sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5450: DTC P0327, P0328 (L15B7/L15BA/L15BY)

- Title: DTC P0327, P0328 (L15B7/L15BA/L15BY)
- Source path: `pages\6627.html`
- Chunk ID: `chunk_69d0a2600227`
- Images: `images\GHH402945.jpeg`
- Duplicate sources: `pages\8214.html`, `pages\23285.html`, `pages\21698.html`

### Full Text

````text
# DTC P0327, P0328 (L15B7/L15BA/L15BY)

DTC P0327: Knock Sensor Circuit Low Voltage

DTC P0328: Knock Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The knock sensor is mounted on the engine block and detects engine knocking. The vibrations caused by the knocking are converted into electrical signals through the piezo ceramic element. The powertrain control module (PCM) controls the ignition timing based on the electrical signal. If the signal from the knock sensor is a specified voltage for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

DTC: P0327

The knock sensor output voltage is 0.50 V or less for at least 2 seconds.

DTC: P0328

The knock sensor output voltage is 4.50 V or more for at least 2 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0327

- Knock sensor KS line short to ground

DTC: P0328

- Knock sensor KS line open

- Knock sensor KSGND line open

Common

- Knock sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5451: DTC P0335 (K20C1) (2017 2018 2019)

- Title: DTC P0335 (K20C1) (2017 2018 2019)
- Source path: `pages\6628.html`
- Chunk ID: `chunk_4f7339ca4459`
- Images: `images\GHH402946.jpeg`
- Duplicate sources: `pages\8215.html`, `pages\23286.html`, `pages\21699.html`

### Full Text

````text
# DTC P0335 (K20C1) (2017 2018 2019)

DTC P0335: Crankshaft Position (CKP) Sensor No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor consists of a pulse plate and a semiconductor that detects rotor position. When the engine starts, the pulse plate turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). The CKP sensor detects injection/ignition timing for each cylinder and the engine speed. If no pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Malfunction detection starts if either conditions is met:

Condition 1

Condition

Starter | ON

Condition 2

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 600 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

No input signals from the CKP sensor are detected while 3 camshaft revolutions are reached.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRK line short to ground

- CKP sensor CRK line short to power

- CKP sensor CRK line open

- CKP sensor VCC line noise interrupted

- CKP sensor SG line noise interrupted

- Large gap between CKP sensor and pulse plate

- CKP sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5452: DTC P0335 (K20C1) (2019 2020 2021)

- Title: DTC P0335 (K20C1) (2019 2020 2021)
- Source path: `pages\6629.html`
- Chunk ID: `chunk_d1c4bc436d2f`
- Images: `images\GHH402947.jpeg`
- Duplicate sources: `pages\8216.html`, `pages\23287.html`, `pages\21700.html`

### Full Text

````text
# DTC P0335 (K20C1) (2019 2020 2021)

DTC P0335: Crankshaft Position (CKP) Sensor No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor consists of a pulse plate and a semiconductor that detects rotor position. When the engine starts, the pulse plate turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). The CKP sensor detects injection/ignition timing for each cylinder and the engine speed. If no pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed] | 1 mph (1 km/h) | 15 mph (25 km/h)

Other | Starter in active or engine speed [Engine Speed] more than 600 rpm

[ ]: HDS Parameter

Malfunction Threshold

No input signals from the CKP sensor are detected while 3 camshaft revolutions are reached.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRK line short to ground

- CKP sensor CRK line short to power

- CKP sensor CRK line open

- CKP sensor VCC line noise interrupted

- CKP sensor SG line noise interrupted

- Large gap between CKP sensor and pulse plate

- CKP sensor failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at vehicle speed [Vehicle Speed] 15 mph (25 km/h) or less for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5453: DTC P0335 (K20C2)

- Title: DTC P0335 (K20C2)
- Source path: `pages\6630.html`
- Chunk ID: `chunk_3dadb98ff07b`
- Images: `images\GHH402948.jpeg`
- Duplicate sources: `pages\8217.html`, `pages\23288.html`, `pages\21701.html`

### Full Text

````text
# DTC P0335 (K20C2)

DTC P0335: Crankshaft Position (CKP) Sensor No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor detects injection/ignition timing for each cylinder and engine speed. The CKP sensor consists of a rotor and a semiconductor that detects rotor position. When the engine starts, the rotor turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). If no pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from the CKP sensor are detected while signals from the camshaft position (CMP) sensor are detected at least 75 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRANK line open

- CKP sensor CRANK line short to ground

- CKP sensor VCC line open

- CKP sensor SG line open

- CKP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5454: DTC P0335 (L15B7/L15BA/L15BY)

- Title: DTC P0335 (L15B7/L15BA/L15BY)
- Source path: `pages\6631.html`
- Chunk ID: `chunk_b493504144f9`
- Images: `images\GHH402949.jpeg`
- Duplicate sources: `pages\8218.html`, `pages\23289.html`, `pages\21702.html`

### Full Text

````text
# DTC P0335 (L15B7/L15BA/L15BY)

DTC P0335: Crankshaft Position (CKP) Sensor No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor detects injection/ignition timing for each cylinder and engine speed. The CKP sensor consists of a rotor and a semiconductor that detects rotor position. When the engine starts, the rotor turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). If no pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from the CKP sensor are detected while signals from the camshaft position (CMP) sensor are detected at least 75 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRKP line open

- CKP sensor CRKP line short to ground

- CKP sensor VCC line open

- CKP sensor SG line open

- CKP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5455: DTC P0339 (K20C1) (2017 2018 2019)

- Title: DTC P0339 (K20C1) (2017 2018 2019)
- Source path: `pages\6632.html`
- Chunk ID: `chunk_4434f8e0713d`
- Images: `images\GHH402950.jpeg`
- Duplicate sources: `pages\8219.html`, `pages\23290.html`, `pages\21703.html`

### Full Text

````text
# DTC P0339 (K20C1) (2017 2018 2019)

DTC P0339: Crankshaft Position (CKP) Sensor Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor consists of a pulse plate and a semiconductor that detects rotor position. When the engine starts, the pulse plate turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). The CKP sensor detects injection/ignition timing for each cylinder and the engine speed. If an abnormal amount of pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second

DTC Type | One drive cycle, MIL on

Enable Conditions

Malfunction detection starts if either conditions is met:

Condition 1

Condition

Starter | ON

Condition 2

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 600 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met at least 8 times:

- The current tooth time period is bigger than 50 milliseconds or smaller than 0.125 millisecond.

- More than 68 tooth counts between detected gaps.

- The ratio of current tooth time to previous tooth time exceeds 1.5 - 2 if gap is not expected.

- The ratio of current tooth time to previous tooth time exceeds 3.38 - 8 if gap is expected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor loose connection or poor contact

- Change of gap between CKP sensor and pulse plate (eccentric pulse plate, large gap, loose CKP sensor mounting, CKP sensor movement)

- Noise disturbance by starter

- Noise disturbance by drive pulse for injection and ignition

- Pulse plate defection

- CKP sensor failure

Confirmation Procedure

Operating Condition

Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5456: DTC P0339 (K20C1) (2019 2020 2021)

- Title: DTC P0339 (K20C1) (2019 2020 2021)
- Source path: `pages\6633.html`
- Chunk ID: `chunk_d497d2ade165`
- Images: `images\GHH402951.jpeg`
- Duplicate sources: `pages\8220.html`, `pages\23291.html`, `pages\21704.html`

### Full Text

````text
# DTC P0339 (K20C1) (2019 2020 2021)

DTC P0339: Crankshaft Position (CKP) Sensor Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor consists of a pulse plate and a semiconductor that detects rotor position. When the engine starts, the pulse plate turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). The CKP sensor detects injection/ignition timing for each cylinder and the engine speed. If an abnormal amount of pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed] | 1 mph (1 km/h) | 15 mph (25 km/h)

Other | Starter in active or engine speed [Engine Speed] more than 600 rpm

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions is met continuously at least 8 times:

- The engine speed calculated from tooth time period is lower than 20 rpm or higher than 12, 000 rpm.

- More than 60 tooth counts between detected gaps.

- The ratio of current tooth time to previous tooth time exceeds 1.5 - 2 if gap is not expected.

- The ratio of current tooth time to previous tooth time exceeds 3.38 - 8 if gap is expected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor loose connection or poor contact

- Change of gap between CKP sensor and pulse plate (eccentric pulse plate, large gap, loose CKP sensor mounting, CKP sensor movement)

- Noise disturbance by starter

- Noise disturbance by drive pulse for injection and ignition

- Pulse plate defection

- CKP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine. Hold the engine speed [Engine Speed] at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

- Drive the vehicle at vehicle speed [Vehicle Speed] 15 mph (25 km/h) or less for at least 1 second.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5457: DTC P0339 (K20C2)

- Title: DTC P0339 (K20C2)
- Source path: `pages\6634.html`
- Chunk ID: `chunk_ed26f9432279`
- Images: `images\GHH402952.jpeg`
- Duplicate sources: `pages\8221.html`, `pages\23292.html`, `pages\21705.html`

### Full Text

````text
# DTC P0339 (K20C2)

DTC P0339: Crankshaft Position (CKP) Sensor Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor detects injection/ignition timing for each cylinder and engine speed. The CKP sensor consists of a rotor and a semiconductor that detects rotor position. When the engine starts, the rotor turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). If abnormal amount of pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Other than 58 pulses are detected during intervals between reference pulses for each crank revolution. This condition has been detected at least 30 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRANK line electrical noise overlapped

- CKP sensor rotor chipped

- CKP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5458: DTC P0339 (L15B7/L15BA/L15BY)

- Title: DTC P0339 (L15B7/L15BA/L15BY)
- Source path: `pages\6635.html`
- Chunk ID: `chunk_80bd0c03a4a7`
- Images: `images\GHH402953.jpeg`
- Duplicate sources: `pages\8222.html`, `pages\23293.html`, `pages\21706.html`

### Full Text

````text
# DTC P0339 (L15B7/L15BA/L15BY)

DTC P0339: Crankshaft Position (CKP) Sensor Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The crankshaft position (CKP) sensor detects injection/ignition timing for each cylinder and engine speed. The CKP sensor consists of a rotor and a semiconductor that detects rotor position. When the engine starts, the rotor turns and the magnetic flux in the semiconductor device changes. The changes of magnetic flux are converted into pulsing signals to the powertrain control module (PCM). If abnormal amount of pulsing signals from the CKP sensor are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Other than 58 pulses are detected during intervals between reference pulses for each crank revolution. This condition has been detected at least 30 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CKP sensor CRKP line electrical noise overlapped

- CKP sensor rotor chipped

- CKP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5459: DTC P0340 (K20C1) (2017 2018 2019)

- Title: DTC P0340 (K20C1) (2017 2018 2019)
- Source path: `pages\6636.html`
- Chunk ID: `chunk_9a1baa455b58`
- Images: `images\GHH402954.jpeg`
- Duplicate sources: `pages\8223.html`, `pages\23294.html`, `pages\21707.html`

### Full Text

````text
# DTC P0340 (K20C1) (2017 2018 2019)

DTC P0340: Camshaft Position (CMP) Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor A mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor A. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor A. If the powertrain control module (PCM) recognizes no signal from CMP sensor A, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.8 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Other | Crankshaft position (CKP) sensor signal with gap detected

Malfunction Threshold

If no signal from CMP sensor A is detected during a crankshaft revolution, a counter is incremented.

The number of consecutive unrecognized signals (counter) exceeds 8 times and the measured input level is less than 0.4 V, or greater than 2.4 V.

*: The counter resets to zero as soon as one or more new camshaft edges were acquired.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A CAM line short to ground

- CMP sensor A CAM line short to power

- CMP sensor A CAM line open

- CMP sensor A failure

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

## Chunk 5460: DTC P0340 (K20C1) (2019 2020 2021)

- Title: DTC P0340 (K20C1) (2019 2020 2021)
- Source path: `pages\6637.html`
- Chunk ID: `chunk_70f0fb5853ef`
- Images: `images\GHH402955.jpeg`
- Duplicate sources: `pages\8224.html`, `pages\23028.html`, `pages\21441.html`

### Full Text

````text
# DTC P0340 (K20C1) (2019 2020 2021)

DTC P0340: Camshaft Position (CMP) Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor A mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor A. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor A. If the powertrain control module (PCM) recognizes no signal from CMP sensor A, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Both conditions occur:

- No camshaft signal is detected at least 8 crankshaft revolutions.

- The measured input level is less than 1.9 V, or more than 3.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A CAM line short to ground

- CMP sensor A CAM line short to power

- CMP sensor A CAM line open

- CMP sensor A failure

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

## Chunk 5461: DTC P0340 (K20C2)

- Title: DTC P0340 (K20C2)
- Source path: `pages\6638.html`
- Chunk ID: `chunk_73823732ddd7`
- Images: `images\GHH402956.jpeg`
- Duplicate sources: `pages\8225.html`, `pages\23029.html`, `pages\21442.html`

### Full Text

````text
# DTC P0340 (K20C2)

DTC P0340: Camshaft Position (CMP) Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A consists of a rotor and a semiconductor that detects rotor position and intake camshaft timing. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). CMP sensor A also detects the top dead center of each cylinder for fuel injection. The PCM determines the camshaft position according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If no pulsing signals from CMP sensor A are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from CMP sensor A are detected while signals from the CKP sensor are detected at least 300 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A TDC line open

- CMP sensor A TDC line short to ground

- CMP sensor A VCC line open

- CMP sensor A SG line open

- CMP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5462: DTC P0340 (L15B7/L15BA/L15BY)

- Title: DTC P0340 (L15B7/L15BA/L15BY)
- Source path: `pages\6639.html`
- Chunk ID: `chunk_114034878fff`
- Images: `images\GHH402957.jpeg`
- Duplicate sources: `pages\8226.html`, `pages\23030.html`, `pages\21443.html`

### Full Text

````text
# DTC P0340 (L15B7/L15BA/L15BY)

DTC P0340: Camshaft Position (CMP) Sensor A No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A consists of a rotor and a semiconductor that detects rotor position and intake camshaft timing. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). CMP sensor A also detects the top dead center of each cylinder for fuel injection. The PCM determines the camshaft position according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If no pulsing signals from CMP sensor A are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from CMP sensor A are detected while signals from the CKP sensor are detected at least 300 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A TDCAM line open

- CMP sensor A TDCAM line short to ground

- CMP sensor A VCC line open

- CMP sensor A SG line open

- CMP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5463: DTC P0341 (K20C2)

- Title: DTC P0341 (K20C2)
- Source path: `pages\6640.html`
- Chunk ID: `chunk_5ff90119423e`
- Images: `images\GHH402958.jpeg`
- Duplicate sources: `pages\8227.html`, `pages\23031.html`, `pages\21444.html`

### Full Text

````text
# DTC P0341 (K20C2)

DTC P0341: Camshaft Position (CMP) Sensor A and Crankshaft Position (CKP) Sensor Incorrect Phase Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A detects the intake camshaft timing and sends pulsing signals to the powertrain control module (PCM). The PCM determines the advance or the retard of the intake camshaft phase according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If the intake camshaft reference phase value deviates from a set range over a specified time period while the variable valve timing control (VTC) is not activated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapse time after starting the engine | 1.0 second | -

Engine speed [ENGINE SPEED] | 500 rpm | -

Other | VTC system not operating

[ ]: HDS Parameter

Malfunction Threshold

The difference between intake camshaft phase measured from CMP sensor A and intake camshaft standard phase value according to the CKP sensor position is 10 deg. or more for at least 4.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A poor installation

- CMP sensor A stuck

- CMP sensor A range/performance problem

- Cam chain poor installation

- VTC actuator A stuck

- VTC actuator A response delay

Confirmation Procedure

Operating Condition

Start the engine, and let it idle. When the diagnosis does not finish, allow the engine cool to an engine coolant temperature of ambient temperature, then restart the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5464: DTC P0341 (Without XM)

- Title: DTC P0341 (Without XM)
- Source path: `pages\6641.html`
- Chunk ID: `chunk_537b059d9f0a`
- Images: `images\GHH402959.jpeg`
- Duplicate sources: `pages\8228.html`, `pages\23032.html`, `pages\21445.html`

### Full Text

````text
# DTC P0341 (Without XM)

DTC P0341: Camshaft Position (CMP) Sensor A and Crankshaft Position (CKP) Sensor Incorrect Phase Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A detects the intake camshaft timing and sends pulsing signals to the powertrain control module (PCM). The PCM determines the advance or the retard of the intake camshaft timing according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If the intake camshaft reference phase value deviates from a set range over a specified time period while the variable valve timing control (VTC) is not activated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapse time after starting the engine | 1.0 second | -

Engine speed [ENGINE SPEED] | 500 rpm | -

Other | VTC system not operating

[ ]: HDS Parameter

Malfunction Threshold

The difference between intake camshaft phase measured from CMP sensor A and intake camshaft standard phase value according to the CKP sensor position is 10 deg. or more for at least 4.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A poor installation

- CMP sensor A stuck

- CMP sensor A range/performance problem

- VTC actuator A stuck

- VTC actuator A response delay

- Cam chain poor installation

Confirmation Procedure

Operating Condition

Start the engine, and let it idle. When the diagnosis does not finish, allow the engine cool to an engine coolant temperature [ECT SENSOR 1] of ambient temperature, then restart the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5465: DTC P0344 (K20C1) (2017 2018 2019)

- Title: DTC P0344 (K20C1) (2017 2018 2019)
- Source path: `pages\6642.html`
- Chunk ID: `chunk_48ab9bf50353`
- Images: `images\GHH402960.jpeg`
- Duplicate sources: `pages\8229.html`, `pages\23033.html`, `pages\21446.html`

### Full Text

````text
# DTC P0344 (K20C1) (2017 2018 2019)

DTC P0344: Camshaft Position (CMP) Sensor A Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor A mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor A. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor A. The PCM compares the generated pulse pattern with a stored calibrated pulse pattern. If the compared pulse pattern does not match, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Any of the conditions is met at least 12 times:

- The segment length is not equal to the reference length.

- The signal pattern does not match the calibrated pattern.

- Too many edge failures are detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Pulse plate defection

- CMP sensor A failure

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

## Chunk 5466: DTC P0344 (K20C1) (2019 2020 2021)

- Title: DTC P0344 (K20C1) (2019 2020 2021)
- Source path: `pages\6643.html`
- Chunk ID: `chunk_a7a1964d40d8`
- Images: `images\GHH402961.jpeg`
- Duplicate sources: `pages\8230.html`, `pages\23034.html`, `pages\21447.html`

### Full Text

````text
# DTC P0344 (K20C1) (2019 2020 2021)

DTC P0344: Camshaft Position (CMP) Sensor A Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor A mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor A. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor A. The PCM compares the generated pulse pattern with a stored calibrated pulse pattern. If the compared pulse pattern does not match, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Any of the conditions is met at least 12 times:

- Camshaft signal has wrong segment length.

- Signal table and reference table have many similar entries but no unique matching was found.

- The latest segment is not in the reference table or it is out of the sequence.

- Too many edge failures are detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Pulse plate defection

- CMP sensor A failure

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

## Chunk 5467: DTC P0344 (K20C2)

- Title: DTC P0344 (K20C2)
- Source path: `pages\6644.html`
- Chunk ID: `chunk_6f22b78748a1`
- Images: `images\GHH402962.jpeg`
- Duplicate sources: `pages\8231.html`, `pages\23035.html`, `pages\21448.html`

### Full Text

````text
# DTC P0344 (K20C2)

DTC P0344: Camshaft Position (CMP) Sensor A Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A consists of a rotor and a semiconductor that detects rotor position and intake camshaft timing. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). CMP sensor A also detects the top dead center of each cylinder for fuel injection. The PCM determines the camshaft position according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If abnormal amount of pulsing signals from CMP sensor A are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Other than 6 pulses are detected during two crankshaft revolutions. This condition has been detected at least 30 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A TDC line electrical noise overlapped

- CMP sensor A rotor chipped

- CMP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5468: DTC P0344 (L15B7/L15BA/L15BY)

- Title: DTC P0344 (L15B7/L15BA/L15BY)
- Source path: `pages\6645.html`
- Chunk ID: `chunk_6cf1e1589d80`
- Images: `images\GHH402963.jpeg`
- Duplicate sources: `pages\8232.html`, `pages\23036.html`, `pages\21449.html`

### Full Text

````text
# DTC P0344 (L15B7/L15BA/L15BY)

DTC P0344: Camshaft Position (CMP) Sensor A Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor A consists of a rotor and a semiconductor that detects rotor position and intake camshaft timing. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). CMP sensor A also detects the top dead center of each cylinder for fuel injection. The PCM determines the camshaft position according to the signals from the crankshaft position (CKP) sensor and CMP sensor A. If abnormal amount of pulsing signals from CMP sensor A are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

Other than 6 pulses are detected during two crankshaft revolutions. This condition has been detected at least 30 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor A TDCAM line electrical noise overlapped

- CMP sensor A rotor chipped

- CMP sensor A failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5469: DTC P0351, P0352, P0353, P0354 (K20C1) (2017 2018 2019)

- Title: DTC P0351, P0352, P0353, P0354 (K20C1) (2017 2018 2019)
- Source path: `pages\6646.html`
- Chunk ID: `chunk_cbac06e9dc0b`
- Images: `images\GHH402964.jpeg`
- Duplicate sources: `pages\8233.html`, `pages\23037.html`, `pages\21450.html`

### Full Text

````text
# DTC P0351, P0352, P0353, P0354 (K20C1) (2017 2018 2019)

DTC P0351: No. 1 Cylinder Ignition Coil Circuit Malfunction

DTC P0352: No. 2 Cylinder Ignition Coil Circuit Malfunction

DTC P0353: No. 3 Cylinder Ignition Coil Circuit Malfunction

DTC P0354: No. 4 Cylinder Ignition Coil Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

Electrical errors in connections from the ignition driver to the ignition coils could be detected by the powertrain control module (PCM) internal circuit. The PCM identifies short circuits and open circuit. The diagnosis of lines are done every 2 rotations of crankshaft. If the ignition coil output is out of a normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 1, 400 rpm | -

12 volt battery voltage [Battery] | 8 V | -

[ ]: HDS Parameter

Malfunction Threshold

- Short circuit to ground The ignition coil output current exceeds 30 mA for at least 0.5 second.

The ignition coil output current exceeds 30 mA for at least 0.5 second.

- Short circuit to power The ignition coil output voltage exceeds 5 V for at least 0.5 second.

The ignition coil output voltage exceeds 5 V for at least 0.5 second.

- Open The ignition coil output current drops below 1 mA for at least 0.5 second.

The ignition coil output current drops below 1 mA for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0351

- No. 1 ignition coil IGN01 line short to ground

- No. 1 ignition coil IGN01 line short to power

- No. 1 ignition coil IGN01 line open

DTC: P0352

- No. 2 ignition coil IGN02 line short to ground

- No. 2 ignition coil IGN02 line short to power

- No. 2 ignition coil IGN02 line open

DTC: P0353

- No. 3 ignition coil IGN03 line short to ground

- No. 3 ignition coil IGN03 line short to power

- No. 3 ignition coil IGN03 line open

DTC: P0354

- No. 4 ignition coil IGN04 line short to ground

- No. 4 ignition coil IGN04 line short to power

- No. 4 ignition coil IGN04 line open

Common

- Ignition coil internal circuit failure

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

## Chunk 5470: DTC P0351, P0352, P0353, P0354 (K20C1) (2019 2020 2021)

- Title: DTC P0351, P0352, P0353, P0354 (K20C1) (2019 2020 2021)
- Source path: `pages\6647.html`
- Chunk ID: `chunk_b5997353c105`
- Images: `images\GHH402965.jpeg`
- Duplicate sources: `pages\8234.html`, `pages\23038.html`, `pages\21451.html`

### Full Text

````text
# DTC P0351, P0352, P0353, P0354 (K20C1) (2019 2020 2021)

DTC P0351: No. 1 Cylinder Ignition Coil Circuit Malfunction

DTC P0352: No. 2 Cylinder Ignition Coil Circuit Malfunction

DTC P0353: No. 3 Cylinder Ignition Coil Circuit Malfunction

DTC P0354: No. 4 Cylinder Ignition Coil Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The power stage of each ignition coil is connected to a dedicated ignition driver module which is built into the powertrain control module (PCM). The PCM identifies short circuits and open circuit. The diagnosis of lines are done every 2 rotations of crankshaft. If the ignition coil output is out of a normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 680 rpm | -

12 volt battery voltage [Battery] | 8 V | -

[ ]: HDS Parameter

Malfunction Threshold

- Open circuit The ignition coil output current is less than 1 mA when the high side switch is active.

The ignition coil output current is less than 1 mA when the high side switch is active.

- Short circuit to power The ignition coil output voltage is more than 5 V when the power stage is on.

The ignition coil output voltage is more than 5 V when the power stage is on.

- Short circuit to ground The ignition coil output current is more than 30 mA when the power stage is on.

The ignition coil output current is more than 30 mA when the power stage is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0351

- No. 1 ignition coil IGN01 line short to ground

- No. 1 ignition coil IGN01 line short to power

- No. 1 ignition coil IGN01 line open

DTC: P0352

- No. 2 ignition coil IGN02 line short to ground

- No. 2 ignition coil IGN02 line short to power

- No. 2 ignition coil IGN02 line open

DTC: P0353

- No. 3 ignition coil IGN03 line short to ground

- No. 3 ignition coil IGN03 line short to power

- No. 3 ignition coil IGN03 line open

DTC: P0354

- No. 4 ignition coil IGN04 line short to ground

- No. 4 ignition coil IGN04 line short to power

- No. 4 ignition coil IGN04 line open

Common

- Ignition coil internal circuit failure

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

## Chunk 5471: DTC P0351, P0352, P0353, P0354 (K20C2)

- Title: DTC P0351, P0352, P0353, P0354 (K20C2)
- Source path: `pages\6648.html`
- Chunk ID: `chunk_9f7b3b15ec69`
- Images: `images\GHH402966.jpeg`
- Duplicate sources: `pages\8235.html`, `pages\23039.html`, `pages\21452.html`

### Full Text

````text
# DTC P0351, P0352, P0353, P0354 (K20C2)

DTC P0351: No. 1 Cylinder Ignition Coil Circuit Malfunction

DTC P0352: No. 2 Cylinder Ignition Coil Circuit Malfunction

DTC P0353: No. 3 Cylinder Ignition Coil Circuit Malfunction

DTC P0354: No. 4 Cylinder Ignition Coil Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The ignition coil is triggered at the optimum time by the powertrain control module (PCM) ON/OFF command. The PCM detects a malfunction when the engine is running and the return signal does not change for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more (when the engine speed is 700 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The return signal does not change for at least 5 seconds when the ignition coil is triggered.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0351

- No. 1 ignition coil IGN01 line open

- No. 1 ignition coil IGN01 line short to ground

DTC: P0352

- No. 2 ignition coil IGN02 line open

- No. 2 ignition coil IGN02 line short to ground

DTC: P0353

- No. 3 ignition coil IGN03 line open

- No. 3 ignition coil IGN03 line short to ground

DTC: P0354

- No. 4 ignition coil IGN04 line open

- No. 4 ignition coil IGN04 line short to ground

Common

- Ignition coil power supply line open

- Ignition coil ground line open

- Ignition coil internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5472: DTC P0351, P0352, P0353, P0354 (L15B7/L15BA)

- Title: DTC P0351, P0352, P0353, P0354 (L15B7/L15BA)
- Source path: `pages\6649.html`
- Chunk ID: `chunk_915ed08ea07d`
- Images: `images\GHH402967.jpeg`
- Duplicate sources: `pages\8236.html`, `pages\23040.html`, `pages\21453.html`

### Full Text

````text
# DTC P0351, P0352, P0353, P0354 (L15B7/L15BA)

DTC P0351: No. 1 Cylinder Ignition Coil Circuit Malfunction

DTC P0352: No. 2 Cylinder Ignition Coil Circuit Malfunction

DTC P0353: No. 3 Cylinder Ignition Coil Circuit Malfunction

DTC P0354: No. 4 Cylinder Ignition Coil Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The ignition coil is triggered at the optimum time by the powertrain control module (PCM) ON/OFF command. The PCM detects a malfunction when the engine is running and the return signal does not change for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more (when the engine speed is 700 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

The return signal does not change for at least 5 seconds when the ignition coil is triggered.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0351

- No. 1 ignition coil IGN01 line open

- No. 1 ignition coil IGN01 line short to ground

DTC: P0352

- No. 2 ignition coil IGN02 line open

- No. 2 ignition coil IGN02 line short to ground

DTC: P0353

- No. 3 ignition coil IGN03 line open

- No. 3 ignition coil IGN03 line short to ground

DTC: P0354

- No. 4 ignition coil IGN04 line open

- No. 4 ignition coil IGN04 line short to ground

Common

- Ignition coil power supply line open

- Ignition coil ground line open

- Ignition coil internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5473: DTC P0365 (K20C1) (2017 2018 2019)

- Title: DTC P0365 (K20C1) (2017 2018 2019)
- Source path: `pages\6650.html`
- Chunk ID: `chunk_9aee971f37ad`
- Images: `images\GHH402968.jpeg`
- Duplicate sources: `pages\8237.html`, `pages\23041.html`, `pages\21454.html`

### Full Text

````text
# DTC P0365 (K20C1) (2017 2018 2019)

DTC P0365: Camshaft Position (CMP) Sensor B Circuit Intermittent High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor B mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor B. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor B. If the powertrain control module (PCM) recognizes no signal from CMP sensor B, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.8 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Other | Crankshaft position (CKP) sensor signal with gap detected

Malfunction Threshold

If no signal from CMP sensor B is detected during a crankshaft revolution, a counter is incremented.

The number of consecutive unrecognized signals (counter) exceeds 8 times and the measured input level is less than 0.4 V, or greater than 2.4 V.

*: The counter resets to zero as soon as one or more new camshaft edges were acquired.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAMEX line short to ground

- CMP sensor B CAMEX line short to power

- CMP sensor B CAMEX line open

- CMP sensor B failure

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

## Chunk 5474: DTC P0365 (K20C1) (2019 2020 2021)

- Title: DTC P0365 (K20C1) (2019 2020 2021)
- Source path: `pages\6651.html`
- Chunk ID: `chunk_31b43f9dd3ca`
- Images: `images\GHH402969.jpeg`
- Duplicate sources: `pages\8238.html`, `pages\23042.html`, `pages\21455.html`

### Full Text

````text
# DTC P0365 (K20C1) (2019 2020 2021)

DTC P0365: Camshaft Position (CMP) Sensor B Circuit Intermittent High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor B mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor B. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor B. If the powertrain control module (PCM) recognizes no signal from CMP sensor B, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Both conditions occur:

- No camshaft signal is detected at least 8 crankshaft revolutions.

- The measured input level is less than 1.9 V, or more than 3.2 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAMEX line short to ground

- CMP sensor B CAMEX line short to power

- CMP sensor B CAMEX line open

- CMP sensor B failure

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

## Chunk 5475: DTC P0365 (K20C2)

- Title: DTC P0365 (K20C2)
- Source path: `pages\6652.html`
- Chunk ID: `chunk_42d3559e07a3`
- Images: `images\GHH402970.jpeg`
- Duplicate sources: `pages\8239.html`, `pages\23043.html`, `pages\21456.html`

### Full Text

````text
# DTC P0365 (K20C2)

DTC P0365: Camshaft Position (CMP) Sensor B Circuit No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B consists of a rotor and a semiconductor that detects rotor position. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). The PCM determines exhaust camshaft timing position according to the pulsing signals from CMP sensor B and the crankshaft position (CKP) sensor. If no CMP sensor B pulsing signals are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from CMP sensor B are detected while signals from the CKP sensor are detected at least 50 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAM line open

- CMP sensor B CAM line short to ground

- CMP sensor B VCC line open

- CMP sensor B SG line open

- CMP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5476: DTC P0365 (Without XM)

- Title: DTC P0365 (Without XM)
- Source path: `pages\6653.html`
- Chunk ID: `chunk_740463bbad31`
- Images: `images\GHH402971.jpeg`
- Duplicate sources: `pages\8240.html`, `pages\23044.html`, `pages\21457.html`

### Full Text

````text
# DTC P0365 (Without XM)

DTC P0365: Camshaft Position (CMP) Sensor B Circuit No Signal

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B consists of a rotor and a semiconductor that detects rotor position. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). The PCM determines exhaust camshaft timing position according to the pulsing signals from CMP sensor B and the crankshaft position (CKP) sensor. If no CMP sensor B pulsing signals are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 2 seconds or more (when the engine speed is 750 rpm)

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

No input signals from CMP sensor B are detected while signals from the CKP sensor are detected at least 50 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAM EX line open

- CMP sensor B CAM EX line short to ground

- CMP sensor B VCC line open

- CMP sensor B SG line open

- CMP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5477: DTC P0366 (K20C2)

- Title: DTC P0366 (K20C2)
- Source path: `pages\6654.html`
- Chunk ID: `chunk_497424d8fab7`
- Images: `images\GHH402972.jpeg`
- Duplicate sources: `pages\8241.html`, `pages\23045.html`, `pages\21458.html`

### Full Text

````text
# DTC P0366 (K20C2)

DTC P0366: Camshaft Position (CMP) Sensor B and Crankshaft Position (CKP) Sensor Incorrect Phase Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B detects the exhaust camshaft timing and sends pulsing signals to the powertrain control module (PCM). The PCM determines the advance or the retard of the exhaust camshaft timing according to the signals from the crankshaft position (CKP) sensor and CMP sensor B. If the exhaust camshaft reference phase value deviates from a set range over a specified time period while the variable valve timing control (VTC) is not activated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapse time after starting the engine | 1.0 second | -

Engine speed [ENGINE SPEED] | 500 rpm | -

Other | VTC system not operating

[ ]: HDS Parameter

Malfunction Threshold

The difference between exhaust camshaft phase measured from CMP sensor B and exhaust camshaft standard phase value according to the CKP sensor position is 10 deg. or more for at least 4.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator B stuck

- VTC actuator B phase deviation

- VTC oil control solenoid valve B stuck

- VTC actuator B failure (return spring cut)

- VTC system abnormal low oil pressure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle. When the diagnosis does not finish, allow the engine cool to an engine coolant temperature [ECT SENSOR 1] of ambient temperature, then restart the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5478: DTC P0366 (L15B7/L15BA/L15BY)

- Title: DTC P0366 (L15B7/L15BA/L15BY)
- Source path: `pages\6655.html`
- Chunk ID: `chunk_045f93630df4`
- Images: `images\GHH402973.jpeg`
- Duplicate sources: `pages\8242.html`, `pages\23046.html`, `pages\21459.html`

### Full Text

````text
# DTC P0366 (L15B7/L15BA/L15BY)

DTC P0366: Camshaft Position (CMP) Sensor B and Crankshaft Position (CKP) Sensor Incorrect Phase Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B detects the exhaust camshaft timing and sends pulsing signals to the powertrain control module (PCM). The PCM determines the advance or the retard of the exhaust camshaft timing according to the signals from the crankshaft position (CKP) sensor and CMP sensor B. If the exhaust camshaft reference phase value deviates from a set range over a specified time period while the variable valve timing control (VTC) is not activated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 4.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapse time after starting the engine | 1.0 second | -

Engine speed [ENGINE SPEED] | 500 rpm | -

Other | VTC system not operating

[ ]: HDS Parameter

Malfunction Threshold

The difference between exhaust camshaft phase measured from CMP sensor B and exhaust camshaft standard phase value according to the CKP sensor position is 10 deg. or more for at least 4.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- VTC actuator B stuck

- VTC actuator B phase deviation

- VTC oil control solenoid valve B stuck

- VTC actuator B failure (return spring cut)

- VTC system abnormal low oil pressure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle. When the diagnosis does not finish, allow the engine cool to an engine coolant temperature [ECT SENSOR 1] of ambient temperature, then restart the engine, and let it idle.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5479: DTC P0369 (K20C1) (2017 2018 2019)

- Title: DTC P0369 (K20C1) (2017 2018 2019)
- Source path: `pages\6656.html`
- Chunk ID: `chunk_928543976c90`
- Images: `images\GHH402974.jpeg`
- Duplicate sources: `pages\8243.html`, `pages\23047.html`, `pages\21460.html`

### Full Text

````text
# DTC P0369 (K20C1) (2017 2018 2019)

DTC P0369: Camshaft Position (CMP) Sensor B Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor B mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor B. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor B. The PCM compares the generated pulse pattern with a stored calibrated pulse pattern. If the compared pulse pattern does not match, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1.2 seconds or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Other | Crankshaft position (CKP) sensor signal with gap detected

Malfunction Threshold

Any of the conditions is met at least 12 times:

- The segment length is not equal to the reference length.

- The signal pattern does not match the calibrated pattern.

- Too many edge failures are detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Pulse plate defection

- CMP sensor B failure

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

## Chunk 5480: DTC P0369 (K20C1) (2019 2020 2021)

- Title: DTC P0369 (K20C1) (2019 2020 2021)
- Source path: `pages\6657.html`
- Chunk ID: `chunk_cb4b4473894f`
- Images: `images\GHH402975.jpeg`
- Duplicate sources: `pages\8244.html`, `pages\23048.html`, `pages\21461.html`

### Full Text

````text
# DTC P0369 (K20C1) (2019 2020 2021)

DTC P0369: Camshaft Position (CMP) Sensor B Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

The camshaft position sensoring operates based on pulse detection and counting. The fundamental components are a pulse plate mounted on the end of the shaft (rotary part) and camshaft position (CMP) sensor B mounted in line with the pulse plate including electronic circuitry (stationary part). Around the circumference of the pulse plate, there are teeth distributed evenly and additional reference markers. This makes it possible to generate an electric pulse pattern when the shaft rotates and the teeth are passing by CMP sensor B. The camshaft position can be determined by counting the number of pulses and deriving the pulse pattern of the electrical signal from CMP sensor B. The PCM compares the generated pulse pattern with a stored calibrated pulse pattern. If the compared pulse pattern does not match, a malfunction is detected and a DTC is stored.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

Any of the conditions is met at least 12 times:

- Camshaft signal has wrong segment length.

- Signal table and reference table have many similar entries but no unique matching was found.

- The latest segment is not in the reference table or it is out of the sequence.

- Too many edge failures are detected.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Pulse plate defection

- CMP sensor B failure

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

## Chunk 5481: DTC P0369 (K20C2)

- Title: DTC P0369 (K20C2)
- Source path: `pages\6658.html`
- Chunk ID: `chunk_058af1acf1a9`
- Images: `images\GHH402976.jpeg`
- Duplicate sources: `pages\8245.html`, `pages\23049.html`, `pages\21462.html`

### Full Text

````text
# DTC P0369 (K20C2)

DTC P0369: Camshaft Position (CMP) Sensor B Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B consists of a rotor and a semiconductor that detects rotor position. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). The PCM determines exhaust camshaft timing position according to the pulsing signals from CMP sensor B and the crankshaft position (CKP) sensor. If abnormal amount of pulsing signals from CMP sensor B are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects abnormal pulsing signals from CMP sensor B at least 60 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAM line electrical noise overlapped

- CMP sensor B rotor chipped

- CMP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5482: DTC P0369 (L15B7/L15BA)

- Title: DTC P0369 (L15B7/L15BA)
- Source path: `pages\6659.html`
- Chunk ID: `chunk_6bfe537e3758`
- Images: `images\GHH402977.jpeg`
- Duplicate sources: `pages\8246.html`, `pages\23050.html`, `pages\21463.html`

### Full Text

````text
# DTC P0369 (L15B7/L15BA)

DTC P0369: Camshaft Position (CMP) Sensor B Circuit Intermittent Interruption

General Description

Courtesy of HONDA, U.S.A., INC.

Camshaft position (CMP) sensor B consists of a rotor and a semiconductor that detects rotor position. When the rotor turns after starting the engine, the changes of magnetic flux in the semiconductor are converted into pulsing signals to the powertrain control module (PCM). The PCM determines exhaust camshaft timing position according to the pulsing signals from CMP sensor B and the crankshaft position (CKP) sensor. If abnormal amount of pulsing signals from CMP sensor B are detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed[ENGINE SPEED] | 400 rpm | -

[ ]: HDS Parameter

Malfunction Threshold

The PCM detects abnormal pulsing signals from CMP sensor B at least 60 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- CMP sensor B CAM EX line electrical noise overlapped

- CMP sensor B rotor chipped

- CMP sensor B failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5483: DTC P0420 (K20C1) (2017 2018 2019)

- Title: DTC P0420 (K20C1) (2017 2018 2019)
- Source path: `pages\6660.html`
- Chunk ID: `chunk_c809722a88aa`
- Images: `images\GHH402978.jpeg`, `images\GHH402979.jpeg`
- Duplicate sources: `pages\8247.html`, `pages\23051.html`, `pages\21464.html`

### Full Text

````text
# DTC P0420 (K20C1) (2017 2018 2019)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the catalyst system for low conversion efficiency. The catalyst conversion efficiency is determined by measuring the oxygen storage capacity (OSC). The measured OSC is normalized to the OSC of the best performing unacceptable (BPU) catalyst. To evaluate this parameter, air/fuel ratio (A/F) sensor (sensor 1) and secondary heated oxygen sensor (secondary HO2S (sensor 2)) are implemented on the side of the TWC. The oxygen stored by the catalytic converter during a lean mode operation is partly or completely used up in ensuing rich mode to oxidize the residual hydrocarbons, carbon monoxide, and nitrogen oxides. The OSC of the catalyst, and hence its oxidization efficiency, diminishes with age.When the enable conditions are met, the enrichment phase is started. This phase continues until the catalyst is purged of oxygen. When the exit conditions are met, the lean phase begins. During this phase, the OSC is measured. The oxygen storage is integrated until the secondary HO2S (sensor 2) voltage is less than a specified value. When the lean phase exit conditions are met, the diagnostics is evaluated. If the measured OSC is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 2 minutes or more

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

The number of OSC measurements is 3 or more and the averaged OSC value of the catalyst is less than 1.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC deterioration (aging, poisoning, and/or overtemperature)

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

## Chunk 5484: DTC P0420 (K20C1) (2019)

- Title: DTC P0420 (K20C1) (2019)
- Source path: `pages\6661.html`
- Chunk ID: `chunk_b0d67cb20f41`
- Images: `images\GHH402980.jpeg`, `images\GHH402981.jpeg`
- Duplicate sources: `pages\8248.html`, `pages\23052.html`, `pages\21465.html`

### Full Text

````text
# DTC P0420 (K20C1) (2019)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the catalyst system for low conversion efficiency. The catalyst conversion efficiency is determined by measuring the oxygen storage capacity (OSC). The measured OSC is normalized to the OSC of the best performing unacceptable (BPU) catalyst. To evaluate this parameter, air/fuel ratio (A/F) sensor (sensor 1) and secondary heated oxygen sensor (secondary HO2S (sensor 2)) are implemented on the side of the TWC. The oxygen stored by the catalytic converter during a lean mode operation is partly or completely used up in ensuing rich mode to oxidize the residual hydrocarbons, carbon monoxide, and nitrogen oxides. The OSC of the catalyst, and hence its oxidization efficiency, diminishes with age.When the enable conditions are met, the enrichment phase is started. This phase continues until the catalyst is purged of oxygen. When the exit conditions are met, the lean phase begins. During this phase, the OSC is measured. The oxygen storage is integrated until the secondary HO2S (sensor 2) voltage is less than a specified value. When the lean phase exit conditions are met, the diagnostics is evaluated. If the measured OSC is a specified value, the PCM detects a malfunction and stores a DTC.

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

The number of OSC measurements is 3 or more and the averaged OSC value of the catalyst is less than 1.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC deterioration (aging, poisoning, and/or overtemperature)

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

## Chunk 5485: DTC P0420 (K20C1) (2020 2021)

- Title: DTC P0420 (K20C1) (2020 2021)
- Source path: `pages\6662.html`
- Chunk ID: `chunk_08252714d75d`
- Images: `images\GHH402982.jpeg`, `images\GHH402983.jpeg`
- Duplicate sources: `pages\8249.html`, `pages\23053.html`, `pages\21466.html`

### Full Text

````text
# DTC P0420 (K20C1) (2020 2021)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the catalyst system for low conversion efficiency. The catalyst conversion efficiency is determined by measuring the oxygen storage capacity (OSC). The measured OSC is normalized to the OSC of the best performing unacceptable (BPU) catalyst. To evaluate this parameter, air/fuel ratio (A/F) sensor (sensor 1) and secondary heated oxygen sensor (secondary HO2S (sensor 2)) are implemented on the side of the TWC. The oxygen stored by the catalytic converter during a lean mode operation is partly or completely used up in ensuing rich mode to oxidize the residual hydrocarbons, carbon monoxide, and nitrogen oxides. The OSC of the catalyst, and hence its oxidization efficiency, diminishes with age.When the enable conditions are met, the enrichment phase is started. This phase continues until the catalyst is purged of oxygen. When the exit conditions are met, the lean phase begins. During this phase, the OSC is measured. The oxygen storage is integrated until the secondary HO2S (sensor 2) voltage is less than a specified value. When the lean phase exit conditions are met, the diagnostics is evaluated. If the measured OSC is a specified value, the PCM detects a malfunction and stores a DTC.

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

The number of OSC measurements is 3 or more and the averaged OSC value of the catalyst is less than 1.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC deterioration (aging, poisoning, and/or overtemperature)

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

## Chunk 5486: DTC P0420 (K20C2)

- Title: DTC P0420 (K20C2)
- Source path: `pages\6663.html`
- Chunk ID: `chunk_d3563f9e531b`
- Images: `images\GHH402984.jpeg`, `images\GHH402985.jpeg`
- Duplicate sources: `pages\8250.html`, `pages\23054.html`, `pages\21467.html`

### Full Text

````text
# DTC P0420 (K20C2)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

The three way catalytic converter (TWC) converts hydrocarbons (HC), carbon monoxide (CO), and oxides of nitrogen (NOx) in the exhaust gas to water vapor, carbon dioxide (CO 2), and dinitrogen (N 2). The powertrain control module (PCM) fluctuates the air/fuel ratio temporarily to detect the performance of the TWC and measures the degree of fluctuation in the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output. If the accumulated value for a set time is too great, deterioration of the performance of the catalyst is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 7.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time that secondary HO2S activity is not monitored after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT Sensor (1)] | -13 deg.F (-25 deg.C) | -

Estimated TWC temperature | 1, 040 deg.F (560 deg.C) | -

Vehicle speed [VEHICLE SPEED] | 26 mph (41 km/h) | -

Fuel trim | 0.69 | 1.47

Fuel feedback | Closed loop at stoichiometric

Monitoring priority | P0133, P219C, P219D, P219E, P219F

Other | Has record of deceleration at least once

Cruise load or more

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) fluctuation integration value is 3.0 V or more for at least 7.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC purification performance deterioration

- Secondary HO2S (sensor 2) line electrical noise overlapped

- Secondary HO2S (sensor 2) connector loose connection

- Exhaust system change (non-genuine part)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 45 - 75 mph (73 - 120 km/h) for at least 5 minutes, to warm up the TWC.

- Drive at a steady speed between 55 - 75 mph (88 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 3 through 4, four times.

- Set a vehicle speed [VEHICLE SPEED] of 55 mph (88 km/h) on the cruise control or equivalent, and drive for at least 68 seconds.

- After disconnecting the 12 volt battery, extend Driving Pattern step 6 to 4 minutes or longer.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5487: DTC P0420 (L15B7/L15BA/L15BY) (2016 2017 2018)

- Title: DTC P0420 (L15B7/L15BA/L15BY) (2016 2017 2018)
- Source path: `pages\6664.html`
- Chunk ID: `chunk_1701c1021cad`
- Images: `images\GHH402986.jpeg`, `images\GHH402987.jpeg`
- Duplicate sources: `pages\8251.html`, `pages\23055.html`, `pages\21468.html`

### Full Text

````text
# DTC P0420 (L15B7/L15BA/L15BY) (2016 2017 2018)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

The three way catalytic converter (TWC) converts hydrocarbons (HC), carbon monoxide (CO), and oxides of nitrogen (NOx) in the exhaust gas to water vapor, carbon dioxide (CO 2), and dinitrogen (N 2). The powertrain control module (PCM) fluctuates the air/fuel ratio temporarily to detect the performance of the TWC and measures the degree of fluctuation in the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output. If the accumulated value for a set time is too great, deterioration of the performance of the catalyst is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 7.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time that secondary HO2S activity is not monitored after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT sensor (1)] | -13 deg.F (-25 deg.C) | -

Estimated TWC temperature | 986 deg.F (530 deg.C) | -

Vehicle speed [VEHICLE SPEED] | 26 mph (41 km/h) | -

Fuel trim | 0.75 | 1.47

Fuel feedback | Closed loop at stoichiometric

Monitoring priority | P0133, P219C, P219D, P219E, P219F

Other | Has record of deceleration at least once

Cruise load or more

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) fluctuation integration value is 3.0 V or more for at least 7.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC purification performance deterioration

- Secondary HO2S (sensor 2) line electrical noise overlapped

- Secondary HO2S (sensor 2) connector loose connection

- Exhaust system change (non-genuine part)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 45 - 75 mph (73 - 120 km/h) for at least 5 minutes, to warm up the TWC.

- Drive at a steady speed between 55 - 75 mph (89 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 3 through 4, four times.

- Drive at steady speed 25 mph (40 km/h) or more for at least 68 seconds.

- After disconnecting the 12 volt battery, extend Driving Pattern step 6 to 4 minutes or longer.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5488: DTC P0420 (L15B7/L15BA/L15BY) (2019 2020 2021)

- Title: DTC P0420 (L15B7/L15BA/L15BY) (2019 2020 2021)
- Source path: `pages\6665.html`
- Chunk ID: `chunk_0c86ad4bdff3`
- Images: `images\GHH402988.jpeg`, `images\GHH402989.jpeg`
- Duplicate sources: `pages\8252.html`, `pages\23056.html`, `pages\21469.html`

### Full Text

````text
# DTC P0420 (L15B7/L15BA/L15BY) (2019 2020 2021)

DTC P0420: Catalyst System Efficiency Below Threshold

General Description

Courtesy of HONDA, U.S.A., INC.

The three way catalytic converter (TWC) converts hydrocarbons (HC), carbon monoxide (CO), and oxides of nitrogen (NOx) in the exhaust gas to water vapor, carbon dioxide (CO 2), and dinitrogen (N 2). The powertrain control module (PCM) fluctuates the air/fuel ratio temporarily to detect the performance of the TWC and measures the degree of fluctuation in the secondary heated oxygen sensor (secondary HO2S (sensor 2)) output. If the accumulated value for a set time is too great, deterioration of the performance of the catalyst is detected, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 7.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time that secondary HO2S activity is not monitored after starting the engine | 15 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 156 deg.F (69 deg.C) | -

Intake air temperature [IAT sensor (1)] | -13 deg.F (-25 deg.C) | -

Estimated TWC temperature* 1 | 1, 022 deg.F (550 deg.C) | -

Estimated TWC temperature* 2 | 986 deg.F (530 deg.C) | -

Vehicle speed [VEHICLE SPEED] | 26 mph (41 km/h) | -

Fuel trim | 0.75 | 1.47

Fuel feedback | Closed loop at stoichiometric

Monitoring priority | P0133, P219C, P219D, P219E, P219F

Other | Has record of deceleration at least once

Cruise load or more

*1: L15B7 (except Si), L15BY

*2: Si, L15BA[ ]: HDS Parameter

[ ]: HDS Parameter

Malfunction Threshold

The secondary HO2S (sensor 2) fluctuation integration value is 3.0 V or more for at least 7.5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- TWC purification performance deterioration

- Secondary HO2S (sensor 2) line electrical noise overlapped

- Secondary HO2S (sensor 2) connector loose connection

- Exhaust system change (non-genuine part)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Drive the vehicle at a speed between 45 - 75 mph (73 - 120 km/h) for at least 5 minutes, to warm up the TWC.

- Drive at a steady speed between 55 - 75 mph (89 - 120 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 3 through 4, four times.

- Drive at steady speed 25 mph (40 km/h) or more for at least 68 seconds.

- After disconnecting the 12 volt battery, extend Driving Pattern step 6 to 4 minutes or longer.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5489: DTC P0441 (K20C2) (2016 2017 2018)

- Title: DTC P0441 (K20C2) (2016 2017 2018)
- Source path: `pages\6666.html`
- Chunk ID: `chunk_3d6782f24c0b`
- Images: `images\GHH402990.jpeg`
- Duplicate sources: `pages\8253.html`, `pages\23057.html`, `pages\21470.html`

### Full Text

````text
# DTC P0441 (K20C2) (2016 2017 2018)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 19 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.69 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 19 seconds.

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

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5490: DTC P0441 (K20C2) (2019 2020 2021)

- Title: DTC P0441 (K20C2) (2019 2020 2021)
- Source path: `pages\6667.html`
- Chunk ID: `chunk_19f71f4fb16a`
- Images: `images\GHH402991.jpeg`
- Duplicate sources: `pages\8254.html`, `pages\23058.html`, `pages\21471.html`

### Full Text

````text
# DTC P0441 (K20C2) (2019 2020 2021)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 19 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24 inHg)

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.69 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 10.0 % or less for at least 19 seconds.

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

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5491: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\6668.html`
- Chunk ID: `chunk_2a115f157a98`
- Images: `images\GHH402992.jpeg`, `images\GHH402993.jpeg`
- Duplicate sources: `pages\8255.html`, `pages\23059.html`, `pages\21472.html`

### Full Text

````text
# DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 11 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 11 seconds.

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

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5492: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)

- Title: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2016 2017 2018 2019)
- Source path: `pages\6668.html`
- Chunk ID: `chunk_2b2eaa6afe3a`
- Images: `images\GHH402992.jpeg`, `images\GHH402993.jpeg`
- Duplicate sources: `pages\6910.html`, `pages\8255.html`, `pages\8497.html`, `pages\23059.html`, `pages\23003.html`, `pages\21472.html`, `pages\21416.html`

### Full Text

````text
t the engine. Hold the engine speed [ENGINE SPEED] at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

- Let the engine idle for at least 64 seconds.

- Drive the vehicle at high load for total of at least 11 seconds.

- Turn the vehicle to the OFF (LOCK) mode and leave the vehicle for at least 10 seconds.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5493: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6669.html`
- Chunk ID: `chunk_96de18379b3d`
- Images: `images\GHH402994.jpeg`, `images\GHH402995.jpeg`
- Duplicate sources: `pages\8256.html`, `pages\23060.html`, `pages\21473.html`

### Full Text

````text
# DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 11 seconds* 1 (9.5 seconds)* 2 or more

DTC Type | Two drive cycles, MIL on

*1: L15B7 (except Si) and L15BY

*2: L15BA

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 11 seconds* 1 (9.5 seconds)* 2.

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

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5494: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)

- Title: DTC P0441 (L15B7 (except Si)/L15BA/L15BY) (2020 2021)
- Source path: `pages\6669.html`
- Chunk ID: `chunk_5e2f51d9d4a6`
- Images: `images\GHH402994.jpeg`, `images\GHH402995.jpeg`
- Duplicate sources: `pages\8256.html`, `pages\23060.html`, `pages\21473.html`

### Full Text

````text
ensor output stuck

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

## Chunk 5495: DTC P0441 (Si) (2017 2018 2019)

- Title: DTC P0441 (Si) (2017 2018 2019)
- Source path: `pages\6670.html`
- Chunk ID: `chunk_b05961f3ba0e`
- Images: `images\GHH402996.jpeg`, `images\GHH402997.jpeg`
- Duplicate sources: `pages\8257.html`, `pages\23061.html`, `pages\21474.html`

### Full Text

````text
# DTC P0441 (Si) (2017 2018 2019)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 9.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 10 % or less for at least 9.5 seconds.

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

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC
````

## Chunk 5496: DTC P0441 (Si) (2017 2018 2019)

- Title: DTC P0441 (Si) (2017 2018 2019)
- Source path: `pages\6670.html`
- Chunk ID: `chunk_5916219c1c2f`
- Images: `images\GHH402996.jpeg`, `images\GHH402997.jpeg`
- Duplicate sources: `pages\6912.html`, `pages\8257.html`, `pages\8499.html`, `pages\23061.html`, `pages\23005.html`, `pages\21474.html`, `pages\21418.html`

### Full Text

````text
re

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

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5497: DTC P0441 (Si) (2020 2021)

- Title: DTC P0441 (Si) (2020 2021)
- Source path: `pages\6671.html`
- Chunk ID: `chunk_ac6c1058c83d`
- Images: `images\GHH402998.jpeg`, `images\GHH402999.jpeg`
- Duplicate sources: `pages\8258.html`, `pages\23062.html`, `pages\21475.html`

### Full Text

````text
# DTC P0441 (Si) (2020 2021)

DTC P0441: Evaporative Emission (EVAP) System Purge Flow Malfunction

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

Sequence | None

Duration | 9.5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Low load duration time | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] before EVAP purge control starts | 131 deg.F (55 deg.C) | -

MAP value [MAP SENSOR] | - | 81 kPa (610 mmHg, 24.0 inHg)

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Fuel trim | 0.75 | 1.47

EVAP canister purge valve duty [EVAP PC DUTY] | 30 % | 80 %

Fuel feedback | Closed loop at stoichiometric

[ ]: HDS Parameter

Malfunction Threshold

The pulses detected by the FTP sensor are 30 % or less for at least 9.5 seconds.

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

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5498: DTC P0441 (Si) (2020 2021)

- Title: DTC P0441 (Si) (2020 2021)
- Source path: `pages\6671.html`
- Chunk ID: `chunk_0ff6f4691063`
- Images: `images\GHH402998.jpeg`, `images\GHH402999.jpeg`
- Duplicate sources: `pages\8258.html`, `pages\23062.html`, `pages\21475.html`

### Full Text

````text
0 rpm without load (in neutral) until the radiator fan comes on.

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

## Chunk 5499: DTC P0442 (K20C1) (2017 2018 2019)

- Title: DTC P0442 (K20C1) (2017 2018 2019)
- Source path: `pages\6672.html`
- Chunk ID: `chunk_2e15112d4fc4`
- Images: `images\GHH403000.jpeg`, `images\GHH403001.jpeg`
- Duplicate sources: `pages\8259.html`, `pages\23063.html`, `pages\21476.html`

### Full Text

````text
# DTC P0442 (K20C1) (2017 2018 2019)

DTC P0442: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air.

Canister purging (P2422)

The EVAP system monitor diagnostic starts with the canister purging. During canister purging, the fuel tank pressure is monitored against low rationality threshold. If the fuel tank pressure reaches the threshold, then the EVAP canister purge valve is commanded closed. If the fuel tank pressure remains below, this threshold for calibrated amount of time after EVAP canister purge valve has been closed, then the powertrain control module (PCM) detects as EVAP canister vent shut valve stuck closed (P2422). If an EVAP canister vent shut valve stuck closed (P2422) is detected, the EVAP system monitor will be aborted.

Conditioning: Pressure stabilization after purging

The EVAP system monitor continues with the closing of the EVAP canister purge valve. The pressure in the fuel tank system is initially lower than the ambient pressure immediately after canister purging. Closing the EVAP canister purge valve causes ambient air to rush into the fuel tank system via the open EVAP canister vent shut valve. This results in a rise in the fuel tank pressure. If the pressure in the fuel tank does not stabilize within a calibrated amount of time, the EVAP system monitor will be aborted.

Phase A: Compensation gradient determination

The EVAP system monitor continues with the closure of the EVAP canister vent shut valve (EVAP canister purge valve remains closed). The pressure in the fuel tank system may rise further due to fuel evaporation. The gradient of the pressure signal is monitored during a calibrated amount of time. EVAP system monitor will be aborted if the gradient exceeds a calibrated threshold - high fuel evaporation. In the event that excessive fuel evaporation is not detected, the compensation gradient will be stored at the end of the observation period (phase A). This compensation gradient will be used at a later time to correct the leak gradient that is measured in phase C.

On the other side, if the pressure in fuel tank falls down below a calibrated rationality threshold, an EVAP canister purge valve stuck open (P0496) will be detected. If an EVAP canister purge valve stuck open (P0496) is detected, the EVAP system monitor will be aborted.

Phase B: EVAP canister purge valve low flow monitor and detection of large leaks

Phase B starts with the opening of the EVAP canister purge valve. The resulting change in the EVAP system pressure (vacuum build up) is monitored by the fuel tank pressure (FTP) sensor. If the resulting pressure does not drop below a calibrated threshold after a calibrated amount of time, an EVAP canister purge valve stuck closed (P0497) will be detected.

In spite of a properly functioning EVAP canister purge valve, the fuel tank pressure can begin to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected.
````

## Chunk 5500: DTC P0442 (K20C1) (2017 2018 2019)

- Title: DTC P0442 (K20C1) (2017 2018 2019)
- Source path: `pages\6672.html`
- Chunk ID: `chunk_be0e75403982`
- Images: `images\GHH403000.jpeg`, `images\GHH403001.jpeg`
- Duplicate sources: `pages\6702.html`, `pages\6727.html`, `pages\6728.html`, `pages\8259.html`, `pages\8289.html`, `pages\8314.html`, `pages\8315.html`, `pages\23063.html`, `pages\23093.html`, `pages\23118.html`, `pages\23119.html`, `pages\21476.html`, `pages\21506.html`, `pages\21531.html`, `pages\21532.html`

### Full Text

````text
to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected. If an EVAP canister purge valve stuck closed (P0497) or an EVAP system large leak (P0455) is detected, the EVAP system monitor will be aborted.

Phase C: Detection of 0.04 inch and 0.02 inch leaks

The monitor proceeds with small leak detection (0.04 inch) only if a large leak has not been detected. Phase C begins with the closing of the EVAP canister purge valve. Since the canister ventilation valve is still closed, the ensuing rise in pressure resulting from vaporization should be equivalent to the previously stored compensation gradient in phase B. If the vacuum decay gradient in the fuel tank (rise in pressure) exceeds a calibrated threshold, an EVAP system small leak (P0442) will be detected. If an EVAP system small leak (P0442) is detected, the EVAP system monitor will be aborted.

The diagnostic threshold for the 0.02 inch monitor is lower when compared with the corresponding threshold for the 0.04 inch test. A flag indicating a leak suspicion will be set if the vacuum decay gradient in the fuel tank (rise in pressure) exceeds the calibrated threshold. It should be stressed that this leak suspicion must be confirmed by an ensuing engine off natural vacuum (EONV) test. The EONV test complements the 0.02 inch leak test of the EVAP system monitor. It is triggered when the EVAP system monitor runs and indicates a 0.02 inch leak may be present in the EVAP system or independently of EVAP system monitor after the vehicle OFF (LOCK) mode.

EONV test

The EONV test detects a small leak in the EVAP system by evaluating the changes in pressure that occur in the fuel system. Heat from a running engine and from the engine exhaust gas, as well as a rise in ambient temperature and pressure all contribute to an increase in fuel temperature. The temperature and pressure in the fuel tank momentarily rises even further when the vehicle is brought to a halt and its engine turned off. This is due to the sudden absence of the cooling effect of the ambient air that opposes the forward motion of the vehicle. Temperature fluctuations contribute to relatively large pressure changes in a leak free EVAP system and cause little pressure changes if there is leakage in the EVAP system.

Phase 1

Phase 1 is executed while the temperature is still rising. A rise in temperature will lead to an increase in pressure in a tight fuel system. Between phase 1 and phase 2, the EVAP canister vent shut valve opens for a calibrated amount of time bleeding off any residual pressure.

Phase 2

Phase 2 is executed only when the pressure built in phase 1 does not reach levels that are typical of a tight fuel system. Phase 2 monitors the vacuum built when the fuel temperature is decreasing. Little or no vacuum is built if there is leakage in the system. For a leak free system, the vacuum build will reach a threshold that is determined by the ambient temperature and the fuel tank level.

If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 minutes | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -
````

## Chunk 5501: DTC P0442 (K20C1) (2017 2018 2019)

- Title: DTC P0442 (K20C1) (2017 2018 2019)
- Source path: `pages\6672.html`
- Chunk ID: `chunk_8ee8d1df6f6e`
- Images: `images\GHH403000.jpeg`, `images\GHH403001.jpeg`
- Duplicate sources: `pages\8259.html`, `pages\23063.html`, `pages\21476.html`

### Full Text

````text
If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

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

The fuel tank pressure vacuum decay gradient is greater than 0.035 kPa/s (0.27 mmHg/s, 0.0104 inHg/s) - 0.053 kPa/s (0.40 mmHg/s, 0.0157 inHg/s) while the EVAP canister purge valve and the EVAP vent shut valve are closed.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system small leak

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

## Chunk 5502: DTC P0442 (K20C1) (2019 2020 2021)

- Title: DTC P0442 (K20C1) (2019 2020 2021)
- Source path: `pages\6673.html`
- Chunk ID: `chunk_fbdce7c5bac2`
- Images: `images\GHH403002.jpeg`
- Duplicate sources: `pages\8260.html`, `pages\23064.html`, `pages\21477.html`

### Full Text

````text
# DTC P0442 (K20C1) (2019 2020 2021)

DTC P0442: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air. Several steps are taken to detect for leakage in the fuel supply system. If the vacuum decay gradient in the fuel tank is a specified value after the EVAP canister purge valve is closed, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

General enable conditions to trigger EVAP system monitor

Condition | Minimum | Maximum

Elapsed time after starting the engine | 9 minutes 10 seconds | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Condition | Minimum | Maximum

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 113 deg.F (45 deg.C)

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

Condition | Minimum | Maximum

FTP sensor | - | -15 hPa (-12 mmHg, -0.45 inHg)

Other | EVAP canister purge valve is commanded open

EVAP canister vent shut valve remains commanded closed

No large leakage fault was detected while vacuum build-up

Phase C: Observation of vacuum decay gradient in fuel tank after EVAP canister purge valve is closed

Condition

Other | EVAP canister purge valve is commanded closed

[ ]: HDS Parameter

Malfunction Threshold

The fuel tank pressure vacuum decay gradient is greater than 0.0349998 kPa/s (0.26252 mmHg/s, 0.01033544 inHg/s) - 0.0539994 kPa/s (0.4050279 mmHg/s, 0.01594602 inHg/s) while the EVAP canister purge valve is closed.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system small leak

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for a while.

- Stop the vehicle and let it idle for 10 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs.
````

## Chunk 5503: DTC P0442 (K20C1) (2019 2020 2021)

- Title: DTC P0442 (K20C1) (2019 2020 2021)
- Source path: `pages\6673.html`
- Chunk ID: `chunk_278250247938`
- Images: `images\GHH403002.jpeg`
- Duplicate sources: `pages\8260.html`, `pages\23064.html`, `pages\21477.html`

### Full Text

````text
a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system small leak

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

## Chunk 5504: DTC P0443 (K20C1) (2017 2018 2019)

- Title: DTC P0443 (K20C1) (2017 2018 2019)
- Source path: `pages\6674.html`
- Chunk ID: `chunk_0e561af45784`
- Images: `images\GHH403003.jpeg`
- Duplicate sources: `pages\8261.html`, `pages\23065.html`, `pages\21478.html`

### Full Text

````text
# DTC P0443 (K20C1) (2017 2018 2019)

DTC P0443: Evaporative Emission (EVAP) Canister Purge Valve Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister purge valve is attached to the vacuum port between the intake manifold and the EVAP canister. The powertrain control module (PCM) does not turn on the EVAP canister purge valve when the engine coolant temperature is less than a specified value. The PCM adjusts the amount of fuel vapor sent to the engine by controlling the EVAP canister purge valve duty cycle. The EVAP canister purge valve output current and voltage are monitored by the PCM. When the monitoring circuit detects other than normal range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16 V

[ ]: HDS Parameter

Malfunction Threshold

- Short circuit to power The EVAP canister purge valve output current exceeds 3 A for at least 0.06 second.

The EVAP canister purge valve output current exceeds 3 A for at least 0.06 second.

- Short circuit to ground The EVAP canister purge valve output voltage lies between 0 V and 2.7 V - 3.3 V while the output current lies between -0.1 and -0.3 A.

The EVAP canister purge valve output voltage lies between 0 V and 2.7 V - 3.3 V while the output current lies between -0.1 and -0.3 A.

- Open circuit The EVAP canister purge valve output voltage lies between 2.7 - 3.3 V and 4.5 V - 5.5 V.

The EVAP canister purge valve output voltage lies between 2.7 - 3.3 V and 4.5 V - 5.5 V.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve PCS line short to power

- EVAP canister purge valve PCS line short to ground

- EVAP canister purge valve PCS line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5505: DTC P0443 (K20C1) (2019 2020 2021)

- Title: DTC P0443 (K20C1) (2019 2020 2021)
- Source path: `pages\6675.html`
- Chunk ID: `chunk_cf897dd36bf5`
- Images: `images\GHH403004.jpeg`
- Duplicate sources: `pages\8262.html`, `pages\23066.html`, `pages\21479.html`

### Full Text

````text
# DTC P0443 (K20C1) (2019 2020 2021)

DTC P0443: Evaporative Emission (EVAP) Canister Purge Valve Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister purge valve is attached to the vacuum port between the intake manifold and the EVAP canister. The powertrain control module (PCM) does not turn on the EVAP canister purge valve when the engine coolant temperature is less than a specified value. The PCM adjusts the amount of fuel vapor sent to the engine by controlling the EVAP canister purge valve duty cycle. The EVAP canister purge valve output current and voltage are monitored by the PCM. When the monitoring circuit detects other than normal range for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Engine speed [Engine Speed] | 80 rpm | -

12 volt battery voltage [Battery] | 8 V | 16 V

Other | EVAP canister purge valve power stage on*

EVAP canister purge valve power stage off**

*: Short circuit to power detection**: Open circuit and short circuit to ground detections[ ]: HDS Parameter

Malfunction Threshold

- Short circuit to power The EVAP canister purge valve output current is 6 A or more for at least 0.5 second.

The EVAP canister purge valve output current is 6 A or more for at least 0.5 second.

- Short circuit to ground The EVAP canister purge valve output voltage is 2.74 V or less for at least 0.5 second.

The EVAP canister purge valve output voltage is 2.74 V or less for at least 0.5 second.

- Open circuit The EVAP canister purge valve output voltage is higher than 3.26 V, or 4.7 V or less for at least 0.5 second.

The EVAP canister purge valve output voltage is higher than 3.26 V, or 4.7 V or less for at least 0.5 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve PCS line short to power

- EVAP canister purge valve PCS line short to ground

- EVAP canister purge valve PCS line open

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5506: DTC P0443 (K20C2)

- Title: DTC P0443 (K20C2)
- Source path: `pages\6676.html`
- Chunk ID: `chunk_828dfe9d8595`
- Images: `images\GHH403005.jpeg`
- Duplicate sources: `pages\8263.html`, `pages\23067.html`, `pages\21480.html`

### Full Text

````text
# DTC P0443 (K20C2)

DTC P0443: Evaporative Emission (EVAP) Canister Purge Valve Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister purge valve is attached to the vacuum port between the intake manifold and the EVAP canister. The powertrain control module (PCM) does not turn on the EVAP canister purge valve when the engine coolant temperature is less than a specified value. The PCM adjusts the amount of fuel vapor sent to the engine by controlling the EVAP canister purge valve duty cycle. When the return signal does not change according to the EVAP canister purge valve output for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

EVAP canister purge valve output duty [EVAP PC DUTY] | 2 % | 98 %

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal does not change according to the EVAP canister purge valve output for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve PCS line open

- EVAP canister purge valve PCS line short to ground

- EVAP canister purge valve power supply line open

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

## Chunk 5507: DTC P0443 (L15B7/L15BA/L15BY)

- Title: DTC P0443 (L15B7/L15BA/L15BY)
- Source path: `pages\6677.html`
- Chunk ID: `chunk_2c74c2dafb57`
- Images: `images\GHH403006.jpeg`
- Duplicate sources: `pages\8264.html`, `pages\23068.html`, `pages\21481.html`

### Full Text

````text
# DTC P0443 (L15B7/L15BA/L15BY)

DTC P0443: Evaporative Emission (EVAP) Canister Purge Valve Circuit Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister purge valve is attached to the vacuum port between the intake manifold and the EVAP canister. The powertrain control module (PCM) does not turn on the EVAP canister purge valve when the engine coolant temperature is less than a specified value. The PCM adjusts the amount of fuel vapor sent to the engine by controlling the EVAP canister purge valve duty cycle. When the return signal does not change according to the EVAP canister purge valve output for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

EVAP canister purge valve output duty | 2 % | 98 %

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal does not change according to the EVAP canister purge valve output for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve IPV line open

- EVAP canister purge valve IPV line short to ground

- EVAP canister purge valve power supply line open

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

## Chunk 5508: DTC P0449 (K20C1) (2017 2018 2019)

- Title: DTC P0449 (K20C1) (2017 2018 2019)
- Source path: `pages\6678.html`
- Chunk ID: `chunk_ae3ab457faad`
- Images: `images\GHH403007.jpeg`
- Duplicate sources: `pages\8265.html`, `pages\23069.html`, `pages\21482.html`

### Full Text

````text
# DTC P0449 (K20C1) (2017 2018 2019)

DTC P0449: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Open

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is within a specified range while the EVAP canister vent shut valve is not actuated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output voltage is in the range of 3 V to 5 V for at least 0.5 second while the EVAP canister vent shut valve is not actuated.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve line open

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5509: DTC P0449 (K20C1) (2019 2020 2021)

- Title: DTC P0449 (K20C1) (2019 2020 2021)
- Source path: `pages\6679.html`
- Chunk ID: `chunk_2f07a63db458`
- Images: `images\GHH403008.jpeg`
- Duplicate sources: `pages\8266.html`, `pages\23070.html`, `pages\21483.html`

### Full Text

````text
# DTC P0449 (K20C1) (2019 2020 2021)

DTC P0449: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Open

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is within a specified range while the EVAP canister vent shut valve is not actuated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

Other | EVAP canister vent shut valve closed

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output voltage is in the range of 3.26 - 4.7 V while the power stage is off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve line open

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5510: DTC P0450 (K20C1) (2020 2021)

- Title: DTC P0450 (K20C1) (2020 2021)
- Source path: `pages\6680.html`
- Chunk ID: `chunk_a5ca28dffea8`
- Images: `images\GHH403009.jpeg`
- Duplicate sources: `pages\8267.html`, `pages\23071.html`, `pages\21484.html`

### Full Text

````text
# DTC P0450 (K20C1) (2020 2021)

DTC P0450: Fuel Tank Pressure (FTP) Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor provides information about the differential pressure of the fuel tank relative to atmospheric pressure. This sensor is required for the powertrain control module (PCM) to diagnose the evaporative emission (EVAP) system. The diagnosis of the FTP sensor consists of functional range check, circuit continuity check, and rationality check of the measured fuel tank pressure. The differential pressure value of the FTP sensor is compared with calibration thresholds to identify open and short circuit failures. If the fuel tank pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Multiple

Sequence | None

Duration | 10 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister vent shut valve is commanded open for at least 3 seconds

[ ]: HDS Parameter

Malfunction Threshold

The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor PTANK line short to power

- FTP sensor PTANK line short to ground

- FTP sensor PTANK line open

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5511: DTC P0450 (K20C2) (2019 2020 2021)

- Title: DTC P0450 (K20C2) (2019 2020 2021)
- Source path: `pages\6681.html`
- Chunk ID: `chunk_70d95d54b81b`
- Images: `images\GHH403010.jpeg`
- Duplicate sources: `pages\8268.html`, `pages\23072.html`, `pages\21485.html`

### Full Text

````text
# DTC P0450 (K20C2) (2019 2020 2021)

DTC P0450: Fuel Tank Pressure (FTP) Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure of the EVAP system. If the FTP sensor output voltage is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The FTP sensor output voltage is 3.62 V or more for at least 6 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5512: DTC P0450 (L15B7/L15BA/L15BY) (2019 2020 2021)

- Title: DTC P0450 (L15B7/L15BA/L15BY) (2019 2020 2021)
- Source path: `pages\6682.html`
- Chunk ID: `chunk_18f7ed01d813`
- Images: `images\GHH403011.jpeg`
- Duplicate sources: `pages\8269.html`, `pages\23073.html`, `pages\21486.html`

### Full Text

````text
# DTC P0450 (L15B7/L15BA/L15BY) (2019 2020 2021)

DTC P0450: Fuel Tank Pressure (FTP) Sensor Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure of the EVAP system. If the FTP sensor output voltage is a set value for a specified time, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The FTP sensor output voltage is 3.62 V or more for at least 6 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5513: DTC P0451 (K20C1) (2017 2018 2019)

- Title: DTC P0451 (K20C1) (2017 2018 2019)
- Source path: `pages\6683.html`
- Chunk ID: `chunk_5c1c01b6fcd2`
- Images: `images\GHH403012.jpeg`, `images\GHH403013.jpeg`, `images\GHH403014.jpeg`
- Duplicate sources: `pages\8270.html`, `pages\23074.html`, `pages\21487.html`

### Full Text

````text
# DTC P0451 (K20C1) (2017 2018 2019)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor provides information about the differential pressure of the fuel tank relative to atmospheric pressure. This sensor is required for the powertrain control module (PCM) to diagnose the evaporative emission (EVAP) system. The diagnosis of the FTP sensor consists of a circuit continuity check and various rationality checks of the measured fuel tank pressure.

Offset check

The signal offset test is used to detect a faulty FTP sensor that may be responding to changes in pressure, but have an offset in the signal output. Initially, the test occurs under conditions when the EVAP system has been isolated from the engine and is expected to have a reading near ambient pressure. This occurs when the EVAP canister purge valve has been closed and the EVAP canister vent shut valve is open, so that the expected differential pressure in the fuel tank system is near zero. If the fuel tank pressure is out of a calibrated range, then offset fault suspicion is set. To confirm FTP sensor offset, fault the plausibility check should be performed. Once fault suspicion is set, then purging phase should take place followed by a plausibility check. The plausibility check will confirm or deny the fault by comparing diagnostic results before and after canister purging.

Signal range check

The differential pressure value of the FTP sensor is compared with calibration thresholds to identify open and short circuit failures.

Incremental check

The incremental check measures the change of the fuel tank pressure caused by the purge mass flow while purge is enabled. Under normal conditions while changing the mass flow through the EVAP canister purge valve, the fuel tank pressure will also change. A sensor that has become stuck in range will cause this test to fail. During evaluation period while the enable conditions are fulfilled, the absolute change in the fuel tank pressure is monitored. To complete the test, the change of the purge mass flow must have also been sufficient. If the purge mass flow has been changed sufficiently without causing the required pressure change, a signal stuck error is detected.

Oscillation check

The oscillation check is designed to detect a pressure signal that is abnormally noisy. This type of sensor noise could potentially cause an incorrect leak detection diagnosis or even prevent the leak detection monitor from running. The oscillation check measures the amplitude and periodicity of the fuel tank pressure signal within an allotted evaluation period. Under normal conditions, the measured pressure signal should be relatively stable with pressure fluctuations less than a calibrated threshold. With the start of the check, two timers will begin to run. The first timer represents the overall evaluation period. The second timer represents an observation window and measures the amount of time the relative pressure signal is within the allotted pressure amplitude. This timer will reset to zero each time the relative pressure is greater than a calibrated amplitude threshold. The relative pressure is formed from a comparison between the current fuel tank pressure and the pressure that was stored at the last time the second timer was reset. If the pressure signal continues to fluctuate for the entire evaluation period, means no positive results are achieved, then a signal noise error is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, Continuous**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check

**: Signal range check, incremental check, and oscillation check

Enable Conditions

Offset check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -

Barometric pressure change within 2 minutes | - | 2 kPa (15 mmHg, 0.6 inHg)

Fuel tank pressure | -9.9976 kPa (-74.981 mmHg, -2.95202 inHg) | 9.9976 kPa (74.981 mmHg, 2.95202 inHg)

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | 62 mph (100 km/h)

Other | No refueling

[ ]: HDS Parameter

Signal range check

Condition | Minimum | Maximum
````

## Chunk 5514: DTC P0451 (K20C1) (2017 2018 2019)

- Title: DTC P0451 (K20C1) (2017 2018 2019)
- Source path: `pages\6683.html`
- Chunk ID: `chunk_0da43fc53420`
- Images: `images\GHH403012.jpeg`, `images\GHH403013.jpeg`, `images\GHH403014.jpeg`
- Duplicate sources: `pages\8270.html`, `pages\23074.html`, `pages\21487.html`

### Full Text

````text
nce, Duration, DTC Type

Execution | Once per driving cycle*, Continuous**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check

**: Signal range check, incremental check, and oscillation check

Enable Conditions

Offset check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -

Barometric pressure change within 2 minutes | - | 2 kPa (15 mmHg, 0.6 inHg)

Fuel tank pressure | -9.9976 kPa (-74.981 mmHg, -2.95202 inHg) | 9.9976 kPa (74.981 mmHg, 2.95202 inHg)

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | 62 mph (100 km/h)

Other | No refueling

[ ]: HDS Parameter

Signal range check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister purge valve is commanded open for at least 3 seconds

Incremental check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -

Fuel tank pressure | -2.5 kPa (-18 mmHg, -0.73 inHg) | 2.5 kPa (18 mmHg, 0.73 inHg)

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Other | EVAP canister purge valve is commanded open

Oscillation check

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed] | - | 18 mph (30 km/h)

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister purge valve is commanded open for at least 3 seconds

Malfunction Threshold

- Offset check When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 03 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 03 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less. - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

- - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- Signal range check The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

- Incremental check During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

- Oscillation check While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

Possible Cause
````

## Chunk 5515: DTC P0451 (K20C1) (2017 2018 2019)

- Title: DTC P0451 (K20C1) (2017 2018 2019)
- Source path: `pages\6683.html`
- Chunk ID: `chunk_1a16d72a2618`
- Images: `images\GHH403012.jpeg`, `images\GHH403013.jpeg`, `images\GHH403014.jpeg`
- Duplicate sources: `pages\8270.html`, `pages\23074.html`, `pages\21487.html`

### Full Text

````text
(45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

- Incremental check During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

- Oscillation check While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor drift

- FTP sensor not mounted

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle within the range of 10 - 62 mph (15 - 100 km/h).

- Stop the vehicle and let it idle for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5516: DTC P0451 (K20C1) (2019)

- Title: DTC P0451 (K20C1) (2019)
- Source path: `pages\6684.html`
- Chunk ID: `chunk_293871acbc5d`
- Images: `images\GHH403015.jpeg`, `images\GHH403016.jpeg`, `images\GHH403017.jpeg`
- Duplicate sources: `pages\8271.html`, `pages\23075.html`, `pages\21488.html`

### Full Text

````text
# DTC P0451 (K20C1) (2019)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor provides information about the differential pressure of the fuel tank relative to atmospheric pressure. This sensor is required for the powertrain control module (PCM) to diagnose the evaporative emission (EVAP) system. The diagnosis of the FTP sensor consists of functional range check, circuit continuity check, and rationality check of the measured fuel tank pressure.

Offset check

The signal offset test is used to detect a faulty FTP sensor that may be responding to changes in pressure, but have an offset in the signal output. Initially, the test occurs under conditions when the EVAP system has been isolated from the engine and is expected to have a reading near ambient pressure. This occurs when the EVAP canister purge valve has been closed and the EVAP canister vent shut valve is open, so that the expected differential pressure in the fuel tank system is near zero.

Offset error suspicion: The offset error is set if the absolute value of the fuel tank pressure is greater than calibrated value while EVAP canister purge valve is commanded closed. Once fault suspicion is set, then the purging phase should take place followed by a plausibility check.

Offset error plausibility check: The plausibility check compares diagnostic results before and after canister purging. Once fault suspicion is set, the purging phase will be triggered. The purging phase is followed by the plausibility check to confirm the fuel tank pressure offset fault. If the absolute difference between fuel tank pressure stored before and after purging phase is a calibrated value and the difference between fuel tank pressure stored before purging phase and its minimum stored value measured during canister purge phase is a calibrated value, an offset error is detected and the corresponding fault will be set.

Signal range check

The differential pressure value of the FTP sensor is compared with calibration thresholds to identify open and short circuit failures. If the fuel tank pressure is a specified value, the PCM detects a malfunction and stores a DTC.

Incremental check

The incremental check measures the change of the fuel tank pressure caused by the purge mass flow while purge is enabled. Under normal conditions while changing the mass flow through the EVAP canister purge valve, the fuel tank pressure will also change. A sensor that has become stuck in range will cause this test to fail. During evaluation period while the enable conditions are fulfilled, the absolute change in the fuel tank pressure is monitored. To complete the test, the change of the purge mass flow must have also been sufficient. If the purge mass flow has been changed sufficiently without causing the required pressure change, a signal stuck error is detected.

Oscillation check

The oscillation check is designed to detect a pressure signal that is abnormally noisy. This type of sensor noise could potentially cause an incorrect leak detection diagnosis or even prevent the leak detection monitor from running. The oscillation check measures the amplitude and periodicity of the fuel tank pressure signal within an allotted evaluation period. Under normal conditions, the measured pressure signal should be relatively stable with pressure fluctuations less than a calibrated threshold. With the start of the check, two timers will begin to run. The first timer represents the overall evaluation period. The second timer represents an observation window and measures the amount of time the relative pressure signal is within the allotted pressure amplitude. This timer will reset to zero each time the relative pressure is greater than a calibrated amplitude threshold. The relative pressure is formed from a comparison between the current fuel tank pressure and the pressure that was stored at the last time the second timer was reset. If the pressure signal continues to fluctuate for the entire evaluation period, means no positive results are achieved, then a signal noise error is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, multiple**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check
````

## Chunk 5517: DTC P0451 (K20C1) (2019)

- Title: DTC P0451 (K20C1) (2019)
- Source path: `pages\6684.html`
- Chunk ID: `chunk_683e36e9a1b5`
- Images: `images\GHH403015.jpeg`, `images\GHH403016.jpeg`, `images\GHH403017.jpeg`
- Duplicate sources: `pages\8271.html`, `pages\23075.html`, `pages\21488.html`

### Full Text

````text
period. The second timer represents an observation window and measures the amount of time the relative pressure signal is within the allotted pressure amplitude. This timer will reset to zero each time the relative pressure is greater than a calibrated amplitude threshold. The relative pressure is formed from a comparison between the current fuel tank pressure and the pressure that was stored at the last time the second timer was reset. If the pressure signal continues to fluctuate for the entire evaluation period, means no positive results are achieved, then a signal noise error is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, multiple**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check

**: Signal range check, incremental check, and oscillation check

Enable Conditions

Offset check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Barometric pressure change in 2 minutes | - | 2 kPa (15 mmHg, 0.6 inHg)

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | 62 mph (100 km/h)

Integrated mass flow | 9.99 g (0.3524 oz) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Other | No refueling

[ ]: HDS Parameter

Signal range check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister purge valve is commanded open for at least 3 seconds

Incremental check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Fuel tank pressure | -2.5 kPa (-18 mmHg, -0.73 inHg) | 2.5 kPa (18 mmHg, 0.73 inHg)

Condition | Minimum | Maximum

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Oscillation check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Vehicle speed [Vehicle Speed] | - | 18 mph (30 km/h)

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister purge valve is commanded open for at least 3 seconds

Malfunction Threshold

- Offset check When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 0.3 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 0.3 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less. - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

- - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- Signal range check The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.
````

## Chunk 5518: DTC P0451 (K20C1) (2019)

- Title: DTC P0451 (K20C1) (2019)
- Source path: `pages\6684.html`
- Chunk ID: `chunk_92741e3ba16e`
- Images: `images\GHH403015.jpeg`, `images\GHH403016.jpeg`, `images\GHH403017.jpeg`
- Duplicate sources: `pages\8271.html`, `pages\23075.html`, `pages\21488.html`

### Full Text

````text
bsolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

- - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- Signal range check The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

The fuel tank pressure is greater than 6 kPa (45 mmHg, 1.8 inHg) or less than -5 kPa (-38 mmHg, -1.5 inHg) for at least 10 seconds.

- Incremental check During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

- Oscillation check While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor drift

- FTP sensor not mounted

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle within the range of 10 - 62 mph (15 - 100 km/h).

- Stop the vehicle and let it idle for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5519: DTC P0451 (K20C1) (2020 2021)

- Title: DTC P0451 (K20C1) (2020 2021)
- Source path: `pages\6685.html`
- Chunk ID: `chunk_5e1f62d00e68`
- Images: `images\GHH403018.jpeg`, `images\GHH403019.jpeg`, `images\GHH403020.jpeg`
- Duplicate sources: `pages\8272.html`, `pages\23076.html`, `pages\21489.html`

### Full Text

````text
# DTC P0451 (K20C1) (2020 2021)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor provides information about the differential pressure of the fuel tank relative to atmospheric pressure. This sensor is required for the powertrain control module (PCM) to diagnose the evaporative emission (EVAP) system. The diagnosis of the FTP sensor consists of functional range check, circuit continuity check, and rationality check of the measured fuel tank pressure.

Offset check

The signal offset test is used to detect a faulty FTP sensor that may be responding to changes in pressure, but have an offset in the signal output. Initially, the test occurs under conditions when the EVAP system has been isolated from the engine and is expected to have a reading near ambient pressure. This occurs when the EVAP canister purge valve has been closed and the EVAP canister vent shut valve is open, so that the expected differential pressure in the fuel tank system is near zero.

Offset error suspicion: The offset error is set if the absolute value of the fuel tank pressure is greater than calibrated value while EVAP canister purge valve is commanded closed. Once fault suspicion is set, then the purging phase should take place followed by a plausibility check.

Offset error plausibility check: The plausibility check compares diagnostic results before and after canister purging. Once fault suspicion is set, the purging phase will be triggered. The purging phase is followed by the plausibility check to confirm the fuel tank pressure offset fault. If the absolute difference between fuel tank pressure stored before and after purging phase is a calibrated value and the difference between fuel tank pressure stored before purging phase and its minimum stored value measured during canister purge phase is a calibrated value, an offset error is detected and the corresponding fault will be set.

Incremental check

The incremental check measures the change of the fuel tank pressure caused by the purge mass flow while purge is enabled. Under normal conditions while changing the mass flow through the EVAP canister purge valve, the fuel tank pressure will also change. A sensor that has become stuck in range will cause this test to fail. During evaluation period while the enable conditions are fulfilled, the absolute change in the fuel tank pressure is monitored. To complete the test, the change of the purge mass flow must have also been sufficient. If the purge mass flow has been changed sufficiently without causing the required pressure change, a signal stuck error is detected.

Oscillation check

The oscillation check is designed to detect a pressure signal that is abnormally noisy. This type of sensor noise could potentially cause an incorrect leak detection diagnosis or even prevent the leak detection monitor from running. The oscillation check measures the amplitude and periodicity of the fuel tank pressure signal within an allotted evaluation period. Under normal conditions, the measured pressure signal should be relatively stable with pressure fluctuations less than a calibrated threshold. With the start of the check, two timers will begin to run. The first timer represents the overall evaluation period. The second timer represents an observation window and measures the amount of time the relative pressure signal is within the allotted pressure amplitude. This timer will reset to zero each time the relative pressure is greater than a calibrated amplitude threshold. The relative pressure is formed from a comparison between the current fuel tank pressure and the pressure that was stored at the last time the second timer was reset. If the pressure signal continues to fluctuate for the entire evaluation period, means no positive results are achieved, then a signal noise error is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, multiple**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check

**: Incremental check, and oscillation check

Enable Conditions

Offset check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)
````

## Chunk 5520: DTC P0451 (K20C1) (2020 2021)

- Title: DTC P0451 (K20C1) (2020 2021)
- Source path: `pages\6685.html`
- Chunk ID: `chunk_0e59828b52f6`
- Images: `images\GHH403018.jpeg`, `images\GHH403019.jpeg`, `images\GHH403020.jpeg`
- Duplicate sources: `pages\8272.html`, `pages\23076.html`, `pages\21489.html`

### Full Text

````text
alibrated amplitude threshold. The relative pressure is formed from a comparison between the current fuel tank pressure and the pressure that was stored at the last time the second timer was reset. If the pressure signal continues to fluctuate for the entire evaluation period, means no positive results are achieved, then a signal noise error is detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle*, multiple**

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

*: Offset check

**: Incremental check, and oscillation check

Enable Conditions

Offset check

Condition | Minimum | Maximum

Elapsed time after starting the engine | 1 second | -

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure change in 2 minutes | - | 2 kPa (15 mmHg, 0.6 inHg)

Vehicle speed [Vehicle Speed] | 10 mph (15 km/h) | 62 mph (100 km/h)

Integrated mass flow | 9.99 g (0.3524 oz) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Other | No refueling

[ ]: HDS Parameter

Incremental check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Fuel tank pressure | -2.5 kPa (-18 mmHg, -0.73 inHg) | 2.5 kPa (18 mmHg, 0.73 inHg)

Vehicle speed [Vehicle Speed] | 7 mph (10 km/h) | -

Fuel level | 0 L (0 US gal) | 41 L (10.8 US gal)

Oscillation check

Condition | Minimum | Maximum

Outside air temperature | 18.5 deg.F (-7.5 deg.C) | 103.6 deg.F (39.8 deg.C)

Vehicle speed [Vehicle Speed] | - | 18 mph (30 km/h)

Other | Engine running in idle

Other than during fuel cut-off operation

EVAP canister purge valve is commanded open for at least 3 seconds

Malfunction Threshold

- Offset check When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 0.3 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

When the absolute value of fuel tank pressure is greater than 1 kPa (8 mmHg, 0.3 inHg) while EVAP canister purge valve is commanded closed, an offset error suspicion is set. Once error suspicion is set, the purging phase is triggered. The DTC is confirmed if both of the following conditions occur.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less. - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- - The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

The absolute difference between the fuel tank pressure stored before and after purging phase is 0.05 kPa (0.3 mmHg, 0.014 inHg) or less.

- - The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

The difference between the fuel tank pressure stored before purging phase and its minimum stored value measured during EVAP canister purge phase is 0.1 kPa (1 mmHg, 0.03 inHg) or more.

- Incremental check During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

During EVAP canister purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

- Oscillation check While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor drift

- FTP sensor not mounted

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle within the range of 10 - 62 mph (15 - 100 km/h).
````

## Chunk 5521: DTC P0451 (K20C1) (2020 2021)

- Title: DTC P0451 (K20C1) (2020 2021)
- Source path: `pages\6685.html`
- Chunk ID: `chunk_5f40c8222e34`
- Images: `images\GHH403018.jpeg`, `images\GHH403019.jpeg`, `images\GHH403020.jpeg`
- Duplicate sources: `pages\8272.html`, `pages\23076.html`, `pages\21489.html`

### Full Text

````text
er purge valve actuating, the purge mass flow change was 2.5 kg/h (5.6 lbs/h) or more and fuel tank pressure change was less than 0.03 kPa (0.2 mmHg, 0.008 inHg) at the same time period.

- Oscillation check While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

While actuating EVAP canister purge valve, the purge mass flow change is 2.5 kg/h (5.6 lbs/h) or more within 10 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor drift

- FTP sensor not mounted

- FTP sensor failure

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle within the range of 10 - 62 mph (15 - 100 km/h).

- Stop the vehicle and let it idle for a while.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5522: DTC P0451 (K20C2) (2019 2020 2021)

- Title: DTC P0451 (K20C2) (2019 2020 2021)
- Source path: `pages\6686.html`
- Chunk ID: `chunk_4bf186ae0fe8`
- Images: `images\GHH403021.jpeg`, `images\GHH403022.jpeg`, `images\GHH403023.jpeg`, `images\GHH403024.jpeg`
- Duplicate sources: `pages\8273.html`, `pages\23077.html`, `pages\21490.html`

### Full Text

````text
# DTC P0451 (K20C2) (2019 2020 2021)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. Rapid changes in the FTP sensor output voltage due to electrical noise or an intermittent open during the EVAP leak detection may cause incorrect leak detection, so abnormal output is monitored. If the FTP sensor output voltage change occurs for specified ratio within a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 32 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

EVAP canister purge valve duty [EVAP PC DUTY] | Other than 0 %

Fuel feedback | During deceleration

Other | Other than purge-cut operation

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor output voltage fluctuation occurs for more than 96.0 % within the set time at least 32 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor electrical noise over lapped

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine, and let it idle until the radiator fan comes on.

- Drive the vehicle at a steady speed 35 mph (56 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 2 through 3, three times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5523: DTC P0451 (K20C2, KA/KC models) (2016 2017 2018)

- Title: DTC P0451 (K20C2, KA/KC models) (2016 2017 2018)
- Source path: `pages\6687.html`
- Chunk ID: `chunk_1c0064b9810e`
- Images: `images\GHH403025.jpeg`, `images\GHH403026.jpeg`, `images\GHH403027.jpeg`, `images\GHH403028.jpeg`
- Duplicate sources: `pages\8274.html`, `pages\23078.html`, `pages\21491.html`

### Full Text

````text
# DTC P0451 (K20C2, KA/KC models) (2016 2017 2018)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. Rapid changes in the FTP sensor output voltage due to electrical noise or an intermittent open during the EVAP leak detection may cause incorrect leak detection, so abnormal output is monitored. If the FTP sensor output voltage change occurs for specified ratio within a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 32 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

EVAP canister purge valve duty [EVAP PC DUTY] | Other than 0 %

Fuel feedback | During deceleration

Other | Other than purge-cut operation

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor output voltage fluctuation occurs for more than 30 % within the set time at least 32 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor electrical noise over lapped

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine, and let it idle until the radiator fan comes on.

- Drive the vehicle at a steady speed 35 mph (56 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 2 through 3, three times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5524: DTC P0451 (L15B7/L15BA)

- Title: DTC P0451 (L15B7/L15BA)
- Source path: `pages\6688.html`
- Chunk ID: `chunk_87cd0840ca2d`
- Images: `images\GHH403029.jpeg`, `images\GHH403030.jpeg`, `images\GHH403031.jpeg`, `images\GHH403032.jpeg`
- Duplicate sources: `pages\8275.html`, `pages\23079.html`, `pages\21492.html`

### Full Text

````text
# DTC P0451 (L15B7/L15BA)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. Rapid changes in the FTP sensor output voltage due to electrical noise or an intermittent open during the EVAP leak detection may cause incorrect leak detection, so abnormal output is monitored. If the FTP sensor output voltage change occurs for specified ratio within a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 32 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

EVAP canister purge valve duty [EVAP PC DUTY] | Other than 0 %

Fuel feedback | During deceleration

Other | Other than purge-cut operation

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor output voltage fluctuation occurs for more than 30 % within the set time at least 32 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor electrical noise over lapped

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine, and let it idle until the radiator fan comes on.

- Drive the vehicle at a steady speed 35 mph (56 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 2 through 3, three times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5525: DTC P0451(Si) (2017 2018 2019 2020 2021)

- Title: DTC P0451(Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6689.html`
- Chunk ID: `chunk_d0f88cde1f4b`
- Images: `images\GHH403033.jpeg`, `images\GHH403034.jpeg`, `images\GHH403035.jpeg`, `images\GHH403036.jpeg`
- Duplicate sources: `pages\8276.html`, `pages\23080.html`, `pages\21493.html`

### Full Text

````text
# DTC P0451(Si) (2017 2018 2019 2020 2021)

DTC P0451: Fuel Tank Pressure (FTP) Sensor Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. Rapid changes in the FTP sensor output voltage due to electrical noise or an intermittent open during the EVAP leak detection may cause incorrect leak detection, so abnormal output is monitored. If the FTP sensor output voltage change occurs for specified ratio within a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 32 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 seconds | -

Engine coolant temperature [ECT SENSOR 1] | 131 deg.F (55 deg.C) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

EVAP canister purge valve duty [EVAP PC DUTY] | Other than 0 %

Fuel feedback | During deceleration

Other | Other than purge-cut operation

[ ]: HDS Parameter

Malfunction Threshold

The FTP sensor output voltage fluctuation occurs for more than 96 % within the set time at least 32 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor electrical noise over lapped

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- Start the engine, and let it idle until the radiator fan comes on.

- Drive the vehicle at a steady speed 35 mph (56 km/h) for at least 10 seconds.

- Decelerate with the throttle valve fully closed.

- Repeat Driving Pattern steps 2 through 3, three times.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5526: DTC P0452 (K20C2) (2016 2017 2018)

- Title: DTC P0452 (K20C2) (2016 2017 2018)
- Source path: `pages\6690.html`
- Chunk ID: `chunk_4be88e2ee770`
- Images: `images\GHH403037.jpeg`, `images\GHH403038.jpeg`, `images\GHH403039.jpeg`
- Duplicate sources: `pages\8277.html`, `pages\23081.html`, `pages\21494.html`

### Full Text

````text
# DTC P0452 (K20C2) (2016 2017 2018)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage does not reach a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than -8 kPa (-55 mmHg, -2.2 inHg) for at least 3.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5527: DTC P0452 (K20C2) (2018 2019 2020 2021)

- Title: DTC P0452 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\6691.html`
- Chunk ID: `chunk_e9e41943ea0e`
- Images: `images\GHH403040.jpeg`, `images\GHH403041.jpeg`, `images\GHH403042.jpeg`
- Duplicate sources: `pages\8278.html`, `pages\23082.html`, `pages\21495.html`

### Full Text

````text
# DTC P0452 (K20C2) (2018 2019 2020 2021)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage does not reach a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than -8 kPa (-58 mmHg, -2.3 inHg) for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5528: DTC P0452 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P0452 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\6692.html`
- Chunk ID: `chunk_ef10f789fe2e`
- Images: `images\GHH403043.jpeg`, `images\GHH403044.jpeg`, `images\GHH403045.jpeg`
- Duplicate sources: `pages\8279.html`, `pages\23083.html`, `pages\21496.html`

### Full Text

````text
# DTC P0452 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage does not reach a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than -8 kPa (-58 mmHg, -2.3 inHg) for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5529: DTC P0452 (L15B7, KA/KC models) (2016 2017 2018)

- Title: DTC P0452 (L15B7, KA/KC models) (2016 2017 2018)
- Source path: `pages\6693.html`
- Chunk ID: `chunk_2d5df55fc976`
- Images: `images\GHH403046.jpeg`, `images\GHH403047.jpeg`, `images\GHH403048.jpeg`
- Duplicate sources: `pages\8280.html`, `pages\23084.html`, `pages\21497.html`

### Full Text

````text
# DTC P0452 (L15B7, KA/KC models) (2016 2017 2018)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage does not reach a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is less than -8 kPa (-55 mmHg, -2.2 inHg) for at least 3.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5530: DTC P0452 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0452 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6694.html`
- Chunk ID: `chunk_c36be005e626`
- Images: `images\GHH403049.jpeg`, `images\GHH403050.jpeg`, `images\GHH403051.jpeg`
- Duplicate sources: `pages\8281.html`, `pages\23085.html`, `pages\21498.html`

### Full Text

````text
# DTC P0452 (Si) (2017 2018 2019 2020 2021)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage does not reach a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is -8 kPa (-58 mmHg, -2.3 inHg) or less for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5531: DTC P0452, P0453 (K20C1) (2017 2018 2019)

- Title: DTC P0452, P0453 (K20C1) (2017 2018 2019)
- Source path: `pages\6695.html`
- Chunk ID: `chunk_8394e4ce6b0c`
- Images: `images\GHH403052.jpeg`
- Duplicate sources: `pages\8282.html`, `pages\23086.html`, `pages\21499.html`

### Full Text

````text
# DTC P0452, P0453 (K20C1) (2017 2018 2019)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. If the FTP sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P0452

The FTP sensor output voltage [FTP SENSOR] is lower than 0.1172 V for at least 0.5 second.

DTC: P0453

The FTP sensor output voltage [FTP SENSOR] is greater than 4.8486 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0452

- FTP sensor line short to ground

DTC: P0453

- FTP sensor line short to power

Common

- FTP sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5532: DTC P0452, P0453 (K20C1) (2019 2020 2021)

- Title: DTC P0452, P0453 (K20C1) (2019 2020 2021)
- Source path: `pages\6696.html`
- Chunk ID: `chunk_ad81e6219a81`
- Images: `images\GHH403053.jpeg`
- Duplicate sources: `pages\8283.html`, `pages\23087.html`, `pages\21500.html`

### Full Text

````text
# DTC P0452, P0453 (K20C1) (2019 2020 2021)

DTC P0452: Fuel Tank Pressure (FTP) Sensor Circuit Low Voltage

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. If the FTP sensor output voltage is a specified value for a specified time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Malfunction Threshold

DTC: P0452

The FTP sensor output voltage [FTP SENSOR] is lower than 0.12 V for at least 0.5 second.

DTC: P0453

The FTP sensor output voltage [FTP SENSOR] is greater than 4.85 V for at least 0.5 second.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0452

- FTP sensor PTANK line short to ground

- FTP sensor VCC line open

DTC: P0453

- FTP sensor PTANK line short to power

- FTP sensor PTANK line open

- FTP sensor SG line open

Common

- FTP sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5533: DTC P0453 (K20C2) (2016 2017 2018)

- Title: DTC P0453 (K20C2) (2016 2017 2018)
- Source path: `pages\6697.html`
- Chunk ID: `chunk_27ad5a0e899c`
- Images: `images\GHH403054.jpeg`, `images\GHH403055.jpeg`, `images\GHH403056.jpeg`
- Duplicate sources: `pages\8284.html`, `pages\23088.html`, `pages\21501.html`

### Full Text

````text
# DTC P0453 (K20C2) (2016 2017 2018)

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage is higher than a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is more than 8 kPa (55 mmHg, 2.2 inHg) for at least 3.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5534: DTC P0453 (K20C2) (2018 2019 2020 2021)

- Title: DTC P0453 (K20C2) (2018 2019 2020 2021)
- Source path: `pages\6698.html`
- Chunk ID: `chunk_c55a3fa37c53`
- Images: `images\GHH403057.jpeg`, `images\GHH403058.jpeg`, `images\GHH403059.jpeg`
- Duplicate sources: `pages\8285.html`, `pages\23089.html`, `pages\21502.html`

### Full Text

````text
# DTC P0453 (K20C2) (2018 2019 2020 2021)

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage is higher than a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is more than 4 kPa (28 mmHg, 1.1 inHg) for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5535: DTC P0453 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

- Title: DTC P0453 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)
- Source path: `pages\6699.html`
- Chunk ID: `chunk_cd2c256da70a`
- Images: `images\GHH403060.jpeg`, `images\GHH403061.jpeg`, `images\GHH403062.jpeg`
- Duplicate sources: `pages\8286.html`, `pages\23090.html`, `pages\21503.html`

### Full Text

````text
# DTC P0453 (L15B7 (except Si)/L15BA/L15BY) (2018 2019 2020 2021)

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage is higher than a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is more than 4 kPa (28 mmHg, 1.1 inHg) for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5536: DTC P0453 (L15B7/L15BA) (2016 2017 2018)

- Title: DTC P0453 (L15B7/L15BA) (2016 2017 2018)
- Source path: `pages\6700.html`
- Chunk ID: `chunk_e5fdc82a5de5`
- Images: `images\GHH403063.jpeg`, `images\GHH403064.jpeg`, `images\GHH403065.jpeg`
- Duplicate sources: `pages\8287.html`, `pages\23091.html`, `pages\21504.html`

### Full Text

````text
# DTC P0453 (L15B7/L15BA) (2016 2017 2018)

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage is higher than a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 3.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is more than 8 kPa (55 mmHg, 2.2 inHg) for at least 3.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5537: DTC P0453 (Si) (2017 2018 2019 2020 2021)

- Title: DTC P0453 (Si) (2017 2018 2019 2020 2021)
- Source path: `pages\6701.html`
- Chunk ID: `chunk_ec7afaf09016`
- Images: `images\GHH403066.jpeg`, `images\GHH403067.jpeg`, `images\GHH403068.jpeg`
- Duplicate sources: `pages\8288.html`, `pages\23092.html`, `pages\21505.html`

### Full Text

````text
# DTC P0453 (Si) (2017 2018 2019 2020 2021)

DTC P0453: Fuel Tank Pressure (FTP) Sensor Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The fuel tank pressure (FTP) sensor is installed on the evaporative emission (EVAP) canister and detects the fuel tank pressure. The FTP sensor is used to detect leaks in the EVAP system. The powertrain control module (PCM) monitors the FTP sensor output voltage. The FTP sensor output voltage rises as the fuel tank pressure increases. Conversely, the FTP sensor output voltage drops as the fuel tank pressure decreases. If the FTP sensor output voltage is higher than a target value for a set time after starting the engine in a cold condition, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 5.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 2.0 seconds | -

Other | At idle

Malfunction Threshold

The output from the FTP sensor [FTP SENSOR] is 4 kPa (28 mmHg, 1.1 inHg) or more for at least 5.0 seconds.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- FTP sensor line open

- FTP sensor line short

Confirmation Procedure

Operating Condition

Start the engine in a cold condition, and let it idle until the radiator fan comes on.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5538: DTC P0455 (K20C1) (2017 2018 2019)

- Title: DTC P0455 (K20C1) (2017 2018 2019)
- Source path: `pages\6702.html`
- Chunk ID: `chunk_3e84620da8ea`
- Images: `images\GHH403069.jpeg`, `images\GHH403070.jpeg`
- Duplicate sources: `pages\8289.html`, `pages\23093.html`, `pages\21506.html`

### Full Text

````text
# DTC P0455 (K20C1) (2017 2018 2019)

DTC P0455: Evaporative Emission (EVAP) System Large Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air.

Canister purging (P2422)

The EVAP system monitor diagnostic starts with the canister purging. During canister purging, the fuel tank pressure is monitored against low rationality threshold. If the fuel tank pressure reaches the threshold, then the EVAP canister purge valve is commanded closed. If the fuel tank pressure remains below, this threshold for calibrated amount of time after EVAP canister purge valve has been closed, then the powertrain control module (PCM) detects as EVAP canister vent shut valve stuck closed (P2422). If an EVAP canister vent shut valve stuck closed (P2422) is detected, the EVAP system monitor will be aborted.

Conditioning: Pressure stabilization after purging

The EVAP system monitor continues with the closing of the EVAP canister purge valve. The pressure in the fuel tank system is initially lower than the ambient pressure immediately after canister purging. Closing the EVAP canister purge valve causes ambient air to rush into the fuel tank system via the open EVAP canister vent shut valve. This results in a rise in the fuel tank pressure. If the pressure in the fuel tank does not stabilize within a calibrated amount of time, the EVAP system monitor will be aborted.

Phase A: Compensation gradient determination

The EVAP system monitor continues with the closure of the EVAP canister vent shut valve (EVAP canister purge valve remains closed). The pressure in the fuel tank system may rise further due to fuel evaporation. The gradient of the pressure signal is monitored during a calibrated amount of time. EVAP system monitor will be aborted if the gradient exceeds a calibrated threshold - high fuel evaporation. In the event that excessive fuel evaporation is not detected, the compensation gradient will be stored at the end of the observation period (phase A). This compensation gradient will be used at a later time to correct the leak gradient that is measured in phase C.

On the other side, if the pressure in fuel tank falls down below a calibrated rationality threshold, an EVAP canister purge valve stuck open (P0496) will be detected. If an EVAP canister purge valve stuck open (P0496) is detected, the EVAP system monitor will be aborted.

Phase B: EVAP canister purge valve low flow monitor and detection of large leaks

Phase B starts with the opening of the EVAP canister purge valve. The resulting change in the EVAP system pressure (vacuum build up) is monitored by the fuel tank pressure (FTP) sensor. If the resulting pressure does not drop below a calibrated threshold after a calibrated amount of time, an EVAP canister purge valve stuck closed (P0497) will be detected.

In spite of a properly functioning EVAP canister purge valve, the fuel tank pressure can begin to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected.
````

## Chunk 5539: DTC P0455 (K20C1) (2017 2018 2019)

- Title: DTC P0455 (K20C1) (2017 2018 2019)
- Source path: `pages\6702.html`
- Chunk ID: `chunk_fa10f76e8b26`
- Images: `images\GHH403069.jpeg`, `images\GHH403070.jpeg`
- Duplicate sources: `pages\8289.html`, `pages\23093.html`, `pages\21506.html`

### Full Text

````text
If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

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

Either of the conditions occurs and should be driven at least 0.2 miles (300 m) with no refueling event has been detected:

- The integrated purge mass flow is greater than 1.96007 g (0.0691395 oz) - 2.2 g (0.078 oz) and the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -1 kPa (-7 mmHg, -0.2 inHg).

- The integrated purge mass flow is greater than 4 g (0.15 oz) and the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -1.5 kPa (-11 mmHg, -0.44 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system large leak

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

## Chunk 5540: DTC P0455 (K20C1) (2019 2020 2021)

- Title: DTC P0455 (K20C1) (2019 2020 2021)
- Source path: `pages\6703.html`
- Chunk ID: `chunk_b6586c6fd190`
- Images: `images\GHH403071.jpeg`
- Duplicate sources: `pages\8290.html`, `pages\23094.html`, `pages\21507.html`

### Full Text

````text
# DTC P0455 (K20C1) (2019 2020 2021)

DTC P0455: Evaporative Emission (EVAP) System Large Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air. Several steps are taken to detect for leakage in the fuel supply system. If the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is a specified value during vacuum build-up, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

General enable conditions to trigger EVAP system monitor

Condition | Minimum | Maximum

Elapsed time after starting the engine | 9 minutes 10 seconds | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Condition | Minimum | Maximum

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 113 deg.F (45 deg.C)

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

Other | EVAP canister vent shut valve is commanded open

EVAP canister purge valve stuck in open position has not been detected

No high evaporation condition

No condensation condition

Phase B: Vacuum build-up

Condition | Minimum | Maximum

FTP sensor | - | -15 hPa (-12 mmHg, -0.45 inHg)

Other | EVAP canister purge valve is commanded open

EVAP canister vent shut valve remains commanded closed

No large leakage fault was detected while vacuum build-up

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occurs and should be driven at least 0.2 miles (300 m) with no refueling event has been detected:

- The integrated purge mass flow is greater than 1.96007 g (0.0691395 oz) - 2.2 g (0.078 oz) and the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -1 kPa (-7 mmHg, -0.2 inHg).

- The integrated purge mass flow is greater than 4 g (0.15 oz) and the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -1.5 kPa (-11 mmHg, -0.44 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system large leak

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for a while.

- Stop the vehicle and let it idle for 10 minutes.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory.
````

## Chunk 5541: DTC P0455 (K20C1) (2019 2020 2021)

- Title: DTC P0455 (K20C1) (2019 2020 2021)
- Source path: `pages\6703.html`
- Chunk ID: `chunk_c4b68daf5a2b`
- Images: `images\GHH403071.jpeg`
- Duplicate sources: `pages\8290.html`, `pages\23094.html`, `pages\21507.html`

### Full Text

````text
nHg).

- The integrated purge mass flow is greater than 4 g (0.15 oz) and the difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -1.5 kPa (-11 mmHg, -0.44 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system large leak

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

## Chunk 5542: DTC P0455 (K20C2)

- Title: DTC P0455 (K20C2)
- Source path: `pages\6704.html`
- Chunk ID: `chunk_43f4b1564b58`
- Images: `images\GHH403072.jpeg`, `images\GHH403073.jpeg`, `images\GHH403074.jpeg`
- Duplicate sources: `pages\8291.html`, `pages\23095.html`, `pages\21508.html`

### Full Text

````text
# DTC P0455 (K20C2)

DTC P0455: Evaporative Emission (EVAP) System Large Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Judgment of detection of 0.09 inch leak as normal operation

Judgment 2: Judgment of detection of 0.02 inch leak as normal operation

Judgment 3: Detection of 0.02 inch leak

<Judgments 1, 2, and 3 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect "no 0.09 inch leak" depending on the variation of the pressure inside the fuel tank.

- If the variation of the pressure is a specified value or more before first monitoring duration has passed, it is identified as normal and the diagnosis completes.

- If the variation of the pressure is less than a specified value for a specified duration after first monitoring duration has passed, it is identified as a "0.09 inch leak" and the diagnosis completes. (P0455)

- If the variation of the pressure is a specified value or more before maximum monitoring duration has passed, it is defined as "no 0.09 inch leak", the judgment of detection of a 0.09 inch leak is completed, and it goes to 0.02 inch leak monitor.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure decrease gradient inside the fuel tank.

- If a "0.02 inch leak" is detected, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no 0.02 inch leak" is detected, it is identified as normal; the diagnosis is completed.

- If the pressure is not atmospheric pressure or less when the detection is completed, Judgment 2 is suspended and determines the judgment by result of Judgment 3.

Judgment 3:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure increase gradient inside the fuel tank.

- If "no leakage" is detected and Judgment 2 is suspended, it is identified as normal; the diagnosis is completed.

- If a "0.02 inch leak" is detected and Judgment 2 is suspended, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no leakage" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as normal without waiting the result of Judgment 2; the diagnosis is completed.

- If a "0.02 inch leak" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as a malfunction without waiting the result of Judgment 2; the diagnosis is completed. (P0456)

- If the pressure of the fuel tank does not increase to a specified value or more within a specified duration, the judgment is suspended.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | At least 7 minutes 45 seconds but not more than 36 minutes 40 seconds

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped
````

## Chunk 5543: DTC P0455 (K20C2)

- Title: DTC P0455 (K20C2)
- Source path: `pages\6704.html`
- Chunk ID: `chunk_2c8c9e86d2ba`
- Images: `images\GHH403072.jpeg`, `images\GHH403073.jpeg`, `images\GHH403074.jpeg`
- Duplicate sources: `pages\8291.html`, `pages\23095.html`, `pages\21508.html`

### Full Text

````text
F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)][ ]: HDS Parameter

Malfunction Threshold

The variation of pressure inside the fuel tank is 0.015 kPa (0.12 mmHg, 0.004 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system leak (EVAP canister purge valve from fuel tank)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 28 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5544: DTC P0455 (L15B7/L15BA/L15BY)

- Title: DTC P0455 (L15B7/L15BA/L15BY)
- Source path: `pages\6705.html`
- Chunk ID: `chunk_b6b3df680dbc`
- Images: `images\GHH403075.jpeg`, `images\GHH403076.jpeg`, `images\GHH403077.jpeg`
- Duplicate sources: `pages\8292.html`, `pages\23096.html`, `pages\21509.html`

### Full Text

````text
# DTC P0455 (L15B7/L15BA/L15BY)

DTC P0455: Evaporative Emission (EVAP) System Large Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Judgment of detection of 0.09 inch leak as normal operation

Judgment 2: Judgment of detection of 0.02 inch leak as normal operation

Judgment 3: Detection of 0.02 inch leak

<Judgments 1, 2, and 3 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect "no 0.09 inch leak" depending on the variation of the pressure inside the fuel tank.

- If the variation of the pressure is a specified value or more before first monitoring duration has passed, it is identified as normal and the diagnosis completes.

- If the variation of the pressure is less than a specified value for a specified duration after first monitoring duration has passed, it is identified as a "0.09 inch leak" and the diagnosis completes. (P0455)

- If the variation of the pressure is a specified value or more before maximum monitoring duration has passed, it is defined as "no 0.09 inch leak", the judgment of detection of a 0.09 inch leak is completed, and it goes to 0.02 inch leak monitor.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure decrease gradient inside the fuel tank.

- If a "0.02 inch leak" is detected, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no 0.02 inch leak" is detected, it is identified as normal; the diagnosis is completed.

- If the pressure is not atmospheric pressure or less when the detection is completed, Judgment 2 is suspended and determines the judgment by result of Judgment 3.

Judgment 3:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure increase gradient inside the fuel tank.

- If "no leakage" is detected and Judgment 2 is suspended, it is identified as normal; the diagnosis is completed.

- If a "0.02 inch leak" is detected and Judgment 2 is suspended, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no leakage" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as normal without waiting the result of Judgment 2; the diagnosis is completed.

- If a "0.02 inch leak" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as a malfunction without waiting the result of Judgment 2; the diagnosis is completed. (P0456)

- If the pressure of the fuel tank does not increase to a specified value or more within a specified duration, the judgment is suspended.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | At least 7 minutes 45 seconds but not more than 36 minutes 40 seconds

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped
````

## Chunk 5545: DTC P0455 (L15B7/L15BA/L15BY)

- Title: DTC P0455 (L15B7/L15BA/L15BY)
- Source path: `pages\6705.html`
- Chunk ID: `chunk_50a4e5de3098`
- Images: `images\GHH403075.jpeg`, `images\GHH403076.jpeg`, `images\GHH403077.jpeg`
- Duplicate sources: `pages\8292.html`, `pages\23096.html`, `pages\21509.html`

### Full Text

````text
F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Malfunction Threshold

The variation of pressure inside the fuel tank is 0.015 kPa (0.12 mmHg, 0.004 inHg) or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system leak (EVAP canister purge valve from fuel tank)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 25 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5546: DTC P0456 (K20C1) (2017 2018 2019)

- Title: DTC P0456 (K20C1) (2017 2018 2019)
- Source path: `pages\6706.html`
- Chunk ID: `chunk_da04136ce0a3`
- Images: `images\GHH403078.jpeg`, `images\GHH403079.jpeg`
- Duplicate sources: `pages\8293.html`, `pages\23097.html`, `pages\21510.html`

### Full Text

````text
# DTC P0456 (K20C1) (2017 2018 2019)

DTC P0456: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air.

Canister purging (P2422)

The EVAP system monitor diagnostic starts with the canister purging. During canister purging, the fuel tank pressure is monitored against low rationality threshold. If the fuel tank pressure reaches the threshold, then the EVAP canister purge valve is commanded closed. If the fuel tank pressure remains below, this threshold for calibrated amount of time after EVAP canister purge valve has been closed, then the powertrain control module (PCM) detects as EVAP canister vent shut valve stuck closed (P2422). If an EVAP canister vent shut valve stuck closed (P2422) is detected, the EVAP system monitor will be aborted.

Conditioning: Pressure stabilization after purging

The EVAP system monitor continues with the closing of the EVAP canister purge valve. The pressure in the fuel tank system is initially lower than the ambient pressure immediately after canister purging. Closing the EVAP canister purge valve causes ambient air to rush into the fuel tank system via the open EVAP canister vent shut valve. This results in a rise in the fuel tank pressure. If the pressure in the fuel tank does not stabilize within a calibrated amount of time, the EVAP system monitor will be aborted.

Phase A: Compensation gradient determination

The EVAP system monitor continues with the closure of the EVAP canister vent shut valve (EVAP canister purge valve remains closed). The pressure in the fuel tank system may rise further due to fuel evaporation. The gradient of the pressure signal is monitored during a calibrated amount of time. EVAP system monitor will be aborted if the gradient exceeds a calibrated threshold - high fuel evaporation. In the event that excessive fuel evaporation is not detected, the compensation gradient will be stored at the end of the observation period (phase A). This compensation gradient will be used at a later time to correct the leak gradient that is measured in phase C.

On the other side, if the pressure in fuel tank falls down below a calibrated rationality threshold, an EVAP canister purge valve stuck open (P0496) will be detected. If an EVAP canister purge valve stuck open (P0496) is detected, the EVAP system monitor will be aborted.

Phase B: EVAP canister purge valve low flow monitor and detection of large leaks

Phase B starts with the opening of the EVAP canister purge valve. The resulting change in the EVAP system pressure (vacuum build up) is monitored by the fuel tank pressure (FTP) sensor. If the resulting pressure does not drop below a calibrated threshold after a calibrated amount of time, an EVAP canister purge valve stuck closed (P0497) will be detected.

In spite of a properly functioning EVAP canister purge valve, the fuel tank pressure can begin to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected.
````

## Chunk 5547: DTC P0456 (K20C1) (2017 2018 2019)

- Title: DTC P0456 (K20C1) (2017 2018 2019)
- Source path: `pages\6706.html`
- Chunk ID: `chunk_f1e64ad03603`
- Images: `images\GHH403078.jpeg`, `images\GHH403079.jpeg`
- Duplicate sources: `pages\8293.html`, `pages\23097.html`, `pages\21510.html`

### Full Text

````text
to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected. If an EVAP canister purge valve stuck closed (P0497) or an EVAP system large leak (P0455) is detected, the EVAP system monitor will be aborted.

Phase C: Detection of 0.04 inch and 0.02 inch leaks

The monitor proceeds with small leak detection (0.04 inch) only if a large leak has not been detected. Phase C begins with the closing of the EVAP canister purge valve. Since the canister ventilation valve is still closed, the ensuing rise in pressure resulting from vaporization should be equivalent to the previously stored compensation gradient in phase B. If the vacuum decay gradient in the fuel tank (rise in pressure) exceeds a calibrated threshold, an EVAP system small leak (P0442) will be detected. If an EVAP system small leak (P0442) is detected, the EVAP system monitor will be aborted.

The diagnostic threshold for the 0.02 inch monitor is lower when compared with the corresponding threshold for the 0.04 inch test. A flag indicating a leak suspicion will be set if the vacuum decay gradient in the fuel tank (rise in pressure) exceeds the calibrated threshold. It should be stressed that this leak suspicion must be confirmed by an ensuing engine off natural vacuum (EONV) test. The EONV test complements the 0.02 inch leak test of the EVAP system monitor. It is triggered when the EVAP system monitor runs and indicates a 0.02 inch leak may be present in the EVAP system or independently of EVAP system monitor after the vehicle OFF (LOCK) mode.

EONV test

The EONV test detects a small leak in the EVAP system by evaluating the changes in pressure that occur in the fuel system. Heat from a running engine and from the engine exhaust gas, as well as a rise in ambient temperature and pressure all contribute to an increase in fuel temperature. The temperature and pressure in the fuel tank momentarily rises even further when the vehicle is brought to a halt and its engine turned off. This is due to the sudden absence of the cooling effect of the ambient air that opposes the forward motion of the vehicle. Temperature fluctuations contribute to relatively large pressure changes in a leak free EVAP system and cause little pressure changes if there is leakage in the EVAP system.

Phase 1

Phase 1 is executed while the temperature is still rising. A rise in temperature will lead to an increase in pressure in a tight fuel system. Between phase 1 and phase 2, the EVAP canister vent shut valve opens for a calibrated amount of time bleeding off any residual pressure.

Phase 2

Phase 2 is executed only when the pressure built in phase 1 does not reach levels that are typical of a tight fuel system. Phase 2 monitors the vacuum built when the fuel temperature is decreasing. Little or no vacuum is built if there is leakage in the system. For a leak free system, the vacuum build will reach a threshold that is determined by the ambient temperature and the fuel tank level.

If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 minutes | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Barometric pressure [Baro Sensor] | 68 kPa (510 mmHg, 20.1 inHg) | -
````

## Chunk 5548: DTC P0456 (K20C1) (2017 2018 2019)

- Title: DTC P0456 (K20C1) (2017 2018 2019)
- Source path: `pages\6706.html`
- Chunk ID: `chunk_8967b3f3fedd`
- Images: `images\GHH403078.jpeg`, `images\GHH403079.jpeg`
- Duplicate sources: `pages\8293.html`, `pages\23097.html`, `pages\21510.html`

### Full Text

````text
If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | One drive cycle, MIL on

Enable Conditions

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

The difference between maximum and minimum fuel tank differential pressure is less than 0.5 kPa (3 mmHg, 0.14 inHg)) - 0.6 kPa (4 mmHg, 0.17 inHg).*

*: Maximum and minimum differential pressures are observable during phases 1 and 2, with minimum time (3 minutes 40 seconds) to wait between phases 1 and 2 to reach barometric pressure (EVAP vent shut valve is commanded open).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system very small leak

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

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5549: DTC P0456 (K20C1) (2019 2020 2021)

- Title: DTC P0456 (K20C1) (2019 2020 2021)
- Source path: `pages\6707.html`
- Chunk ID: `chunk_7acac1111960`
- Images: `images\GHH403080.jpeg`
- Duplicate sources: `pages\8294.html`, `pages\23098.html`, `pages\21511.html`

### Full Text

````text
# DTC P0456 (K20C1) (2019 2020 2021)

DTC P0456: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

EONV test

The EONV test detects a small leak in the evaporative emission (EVAP) system by evaluating the changes in pressure that occur in the fuel system. The monitor is divided into two phases.

Phase 1

Phase 1 is executed while the temperature is still rising. A rise in temperature will lead to an increase in pressure in a tight fuel system. Between phase 1 and phase 2, the EVAP canister vent shut valve opens for a calibrated amount of time bleeding off any residual pressure.

Phase 2

Phase 2 is executed only when the pressure built in phase 1 does not reach levels that are typical of a tight fuel system. Phase 2 monitors the vacuum built when the fuel temperature is decreasing. Little or no vacuum is built if there is leakage in the system. For a leak free system, the vacuum build will reach a threshold that is determined by the ambient temperature and the fuel tank level.

The cases below are all possible fuel tank pressure characteristics.

- Case A: The pressure of a leak free system reaches the calibrated target differential pressure. The diagnostic is immediately terminated (no phase 2) when this calibrated threshold for a leak free system is achieved.

- Case B: The tank pressure does not reach the target pressure but a maximum differential pressure has been observed. The diagnosis will continue by opening the EVAP canister vent shut valve.

- Case C: A vacuum build is recognized when the pressure falls below a calibrated threshold for a calibrated time. In this case, the diagnosis will continue with phase 2 without the re-opening and closing of the EVAP canister vent shut valve.

- Case D: If the tank pressure remains within a calibrated window around barometric pressure for a certain time, the EVAP canister vent shut valve will be opened.

- Case E: The tank pressure gradually increases and does not reach the target pressure when phase 1 exceeds the maximum allowable run-time. The diagnosis will then proceed with the opening of the EVAP canister vent shut valve.

- Case F: After Phase 1 is complete, if the pressure reaches an upper limit, then further pressure is relieved by opening the EVAP canister vent shut valve for a calibrated amount of time. Opening and closing can be repeated up to a calibrated number of times within the maximum allowable calibrated run-time.

- Case G: The tank pressure remains close to ambient pressure within a calibrated window for a calibrated time in phase 2.

- Case H: The integrity of the system cannot be determined when the diagnostic exceeds the maximum allowable run-time.

- Case I: The tank pressure reaches a lower threshold and rises more than a calibrated value within the maximum allowable run-time. This confirms a minimum differential pressure had been achieved.

- Case J: The tank pressure (vacuum) reaches the possible minimal differential pressure in phase 2 within the maximum allowable run-time.

If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

Start of diagnosis

Condition | Minimum | Maximum

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Initial engine coolant temperature [ECT Sensor 1] | - | 113 deg.F (45 deg.C)

Difference between initial engine coolant temperature and outside air temperature | - | 27 deg.F (15 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Other | EVAP canister vent shut valve is closed

Operation conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 minutes | -

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 20 seconds | -

Distance travelled | 4 miles (5 km) | -

12 volt battery voltage [Battery] | 10.7 V | -

Condition | Minimum | Maximum

Fuel level | 0.5 L (0.14 US gal) | 41.5 L (10.96 US gal)

Other | Smallest leak not detected

No refueling

Diagnosis pressure phase (phase 1)

Condition

Other | EVAP canister vent shut valve is closed for EONV

Cases A, B, or C occurs

Case A: Pressure threshold is reached
````

## Chunk 5550: DTC P0456 (K20C1) (2019 2020 2021)

- Title: DTC P0456 (K20C1) (2019 2020 2021)
- Source path: `pages\6707.html`
- Chunk ID: `chunk_8daf52d11d42`
- Images: `images\GHH403080.jpeg`
- Duplicate sources: `pages\8294.html`, `pages\23098.html`, `pages\21511.html`

### Full Text

````text
en initial engine coolant temperature and outside air temperature | - | 27 deg.F (15 deg.C)

Barometric pressure [Baro Sensor] | 74 kPa (555 mmHg, 21.9 inHg) | -

Other | EVAP canister vent shut valve is closed

Operation conditions

Condition | Minimum | Maximum

Elapsed time after starting the engine | 10 minutes | -

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 20 seconds | -

Distance travelled | 4 miles (5 km) | -

12 volt battery voltage [Battery] | 10.7 V | -

Condition | Minimum | Maximum

Fuel level | 0.5 L (0.14 US gal) | 41.5 L (10.96 US gal)

Other | Smallest leak not detected

No refueling

Diagnosis pressure phase (phase 1)

Condition

Other | EVAP canister vent shut valve is closed for EONV

Cases A, B, or C occurs

Case A: Pressure threshold is reached

Condition | Minimum | Maximum

Fuel tank pressure | 0.5 kPa (4 mmHg, 0.15 inHg) - 1.67 kPa (12.6 mmHg, 0.494 inHg)* | -

*: Depends on fuel level

Case B: Maximum pressure is detected

Condition | Minimum | Maximum

Fuel tank pressure | 0 kPa (0 mmHg, 0 inHg) | -

Fuel tank pressure peak* | 0.01 kPa (0.1 mmHg, 0.003 inHg) | -

*: For at least 50 seconds

Case C: Vacuum builds

Condition | Minimum | Maximum

Fuel tank pressure* | -0.125 kPa (-0.93 mmHg, -0.0369 inHg) | -

*: For at least 25 seconds

Diagnosis vacuum phase (phase 2)

Condition

Other | Vacuum phase is activated for EONV

EVAP canister vent shut valve is not closed for EONV

Cases F, G, H, I, J, or D occurs

Case F: Pressure build

Condition | Minimum | Maximum

Fuel tank pressure | 0.075 kPa (0.57 mmHg, 0.0222 inHg) | -

Other | Diagnosis is not rejected

Case G: Stabilization at zero

Condition | Minimum | Maximum

Absolute fuel tank pressure* | - | 0.063 kPa (0.47 mmHg, 0.0186 inHg)

Other | Diagnosis is not rejected

*: For at least 10 minutes

Case H: Diagnosis timeout

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 45 minutes | -

Other | Diagnosis is not rejected

Case I: Vacuum peaks

Condition | Minimum | Maximum

Fuel tank pressure* | - | -0.125 kPa (-0.93 mmHg, -0.0369 inHg)

Fuel tank pressure (vacuum) peak* | 0.01 kPa (0.1 mmHg, 0.003 inHg) | -

Other | Diagnosis is not rejected

*: For at least 50 seconds

Case J: Vacuum threshold is reached

Condition | Minimum | Maximum

Fuel tank pressure | 0.5 kPa (4 mmHg, 0.15 inHg) - 1.67 kPa (12.6 mmHg, 0.494 inHg)* | -

Other | Diagnosis is not rejected

*: Depends on fuel level.

Case D: Vacuum builds

Condition | Minimum | Maximum

Absolute fuel tank pressure* | - | 0.063 kPa (0.47 mmHg, 0.0186 inHg)

*: For at least 10 minutes

Diagnosis canister close valve is open (between phase 1 and phase 2)

Condition

Other | Pressure phase is not activated for EONV

Vacuum phase is not activated for EONV

EVAP canister vent shut valve is not opened for EONV

Diagnosis vacuum phase (phase 2)

Condition

Other | Vacuum phase is activated for EONV

Pressure phase is not activated for EONV

EVAP canister vent shut valve is closed for EONV

Cases F, G, H, I, J, or E occurs

Case F: Pressure build

Condition | Minimum | Maximum

Fuel tank pressure | 0.075 kPa (0.57 mmHg, 0.0222 inHg) | -

Other | Diagnosis is not rejected

Case G: Stabilization at zero

Condition | Minimum | Maximum

Absolute fuel tank pressure* | - | 0.063 kPa (0.47 mmHg, 0.0186 inHg)

Other | Diagnosis is not rejected

*: For at least 10 minutes

Case H: Diagnosis timeout

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 45 minutes | -

Other | Diagnosis is not rejected

Case I: Vacuum peaks

Condition | Minimum | Maximum

Fuel tank pressure* | - | -0.125 kPa (-0.93 mmHg, -0.0369 inHg)

Fuel tank pressure (vacuum) peak* | 0.01 kPa (0.1 mmHg, 0.003 inHg) | -

Other | Diagnosis is not rejected

*: For at least 50 seconds

Case J: Vacuum threshold is reached

Condition | Minimum | Maximum

Fuel tank pressure | 0.5 kPa (4 mmHg, 0.15 inHg) - 1.67 kPa (12.6 mmHg, 0.494 inHg)* | -

Other | Diagnosis is not rejected

*: Depends on fuel level

Case E: Pressure build timeout

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 45 minutes | -

Malfunction Threshold

The pressure difference for leak decision between overpressure and vacuum phase is less than 0.2 kPa (1 mmHg, 0.05 inHg) - 0.35 kPa (2.6 mmHg, 0.103 inHg)*.

*: Depends on fuel level

Possible Cause
````

## Chunk 5551: DTC P0456 (K20C1) (2019 2020 2021)

- Title: DTC P0456 (K20C1) (2019 2020 2021)
- Source path: `pages\6707.html`
- Chunk ID: `chunk_df58042fea2a`
- Images: `images\GHH403080.jpeg`
- Duplicate sources: `pages\8294.html`, `pages\23098.html`, `pages\21511.html`

### Full Text

````text
m | Maximum

Fuel tank pressure* | - | -0.125 kPa (-0.93 mmHg, -0.0369 inHg)

Fuel tank pressure (vacuum) peak* | 0.01 kPa (0.1 mmHg, 0.003 inHg) | -

Other | Diagnosis is not rejected

*: For at least 50 seconds

Case J: Vacuum threshold is reached

Condition | Minimum | Maximum

Fuel tank pressure | 0.5 kPa (4 mmHg, 0.15 inHg) - 1.67 kPa (12.6 mmHg, 0.494 inHg)* | -

Other | Diagnosis is not rejected

*: Depends on fuel level

Case E: Pressure build timeout

Condition | Minimum | Maximum

Elapsed time after the vehicle is turned to the OFF (LOCK) mode | 45 minutes | -

Malfunction Threshold

The pressure difference for leak decision between overpressure and vacuum phase is less than 0.2 kPa (1 mmHg, 0.05 inHg) - 0.35 kPa (2.6 mmHg, 0.103 inHg)*.

*: Depends on fuel level

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system very small leak

Confirmation Procedure

Operating Condition

- Start the engine and drive the vehicle for at least 4 miles (5 km).

- Turn the vehicle to the OFF (LOCK) mode and wait for a while.

- Avoid driving conditions that could lead to fuel slosh in the fuel tank.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5552: DTC P0456 (K20C2, KA/KC models)

- Title: DTC P0456 (K20C2, KA/KC models)
- Source path: `pages\6708.html`
- Chunk ID: `chunk_a58836287f3e`
- Images: `images\GHH403081.jpeg`, `images\GHH403082.jpeg`, `images\GHH403083.jpeg`
- Duplicate sources: `pages\8295.html`, `pages\23099.html`, `pages\21512.html`

### Full Text

````text
# DTC P0456 (K20C2, KA/KC models)

DTC P0456: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Judgment of detection of 0.09 inch leak as normal operation

Judgment 2: Judgment of detection of 0.02 inch leak as normal operation

Judgment 3: Detection of 0.02 inch leak

<Judgments 1, 2, and 3 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect "no 0.09 inch leak" depending on the variation of the pressure inside the fuel tank.

- If the variation of the pressure is a specified value or more before first monitoring duration has passed, it is identified as normal and the diagnosis completes.

- If the variation of the pressure is less than a specified value for a specified duration after first monitoring duration has passed, it is identified as a "0.09 inch leak" and the diagnosis completes. (P0455)

- If the variation of the pressure is a specified value or more before maximum monitoring duration has passed, it is defined as "no 0.09 inch leak", the judgment of detection of a 0.09 inch leak is completed, and it goes to 0.02 inch leak monitor.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure decrease gradient inside the fuel tank.

- If a "0.02 inch leak" is detected, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no 0.02 inch leak" is detected, it is identified as normal; the diagnosis is completed.

- If the pressure is not atmospheric pressure or less when the detection is completed, Judgment 2 is suspended and determines the judgment by result of Judgment 3.

Judgment 3:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure increase gradient inside the fuel tank.

- If "no leakage" is detected and Judgment 2 is suspended, it is identified as normal; the diagnosis is completed.

- If a "0.02 inch leak" is detected and Judgment 2 is suspended, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no leakage" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as normal without waiting the result of Judgment 2; the diagnosis is completed.

- If a "0.02 inch leak" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as a malfunction without waiting the result of Judgment 2; the diagnosis is completed. (P0456)

- If the pressure of the fuel tank does not increase to a specified value or more within a specified duration, the judgment is suspended.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0455 is judged as OK

Duration | At least 7 minutes 45 seconds but not more than 36 minutes 40 seconds

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped
````

## Chunk 5553: DTC P0456 (K20C2, KA/KC models)

- Title: DTC P0456 (K20C2, KA/KC models)
- Source path: `pages\6708.html`
- Chunk ID: `chunk_efa8a5f189fb`
- Images: `images\GHH403081.jpeg`, `images\GHH403082.jpeg`, `images\GHH403083.jpeg`
- Duplicate sources: `pages\8295.html`, `pages\23099.html`, `pages\21512.html`

### Full Text

````text
F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Malfunction Threshold

- The change rate of the pressure increase gradient inside the fuel tank is 5.0 or more.

- The change rate of the pressure decrease gradient inside the fuel tank is 0.8 or more.

- The barometric pressure is stable for at least 34 minutes.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system leak (EVAP canister purge valve from fuel tank)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 28 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5554: DTC P0456 (L15B7/L15BA)

- Title: DTC P0456 (L15B7/L15BA)
- Source path: `pages\6709.html`
- Chunk ID: `chunk_92139ce19003`
- Images: `images\GHH403084.jpeg`, `images\GHH403085.jpeg`, `images\GHH403086.jpeg`
- Duplicate sources: `pages\8296.html`, `pages\23100.html`, `pages\21513.html`

### Full Text

````text
# DTC P0456 (L15B7/L15BA)

DTC P0456: Evaporative Emission (EVAP) System Very Small Leak Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) leak detection system uses an engine off natural vacuum (EONV) method. The EONV method detects leakage from the change in fuel tank pressure via the fuel tank pressure (FTP) sensor with the engine off.

Here is an overview of the malfunction detection for the EONV method:

Judgment 1: Judgment of detection of 0.09 inch leak as normal operation

Judgment 2: Judgment of detection of 0.02 inch leak as normal operation

Judgment 3: Detection of 0.02 inch leak

<Judgments 1, 2, and 3 happen at the same time.>

Judgment 1:

After the engine has stopped, the powertrain control module (PCM) monitors the variation of the FTP sensor output to detect "no 0.09 inch leak" depending on the variation of the pressure inside the fuel tank.

- If the variation of the pressure is a specified value or more before first monitoring duration has passed, it is identified as normal and the diagnosis completes.

- If the variation of the pressure is less than a specified value for a specified duration after first monitoring duration has passed, it is identified as a "0.09 inch leak" and the diagnosis completes. (P0455)

- If the variation of the pressure is a specified value or more before maximum monitoring duration has passed, it is defined as "no 0.09 inch leak", the judgment of detection of a 0.09 inch leak is completed, and it goes to 0.02 inch leak monitor.

Judgment 2:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure decrease gradient inside the fuel tank.

- If a "0.02 inch leak" is detected, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no 0.02 inch leak" is detected, it is identified as normal; the diagnosis is completed.

- If the pressure is not atmospheric pressure or less when the detection is completed, Judgment 2 is suspended and determines the judgment by result of Judgment 3.

Judgment 3:

After the engine has stopped, the PCM monitors the variation of the FTP sensor output to detect "no 0.02 inch leak" depending on the variation corresponding to the change rate of pressure increase gradient inside the fuel tank.

- If "no leakage" is detected and Judgment 2 is suspended, it is identified as normal; the diagnosis is completed.

- If a "0.02 inch leak" is detected and Judgment 2 is suspended, it is identified as a malfunction; the diagnosis is completed. (P0456)

- If "no leakage" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as normal without waiting the result of Judgment 2; the diagnosis is completed.

- If a "0.02 inch leak" is detected and the pressure inside the fuel tank reaches to a specified value, it is identified as a malfunction without waiting the result of Judgment 2; the diagnosis is completed. (P0456)

- If the pressure of the fuel tank does not increase to a specified value or more within a specified duration, the judgment is suspended.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | P0455 is judged as OK

Duration | At least 7 minutes 45 seconds but not more than 36 minutes 40 seconds

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time before starting the engine | 6 hours | -

Initial condition A* | - | 36 deg.F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped
````

## Chunk 5555: DTC P0456 (L15B7/L15BA)

- Title: DTC P0456 (L15B7/L15BA)
- Source path: `pages\6709.html`
- Chunk ID: `chunk_306758b33246`
- Images: `images\GHH403084.jpeg`, `images\GHH403085.jpeg`, `images\GHH403086.jpeg`
- Duplicate sources: `pages\8296.html`, `pages\23100.html`, `pages\21513.html`

### Full Text

````text
F (20 deg.C)

Initial condition B** | - | 18 deg.F (10 deg.C)

Initial engine coolant temperature [ECT SENSOR 1] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Initial intake air temperature [IAT Sensor (1)] | 40 deg.F (5 deg.C) | 95 deg.F (35 deg.C)

Barometric pressure [BARO SENSOR] | 76 kPa (569 mmHg, 22.5 inHg) | -

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Avoid abrupt acceleration, deceleration, and turns

Test-drive on a flat road to avoid misdetection

No refueling is required

Vehicle stopped

*: The initial intake air temperature [IAT Sensor (1)] minus the current intake air temperature [IAT Sensor (1)]

**: The initial engine coolant temperature [ECT SENSOR 1] minus the initial intake air temperature [IAT Sensor (1)]

[ ]: HDS Parameter

Malfunction Threshold

- The change rate of the pressure increase gradient inside the fuel tank is 5.0 or more.

- The change rate of the pressure increase gradient inside the fuel tank is 0.8 or more.

- The barometric pressure is stable for at least 34 minutes.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP system leak (EVAP canister purge valve from fuel tank)

Confirmation Procedure

Operating Condition

Courtesy of HONDA, U.S.A., INC.

- After the vehicle has been left for an appropriate amount of time as specified, with the engine coolant temperature [ECT SENSOR 1] and intake air temperature [IAT Sensor (1)] within the specified range, start the engine.

- Drive the vehicle immediately at a speed between 25 - 75 mph (40 - 120 km/h) for at least 25 minutes.

- After stopping the vehicle, turn the vehicle to the OFF (LOCK) mode and leave the vehicle in this condition for at least 37 minutes (EONV executes).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle with the engine coolant temperature and intake air temperature at engine start-up within the specified temperature range, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5556: DTC P0460 (K20C2) (2019 2020 2021)

- Title: DTC P0460 (K20C2) (2019 2020 2021)
- Source path: `pages\6710.html`
- Chunk ID: `chunk_25645083f264`
- Images: `images\GHH403087.jpeg`
- Duplicate sources: `pages\8297.html`, `pages\23101.html`, `pages\21514.html`

### Full Text

````text
# DTC P0460 (K20C2) (2019 2020 2021)

DTC P0460: Fuel Level Sensor (Fuel Gauge Sending Unit) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensors (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The fuel level sensor (fuel gauge sending unit) output voltage is 0.19 V or less, or 4.03 V or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5557: DTC P0460 (L15B7/L15BY) (2019 2020 2021)

- Title: DTC P0460 (L15B7/L15BY) (2019 2020 2021)
- Source path: `pages\6711.html`
- Chunk ID: `chunk_033db4468e1c`
- Images: `images\GHH403088.jpeg`
- Duplicate sources: `pages\8298.html`, `pages\23102.html`, `pages\21515.html`

### Full Text

````text
# DTC P0460 (L15B7/L15BY) (2019 2020 2021)

DTC P0460: Fuel Level Sensor (Fuel Gauge Sending Unit) Out of Range

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensors (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 6.0 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The fuel level sensor (fuel gauge sending unit) output voltage is 0.19 V or less, or 4.03 V or more for at least 6.0 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5558: DTC P0461 (K20C1) (2017 2018 2019)

- Title: DTC P0461 (K20C1) (2017 2018 2019)
- Source path: `pages\6712.html`
- Chunk ID: `chunk_a0efbdb23adb`
- Images: none
- Duplicate sources: `pages\8299.html`, `pages\23103.html`, `pages\21516.html`

### Full Text

````text
# DTC P0461 (K20C1) (2017 2018 2019)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

The powertrain control module (PCM) monitors the fuel level sensor which is installed in the fuel tank. If the fuel level sensor outputs an abnormal value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 10 seconds

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16 V

Fuel level sensor voltage* | 0.1515 V | 4.8489 V

State of the engine | Running

Other | Fuel level sensor value and CAN signal are valid

*: Condition is met for at least 11 seconds

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions occurs:

- The fuel level is above 6, 553 L (1, 731.1 US gal) for at least 10 seconds.

- The difference between initial fuel level and current filtered fuel level is 0.5 L (0.13 US gal) or more.

- Consumed fuel minus fuel level difference is less than 0.5 L (0.13 US gal) for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5559: DTC P0461(K20C1) (2019)

- Title: DTC P0461(K20C1) (2019)
- Source path: `pages\6713.html`
- Chunk ID: `chunk_3d944bc78345`
- Images: none
- Duplicate sources: `pages\8300.html`, `pages\23104.html`, `pages\21517.html`

### Full Text

````text
# DTC P0461(K20C1) (2019)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

The powertrain control module (PCM) monitors the fuel level sensor which is installed in the fuel tank. If the fuel level sensor outputs an abnormal value, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16 V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

Any of the conditions occurs:

- The fuel level is above 6, 553 L (1, 731.1 US gal) for at least 10 seconds.

- The difference between initial fuel level and current filtered fuel level is 0.5 L (0.13 US gal) or more.

- The absolute difference between consumed fuel and fuel level is less than 15 L (4.0 US gal) for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5560: DTC P0461 (K20C1) (2020 2021)

- Title: DTC P0461 (K20C1) (2020 2021)
- Source path: `pages\6714.html`
- Chunk ID: `chunk_1cc0b0e9ebd7`
- Images: `images\GHH403089.jpeg`
- Duplicate sources: `pages\8301.html`, `pages\23105.html`, `pages\21518.html`

### Full Text

````text
# DTC P0461 (K20C1) (2020 2021)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor in the fuel tank measures the fuel level of the fuel tank. The powertrain control module (PCM) checks the change in the fuel level sensor output and then compares it to the calculated fuel consumption value. A malfunction is detected by the following checks.

- If the absolute difference between the fuel consumption and fuel level sensor output change is a specified value for a specified duration when a certain fuel amount is consumed, the PCM detects a malfunction and stores a DTC.

- If the absolute difference between the fuel level at the start of the sensor-stuck check and the filtered fuel level is a specified value, the PCM detects a malfunction and stores a DTC.

Repeatedly filling the tank with less than the specified amount may lead to a mismatch in the actual fuel amount versus the calculated amount.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16 V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

Either of the conditions occur:

- The absolute difference between the fuel consumption and fuel level sensor output change is less than 14 L (3.6 US gal) for at least 5 seconds when a certain fuel amount is consumed.

- The absolute difference between the fuel level at the start of the sensor-stuck check and the filtered fuel level is less than 0.5 L (0.13 US gal).

Possible Cause

NOTE:

- - The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- - Refueling the tank with less than the specified amount of 5 L (1.32 US gal) four times, may lead to a mismatch in the actual fuel amount versus the calculated amount. To prevent this, make sure that the customer fills the tank with the minimum specified amount during refueling. Refer to the How to Refuel section of the owner's manual for details.

Refueling the tank with less than the specified amount of 5 L (1.32 US gal) four times, may lead to a mismatch in the actual fuel amount versus the calculated amount. To prevent this, make sure that the customer fills the tank with the minimum specified amount during refueling. Refer to the How to Refuel section of the owner's manual for details.

- Fuel level sensor failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command.
````

## Chunk 5561: DTC P0461 (K20C2) (2016 2017 2018)

- Title: DTC P0461 (K20C2) (2016 2017 2018)
- Source path: `pages\6715.html`
- Chunk ID: `chunk_2e0cbcb12cde`
- Images: `images\GHH403090.jpeg`
- Duplicate sources: `pages\8302.html`, `pages\23106.html`, `pages\21519.html`

### Full Text

````text
# DTC P0461 (K20C2) (2016 2017 2018)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated with the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float into electrical signals that correspond to the fuel level, and it indicates the amount of fuel in the fuel tank. If the powertrain control module (PCM) receives no change in the fuel level sensor (fuel gauge sending unit) output after driving for a specified number of miles, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Every 124 miles (200 km)

Sequence | P0456 is judged as NG

Duration | -

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Mileage | 124 miles (200 km) | -

Other | Avoid driving and stopping on a steep road

Malfunction Threshold

The change in the fuel level sensor (fuel gauge sending unit) output [FUEL LEVEL] is 3.5 % or less.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Confirmation Procedure

Operating Condition

Drive for 124 miles (200 km) or more under Enable Conditions (see "Other") without refueling (turning the vehicle to the OFF (LOCK) mode is acceptable).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected in a certain drive cycle and a malfunction of 0.02 inch leak is detected in the same drive cycle, and DTC P0456 is stored, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5562: DTC P0461 (K20C2) (2019 2020 2021)

- Title: DTC P0461 (K20C2) (2019 2020 2021)
- Source path: `pages\6716.html`
- Chunk ID: `chunk_482fd8a2aeeb`
- Images: `images\GHH403091.jpeg`
- Duplicate sources: `pages\8303.html`, `pages\23107.html`, `pages\21520.html`

### Full Text

````text
# DTC P0461 (K20C2) (2019 2020 2021)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor in the fuel tank measures a fuel level of the fuel tank. The powertrain control module (PCM) confirms the correlation between the fuel level sensor output and the fuel level converted from the fuel consumption. If the correlation is out of normal range, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.1 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the vehicle condition is turned to the ON mode | 520 milliseconds | -

Total driving distance | 31.1 miles (50.0 km) | -

Fuel consumption after refueling | 8.422 L (2.2249 US gal) | -

12 volt battery voltage [BATTERY] | 10.5 V | -

Other | Test-drive on a flat road to avoid misdetection

[ ]: HDS Parameter

Malfunction Threshold

Any of the condition occurs:

- The fuel level sensor output change is 53 % or more when the fuel consumption is 32 %.

- The fuel level sensor output change is 88 % or more when the fuel consumption is 64 %.

- The fuel level sensor output change is 12.6 % or less.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel level sensor failure

Confirmation Procedure

Operating Condition

- Start the engine.

- Drive the vehicle at least 31.1 miles (50.0 km/h) without refueling.

- Does not matter to turn the vehicle to the OFF (LOCK) during the test-drive.

- Test-drive on a flat road to avoid misdetection.

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool clear command or by disconnecting the 12 volt battery.
````

## Chunk 5563: DTC P0461 (L15B7 (except Si)/L15BY) (2019 2020 2021)

- Title: DTC P0461 (L15B7 (except Si)/L15BY) (2019 2020 2021)
- Source path: `pages\6717.html`
- Chunk ID: `chunk_3b47b788d249`
- Images: `images\GHH403092.jpeg`
- Duplicate sources: `pages\8304.html`, `pages\23108.html`, `pages\21521.html`

### Full Text

````text
# DTC P0461 (L15B7 (except Si)/L15BY) (2019 2020 2021)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated with the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float into electrical signals that correspond to the fuel level, and it indicates the amount of fuel in the fuel tank. If the powertrain control module (PCM) receives no change in the fuel level sensor (fuel gauge sending unit) output after driving for a specified number of miles, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Every 124 miles (200 km)

Sequence | P0456 is judged as NG

Duration | -

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Mileage | 124 miles (200 km) | -

Other | Avoid driving and stopping on a steep road

Malfunction Threshold

The change in the fuel level sensor (fuel gauge sending unit) output [FUEL LEVEL] is 3.5 % or less.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Confirmation Procedure

Operating Condition

Drive for 124 miles (200 km) or more under Enable Conditions (see "Other") without refueling (turning the vehicle to the OFF (LOCK) mode is acceptable).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected in a certain drive cycle and a malfunction of 0.02 inch leak is detected in the same drive cycle, and DTC P0456 is stored, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5564: DTC P0461 (L15B7/L15BA/L15BY) (2016 2017 2018)

- Title: DTC P0461 (L15B7/L15BA/L15BY) (2016 2017 2018)
- Source path: `pages\6718.html`
- Chunk ID: `chunk_5aef308121f3`
- Images: `images\GHH403093.jpeg`
- Duplicate sources: `pages\8305.html`, `pages\23109.html`, `pages\21522.html`

### Full Text

````text
# DTC P0461 (L15B7/L15BA/L15BY) (2016 2017 2018)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated with the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float into electrical signals that correspond to the fuel level, and it indicates the amount of fuel in the fuel tank. If the powertrain control module (PCM) receives no change in the fuel level sensor (fuel gauge sending unit) output after driving for a specified number of miles, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Every 124 miles (200 km)

Sequence | P0456 is judged as NG

Duration | -

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Mileage | 124 miles (200 km) | -

Other | Avoid driving and stopping on a steep road

Malfunction Threshold

The change in the fuel level sensor (fuel gauge sending unit) output [FUEL LEVEL] is 3.5 % or less.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Confirmation Procedure

Operating Condition

Drive for 124 miles (200 km) or more under Enable Conditions (see "Other") without refueling (turning the vehicle to the OFF (LOCK) mode is acceptable).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected in a certain drive cycle and a malfunction of 0.02 inch leak is detected in the same drive cycle, and DTC P0456 is stored, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5565: DTC P0461 (Si/L15BA) (2019 2020 2021)

- Title: DTC P0461 (Si/L15BA) (2019 2020 2021)
- Source path: `pages\6719.html`
- Chunk ID: `chunk_ad54fcfd762c`
- Images: `images\GHH403094.jpeg`
- Duplicate sources: `pages\8306.html`, `pages\23110.html`, `pages\21523.html`

### Full Text

````text
# DTC P0461 (Si/L15BA) (2019 2020 2021)

DTC P0461: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Range/Performance Problem

General Description

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated with the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float into electrical signals that correspond to the fuel level, and it indicates the amount of fuel in the fuel tank. If the powertrain control module (PCM) receives no change in the fuel level sensor (fuel gauge sending unit) output after driving for a specified number of miles, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Every 124 miles (200 km)

Sequence | P0456 is judged as NG

Duration | -

DTC Type | One drive cycle, MIL off

Enable Conditions

Condition | Minimum | Maximum

Mileage | 124 miles (200 km) | -

Other | Avoid driving and stopping on a steep road

Malfunction Threshold

The change in the fuel level sensor (fuel gauge sending unit) output [FUEL LEVEL] is 3.5 % or less.

[ ]: HDS Parameter

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Fuel gauge sending unit failure

Confirmation Procedure

Operating Condition

Drive for 124 miles (200 km) or more under Enable Conditions (see "Other") without refueling (turning the vehicle to the OFF (LOCK) mode is acceptable).

- Drive the vehicle in this manner only if the traffic regulations and ambient conditions allow.

With the HDS

None.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected in a certain drive cycle and a malfunction of 0.02 inch leak is detected in the same drive cycle, and DTC P0456 is stored, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5566: DTC P0462, P0463 (K20C1) (2017 2018 2019)

- Title: DTC P0462, P0463 (K20C1) (2017 2018 2019)
- Source path: `pages\6720.html`
- Chunk ID: `chunk_02324f128829`
- Images: none
- Duplicate sources: `pages\8307.html`, `pages\23111.html`, `pages\21524.html`

### Full Text

````text
# DTC P0462, P0463 (K20C1) (2017 2018 2019)

DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

DTC P0463: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage

General Description

The fuel level sensor (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0462

The fuel level sensor (fuel gauge sending unit) output voltage is lower than 0.1515 V for at least 1 second.

DTC: P0463

The fuel level sensor (fuel gauge sending unit) output voltage is higher than 4.8489 V for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0462

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line short to ground

DTC: P0463

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line open

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE- line open

Common

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5567: DTC P0462, P0463 (K20C1) (2019)

- Title: DTC P0462, P0463 (K20C1) (2019)
- Source path: `pages\6721.html`
- Chunk ID: `chunk_b32dbcbca780`
- Images: none
- Duplicate sources: `pages\8308.html`, `pages\23112.html`, `pages\21525.html`

### Full Text

````text
# DTC P0462, P0463 (K20C1) (2019)

DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

DTC P0463: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage

General Description

The fuel level sensor (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0462

The fuel level sensor (fuel gauge sending unit) output voltage is lower than 0.15 V for at least 1 second.

DTC: P0463

The fuel level sensor (fuel gauge sending unit) output voltage is higher than 4.84 V for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0462

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line short to ground

DTC: P0463

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line open

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE- line open

Common

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5568: DTC P0462, P0463 (K20C1) (2020 2021)

- Title: DTC P0462, P0463 (K20C1) (2020 2021)
- Source path: `pages\6722.html`
- Chunk ID: `chunk_5f0a9e64a87e`
- Images: none
- Duplicate sources: `pages\8309.html`, `pages\23113.html`, `pages\21526.html`

### Full Text

````text
# DTC P0462, P0463 (K20C1) (2020 2021)

DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

DTC P0463: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage

General Description

The fuel level sensor (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 9 V | 16V

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0462

The fuel level sensor (fuel gauge sending unit) output voltage is lower than 0.15 V for at least 1 second.

DTC: P0463

The fuel level sensor (fuel gauge sending unit) output voltage is higher than 4.85 V for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0462

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line short to ground

DTC: P0463

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line open

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE- line open

Common

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5569: DTC P0462, P0463 (K20C2)

- Title: DTC P0462, P0463 (K20C2)
- Source path: `pages\6723.html`
- Chunk ID: `chunk_fbdffd1dfd4f`
- Images: `images\GHH403095.jpeg`, `images\GHH403096.jpeg`
- Duplicate sources: `pages\8310.html`, `pages\23114.html`, `pages\21527.html`

### Full Text

````text
# DTC P0462, P0463 (K20C2)

DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

DTC P0463: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage

General Description

Without CAN Gateway:

Courtesy of HONDA, U.S.A., INC.

With CAN Gateway:

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0462

The fuel level sensor (fuel gauge sending unit) output voltage is 0.10 V or less for at least 5 seconds.

DTC: P0463

The fuel level sensor (fuel gauge sending unit) output voltage is 4.92 V or more for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0462

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line short to ground

DTC: P0463

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line open

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE- line open

Common

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5570: DTC P0462, P0463 (Without XM)

- Title: DTC P0462, P0463 (Without XM)
- Source path: `pages\6724.html`
- Chunk ID: `chunk_4653d0292e6f`
- Images: `images\GHH403097.jpeg`, `images\GHH403098.jpeg`
- Duplicate sources: `pages\8311.html`, `pages\23115.html`, `pages\21528.html`

### Full Text

````text
# DTC P0462, P0463 (Without XM)

DTC P0462: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit Low Voltage

DTC P0463: Fuel Level Sensor (Fuel Gauge Sending Unit) Circuit High Voltage

General Description

Without CAN Gateway:

Courtesy of HONDA, U.S.A., INC.

With CAN Gateway:

Courtesy of HONDA, U.S.A., INC.

The fuel level sensor (fuel gauge sending unit) is incorporated into the fuel pump and installed in the fuel tank. Using a built-in potentiometer and float, it converts the movement of the float to electrical signals as an output that corresponds fuel level variations in the fuel tank. The fuel level, which is indicated by the gauge control module, is sent to the powertrain control module (PCM) via the controller area network (CAN). If the PCM detects a signal from the fuel level sensor (fuel gauge sending unit) is a predetermined value for a set time, it detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

DTC: P0462

The fuel level sensor (fuel gauge sending unit) output voltage is 0.10 V or less for at least 5 seconds.

DTC: P0463

The fuel level sensor (fuel gauge sending unit) output voltage is 4.92 V or more for at least 5 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

DTC: P0462

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line short to ground

DTC: P0463

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE+ line open

- Fuel level sensor (fuel gauge sending unit) FUEL GAUGE- line open

Common

- Fuel level sensor (fuel gauge sending unit) failure

- Gauge control module internal circuit failure

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5571: DTC P0480 (K20C2)

- Title: DTC P0480 (K20C2)
- Source path: `pages\6725.html`
- Chunk ID: `chunk_2fb05c356fae`
- Images: `images\GHH403099.jpeg`
- Duplicate sources: `pages\8312.html`, `pages\23116.html`, `pages\21529.html`

### Full Text

````text
# DTC P0480 (K20C2)

DTC P0480: Radiator Fan Control (RFC) System Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The radiator fan control (RFC) unit cools the radiator and the A/C condenser by controlling the cooling fan motor. The powertrain control module (PCM) communicates with the RFC unit using the pulse-width modulation (PWM) signal. The PCM sends drive command to the RFC unit via the FAN CONTROL line using the PWM signal according to the condition of the vehicle. When a malfunction in the system is detected by self-diagnosis, the RFC unit makes FAN CONTROL line signal output to GND. When the PCM cannot receive the PWM signal via the FAN CONTROL line for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 12 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the PCM is activated | 2 seconds | -

12 volt battery voltage [BATTERY] | 10 V | 18 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot receive PWM signal from the RFC unit via the FAN CONTROL line for at least 12 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- RFC unit RFC DRIVER RLY OUT line open

- RFC unit GND line open

- RFC unit FAN CONTROL line open

- RFC unit FAN CONTROL line short

- RFC relay stuck off

- RFC unit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Turn the vehicle to the ON mode.

With the HDS

Select the RADIATOR FAN in the INSPECTION MENU with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5572: DTC P0480 (L15B7/L15BA/L15BY)

- Title: DTC P0480 (L15B7/L15BA/L15BY)
- Source path: `pages\6726.html`
- Chunk ID: `chunk_e9df5395599b`
- Images: `images\GHH403100.jpeg`
- Duplicate sources: `pages\8313.html`, `pages\23117.html`, `pages\21530.html`

### Full Text

````text
# DTC P0480 (L15B7/L15BA/L15BY)

DTC P0480: Radiator Fan Control (RFC) System Malfunction

General Description

Courtesy of HONDA, U.S.A., INC.

The radiator fan control (RFC) unit cools the radiator and the A/C condenser by controlling the cooling fan motor. The powertrain control module (PCM) communicates with the RFC unit using the pulse-width modulation (PWM) signal. The PCM sends drive command to the RFC unit via the FAN CONTROL line using the PWM signal according to the condition of the vehicle. When a malfunction in the system is detected by self-diagnosis, the RFC unit makes FAN CONTROL line signal output to GND. When the PCM cannot receive the PWM signal via the FAN CONTROL line for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 12 seconds or more

DTC Type | Two drive cycles, MIL off

Enable Conditions

Condition | Minimum | Maximum

Elapsed time after the PCM is activated | 2 seconds | -

12 volt battery voltage [BATTERY] | 10 V | 18 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The PCM cannot receive PWM signal from the RFC unit via the FAN CONTROL line for at least 12 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- RFC unit RFC DRIVER RLY OUT line open

- RFC unit GND line open

- RFC unit FAN CONTROL line open

- RFC unit FAN CONTROL line short

- RFC relay stuck off

- RFC unit failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Turn the vehicle to the ON mode.

With the HDS

Select the RADIATOR FAN in the INSPECTION MENU with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5573: DTC P0496 (K20C1) (2017 2018)

- Title: DTC P0496 (K20C1) (2017 2018)
- Source path: `pages\6727.html`
- Chunk ID: `chunk_31ac4d61abf0`
- Images: `images\GHH403101.jpeg`, `images\GHH403102.jpeg`
- Duplicate sources: `pages\8314.html`, `pages\23118.html`, `pages\21531.html`

### Full Text

````text
# DTC P0496 (K20C1) (2017 2018)

DTC P0496: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air.

Canister purging (P2422)

The EVAP system monitor diagnostic starts with the canister purging. During canister purging, the fuel tank pressure is monitored against low rationality threshold. If the fuel tank pressure reaches the threshold, then the EVAP canister purge valve is commanded closed. If the fuel tank pressure remains below, this threshold for calibrated amount of time after EVAP canister purge valve has been closed, then the powertrain control module (PCM) detects as EVAP canister vent shut valve stuck closed (P2422). If an EVAP canister vent shut valve stuck closed (P2422) is detected, the EVAP system monitor will be aborted.

Conditioning: Pressure stabilization after purging

The EVAP system monitor continues with the closing of the EVAP canister purge valve. The pressure in the fuel tank system is initially lower than the ambient pressure immediately after canister purging. Closing the EVAP canister purge valve causes ambient air to rush into the fuel tank system via the open EVAP canister vent shut valve. This results in a rise in the fuel tank pressure. If the pressure in the fuel tank does not stabilize within a calibrated amount of time, the EVAP system monitor will be aborted.

Phase A: Compensation gradient determination

The EVAP system monitor continues with the closure of the EVAP canister vent shut valve (EVAP canister purge valve remains closed). The pressure in the fuel tank system may rise further due to fuel evaporation. The gradient of the pressure signal is monitored during a calibrated amount of time. EVAP system monitor will be aborted if the gradient exceeds a calibrated threshold - high fuel evaporation. In the event that excessive fuel evaporation is not detected, the compensation gradient will be stored at the end of the observation period (phase A). This compensation gradient will be used at a later time to correct the leak gradient that is measured in phase C.

On the other side, if the pressure in fuel tank falls down below a calibrated rationality threshold, an EVAP canister purge valve stuck open (P0496) will be detected. If an EVAP canister purge valve stuck open (P0496) is detected, the EVAP system monitor will be aborted.

Phase B: EVAP canister purge valve low flow monitor and detection of large leaks

Phase B starts with the opening of the EVAP canister purge valve. The resulting change in the EVAP system pressure (vacuum build up) is monitored by the fuel tank pressure (FTP) sensor. If the resulting pressure does not drop below a calibrated threshold after a calibrated amount of time, an EVAP canister purge valve stuck closed (P0497) will be detected.

In spite of a properly functioning EVAP canister purge valve, the fuel tank pressure can begin to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected.
````

## Chunk 5574: DTC P0496 (K20C1) (2017 2018)

- Title: DTC P0496 (K20C1) (2017 2018)
- Source path: `pages\6727.html`
- Chunk ID: `chunk_03b4f97212a3`
- Images: `images\GHH403101.jpeg`, `images\GHH403102.jpeg`
- Duplicate sources: `pages\8314.html`, `pages\23118.html`, `pages\21531.html`

### Full Text

````text
If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

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

The difference between the fuel tank pressure and its reference (start) value during compensation gradient determination measurement is less than -0.175 kPa (-1.32 mmHg, -0.0517 inHg) within 4 seconds.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

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

## Chunk 5575: DTC P0497 (K20C1) (2017 2018)

- Title: DTC P0497 (K20C1) (2017 2018)
- Source path: `pages\6728.html`
- Chunk ID: `chunk_9604cff76cd7`
- Images: `images\GHH403103.jpeg`, `images\GHH403104.jpeg`
- Duplicate sources: `pages\8315.html`, `pages\23119.html`, `pages\21532.html`

### Full Text

````text
# DTC P0497 (K20C1) (2017 2018)

DTC P0497: Evaporative Emission (EVAP) System Low Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air.

Canister purging (P2422)

The EVAP system monitor diagnostic starts with the canister purging. During canister purging, the fuel tank pressure is monitored against low rationality threshold. If the fuel tank pressure reaches the threshold, then the EVAP canister purge valve is commanded closed. If the fuel tank pressure remains below, this threshold for calibrated amount of time after EVAP canister purge valve has been closed, then the powertrain control module (PCM) detects as EVAP canister vent shut valve stuck closed (P2422). If an EVAP canister vent shut valve stuck closed (P2422) is detected, the EVAP system monitor will be aborted.

Conditioning: Pressure stabilization after purging

The EVAP system monitor continues with the closing of the EVAP canister purge valve. The pressure in the fuel tank system is initially lower than the ambient pressure immediately after canister purging. Closing the EVAP canister purge valve causes ambient air to rush into the fuel tank system via the open EVAP canister vent shut valve. This results in a rise in the fuel tank pressure. If the pressure in the fuel tank does not stabilize within a calibrated amount of time, the EVAP system monitor will be aborted.

Phase A: Compensation gradient determination

The EVAP system monitor continues with the closure of the EVAP canister vent shut valve (EVAP canister purge valve remains closed). The pressure in the fuel tank system may rise further due to fuel evaporation. The gradient of the pressure signal is monitored during a calibrated amount of time. EVAP system monitor will be aborted if the gradient exceeds a calibrated threshold - high fuel evaporation. In the event that excessive fuel evaporation is not detected, the compensation gradient will be stored at the end of the observation period (phase A). This compensation gradient will be used at a later time to correct the leak gradient that is measured in phase C.

On the other side, if the pressure in fuel tank falls down below a calibrated rationality threshold, an EVAP canister purge valve stuck open (P0496) will be detected. If an EVAP canister purge valve stuck open (P0496) is detected, the EVAP system monitor will be aborted.

Phase B: EVAP canister purge valve low flow monitor and detection of large leaks

Phase B starts with the opening of the EVAP canister purge valve. The resulting change in the EVAP system pressure (vacuum build up) is monitored by the fuel tank pressure (FTP) sensor. If the resulting pressure does not drop below a calibrated threshold after a calibrated amount of time, an EVAP canister purge valve stuck closed (P0497) will be detected.

In spite of a properly functioning EVAP canister purge valve, the fuel tank pressure can begin to drop but would not reach the calibrated differential pressure threshold. In this case, the continuous evaluation of the differential pressure gradient will be terminated after a calibrated amount of time has elapsed - timeout. A fault indicating a large leak will be set if the differential pressure gradient calculated during this vacuum build up time is less than a calibrated threshold. If the fuel tank pressure has reached the calibrated differential pressure threshold, then the vacuum build up process will be performed further till the fuel tank pressure decreases to the next calibrated differential pressure threshold for 0.02 inch leak test. If this leak test specific threshold has been not achieved within calibrated amount of time, an EVAP system large leak (P0455) will be detected.
````

## Chunk 5576: DTC P0497 (K20C1) (2017 2018)

- Title: DTC P0497 (K20C1) (2017 2018)
- Source path: `pages\6728.html`
- Chunk ID: `chunk_1a81ffddbdce`
- Images: `images\GHH403103.jpeg`, `images\GHH403104.jpeg`
- Duplicate sources: `pages\8315.html`, `pages\23119.html`, `pages\21532.html`

### Full Text

````text
If the difference between the maximum differential pressure obtained in phase 1 and the minimum differential pressure obtained in phase 2 is less than the calibrated threshold, an EVAP system very small leak (P0456) will be detected.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | -

DTC Type | Two drive cycles, MIL on

Enable Conditions

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

The difference between the fuel tank pressure and its reference (start) value during vacuum build-up is greater than -0.001221 kPa (-0.00915 mmHg, -0.0003605 inHg) (no significant pressure decrease has been detected) and integrated purge mass flow has reached 0.35 g (0.0124 oz).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve closed stuck

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

## Chunk 5577: DTC P0498 (K20C1) (2017 2018 2019)

- Title: DTC P0498 (K20C1) (2017 2018 2019)
- Source path: `pages\6729.html`
- Chunk ID: `chunk_91e4932f9831`
- Images: `images\GHH403105.jpeg`
- Duplicate sources: `pages\8316.html`, `pages\23120.html`, `pages\21533.html`

### Full Text

````text
# DTC P0498 (K20C1) (2017 2018 2019)

DTC P0498: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is a specified value while the EVAP canister vent shut valve is not actuated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output voltage is less than 3 V for at least 0.5 second while the EVAP canister vent shut valve is not actuated.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line short to ground

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5578: DTC P0498 (K20C1) (2019 2020 2021)

- Title: DTC P0498 (K20C1) (2019 2020 2021)
- Source path: `pages\6730.html`
- Chunk ID: `chunk_2a6f4f118b50`
- Images: `images\GHH403106.jpeg`
- Duplicate sources: `pages\8317.html`, `pages\23121.html`, `pages\21534.html`

### Full Text

````text
# DTC P0498 (K20C1) (2019 2020 2021)

DTC P0498: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is a specified value while the power stage is off, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

State of the engine | Running

Other | EVAP canister vent shut valve is closed

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output voltage is less than 2.74 V for at least 0.5 second while the power stage is off.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line short to ground

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5579: DTC P0498 (K20C2)

- Title: DTC P0498 (K20C2)
- Source path: `pages\6731.html`
- Chunk ID: `chunk_ca4db403fbb1`
- Images: `images\GHH403107.jpeg`
- Duplicate sources: `pages\8318.html`, `pages\23122.html`, `pages\21535.html`

### Full Text

````text
# DTC P0498 (K20C2)

DTC P0498: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister vent shut valve is attached to the EVAP canister to control the venting of the EVAP canister to atmosphere. The EVAP canister vent shut valve is open (open to atmosphere) when the VSV signal is OFF. If the return signal is "OFF" when the powertrain control module (PCM) outputs the "ON" signal to the EVAP canister vent shut valve, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal is "OFF" for at least 5 seconds when the PCM outputs the "ON" signal to the EVAP canister vent shut valve.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line open

- EVAP canister vent shut valve VSV line short to ground

- EVAP canister vent shut valve power supply line open

- EVAP canister vent shut valve failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 5 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5580: DTC P0498 (L15B7/L15BA/L15BY)

- Title: DTC P0498 (L15B7/L15BA/L15BY)
- Source path: `pages\6732.html`
- Chunk ID: `chunk_271a97468ea6`
- Images: `images\GHH403108.jpeg`
- Duplicate sources: `pages\8319.html`, `pages\23123.html`, `pages\21536.html`

### Full Text

````text
# DTC P0498 (L15B7/L15BA/L15BY)

DTC P0498: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit Low Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister vent shut valve is attached to the EVAP canister to control the venting of the EVAP canister to atmosphere. The EVAP canister vent shut valve is open (open to atmosphere) when the VSV signal is OFF. If the return signal is "OFF" when the powertrain control module (PCM) outputs the "ON" signal to the EVAP canister vent shut valve, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal is "OFF" for at least 5 seconds when the PCM outputs the "ON" signal to the EVAP canister vent shut valve.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line open

- EVAP canister vent shut valve VSV line short to ground

- EVAP canister vent shut valve power supply line open

- EVAP canister vent shut valve failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 5 seconds.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5581: DTC P0499 (K20C1) (2017 2018 2019)

- Title: DTC P0499 (K20C1) (2017 2018 2019)
- Source path: `pages\6733.html`
- Chunk ID: `chunk_7874b3089e3e`
- Images: `images\GHH403109.jpeg`
- Duplicate sources: `pages\8320.html`, `pages\23124.html`, `pages\21537.html`

### Full Text

````text
# DTC P0499 (K20C1) (2017 2018 2019)

DTC P0499: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is a specified value while the EVAP canister vent shut valve is actuated, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16 V

Vehicle | ON mode

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output current is greater than 1 - 2 A for at least 0.5 second while the EVAP canister vent shut valve is actuated.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve line short to power

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5582: DTC P0499 (K20C1) (2019)

- Title: DTC P0499 (K20C1) (2019)
- Source path: `pages\6734.html`
- Chunk ID: `chunk_21dcccc73ca1`
- Images: `images\GHH403110.jpeg`
- Duplicate sources: `pages\8321.html`, `pages\23125.html`, `pages\21538.html`

### Full Text

````text
# DTC P0499 (K20C1) (2019)

DTC P0499: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is a specified value while the power stage is on, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition

State of the engine | Running

Other | EVAP canister vent shut valve is closed

Malfunction Threshold

The EVAP canister vent shut valve output current is greater than 2 A while the power stage is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve line short to power

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5583: DTC P0499 (K20C1) (2020 2021)

- Title: DTC P0499 (K20C1) (2020 2021)
- Source path: `pages\6735.html`
- Chunk ID: `chunk_906ef01473c6`
- Images: `images\GHH403111.jpeg`
- Duplicate sources: `pages\8322.html`, `pages\23126.html`, `pages\21539.html`

### Full Text

````text
# DTC P0499 (K20C1) (2020 2021)

DTC P0499: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The powertrain control module (PCM) monitors the evaporative emission (EVAP) canister vent shut valve for electrical malfunctions. The EVAP canister vent shut valve is mounted in the canister and serves to perform a diagnosis of the EVAP system. If the EVAP canister vent shut valve output voltage is a specified value while the power stage is on, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [Battery] | 8 V | 16V

State of the engine | Running

Other | EVAP canister vent shut valve is closed

[ ]: HDS Parameter

Malfunction Threshold

The EVAP canister vent shut valve output current is greater than 2 A while the power stage is on.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve line short to power

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 5584: DTC P0499 (K20C2)

- Title: DTC P0499 (K20C2)
- Source path: `pages\6736.html`
- Chunk ID: `chunk_4c21950cb5da`
- Images: `images\GHH403112.jpeg`
- Duplicate sources: `pages\8323.html`, `pages\23127.html`, `pages\21540.html`

### Full Text

````text
# DTC P0499 (K20C2)

DTC P0499: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister vent shut valve is attached to the EVAP canister to control the venting of the EVAP canister to atmosphere. The EVAP canister vent shut valve is open (open to atmosphere) when the VSV signal is OFF. If the return signal is "ON" when the powertrain control module (PCM) outputs the "OFF" signal to the EVAP canister vent shut valve, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal is "ON" for at least 5 seconds when the PCM outputs the "OFF" signal to the EVAP canister vent shut valve.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line short to power

- EVAP canister vent shut valve failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5585: DTC P0499 (L15B7/L15BA)

- Title: DTC P0499 (L15B7/L15BA)
- Source path: `pages\6737.html`
- Chunk ID: `chunk_a9b145d72b3f`
- Images: `images\GHH403113.jpeg`
- Duplicate sources: `pages\8324.html`, `pages\23128.html`, `pages\21541.html`

### Full Text

````text
# DTC P0499 (L15B7/L15BA)

DTC P0499: Evaporative Emission (EVAP) Canister Vent Shut Valve Circuit High Voltage

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) canister vent shut valve is attached to the EVAP canister to control the venting of the EVAP canister to atmosphere. The EVAP canister vent shut valve is open (open to atmosphere) when the VSV signal is OFF. If the return signal is "ON" when the powertrain control module (PCM) outputs the "OFF" signal to the EVAP canister vent shut valve, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 5 seconds or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

Condition | Minimum | Maximum

12 volt battery voltage [BATTERY] | 10.0 V | -

State of the engine | Running

[ ]: HDS Parameter

Malfunction Threshold

The return signal is "ON" for at least 5 seconds when the PCM outputs the "OFF" signal to the EVAP canister vent shut valve.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister vent shut valve VSV line short to power

- EVAP canister vent shut valve failure

- PCM internal circuit failure

Confirmation Procedure

Operating Condition

Start the engine.

With the HDS

Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, the MIL comes on and a Confirmed DTC and the freeze data are stored.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 5586: DTC P04DF (K20C1) (2019 2020 2021)

- Title: DTC P04DF (K20C1) (2019 2020 2021)
- Source path: `pages\6738.html`
- Chunk ID: `chunk_7740b93f1526`
- Images: `images\GHH403114.jpeg`
- Duplicate sources: `pages\8325.html`, `pages\23129.html`, `pages\21542.html`

### Full Text

````text
# DTC P04DF (K20C1) (2019 2020 2021)

DTC P04DF: Evaporative Emission (EVAP) System High Purge Flow Detected

General Description

Courtesy of HONDA, U.S.A., INC.

The evaporative emission (EVAP) system monitor detects leaks in the fuel supply system by inducing and utilizing negative pressure in engine idle and vehicle OFF (LOCK) mode. This monitor is also used for diagnosing both the EVAP canister purge valve and EVAP canister vent shut valve for rationality malfunctions. Fuel that evaporates from the fuel canister gets stored in the EVAP canister. The evaporated fuel trapped in the EVAP canister is occasionally flushed at the appropriate engine operating conditions into the intake manifold via the EVAP canister purge valve. The EVAP canister vent shut valve isolates the evaporative system from ambient air. Several steps are taken to detect for leakage in the fuel supply system. If the difference between the fuel tank pressure and its reference (start) value during compensation gradient determination measurement is a specified value, the powertrain control module (PCM) detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Once per driving cycle

Sequence | None

Duration | 0.5 second or more

DTC Type | Two drive cycles, MIL on

Enable Conditions

General enable conditions to trigger EVAP system monitor

Condition | Minimum | Maximum

Elapsed time after starting the engine | 9 minutes 10 seconds | -

Elapsed time since the last canister purging | - | 30 seconds

Outside air temperature | 32 deg.F (0 deg.C) | 103.6 deg.F (39.8 deg.C)

Condition | Minimum | Maximum

Initial engine coolant temperature [ECT Sensor 1] | 32 deg.F (0 deg.C) | 113 deg.F (45 deg.C)

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

[ ]: HDS Parameter

Malfunction Threshold

The difference between the fuel tank pressure and its reference (start) value during compensation gradient determination measurement is less than -0.175 kPa (-1.32 mmHg, -0.0517 inHg).

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- EVAP canister purge valve open stuck

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

## Sources Used

- `pages\6542.html`
- `pages\6543.html`
- `pages\6544.html`
- `pages\6545.html`
- `pages\6546.html`
- `pages\6547.html`
- `pages\6548.html`
- `pages\6549.html`
- `pages\6550.html`
- `pages\6551.html`
- `pages\6552.html`
- `pages\6553.html`
- `pages\6554.html`
- `pages\6555.html`
- `pages\6556.html`
- `pages\6557.html`
- `pages\6558.html`
- `pages\6559.html`
- `pages\6560.html`
- `pages\6561.html`
- `pages\6562.html`
- `pages\6563.html`
- `pages\6564.html`
- `pages\6565.html`
- `pages\6566.html`
- `pages\6567.html`
- `pages\6568.html`
- `pages\6569.html`
- `pages\6570.html`
- `pages\6571.html`
- `pages\6572.html`
- `pages\6573.html`
- `pages\6574.html`
- `pages\6575.html`
- `pages\6576.html`
- `pages\6577.html`
- `pages\6578.html`
- `pages\6579.html`
- `pages\6580.html`
- `pages\6581.html`
- `pages\6582.html`
- `pages\6583.html`
- `pages\6584.html`
- `pages\6585.html`
- `pages\6586.html`
- `pages\6587.html`
- `pages\6588.html`
- `pages\6589.html`
- `pages\6590.html`
- `pages\6591.html`
- `pages\6592.html`
- `pages\6593.html`
- `pages\6594.html`
- `pages\6595.html`
- `pages\6596.html`
- `pages\6597.html`
- `pages\6598.html`
- `pages\6599.html`
- `pages\6600.html`
- `pages\6601.html`
- `pages\6602.html`
- `pages\6603.html`
- `pages\6604.html`
- `pages\6605.html`
- `pages\6606.html`
- `pages\6607.html`
- `pages\6608.html`
- `pages\6609.html`
- `pages\6610.html`
- `pages\6611.html`
- `pages\6612.html`
- `pages\6613.html`
- `pages\6614.html`
- `pages\6615.html`
- `pages\6616.html`
- `pages\6617.html`
- `pages\6618.html`
- `pages\6619.html`
- `pages\6620.html`
- `pages\6621.html`
- `pages\6622.html`
- `pages\6623.html`
- `pages\6624.html`
- `pages\6625.html`
- `pages\6626.html`
- `pages\6627.html`
- `pages\6628.html`
- `pages\6629.html`
- `pages\6630.html`
- `pages\6631.html`
- `pages\6632.html`
- `pages\6633.html`
- `pages\6634.html`
- `pages\6635.html`
- `pages\6636.html`
- `pages\6637.html`
- `pages\6638.html`
- `pages\6639.html`
- `pages\6640.html`
- `pages\6641.html`
- `pages\6642.html`
- `pages\6643.html`
- `pages\6644.html`
- `pages\6645.html`
- `pages\6646.html`
- `pages\6647.html`
- `pages\6648.html`
- `pages\6649.html`
- `pages\6650.html`
- `pages\6651.html`
- `pages\6652.html`
- `pages\6653.html`
- `pages\6654.html`
- `pages\6655.html`
- `pages\6656.html`
- `pages\6657.html`
- `pages\6658.html`
- `pages\6659.html`
- `pages\6660.html`
- `pages\6661.html`
- `pages\6662.html`
- `pages\6663.html`
- `pages\6664.html`
- `pages\6665.html`
- `pages\6666.html`
- `pages\6667.html`
- `pages\6668.html`
- `pages\6669.html`
- `pages\6670.html`
- `pages\6671.html`
- `pages\6672.html`
- `pages\6673.html`
- `pages\6674.html`
- `pages\6675.html`
- `pages\6676.html`
- `pages\6677.html`
- `pages\6678.html`
- `pages\6679.html`
- `pages\6680.html`
- `pages\6681.html`
- `pages\6682.html`
- `pages\6683.html`
- `pages\6684.html`
- `pages\6685.html`
- `pages\6686.html`
- `pages\6687.html`
- `pages\6688.html`
- `pages\6689.html`
- `pages\6690.html`
- `pages\6691.html`
- `pages\6692.html`
- `pages\6693.html`
- `pages\6694.html`
- `pages\6695.html`
- `pages\6696.html`
- `pages\6697.html`
- `pages\6698.html`
- `pages\6699.html`
- `pages\6700.html`
- `pages\6701.html`
- `pages\6702.html`
- `pages\6703.html`
- `pages\6704.html`
- `pages\6705.html`
- `pages\6706.html`
- `pages\6707.html`
- `pages\6708.html`
- `pages\6709.html`
- `pages\6710.html`
- `pages\6711.html`
- `pages\6712.html`
- `pages\6713.html`
- `pages\6714.html`
- `pages\6715.html`
- `pages\6716.html`
- `pages\6717.html`
- `pages\6718.html`
- `pages\6719.html`
- `pages\6720.html`
- `pages\6721.html`
- `pages\6722.html`
- `pages\6723.html`
- `pages\6724.html`
- `pages\6725.html`
- `pages\6726.html`
- `pages\6727.html`
- `pages\6728.html`
- `pages\6729.html`
- `pages\6730.html`
- `pages\6731.html`
- `pages\6732.html`
- `pages\6733.html`
- `pages\6734.html`
- `pages\6735.html`
- `pages\6736.html`
- `pages\6737.html`
- `pages\6738.html`
