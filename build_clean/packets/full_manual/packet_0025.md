# Deep Research Manual Packet 0025

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0025
- Chunk count: 195
- Chunk range: 6116-6310
- Source count: 120
- Target maximum characters: 750000

## Manual Chunks

## Chunk 6116: DTC U0155 (L15B7: With CAN gateway)

- Title: DTC U0155 (L15B7: With CAN gateway)
- Source path: `pages\7239.html`
- Chunk ID: `chunk_bb68bf1b6c2e`
- Images: `images\GHH403739.jpeg`
- Duplicate sources: `pages\8826.html`, `pages\22686.html`, `pages\21099.html`

### Full Text

````text
# DTC U0155 (L15B7: With CAN gateway)

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

- The PCM does not receive any signals via the F-CAN lines for at least 1.5 seconds.

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

## Chunk 6117: DTC U0301 (K20C2 (CVT))

- Title: DTC U0301 (K20C2 (CVT))
- Source path: `pages\7240.html`
- Chunk ID: `chunk_2413d4921d4c`
- Images: `images\GHH403740.jpeg`
- Duplicate sources: `pages\8827.html`, `pages\22687.html`, `pages\21100.html`

### Full Text

````text
# DTC U0301 (K20C2 (CVT))

DTC U0301: PGM-FI System and Transmission System Program Version Mismatch

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) uses two signal lines. TM-CAN_H and TM-CAN_L, and it receives and transmits multiple signals simultaneously to/from multiple control modules. When the software version in the powertrain control module (PCM) and the transmission control module (TCM) are mismatched for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The software version in the PCM and the TCM are mismatched for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM software data not updated

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6118: DTC U0301 (L15B7/L15BA (CVT))

- Title: DTC U0301 (L15B7/L15BA (CVT))
- Source path: `pages\7241.html`
- Chunk ID: `chunk_073495c106c2`
- Images: `images\GHH403741.jpeg`
- Duplicate sources: `pages\8828.html`, `pages\22688.html`, `pages\21101.html`

### Full Text

````text
# DTC U0301 (L15B7/L15BA (CVT))

DTC U0301: PGM-FI System and Transmission System Program Version Mismatch

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) uses two signal lines. TM-CAN_H and TM-CAN_L, and it receives and transmits multiple signals simultaneously to/from multiple control modules. When the software version in the powertrain control module (PCM) and the transmission control module (TCM) are mismatched for a set time, the PCM detects a malfunction and stores a DTC.

Monitor Execution, Sequence, Duration, DTC Type

Execution | Continuous

Sequence | None

Duration | 1 second or more

DTC Type | One drive cycle, MIL on

Enable Conditions

Condition

Vehicle | ON mode

Malfunction Threshold

The software version in the PCM and the TCM are mismatched for at least 1 second.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- PCM software data not updated

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, the MIL comes on and a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory.

Conditions for clearing the DTC

The MIL is cleared if the malfunction does not return in three consecutive trips in which the diagnostic runs. The MIL, the Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6119: DTC U129E (K20C1 (PGM-FI System)) (2019)

- Title: DTC U129E (K20C1 (PGM-FI System)) (2019)
- Source path: `pages\7242.html`
- Chunk ID: `chunk_cd5195089401`
- Images: `images\GHH403742.jpeg`
- Duplicate sources: `pages\8829.html`, `pages\22689.html`, `pages\21102.html`

### Full Text

````text
# DTC U129E (K20C1 (PGM-FI System)) (2019)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the body control module via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

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

- Body control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6120: DTC U129E (K20C1 (PGM-FI System)) (2020 2021)

- Title: DTC U129E (K20C1 (PGM-FI System)) (2020 2021)
- Source path: `pages\7243.html`
- Chunk ID: `chunk_6a00c1feb1aa`
- Images: `images\GHH403743.jpeg`, `images\GHH403744.jpeg`
- Duplicate sources: `pages\8830.html`, `pages\22690.html`, `pages\21103.html`

### Full Text

````text
# DTC U129E (K20C1 (PGM-FI System)) (2020 2021)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Without CAN gateway

Courtesy of HONDA, U.S.A., INC.

With CAN gateway

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the body control module via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

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

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line open

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line open

- F-CAN circuit F-CAN_H* 1, F-CAN A_H* 2 line short to ground

- F-CAN circuit F-CAN_L* 1, F-CAN A_L* 2 line short to ground

- F-CAN circuit F-CAN B_H* 2 line open

- F-CAN circuit F-CAN B_L* 2 line open

- F-CAN circuit F-CAN B_H* 2 line short to ground

- F-CAN circuit F-CAN B_L* 2 line short to ground

- Body control module failure (include fuse fall-outs)

- PCM internal circuit failure

*1: Without CAN gateway

*2: With CAN gateway

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6121: DTC U129E (K20C1) (2017 2018 2019)

- Title: DTC U129E (K20C1) (2017 2018 2019)
- Source path: `pages\7244.html`
- Chunk ID: `chunk_02a1bf493b90`
- Images: `images\GHH403745.jpeg`
- Duplicate sources: `pages\8831.html`, `pages\22691.html`, `pages\21104.html`

### Full Text

````text
# DTC U129E (K20C1) (2017 2018 2019)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the powertrain control module (PCM) does not receive the signals from the body control module via the CAN lines for a certain period of time or receives incorrect message frames, the PCM detects a malfunction and stores a DTC.

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

Vehicle | ON mode

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

- Body control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected during the first drive cycle, a Pending DTC is stored in the PCM memory. If the malfunction returns in the next (second) drive cycle, a Confirmed DTC and the freeze data are stored. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command.
````

## Chunk 6122: DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2016 2017 2018)

- Title: DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2016 2017 2018)
- Source path: `pages\7245.html`
- Chunk ID: `chunk_b6446aa0e341`
- Images: `images\GHH403746.jpeg`
- Duplicate sources: `pages\8832.html`, `pages\22692.html`, `pages\21105.html`

### Full Text

````text
# DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2016 2017 2018)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The PCM does not receive any signals via the F-CAN A lines for at least 1.5 seconds.

- The information sent from the body control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Body control module failure (include fuse fall-outs)

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

## Chunk 6123: DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2019 2020 2021)

- Title: DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2019 2020 2021)
- Source path: `pages\7246.html`
- Chunk ID: `chunk_074f247a31c7`
- Images: `images\GHH403747.jpeg`
- Duplicate sources: `pages\8833.html`, `pages\22693.html`, `pages\21106.html`

### Full Text

````text
# DTC U129E (K20C2 (with CAN gateway) with Keyless Access System) (2019 2020 2021)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The PCM cannot receive any signals from the body control module via the F-CAN A lines for at least 1.5 seconds.

- The information sent from the body control module is abnormal at least 20 times.

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

- Body control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6124: DTC U129E (K20C2 (without CAN gateway) with Keyless Access System)

- Title: DTC U129E (K20C2 (without CAN gateway) with Keyless Access System)
- Source path: `pages\7247.html`
- Chunk ID: `chunk_0517fd48800e`
- Images: `images\GHH403748.jpeg`
- Duplicate sources: `pages\8834.html`, `pages\22694.html`, `pages\21107.html`

### Full Text

````text
# DTC U129E (K20C2 (without CAN gateway) with Keyless Access System)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The information sent from the body control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Body control module failure (include fuse fall-outs)

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

## Chunk 6125: DTC U129E (L15B7/L15BA/L15BY (with CAN gateway) with Keyless Access System (12P connector type))

- Title: DTC U129E (L15B7/L15BA/L15BY (with CAN gateway) with Keyless Access System (12P connector type))
- Source path: `pages\7248.html`
- Chunk ID: `chunk_1a2a6d9eae0f`
- Images: `images\GHH403749.jpeg`
- Duplicate sources: `pages\8835.html`, `pages\22695.html`, `pages\21108.html`

### Full Text

````text
# DTC U129E (L15B7/L15BA/L15BY (with CAN gateway) with Keyless Access System (12P connector type))

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using F-CAN A and B signal lines. When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The information sent from the body control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Body control module failure (include fuse fall-outs)

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

## Chunk 6126: DTC U129E (L15B7/L15BY (with CAN gateway) with Keyless Access System (16P connector type)) (2019 2020 2021)

- Title: DTC U129E (L15B7/L15BY (with CAN gateway) with Keyless Access System (16P connector type)) (2019 2020 2021)
- Source path: `pages\7249.html`
- Chunk ID: `chunk_e8f2a80383e9`
- Images: `images\GHH403750.jpeg`
- Duplicate sources: `pages\8836.html`, `pages\22696.html`, `pages\21109.html`

### Full Text

````text
# DTC U129E (L15B7/L15BY (with CAN gateway) with Keyless Access System (16P connector type)) (2019 2020 2021)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The PCM cannot receive any signals from the body control module via the F-CAN lines for at least 1.5 seconds.

- The information sent from the body control module is abnormal at least 20 times.

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

- Body control module failure (include fuse fall-outs)

- PCM internal circuit failure

Diagnosis Details

Conditions for setting the DTC

When a malfunction is detected, a Pending DTC, a Confirmed DTC, and the freeze data are stored in the PCM memory. The MIL does not come on.

Conditions for clearing the DTC

The Pending DTC, the Confirmed DTC, and the freeze data can be cleared with the scan tool Clear command or by disconnecting the 12 volt battery.
````

## Chunk 6127: DTC U129E (L15B7: Without CAN gateway)

- Title: DTC U129E (L15B7: Without CAN gateway)
- Source path: `pages\7250.html`
- Chunk ID: `chunk_cc8bda2f37c6`
- Images: `images\GHH403751.jpeg`
- Duplicate sources: `pages\8837.html`, `pages\22697.html`, `pages\21110.html`

### Full Text

````text
# DTC U129E (L15B7: Without CAN gateway)

DTC U129E: F-CAN Malfunction (Powertrain Control Module (PCM)-Power Control Unit (PCU))

General Description

Courtesy of HONDA, U.S.A., INC.

The controller area network (CAN) transmits/receives pulsing signals to/from the control modules simultaneously by using two signal lines (F-CAN_H and F-CAN_L). When the information is not sent from the body control module via the F-CAN lines and this condition continues for a specified time or when the information sent from the body control module is abnormal and this condition continues for a specified cycle, the powertrain control module (PCM) detects a malfunction and stores a DTC.

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

- The information sent from the body control module is abnormal at least 20 times.

Possible Cause

NOTE: The causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.

- Body control module failure (include fuse fall-outs)

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

## Chunk 6128: DTC P0016

- Title: DTC P0016
- Source path: `pages\7251.html`
- Chunk ID: `chunk_68339f8df674`
- Images: none
- Duplicate sources: `pages\8838.html`, `pages\22458.html`, `pages\14634.html`

### Full Text

````text
# DTC P0016

DTC P0016 : CMP Sensor A and CKP Sensor Correlation

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0335 and/or P0339 are stored at the same time as DTC P0016, troubleshoot those DTCs first, then recheck for DTC P0016.

DTC Description | Confirmed DTC | Pending DTC

P0016 CMP Sensor A and CKP Sensor Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0016 CMP Sensor A and CKP Sensor Correlation Is DTC P0016 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor, CMP sensor A, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0016 CMP Sensor A and CKP Sensor Correlation

Is DTC P0016 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor, CMP sensor A, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CKP sensor and CMP sensor A installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check that the CKP sensor and CMP sensor A are installed correctly. Are the CKP sensor or CMP sensor A installed correctly? YES Installation is OK. Go to step 3. NO Installation is not correct, reinstall the CKP sensor and/or CMP sensor A.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check that the CKP sensor and CMP sensor A are installed correctly.

Are the CKP sensor or CMP sensor A installed correctly?

YES

Installation is OK. Go to step 3.

NO

Installation is not correct, reinstall the CKP sensor and/or CMP sensor A.

- CMP pulse plate A visual check -1. Remove CMP sensor A , and check for damage to CMP pulse plate A. Is the pulse plate damaged? YES Replace the intake camshaft . NO Go to step 4.

-1. Remove CMP sensor A , and check for damage to CMP pulse plate A.

Is the pulse plate damaged?

YES

Replace the intake camshaft .

NO

Go to step 4.

- Camshaft timing check -1. Check the camshaft timing . Is the camshaft timing OK? YES Go to step 5. NO Reset the camshaft timing .

-1. Check the camshaft timing .

Is the camshaft timing OK?

YES

Go to step 5.

NO

Reset the camshaft timing .

- Cam chain check -1. Check for damage or stretch at the cam chain . Is the cam chain damaged or stretched? YES Replace the cam chain and the cam chain auto-tensioner . NO Go to step 6.

-1. Check for damage or stretch at the cam chain .

Is the cam chain damaged or stretched?

YES

Replace the cam chain and the cam chain auto-tensioner .

NO

Go to step 6.

- CKP sensor check -1. Substitute a known-good CKP sensor . -2. Reconnect all connectors. -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Start the engine. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0016 CMP Sensor A and CKP Sensor Correlation Is DTC P0016 indicated? YES The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0016 goes away and the PCM was substituted, replace the original PCM . NO Replace the original CKP sensor .

-1. Substitute a known-good CKP sensor .

-2. Reconnect all connectors.

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0016 CMP Sensor A and CKP Sensor Correlation

Is DTC P0016 indicated?

YES

The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0016 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original CKP sensor .
````

## Chunk 6129: DTC P0017

- Title: DTC P0017
- Source path: `pages\7252.html`
- Chunk ID: `chunk_188b2b016e41`
- Images: none
- Duplicate sources: `pages\8839.html`, `pages\22459.html`, `pages\14635.html`

### Full Text

````text
# DTC P0017

DTC P0017 : CMP Sensor B and CKP Sensor Correlation

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0335 and/or P0339 are stored at the same time as DTC P0017, troubleshoot those DTCs first, then recheck for DTC P0017.

DTC Description | Confirmed DTC | Pending DTC

P0017 CMP Sensor B and CKP Sensor Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0017 CMP Sensor B and CKP Sensor Correlation Is DTC P0017 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor, CMP sensor B, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0017 CMP Sensor B and CKP Sensor Correlation

Is DTC P0017 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor, CMP sensor B, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CKP sensor and CMP sensor B installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check that the CKP sensor and CMP sensor B are installed correctly. Are the CKP sensor or CMP sensor B installed correctly? YES Installation is OK. Go to step 3. NO Installation is not correct, reinstall the CKP sensor and/or CMP sensor B.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check that the CKP sensor and CMP sensor B are installed correctly.

Are the CKP sensor or CMP sensor B installed correctly?

YES

Installation is OK. Go to step 3.

NO

Installation is not correct, reinstall the CKP sensor and/or CMP sensor B.

- CMP pulse plate B visual check -1. Remove CMP sensor B , and check for damage to CMP pulse plate B. Is the pulse plate damaged? YES Replace the exhaust camshaft . NO Go to step 4.

-1. Remove CMP sensor B , and check for damage to CMP pulse plate B.

Is the pulse plate damaged?

YES

Replace the exhaust camshaft .

NO

Go to step 4.

- Camshaft timing check -1. Check the camshaft timing . Is the camshaft timing OK? YES Go to step 5. NO Reset the camshaft timing .

-1. Check the camshaft timing .

Is the camshaft timing OK?

YES

Go to step 5.

NO

Reset the camshaft timing .

- Cam chain check -1. Check for damage or stretch at the cam chain . Is the cam chain damaged or stretched? YES Replace the cam chain and the cam chain auto-tensioner . NO Go to step 6.

-1. Check for damage or stretch at the cam chain .

Is the cam chain damaged or stretched?

YES

Replace the cam chain and the cam chain auto-tensioner .

NO

Go to step 6.

- CKP sensor check -1. Substitute a known-good CKP sensor . -2. Reconnect all connectors. -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Start the engine. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0017 CMP Sensor B and CKP Sensor Correlation Is DTC P0017 indicated? YES The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0017 goes away and the PCM was substituted, replace the original PCM . NO Replace the original CKP sensor .

-1. Substitute a known-good CKP sensor .

-2. Reconnect all connectors.

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0017 CMP Sensor B and CKP Sensor Correlation

Is DTC P0017 indicated?

YES

The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0017 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original CKP sensor .
````

## Chunk 6130: DTC P0034 (K20C1) (17-21)

- Title: DTC P0034 (K20C1) (17-21)
- Source path: `pages\7253.html`
- Chunk ID: `chunk_dafcf94c4525`
- Images: `images\GHH403812.png`, `images\GHH403813.png`, `images\GHH403814.jpeg`, `images\GHH403815.png`, `images\GHH403816.jpeg`, `images\GHH403817.png`, `images\GHH403818.jpeg`
- Duplicate sources: `pages\8840.html`, `pages\22460.html`, `pages\14636.html`

### Full Text

````text
# DTC P0034 (K20C1) (17-21)

DTC P0034 : Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Do the ABV TEST in the INSPECTION MENU with the HDS. ABV TEST -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage Is DTC P0034 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Do the ABV TEST in the INSPECTION MENU with the HDS.

ABV TEST

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

Is DTC P0034 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Turbocharger bypass control solenoid valve internal circuit check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger bypass control solenoid valve 2P connector -3. At the turbocharger bypass control solenoid valve side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector (male terminals) No. 1 (solenoid valve side): Test point 2 Turbocharger bypass control solenoid valve 2P connector (male terminals) No. 2 (solenoid valve side): Courtesy of HONDA, U.S.A., INC. Is there about 30-34 Ω at room temperature? YES The turbocharger bypass control solenoid valve OK. Go to step 3. NO Replace the turbocharger bypass control solenoid valve .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Turbocharger bypass control solenoid valve 2P connector

-3. At the turbocharger bypass control solenoid valve side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector (male terminals) No. 1 (solenoid valve side):

Test point 2 | Turbocharger bypass control solenoid valve 2P connector (male terminals) No. 2 (solenoid valve side):

Courtesy of HONDA, U.S.A., INC.

Is there about 30-34 Ω at room temperature?

YES

The turbocharger bypass control solenoid valve OK. Go to step 3.

NO

Replace the turbocharger bypass control solenoid valve .

- Fuse check -1. Check the following fuse. Fuse No. A11 (5 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Repair a short in the IGPS(ABV)/IGPS(LAF) wire between the turbocharger bypass control solenoid valve and the No. A11 (5 A) fuse. If needed, replace the under-hood fuse/relay box . Also replace the No. A11 (5 A) fuse.

-1. Check the following fuse.

Fuse | No. A11 (5 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Repair a short in the IGPS(ABV)/IGPS(LAF) wire between the turbocharger bypass control solenoid valve and the No. A11 (5 A) fuse. If needed, replace the under-hood fuse/relay box . Also replace the No. A11 (5 A) fuse.

- Open wire check (IGPS(ABV)/IGPS(LAF) line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 5.
````

## Chunk 6131: DTC P0034 (K20C1) (17-21)

- Title: DTC P0034 (K20C1) (17-21)
- Source path: `pages\7253.html`
- Chunk ID: `chunk_e1e08a2be947`
- Images: `images\GHH403812.png`, `images\GHH403813.png`, `images\GHH403814.jpeg`, `images\GHH403815.png`, `images\GHH403816.jpeg`, `images\GHH403817.png`, `images\GHH403818.jpeg`
- Duplicate sources: `pages\8840.html`, `pages\22460.html`, `pages\14636.html`

### Full Text

````text
A11 (5 A) fuse.

-1. Check the following fuse.

Fuse | No. A11 (5 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Repair a short in the IGPS(ABV)/IGPS(LAF) wire between the turbocharger bypass control solenoid valve and the No. A11 (5 A) fuse. If needed, replace the under-hood fuse/relay box . Also replace the No. A11 (5 A) fuse.

- Open wire check (IGPS(ABV)/IGPS(LAF) line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 5. NO Repair an open in the IGPS(ABV)/IGPS(LAF) wire between the turbocharger bypass control solenoid valve and the No. A11 (5 A) fuse in the under-hood fuse/relay box. If need, replace the under-hood fuse/relay box .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 5.

NO

Repair an open in the IGPS(ABV)/IGPS(LAF) wire between the turbocharger bypass control solenoid valve and the No. A11 (5 A) fuse in the under-hood fuse/relay box. If need, replace the under-hood fuse/relay box .

- Short wire check (ABV line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line wire the HDS. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the ABV wire between PCM connector No. 1 terminal No. 21 and the turbocharger bypass control solenoid valve. NO The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0034 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line wire the HDS.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the ABV wire between PCM connector No. 1 terminal No. 21 and the turbocharger bypass control solenoid valve.

NO

The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0034 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6132: DTC P0034 (L15B7/L15BA/L15BY)

- Title: DTC P0034 (L15B7/L15BA/L15BY)
- Source path: `pages\7254.html`
- Chunk ID: `chunk_2c68966fe693`
- Images: `images\GHH403819.jpeg`, `images\GHH403820.jpeg`, `images\GHH403821.jpeg`
- Duplicate sources: `pages\8841.html`, `pages\22461.html`, `pages\14637.html`

### Full Text

````text
# DTC P0034 (L15B7/L15BA/L15BY)

DTC P0034 : Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Do the ABV TEST in the INSPECTION MENU with the HDS. ABV TEST -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage Is DTC P0034 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Do the ABV TEST in the INSPECTION MENU with the HDS.

ABV TEST

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0034 Turbocharger Bypass Control Solenoid Valve Circuit Low Voltage

Is DTC P0034 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Turbocharger bypass control solenoid valve internal circuit check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger bypass control solenoid valve 2P connector -3. At the solenoid valve side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector No. 1 (solenoid valve side) Test point 2 Turbocharger bypass control solenoid valve 2P connector No. 2 (solenoid valve side) Courtesy of HONDA, U.S.A., INC. Is there about 30-34 Ω at room temperature? YES The turbocharger bypass control solenoid valve OK. Go to step 3. NO Replace the turbocharger bypass control solenoid valve .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Turbocharger bypass control solenoid valve 2P connector

-3. At the solenoid valve side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector No. 1 (solenoid valve side)

Test point 2 | Turbocharger bypass control solenoid valve 2P connector No. 2 (solenoid valve side)

Courtesy of HONDA, U.S.A., INC.

Is there about 30-34 Ω at room temperature?

YES

The turbocharger bypass control solenoid valve OK. Go to step 3.

NO

Replace the turbocharger bypass control solenoid valve .

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 4. NO Repair a short in the IG1 ACG/IG1(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Repair a short in the IG1 ACG/IG1(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG/IG1(ABV) line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 5. NO Repair an open in the IG1 ACG/IG1(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse in the under-dash fuse/relay box. If needed, replace the under-dash fuse/relay box .

-1. Turn the vehicle to the ON mode.

-2.
````

## Chunk 6133: DTC P0034 (L15B7/L15BA/L15BY)

- Title: DTC P0034 (L15B7/L15BA/L15BY)
- Source path: `pages\7254.html`
- Chunk ID: `chunk_2de253309611`
- Images: `images\GHH403819.jpeg`, `images\GHH403820.jpeg`, `images\GHH403821.jpeg`
- Duplicate sources: `pages\8841.html`, `pages\22461.html`, `pages\14637.html`

### Full Text

````text
(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG/IG1(ABV) line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger bypass control solenoid valve 2P connector: disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 5. NO Repair an open in the IG1 ACG/IG1(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse in the under-dash fuse/relay box. If needed, replace the under-dash fuse/relay box .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 5.

NO

Repair an open in the IG1 ACG/IG1(ABV) wire between the turbocharger bypass control solenoid valve and the No. B21 (10 A) fuse in the under-dash fuse/relay box. If needed, replace the under-dash fuse/relay box .

- Short wire check (ABV line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS Short -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the ABV wire between the PCM (E79) and the turbocharger bypass control solenoid valve. NO The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0034 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS Short

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the ABV wire between the PCM (E79) and the turbocharger bypass control solenoid valve.

NO

The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0034 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6134: DTC P0035 (K20C1) (17-21)

- Title: DTC P0035 (K20C1) (17-21)
- Source path: `pages\7255.html`
- Chunk ID: `chunk_9329502e64e9`
- Images: `images\GHH403822.png`, `images\GHH403823.jpeg`
- Duplicate sources: `pages\8842.html`, `pages\22462.html`, `pages\14638.html`

### Full Text

````text
# DTC P0035 (K20C1) (17-21)

DTC P0035 : Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Do the ABV TEST in the INSPECTION MENU with the HDS. ABV TEST -4. Monitor the OBD STATUS for DTC P0035 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage Does the HDS indicate FAILED? YES Go to step 2. NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Do the ABV TEST in the INSPECTION MENU with the HDS.

ABV TEST

-4. Monitor the OBD STATUS for DTC P0035 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

Does the HDS indicate FAILED?

YES

Go to step 2.

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.

- Open wire check (ABV line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line wire the HDS. SCS Short -3. Disconnect the following connectors. Turbocharger bypass control solenoid valve 2P connector PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 21 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0035 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the ABV wire between PCM connector No. 1 terminal No. 21 and the turbocharger bypass control solenoid valve.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line wire the HDS.

SCS Short

-3. Disconnect the following connectors.

Turbocharger bypass control solenoid valve 2P connector

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 21

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0035 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ABV wire between PCM connector No. 1 terminal No. 21 and the turbocharger bypass control solenoid valve.
````

## Chunk 6135: DTC P0035 (L15B7/L15BA/L15BY)

- Title: DTC P0035 (L15B7/L15BA/L15BY)
- Source path: `pages\7256.html`
- Chunk ID: `chunk_287390952206`
- Images: `images\GHH403824.jpeg`
- Duplicate sources: `pages\8843.html`, `pages\22463.html`, `pages\14639.html`

### Full Text

````text
# DTC P0035 (L15B7/L15BA/L15BY)

DTC P0035 : Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Do the ABV TEST in the INSPECTION MENU with the HDS. ABV TEST -4. Monitor the OBD STATUS for DTC P0035 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage Does the HDS indicate FAILED? YES Go to step 2. NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Do the ABV TEST in the INSPECTION MENU with the HDS.

ABV TEST

-4. Monitor the OBD STATUS for DTC P0035 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0035 Turbocharger Bypass Control Solenoid Valve Circuit High Voltage

Does the HDS indicate FAILED?

YES

Go to step 2.

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger bypass control solenoid valve and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.

- Open wire check (ABV line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS Short -3. Disconnect the following connectors. Turbocharger bypass control solenoid valve 2P connector PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger bypass control solenoid valve 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger bypass control solenoid valve 2P connector No. 1 Test point 2 PCM connector E (80P) No. 79 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0035 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the ABV wire between the PCM (E79) and the turbocharger bypass control solenoid valve.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS Short

-3. Disconnect the following connectors.

Turbocharger bypass control solenoid valve 2P connector

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger bypass control solenoid valve 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger bypass control solenoid valve 2P connector No. 1

Test point 2 | PCM connector E (80P) No. 79

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ABV wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0035 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ABV wire between the PCM (E79) and the turbocharger bypass control solenoid valve.
````

## Chunk 6136: DTC P003A, P0046 (K20C1) (17-21)

- Title: DTC P003A, P0046 (K20C1) (17-21)
- Source path: `pages\7257.html`
- Chunk ID: `chunk_0c68453ee2b3`
- Images: `images\GHH403825.png`, `images\GHH403826.png`, `images\GHH403827.jpeg`
- Duplicate sources: `pages\8844.html`, `pages\22464.html`, `pages\14640.html`

### Full Text

````text
# DTC P003A, P0046 (K20C1) (17-21)

DTC P003A : Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

DTC P0046 : Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on. -5. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem Is DTC P003A or P0046 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on.

-5. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

Is DTC P003A or P0046 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Turbocharger check -1. Check for the foreign materials at the turbocharger wastegate control actuator link part and the damage on the exhaust chamber cover. Is there foreign materials at the turbocharger wastegate control actuator link part or the damage on the exhaust chamber cover? YES Repair the turbocharger wastegate control actuator or the exhaust chamber cover, then go to step 1. NO Go to step 3.

-1. Check for the foreign materials at the turbocharger wastegate control actuator link part and the damage on the exhaust chamber cover.

Is there foreign materials at the turbocharger wastegate control actuator link part or the damage on the exhaust chamber cover?

YES

Repair the turbocharger wastegate control actuator or the exhaust chamber cover, then go to step 1.

NO

Go to step 3.

- Turbocharger wastegate control actuator check -1. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -2. Visually inspect the operation of the turbocharger wastegate control actuator. Does the turbocharger wastegate control actuator operate? YES Go to step 4. NO Replace the turbocharger .

-1. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-2. Visually inspect the operation of the turbocharger wastegate control actuator.

Does the turbocharger wastegate control actuator operate?

YES

Go to step 4.

NO

Replace the turbocharger .

- Turbocharger wastegate control actuator position sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 2: Test point 2 Turbocharger 5P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the turbocharger . NO The turbocharger wastegate control actuator position sensor is OK.
````

## Chunk 6137: DTC P003A, P0046 (K20C1) (17-21)

- Title: DTC P003A, P0046 (K20C1) (17-21)
- Source path: `pages\7257.html`
- Chunk ID: `chunk_8b07c2fd79ed`
- Images: `images\GHH403825.png`, `images\GHH403826.png`, `images\GHH403827.jpeg`
- Duplicate sources: `pages\8844.html`, `pages\22464.html`, `pages\14640.html`

### Full Text

````text
spect the operation of the turbocharger wastegate control actuator.

Does the turbocharger wastegate control actuator operate?

YES

Go to step 4.

NO

Replace the turbocharger .

- Turbocharger wastegate control actuator position sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 2: Test point 2 Turbocharger 5P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the turbocharger . NO The turbocharger wastegate control actuator position sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P003A and/or P0046 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Turbocharger 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 2:

Test point 2 | Turbocharger 5P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the turbocharger .

NO

The turbocharger wastegate control actuator position sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P003A and/or P0046 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6138: DTC P003A, P0046 (L15B7/L15BA/L15BY)

- Title: DTC P003A, P0046 (L15B7/L15BA/L15BY)
- Source path: `pages\7258.html`
- Chunk ID: `chunk_b52b98a0428b`
- Images: `images\GHH403828.png`, `images\GHH403829.png`, `images\GHH403830.jpeg`
- Duplicate sources: `pages\8845.html`, `pages\22465.html`, `pages\14641.html`

### Full Text

````text
# DTC P003A, P0046 (L15B7/L15BA/L15BY)

DTC P003A : Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

DTC P0046 : Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on. -4. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem Is DTC P003A or P0046 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

-4. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P003A Turbocharger Wastegate Control Actuator Position Exceeded Learning Limit

P0046 Turbocharger Wastegate Control Actuator Circuit Range/Performance Problem

Is DTC P003A or P0046 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Turbocharger check -1. Check for the foreign materials at the turbocharger wastegate control actuator link part and the damage on the turbocharger cover. Is there foreign materials at the turbocharger wastegate control actuator link part or the damage on the turbocharger cover? YES Repair the turbocharger wastegate control actuator or the turbocharger cover, then go to step 1. NO Go to step 3.

-1. Check for the foreign materials at the turbocharger wastegate control actuator link part and the damage on the turbocharger cover.

Is there foreign materials at the turbocharger wastegate control actuator link part or the damage on the turbocharger cover?

YES

Repair the turbocharger wastegate control actuator or the turbocharger cover, then go to step 1.

NO

Go to step 3.

- Turbocharger wastegate control actuator check -1. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -2. Visually inspect the operation of the turbocharger wastegate control actuator. Does the turbocharger wastegate control actuator operate? YES Go to step 4. NO Replace the turbocharger .

-1. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-2. Visually inspect the operation of the turbocharger wastegate control actuator.

Does the turbocharger wastegate control actuator operate?

YES

Go to step 4.

NO

Replace the turbocharger .

- Determine possible failure area (turbocharger wastegate control actuator position sensor, PCM) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 2: Test point 2 Turbocharger 5P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the turbocharger . NO The turbocharger wastegate control actuator position sensor is OK.
````

## Chunk 6139: DTC P003A, P0046 (L15B7/L15BA/L15BY)

- Title: DTC P003A, P0046 (L15B7/L15BA/L15BY)
- Source path: `pages\7258.html`
- Chunk ID: `chunk_64ddd64cadd6`
- Images: `images\GHH403828.png`, `images\GHH403829.png`, `images\GHH403830.jpeg`
- Duplicate sources: `pages\8845.html`, `pages\22465.html`, `pages\14641.html`

### Full Text

````text
harger wastegate control actuator.

Does the turbocharger wastegate control actuator operate?

YES

Go to step 4.

NO

Replace the turbocharger .

- Determine possible failure area (turbocharger wastegate control actuator position sensor, PCM) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Turbocharger 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 2: Test point 2 Turbocharger 5P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the turbocharger . NO The turbocharger wastegate control actuator position sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P003A or P0046 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Turbocharger 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 2:

Test point 2 | Turbocharger 5P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the turbocharger .

NO

The turbocharger wastegate control actuator position sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P003A or P0046 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6140: DTC P0045 (K20C1) (17-21)

- Title: DTC P0045 (K20C1) (17-21)
- Source path: `pages\7259.html`
- Chunk ID: `chunk_91c32eb7a8c3`
- Images: `images\GHH403831.png`, `images\GHH403832.jpeg`, `images\GHH403833.png`, `images\GHH403834.jpeg`, `images\GHH403835.png`, `images\GHH403836.jpeg`, `images\GHH403837.png`, `images\GHH403838.jpeg`, `images\GHH403839.png`, `images\GHH403840.png`, `images\GHH403841.jpeg`, `images\GHH403842.png`, `images\GHH403843.png`, `images\GHH403844.jpeg`, `images\GHH403845.png`, `images\GHH403846.jpeg`
- Duplicate sources: `pages\8846.html`, `pages\22466.html`, `pages\14642.html`

### Full Text

````text
# DTC P0045 (K20C1) (17-21)

DTC P0045 : Turbocharger Wastegate Control Actuator Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -5. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction Is DTC P0045 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction

Is DTC P0045 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (WGMTR1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS Short -3. Disconnect the following connectors. Turbocharger 5P connector PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR1 wire between PCM connector No. 1 terminal No. 5 and the turbocharger. NO The WGMTR1 wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS Short

-3. Disconnect the following connectors.

Turbocharger 5P connector

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR1 wire between PCM connector No. 1 terminal No. 5 and the turbocharger.

NO

The WGMTR1 wire is not shorted. Go to step 3.

- Shorted wire check (WGMTR2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger. NO The WGMTR2 wire is not shorted. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger.

NO

The WGMTR2 wire is not shorted. Go to step 4.

- Open wire check (WGMTR1 line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6141: DTC P0045 (K20C1) (17-21)

- Title: DTC P0045 (K20C1) (17-21)
- Source path: `pages\7259.html`
- Chunk ID: `chunk_2b36a47c9d53`
- Images: `images\GHH403831.png`, `images\GHH403832.jpeg`, `images\GHH403833.png`, `images\GHH403834.jpeg`, `images\GHH403835.png`, `images\GHH403836.jpeg`, `images\GHH403837.png`, `images\GHH403838.jpeg`, `images\GHH403839.png`, `images\GHH403840.png`, `images\GHH403841.jpeg`, `images\GHH403842.png`, `images\GHH403843.png`, `images\GHH403844.jpeg`, `images\GHH403845.png`, `images\GHH403846.jpeg`
- Duplicate sources: `pages\8846.html`, `pages\22466.html`, `pages\14642.html`

### Full Text

````text
point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger. NO The WGMTR2 wire is not shorted. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger.

NO

The WGMTR2 wire is not shorted. Go to step 4.

- Open wire check (WGMTR1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 5. NO Repair an open in the WGMTR1 wire between PCM connector No. 1 terminal No. 5 and the turbocharger.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 5

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 5.

NO

Repair an open in the WGMTR1 wire between PCM connector No. 1 terminal No. 5 and the turbocharger.

- Open wire check (WGMTR2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 6. NO Repair an open in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 6.

NO

Repair an open in the WGMTR2 wire between PCM connector No. 1 terminal No. 10 and the turbocharger.

- Shorted wire check (WGMTR1 line to WGMTR2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 Turbocharger 5P connector (female terminals) No. 5: Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR1 wire to the WGMTR2 wire between PCM connector No. 1 terminals (No. 5, No. 10) and the turbocharger. NO Go to step 7.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Turbocharger 5P connector (female terminals) No. 5:

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR1 wire to the WGMTR2 wire between PCM connector No. 1 terminals (No. 5, No. 10) and the turbocharger.

NO

Go to step 7.

- Turbocharger wastegate control actuator internal circuit check (short in wires) -1. At the turbocharger side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side): Test point 2 Turbocharger 5P connector (male terminals) No. 5 (turbocharger side): Courtesy of HONDA, U.S.A., INC. Is there about 1.2 Ω - 1.0 kΩ? YES Go to step 8. NO Replace the turbocharger .

-1. At the turbocharger side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected
````

## Chunk 6142: DTC P0045 (K20C1) (17-21)

- Title: DTC P0045 (K20C1) (17-21)
- Source path: `pages\7259.html`
- Chunk ID: `chunk_82b9a4778265`
- Images: `images\GHH403831.png`, `images\GHH403832.jpeg`, `images\GHH403833.png`, `images\GHH403834.jpeg`, `images\GHH403835.png`, `images\GHH403836.jpeg`, `images\GHH403837.png`, `images\GHH403838.jpeg`, `images\GHH403839.png`, `images\GHH403840.png`, `images\GHH403841.jpeg`, `images\GHH403842.png`, `images\GHH403843.png`, `images\GHH403844.jpeg`, `images\GHH403845.png`, `images\GHH403846.jpeg`
- Duplicate sources: `pages\8846.html`, `pages\22466.html`, `pages\14642.html`

### Full Text

````text
urbocharger.

NO

Go to step 7.

- Turbocharger wastegate control actuator internal circuit check (short in wires) -1. At the turbocharger side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side): Test point 2 Turbocharger 5P connector (male terminals) No. 5 (turbocharger side): Courtesy of HONDA, U.S.A., INC. Is there about 1.2 Ω - 1.0 kΩ? YES Go to step 8. NO Replace the turbocharger .

-1. At the turbocharger side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (male terminals) No. 1 (turbocharger side):

Test point 2 | Turbocharger 5P connector (male terminals) No. 5 (turbocharger side):

Courtesy of HONDA, U.S.A., INC.

Is there about 1.2 Ω - 1.0 kΩ?

YES

Go to step 8.

NO

Replace the turbocharger .

- Turbocharger wastegate control actuator internal circuit check (short to ground) -1. At the turbocharger side, check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side) and No. 5 (turbocharger side): Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the turbocharger . NO The turbocharger wastegate control actuator internal circuit is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0045 goes away and the PCM was substituted, replace the original PCM .

-1. At the turbocharger side, check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Turbocharger 5P connector (male terminals) No. 1 (turbocharger side) and No. 5 (turbocharger side):

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the turbocharger .

NO

The turbocharger wastegate control actuator internal circuit is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0045 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6143: DTC P0045 (L15B7/L15BA/L15BY)

- Title: DTC P0045 (L15B7/L15BA/L15BY)
- Source path: `pages\7260.html`
- Chunk ID: `chunk_4d373e9ad51b`
- Images: `images\GHH403847.png`, `images\GHH403848.jpeg`, `images\GHH403849.png`, `images\GHH403850.jpeg`, `images\GHH403851.png`, `images\GHH403852.jpeg`, `images\GHH403853.png`, `images\GHH403854.jpeg`, `images\GHH403855.png`, `images\GHH403856.png`, `images\GHH403857.jpeg`, `images\GHH403858.png`, `images\GHH403859.png`, `images\GHH403860.jpeg`, `images\GHH403861.png`, `images\GHH403862.png`, `images\GHH403863.jpeg`
- Duplicate sources: `pages\8847.html`, `pages\22467.html`, `pages\14643.html`

### Full Text

````text
# DTC P0045 (L15B7/L15BA/L15BY)

DTC P0045 : Turbocharger Wastegate Control Actuator Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -4. Select the Electric Waste Gate in the INSPECTION MENU with the HDS. Electric Waste Gate -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction Is DTC P0045 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-4. Select the Electric Waste Gate in the INSPECTION MENU with the HDS.

Electric Waste Gate

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0045 Turbocharger Wastegate Control Actuator Circuit Malfunction

Is DTC P0045 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger wastegate control actuator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (WGMTR1(+) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. Turbocharger 5P connector PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR1(+) wire between the PCM (E26) and the turbocharger. NO The WGMTR1(+) wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

Turbocharger 5P connector

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR1(+) wire between the PCM (E26) and the turbocharger.

NO

The WGMTR1(+) wire is not shorted. Go to step 3.

- Shorted wire check (WGMTR2(-) line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR2(-) wire between the PCM (E25) and the turbocharger. NO The WGMTR2(-) wire is not shorted. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR2(-) wire between the PCM (E25) and the turbocharger.

NO

The WGMTR2(-) wire is not shorted. Go to step 4.

- Open wire check (WGMTR1(+) line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6144: DTC P0045 (L15B7/L15BA/L15BY)

- Title: DTC P0045 (L15B7/L15BA/L15BY)
- Source path: `pages\7260.html`
- Chunk ID: `chunk_fd5db56b9d9b`
- Images: `images\GHH403847.png`, `images\GHH403848.jpeg`, `images\GHH403849.png`, `images\GHH403850.jpeg`, `images\GHH403851.png`, `images\GHH403852.jpeg`, `images\GHH403853.png`, `images\GHH403854.jpeg`, `images\GHH403855.png`, `images\GHH403856.png`, `images\GHH403857.jpeg`, `images\GHH403858.png`, `images\GHH403859.png`, `images\GHH403860.jpeg`, `images\GHH403861.png`, `images\GHH403862.png`, `images\GHH403863.jpeg`
- Duplicate sources: `pages\8847.html`, `pages\22467.html`, `pages\14643.html`

### Full Text

````text
or (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR2(-) wire between the PCM (E25) and the turbocharger. NO The WGMTR2(-) wire is not shorted. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR2(-) wire between the PCM (E25) and the turbocharger.

NO

The WGMTR2(-) wire is not shorted. Go to step 4.

- Open wire check (WGMTR1(+) line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 26 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 5. NO Repair an open in the WGMTR1(+) wire between the PCM (E26) and the turbocharger.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 5:

Test point 2 | PCM connector E (80P) No. 26

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 5.

NO

Repair an open in the WGMTR1(+) wire between the PCM (E26) and the turbocharger.

- Open wire check (WGMTR2(-) line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Turbocharger 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 6. NO Repair an open in the WGMTR2(-) wire between the PCM (E25) and the turbocharger.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Turbocharger 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 6.

NO

Repair an open in the WGMTR2(-) wire between the PCM (E25) and the turbocharger.

- Shorted wire check (WGMTR1(+) line to WGMTR2(-) line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (female terminals) No. 1: Test point 2 Turbocharger 5P connector (female terminals) No. 5: Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the WGMTR1(+) wire to the WGMTR2(-) wire between the PCM (E25, E26) and the turbocharger. NO Go to step 7.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (female terminals) No. 1:

Test point 2 | Turbocharger 5P connector (female terminals) No. 5:

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the WGMTR1(+) wire to the WGMTR2(-) wire between the PCM (E25, E26) and the turbocharger.

NO

Go to step 7.

- Turbocharger wastegate control actuator internal circuit check (short in wires) -1. At the turbocharger side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side): Test point 2 Turbocharger 5P connector (male terminals) No. 5 (turbocharger side): Courtesy of HONDA, U.S.A., INC. Is there about 1.2Ω - 1.0 kΩ? YES Go to step 8. NO Replace the turbocharger .

-1. At the turbocharger side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (male terminals) No. 1 (turbocharger side):

Test point 2 | Turbocharger 5P connector (male terminals) No.
````

## Chunk 6145: DTC P0045 (L15B7/L15BA/L15BY)

- Title: DTC P0045 (L15B7/L15BA/L15BY)
- Source path: `pages\7260.html`
- Chunk ID: `chunk_92b211b405d1`
- Images: `images\GHH403847.png`, `images\GHH403848.jpeg`, `images\GHH403849.png`, `images\GHH403850.jpeg`, `images\GHH403851.png`, `images\GHH403852.jpeg`, `images\GHH403853.png`, `images\GHH403854.jpeg`, `images\GHH403855.png`, `images\GHH403856.png`, `images\GHH403857.jpeg`, `images\GHH403858.png`, `images\GHH403859.png`, `images\GHH403860.jpeg`, `images\GHH403861.png`, `images\GHH403862.png`, `images\GHH403863.jpeg`
- Duplicate sources: `pages\8847.html`, `pages\22467.html`, `pages\14643.html`

### Full Text

````text
side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side): Test point 2 Turbocharger 5P connector (male terminals) No. 5 (turbocharger side): Courtesy of HONDA, U.S.A., INC. Is there about 1.2Ω - 1.0 kΩ? YES Go to step 8. NO Replace the turbocharger .

-1. At the turbocharger side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (male terminals) No. 1 (turbocharger side):

Test point 2 | Turbocharger 5P connector (male terminals) No. 5 (turbocharger side):

Courtesy of HONDA, U.S.A., INC.

Is there about 1.2Ω - 1.0 kΩ?

YES

Go to step 8.

NO

Replace the turbocharger .

- Turbocharger wastegate control actuator internal circuit check (short to ground) -1. At the turbocharger side, check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Turbocharger 5P connector: disconnected Test point 1 Turbocharger 5P connector (male terminals) No. 1 (turbocharger side): Turbocharger 5P connector (male terminals) No. 5 (turbocharger side): Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the turbocharger . NO The turbocharger wastegate control actuator internal circuit is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0045 goes away and the PCM was substituted, replace the original PCM .

-1. At the turbocharger side, check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Turbocharger 5P connector: disconnected

Test point 1 | Turbocharger 5P connector (male terminals) No. 1 (turbocharger side):

Turbocharger 5P connector (male terminals) No. 5 (turbocharger side):

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the turbocharger .

NO

The turbocharger wastegate control actuator internal circuit is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0045 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6146: DTC P0068

- Title: DTC P0068
- Source path: `pages\7261.html`
- Chunk ID: `chunk_e62d94d2add5`
- Images: none
- Duplicate sources: `pages\8848.html`, `pages\22468.html`, `pages\14644.html`

### Full Text

````text
# DTC P0068

DTC P0068 : Throttle Position Correlation

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0068 Throttle Position Correlation

DTC (PGM-FI)

- Throttle body condition check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body . -3. Check for sludge or carbon on the throttle valve. Is there sludge or carbon on the throttle valve? YES Clean the throttle body . NO Go to step 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body .

-3. Check for sludge or carbon on the throttle valve.

Is there sludge or carbon on the throttle valve?

YES

Clean the throttle body .

NO

Go to step 2.

- Problem verification -1. Reconnect the throttle body inlet pipe and the throttle body connector tube to the throttle body . -2. Record all the on-board snapshots with the HDS. -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Start the engine. -6. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0068 Throttle Position Correlation Is DTC P0068 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1, MAP sensor/IAT sensor 2, the turbocharger boost sensor, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Reconnect the throttle body inlet pipe and the throttle body connector tube to the throttle body .

-2. Record all the on-board snapshots with the HDS.

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine.

-6. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- Engine Speed

- Vehicle Speed

- MAP Sensor (Hi Res)

- TC Boost Pressure

- Baro Sensor

- REL TP Sensor

On-board Snapshot

Signal | Current conditions

Values | Unit

Engine Speed

Vehicle Speed

MAP Sensor (Hi Res)

TC Boost Pressure

Baro Sensor

REL TP Sensor

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0068 Throttle Position Correlation

Is DTC P0068 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1, MAP sensor/IAT sensor 2, the turbocharger boost sensor, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Sensor signal check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit Baro Sensor TC Boost Pressure MAP Sensor (Hi Res) -4. Check the difference of A: Baro Sensor and TC Boost Pressure, and B: Baro Sensor and MAP Sensor (Hi Res), then compare the results with the following table. A (Difference of Baro Sensor and TC Boost Sensor) B (Difference of Baro Sensor and MAP Sensor (Hi Res)) Pattern 1 Almost 0 Difference exists Pattern 2 Difference exists Almost 0 Pattern 3 Almost 0 Almost 0 Pattern 4 Difference exists nearly the same as B Difference exists nearly the same as A Which pattern do the results match? Pattern 1 Go to step 4. Pattern 2 Go to step 5. Pattern 3 Go to step 4. Pattern 4 Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

Baro Sensor

TC Boost Pressure
````

## Chunk 6147: DTC P0068

- Title: DTC P0068
- Source path: `pages\7261.html`
- Chunk ID: `chunk_9b942e71a238`
- Images: none
- Duplicate sources: `pages\8848.html`, `pages\22468.html`, `pages\14644.html`

### Full Text

````text
Res) -4. Check the difference of A: Baro Sensor and TC Boost Pressure, and B: Baro Sensor and MAP Sensor (Hi Res), then compare the results with the following table. A (Difference of Baro Sensor and TC Boost Sensor) B (Difference of Baro Sensor and MAP Sensor (Hi Res)) Pattern 1 Almost 0 Difference exists Pattern 2 Difference exists Almost 0 Pattern 3 Almost 0 Almost 0 Pattern 4 Difference exists nearly the same as B Difference exists nearly the same as A Which pattern do the results match? Pattern 1 Go to step 4. Pattern 2 Go to step 5. Pattern 3 Go to step 4. Pattern 4 Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

Baro Sensor

TC Boost Pressure

MAP Sensor (Hi Res)

-4. Check the difference of A: Baro Sensor and TC Boost Pressure, and B: Baro Sensor and MAP Sensor (Hi Res), then compare the results with the following table.

A (Difference of Baro Sensor and TC Boost Sensor) | B (Difference of Baro Sensor and MAP Sensor (Hi Res))

Pattern 1 | Almost 0 | Difference exists

Pattern 2 | Difference exists | Almost 0

Pattern 3 | Almost 0 | Almost 0

Pattern 4 | Difference exists nearly the same as B | Difference exists nearly the same as A

Which pattern do the results match?

Pattern 1

Go to step 4.

Pattern 2

Go to step 5.

Pattern 3

Go to step 4.

Pattern 4

Go to step 4.

- MAP sensor/IAT sensor 2 check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Substitute a known-good MAP sensor/IAT sensor 2 . -3. Reconnect all connectors. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Start the engine. -7. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor -8. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0068 Throttle Position Correlation Is DTC P0068 indicated? YES MAP sensor/IAT sensor 2 is OK. Replace the turbocharger boost sensor and recheck. If DTC P0068 is indicated again, replace the throttle body . NO Replace original MAP sensor/IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Substitute a known-good MAP sensor/IAT sensor 2 .

-3. Reconnect all connectors.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Start the engine.

-7. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- Engine Speed

- Vehicle Speed

- MAP Sensor (Hi Res)

- TC Boost Pressure

- Baro Sensor

- REL TP Sensor

On-board Snapshot

Signal | Current conditions

Values | Unit

Engine Speed

Vehicle Speed

MAP Sensor (Hi Res)

TC Boost Pressure

Baro Sensor

REL TP Sensor

-8. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0068 Throttle Position Correlation

Is DTC P0068 indicated?

YES

MAP sensor/IAT sensor 2 is OK. Replace the turbocharger boost sensor and recheck. If DTC P0068 is indicated again, replace the throttle body .

NO

Replace original MAP sensor/IAT sensor 2 .

- Turbocharger boost sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Substitute a known-good turbocharger boost sensor . -3. Reconnect all connectors. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Start the engine. -7. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor -8. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0068 Throttle Position Correlation Is DTC P0068 indicated? YES The turbocharger boost sensor is OK. Replace MAP sensor/IAT sensor 2 and recheck. If DTC P0068 is indicated again, replace the throttle body . NO Replace the original turbocharger boost sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Substitute a known-good turbocharger boost sensor .

-3. Reconnect all connectors.

-4.
````

## Chunk 6148: DTC P0068

- Title: DTC P0068
- Source path: `pages\7261.html`
- Chunk ID: `chunk_865bfef83e59`
- Images: none
- Duplicate sources: `pages\8848.html`, `pages\22468.html`, `pages\14644.html`

### Full Text

````text
minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed MAP Sensor (Hi Res) TC Boost Pressure Baro Sensor REL TP Sensor -8. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0068 Throttle Position Correlation Is DTC P0068 indicated? YES The turbocharger boost sensor is OK. Replace MAP sensor/IAT sensor 2 and recheck. If DTC P0068 is indicated again, replace the throttle body . NO Replace the original turbocharger boost sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Substitute a known-good turbocharger boost sensor .

-3. Reconnect all connectors.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Start the engine.

-7. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- Engine Speed

- Vehicle Speed

- MAP Sensor (Hi Res)

- TC Boost Pressure

- Baro Sensor

- REL TP Sensor

On-board Snapshot

Signal | Current conditions

Values | Unit

Engine Speed

Vehicle Speed

MAP Sensor (Hi Res)

TC Boost Pressure

Baro Sensor

REL TP Sensor

-8. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0068 Throttle Position Correlation

Is DTC P0068 indicated?

YES

The turbocharger boost sensor is OK. Replace MAP sensor/IAT sensor 2 and recheck. If DTC P0068 is indicated again, replace the throttle body .

NO

Replace the original turbocharger boost sensor .
````

## Chunk 6149: DTC P0069 (K20C2)

- Title: DTC P0069 (K20C2)
- Source path: `pages\7262.html`
- Chunk ID: `chunk_d8fb02151181`
- Images: none
- Duplicate sources: `pages\8849.html`, `pages\22469.html`, `pages\14645.html`

### Full Text

````text
# DTC P0069 (K20C2)

DTC P0069 : BARO Sensor Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0069 BARO Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0069 BARO Sensor Circuit Range/Performance Problem Is DTC P0069 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0069 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0069 BARO Sensor Circuit Range/Performance Problem

Is DTC P0069 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0069 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6150: DTC P0069 (L15B7/L15BA/L15BY)

- Title: DTC P0069 (L15B7/L15BA/L15BY)
- Source path: `pages\7263.html`
- Chunk ID: `chunk_4c47b825deb7`
- Images: none
- Duplicate sources: `pages\8850.html`, `pages\22470.html`, `pages\14646.html`

### Full Text

````text
# DTC P0069 (L15B7/L15BA/L15BY)

DTC P0069 : BARO Sensor Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0069 BARO Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle under these conditions: Engine speed above 1, 700 rpm REL TP SENSOR above 42.2 deg Drive 6 seconds or more Signal Current conditions Values Unit ECT SENSOR 1 ENGINE SPEED REL TP Sensor -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0069 BARO Sensor Circuit Range/Performance Problem Is DTC P0069 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0069 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle under these conditions:

- Engine speed above 1, 700 rpm

- REL TP SENSOR above 42.2 deg

- Drive 6 seconds or more

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ENGINE SPEED

REL TP Sensor

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0069 BARO Sensor Circuit Range/Performance Problem

Is DTC P0069 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0069 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6151: DTC P006A (K20C2)

- Title: DTC P006A (K20C2)
- Source path: `pages\7264.html`
- Chunk ID: `chunk_c20e0b46f074`
- Images: none
- Duplicate sources: `pages\8851.html`, `pages\22471.html`, `pages\14647.html`

### Full Text

````text
# DTC P006A (K20C2)

DTC P006A : MAF Sensor Circuit Range/Performance Problem

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2073, P2074, P2228, and/or P2229 are stored at the same time as DTC P006A, troubleshoot those DTCs first, then recheck for DTC P006A.

DTC Description | Confirmed DTC | Pending DTC

P006A MAF Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV valve PCV hose Intake air duct Air cleaner Purge (PCS) line Brake booster Brake booster hose Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV valve

- PCV hose

- Intake air duct

- Air cleaner

- Purge (PCS) line

- Brake booster

- Brake booster hose

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- Intake air duct visual check -1. Check for damage or looseness of the intake air duct from the throttle body to the air cleaner. Is it OK? YES Go to step 3. NO Reconnect or replace the intake air duct from the throttle body to the air cleaner.

-1. Check for damage or looseness of the intake air duct from the throttle body to the air cleaner.

Is it OK?

YES

Go to step 3.

NO

Reconnect or replace the intake air duct from the throttle body to the air cleaner.

- Air cleaner element visual check -1. Check for a dirty air cleaner element. Is it dirty? YES Replace the air cleaner element . NO Go to step 4.

-1. Check for a dirty air cleaner element.

Is it dirty?

YES

Replace the air cleaner element .

NO

Go to step 4.

- MAF sensor signal check (without engine running) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR About 0.2 g/s Do the current condition(s) match the threshold? YES Go to step 5. NO Replace the MAF sensor/IAT sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | About 0.2 | g/s

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace the MAF sensor/IAT sensor .

- MAF sensor signal check (with engine running) -1. Start the engine. -2. Vary the engine speed between 2, 000 rpm and 3000 RPM. -3. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit MAF SENSOR Does the MAF SENSOR reading change? YES Go to step 6. NO Replace the MAF sensor/IAT sensor .

-1. Start the engine.

-2. Vary the engine speed between 2, 000 rpm and 3000 RPM.

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

MAF SENSOR

Does the MAF SENSOR reading change?

YES

Go to step 6.

NO

Replace the MAF sensor/IAT sensor .

- MAF sensor check -1. Hold the engine speed at 3000 RPM without load (in P or N) until the radiator fan comes on, then let it idle. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR -3. Monitor the OBD STATUS for DTC P006A with the HDS. DTC Description OBD STATUS P006A MAF Sensor Circuit Range/Performance Problem Does the HDS indicate FAILED? YES Replace the MAF sensor/IAT sensor . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (in P or N) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P006A with the HDS.

DTC Description | OBD STATUS

P006A MAF Sensor Circuit Range/Performance Problem
````

## Chunk 6152: DTC P006A (K20C2)

- Title: DTC P006A (K20C2)
- Source path: `pages\7264.html`
- Chunk ID: `chunk_646669368cc4`
- Images: none
- Duplicate sources: `pages\8851.html`, `pages\22471.html`, `pages\14647.html`

### Full Text

````text
ections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (in P or N) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P006A with the HDS.

DTC Description | OBD STATUS

P006A MAF Sensor Circuit Range/Performance Problem

Does the HDS indicate FAILED?

YES

Replace the MAF sensor/IAT sensor .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.
````

## Chunk 6153: DTC P006A (L15B7/L15BA/L15BY)

- Title: DTC P006A (L15B7/L15BA/L15BY)
- Source path: `pages\7265.html`
- Chunk ID: `chunk_d183c613d193`
- Images: none
- Duplicate sources: `pages\8852.html`, `pages\22472.html`, `pages\14648.html`

### Full Text

````text
# DTC P006A (L15B7/L15BA/L15BY)

DTC P006A : MAF Sensor Circuit Range/Performance Problem

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2228 and/or P2229 are stored at the same time as DTC P006A, troubleshoot those DTCs first, then recheck for DTC P006A.

DTC Description | Confirmed DTC | Pending DTC

P006A MAF Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV valve PCV hose Air cleaner Intake air duct Purge (PCS) line Brake booster Brake booster hose All parts through the turbocharger joint to the throttle body Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV valve

- PCV hose

- Air cleaner

- Intake air duct

- Purge (PCS) line

- Brake booster

- Brake booster hose

- All parts through the turbocharger joint to the throttle body

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- Intake air duct visual check -1. Check for damage or looseness at the intake air duct. Is it OK? YES Go to step 3. NO Reconnect or replace the intake air duct.

-1. Check for damage or looseness at the intake air duct.

Is it OK?

YES

Go to step 3.

NO

Reconnect or replace the intake air duct.

- Air cleaner element visual check -1. Check for a dirty air cleaner element. Is it dirty? YES Replace the air cleaner element . NO Go to step 4.

-1. Check for a dirty air cleaner element.

Is it dirty?

YES

Replace the air cleaner element .

NO

Go to step 4.

- MAF sensor signal check (without engine running) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR About 0.2 g/s Do the current condition(s) match the threshold? YES Go to step 5. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | About 0.2 | g/s

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace MAF sensor/IAT sensor 1 .

- MAF sensor signal check (with engine running) -1. Start the engine. -2. Vary the engine speed between 2, 000 rpm and 3000 RPM. -3. Check the MAF SENSOR in the DATA LIST with the HDS. Signal Current conditions Values Unit MAF SENSOR Does the reading change? YES Go to step 6. NO Replace MAF sensor/IAT sensor 1 .

-1. Start the engine.

-2. Vary the engine speed between 2, 000 rpm and 3000 RPM.

-3. Check the MAF SENSOR in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

MAF SENSOR

Does the reading change?

YES

Go to step 6.

NO

Replace MAF sensor/IAT sensor 1 .

- MAF sensor check -1. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR -3. Monitor the OBD STATUS for DTC P006A with the HDS. DTC Description OBD STATUS P006A MAF Sensor Circuit Range/Performance Problem Does the HDS indicate FAILED? YES Replace MAF sensor/IAT sensor 1 . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P006A with the HDS.

DTC Description | OBD STATUS

P006A MAF Sensor Circuit Range/Performance Problem

Does the HDS indicate FAILED?

YES
````

## Chunk 6154: DTC P006A (L15B7/L15BA/L15BY)

- Title: DTC P006A (L15B7/L15BA/L15BY)
- Source path: `pages\7265.html`
- Chunk ID: `chunk_88ccd32955df`
- Images: none
- Duplicate sources: `pages\8852.html`, `pages\22472.html`, `pages\14648.html`

### Full Text

````text
and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P006A with the HDS.

DTC Description | OBD STATUS

P006A MAF Sensor Circuit Range/Performance Problem

Does the HDS indicate FAILED?

YES

Replace MAF sensor/IAT sensor 1 .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.
````

## Chunk 6155: DTC P006E (L15B7)

- Title: DTC P006E (L15B7)
- Source path: `pages\7266.html`
- Chunk ID: `chunk_8aa4cf061ba4`
- Images: `images\GHH403864.jpeg`
- Duplicate sources: `pages\8853.html`, `pages\22473.html`, `pages\14649.html`

### Full Text

````text
# DTC P006E (L15B7)

DTC P006E : Turbocharger Power Supply Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P006E Turbocharger Power Supply Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P006E Turbocharger Power Supply Circuit Malfunction Is DTC P006E indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P006E Turbocharger Power Supply Circuit Malfunction

Is DTC P006E indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1658 ETCS Control Relay ON Malfunction P1659 ETCS Control Relay OFF Malfunction Is DTC P1658 and/or P1659 indicated? YES Go to the indicated DTC's troubleshooting. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1658 ETCS Control Relay ON Malfunction

P1659 ETCS Control Relay OFF Malfunction

Is DTC P1658 and/or P1659 indicated?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to step 3.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A27 (10 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A27 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (VB ACT/FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector C (18P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board connector C (18P): disconnected PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 1 Test point 2 PCM connector A (50P) No. 3 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VB ACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P006E goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VB ACT/FI SUB RLY OUT wire between the PCM (A3) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector C (18P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector C (18P): disconnected

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 1

Test point 2 | PCM connector A (50P) No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VB ACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P006E goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VB ACT/FI SUB RLY OUT wire between the PCM (A3) and the relay circuit board.

- Shorted wire check (VB ACT line) -1. Remove the blown No. A27 (10 A) fuse from the under-hood fuse/relay box. -2.
````

## Chunk 6156: DTC P006E (L15B7)

- Title: DTC P006E (L15B7)
- Source path: `pages\7266.html`
- Chunk ID: `chunk_82b9292288ea`
- Images: `images\GHH403864.jpeg`
- Duplicate sources: `pages\8853.html`, `pages\22473.html`, `pages\14649.html`

### Full Text

````text
ard connector C (18P): disconnected

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 1

Test point 2 | PCM connector A (50P) No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VB ACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P006E goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VB ACT/FI SUB RLY OUT wire between the PCM (A3) and the relay circuit board.

- Shorted wire check (VB ACT line) -1. Remove the blown No. A27 (10 A) fuse from the under-hood fuse/relay box. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector A (50P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 3 Test point 2 Body ground Is there continuity? YES Repair a short in the VB ACT wire between the PCM (A3) and the No. A27 (10 A) fuse in the under-hood fuse/relay box. Also replace No. A27 (10 A) fuse. NO Replace the No. A27 (10 A) fuse in the under-hood fuse/relay box and recheck. If the fuse blown again, replace the under-hood fuse/relay box .

-1. Remove the blown No. A27 (10 A) fuse from the under-hood fuse/relay box.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 3

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the VB ACT wire between the PCM (A3) and the No. A27 (10 A) fuse in the under-hood fuse/relay box. Also replace No. A27 (10 A) fuse.

NO

Replace the No. A27 (10 A) fuse in the under-hood fuse/relay box and recheck. If the fuse blown again, replace the under-hood fuse/relay box .
````

## Chunk 6157: DTC P006E (L15BA/L15BY) (17-21)

- Title: DTC P006E (L15BA/L15BY) (17-21)
- Source path: `pages\7267.html`
- Chunk ID: `chunk_99d0e997b2ec`
- Images: `images\GHH403865.png`, `images\GHH403866.jpeg`
- Duplicate sources: `pages\8854.html`, `pages\22474.html`, `pages\14650.html`

### Full Text

````text
# DTC P006E (L15BA/L15BY) (17-21)

DTC P006E : Turbocharger Power Supply Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P006E Turbocharger Power Supply Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P006E Turbocharger Power Supply Circuit Malfunction Is DTC P006E indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P006E Turbocharger Power Supply Circuit Malfunction

Is DTC P006E indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1658 ETCS Control Relay ON Malfunction P1659 ETCS Control Relay OFF Malfunction Is DTC P1658 and/or P1659 indicated? YES Go to the indicated DTC's troubleshooting. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1658 ETCS Control Relay ON Malfunction

P1659 ETCS Control Relay OFF Malfunction

Is DTC P1658 and/or P1659 indicated?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to step 3.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A33 (5 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Repair a short in the +B VBACT wire between the PCM (A3) and the No. A33 (5 A) fuse. Also replace No. A33 (5 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A33 (5 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Repair a short in the +B VBACT wire between the PCM (A3) and the No. A33 (5 A) fuse. Also replace No. A33 (5 A) fuse.

- Open wire check (+B VBACT/FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector C (18P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board connector C (18P): disconnected PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 11: Test point 2 PCM connector A (50P) No. 3 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The +B VBACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P006E goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the +B VBACT/FI SUB RLY OUT wire between the PCM (A3) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector C (18P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector C (18P): disconnected

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 11:

Test point 2 | PCM connector A (50P) No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The +B VBACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6158: DTC P006E (L15BA/L15BY) (17-21)

- Title: DTC P006E (L15BA/L15BY) (17-21)
- Source path: `pages\7267.html`
- Chunk ID: `chunk_7cc33dcfd822`
- Images: `images\GHH403865.png`, `images\GHH403866.jpeg`
- Duplicate sources: `pages\8854.html`, `pages\22474.html`, `pages\14650.html`

### Full Text

````text
mp the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector C (18P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector C (18P): disconnected

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 11:

Test point 2 | PCM connector A (50P) No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The +B VBACT/FI SUB RLY OUT wire is OK. Remove and test the relay circuit board . If the relay circuit board is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P006E goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the +B VBACT/FI SUB RLY OUT wire between the PCM (A3) and the relay circuit board.
````

## Chunk 6159: DTC P0087 (K20C1) (17-21)

- Title: DTC P0087 (K20C1) (17-21)
- Source path: `pages\7268.html`
- Chunk ID: `chunk_331ec8eec237`
- Images: none
- Duplicate sources: `pages\8855.html`, `pages\22475.html`, `pages\14651.html`

### Full Text

````text
# DTC P0087 (K20C1) (17-21)

DTC P0087 : Fuel Rail Pressure Too Low

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the vehicle was out of fuel and the engine stalled before this DTC was stored, refuel, then clear the DTC with the HDS.

- If a fuel leak occurs, this DTC will be stored. Repair the fuel leak before troubleshooting.

- If any of the DTCs listed below are stored at the same time as P0087, troubleshoot those DTCs first, then recheck for P0087. P0190, P0191, P0192, P0193: Fuel rail pressure sensor P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s) P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s) P2623: High pressure fuel pump

P0190, P0191, P0192, P0193: Fuel rail pressure sensor

P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s)

P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire

P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s)

P2623: High pressure fuel pump

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

DTC (PGM-FI)

- Problem verification (idling) -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Start the engine. -5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS. DI Fuel Pressure Test Is the result OK? YES Go to step 2. NO The failure is duplicated. Go to step 3.

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Start the engine.

-5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS.

DI Fuel Pressure Test

Is the result OK?

YES

Go to step 2.

NO

The failure is duplicated. Go to step 3.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 Signal Current conditions Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0087 Fuel Rail Pressure Too Low Is DTC P0087 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

- APP SENSOR

- ECT SENSOR 1

- FUEL PRESSURE CONVERTED FROM PF SENSOR

- FUEL PRESSURE DIRECT INJECTION SYSTEM

- IAT SENSOR (1)

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

APP SENSOR

ECT SENSOR 1

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

Is DTC P0087 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Spill valve operation check -1. Start the engine, then let it idle. -2.
````

## Chunk 6160: DTC P0087 (K20C1) (17-21)

- Title: DTC P0087 (K20C1) (17-21)
- Source path: `pages\7268.html`
- Chunk ID: `chunk_5ecd15a35c05`
- Images: none
- Duplicate sources: `pages\8855.html`, `pages\22475.html`, `pages\14651.html`

### Full Text

````text
OR

ECT SENSOR 1

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

Is DTC P0087 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Spill valve operation check -1. Start the engine, then let it idle. -2. Check for noise or vibration from the spill valve on the high pressure fuel pump. When the high pressure fuel pump runs, you will hear some noise from the spill valve. Is there any noise or vibration? YES Go to step 4. NO Replace the high pressure fuel pump .

-1. Start the engine, then let it idle.

-2. Check for noise or vibration from the spill valve on the high pressure fuel pump.

When the high pressure fuel pump runs, you will hear some noise from the spill valve.

Is there any noise or vibration?

YES

Go to step 4.

NO

Replace the high pressure fuel pump .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4. After the engine stalls, crank the engine for several times. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR Less than 2, 000 kPa NOTE: It is normal if the value of several hundred kPa is indicated. Do the current condition(s) match the threshold? YES Go to step 5. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove PGM-FI main relay 2 .

-3. Start the engine, and let it idle until it stalls.

-4. After the engine stalls, crank the engine for several times.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR | Less than 2, 000 | kPa

NOTE: It is normal if the value of several hundred kPa is indicated.

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel rail pressure sensor check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Install PGM-FI main relay 2 . -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -5. Snap the throttle for several times. -6. Check the parameter(s) below with the HDS. NOTE: Use the Line Graph Setup mode with the HDS to compare the values. Signal Current conditions Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM Are both values almost the same? YES The fuel rail pressure sensor is OK. Go to step 6. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Install PGM-FI main relay 2 .

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Snap the throttle for several times.

-6. Check the parameter(s) below with the HDS.

NOTE: Use the Line Graph Setup mode with the HDS to compare the values.

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

Are both values almost the same?

YES

The fuel rail pressure sensor is OK. Go to step 6.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 7. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

The fuel pressure (low pressure side) is OK. Go to step 7.

NO

Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

- High pressure fuel pump cam and pump lifter visual check -1. Remove the high pressure fuel pump . -2.
````

## Chunk 6161: DTC P0087 (K20C1) (17-21)

- Title: DTC P0087 (K20C1) (17-21)
- Source path: `pages\7268.html`
- Chunk ID: `chunk_8b61bbecb38e`
- Images: none
- Duplicate sources: `pages\8855.html`, `pages\22475.html`, `pages\14651.html`

### Full Text

````text
FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

Are both values almost the same?

YES

The fuel rail pressure sensor is OK. Go to step 6.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 7. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

The fuel pressure (low pressure side) is OK. Go to step 7.

NO

Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

- High pressure fuel pump cam and pump lifter visual check -1. Remove the high pressure fuel pump . -2. Visually check the cam that drives the high pressure fuel pump and the pump lifter of the high pressure fuel pump for wear or damage . Are the parts OK? YES Replace the high pressure fuel pump . NO Check for damage of the cam and the pump lifter , and replace the exhaust camshaft and/or the high pressure fuel pump if needed.

-1. Remove the high pressure fuel pump .

-2. Visually check the cam that drives the high pressure fuel pump and the pump lifter of the high pressure fuel pump for wear or damage .

Are the parts OK?

YES

Replace the high pressure fuel pump .

NO

Check for damage of the cam and the pump lifter , and replace the exhaust camshaft and/or the high pressure fuel pump if needed.
````

## Chunk 6162: DTC P0087 (L15B7/L15BA/L15BY)

- Title: DTC P0087 (L15B7/L15BA/L15BY)
- Source path: `pages\7269.html`
- Chunk ID: `chunk_54c827fa5b76`
- Images: none
- Duplicate sources: `pages\8856.html`, `pages\22476.html`, `pages\14652.html`

### Full Text

````text
# DTC P0087 (L15B7/L15BA/L15BY)

DTC P0087 : Fuel Rail Pressure Too Low

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the vehicle was out of fuel and the engine stalled before this DTC was stored, refuel, then clear the DTC with the HDS.

- If a fuel leak occurs, this DTC will be stored. Repair the fuel leak before troubleshooting.

- If any of the DTCs listed below are stored at the same time as P0087, troubleshoot those DTCs first, then recheck for P0087. P0192, P0193: Fuel rail pressure sensor P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s) P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s) P219C, P219D, P219E, P219F: No. 1-No. 4 cylinder A/F variation P2623: High pressure fuel pump

P0192, P0193: Fuel rail pressure sensor

P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s)

P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire

P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s)

P219C, P219D, P219E, P219F: No. 1-No. 4 cylinder A/F variation

P2623: High pressure fuel pump

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

DTC (PGM-FI)

- Problem verification (idling) -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -4. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS. DI Fuel Pressure Test Is the result OK? YES Go to step 2. NO Go to step 3.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-4. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS.

DI Fuel Pressure Test

Is the result OK?

YES

Go to step 2.

NO

Go to step 3.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0087 Fuel Rail Pressure Too Low Is DTC P0087 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

- APP SENSOR

- ECT SENSOR 1

- FUEL PRESSURE CONVERTED FROM PF SENSOR

- FUEL PRESSURE DIRECT INJECTION SYSTEM

- IAT SENSOR (1)

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

APP SENSOR

ECT SENSOR 1

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

Is DTC P0087 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Spill valve operation check -1. Start the engine, then let it idle. -2. Check for noise or vibration from the spill valve on the high pressure fuel pump. When the high pressure fuel pump runs, you will hear some noise from the spill valve.
````

## Chunk 6163: DTC P0087 (L15B7/L15BA/L15BY)

- Title: DTC P0087 (L15B7/L15BA/L15BY)
- Source path: `pages\7269.html`
- Chunk ID: `chunk_6936b95ad0c8`
- Images: none
- Duplicate sources: `pages\8856.html`, `pages\22476.html`, `pages\14652.html`

### Full Text

````text
or Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0087 Fuel Rail Pressure Too Low

Is DTC P0087 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Spill valve operation check -1. Start the engine, then let it idle. -2. Check for noise or vibration from the spill valve on the high pressure fuel pump. When the high pressure fuel pump runs, you will hear some noise from the spill valve. Is there any noise or vibration? YES Go to step 4. NO Replace the high pressure fuel pump .

-1. Start the engine, then let it idle.

-2. Check for noise or vibration from the spill valve on the high pressure fuel pump.

When the high pressure fuel pump runs, you will hear some noise from the spill valve.

Is there any noise or vibration?

YES

Go to step 4.

NO

Replace the high pressure fuel pump .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4. After the engine stalls, crank the engine for several times. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR Less than 1, 000 kPa NOTE: It is normal if the value of several hundred kPa is indicated. Do the current condition(s) match the threshold? YES Go to step 5. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove PGM-FI main relay 2 .

-3. Start the engine, and let it idle until it stalls.

-4. After the engine stalls, crank the engine for several times.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR | Less than 1, 000 | kPa

NOTE: It is normal if the value of several hundred kPa is indicated.

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel rail pressure sensor check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Install PGM-FI main relay 2. -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. CVT: Shift the transmission to D position/mode while pressing the brake pedal firmly, then press the accelerator pedal. NOTE: Do not shift the transmission or remove your foot off the brake pedal, while raising the engine speed. M/T: Snap the throttle for several times. -6. Check the parameter(s) below with the HDS. NOTE: For M/T: use the Line Graph Setup mode with the HDS to compare the value. Signal Current conditions Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM Are both values almost the same? YES The fuel rail pressure sensor is OK. Go to step 6. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Install PGM-FI main relay 2.

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. CVT: Shift the transmission to D position/mode while pressing the brake pedal firmly, then press the accelerator pedal.

NOTE: Do not shift the transmission or remove your foot off the brake pedal, while raising the engine speed.

M/T: Snap the throttle for several times.

-6. Check the parameter(s) below with the HDS.

NOTE: For M/T: use the Line Graph Setup mode with the HDS to compare the value.

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

Are both values almost the same?

YES

The fuel rail pressure sensor is OK. Go to step 6.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 7. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1.
````

## Chunk 6164: DTC P0087 (L15B7/L15BA/L15BY)

- Title: DTC P0087 (L15B7/L15BA/L15BY)
- Source path: `pages\7269.html`
- Chunk ID: `chunk_64264fa6d683`
- Images: none
- Duplicate sources: `pages\8856.html`, `pages\22476.html`, `pages\14652.html`

### Full Text

````text
not shift the transmission or remove your foot off the brake pedal, while raising the engine speed.

M/T: Snap the throttle for several times.

-6. Check the parameter(s) below with the HDS.

NOTE: For M/T: use the Line Graph Setup mode with the HDS to compare the value.

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

Are both values almost the same?

YES

The fuel rail pressure sensor is OK. Go to step 6.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 7. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

The fuel pressure (low pressure side) is OK. Go to step 7.

NO

Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

- High pressure fuel pump visual check -1. Remove the high pressure fuel pump . -2. Visually check the cam that drives a high pressure fuel pump and the roller of the high pressure fuel pump for wear or damage . Are the parts OK? YES Replace the high pressure fuel pump . NO Check for damage of the cam and the roller , and replace the intake camshaft and/or the high pressure fuel pump if needed.

-1. Remove the high pressure fuel pump .

-2. Visually check the cam that drives a high pressure fuel pump and the roller of the high pressure fuel pump for wear or damage .

Are the parts OK?

YES

Replace the high pressure fuel pump .

NO

Check for damage of the cam and the roller , and replace the intake camshaft and/or the high pressure fuel pump if needed.
````

## Chunk 6165: DTC P0088 (K20C1) (17-21)

- Title: DTC P0088 (K20C1) (17-21)
- Source path: `pages\7270.html`
- Chunk ID: `chunk_dc2f9147848a`
- Images: none
- Duplicate sources: `pages\8857.html`, `pages\22477.html`, `pages\14653.html`

### Full Text

````text
# DTC P0088 (K20C1) (17-21)

DTC P0088 : Fuel Rail Pressure Too High

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If any of the DTCs listed below are stored at the same time as P0088, troubleshoot those DTCs first, then recheck for P0088. P0190, P0191, P0192, P0193: Fuel rail pressure sensor P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s) P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s) P2623: High pressure fuel pump

P0190, P0191, P0192, P0193: Fuel rail pressure sensor

P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s)

P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s)

P2623: High pressure fuel pump

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

DTC (PGM-FI)

- Problem verification (idling) -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Start the engine. -5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS. DI Fuel Pressure Test Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0088 Fuel Rail Pressure Too High Is DTC P0088 indicated? YES The failure is duplicated. Go to step 3. NO Go to step 2.

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Start the engine.

-5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS.

DI Fuel Pressure Test

Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Go to step 2.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0088 Fuel Rail Pressure Too High Is DTC P0088 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

- APP SENSOR

- ECT SENSOR 1

- FUEL PRESSURE CONVERTED FROM PF SENSOR

- FUEL PRESSURE DIRECT INJECTION SYSTEM

- IAT SENSOR (1)

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

APP SENSOR

ECT SENSOR 1

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4. After the engine stalls, press the accelerator pedal to the floor and crank the engine several times. -5. Check the parameter(s) below with the HDS.
````

## Chunk 6166: DTC P0088 (K20C1) (17-21)

- Title: DTC P0088 (K20C1) (17-21)
- Source path: `pages\7270.html`
- Chunk ID: `chunk_7f43163a3dba`
- Images: none
- Duplicate sources: `pages\8857.html`, `pages\22477.html`, `pages\14653.html`

### Full Text

````text
the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4. After the engine stalls, press the accelerator pedal to the floor and crank the engine several times. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR Less than 2, 000 kPa Do the current condition(s) match the threshold? YES Go to step 4. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove PGM-FI main relay 2 .

-3. Start the engine, and let it idle until it stalls.

-4. After the engine stalls, press the accelerator pedal to the floor and crank the engine several times.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR | Less than 2, 000 | kPa

Do the current condition(s) match the threshold?

YES

Go to step 4.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel rail pressure sensor check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Install PGM-FI main relay 2 . -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -5. Snap the throttle for several times. -6. Check the parameter(s) below with the HDS. NOTE: Use the Line Grape Setup mode with the HDS to compare the values. Signal Current conditions Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR Signal Current conditions Values Unit FUEL PRESSURE DIRECT INJECTION SYSTEM RELIEF VALVE Are both values almost the same, and does the RELIEF VALVE indicate Normal? YES The fuel rail pressure sensor is OK. Go to step 5. NO (the values are not the same) Replace the fuel rail (fuel rail pressure sensor) . NO (Abnormal is indicated) Replace the high pressure fuel pump .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Install PGM-FI main relay 2 .

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Snap the throttle for several times.

-6. Check the parameter(s) below with the HDS.

NOTE: Use the Line Grape Setup mode with the HDS to compare the values.

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

Signal | Current conditions

Values | Unit

FUEL PRESSURE DIRECT INJECTION SYSTEM

RELIEF VALVE

Are both values almost the same, and does the RELIEF VALVE indicate Normal?

YES

The fuel rail pressure sensor is OK. Go to step 5.

NO (the values are not the same)

Replace the fuel rail (fuel rail pressure sensor) .

NO (Abnormal is indicated)

Replace the high pressure fuel pump .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES Replace the high pressure fuel pump . NO Check the fuel supply system (low pressure side).

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

Replace the high pressure fuel pump .

NO

Check the fuel supply system (low pressure side).
````

## Chunk 6167: DTC P0088 (L15B7/L15BA/L15BY)

- Title: DTC P0088 (L15B7/L15BA/L15BY)
- Source path: `pages\7271.html`
- Chunk ID: `chunk_f601acd3950b`
- Images: none
- Duplicate sources: `pages\8858.html`, `pages\22478.html`, `pages\14654.html`

### Full Text

````text
# DTC P0088 (L15B7/L15BA/L15BY)

DTC P0088 : Fuel Rail Pressure Too High

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If any of the DTCs listed below are stored at the same time as P0088, troubleshoot those DTCs first, then recheck for P0088. P0192, P0193: Fuel rail pressure sensor P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s) P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s) P219C, P219D, P219E, P219F: No. 1-No. 4 cylinder A/F variation P2623: High pressure fuel pump

P0192, P0193: Fuel rail pressure sensor

P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s)

P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s)

P219C, P219D, P219E, P219F: No. 1-No. 4 cylinder A/F variation

P2623: High pressure fuel pump

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

DTC (PGM-FI)

- Problem verification (idling) -1. Record on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Start the engine. -5. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS. DI Fuel Pressure Test Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0088 Fuel Rail Pressure Too High Is DTC P0088 indicated? YES The failure is duplicated. Go to step 3. NO Go to step 2.

-1. Record on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Start the engine.

-5. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS.

DI Fuel Pressure Test

Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Go to step 2.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0088 Fuel Rail Pressure Too High Is DTC P0088 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

- APP SENSOR

- ECT SENSOR 1

- FUEL PRESSURE CONVERTED FROM PF SENSOR

- FUEL PRESSURE DIRECT INJECTION SYSTEM

- IAT SENSOR (1)

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

APP SENSOR

ECT SENSOR 1

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4.
````

## Chunk 6168: DTC P0088 (L15B7/L15BA/L15BY)

- Title: DTC P0088 (L15B7/L15BA/L15BY)
- Source path: `pages\7271.html`
- Chunk ID: `chunk_5de1ad6deeb3`
- Images: none
- Duplicate sources: `pages\8858.html`, `pages\22478.html`, `pages\14654.html`

### Full Text

````text
ENSOR 1

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0088 Fuel Rail Pressure Too High

Is DTC P0088 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel rail pressure sensor check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove PGM-FI main relay 2 . -3. Start the engine, and let it idle until it stalls. -4. After the engine stalls, press the accelerator pedal to the floor and crank the engine several times. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR Less than 1, 000 kPa Do the current condition(s) match the threshold? YES Go to step 4. NO Replace the fuel rail (fuel rail pressure sensor) .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove PGM-FI main relay 2 .

-3. Start the engine, and let it idle until it stalls.

-4. After the engine stalls, press the accelerator pedal to the floor and crank the engine several times.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR | Less than 1, 000 | kPa

Do the current condition(s) match the threshold?

YES

Go to step 4.

NO

Replace the fuel rail (fuel rail pressure sensor) .

- Fuel rail pressure sensor check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Install PGM-FI main relay 2. -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. CVT: Shift the transmission to D position/mode while pressing the brake pedal firmly, then press the accelerator pedal. NOTE: Do not shift the transmission or remove your foot off the brake pedal, while raising the engine speed. M/T: Snap the throttle for several times. -6. Check the parameter(s) below with the HDS. NOTE: For M/T: use the Line Graph Setup mode with the HDS to compare the value. Signal Current conditions Values Unit FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM RELIEF VALVE Are both values almost the same, and does the RELIEF VALVE indicate Normal? YES The fuel rail pressure sensor is OK. Go to step 5. NO (the values are not the same) Replace the fuel rail (fuel rail pressure sensor) . NO (Abnormal is indicated) Replace the high pressure fuel pump .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Install PGM-FI main relay 2.

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. CVT: Shift the transmission to D position/mode while pressing the brake pedal firmly, then press the accelerator pedal.

NOTE: Do not shift the transmission or remove your foot off the brake pedal, while raising the engine speed.

M/T: Snap the throttle for several times.

-6. Check the parameter(s) below with the HDS.

NOTE: For M/T: use the Line Graph Setup mode with the HDS to compare the value.

Signal | Current conditions

Values | Unit

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

RELIEF VALVE

Are both values almost the same, and does the RELIEF VALVE indicate Normal?

YES

The fuel rail pressure sensor is OK. Go to step 5.

NO (the values are not the same)

Replace the fuel rail (fuel rail pressure sensor) .

NO (Abnormal is indicated)

Replace the high pressure fuel pump .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES Replace the high pressure fuel pump . NO Check the fuel supply system (low pressure side).

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

Replace the high pressure fuel pump .

NO

Check the fuel supply system (low pressure side).
````

## Chunk 6169: DTC P0089

- Title: DTC P0089
- Source path: `pages\7272.html`
- Chunk ID: `chunk_82488f310699`
- Images: none
- Duplicate sources: `pages\8859.html`, `pages\22479.html`, `pages\14655.html`

### Full Text

````text
# DTC P0089

DTC P0089 : Fuel Pressure Regulator Performance

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If any of the DTCs listed below are stored at the same time as P0089, troubleshoot those DTCs first, then recheck for P0089. P0171, P0172: Fuel system P0190, P0191, P0192, P0193: Fuel rail pressure sensor P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s) P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s) P2623: High pressure fuel pump

P0171, P0172: Fuel system

P0190, P0191, P0192, P0193: Fuel rail pressure sensor

P0201, P0202, P0203, P0204: No. 1-No. 4 cylinder injector(s)

P0300, P0301, P0302, P0303, P0304: No. 1-No. 4 cylinder misfire

P0351, P0352, P0353, P0354: No. 1-No. 4 cylinder ignition coil(s)

P2623: High pressure fuel pump

DTC Description | Confirmed DTC | Pending DTC

P0089 Fuel Pressure Regulator Performance

DTC (PGM-FI)

- Problem verification (idling) -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Start the engine. -5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS. DI Fuel Pressure Test Is the result OK? YES Go to step 2. NO The failure is duplicated. Go to step 3.

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Start the engine.

-5. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-6. Select the DI Fuel Pressure Test in the INSPECTION MENU with the HDS.

DI Fuel Pressure Test

Is the result OK?

YES

Go to step 2.

NO

The failure is duplicated. Go to step 3.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP Sensor (Hi Res) TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP Sensor (Hi Res) TP SENSOR APP SENSOR ECT SENSOR 1 FUEL PRESSURE CONVERTED FROM PF SENSOR FUEL PRESSURE DIRECT INJECTION SYSTEM IAT SENSOR (1) -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0089 Fuel Pressure Regulator Performance Is DTC P0089 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP Sensor (Hi Res)

- TP SENSOR

- APP SENSOR

- ECT SENSOR 1

- FUEL PRESSURE CONVERTED FROM PF SENSOR

- FUEL PRESSURE DIRECT INJECTION SYSTEM

- IAT SENSOR (1)

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP Sensor (Hi Res)

TP SENSOR

APP SENSOR

ECT SENSOR 1

FUEL PRESSURE CONVERTED FROM PF SENSOR

FUEL PRESSURE DIRECT INJECTION SYSTEM

IAT SENSOR (1)

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0089 Fuel Pressure Regulator Performance

Is DTC P0089 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 4. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES
````

## Chunk 6170: DTC P0089

- Title: DTC P0089
- Source path: `pages\7272.html`
- Chunk ID: `chunk_b66f3793fae6`
- Images: none
- Duplicate sources: `pages\8859.html`, `pages\22479.html`, `pages\14655.html`

### Full Text

````text
ing DTC

P0089 Fuel Pressure Regulator Performance

Is DTC P0089 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Test PGM-FI main relay 2 . If the relay is OK, check for a poor connection or loose terminals at the fuel rail pressure sensor, the high pressure fuel pump, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuel pressure check (low pressure side) -1. Check the fuel pressure . Is the fuel pressure OK? YES The fuel pressure (low pressure side) is OK. Go to step 4. NO Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

-1. Check the fuel pressure .

Is the fuel pressure OK?

YES

The fuel pressure (low pressure side) is OK. Go to step 4.

NO

Check the fuel pump, the fuel pressure regulator, the fuel filter , and the fuel lines .

- High pressure fuel pump cam and pump lifter visual check -1. Remove the high pressure fuel pump . -2. Visually check the cam that drives the high pressure fuel pump and the pump lifter of the high pressure fuel pump for wear or damage . Are the parts OK? YES Replace the high pressure fuel pump . NO Check for damage of the cam and the pump lifter , and replace the exhaust camshaft and/or the high pressure fuel pump if needed.

-1. Remove the high pressure fuel pump .

-2. Visually check the cam that drives the high pressure fuel pump and the pump lifter of the high pressure fuel pump for wear or damage .

Are the parts OK?

YES

Replace the high pressure fuel pump .

NO

Check for damage of the cam and the pump lifter , and replace the exhaust camshaft and/or the high pressure fuel pump if needed.
````

## Chunk 6171: DTC P0095

- Title: DTC P0095
- Source path: `pages\7273.html`
- Chunk ID: `chunk_d63665cbf538`
- Images: `images\GHH403867.png`, `images\GHH403868.jpeg`
- Duplicate sources: `pages\8860.html`, `pages\22480.html`, `pages\14656.html`

### Full Text

````text
# DTC P0095

DTC P0095 : IAT Sensor 2 Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0095 IAT Sensor 2 Out of Range

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (2) More than 264.31 deg.F More than 129.06 deg.C Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (2) | More than 264.31 | deg.F

More than 129.06 | deg.C

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- IAT sensor 2 circuit connectors and terminals condition check -1. Turn the vehicle to the OFF (LOCK) mode. Check for poor connections or loose terminals at these locations: MAP sensor/IAT sensor 2 PCM Engine ground Body ground Are the connections and terminals OK? YES Go to step 3. NO Repair the connections or terminals.

-1. Turn the vehicle to the OFF (LOCK) mode.

Check for poor connections or loose terminals at these locations:

- MAP sensor/IAT sensor 2

- PCM

- Engine ground

- Body ground

Are the connections and terminals OK?

YES

Go to step 3.

NO

Repair the connections or terminals.

- Shorted wire check (TA line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. MAP sensor/IAT sensor 2 4P connector PCM connector No. 1 (96P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2. NO The TA wire is OK. Replace MAP sensor/IAT sensor 2 .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

MAP sensor/IAT sensor 2 4P connector

PCM connector No. 1 (96P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

NO

The TA wire is OK. Replace MAP sensor/IAT sensor 2 .
````

## Chunk 6172: DTC P0096 (K20C1) (17-21)

- Title: DTC P0096 (K20C1) (17-21)
- Source path: `pages\7274.html`
- Chunk ID: `chunk_1eb4db63925a`
- Images: none
- Duplicate sources: `pages\8861.html`, `pages\22481.html`, `pages\14657.html`

### Full Text

````text
# DTC P0096 (K20C1) (17-21)

DTC P0096 : IAT Sensor 2 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0096 IAT Sensor 2 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals of these connectors. ECT sensor 1 ECT sensor 2 MAF sensor/IAT sensor 1 MAP sensor/IAT sensor 2 Are the connections and terminals OK? YES Go to step 2. NO Repair the connections or terminals.

Check for poor connections or loose terminals of these connectors.

- ECT sensor 1

- ECT sensor 2

- MAF sensor/IAT sensor 1

- MAP sensor/IAT sensor 2

Are the connections and terminals OK?

YES

Go to step 2.

NO

Repair the connections or terminals.

- IAT sensor 2 performance check (low temperature) -1. Remove MAP sensor/IAT sensor 2 . -2. Allow IAT sensor 2 to cool to the ambient temperature. -3. Note the ambient temperature. -4. Connect MAP sensor/IAT sensor 2 to its 4P connector, but do not install it. -5. Turn the vehicle to the ON mode. -6. Quickly note the value of IAT Sensor (2) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (2) -7. Compare the value of IAT Sensor (2) to the ambient temperature. Does the value of IAT Sensor (2) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature? YES Replace MAP sensor/IAT sensor 2 . NO Go to step 3.

-1. Remove MAP sensor/IAT sensor 2 .

-2. Allow IAT sensor 2 to cool to the ambient temperature.

-3. Note the ambient temperature.

-4. Connect MAP sensor/IAT sensor 2 to its 4P connector, but do not install it.

-5. Turn the vehicle to the ON mode.

-6. Quickly note the value of IAT Sensor (2) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (2)

-7. Compare the value of IAT Sensor (2) to the ambient temperature.

Does the value of IAT Sensor (2) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature?

YES

Replace MAP sensor/IAT sensor 2 .

NO

Go to step 3.

- IAT sensor 2 performance check (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor/IAT sensor 2 4P connector -3. Using a heat gun, blow hot air on IAT sensor 2 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor. -4. Connect MAP sensor/IAT sensor 2 to its 4P connector, but do not install it. -5. Turn the vehicle to the ON mode. -6. Check IAT Sensor (2) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (2) Does IAT Sensor (2) change 76 deg.F (42 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Replace MAP sensor/IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor/IAT sensor 2 4P connector

-3. Using a heat gun, blow hot air on IAT sensor 2 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

-4. Connect MAP sensor/IAT sensor 2 to its 4P connector, but do not install it.

-5. Turn the vehicle to the ON mode.

-6. Check IAT Sensor (2) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (2)

Does IAT Sensor (2) change 76 deg.F (42 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Replace MAP sensor/IAT sensor 2 .
````

## Chunk 6173: DTC P0096 (L15B7/L15BA/L15BY)

- Title: DTC P0096 (L15B7/L15BA/L15BY)
- Source path: `pages\7275.html`
- Chunk ID: `chunk_72f1fe7ed2e6`
- Images: none
- Duplicate sources: `pages\8862.html`, `pages\22482.html`, `pages\14658.html`

### Full Text

````text
# DTC P0096 (L15B7/L15BA/L15BY)

DTC P0096 : IAT Sensor 2 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0096 IAT Sensor 2 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals of these connectors. ECT sensor 1 ECT sensor 2 MAF sensor/IAT sensor 1 IAT sensor 2 Are the connections and terminals OK? YES Go to step 2. NO Repair the connections or terminals.

Check for poor connections or loose terminals of these connectors.

- ECT sensor 1

- ECT sensor 2

- MAF sensor/IAT sensor 1

- IAT sensor 2

Are the connections and terminals OK?

YES

Go to step 2.

NO

Repair the connections or terminals.

- IAT sensor 2 performance check (low temperature) -1. Remove IAT sensor 2 . -2. Allow IAT sensor 2 to cool to the ambient temperature. -3. Note the ambient temperature. -4. Connect IAT sensor 2 to its 2P connector, but do not install it. -5. Turn the vehicle to the ON mode. -6. Quickly note the value of IAT Sensor (2) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (2) -7. Compare the value of IAT Sensor (2) to the ambient temperature. Does the value of IAT Sensor (2) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature? YES Replace IAT sensor 2 . NO Go to step 3.

-1. Remove IAT sensor 2 .

-2. Allow IAT sensor 2 to cool to the ambient temperature.

-3. Note the ambient temperature.

-4. Connect IAT sensor 2 to its 2P connector, but do not install it.

-5. Turn the vehicle to the ON mode.

-6. Quickly note the value of IAT Sensor (2) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (2)

-7. Compare the value of IAT Sensor (2) to the ambient temperature.

Does the value of IAT Sensor (2) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature?

YES

Replace IAT sensor 2 .

NO

Go to step 3.

- IAT sensor 2 performance check (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. IAT sensor 2 2P connector -3. Using a heat gun, blow hot air on IAT sensor 2 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor. -4. Connect IAT sensor 2 to its 2P connector, but do not install it. -5. Turn the vehicle to the ON mode. -6. Check IAT Sensor (2) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (2) Does IAT Sensor (2) change 76 deg.F (42 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Replace IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

IAT sensor 2 2P connector

-3. Using a heat gun, blow hot air on IAT sensor 2 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

-4. Connect IAT sensor 2 to its 2P connector, but do not install it.

-5. Turn the vehicle to the ON mode.

-6. Check IAT Sensor (2) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (2)

Does IAT Sensor (2) change 76 deg.F (42 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Replace IAT sensor 2 .
````

## Chunk 6174: DTC P0097 (K20C1) (17-21)

- Title: DTC P0097 (K20C1) (17-21)
- Source path: `pages\7276.html`
- Chunk ID: `chunk_0a5e5574931b`
- Images: `images\GHH403869.png`, `images\GHH403870.jpeg`
- Duplicate sources: `pages\8863.html`, `pages\22483.html`, `pages\14659.html`

### Full Text

````text
# DTC P0097 (K20C1) (17-21)

DTC P0097 : IAT Sensor 2 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0097 IAT Sensor 2 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0097 IAT Sensor 2 Circuit Low Voltage Is DTC P0097 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0097 IAT Sensor 2 Circuit Low Voltage

Is DTC P0097 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAP sensor/IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor/IAT sensor 2 4P connector -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0097 IAT Sensor 2 Circuit Low Voltage Is DTC P0097 indicated? YES Go to step 3. NO Replace MAP sensor/IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor/IAT sensor 2 4P connector

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0097 IAT Sensor 2 Circuit Low Voltage

Is DTC P0097 indicated?

YES

Go to step 3.

NO

Replace MAP sensor/IAT sensor 2 .

- Shorted wire check (TA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2. NO The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0097 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

NO

The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0097 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6175: DTC P0097 (L15B7/L15BA/L15BY)

- Title: DTC P0097 (L15B7/L15BA/L15BY)
- Source path: `pages\7277.html`
- Chunk ID: `chunk_12e4a12fe88c`
- Images: `images\GHH403871.jpeg`
- Duplicate sources: `pages\8864.html`, `pages\22484.html`, `pages\14660.html`

### Full Text

````text
# DTC P0097 (L15B7/L15BA/L15BY)

DTC P0097 : IAT Sensor 2 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0097 IAT Sensor 2 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (2) Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (2) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. IAT sensor 2 2P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (2) Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

IAT sensor 2 2P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (2) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace IAT sensor 2 .

- Shorted wire check (ITA2(INTA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode IAT sensor 2 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 IAT sensor 2 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the ITA2 (INTA) wire between the PCM (E55) and IAT sensor 2. NO The ITA2(INTA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0097 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

IAT sensor 2 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | IAT sensor 2 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the ITA2 (INTA) wire between the PCM (E55) and IAT sensor 2.

NO

The ITA2(INTA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0097 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6176: DTC P0098 (K20C1) (17-21)

- Title: DTC P0098 (K20C1) (17-21)
- Source path: `pages\7278.html`
- Chunk ID: `chunk_93f55b32baeb`
- Images: `images\GHH403872.png`, `images\GHH403873.png`, `images\GHH403874.jpeg`, `images\GHH403875.png`, `images\GHH403876.jpeg`, `images\GHH403877.png`, `images\GHH403878.jpeg`, `images\GHH403879.png`, `images\GHH403880.jpeg`
- Duplicate sources: `pages\8865.html`, `pages\22485.html`, `pages\14661.html`

### Full Text

````text
# DTC P0098 (K20C1) (17-21)

DTC P0098 : IAT Sensor 2 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0098 IAT Sensor 2 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0098 IAT Sensor 2 Circuit High Voltage Is DTC P0098 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0098 IAT Sensor 2 Circuit High Voltage

Is DTC P0098 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor/IAT sensor 2 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Terminal B MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0098 IAT Sensor 2 Circuit High Voltage Is DTC P0098 indicated? YES Go to step 3. NO Replace MAP sensor/IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor/IAT sensor 2 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Terminal B | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0098 IAT Sensor 2 Circuit High Voltage

Is DTC P0098 indicated?

YES

Go to step 3.

NO

Replace MAP sensor/IAT sensor 2 .

- Determine possible failure area (TA line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAP sensor/IAT sensor 2 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor/IAT sensor 2 4P connector: disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAP sensor/IAT sensor 2 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor/IAT sensor 2 4P connector: disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG5 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 29 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG5 wire is OK.
````

## Chunk 6177: DTC P0098 (K20C1) (17-21)

- Title: DTC P0098 (K20C1) (17-21)
- Source path: `pages\7278.html`
- Chunk ID: `chunk_b7786e8df8e7`
- Images: `images\GHH403872.png`, `images\GHH403873.png`, `images\GHH403874.jpeg`, `images\GHH403875.png`, `images\GHH403876.jpeg`, `images\GHH403877.png`, `images\GHH403878.jpeg`, `images\GHH403879.png`, `images\GHH403880.jpeg`
- Duplicate sources: `pages\8865.html`, `pages\22485.html`, `pages\14661.html`

### Full Text

````text
connected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG5 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 29 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG5 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 29

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG5 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.

- Open wire check (TA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 45 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 45

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.
````

## Chunk 6178: DTC P0098 (L15B7/L15BA/L15BY)

- Title: DTC P0098 (L15B7/L15BA/L15BY)
- Source path: `pages\7279.html`
- Chunk ID: `chunk_32422da4a7f1`
- Images: `images\GHH403881.jpeg`, `images\GHH403882.jpeg`, `images\GHH403883.jpeg`, `images\GHH403884.jpeg`
- Duplicate sources: `pages\8866.html`, `pages\22486.html`, `pages\14662.html`

### Full Text

````text
# DTC P0098 (L15B7/L15BA/L15BY)

DTC P0098 : IAT Sensor 2 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0098 IAT Sensor 2 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (2) More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (2) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. IAT sensor 2 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A IAT sensor 2 2P connector No. 1 Terminal B IAT sensor 2 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (2) More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

IAT sensor 2 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | IAT sensor 2 2P connector No. 1

Terminal B | IAT sensor 2 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (2) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace IAT sensor 2 .

- Determine possible failure area (ITA2(INTA) line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the IAT sensor 2 2P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode IAT sensor 2 2P connector: disconnected Test point 1 IAT sensor 2 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the IAT sensor 2 2P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

IAT sensor 2 2P connector: disconnected

Test point 1 | IAT sensor 2 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode IAT sensor 2 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 IAT sensor 2 2P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.
````

## Chunk 6179: DTC P0098 (L15B7/L15BA/L15BY)

- Title: DTC P0098 (L15B7/L15BA/L15BY)
- Source path: `pages\7279.html`
- Chunk ID: `chunk_5c62ded9abae`
- Images: `images\GHH403881.jpeg`, `images\GHH403882.jpeg`, `images\GHH403883.jpeg`, `images\GHH403884.jpeg`
- Duplicate sources: `pages\8866.html`, `pages\22486.html`, `pages\14662.html`

### Full Text

````text
tor E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode IAT sensor 2 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 IAT sensor 2 2P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

IAT sensor 2 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | IAT sensor 2 2P connector No. 2

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and IAT sensor 2.

- Open wire check (ITA2(INTA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode IAT sensor 2 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 IAT sensor 2 2P connector No. 1 Test point 2 PCM connector E (80P) No. 55 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ITA2 (INTA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the ITA2 (INTA) wire between the PCM (E55) and IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

IAT sensor 2 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | IAT sensor 2 2P connector No. 1

Test point 2 | PCM connector E (80P) No. 55

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ITA2 (INTA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0098 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ITA2 (INTA) wire between the PCM (E55) and IAT sensor 2.
````

## Chunk 6180: DTC P0099 (K20C1) (17-21)

- Title: DTC P0099 (K20C1) (17-21)
- Source path: `pages\7280.html`
- Chunk ID: `chunk_7df3477a9cd4`
- Images: `images\GHH403885.png`, `images\GHH403886.jpeg`, `images\GHH403887.png`, `images\GHH403888.jpeg`, `images\GHH403889.png`, `images\GHH403890.jpeg`
- Duplicate sources: `pages\8867.html`, `pages\22487.html`, `pages\14663.html`

### Full Text

````text
# DTC P0099 (K20C1) (17-21)

DTC P0099 : IAT Sensor 2 Intermittent Interruption

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for damage or corrosion at MAP sensor/IAT sensor 2 connector terminals.

DTC Description | Confirmed DTC | Pending DTC

P0099 IAT Sensor 2 Intermittent Interruption

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0099 IAT Sensor 2 Intermittent Interruption Is DTC P0099 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0099 IAT Sensor 2 Intermittent Interruption

Is DTC P0099 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (TA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. MAP sensor/IAT sensor 2 4P connector PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2. NO The TA wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

MAP sensor/IAT sensor 2 4P connector

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

NO

The TA wire is not shorted. Go to step 3.

- Open wire check (TA line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 45 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TA wire is OK. Go to step 4. NO Repair an open in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 45

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA wire is OK. Go to step 4.

NO

Repair an open in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

- Open wire check (SG5 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 29 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG5 wire is OK. Replace MAP sensor/IAT sensor 2 .
````

## Chunk 6181: DTC P0099 (K20C1) (17-21)

- Title: DTC P0099 (K20C1) (17-21)
- Source path: `pages\7280.html`
- Chunk ID: `chunk_6a8f924b8da0`
- Images: `images\GHH403885.png`, `images\GHH403886.jpeg`, `images\GHH403887.png`, `images\GHH403888.jpeg`, `images\GHH403889.png`, `images\GHH403890.jpeg`
- Duplicate sources: `pages\8867.html`, `pages\22487.html`, `pages\14663.html`

### Full Text

````text
. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 45

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA wire is OK. Go to step 4.

NO

Repair an open in the TA wire between PCM connector No. 1 terminal No. 45 and MAP sensor/IAT sensor 2.

- Open wire check (SG5 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 29 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG5 wire is OK. Replace MAP sensor/IAT sensor 2 . NO Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 29

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG5 wire is OK. Replace MAP sensor/IAT sensor 2 .

NO

Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.
````

## Chunk 6182: DTC P00CF (K20C1) (17-21)

- Title: DTC P00CF (K20C1) (17-21)
- Source path: `pages\7281.html`
- Chunk ID: `chunk_ff2345de6ddc`
- Images: none
- Duplicate sources: `pages\8868.html`, `pages\22488.html`, `pages\14664.html`

### Full Text

````text
# DTC P00CF (K20C1) (17-21)

DTC P00CF : Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Start the engine and let it idle. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation Is DTC P00CF indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger boost sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Start the engine and let it idle.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

Is DTC P00CF indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the turbocharger boost sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Turbocharger boost sensor port check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the turbocharger boost sensor . -3. Check the pressure measurement port of the turbocharger boost sensor for clogging or foreign objects. Is the turbocharger boost sensor measurement port clogged? YES Clean the turbocharger boost sensor measurement port, and recheck. NO The turbocharger boost sensor measurement port is OK. Replace the turbocharger boost sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the turbocharger boost sensor .

-3. Check the pressure measurement port of the turbocharger boost sensor for clogging or foreign objects.

Is the turbocharger boost sensor measurement port clogged?

YES

Clean the turbocharger boost sensor measurement port, and recheck.

NO

The turbocharger boost sensor measurement port is OK. Replace the turbocharger boost sensor .
````

## Chunk 6183: DTC P00CF (L15B7/L15BA/L15BY)

- Title: DTC P00CF (L15B7/L15BA/L15BY)
- Source path: `pages\7282.html`
- Chunk ID: `chunk_4080e0c0df6b`
- Images: none
- Duplicate sources: `pages\8869.html`, `pages\22489.html`, `pages\14665.html`

### Full Text

````text
# DTC P00CF (L15B7/L15BA/L15BY)

DTC P00CF : Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P00CF is indicated alone, do the troubleshooting for DTC P0069 and P0236 using the on-board snapshot for P00CF.

- If any of the DTCs listed below are indicated at the same time as DTC P00CF, troubleshoot those DTCs first, then recheck for P00CF. P0069: BARO sensor P0236: Turbocharger boost sensor

P0069: BARO sensor

P0236: Turbocharger boost sensor

DTC Description | Confirmed DTC | Pending DTC

P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

DTC (PGM-FI)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0069 BARO Sensor Circuit Range/Performance Problem P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation P0236 Turbocharger Boost Sensor Circuit Range/Performance Problem Are DTC P0069 or P0236 and P00CF indicated at the same time? YES Go to the indicated DTC's troubleshooting. NO Go to the troubleshooting for DTC P0069 and DTC P0236 .

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0069 BARO Sensor Circuit Range/Performance Problem

P00CF Turbocharger Boost Sensor/BARO Sensor Incorrect Correlation

P0236 Turbocharger Boost Sensor Circuit Range/Performance Problem

Are DTC P0069 or P0236 and P00CF indicated at the same time?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to the troubleshooting for DTC P0069 and DTC P0236 .
````

## Chunk 6184: DTC P00FE (K20C1) (2020 2021)

- Title: DTC P00FE (K20C1) (2020 2021)
- Source path: `pages\7283.html`
- Chunk ID: `chunk_cf0aac6c25b9`
- Images: `images\GHH403891.jpeg`, `images\GHH403892.jpeg`
- Duplicate sources: `pages\8870.html`, `pages\22490.html`, `pages\14666.html`

### Full Text

````text
# DTC P00FE (K20C1) (2020 2021)

DTC P00FE : EVAP Vent Line Blockage

Special Tools Required

Vacuum Pump/Gauge, 0-30 inHg Snap-on YA4000A or equivalent, commercially available

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P00FE EVAP Vent Line Blockage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS. FUNCTION TEST Is the result OK? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, the EVAP canister vent shut valve, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Select the EVAP TEST in the INSPECTION MENU, then select the FUNCTION TEST with the HDS.

FUNCTION TEST

Is the result OK?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister purge valve, the EVAP canister vent shut valve, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Fuel vent tube visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the fuel vent tube from the fuel tank unit . -3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg (C), to the fuel vent tube as shown. Courtesy of HONDA, U.S.A., INC. -4. Apply vacuum to the fuel vent tube. Does the tube hold vacuum? YES Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the fuel vent tube from the fuel tank unit .

-3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg (C), to the fuel vent tube as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Apply vacuum to the fuel vent tube.

Does the tube hold vacuum?

YES

Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed.

NO

Go to step 3.

- EVAP canister check -1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg (C), to the hose as shown. Courtesy of HONDA, U.S.A., INC. -2. Turn the vehicle to the ON mode. -3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose. NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged. -4. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit FTP Sensor Does the value of FTP Sensor change? YES Replace the fuel tank . NO Replace the EVAP canister .

-1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg (C), to the hose as shown.

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

-3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose.

NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

FTP Sensor

Does the value of FTP Sensor change?

YES

Replace the fuel tank .

NO

Replace the EVAP canister .
````

## Chunk 6185: DTC P00FE (K20C2) (2019 2020 2021)

- Title: DTC P00FE (K20C2) (2019 2020 2021)
- Source path: `pages\7284.html`
- Chunk ID: `chunk_53070835b843`
- Images: `images\GHH403893.jpeg`, `images\GHH403894.jpeg`
- Duplicate sources: `pages\8871.html`, `pages\22491.html`, `pages\14667.html`

### Full Text

````text
# DTC P00FE (K20C2) (2019 2020 2021)

DTC P00FE : EVAP Vent Line Blockage

Special Tools Required

Vacuum Pump/Gauge, 0-30 inHg Snap-on YA4000A or equivalent, commercially available

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P00FE EVAP Vent Line Blockage

DTC (PGM-FI)

- Fuel vent tube visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the fuel vent tube from the fuel tank unit . -3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg, to the fuel vent tube as shown. Courtesy of HONDA, U.S.A., INC. -4. Apply vacuum to the fuel vent tube. Does the tube hold vacuum? YES Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed. NO Go to step 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the fuel vent tube from the fuel tank unit .

-3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg, to the fuel vent tube as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Apply vacuum to the fuel vent tube.

Does the tube hold vacuum?

YES

Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed.

NO

Go to step 2.

- EVAP canister check -1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg, to the hose as shown. Courtesy of HONDA, U.S.A., INC. -2. Turn the vehicle to the ON mode. -3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose. NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged. -4. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR Does the value of FTP SENSOR change? YES Replace the fuel tank . NO Replace the EVAP canister .

-1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg, to the hose as shown.

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

-3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose.

NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

FTP SENSOR

Does the value of FTP SENSOR change?

YES

Replace the fuel tank .

NO

Replace the EVAP canister .
````

## Chunk 6186: DTC P00FE (L15B7/L15BA/L15BY) (2019 2020 2021)

- Title: DTC P00FE (L15B7/L15BA/L15BY) (2019 2020 2021)
- Source path: `pages\7285.html`
- Chunk ID: `chunk_b2ca2979149d`
- Images: `images\GHH403895.jpeg`, `images\GHH403896.jpeg`
- Duplicate sources: `pages\8872.html`, `pages\22492.html`, `pages\14668.html`

### Full Text

````text
# DTC P00FE (L15B7/L15BA/L15BY) (2019 2020 2021)

DTC P00FE : EVAP Vent Line Blockage

Special Tools Required

Vacuum Pump/Gauge, 0-30 inHg Snap-on YA4000A or equivalent, commercially available

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P00FE EVAP Vent Line Blockage

DTC (PGM-FI)

- Fuel vent tube visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the fuel vent tube from the fuel tank unit . -3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg, to the fuel vent tube as shown. Courtesy of HONDA, U.S.A., INC. -4. Apply vacuum to the fuel vent tube. Does the tube hold vacuum? YES Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed. NO Go to step 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the fuel vent tube from the fuel tank unit .

-3. Disconnect the fuel vent tube (A) from the EVAP canister (B), and connect the vacuum pump/gauge, 0-30 inHg, to the fuel vent tube as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Apply vacuum to the fuel vent tube.

Does the tube hold vacuum?

YES

Remove the fuel tank , and remove the fuel vent tube. Then visually check the fuel vent tube for deformation, excessive bend, foreign object clogged, or restrictions, and repair or replace it if needed.

NO

Go to step 2.

- EVAP canister check -1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg, to the hose as shown. Courtesy of HONDA, U.S.A., INC. -2. Turn the vehicle to the ON mode. -3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose. NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged. -4. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR Does the value of FTP SENSOR change? YES Replace the fuel tank . NO Replace the EVAP canister .

-1. Connect the hose (A) to the EVAP canister fuel vent tube port (B), and connect the vacuum pump/gauge, 0-30 inHg, to the hose as shown.

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

-3. Apply 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum to the hose.

NOTE: Be careful not to exceed the vacuum. If you do, the FTP sensor can be damaged.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

FTP SENSOR

Does the value of FTP SENSOR change?

YES

Replace the fuel tank .

NO

Replace the EVAP canister .
````

## Chunk 6187: DTC P0100 (K20C2)

- Title: DTC P0100 (K20C2)
- Source path: `pages\7286.html`
- Chunk ID: `chunk_114f0f7feaed`
- Images: `images\GHH403897.jpeg`, `images\GHH403898.jpeg`, `images\GHH403899.jpeg`, `images\GHH403900.jpeg`, `images\GHH403901.jpeg`, `images\GHH403902.jpeg`, `images\GHH403903.jpeg`
- Duplicate sources: `pages\8873.html`, `pages\22493.html`, `pages\14669.html`

### Full Text

````text
# DTC P0100 (K20C2)

DTC P0100 : MAF Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 2 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0100 MAF Sensor Circuit Malfunction Is DTC P0100 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 2 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

Is DTC P0100 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (VGP line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 4P connector: disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 2 Test point 2 MAF sensor/IAT sensor 4P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 4P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 2

Test point 2 | MAF sensor/IAT sensor 4P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 6.

NO

Go to step 3.

- Shorted wire check (VCC2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor. NO The VCC2 wire is not shorted. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor.

NO

The VCC2 wire is not shorted. Go to step 4.

- Open wire check (VCC2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 3 Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Go to step 5. NO Repair an open in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected
````

## Chunk 6188: DTC P0100 (K20C2)

- Title: DTC P0100 (K20C2)
- Source path: `pages\7286.html`
- Chunk ID: `chunk_6151d9da700f`
- Images: `images\GHH403897.jpeg`, `images\GHH403898.jpeg`, `images\GHH403899.jpeg`, `images\GHH403900.jpeg`, `images\GHH403901.jpeg`, `images\GHH403902.jpeg`, `images\GHH403903.jpeg`
- Duplicate sources: `pages\8873.html`, `pages\22493.html`, `pages\14669.html`

### Full Text

````text
air a short in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor.

NO

The VCC2 wire is not shorted. Go to step 4.

- Open wire check (VCC2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 3 Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Go to step 5. NO Repair an open in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 3

Test point 2 | PCM connector E (80P) No. 77

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC2 wire is OK. Go to step 5.

NO

Repair an open in the VCC2 wire between the PCM (E77) and the MAF sensor/IAT sensor.

- Open wire check (SG2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the MAF sensor/IAT sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and the MAF sensor/IAT sensor.

- Shorted wire check (VGP line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor. NO The VGP wire is not shorted to ground. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor.

NO

The VGP wire is not shorted to ground. Go to step 7.

- Open wire check (VGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 1 Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGP wire is not open. Go to step 8. NO Repair an open in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 1
````

## Chunk 6189: DTC P0100 (K20C2)

- Title: DTC P0100 (K20C2)
- Source path: `pages\7286.html`
- Chunk ID: `chunk_d771dea8cf48`
- Images: `images\GHH403897.jpeg`, `images\GHH403898.jpeg`, `images\GHH403899.jpeg`, `images\GHH403900.jpeg`, `images\GHH403901.jpeg`, `images\GHH403902.jpeg`, `images\GHH403903.jpeg`
- Duplicate sources: `pages\8873.html`, `pages\22493.html`, `pages\14669.html`

### Full Text

````text
/IAT sensor.

NO

The VGP wire is not shorted to ground. Go to step 7.

- Open wire check (VGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 1 Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGP wire is not open. Go to step 8. NO Repair an open in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 1

Test point 2 | PCM connector E (80P) No. 61

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGP wire is not open. Go to step 8.

NO

Repair an open in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor.

- Shorted wire check (VGP line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor. NO The VGP wire is OK. Go to step 9.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the VGP wire between the PCM (E61) and the MAF sensor/IAT sensor.

NO

The VGP wire is OK. Go to step 9.

- MAF sensor/IAT sensor check (substitution) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Substitute a known-good MAF sensor/IAT sensor . -3. Reconnect all connectors. -4. Exit the SCS mode with the HDS. -5. Turn the vehicle to the ON mode. -6. Clear the DTC with the HDS. Clear DTC -7. Wait 2 seconds or more. -8. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0100 MAF Sensor Circuit Malfunction Is DTC P0100 indicated? YES The MAF sensor/IAT sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM . NO Replace the original MAF sensor/IAT sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Substitute a known-good MAF sensor/IAT sensor .

-3. Reconnect all connectors.

-4. Exit the SCS mode with the HDS.

-5. Turn the vehicle to the ON mode.

-6. Clear the DTC with the HDS.

Clear DTC

-7. Wait 2 seconds or more.

-8. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

Is DTC P0100 indicated?

YES

The MAF sensor/IAT sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original MAF sensor/IAT sensor .
````

## Chunk 6190: DTC P0100 (Si) (17-21)

- Title: DTC P0100 (Si) (17-21)
- Source path: `pages\7287.html`
- Chunk ID: `chunk_0fed25f100a1`
- Images: `images\GHH403904.png`, `images\GHH403905.png`, `images\GHH403906.jpeg`, `images\GHH403907.png`, `images\GHH403908.jpeg`, `images\GHH403909.png`, `images\GHH403910.jpeg`, `images\GHH403911.png`, `images\GHH403912.jpeg`, `images\GHH403913.png`, `images\GHH403914.jpeg`, `images\GHH403915.png`, `images\GHH403916.jpeg`, `images\GHH403917.png`, `images\GHH403918.jpeg`
- Duplicate sources: `pages\8874.html`, `pages\22494.html`, `pages\14670.html`

### Full Text

````text
# DTC P0100 (Si) (17-21)

DTC P0100 : MAF Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 2 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0100 MAF Sensor Circuit Malfunction Is DTC P0100 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 2 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

Is DTC P0100 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (FGP line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 4P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2: Test point 2 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 4P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2:

Test point 2 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 6.

NO

Go to step 3.

- Shorted wire check (VCC2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1. NO The VCC2 wire is not shorted. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1.

NO

The VCC2 wire is not shorted. Go to step 4.

- Open wire check (VCC2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Go to step 5. NO Repair an open in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1.

-1.
````

## Chunk 6191: DTC P0100 (Si) (17-21)

- Title: DTC P0100 (Si) (17-21)
- Source path: `pages\7287.html`
- Chunk ID: `chunk_f50b04984a8b`
- Images: `images\GHH403904.png`, `images\GHH403905.png`, `images\GHH403906.jpeg`, `images\GHH403907.png`, `images\GHH403908.jpeg`, `images\GHH403909.png`, `images\GHH403910.jpeg`, `images\GHH403911.png`, `images\GHH403912.jpeg`, `images\GHH403913.png`, `images\GHH403914.jpeg`, `images\GHH403915.png`, `images\GHH403916.jpeg`, `images\GHH403917.png`, `images\GHH403918.jpeg`
- Duplicate sources: `pages\8874.html`, `pages\22494.html`, `pages\14670.html`

### Full Text

````text
1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1.

NO

The VCC2 wire is not shorted. Go to step 4.

- Open wire check (VCC2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Go to step 5. NO Repair an open in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 77

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC2 wire is OK. Go to step 5.

NO

Repair an open in the VCC2 wire between the PCM (E77) and MAF sensor/IAT sensor 1.

- Open wire check (SG2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

- Shorted wire check (FGP line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1. NO The FGP wire is not shorted to ground. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

NO

The FGP wire is not shorted to ground. Go to step 7.

- Open wire check (FGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FGP wire is not open. Go to step 8.
````

## Chunk 6192: DTC P0100 (Si) (17-21)

- Title: DTC P0100 (Si) (17-21)
- Source path: `pages\7287.html`
- Chunk ID: `chunk_7834b3de9dbc`
- Images: `images\GHH403904.png`, `images\GHH403905.png`, `images\GHH403906.jpeg`, `images\GHH403907.png`, `images\GHH403908.jpeg`, `images\GHH403909.png`, `images\GHH403910.jpeg`, `images\GHH403911.png`, `images\GHH403912.jpeg`, `images\GHH403913.png`, `images\GHH403914.jpeg`, `images\GHH403915.png`, `images\GHH403916.jpeg`, `images\GHH403917.png`, `images\GHH403918.jpeg`
- Duplicate sources: `pages\8874.html`, `pages\22494.html`, `pages\14670.html`

### Full Text

````text
r 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

NO

The FGP wire is not shorted to ground. Go to step 7.

- Open wire check (FGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FGP wire is not open. Go to step 8. NO Repair an open in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 61

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FGP wire is not open. Go to step 8.

NO

Repair an open in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

- Shorted wire check (FGP line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1. NO The FGP wire is OK. Go to step 9.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the FGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

NO

The FGP wire is OK. Go to step 9.

- MAF sensor/IAT sensor 1 check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Substitute a known-good MAF sensor/IAT sensor 1 . -3. Reconnect all connectors. -4. Exit the SCS mode with the HDS. -5. Turn the vehicle to the ON mode. -6. Clear the DTC with the HDS. Clear DTC -7. Wait 2 seconds or more. -8. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0100 MAF Sensor Circuit Malfunction Is DTC P0100 indicated? YES MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM . NO Replace original MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Substitute a known-good MAF sensor/IAT sensor 1 .

-3. Reconnect all connectors.

-4. Exit the SCS mode with the HDS.

-5. Turn the vehicle to the ON mode.

-6. Clear the DTC with the HDS.

Clear DTC

-7. Wait 2 seconds or more.

-8. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0100 MAF Sensor Circuit Malfunction

Is DTC P0100 indicated?

YES

MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0100 goes away and the PCM was substituted, replace the original PCM .

NO

Replace original MAF sensor/IAT sensor 1 .
````

## Chunk 6193: DTC P0101 (K20C1) (17-21)

- Title: DTC P0101 (K20C1) (17-21)
- Source path: `pages\7288.html`
- Chunk ID: `chunk_9d5e098b9b57`
- Images: none
- Duplicate sources: `pages\8875.html`, `pages\22495.html`, `pages\14671.html`

### Full Text

````text
# DTC P0101 (K20C1) (17-21)

DTC P0101 : MAF Sensor Circuit Range/Performance Problem

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2228 and/or P2229 are stored at the same time as DTC P0101, troubleshoot those DTCs first, then recheck for DTC P0101.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV valve PCV hose Air cleaner Intake air duct Purge (PCS) line Brake booster Brake booster hose All parts through the turbocharger to the throttle body Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV valve

- PCV hose

- Air cleaner

- Intake air duct

- Purge (PCS) line

- Brake booster

- Brake booster hose

- All parts through the turbocharger to the throttle body

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- Intake air duct visual check -1. Check for damage or looseness of the intake air duct in the air cleaner. Is it OK? YES Go to step 3. NO Reconnect or replace the intake air duct in the air cleaner.

-1. Check for damage or looseness of the intake air duct in the air cleaner.

Is it OK?

YES

Go to step 3.

NO

Reconnect or replace the intake air duct in the air cleaner.

- Air cleaner element visual check -1. Check for a dirty air cleaner element. Is it dirty? YES Replace the air cleaner element . NO Go to step 4.

-1. Check for a dirty air cleaner element.

Is it dirty?

YES

Replace the air cleaner element .

NO

Go to step 4.

- MAF sensor signal check (without engine running) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR About 0.2 g/s Do the current condition(s) match the threshold? YES Go to step 5. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | About 0.2 | g/s

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace MAF sensor/IAT sensor 1 .

- MAF sensor signal check (with engine running) -1. Start the engine. -2. Vary the engine speed between 2, 000 rpm and 3000 RPM. -3. Check the MAF SENSOR in the DATA LIST with the HDS. Signal Current conditions Values Unit MAF SENSOR Does the reading change? YES Go to step 6. NO Replace MAF sensor/IAT sensor 1 .

-1. Start the engine.

-2. Vary the engine speed between 2, 000 rpm and 3000 RPM.

-3. Check the MAF SENSOR in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

MAF SENSOR

Does the reading change?

YES

Go to step 6.

NO

Replace MAF sensor/IAT sensor 1 .

- Problem verification -1. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR On-board Snapshot Signal Current conditions Values Unit ENGINE SPEED VEHICLE SPEED MAP SENSOR TP SENSOR -3. Monitor the OBD STATUS for DTC P0101 with the HDS. DTC Description OBD STATUS P0101 MAF Sensor Circuit Range/Performance Problem Does the HDS indicate FAILED? YES Replace MAF sensor/IAT sensor 1 . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P0101 with the HDS.

DTC Description | OBD STATUS

P0101 MAF Sensor Circuit Range/Performance Problem
````

## Chunk 6194: DTC P0101 (K20C1) (17-21)

- Title: DTC P0101 (K20C1) (17-21)
- Source path: `pages\7288.html`
- Chunk ID: `chunk_77f0e78bdbeb`
- Images: none
- Duplicate sources: `pages\8875.html`, `pages\22495.html`, `pages\14671.html`

### Full Text

````text
nections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.

-1. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- VEHICLE SPEED

- MAP SENSOR

- TP SENSOR

On-board Snapshot

Signal | Current conditions

Values | Unit

ENGINE SPEED

VEHICLE SPEED

MAP SENSOR

TP SENSOR

-3. Monitor the OBD STATUS for DTC P0101 with the HDS.

DTC Description | OBD STATUS

P0101 MAF Sensor Circuit Range/Performance Problem

Does the HDS indicate FAILED?

YES

Replace MAF sensor/IAT sensor 1 .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, go to step 6-2 and recheck.
````

## Chunk 6195: DTC P0101 (K20C2)

- Title: DTC P0101 (K20C2)
- Source path: `pages\7289.html`
- Chunk ID: `chunk_250deaf526c8`
- Images: none
- Duplicate sources: `pages\8876.html`, `pages\22496.html`, `pages\14672.html`

### Full Text

````text
# DTC P0101 (K20C2)

DTC P0101 : MAF Sensor Circuit Range/Performance Problem (Out of Range)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2073, P2074, P2228, and/or P2229 are stored at the same time as DTC P0101, troubleshoot those DTCs first, then recheck for DTC P0101.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range)

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV valve PCV hose Intake air duct Air cleaner Purge (PCS) line Brake booster Brake booster hose Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV valve

- PCV hose

- Intake air duct

- Air cleaner

- Purge (PCS) line

- Brake booster

- Brake booster hose

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- Intake air duct visual check -1. Check for damage or looseness of the intake air duct from the throttle body to the air cleaner. Is it OK? YES Go to step 3. NO Reconnect or replace the intake air duct from the throttle body to the air cleaner.

-1. Check for damage or looseness of the intake air duct from the throttle body to the air cleaner.

Is it OK?

YES

Go to step 3.

NO

Reconnect or replace the intake air duct from the throttle body to the air cleaner.

- Air cleaner element visual check -1. Check for a dirty air cleaner element. Is it dirty? YES Replace the air cleaner element . NO Go to step 4.

-1. Check for a dirty air cleaner element.

Is it dirty?

YES

Replace the air cleaner element .

NO

Go to step 4.

- MAF sensor signal check (without engine running) -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor 520-10000 Hz Do the current condition(s) match the threshold? YES Go to step 5. NO Replace the MAF sensor/IAT sensor .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | 520-10000 | Hz

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace the MAF sensor/IAT sensor .

- MAF sensor signal check (with engine running) -1. Start the engine and let it idle. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor 520-10000 Hz Do the current condition(s) match the threshold? YES Go to step 6. NO Replace the MAF sensor/IAT sensor .

-1. Start the engine and let it idle.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | 520-10000 | Hz

Do the current condition(s) match the threshold?

YES

Go to step 6.

NO

Replace the MAF sensor/IAT sensor .

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Wait 3 seconds or more. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range) Is DTC P0101 indicated? YES The failure is duplicated. Replace the MAF sensor/IAT sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Wait 3 seconds or more.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range)

Is DTC P0101 indicated?

YES

The failure is duplicated. Replace the MAF sensor/IAT sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6196: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)

- Title: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)
- Source path: `pages\7290.html`
- Chunk ID: `chunk_6ef539cfd67f`
- Images: `images\GHH403919.png`, `images\GHH403920.jpeg`, `images\GHH403921.png`, `images\GHH403922.jpeg`, `images\GHH403923.png`, `images\GHH403924.jpeg`, `images\GHH403925.png`, `images\GHH403926.jpeg`, `images\GHH403927.jpeg`
- Duplicate sources: `pages\8877.html`, `pages\22497.html`, `pages\14673.html`

### Full Text

````text
# DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)

DTC P0101 : MAF Sensor Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 10 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0101 MAF Sensor Circuit Range/Performance Problem Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 10 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse and MAF sensor/IAT sensor 1. Also replace the No. B21 (10 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse and MAF sensor/IAT sensor 1. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG/IG1(AFM) line) -1. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG/IG1(AFM) wire is OK. Go to step 4. NO Repair an open in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse in the under-dash fuse/relay box and MAF sensor/IAT sensor 1.

-1. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG/IG1(AFM) wire is OK. Go to step 4.

NO

Repair an open in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse in the under-dash fuse/relay box and MAF sensor/IAT sensor 1.

- Determine possible failure area (VGP line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there 190-210 kΩ? YES Go to step 7. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there 190-210 kΩ?

YES

Go to step 7.

NO

Go to step 5.

- Shorted wire check (VGP line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3.
````

## Chunk 6197: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)

- Title: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)
- Source path: `pages\7290.html`
- Chunk ID: `chunk_3fa8d8aeb500`
- Images: `images\GHH403919.png`, `images\GHH403920.jpeg`, `images\GHH403921.png`, `images\GHH403922.jpeg`, `images\GHH403923.png`, `images\GHH403924.jpeg`, `images\GHH403925.png`, `images\GHH403926.jpeg`, `images\GHH403927.jpeg`
- Duplicate sources: `pages\8877.html`, `pages\22497.html`, `pages\14673.html`

### Full Text

````text
AF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there 190-210 kΩ? YES Go to step 7. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there 190-210 kΩ?

YES

Go to step 7.

NO

Go to step 5.

- Shorted wire check (VGP line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1. NO The VGP wire is not shorted. Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

NO

The VGP wire is not shorted. Go to step 6.

- Open wire check (VGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGP wire is OK. Go to step 8. NO Repair an open in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector E (80P) No. 61

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGP wire is OK. Go to step 8.

NO

Repair an open in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

- Open wire check (VGM line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 4 Test point 2 PCM connector E (80P) No. 62 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGM wire is OK. Go to step 8. NO Repair an open in the VGM wire between the PCM (E62) and MAF sensor/IAT sensor 1.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 4

Test point 2 | PCM connector E (80P) No. 62

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGM wire is OK. Go to step 8.

NO

Repair an open in the VGM wire between the PCM (E62) and MAF sensor/IAT sensor 1.

- MAF sensor/IAT sensor 1 check -1. Substitute a known-good MAF sensor/IAT sensor 1 . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS.
````

## Chunk 6198: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)

- Title: DTC P0101 (L15B7) (18-21) (Except Si/L15BA/L15BY)
- Source path: `pages\7290.html`
- Chunk ID: `chunk_8d01bb027e32`
- Images: `images\GHH403919.png`, `images\GHH403920.jpeg`, `images\GHH403921.png`, `images\GHH403922.jpeg`, `images\GHH403923.png`, `images\GHH403924.jpeg`, `images\GHH403925.png`, `images\GHH403926.jpeg`, `images\GHH403927.jpeg`
- Duplicate sources: `pages\8877.html`, `pages\22497.html`, `pages\14673.html`

### Full Text

````text
ector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 4

Test point 2 | PCM connector E (80P) No. 62

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGM wire is OK. Go to step 8.

NO

Repair an open in the VGM wire between the PCM (E62) and MAF sensor/IAT sensor 1.

- MAF sensor/IAT sensor 1 check -1. Substitute a known-good MAF sensor/IAT sensor 1 . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0101 MAF Sensor Circuit Range/Performance Problem Is DTC P0101 indicated? YES MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0101 goes away and the PCM was substituted, replace the original PCM . NO Replace original MAF sensor/IAT sensor 1 .

-1. Substitute a known-good MAF sensor/IAT sensor 1 .

-2. Reconnect all connectors.

-3. Exit the SCS mode with the HDS.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Wait 10 seconds or more.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem

Is DTC P0101 indicated?

YES

MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0101 goes away and the PCM was substituted, replace the original PCM .

NO

Replace original MAF sensor/IAT sensor 1 .
````

## Chunk 6199: DTC P0101 (Si) (17-21)

- Title: DTC P0101 (Si) (17-21)
- Source path: `pages\7291.html`
- Chunk ID: `chunk_532b9e24f277`
- Images: none
- Duplicate sources: `pages\8878.html`, `pages\22498.html`, `pages\14674.html`

### Full Text

````text
# DTC P0101 (Si) (17-21)

DTC P0101 : MAF Sensor Circuit Range/Performance Problem (Out of Range)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2073, P2074, P2228, and/or P2229 are stored at the same time as DTC P0101, troubleshoot those DTCs first, then recheck for DTC P0101.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range)

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV valve PCV hose Intake air duct Air cleaner Purge (PCS) line Brake booster Brake booster hose All parts through the turbocharger joint to the throttle body Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV valve

- PCV hose

- Intake air duct

- Air cleaner

- Purge (PCS) line

- Brake booster

- Brake booster hose

- All parts through the turbocharger joint to the throttle body

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- Intake air duct visual check -1. Check for damage or looseness of the intake air duct in the air cleaner. Is it OK? YES Go to step 3. NO Reconnect or replace the intake air duct in the air cleaner.

-1. Check for damage or looseness of the intake air duct in the air cleaner.

Is it OK?

YES

Go to step 3.

NO

Reconnect or replace the intake air duct in the air cleaner.

- Air cleaner element visual check -1. Check for a dirty air cleaner element. Is it dirty? YES Replace the air cleaner element . NO Go to step 4.

-1. Check for a dirty air cleaner element.

Is it dirty?

YES

Replace the air cleaner element .

NO

Go to step 4.

- MAF sensor signal check (without engine running) -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor 520-10000 Hz Do the current condition(s) match the threshold? YES Go to step 5. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | 520-10000 | Hz

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Replace MAF sensor/IAT sensor 1 .

- MAF sensor signal check (with engine running) -1. Start the engine and let it idle. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor 520-10000 Hz Do the current condition(s) match the threshold? YES Go to step 6. NO Replace MAF sensor/IAT sensor 1 .

-1. Start the engine and let it idle.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | 520-10000 | Hz

Do the current condition(s) match the threshold?

YES

Go to step 6.

NO

Replace MAF sensor/IAT sensor 1 .

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. Clear DTC -4. Wait 3 seconds or more. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range) Is DTC P0101 indicated? YES The failure is duplicated. Replace MAF sensor/IAT sensor 1 . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

Clear DTC

-4. Wait 3 seconds or more.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0101 MAF Sensor Circuit Range/Performance Problem (Out of Range)

Is DTC P0101 indicated?

YES

The failure is duplicated. Replace MAF sensor/IAT sensor 1 .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6200: DTC P0102 (K20C1) (17-21)

- Title: DTC P0102 (K20C1) (17-21)
- Source path: `pages\7292.html`
- Chunk ID: `chunk_1f912701107b`
- Images: `images\GHH403928.png`, `images\GHH403929.jpeg`, `images\GHH403930.png`, `images\GHH403931.png`, `images\GHH403932.jpeg`, `images\GHH403933.png`, `images\GHH403934.jpeg`, `images\GHH403935.png`, `images\GHH403936.jpeg`, `images\GHH403937.png`, `images\GHH403938.png`, `images\GHH403939.jpeg`, `images\GHH403940.png`, `images\GHH403941.jpeg`
- Duplicate sources: `pages\8879.html`, `pages\22499.html`, `pages\14675.html`

### Full Text

````text
# DTC P0102 (K20C1) (17-21)

DTC P0102 : MAF Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0102 MAF Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode, and wait 2 seconds. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR Less than 0.11 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode, and wait 2 seconds.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | Less than 0.11 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse and MAF sensor/IAT sensor 1. Also replace the No. B21 (10 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the IG1 ACG/IG1(AFM) wire between the No. B21 (10 A) fuse and MAF sensor/IAT sensor 1. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG/IG1(AFM) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG/IG1(AFM) wire is OK. Go to step 4. NO Repair an open in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse in the under-dash fuse/relay box.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG/IG1(AFM) wire is OK. Go to step 4.

NO

Repair an open in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse in the under-dash fuse/relay box.

- Determine possible failure area (VCC1 AFM line, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 8.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 8.

- Shorted wire check (AFM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4.
````

## Chunk 6201: DTC P0102 (K20C1) (17-21)

- Title: DTC P0102 (K20C1) (17-21)
- Source path: `pages\7292.html`
- Chunk ID: `chunk_61f06076ca55`
- Images: `images\GHH403928.png`, `images\GHH403929.jpeg`, `images\GHH403930.png`, `images\GHH403931.png`, `images\GHH403932.jpeg`, `images\GHH403933.png`, `images\GHH403934.jpeg`, `images\GHH403935.png`, `images\GHH403936.jpeg`, `images\GHH403937.png`, `images\GHH403938.png`, `images\GHH403939.jpeg`, `images\GHH403940.png`, `images\GHH403941.jpeg`
- Duplicate sources: `pages\8879.html`, `pages\22499.html`, `pages\14675.html`

### Full Text

````text
tor (female terminals) No. 2: Test point 2 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 8.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 8.

- Shorted wire check (AFM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1. NO The AFM wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1.

NO

The AFM wire is not shorted. Go to step 6.

- Open wire check (AFM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 53 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The AFM wire is OK. Go to step 7. NO Repair an open in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 53

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The AFM wire is OK. Go to step 7.

NO

Repair an open in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1.

- Determine possible failure area (MAF sensor, others) -1. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1: Terminal B MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. -2. Turn the vehicle to the ON mode. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor Less than 0.11 V Do the current condition(s) match the threshold? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Replace MAF sensor/IAT sensor 1 .

-1. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1:

Terminal B | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | Less than 0.11 | V

Do the current condition(s) match the threshold?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6202: DTC P0102 (K20C1) (17-21)

- Title: DTC P0102 (K20C1) (17-21)
- Source path: `pages\7292.html`
- Chunk ID: `chunk_8818dab14651`
- Images: `images\GHH403928.png`, `images\GHH403929.jpeg`, `images\GHH403930.png`, `images\GHH403931.png`, `images\GHH403932.jpeg`, `images\GHH403933.png`, `images\GHH403934.jpeg`, `images\GHH403935.png`, `images\GHH403936.jpeg`, `images\GHH403937.png`, `images\GHH403938.png`, `images\GHH403939.jpeg`, `images\GHH403940.png`, `images\GHH403941.jpeg`
- Duplicate sources: `pages\8879.html`, `pages\22499.html`, `pages\14675.html`

### Full Text

````text
ng, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Replace MAF sensor/IAT sensor 1 .

-1. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1:

Terminal B | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | Less than 0.11 | V

Do the current condition(s) match the threshold?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM .

NO

Replace MAF sensor/IAT sensor 1 .

- Open wire check (VCC1 AFM line) -1. Turn the vehicle to the OFF (LOCK) mode, and wait 2 minutes. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Test point 2 PCM connector No. 1 (96P) No. 63 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC1 AFM wire between PCM connector No. 1 terminal No. 63 and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode, and wait 2 minutes.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Test point 2 | PCM connector No. 1 (96P) No. 63

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC1 AFM wire between PCM connector No. 1 terminal No. 63 and MAF sensor/IAT sensor 1.
````

## Chunk 6203: DTC P0102 (L15B7/L15BA/L15BY)

- Title: DTC P0102 (L15B7/L15BA/L15BY)
- Source path: `pages\7293.html`
- Chunk ID: `chunk_a5dca957702a`
- Images: `images\GHH403942.png`, `images\GHH403943.jpeg`, `images\GHH403944.png`, `images\GHH403945.jpeg`, `images\GHH403946.png`, `images\GHH403947.jpeg`, `images\GHH403948.png`, `images\GHH403949.jpeg`
- Duplicate sources: `pages\8880.html`, `pages\22500.html`, `pages\14676.html`

### Full Text

````text
# DTC P0102 (L15B7/L15BA/L15BY)

DTC P0102 : MAF Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0102 MAF Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode, and wait 2 seconds. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR Less than 0.1 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode, and wait 2 seconds.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | Less than 0.1 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse. Also replace the No. B21 (10 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG/IG1(AFM) line) -1. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG/IG1(AFM) wire is OK. Go to step 4. NO Repair an open in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse in the under-dash fuse/relay box.

-1. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG/IG1(AFM) wire is OK. Go to step 4.

NO

Repair an open in the IG1 ACG/IG1(AFM) wire between MAF sensor/IAT sensor 1 and the No. B21 (10 A) fuse in the under-dash fuse/relay box.

- Determine possible failure area (VGP line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there 190-210 kΩ? YES Go to step 7. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there 190-210 kΩ?

YES

Go to step 7.

NO

Go to step 5.

- Shorted wire check (VGP line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2.
````

## Chunk 6204: DTC P0102 (L15B7/L15BA/L15BY)

- Title: DTC P0102 (L15B7/L15BA/L15BY)
- Source path: `pages\7293.html`
- Chunk ID: `chunk_b9b6735e9002`
- Images: `images\GHH403942.png`, `images\GHH403943.jpeg`, `images\GHH403944.png`, `images\GHH403945.jpeg`, `images\GHH403946.png`, `images\GHH403947.jpeg`, `images\GHH403948.png`, `images\GHH403949.jpeg`
- Duplicate sources: `pages\8880.html`, `pages\22500.html`, `pages\14676.html`

### Full Text

````text
Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there 190-210 kΩ? YES Go to step 7. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there 190-210 kΩ?

YES

Go to step 7.

NO

Go to step 5.

- Shorted wire check (VGP line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1. NO The VGP wire is not shorted. Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

NO

The VGP wire is not shorted. Go to step 6.

- Open wire check (VGP line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGP wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector E (80P) No. 61

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGP wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VGP wire between the PCM (E61) and MAF sensor/IAT sensor 1.

- MAF sensor/IAT sensor 1 check (substitution) -1. Substitute a known-good MAF sensor/IAT sensor 1 . -2. Reconnect all connectors. -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Start the engine. -6. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral). -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0102 MAF Sensor Circuit Low Voltage Is DTC P0102 indicated? YES MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Replace original MAF sensor/IAT sensor 1 .

-1. Substitute a known-good MAF sensor/IAT sensor 1 .

-2. Reconnect all connectors.

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine.

-6. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral).

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0102 MAF Sensor Circuit Low Voltage

Is DTC P0102 indicated?

YES
````

## Chunk 6205: DTC P0102 (L15B7/L15BA/L15BY)

- Title: DTC P0102 (L15B7/L15BA/L15BY)
- Source path: `pages\7293.html`
- Chunk ID: `chunk_866e9c677782`
- Images: `images\GHH403942.png`, `images\GHH403943.jpeg`, `images\GHH403944.png`, `images\GHH403945.jpeg`, `images\GHH403946.png`, `images\GHH403947.jpeg`, `images\GHH403948.png`, `images\GHH403949.jpeg`
- Duplicate sources: `pages\8880.html`, `pages\22500.html`, `pages\14676.html`

### Full Text

````text
ircuit Low Voltage Is DTC P0102 indicated? YES MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM . NO Replace original MAF sensor/IAT sensor 1 .

-1. Substitute a known-good MAF sensor/IAT sensor 1 .

-2. Reconnect all connectors.

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine.

-6. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral).

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0102 MAF Sensor Circuit Low Voltage

Is DTC P0102 indicated?

YES

MAF sensor/IAT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0102 goes away and the PCM was substituted, replace the original PCM .

NO

Replace original MAF sensor/IAT sensor 1 .
````

## Chunk 6206: DTC P0103 (K20C1) (17-21)

- Title: DTC P0103 (K20C1) (17-21)
- Source path: `pages\7294.html`
- Chunk ID: `chunk_3ae5ac0d3600`
- Images: `images\GHH403950.png`, `images\GHH403951.png`, `images\GHH403952.jpeg`, `images\GHH403953.png`, `images\GHH403954.jpeg`, `images\GHH403955.png`, `images\GHH403956.jpeg`
- Duplicate sources: `pages\8881.html`, `pages\22501.html`, `pages\14677.html`

### Full Text

````text
# DTC P0103 (K20C1) (17-21)

DTC P0103 : MAF Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0103 MAF Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF Sensor More than 4.95 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF Sensor | More than 4.95 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0103 MAF Sensor Circuit High Voltage P0113 IAT Sensor Circuit High Voltage Are DTC P0103 and P0113 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0103 MAF Sensor Circuit High Voltage

P0113 IAT Sensor Circuit High Voltage

Are DTC P0103 and P0113 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (MAF sensor/IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace MAF sensor/IAT sensor 1 . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace MAF sensor/IAT sensor 1 .

NO

Go to step 4.

- Open wire check (SG AFM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected
````

## Chunk 6207: DTC P0103 (K20C1) (17-21)

- Title: DTC P0103 (K20C1) (17-21)
- Source path: `pages\7294.html`
- Chunk ID: `chunk_144247465a50`
- Images: `images\GHH403950.png`, `images\GHH403951.png`, `images\GHH403952.jpeg`, `images\GHH403953.png`, `images\GHH403954.jpeg`, `images\GHH403955.png`, `images\GHH403956.jpeg`
- Duplicate sources: `pages\8881.html`, `pages\22501.html`, `pages\14677.html`

### Full Text

````text
96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

- Determine possible failure area (MAF sensor/IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit MAF Sensor Is there any voltage? YES Go to step 6. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

MAF Sensor

Is there any voltage?

YES

Go to step 6.

NO

Replace MAF sensor/IAT sensor 1 .

- Shorted wire check (AFM line to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1. NO The AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the AFM wire between PCM connector No. 1 terminal No. 53 and MAF sensor/IAT sensor 1.

NO

The AFM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6208: DTC P0103 (L15B7/L15BA/L15BY)

- Title: DTC P0103 (L15B7/L15BA/L15BY)
- Source path: `pages\7295.html`
- Chunk ID: `chunk_f0b897d4bdf7`
- Images: `images\GHH403957.png`, `images\GHH403958.jpeg`, `images\GHH403959.png`, `images\GHH403960.jpeg`
- Duplicate sources: `pages\8882.html`, `pages\22502.html`, `pages\14678.html`

### Full Text

````text
# DTC P0103 (L15B7/L15BA/L15BY)

DTC P0103 : MAF Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0103 MAF Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode, and wait 2 seconds. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAF SENSOR More than 4.89 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode, and wait 2 seconds.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAF SENSOR | More than 4.89 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Open wire check (VGM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. MAF sensor/IAT sensor 1 5P connector PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Test point 2 PCM connector E (80P) No. 62 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VGM wire is OK. Go to step 3. NO Repair an open in the VGM wire between the PCM (E62) and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

MAF sensor/IAT sensor 1 5P connector

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Test point 2 | PCM connector E (80P) No. 62

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VGM wire is OK. Go to step 3.

NO

Repair an open in the VGM wire between the PCM (E62) and MAF sensor/IAT sensor 1.

- PCM internal circuit check -1. Reconnect the following connector. PCM connector E (80P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PCM internal circuit is OK. Replace MAF sensor/IAT sensor 1 . NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM .

-1. Reconnect the following connector.

PCM connector E (80P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PCM internal circuit is OK. Replace MAF sensor/IAT sensor 1 .

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0103 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6209: DTC P0105 (K20C2) (18-21)

- Title: DTC P0105 (K20C2) (18-21)
- Source path: `pages\7296.html`
- Chunk ID: `chunk_525926747faa`
- Images: `images\GHH403961.png`, `images\GHH403962.png`, `images\GHH403963.jpeg`, `images\GHH403964.png`, `images\GHH403965.png`, `images\GHH403966.jpeg`, `images\GHH403967.png`, `images\GHH403968.jpeg`, `images\GHH403969.png`, `images\GHH403970.jpeg`
- Duplicate sources: `pages\8883.html`, `pages\22503.html`, `pages\14679.html`

### Full Text

````text
# DTC P0105 (K20C2) (18-21)

DTC P0105 : MAP Sensor Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0105 MAP Sensor Out of Range

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 3.30 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 3.30 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAP sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAP sensor 3P connector (female terminals) No. 1: Terminal B MAP sensor 3P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 3.30 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace the MAP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAP sensor 3P connector (female terminals) No. 1:

Terminal B | MAP sensor 3P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 3.30 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace the MAP sensor .

- Determine possible failure area (SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAP sensor 3P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 1: Test point 2 MAP sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAP sensor 3P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 1:

Test point 2 | MAP sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 4.

- Open wire check (SG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1.
````

## Chunk 6210: DTC P0105 (K20C2) (18-21)

- Title: DTC P0105 (K20C2) (18-21)
- Source path: `pages\7296.html`
- Chunk ID: `chunk_e79586b7afdf`
- Images: `images\GHH403961.png`, `images\GHH403962.png`, `images\GHH403963.jpeg`, `images\GHH403964.png`, `images\GHH403965.png`, `images\GHH403966.jpeg`, `images\GHH403967.png`, `images\GHH403968.jpeg`, `images\GHH403969.png`, `images\GHH403970.jpeg`
- Duplicate sources: `pages\8883.html`, `pages\22503.html`, `pages\14679.html`

### Full Text

````text
FF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 71

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

- Open wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 56 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 56

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the PB wire between the PCM (E56) and the MAP sensor.
````

## Chunk 6211: DTC P0105 (Si) (17-21)

- Title: DTC P0105 (Si) (17-21)
- Source path: `pages\7297.html`
- Chunk ID: `chunk_c912e607b083`
- Images: `images\GHH403971.png`, `images\GHH403972.png`, `images\GHH403973.jpeg`, `images\GHH403974.png`, `images\GHH403975.jpeg`, `images\GHH403976.png`, `images\GHH403977.jpeg`, `images\GHH403978.png`, `images\GHH403979.jpeg`, `images\GHH403980.png`, `images\GHH403981.jpeg`, `images\GHH403982.png`, `images\GHH403983.jpeg`
- Duplicate sources: `pages\8884.html`, `pages\22504.html`, `pages\14680.html`

### Full Text

````text
# DTC P0105 (Si) (17-21)

DTC P0105 : MAP Sensor Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0105 MAP Sensor Out of Range

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 10 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0105 MAP Sensor Out of Range Is DTC P0105 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 10 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0105 MAP Sensor Out of Range

Is DTC P0105 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (PB line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 1: Test point 2 MAP sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 1:

Test point 2 | MAP sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 6.

NO

Go to step 3.

- Shorted wire check (VCC1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VCC1 wire between the PCM (E70) and the MAP sensor. NO The VCC1 wire is not shorted. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VCC1 wire between the PCM (E70) and the MAP sensor.

NO

The VCC1 wire is not shorted. Go to step 4.

- Open wire check (VCC1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 70 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 wire is OK. Go to step 5. NO Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 70

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6212: DTC P0105 (Si) (17-21)

- Title: DTC P0105 (Si) (17-21)
- Source path: `pages\7297.html`
- Chunk ID: `chunk_9b97f7a7e6eb`
- Images: `images\GHH403971.png`, `images\GHH403972.png`, `images\GHH403973.jpeg`, `images\GHH403974.png`, `images\GHH403975.jpeg`, `images\GHH403976.png`, `images\GHH403977.jpeg`, `images\GHH403978.png`, `images\GHH403979.jpeg`, `images\GHH403980.png`, `images\GHH403981.jpeg`, `images\GHH403982.png`, `images\GHH403983.jpeg`
- Duplicate sources: `pages\8884.html`, `pages\22504.html`, `pages\14680.html`

### Full Text

````text
to step 4.

- Open wire check (VCC1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 70 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 wire is OK. Go to step 5. NO Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 70

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 wire is OK. Go to step 5.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

- Open wire check (SG1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Go to step 8. NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 71

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG1 wire is OK. Go to step 8.

NO

Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

- Shorted wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the PB wire between the PCM (E56) and the MAP sensor. NO The PB wire is not shorted. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the PB wire between the PCM (E56) and the MAP sensor.

NO

The PB wire is not shorted. Go to step 7.

- Open wire check (PB line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 56 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PB wire is OK. Go to step 8. NO Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 56

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Go to step 8.

NO

Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

- MAP sensor check -1. Substitute a known-good MAP sensor . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0105 MAP Sensor Out of Range Is DTC P0105 indicated? YES The MAP sensor is OK.
````

## Chunk 6213: DTC P0105 (Si) (17-21)

- Title: DTC P0105 (Si) (17-21)
- Source path: `pages\7297.html`
- Chunk ID: `chunk_ec5a075c96cc`
- Images: `images\GHH403971.png`, `images\GHH403972.png`, `images\GHH403973.jpeg`, `images\GHH403974.png`, `images\GHH403975.jpeg`, `images\GHH403976.png`, `images\GHH403977.jpeg`, `images\GHH403978.png`, `images\GHH403979.jpeg`, `images\GHH403980.png`, `images\GHH403981.jpeg`, `images\GHH403982.png`, `images\GHH403983.jpeg`
- Duplicate sources: `pages\8884.html`, `pages\22504.html`, `pages\14680.html`

### Full Text

````text
ition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 56

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Go to step 8.

NO

Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

- MAP sensor check -1. Substitute a known-good MAP sensor . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0105 MAP Sensor Out of Range Is DTC P0105 indicated? YES The MAP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM . NO Replace the original MAP sensor .

-1. Substitute a known-good MAP sensor .

-2. Reconnect all connectors.

-3. Exit the SCS mode with the HDS.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Wait 10 seconds or more.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0105 MAP Sensor Out of Range

Is DTC P0105 indicated?

YES

The MAP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0105 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original MAP sensor .
````

## Chunk 6214: DTC P0106

- Title: DTC P0106
- Source path: `pages\7298.html`
- Chunk ID: `chunk_b51ff97a8ba8`
- Images: none
- Duplicate sources: `pages\8885.html`, `pages\22505.html`, `pages\14681.html`

### Full Text

````text
# DTC P0106

DTC P0106 : MAP Sensor Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0106 MAP Sensor Range/Performance Problem

DTC (PGM-FI)

- Parts condition check: Check for poor connections or damage to these parts: PCV hose Purge (PCS) line Air cleaner Intake air duct Intake manifold Throttle body Are the parts OK? YES Go to step 2. NO Repair or replace the damaged part(s).

Check for poor connections or damage to these parts:

- PCV hose

- Purge (PCS) line

- Air cleaner

- Intake air duct

- Intake manifold

- Throttle body

Are the parts OK?

YES

Go to step 2.

NO

Repair or replace the damaged part(s).

- MAP sensor visual check -1. Remove MAP sensor/IAT sensor 2 . -2. Check the MAP sensor port for clogging or restrictions (foreign material, carbon or sludge, etc.). Is the MAP sensor port clogged or restricted? YES Remove the clog or restriction from the MAP sensor port. NO Reinstall MAP sensor/IAT sensor 2 , then go to step 3.

-1. Remove MAP sensor/IAT sensor 2 .

-2. Check the MAP sensor port for clogging or restrictions (foreign material, carbon or sludge, etc.).

Is the MAP sensor port clogged or restricted?

YES

Remove the clog or restriction from the MAP sensor port.

NO

Reinstall MAP sensor/IAT sensor 2 , then go to step 3.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0106 MAP Sensor Range/Performance Problem Is DTC P0106 indicated? YES Replace MAP sensor/IAT sensor 2 . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0106 MAP Sensor Range/Performance Problem

Is DTC P0106 indicated?

YES

Replace MAP sensor/IAT sensor 2 .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6215: DTC P0107 (K20C1) (17-21)

- Title: DTC P0107 (K20C1) (17-21)
- Source path: `pages\7299.html`
- Chunk ID: `chunk_6c8fb6335c57`
- Images: `images\GHH403984.png`, `images\GHH403985.png`, `images\GHH403986.jpeg`, `images\GHH403987.png`, `images\GHH403988.jpeg`, `images\GHH403989.png`, `images\GHH403990.jpeg`
- Duplicate sources: `pages\8886.html`, `pages\22506.html`, `pages\14682.html`

### Full Text

````text
# DTC P0107 (K20C1) (17-21)

DTC P0107 : MAP Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0107 MAP Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine, and let it idle. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0107 MAP Sensor Circuit Low Voltage Is DTC P0107 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine, and let it idle.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0107 MAP Sensor Circuit Low Voltage

Is DTC P0107 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (PB line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor/IAT sensor 2 4P connector -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Start the engine, and let it idle. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0107 MAP Sensor Circuit Low Voltage Is DTC P0107 indicated? YES Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor/IAT sensor 2 4P connector

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Start the engine, and let it idle.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0107 MAP Sensor Circuit Low Voltage

Is DTC P0107 indicated?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (MAP sensor/IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor/IAT sensor 2 4P connector: disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace MAP sensor/IAT sensor 2 . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor/IAT sensor 2 4P connector: disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace MAP sensor/IAT sensor 2 .

NO

Go to step 4.

- Open wire check (VCC2 2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3: Test point 2 PCM connector No. 1 (96P) No. 64 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 2 wire between PCM connector No. 1 terminal No. 64 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2.
````

## Chunk 6216: DTC P0107 (K20C1) (17-21)

- Title: DTC P0107 (K20C1) (17-21)
- Source path: `pages\7299.html`
- Chunk ID: `chunk_60c74fadb122`
- Images: `images\GHH403984.png`, `images\GHH403985.png`, `images\GHH403986.jpeg`, `images\GHH403987.png`, `images\GHH403988.jpeg`, `images\GHH403989.png`, `images\GHH403990.jpeg`
- Duplicate sources: `pages\8886.html`, `pages\22506.html`, `pages\14682.html`

### Full Text

````text
PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3: Test point 2 PCM connector No. 1 (96P) No. 64 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 2 wire between PCM connector No. 1 terminal No. 64 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3:

Test point 2 | PCM connector No. 1 (96P) No. 64

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC2 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC2 2 wire between PCM connector No. 1 terminal No. 64 and MAP sensor/IAT sensor 2.

- Shorted wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the PB wire between PCM connector No. 1 terminal No. 27 and MAP sensor/IAT sensor 2. NO The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the PB wire between PCM connector No. 1 terminal No. 27 and MAP sensor/IAT sensor 2.

NO

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6217: DTC P0107 (K20C2)

- Title: DTC P0107 (K20C2)
- Source path: `pages\7300.html`
- Chunk ID: `chunk_0d416c181008`
- Images: `images\GHH403991.jpeg`, `images\GHH403992.jpeg`, `images\GHH403993.jpeg`
- Duplicate sources: `pages\8887.html`, `pages\22507.html`, `pages\14683.html`

### Full Text

````text
# DTC P0107 (K20C2)

DTC P0107 : MAP Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0107 MAP Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR Less than 0.23 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | Less than 0.23 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (PB line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR Less than 0.23 V Do the current condition(s) match the threshold? YES Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | Less than 0.23 | V

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (MAP sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 MAP sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the MAP sensor . NO Go to step 4.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | MAP sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the MAP sensor .

NO

Go to step 4.

- Open wire check (VCC1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 3 Test point 2 PCM connector E (80P) No. 70 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 3

Test point 2 | PCM connector E (80P) No. 70

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

NO
````

## Chunk 6218: DTC P0107 (K20C2)

- Title: DTC P0107 (K20C2)
- Source path: `pages\7300.html`
- Chunk ID: `chunk_910ae64e5b0c`
- Images: `images\GHH403991.jpeg`, `images\GHH403992.jpeg`, `images\GHH403993.jpeg`
- Duplicate sources: `pages\7301.html`, `pages\8887.html`, `pages\8888.html`, `pages\22507.html`, `pages\22508.html`, `pages\14683.html`, `pages\14684.html`

### Full Text

````text
ire between the PCM (E70) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 3

Test point 2 | PCM connector E (80P) No. 70

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

- Shorted wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the PB wire between the PCM (E56) and the MAP sensor. NO The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the PB wire between the PCM (E56) and the MAP sensor.

NO

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6219: DTC P0107 (L15B7/L15BA/L15BY)

- Title: DTC P0107 (L15B7/L15BA/L15BY)
- Source path: `pages\7301.html`
- Chunk ID: `chunk_d8b609a171d2`
- Images: `images\GHH403994.jpeg`, `images\GHH403995.jpeg`, `images\GHH403996.jpeg`
- Duplicate sources: `pages\8888.html`, `pages\22508.html`, `pages\14684.html`

### Full Text

````text
# DTC P0107 (L15B7/L15BA/L15BY)

DTC P0107 : MAP Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0107 MAP Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR Less than 0.23 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | Less than 0.23 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (PB line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR Less than 0.23 V Do the current condition(s) match the threshold? YES Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | Less than 0.23 | V

Do the current condition(s) match the threshold?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (MAP sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 MAP sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the MAP sensor . NO Go to step 4.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | MAP sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the MAP sensor .

NO

Go to step 4.

- Open wire check (VCC1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 3 Test point 2 PCM connector E (80P) No. 70 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC1 wire between the PCM (E70) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 3

Test point 2 | PCM connector E (80P) No. 70

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0107 goes away and the PCM was substituted, replace the original PCM .

NO
````

## Chunk 6220: DTC P0108 (K20C1) (17-21)

- Title: DTC P0108 (K20C1) (17-21)
- Source path: `pages\7302.html`
- Chunk ID: `chunk_7ba65c7bbd64`
- Images: `images\GHH403997.png`, `images\GHH403998.png`, `images\GHH403999.jpeg`, `images\GHH404000.png`, `images\GHH404001.png`, `images\GHH404002.jpeg`, `images\GHH404003.png`, `images\GHH404004.jpeg`, `images\GHH404005.png`, `images\GHH404006.jpeg`
- Duplicate sources: `pages\8889.html`, `pages\22509.html`, `pages\14685.html`

### Full Text

````text
# DTC P0108 (K20C1) (17-21)

DTC P0108 : MAP Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0108 MAP Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine, and let it idle. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0108 MAP Sensor Circuit High Voltage Is DTC P0108 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine, and let it idle.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0108 MAP Sensor Circuit High Voltage

Is DTC P0108 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAP sensor/IAT sensor 2 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAP sensor/IAT sensor 2, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor/IAT sensor 2 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Terminal B MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Start the engine, and let it idle. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0108 MAP Sensor Circuit High Voltage Is DTC P0108 indicated? YES Go to step 3. NO Replace MAP sensor/IAT sensor 2 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor/IAT sensor 2 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Terminal B | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Start the engine, and let it idle.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0108 MAP Sensor Circuit High Voltage

Is DTC P0108 indicated?

YES

Go to step 3.

NO

Replace MAP sensor/IAT sensor 2 .

- Determine possible failure area (SG5 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAP sensor/IAT sensor 2 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor/IAT sensor 2 4P connector: disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAP sensor/IAT sensor 2 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor/IAT sensor 2 4P connector: disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 4.

- Open wire check (SG5 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No.
````

## Chunk 6221: DTC P0108 (K20C1) (17-21)

- Title: DTC P0108 (K20C1) (17-21)
- Source path: `pages\7302.html`
- Chunk ID: `chunk_36b60f47f295`
- Images: `images\GHH403997.png`, `images\GHH403998.png`, `images\GHH403999.jpeg`, `images\GHH404000.png`, `images\GHH404001.png`, `images\GHH404002.jpeg`, `images\GHH404003.png`, `images\GHH404004.jpeg`, `images\GHH404005.png`, `images\GHH404006.jpeg`
- Duplicate sources: `pages\8889.html`, `pages\22509.html`, `pages\14685.html`

### Full Text

````text
.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor/IAT sensor 2 4P connector: disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 4.

- Open wire check (SG5 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 29 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG5 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 29

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG5 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG5 wire between PCM connector No. 1 terminal No. 29 and MAP sensor/IAT sensor 2.

- Open wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor/IAT sensor 2 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4: Test point 2 PCM connector No. 1 (96P) No. 27 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the PB wire between PCM connector No. 1 terminal No. 27 and MAP sensor/IAT sensor 2.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor/IAT sensor 2 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAP sensor/IAT sensor 2 4P connector (female terminals) No. 4:

Test point 2 | PCM connector No. 1 (96P) No. 27

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the PB wire between PCM connector No. 1 terminal No. 27 and MAP sensor/IAT sensor 2.
````

## Chunk 6222: DTC P0108 (K20C2)

- Title: DTC P0108 (K20C2)
- Source path: `pages\7303.html`
- Chunk ID: `chunk_c7e96bd847b1`
- Images: `images\GHH404007.jpeg`, `images\GHH404008.jpeg`, `images\GHH404009.jpeg`, `images\GHH404010.jpeg`
- Duplicate sources: `pages\8890.html`, `pages\22510.html`, `pages\14686.html`

### Full Text

````text
# DTC P0108 (K20C2)

DTC P0108 : MAP Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0108 MAP Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 4.49 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 4.49 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAP sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAP sensor 3P connector No. 1 Terminal B MAP sensor 3P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 4.49 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace the MAP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAP sensor 3P connector No. 1

Terminal B | MAP sensor 3P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 4.49 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace the MAP sensor .

- Determine possible failure area (SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAP sensor 3P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 MAP sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAP sensor 3P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | MAP sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 4.

- Open wire check (SG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)
````

## Chunk 6223: DTC P0108 (K20C2)

- Title: DTC P0108 (K20C2)
- Source path: `pages\7303.html`
- Chunk ID: `chunk_31a2161ee7ab`
- Images: `images\GHH404007.jpeg`, `images\GHH404008.jpeg`, `images\GHH404009.jpeg`, `images\GHH404010.jpeg`
- Duplicate sources: `pages\8890.html`, `pages\22510.html`, `pages\14686.html`

### Full Text

````text
for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | PCM connector E (80P) No. 71

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

- Open wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 2 Test point 2 PCM connector E (80P) No. 56 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 2

Test point 2 | PCM connector E (80P) No. 56

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the PB wire between the PCM (E56) and the MAP sensor.
````

## Chunk 6224: DTC P0108 (L15B7/L15BA/L15BY)

- Title: DTC P0108 (L15B7/L15BA/L15BY)
- Source path: `pages\7304.html`
- Chunk ID: `chunk_41161c0e6adf`
- Images: `images\GHH404011.jpeg`, `images\GHH404012.jpeg`, `images\GHH404013.jpeg`, `images\GHH404014.jpeg`
- Duplicate sources: `pages\8891.html`, `pages\22511.html`, `pages\14687.html`

### Full Text

````text
# DTC P0108 (L15B7/L15BA/L15BY)

DTC P0108 : MAP Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0108 MAP Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the MAP SENSOR in the DATA LIST with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 4.49 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the MAP SENSOR in the DATA LIST with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 4.49 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAP sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAP sensor 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAP sensor 3P connector No. 1 Terminal B MAP sensor 3P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit MAP SENSOR More than 4.49 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace the MAP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAP sensor 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAP sensor 3P connector No. 1

Terminal B | MAP sensor 3P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

MAP SENSOR | More than 4.49 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace the MAP sensor .

- Determine possible failure area (SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAP sensor 3P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAP sensor 3P connector: disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 MAP sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 5. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAP sensor 3P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAP sensor 3P connector: disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | MAP sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 5.

NO

Go to step 4.

- Open wire check (SG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3.
````

## Chunk 6225: DTC P0108 (L15B7/L15BA/L15BY)

- Title: DTC P0108 (L15B7/L15BA/L15BY)
- Source path: `pages\7304.html`
- Chunk ID: `chunk_db14a5dbcdd4`
- Images: `images\GHH404011.jpeg`, `images\GHH404012.jpeg`, `images\GHH404013.jpeg`, `images\GHH404014.jpeg`
- Duplicate sources: `pages\8891.html`, `pages\22511.html`, `pages\14687.html`

### Full Text

````text
ect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 1 Test point 2 PCM connector E (80P) No. 71 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 1

Test point 2 | PCM connector E (80P) No. 71

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG1 wire between the PCM (E71) and the MAP sensor.

- Open wire check (PB line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAP sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAP sensor 3P connector No. 2 Test point 2 PCM connector E (80P) No. 56 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the PB wire between the PCM (E56) and the MAP sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAP sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAP sensor 3P connector No. 2

Test point 2 | PCM connector E (80P) No. 56

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PB wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0108 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the PB wire between the PCM (E56) and the MAP sensor.
````

## Chunk 6226: DTC P0110, P0111, P011B (K20C1) (17-21)

- Title: DTC P0110, P0111, P011B (K20C1) (17-21)
- Source path: `pages\7305.html`
- Chunk ID: `chunk_451ed6a675fd`
- Images: none
- Duplicate sources: `pages\8892.html`, `pages\22512.html`, `pages\14688.html`

### Full Text

````text
# DTC P0110, P0111, P011B (K20C1) (17-21)

DTC P0110 : IAT Sensor 1 Out of Range

DTC P0111 : IAT Sensor 1 Circuit Range/Performance Problem

DTC P011B : IAT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0110 IAT Sensor 1 Out of Range

P0111 IAT Sensor 1 Circuit Range/Performance Problem

P011B IAT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals at these locations: MAF sensor/IAT sensor 1 ECT sensor 1 ECT sensor 2 Are the connections and terminals OK? YES Go to step 2. NO Repair the connections or terminals.

Check for poor connections or loose terminals at these locations:

- MAF sensor/IAT sensor 1

- ECT sensor 1

- ECT sensor 2

Are the connections and terminals OK?

YES

Go to step 2.

NO

Repair the connections or terminals.

- IAT sensor performance check (low temperature) -1. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -2. Remove MAF sensor/IAT sensor 1 . -3. Allow MAF sensor/IAT sensor 1 to cool to the ambient temperature. -4. Note the ambient temperature. -5. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it. -6. Turn the vehicle to the ON mode. -7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (1) -8. Compare the value of the IAT Sensor (1) to the ambient temperature. Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature? YES Replace MAF sensor/IAT sensor 1 . NO Go to step 3.

-1. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-2. Remove MAF sensor/IAT sensor 1 .

-3. Allow MAF sensor/IAT sensor 1 to cool to the ambient temperature.

-4. Note the ambient temperature.

-5. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it.

-6. Turn the vehicle to the ON mode.

-7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

-8. Compare the value of the IAT Sensor (1) to the ambient temperature.

Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature?

YES

Replace MAF sensor/IAT sensor 1 .

NO

Go to step 3.

- IAT sensor performance check (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Using a heat gun, blow hot air on MAF sensor/IAT sensor 1 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor. -4. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it. -5. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit IAT Sensor (1) Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Using a heat gun, blow hot air on MAF sensor/IAT sensor 1 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

-4. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it.

-5. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Replace MAF sensor/IAT sensor 1 .
````

## Chunk 6227: DTC P0111, P011B (K20C2)

- Title: DTC P0111, P011B (K20C2)
- Source path: `pages\7306.html`
- Chunk ID: `chunk_57d1a0f16c59`
- Images: none
- Duplicate sources: `pages\8893.html`, `pages\22513.html`, `pages\14689.html`

### Full Text

````text
# DTC P0111, P011B (K20C2)

DTC P0111 : IAT Sensor Circuit Range/Performance Problem

DTC P011B : IAT Sensor Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0111 IAT Sensor Circuit Range/Performance Problem

P011B IAT Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals at these locations: MAF sensor/IAT sensor ECT sensor 1 ECT sensor 2 Are the connections and terminals OK? YES Go to step 2. NO Repair the connections or terminals.

Check for poor connections or loose terminals at these locations:

- MAF sensor/IAT sensor

- ECT sensor 1

- ECT sensor 2

Are the connections and terminals OK?

YES

Go to step 2.

NO

Repair the connections or terminals.

- IAT sensor performance check (low temperature) -1. Disconnect the following connector. MAF sensor/IAT sensor 4P connector -2. Remove the MAF sensor/IAT sensor . -3. Allow the MAF sensor/IAT sensor to cool to the ambient temperature. -4. Note the ambient temperature. -5. Connect the MAF sensor/IAT sensor to its 4P connector, but do not install it. -6. Turn the vehicle to the ON mode. -7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (1) -8. Compare the value of the IAT Sensor (1) to the ambient temperature. Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature? YES Replace the MAF sensor/IAT sensor . NO Go to step 3.

-1. Disconnect the following connector.

MAF sensor/IAT sensor 4P connector

-2. Remove the MAF sensor/IAT sensor .

-3. Allow the MAF sensor/IAT sensor to cool to the ambient temperature.

-4. Note the ambient temperature.

-5. Connect the MAF sensor/IAT sensor to its 4P connector, but do not install it.

-6. Turn the vehicle to the ON mode.

-7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

-8. Compare the value of the IAT Sensor (1) to the ambient temperature.

Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature?

YES

Replace the MAF sensor/IAT sensor .

NO

Go to step 3.

- IAT sensor performance check (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 4P connector -3. Using a heat gun, blow hot air on the MAF sensor/IAT sensor for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor. -4. Connect the MAF sensor/IAT sensor to its 4P connector, but do not install it. -5. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit IAT Sensor (1) Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Replace the MAF sensor/IAT sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 4P connector

-3. Using a heat gun, blow hot air on the MAF sensor/IAT sensor for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

-4. Connect the MAF sensor/IAT sensor to its 4P connector, but do not install it.

-5. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Replace the MAF sensor/IAT sensor .
````

## Chunk 6228: DTC P0111, P011B (L15B7/L15BA/L15BY)

- Title: DTC P0111, P011B (L15B7/L15BA/L15BY)
- Source path: `pages\7307.html`
- Chunk ID: `chunk_88cfefe3a496`
- Images: none
- Duplicate sources: `pages\8894.html`, `pages\22514.html`, `pages\14690.html`

### Full Text

````text
# DTC P0111, P011B (L15B7/L15BA/L15BY)

DTC P0111 : IAT Sensor 1 Circuit Range/Performance Problem

DTC P011B : IAT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0111 IAT Sensor 1 Circuit Range/Performance Problem

P011B IAT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals at these locations: MAF sensor/IAT sensor 1 ECT sensor 1 ECT sensor 2 Are the connections and terminals OK? YES Go to step 2. NO Repair the connections or terminals.

Check for poor connections or loose terminals at these locations:

- MAF sensor/IAT sensor 1

- ECT sensor 1

- ECT sensor 2

Are the connections and terminals OK?

YES

Go to step 2.

NO

Repair the connections or terminals.

- IAT sensor performance check (low temperature) -1. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -2. Remove MAF sensor/IAT sensor 1 . -3. Allow MAF sensor/IAT sensor 1 to cool to the ambient temperature. -4. Note the ambient temperature. -5. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it. -6. Turn the vehicle to the ON mode. -7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS. Signal Current conditions Values Unit IAT Sensor (1) -8. Compare the value of the IAT Sensor (1) to the ambient temperature. Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature? YES Replace MAF sensor/IAT sensor 1 . NO Go to step 3.

-1. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-2. Remove MAF sensor/IAT sensor 1 .

-3. Allow MAF sensor/IAT sensor 1 to cool to the ambient temperature.

-4. Note the ambient temperature.

-5. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it.

-6. Turn the vehicle to the ON mode.

-7. Quickly note the value of the IAT Sensor (1) in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

-8. Compare the value of the IAT Sensor (1) to the ambient temperature.

Does the value of the IAT Sensor (1) differ 5.4 deg.F (3 deg.C) or more from the ambient temperature?

YES

Replace MAF sensor/IAT sensor 1 .

NO

Go to step 3.

- IAT sensor performance check (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Using a heat gun, blow hot air on MAF sensor/IAT sensor 1 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor. -4. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it. -5. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit IAT Sensor (1) Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Using a heat gun, blow hot air on MAF sensor/IAT sensor 1 for a few seconds. Do not apply the heat longer than a few seconds or you will damage the sensor.

-4. Connect MAF sensor/IAT sensor 1 to its 5P connector, but do not install it.

-5. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

IAT Sensor (1)

Does the IAT Sensor (1) change 76 deg.F (42 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Replace MAF sensor/IAT sensor 1 .
````

## Chunk 6229: DTC P0112 (K20C1) (17-21)

- Title: DTC P0112 (K20C1) (17-21)
- Source path: `pages\7308.html`
- Chunk ID: `chunk_aefcd887146c`
- Images: `images\GHH404015.png`, `images\GHH404016.jpeg`
- Duplicate sources: `pages\8895.html`, `pages\22515.html`, `pages\14691.html`

### Full Text

````text
# DTC P0112 (K20C1) (17-21)

DTC P0112 : IAT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0112 IAT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) Less than 0.16 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | Less than 0.16 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) Less than 0.16 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | Less than 0.16 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Shorted wire check (TA2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1. NO The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

NO

The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6230: DTC P0112 (K20C2)

- Title: DTC P0112 (K20C2)
- Source path: `pages\7309.html`
- Chunk ID: `chunk_856bd1a2caa0`
- Images: `images\GHH404017.jpeg`
- Duplicate sources: `pages\8896.html`, `pages\22516.html`, `pages\14692.html`

### Full Text

````text
# DTC P0112 (K20C2)

DTC P0112 : IAT Sensor Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0112 IAT Sensor Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace the MAF sensor/IAT sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace the MAF sensor/IAT sensor .

- Shorted wire check (TA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TA wire between the PCM (E53) and the MAF sensor/IAT sensor. NO The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TA wire between the PCM (E53) and the MAF sensor/IAT sensor.

NO

The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6231: DTC P0112 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0112 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7310.html`
- Chunk ID: `chunk_52360042e2bb`
- Images: `images\GHH404018.jpeg`
- Duplicate sources: `pages\8897.html`, `pages\22517.html`, `pages\14693.html`

### Full Text

````text
# DTC P0112 (L15B7 (except Si)/L15BA/L15BY)

DTC P0112 : IAT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0112 IAT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Shorted wire check (ITA1 (TA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1. NO The ITA1(TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.

NO

The ITA1(TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6232: DTC P0112 (Si) (17-21)

- Title: DTC P0112 (Si) (17-21)
- Source path: `pages\7311.html`
- Chunk ID: `chunk_3112093e0737`
- Images: `images\GHH404019.png`, `images\GHH404020.jpeg`
- Duplicate sources: `pages\8898.html`, `pages\22518.html`, `pages\14694.html`

### Full Text

````text
# DTC P0112 (Si) (17-21)

DTC P0112 : IAT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0112 IAT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAF sensor/IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 4P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 4P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Shorted wire check (ITA1 (TA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1. NO The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.

NO

The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0112 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6233: DTC P0113 (K20C1) (17-18)

- Title: DTC P0113 (K20C1) (17-18)
- Source path: `pages\7312.html`
- Chunk ID: `chunk_a0ee504dcf0a`
- Images: `images\GHH404021.png`, `images\GHH404022.png`, `images\GHH404023.jpeg`, `images\GHH404024.png`, `images\GHH404025.jpeg`, `images\GHH404026.png`, `images\GHH404027.jpeg`
- Duplicate sources: `pages\8899.html`, `pages\22519.html`, `pages\14695.html`

### Full Text

````text
# DTC P0113 (K20C1) (17-18)

DTC P0113 : IAT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0113 IAT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) More than 4.87 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | More than 4.87 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Terminal B MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) More than 4.87 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Terminal B | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | More than 4.87 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Open wire check (SG AFM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAF sensor/IAT sensor 1 5P connector. -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector No. 1 (96P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG AFM wire is OK. Go to step 4. NO Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAF sensor/IAT sensor 1 5P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector No. 1 (96P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG AFM wire is OK. Go to step 4.

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

- Open wire check (TA2 line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6234: DTC P0113 (K20C1) (17-18)

- Title: DTC P0113 (K20C1) (17-18)
- Source path: `pages\7312.html`
- Chunk ID: `chunk_12cb61440b0f`
- Images: `images\GHH404021.png`, `images\GHH404022.png`, `images\GHH404023.jpeg`, `images\GHH404024.png`, `images\GHH404025.jpeg`, `images\GHH404026.png`, `images\GHH404027.jpeg`
- Duplicate sources: `pages\8899.html`, `pages\22519.html`, `pages\14695.html`

### Full Text

````text
er wire from the MAF sensor/IAT sensor 1 5P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector No. 1 (96P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG AFM wire is OK. Go to step 4.

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

- Open wire check (TA2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.
````

## Chunk 6235: DTC P0113 (K20C1) (19-21)

- Title: DTC P0113 (K20C1) (19-21)
- Source path: `pages\7313.html`
- Chunk ID: `chunk_651f6aefe3bc`
- Images: `images\GHH404028.png`, `images\GHH404029.png`, `images\GHH404030.jpeg`, `images\GHH404031.png`, `images\GHH404032.jpeg`, `images\GHH404033.png`, `images\GHH404034.jpeg`
- Duplicate sources: `pages\8900.html`, `pages\22520.html`, `pages\14696.html`

### Full Text

````text
# DTC P0113 (K20C1) (19-21)

DTC P0113 : IAT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0113 IAT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) More than 4.99 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | More than 4.99 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAF sensor/IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Terminal B MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT Sensor (1) More than 4.99 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Terminal B | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT Sensor (1) | More than 4.99 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Open wire check (SG AFM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAF sensor/IAT sensor 1 5P connector. -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector No. 1 (96P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The SG AFM wire is OK. Go to step 4. NO Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAF sensor/IAT sensor 1 5P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector No. 1 (96P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The SG AFM wire is OK. Go to step 4.

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

- Open wire check (TA2 line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6236: DTC P0113 (K20C1) (19-21)

- Title: DTC P0113 (K20C1) (19-21)
- Source path: `pages\7313.html`
- Chunk ID: `chunk_10ea4a1d2800`
- Images: `images\GHH404028.png`, `images\GHH404029.png`, `images\GHH404030.jpeg`, `images\GHH404031.png`, `images\GHH404032.jpeg`, `images\GHH404033.png`, `images\GHH404034.jpeg`
- Duplicate sources: `pages\8900.html`, `pages\22520.html`, `pages\14696.html`

### Full Text

````text
wire from the MAF sensor/IAT sensor 1 5P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector No. 1 (96P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The SG AFM wire is OK. Go to step 4.

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

- Open wire check (TA2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The TA2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.
````

## Chunk 6237: DTC P0113 (K20C2)

- Title: DTC P0113 (K20C2)
- Source path: `pages\7314.html`
- Chunk ID: `chunk_1504995182a9`
- Images: `images\GHH404035.jpeg`, `images\GHH404036.jpeg`, `images\GHH404037.jpeg`, `images\GHH404038.jpeg`
- Duplicate sources: `pages\8901.html`, `pages\22521.html`, `pages\14697.html`

### Full Text

````text
# DTC P0113 (K20C2)

DTC P0113 : IAT Sensor Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0113 IAT Sensor Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the MAF sensor/IAT sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 4P connector No. 2 Terminal B MAF sensor/IAT sensor 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace the MAF sensor/IAT sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 4P connector No. 2

Terminal B | MAF sensor/IAT sensor 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace the MAF sensor/IAT sensor .

- Determine possible failure area (TA line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAF sensor/IAT sensor 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 4P connector: disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAF sensor/IAT sensor 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 4P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6238: DTC P0113 (K20C2)

- Title: DTC P0113 (K20C2)
- Source path: `pages\7314.html`
- Chunk ID: `chunk_67968de407c8`
- Images: `images\GHH404035.jpeg`, `images\GHH404036.jpeg`, `images\GHH404037.jpeg`, `images\GHH404038.jpeg`
- Duplicate sources: `pages\8901.html`, `pages\22521.html`, `pages\14697.html`

### Full Text

````text
NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the MAF sensor/IAT sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 2

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and the MAF sensor/IAT sensor.

- Open wire check (TA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 4P connector No. 4 Test point 2 PCM connector E (80P) No. 53 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TA wire between the PCM (E53) and the MAF sensor/IAT sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 4P connector No. 4

Test point 2 | PCM connector E (80P) No. 53

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TA wire between the PCM (E53) and the MAF sensor/IAT sensor.
````

## Chunk 6239: DTC P0113 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0113 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7315.html`
- Chunk ID: `chunk_d0525ceced18`
- Images: `images\GHH404039.jpeg`, `images\GHH404040.jpeg`, `images\GHH404041.jpeg`, `images\GHH404042.jpeg`
- Duplicate sources: `pages\8902.html`, `pages\22522.html`, `pages\14698.html`

### Full Text

````text
# DTC P0113 (L15B7 (except Si)/L15BA/L15BY)

DTC P0113 : IAT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0113 IAT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 5P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 1 5P connector No. 1 Terminal B MAF sensor/IAT sensor 1 5P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 5P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 5P connector No. 1

Terminal B | MAF sensor/IAT sensor 1 5P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Determine possible failure area (ITA1(TA) line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from MAF sensor/IAT sensor 1 5P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 5P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from MAF sensor/IAT sensor 1 5P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 5P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6240: DTC P0113 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0113 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7315.html`
- Chunk ID: `chunk_f8cc1d46eec3`
- Images: `images\GHH404039.jpeg`, `images\GHH404040.jpeg`, `images\GHH404041.jpeg`, `images\GHH404042.jpeg`
- Duplicate sources: `pages\8902.html`, `pages\22522.html`, `pages\14698.html`

### Full Text

````text
Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 2

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

- Open wire check (ITA1 (TA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector No. 1 Test point 2 PCM connector E (80P) No. 53 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector No. 1

Test point 2 | PCM connector E (80P) No. 53

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.
````

## Chunk 6241: DTC P0113 (Si) (17-21)

- Title: DTC P0113 (Si) (17-21)
- Source path: `pages\7316.html`
- Chunk ID: `chunk_046909d55471`
- Images: `images\GHH404043.png`, `images\GHH404044.png`, `images\GHH404045.jpeg`, `images\GHH404046.png`, `images\GHH404047.jpeg`, `images\GHH404048.png`, `images\GHH404049.jpeg`, `images\GHH404050.png`, `images\GHH404051.jpeg`
- Duplicate sources: `pages\8903.html`, `pages\22523.html`, `pages\14699.html`

### Full Text

````text
# DTC P0113 (Si) (17-21)

DTC P0113 : IAT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0113 IAT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (MAF sensor/IAT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. MAF sensor/IAT sensor 1 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2: Terminal B MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit IAT SENSOR (1) More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

MAF sensor/IAT sensor 1 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2:

Terminal B | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

IAT SENSOR (1) | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace MAF sensor/IAT sensor 1 .

- Determine possible failure area (ITA1 (TA) line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the MAF sensor/IAT sensor 1 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode MAF sensor/IAT sensor 1 4P connector: disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the MAF sensor/IAT sensor 1 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

MAF sensor/IAT sensor 1 4P connector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK.
````

## Chunk 6242: DTC P0113 (Si) (17-21)

- Title: DTC P0113 (Si) (17-21)
- Source path: `pages\7316.html`
- Chunk ID: `chunk_cad9c9fcf2d6`
- Images: `images\GHH404043.png`, `images\GHH404044.png`, `images\GHH404045.jpeg`, `images\GHH404046.png`, `images\GHH404047.jpeg`, `images\GHH404048.png`, `images\GHH404049.jpeg`, `images\GHH404050.png`, `images\GHH404051.jpeg`
- Duplicate sources: `pages\8903.html`, `pages\22523.html`, `pages\14699.html`

### Full Text

````text
nnector: disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and MAF sensor/IAT sensor 1.

- Open wire check (ITA1 (TA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4: Test point 2 PCM connector E (80P) No. 53 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 4P connector (female terminals) No. 4:

Test point 2 | PCM connector E (80P) No. 53

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ITA1 (TA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0113 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ITA1 (TA) wire between the PCM (E53) and MAF sensor/IAT sensor 1.
````

## Chunk 6243: DTC P0114

- Title: DTC P0114
- Source path: `pages\7317.html`
- Chunk ID: `chunk_6dfbd9a3a699`
- Images: `images\GHH404052.png`, `images\GHH404053.jpeg`, `images\GHH404054.png`, `images\GHH404055.jpeg`, `images\GHH404056.png`, `images\GHH404057.jpeg`
- Duplicate sources: `pages\8904.html`, `pages\22524.html`, `pages\14700.html`

### Full Text

````text
# DTC P0114

DTC P0114 : IAT Sensor 1 Intermittent Interruption

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for damage or corrosion at MAF sensor/IAT sensor 1 connector terminals.

DTC Description | Confirmed DTC | Pending DTC

P0114 IAT Sensor 1 Intermittent Interruption

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0114 IAT Sensor 1 Intermittent Interruption Is DTC P0114 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0114 IAT Sensor 1 Intermittent Interruption

Is DTC P0114 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at MAF sensor/IAT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (TA2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. MAF sensor/IAT sensor 1 5P connector PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1. NO The TA2 wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

MAF sensor/IAT sensor 1 5P connector

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

NO

The TA2 wire is not shorted. Go to step 3.

- Open wire check (TA2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TA2 wire is OK. Go to step 4. NO Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA2 wire is OK. Go to step 4.

NO

Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

- Open wire check (SG AFM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG AFM wire is OK. Replace MAF sensor/IAT sensor 1 .
````

## Chunk 6244: DTC P0114

- Title: DTC P0114
- Source path: `pages\7317.html`
- Chunk ID: `chunk_71aceb06ba50`
- Images: `images\GHH404052.png`, `images\GHH404053.jpeg`, `images\GHH404054.png`, `images\GHH404055.jpeg`, `images\GHH404056.png`, `images\GHH404057.jpeg`
- Duplicate sources: `pages\8904.html`, `pages\22524.html`, `pages\14700.html`

### Full Text

````text
): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TA2 wire is OK. Go to step 4.

NO

Repair an open in the TA2 wire between PCM connector No. 1 terminal No. 52 and MAF sensor/IAT sensor 1.

- Open wire check (SG AFM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode MAF sensor/IAT sensor 1 5P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG AFM wire is OK. Replace MAF sensor/IAT sensor 1 . NO Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

MAF sensor/IAT sensor 1 5P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | MAF sensor/IAT sensor 1 5P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG AFM wire is OK. Replace MAF sensor/IAT sensor 1 .

NO

Repair an open in the SG AFM wire between PCM connector No. 1 terminal No. 35 and MAF sensor/IAT sensor 1.
````

## Chunk 6245: DTC P0115 (K20C2) (18-21)

- Title: DTC P0115 (K20C2) (18-21)
- Source path: `pages\7318.html`
- Chunk ID: `chunk_d20b02925414`
- Images: `images\GHH404058.png`, `images\GHH404059.jpeg`, `images\GHH404060.png`, `images\GHH404061.png`, `images\GHH404062.jpeg`, `images\GHH404063.png`, `images\GHH404064.jpeg`, `images\GHH404065.png`, `images\GHH404066.jpeg`, `images\GHH404067.png`, `images\GHH404068.jpeg`
- Duplicate sources: `pages\8905.html`, `pages\22525.html`, `pages\14701.html`

### Full Text

````text
# DTC P0115 (K20C2) (18-21)

DTC P0115 : ECT Sensor 1 Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0115 ECT Sensor 1 Out of Range

DTC (PGM-FI)

- Problem verification 1 -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.14 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 3. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.14 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 3.

NO

Go to step 2.

- Problem verification 2 -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.99 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 5. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.99 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 5.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.14 V Do the current condition(s) match the threshold? YES Go to step 4. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.14 | V

Do the current condition(s) match the threshold?

YES

Go to step 4.

NO

Replace ECT sensor 1 .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between the PCM (E52) and ECT sensor 1. NO The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between the PCM (E52) and ECT sensor 1.

NO

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (ECT sensor 1, others) -1.
````

## Chunk 6246: DTC P0115 (K20C2) (18-21)

- Title: DTC P0115 (K20C2) (18-21)
- Source path: `pages\7318.html`
- Chunk ID: `chunk_73652b101841`
- Images: `images\GHH404058.png`, `images\GHH404059.jpeg`, `images\GHH404060.png`, `images\GHH404061.png`, `images\GHH404062.jpeg`, `images\GHH404063.png`, `images\GHH404064.jpeg`, `images\GHH404065.png`, `images\GHH404066.jpeg`, `images\GHH404067.png`, `images\GHH404068.jpeg`
- Duplicate sources: `pages\8905.html`, `pages\22525.html`, `pages\14701.html`

### Full Text

````text
more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between the PCM (E52) and ECT sensor 1.

NO

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A ECT sensor 1 2P connector (female terminals) No. 1: Terminal B ECT sensor 1 2P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.99 V Do the current condition(s) match the threshold? YES Go to step 6. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | ECT sensor 1 2P connector (female terminals) No. 1:

Terminal B | ECT sensor 1 2P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.99 | V

Do the current condition(s) match the threshold?

YES

Go to step 6.

NO

Replace ECT sensor 1 .

- Determine possible failure area (TW line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the ECT sensor 1 2P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ECT sensor 1 2P connector: disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 7. NO Go to step 8.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the ECT sensor 1 2P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ECT sensor 1 2P connector: disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 7.

NO

Go to step 8.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK.
````

## Chunk 6247: DTC P0115 (K20C2) (18-21)

- Title: DTC P0115 (K20C2) (18-21)
- Source path: `pages\7318.html`
- Chunk ID: `chunk_acc886606715`
- Images: `images\GHH404058.png`, `images\GHH404059.jpeg`, `images\GHH404060.png`, `images\GHH404061.png`, `images\GHH404062.jpeg`, `images\GHH404063.png`, `images\GHH404064.jpeg`, `images\GHH404065.png`, `images\GHH404066.jpeg`, `images\GHH404067.png`, `images\GHH404068.jpeg`
- Duplicate sources: `pages\8905.html`, `pages\22525.html`, `pages\14701.html`

### Full Text

````text
elated to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

- Open wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.
````

## Chunk 6248: DTC P0115 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0115 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7319.html`
- Chunk ID: `chunk_c80774e2158d`
- Images: `images\GHH404069.png`, `images\GHH404070.jpeg`, `images\GHH404071.png`, `images\GHH404072.jpeg`, `images\GHH404073.png`, `images\GHH404074.jpeg`
- Duplicate sources: `pages\8906.html`, `pages\22526.html`, `pages\14702.html`

### Full Text

````text
# DTC P0115 (L15B7/L15BA/L15BY) (17-21)

DTC P0115 : ECT Sensor 1 Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0115 ECT Sensor 1 Out of Range

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 10 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0115 ECT Sensor 1 Out of Range Is DTC P0115 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 10 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0115 ECT Sensor 1 Out of Range

Is DTC P0115 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between the PCM (E52) and ECT sensor 1. NO The TW wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between the PCM (E52) and ECT sensor 1.

NO

The TW wire is not shorted. Go to step 3.

- Open wire check (TW line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Go to step 4. NO Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Go to step 4.

NO

Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.

- Open wire check (SG2 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Go to step 5. NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Go to step 5.

NO
````

## Chunk 6249: DTC P0115 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0115 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7319.html`
- Chunk ID: `chunk_6499658f8568`
- Images: `images\GHH404069.png`, `images\GHH404070.jpeg`, `images\GHH404071.png`, `images\GHH404072.jpeg`, `images\GHH404073.png`, `images\GHH404074.jpeg`
- Duplicate sources: `pages\8906.html`, `pages\22526.html`, `pages\14702.html`

### Full Text

````text
ween test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Go to step 5. NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Go to step 5.

NO

Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

- ECT sensor 1 check -1. Substitute a known-good ECT sensor 1 . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0115 ECT Sensor 1 Out of Range Is DTC P0115 indicated? YES ECT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM . NO Replace original ECT sensor 1 .

-1. Substitute a known-good ECT sensor 1 .

-2. Reconnect all connectors.

-3. Exit the SCS mode with the HDS.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Wait 10 seconds or more.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0115 ECT Sensor 1 Out of Range

Is DTC P0115 indicated?

YES

ECT sensor 1 is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0115 goes away and the PCM was substituted, replace the original PCM .

NO

Replace original ECT sensor 1 .
````

## Chunk 6250: DTC P0115, P0116 (K20C1) (17-21)

- Title: DTC P0115, P0116 (K20C1) (17-21)
- Source path: `pages\7320.html`
- Chunk ID: `chunk_957b571afdc0`
- Images: none
- Duplicate sources: `pages\8907.html`, `pages\22527.html`, `pages\14703.html`

### Full Text

````text
# DTC P0115, P0116 (K20C1) (17-21)

DTC P0115 : ECT Sensor 1 Out of Range

DTC P0116 : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0115 ECT Sensor 1 Out of Range

P0116 ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Problem verification 1 -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 176 deg.F More than 80 deg.C Do the current condition(s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 176 | deg.F

More than 80 | deg.C

Do the current condition(s) match the threshold?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Go to step 2.

- Problem verification 2 -1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 -2. Start the engine. -3. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -4. Check ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Replace ECT sensor 1 .

-1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-2. Start the engine.

-3. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-4. Check ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Replace ECT sensor 1 .
````

## Chunk 6251: DTC P0116 (K20C2)

- Title: DTC P0116 (K20C2)
- Source path: `pages\7321.html`
- Chunk ID: `chunk_d06044fdbd65`
- Images: none
- Duplicate sources: `pages\8908.html`, `pages\22528.html`, `pages\14704.html`

### Full Text

````text
# DTC P0116 (K20C2)

DTC P0116 : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0116 ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- ECT sensor 1 check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 176 deg.F More than 80 deg.C Do the current condition(s) match the threshold? YES Note the value of ECT SENSOR 1, then go to step 3. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 176 | deg.F

More than 80 | deg.C

Do the current condition(s) match the threshold?

YES

Note the value of ECT SENSOR 1, then go to step 3.

NO

Go to step 2.

- Problem verification (low temperature) -1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 -2. Start the engine. -3. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -4. Check ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Replace ECT sensor 1 .

-1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-2. Start the engine.

-3. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-4. Check ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Replace ECT sensor 1 .

- Problem verification (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Open the hood, and let the engine cool for 3 hours. -3. Turn the vehicle to the ON mode. -4. Check ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Open the hood, and let the engine cool for 3 hours.

-3. Turn the vehicle to the ON mode.

-4. Check ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Replace ECT sensor 1 .
````

## Chunk 6252: DTC P0116 (L15B7/L15BA/L15BY)

- Title: DTC P0116 (L15B7/L15BA/L15BY)
- Source path: `pages\7322.html`
- Chunk ID: `chunk_0bda1fe21936`
- Images: none
- Duplicate sources: `pages\8909.html`, `pages\22529.html`, `pages\14705.html`

### Full Text

````text
# DTC P0116 (L15B7/L15BA/L15BY)

DTC P0116 : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0116 ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- ECT sensor 1 check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 176 deg.F ECT SENSOR 1 More than 80 deg.C Do the current condition(s) match the threshold? YES Note the value of ECT SENSOR 1, then go to step 3. NO Note the value of ECT SENSOR 1, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 176 | deg.F

ECT SENSOR 1 | More than 80 | deg.C

Do the current condition(s) match the threshold?

YES

Note the value of ECT SENSOR 1, then go to step 3.

NO

Note the value of ECT SENSOR 1, then go to step 2.

- Problem verification (low temperature) -1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 -2. Start the engine. -3. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -4. Check ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Replace ECT sensor 1 .

-1. Note the value of ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-2. Start the engine.

-3. Hold the engine speed at 3000 RPM without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-4. Check ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Replace ECT sensor 1 .

- Problem verification (high temperature) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Open the hood, and let the engine cool for 3 hours. -3. Turn the vehicle to the ON mode. -4. Check ECT SENSOR 1 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Open the hood, and let the engine cool for 3 hours.

-3. Turn the vehicle to the ON mode.

-4. Check ECT SENSOR 1 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

Does ECT SENSOR 1 change 18 deg.F (10 deg.C) or more?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Replace ECT sensor 1 .
````

## Chunk 6253: DTC P0117 (K20C1) (17-21)

- Title: DTC P0117 (K20C1) (17-21)
- Source path: `pages\7323.html`
- Chunk ID: `chunk_a0e466d13cb6`
- Images: `images\GHH404075.png`, `images\GHH404076.jpeg`
- Duplicate sources: `pages\8910.html`, `pages\22530.html`, `pages\14630.html`

### Full Text

````text
# DTC P0117 (K20C1) (17-21)

DTC P0117 : ECT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0117 ECT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0117 ECT Sensor 1 Circuit Low Voltage Is DTC P0117 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0117 ECT Sensor 1 Circuit Low Voltage

Is DTC P0117 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. Clear DTC -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0117 ECT Sensor 1 Circuit Low Voltage Is DTC P0117 indicated? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

Clear DTC

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0117 ECT Sensor 1 Circuit Low Voltage

Is DTC P0117 indicated?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1. NO The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

NO

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6254: DTC P0117 (K20C2)

- Title: DTC P0117 (K20C2)
- Source path: `pages\7324.html`
- Chunk ID: `chunk_12af76b7cf66`
- Images: `images\GHH404077.jpeg`
- Duplicate sources: `pages\8911.html`, `pages\22531.html`, `pages\14706.html`

### Full Text

````text
# DTC P0117 (K20C2)

DTC P0117 : ECT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0117 ECT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between the PCM (E52) and ECT sensor 1. NO The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between the PCM (E52) and ECT sensor 1.

NO

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6255: DTC P0117 (L15B7/L15BA/L15BY)

- Title: DTC P0117 (L15B7/L15BA/L15BY)
- Source path: `pages\7325.html`
- Chunk ID: `chunk_4eb188463d3f`
- Images: `images\GHH404078.jpeg`
- Duplicate sources: `pages\8912.html`, `pages\22532.html`, `pages\14707.html`

### Full Text

````text
# DTC P0117 (L15B7/L15BA/L15BY)

DTC P0117 : ECT Sensor 1 Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0117 ECT Sensor 1 Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.08 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0.08 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0.08 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between the PCM (E52) and ECT sensor 1. NO The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between the PCM (E52) and ECT sensor 1.

NO

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0117 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6256: DTC P0118 (K20C1) (17-21)

- Title: DTC P0118 (K20C1) (17-21)
- Source path: `pages\7326.html`
- Chunk ID: `chunk_53221c9b84ce`
- Images: `images\GHH404079.png`, `images\GHH404080.png`, `images\GHH404081.jpeg`, `images\GHH404082.png`, `images\GHH404083.jpeg`, `images\GHH404084.png`, `images\GHH404085.jpeg`, `images\GHH404086.png`, `images\GHH404087.jpeg`
- Duplicate sources: `pages\8913.html`, `pages\22533.html`, `pages\14631.html`

### Full Text

````text
# DTC P0118 (K20C1) (17-21)

DTC P0118 : ECT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0118 ECT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0118 ECT Sensor 1 Circuit High Voltage Is DTC P0118 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0118 ECT Sensor 1 Circuit High Voltage

Is DTC P0118 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A ECT sensor 1 2P connector (female terminals) No. 1: Terminal B ECT sensor 1 2P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0118 ECT Sensor 1 Circuit High Voltage Is DTC P0118 indicated? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | ECT sensor 1 2P connector (female terminals) No. 1:

Terminal B | ECT sensor 1 2P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0118 ECT Sensor 1 Circuit High Voltage

Is DTC P0118 indicated?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Determine possible failure area (TW line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the ECT sensor 1 2P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ECT sensor 1 2P connector: disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the ECT sensor 1 2P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ECT sensor 1 2P connector: disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 91 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6257: DTC P0118 (K20C1) (17-21)

- Title: DTC P0118 (K20C1) (17-21)
- Source path: `pages\7326.html`
- Chunk ID: `chunk_1c63cd78f0e2`
- Images: `images\GHH404079.png`, `images\GHH404080.png`, `images\GHH404081.jpeg`, `images\GHH404082.png`, `images\GHH404083.jpeg`, `images\GHH404084.png`, `images\GHH404085.jpeg`, `images\GHH404086.png`, `images\GHH404087.jpeg`
- Duplicate sources: `pages\8913.html`, `pages\22533.html`, `pages\14631.html`

### Full Text

````text
ep 5.

- Open wire check (SG3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 91 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG3 wire between PCM connector No. 1 terminal No. 91 and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 91

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG3 wire between PCM connector No. 1 terminal No. 91 and ECT sensor 1.

- Open wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 49 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 49

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.
````

## Chunk 6258: DTC P0118 (K20C2)

- Title: DTC P0118 (K20C2)
- Source path: `pages\7327.html`
- Chunk ID: `chunk_8543c4292b1b`
- Images: `images\GHH404088.jpeg`, `images\GHH404089.jpeg`, `images\GHH404090.jpeg`, `images\GHH404091.jpeg`
- Duplicate sources: `pages\8914.html`, `pages\22534.html`, `pages\14708.html`

### Full Text

````text
# DTC P0118 (K20C2)

DTC P0118 : ECT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0118 ECT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A ECT sensor 1 2P connector No. 1 Terminal B ECT sensor 1 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | ECT sensor 1 2P connector No. 1

Terminal B | ECT sensor 1 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Determine possible failure area (TW line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the ECT sensor 1 2P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ECT sensor 1 2P connector: disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the ECT sensor 1 2P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ECT sensor 1 2P connector: disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 1 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4.
````

## Chunk 6259: DTC P0118 (K20C2)

- Title: DTC P0118 (K20C2)
- Source path: `pages\7327.html`
- Chunk ID: `chunk_36d86132d782`
- Images: `images\GHH404088.jpeg`, `images\GHH404089.jpeg`, `images\GHH404090.jpeg`, `images\GHH404091.jpeg`
- Duplicate sources: `pages\8914.html`, `pages\22534.html`, `pages\14708.html`

### Full Text

````text
ontinuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 1 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 1

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

- Open wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 PCM connector E (80P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | PCM connector E (80P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.
````

## Chunk 6260: DTC P0118 (L15B7/L15BA/L15BY)

- Title: DTC P0118 (L15B7/L15BA/L15BY)
- Source path: `pages\7328.html`
- Chunk ID: `chunk_f154a7d39acc`
- Images: `images\GHH404092.jpeg`, `images\GHH404093.jpeg`, `images\GHH404094.jpeg`, `images\GHH404095.jpeg`
- Duplicate sources: `pages\8915.html`, `pages\22535.html`, `pages\14709.html`

### Full Text

````text
# DTC P0118 (L15B7/L15BA/L15BY)

DTC P0118 : ECT Sensor 1 Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0118 ECT Sensor 1 Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.92 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (ECT sensor 1, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. ECT sensor 1 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A ECT sensor 1 2P connector No. 1 Terminal B ECT sensor 1 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 More than 4.92 V Do the current condition(s) match the threshold? YES Go to step 3. NO Replace ECT sensor 1 .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

ECT sensor 1 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | ECT sensor 1 2P connector No. 1

Terminal B | ECT sensor 1 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | More than 4.92 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Replace ECT sensor 1 .

- Determine possible failure area (TW line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the ECT sensor 1 2P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ECT sensor 1 2P connector: disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the ECT sensor 1 2P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ECT sensor 1 2P connector: disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 5.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 1 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.
````

## Chunk 6261: DTC P0118 (L15B7/L15BA/L15BY)

- Title: DTC P0118 (L15B7/L15BA/L15BY)
- Source path: `pages\7328.html`
- Chunk ID: `chunk_97072bd1f432`
- Images: `images\GHH404092.jpeg`, `images\GHH404093.jpeg`, `images\GHH404094.jpeg`, `images\GHH404095.jpeg`
- Duplicate sources: `pages\8915.html`, `pages\22535.html`, `pages\14709.html`

### Full Text

````text
tor E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 1 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 1

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and ECT sensor 1.

- Open wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector E (80P): disconnected Test point 1 ECT sensor 1 2P connector No. 2 Test point 2 PCM connector E (80P) No. 52 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | ECT sensor 1 2P connector No. 2

Test point 2 | PCM connector E (80P) No. 52

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0118 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TW wire between the PCM (E52) and ECT sensor 1.
````

## Chunk 6262: DTC P0119

- Title: DTC P0119
- Source path: `pages\7329.html`
- Chunk ID: `chunk_e17b93b1bf90`
- Images: `images\GHH404096.png`, `images\GHH404097.jpeg`, `images\GHH404098.png`, `images\GHH404099.jpeg`, `images\GHH404100.png`, `images\GHH404101.jpeg`
- Duplicate sources: `pages\8916.html`, `pages\22536.html`, `pages\14710.html`

### Full Text

````text
# DTC P0119

DTC P0119 : ECT Sensor 1 Circuit Out of Range

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for damage or corrosion at ECT sensor 1 connector terminals.

DTC Description | Confirmed DTC | Pending DTC

P0119 ECT Sensor 1 Circuit Out of Range

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0119 ECT Sensor 1 Circuit Out of Range Is DTC P0119 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Hold the engine speed at 3000 RPM without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0119 ECT Sensor 1 Circuit Out of Range

Is DTC P0119 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1 and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (TW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. ECT sensor 1 2P connector PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1. NO The TW wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

ECT sensor 1 2P connector

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

NO

The TW wire is not shorted. Go to step 3.

- Open wire check (TW line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 49 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TW wire is OK. Go to step 4. NO Repair an open in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 49

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Go to step 4.

NO

Repair an open in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

- Open wire check (SG3 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 91 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK.
````

## Chunk 6263: DTC P0119

- Title: DTC P0119
- Source path: `pages\7329.html`
- Chunk ID: `chunk_e62d204c59bf`
- Images: `images\GHH404096.png`, `images\GHH404097.jpeg`, `images\GHH404098.png`, `images\GHH404099.jpeg`, `images\GHH404100.png`, `images\GHH404101.jpeg`
- Duplicate sources: `pages\8916.html`, `pages\22536.html`, `pages\14710.html`

### Full Text

````text
cle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 49

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TW wire is OK. Go to step 4.

NO

Repair an open in the TW wire between PCM connector No. 1 terminal No. 49 and ECT sensor 1.

- Open wire check (SG3 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode ECT sensor 1 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 ECT sensor 1 2P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 91 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK. Replace ECT sensor 1 . NO Repair an open in the SG3 wire between PCM connector No. 1 terminal No. 91 and ECT sensor 1.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

ECT sensor 1 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | ECT sensor 1 2P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 91

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 wire is OK. Replace ECT sensor 1 .

NO

Repair an open in the SG3 wire between PCM connector No. 1 terminal No. 91 and ECT sensor 1.
````

## Chunk 6264: DTC P011A (K20C1) (17-21)

- Title: DTC P011A (K20C1) (17-21)
- Source path: `pages\7330.html`
- Chunk ID: `chunk_48ba5087db30`
- Images: none
- Duplicate sources: `pages\8917.html`, `pages\22537.html`, `pages\14711.html`

### Full Text

````text
# DTC P011A (K20C1) (17-21)

DTC P011A : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P011A ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals of these connectors. ECT sensor 1 ECT sensor 2 MAF sensor/IAT sensor 1 Are the connection and terminals OK? YES Replace ECT sensor 1 . NO Repair the connections or terminals, then recheck.

Check for poor connections or loose terminals of these connectors.

- ECT sensor 1

- ECT sensor 2

- MAF sensor/IAT sensor 1

Are the connection and terminals OK?

YES

Replace ECT sensor 1 .

NO

Repair the connections or terminals, then recheck.
````

## Chunk 6265: DTC P011A (K20C2)

- Title: DTC P011A (K20C2)
- Source path: `pages\7331.html`
- Chunk ID: `chunk_813c08b58501`
- Images: none
- Duplicate sources: `pages\8918.html`, `pages\22538.html`, `pages\14712.html`

### Full Text

````text
# DTC P011A (K20C2)

DTC P011A : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P011A ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals of these connectors. ECT sensor 1 ECT sensor 2 MAF sensor/IAT sensor Are the connections and terminals OK? YES Replace ECT sensor 1 . NO Repair the connections or terminals, then recheck.

Check for poor connections or loose terminals of these connectors.

- ECT sensor 1

- ECT sensor 2

- MAF sensor/IAT sensor

Are the connections and terminals OK?

YES

Replace ECT sensor 1 .

NO

Repair the connections or terminals, then recheck.
````

## Chunk 6266: DTC P011A (L15B7/L15BA/L15BY)

- Title: DTC P011A (L15B7/L15BA/L15BY)
- Source path: `pages\7332.html`
- Chunk ID: `chunk_850dbf9c8209`
- Images: none
- Duplicate sources: `pages\8919.html`, `pages\22539.html`, `pages\14713.html`

### Full Text

````text
# DTC P011A (L15B7/L15BA/L15BY)

DTC P011A : ECT Sensor 1 Circuit Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P011A ECT Sensor 1 Circuit Range/Performance Problem

DTC (PGM-FI)

- Connector visual check: Check for poor connections or loose terminals of these connectors. ECT sensor 1 ECT sensor 2 MAF sensor/IAT sensor 1 Are the connection and terminals OK? YES Replace ECT sensor 1 . NO Repair the connections or terminals, then recheck.

Check for poor connections or loose terminals of these connectors.

- ECT sensor 1

- ECT sensor 2

- MAF sensor/IAT sensor 1

Are the connection and terminals OK?

YES

Replace ECT sensor 1 .

NO

Repair the connections or terminals, then recheck.
````

## Chunk 6267: DTC P0121 (K20C2) (18-21)

- Title: DTC P0121 (K20C2) (18-21)
- Source path: `pages\7333.html`
- Chunk ID: `chunk_e75979ecec70`
- Images: `images\GHH404102.png`, `images\GHH404103.jpeg`, `images\GHH404104.png`, `images\GHH404105.jpeg`, `images\GHH404106.png`, `images\GHH404107.jpeg`, `images\GHH404108.png`, `images\GHH404109.jpeg`, `images\GHH404110.png`, `images\GHH404111.jpeg`, `images\GHH404112.png`, `images\GHH404113.jpeg`
- Duplicate sources: `pages\8920.html`, `pages\22540.html`, `pages\14714.html`

### Full Text

````text
# DTC P0121 (K20C2) (18-21)

DTC P0121 : TP Sensor A Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

DTC (PGM-FI)

- Problem verification 1 -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A Less than 0.38 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 3. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | Less than 0.38 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 3.

NO

Go to step 2.

- Problem verification 2 -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A More than 4.50 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 7. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | More than 4.50 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 7.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (THL1 line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0121 TP Sensor A Out of Range P0221 TP Sensor B Out of Range Are DTC P0121 and P0221 indicated at the same time? YES Go to step 5. NO Go to step 4.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

P0221 TP Sensor B Out of Range

Are DTC P0121 and P0221 indicated at the same time?

YES

Go to step 5.

NO

Go to step 4.

- Shorted wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the THL1 wire between the PCM (E50) and the throttle body. NO The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between the PCM (E50) and the throttle body.

NO

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3.
````

## Chunk 6268: DTC P0121 (K20C2) (18-21)

- Title: DTC P0121 (K20C2) (18-21)
- Source path: `pages\7333.html`
- Chunk ID: `chunk_0fd8acd32fec`
- Images: `images\GHH404102.png`, `images\GHH404103.jpeg`, `images\GHH404104.png`, `images\GHH404105.jpeg`, `images\GHH404106.png`, `images\GHH404107.jpeg`, `images\GHH404108.png`, `images\GHH404109.jpeg`, `images\GHH404110.png`, `images\GHH404111.jpeg`, `images\GHH404112.png`, `images\GHH404113.jpeg`
- Duplicate sources: `pages\8920.html`, `pages\22540.html`, `pages\14714.html`

### Full Text

````text
points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between the PCM (E50) and the throttle body.

NO

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 6.

- Open wire check (VCC3 (DBW) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 75 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC3 (DBW) wire between the PCM (E75) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | PCM connector E (80P) No. 75

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC3 (DBW) wire between the PCM (E75) and the throttle body.

- Determine possible failure area (SG3 (DBW) line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0121 TP Sensor A Out of Range P0221 TP Sensor B Out of Range Are DTC P0121 and P0221 indicated at the same time? YES Go to step 10. NO Go to step 8.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

P0221 TP Sensor B Out of Range

Are DTC P0121 and P0221 indicated at the same time?

YES

Go to step 10.

NO

Go to step 8.

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 9.

-1.
````

## Chunk 6269: DTC P0121 (K20C2) (18-21)

- Title: DTC P0121 (K20C2) (18-21)
- Source path: `pages\7333.html`
- Chunk ID: `chunk_f11e02088047`
- Images: `images\GHH404102.png`, `images\GHH404103.jpeg`, `images\GHH404104.png`, `images\GHH404105.jpeg`, `images\GHH404106.png`, `images\GHH404107.jpeg`, `images\GHH404108.png`, `images\GHH404109.jpeg`, `images\GHH404110.png`, `images\GHH404111.jpeg`, `images\GHH404112.png`, `images\GHH404113.jpeg`
- Duplicate sources: `pages\8920.html`, `pages\22540.html`, `pages\14714.html`

### Full Text

````text
o step 8.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

P0221 TP Sensor B Out of Range

Are DTC P0121 and P0221 indicated at the same time?

YES

Go to step 10.

NO

Go to step 8.

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 9.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 9.

- Open wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 PCM connector E (80P) No. 50 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

- Open wire check (SG3(DBW) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 76 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG3 (DBW) wire between the PCM (E76) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 76

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES
````

## Chunk 6270: DTC P0121 (K20C2) (18-21)

- Title: DTC P0121 (K20C2) (18-21)
- Source path: `pages\7333.html`
- Chunk ID: `chunk_599fc6573dce`
- Images: `images\GHH404102.png`, `images\GHH404103.jpeg`, `images\GHH404104.png`, `images\GHH404105.jpeg`, `images\GHH404106.png`, `images\GHH404107.jpeg`, `images\GHH404108.png`, `images\GHH404109.jpeg`, `images\GHH404110.png`, `images\GHH404111.jpeg`, `images\GHH404112.png`, `images\GHH404113.jpeg`
- Duplicate sources: `pages\8920.html`, `pages\22540.html`, `pages\14714.html`

### Full Text

````text
symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG3 (DBW) wire between the PCM (E76) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 76

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG3 (DBW) wire between the PCM (E76) and the throttle body.
````

## Chunk 6271: DTC P0121 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0121 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7334.html`
- Chunk ID: `chunk_1aa91a5326cc`
- Images: `images\GHH404114.png`, `images\GHH404115.png`, `images\GHH404116.jpeg`, `images\GHH404117.png`, `images\GHH404118.jpeg`, `images\GHH404119.png`, `images\GHH404120.jpeg`, `images\GHH404121.png`, `images\GHH404122.jpeg`, `images\GHH404123.png`, `images\GHH404124.jpeg`, `images\GHH404125.png`, `images\GHH404126.jpeg`
- Duplicate sources: `pages\8921.html`, `pages\22541.html`, `pages\14715.html`

### Full Text

````text
# DTC P0121 (L15B7/L15BA/L15BY) (17-21)

DTC P0121 : TP Sensor A Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Wait 10 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0121 TP Sensor A Out of Range Is DTC P0121 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Wait 10 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

Is DTC P0121 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (THL1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 3: Test point 2 Throttle body 6P connector (female terminals) No. 5: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 3:

Test point 2 | Throttle body 6P connector (female terminals) No. 5:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 6.

NO

Go to step 3.

- Shorted wire check (VCC3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the VCC3 wire between the PCM (E75) and the throttle body. NO The VCC3 wire is not shorted. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the VCC3 wire between the PCM (E75) and the throttle body.

NO

The VCC3 wire is not shorted. Go to step 4.

- Open wire check (VCC3 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 75 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC3 wire is OK. Go to step 5. NO Repair an open in the VCC3 wire between the PCM (E75) and the throttle body.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No.
````

## Chunk 6272: DTC P0121 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0121 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7334.html`
- Chunk ID: `chunk_29b0d4e5c2c9`
- Images: `images\GHH404114.png`, `images\GHH404115.png`, `images\GHH404116.jpeg`, `images\GHH404117.png`, `images\GHH404118.jpeg`, `images\GHH404119.png`, `images\GHH404120.jpeg`, `images\GHH404121.png`, `images\GHH404122.jpeg`, `images\GHH404123.png`, `images\GHH404124.jpeg`, `images\GHH404125.png`, `images\GHH404126.jpeg`
- Duplicate sources: `pages\8921.html`, `pages\22541.html`, `pages\14715.html`

### Full Text

````text
(E75) and the throttle body.

NO

The VCC3 wire is not shorted. Go to step 4.

- Open wire check (VCC3 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 PCM connector E (80P) No. 75 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC3 wire is OK. Go to step 5. NO Repair an open in the VCC3 wire between the PCM (E75) and the throttle body.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | PCM connector E (80P) No. 75

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC3 wire is OK. Go to step 5.

NO

Repair an open in the VCC3 wire between the PCM (E75) and the throttle body.

- Open wire check (SG3 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 76 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK. Go to step 8. NO Repair an open in the SG3 wire between the PCM (E76) and the throttle body.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 76

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 wire is OK. Go to step 8.

NO

Repair an open in the SG3 wire between the PCM (E76) and the throttle body.

- Shorted wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the THL1 wire between the PCM (E50) and the throttle body. NO The THL1 wire is not shorted. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between the PCM (E50) and the throttle body.

NO

The THL1 wire is not shorted. Go to step 7.

- Open wire check (THL1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 PCM connector E (80P) No. 50 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The THL1 wire is OK. Go to step 8. NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Go to step 8.

NO

Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

- Throttle body check -1. Substitute a known-good throttle body . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS.
````

## Chunk 6273: DTC P0121 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0121 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7334.html`
- Chunk ID: `chunk_e565a9ba032f`
- Images: `images\GHH404114.png`, `images\GHH404115.png`, `images\GHH404116.jpeg`, `images\GHH404117.png`, `images\GHH404118.jpeg`, `images\GHH404119.png`, `images\GHH404120.jpeg`, `images\GHH404121.png`, `images\GHH404122.jpeg`, `images\GHH404123.png`, `images\GHH404124.jpeg`, `images\GHH404125.png`, `images\GHH404126.jpeg`
- Duplicate sources: `pages\8921.html`, `pages\22541.html`, `pages\14715.html`

### Full Text

````text
the PCM (E50) and the throttle body.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Go to step 8.

NO

Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

- Throttle body check -1. Substitute a known-good throttle body . -2. Reconnect all connectors. -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Clear the DTC with the HDS. Clear DTC -6. Wait 10 seconds or more. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0121 TP Sensor A Out of Range Is DTC P0121 indicated? YES The throttle body is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM . NO Replace the original throttle body .

-1. Substitute a known-good throttle body .

-2. Reconnect all connectors.

-3. Exit the SCS mode with the HDS.

-4. Turn the vehicle to the ON mode.

-5. Clear the DTC with the HDS.

Clear DTC

-6. Wait 10 seconds or more.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Out of Range

Is DTC P0121 indicated?

YES

The throttle body is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original throttle body .
````

## Chunk 6274: DTC P0121, P0221 (K20C1) (17-21)

- Title: DTC P0121, P0221 (K20C1) (17-21)
- Source path: `pages\7335.html`
- Chunk ID: `chunk_8a7103a9f840`
- Images: none
- Duplicate sources: `pages\8922.html`, `pages\22542.html`, `pages\14716.html`

### Full Text

````text
# DTC P0121, P0221 (K20C1) (17-21)

DTC P0121 : TP Sensor A Range/Performance Problem

DTC P0221 : TP Sensor B Range/Performance Problem

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Range/Performance Problem

P0221 TP Sensor B Range/Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0121 TP Sensor A Range/Performance Problem P0221 TP Sensor B Range/Performance Problem Is DTC P0121 and/or P0221 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0121 TP Sensor A Range/Performance Problem

P0221 TP Sensor B Range/Performance Problem

Is DTC P0121 and/or P0221 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (throttle body, others) -1. Check the parameter(s) below with the HDS. Signal Current conditions Values Unit TP SENSOR A TP SENSOR B Are they the same voltage? YES Go to step 3. NO Replace the throttle body .

-1. Check the parameter(s) below with the HDS.

Signal | Current conditions

Values | Unit

TP SENSOR A

TP SENSOR B

Are they the same voltage?

YES

Go to step 3.

NO

Replace the throttle body .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 88 Test point 2 PCM connector No. 1 (96P) No. 89 Is there continuity? YES Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 and/or P0221 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Test point 1 | PCM connector No. 1 (96P) No. 88

Test point 2 | PCM connector No. 1 (96P) No. 89

Is there continuity?

YES

Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0121 and/or P0221 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (THL1 line to THL2 line) -1. Disconnect the following connector. Throttle body 6P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Throttle body 6P connector: disconnected Test point 1 PCM connector No. 1 (96P) No. 88 Test point 2 PCM connector No. 1 (96P) No. 89 Is there continuity? YES Repair a short in the THL1 wire to the THL2 wire between the PCM and the throttle body. NO Replace the throttle body .

-1. Disconnect the following connector.

Throttle body 6P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | PCM connector No. 1 (96P) No. 88

Test point 2 | PCM connector No. 1 (96P) No. 89

Is there continuity?

YES
````

## Chunk 6275: DTC P0121, P0221 (K20C1) (17-21)

- Title: DTC P0121, P0221 (K20C1) (17-21)
- Source path: `pages\7335.html`
- Chunk ID: `chunk_ce0a9731ad45`
- Images: none
- Duplicate sources: `pages\8922.html`, `pages\22542.html`, `pages\14716.html`

### Full Text

````text
dy 6P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Throttle body 6P connector: disconnected Test point 1 PCM connector No. 1 (96P) No. 88 Test point 2 PCM connector No. 1 (96P) No. 89 Is there continuity? YES Repair a short in the THL1 wire to the THL2 wire between the PCM and the throttle body. NO Replace the throttle body .

-1. Disconnect the following connector.

Throttle body 6P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | PCM connector No. 1 (96P) No. 88

Test point 2 | PCM connector No. 1 (96P) No. 89

Is there continuity?

YES

Repair a short in the THL1 wire to the THL2 wire between the PCM and the throttle body.

NO

Replace the throttle body .
````

## Chunk 6276: DTC P0122 (K20C1) (17-21)

- Title: DTC P0122 (K20C1) (17-21)
- Source path: `pages\7336.html`
- Chunk ID: `chunk_8bd269e3d895`
- Images: `images\GHH404127.png`, `images\GHH404128.jpeg`, `images\GHH404129.png`, `images\GHH404130.jpeg`, `images\GHH404131.png`, `images\GHH404132.jpeg`
- Duplicate sources: `pages\8923.html`, `pages\22543.html`, `pages\14717.html`

### Full Text

````text
# DTC P0122 (K20C1) (17-21)

DTC P0122 : TP Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0122 TP Sensor A Circuit Low Voltage Is DTC P0122 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

Is DTC P0122 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (THL1 line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0122 TP Sensor A Circuit Low Voltage P0222 TP Sensor B Circuit Low Voltage Are DTC P0122 and P0222 indicated at the same time? YES Go to step 4. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

P0222 TP Sensor B Circuit Low Voltage

Are DTC P0122 and P0222 indicated at the same time?

YES

Go to step 4.

NO

Go to step 3.

- Shorted wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector No. 1 (96P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the THL1 wire between PCM connector No. 1 terminal No. 89 and the throttle body. NO The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector No. 1 (96P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between PCM connector No. 1 terminal No. 89 and the throttle body.

NO

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4.
````

## Chunk 6277: DTC P0122 (K20C1) (17-21)

- Title: DTC P0122 (K20C1) (17-21)
- Source path: `pages\7336.html`
- Chunk ID: `chunk_3d15bfaff0f7`
- Images: `images\GHH404127.png`, `images\GHH404128.jpeg`, `images\GHH404129.png`, `images\GHH404130.jpeg`, `images\GHH404131.png`, `images\GHH404132.jpeg`
- Duplicate sources: `pages\8923.html`, `pages\22543.html`, `pages\14717.html`

### Full Text

````text
ute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 5.

- Open wire check (VCC THL line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 61 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC THL wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC THL wire between PCM connector No. 1 terminal No. 61 and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 61

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC THL wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC THL wire between PCM connector No. 1 terminal No. 61 and the throttle body.
````

## Chunk 6278: DTC P0122 (K20C2)

- Title: DTC P0122 (K20C2)
- Source path: `pages\7337.html`
- Chunk ID: `chunk_bb03079f3285`
- Images: `images\GHH404133.jpeg`, `images\GHH404134.jpeg`, `images\GHH404135.jpeg`
- Duplicate sources: `pages\8924.html`, `pages\22544.html`, `pages\14718.html`

### Full Text

````text
# DTC P0122 (K20C2)

DTC P0122 : TP Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A Less than 0.3 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | Less than 0.3 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (THL1 line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0122 TP Sensor A Circuit Low Voltage P0222 TP Sensor B Circuit Low Voltage Are DTC P0122 and P0222 indicated at the same time? YES Go to step 4. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

P0222 TP Sensor B Circuit Low Voltage

Are DTC P0122 and P0222 indicated at the same time?

YES

Go to step 4.

NO

Go to step 3.

- Shorted wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the THL1 wire between the PCM (E50) and the throttle body. NO The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between the PCM (E50) and the throttle body.

NO

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode
````

## Chunk 6279: DTC P0122 (K20C2)

- Title: DTC P0122 (K20C2)
- Source path: `pages\7337.html`
- Chunk ID: `chunk_171fda103a07`
- Images: `images\GHH404133.jpeg`, `images\GHH404134.jpeg`, `images\GHH404135.jpeg`
- Duplicate sources: `pages\8924.html`, `pages\22544.html`, `pages\14718.html`

### Full Text

````text
the PCM was substituted, replace the original PCM .

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 5.

- Open wire check (VCC3 (DBW) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 PCM connector E (80P) No. 75 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC3 (DBW) wire between the PCM (E75) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 5

Test point 2 | PCM connector E (80P) No. 75

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC3 (DBW) wire between the PCM (E75) and the throttle body.
````

## Chunk 6280: DTC P0122 (L15B7/L15BA/L15BY)

- Title: DTC P0122 (L15B7/L15BA/L15BY)
- Source path: `pages\7338.html`
- Chunk ID: `chunk_91eff0764bbe`
- Images: `images\GHH404136.jpeg`, `images\GHH404137.jpeg`, `images\GHH404138.jpeg`
- Duplicate sources: `pages\8925.html`, `pages\22397.html`, `pages\14996.html`

### Full Text

````text
# DTC P0122 (L15B7/L15BA/L15BY)

DTC P0122 : TP Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A Less than 0.3 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | Less than 0.3 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (THL1 line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0122 TP Sensor A Circuit Low Voltage P0222 TP Sensor B Circuit Low Voltage Are DTC P0122 and P0222 indicated at the same time? YES Go to step 4. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0122 TP Sensor A Circuit Low Voltage

P0222 TP Sensor B Circuit Low Voltage

Are DTC P0122 and P0222 indicated at the same time?

YES

Go to step 4.

NO

Go to step 3.

- Shorted wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the THL1 wire between the PCM (E50) and the throttle body. NO The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the THL1 wire between the PCM (E50) and the throttle body.

NO

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (VCC3 line, throttle body) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode
````

## Chunk 6281: DTC P0122 (L15B7/L15BA/L15BY)

- Title: DTC P0122 (L15B7/L15BA/L15BY)
- Source path: `pages\7338.html`
- Chunk ID: `chunk_4ad848c2a5d6`
- Images: `images\GHH404136.jpeg`, `images\GHH404137.jpeg`, `images\GHH404138.jpeg`
- Duplicate sources: `pages\8925.html`, `pages\22397.html`, `pages\14996.html`

### Full Text

````text
PCM was substituted, replace the original PCM .

- Determine possible failure area (VCC3 line, throttle body) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 5.

- Open wire check (VCC3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector No. 5 Test point 2 PCM connector E (80P) No. 75 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC3 wire between the PCM (E75) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 5

Test point 2 | PCM connector E (80P) No. 75

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0122 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC3 wire between the PCM (E75) and the throttle body.
````

## Chunk 6282: DTC P0123 (K20C1) (17-21)

- Title: DTC P0123 (K20C1) (17-21)
- Source path: `pages\7339.html`
- Chunk ID: `chunk_15b6bc86f149`
- Images: `images\GHH404139.png`, `images\GHH404140.jpeg`, `images\GHH404141.png`, `images\GHH404142.jpeg`, `images\GHH404143.png`, `images\GHH404144.jpeg`
- Duplicate sources: `pages\8926.html`, `pages\22398.html`, `pages\14799.html`

### Full Text

````text
# DTC P0123 (K20C1) (17-21)

DTC P0123 : TP Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0123 TP Sensor A Circuit High Voltage Is DTC P0123 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

Is DTC P0123 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (SG THL line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0123 TP Sensor A Circuit High Voltage P0223 TP Sensor B Circuit High Voltage Are DTC P0123 and P0223 indicated at the same time? YES Go to step 5. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

P0223 TP Sensor B Circuit High Voltage

Are DTC P0123 and P0223 indicated at the same time?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 4.

- Open wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Throttle body 6P connector (female terminals) No. 6: Test point 2 PCM connector No. 1 (96P) No. 89 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between PCM connector No. 1 terminal No. 89 and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | PCM connector No. 1 (96P) No. 89

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK.
````

## Chunk 6283: DTC P0123 (K20C1) (17-21)

- Title: DTC P0123 (K20C1) (17-21)
- Source path: `pages\7339.html`
- Chunk ID: `chunk_12cd5be04f91`
- Images: `images\GHH404139.png`, `images\GHH404140.jpeg`, `images\GHH404141.png`, `images\GHH404142.jpeg`, `images\GHH404143.png`, `images\GHH404144.jpeg`
- Duplicate sources: `pages\8926.html`, `pages\22398.html`, `pages\14799.html`

### Full Text

````text
bleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between PCM connector No. 1 terminal No. 89 and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 6:

Test point 2 | PCM connector No. 1 (96P) No. 89

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the THL1 wire between PCM connector No. 1 terminal No. 89 and the throttle body.

- Open wire check (SG THL line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector No. 1 (96P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector (female terminals) No. 3: Test point 2 PCM connector No. 1 (96P) No. 23 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG THL wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG THL wire between PCM connector No. 1 terminal No. 23 and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector No. 1 (96P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector (female terminals) No. 3:

Test point 2 | PCM connector No. 1 (96P) No. 23

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG THL wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG THL wire between PCM connector No. 1 terminal No. 23 and the throttle body.
````

## Chunk 6284: DTC P0123 (K20C2)

- Title: DTC P0123 (K20C2)
- Source path: `pages\7340.html`
- Chunk ID: `chunk_26c1a0c9c17d`
- Images: `images\GHH404145.jpeg`, `images\GHH404146.jpeg`, `images\GHH404147.jpeg`
- Duplicate sources: `pages\8927.html`, `pages\22399.html`, `pages\14997.html`

### Full Text

````text
# DTC P0123 (K20C2)

DTC P0123 : TP Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A More than 4.8 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | More than 4.8 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (SG3 (DBW) line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0123 TP Sensor A Circuit High Voltage P0223 TP Sensor B Circuit High Voltage Are DTC P0123 and P0223 indicated at the same time? YES Go to step 5. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

P0223 TP Sensor B Circuit High Voltage

Are DTC P0123 and P0223 indicated at the same time?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (throttle body, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 4.

- Open wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 PCM connector E (80P) No. 50 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK.
````

## Chunk 6285: DTC P0123 (K20C2)

- Title: DTC P0123 (K20C2)
- Source path: `pages\7340.html`
- Chunk ID: `chunk_99f19cffdbfa`
- Images: `images\GHH404145.jpeg`, `images\GHH404146.jpeg`, `images\GHH404147.jpeg`
- Duplicate sources: `pages\8927.html`, `pages\22399.html`, `pages\14997.html`

### Full Text

````text
formation related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

- Open wire check (SG3 (DBW) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 3 Test point 2 PCM connector E (80P) No. 76 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG3 (DBW) wire between the PCM (E76) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 3

Test point 2 | PCM connector E (80P) No. 76

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 (DBW) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG3 (DBW) wire between the PCM (E76) and the throttle body.
````

## Chunk 6286: DTC P0123 (L15B7/L15BA/L15BY)

- Title: DTC P0123 (L15B7/L15BA/L15BY)
- Source path: `pages\7341.html`
- Chunk ID: `chunk_e18187bb1ab0`
- Images: `images\GHH404148.jpeg`, `images\GHH404149.jpeg`, `images\GHH404150.jpeg`
- Duplicate sources: `pages\8928.html`, `pages\22400.html`, `pages\14998.html`

### Full Text

````text
# DTC P0123 (L15B7/L15BA/L15BY)

DTC P0123 : TP Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit TP SENSOR A More than 4.8 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

TP SENSOR A | More than 4.8 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (SG3 line, others) -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0123 TP Sensor A Circuit High Voltage P0223 TP Sensor B Circuit High Voltage Are DTC P0123 and P0223 indicated at the same time? YES Go to step 5. NO Go to step 3.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0123 TP Sensor A Circuit High Voltage

P0223 TP Sensor B Circuit High Voltage

Are DTC P0123 and P0223 indicated at the same time?

YES

Go to step 5.

NO

Go to step 3.

- Determine possible failure area (THL1 line, throttle body) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Throttle body 6P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the throttle body . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Throttle body 6P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the throttle body .

NO

Go to step 4.

- Open wire check (THL1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Throttle body 6P connector: disconnected PCM connector E (80P): disconnected Test point 1 Throttle body 6P connector No. 6 Test point 2 PCM connector E (80P) No. 50 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK.
````

## Chunk 6287: DTC P0123 (L15B7/L15BA/L15BY)

- Title: DTC P0123 (L15B7/L15BA/L15BY)
- Source path: `pages\7341.html`
- Chunk ID: `chunk_ed472aa4c024`
- Images: `images\GHH404148.jpeg`, `images\GHH404149.jpeg`, `images\GHH404150.jpeg`
- Duplicate sources: `pages\8928.html`, `pages\22400.html`, `pages\14998.html`

### Full Text

````text
formation related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Throttle body 6P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Throttle body 6P connector No. 6

Test point 2 | PCM connector E (80P) No. 50

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The THL1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the THL1 wire between the PCM (E50) and the throttle body.

- Open wire check (SG3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector E (80P) Throttle body 6P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Throttle body 6P connector: disconnected Test point 1 Throttle body 6P connector No. 3 Test point 2 PCM connector E (80P) No. 76 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG3 wire between the PCM (E76) and the throttle body.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector E (80P)

Throttle body 6P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Throttle body 6P connector: disconnected

Test point 1 | Throttle body 6P connector No. 3

Test point 2 | PCM connector E (80P) No. 76

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG3 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0123 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG3 wire between the PCM (E76) and the throttle body.
````

## Chunk 6288: DTC P0125 (K20C2)

- Title: DTC P0125 (K20C2)
- Source path: `pages\7342.html`
- Chunk ID: `chunk_9e05a67211d0`
- Images: none
- Duplicate sources: `pages\8929.html`, `pages\22401.html`, `pages\14999.html`

### Full Text

````text
# DTC P0125 (K20C2)

DTC P0125 : ECT Sensor 1 Malfunction/Slow Response

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0125 ECT Sensor 1 Malfunction/Slow Response

DTC (PGM-FI)

- ECT sensor 1 check -1. Start the engine, and let it idle for 5 minutes or more. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0 deg.F Less than -18 deg.C Do the current condition (s) match the threshold? YES Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If they are OK, replace ECT sensor 1 . NO Go to step 2.

-1. Start the engine, and let it idle for 5 minutes or more.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0 | deg.F

Less than -18 | deg.C

Do the current condition (s) match the threshold?

YES

Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If they are OK, replace ECT sensor 1 .

NO

Go to step 2.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Allow the engine to cool to 104 deg.F (40 deg.C) or less. -3. Start the engine, and let it idle until ECT SENSOR 1 goes up to about 158 deg.F (70 deg.C). Signal Current conditions Values Unit ECT SENSOR 1 -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 2 About 158 deg.F About 70 deg.C Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Allow the engine to cool to 104 deg.F (40 deg.C) or less.

-3. Start the engine, and let it idle until ECT SENSOR 1 goes up to about 158 deg.F (70 deg.C).

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 2 | About 158 | deg.F

About 70 | deg.C

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Thermostat check -1. Check the thermostat . Is the thermostat OK? YES Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the connections and terminals are OK, replace ECT sensor 1 . NO Replace the thermostat .

-1. Check the thermostat .

Is the thermostat OK?

YES

Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the connections and terminals are OK, replace ECT sensor 1 .

NO

Replace the thermostat .
````

## Chunk 6289: DTC P0125 (L15B7/L15BA/L15BY)

- Title: DTC P0125 (L15B7/L15BA/L15BY)
- Source path: `pages\7343.html`
- Chunk ID: `chunk_f3acb703e071`
- Images: none
- Duplicate sources: `pages\8930.html`, `pages\22402.html`, `pages\15000.html`

### Full Text

````text
# DTC P0125 (L15B7/L15BA/L15BY)

DTC P0125 : ECT Sensor 1 Malfunction/Slow Response

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0125 ECT Sensor 1 Malfunction/Slow Response

DTC (PGM-FI)

- ECT sensor 1 check -1. Start the engine, and let it idle for 5 minutes or more. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 1 Less than 0 deg.F Less than -18 deg.C Do the current condition (s) match the threshold? YES Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If they are OK, replace ECT sensor 1 . NO Go to step 2.

-1. Start the engine, and let it idle for 5 minutes or more.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 1 | Less than 0 | deg.F

Less than -18 | deg.C

Do the current condition (s) match the threshold?

YES

Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If they are OK, replace ECT sensor 1 .

NO

Go to step 2.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Allow the engine to cool to 104 deg.F (40 deg.C) or less. -3. Start the engine, and let it idle until ECT SENSOR 1 goes up to about 158 deg.F (70 deg.C). Signal Current conditions Values Unit ECT SENSOR 1 -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit ECT SENSOR 2 About 158 deg.F About 70 deg.C Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Allow the engine to cool to 104 deg.F (40 deg.C) or less.

-3. Start the engine, and let it idle until ECT SENSOR 1 goes up to about 158 deg.F (70 deg.C).

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

ECT SENSOR 2 | About 158 | deg.F

About 70 | deg.C

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Thermostat check -1. Check the thermostat . Is the thermostat OK? YES Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the connections and terminals are OK, replace ECT sensor 1 . NO Replace the thermostat .

-1. Check the thermostat .

Is the thermostat OK?

YES

Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the connections and terminals are OK, replace ECT sensor 1 .

NO

Replace the thermostat .
````

## Chunk 6290: DTC P0127

- Title: DTC P0127
- Source path: `pages\7344.html`
- Chunk ID: `chunk_e41be71c2582`
- Images: none
- Duplicate sources: `pages\8931.html`, `pages\22403.html`, `pages\14800.html`

### Full Text

````text
# DTC P0127

DTC P0127 : IAT Sensor Too High

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0127 IAT Sensor Too High

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0110 IAT Sensor 1 Out of Range P0111 IAT Sensor 1 Circuit Range/Performance Problem P0112 IAT Sensor 1 Circuit Low Voltage P0113 IAT Sensor 1 Circuit High Voltage P011B IAT Sensor 1 Circuit Range/Performance Problem P0127 IAT Sensor Too High Are DTC P0127 and P0110, P0111, P0112, P0113, or P011B indicated at the same time? YES Go to the indicated DTC's troubleshooting. NO Replace MAF sensor/IAT sensor 1 .

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0110 IAT Sensor 1 Out of Range

P0111 IAT Sensor 1 Circuit Range/Performance Problem

P0112 IAT Sensor 1 Circuit Low Voltage

P0113 IAT Sensor 1 Circuit High Voltage

P011B IAT Sensor 1 Circuit Range/Performance Problem

P0127 IAT Sensor Too High

Are DTC P0127 and P0110, P0111, P0112, P0113, or P011B indicated at the same time?

YES

Go to the indicated DTC's troubleshooting.

NO

Replace MAF sensor/IAT sensor 1 .
````

## Chunk 6291: DTC P0128 (K20C1) (17-21)

- Title: DTC P0128 (K20C1) (17-21)
- Source path: `pages\7345.html`
- Chunk ID: `chunk_7af0ffab5d4a`
- Images: none
- Duplicate sources: `pages\8932.html`, `pages\22404.html`, `pages\14801.html`

### Full Text

````text
# DTC P0128 (K20C1) (17-21)

DTC P0128 : Cooling System Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0128 Cooling System Malfunction

DTC (PGM-FI)

- Radiator fan control command check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the blower switch off. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FAN HIGH CTRL OFF FAN LOW CTRL OFF Do the current condition (s) match the threshold? YES Go to step 2. NO Wait until the FAN HIGH CTRL and the FAN LOW CTRL are OFF, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the blower switch off.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FAN HIGH CTRL | OFF

FAN LOW CTRL | OFF

Do the current condition (s) match the threshold?

YES

Go to step 2.

NO

Wait until the FAN HIGH CTRL and the FAN LOW CTRL are OFF, then go to step 2.

- Radiator fan operation check -1. Check the radiator fan operation. Does the radiator fan keep running? YES Go to step 3. NO Go to step 4.

-1. Check the radiator fan operation.

Does the radiator fan keep running?

YES

Go to step 3.

NO

Go to step 4.

- Radiator fan circuit and radiator fan relay check -1. Check the radiator fan circuit and the radiator fan relay. Is it OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM . NO Repair the radiator fan circuit, and the radiator fan relay.

-1. Check the radiator fan circuit and the radiator fan relay.

Is it OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM .

NO

Repair the radiator fan circuit, and the radiator fan relay.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Let the engine cool until the coolant temperature is 104 deg.F (40 deg.C) or less. -3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 ECT SENSOR 2 -4. Start the engine, and let it idle. -5. Let the engine idle until ECT SENSOR 1 goes up 40 deg.F (22 deg.C) or more from the recorded start temperature. Signal Current conditions Values Unit ECT SENSOR 1 -6. Check ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 2 -7. Compare the recorded start value of ECT SENSOR 2 and the present value of ECT SENSOR 2. Did the temperature rise 13 deg.F (7 deg.C) or more? YES Test the thermostat and replace it if needed. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Let the engine cool until the coolant temperature is 104 deg.F (40 deg.C) or less.

-3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ECT SENSOR 2

-4. Start the engine, and let it idle.

-5. Let the engine idle until ECT SENSOR 1 goes up 40 deg.F (22 deg.C) or more from the recorded start temperature.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-6. Check ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 2

-7. Compare the recorded start value of ECT SENSOR 2 and the present value of ECT SENSOR 2.

Did the temperature rise 13 deg.F (7 deg.C) or more?

YES

Test the thermostat and replace it if needed.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6292: DTC P0128 (K20C2)

- Title: DTC P0128 (K20C2)
- Source path: `pages\7346.html`
- Chunk ID: `chunk_c1195e29c908`
- Images: none
- Duplicate sources: `pages\8933.html`, `pages\22405.html`, `pages\15001.html`

### Full Text

````text
# DTC P0128 (K20C2)

DTC P0128 : Cooling System Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0128 Cooling System Malfunction

DTC (PGM-FI)

- Radiator fan control command check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the blower switch off. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit RADIATOR FAN CONTROL About 0 % Do the current condition (s) match the threshold? YES Go to step 2. NO Wait until the RADIATOR FAN CONTROL is about 0 %, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the blower switch off.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

RADIATOR FAN CONTROL | About 0 | %

Do the current condition (s) match the threshold?

YES

Go to step 2.

NO

Wait until the RADIATOR FAN CONTROL is about 0 %, then go to step 2.

- Radiator fan operation check -1. Check the radiator fan operation. Does the radiator fan keep running? YES Go to step 3. NO Go to step 4.

-1. Check the radiator fan operation.

Does the radiator fan keep running?

YES

Go to step 3.

NO

Go to step 4.

- Radiator fan circuit and RFC relay check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the RFC unit, the radiator fan circuit, and the RFC relay. Are they OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM . NO Check the radiator fan circuit and the RFC relay, if they are OK, replace the RFC unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the RFC unit, the radiator fan circuit, and the RFC relay.

Are they OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM .

NO

Check the radiator fan circuit and the RFC relay, if they are OK, replace the RFC unit .

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Let the engine cool until the coolant temperature is 122 deg.F (50 deg.C) or less. -3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 ECT SENSOR 2 -4. Start the engine. -5. Let the engine idle until ECT SENSOR 1 goes up 36 deg.F (20 deg.C) or more from the recorded temperature. Signal Current conditions Values Unit ECT SENSOR 1 -6. Check ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 2 -7. Compare the recorded value of ECT SENSOR 2 and the present value of ECT SENSOR 2. Did the temperature rise 14 deg.F (8 deg.C) or more? YES Test the thermostat and replace it if needed. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Let the engine cool until the coolant temperature is 122 deg.F (50 deg.C) or less.

-3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ECT SENSOR 2

-4. Start the engine.

-5. Let the engine idle until ECT SENSOR 1 goes up 36 deg.F (20 deg.C) or more from the recorded temperature.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-6. Check ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 2

-7. Compare the recorded value of ECT SENSOR 2 and the present value of ECT SENSOR 2.

Did the temperature rise 14 deg.F (8 deg.C) or more?

YES

Test the thermostat and replace it if needed.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6293: DTC P0128 (L15B7/L15BA/L15BY)

- Title: DTC P0128 (L15B7/L15BA/L15BY)
- Source path: `pages\7347.html`
- Chunk ID: `chunk_c1cebfd68ef7`
- Images: none
- Duplicate sources: `pages\8934.html`, `pages\22406.html`, `pages\15002.html`

### Full Text

````text
# DTC P0128 (L15B7/L15BA/L15BY)

DTC P0128 : Cooling System Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0128 Cooling System Malfunction

DTC (PGM-FI)

- Radiator fan control command check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the blower switch off. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit RADIATOR FAN CONTROL About 0 % Do the current condition (s) match the threshold? YES Go to step 2. NO Wait until the RADIATOR FAN CONTROL is about 0 %, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the blower switch off.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

RADIATOR FAN CONTROL | About 0 | %

Do the current condition (s) match the threshold?

YES

Go to step 2.

NO

Wait until the RADIATOR FAN CONTROL is about 0 %, then go to step 2.

- Cooling fan operation check -1. Check the cooling fan operation. Does the cooling fan keep running? YES Go to step 3. NO Go to step 4.

-1. Check the cooling fan operation.

Does the cooling fan keep running?

YES

Go to step 3.

NO

Go to step 4.

- Cooling fan circuit and RFC relay check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the cooling fan circuit and the RFC relay. Are they OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM . NO Check the cooling fan circuit and the RFC relay, if they are OK, replace the RFC unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the cooling fan circuit and the RFC relay.

Are they OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0128 goes away and the PCM was substituted, replace the original PCM .

NO

Check the cooling fan circuit and the RFC relay, if they are OK, replace the RFC unit .

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Let the engine cool until the coolant temperature is 104 deg.F (40 deg.C) or less. -3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 1 ECT SENSOR 2 -4. Start the engine, and let it idle. -5. Let the engine idle until ECT SENSOR 1 goes up 40 deg.F (22 deg.C) or more from the recorded start temperature. Signal Current conditions Values Unit ECT SENSOR 1 -6. Check ECT SENSOR 2 in the DATA LIST with the HDS. Signal Current conditions Values Unit ECT SENSOR 2 -7. Compare the recorded start value of ECT SENSOR 2 and the present value of ECT SENSOR 2. Did the temperature rise 13 deg.F (7 deg.C) or more? YES Test the thermostat and replace it if needed. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Let the engine cool until the coolant temperature is 104 deg.F (40 deg.C) or less.

-3. Note the value of ECT SENSOR 1 and ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ECT SENSOR 2

-4. Start the engine, and let it idle.

-5. Let the engine idle until ECT SENSOR 1 goes up 40 deg.F (22 deg.C) or more from the recorded start temperature.

Signal | Current conditions

Values | Unit

ECT SENSOR 1

-6. Check ECT SENSOR 2 in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

ECT SENSOR 2

-7. Compare the recorded start value of ECT SENSOR 2 and the present value of ECT SENSOR 2.

Did the temperature rise 13 deg.F (7 deg.C) or more?

YES

Test the thermostat and replace it if needed.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at ECT sensor 1, ECT sensor 2, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6294: DTC P0130 (K20C2) (18-21)

- Title: DTC P0130 (K20C2) (18-21)
- Source path: `pages\7348.html`
- Chunk ID: `chunk_4817c5f00e80`
- Images: none
- Duplicate sources: `pages\8935.html`, `pages\22407.html`, `pages\15003.html`

### Full Text

````text
# DTC P0130 (K20C2) (18-21)

DTC P0130 : A/F Sensor (Sensor 1) Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0130 A/F Sensor (Sensor 1) Out of Range

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Monitor the OBD STATUS for P0130 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0130 A/F Sensor (Sensor 1) Out of Range Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Monitor the OBD STATUS for P0130 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0130 A/F Sensor (Sensor 1) Out of Range

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.
````

## Chunk 6295: DTC P0130 (L15B7/L15BA/L15BY) (17-21)

- Title: DTC P0130 (L15B7/L15BA/L15BY) (17-21)
- Source path: `pages\7349.html`
- Chunk ID: `chunk_ea66d612517e`
- Images: none
- Duplicate sources: `pages\8936.html`, `pages\22408.html`, `pages\15004.html`

### Full Text

````text
# DTC P0130 (L15B7/L15BA/L15BY) (17-21)

DTC P0130 : A/F Sensor (Sensor 1) Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0130 A/F Sensor (Sensor 1) Out of Range

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -5. Monitor the OBD STATUS for P0130 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0130 A/F Sensor (Sensor 1) Out of Range Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Monitor the OBD STATUS for P0130 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0130 A/F Sensor (Sensor 1) Out of Range

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.
````

## Chunk 6296: DTC P0131

- Title: DTC P0131
- Source path: `pages\7350.html`
- Chunk ID: `chunk_b929203b7ca1`
- Images: `images\GHH404151.png`, `images\GHH404152.jpeg`, `images\GHH404153.png`, `images\GHH404154.jpeg`
- Duplicate sources: `pages\8937.html`, `pages\22409.html`, `pages\14802.html`

### Full Text

````text
# DTC P0131

DTC P0131 : A/F Sensor (Sensor 1) Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0131 A/F Sensor (Sensor 1) Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0131 A/F Sensor (Sensor 1) Circuit Low Voltage Is DTC P0131 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0131 A/F Sensor (Sensor 1) Circuit Low Voltage

Is DTC P0131 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- A/F sensor (Sensor 1) internal circuit check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -3. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and body ground individually. Test condition Vehicle OFF (LOCK) mode A/F sensor (Sensor 1) 6P connector: disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): No. 1 No. 3 No. 4 No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity at any terminal? YES Replace the A/F sensor (Sensor 1) . NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-3. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

A/F sensor (Sensor 1) 6P connector: disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminal?

YES

Replace the A/F sensor (Sensor 1) .

NO

Go to step 3.

- Shorted wire check (LAF lines) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between the following test points and body ground individually. Test condition Vehicle OFF (LOCK) mode A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (female terminals): No. 1 No. 3 No. 4 No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity at any terminal? YES Repair a short in the wire (s) between PCM connector No. 1 terminals No. 54 (LAF VN wire), No. 36 (LAF VG wire), No. 55 (LAF CA wire), and/or No. 37 (LAF CP wire) and the A/F sensor (Sensor 1). NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0131 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between the following test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (female terminals): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminal?

YES

Repair a short in the wire (s) between PCM connector No. 1 terminals No.
````

## Chunk 6297: DTC P0131

- Title: DTC P0131
- Source path: `pages\7350.html`
- Chunk ID: `chunk_42ec1957324f`
- Images: `images\GHH404151.png`, `images\GHH404152.jpeg`, `images\GHH404153.png`, `images\GHH404154.jpeg`
- Duplicate sources: `pages\8937.html`, `pages\22409.html`, `pages\14802.html`

### Full Text

````text
ion related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0131 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between the following test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (female terminals): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminal?

YES

Repair a short in the wire (s) between PCM connector No. 1 terminals No. 54 (LAF VN wire), No. 36 (LAF VG wire), No. 55 (LAF CA wire), and/or No. 37 (LAF CP wire) and the A/F sensor (Sensor 1).

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0131 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6298: DTC P0132

- Title: DTC P0132
- Source path: `pages\7351.html`
- Chunk ID: `chunk_8a9f2f3f6435`
- Images: `images\GHH404155.png`, `images\GHH404156.jpeg`, `images\GHH404157.png`, `images\GHH404158.jpeg`
- Duplicate sources: `pages\8938.html`, `pages\22410.html`, `pages\14803.html`

### Full Text

````text
# DTC P0132

DTC P0132 : A/F Sensor (Sensor 1) Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0132 A/F Sensor (Sensor 1) Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0132 A/F Sensor (Sensor 1) Circuit High Voltage Is DTC P0132 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0132 A/F Sensor (Sensor 1) Circuit High Voltage

Is DTC P0132 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- A/F sensor (Sensor 1) internal circuit check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -3. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and the A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 individually. Test condition Vehicle OFF (LOCK) mode A/F sensor (Sensor 1) 6P connector: disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): No. 1 No. 3 No. 4 No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity at any terminals? YES Replace the A/F sensor (Sensor 1) . NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-3. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and the A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 individually.

Test condition | Vehicle OFF (LOCK) mode

A/F sensor (Sensor 1) 6P connector: disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminals?

YES

Replace the A/F sensor (Sensor 1) .

NO

Go to step 3.

- Shorted wire check (LAF lines to power) -1. Jump the SCS line with the HDS and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between the following test points and body ground individually. Test condition Vehicle ON mode A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (female terminals): No. 1 No. 3 No. 4 No. 6 Courtesy of HONDA, U.S.A., INC. Is there battery voltage at any terminal? YES Repair a short to power in the wire (s) between PCM connector No. 1 terminals No. 54 (LAF VN wire), No. 36 (LAF VG wire), No. 55 (LAF CA wire), and/or No. 37 (LAF CP wire) and the A/F sensor (Sensor 1). NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0132 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between the following test points and body ground individually.

Test condition | Vehicle ON mode

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Connector | Terminal
````

## Chunk 6299: DTC P0132

- Title: DTC P0132
- Source path: `pages\7351.html`
- Chunk ID: `chunk_898a61c8c097`
- Images: `images\GHH404155.png`, `images\GHH404156.jpeg`, `images\GHH404157.png`, `images\GHH404158.jpeg`
- Duplicate sources: `pages\8938.html`, `pages\22410.html`, `pages\14803.html`

### Full Text

````text
etween PCM connector No. 1 terminals No. 54 (LAF VN wire), No. 36 (LAF VG wire), No. 55 (LAF CA wire), and/or No. 37 (LAF CP wire) and the A/F sensor (Sensor 1). NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0132 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between the following test points and body ground individually.

Test condition | Vehicle ON mode

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (female terminals): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage at any terminal?

YES

Repair a short to power in the wire (s) between PCM connector No. 1 terminals No. 54 (LAF VN wire), No. 36 (LAF VG wire), No. 55 (LAF CA wire), and/or No. 37 (LAF CP wire) and the A/F sensor (Sensor 1).

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0132 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6300: DTC P0133 (K20C1) (17-21)

- Title: DTC P0133 (K20C1) (17-21)
- Source path: `pages\7352.html`
- Chunk ID: `chunk_3991b9843c4b`
- Images: none
- Duplicate sources: `pages\8939.html`, `pages\22411.html`, `pages\14804.html`

### Full Text

````text
# DTC P0133 (K20C1) (17-21)

DTC P0133 : A/F Sensor (Sensor 1) Malfunction/Slow Response

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

DTC (PGM-FI)

- Problem verification -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Start the engine. -5. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed ECT Sensor 1 MAP Sensor (Hi Res) REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed ECT Sensor 1 MAP Sensor (Hi Res) REL TP Sensor -7. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response Does the HDS indicate FAILED? YES Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-6 on this step and recheck.

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Start the engine.

-5. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- Engine Speed

- Vehicle Speed

- ECT Sensor 1

- MAP Sensor (Hi Res)

- REL TP Sensor

On-board Snapshot

Signal | Current conditions

Values | Unit

Engine Speed

Vehicle Speed

ECT Sensor 1

MAP Sensor (Hi Res)

REL TP Sensor

-7. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

Does the HDS indicate FAILED?

YES

Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-6 on this step and recheck.
````

## Chunk 6301: DTC P0133 (K20C2)

- Title: DTC P0133 (K20C2)
- Source path: `pages\7353.html`
- Chunk ID: `chunk_49d870c327c8`
- Images: none
- Duplicate sources: `pages\8940.html`, `pages\22412.html`, `pages\15005.html`

### Full Text

````text
# DTC P0133 (K20C2)

DTC P0133 : A/F Sensor (Sensor 1) Malfunction/Slow Response

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0139 is stored at the same time as DTC P0133, troubleshoot DTC P0139 first, then recheck for DTC P0133.

DTC Description | Confirmed DTC | Pending DTC

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle under these conditions: Engine coolant temperature (ECT SENSOR 1) above 158 deg.F (70 deg.C) CVT in D, M/T in 3rd or 4th Engine speed between 1, 250-3, 300 rpm Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at a steady speed of 32 mph (52 km/h) or more Signal Current conditions Values Unit ECT SENSOR 1 ENGINE SPEED VEHICLE SPEED -6. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-3 on this step and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle under these conditions:

- Engine coolant temperature (ECT SENSOR 1) above 158 deg.F (70 deg.C)

- CVT in D, M/T in 3rd or 4th

- Engine speed between 1, 250-3, 300 rpm

- Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at a steady speed of 32 mph (52 km/h) or more

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ENGINE SPEED

VEHICLE SPEED

-6. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-3 on this step and recheck.
````

## Chunk 6302: DTC P0133 (L15B7/L15BA/L15BY)

- Title: DTC P0133 (L15B7/L15BA/L15BY)
- Source path: `pages\7354.html`
- Chunk ID: `chunk_38b8aadc6555`
- Images: none
- Duplicate sources: `pages\8941.html`, `pages\22413.html`, `pages\15006.html`

### Full Text

````text
# DTC P0133 (L15B7/L15BA/L15BY)

DTC P0133 : A/F Sensor (Sensor 1) Malfunction/Slow Response

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0139 is stored at the same time as DTC P0133, troubleshoot DTC P0139 first, then recheck for DTC P0133.

DTC Description | Confirmed DTC | Pending DTC

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. Test-drive the vehicle under these conditions: Engine coolant temperature (ECT SENSOR 1) above 158 deg.F (70 deg.C) CVT in D, M/T in 3rd or 4th Engine speed between 1, 500-3, 000 rpm Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at a steady speed of 25 mph (41 km/h) or more Signal Current conditions Values Unit ECT SENSOR 1 ENGINE SPEED VEHICLE SPEED -6. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS. DTC Description OBD STATUS P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-3 on this step and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

Test-drive the vehicle under these conditions:

- Engine coolant temperature (ECT SENSOR 1) above 158 deg.F (70 deg.C)

- CVT in D, M/T in 3rd or 4th

- Engine speed between 1, 500-3, 000 rpm

- Drive the vehicle at 25 mph (40 km/h) or less for 5 minutes, then drive at a steady speed of 25 mph (41 km/h) or more

Signal | Current conditions

Values | Unit

ECT SENSOR 1

ENGINE SPEED

VEHICLE SPEED

-6. Monitor the OBD STATUS for DTC P0133 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P0133 A/F Sensor (Sensor 1) Malfunction/Slow Response

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-3 on this step and recheck.
````

## Chunk 6303: DTC P0134 (K20C1) (17-21)

- Title: DTC P0134 (K20C1) (17-21)
- Source path: `pages\7355.html`
- Chunk ID: `chunk_dbc44b0d5487`
- Images: none
- Duplicate sources: `pages\8942.html`, `pages\22414.html`, `pages\14805.html`

### Full Text

````text
# DTC P0134 (K20C1) (17-21)

DTC P0134 : A/F Sensor (Sensor 1) Heater System Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0135 is stored at the same time as DTC P0134, troubleshoot DTC P0135 first, then recheck for P0134.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

DTC (PGM-FI)

- Problem verification -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Start the engine, and let it idle without load (in neutral) for at least 1 minute. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: Engine Speed Vehicle Speed ECT Sensor 1 MAP Sensor (Hi Res) REL TP Sensor On-board Snapshot Signal Current conditions Values Unit Engine Speed Vehicle Speed ECT Sensor 1 MAP Sensor (Hi Res) REL TP Sensor -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0134 A/F Sensor (Sensor 1) Heater System Malfunction Is DTC P0134 indicated? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Start the engine, and let it idle without load (in neutral) for at least 1 minute.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- Engine Speed

- Vehicle Speed

- ECT Sensor 1

- MAP Sensor (Hi Res)

- REL TP Sensor

On-board Snapshot

Signal | Current conditions

Values | Unit

Engine Speed

Vehicle Speed

ECT Sensor 1

MAP Sensor (Hi Res)

REL TP Sensor

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

Is DTC P0134 indicated?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6304: DTC P0134 (K20C2)

- Title: DTC P0134 (K20C2)
- Source path: `pages\7356.html`
- Chunk ID: `chunk_3b17ed7f57bc`
- Images: `images\GHH404159.jpeg`, `images\GHH404160.jpeg`
- Duplicate sources: `pages\8943.html`, `pages\22415.html`, `pages\15007.html`

### Full Text

````text
# DTC P0134 (K20C2)

DTC P0134 : A/F Sensor (Sensor 1) Heater System Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0135 is stored at the same time as DTC P0134, troubleshoot DTC P0135 first, then recheck for P0134.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0134 A/F Sensor (Sensor 1) Heater System Malfunction Is DTC P0134 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

Is DTC P0134 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Open wire check (VS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. A/F sensor (Sensor 1) 6P connector PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 A/F sensor (Sensor 1) 6P connector No. 6 Test point 2 PCM connector E (80P) No. 73 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VS wire is OK. Go to step 3. NO Repair an open in the VS wire between the PCM (E73) and the A/F sensor (Sensor 1).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

A/F sensor (Sensor 1) 6P connector

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector No. 6

Test point 2 | PCM connector E (80P) No. 73

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VS wire is OK. Go to step 3.

NO

Repair an open in the VS wire between the PCM (E73) and the A/F sensor (Sensor 1).

- PCM internal circuit check -1. Reconnect the following connector. PCM connector E (80P) -2. Exit the SCS mode with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute. -4. Measure the voltage between test point 1 and 2. Test condition Engine running A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 A/F sensor (Sensor 1) 6P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 0.2 V or less? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM . NO Replace the A/F sensor (Sensor 1) .

-1. Reconnect the following connector.

PCM connector E (80P)

-2. Exit the SCS mode with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Measure the voltage between test point 1 and 2.

Test condition | Engine running

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6305: DTC P0134 (K20C2)

- Title: DTC P0134 (K20C2)
- Source path: `pages\7356.html`
- Chunk ID: `chunk_dc9ebf264175`
- Images: `images\GHH404159.jpeg`, `images\GHH404160.jpeg`
- Duplicate sources: `pages\8943.html`, `pages\22415.html`, `pages\15007.html`

### Full Text

````text
round Courtesy of HONDA, U.S.A., INC. Is there about 0.2 V or less? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM . NO Replace the A/F sensor (Sensor 1) .

-1. Reconnect the following connector.

PCM connector E (80P)

-2. Exit the SCS mode with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Measure the voltage between test point 1 and 2.

Test condition | Engine running

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 0.2 V or less?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the A/F sensor (Sensor 1) .
````

## Chunk 6306: DTC P0134 (L15B7/L15BA/L15BY)

- Title: DTC P0134 (L15B7/L15BA/L15BY)
- Source path: `pages\7357.html`
- Chunk ID: `chunk_b3ff689391b6`
- Images: `images\GHH404161.png`, `images\GHH404162.jpeg`, `images\GHH404163.png`, `images\GHH404164.jpeg`
- Duplicate sources: `pages\8944.html`, `pages\22416.html`, `pages\15008.html`

### Full Text

````text
# DTC P0134 (L15B7/L15BA/L15BY)

DTC P0134 : A/F Sensor (Sensor 1) Heater System Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P2251 is stored at the same time as DTC P0134, troubleshoot DTC P2251 first, then recheck for P0134.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0134 A/F Sensor (Sensor 1) Heater System Malfunction Is DTC P0134 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0134 A/F Sensor (Sensor 1) Heater System Malfunction

Is DTC P0134 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board, and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Open wire check (VS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. A/F sensor (Sensor 1) 6P connector PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 6: Test point 2 PCM connector E (80P) No. 73 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VS wire is OK. Go to step 3. NO Repair an open in the VS wire between the PCM (E73) and the A/F sensor (Sensor 1).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

A/F sensor (Sensor 1) 6P connector

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 6:

Test point 2 | PCM connector E (80P) No. 73

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VS wire is OK. Go to step 3.

NO

Repair an open in the VS wire between the PCM (E73) and the A/F sensor (Sensor 1).

- PCM internal circuit check -1. Reconnect the following connector. PCM connector E (80P) -2. Exit the SCS mode with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute. -4. Measure the voltage between test point 1 and 2. Test condition Engine running A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 6: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 0.2 V or less? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM . NO Replace the A/F sensor (Sensor 1) .

-1. Reconnect the following connector.

PCM connector E (80P)

-2. Exit the SCS mode with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Measure the voltage between test point 1 and 2.

Test condition | Engine running

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 6:

Test point 2 | Body ground
````

## Chunk 6307: DTC P0134 (L15B7/L15BA/L15BY)

- Title: DTC P0134 (L15B7/L15BA/L15BY)
- Source path: `pages\7357.html`
- Chunk ID: `chunk_17ddd07112df`
- Images: `images\GHH404161.png`, `images\GHH404162.jpeg`, `images\GHH404163.png`, `images\GHH404164.jpeg`
- Duplicate sources: `pages\8944.html`, `pages\22416.html`, `pages\15008.html`

### Full Text

````text
oint 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 0.2 V or less? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM . NO Replace the A/F sensor (Sensor 1) .

-1. Reconnect the following connector.

PCM connector E (80P)

-2. Exit the SCS mode with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) for at least 1 minute.

-4. Measure the voltage between test point 1 and 2.

Test condition | Engine running

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 6:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 0.2 V or less?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0134 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the A/F sensor (Sensor 1) .
````

## Chunk 6308: DTC P0135 (K20C1) (17-21)

- Title: DTC P0135 (K20C1) (17-21)
- Source path: `pages\7358.html`
- Chunk ID: `chunk_de36a74d7aed`
- Images: `images\GHH404165.png`, `images\GHH404166.png`, `images\GHH404167.jpeg`, `images\GHH404168.png`, `images\GHH404169.jpeg`, `images\GHH404170.png`, `images\GHH404171.jpeg`, `images\GHH404172.png`, `images\GHH404173.jpeg`, `images\GHH404174.png`, `images\GHH404175.jpeg`, `images\GHH404176.png`, `images\GHH404177.jpeg`
- Duplicate sources: `pages\8945.html`, `pages\22417.html`, `pages\14806.html`

### Full Text

````text
# DTC P0135 (K20C1) (17-21)

DTC P0135 : A/F Sensor (Sensor 1) Heater Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0135 A/F Sensor (Sensor 1) Heater Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0135 A/F Sensor (Sensor 1) Heater Circuit Malfunction Is DTC P0135 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0135 A/F Sensor (Sensor 1) Heater Circuit Malfunction

Is DTC P0135 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F sensor (Sensor 1), the relay circuit board (PGM-FI subrelay circuit), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A9 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the +B DBW wire between the No. A9 (15 A) fuse and the relay circuit board or in the IGPS (LAF)/FI SUB RLY OUT wire between the A/F sensor (Sensor 1) and the relay circuit board. Also replace the No. A9 (15 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A9 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the +B DBW wire between the No. A9 (15 A) fuse and the relay circuit board or in the IGPS (LAF)/FI SUB RLY OUT wire between the A/F sensor (Sensor 1) and the relay circuit board. Also replace the No. A9 (15 A) fuse.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 4. NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 4.

NO

Replace the relay circuit board .

- A/F sensor (Sensor 1) internal heater resistance check -1. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -2. At the A/F sensor (Sensor 1) side, measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 (sensor side): Test point 2 A/F sensor (Sensor 1) 6P connector (male terminals) No. 5 (sensor side): Courtesy of HONDA, U.S.A., INC. Is there 2.4-4.0 Ω at room temperature? YES Go to step 5. NO Replace the A/F sensor (Sensor 1) .

-1. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-2. At the A/F sensor (Sensor 1) side, measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 (sensor side):

Test point 2 | A/F sensor (Sensor 1) 6P connector (male terminals) No. 5 (sensor side):

Courtesy of HONDA, U.S.A., INC.

Is there 2.4-4.0 Ω at room temperature?

YES

Go to step 5.

NO

Replace the A/F sensor (Sensor 1) .

- A/F sensor (Sensor 1) internal circuit check (short to ground) -1. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and body ground individually. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): No. 1 No. 2 No. 3 No. 4 No. 5 No. 6 Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6309: DTC P0135 (K20C1) (17-21)

- Title: DTC P0135 (K20C1) (17-21)
- Source path: `pages\7358.html`
- Chunk ID: `chunk_99f39f18fda1`
- Images: `images\GHH404165.png`, `images\GHH404166.png`, `images\GHH404167.jpeg`, `images\GHH404168.png`, `images\GHH404169.jpeg`, `images\GHH404170.png`, `images\GHH404171.jpeg`, `images\GHH404172.png`, `images\GHH404173.jpeg`, `images\GHH404174.png`, `images\GHH404175.jpeg`, `images\GHH404176.png`, `images\GHH404177.jpeg`
- Duplicate sources: `pages\8945.html`, `pages\22417.html`, `pages\14806.html`

### Full Text

````text
6P connector: disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 (sensor side):

Test point 2 | A/F sensor (Sensor 1) 6P connector (male terminals) No. 5 (sensor side):

Courtesy of HONDA, U.S.A., INC.

Is there 2.4-4.0 Ω at room temperature?

YES

Go to step 5.

NO

Replace the A/F sensor (Sensor 1) .

- A/F sensor (Sensor 1) internal circuit check (short to ground) -1. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and body ground individually. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): No. 1 No. 2 No. 3 No. 4 No. 5 No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity at any terminal? YES Replace the A/F sensor (Sensor 1) . NO Go to step 6.

-1. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): | No. 1

No. 2

No. 3

No. 4

No. 5

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminal?

YES

Replace the A/F sensor (Sensor 1) .

NO

Go to step 6.

- A/F sensor (Sensor 1) internal circuit check -1. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and the A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 individually. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Connector Terminal A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): No. 1 No. 3 No. 4 No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity at any terminal? YES Replace the A/F sensor (Sensor 1) . NO Go to step 7.

-1. At the A/F sensor (Sensor 1) side, check for continuity between the following test points and the A/F sensor (Sensor 1) 6P connector (male terminals) No. 2 individually.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Connector | Terminal

A/F sensor (Sensor 1) 6P connector (male terminals) (sensor side): | No. 1

No. 3

No. 4

No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity at any terminal?

YES

Replace the A/F sensor (Sensor 1) .

NO

Go to step 7.

- Shorted wire check (AFHT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1). NO The AFHT wire is not shorted. Go to step 8.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | PCM connector No. 1 (96P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

NO

The AFHT wire is not shorted. Go to step 8.

- Open wire check (AFHT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The AFHT wire is OK. Go to step 9. NO Repair an open in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed
````

## Chunk 6310: DTC P0135 (K20C1) (17-21)

- Title: DTC P0135 (K20C1) (17-21)
- Source path: `pages\7358.html`
- Chunk ID: `chunk_f5f715c54e16`
- Images: `images\GHH404165.png`, `images\GHH404166.png`, `images\GHH404167.jpeg`, `images\GHH404168.png`, `images\GHH404169.jpeg`, `images\GHH404170.png`, `images\GHH404171.jpeg`, `images\GHH404172.png`, `images\GHH404173.jpeg`, `images\GHH404174.png`, `images\GHH404175.jpeg`, `images\GHH404176.png`, `images\GHH404177.jpeg`
- Duplicate sources: `pages\8945.html`, `pages\22417.html`, `pages\14806.html`

### Full Text

````text
nector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

NO

The AFHT wire is not shorted. Go to step 8.

- Open wire check (AFHT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The AFHT wire is OK. Go to step 9. NO Repair an open in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The AFHT wire is OK. Go to step 9.

NO

Repair an open in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

- Open wire check (FI SUB RLY CL- line) -1. Disconnect the following connector. PCM connector No. 2 (58P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector B (6P) (female terminals) No. 2: Test point 2 PCM connector No. 2 (58P) No. 47 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY CL- wire is OK. Go to step 10. NO Repair an open in the FI SUB RLY CL- wire between PCM connector No. 2 terminal No. 47 and the relay circuit board.

-1. Disconnect the following connector.

PCM connector No. 2 (58P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

PCM connector No. 2 (58P): disconnected

Test point 1 | Relay circuit board connector B (6P) (female terminals) No. 2:

Test point 2 | PCM connector No. 2 (58P) No. 47

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY CL- wire is OK. Go to step 10.

NO

Repair an open in the FI SUB RLY CL- wire between PCM connector No. 2 terminal No. 47 and the relay circuit board.

- Open wire check (IGPS (LAF)/FI SUB RLY OUT line) -1. Reconnect PCM connector No. 2 (58P). -2. Reinstall the relay circuit board . -3. Exit the SCS mode with the HDS. -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IGPS (LAF)/FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0135 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the IGPS (LAF)/FI SUB RLY OUT wire between the A/F sensor (Sensor 1) and the relay circuit board.

-1. Reconnect PCM connector No. 2 (58P).

-2. Reinstall the relay circuit board .

-3. Exit the SCS mode with the HDS.

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IGPS (LAF)/FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0135 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the IGPS (LAF)/FI SUB RLY OUT wire between the A/F sensor (Sensor 1) and the relay circuit board.
````

## Sources Used

- `pages\7239.html`
- `pages\7240.html`
- `pages\7241.html`
- `pages\7242.html`
- `pages\7243.html`
- `pages\7244.html`
- `pages\7245.html`
- `pages\7246.html`
- `pages\7247.html`
- `pages\7248.html`
- `pages\7249.html`
- `pages\7250.html`
- `pages\7251.html`
- `pages\7252.html`
- `pages\7253.html`
- `pages\7254.html`
- `pages\7255.html`
- `pages\7256.html`
- `pages\7257.html`
- `pages\7258.html`
- `pages\7259.html`
- `pages\7260.html`
- `pages\7261.html`
- `pages\7262.html`
- `pages\7263.html`
- `pages\7264.html`
- `pages\7265.html`
- `pages\7266.html`
- `pages\7267.html`
- `pages\7268.html`
- `pages\7269.html`
- `pages\7270.html`
- `pages\7271.html`
- `pages\7272.html`
- `pages\7273.html`
- `pages\7274.html`
- `pages\7275.html`
- `pages\7276.html`
- `pages\7277.html`
- `pages\7278.html`
- `pages\7279.html`
- `pages\7280.html`
- `pages\7281.html`
- `pages\7282.html`
- `pages\7283.html`
- `pages\7284.html`
- `pages\7285.html`
- `pages\7286.html`
- `pages\7287.html`
- `pages\7288.html`
- `pages\7289.html`
- `pages\7290.html`
- `pages\7291.html`
- `pages\7292.html`
- `pages\7293.html`
- `pages\7294.html`
- `pages\7295.html`
- `pages\7296.html`
- `pages\7297.html`
- `pages\7298.html`
- `pages\7299.html`
- `pages\7300.html`
- `pages\7301.html`
- `pages\7302.html`
- `pages\7303.html`
- `pages\7304.html`
- `pages\7305.html`
- `pages\7306.html`
- `pages\7307.html`
- `pages\7308.html`
- `pages\7309.html`
- `pages\7310.html`
- `pages\7311.html`
- `pages\7312.html`
- `pages\7313.html`
- `pages\7314.html`
- `pages\7315.html`
- `pages\7316.html`
- `pages\7317.html`
- `pages\7318.html`
- `pages\7319.html`
- `pages\7320.html`
- `pages\7321.html`
- `pages\7322.html`
- `pages\7323.html`
- `pages\7324.html`
- `pages\7325.html`
- `pages\7326.html`
- `pages\7327.html`
- `pages\7328.html`
- `pages\7329.html`
- `pages\7330.html`
- `pages\7331.html`
- `pages\7332.html`
- `pages\7333.html`
- `pages\7334.html`
- `pages\7335.html`
- `pages\7336.html`
- `pages\7337.html`
- `pages\7338.html`
- `pages\7339.html`
- `pages\7340.html`
- `pages\7341.html`
- `pages\7342.html`
- `pages\7343.html`
- `pages\7344.html`
- `pages\7345.html`
- `pages\7346.html`
- `pages\7347.html`
- `pages\7348.html`
- `pages\7349.html`
- `pages\7350.html`
- `pages\7351.html`
- `pages\7352.html`
- `pages\7353.html`
- `pages\7354.html`
- `pages\7355.html`
- `pages\7356.html`
- `pages\7357.html`
- `pages\7358.html`
