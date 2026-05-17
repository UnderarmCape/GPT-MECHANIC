# Deep Research Manual Packet 0012

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0012
- Chunk count: 334
- Chunk range: 2310-2643
- Source count: 266
- Target maximum characters: 750000

## Manual Chunks

## Chunk 2310: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)
- Source path: `pages\1146.html`
- Chunk ID: `chunk_2014f4a42739`
- Images: `images\GHH401652.png`, `images\GHH401653.png`, `images\GHH401654.jpeg`, `images\GHH401655.png`, `images\GHH401656.png`, `images\GHH401657.png`, `images\GHH401658.png`, `images\GHH401659.jpeg`, `images\GHH401660.png`, `images\GHH401661.png`, `images\GHH401662.png`, `images\GHH401663.png`, `images\GHH401664.png`, `images\GHH401665.jpeg`, `images\GHH401666.png`, `images\GHH401667.png`, `images\GHH401668.jpeg`
- Duplicate sources: `pages\16697.html`

### Full Text

````text
connector

U0100-F1 | PCM connector A (50P)

U0101-F1 *1 | PCM connector A (50P)

U0101-F1 *2 | TCM 50P connector

U0122-F1 | VSA modulator-control unit 46P connector

*1: M/T

*2: CVT

NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 11 | No. 36

U0101-F1 *1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 11 | No. 36

U0101-F1 *2 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | TCM 50P connector | No. 3

F-CAN A_L | No. 11 | No. 11

U0122-F1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | VSA modulator-control unit 46P connector | No. 20

F-CAN A_L | No. 11 | No. 21

*1: M/T

*2: CVT

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 *1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 *2 | Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known TCM , then recheck. If they are OK, replace the original TCM .

U0122-F1 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

*1: M/T

*2: CVT

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 16P connector U0100-F1 PCM connector A (50P) U0101-F1 PCM connector A (50P) U0122-F1 VSA modulator-control unit 46P connector U0131-F1 EPS control unit connector B (6P) U0151-F1 SRS unit connector A (39P) NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute. Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0101-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 U0131-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 EPS control unit connector B (6P) No. 3 F-CAN B_L No. 14 No. 1 U0151-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 SRS unit connector A (39P) No. 34 F-CAN B_L No. 14 No. 35 Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2311: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)
- Source path: `pages\1146.html`
- Chunk ID: `chunk_55849c8d2ec4`
- Images: `images\GHH401652.png`, `images\GHH401653.png`, `images\GHH401654.jpeg`, `images\GHH401655.png`, `images\GHH401656.png`, `images\GHH401657.png`, `images\GHH401658.png`, `images\GHH401659.jpeg`, `images\GHH401660.png`, `images\GHH401661.png`, `images\GHH401662.png`, `images\GHH401663.png`, `images\GHH401664.png`, `images\GHH401665.jpeg`, `images\GHH401666.png`, `images\GHH401667.png`, `images\GHH401668.jpeg`
- Duplicate sources: `pages\16697.html`

### Full Text

````text
st point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0101-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 U0131-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 EPS control unit connector B (6P) No. 3 F-CAN B_L No. 14 No. 1 U0151-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 SRS unit connector A (39P) No. 34 F-CAN B_L No. 14 No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100-F1 Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0101-F1 Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0122-F1 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit . U0131-F1 Check for poor connections or loose terminals at the CAN gateway and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit . U0151-F1 Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 16P connector

U0100-F1 | PCM connector A (50P)

U0101-F1 | PCM connector A (50P)

U0122-F1 | VSA modulator-control unit 46P connector

U0131-F1 | EPS control unit connector B (6P)

U0151-F1 | SRS unit connector A (39P)

NOTE:

- Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0101-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0122-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 14 | No. 25

U0131-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | EPS control unit connector B (6P) | No. 3

F-CAN B_L | No. 14 | No. 1

U0151-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 14 | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM.
````

## Chunk 2312: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (2/4-door: Millimeter Wave Radar) (2019 2020 2021)
- Source path: `pages\1146.html`
- Chunk ID: `chunk_90e6ad1d3301`
- Images: `images\GHH401652.png`, `images\GHH401653.png`, `images\GHH401654.jpeg`, `images\GHH401655.png`, `images\GHH401656.png`, `images\GHH401657.png`, `images\GHH401658.png`, `images\GHH401659.jpeg`, `images\GHH401660.png`, `images\GHH401661.png`, `images\GHH401662.png`, `images\GHH401663.png`, `images\GHH401664.png`, `images\GHH401665.jpeg`, `images\GHH401666.png`, `images\GHH401667.png`, `images\GHH401668.jpeg`
- Duplicate sources: `pages\16697.html`

### Full Text

````text
(50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0122-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 14 | No. 25

U0131-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | EPS control unit connector B (6P) | No. 3

F-CAN B_L | No. 14 | No. 1

U0151-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 14 | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0122-F1 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

U0131-F1 | Check for poor connections or loose terminals at the CAN gateway and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit .

U0151-F1 | Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN C_H line, F-CAN C_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 5: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 16P connector (female terminals) No. 13: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire or the F-CAN C_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

Gauge control module connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Gauge control module connector A (32P): disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 5:

Test point 2 | Gauge control module connector A (32P) No. 19

Test point 1 | CAN gateway 16P connector (female terminals) No. 13:

Test point 2 | Gauge control module connector A (32P) No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module .

NO

Repair an open in the F-CAN C_H wire or the F-CAN C_L wire between the gauge control module and the CAN gateway.
````

## Chunk 2313: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_bfd536c157d1`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
# DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

DTC U0100-F1 : Lost Communication With The PCM (PGM-FI System) (Multipurpose Camera Unit)

DTC U0101-F1 : Lost Communication With The PCM/TCM (Multipurpose Camera Unit)

DTC U0122-F1 : Lost Communication With The VSA Modulator-Control Unit (Multipurpose Camera Unit)

DTC U0131-F1 : Lost Communication With The EPS Control Unit (Multipurpose Camera Unit)

DTC U0151-F1 : Lost Communication With The SRS Unit (Multipurpose Camera Unit)

DTC U0155-F1 : Lost Communication With The Gauge Control Module (Multipurpose Camera Unit)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the transmitting control unit is malfunctioning, a DTC may be recorded. According to the recorded DTC, inspect the power circuits and ground circuits of the units with which the multipurpose camera unit does not communicate.

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0100-F1 Lost Communication With The PCM (PGM-FI System) (Multipurpose Camera Unit)

U0101-F1 Lost Communication With The PCM/TCM (Multipurpose Camera Unit)

U0122-F1 Lost Communication With The VSA Modulator-Control Unit (Multipurpose Camera Unit)

U0131-F1 Lost Communication With The EPS Control Unit (Multipurpose Camera Unit)

U0151-F1 Lost Communication With The SRS Unit (Multipurpose Camera Unit)

U0155-F1 Lost Communication With The Gauge Control Module (Multipurpose Camera Unit)

DTC (IDAS)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Check for CAN gateway system DTCs with the HDS. DTC Description DTC U0029-00 CAN Gateway F-CAN ch A Bus Off U0047-00 CAN Gateway F-CAN ch B Bus Off U3000-49 CAN Gateway Internal Failure Is DTC U0029-00, U0047-00, and/or U3000-49 indicated? YES Go to the indicated DTCs troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

U0029-00 CAN Gateway F-CAN ch A Bus Off

U0047-00 CAN Gateway F-CAN ch B Bus Off

U3000-49 CAN Gateway Internal Failure

Is DTC U0029-00, U0047-00, and/or U3000-49 indicated?

YES

Go to the indicated DTCs troubleshooting .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the millimeter wave radar detect the CAN gateway Bus channels B? Bus B is Not Available Go to step 3. Bus B is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the millimeter wave radar detect the CAN gateway Bus channels B?

Bus B is Not Available

Go to step 3.

Bus B is Available

Go to step 4.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector Multipurpose camera unit 12P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Multipurpose camera unit 12P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Multipurpose camera unit 12P connector No. 5 Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Multipurpose camera unit 12P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

Multipurpose camera unit 12P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Multipurpose camera unit 12P connector: disconnected
````

## Chunk 2314: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_4be4d1620da1`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
2P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

Multipurpose camera unit 12P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Multipurpose camera unit 12P connector: disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 5:

Test point 2 | Multipurpose camera unit 12P connector No. 5

Test point 1 | CAN gateway 12P connector (female terminals) No. 12:

Test point 2 | Multipurpose camera unit 12P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit and the CAN gateway.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0100-F1 PCM A, B U0101-F1 PCM A, B U0122-F1 VSA modulator-control unit A, B U0131-F1 EPS control unit B U0151-F1 SRS unit B U0155-F1 Gauge control module A Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100-F1: PCM is Not Available for Bus A Go to step 5. U0100-F1: PCM is Not Available for Bus B Go to step 6. U0101-F1: PCM is Not Available for Bus A Go to step 5. U0101-F1: PCM is Not Available for Bus B Go to step 6. U0122-F1: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122-F1: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0131-F1: EPS control unit is Not Available for Bus B Go to step 6. U0151-F1: SRS unit is Not Available for Bus B Go to step 6. U0155-F1: Gauge control module is Not Available for Bus A Go to step 5.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0100-F1 | PCM | A, B

U0101-F1 | PCM | A, B

U0122-F1 | VSA modulator-control unit | A, B

U0131-F1 | EPS control unit | B

U0151-F1 | SRS unit | B

U0155-F1 | Gauge control module | A

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100-F1: PCM is Not Available for Bus A

Go to step 5.

U0100-F1: PCM is Not Available for Bus B

Go to step 6.

U0101-F1: PCM is Not Available for Bus A

Go to step 5.

U0101-F1: PCM is Not Available for Bus B

Go to step 6.

U0122-F1: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122-F1: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0131-F1: EPS control unit is Not Available for Bus B

Go to step 6.

U0151-F1: SRS unit is Not Available for Bus B

Go to step 6.

U0155-F1: Gauge control module is Not Available for Bus A

Go to step 5.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).
````

## Chunk 2315: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_6c3232e69aa9`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
100-F1: PCM is Not Available for Bus A

Go to step 5.

U0100-F1: PCM is Not Available for Bus B

Go to step 6.

U0101-F1: PCM is Not Available for Bus A

Go to step 5.

U0101-F1: PCM is Not Available for Bus B

Go to step 6.

U0122-F1: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122-F1: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0131-F1: EPS control unit is Not Available for Bus B

Go to step 6.

U0151-F1: SRS unit is Not Available for Bus B

Go to step 6.

U0155-F1: Gauge control module is Not Available for Bus A

Go to step 5.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 12P connector U0100-F1 PCM connector A (50P) U0101-F1 PCM connector A (50P) U0122-F1 VSA modulator-control unit 46P connector U0155-F1 Gauge control module connector A (32P) NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN A_H CAN gateway 12P connector (female terminals) No. 3: PCM connector A (50P) No. 37 F-CAN A_L No. 9: No. 36 U0101-F1 F-CAN A_H CAN gateway 12P connector (female terminals) No. 3: PCM connector A (50P) No. 37 F-CAN A_L No. 9: No. 36 U0122-F1 F-CAN A_H CAN gateway 12P connector (female terminals) No. 3: VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 9: No. 21 U0155-F1 F-CAN A_H CAN gateway 12P connector (female terminals) No. 3: Gauge control module connector A (32P) No. 19 F-CAN A_L No. 9: No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100-F1 Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0101-F1 Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0122-F1 Check for poor connections or loose terminals at the millimeter wave radar and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit . U0155-F1 Check for poor connections or loose terminals at the millimeter wave radar and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 12P connector

U0100-F1 | PCM connector A (50P)

U0101-F1 | PCM connector A (50P)

U0122-F1 | VSA modulator-control unit 46P connector

U0155-F1 | Gauge control module connector A (32P)

NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN A_H | CAN gateway 12P connector (female terminals) | No. 3: | PCM connector A (50P) | No. 37

F-CAN A_L | No. 9: | No.
````

## Chunk 2316: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_eee099efa01b`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
ay 12P connector

U0100-F1 | PCM connector A (50P)

U0101-F1 | PCM connector A (50P)

U0122-F1 | VSA modulator-control unit 46P connector

U0155-F1 | Gauge control module connector A (32P)

NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN A_H | CAN gateway 12P connector (female terminals) | No. 3: | PCM connector A (50P) | No. 37

F-CAN A_L | No. 9: | No. 36

U0101-F1 | F-CAN A_H | CAN gateway 12P connector (female terminals) | No. 3: | PCM connector A (50P) | No. 37

F-CAN A_L | No. 9: | No. 36

U0122-F1 | F-CAN A_H | CAN gateway 12P connector (female terminals) | No. 3: | VSA modulator-control unit 46P connector | No. 20

F-CAN A_L | No. 9: | No. 21

U0155-F1 | F-CAN A_H | CAN gateway 12P connector (female terminals) | No. 3: | Gauge control module connector A (32P) | No. 19

F-CAN A_L | No. 9: | No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0122-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

U0155-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 12P connector U0100-F1 PCM connector A (50P) U0101-F1 PCM connector A (50P) U0122-F1 VSA modulator-control unit 46P connector U0131-F1 EPS control unit connector B (6P) U0151-F1 SRS unit connector A (39P) NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: PCM connector A (50P) No. 39 F-CAN B_L No. 5: No. 38 U0101-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: PCM connector A (50P) No. 39 F-CAN B_L No. 5: No. 38 U0122-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 5: No. 25 U0131-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: EPS control unit connector B (6P) No. 3 F-CAN B_L No. 5: No. 1 U0151-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: SRS unit connector A (39P) No. 34 F-CAN B_L No. 5: No. 35 Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2317: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_9ab609e27629`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
int 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: PCM connector A (50P) No. 39 F-CAN B_L No. 5: No. 38 U0101-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: PCM connector A (50P) No. 39 F-CAN B_L No. 5: No. 38 U0122-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 5: No. 25 U0131-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: EPS control unit connector B (6P) No. 3 F-CAN B_L No. 5: No. 1 U0151-F1 F-CAN B_H CAN gateway 12P connector (female terminals) No. 12: SRS unit connector A (39P) No. 34 F-CAN B_L No. 5: No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100-F1 Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . DTC Operation for transmitting control unit U0101-F1 Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0122-F1 Check for poor connections or loose terminals at the millimeter wave radar and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit . U0131-F1 Check for poor connections or loose terminals at the multipurpose camera unit and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit . U0151-F1 Check for poor connections or loose terminals at the millimeter wave radar and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 12P connector

U0100-F1 | PCM connector A (50P)

U0101-F1 | PCM connector A (50P)

U0122-F1 | VSA modulator-control unit 46P connector

U0131-F1 | EPS control unit connector B (6P)

U0151-F1 | SRS unit connector A (39P)

NOTE: Before disconnecting the PCM connector A (50P), jump the SCS line with the HDS, and wait more than 1 minute.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | PCM connector A (50P) | No. 39

F-CAN B_L | No. 5: | No. 38

U0101-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | PCM connector A (50P) | No. 39

F-CAN B_L | No. 5: | No. 38

U0122-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 5: | No. 25

U0131-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | EPS control unit connector B (6P) | No. 3

F-CAN B_L | No. 5: | No. 1

U0151-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 5: | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the PCM.
````

## Chunk 2318: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2017 2018 2019)
- Source path: `pages\1147.html`
- Chunk ID: `chunk_afb7e3940a01`
- Images: `images\GHH401669.png`, `images\GHH401670.png`, `images\GHH401671.jpeg`, `images\GHH401672.png`, `images\GHH401673.png`, `images\GHH401674.png`, `images\GHH401675.png`, `images\GHH401676.png`, `images\GHH401677.png`, `images\GHH401678.png`, `images\GHH401679.png`, `images\GHH401680.jpeg`, `images\GHH401681.png`, `images\GHH401682.png`, `images\GHH401683.png`, `images\GHH401684.png`, `images\GHH401685.png`, `images\GHH401686.png`, `images\GHH401687.png`, `images\GHH401688.png`, `images\GHH401689.png`, `images\GHH401690.png`, `images\GHH401691.jpeg`
- Duplicate sources: `pages\16497.html`

### Full Text

````text
9

F-CAN B_L | No. 5: | No. 38

U0122-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 5: | No. 25

U0131-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | EPS control unit connector B (6P) | No. 3

F-CAN B_L | No. 5: | No. 1

U0151-F1 | F-CAN B_H | CAN gateway 12P connector (female terminals) | No. 12: | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 5: | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

DTC | Operation for transmitting control unit

U0101-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0122-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

U0131-F1 | Check for poor connections or loose terminals at the multipurpose camera unit and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit .

U0151-F1 | Check for poor connections or loose terminals at the millimeter wave radar and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.
````

## Chunk 2319: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_969dd53cd478`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
# DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

DTC U0100-F1 : Lost Communication With The PCM (PGM-FI System) (Multipurpose Camera Unit)

DTC U0101-F1 : Lost Communication With The PCM/TCM (Multipurpose Camera Unit)

DTC U0122-F1 : Lost Communication With The VSA Modulator-Control Unit (Multipurpose Camera Unit)

DTC U0131-F1 : Lost Communication With The EPS Control Unit (Multipurpose Camera Unit)

DTC U0151-F1 : Lost Communication With The SRS Unit (Multipurpose Camera Unit)

DTC U0155-F1 : Lost Communication With The Gauge Control Module (Multipurpose Camera Unit)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the transmitting control unit is malfunctioning, a DTC may be recorded. According to the recorded DTC, inspect the power circuits and ground circuits of the units with which the multipurpose camera unit does not communicate.

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0100-F1 Lost Communication With The PCM (PGM-FI System) (Multipurpose Camera Unit)

U0101-F1 Lost Communication With The PCM/TCM (Multipurpose Camera Unit)

U0122-F1 Lost Communication With The VSA Modulator-Control Unit (Multipurpose Camera Unit)

U0131-F1 Lost Communication With The EPS Control Unit (Multipurpose Camera Unit)

U0151-F1 Lost Communication With The SRS Unit (Multipurpose Camera Unit)

U0155-F1 Lost Communication With The Gauge Control Module (Multipurpose Camera Unit)

DTC (IDAS)

- CAN gateway system DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the troubleshooting for CAN gateway system DTC(s) . NO Go to step 2.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the troubleshooting for CAN gateway system DTC(s) .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the CAN gateway detect the multipurpose camera unit Bus channels B? Bus B is Not Available Go to step 3. Bus B is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the CAN gateway detect the multipurpose camera unit Bus channels B?

Bus B is Not Available

Go to step 3.

Bus B is Available

Go to step 4.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector Multipurpose camera unit 12P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Multipurpose camera unit 12P connector: disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 14: Test point 2 Multipurpose camera unit 12P connector No. 5 Test point 1 CAN gateway 16P connector (female terminals) No. 6: Test point 2 Multipurpose camera unit 12P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

Multipurpose camera unit 12P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Multipurpose camera unit 12P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 14:

Test point 2 | Multipurpose camera unit 12P connector No. 5

Test point 1 | CAN gateway 16P connector (female terminals) No. 6:

Test point 2 | Multipurpose camera unit 12P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit.
````

## Chunk 2320: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_e78d52502319`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
mera unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

Multipurpose camera unit 12P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Multipurpose camera unit 12P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 14:

Test point 2 | Multipurpose camera unit 12P connector No. 5

Test point 1 | CAN gateway 16P connector (female terminals) No. 6:

Test point 2 | Multipurpose camera unit 12P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

Check for poor connections or loose terminals at the CAN gateway and the multipurpose camera unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit and the CAN gateway.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN gateway Bus channel(s) at normal U0100-F1 PCM A, B U0101-F1 *1 PCM A, B U0101-F1 *2 TCM A *1: M/T *2: CVT DTC Transmitting control unit Detected CAN gateway Bus channel(s) at normal U0122-F1 VSA modulator-control unit A, B U0131-F1 EPS control unit B U0151-F1 SRS unit B U0155-F1 Gauge control module C *1: M/T *2: CVT Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100-F1: PCM is Not Available for Bus A Go to step 5. U0100-F1: PCM is Not Available for Bus B Go to step 6. U0101-F1: PCM (M/T) or TCM (CVT) is Not Available for Bus A Go to step 5. U0101-F1: PCM is Not Available for Bus B Go to step 6. U0122-F1: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122-F1: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0131-F1: EPS control unit is Not Available for Bus B Go to step 6. U0151-F1: SRS unit is Not Available for Bus B Go to step 6. U0155-F1: Gauge control module is Not Available for Bus C Go to step 7.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN gateway Bus channel(s) at normal

U0100-F1 | PCM | A, B

U0101-F1 *1 | PCM | A, B

U0101-F1 *2 | TCM | A

*1: M/T

*2: CVT

DTC | Transmitting control unit | Detected CAN gateway Bus channel(s) at normal

U0122-F1 | VSA modulator-control unit | A, B

U0131-F1 | EPS control unit | B

U0151-F1 | SRS unit | B

U0155-F1 | Gauge control module | C

*1: M/T

*2: CVT

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100-F1: PCM is Not Available for Bus A

Go to step 5.

U0100-F1: PCM is Not Available for Bus B

Go to step 6.

U0101-F1: PCM (M/T) or TCM (CVT) is Not Available for Bus A

Go to step 5.

U0101-F1: PCM is Not Available for Bus B

Go to step 6.

U0122-F1: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122-F1: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0131-F1: EPS control unit is Not Available for Bus B

Go to step 6.

U0151-F1: SRS unit is Not Available for Bus B

Go to step 6.

U0155-F1: Gauge control module is Not Available for Bus C

Go to step 7.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 16P connector U0100-F1 PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 U0101-F1 *1 PCM connector A (50P) *3 or PCM connector No.
````

## Chunk 2321: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_5510e2fd363b`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
5.

U0101-F1: PCM is Not Available for Bus B

Go to step 6.

U0122-F1: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122-F1: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0131-F1: EPS control unit is Not Available for Bus B

Go to step 6.

U0151-F1: SRS unit is Not Available for Bus B

Go to step 6.

U0155-F1: Gauge control module is Not Available for Bus C

Go to step 7.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 16P connector U0100-F1 PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 U0101-F1 *1 PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 U0101-F1 *2 TCM 50P connector U0122-F1 VSA modulator-control unit 46P connector *1: M/T *2: CVT *3: Except Type-R *4: Type-R NOTE: Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute. *1: Except Type-R *2: Type-R -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 No. 37 *3 or No. 15 *4 F-CAN A_L No. 11 No. 36 *3 or No. 27 *4 U0101-F1 *1 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 No. 37 *3 or No. 15 *4 F-CAN A_L No. 11 No. 36 *3 or No. 27 *4 U0101-F1 *2 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 TCM 50P connector No. 3 F-CAN A_L No. 11 No. 11 U0122-F1 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 11 No. 21 *1: M/T *2: CVT *3: Except Type-R *4: Type-R Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100-F1 Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0101-F1 *1 Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0101-F1 *2 Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known TCM , then recheck. If they are OK, replace the original TCM . U0122-F1 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit . *1: M/T *2: CVT NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 16P connector

U0100-F1 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4

U0101-F1 *1 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4

U0101-F1 *2 | TCM 50P connector

U0122-F1 | VSA modulator-control unit 46P connector

*1: M/T

*2: CVT

*3: Except Type-R

*4: Type-R

NOTE: Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute.

*1: Except Type-R

*2: Type-R

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected
````

## Chunk 2322: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_839a135450bf`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
ted DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 16P connector

U0100-F1 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4

U0101-F1 *1 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4

U0101-F1 *2 | TCM 50P connector

U0122-F1 | VSA modulator-control unit 46P connector

*1: M/T

*2: CVT

*3: Except Type-R

*4: Type-R

NOTE: Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute.

*1: Except Type-R

*2: Type-R

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 | No. 37 *3 or No. 15 *4

F-CAN A_L | No. 11 | No. 36 *3 or No. 27 *4

U0101-F1 *1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) *3 or PCM connector No. 2 (58P) *4 | No. 37 *3 or No. 15 *4

F-CAN A_L | No. 11 | No. 36 *3 or No. 27 *4

U0101-F1 *2 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | TCM 50P connector | No. 3

F-CAN A_L | No. 11 | No. 11

U0122-F1 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | VSA modulator-control unit 46P connector | No. 20

F-CAN A_L | No. 11 | No. 21

*1: M/T

*2: CVT

*3: Except Type-R

*4: Type-R

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 *1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 *2 | Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known TCM , then recheck. If they are OK, replace the original TCM .

U0122-F1 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

*1: M/T

*2: CVT

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector CAN gateway 16P connector U0100-F1 PCM connector A (50P) U0101-F1 PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2 U0122-F1 VSA modulator-control unit 46P connector U0131-F1 EPS control unit connector B (6P) U0151-F1 SRS unit connector A (39P) *1: Except Type-R *2: Type-R NOTE: Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute. Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. *1: Except Type-R *2: Type-R -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No.
````

## Chunk 2323: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_ca66f8cfaf68`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
Except Type-R *2: Type-R NOTE: Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute. Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. *1: Except Type-R *2: Type-R -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0101-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2 No. 39 *1 or No. 29 *2 F-CAN B_L No. 14 No. 38 *1 or No. 17 *2 U0122-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 U0131-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 EPS control unit connector B (6P) No. 3 F-CAN B_L No. 14 No. 1 U0151-F1 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 SRS unit connector A (39P) No. 34 F-CAN B_L No. 14 No. 35 *1: Except Type-R *2: Type-R Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100-F1 Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0101-F1 * Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM . U0122-F1 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit . *: M/T DTC Operation for transmitting control unit U0131-F1 Check for poor connections or loose terminals at the CAN gateway and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit . U0151-F1 Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit . *: M/T NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

CAN gateway 16P connector

U0100-F1 | PCM connector A (50P)

U0101-F1 | PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2

U0122-F1 | VSA modulator-control unit 46P connector

U0131-F1 | EPS control unit connector B (6P)

U0151-F1 | SRS unit connector A (39P)

*1: Except Type-R

*2: Type-R

NOTE:

- Before disconnecting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

*1: Except Type-R

*2: Type-R

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38
````

## Chunk 2324: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_99c87a4c94b3`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
necting the PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2, jump the SCS line with the HDS, and wait more than 1 minute.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

*1: Except Type-R

*2: Type-R

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0101-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) *1 or PCM connector No. 2 (58P) *2 | No. 39 *1 or No. 29 *2

F-CAN B_L | No. 14 | No. 38 *1 or No. 17 *2

U0122-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 14 | No. 25

U0131-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | EPS control unit connector B (6P) | No. 3

F-CAN B_L | No. 14 | No. 1

U0151-F1 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 14 | No. 35

*1: Except Type-R

*2: Type-R

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100-F1 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0101-F1 * | Check for poor connections or loose terminals at the CAN gateway and the PCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a good-known PCM , then recheck. If they are OK, replace the original PCM .

U0122-F1 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the VSA modulator-control unit .

*: M/T

DTC | Operation for transmitting control unit

U0131-F1 | Check for poor connections or loose terminals at the CAN gateway and the EPS control unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the EPS motor/control unit .

U0151-F1 | Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the SRS unit .

*: M/T

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN C_H line, F-CAN C_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 5: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 16P connector (female terminals) No. 13: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire or the F-CAN C_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector
````

## Chunk 2325: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)

- Title: DTC U0100-F1, U0101-F1, U0122-F1, U0131-F1, U0151-F1, U0155-F1 (5-door: Millimeter Wave Radar) (2020 2021)
- Source path: `pages\1148.html`
- Chunk ID: `chunk_8ddefad83262`
- Images: `images\GHH401692.png`, `images\GHH401693.png`, `images\GHH401694.jpeg`, `images\GHH401695.png`, `images\GHH401696.png`, `images\GHH401697.png`, `images\GHH401698.png`, `images\GHH401699.jpeg`, `images\GHH401700.png`, `images\GHH401701.png`, `images\GHH401702.png`, `images\GHH401703.png`, `images\GHH401704.png`, `images\GHH401705.jpeg`, `images\GHH401706.png`, `images\GHH401707.png`, `images\GHH401708.jpeg`
- Duplicate sources: `pages\16698.html`

### Full Text

````text
5: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 16P connector (female terminals) No. 13: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire or the F-CAN C_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

Gauge control module connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Gauge control module connector A (32P): disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 5:

Test point 2 | Gauge control module connector A (32P) No. 19

Test point 1 | CAN gateway 16P connector (female terminals) No. 13:

Test point 2 | Gauge control module connector A (32P) No. 20

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good gauge control module , then recheck. If they are OK, replace the original gauge control module .

NO

Repair an open in the F-CAN C_H wire or the F-CAN C_L wire between the gauge control module and the CAN gateway.
````

## Chunk 2326: DTC U0401-53, U0401-92 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U0401-53, U0401-92 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1149.html`
- Chunk ID: `chunk_0567eb25709d`
- Images: none
- Duplicate sources: `pages\16498.html`

### Full Text

````text
# DTC U0401-53, U0401-92 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U0401-53 : Temporary stop of Integrated Driver Support System (Received stop request by PGM-FI System)

DTC U0401-92 : Temporary stop of Integrated Driver Support System (Rejected control request by PGM-FI System)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If these DTC are recorded, the following is suspected:

- - ACC operation is inhibited this way when there is a transmission malfunction, transmission and transmission fluid temperatures are too high, or if the PCM determines ACC is still active when the brake pedal is pressed. - The brake pedal position switch is failed or out of adjustment, or the brake pedal was pressed lightly while driving. (electric brake booster equipped models) - If this sets due to transmission fluid temperature, a warning will also be displayed in the MID.

- - ACC operation is inhibited this way when there is a transmission malfunction, transmission and transmission fluid temperatures are too high, or if the PCM determines ACC is still active when the brake pedal is pressed.

ACC operation is inhibited this way when there is a transmission malfunction, transmission and transmission fluid temperatures are too high, or if the PCM determines ACC is still active when the brake pedal is pressed.

- - The brake pedal position switch is failed or out of adjustment, or the brake pedal was pressed lightly while driving. (electric brake booster equipped models)

The brake pedal position switch is failed or out of adjustment, or the brake pedal was pressed lightly while driving. (electric brake booster equipped models)

- - If this sets due to transmission fluid temperature, a warning will also be displayed in the MID.

If this sets due to transmission fluid temperature, a warning will also be displayed in the MID.

- If these DTC are recorded, some of the integrated driver support system functions are temporarily canceled but it is not a failure.

- When the PCM becomes ready to receive a control request from the millimeter wave radar and the multipurpose camera unit, the temporarily cancelled integrated driver support system functions are re-activated.

- The functions of the integrated driver support system that will be temporarily canceled when these DTC are recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0401-53 Temporary stop of Integrated Driver Support System (Received stop request by PGM-FI System)

U0401-92 Temporary stop of Integrated Driver Support System (Rejected control request by PGM-FI System)

DTC (IDAS)

- DTC check -1. Turn the vehicle to the ON mode, then wait for at least 6 seconds. -2. Check for DTCs with the HDS. DTC Description DTC U0401-53 Temporary stop of Integrated Driver Support System (Received stop request by PGM-FI System) U0401-92 Temporary stop of Integrated Driver Support System (Rejected control request by PGM-FI System) Is there any DTC(s) other than DTC U0401-53 or U0401-92? YES Perform a troubleshooting for the recorded DTC. NO Clear the DTC with the HDS and explain to the customer that it is not a failure.

-1. Turn the vehicle to the ON mode, then wait for at least 6 seconds.

-2. Check for DTCs with the HDS.

DTC Description | DTC

U0401-53 Temporary stop of Integrated Driver Support System (Received stop request by PGM-FI System)

U0401-92 Temporary stop of Integrated Driver Support System (Rejected control request by PGM-FI System)

Is there any DTC(s) other than DTC U0401-53 or U0401-92?

YES

Perform a troubleshooting for the recorded DTC.

NO

Clear the DTC with the HDS and explain to the customer that it is not a failure.
````

## Chunk 2327: DTC U0416-92, U0416-9A (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U0416-92, U0416-9A (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1150.html`
- Chunk ID: `chunk_16606d22ac3e`
- Images: none
- Duplicate sources: `pages\16499.html`

### Full Text

````text
# DTC U0416-92, U0416-9A (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U0416-92 : Temporary stop of Integrated Driver Support System (Rejected control request by VSA System)

DTC U0416-9A : Temporary stop of Integrated Driver Support System (Unstable Wheel Speed Sensor Signal)

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- These DTCs are recorded when the VSA modulator-control unit cannot temporarily receives a brake request from the integrated driver support system due to a drop in the 12 volt battery voltage supplied to the VSA modulator-control unit.

- If this DTC is recorded, some of the integrated driver support system functions are temporarily canceled but it is not a failure.

- When the VSA modulator-control unit returns to normal, the temporarily cancelled integrated driver support system functions are re-activated.

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0416-92 Temporary stop of Integrated Driver Support System (Rejected control request by VSA System)

U0416-9A Temporary stop of Integrated Driver Support System (Unstable Wheel Speed Sensor Signal)

DTC (IDAS)

- DTC check -1. Turn the vehicle to the ON mode, then wait for at least 6 seconds. -2. Check for DTCs with the HDS. DTC Description DTC U0416-92 Temporary stop of Integrated Driver Support System (Rejected control request by VSA System) U0416-9A Temporary stop of Integrated Driver Support System (Unstable Wheel Speed Sensor Signal) Is there any DTC(s) other than U0416-92 or U0416-9A? YES Perform a troubleshooting for the recorded DTC. NO Clear the DTC with the HDS and explain to the customer that it is not a failure.

-1. Turn the vehicle to the ON mode, then wait for at least 6 seconds.

-2. Check for DTCs with the HDS.

DTC Description | DTC

U0416-92 Temporary stop of Integrated Driver Support System (Rejected control request by VSA System)

U0416-9A Temporary stop of Integrated Driver Support System (Unstable Wheel Speed Sensor Signal)

Is there any DTC(s) other than U0416-92 or U0416-9A?

YES

Perform a troubleshooting for the recorded DTC.

NO

Clear the DTC with the HDS and explain to the customer that it is not a failure.
````

## Chunk 2328: DTC U0417-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U0417-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1151.html`
- Chunk ID: `chunk_3522a1fd27ab`
- Images: none
- Duplicate sources: `pages\16500.html`

### Full Text

````text
# DTC U0417-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U0417-68 : Electric Parking Brake Control Unit Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTCs are recorded when the millimeter wave radar receives electric parking brake control unit failure information via the F-CAN.

- If a DTC is recorded again after it is cleared with the HDS, perform a troubleshooting for the electric parking brake system .

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0417-68 Electric Parking Brake Control Unit Malfunction

DTC (IDAS)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode, then wait for at least 6 seconds. -5. Check for DTCs with the HDS. DTC Description DTC U0417-68 Electric Parking Brake Control Unit Malfunction Is DTC U0417-68 indicated? YES The failure is duplicated. Go to the indicated DTC's troubleshooting in the electric parking brake system . NO Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode, then wait for at least 6 seconds.

-5. Check for DTCs with the HDS.

DTC Description | DTC

U0417-68 Electric Parking Brake Control Unit Malfunction

Is DTC U0417-68 indicated?

YES

The failure is duplicated. Go to the indicated DTC's troubleshooting in the electric parking brake system .

NO

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .
````

## Chunk 2329: DTC U0420-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U0420-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1152.html`
- Chunk ID: `chunk_4298d8e29d6a`
- Images: none
- Duplicate sources: `pages\16501.html`

### Full Text

````text
# DTC U0420-68 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U0420-68 : EPS Control Unit Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is recorded when the millimeter wave radar receives the EPS control unit failure information via the F-CAN.

- If a DTC is recorded again after it is cleared with the HDS, perform a troubleshooting for the EPS system .

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0420-68 EPS Control Unit Malfunction

DTC (IDAS)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode, then wait for at least 6 seconds. -5. Check for DTCs with the HDS. DTC Description DTC U0420-68 EPS Control Unit Malfunction Is DTC U0420-68 indicated? YES The failure is duplicated. Go to the indicated DTC's troubleshooting in the EPS system . NO Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode, then wait for at least 6 seconds.

-5. Check for DTCs with the HDS.

DTC Description | DTC

U0420-68 EPS Control Unit Malfunction

Is DTC U0420-68 indicated?

YES

The failure is duplicated. Go to the indicated DTC's troubleshooting in the EPS system .

NO

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .
````

## Chunk 2330: DTC U0423-68, U1280-00, U1281-00, U128C-00 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U0423-68, U1280-00, U1281-00, U128C-00 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1153.html`
- Chunk ID: `chunk_208bc2ed506e`
- Images: none
- Duplicate sources: `pages\16502.html`

### Full Text

````text
# DTC U0423-68, U1280-00, U1281-00, U128C-00 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U0423-68 : Gauge Control Module Malfunction

DTC U1280-00 : Lost Communication With The B-CAN Systems

DTC U1281-00 : Lost Communication with The MICU

DTC U128C-00 : Lost Communication with The Wiper Control Unit

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- These DTCs are recorded when the millimeter wave radar receives failure information for relevant B-CAN systems or switches judged by the gauge control module.

- B-CAN system information used to control the integrated driver support system of this vehicle is obtained from the gauge control module via the F-CAN.

- If a DTC is recorded after it is cleared with the HDS, perform a self-diagnostic function for the gauge control module .

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U0423-68 Gauge Control Module Malfunction

U1280-00 Lost Communication With The B-CAN Systems

U1281-00 Lost Communication with The MICU

U128C-00 Lost Communication with The Wiper Control Unit

DTC (IDAS)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode, then wait for at least 6 seconds. -5. Check for DTCs with the HDS. DTC Description DTC U0423-68 Gauge Control Module Malfunction DTC Description DTC U1280-00 Lost Communication With The B-CAN Systems U1281-00 Lost Communication with The MICU U128C-00 Lost Communication with The Wiper Control Unit Is DTC U0423-68, U1280-00, U1281-00, or U128C-00 indicated? YES The failure is duplicated. Go to the indicated DTC's troubleshooting in the gauge control module . NO Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode, then wait for at least 6 seconds.

-5. Check for DTCs with the HDS.

DTC Description | DTC

U0423-68 Gauge Control Module Malfunction

DTC Description | DTC

U1280-00 Lost Communication With The B-CAN Systems

U1281-00 Lost Communication with The MICU

U128C-00 Lost Communication with The Wiper Control Unit

Is DTC U0423-68, U1280-00, U1281-00, or U128C-00 indicated?

YES

The failure is duplicated. Go to the indicated DTC's troubleshooting in the gauge control module .

NO

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .
````

## Chunk 2331: DTC U3000-51 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

- Title: DTC U3000-51 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)
- Source path: `pages\1154.html`
- Chunk ID: `chunk_d8387f2d37d4`
- Images: none
- Duplicate sources: `pages\16503.html`

### Full Text

````text
# DTC U3000-51 (Millimeter Wave Radar) (2017 2018 2019 2020 2021)

DTC U3000-51 : Millimeter Wave Radar Update Incomplete

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is indicated when a millimeter wave radar update is not completed properly.

- This DTC is not deleted until the millimeter wave radar is updated.

- After the update is successfully completed, these DTCs are automatically deleted without using the HDS.

- The functions of the integrated driver support system that will be temporarily canceled when this DTC is recorded can be confirmed with the DTC troubleshooting index .

DTC Description | DTC

U3000-51 Millimeter Wave Radar Update Incomplete

DTC (IDAS)

- Millimeter wave radar (update) -1. Update the millimeter wave radar . NOTE: When updating control units, use the most current version of the HDS software and interface device. Check any official service information website for more information about updating control units. -2. Check for DTCs with the HDS. DTC Description DTC U3000-51 Millimeter Wave Radar Update Incomplete Is DTC U3000-51 indicated? YES The failure is duplicated. Replace the millimeter wave radar . NO Update is complete.

-1. Update the millimeter wave radar .

NOTE: When updating control units, use the most current version of the HDS software and interface device. Check any official service information website for more information about updating control units.

-2. Check for DTCs with the HDS.

DTC Description | DTC

U3000-51 Millimeter Wave Radar Update Incomplete

Is DTC U3000-51 indicated?

YES

The failure is duplicated. Replace the millimeter wave radar .

NO

Update is complete.
````

## Chunk 2332: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1155.html`
- Chunk ID: `chunk_b16797534be0`
- Images: `images\GHH401839.jpeg`, `images\GHH401840.jpeg`
- Duplicate sources: `pages\1157.html`, `pages\1163.html`, `pages\13726.html`, `pages\13728.html`, `pages\13734.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations , and the precautions and procedures before doing repairs or service.

- Driver's Airbag - Remove

- Steering Wheel Trim - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the screws (A). 2. Disconnect connectors (B). 3. Remove the steering wheel trim (C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the screws (A). 2. Disconnect connectors (B). 3. Remove the steering wheel trim (C).

2. Disconnect connectors (B).

3. Remove the steering wheel trim (C).

- ACC Combination Switch - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 2333: ACC Combination Switch Removal, Installation, and Test: Test

- Title: ACC Combination Switch Removal, Installation, and Test: Test
- Source path: `pages\1156.html`
- Chunk ID: `chunk_0145d2a67045`
- Images: `images\GHH401841.jpeg`, `images\GHH401842.jpeg`
- Duplicate sources: `pages\13727.html`

### Full Text

````text
# ACC Combination Switch Removal, Installation, and Test: Test

- ACC Combination Switch - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch. Position Resistance OFF About 2.2 kΩ MAIN (PRESSED) About 60 Ω CANCEL (PRESSED) About 190 Ω SET- (PRESSED) About 450 Ω RES+ (PRESSED) About 900 Ω Courtesy of HONDA, U.S.A., INC. 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch.

- If there is no resistance in one or more positions, replace the ACC combination switch.

Position | Resistance

OFF | About 2.2 kΩ

MAIN (PRESSED) | About 60 Ω

CANCEL (PRESSED) | About 190 Ω

SET- (PRESSED) | About 450 Ω

RES+ (PRESSED) | About 900 Ω

Courtesy of HONDA, U.S.A., INC. | 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.
````

## Chunk 2334: Adaptive Cruise Control (ACC) Distance Switch Removal, Installation, and Test: Test

- Title: Adaptive Cruise Control (ACC) Distance Switch Removal, Installation, and Test: Test
- Source path: `pages\1158.html`
- Chunk ID: `chunk_e9cbbe79e5d4`
- Images: `images\GHH401845.jpeg`, `images\GHH401846.jpeg`
- Duplicate sources: `pages\13729.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Distance Switch Removal, Installation, and Test: Test

- Distance Switch - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch. Position Resistance OFF About 2.2 kΩ DISTANCE (PRESSED) About 450 Ω Courtesy of HONDA, U.S.A., INC. 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch.

- If there is no resistance in one or more positions, replace the ACC combination switch.

Position | Resistance

OFF | About 2.2 kΩ

DISTANCE (PRESSED) | About 450 Ω

Courtesy of HONDA, U.S.A., INC. | 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.
````

## Chunk 2335: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1159.html`
- Chunk ID: `chunk_fe4fc03dcb21`
- Images: `images\GHH401847.jpeg`
- Duplicate sources: `pages\13730.html`

### Full Text

````text
# Removal and Installation

- Driver's Dashboard Lower Cover - Remove

- CMBS OFF Switch - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Position of the switch is different depending on the model.

Courtesy of HONDA, U.S.A., INC.

NOTE: Position of the switch is different depending on the model.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 2336: CMBS OFF Switch Removal, Installation, and Test: Test

- Title: CMBS OFF Switch Removal, Installation, and Test: Test
- Source path: `pages\1160.html`
- Chunk ID: `chunk_3e728f7981ad`
- Images: `images\GHH401848.jpeg`, `images\GHH401849.jpeg`, `images\GHH401850.jpeg`
- Duplicate sources: `pages\13731.html`

### Full Text

````text
# CMBS OFF Switch Removal, Installation, and Test: Test

- CMBS OFF Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Check for continuity between CMBS OFF switch 10P connector terminals in each switch position according to the table. If the continuity is not as specified, replace the CMBS OFF switch. Courtesy of HONDA, U.S.A., INC. 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the CMBS OFF switch.

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Check for continuity between CMBS OFF switch 10P connector terminals in each switch position according to the table. If the continuity is not as specified, replace the CMBS OFF switch.

- If the continuity is not as specified, replace the CMBS OFF switch.

Courtesy of HONDA, U.S.A., INC. | 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the CMBS OFF switch.
````

## Chunk 2337: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1161.html`
- Chunk ID: `chunk_b74e9412bef8`
- Images: `images\GHH401851.jpeg`, `images\GHH401852.jpeg`, `images\GHH401853.jpeg`
- Duplicate sources: `pages\13732.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations , and the precautions and procedures before doing repairs or service.

- Driver's Airbag - Remove

- Steering Wheel Trim - Remove Screw fixed type Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Hook fixed type Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Remove the screws (A). 2. Disconnect the ground cable (B) with screw. 3. Disconnect connectors (C). 4. Remove the steering wheel trim (D).

Screw fixed type Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Hook fixed type Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Remove the screws (A). 2. Disconnect the ground cable (B) with screw. 3. Disconnect connectors (C). 4. Remove the steering wheel trim (D).

Hook fixed type

2. Disconnect the ground cable (B) with screw.

3. Disconnect connectors (C).

4. Remove the steering wheel trim (D).

- Cruise Control Combination Switch - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 2338: Cruise Control Combination Switch Removal, Installation, and Test: Test

- Title: Cruise Control Combination Switch Removal, Installation, and Test: Test
- Source path: `pages\1162.html`
- Chunk ID: `chunk_11ad2582ea8f`
- Images: `images\GHH401854.jpeg`, `images\GHH401855.jpeg`
- Duplicate sources: `pages\13733.html`

### Full Text

````text
# Cruise Control Combination Switch Removal, Installation, and Test: Test

- Cruise Control Combination Switch - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between the cruise control combination switch 12P connector (male terminals) terminals No. 5 and No. 6 according to the table. If there is no resistance in one or more positions, replace the cruise control combination switch. Position Resistance at normal ambient temperature OFF 2.0-2.4 kΩ CRUISE (Pressed and held) 54.3-66.3 Ω CANCEL (Pressed and held) 165.0-201.7 Ω SET- (Pressed and held) 401.7-491.0 Ω RES+ (Pressed and held) 802.7-981.1 Ω Courtesy of HONDA, U.S.A., INC. 2. Check the LED for illumination by applying power and ground to the terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the cruise control combination switch.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between the cruise control combination switch 12P connector (male terminals) terminals No. 5 and No. 6 according to the table. If there is no resistance in one or more positions, replace the cruise control combination switch.

If there is no resistance in one or more positions, replace the cruise control combination switch.

Position | Resistance at normal ambient temperature

OFF | 2.0-2.4 kΩ

CRUISE (Pressed and held) | 54.3-66.3 Ω

CANCEL (Pressed and held) | 165.0-201.7 Ω

SET- (Pressed and held) | 401.7-491.0 Ω

RES+ (Pressed and held) | 802.7-981.1 Ω

Courtesy of HONDA, U.S.A., INC. | 2. Check the LED for illumination by applying power and ground to the terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the cruise control combination switch.
````

## Chunk 2339: LKAS Switch Removal, Installation, and Test: Test

- Title: LKAS Switch Removal, Installation, and Test: Test
- Source path: `pages\1164.html`
- Chunk ID: `chunk_9066016539aa`
- Images: `images\GHH401858.jpeg`, `images\GHH401859.jpeg`
- Duplicate sources: `pages\13735.html`

### Full Text

````text
# LKAS Switch Removal, Installation, and Test: Test

- LKAS Switch - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch. Position Resistance OFF About 2.2 kΩ LKAS (PRESSED) About 60 Ω Courtesy of HONDA, U.S.A., INC. 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between ACC combination switch connector terminals No. 5 and No. 12 according to the table. If there is no resistance in one or more positions, replace the ACC combination switch.

- If there is no resistance in one or more positions, replace the ACC combination switch.

Position | Resistance

OFF | About 2.2 kΩ

LKAS (PRESSED) | About 60 Ω

Courtesy of HONDA, U.S.A., INC. | 2. Check the LED for illumination when connecting battery power and ground to the switch terminals according to the table. NOTE: Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). If the results are not as specified, replace the ACC combination switch.
````

## Chunk 2340: Adaptive Cruise Control (ACC) Symptom Troubleshooting Index (Adaptive Cruise Control (ACC))

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting Index (Adaptive Cruise Control (ACC))
- Source path: `pages\1165.html`
- Chunk ID: `chunk_f0753d54a956`
- Images: none
- Duplicate sources: `pages\12942.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting Index (Adaptive Cruise Control (ACC))

NOTE: The ACC system is cancelled when the VSA system is activated.

Symptom | Diagnostic procedure | Also check for

Vehicle speed can be set, but there is no ACC indication on the MID | Do the gauge control module self-diagnostic function procedure .

ACC OFF is displayed on the MID unexpectedly | Check the ACC system auto stop control history .

Vehicle speed cannot be set when the SET switch is pressed between the 25 mph (40 km/h) and 90 mph (145 km/h) | Test the ACC combination switch . Test the brake pedal position switch . | An open in the wire A short in the wire The system is in service mode

- Test the ACC combination switch .

- Test the brake pedal position switch .

- An open in the wire

- A short in the wire

- The system is in service mode

Vehicle does not decelerate or accelerate accordingly when the SET or RES switch is pressed | Test the ACC combination switch . | An open in the wire

Set speed does not cancel when the brake pedal is pressed | Test the brake pedal position switch . | An open in the wire

Set speed does not cancel when the MAIN switch is turned off | Test the ACC combination switch . | An open in the wire

Set distance cannot be adjusted with the distance switch | Test the distance switch .

Vehicle speed can be set, but vehicle decelerates | Check for DTCs in the PGM-FI system with the HDS . | Faulty ETCS

ACC activation indicator (on the MID) does not come on | Symptom troubleshooting .

ACC activation indicator (on the MID) does not go off | Symptom troubleshooting .

ACC indicator (on the MID) does not come on | Symptom troubleshooting .

ACC indicator (on the MID) does not go off | Symptom troubleshooting .

Senses a vehicle driving in another lane | Symptom troubleshooting . | Incorrect millimeter wave radar installation Wheel alignment

- Incorrect millimeter wave radar installation

- Wheel alignment

Does not sense the vehicle driving ahead | Symptom troubleshooting . | Out of the performance limits Wheel alignment Undetectable environment

- Out of the performance limits

- Wheel alignment

- Undetectable environment

Intermittently senses the vehicle driving ahead | Symptom troubleshooting . | Incorrect millimeter wave radar installation Wheel alignment Undetectable environment

- Incorrect millimeter wave radar installation

- Wheel alignment

- Undetectable environment
````

## Chunk 2341: Collision Mitigation Braking System (CMBS) Symptom Troubleshooting Index (Collision Mitigation Braking System (CMBS))

- Title: Collision Mitigation Braking System (CMBS) Symptom Troubleshooting Index (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1166.html`
- Chunk ID: `chunk_cbe5ac8986fc`
- Images: none
- Duplicate sources: `pages\12943.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Symptom Troubleshooting Index (Collision Mitigation Braking System (CMBS))

Symptom | Diagnostic procedure | Also check for

CMBS OFF switch does not turn On/turn Off (CMBS indicator does not change) | Do the gauge control module self-diagnostic function procedure . Test the CMBS OFF switch . | An open or increased resistance in the wire A short in the wire

- Do the gauge control module self-diagnostic function procedure .

- Test the CMBS OFF switch .

- An open or increased resistance in the wire

- A short in the wire

The MID does not indicate when the CMBS OFF switch is operated | Do the gauge control module self-diagnostic function procedure . Test the CMBS OFF switch . | An open or increased resistance in the wire A short in the wire

- Do the gauge control module self-diagnostic function procedure .

- Test the CMBS OFF switch .

- An open or increased resistance in the wire

- A short in the wire

The buzzer does not sound | Do the gauge control module self-diagnostic function procedure .

The buzzer does not sound when the CMBS OFF switch is operated | Do the gauge control module self-diagnostic function procedure .

Though CMBS operates, the information is not displayed on the MID | Do the gauge control module self-diagnostic function procedure .

The CMBS operates frequently | Check the millimeter wave radar installation . Check the wheel alignment . | Driving conditions, weather, environmental influence

- Check the millimeter wave radar installation .

- Check the wheel alignment .

The CMBS operated without danger of collision | Check the millimeter wave radar installation . Check the wheel alignment . | Driving conditions, weather, environmental influence

- Check the millimeter wave radar installation .

- Check the wheel alignment .

The CMBS did not operate | Check the millimeter wave radar installation . Check the wheel alignment . | Driving conditions, weather, environmental influences Undetectable environment

- Check the millimeter wave radar installation .

- Check the wheel alignment .

- Driving conditions, weather, environmental influences

- Undetectable environment

CMBS indicator does not come on | Do the gauge control module self-diagnostic function procedure .

CMBS indicator (on the MID) does not go off | Symptom troubleshooting .
````

## Chunk 2342: Cruise Control Symptom Troubleshooting Index (Cruise Control)

- Title: Cruise Control Symptom Troubleshooting Index (Cruise Control)
- Source path: `pages\1167.html`
- Chunk ID: `chunk_7b23a8e1f2d6`
- Images: none
- Duplicate sources: `pages\16570.html`

### Full Text

````text
# Cruise Control Symptom Troubleshooting Index (Cruise Control)

Symptom | Diagnostic procedure | Also check for

Cruise control cannot be set | Check the PGM-FI system . Check the No. B21 (10 A) fuse in the under-dash fuse/relay box. Do the cruise control combination switch test . Do the cruise control input test . | Open circuit, loose or disconnected terminals: GRN, TAN, GRY, or LT GRN wire between the cruise control combination switch and the gauge control module Faulty gauge control module Faulty cable reel

- Check the PGM-FI system .

- Check the No. B21 (10 A) fuse in the under-dash fuse/relay box.

- Do the cruise control combination switch test .

- Do the cruise control input test .

- Open circuit, loose or disconnected terminals: GRN, TAN, GRY, or LT GRN wire between the cruise control combination switch and the gauge control module

- Faulty gauge control module

- Faulty cable reel

Cruise control can be set, but the cruise main indicator does not come on | Do the gauge control module self-diagnostic function procedure . Do the cruise control input test . Test the cruise main indicator signal input. Check the PGM-FI system . | Faulty gauge control module

- Do the gauge control module self-diagnostic function procedure .

- Do the cruise control input test . Test the cruise main indicator signal input.

- Check the PGM-FI system .

Cruise control can be set, but the cruise control indicator does not come on | Do the gauge control module self-diagnostic function procedure . Do the cruise control input test . Test the cruise control indicator signal input. Check the PGM-FI system . | Faulty gauge control module

- Do the gauge control module self-diagnostic function procedure .

- Do the cruise control input test . Test the cruise control indicator signal input.

- Check the PGM-FI system .

Vehicle does not accelerate accordingly when the RES+ button is pressed | Do the cruise control combination switch test . Do the cruise control input test . Test the RES/+ switch signal input. Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the RES/+ switch signal input.

- Check the PGM-FI system .

Set speed does not cancel when the brake pedal is pressed | Do the brake pedal position switch test . Do the cruise control input test . Test the brake pedal position switch signal input. Check the PGM-FI system . | Faulty brake pedal position switch An open in the wire between the PCM and the brake pedal position switch A wire shorted to ground or power between the PCM and the brake pedal position switch

- Do the brake pedal position switch test .

- Do the cruise control input test . Test the brake pedal position switch signal input.

- Check the PGM-FI system .

- Faulty brake pedal position switch

- An open in the wire between the PCM and the brake pedal position switch

- A wire shorted to ground or power between the PCM and the brake pedal position switch

Symptom | Diagnostic procedure | Also check for

Set speed does not cancel (engine RPM stays high) when the clutch pedal is pressed for more than five seconds (M/T) | Do the cruise control input test . Test the CANCEL switch signal input. Test clutch pedal position switch A . Check for DTCs in the VSA system with the HDS . | Faulty clutch pedal position switch A An open in the wire between the PCM and clutch pedal position switch A A wire shorted to ground or power between the PCM and clutch pedal position switch A Faulty clutch pedal stroke sensor

- Do the cruise control input test . Test the CANCEL switch signal input.

- Test clutch pedal position switch A .

- Check for DTCs in the VSA system with the HDS .

- Faulty clutch pedal position switch A

- An open in the wire between the PCM and clutch pedal position switch A

- A wire shorted to ground or power between the PCM and clutch pedal position switch A

- Faulty clutch pedal stroke sensor

Set speed does not cancel when the CRUISE button is pressed | Do the cruise control combination switch test . Do the cruise control input test . Test the CRUISE switch signal input. Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the CRUISE switch signal input.

- Check the PGM-FI system .

Set speed does not cancel when the CANCEL button is pressed | Do the cruise control combination switch test . Do the cruise control input test . Test the CANCEL switch signal input.
````

## Chunk 2343: Cruise Control Symptom Troubleshooting Index (Cruise Control)

- Title: Cruise Control Symptom Troubleshooting Index (Cruise Control)
- Source path: `pages\1167.html`
- Chunk ID: `chunk_3ca4002e51ca`
- Images: none
- Duplicate sources: `pages\16570.html`

### Full Text

````text
ith the HDS .

- Faulty clutch pedal position switch A

- An open in the wire between the PCM and clutch pedal position switch A

- A wire shorted to ground or power between the PCM and clutch pedal position switch A

- Faulty clutch pedal stroke sensor

Set speed does not cancel when the CRUISE button is pressed | Do the cruise control combination switch test . Do the cruise control input test . Test the CRUISE switch signal input. Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the CRUISE switch signal input.

- Check the PGM-FI system .

Set speed does not cancel when the CANCEL button is pressed | Do the cruise control combination switch test . Do the cruise control input test . Test the CANCEL switch signal input. Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the CANCEL switch signal input.

- Check the PGM-FI system .

Set speed does not resume when the RES+ button is pressed (with the CRUISE button pressed on, and set speed temporarily canceled by pressing the brake pedal) | Check the PGM-FI system . Do the cruise control combination switch test . Do the cruise control input test . Test the RES+ switch signal input.

- Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the RES+ switch signal input.
````

## Chunk 2344: Lane Keeping Assist System (LKAS) Symptom Troubleshooting Index (Lane Keeping Assist System (LKAS))

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting Index (Lane Keeping Assist System (LKAS))
- Source path: `pages\1168.html`
- Chunk ID: `chunk_ace83f062386`
- Images: none
- Duplicate sources: `pages\12940.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting Index (Lane Keeping Assist System (LKAS))

Symptom | Diagnostic procedure | Also check for

LKAS indicator (on the MID) does not come on | Symptom troubleshooting .

LKAS indicator (on the MID) does not go off | Symptom troubleshooting .

LKAS activation indicator (on the MID) does not come on | Symptom troubleshooting .

LKAS activation indicator (on the MID) does not go off | Symptom troubleshooting .
````

## Chunk 2345: Adaptive Cruise Control (ACC) Component Location Index

- Title: Adaptive Cruise Control (ACC) Component Location Index
- Source path: `pages\1169.html`
- Chunk ID: `chunk_98ad54a06834`
- Images: `images\GHH401709.jpeg`, `images\GHH401710.jpeg`, `images\GHH401711.jpeg`
- Duplicate sources: `pages\15679.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Component Location Index

Courtesy of HONDA, U.S.A., INC.

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2346: Collision Mitigation Braking System (CMBS) Component Location Index

- Title: Collision Mitigation Braking System (CMBS) Component Location Index
- Source path: `pages\1170.html`
- Chunk ID: `chunk_240c05153ad3`
- Images: `images\GHH401712.jpeg`, `images\GHH401713.jpeg`, `images\GHH401714.jpeg`
- Duplicate sources: `pages\16571.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Component Location Index

Courtesy of HONDA, U.S.A., INC.

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2347: Cruise Control Component Location Index

- Title: Cruise Control Component Location Index
- Source path: `pages\1171.html`
- Chunk ID: `chunk_bfda094cbea8`
- Images: `images\GHH401715.jpeg`, `images\GHH401716.jpeg`, `images\GHH401717.jpeg`, `images\GHH401718.jpeg`
- Duplicate sources: `pages\16572.html`

### Full Text

````text
# Cruise Control Component Location Index

M/T

Courtesy of HONDA, U.S.A., INC.

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2348: Lane Keeping Assist System (LKAS) Component Location Index (2019 2020 2021)

- Title: Lane Keeping Assist System (LKAS) Component Location Index (2019 2020 2021)
- Source path: `pages\1172.html`
- Chunk ID: `chunk_ce927217a82d`
- Images: `images\GHH401719.jpeg`, `images\GHH401720.jpeg`, `images\GHH401721.jpeg`
- Duplicate sources: `pages\16573.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Component Location Index (2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2349: Lane Keeping Assist System (LKAS) Component Location Index (2/4-door) (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Component Location Index (2/4-door) (2016 2017 2018)
- Source path: `pages\1173.html`
- Chunk ID: `chunk_487f7d94379c`
- Images: `images\GHH401722.jpeg`, `images\GHH401723.jpeg`
- Duplicate sources: `pages\15735.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Component Location Index (2/4-door) (2016 2017 2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2350: Lane Keeping Assist System (LKAS) Component Location Index (5-door) (2017 2018)

- Title: Lane Keeping Assist System (LKAS) Component Location Index (5-door) (2017 2018)
- Source path: `pages\1174.html`
- Chunk ID: `chunk_b98f976998be`
- Images: `images\GHH401724.jpeg`, `images\GHH401725.jpeg`, `images\GHH401726.jpeg`
- Duplicate sources: `pages\15734.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Component Location Index (5-door) (2017 2018)

Courtesy of HONDA, U.S.A., INC.

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2351: Cruise Control (ECM/PCM) Input Test

- Title: Cruise Control (ECM/PCM) Input Test
- Source path: `pages\1175.html`
- Chunk ID: `chunk_efb68c5d9cc4`
- Images: none
- Duplicate sources: `pages\16574.html`

### Full Text

````text
# Cruise Control (ECM/PCM) Input Test

NOTE: Always make sure that you have the latest HDS software.

1. Turn the vehicle to the OFF (LOCK) mode.

2. Connect the HDS

3. Select PGM-FI system and check the diagnostic trouble code (DTC) in the DTC MENU on the screen and note it. Also check the freeze data and/or onboard snapshot data, and download any data found. Then refer to the indicated DTC's troubleshooting, and begin the appropriate troubleshooting procedure.

4. If no DTCs are found, do the following tests while monitoring parameters in the DATA LIST with the HDS.

5. If the input tests prove OK, replace the PCM .

NOTE: Intermittent failures are often caused by loose circuit connections. While monitoring cruise control inputs, flex the circuit wires, and note if any of the test results change.

Signal to be tested | Test condition | Parameter: Desired result | Possible cause if result is not obtained

Cruise control system switch status | Cruise control combination switch buttons are not pressed | CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list should indicate DEFAULT when the cruise control combination switch buttons are not pressed. | If the CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list indicates SIGNAL LOST, check as shown: Check for DTCs in the PGM-FI system and do the appropriate troubleshooting. Faulty gauge control module Faulty cruise control combination switch An open in the wire between the gauge control module and the cruise control combination switch A short to power in the wire between the gauge control module and the cruise control combination switch when the combination light switch is turned on If the CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list indicates SIGNAL SHORT, check as shown: Check for DTCs in the PGM-FI system and do the appropriate troubleshooting Faulty gauge control module Faulty cruise control combination switch A short to ground in the wire between the gauge control module and the cruise control combination switch If the CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list indicates a different status, check for a faulty cruise control combination switch.

- Check for DTCs in the PGM-FI system and do the appropriate troubleshooting.

- Faulty gauge control module

- Faulty cruise control combination switch

- An open in the wire between the gauge control module and the cruise control combination switch

- A short to power in the wire between the gauge control module and the cruise control combination switch when the combination light switch is turned on

If the CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list indicates SIGNAL SHORT, check as shown:

- Check for DTCs in the PGM-FI system and do the appropriate troubleshooting

- Faulty gauge control module

- Faulty cruise control combination switch

- A short to ground in the wire between the gauge control module and the cruise control combination switch

If the CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list indicates a different status, check for a faulty cruise control combination switch.

CRUISE button is pressed | CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list should indicate MAIN switch when the CRUISE button is pressed.

CANCEL button is pressed | CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list should indicate CANCEL switch when the CANCEL button is pressed.

SET- button is pressed | CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list should indicate SET switch when the SET- button is pressed.

RES+ button is pressed | CRUISE CONTROL SYSTEM SWITCH STATUS in the HDS data list should indicate RES switch when the RES+ button is pressed.

Signal to be tested | Test condition | Parameter: Desired result | Possible cause if result is not obtained

Cruise control indicator signal | Start the engine, press the cruise control main button on and drive the vehicle above 25 mph (40 km/h) with the cruise control set and cancel the cruise control | CRUISE INDICATOR should indicate ON when the cruise control is set and OFF when the cruise control is canceled. | Faulty gauge control module Faulty cruise control combination switch An open in the wire between the gauge control module and the cruise control combination switch A wire shorted to ground between the gauge control module and the cruise control combination switch

- Faulty gauge control module

- Faulty cruise control combination switch
````

## Chunk 2352: Cruise Control (ECM/PCM) Input Test

- Title: Cruise Control (ECM/PCM) Input Test
- Source path: `pages\1175.html`
- Chunk ID: `chunk_2587d0a9de2e`
- Images: none
- Duplicate sources: `pages\16574.html`

### Full Text

````text
switch when the RES+ button is pressed.

Signal to be tested | Test condition | Parameter: Desired result | Possible cause if result is not obtained

Cruise control indicator signal | Start the engine, press the cruise control main button on and drive the vehicle above 25 mph (40 km/h) with the cruise control set and cancel the cruise control | CRUISE INDICATOR should indicate ON when the cruise control is set and OFF when the cruise control is canceled. | Faulty gauge control module Faulty cruise control combination switch An open in the wire between the gauge control module and the cruise control combination switch A wire shorted to ground between the gauge control module and the cruise control combination switch

- Faulty gauge control module

- Faulty cruise control combination switch

- An open in the wire between the gauge control module and the cruise control combination switch

- A wire shorted to ground between the gauge control module and the cruise control combination switch

Brake pedal position switch signal | Brake pedal is pressed, then released | CRUISE BRAKE SW should indicate OPEN when the brake pedal is pressed and CLOSE when the brake pedal is released. | Faulty brake pedal position switch Blown No. B21 (10 A) fuse in the under-dash fuse/relay box An open in the wire between the PCM and the brake pedal position switch A wire shorted to ground or power between the PCM and the brake pedal position switch

- Faulty brake pedal position switch

- Blown No. B21 (10 A) fuse in the under-dash fuse/relay box

- An open in the wire between the PCM and the brake pedal position switch

- A wire shorted to ground or power between the PCM and the brake pedal position switch

Clutch pedal position switch A signal (M/T) | Clutch pedal is pressed, then released | CLUTCH PEDAL POSITION SWITCH should indicate OPEN when the clutch pedal is pressed and CLOSE when the clutch pedal is released. | Faulty clutch pedal position switch A An open in the wire between the PCM and clutch pedal position switch A A wire shorted to ground between the PCM and clutch pedal position switch A

- Faulty clutch pedal position switch A

- An open in the wire between the PCM and clutch pedal position switch A

- A wire shorted to ground between the PCM and clutch pedal position switch A
````

## Chunk 2353: ACC System Auto Stop Control History: Notes

- Title: ACC System Auto Stop Control History: Notes
- Source path: `pages\1176.html`
- Chunk ID: `chunk_c3e7b0173e8b`
- Images: `images\GHH401727.jpeg`, `images\GHH401728.jpeg`, `images\GHH401729.jpeg`
- Duplicate sources: `pages\16575.html`

### Full Text

````text
# ACC System Auto Stop Control History: Notes

When the ACC is activated, if the multipurpose camera unit determines that the ACC is unable to operate normally due to an environmental factors (such as weather or road surface condition and driving or vehicle condition) or other reasons even when the ACC system itself is normal, the multipurpose camera unit automatically cancels the activation of the ACC and records the ACC system auto stop control code in it.

When the ACC is automatically cancelled, "ACC OFF" is displayed on the multi-information display (MID) to notify the driver of the cancellation. At this time, the ACC indicator (amber) does not come on.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2354: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_99199929a969`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
# Checking for ACC System Auto Stop Control Codes

The ACC system auto stop control codes recorded in the multipurpose camera unit can be read out by the procedure below.

NOTE: Make sure the 12 volt battery is fully charged before you begin.

1. Connect the HDS .

2. In the DRIVING SUPPORT MENU of the HDS, select Integrated Driver Support System, then select Data List on the HDS.

3. Checking for ACC system auto stop control codes recorded in the Data List.

NOTE:

- ACC system auto stop control history is recorded from 1. When automatic cancellation takes place 11 times or more, the past 10 records are held. In this case, history 10 is the latest record and the 10 latest records are held. When 0, no record is held.

- When DTCs are cleared with the HDS, ACC system auto stop control history is cleared as well.

- Some of the following ACC system auto stop control codes may not be used for specific model specifications.

ACC System Auto Stop Control Codes

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

80 | Engine Speed too high or too low | The vehicle decelerated because the leading vehicle decelerated, and the engine speed dropped below the mid-speed ranges. | The driver did not operate the clutch pedal within 10 seconds after the shift-down request was displayed. | The engine speed returned to the specified speed or higher. | Prevention of engine stall while the vehicle is decelerating because the leading vehicle is decelerating.

82 | Adaptive cruise control (ACC) brake control temporarily prohibited by Electric Parking Brake | 12 Volt battery deterioration 24 Volt battery installation | The multipurpose camera unit received ACC brake temporary prohibition information from the EPB. NOTE: When the EPB power supply voltage is outside the operating range, the EPB sends ACC brake temporary prohibition information to the multipurpose camera unit. | The EPB power supply voltage returns to normal and the ACC brake temporary prohibition information is cleared. | The EPB cannot maintain the vehicle stopping state.

- 12 Volt battery deterioration

- 24 Volt battery installation

NOTE: When the EPB power supply voltage is outside the operating range, the EPB sends ACC brake temporary prohibition information to the multipurpose camera unit.

83 | Radar detection unstable | The vehicle followed a narrow vehicle, such as a motorcycle, or a specialized vehicle. The reception level of the millimeter wave radar decreased due to rain or snow. | The reception of the millimeter wave radar (average) is outside the range where ACC control is available. | The reception level of the millimeter wave radar (average) returned to within the range where ACC control is available and the leading vehicle was detected. | For preventing the vehicle from accelerating after the leading vehicle is lost because the detection state of the leading vehicle becomes unstable while the vehicle is following the leading vehicle.

- The vehicle followed a narrow vehicle, such as a motorcycle, or a specialized vehicle.

- The reception level of the millimeter wave radar decreased due to rain or snow.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

84 | Target vehicle comes closer than the radar detecting limits | The leading vehicle slowed down rapidly. Another vehicle suddenly cuts in front of your vehicle. | The distance between the leading vehicle and your vehicle is less than the minimum allowable vehicle-to-vehicle distance. Models with the low speed follow (LSF) feature: 1.5 m (4.9 ft) Models without the low speed follow (LSF) feature: 5 m (16 ft) | The system returns to normal when the distance between the leading vehicle and your vehicle reaches or exceeds the minimum allowable vehicle-to-vehicle distance + 0.5 m (1.6 ft).
````

## Chunk 2355: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_c3ab900fd6df`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
ly the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

84 | Target vehicle comes closer than the radar detecting limits | The leading vehicle slowed down rapidly. Another vehicle suddenly cuts in front of your vehicle. | The distance between the leading vehicle and your vehicle is less than the minimum allowable vehicle-to-vehicle distance. Models with the low speed follow (LSF) feature: 1.5 m (4.9 ft) Models without the low speed follow (LSF) feature: 5 m (16 ft) | The system returns to normal when the distance between the leading vehicle and your vehicle reaches or exceeds the minimum allowable vehicle-to-vehicle distance + 0.5 m (1.6 ft). | The control is prohibited at a close distance to the leading vehicle where the ACC system is unavailable. If the leading vehicle is too close to your vehicle, the millimeter wave radar may fail to detect the leading vehicle.

- The leading vehicle slowed down rapidly.

- Another vehicle suddenly cuts in front of your vehicle.

- Models with the low speed follow (LSF) feature: 1.5 m (4.9 ft)

- Models without the low speed follow (LSF) feature: 5 m (16 ft)

85 | Extensive driving on a rough or winding road | The vehicle continued to run in an unstable state without stopping: Driving on a road with many curves or a rough road Repeated acceleration and deceleration Rapid acceleration/deceleration Continuous, unstable, or rapid steering wheel operation | The yaw rate-acceleration neutral position was not corrected when the yaw rate sensor temperature changed by 50°F (10°C). | Stop the vehicle or drive the vehicle in a stable state at 3 mph (5 km/h) or more. NOTE: While the vehicle is running, the correction is made based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 85 is stored. | Because the accuracy of the yaw rate sensor cannot be maintained, possibly resulting in an incorrect estimated vehicle trajectory or incorrect leading vehicle selection.

- Driving on a road with many curves or a rough road

- Repeated acceleration and deceleration

- Rapid acceleration/deceleration

- Continuous, unstable, or rapid steering wheel operation

NOTE: While the vehicle is running, the correction is made based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 85 is stored.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

86 | Abnormal tire pressure | Low tire pressure (including a flat tire) Driving on a split road (the right and left wheels run on different types of road surfaces) | The estimated yaw rate calculated based on the difference between the right and left wheel speeds differs between the front and rear wheels (estimated yaw rate difference: 2 deg/s or more). | Estimated yaw rate difference: 0.25 deg/s or less | Because the estimated running trajectory of the vehicle is incorrect, so the leading vehicle cannot be selected correctly. NOTE: If the tire pressure is abnormal, the yaw rate-acceleration neutral position is not corrected normally.

- Low tire pressure (including a flat tire)

- Driving on a split road (the right and left wheels run on different types of road surfaces)

NOTE: If the tire pressure is abnormal, the yaw rate-acceleration neutral position is not corrected normally.

87 | Adaptive cruise control (ACC) brake control temporality prohibited by VSA | 12 Volt battery deterioration 24 Volt battery installation | The multipurpose camera unit received ACC brake temporary prohibition information from the VSA modulator-control unit.
````

## Chunk 2356: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_8ca1f828e3b0`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
| Estimated yaw rate difference: 0.25 deg/s or less | Because the estimated running trajectory of the vehicle is incorrect, so the leading vehicle cannot be selected correctly. NOTE: If the tire pressure is abnormal, the yaw rate-acceleration neutral position is not corrected normally.

- Low tire pressure (including a flat tire)

- Driving on a split road (the right and left wheels run on different types of road surfaces)

NOTE: If the tire pressure is abnormal, the yaw rate-acceleration neutral position is not corrected normally.

87 | Adaptive cruise control (ACC) brake control temporality prohibited by VSA | 12 Volt battery deterioration 24 Volt battery installation | The multipurpose camera unit received ACC brake temporary prohibition information from the VSA modulator-control unit. NOTE: When the VSA modulator-control unit power supply voltage or the brake light relay actuation circuit voltage is outside the operating range, the VSA modulator-control unit sends ACC brake temporary prohibition information to the multipurpose camera unit. | The VSA modulator-control unit power supply voltage returns to normal and the ACC brake temporary prohibition information is cleared. | Because the ACC brake may not be activated or the brake light may not come on even when the ACC brake is activated.

- 12 Volt battery deterioration

- 24 Volt battery installation

NOTE: When the VSA modulator-control unit power supply voltage or the brake light relay actuation circuit voltage is outside the operating range, the VSA modulator-control unit sends ACC brake temporary prohibition information to the multipurpose camera unit.

88 *1 | Radar temporary problem (temperature, voltage, etc.) | Traffic congestion at a high temperature Continuous hill climbing 12 Volt battery deterioration | The multipurpose camera unit received the following error information from the millimeter wave radar. Temperature in the millimeter wave radar: 203°F (95°C) or more Millimeter wave radar power supply voltage: 9 V or less The millimeter wave radar cannot temporarily receive signals from the multipurpose camera unit. | The millimeter wave radar sends restoration information, which is received and cleared by the multipurpose camera unit. | The millimeter wave radar cannot normally detect the leading vehicle and measure the vehicle-to-vehicle distance. Prevention of incorrect detection of the leading vehicle or incorrect ACC control.

- Traffic congestion at a high temperature

- Continuous hill climbing

- 12 Volt battery deterioration

- Temperature in the millimeter wave radar: 203°F (95°C) or more

- Millimeter wave radar power supply voltage: 9 V or less

- The millimeter wave radar cannot temporarily receive signals from the multipurpose camera unit.

- The millimeter wave radar cannot normally detect the leading vehicle and measure the vehicle-to-vehicle distance.

- Prevention of incorrect detection of the leading vehicle or incorrect ACC control.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

89 | Front wheel spin | Driving on a low μ road TCS control is executed. | A change in the wheel speed equivalent to 0.75 G occurs. | Other than those listed to the left | Prevention of use of ACC on a road where vehicle behavior is unstable

- Driving on a low μ road

- TCS control is executed.

91 | Vehicle skidded, spun out, or abrupt steering wheel movements | Spin on a low μ road due to improper steering wheel operation Rapid steering wheel operation VSA control was executed. | Lateral acceleration of 0.60 G or more occurred within 1 second after the yaw rate changed by 2 deg/s or more in 0.1 second. | Other than those listed to the left | Prevention of use of ACC on a road where vehicle behavior is unstable

- Spin on a low μ road due to improper steering wheel operation

- Rapid steering wheel operation

- VSA control was executed.
````

## Chunk 2357: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_e9d7eccd81ac`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
control is executed. | A change in the wheel speed equivalent to 0.75 G occurs. | Other than those listed to the left | Prevention of use of ACC on a road where vehicle behavior is unstable

- Driving on a low μ road

- TCS control is executed.

91 | Vehicle skidded, spun out, or abrupt steering wheel movements | Spin on a low μ road due to improper steering wheel operation Rapid steering wheel operation VSA control was executed. | Lateral acceleration of 0.60 G or more occurred within 1 second after the yaw rate changed by 2 deg/s or more in 0.1 second. | Other than those listed to the left | Prevention of use of ACC on a road where vehicle behavior is unstable

- Spin on a low μ road due to improper steering wheel operation

- Rapid steering wheel operation

- VSA control was executed.

93 | Front tire problem | Flat tire Large air pressure difference One wheel slips | The estimated yaw rate calculated based on the wheel speed difference between the right and left wheels is 60 deg/s or more. | Stop the vehicle. | Because the estimated running trajectory of the own vehicle is incorrect, and the leading vehicle cannot be selected correctly. NOTE: When there is a problem with a tire, the yaw rate-acceleration neutral position is not corrected normally.

- Flat tire

- Large air pressure difference

- One wheel slips

NOTE: When there is a problem with a tire, the yaw rate-acceleration neutral position is not corrected normally.

94 | Rear tire problem | Flat tire Large air pressure difference One wheel slips | The estimated yaw rate calculated based on the wheel speed difference between the right and left wheels is 60 deg/s or more. | Stop the vehicle. | Because the estimated running trajectory of the own vehicle is incorrect, and the leading vehicle cannot be selected correctly. NOTE: When there is a problem with a tire, the yaw rate-acceleration neutral position is not corrected normally.

- Flat tire

- Large air pressure difference

- One wheel slips

NOTE: When there is a problem with a tire, the yaw rate-acceleration neutral position is not corrected normally.

95 *1 | Power supply voltage too high | 24 Volt battery installation | Power supply voltage: 16.8 V or more | Power supply voltage: 16.5 V or less | The multipurpose camera unit may not operate properly.

96 *1 | Power supply voltage too low | 12 Volt battery deterioration | Power supply voltage: 9.5 V or less | Power supply voltage: 9.8 V or more | The multipurpose camera unit may not operate properly.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

97 *1 | Extensive driving on a rough or winding road. (CMBS/FCW) | The vehicle continued to run in an unstable state without stopping: Driving on a road with many curves or a rough road Repeated acceleration and deceleration Rapid acceleration/deceleration Continuous, unstable, or rapid steering wheel operation | When the yaw rate sensor temperature changed by 86°F (30°C) or more and the correction logic is not executed for approximately 8 seconds or more | Stop the vehicle. NOTE: While the vehicle is running, the correction is made based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 97 is stored. Yaw rate-acceleration neutral position memorization execution conditions: Stop the vehicle or drive the vehicle stably at a 6 mph (10 km/h) or more. | Because the system may be activated for an obstacle against which the vehicle is unlikely to collide.

- Driving on a road with many curves or a rough road

- Repeated acceleration and deceleration

- Rapid acceleration/deceleration

- Continuous, unstable, or rapid steering wheel operation

NOTE: While the vehicle is running, the correction is made based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 97 is stored.
````

## Chunk 2358: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_b7e911198439`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 97 is stored. Yaw rate-acceleration neutral position memorization execution conditions: Stop the vehicle or drive the vehicle stably at a 6 mph (10 km/h) or more. | Because the system may be activated for an obstacle against which the vehicle is unlikely to collide.

- Driving on a road with many curves or a rough road

- Repeated acceleration and deceleration

- Rapid acceleration/deceleration

- Continuous, unstable, or rapid steering wheel operation

NOTE: While the vehicle is running, the correction is made based on the correction value when the vehicle is stopped, so the correct will not be made once the ACC system auto stop control code 97 is stored.

Yaw rate-acceleration neutral position memorization execution conditions:

- Stop the vehicle or drive the vehicle stably at a 6 mph (10 km/h) or more.

98 | Multipurpose camera unit temperature too high | Parked under the blazing sun for a certain time. | Multipurpose camera unit temperature: Approx 185°F (85°C) or more. | Multipurpose camera unit temperature: Approx 180°F (82°C) or less. | The ECU may not operate properly. Protection for the internal circuit.

- The ECU may not operate properly.

- Protection for the internal circuit.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

99 | Acceleration/deceleration abnormality | The inclination of the road changed significantly while the vehicle accelerates/decelerates at around the maximum acceleration/deceleration speed of the ACC system. The powertrain or brake system is abnormal. | While the ACC was operating, an acceleration of 0.4 G or more* 2 continued for 1.0 second or more. While the ACC was operating, a deceleration of -0.5 G or less* 2 continued for 1.5 seconds or more. | Other than those listed to the left | Because the maximum acceleration/deceleration speed for the ACC system is exceeded.

- The inclination of the road changed significantly while the vehicle accelerates/decelerates at around the maximum acceleration/deceleration speed of the ACC system.

- The powertrain or brake system is abnormal.

- While the ACC was operating, an acceleration of 0.4 G or more* 2 continued for 1.0 second or more.

- While the ACC was operating, a deceleration of -0.5 G or less* 2 continued for 1.5 seconds or more.

101 | Rear wheel locked | The parking brake is not released or the vehicle is driven on a frozen road surface. | A signal of 5 mph (8 km/h) or more is inputted to the front wheel sensor and a signal of 0 mph (0 km/h) is inputted to the rear wheel sensor. | The front and rear wheel sensors detect a wheel speed. | Prevention of unstable vehicle behavior

108 | Adaptive cruise control (ACC) brake control temporarily prohibited by ESB | 12 Volt battery deterioration 24 Volt battery installation | The multipurpose camera unit received ACC brake temporary prohibition information from the ESB. NOTE: When the ESB power supply voltage is outside the operating range, the ESB sends ACC brake temporary prohibition information to the multipurpose camera unit. CAN communication fail is being detected between the ESB control unit and multipurpose camera unit. | The ESB power supply voltage returns to normal and the ACC brake temporary prohibition information is cleared. | Because ACC brake cannot be activated.

- 12 Volt battery deterioration

- 24 Volt battery installation

NOTE:

- When the ESB power supply voltage is outside the operating range, the ESB sends ACC brake temporary prohibition information to the multipurpose camera unit.

- CAN communication fail is being detected between the ESB control unit and multipurpose camera unit.
````

## Chunk 2359: Checking for ACC System Auto Stop Control Codes

- Title: Checking for ACC System Auto Stop Control Codes
- Source path: `pages\1177.html`
- Chunk ID: `chunk_f9572d2a960e`
- Images: none
- Duplicate sources: `pages\16576.html`

### Full Text

````text
temporary prohibition information from the ESB. NOTE: When the ESB power supply voltage is outside the operating range, the ESB sends ACC brake temporary prohibition information to the multipurpose camera unit. CAN communication fail is being detected between the ESB control unit and multipurpose camera unit. | The ESB power supply voltage returns to normal and the ACC brake temporary prohibition information is cleared. | Because ACC brake cannot be activated.

- 12 Volt battery deterioration

- 24 Volt battery installation

NOTE:

- When the ESB power supply voltage is outside the operating range, the ESB sends ACC brake temporary prohibition information to the multipurpose camera unit.

- CAN communication fail is being detected between the ESB control unit and multipurpose camera unit.

109 | Movement distance too short after initiation | When the millimeter wave radar detects an object that turns on low speed follow (LSF) control immediately after vehicle ON mode. | When the distance the vehicle travels after vehicle ON mode, which is calculated based on the vehicle speed, is less than 8 m (26 ft). | When the distance the vehicle travels is 8 m (26 ft) or more. | This is because an object other than a vehicle may be recognized as the leading vehicle after vehicle ON mode in a parking lot etc.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.

Code | ACC System Auto Stops Operating | Concrete Examples | Detection Conditions | Restoration Conditions (Conditions under which ACC SET is possible) | Reasons for Control OFF

110 | Shift position 1st | While driving in 1st gear. Vehicle is driven at an extremely low speed. | 1st gear shift position is detected. | Vehicle is driven in 2nd or higher gear (forward gear). | Inappropriate gear is selected for ACC system.

- While driving in 1st gear.

- Vehicle is driven at an extremely low speed.

127 | i-DCD cannot receive traction request | After the DCT (the built-in motor type) shifted during the acceleration. (especially low speed). | The multipurpose camera unit received DCT (the built-in motor type) traction request rejection information from the engine ECU *3. | The engine ECU *3 to normal and the DCT (the built-in motor type) traction request rejection information is cleared. | Because the driving force required by the ACC cannot be generated in a state in which the gears of the transmission are not engaged properly.

140 *4 | Yaw rate sensor temporarily error (low voltage, etc.) | 12 Volt battery deterioration. | The multipurpose camera unit received yaw rate sensor temporarily error information from the SRS unit. | The SRS unit to normal and the yaw rate sensor temporary prohibition information is cleared. | Prevention of incorrect detection of the leading vehicle due to deviation of own vehicle locus estimation.

*1: While the code is detected, the CMBS operation stops temporarily and the CMBS indicator (amber) comes on.

*2: This value differs depending on whether or not the vehicle is equipped with Low Speed Follow (LSF) feature.

*3:

- When the PGM-FI ECU and TCM are integrated, the engine ECU represents the PGM-FI ECU.

- When the PGM-FI ECU and TCM are separate, the engine ECU represents the TCM.

*4: The yaw rate sensor records only the built-in SRS unit.
````

## Chunk 2360: ACC Indicator (Amber)

- Title: ACC Indicator (Amber)
- Source path: `pages\1178.html`
- Chunk ID: `chunk_3dbbe3686a1b`
- Images: `images\GHH401730.jpeg`
- Duplicate sources: `pages\16577.html`

### Full Text

````text
# ACC Indicator (Amber)

When the ACC system detects a problem while operating, the ACC system stops working, then the ACC indicator and the brake system indicator (amber) stay on.

NOTE:

- For ACC function, review the Adaptive Cruise Control (ACC) Description .

- The ACC system communication with other control units via the F-CAN. For ACC system diagram, review the ACC System Diagram . If a connected unit malfunctions, the ACC system will not operate. In this case, both ACC indicator and connected unit indicator come on and stay on (except for the gauge control module).

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2361: Multi-Information Display (MID) Indication

- Title: Multi-Information Display (MID) Indication
- Source path: `pages\1179.html`
- Chunk ID: `chunk_694e5847f083`
- Images: `images\GHH401731.jpeg`
- Duplicate sources: `pages\16578.html`

### Full Text

````text
# Multi-Information Display (MID) Indication

When the ACC system OK, the ACC indicates its status on the multi-information display (MID) when the MAIN switch is ON.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2362: Self-Diagnostic Function

- Title: Self-Diagnostic Function
- Source path: `pages\1180.html`
- Chunk ID: `chunk_4bd62b60307a`
- Images: `images\GHH401732.jpeg`
- Duplicate sources: `pages\16579.html`

### Full Text

````text
# Self-Diagnostic Function

The ACC system has a self-diagnostic function. If the self-diagnostic function detects a malfunction, the ACC system stops operating. The ACC indicator comes on, and the ACC system indicates "Adaptive Cruise Control Problem" on the MID.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2363: Millimeter Wave Radar

- Title: Millimeter Wave Radar
- Source path: `pages\1181.html`
- Chunk ID: `chunk_eddde00c2f7c`
- Images: none
- Duplicate sources: `pages\16580.html`

### Full Text

````text
# Millimeter Wave Radar

The millimeter wave radar measures the distance between your vehicle and the vehicle directly ahead to calculate the difference in speed between the vehicles.

2/4-door: The millimeter wave radar also has an error detection function which sends a signal to the multipurpose camera unit if an error is detected.

5-door: The millimeter wave radar has a self-diagnostic function. If the system detects a problem, it disables the ACC, and turns on the ACC indicator.
````

## Chunk 2364: Dirt or dust detective function (Clean Millimeter Wave Radar Indication)

- Title: Dirt or dust detective function (Clean Millimeter Wave Radar Indication)
- Source path: `pages\1182.html`
- Chunk ID: `chunk_6d8a3ad03914`
- Images: `images\GHH401733.jpeg`
- Duplicate sources: `pages\16581.html`

### Full Text

````text
# Dirt or dust detective function (Clean Millimeter Wave Radar Indication)

If the millimeter wave radar or radar cover gets dirty, the ACC system stops operating and the following message will appear: Some Driver Assist Systems Cannot Operate: Radar Obstructed appears on the MID. Clean the millimeter wave radar and the radar cover surface. Once the millimeter wave radar and radar cover surface are clean, the message on the MID disappears and the ACC system automatically turns on.

NOTE:

- Under the above conditions DTC P2583-97 is stored.

- When it is snowing, the radio waves transmitted and received by the millimeter wave radar may be refracted by the snow or ice attached around the millimeter wave radar such as the front grille. At this time, DTC P2583-76 is stored depending on the situation.

- After DTC P2583-76 is stored, the message (Radar Obstructed) is displayed on the MID at the initial stage in some models, and then the indicators come on.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2365: Millimeter Wave Radar Aiming

- Title: Millimeter Wave Radar Aiming
- Source path: `pages\1183.html`
- Chunk ID: `chunk_7aba444ee54a`
- Images: none
- Duplicate sources: `pages\16582.html`

### Full Text

````text
# Millimeter Wave Radar Aiming

If the millimeter wave radar is removed or replaced, you must do the millimeter wave radar aiming procedure, otherwise the ACC indicator blinks.
````

## Chunk 2366: Multipurpose Camera Unit

- Title: Multipurpose Camera Unit
- Source path: `pages\1184.html`
- Chunk ID: `chunk_9f14894d4e9a`
- Images: none
- Duplicate sources: `pages\16583.html`

### Full Text

````text
# Multipurpose Camera Unit

The multipurpose camera unit uses inputs from the millimeter wave radar to maintain a constant distance between your vehicle and the vehicle directly ahead by accelerating and braking as needed.

The multipurpose camera unit also has an error detection function which sends a signal to the millimeter wave radar if an error is detected.
````

## Chunk 2367: Multipurpose Camera Aiming Function

- Title: Multipurpose Camera Aiming Function
- Source path: `pages\1185.html`
- Chunk ID: `chunk_056993744ea2`
- Images: none
- Duplicate sources: `pages\16584.html`

### Full Text

````text
# Multipurpose Camera Aiming Function

If the multipurpose camera unit is removed or replaced, you must do the multipurpose camera aiming procedure. If the aiming is incomplete, the ACC indicator blinks.
````

## Chunk 2368: CAN Communication

- Title: CAN Communication
- Source path: `pages\1186.html`
- Chunk ID: `chunk_2d8f612167e3`
- Images: none
- Duplicate sources: `pages\16585.html`

### Full Text

````text
# CAN Communication

The ACC system communicates with other control units via the F-CAN. For ACC system diagram, review the ACC System Diagram .

If the multipurpose camera unit detects a communication error or a malfunction in another connected unit, the ACC system will not operate even though it is OK. In this case, both the ACC indicator and the related unit indicator will come on and stay on.
````

## Chunk 2369: How to Troubleshoot DTCs

- Title: How to Troubleshoot DTCs
- Source path: `pages\1188.html`
- Chunk ID: `chunk_610989664687`
- Images: none
- Duplicate sources: `pages\16587.html`

### Full Text

````text
# How to Troubleshoot DTCs

Check the DTCs with the HDS.

NOTE: For ACC system DTCs, refer to the DTC troubleshooting index .

Before troubleshooting, check and note these items:

- Ask the customer about the conditions when the problem occurred, and try to reproduce the same conditions for troubleshooting.

- If the symptom does not appear and the ACC indicator does not come on while test-driving, but if your troubleshooting was based on a DTC, check for poor connections or loose terminals at all connectors related to the circuit that you are troubleshooting.

- After the troubleshooting or repairs are done, clear the DTCs, and test-drive the vehicle under the same conditions as when the DTC was originally set. Make sure the ACC indicator does not come on.

- The ACC system sometimes stops operating because of certain environmental conditions (weather, road conditions, driving conditions, etc.). A intermittent failure DTCs or ACC System Auto Stop Control Codes may be stored in these cases.

DTC may be stored even when the system is OK:

NOTE: The ACC indicator does not come on when DTC B2A00-F8 : ACC Brake Control Temporarily Prohibited is stored.
````

## Chunk 2370: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not come on

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not come on
- Source path: `pages\1191.html`
- Chunk ID: `chunk_b1a498140a3e`
- Images: `images\GHH401734.jpeg`
- Duplicate sources: `pages\16564.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not come on

- Gauge control module operation check -1. Do the gauge control module self-diagnostic function . Is the gauge control module OK? YES Go to step 2. NO Replace the gauge control module .

-1. Do the gauge control module self-diagnostic function .

Is the gauge control module OK?

YES

Go to step 2.

NO

Replace the gauge control module .

- ACC combination switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the ACC combination switch . Is the switch OK? YES Go to step 3. NO Replace the ACC combination switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the ACC combination switch .

Is the switch OK?

YES

Go to step 3.

NO

Replace the ACC combination switch .

- Open wire check (CRUISE SW line) -1. Disconnect the following connector. ACC combination switch 12P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ACC combination switch 12P connector: disconnected Test point 1 ACC combination switch 12P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Repair an open in the CRUISE GND wire between the ACC combination switch and the gauge control module. NO Repair an open in the CRUISE SW wire between the ACC combination switch and the gauge control module.

-1. Disconnect the following connector.

ACC combination switch 12P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ACC combination switch 12P connector: disconnected

Test point 1 | ACC combination switch 12P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Repair an open in the CRUISE GND wire between the ACC combination switch and the gauge control module.

NO

Repair an open in the CRUISE SW wire between the ACC combination switch and the gauge control module.
````

## Chunk 2371: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not go off

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not go off
- Source path: `pages\1192.html`
- Chunk ID: `chunk_b8eb84192e7e`
- Images: none
- Duplicate sources: `pages\16565.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC activation indicator (on the MID) does not go off

- Gauge control module operation check -1. Do the gauge control module self-diagnostic function . Is the gauge control module OK? YES Go to step 2. NO Replace the gauge control module .

-1. Do the gauge control module self-diagnostic function .

Is the gauge control module OK?

YES

Go to step 2.

NO

Replace the gauge control module .

- ACC combination switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the ACC combination switch . Is the switch OK? YES Repair a short to ground in the CRUISE GND wire between the ACC combination switch and the gauge control module. NO Replace the ACC combination switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the ACC combination switch .

Is the switch OK?

YES

Repair a short to ground in the CRUISE GND wire between the ACC combination switch and the gauge control module.

NO

Replace the ACC combination switch .
````

## Chunk 2372: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not come on

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not come on
- Source path: `pages\1193.html`
- Chunk ID: `chunk_0a1a4aa86b89`
- Images: none
- Duplicate sources: `pages\16566.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not come on

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check the following indicators in the gauge control module: Malfunction indicator lamp (MIL) Brake system indicator Battery charging system indicator Do the indicators come on? YES Go to the gauge control module self-diagnostic function . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the following indicators in the gauge control module:

- Malfunction indicator lamp (MIL)

- Brake system indicator

- Battery charging system indicator

Do the indicators come on?

YES

Go to the gauge control module self-diagnostic function .

NO

Go to step 2.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B7 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 3. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B7 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 3.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

- Open wire check (IG1 METER line) 1 -1. Disconnect the following connector. Gauge control module connector A (32P) -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Gauge control module connector A (32P): disconnected Test point 1 Gauge control module connector A (32P) No. 17 Test point 2 Body ground Is there battery voltage? YES Replace the gauge control module . NO Repair an open in the IG1 METER wire between the under-dash fuse/relay box and the gauge control module.

-1. Disconnect the following connector.

Gauge control module connector A (32P)

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Gauge control module connector A (32P): disconnected

Test point 1 | Gauge control module connector A (32P) No. 17

Test point 2 | Body ground

Is there battery voltage?

YES

Replace the gauge control module .

NO

Repair an open in the IG1 METER wire between the under-dash fuse/relay box and the gauge control module.
````

## Chunk 2373: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off
- Source path: `pages\1194.html`
- Chunk ID: `chunk_bc2b237a34cd`
- Images: `images\GHH401735.png`, `images\GHH401736.png`, `images\GHH401737.jpeg`, `images\GHH401738.png`, `images\GHH401739.png`, `images\GHH401740.png`, `images\GHH401741.png`, `images\GHH401742.jpeg`
- Duplicate sources: `pages\15300.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off

- DTCs check -1. Turn the vehicle to the ON mode. -2. Check for DTCs with the HDS. DTC Description DTC DTC (IDAS) Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for DTCs with the HDS.

DTC Description | DTC

DTC (IDAS)

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- CAN gateway system DTC check -1. Check for DTCs with the HDS. DTC Description DTC U0029-00 CAN Gateway F-CAN ch A Bus Off U0047-00 CAN Gateway F-CAN ch B Bus Off U3000-49 CAN Gateway Internal Failure Is DTC U0029-00, U0047-00, and/or U3000-49 indicated? YES Go to the indicated DTCs troubleshooting . NO Go to step 3.

-1. Check for DTCs with the HDS.

DTC Description | DTC

U0029-00 CAN Gateway F-CAN ch A Bus Off

U0047-00 CAN Gateway F-CAN ch B Bus Off

U3000-49 CAN Gateway Internal Failure

Is DTC U0029-00, U0047-00, and/or U3000-49 indicated?

YES

Go to the indicated DTCs troubleshooting .

NO

Go to step 3.

- Fuse check1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B7 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 4. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B7 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 4.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

- Fuse check2 -1. Check the following fuse. 2/4-door: Fuse No. B17 (5 A) *1, No. B4 (5 A) *2 Location Under-dash fuse/relay box *1: Without keyless access system *2: With keyless access system 5-door: Fuse No. B5 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 5. NO 2/4-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B17 (5 A) *1, No. B4 (5 A) *2 fuse circuit. *1: Without keyless access system *2: With keyless access system 5-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 (10 A) fuse circuit.

-1. Check the following fuse.

2/4-door:

Fuse | No. B17 (5 A) *1, No. B4 (5 A) *2

Location | Under-dash fuse/relay box

*1: Without keyless access system

*2: With keyless access system

5-door:

Fuse | No. B5 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 5.

NO

2/4-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B17 (5 A) *1, No. B4 (5 A) *2 fuse circuit.

*1: Without keyless access system

*2: With keyless access system

5-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 (10 A) fuse circuit.

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check if all of the gauge indicators come on for a few seconds. Do the indicator come on? YES Go to step 6. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check if all of the gauge indicators come on for a few seconds.

Do the indicator come on?

YES

Go to step 6.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. 2/4-door: Test condition Vehicle ON mode Multipurpose camera unit 20P connector: disconnected Test point 1 Multipurpose camera unit 20P connector No.
````

## Chunk 2374: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off
- Source path: `pages\1194.html`
- Chunk ID: `chunk_4b6a48cd8425`
- Images: `images\GHH401735.png`, `images\GHH401736.png`, `images\GHH401737.jpeg`, `images\GHH401738.png`, `images\GHH401739.png`, `images\GHH401740.png`, `images\GHH401741.png`, `images\GHH401742.jpeg`
- Duplicate sources: `pages\15300.html`

### Full Text

````text
icator come on? YES Go to step 6. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check if all of the gauge indicators come on for a few seconds.

Do the indicator come on?

YES

Go to step 6.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. 2/4-door: Test condition Vehicle ON mode Multipurpose camera unit 20P connector: disconnected Test point 1 Multipurpose camera unit 20P connector No. 19 Test point 2 Body ground 5-door: Test condition Vehicle ON mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 1 Test point 2 Body ground Is there battery voltage? YES Go to step 7. NO Repair an open in the IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) wire between the under-dash fuse/relay box and the multipurpose camera unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

2/4-door:

Test condition | Vehicle ON mode

Multipurpose camera unit 20P connector: disconnected

Test point 1 | Multipurpose camera unit 20P connector No. 19

Test point 2 | Body ground

5-door:

Test condition | Vehicle ON mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 7.

NO

Repair an open in the IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) wire between the under-dash fuse/relay box and the multipurpose camera unit.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode Multipurpose camera unit 20P connector: disconnected Test point 1 Multipurpose camera unit 20P connector No. 14 Test point 2 Body ground 5-door: Test condition Vehicle OFF (LOCK) mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 8 Test point 2 Body ground Is there continuity? YES Go to step 8. NO 2/4-door: Repair an open in the GND wire between the multipurpose camera unit and body ground (G502), or repair poor ground (G502). 5-door: Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

2/4-door:

Test condition | Vehicle OFF (LOCK) mode

Multipurpose camera unit 20P connector: disconnected

Test point 1 | Multipurpose camera unit 20P connector No. 14

Test point 2 | Body ground

5-door:

Test condition | Vehicle OFF (LOCK) mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 8

Test point 2 | Body ground

Is there continuity?

YES

Go to step 8.

NO

2/4-door: Repair an open in the GND wire between the multipurpose camera unit and body ground (G502), or repair poor ground (G502).

5-door: Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

- F-CAN circuit communication check -1. Reconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -2. Turn the vehicle to the ON mode. -3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? Gauge control module (Bus A) is Not Available Go to step 9. Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available Go to step 10. Multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and gauge control module are Detected Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Reconnect the following connector.
````

## Chunk 2375: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off
- Source path: `pages\1194.html`
- Chunk ID: `chunk_c88bdf870ad0`
- Images: `images\GHH401735.png`, `images\GHH401736.png`, `images\GHH401737.jpeg`, `images\GHH401738.png`, `images\GHH401739.png`, `images\GHH401740.png`, `images\GHH401741.png`, `images\GHH401742.jpeg`
- Duplicate sources: `pages\15300.html`

### Full Text

````text
- F-CAN circuit communication check -1. Reconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -2. Turn the vehicle to the ON mode. -3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? Gauge control module (Bus A) is Not Available Go to step 9. Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available Go to step 10. Multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and gauge control module are Detected Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Reconnect the following connector.

2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector

-2. Turn the vehicle to the ON mode.

-3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Which result is indicated?

Gauge control module (Bus A) is Not Available

Go to step 9.

Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available

Go to step 10.

Multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and gauge control module are Detected

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

- Open wire check (F-CAN A_L, F-CAN A_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 24P connector (female terminals) No. 3: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 12P connector (female terminals) No. 9: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for loose terminals in the CAN gateway 12P connector and gauge control module connector A (32P). If they are OK, substitute a known-good gauge control module , then retest. If the indicators come on then go off after substitution, replace the original gauge control module . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

Gauge control module connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Gauge control module connector A (32P): disconnected

Test point 1 | CAN gateway 24P connector (female terminals) No. 3:

Test point 2 | Gauge control module connector A (32P) No. 19

Test point 1 | CAN gateway 12P connector (female terminals) No. 9:

Test point 2 | Gauge control module connector A (32P) No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for loose terminals in the CAN gateway 12P connector and gauge control module connector A (32P). If they are OK, substitute a known-good gauge control module , then retest. If the indicators come on then go off after substitution, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

- Open wire check (F-CAN B_L, F-CAN B_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Multipurpose camera unit 20P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Multipurpose camera unit 20P connector No. 2 Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Multipurpose camera unit 20P connector No.
````

## Chunk 2376: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off
- Source path: `pages\1194.html`
- Chunk ID: `chunk_be8e5ee38912`
- Images: `images\GHH401735.png`, `images\GHH401736.png`, `images\GHH401737.jpeg`, `images\GHH401738.png`, `images\GHH401739.png`, `images\GHH401740.png`, `images\GHH401741.png`, `images\GHH401742.jpeg`
- Duplicate sources: `pages\15300.html`

### Full Text

````text
r an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

- Open wire check (F-CAN B_L, F-CAN B_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Multipurpose camera unit 20P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Multipurpose camera unit 20P connector No. 2 Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Multipurpose camera unit 20P connector No. 13 5-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Millimeter wave radar 8P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Millimeter wave radar 8P connector No. 7 Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Millimeter wave radar 8P connector No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

2/4-door: Multipurpose camera unit 20P connector

5-door: Millimeter wave radar 8P connector

-3. Check for continuity between test points 1 and 2.

2/4-door:

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Multipurpose camera unit 20P connector: disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 12:

Test point 2 | Multipurpose camera unit 20P connector No. 2

Test point 1 | CAN gateway 12P connector (female terminals) No. 5:

Test point 2 | Multipurpose camera unit 20P connector No. 13

5-door:

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Millimeter wave radar 8P connector: disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 12:

Test point 2 | Millimeter wave radar 8P connector No. 7

Test point 1 | CAN gateway 12P connector (female terminals) No. 5:

Test point 2 | Millimeter wave radar 8P connector No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and the CAN gateway.
````

## Chunk 2377: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)
- Source path: `pages\1195.html`
- Chunk ID: `chunk_8b993b0353cd`
- Images: none
- Duplicate sources: `pages\16590.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - ACC indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)

- DTCs check -1. Turn the vehicle to the ON mode. -2. Check for DTCs with the HDS. DTC Description DTC DTC (IDAS) Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for DTCs with the HDS.

DTC Description | DTC

DTC (IDAS)

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- CAN gateway system DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 3.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 3.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B5 Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 4. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B5

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 4.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 fuse circuit.

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check if all of the gauge indicators come on for a few seconds. Do the indicators come on? YES Go to step 5. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check if all of the gauge indicators come on for a few seconds.

Do the indicators come on?

YES

Go to step 5.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Millimeter wave radar 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 1 Test point 2 Body ground Is there battery voltage? YES Go to step 6. NO Repair an open in the IG1 OPTION wire between the under-dash fuse/relay box and the millimeter wave radar.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Millimeter wave radar 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 6.

NO

Repair an open in the IG1 OPTION wire between the under-dash fuse/relay box and the millimeter wave radar.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 8 Test point 2 Body ground Is there continuity? YES Check for poor connections or loose terminals at the millimeter wave radar. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the millimeter wave radar . NO Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 8

Test point 2 | Body ground

Is there continuity?

YES

Check for poor connections or loose terminals at the millimeter wave radar. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the millimeter wave radar .

NO

Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).
````

## Chunk 2378: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Does not sense the vehicle driving ahead

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Does not sense the vehicle driving ahead
- Source path: `pages\1196.html`
- Chunk ID: `chunk_b71a5d181809`
- Images: none
- Duplicate sources: `pages\16568.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - Does not sense the vehicle driving ahead

- All condition check -1. Find out if the detection problem occurs under all conditions. Does it occur under all conditions? YES The millimeter wave radar vertical aiming is incorrect. Aim the millimeter wave radar . NO Go to step 2.

-1. Find out if the detection problem occurs under all conditions.

Does it occur under all conditions?

YES

The millimeter wave radar vertical aiming is incorrect. Aim the millimeter wave radar .

NO

Go to step 2.

- Road condition check -1. Find out if the detection problem occurs only on a particular road such as a winding road, an entrance of a corner, an exit of a corner, a tight corner, or a bad road. Does it occur only on a particular road? YES Explain to the customer that the system sometimes cannot detect under certain road conditions. NO Go to step 3.

-1. Find out if the detection problem occurs only on a particular road such as a winding road, an entrance of a corner, an exit of a corner, a tight corner, or a bad road.

Does it occur only on a particular road?

YES

Explain to the customer that the system sometimes cannot detect under certain road conditions.

NO

Go to step 3.

- Weather condition check -1. Find out if the detection problem occurs only under poor weather conditions such as fog, snow, heavy rain, or gusty winds. Does it occur only under poor weather conditions? YES Explain to the customer that the system sometimes cannot detect under poor weather conditions. NO Go to step 4.

-1. Find out if the detection problem occurs only under poor weather conditions such as fog, snow, heavy rain, or gusty winds.

Does it occur only under poor weather conditions?

YES

Explain to the customer that the system sometimes cannot detect under poor weather conditions.

NO

Go to step 4.

- Driving condition check: -1. Find out if the detection problem occurs only when the vehicle ahead drives under these conditions: Merged into the lane suddenly. Closing on a vehicle within 4 m (13 ft). Does it occur only under certain driving conditions? YES Explain to the customer that the system sometimes cannot detect under certain driving conditions. NO Go to step 5.

-1. Find out if the detection problem occurs only when the vehicle ahead drives under these conditions:

- Merged into the lane suddenly.

- Closing on a vehicle within 4 m (13 ft).

Does it occur only under certain driving conditions?

YES

Explain to the customer that the system sometimes cannot detect under certain driving conditions.

NO

Go to step 5.

- Millimeter wave radar aiming check -1. Confirm if the radar detects vehicles driving in another lane. Does it detect vehicles in other lanes? YES The millimeter wave radar horizontal aiming is incorrect. Aim the millimeter wave radar . NO Go to step 6.

-1. Confirm if the radar detects vehicles driving in another lane.

Does it detect vehicles in other lanes?

YES

The millimeter wave radar horizontal aiming is incorrect. Aim the millimeter wave radar .

NO

Go to step 6.

- Other component check -1. Confirm if the detection problem is caused by instability. NOTE: If the cause of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions. Is the vehicle unstable? (Compare it to a known-good, like vehicle.) YES Check other components such as VSA modulator-control unit or wheel speed sensors, etc. NO Go to step 7.

-1. Confirm if the detection problem is caused by instability.

NOTE: If the cause of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions.

Is the vehicle unstable? (Compare it to a known-good, like vehicle.)

YES

Check other components such as VSA modulator-control unit or wheel speed sensors, etc.

NO

Go to step 7.

- Heavy load check -1. Check if there is a heavy load in the trunk. Is there a heavy load in the trunk? YES Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads. NO Go to step 8.

-1. Check if there is a heavy load in the trunk.

Is there a heavy load in the trunk?

YES

Remove the heavy load from the trunk.
````

## Chunk 2379: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Does not sense the vehicle driving ahead

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Does not sense the vehicle driving ahead
- Source path: `pages\1196.html`
- Chunk ID: `chunk_43e10aa7c662`
- Images: none
- Duplicate sources: `pages\16568.html`

### Full Text

````text
e cause of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions.

Is the vehicle unstable? (Compare it to a known-good, like vehicle.)

YES

Check other components such as VSA modulator-control unit or wheel speed sensors, etc.

NO

Go to step 7.

- Heavy load check -1. Check if there is a heavy load in the trunk. Is there a heavy load in the trunk? YES Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads. NO Go to step 8.

-1. Check if there is a heavy load in the trunk.

Is there a heavy load in the trunk?

YES

Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads.

NO

Go to step 8.

- Millimeter wave radar visual check -1. Check for dirt, dust, or snow on the surface of the millimeter wave radar. Are the millimeter wave radar OK? YES Go to step 9. NO Clean the millimeter wave radar.

-1. Check for dirt, dust, or snow on the surface of the millimeter wave radar.

Are the millimeter wave radar OK?

YES

Go to step 9.

NO

Clean the millimeter wave radar.

- Vehicle ride height check -1. Measure the front and rear vehicle ride height. Is the vehicle ride height equal? YES Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting . NO Inspect the suspension for damage, and compare ride height to a known-good vehicle. Adjust the wheel alignment as needed .

-1. Measure the front and rear vehicle ride height.

Is the vehicle ride height equal?

YES

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

NO

Inspect the suspension for damage, and compare ride height to a known-good vehicle. Adjust the wheel alignment as needed .
````

## Chunk 2380: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Intermittently senses the vehicle driving ahead

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Intermittently senses the vehicle driving ahead
- Source path: `pages\1197.html`
- Chunk ID: `chunk_4dbb429e0487`
- Images: none
- Duplicate sources: `pages\16569.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - Intermittently senses the vehicle driving ahead

- Road condition check -1. Find out if the detection problem occurs only on a particular road such as a winding road, an entrance of a corner, an exit of a corner, a tight corner, or a bad road. Does it occur only on a particular road? YES Explain to the customer that the system sometimes cannot detect under certain road conditions. NO Go to step 2.

-1. Find out if the detection problem occurs only on a particular road such as a winding road, an entrance of a corner, an exit of a corner, a tight corner, or a bad road.

Does it occur only on a particular road?

YES

Explain to the customer that the system sometimes cannot detect under certain road conditions.

NO

Go to step 2.

- Weather condition check -1. Find out if the detection problem occurs only under poor weather conditions such as fog, snow, heavy rain, or gusty winds. Does it occur only under poor weather conditions? YES Explain to the customer that the system sometimes cannot detect under poor weather conditions. NO Go to step 3.

-1. Find out if the detection problem occurs only under poor weather conditions such as fog, snow, heavy rain, or gusty winds.

Does it occur only under poor weather conditions?

YES

Explain to the customer that the system sometimes cannot detect under poor weather conditions.

NO

Go to step 3.

- Driving condition check: -1. Find out if the detection problem occurs only when the vehicle ahead drives under these conditions: Merged into the lane suddenly. Closing on a vehicle within 4 m (13 ft). Does it occur only under certain driving conditions? YES Explain to the customer that the system sometimes cannot detect under certain driving conditions. NO Go to step 4.

-1. Find out if the detection problem occurs only when the vehicle ahead drives under these conditions:

- Merged into the lane suddenly.

- Closing on a vehicle within 4 m (13 ft).

Does it occur only under certain driving conditions?

YES

Explain to the customer that the system sometimes cannot detect under certain driving conditions.

NO

Go to step 4.

- Millimeter wave radar aiming check -1. Confirm if the radar detects vehicles driving in another lane. Does it detect vehicles in other lanes? YES The millimeter wave radar horizontal aiming is incorrect. Aim the millimeter wave radar . NO Go to step 5.

-1. Confirm if the radar detects vehicles driving in another lane.

Does it detect vehicles in other lanes?

YES

The millimeter wave radar horizontal aiming is incorrect. Aim the millimeter wave radar .

NO

Go to step 5.

- All condition check -1. Find out if the detection problem occurs under all conditions. Does it occur under all conditions? YES The millimeter wave radar vertical aiming is incorrect. Aim the millimeter wave radar . NO Go to step 6.

-1. Find out if the detection problem occurs under all conditions.

Does it occur under all conditions?

YES

The millimeter wave radar vertical aiming is incorrect. Aim the millimeter wave radar .

NO

Go to step 6.

- Other component check -1. Confirm if the detection problem is caused by instability. NOTE: If the cause of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions. Is the vehicle unstable? (Compare it to a known-good, like vehicle.) YES Check other components such as VSA modulator-control unit or wheel speed sensors, etc. NO Go to step 7.

-1. Confirm if the detection problem is caused by instability.

NOTE: If the cause of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions.

Is the vehicle unstable? (Compare it to a known-good, like vehicle.)

YES

Check other components such as VSA modulator-control unit or wheel speed sensors, etc.

NO

Go to step 7.

- Heavy load check -1. Check if there was a heavy load in the trunk. Was there a heavy load in the trunk? YES Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads. NO Go to step 8.

-1. Check if there was a heavy load in the trunk.

Was there a heavy load in the trunk?

YES

Remove the heavy load from the trunk.
````

## Chunk 2381: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Intermittently senses the vehicle driving ahead

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Intermittently senses the vehicle driving ahead
- Source path: `pages\1197.html`
- Chunk ID: `chunk_d02b91fe50f5`
- Images: none
- Duplicate sources: `pages\16569.html`

### Full Text

````text
use of the misdetection or undetectable problems is unclear, it is possible that the problem was caused by environmental conditions. Explain to the customer that intermittent failures are sometimes caused by environmental conditions.

Is the vehicle unstable? (Compare it to a known-good, like vehicle.)

YES

Check other components such as VSA modulator-control unit or wheel speed sensors, etc.

NO

Go to step 7.

- Heavy load check -1. Check if there was a heavy load in the trunk. Was there a heavy load in the trunk? YES Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads. NO Go to step 8.

-1. Check if there was a heavy load in the trunk.

Was there a heavy load in the trunk?

YES

Remove the heavy load from the trunk. Advise the customer that this problem may occur temporarily when hauling heavy loads.

NO

Go to step 8.

- Millimeter wave radar visual check -1. Check for dirt, dust, or snow on the surface of the millimeter wave radar. Are the millimeter wave radar OK? YES Go to step 9. NO Clean the millimeter wave radar.

-1. Check for dirt, dust, or snow on the surface of the millimeter wave radar.

Are the millimeter wave radar OK?

YES

Go to step 9.

NO

Clean the millimeter wave radar.

- Vehicle's history check -1. Check the vehicle's history for front end collision repairs. Has the vehicle been in a collision and repaired? YES Go to step 10. NO Go to step 12.

-1. Check the vehicle's history for front end collision repairs.

Has the vehicle been in a collision and repaired?

YES

Go to step 10.

NO

Go to step 12.

- Millimeter wave radar installation check -1. Check if the millimeter wave radar assembly is installed correctly, and also check if the vehicle frame is straight. Are all parts installed correctly? YES Go to step 11. NO Reinstall the part correctly, or if damaged, replace the part, then aim the millimeter wave radar .

-1. Check if the millimeter wave radar assembly is installed correctly, and also check if the vehicle frame is straight.

Are all parts installed correctly?

YES

Go to step 11.

NO

Reinstall the part correctly, or if damaged, replace the part, then aim the millimeter wave radar .

- Vehicle ride height check -1. Measure the front and rear vehicle ride height. Is the vehicle ride height equal? YES Go to step 12. NO Inspect the suspension for damage, and compare ride height to a known-good vehicle. Adjust the wheel alignment as needed .

-1. Measure the front and rear vehicle ride height.

Is the vehicle ride height equal?

YES

Go to step 12.

NO

Inspect the suspension for damage, and compare ride height to a known-good vehicle. Adjust the wheel alignment as needed .

- Wheel alignment check -1. Check the wheel alignment . Is the wheel alignment OK? YES Aim the millimeter wave radar . NO Adjust the wheel alignment .

-1. Check the wheel alignment .

Is the wheel alignment OK?

YES

Aim the millimeter wave radar .

NO

Adjust the wheel alignment .
````

## Chunk 2382: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Senses a vehicle driving in another lane

- Title: Adaptive Cruise Control (ACC) Symptom Troubleshooting - Senses a vehicle driving in another lane
- Source path: `pages\1198.html`
- Chunk ID: `chunk_75dc72e71ac1`
- Images: none
- Duplicate sources: `pages\16567.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Symptom Troubleshooting - Senses a vehicle driving in another lane

- Problem verification 1 -1. Find out when and under what conditions the system has misdetections. Do they occur within 20 minutes or less? YES Go to step 2. NO Explain to the customer that system misdetections are sometimes caused by the environment (weather, road conditions, driving conditions, etc.).

-1. Find out when and under what conditions the system has misdetections.

Do they occur within 20 minutes or less?

YES

Go to step 2.

NO

Explain to the customer that system misdetections are sometimes caused by the environment (weather, road conditions, driving conditions, etc.).

- Problem verification 2 -1. Find out if the detection problem occurs only with certain types of vehicles (dirty vehicle, tall vehicle, motorcycle, or special vehicle). Does it occur only with certain types of vehicles? YES Explain to the customer that the system sometimes cannot detect certain vehicle types. NO Go to step 3.

-1. Find out if the detection problem occurs only with certain types of vehicles (dirty vehicle, tall vehicle, motorcycle, or special vehicle).

Does it occur only with certain types of vehicles?

YES

Explain to the customer that the system sometimes cannot detect certain vehicle types.

NO

Go to step 3.

- Vehicle's history check -1. Check the vehicle's history for front end collision repairs. Has the vehicle been in a collision and repaired? YES Go to step 4. NO Go to step 5.

-1. Check the vehicle's history for front end collision repairs.

Has the vehicle been in a collision and repaired?

YES

Go to step 4.

NO

Go to step 5.

- Millimeter wave radar installation check -1. Check if the millimeter wave radar assembly is installed correctly, and also check if the vehicle frame is straight. Are all parts installed correctly? YES Go to step 5. NO Reinstall the part correctly, or if damaged, replace the part, then aim the millimeter wave radar .

-1. Check if the millimeter wave radar assembly is installed correctly, and also check if the vehicle frame is straight.

Are all parts installed correctly?

YES

Go to step 5.

NO

Reinstall the part correctly, or if damaged, replace the part, then aim the millimeter wave radar .

- Wheel alignment check -1. Check the wheel alignment . Is the wheel alignment OK? YES Aim the millimeter wave radar . NO Adjust the wheel alignment .

-1. Check the wheel alignment .

Is the wheel alignment OK?

YES

Aim the millimeter wave radar .

NO

Adjust the wheel alignment .
````

## Chunk 2383: Collision Mitigation Braking System (CMBS) Symptom Troubleshooting - CMBS indicator (on the MID) does not go off

- Title: Collision Mitigation Braking System (CMBS) Symptom Troubleshooting - CMBS indicator (on the MID) does not go off
- Source path: `pages\1199.html`
- Chunk ID: `chunk_b9aa7082ee97`
- Images: none
- Duplicate sources: `pages\13724.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Symptom Troubleshooting - CMBS indicator (on the MID) does not go off

- DTCs check -1. Turn the vehicle to the ON mode. -2. Check for DTCs with the HDS. DTC Description DTC DTC (IDAS) Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for DTCs with the HDS.

DTC Description | DTC

DTC (IDAS)

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- VSA system DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 3.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 3.

- PGM-FI system DTC check -1. Check for DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 4.

-1. Check for DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 4.

- Gauge control module operation check -1. Do the gauge control module self-diagnostic function . Is the gauge control module OK? YES Go to step 5. NO Replace the gauge control module .

-1. Do the gauge control module self-diagnostic function .

Is the gauge control module OK?

YES

Go to step 5.

NO

Replace the gauge control module .

- CMBS OFF switch check -1. Test the CMBS OFF switch . Is the switch OK? YES Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) . NO Replace the CMBS OFF switch .

-1. Test the CMBS OFF switch .

Is the switch OK?

YES

Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) .

NO

Replace the CMBS OFF switch .
````

## Chunk 2384: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not come on

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not come on
- Source path: `pages\1200.html`
- Chunk ID: `chunk_629871492766`
- Images: `images\GHH401743.jpeg`
- Duplicate sources: `pages\16591.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not come on

- Gauge control module operation check -1. Do the gauge control module self-diagnostic function . Is the gauge control module OK? YES Go to step 2. NO Replace the gauge control module .

-1. Do the gauge control module self-diagnostic function .

Is the gauge control module OK?

YES

Go to step 2.

NO

Replace the gauge control module .

- ACC combination switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the ACC combination switch . Is the switch OK? YES Go to step 3. NO Replace the ACC combination switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the ACC combination switch .

Is the switch OK?

YES

Go to step 3.

NO

Replace the ACC combination switch .

- Open wire check (CRUISE SW line) -1. Disconnect the following connector. ACC combination switch 12P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode ACC combination switch 12P connector: disconnected Test point 1 ACC combination switch 12P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Repair an open in the CRUISE GND wire between the ACC combination switch and the gauge control module. NO Repair an open in the CRUISE SW wire between the ACC combination switch and the gauge control module.

-1. Disconnect the following connector.

ACC combination switch 12P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

ACC combination switch 12P connector: disconnected

Test point 1 | ACC combination switch 12P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Repair an open in the CRUISE GND wire between the ACC combination switch and the gauge control module.

NO

Repair an open in the CRUISE SW wire between the ACC combination switch and the gauge control module.
````

## Chunk 2385: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not go off

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not go off
- Source path: `pages\1201.html`
- Chunk ID: `chunk_e7d062406059`
- Images: none
- Duplicate sources: `pages\16592.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS activation indicator (on the MID) does not go off

- Gauge control module operation check -1. Do the gauge control module self-diagnostic function . Is the gauge control module OK? YES Go to step 2. NO Replace the gauge control module .

-1. Do the gauge control module self-diagnostic function .

Is the gauge control module OK?

YES

Go to step 2.

NO

Replace the gauge control module .

- ACC combination switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the ACC combination switch . Is the switch OK? YES Repair a short to ground in the CRUISE GND wire between the ACC combination switch and the gauge control module. NO Replace the ACC combination switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the ACC combination switch .

Is the switch OK?

YES

Repair a short to ground in the CRUISE GND wire between the ACC combination switch and the gauge control module.

NO

Replace the ACC combination switch .
````

## Chunk 2386: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not come on

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not come on
- Source path: `pages\1202.html`
- Chunk ID: `chunk_648b03e50245`
- Images: none
- Duplicate sources: `pages\16593.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not come on

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check the following indicators in the gauge control module: Malfunction indicator lamp (MIL) Brake system indicator Battery charging system indicator Do the indicators come on? YES Go to the gauge control module self-diagnostic function . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the following indicators in the gauge control module:

- Malfunction indicator lamp (MIL)

- Brake system indicator

- Battery charging system indicator

Do the indicators come on?

YES

Go to the gauge control module self-diagnostic function .

NO

Go to step 2.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B7 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 3. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B7 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 3.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

- Open wire check (IG1 METER line) -1. Disconnect the following connector. Gauge control module connector A (32P) -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Gauge control module connector A (32P): disconnected Test point 1 Gauge control module connector A (32P) No. 17 Test point 2 Body ground Is there battery voltage? YES Replace the gauge control module . NO Repair an open in the IG1 METER wire between the under-dash fuse/relay box and the gauge control module.

-1. Disconnect the following connector.

Gauge control module connector A (32P)

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Gauge control module connector A (32P): disconnected

Test point 1 | Gauge control module connector A (32P) No. 17

Test point 2 | Body ground

Is there battery voltage?

YES

Replace the gauge control module .

NO

Repair an open in the IG1 METER wire between the under-dash fuse/relay box and the gauge control module.
````

## Chunk 2387: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)
- Source path: `pages\1203.html`
- Chunk ID: `chunk_70d829aee2d2`
- Images: `images\GHH401744.png`, `images\GHH401745.png`, `images\GHH401746.jpeg`, `images\GHH401747.png`, `images\GHH401748.png`, `images\GHH401749.png`, `images\GHH401750.png`, `images\GHH401751.jpeg`
- Duplicate sources: `pages\15301.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)

- DTCs check -1. Turn the vehicle to the ON mode. -2. Check for DTCs with the HDS. DTC Description DTC DTC (IDAS) Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for DTCs with the HDS.

DTC Description | DTC

DTC (IDAS)

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- CAN gateway system DTC check -1. Check for DTCs with the HDS. DTC Description DTC U0029-00 CAN Gateway F-CAN ch A Bus Off U0047-00 CAN Gateway F-CAN ch B Bus Off U3000-49 CAN Gateway Internal Failure Is DTC U0029-00, U0047-00, and/or U3000-49 indicated? YES Go to the indicated DTCs troubleshooting . NO Go to step 3.

-1. Check for DTCs with the HDS.

DTC Description | DTC

U0029-00 CAN Gateway F-CAN ch A Bus Off

U0047-00 CAN Gateway F-CAN ch B Bus Off

U3000-49 CAN Gateway Internal Failure

Is DTC U0029-00, U0047-00, and/or U3000-49 indicated?

YES

Go to the indicated DTCs troubleshooting .

NO

Go to step 3.

- EPS system DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 4.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 4.

- Fuse check1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B7 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 5. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B7 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 5.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B7 (10 A) fuse circuit.

- Fuse check2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. 2/4-door: Fuse No. B17 (5 A) *1, No. B4 (5 A) *2 Location Under-dash fuse/relay box *1: Without keyless access system *2: With keyless access system 5-door: Fuse No. B5 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 6. NO 2/4-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B17 (5 A) *1, No. B4 (5 A) *2 fuse circuit. *1: Without keyless access system *2: With keyless access system 5-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 (10 A) fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

2/4-door:

Fuse | No. B17 (5 A) *1, No. B4 (5 A) *2

Location | Under-dash fuse/relay box

*1: Without keyless access system

*2: With keyless access system

5-door:

Fuse | No. B5 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 6.

NO

2/4-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B17 (5 A) *1, No. B4 (5 A) *2 fuse circuit.

*1: Without keyless access system

*2: With keyless access system

5-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 (10 A) fuse circuit.

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check the indicator in the gauge control module. Do the indicators come on? YES Go to step 7. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check the indicator in the gauge control module.

Do the indicators come on?

YES

Go to step 7.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector.
````

## Chunk 2388: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)
- Source path: `pages\1203.html`
- Chunk ID: `chunk_72b2c74d749f`
- Images: `images\GHH401744.png`, `images\GHH401745.png`, `images\GHH401746.jpeg`, `images\GHH401747.png`, `images\GHH401748.png`, `images\GHH401749.png`, `images\GHH401750.png`, `images\GHH401751.jpeg`
- Duplicate sources: `pages\15301.html`

### Full Text

````text
*2: With keyless access system

5-door: Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 (10 A) fuse circuit.

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check the indicator in the gauge control module. Do the indicators come on? YES Go to step 7. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check the indicator in the gauge control module.

Do the indicators come on?

YES

Go to step 7.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. 2/4-door: Test condition Vehicle ON mode Multipurpose camera unit 20P connector: disconnected Test point 1 Multipurpose camera unit 20P connector No. 19 Test point 2 Body ground 5-door: Test condition Vehicle ON mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 1 Test point 2 Body ground Is there battery voltage? YES Go to step 8. NO Repair an open in the IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) wire between the under-dash fuse/relay box and the multipurpose camera unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

2/4-door:

Test condition | Vehicle ON mode

Multipurpose camera unit 20P connector: disconnected

Test point 1 | Multipurpose camera unit 20P connector No. 19

Test point 2 | Body ground

5-door:

Test condition | Vehicle ON mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 8.

NO

Repair an open in the IG1 OPTION3 (2/4-door) or IG1 OPTION (5-door) wire between the under-dash fuse/relay box and the multipurpose camera unit.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode Multipurpose camera unit 20P connector: disconnected Test point 1 Multipurpose camera unit 20P connector No. 14 Test point 2 Body ground 5-door: Test condition Vehicle OFF (LOCK) mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 8 Test point 2 Body ground Is there continuity? YES Go to step 9. NO 2/4-door: Repair an open in the GND wire between the multipurpose camera unit and body ground (G502), or repair poor ground (G502). 5-door: Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

2/4-door:

Test condition | Vehicle OFF (LOCK) mode

Multipurpose camera unit 20P connector: disconnected

Test point 1 | Multipurpose camera unit 20P connector No. 14

Test point 2 | Body ground

5-door:

Test condition | Vehicle OFF (LOCK) mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 8

Test point 2 | Body ground

Is there continuity?

YES

Go to step 9.

NO

2/4-door: Repair an open in the GND wire between the multipurpose camera unit and body ground (G502), or repair poor ground (G502).

5-door: Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

- F-CAN circuit communication check -1. Reconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -2. Turn the vehicle to the ON mode. -3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? Gauge control module (Bus A) is Not Available Go to step 10. Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available Go to step 11.
````

## Chunk 2389: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)
- Source path: `pages\1203.html`
- Chunk ID: `chunk_8fca8fc57542`
- Images: `images\GHH401744.png`, `images\GHH401745.png`, `images\GHH401746.jpeg`, `images\GHH401747.png`, `images\GHH401748.png`, `images\GHH401749.png`, `images\GHH401750.png`, `images\GHH401751.jpeg`
- Duplicate sources: `pages\15301.html`

### Full Text

````text
epair an open in the GND wire between the multipurpose camera unit and body ground (G502), or repair poor ground (G502).

5-door: Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

- F-CAN circuit communication check -1. Reconnect the following connector. 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -2. Turn the vehicle to the ON mode. -3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? Gauge control module (Bus A) is Not Available Go to step 10. Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available Go to step 11. Multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and gauge control module are Detected Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

-1. Reconnect the following connector.

2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector

-2. Turn the vehicle to the ON mode.

-3. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Which result is indicated?

Gauge control module (Bus A) is Not Available

Go to step 10.

Multipurpose camera unit (Bus B) (2/4-door) or millimeter wave radar (Bus B) (5-door) is Not Available

Go to step 11.

Multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and gauge control module are Detected

Intermittent failure, the system is OK at this time. Refer to intermittent failures troubleshooting .

- Open wire check (F-CAN A_L, F-CAN A_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 3: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 12P connector (female terminals) No. 9: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for loose terminals in the CAN gateway 12P connector and gauge control module connector A (32P). If they are OK, substitute a known-good gauge control module , then retest. If the indicators come on then go off after substitution, replace the original gauge control module . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

Gauge control module connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Gauge control module connector A (32P): disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 3:

Test point 2 | Gauge control module connector A (32P) No. 19

Test point 1 | CAN gateway 12P connector (female terminals) No. 9:

Test point 2 | Gauge control module connector A (32P) No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for loose terminals in the CAN gateway 12P connector and gauge control module connector A (32P). If they are OK, substitute a known-good gauge control module , then retest. If the indicators come on then go off after substitution, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

- Open wire check (F-CAN B_L, F-CAN B_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Multipurpose camera unit 20P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Multipurpose camera unit 20P connector No.
````

## Chunk 2390: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2016 2017 2018)
- Source path: `pages\1203.html`
- Chunk ID: `chunk_2649e6884f3b`
- Images: `images\GHH401744.png`, `images\GHH401745.png`, `images\GHH401746.jpeg`, `images\GHH401747.png`, `images\GHH401748.png`, `images\GHH401749.png`, `images\GHH401750.png`, `images\GHH401751.jpeg`
- Duplicate sources: `pages\15301.html`

### Full Text

````text
en retest. If the indicators come on then go off after substitution, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the gauge control module and the CAN gateway.

- Open wire check (F-CAN B_L, F-CAN B_H lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector 2/4-door: Multipurpose camera unit 20P connector 5-door: Millimeter wave radar 8P connector -3. Check for continuity between test points 1 and 2. 2/4-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Multipurpose camera unit 20P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Multipurpose camera unit 20P connector No. 2 Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Multipurpose camera unit 20P connector No. 13 5-door: Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Millimeter wave radar 8P connector: disconnected Test point 1 CAN gateway 12P connector (female terminals) No. 12: Test point 2 Millimeter wave radar 8P connector No. 7 Test point 1 CAN gateway 12P connector (female terminals) No. 5: Test point 2 Millimeter wave radar 8P connector No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

2/4-door: Multipurpose camera unit 20P connector

5-door: Millimeter wave radar 8P connector

-3. Check for continuity between test points 1 and 2.

2/4-door:

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Multipurpose camera unit 20P connector: disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 12:

Test point 2 | Multipurpose camera unit 20P connector No. 2

Test point 1 | CAN gateway 12P connector (female terminals) No. 5:

Test point 2 | Multipurpose camera unit 20P connector No. 13

5-door:

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Millimeter wave radar 8P connector: disconnected

Test point 1 | CAN gateway 12P connector (female terminals) No. 12:

Test point 2 | Millimeter wave radar 8P connector No. 7

Test point 1 | CAN gateway 12P connector (female terminals) No. 5:

Test point 2 | Millimeter wave radar 8P connector No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Check for loose terminals and poor connections in the multipurpose camera unit 20P connector (2/4-door) or millimeter wave radar 8P connector (5-door). Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the multipurpose camera unit (2/4-door) or millimeter wave radar (5-door) and the CAN gateway.
````

## Chunk 2391: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)
- Source path: `pages\1204.html`
- Chunk ID: `chunk_0d0191453210`
- Images: none
- Duplicate sources: `pages\16594.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)

- DTCs check -1. Turn the vehicle to the ON mode. -2. Check for DTCs with the HDS. DTC Description DTC DTC (IDAS) Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for DTCs with the HDS.

DTC Description | DTC

DTC (IDAS)

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- CAN gateway system DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 3.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 3.

- EPS DTC check -1. Check for DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 4.

-1. Check for DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 4.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B5 Is the fuse OK? YES The fuse is OK. Reinstall the fuse, then go to step 5. NO Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B5

Is the fuse OK?

YES

The fuse is OK. Reinstall the fuse, then go to step 5.

NO

Replace the fuse. Turn the vehicle to the ON mode, then the OFF (LOCK) mode. If the fuse blows again, repair the short to ground on the No. B5 fuse circuit.

- Gauge control module operation check -1. Turn the vehicle to the ON mode. -2. Check the indicator in the gauge control module. Do the indicators come on? YES Go to step 6. NO Go to the gauge control module self-diagnostic function .

-1. Turn the vehicle to the ON mode.

-2. Check the indicator in the gauge control module.

Do the indicators come on?

YES

Go to step 6.

NO

Go to the gauge control module self-diagnostic function .

- Open wire check (IG1 OPTION line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Millimeter wave radar 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 1 Test point 2 Body ground Is there battery voltage? YES Go to step 7. NO Repair an open in the IG1 OPTION wire between the under-dash fuse/relay box and the millimeter wave radar.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Millimeter wave radar 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 7.

NO

Repair an open in the IG1 OPTION wire between the under-dash fuse/relay box and the millimeter wave radar.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Millimeter wave radar 8P connector: disconnected Test point 1 Millimeter wave radar 8P connector No. 8 Test point 2 Body ground Is there continuity? YES Check for poor connections or loose terminals at the millimeter wave radar. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the millimeter wave radar . NO Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 8

Test point 2 | Body ground

Is there continuity?

YES

Check for poor connections or loose terminals at the millimeter wave radar.
````

## Chunk 2392: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)

- Title: Lane Keeping Assist System (LKAS) Symptom Troubleshooting - LKAS indicator (on the MID) does not go off (2/4-door) (2019 2020 2021)
- Source path: `pages\1204.html`
- Chunk ID: `chunk_5731515e2e6c`
- Images: none
- Duplicate sources: `pages\16594.html`

### Full Text

````text
connector No. 8 Test point 2 Body ground Is there continuity? YES Check for poor connections or loose terminals at the millimeter wave radar. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the millimeter wave radar . NO Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Millimeter wave radar 8P connector: disconnected

Test point 1 | Millimeter wave radar 8P connector No. 8

Test point 2 | Body ground

Is there continuity?

YES

Check for poor connections or loose terminals at the millimeter wave radar. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. If they are OK, replace the millimeter wave radar .

NO

Repair an open in the GND wire between the millimeter wave radar and body ground (G401), or repair poor ground (G401).
````

## Chunk 2393: Adaptive Cruise Control (ACC) System Description - Control/Function

- Title: Adaptive Cruise Control (ACC) System Description - Control/Function
- Source path: `pages\1205.html`
- Chunk ID: `chunk_2dbdd8960b80`
- Images: `images\GHH401752.jpeg`, `images\GHH401753.jpeg`, `images\GHH401754.jpeg`
- Duplicate sources: `pages\16595.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - Control/Function

Basic Controls of the ACC System with Low Speed Follow (LSF)

- The ACC system uses the millimeter wave radar to detect the leading vehicle, determines the target vehicle and measures the distance to the target vehicle and its vehicle speed (the system also uses the multipurpose camera as needed to determine the target vehicle based on the lane and vehicle position information).

- When there is no leading vehicle, your vehicle drives at the preset speed. When there is a leading vehicle, your vehicle follows the vehicle and drives within the preset speed.

Example driving pattern: vehicle-following in heavy traffic.

Courtesy of HONDA, U.S.A., INC.

Example of driving pattern: Stop-in-traffic to vehicle-following

Courtesy of HONDA, U.S.A., INC.

The system estimates the driving course based on your vehicle speed and yaw rate and detects a vehicle that enters the camera range and differentiate it from the leading vehicle using the lane and leading vehicle information from the multipurpose camera.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2394: Adaptive Cruise Control (ACC) System Description - Overview (2016 2017 2018 2019)

- Title: Adaptive Cruise Control (ACC) System Description - Overview (2016 2017 2018 2019)
- Source path: `pages\1206.html`
- Chunk ID: `chunk_10d96b0065dc`
- Images: `images\GHH401755.jpeg`
- Duplicate sources: `pages\16596.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - Overview (2016 2017 2018 2019)

Function

ACC system with Low Speed Follow (LSF) uses the multipurpose camera unit to calculate and adjust your vehicle speed to maintain the appropriate distance from the your vehicle to the leading vehicle on the road based on your vehicle speed and driving conditions using the millimeter wave radar. When another vehicle cuts in between your vehicle and the leading vehicle, the system switches the target vehicle to a new vehicle using the image information (vehicle and lane information) from the multipurpose camera. When the leading vehicle changes lanes or goes out of the detection range, the vehicle drives at the preset vehicle speed until detecting a new target vehicle. ACC system works with the cruise control system to adjust the vehicle speed.

The cruise control mode can be entered by operating the distance switch while the ACC is working.

Control Block Diagram

Courtesy of HONDA, U.S.A., INC.

Operation Conditions

Control vehicle speed | Following function | 0 - 90 mph (0 - 145 km/h)

Set speed range | 25 - 90 mph (40 - 145 km/h)

Maximum acceleration | 0.2 G

Maximum deceleration | 0.4 G (0.3 G for all speeds from 37 mph (60 km/h) up)

Left/right detection angle of millimeter wave radar | 2/4-door: +/-15 degrees 5-door: +/-42.6 degrees

Up/down detection angle of millimeter wave radar | 2/4-door: +/-2 degrees 5-door: -6 to +11.5 degrees

Road inclination | Less than 6%

Detection object | Vehicle only
````

## Chunk 2395: Adaptive Cruise Control (ACC) System Description - Overview (2019 2020 2021)

- Title: Adaptive Cruise Control (ACC) System Description - Overview (2019 2020 2021)
- Source path: `pages\1207.html`
- Chunk ID: `chunk_b893e80dd58a`
- Images: `images\GHH401756.jpeg`
- Duplicate sources: `pages\16597.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - Overview (2019 2020 2021)

Function

ACC system with Low Speed Follow (LSF) uses the multipurpose camera unit to calculate and adjust your vehicle speed to maintain the appropriate distance from the your vehicle to the leading vehicle on the road based on your vehicle speed and driving conditions using the millimeter wave radar. When another vehicle cuts in between your vehicle and the leading vehicle, the system switches the target vehicle to a new vehicle using the image information (vehicle and lane information) from the multipurpose camera. When the leading vehicle changes lanes or goes out of the detection range, the vehicle drives at the preset vehicle speed until detecting a new target vehicle. ACC system works with the cruise control system to adjust the vehicle speed.

The cruise control mode can be entered by operating the distance switch while the ACC is working.

Control Block Diagram

Courtesy of HONDA, U.S.A., INC.

Operation Conditions

Control vehicle speed | Following function | 0 - 90 mph (0 - 145 km/h)

Set speed range | 25 - 90 mph (40 - 145 km/h)

Maximum acceleration | 0.2 G

Maximum deceleration | 0.4 G (0.3 G for all speeds from 37 mph (60 km/h) up)

Left/right detection angle of millimeter wave radar | +/-42.6 degrees

Up/down detection angle of millimeter wave radar | -6 to +11.5 degrees

Road inclination | Less than 6%

Detection object | Vehicle only
````

## Chunk 2396: Adaptive Cruise Control (ACC) System Description - System Diagram (2019 2020 2021)

- Title: Adaptive Cruise Control (ACC) System Description - System Diagram (2019 2020 2021)
- Source path: `pages\1208.html`
- Chunk ID: `chunk_9dd091f39903`
- Images: `images\GHH401757.jpeg`
- Duplicate sources: `pages\16598.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - System Diagram (2019 2020 2021)

The system diagram of the ACC system is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- CVT: Transmission control module (TCM)

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Millimeter Wave Radar Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | Steering angle signal Steering angle neutral position learning information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | ACC combination switch signal (switch failure information) Customization signal

- ACC combination switch signal (switch failure information)

- Customization signal

Multipurpose camera unit | Object recognition information Multipurpose camera unit failure information Traffic lane information

- Object recognition information

- Multipurpose camera unit failure information

- Traffic lane information

Originating Unit | Signal Name

PCM | PCM failure information for ACC system Accelerator pedal position (APP) sensor control state signal Brake pedal position switch signal Shift position status Transmission failure information for ACC system Vehicle speed signal for transmission

- PCM failure information for ACC system

- Accelerator pedal position (APP) sensor control state signal

- Brake pedal position switch signal

- Shift position status

- Transmission failure information for ACC system

- Vehicle speed signal for transmission

SRS unit | Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information Yaw rate sensor signal, Yaw rate sensor failure information

- Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information

- Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information

- Yaw rate sensor signal, Yaw rate sensor failure information

VSA modulator-control unit | Brake control state signal Brake light relay failure information Electric parking brake status signal, Electric parking brake system failure information Master cylinder pressure signal, Master cylinder pressure sensor failure information VSA system failure information for ACC system Wheel speed sensor signals, Wheel speed sensor failure information

- Brake control state signal

- Brake light relay failure information

- Electric parking brake status signal, Electric parking brake system failure information

- Master cylinder pressure signal, Master cylinder pressure sensor failure information

- VSA system failure information for ACC system

- Wheel speed sensor signals, Wheel speed sensor failure information

Millimeter Wave Radar Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | ---

Gauge control module | ACC system failure information Buzzer request signal Customization information Multi information display (MID) screen requirement: ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC system failure information

- Buzzer request signal

- Customization information

- Multi information display (MID) screen requirement:

- ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC indicator

- ACC activation indicator

- ACC system indicates for self-diagnostic function

Multipurpose camera unit | Vehicle information

PCM | ACC system failure information Shift position down request signal Engine torque request

- ACC system failure information

- Shift position down request signal

- Engine torque request

SRS unit | ---

VSA modulator-control unit | Deceleration request ACC system failure information Electric parking brake actuation request signal Stop hold request

- Deceleration request

- ACC system failure information

- Electric parking brake actuation request signal

- Stop hold request
````

## Chunk 2397: Adaptive Cruise Control (ACC) System Description - System Diagram (2/4-door) (2016 2017 2018 2019)

- Title: Adaptive Cruise Control (ACC) System Description - System Diagram (2/4-door) (2016 2017 2018 2019)
- Source path: `pages\1209.html`
- Chunk ID: `chunk_a8414df8bef3`
- Images: `images\GHH401758.jpeg`
- Duplicate sources: `pages\16599.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - System Diagram (2/4-door) (2016 2017 2018 2019)

The system diagram of the ACC system is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Multipurpose camera unit

- PCM

- SRS unit

- Transmission control module (TCM)

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Multipurpose Camera Unit Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | Steering angle signal Steering angle neutral position learning information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | ACC combination switch signal (switch failure information) Customization signal

- ACC combination switch signal (switch failure information)

- Customization signal

Millimeter wave radar | Object recognition information Millimeter wave radar failure information

- Object recognition information

- Millimeter wave radar failure information

PCM | Cruise control system operating status, Cruise control system failure information Accelerator pedal position (APP) sensor control state signal Brake pedal position switch signal Shift position status Transmission failure information for ACC system Vehicle speed signal for transmission

- Cruise control system operating status, Cruise control system failure information

- Accelerator pedal position (APP) sensor control state signal

- Brake pedal position switch signal

- Shift position status

- Transmission failure information for ACC system

- Vehicle speed signal for transmission

SRS unit | Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information Yaw rate sensor signal, Yaw rate sensor failure information

- Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information

- Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information

- Yaw rate sensor signal, Yaw rate sensor failure information

VSA modulator-control unit | Brake control state signal Brake light relay control signal, Brake light relay failure information Electric parking brake status signal, Electric parking brake system failure information Master cylinder pressure signal, Master cylinder pressure sensor failure information VSA system failure information for ACC system Wheel speed sensor signals, Wheel speed sensor failure information

- Brake control state signal

- Brake light relay control signal, Brake light relay failure information

- Electric parking brake status signal, Electric parking brake system failure information

- Master cylinder pressure signal, Master cylinder pressure sensor failure information

- VSA system failure information for ACC system

- Wheel speed sensor signals, Wheel speed sensor failure information

Multipurpose Camera Unit Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | ---

Gauge control module | ACC system failure information Buzzer request signal Customization information Multi information display (MID) screen requirement: ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC system failure information

- Buzzer request signal

- Customization information

- Multi information display (MID) screen requirement:

- ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC indicator

- ACC activation indicator

- ACC system indicates for self-diagnostic function

Millimeter wave radar | Vehicle information

PCM | ACC system failure information Shift position down request signal Throttle actuator control request signal

- ACC system failure information

- Shift position down request signal

- Throttle actuator control request signal

SRS unit | ---

VSA modulator-control unit | ACC automatic brake actuation request signal ACC system failure information Brake light relay actuation request signal Electric parking brake actuation request signal Low speed follow (LSF) actuation request signal

- ACC automatic brake actuation request signal

- ACC system failure information

- Brake light relay actuation request signal

- Electric parking brake actuation request signal

- Low speed follow (LSF) actuation request signal
````

## Chunk 2398: Adaptive Cruise Control (ACC) System Description - System Diagram (5-door) (2017 2018 2019)

- Title: Adaptive Cruise Control (ACC) System Description - System Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1210.html`
- Chunk ID: `chunk_b69f7ac00933`
- Images: `images\GHH401759.jpeg`
- Duplicate sources: `pages\16600.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) System Description - System Diagram (5-door) (2017 2018 2019)

The system diagram of the ACC system is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- CVT: Transmission control module (TCM)

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Millimeter Wave Radar Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | Steering angle signal Steering angle neutral position learning information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | ACC combination switch signal (switch failure information) Customization signal

- ACC combination switch signal (switch failure information)

- Customization signal

Multipurpose camera unit | Object recognition information Multipurpose camera unit failure information Traffic lane information

- Object recognition information

- Multipurpose camera unit failure information

- Traffic lane information

Originating Unit | Signal Name

PCM | PCM failure information for ACC system Accelerator pedal position (APP) sensor control state signal Brake pedal position switch signal Shift position status Transmission failure information for ACC system Vehicle speed signal for transmission

- PCM failure information for ACC system

- Accelerator pedal position (APP) sensor control state signal

- Brake pedal position switch signal

- Shift position status

- Transmission failure information for ACC system

- Vehicle speed signal for transmission

SRS unit | Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information Yaw rate sensor signal, Yaw rate sensor failure information

- Driver's seat belt buckle switch status, Driver's seat belt buckle switch failure information

- Longitudinal acceleration sensor signal, Longitudinal acceleration sensor failure information

- Yaw rate sensor signal, Yaw rate sensor failure information

VSA modulator-control unit | Brake control state signal Brake light relay failure information Electric parking brake status signal, Electric parking brake system failure information Master cylinder pressure signal, Master cylinder pressure sensor failure information VSA system failure information for ACC system Wheel speed sensor signals, Wheel speed sensor failure information

- Brake control state signal

- Brake light relay failure information

- Electric parking brake status signal, Electric parking brake system failure information

- Master cylinder pressure signal, Master cylinder pressure sensor failure information

- VSA system failure information for ACC system

- Wheel speed sensor signals, Wheel speed sensor failure information

Millimeter Wave Radar Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | ---

Gauge control module | ACC system failure information Buzzer request signal Customization information Multi information display (MID) screen requirement: ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC system failure information

- Buzzer request signal

- Customization information

- Multi information display (MID) screen requirement:

- ACC indicator ACC activation indicator ACC system indicates for self-diagnostic function

- ACC indicator

- ACC activation indicator

- ACC system indicates for self-diagnostic function

Multipurpose camera unit | Vehicle information

PCM | ACC system failure information Shift position down request signal Engine torque request

- ACC system failure information

- Shift position down request signal

- Engine torque request

SRS unit | ---

VSA modulator-control unit | Deceleration request ACC system failure information Electric parking brake actuation request signal Stop hold request

- Deceleration request

- ACC system failure information

- Electric parking brake actuation request signal

- Stop hold request
````

## Chunk 2399: Collision Mitigation Braking System (CMBS) Description - Overview (2019 2020 2021)

- Title: Collision Mitigation Braking System (CMBS) Description - Overview (2019 2020 2021)
- Source path: `pages\1211.html`
- Chunk ID: `chunk_c3262254aeef`
- Images: `images\GHH401760.jpeg`, `images\GHH401761.jpeg`
- Duplicate sources: `pages\16601.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - Overview (2019 2020 2021)

The CMBS can detect a possible collision and assists brake operation to reduce the impact on occupants and vehicle damage.

Courtesy of HONDA, U.S.A., INC.

CMBS Operation Sequence:

- When a speed difference between your vehicle and the leading vehicle or pedestrian in front of your vehicle is greater than 3 mph (5 km/h) and the system detects a possible collision, the system issues a warning message on the multi information display (MID) and sets an alarm off.

- When your vehicle is getting close to the leading vehicle or pedestrian ahead of your vehicle, the system issues a warning message on the MID and sets an alarm off to give the warning to the driver that there is a possible collision (First step).

- When your vehicle gets even closer to the leading vehicle or pedestrian ahead of your vehicle and the system anticipates a collision, the CMBS applies light braking force while issuing the MID warning and setting an alarm off (Second step).

- When the system determines that a collision is inevitable, the CMBS applies strong brake force while issuing the MID warning and setting an alarm off (Third step).

Courtesy of HONDA, U.S.A., INC.

- The multipurpose camera unit records the number of operations from vehicle ON mode to OFF (LOCK) mode. When the limit for the number of operations is exceeded, "excessive CMBS operation" is judged and the CMBS function is disabled. The warning indicator comes on and DTCs are stored. The limit for the number of operations differs according to the CMBS operation conditions.

- When the multipurpose camera is malfunctioning (including a temporary function stop), CMBS does not function.

Operation Conditions

Vehicle Ahead | Opposite Vehicle | Pedestrian

Conditions for the object | Passenger vehicles, subcompact, or large vehicle (The system may have difficulty recognizing two wheeled vehicles, like motorcycles, or other unusual body styles. The system will function as designed if the vehicles are detected.). | The system uses an analysis method using preprogrammed human figure patterns to detect pedestrians. (heights needs to be approximately 1.0-2.0 m (3.3-6.6 ft) for the system to recognize figures as pedestrians) Pedestrians behind the vehicle, and persons crossing the road: In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. The system may detect human-shaped signboards along the road as actual pedestrians depending on the shape and material.

- Pedestrians behind the vehicle, and persons crossing the road:

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. The system may detect human-shaped signboards along the road as actual pedestrians depending on the shape and material.

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running.

- The system may detect human-shaped signboards along the road as actual pedestrians depending on the shape and material.

System operation conditions | Operation vehicle speed | About 3 mph (5 km/h) or more | Between about 3 mph (5 km/h) and 62 mph (100 km/h).

Relative velocity | About 3 mph (5 km/h) or more | About 9 mph (15 km/h) or more | About 3 mph (5 km/h) or more

Environment conditions *1 | There is sufficient visibility and light available for the multipurpose camera to recognize objects In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

- There is sufficient visibility and light available for the multipurpose camera to recognize objects

- In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

*1: For more details on environmental conditions and objects that are hard to be recognized, please refer to the Owner's Manual.
````

## Chunk 2400: Collision Mitigation Braking System (CMBS) Description - Overview (2/4-door) (2016 2017 2018 2019)

- Title: Collision Mitigation Braking System (CMBS) Description - Overview (2/4-door) (2016 2017 2018 2019)
- Source path: `pages\1212.html`
- Chunk ID: `chunk_9bb61e12eff6`
- Images: `images\GHH401762.jpeg`, `images\GHH401763.jpeg`
- Duplicate sources: `pages\16519.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - Overview (2/4-door) (2016 2017 2018 2019)

The CMBS can detect a possible collision and assists brake operation to reduce the impact on occupants and vehicle damage.

Courtesy of HONDA, U.S.A., INC.

CMBS Operation Sequence:

- When a speed difference between your vehicle and the leading vehicle or the pedestrian in front of your vehicle is greater than 3 mph (5 km/h) and the system detects a possible collision, the system issues a warning message on the multi information display (MID) and sets an alarm off.

- When your vehicle is getting close to the leading vehicle or the pedestrian ahead of your vehicle, the system issues a warning message on the MID and sets an alarm off to give the warning to the driver that there is a possible collision (First step). For an opposite vehicle, the system vibrates the steering wheel to give an additional warning to the driver.

- When your vehicle gets even closer to the leading vehicle or the pedestrian ahead of your vehicle and the system anticipates a collision, the CMBS applies light braking force while issuing the MID warning and setting an alarm off (Second step).

- When the system determines that a collision is inevitable, the CMBS applies strong brake force while issuing the MID warning and setting an alarm off (Third step).

Courtesy of HONDA, U.S.A., INC.

- The braking force does not change whether the object is a pedestrian or a vehicle.

- The multipurpose camera unit records the number of operations from vehicle ON mode to OFF (LOCK) mode. When the limit for the number of operations is exceeded, "excessive CMBS operation" is judged and the CMBS function is disabled. The warning indicator comes on and DTCs are stored. The limit for the number of operations differs according to the CMBS operation conditions.

- When the multipurpose camera is malfunctioning (including a temporary function stop), CMBS does not function.

Operation Conditions

Vehicle Ahead | Opposite Vehicle | Pedestrian

Conditions for the object | Passenger vehicles, subcompact, or large vehicle (The system may have difficulty recognizing two wheeled vehicles, like motorcycles, or other unusual body styles. The system will function as designed if the vehicles are detected.). | Adult (judgment basically is by body height. Analysis is performed for compatibility with human patterns, which were programmed in advance), an analysis for children is performed when detection was successful. Pedestrians behind the vehicle, and persons crossing the road: In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. Depending on shape and material, human shaped posters and signs along the road may be detected.

- Pedestrians behind the vehicle, and persons crossing the road:

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. Depending on shape and material, human shaped posters and signs along the road may be detected.

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running.

- Depending on shape and material, human shaped posters and signs along the road may be detected.

System operation conditions | Operation vehicle speed | About 3 mph (5 km/h) or more | Between about 3 mph (5 km/h) and 62 mph (100 km/h).

Relative velocity | About 3 mph (5 km/h) or more | About 9 mph (15 km/h) or more | About 3 mph (5 km/h) or more

Environment conditions *1 | There is sufficient visibility and light available for the multipurpose camera to recognize objects In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

- There is sufficient visibility and light available for the multipurpose camera to recognize objects

- In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

*1: For more details on environmental conditions and objects that are hard to be recognized, please refer to the Owner's Manual. However, these are not selectable when the CMBS is turned OFF.
````

## Chunk 2401: Collision Mitigation Braking System (CMBS) Description - Overview (5-door) (2017 2018 2019)

- Title: Collision Mitigation Braking System (CMBS) Description - Overview (5-door) (2017 2018 2019)
- Source path: `pages\1213.html`
- Chunk ID: `chunk_07978c7914bc`
- Images: `images\GHH401764.jpeg`, `images\GHH401765.jpeg`
- Duplicate sources: `pages\16602.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - Overview (5-door) (2017 2018 2019)

The CMBS can detect a possible collision and assists brake operation to reduce the impact on occupants and vehicle damage.

Courtesy of HONDA, U.S.A., INC.

CMBS Operation Sequence:

- When a speed difference between your vehicle and the leading vehicle or the pedestrian in front of your vehicle is greater than 3 mph (5 km/h) and the system detects a possible collision, the system issues a warning message on the multi information display (MID) and sets an alarm off.

- When your vehicle is getting close to the leading vehicle or the pedestrian ahead of your vehicle, the system issues a warning message on the MID and sets an alarm off to give the warning to the driver that there is a possible collision (First step).

- When your vehicle gets even closer to the leading vehicle or the pedestrian ahead of your vehicle and the system anticipates a collision, the CMBS applies light braking force while issuing the MID warning and setting an alarm off (Second step).

- When the system determines that a collision is inevitable, the CMBS applies strong brake force while issuing the MID warning and setting an alarm off (Third step).

Courtesy of HONDA, U.S.A., INC.

- The multipurpose camera unit records the number of operations from vehicle ON mode to OFF (LOCK) mode. When the limit for the number of operations is exceeded, "excessive CMBS operation" is judged and the CMBS function is disabled. The warning indicator comes on and DTCs are stored. The limit for the number of operations differs according to the CMBS operation conditions.

- When the multipurpose camera is malfunctioning (including a temporary function stop), CMBS does not function.

Operation Conditions

Vehicle Ahead | Opposite Vehicle | Pedestrian

Conditions for the object | Passenger vehicles, subcompact, or large vehicle (The system may have difficulty recognizing two wheeled vehicles, like motorcycles, or other unusual body styles. The system will function as designed if the vehicles are detected.). | Adult (judgment basically is by body height. Analysis is performed for compatibility with human patterns, which were programmed in advance), an analysis for children is performed when detection was successful. Pedestrians behind the vehicle, and persons crossing the road: In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. Depending on shape and material, human shaped posters and signs along the road may be detected.

- Pedestrians behind the vehicle, and persons crossing the road:

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running. Depending on shape and material, human shaped posters and signs along the road may be detected.

- In some cases, persons crossing the road may not be detected if they jump out onto the road or are running.

- Depending on shape and material, human shaped posters and signs along the road may be detected.

System operation conditions | Operation vehicle speed | About 3 mph (5 km/h) or more | Between about 3 mph (5 km/h) and 62 mph (100 km/h).

Relative velocity | About 3 mph (5 km/h) or more | About 9 mph (15 km/h) or more | About 3 mph (5 km/h) or more

Environment conditions *1 | There is sufficient visibility and light available for the multipurpose camera to recognize objects In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

- There is sufficient visibility and light available for the multipurpose camera to recognize objects

- In environments where millimeter wave transmission/reception is not blocked (Some weather conditions such as fog, snowfall may have impact on system operation)

*1: For more details on environmental conditions and objects that are hard to be recognized, please refer to the Owner's Manual.
````

## Chunk 2402: Collision Mitigation Braking System (CMBS) Description - System Diagram (2019 2020 2021)

- Title: Collision Mitigation Braking System (CMBS) Description - System Diagram (2019 2020 2021)
- Source path: `pages\1214.html`
- Chunk ID: `chunk_1baffcab7d50`
- Images: `images\GHH401766.jpeg`
- Duplicate sources: `pages\16603.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - System Diagram (2019 2020 2021)

The system diagram of the CMBS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Millimeter Wave Radar Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle signal Steering angle neutral position learning information

- EPS system failure information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | CMBS OFF switch status information Gauge control module failure information Customized information

- CMBS OFF switch status information

- Gauge control module failure information

- Customized information

Multipurpose camera unit | Object recognition information Multipurpose camera unit failure information

- Object recognition information

- Multipurpose camera unit failure information

Originating Unit | Signal Name

PCM | Accelerator pedal position (APP) sensor signal Brake pedal position switch signal Shift position status Transmission failure information

- Accelerator pedal position (APP) sensor signal

- Brake pedal position switch signal

- Shift position status

- Transmission failure information

SRS unit | Yaw rate sensor signal Yaw rate sensor failure information Longitudinal acceleration sensor signal

- Yaw rate sensor signal

- Yaw rate sensor failure information

- Longitudinal acceleration sensor signal

VSA modulator-control unit | Master cylinder pressure signal VSA system actuation information VSA system failure information Wheel speed sensor signals

- Master cylinder pressure signal

- VSA system actuation information

- VSA system failure information

- Wheel speed sensor signals

Millimeter Wave Radar Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | ---

Gauge control module | Buzzer request signal CMBS status information Multi information display (MID) screen requirement: CMBS indicator CMBS indicates for self-diagnostic function Customized information

- Buzzer request signal

- CMBS status information

- Multi information display (MID) screen requirement:

- CMBS indicator CMBS indicates for self-diagnostic function Customized information

- CMBS indicator

- CMBS indicates for self-diagnostic function

- Customized information

Multipurpose camera unit | Vehicle information

SRS unit | CMBS operating information

VSA modulator-control unit | Automatic brake actuation request signal Brake light lighting control request signal CMBS failure information

- Automatic brake actuation request signal

- Brake light lighting control request signal

- CMBS failure information
````

## Chunk 2403: Collision Mitigation Braking System (CMBS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)

- Title: Collision Mitigation Braking System (CMBS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)
- Source path: `pages\1215.html`
- Chunk ID: `chunk_4b367e245f35`
- Images: `images\GHH401767.jpeg`
- Duplicate sources: `pages\16604.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)

The system diagram of the CMBS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Multipurpose camera unit

- SRS unit

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Multipurpose Camera Unit Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle signal Steering angle neutral position learning information

- EPS system failure information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | CMBS OFF switch status information Gauge control module failure information Customized information

- CMBS OFF switch status information

- Gauge control module failure information

- Customized information

Millimeter wave radar | Object recognition information Millimeter wave radar failure information

- Object recognition information

- Millimeter wave radar failure information

SRS unit | SRS system failure information Yaw rate sensor signal

- SRS system failure information

- Yaw rate sensor signal

VSA modulator-control unit | Master cylinder pressure signal VSA system failure information Wheel speed sensor signals

- Master cylinder pressure signal

- VSA system failure information

- Wheel speed sensor signals

Multipurpose Camera Unit Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | Steering wheel vibration request signal

- Steering wheel vibration request signal

Gauge control module | Buzzer request signal CMBS status information Multi information display (MID) screen requirement: CMBS indicator CMBS indicates for self-diagnostic function Customized information

- Buzzer request signal

- CMBS status information

- Multi information display (MID) screen requirement:

- CMBS indicator CMBS indicates for self-diagnostic function Customized information

- CMBS indicator

- CMBS indicates for self-diagnostic function

- Customized information

Millimeter wave radar | Vehicle information

SRS unit | CMBS operating information

VSA modulator-control unit | Automatic brake actuation request signal Brake light lighting control request signal CMBS failure information

- Automatic brake actuation request signal

- Brake light lighting control request signal

- CMBS failure information
````

## Chunk 2404: Collision Mitigation Braking System (CMBS) Description - System Diagram (5-door) (2017 2018 2019)

- Title: Collision Mitigation Braking System (CMBS) Description - System Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1216.html`
- Chunk ID: `chunk_2f3765d38ec0`
- Images: `images\GHH401768.jpeg`
- Duplicate sources: `pages\16605.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Description - System Diagram (5-door) (2017 2018 2019)

The system diagram of the CMBS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Millimeter Wave Radar Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle signal Steering angle neutral position learning information

- EPS system failure information

- Steering angle signal

- Steering angle neutral position learning information

Gauge control module | CMBS OFF switch status information Gauge control module failure information Customized information

- CMBS OFF switch status information

- Gauge control module failure information

- Customized information

Multipurpose camera unit | Object recognition information Multipurpose camera unit failure information

- Object recognition information

- Multipurpose camera unit failure information

Originating Unit | Signal Name

PCM | Accelerator pedal position (APP) sensor signal Brake pedal position switch signal Shift position status Transmission failure information

- Accelerator pedal position (APP) sensor signal

- Brake pedal position switch signal

- Shift position status

- Transmission failure information

SRS unit | Yaw rate sensor signal Yaw rate sensor failure information Longitudinal acceleration sensor signal

- Yaw rate sensor signal

- Yaw rate sensor failure information

- Longitudinal acceleration sensor signal

VSA modulator-control unit | Master cylinder pressure signal VSA system actuation information VSA system failure information Wheel speed sensor signals

- Master cylinder pressure signal

- VSA system actuation information

- VSA system failure information

- Wheel speed sensor signals

Millimeter Wave Radar Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | ---

Gauge control module | Buzzer request signal CMBS status information Multi information display (MID) screen requirement: CMBS indicator CMBS indicates for self-diagnostic function Customized information

- Buzzer request signal

- CMBS status information

- Multi information display (MID) screen requirement:

- CMBS indicator CMBS indicates for self-diagnostic function Customized information

- CMBS indicator

- CMBS indicates for self-diagnostic function

- Customized information

Multipurpose camera unit | Vehicle information

SRS unit | CMBS operating information

VSA modulator-control unit | Automatic brake actuation request signal Brake light lighting control request signal CMBS failure information

- Automatic brake actuation request signal

- Brake light lighting control request signal

- CMBS failure information
````

## Chunk 2405: Cruise Control System Description - Overview

- Title: Cruise Control System Description - Overview
- Source path: `pages\1217.html`
- Chunk ID: `chunk_2c01ee34dcae`
- Images: `images\GHH401769.jpeg`
- Duplicate sources: `pages\16606.html`

### Full Text

````text
# Cruise Control System Description - Overview

The cruise control system maintains a constant vehicle speed without operating the accelerator pedal.

Operation

To operate the cruise control system, the driver must first turn on the CRUISE/MAIN switch. With the CRUISE/MAIN switch on, the cruise main indicator appears in the gauge control module, and the gauge control module will send cruise control commands to the PCM via the F-CAN line.

The speed value is set at the moment the driver releases the SET button on the combination switch. Once the speed is set, the cruise control system maintains this speed in the system memory until: A new speed replaces the current value, the CRUISE/MAIN switch is turned off, the brake pedal is depressed, the clutch pedal (M/T) is depressed for more than five seconds, or the CANCEL button is pressed.

The driver can also increase and decrease the set speed by pressing the plus (+) and minus (-) buttons on the combination switch.

To maintain the set speed, the PCM monitors the throttle actuator position using the throttle position sensor and controls the speed by commanding the throttle actuator to open and close as needed.

The system changes its cruise control throttle inputs depending on whether the vehicle's ECON mode is on or off.

When the ECON mode is on, the system limits the throttle position to prevent excessive throttle application to improve fuel economy when there is a change in vehicle load - for example, it will take longer for the vehicle to accelerate to the set speed or applying throttle to maintain speed when climbing a hill. When the ECON mode is off, the vehicle will accelerate quicker to compensate for the change in vehicle load.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2406: Cruise Control System Description - System Diagram

- Title: Cruise Control System Description - System Diagram
- Source path: `pages\1218.html`
- Chunk ID: `chunk_8ff83f92180c`
- Images: `images\GHH401770.jpeg`, `images\GHH401771.jpeg`
- Duplicate sources: `pages\16607.html`

### Full Text

````text
# Cruise Control System Description - System Diagram

The system diagram of the cruise control system is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- Brake Pedal Position Switch

- Clutch pedal position switch A

- Cruise control combination switch

- Gauge control module

- PCM

- Throttle Body (Throttle Actuator, Throttle Position (TP) Sensor)

- Transmission control module (TCM), Transmission range switch, CVT speed sensor

- VSA modulator-control unit

M/T

Courtesy of HONDA, U.S.A., INC.

CVT

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2407: Lane Keeping Assist System (LKAS) Description - Overview

- Title: Lane Keeping Assist System (LKAS) Description - Overview
- Source path: `pages\1219.html`
- Chunk ID: `chunk_d8f96105bdba`
- Images: `images\GHH401772.jpeg`, `images\GHH401773.jpeg`, `images\GHH401774.jpeg`
- Duplicate sources: `pages\16608.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Description - Overview

Lane Keeping Assist System (LKAS)

The LKAS uses the multipurpose camera to read the lane lines on both sides of the road. The multipurpose camera unit draws an imaginary line at the center between both lane lines, and lane keeping assist control is performed by assisting the steering so that the vehicle is guided along this imaginary line near the center of the lane.

The system gets suspended when the system determines that the driver is not holding the steering wheel for a certain period of time while LKAS is in operation.

Courtesy of HONDA, U.S.A., INC.

LKAS Inoperative Road Conditions

LKAS does not operate in the following road conditions (LKAS is inoperative while LDW continues to operate).

Courtesy of HONDA, U.S.A., INC.

In case one side of lane mark is temporary missing

LKAS will continue to work even when one side of the lane mark is missing temporarily such as an intersection or a junction.

Courtesy of HONDA, U.S.A., INC.

Operation Conditions

System Operation Conditions | Operation under conditions where lane line recognition is possible on both sides (Lane line recognition may not be possible in bad weather, snow-covered roads, or areas with backlight).

Operation vehicle speed | 45 - 90 mph (72 - 145 km/h)

Object lane line types | Broken lines or solid lines on the road (white and yellow)

Driver operation | No operation when the driver's intent to act is recognized by movements of the steering wheel, accelerator pedal, brake pedal, turn signal switch, etc.

LKAS Cancel Alarm | When the LKAS system is canceled, a buzzer sounds (continuous "beep") to warn the driver. The alarm can be set ON/OFF.
````

## Chunk 2408: Lane Keeping Assist System (LKAS) Description - System Diagram (2019 2020 2021)

- Title: Lane Keeping Assist System (LKAS) Description - System Diagram (2019 2020 2021)
- Source path: `pages\1220.html`
- Chunk ID: `chunk_88906bfe673b`
- Images: `images\GHH401775.jpeg`
- Duplicate sources: `pages\16609.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Description - System Diagram (2019 2020 2021)

The system diagram of the LKAS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- VSA modulator-control unit

The LKAS for this vehicle uses the multipurpose camera unit to calculate camera image information, and sends the LKAS indicated value to the control unit via the millimeter wave radar.

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Multipurpose Camera Unit Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle neutral position learning information Steering angle signal Torque sensor signal

- EPS system failure information

- Steering angle neutral position learning information

- Steering angle signal

- Torque sensor signal

Originating Unit | Signal Name

Gauge control module | Customization signal MAIN switch signal LKAS switch signal Turn signal lights operating status Wiper operating status

- Customization signal

- MAIN switch signal

- LKAS switch signal

- Turn signal lights operating status

- Wiper operating status

PCM | Brake pedal position switch signal PCM failure information Vehicle speed signal

- Brake pedal position switch signal

- PCM failure information

- Vehicle speed signal

SRS unit | Yaw rate sensor signal Yaw rate sensor failure information

- Yaw rate sensor signal

- Yaw rate sensor failure information

VSA modulator-control unit | VSA system actuation information VSA system failure information Wheel speed sensor signals

- VSA system actuation information

- VSA system failure information

- Wheel speed sensor signals

Multipurpose Camera Unit Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | Integrated driver support system failure information LKAS control command

- Integrated driver support system failure information

- LKAS control command

Gauge control module | Buzzer request signal Customization information Integrated driver support system failure information Multi information display (MID) screen requirement: LKAS indicator LKAS activation indicator LKAS indicates for self-diagnostic function

- Buzzer request signal

- Customization information

- Integrated driver support system failure information

- Multi information display (MID) screen requirement:

- LKAS indicator LKAS activation indicator LKAS indicates for self-diagnostic function

- LKAS indicator

- LKAS activation indicator

- LKAS indicates for self-diagnostic function

PCM | ---

SRS unit | ---

VSA modulator-control unit | ---
````

## Chunk 2409: Lane Keeping Assist System (LKAS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)

- Title: Lane Keeping Assist System (LKAS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)
- Source path: `pages\1221.html`
- Chunk ID: `chunk_149f04724641`
- Images: `images\GHH401776.jpeg`
- Duplicate sources: `pages\16610.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Description - System Diagram (2/4-door) (2016 2017 2018 2019)

The system diagram of the LKAS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Multipurpose camera unit

- PCM

- SRS unit

- VSA modulator-control unit

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Multipurpose Camera Unit Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle neutral position learning information Steering angle signal Torque sensor signal

- EPS system failure information

- Steering angle neutral position learning information

- Steering angle signal

- Torque sensor signal

Gauge control module | Customization signal MAIN switch signal LKAS switch signal

- Customization signal

- MAIN switch signal

- LKAS switch signal

PCM | Brake pedal position switch signal PCM failure information Vehicle speed signal

- Brake pedal position switch signal

- PCM failure information

- Vehicle speed signal

SRS unit | Yaw rate sensor signal Yaw rate sensor failure information

- Yaw rate sensor signal

- Yaw rate sensor failure information

Originating Unit | Signal Name

VSA modulator-control unit | VSA system actuation information VSA system failure information Wheel speed sensor signals

- VSA system actuation information

- VSA system failure information

- Wheel speed sensor signals

Multipurpose Camera Unit Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | Integrated driver support system failure information LKAS control command

- Integrated driver support system failure information

- LKAS control command

Gauge control module | Customization information Integrated driver support system failure information Multi information display (MID) screen requirement: LKAS indicator LKAS activation indicator LKAS system indicates for self-diagnostic function

- Customization information

- Integrated driver support system failure information

- Multi information display (MID) screen requirement:

- LKAS indicator LKAS activation indicator LKAS system indicates for self-diagnostic function

- LKAS indicator

- LKAS activation indicator

- LKAS system indicates for self-diagnostic function

PCM | ---

SRS unit | ---

VSA modulator-control unit | ---
````

## Chunk 2410: Lane Keeping Assist System (LKAS) Description - System Diagram (5-door) (2017 2018 2019)

- Title: Lane Keeping Assist System (LKAS) Description - System Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1222.html`
- Chunk ID: `chunk_1500243152a7`
- Images: `images\GHH401777.jpeg`
- Duplicate sources: `pages\16611.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Description - System Diagram (5-door) (2017 2018 2019)

The system diagram of the LKAS is shown below.

For locations of each component on vehicle, refer to Component Location Index:

- EPS motor/control unit

- Gauge control module

- Millimeter wave radar

- Multipurpose camera unit

- PCM

- SRS unit

- VSA modulator-control unit

The LKAS for this vehicle uses the multipurpose camera unit to calculate camera image information, and sends the LKAS indicated value to the control unit via the millimeter wave radar.

Courtesy of HONDA, U.S.A., INC.

F-CAN Communication Data

Multipurpose Camera Unit Receiving Signal:

Originating Unit | Signal Name

EPS motor/control unit | EPS system failure information Steering angle neutral position learning information Steering angle signal Torque sensor signal

- EPS system failure information

- Steering angle neutral position learning information

- Steering angle signal

- Torque sensor signal

Originating Unit | Signal Name

Gauge control module | Customization signal MAIN switch signal LKAS switch signal Turn signal lights operating status Wiper operating status

- Customization signal

- MAIN switch signal

- LKAS switch signal

- Turn signal lights operating status

- Wiper operating status

PCM | Brake pedal position switch signal PCM failure information Vehicle speed signal

- Brake pedal position switch signal

- PCM failure information

- Vehicle speed signal

SRS unit | Yaw rate sensor signal Yaw rate sensor failure information

- Yaw rate sensor signal

- Yaw rate sensor failure information

VSA modulator-control unit | VSA system actuation information VSA system failure information Wheel speed sensor signals

- VSA system actuation information

- VSA system failure information

- Wheel speed sensor signals

Multipurpose Camera Unit Transmitting Signal:

Destination Unit | Signal Name

EPS motor/control unit | Integrated driver support system failure information LKAS control command

- Integrated driver support system failure information

- LKAS control command

Gauge control module | Buzzer request signal Customization information Integrated driver support system failure information Multi information display (MID) screen requirement: LKAS indicator LKAS activation indicator LKAS indicates for self-diagnostic function

- Buzzer request signal

- Customization information

- Integrated driver support system failure information

- Multi information display (MID) screen requirement:

- LKAS indicator LKAS activation indicator LKAS indicates for self-diagnostic function

- LKAS indicator

- LKAS activation indicator

- LKAS indicates for self-diagnostic function

PCM | ---

SRS unit | ---

VSA modulator-control unit | ---
````

## Chunk 2411: ACC OFF is displayed on the MID unexpectedly (Adaptive Cruise Control (ACC))

- Title: ACC OFF is displayed on the MID unexpectedly (Adaptive Cruise Control (ACC))
- Source path: `pages\1223.html`
- Chunk ID: `chunk_a646de63f375`
- Images: none
- Duplicate sources: `pages\16612.html`

### Full Text

````text
# ACC OFF is displayed on the MID unexpectedly (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Check the ACC system auto stop control history .
````

## Chunk 2412: ACC activation indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))

- Title: ACC activation indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))
- Source path: `pages\1224.html`
- Chunk ID: `chunk_f8a3e46e2bb8`
- Images: none
- Duplicate sources: `pages\16613.html`

### Full Text

````text
# ACC activation indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2413: ACC activation indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))

- Title: ACC activation indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))
- Source path: `pages\1225.html`
- Chunk ID: `chunk_76fe98e3710a`
- Images: none
- Duplicate sources: `pages\16614.html`

### Full Text

````text
# ACC activation indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2414: ACC indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))

- Title: ACC indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))
- Source path: `pages\1226.html`
- Chunk ID: `chunk_968162463bd6`
- Images: none
- Duplicate sources: `pages\16615.html`

### Full Text

````text
# ACC indicator (on the MID) does not come on (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2415: ACC indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))

- Title: ACC indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))
- Source path: `pages\1227.html`
- Chunk ID: `chunk_4e2e4114d28d`
- Images: none
- Duplicate sources: `pages\16616.html`

### Full Text

````text
# ACC indicator (on the MID) does not go off (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2416: CMBS OFF switch does not turn On/turn Off (CMBS indicator does not change) (Collision Mitigation Braking System (CMBS))

- Title: CMBS OFF switch does not turn On/turn Off (CMBS indicator does not change) (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1228.html`
- Chunk ID: `chunk_0f84434d0423`
- Images: none
- Duplicate sources: `pages\16617.html`

### Full Text

````text
# CMBS OFF switch does not turn On/turn Off (CMBS indicator does not change) (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .

- Test the CMBS OFF switch .

Also check for

- An open or increased resistance in the wire

- A short in the wire
````

## Chunk 2417: CMBS indicator (on the MID) does not go off (Collision Mitigation Braking System (CMBS))

- Title: CMBS indicator (on the MID) does not go off (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1229.html`
- Chunk ID: `chunk_aac4bedd20cd`
- Images: none
- Duplicate sources: `pages\16618.html`

### Full Text

````text
# CMBS indicator (on the MID) does not go off (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2418: CMBS indicator does not come on (Collision Mitigation Braking System (CMBS))

- Title: CMBS indicator does not come on (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1230.html`
- Chunk ID: `chunk_03233a2f2833`
- Images: none
- Duplicate sources: `pages\16619.html`

### Full Text

````text
# CMBS indicator does not come on (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .
````

## Chunk 2419: Cruise control can be set, but the cruise control indicator does not come on (Cruise Control)

- Title: Cruise control can be set, but the cruise control indicator does not come on (Cruise Control)
- Source path: `pages\1231.html`
- Chunk ID: `chunk_72215b1f37f8`
- Images: none
- Duplicate sources: `pages\16620.html`

### Full Text

````text
# Cruise control can be set, but the cruise control indicator does not come on (Cruise Control)

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .

- Do the cruise control input test . Test the cruise control indicator signal input.

- Check the PGM-FI system .

Also check for

Faulty gauge control module
````

## Chunk 2420: Cruise control can be set, but the cruise main indicator does not come on (Cruise Control)

- Title: Cruise control can be set, but the cruise main indicator does not come on (Cruise Control)
- Source path: `pages\1232.html`
- Chunk ID: `chunk_3ee017f0d8f9`
- Images: none
- Duplicate sources: `pages\16621.html`

### Full Text

````text
# Cruise control can be set, but the cruise main indicator does not come on (Cruise Control)

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .

- Do the cruise control input test . Test the cruise main indicator signal input.

- Check the PGM-FI system .

Also check for

Faulty gauge control module
````

## Chunk 2421: Cruise control cannot be set (Cruise Control)

- Title: Cruise control cannot be set (Cruise Control)
- Source path: `pages\1233.html`
- Chunk ID: `chunk_a5a96987dbe1`
- Images: none
- Duplicate sources: `pages\16622.html`

### Full Text

````text
# Cruise control cannot be set (Cruise Control)

Diagnostic procedure

- Check the PGM-FI system .

- Check the No. B21 (10 A) fuse in the under-dash fuse/relay box.

- Do the cruise control combination switch test .

- Do the cruise control input test .

Also check for

- Open circuit, loose or disconnected terminals: GRN, TAN, GRY, or LT GRN wire between the cruise control combination switch and the gauge control module

- Faulty gauge control module

- Faulty cable reel
````

## Chunk 2422: Does not sense the vehicle driving ahead (Adaptive Cruise Control (ACC))

- Title: Does not sense the vehicle driving ahead (Adaptive Cruise Control (ACC))
- Source path: `pages\1234.html`
- Chunk ID: `chunk_1cd4e48d652a`
- Images: none
- Duplicate sources: `pages\16623.html`

### Full Text

````text
# Does not sense the vehicle driving ahead (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .

Also check for

- Out of the performance limits

- Wheel alignment

- Undetectable environment
````

## Chunk 2423: Intermittently senses the vehicle driving ahead (Adaptive Cruise Control (ACC))

- Title: Intermittently senses the vehicle driving ahead (Adaptive Cruise Control (ACC))
- Source path: `pages\1235.html`
- Chunk ID: `chunk_0ae4de205082`
- Images: none
- Duplicate sources: `pages\16624.html`

### Full Text

````text
# Intermittently senses the vehicle driving ahead (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .

Also check for

- Incorrect millimeter wave radar installation

- Wheel alignment

- Undetectable environment
````

## Chunk 2424: LKAS activation indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))

- Title: LKAS activation indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))
- Source path: `pages\1236.html`
- Chunk ID: `chunk_25157cc1ebe7`
- Images: none
- Duplicate sources: `pages\16625.html`

### Full Text

````text
# LKAS activation indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2425: LKAS activation indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))

- Title: LKAS activation indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))
- Source path: `pages\1237.html`
- Chunk ID: `chunk_b2a3b45577a7`
- Images: none
- Duplicate sources: `pages\16626.html`

### Full Text

````text
# LKAS activation indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2426: LKAS indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))

- Title: LKAS indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))
- Source path: `pages\1238.html`
- Chunk ID: `chunk_0a798acaa01f`
- Images: none
- Duplicate sources: `pages\16627.html`

### Full Text

````text
# LKAS indicator (on the MID) does not come on (Lane Keeping Assist System (LKAS))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2427: LKAS indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))

- Title: LKAS indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))
- Source path: `pages\1239.html`
- Chunk ID: `chunk_e3df27eaf9af`
- Images: none
- Duplicate sources: `pages\16628.html`

### Full Text

````text
# LKAS indicator (on the MID) does not go off (Lane Keeping Assist System (LKAS))

Diagnostic procedure

- Symptom troubleshooting .
````

## Chunk 2428: Senses a vehicle driving in another lane (Adaptive Cruise Control (ACC))

- Title: Senses a vehicle driving in another lane (Adaptive Cruise Control (ACC))
- Source path: `pages\1240.html`
- Chunk ID: `chunk_9c22bdc39400`
- Images: none
- Duplicate sources: `pages\16629.html`

### Full Text

````text
# Senses a vehicle driving in another lane (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Symptom troubleshooting .

Also check for

- Incorrect millimeter wave radar installation

- Wheel alignment
````

## Chunk 2429: Set distance cannot be adjusted with the distance switch (Adaptive Cruise Control (ACC))

- Title: Set distance cannot be adjusted with the distance switch (Adaptive Cruise Control (ACC))
- Source path: `pages\1241.html`
- Chunk ID: `chunk_637abb1e3eb2`
- Images: none
- Duplicate sources: `pages\16630.html`

### Full Text

````text
# Set distance cannot be adjusted with the distance switch (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Test the distance switch .
````

## Chunk 2430: Set speed does not cancel (engine RPM stays high) when the clutch pedal is pressed for more than five seconds (M/T) (Cruise Control)

- Title: Set speed does not cancel (engine RPM stays high) when the clutch pedal is pressed for more than five seconds (M/T) (Cruise Control)
- Source path: `pages\1242.html`
- Chunk ID: `chunk_4cdd68e95508`
- Images: none
- Duplicate sources: `pages\16631.html`

### Full Text

````text
# Set speed does not cancel (engine RPM stays high) when the clutch pedal is pressed for more than five seconds (M/T) (Cruise Control)

Diagnostic procedure

- Do the cruise control input test . Test the CANCEL switch signal input.

- Test clutch pedal position switch A .

- Check for DTCs in the VSA system with the HDS .

Also check for

- Faulty clutch pedal position switch A

- An open in the wire between the PCM and clutch pedal position switch A

- A wire shorted to ground or power between the PCM and clutch pedal position switch A

- Faulty clutch pedal stroke sensor
````

## Chunk 2431: Set speed does not cancel when the CANCEL button is pressed (Cruise Control)

- Title: Set speed does not cancel when the CANCEL button is pressed (Cruise Control)
- Source path: `pages\1243.html`
- Chunk ID: `chunk_309590b5f22e`
- Images: none
- Duplicate sources: `pages\16632.html`

### Full Text

````text
# Set speed does not cancel when the CANCEL button is pressed (Cruise Control)

Diagnostic procedure

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the CANCEL switch signal input.

- Check the PGM-FI system .
````

## Chunk 2432: Set speed does not cancel when the CRUISE button is pressed (Cruise Control)

- Title: Set speed does not cancel when the CRUISE button is pressed (Cruise Control)
- Source path: `pages\1244.html`
- Chunk ID: `chunk_c7972cd4dce1`
- Images: none
- Duplicate sources: `pages\16633.html`

### Full Text

````text
# Set speed does not cancel when the CRUISE button is pressed (Cruise Control)

Diagnostic procedure

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the CRUISE switch signal input.

- Check the PGM-FI system .
````

## Chunk 2433: Set speed does not cancel when the MAIN switch is turned off (Adaptive Cruise Control (ACC))

- Title: Set speed does not cancel when the MAIN switch is turned off (Adaptive Cruise Control (ACC))
- Source path: `pages\1245.html`
- Chunk ID: `chunk_37ade8a1ed0a`
- Images: none
- Duplicate sources: `pages\16634.html`

### Full Text

````text
# Set speed does not cancel when the MAIN switch is turned off (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Test the ACC combination switch .

Also check for

An open in the wire
````

## Chunk 2434: Set speed does not cancel when the brake pedal is pressed (Adaptive Cruise Control (ACC))

- Title: Set speed does not cancel when the brake pedal is pressed (Adaptive Cruise Control (ACC))
- Source path: `pages\1246.html`
- Chunk ID: `chunk_663eacc27066`
- Images: none
- Duplicate sources: `pages\16635.html`

### Full Text

````text
# Set speed does not cancel when the brake pedal is pressed (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Test the brake pedal position switch .

Also check for

An open in the wire
````

## Chunk 2435: Set speed does not cancel when the brake pedal is pressed (Cruise Control)

- Title: Set speed does not cancel when the brake pedal is pressed (Cruise Control)
- Source path: `pages\1247.html`
- Chunk ID: `chunk_aa5de8906bfc`
- Images: none
- Duplicate sources: `pages\16636.html`

### Full Text

````text
# Set speed does not cancel when the brake pedal is pressed (Cruise Control)

Diagnostic procedure

- Do the brake pedal position switch test .

- Do the cruise control input test . Test the brake pedal position switch signal input.

- Check the PGM-FI system .

Also check for

- Faulty brake pedal position switch

- An open in the wire between the PCM and the brake pedal position switch

- A wire shorted to ground or power between the PCM and the brake pedal position switch
````

## Chunk 2436: Set speed does not resume when the RES+ button is pressed (with the CRUISE button pressed on, and set speed temporarily canceled by pressing the brake pedal) (Cruise Control)

- Title: Set speed does not resume when the RES+ button is pressed (with the CRUISE button pressed on, and set speed temporarily canceled by pressing the brake pedal) (Cruise Control)
- Source path: `pages\1248.html`
- Chunk ID: `chunk_a7d48a7493f4`
- Images: none
- Duplicate sources: `pages\16637.html`

### Full Text

````text
# Set speed does not resume when the RES+ button is pressed (with the CRUISE button pressed on, and set speed temporarily canceled by pressing the brake pedal) (Cruise Control)

Diagnostic procedure

- Check the PGM-FI system .

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the RES+ switch signal input.
````

## Chunk 2437: The CMBS did not operate (Collision Mitigation Braking System (CMBS))

- Title: The CMBS did not operate (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1249.html`
- Chunk ID: `chunk_8910fd830466`
- Images: none
- Duplicate sources: `pages\16638.html`

### Full Text

````text
# The CMBS did not operate (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Check the millimeter wave radar installation .

- Check the wheel alignment .

Also check for

- Driving conditions, weather, environmental influences

- Undetectable environment
````

## Chunk 2438: The CMBS operated without danger of collision (Collision Mitigation Braking System (CMBS))

- Title: The CMBS operated without danger of collision (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1250.html`
- Chunk ID: `chunk_7e60ce15f619`
- Images: none
- Duplicate sources: `pages\16639.html`

### Full Text

````text
# The CMBS operated without danger of collision (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Check the millimeter wave radar installation .

- Check the wheel alignment .

Also check for

Driving conditions, weather, environmental influence
````

## Chunk 2439: The CMBS operates frequently (Collision Mitigation Braking System (CMBS))

- Title: The CMBS operates frequently (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1251.html`
- Chunk ID: `chunk_c80694cfe2cc`
- Images: none
- Duplicate sources: `pages\16640.html`

### Full Text

````text
# The CMBS operates frequently (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Check the millimeter wave radar installation .

- Check the wheel alignment .

Also check for

Driving conditions, weather, environmental influence
````

## Chunk 2440: The MID does not indicate when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))

- Title: The MID does not indicate when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1252.html`
- Chunk ID: `chunk_1e6b4f1d24ca`
- Images: none
- Duplicate sources: `pages\16641.html`

### Full Text

````text
# The MID does not indicate when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .

- Test the CMBS OFF switch .

Also check for

- An open or increased resistance in the wire

- A short in the wire
````

## Chunk 2441: The buzzer does not sound when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))

- Title: The buzzer does not sound when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1253.html`
- Chunk ID: `chunk_83a2204564fc`
- Images: none
- Duplicate sources: `pages\16642.html`

### Full Text

````text
# The buzzer does not sound when the CMBS OFF switch is operated (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .
````

## Chunk 2442: The buzzer does not sound (Collision Mitigation Braking System (CMBS))

- Title: The buzzer does not sound (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1254.html`
- Chunk ID: `chunk_0054cd2297a7`
- Images: none
- Duplicate sources: `pages\16643.html`

### Full Text

````text
# The buzzer does not sound (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .
````

## Chunk 2443: Though CMBS operates, the information is not displayed on the MID (Collision Mitigation Braking System (CMBS))

- Title: Though CMBS operates, the information is not displayed on the MID (Collision Mitigation Braking System (CMBS))
- Source path: `pages\1255.html`
- Chunk ID: `chunk_cd2209c5a972`
- Images: none
- Duplicate sources: `pages\16644.html`

### Full Text

````text
# Though CMBS operates, the information is not displayed on the MID (Collision Mitigation Braking System (CMBS))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .
````

## Chunk 2444: Vehicle does not accelerate accordingly when the RES+ button is pressed (Cruise Control)

- Title: Vehicle does not accelerate accordingly when the RES+ button is pressed (Cruise Control)
- Source path: `pages\1256.html`
- Chunk ID: `chunk_4437ed87e432`
- Images: none
- Duplicate sources: `pages\16645.html`

### Full Text

````text
# Vehicle does not accelerate accordingly when the RES+ button is pressed (Cruise Control)

Diagnostic procedure

- Do the cruise control combination switch test .

- Do the cruise control input test . Test the RES/+ switch signal input.

- Check the PGM-FI system .
````

## Chunk 2445: Vehicle does not decelerate or accelerate accordingly when the SET or RES switch is pressed (Adaptive Cruise Control (ACC))

- Title: Vehicle does not decelerate or accelerate accordingly when the SET or RES switch is pressed (Adaptive Cruise Control (ACC))
- Source path: `pages\1257.html`
- Chunk ID: `chunk_d1bfdb982821`
- Images: none
- Duplicate sources: `pages\16646.html`

### Full Text

````text
# Vehicle does not decelerate or accelerate accordingly when the SET or RES switch is pressed (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Test the ACC combination switch .

Also check for

An open in the wire
````

## Chunk 2446: Vehicle speed can be set, but there is no ACC indication on the MID (Adaptive Cruise Control (ACC))

- Title: Vehicle speed can be set, but there is no ACC indication on the MID (Adaptive Cruise Control (ACC))
- Source path: `pages\1258.html`
- Chunk ID: `chunk_577855623973`
- Images: none
- Duplicate sources: `pages\16647.html`

### Full Text

````text
# Vehicle speed can be set, but there is no ACC indication on the MID (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Do the gauge control module self-diagnostic function procedure .
````

## Chunk 2447: Vehicle speed can be set, but vehicle decelerates (Adaptive Cruise Control (ACC))

- Title: Vehicle speed can be set, but vehicle decelerates (Adaptive Cruise Control (ACC))
- Source path: `pages\1259.html`
- Chunk ID: `chunk_d90322d70c04`
- Images: none
- Duplicate sources: `pages\16648.html`

### Full Text

````text
# Vehicle speed can be set, but vehicle decelerates (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Check for DTCs in the PGM-FI system with the HDS .

Also check for

Faulty ETCS
````

## Chunk 2448: Vehicle speed cannot be set when the SET switch is pressed between the 25 mph (40 km/h) and 90 mph (145 km/h) (Adaptive Cruise Control (ACC))

- Title: Vehicle speed cannot be set when the SET switch is pressed between the 25 mph (40 km/h) and 90 mph (145 km/h) (Adaptive Cruise Control (ACC))
- Source path: `pages\1260.html`
- Chunk ID: `chunk_290ee346a9f7`
- Images: none
- Duplicate sources: `pages\16649.html`

### Full Text

````text
# Vehicle speed cannot be set when the SET switch is pressed between the 25 mph (40 km/h) and 90 mph (145 km/h) (Adaptive Cruise Control (ACC))

Diagnostic procedure

- Test the ACC combination switch .

- Test the brake pedal position switch .

Also check for

- An open in the wire

- A short in the wire

- The system is in service mode
````

## Chunk 2449: Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2016 2017 2018)

- Title: Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2016 2017 2018)
- Source path: `pages\1261.html`
- Chunk ID: `chunk_8de5a758e3b4`
- Images: `images\GHH401778.jpeg`, `images\GHH401779.jpeg`, `images\GHH401780.jpeg`, `images\GHH401781.jpeg`
- Duplicate sources: `pages\16650.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2016 2017 2018)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2450: Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2019 2020 2021)

- Title: Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2019 2020 2021)
- Source path: `pages\1262.html`
- Chunk ID: `chunk_73d00f901db0`
- Images: `images\GHH401782.jpeg`, `images\GHH401783.jpeg`, `images\GHH401784.jpeg`, `images\GHH401785.jpeg`
- Duplicate sources: `pages\16651.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Circuit Diagram (2/4-door) (2019 2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2451: Adaptive Cruise Control (ACC) Circuit Diagram (4-door, Japan Production) (2018)

- Title: Adaptive Cruise Control (ACC) Circuit Diagram (4-door, Japan Production) (2018)
- Source path: `pages\1263.html`
- Chunk ID: `chunk_5d973931b0a0`
- Images: `images\GHH401786.jpeg`, `images\GHH401787.jpeg`
- Duplicate sources: `pages\16652.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Circuit Diagram (4-door, Japan Production) (2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2452: Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2017 2018 2019)

- Title: Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1264.html`
- Chunk ID: `chunk_447e21a8edce`
- Images: `images\GHH401788.jpeg`, `images\GHH401789.jpeg`, `images\GHH401790.jpeg`, `images\GHH401791.jpeg`
- Duplicate sources: `pages\16653.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2017 2018 2019)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2453: Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2020 2021)

- Title: Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2020 2021)
- Source path: `pages\1265.html`
- Chunk ID: `chunk_20f07972820d`
- Images: `images\GHH401792.jpeg`, `images\GHH401793.jpeg`, `images\GHH401794.jpeg`, `images\GHH401795.jpeg`
- Duplicate sources: `pages\16654.html`

### Full Text

````text
# Adaptive Cruise Control (ACC) Circuit Diagram (5-door) (2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2454: Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2016 2017 2018)

- Title: Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2016 2017 2018)
- Source path: `pages\1266.html`
- Chunk ID: `chunk_b298b3779785`
- Images: `images\GHH401796.jpeg`, `images\GHH401797.jpeg`, `images\GHH401798.jpeg`, `images\GHH401799.jpeg`
- Duplicate sources: `pages\16655.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2016 2017 2018)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2455: Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2019 2020 2021)

- Title: Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2019 2020 2021)
- Source path: `pages\1267.html`
- Chunk ID: `chunk_7e8322aac8ae`
- Images: `images\GHH401800.jpeg`, `images\GHH401801.jpeg`, `images\GHH401802.jpeg`, `images\GHH401803.jpeg`
- Duplicate sources: `pages\16656.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Circuit Diagram (2/4-door) (2019 2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2456: Collision Mitigation Braking System (CMBS) Circuit Diagram (4-door, Japan Production) (2018)

- Title: Collision Mitigation Braking System (CMBS) Circuit Diagram (4-door, Japan Production) (2018)
- Source path: `pages\1268.html`
- Chunk ID: `chunk_70113a9d8d14`
- Images: `images\GHH401804.jpeg`, `images\GHH401805.jpeg`
- Duplicate sources: `pages\16657.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Circuit Diagram (4-door, Japan Production) (2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2457: Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2017 2018 2019)

- Title: Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1269.html`
- Chunk ID: `chunk_44e7fa98b0b7`
- Images: `images\GHH401806.jpeg`, `images\GHH401807.jpeg`, `images\GHH401808.jpeg`, `images\GHH401809.jpeg`
- Duplicate sources: `pages\16658.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2017 2018 2019)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2458: Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2020 2021)

- Title: Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2020 2021)
- Source path: `pages\1270.html`
- Chunk ID: `chunk_3ce92a21d313`
- Images: `images\GHH401810.jpeg`, `images\GHH401811.jpeg`, `images\GHH401812.jpeg`, `images\GHH401813.jpeg`
- Duplicate sources: `pages\16659.html`

### Full Text

````text
# Collision Mitigation Braking System (CMBS) Circuit Diagram (5-door) (2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2459: Cruise Control Circuit Diagram (2017 2018 2019 2020 2021)

- Title: Cruise Control Circuit Diagram (2017 2018 2019 2020 2021)
- Source path: `pages\1271.html`
- Chunk ID: `chunk_ebf17d92b719`
- Images: `images\GHH401814.jpeg`, `images\GHH401815.jpeg`
- Duplicate sources: `pages\16660.html`

### Full Text

````text
# Cruise Control Circuit Diagram (2017 2018 2019 2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2460: Cruise Control Circuit Diagram (2/4-door, Except Si) (2016 2017 2018)

- Title: Cruise Control Circuit Diagram (2/4-door, Except Si) (2016 2017 2018)
- Source path: `pages\1272.html`
- Chunk ID: `chunk_2157789c838b`
- Images: `images\GHH401816.jpeg`, `images\GHH401817.jpeg`
- Duplicate sources: `pages\16661.html`

### Full Text

````text
# Cruise Control Circuit Diagram (2/4-door, Except Si) (2016 2017 2018)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2461: Cruise Control Circuit Diagram (Type-R/Si) (2017 2018 2019 2020 2021)

- Title: Cruise Control Circuit Diagram (Type-R/Si) (2017 2018 2019 2020 2021)
- Source path: `pages\1274.html`
- Chunk ID: `chunk_25855a0c03f1`
- Images: `images\GHH401819.jpeg`, `images\GHH401820.jpeg`
- Duplicate sources: `pages\16663.html`

### Full Text

````text
# Cruise Control Circuit Diagram (Type-R/Si) (2017 2018 2019 2020 2021)

Si

Courtesy of HONDA, U.S.A., INC.

Type-R

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2462: Lane Keeping Assist System (LKAS) Circuit Diagram (2016 2017 2018)

- Title: Lane Keeping Assist System (LKAS) Circuit Diagram (2016 2017 2018)
- Source path: `pages\1275.html`
- Chunk ID: `chunk_6d2664b85f3f`
- Images: `images\GHH401821.jpeg`, `images\GHH401822.jpeg`, `images\GHH401823.jpeg`, `images\GHH401824.jpeg`
- Duplicate sources: `pages\16664.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Circuit Diagram (2016 2017 2018)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2463: Lane Keeping Assist System (LKAS) Circuit Diagram (2/4-door) (2019 2020 2021)

- Title: Lane Keeping Assist System (LKAS) Circuit Diagram (2/4-door) (2019 2020 2021)
- Source path: `pages\1276.html`
- Chunk ID: `chunk_84ac0cdf741c`
- Images: `images\GHH401825.jpeg`, `images\GHH401826.jpeg`, `images\GHH401827.jpeg`, `images\GHH401828.jpeg`
- Duplicate sources: `pages\16665.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Circuit Diagram (2/4-door) (2019 2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2464: Lane Keeping Assist System (LKAS) Circuit Diagram (4-door, Japan Production) (2018)

- Title: Lane Keeping Assist System (LKAS) Circuit Diagram (4-door, Japan Production) (2018)
- Source path: `pages\1277.html`
- Chunk ID: `chunk_f3661804b47c`
- Images: `images\GHH401829.jpeg`, `images\GHH401830.jpeg`
- Duplicate sources: `pages\16666.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Circuit Diagram (4-door, Japan Production) (2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2465: Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2017 2018 2019)

- Title: Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2017 2018 2019)
- Source path: `pages\1278.html`
- Chunk ID: `chunk_6341ea8f39d9`
- Images: `images\GHH401831.jpeg`, `images\GHH401832.jpeg`, `images\GHH401833.jpeg`, `images\GHH401834.jpeg`
- Duplicate sources: `pages\16667.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2017 2018 2019)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2466: Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2020 2021)

- Title: Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2020 2021)
- Source path: `pages\1279.html`
- Chunk ID: `chunk_c14dd943f416`
- Images: `images\GHH401835.jpeg`, `images\GHH401836.jpeg`, `images\GHH401837.jpeg`, `images\GHH401838.jpeg`
- Duplicate sources: `pages\16668.html`

### Full Text

````text
# Lane Keeping Assist System (LKAS) Circuit Diagram (5-door) (2020 2021)

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

Without keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.

With keyless access system

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2467: Active Sound Control Unit Connector for Inputs and Outputs

- Title: Active Sound Control Unit Connector for Inputs and Outputs
- Source path: `pages\1440.html`
- Chunk ID: `chunk_ff3ca9f97ae8`
- Images: `images\GHH399534.jpeg`
- Duplicate sources: `pages\1890.html`, `pages\25959.html`, `pages\13342.html`

### Full Text

````text
# Active Sound Control Unit Connector for Inputs and Outputs

Active Sound Control Unit 20P Connector (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

1 | GND | Ground for active sound control unit (G505)

2 | Not used | ---

3 | SWD+B | Inputs signal for active sound control unit switching on/off

4 | F-CAN C_H | Communication signal

5 | F-CAN C_L | Communication signal

6 | Not used | ---

7 | SH ANC F MIC | Shield for terminal No. 18

8 | ANC SH | Shield for terminals No. 9, No. 10, No. 19, and No. 20

9 | ANC R- *1 | Not used

ANC R- *2 | Outputs signal for acceleration sound enhancement

10 | ANC F- | Outputs signal for acceleration sound enhancement

11 | +B BACK UP | Continuous power source

12 | IG1 METER | IG1 power source

13 | Not used | ---

14 | K LINE | Detects scan tool signal (serial data)

15 | Not used | ---

16 | Not used | ---

17 | Not used | ---

18 | ANC F MIC+8V | Inputs sound signal from HFL microphone

19 | ANC R+ *1 | Not used

ANC R+ *2 | Outputs signal for acceleration sound enhancement

20 | ANC F+ | Outputs signal for acceleration sound enhancement

*1: 2-door

*2: Except 2-door
````

## Chunk 2468: Audio Remote-HFL Switch Connector for Inputs and Outputs

- Title: Audio Remote-HFL Switch Connector for Inputs and Outputs
- Source path: `pages\1441.html`
- Chunk ID: `chunk_e8b688c0a074`
- Images: `images\GHH399535.jpeg`
- Duplicate sources: `pages\1891.html`, `pages\25960.html`, `pages\13343.html`

### Full Text

````text
# Audio Remote-HFL Switch Connector for Inputs and Outputs

AUDIO REMOTE-HFL SWITCH 12P CONNECTOR

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

1 | Not used | ---

2 | Not used | ---

3 | Not used | ---

4 | ILL-(LED) | Outputs illumination control signal for cruise control combination switch

5 | Not used | ---

6 | Not used | ---

7 | +B | Continuous power source

8 | ILLUMI+ | Outputs illumination signal for cruise control combination switch

9 | Not used | ---

10 | STRG GND | Ground for audio remote-HFL switch (G502)

11 | Not used | ---

12 | STRG SW LIN | Communication signal for gauge control module
````

## Chunk 2469: Audio Unit Connector for Inputs and Outputs (2/4 door: Color Audio Type (5-inch Screen)) (2016 2017 2018)

- Title: Audio Unit Connector for Inputs and Outputs (2/4 door: Color Audio Type (5-inch Screen)) (2016 2017 2018)
- Source path: `pages\1442.html`
- Chunk ID: `chunk_d7f765a5b86f`
- Images: `images\GHH399536.jpeg`, `images\GHH399537.jpeg`, `images\GHH399538.jpeg`, `images\GHH399539.jpeg`
- Duplicate sources: `pages\1892.html`, `pages\25961.html`, `pages\13344.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (2/4 door: Color Audio Type (5-inch Screen)) (2016 2017 2018)

Connector Index

Audio Unit Connector A (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (3P)

Audio Unit Connector F (5P)

AUDIO UNIT CONNECTOR A (24P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker

A6 | RL SPKR- | Outputs sound signal for left rear speaker

A7 | RR SPKR+ | Outputs sound signal for right rear speaker

A8 | RR SPKR- | Outputs sound signal for right rear speaker

A9 * | AUDIO REMOTE SW | Detects control signal from audio remote switch

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker

A16 | FL SPKR- | Outputs sound signal for driver's door speaker

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker

A19 * | REMOTE SW GND | Ground for audio remote-HFL switch

A20 * | HFT/NAVI REMOTE SW | Detects control signal from HFL switch

A21 | Not used | ---

A22 | Not used | ---

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

*: Without multi-information display (MID)

AUDIO UNIT CONNECTOR C (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | Not used | ---

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | Not used | ---

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source (Not used)

C11 | Not used | ---

C12 | Not used | ---

C13 * | CAMERA VCC | Power source for rearview camera

C14 * | CAMERA GND | Ground for rearview camera

C15 | Not used | ---

C16 * | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 * | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 * | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 * | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 * | CAMERA BIT1 | Outputs mode select signal for rearview camera

*: With rearview camera

AUDIO UNIT CONNECTOR E (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | ANT+B | Power source for AM/FM antenna amplifier

E2 | RF IN | Inputs AM/FM signal

E3 | SH(RF IN) | Shield for terminal No. 2

AUDIO UNIT CONNECTOR F (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port

F2 | USB1 VBUS | Outputs power source for USB port

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4
````

## Chunk 2470: Audio Unit Connector for Inputs and Outputs (2/4-door: Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (2/4-door: Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1443.html`
- Chunk ID: `chunk_7ba4d5a81bf2`
- Images: `images\GHH399540.jpeg`, `images\GHH399541.jpeg`, `images\GHH399542.jpeg`, `images\GHH399543.jpeg`
- Duplicate sources: `pages\1893.html`, `pages\25962.html`, `pages\13345.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (2/4-door: Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

Connector Index

Audio Unit Connector A (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (3P)

Audio Unit Connector F (5P)

Audio Unit Connector A (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker

A6 | RL SPKR- | Outputs sound signal for left rear speaker

A7 | RR SPKR+ | Outputs sound signal for right rear speaker

A8 | RR SPKR- | Outputs sound signal for right rear speaker

A9 *1 | AUDIO REMOTE SW | Detects control signal from audio remote switch

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker

A16 | FL SPKR- | Outputs sound signal for driver's door speaker

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker

A19 *1 | REMOTE SW GND | Ground for audio remote-HFL switch

A20 *1 | HFT/NAVI REMOTE SW | Detects control signal from HFL switch

A21 | Not used | ---

A22 | Not used | ---

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Without multi-information display (MID)

*2: USA and Canada models

*3: Mexico models

Audio Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | Not used | ---

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | Not used | ---

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source (not used)

C11 | Not used | ---

C12 | Not used | ---

C13 * | CAMERA VCC | Power source for rearview camera

C14 * | CAMERA GND | Ground for rearview camera

C15 | Not used | ---

C16 * | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 * | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 * | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 * | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 * | CAMERA BIT1 | Outputs mode select signal for rearview camera

*: With rearview camera

Audio Unit Connector E (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | ANT+B | Power source for AM/FM antenna amplifier

E2 | RF IN | Inputs AM/FM signal

E3 | SH(RF IN) | Shield for terminal No. 2

Audio Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port

F2 | USB1 VBUS | Outputs power source for USB port

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4
````

## Chunk 2471: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1444.html`
- Chunk ID: `chunk_6dc32b8a728b`
- Images: `images\GHH399544.jpeg`, `images\GHH399545.jpeg`, `images\GHH399546.jpeg`, `images\GHH399547.jpeg`, `images\GHH399548.jpeg`, `images\GHH399549.jpeg`, `images\GHH399550.jpeg`, `images\GHH399551.jpeg`, `images\GHH399552.jpeg`, `images\GHH399553.jpeg`, `images\GHH399554.jpeg`, `images\GHH399555.jpeg`, `images\GHH399556.jpeg`
- Duplicate sources: `pages\1894.html`, `pages\25963.html`, `pages\13346.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

Connector Index

Audio Unit Connector A (24P) (With Stereo Amplifier)

Audio Unit Connector A (24P) (Without Stereo Amplifier)

Audio Unit Connector B (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (16P)

Audio Unit Connector F (5P)

Audio Unit Connector G (5P)

Audio Unit Connector H (3P)

Audio Unit Connector J (3P)

Audio Unit Connector K (2P)

Audio Unit Connector L (2P)

Audio Unit Connector M (4P) (With Stereo Amplifier)

Audio Unit Connector N (2P) (With XM)

Audio Unit Connector A (24P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 *1 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

A20 | Not used | ---

*1: Japan production

*2: USA and Canada models

*3: Mexico models

*4:'20-21Si

Cavity | Terminal Name | Description

A21 | SWD+B | Outputs signal for stereo amplifier and active sound control unit *4 switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Japan production

*2: USA and Canada models

*3: Mexico models

*4:'20-21Si

Audio Unit Connector A (24P) (female terminals) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker and left rear tweeter

A6 | RL SPKR- | Outputs sound signal for left rear speaker and left rear tweeter

A7 | RR SPKR+ | Outputs sound signal for right rear speaker and right rear tweeter

A8 | RR SPKR- | Outputs sound signal for right rear speaker and right rear tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 *1 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 | Not used | ---

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Japan production

*2: USA and Canada models

*3: Mexico models

Audio Unit Connector B (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 *1 | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 *1 | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 *2 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With stereo amplifier
````

## Chunk 2472: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1444.html`
- Chunk ID: `chunk_edf000904f5f`
- Images: `images\GHH399544.jpeg`, `images\GHH399545.jpeg`, `images\GHH399546.jpeg`, `images\GHH399547.jpeg`, `images\GHH399548.jpeg`, `images\GHH399549.jpeg`, `images\GHH399550.jpeg`, `images\GHH399551.jpeg`, `images\GHH399552.jpeg`, `images\GHH399553.jpeg`, `images\GHH399554.jpeg`, `images\GHH399555.jpeg`, `images\GHH399556.jpeg`
- Duplicate sources: `pages\1894.html`, `pages\25963.html`, `pages\13346.html`

### Full Text

````text
| Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With stereo amplifier

*2: With LaneWatch

Audio Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | Not used | ---

C12 | Not used | ---

C13 * | CAMERA VCC | Power source for rearview camera

C14 * | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 * | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 * | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 * | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 * | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 * | CAMERA BIT1 | Outputs mode select signal for rearview camera

*: With rearview camera

Audio Unit Connector E (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN C_H *2F-CAN_H *3 | Communication signal

E6 *4 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *4 | RS485+ | Communication signal for stereo amplifier

E8 *4 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_L *1F-CAN C_L *2F-CAN_L *3 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1:'18with CMBS

*2:'19-21with CMBS

*3: Without CMBS

*4: With stereo amplifier

Audio Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

F2 | USB1 VBUS | Outputs power source for USB port A

Cavity | Terminal Name | Description

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2
````

## Chunk 2473: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (2/4-door: Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1444.html`
- Chunk ID: `chunk_1c457cc8ba33`
- Images: `images\GHH399544.jpeg`, `images\GHH399545.jpeg`, `images\GHH399546.jpeg`, `images\GHH399547.jpeg`, `images\GHH399548.jpeg`, `images\GHH399549.jpeg`, `images\GHH399550.jpeg`, `images\GHH399551.jpeg`, `images\GHH399552.jpeg`, `images\GHH399553.jpeg`, `images\GHH399554.jpeg`, `images\GHH399555.jpeg`, `images\GHH399556.jpeg`
- Duplicate sources: `pages\1894.html`, `pages\25963.html`, `pages\13346.html`

### Full Text

````text
SB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

Audio Unit Connector K (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

Audio Unit Connector L (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

Audio Unit Connector M (4P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

Audio Unit Connector N (2P) (female terminals) (With XM)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2474: Audio Unit Connector for Inputs and Outputs (5-door: Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (5-door: Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1445.html`
- Chunk ID: `chunk_ec09ea621675`
- Images: `images\GHH399557.jpeg`, `images\GHH399558.jpeg`, `images\GHH399559.jpeg`, `images\GHH399560.jpeg`
- Duplicate sources: `pages\1895.html`, `pages\25964.html`, `pages\13347.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (5-door: Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)

Connector Index

Audio Unit Connector A (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (3P)

Audio Unit Connector F (5P)

Audio Unit Connector A (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL DOOR SPKR+ | Outputs sound signal for left rear door speaker

A6 | RL DOOR SPKR- | Outputs sound signal for left rear door speaker

A7 | RR DOOR SPKR+ | Outputs sound signal for right rear door speaker

A8 | RR DOOR SPKR- | Outputs sound signal for right rear door speaker

A9 *1 | AUDIO REMOTE SW | Detects control signal from audio remote switch

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker

A16 | FL SPKR- | Outputs sound signal for driver's door speaker

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker

A19 *1 | REMOTE SW GND | Ground for audio remote-HFL switch

A20 *1 | HFT/NAVI REMOTE SW | Detects control signal from HFL switch

A21 | Not used | ---

A22 | Not used | ---

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Without multi-information display (MID)

*2: With RR CAMERA ACC DIODE circuit

*3: Without RR CAMERA ACC DIODE circuit

Audio Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | Not used | ---

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | Not used | ---

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source (Not used)

C11 | Not used | ---

C12 | Not used | ---

C13 | CAMERA VCC | Power source for rearview camera

C14 | CAMERA GND | Ground for rearview camera

C15 | Not used | ---

C16 | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 | CAMERA BIT1 | Outputs mode select signal for rearview camera

Audio Unit Connector E (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | ANT +B | Power source for roof antenna

E2 | RF IN | Inputs AM/FM signal

E3 | SH(RF IN) | Shield for terminal No. 2

Audio Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port

F2 | USB1 VBUS | Outputs power source for USB port

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4
````

## Chunk 2475: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1446.html`
- Chunk ID: `chunk_63518f6ae814`
- Images: `images\GHH399561.jpeg`, `images\GHH399562.jpeg`, `images\GHH399563.jpeg`, `images\GHH399564.jpeg`, `images\GHH399565.jpeg`, `images\GHH399566.jpeg`, `images\GHH399567.jpeg`, `images\GHH399568.jpeg`, `images\GHH399569.jpeg`, `images\GHH399570.jpeg`, `images\GHH399571.jpeg`, `images\GHH399572.jpeg`, `images\GHH399573.jpeg`
- Duplicate sources: `pages\1896.html`, `pages\25965.html`, `pages\13348.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

Connector Index

Audio Unit Connector A (24P) (With Stereo Amplifier)

Audio Unit Connector A (24P) (Without Stereo Amplifier)

Audio Unit Connector B (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (16P)

Audio Unit Connector F (5P)

Audio Unit Connector G (5P)

Audio Unit Connector H (3P)

Audio Unit Connector J (3P)

Audio Unit Connector K (2P)

Audio Unit Connector L (2P)

Audio Unit Connector M (4P) (With Stereo Amplifier)

Audio Unit Connector N (2P) (With XM)

Audio Unit Connector A (24P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

A20 | Not used | ---

*:'20-21Type-R

Cavity | Terminal Name | Description

A21 | SWD+B | Outputs signal for stereo amplifier and active sound control unit * switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

*:'20-21Type-R

Audio Unit Connector A (24P) (female terminals) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL DOOR SPKR+ | Outputs sound signal for left rear door speaker and left rear door tweeter

A6 | RL DOOR SPKR- | Outputs sound signal for left rear door speaker and left rear door tweeter

A7 | RR DOOR SPKR+ | Outputs sound signal for right rear door speaker and right rear door tweeter

A8 | RR DOOR SPKR- | Outputs sound signal for right rear door speaker and right rear door tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 *3 | SWD+B | Outputs signal for active sound control unit switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *1 | Power source for accessories or detects reverse signal

ACC *2 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: With RR CAMERA ACC DIODE circuit

*2: Without RR CAMERA ACC DIODE circuit

*3:'20-21Type-R

Audio Unit Connector B (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 *1 | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 *1 | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 *2 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With stereo amplifier

*2: With LaneWatch

Audio Unit Connector C (32P) (female terminals)
````

## Chunk 2476: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1446.html`
- Chunk ID: `chunk_3645ecdec895`
- Images: `images\GHH399561.jpeg`, `images\GHH399562.jpeg`, `images\GHH399563.jpeg`, `images\GHH399564.jpeg`, `images\GHH399565.jpeg`, `images\GHH399566.jpeg`, `images\GHH399567.jpeg`, `images\GHH399568.jpeg`, `images\GHH399569.jpeg`, `images\GHH399570.jpeg`, `images\GHH399571.jpeg`, `images\GHH399572.jpeg`, `images\GHH399573.jpeg`
- Duplicate sources: `pages\1896.html`, `pages\25965.html`, `pages\13348.html`

### Full Text

````text
mera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With stereo amplifier

*2: With LaneWatch

Audio Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 * | ANC R+ | Inputs signal for acceleration sound enhancement from active sound control unit

C2 * | ANC R- | Inputs signal for acceleration sound enhancement from active sound control unit

C3 | PARK BUSY | Detects parking brake on signal

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | PARK BUSY | Detects parking brake on signal

C12 | Not used | ---

C13 | CAMERA VCC | Power source for rearview camera

C14 | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 | CAMERA ADPT | Detects connection for rearview camera

C17 * | ANC F+ | Inputs signal for acceleration sound enhancement from active sound control unit

C18 * | ANC F- | Inputs signal for acceleration sound enhancement from active sound control unit

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 | CAMERA BIT1 | Outputs mode select signal for rearview camera

*:'20-21Type-R without stereo amplifier

Audio Unit Connector E (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN C_H *2F-CAN_H *3 | Communication signal

E6 *4 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *4 | RS485+ | Communication signal for stereo amplifier

E8 *4 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_L *1F-CAN C_L *2F-CAN_L *3 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1:'17-19with CMBS

*2:'20-21with CMBS

*3: Without CMBS

*4: With stereo amplifier

Audio Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

Cavity | Terminal Name | Description

F2 | USB1 VBUS | Outputs power source for USB port A

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2
````

## Chunk 2477: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio Unit Connector for Inputs and Outputs (5-door: Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1446.html`
- Chunk ID: `chunk_8ef4b556feba`
- Images: `images\GHH399561.jpeg`, `images\GHH399562.jpeg`, `images\GHH399563.jpeg`, `images\GHH399564.jpeg`, `images\GHH399565.jpeg`, `images\GHH399566.jpeg`, `images\GHH399567.jpeg`, `images\GHH399568.jpeg`, `images\GHH399569.jpeg`, `images\GHH399570.jpeg`, `images\GHH399571.jpeg`, `images\GHH399572.jpeg`, `images\GHH399573.jpeg`
- Duplicate sources: `pages\1896.html`, `pages\25965.html`, `pages\13348.html`

### Full Text

````text
F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

Audio Unit Connector K (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

Audio Unit Connector L (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

Audio Unit Connector M (4P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

Audio Unit Connector N (2P) (female terminals) (With XM)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2478: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1447.html`
- Chunk ID: `chunk_85a53c655584`
- Images: `images\GHH399574.jpeg`, `images\GHH399575.jpeg`, `images\GHH399576.jpeg`, `images\GHH399577.jpeg`, `images\GHH399578.jpeg`, `images\GHH399579.jpeg`, `images\GHH399580.jpeg`, `images\GHH399581.jpeg`, `images\GHH399582.jpeg`, `images\GHH399583.jpeg`, `images\GHH399584.jpeg`, `images\GHH399585.jpeg`, `images\GHH399586.jpeg`
- Duplicate sources: `pages\1897.html`, `pages\25966.html`, `pages\13349.html`

### Full Text

````text
# Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)

Connector Index

Audio Unit Connector A (24P) (With Stereo Amplifier)

Audio Unit Connector A (24P) (Without Stereo Amplifier)

Audio Unit Connector B (24P)

Audio Unit Connector C (32P)

Audio Unit Connector E (16P)

Audio Unit Connector F (5P)

Audio Unit Connector G (5P)

Audio Unit Connector H (3P)

Audio Unit Connector J (3P)

Audio Unit Connector K (2P)

Audio Unit Connector L (2P)

Audio Unit Connector M (4P) (With Stereo Amplifier)

Audio Unit Connector N (2P) (With XM)

AUDIO UNIT CONNECTOR A (24P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

A20 | Not used | ---

A21 | SWD+B | Outputs signal for stereo amplifier switching on/off

A22 | VSP | Inputs vehicle speed pulse

Cavity | Terminal Name | Description

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

AUDIO UNIT CONNECTOR A (24P) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker and left rear tweeter

A6 | RL SPKR- | Outputs sound signal for left rear speaker and left rear tweeter

A7 | RR SPKR+ | Outputs sound signal for right rear speaker and right rear tweeter

A8 | RR SPKR- | Outputs sound signal for right rear speaker and right rear tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 | Not used | ---

A22 | VSP | Inputs vehicle speed pulse

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

AUDIO UNIT CONNECTOR B (24P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 *1 | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 *1 | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 *2 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With Stereo Amplifier

*2: With LaneWatch

AUDIO UNIT CONNECTOR C (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | Not used | ---

C12 | Not used | ---

C13 * | CAMERA VCC | Power source for rearview camera
````

## Chunk 2479: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1447.html`
- Chunk ID: `chunk_f40b1533f5e6`
- Images: `images\GHH399574.jpeg`, `images\GHH399575.jpeg`, `images\GHH399576.jpeg`, `images\GHH399577.jpeg`, `images\GHH399578.jpeg`, `images\GHH399579.jpeg`, `images\GHH399580.jpeg`, `images\GHH399581.jpeg`, `images\GHH399582.jpeg`, `images\GHH399583.jpeg`, `images\GHH399584.jpeg`, `images\GHH399585.jpeg`, `images\GHH399586.jpeg`
- Duplicate sources: `pages\1897.html`, `pages\25966.html`, `pages\13349.html`

### Full Text

````text
Watch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With Stereo Amplifier

*2: With LaneWatch

AUDIO UNIT CONNECTOR C (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | Not used | ---

C12 | Not used | ---

C13 * | CAMERA VCC | Power source for rearview camera

C14 * | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 * | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 * | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 * | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 * | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 * | CAMERA BIT1 | Outputs mode select signal for rearview camera

*: With rearview camera

AUDIO UNIT CONNECTOR E (16P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN_H *2 | Communication signal

E6 *3 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *3 | RS485+ | Communication signal for stereo amplifier

E8 *3 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_L *1F-CAN_L *2 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1: With CMBS

*2: Without CMBS

*3: With Stereo Amplifier

AUDIO UNIT CONNECTOR F (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

F2 | USB1 VBUS | Outputs power source for USB port A

Cavity | Terminal Name | Description

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

AUDIO UNIT CONNECTOR G (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

AUDIO UNIT CONNENTOR H (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

AUDIO UNIT CONNECTOR J (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

AUDIO UNIT CONNECTOR K (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

AUDIO UNIT CONNECTOR L (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

AUDIO UNIT CONNECTOR M (4P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

AUDIO UNIT CONNECTOR N (2P) (With XM)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2480: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio Unit Connector for Inputs and Outputs (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1447.html`
- Chunk ID: `chunk_e50315a7b234`
- Images: `images\GHH399574.jpeg`, `images\GHH399575.jpeg`, `images\GHH399576.jpeg`, `images\GHH399577.jpeg`, `images\GHH399578.jpeg`, `images\GHH399579.jpeg`, `images\GHH399580.jpeg`, `images\GHH399581.jpeg`, `images\GHH399582.jpeg`, `images\GHH399583.jpeg`, `images\GHH399584.jpeg`, `images\GHH399585.jpeg`, `images\GHH399586.jpeg`
- Duplicate sources: `pages\1897.html`, `pages\25966.html`, `pages\13349.html`

### Full Text

````text
nal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

AUDIO UNIT CONNECTOR K (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

AUDIO UNIT CONNECTOR L (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

AUDIO UNIT CONNECTOR M (4P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

AUDIO UNIT CONNECTOR N (2P) (With XM)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2481: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)
- Source path: `pages\1448.html`
- Chunk ID: `chunk_401e58aac29d`
- Images: `images\GHH399587.jpeg`, `images\GHH399588.jpeg`, `images\GHH399589.jpeg`, `images\GHH399590.jpeg`, `images\GHH399591.jpeg`, `images\GHH399592.jpeg`, `images\GHH399593.jpeg`, `images\GHH399594.jpeg`, `images\GHH399595.jpeg`, `images\GHH399596.jpeg`, `images\GHH399597.jpeg`, `images\GHH399598.jpeg`, `images\GHH399599.jpeg`
- Duplicate sources: `pages\1898.html`, `pages\25967.html`, `pages\13350.html`

### Full Text

````text
# Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)

Connector Index

Audio-Navigation Unit Connector A (24P) (With Stereo Amplifier)

Audio-Navigation Unit Connector A (24P) (Without Stereo Amplifier)

Audio-Navigation Unit Connector B (24P)

Audio-Navigation Unit Connector C (32P)

Audio-Navigation Unit Connector E (16P)

Audio-Navigation Unit Connector F (5P)

Audio-Navigation Unit Connector G (5P)

Audio-Navigation Unit Connector H (3P)

Audio-Navigation Unit Connector J (3P)

Audio-Navigation Unit Connector K (2P)

Audio-Navigation Unit Connector L (2P)

Audio-Navigation Unit Connector M (4P) (With Stereo Amplifier)

Audio-Navigation Unit Connector N (2P) (With XM)

AUDIO-NAVIGATION UNIT CONNECTOR A (24P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

A20 | Not used | ---

Cavity | Terminal Name | Description

A21 | SWD+B | Outputs signal for stereo amplifier switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

AUDIO-NAVIGATION UNIT CONNECTOR A (24P) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker and left rear tweeter

A6 | RL SPKR- | Outputs sound signal for left rear speaker and left rear tweeter

A7 | RR SPKR+ | Outputs sound signal for right rear speaker and right rear tweeter

A8 | RR SPKR- | Outputs sound signal for right rear speaker and right rear tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | Not used | ---

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 | Not used | ---

A22 | VSP | Inputs vehicle speed pulse

A23 | ACC | Power source for accessories

A24 | B-CAN_L | Communication signal

AUDIO-NAVIGATION UNIT CONNECTOR B (24P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 * | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 * | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 | LWC CAM VCC | Power source for LaneWatch camera

B9 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 * | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 * | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 | LWC CAM VGND | Ground for LaneWatch camera

B22 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*: With stereo amplifier

AUDIO-NAVIGATION UNIT CONNECTOR C (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---
````

## Chunk 2482: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)
- Source path: `pages\1448.html`
- Chunk ID: `chunk_fc3107b0626c`
- Images: `images\GHH399587.jpeg`, `images\GHH399588.jpeg`, `images\GHH399589.jpeg`, `images\GHH399590.jpeg`, `images\GHH399591.jpeg`, `images\GHH399592.jpeg`, `images\GHH399593.jpeg`, `images\GHH399594.jpeg`, `images\GHH399595.jpeg`, `images\GHH399596.jpeg`, `images\GHH399597.jpeg`, `images\GHH399598.jpeg`, `images\GHH399599.jpeg`
- Duplicate sources: `pages\1898.html`, `pages\25967.html`, `pages\13350.html`

### Full Text

````text
Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 | LWC CAM VGND | Ground for LaneWatch camera

B22 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*: With stereo amplifier

AUDIO-NAVIGATION UNIT CONNECTOR C (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | Not used | ---

C12 | Not used | ---

C13 | CAMERA VCC | Power source for rearview camera

C14 | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 | CAMERA BIT1 | Outputs mode select signal for rearview camera

AUDIO-NAVIGATION UNIT CONNECTOR E (16P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

Cavity | Terminal Name | Description

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN_H *2 | Communication signal

E6 *3 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *3 | RS485+ | Communication signal for stereo amplifier

E8 *3 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_L *1F-CAN_L *2 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1: With CMBS

*2: Without CMBS

*3: With stereo amplifier

AUDIO-NAVIGATION UNIT CONNECTOR F (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

F2 | USB1 VBUS | Outputs power source for USB port A

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

AUDIO-NAVIGATION UNIT CONNECTOR G (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

AUDIO-NAVIGATION UNIT CONNECTOR H (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

AUDIO-NAVIGATION UNIT CONNECTOR J (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

AUDIO-NAVIGATION UNIT CONNECTOR K (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

AUDIO-NAVIGATION UNIT CONNECTOR L (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

AUDIO-NAVIGATION UNIT CONNECTOR M (4P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier
````

## Chunk 2483: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2016 2017 2018)
- Source path: `pages\1448.html`
- Chunk ID: `chunk_598fc36ebce3`
- Images: `images\GHH399587.jpeg`, `images\GHH399588.jpeg`, `images\GHH399589.jpeg`, `images\GHH399590.jpeg`, `images\GHH399591.jpeg`, `images\GHH399592.jpeg`, `images\GHH399593.jpeg`, `images\GHH399594.jpeg`, `images\GHH399595.jpeg`, `images\GHH399596.jpeg`, `images\GHH399597.jpeg`, `images\GHH399598.jpeg`, `images\GHH399599.jpeg`
- Duplicate sources: `pages\1898.html`, `pages\25967.html`, `pages\13350.html`

### Full Text

````text
y | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

AUDIO-NAVIGATION UNIT CONNECTOR K (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

AUDIO-NAVIGATION UNIT CONNECTOR L (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

AUDIO-NAVIGATION UNIT CONNECTOR M (4P) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

AUDIO-NAVIGATION UNIT CONNECTOR N (2P) (With XM)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2484: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)
- Source path: `pages\1449.html`
- Chunk ID: `chunk_616a631aee71`
- Images: `images\GHH399600.jpeg`, `images\GHH399601.jpeg`, `images\GHH399602.jpeg`, `images\GHH399603.jpeg`, `images\GHH399604.jpeg`, `images\GHH399605.jpeg`, `images\GHH399606.jpeg`, `images\GHH399607.jpeg`, `images\GHH399608.jpeg`, `images\GHH399609.jpeg`, `images\GHH399610.jpeg`, `images\GHH399611.jpeg`, `images\GHH399612.jpeg`
- Duplicate sources: `pages\1899.html`, `pages\25968.html`, `pages\13351.html`

### Full Text

````text
# Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)

Connector Index

Audio-Navigation Unit Connector A (24P) (With Stereo Amplifier)

Audio-Navigation Unit Connector A (24P) (Without Stereo Amplifier)

Audio-Navigation Unit Connector B (24P)

Audio-Navigation Unit Connector C (32P)

Audio-Navigation Unit Connector E (16P)

Audio-Navigation Unit Connector F (5P)

Audio-Navigation Unit Connector G (5P)

Audio-Navigation Unit Connector H (3P)

Audio-Navigation Unit Connector J (3P)

Audio-Navigation Unit Connector K (2P)

Audio-Navigation Unit Connector L (2P)

Audio-Navigation Unit Connector M (4P) (With Stereo Amplifier)

Audio-Navigation Unit Connector N (2P) (With XM)

Audio-Navigation Unit Connector A (24P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 *1 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

*1: Japan production

*2: USA and Canada models

*3: Mexico models

*4:'20-21Si

Cavity | Terminal Name | Description

A20 | Not used | ---

A21 | SWD+B | Outputs signal for stereo amplifier and active sound control unit *4 switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Japan production

*2: USA and Canada models

*3: Mexico models

*4:'20-21Si

Audio-Navigation Unit Connector A (24P) (female terminals) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL SPKR+ | Outputs sound signal for left rear speaker and left rear tweeter

A6 | RL SPKR- | Outputs sound signal for left rear speaker and left rear tweeter

A7 | RR SPKR+ | Outputs sound signal for right rear speaker and right rear tweeter

A8 | RR SPKR- | Outputs sound signal for right rear speaker and right rear tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 *1 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 | Not used | ---

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *2 | Power source for accessories or detects reverse signal

ACC *3 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: Japan production

*2: USA and Canada models

*3: Mexico models

Audio-Navigation Unit Connector B (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 * | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 * | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 | LWC CAM VCC | Power source for LaneWatch camera

B9 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 * | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 * | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 | LWC CAM VGND | Ground for LaneWatch camera
````

## Chunk 2485: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)
- Source path: `pages\1449.html`
- Chunk ID: `chunk_e1a303cbe0b7`
- Images: `images\GHH399600.jpeg`, `images\GHH399601.jpeg`, `images\GHH399602.jpeg`, `images\GHH399603.jpeg`, `images\GHH399604.jpeg`, `images\GHH399605.jpeg`, `images\GHH399606.jpeg`, `images\GHH399607.jpeg`, `images\GHH399608.jpeg`, `images\GHH399609.jpeg`, `images\GHH399610.jpeg`, `images\GHH399611.jpeg`, `images\GHH399612.jpeg`
- Duplicate sources: `pages\1899.html`, `pages\25968.html`, `pages\13351.html`

### Full Text

````text
No. 14

B2 * | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 | LWC CAM VCC | Power source for LaneWatch camera

B9 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 * | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 * | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 | LWC CAM VGND | Ground for LaneWatch camera

B22 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*: With stereo amplifier

Audio-Navigation Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | Not used | ---

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | Not used | ---

C12 | Not used | ---

C13 | CAMERA VCC | Power source for rearview camera

C14 | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 | CAMERA BIT1 | Outputs mode select signal for rearview camera

Audio-Navigation Unit Connector E (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN C_H *2F-CAN_H *3 | Communication signal

E6 *4 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *4 | RS485+ | Communication signal for stereo amplifier

E8 *4 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_H *1F-CAN C_H *2F-CAN_H *3 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1:'18with CMBS

*2:'19-21with CMBS

*3: Without CMBS

*4: With stereo amplifier

Audio-Navigation Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

F2 | USB1 VBUS | Outputs power source for USB port A

Cavity | Terminal Name | Description

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio-Navigation Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description
````

## Chunk 2486: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (2/4-door) (2018 2019 2020 2021)
- Source path: `pages\1449.html`
- Chunk ID: `chunk_5a2420eaa569`
- Images: `images\GHH399600.jpeg`, `images\GHH399601.jpeg`, `images\GHH399602.jpeg`, `images\GHH399603.jpeg`, `images\GHH399604.jpeg`, `images\GHH399605.jpeg`, `images\GHH399606.jpeg`, `images\GHH399607.jpeg`, `images\GHH399608.jpeg`, `images\GHH399609.jpeg`, `images\GHH399610.jpeg`, `images\GHH399611.jpeg`, `images\GHH399612.jpeg`
- Duplicate sources: `pages\1899.html`, `pages\25968.html`, `pages\13351.html`

### Full Text

````text
o-Navigation Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio-Navigation Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

Audio-Navigation Unit Connector K (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

Audio-Navigation Unit Connector L (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

Audio-Navigation Unit Connector M (4P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

Audio-Navigation Unit Connector N (2P) (female terminals) (With XM)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2487: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\1450.html`
- Chunk ID: `chunk_08cba97157de`
- Images: `images\GHH399613.jpeg`, `images\GHH399614.jpeg`, `images\GHH399615.jpeg`, `images\GHH399616.jpeg`, `images\GHH399617.jpeg`, `images\GHH399618.jpeg`, `images\GHH399619.jpeg`, `images\GHH399620.jpeg`, `images\GHH399621.jpeg`, `images\GHH399622.jpeg`, `images\GHH399623.jpeg`, `images\GHH399624.jpeg`, `images\GHH399625.jpeg`
- Duplicate sources: `pages\1900.html`, `pages\25969.html`, `pages\13352.html`

### Full Text

````text
# Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

Connector Index

Audio-Navigation Unit Connector A (24P) (With Stereo Amplifier)

Audio-Navigation Unit Connector A (24P) (Without Stereo Amplifier)

Audio-Navigation Unit Connector B (24P)

Audio-Navigation Unit Connector C (32P)

Audio-Navigation Unit Connector E (16P)

Audio-Navigation Unit Connector F (5P)

Audio-Navigation Unit Connector G (5P)

Audio-Navigation Unit Connector H (3P)

Audio-Navigation Unit Connector J (3P)

Audio-Navigation Unit Connector K (2P)

Audio-Navigation Unit Connector L (2P)

Audio-Navigation Unit Connector M (4P) (With Stereo Amplifier)

Audio-Navigation Unit Connector N (2P)

Audio-Navigation Unit Connector A (24P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | Not used | ---

A6 | Not used | ---

A7 | Not used | ---

A8 | Not used | ---

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | Not used | ---

A16 | Not used | ---

A17 | Not used | ---

A18 | Not used | ---

A19 | Not used | ---

A20 | Not used | ---

*1: With RR CAMERA ACC DIODE circuit

*2: Without RR CAMERA ACC DIODE circuit

*3:'20-21Type-R

Cavity | Terminal Name | Description

A21 | SWD+B | Outputs signal for stereo amplifier and active sound control unit *3 switching on/off

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *1 | Power source for accessories or detects reverse signal

ACC *2 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: With RR CAMERA ACC DIODE circuit

*2: Without RR CAMERA ACC DIODE circuit

*3:'20-21Type-R

Audio-Navigation Unit Connector A (24P) (female terminals) (Without Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for audio-navigation unit (G504)

A2 | Not used | ---

A3 | +B AUDIO | Continuous power source

A4 | Not used | ---

A5 | RL DOOR SPKR+ | Outputs sound signal for left rear door speaker and left rear door tweeter

A6 | RL DOOR SPKR- | Outputs sound signal for left rear door speaker and left rear door tweeter

A7 | RR DOOR SPKR+ | Outputs sound signal for right rear door speaker and right rear door tweeter

A8 | RR DOOR SPKR- | Outputs sound signal for right rear door speaker and right rear door tweeter

A9 | Not used | ---

A10 | Not used | ---

A11 | Not used | ---

A12 | K LINE | Detects scan tool signal (serial data)

A13 | ACC | Power source for accessories

A14 | B-CAN_H | Communication signal

A15 | FL SPKR+ | Outputs sound signal for driver's door speaker and left front tweeter

A16 | FL SPKR- | Outputs sound signal for driver's door speaker and left front tweeter

A17 | FR SPKR+ | Outputs sound signal for front passenger's door speaker and right front tweeter

A18 | FR SPKR- | Outputs sound signal for front passenger's door speaker and right front tweeter

A19 | Not used | ---

A20 | Not used | ---

A21 | Not used | ---

A22 | VSP | Inputs vehicle speed pulse

A23 | RR CAMERA ACC DIODE *1 | Power source for accessories or detects reverse signal

ACC *2 | Power source for accessories

A24 | B-CAN_L | Communication signal

*1: With RR CAMERA ACC DIODE circuit

*2: Without RR CAMERA ACC DIODE circuit

Audio-Navigation Unit Connector B (24P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 *1 | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 *1 | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 *2 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---
````

## Chunk 2488: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\1450.html`
- Chunk ID: `chunk_fd4f0092e888`
- Images: `images\GHH399613.jpeg`, `images\GHH399614.jpeg`, `images\GHH399615.jpeg`, `images\GHH399616.jpeg`, `images\GHH399617.jpeg`, `images\GHH399618.jpeg`, `images\GHH399619.jpeg`, `images\GHH399620.jpeg`, `images\GHH399621.jpeg`, `images\GHH399622.jpeg`, `images\GHH399623.jpeg`, `images\GHH399624.jpeg`, `images\GHH399625.jpeg`
- Duplicate sources: `pages\1900.html`, `pages\25969.html`, `pages\13352.html`

### Full Text

````text
Cavity | Terminal Name | Description

B1 *1 | AUX NAVI SH | Shield for terminals No. 2, No. 13, and No. 14

B2 *1 | AUX BEEP | Outputs system beep signal

B3 | Not used | ---

B4 | Not used | ---

B5 | Not used | ---

B6 *2 | LANEWATCH SW | Detects LaneWatch on/off signal from LaneWatch switch

B7 | Not used | ---

B8 *2 | LWC CAM VCC | Power source for LaneWatch camera

B9 *2 | SH LWC CAM | Shield for terminals No. 8, No. 20, No. 21, No. 22, and No. 23

B10 | Not used | ---

B11 | Not used | ---

B12 | Not used | ---

B13 *1 | AUX NAVI | Outputs sound signal for voice guidance and Voice Recognition (VR) prompts

B14 *1 | AUX NAVI GND | Basis ground for terminals No. 2 and No. 13

B15 | Not used | ---

B16 | Not used | ---

B17 | Not used | ---

B18 | Not used | ---

B19 | Not used | ---

B20 *2 | LWC CAM VID | Inputs video signal from LaneWatch camera

B21 *2 | LWC CAM VGND | Ground for LaneWatch camera

B22 *2 | UNIT TO LWC | Communication signal for LaneWatch camera

B23 *2 | LWC TO UNIT | Communication signal for LaneWatch camera

B24 | Not used | ---

*1: With stereo amplifier

*2: With LaneWatch

Audio-Navigation Unit Connector C (32P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | Not used | ---

C2 | Not used | ---

C3 | PARK BUSY | Detects parking brake on signal

C4 | Not used | ---

C5 | HFT MUTE | Outputs HFL microphone directivity switching signal

C6 | SH MIC | Shield for terminals No. 22 and No. 23

C7 | MIC PWR | Power source for HFL microphone

C8 | Not used | ---

C9 | Not used | ---

C10 | IG1 METER | IG1 power source

C11 | PARK BUSY | Detects parking brake on signal

C12 | Not used | ---

C13 | CAMERA VCC | Power source for rearview camera

C14 | CAMERA GND | Ground for rearview camera

C15 | BACK LT | Detects reverse signal

C16 | CAMERA ADPT | Detects connection for rearview camera

C17 | Not used | ---

C18 | Not used | ---

C19 | Not used | ---

C20 | Not used | ---

C21 | Not used | ---

C22 | MIC+ | Inputs sound signal from HFL microphone

C23 | MIC GND | Ground for HFL microphone

C24 | Not used | ---

C25 | Not used | ---

C26 | Not used | ---

C27 | Not used | ---

C28 | SH CAMERA | Shield for terminals No. 13, No. 14, and No. 29

C29 | CAMERA V | Inputs NTSC video signal from rearview camera

C30 | Not used | ---

C31 | CAMERA BIT0 | Outputs mode select signal for rearview camera

C32 | CAMERA BIT1 | Outputs mode select signal for rearview camera

Audio-Navigation Unit Connector E (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

E1 | TUNER 6V | Power source for tuner unit

E2 | TUNER 9V | Power source for tuner unit

E3 | Not used | ---

E4 | DISP CONT | Outputs signal for center display unit switching on/off

E5 | F-CAN B_H *1F-CAN C_H *2F-CAN_H *3 | Communication signal

E6 *4 | AMP RS485 SH | Shield for terminals No. 7 and No. 8

E7 *4 | RS485+ | Communication signal for stereo amplifier

E8 *4 | RS485- | Communication signal for stereo amplifier

E9 | TUNER GND | Ground for tuner unit

E10 | Not used | ---

E11 | Not used | ---

E12 | Not used | ---

E13 | F-CAN B_L *1F-CAN C_L *2F-CAN_L *3 | Communication signal

E14 | TUNER RS485 SH | Shield for terminals No. 15 and No. 16

E15 | TUNER RS485+ | Communication signal for tuner unit

E16 | TUNER RS485- | Communication signal for tuner unit

*1:'17-19 with CMBS

*2:'20-21

*3: Without CMBS

*4: With stereo amplifier

Audio-Navigation Unit Connector F (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

F1 | USB1 GND | Ground for USB port A

Cavity | Terminal Name | Description

F2 | USB1 VBUS | Outputs power source for USB port A

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit
````

## Chunk 2489: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

- Title: Audio-Navigation Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\1450.html`
- Chunk ID: `chunk_21cbd8c1adfa`
- Images: `images\GHH399613.jpeg`, `images\GHH399614.jpeg`, `images\GHH399615.jpeg`, `images\GHH399616.jpeg`, `images\GHH399617.jpeg`, `images\GHH399618.jpeg`, `images\GHH399619.jpeg`, `images\GHH399620.jpeg`, `images\GHH399621.jpeg`, `images\GHH399622.jpeg`, `images\GHH399623.jpeg`, `images\GHH399624.jpeg`, `images\GHH399625.jpeg`
- Duplicate sources: `pages\1900.html`, `pages\25969.html`, `pages\13352.html`

### Full Text

````text
ts power source for USB port A

F3 | USB1 DATA+ | Communication signal

F4 | USB1 DATA- | Communication signal

F5 | USB1 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector G (5P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

G1 | USB2 GND | Ground for USB port B

G2 | USB2 VBUS | Outputs power source for USB port B

G3 | USB2 DATA+ | Communication signal

G4 | USB2 DATA- | Communication signal

G5 | USB2 SH | Shield for terminals No. 1, No. 2, No. 3, and No. 4

Audio-Navigation Unit Connector H (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

H1 | LVDS1+ | Communication signal for center display unit

H2 | LVDS1- | Communication signal for center display unit

H3 | LVDS1 SH | Shield for terminals No. 1 and No. 2

Audio-Navigation Unit Connector J (3P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

J1 | LVDS2+ | Communication signal for gauge control module

J2 | LVDS2- | Communication signal for gauge control module

J3 | LVDS2 SH | Shield for terminals No. 1 and No. 2

Audio-Navigation Unit Connector K (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

K1 | GPS ANT | Inputs GPS signal

K2 | GPS SH | Shield for terminal No. 1

Audio-Navigation Unit Connector L (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

L1 | SPDIF1 SIG | Communication signal for tuner unit

L2 | SPDIF1 SH | Shield for terminal No. 1

Audio-Navigation Unit Connector M (4P) (female terminals) (With Stereo Amplifier)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

M1 | SPDIF2 SIG | Communication signal for stereo amplifier

M2 | Not used | ---

M3 | SPDIF2 SH | Shield for terminal No. 1

M4 | Not used | ---

Audio-Navigation Unit Connector N (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

N1 | SAT/TER | Inputs satellite/terrestrial signal

N2 | SH(SAT/TER) | Shield for terminal No. 1
````

## Chunk 2490: Center Display Unit Connector for Inputs and Outputs

- Title: Center Display Unit Connector for Inputs and Outputs
- Source path: `pages\1451.html`
- Chunk ID: `chunk_9499a1af9b1b`
- Images: `images\GHH399626.jpeg`, `images\GHH399627.jpeg`
- Duplicate sources: `pages\1901.html`, `pages\25970.html`, `pages\13353.html`

### Full Text

````text
# Center Display Unit Connector for Inputs and Outputs

Connector Index

Center Display Unit Connector A (5P)

Center Display Unit Connector B (3P)

CENTER DISPLAY UNIT CONNECTOR A (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | +B AUDIO | Continuous power source

A2 | Not used | ---

A3 | ILLUMI+ | Detects illumination on signal

A4 | DISP CONT | Inputs signal for center display unit switching on/off

A5 | GND | Ground for center display unit (G504)

CENTER DISPLAY UNIT CONNECTOR B (3P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 | LVDS1+ | Communication signal for audio-navigation unit or audio unit

B2 | LVDS1- | Communication signal for audio-navigation unit or audio unit

B3 | LVDS1 SH | Shield for terminals No. 1 and No. 2
````

## Chunk 2491: HFL Microphone Connector for Inputs and Outputs

- Title: HFL Microphone Connector for Inputs and Outputs
- Source path: `pages\1452.html`
- Chunk ID: `chunk_402259a6db0c`
- Images: `images\GHH399628.jpeg`
- Duplicate sources: `pages\1902.html`, `pages\25971.html`, `pages\13354.html`

### Full Text

````text
# HFL Microphone Connector for Inputs and Outputs

HFL Microphone 8P Connector (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

1 | MIC GND | Ground for HFL microphone

2 | MIC+ | Outputs sound signal to audio-navigation unit or audio unit

3 | Not used | ---

4 | MIC PWR | Power source from audio-navigation unit or audio unit

5 | Not used | ---

6 | Not used | ---

7 | HFT MUTE | Inputs HFL microphone directivity switching signal

8 * | ANC F MIC+8V | Outputs sound signal to active sound control unit

*:'20-21Si
````

## Chunk 2492: Rearview Camera Connector for Inputs and Outputs

- Title: Rearview Camera Connector for Inputs and Outputs
- Source path: `pages\1453.html`
- Chunk ID: `chunk_33bc31ccfbc2`
- Images: `images\GHH399629.jpeg`
- Duplicate sources: `pages\1903.html`, `pages\25972.html`, `pages\13355.html`

### Full Text

````text
# Rearview Camera Connector for Inputs and Outputs

REARVIEW CAMERA 8P CONNECTOR (male terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

1 *1 | CAMERA ADPT | Detects connection for rearview camera

2 | CAMERA VCC | Power source from audio-navigation unit or audio unit

3 | CAMERA BIT0 | Inputs mode select signal for rearview camera

4 | CAMERA BIT1 | Inputs mode select signal for rearview camera

5 | SH CAMERA | Shield for terminals No. 2, No. 7, and No. 8

6 *2 | CAMERA ADPT | Detects connection for rearview camera

7 | CAMERA V | Outputs NTSC video signal to audio-navigation unit or audio unit

8 | CAMERA GND | Ground for rearview camera

*1: 2-door

*2: Except 2-door
````

## Chunk 2493: Stereo Amplifier Connector for Inputs and Outputs (2/4-door)

- Title: Stereo Amplifier Connector for Inputs and Outputs (2/4-door)
- Source path: `pages\1454.html`
- Chunk ID: `chunk_ab19ea159623`
- Images: `images\GHH399630.jpeg`, `images\GHH399631.jpeg`, `images\GHH399632.jpeg`, `images\GHH399633.jpeg`
- Duplicate sources: `pages\1904.html`, `pages\25973.html`, `pages\13356.html`

### Full Text

````text
# Stereo Amplifier Connector for Inputs and Outputs (2/4-door)

Connector Index

Stereo Amplifier Connector A (18P)

Stereo Amplifier Connector B (8P)

Stereo Amplifier Connector C (16P)

Stereo Amplifier Connector D (2P)

Stereo Amplifier Connector A (18P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for stereo amplifier (G504)

A2 | SUB WOOFER+ | Outputs sound signal for subwoofer

A3 | +B AUDIO AMP | Continuous power source

A4 | SUB WOOFER- | Outputs sound signal for subwoofer

A5 | FL SPKR+ | Outputs sound signal for driver's door speaker

A6 | FL SPKR- | Outputs sound signal for driver's door speaker

A7 | SATR SP-(N/W IN) | Outputs sound signal for right rear speaker

A8 | SATR SP+(N/W IN) | Outputs sound signal for right rear speaker

A9 | SATL SP-(N/W IN) | Outputs sound signal for left rear speaker

A10 | SATL SP+(N/W IN) | Outputs sound signal for left rear speaker

A11 | CTR SPKR+ | Outputs sound signal for front center speaker

A12 | FR SPKR- | Outputs sound signal for front passenger's door speaker

A13 | FR SPKR+ | Outputs sound signal for front passenger's door speaker

A14 | FL TWEETER+ | Outputs sound signal for left front tweeter

A15 | FL TWEETER- | Outputs sound signal for left front tweeter

A16 | FR TWEETER+ | Outputs sound signal for right front tweeter

A17 | FR TWEETER- | Outputs sound signal for right front tweeter

A18 | CTR SPKR- | Outputs sound signal for front center speaker

Stereo Amplifier Connector B (8P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 | Not used | ---

B2 | Not used | ---

B3 | Not used | ---

B4 | Not used | ---

B5 | RR TWEETER+ *1SATR TWEETER+ *2 | Outputs sound signal for right rear tweeter

B6 | RR TWEETER- *1SATR TWEETER- *2 | Outputs sound signal for right rear tweeter

B7 | RL TWEETER+ *1SATL TWEETER+ *2 | Outputs sound signal for left rear tweeter

B8 | RL TWEETER- *1SATL TWEETER- *2 | Outputs sound signal for left rear tweeter

*1: USA and Canada production

*2: Japan production

Stereo Amplifier Connector C (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 *1 | ANC R- *2 | Not used

ANC R- *3 | Inputs signal for acceleration sound enhancement from active sound control unit

C2 *1 | ANC F- | Inputs signal for acceleration sound enhancement from active sound control unit

C3 | Not used | ---

C4 | AUX BEEP | Inputs system beep signal

C5 | AUX NAVI GND | Basis ground for terminals No. 4 and No. 12

C6 | Not used | ---

C7 | RS485- | Communication signal for audio-navigation unit or audio unit

C8 | Not used | ---

*1:'20-21Si

*2: 2-door

*3: 4-door

Cavity | Terminal Name | Description

C9 *1 | ANC R+ *2 | Not used

ANC R+ *3 | Inputs signal for acceleration sound enhancement from active sound control unit

C10 *1 | ANC F+ | Inputs signal for acceleration sound enhancement from active sound control unit

C11 | Not used | ---

C12 | AUX NAVI | Inputs sound signal for voice guidance and Voice Recognition (VR) prompts

C13 | Not used | ---

C14 | SWD+B | Inputs signal for stereo amplifier switching on/off

C15 | RS485+ | Communication signal for audio-navigation unit or audio unit

C16 | Not used | ---

*1:'20-21Si

*2: 2-door

*3: 4-door

Stereo Amplifier Connector D (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

D1 | SPDIF2 SIG | Communication signal for audio-navigation unit or audio unit

D2 | SPDIF2 SH | Shield for terminal No. 1
````

## Chunk 2494: Stereo Amplifier Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

- Title: Stereo Amplifier Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\1455.html`
- Chunk ID: `chunk_f9d084494480`
- Images: `images\GHH399634.jpeg`, `images\GHH399635.jpeg`, `images\GHH399636.jpeg`, `images\GHH399637.jpeg`
- Duplicate sources: `pages\1905.html`, `pages\25974.html`, `pages\13357.html`

### Full Text

````text
# Stereo Amplifier Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

Connector Index

Stereo Amplifier Connector A (18P)

Stereo Amplifier Connector B (8P)

Stereo Amplifier Connector C (16P)

Stereo Amplifier Connector D (2P)

Stereo Amplifier Connector A (18P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | GND | Ground for stereo amplifier (G504)

A2 | SUB WOOFER+ | Outputs sound signal for subwoofer

A3 | +B AUDIO AMP | Continuous power source

A4 | SUB WOOFER- | Outputs sound signal for subwoofer

A5 | FL SPKR+ | Outputs sound signal for driver's door speaker

A6 | FL SPKR- | Outputs sound signal for driver's door speaker

A7 | RR DOOR SPKR- | Outputs sound signal for right rear door speaker

A8 | RR DOOR SPKR+ | Outputs sound signal for right rear door speaker

A9 | RL DOOR SPKR- | Outputs sound signal for left rear door speaker

A10 | RL DOOR SPKR+ | Outputs sound signal for left rear door speaker

A11 | CTR SPKR+ | Outputs sound signal for front center speaker

A12 | FR SPKR- | Outputs sound signal for front passenger's door speaker

A13 | FR SPKR+ | Outputs sound signal for front passenger's door speaker

A14 | FL TWEETER+ | Outputs sound signal for left front tweeter

A15 | FL TWEETER- | Outputs sound signal for left front tweeter

A16 | FR TWEETER+ | Outputs sound signal for right front tweeter

A17 | FR TWEETER- | Outputs sound signal for right front tweeter

A18 | CTR SPKR- | Outputs sound signal for front center speaker

Stereo Amplifier Connector B (8P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 | SATR SP+(N/W IN) | Outputs sound signal for right satellite speaker

B2 | SATR SP-(N/W IN) | Outputs sound signal for right satellite speaker

B3 | SATL SP+(N/W IN) | Outputs sound signal for left satellite speaker

B4 | SATL SP-(N/W IN) | Outputs sound signal for left satellite speaker

B5 | RR TWEETER+ | Outputs sound signal for right rear door tweeter

B6 | RR TWEETER- | Outputs sound signal for right rear door tweeter

B7 | RL TWEETER+ | Outputs sound signal for left rear door tweeter

B8 | RL TWEETER- | Outputs sound signal for left rear door tweeter

Stereo Amplifier Connector C (16P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 * | ANC R- | Inputs signal for acceleration sound enhancement from active sound control unit

C2 * | ANC F- | Inputs signal for acceleration sound enhancement from active sound control unit

C3 | Not used | ---

C4 | AUX BEEP | Inputs system beep signal

C5 | AUX NAVI GND | Basis ground for terminals No. 4 and No. 12

C6 | Not used | ---

C7 | RS485- | Communication signal for audio-navigation unit or audio unit

C8 | Not used | ---

C9 * | ANC R+ | Inputs signal for acceleration sound enhancement from active sound control unit

C10 * | ANC F+ | Inputs signal for acceleration sound enhancement from active sound control unit

C11 | Not used | ---

C12 | AUX NAVI | Inputs sound signal for voice guidance and Voice Recognition (VR) prompts

C13 | Not used | ---

C14 | SWD+B | Inputs signal for stereo amplifier switching on/off

*:'20-21Type-R

Cavity | Terminal Name | Description

C15 | RS485+ | Communication signal for audio-navigation unit or audio unit

C16 | Not used | ---

*:'20-21Type-R

Stereo Amplifier Connector D (2P) (female terminals)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

D1 | SPDIF2 SIG | Communication signal for audio-navigation unit or audio unit

D2 | SPDIF2 SH | Shield for terminal No. 1
````

## Chunk 2495: Tuner Unit Connector for Inputs and Outputs

- Title: Tuner Unit Connector for Inputs and Outputs
- Source path: `pages\1456.html`
- Chunk ID: `chunk_31beb503af77`
- Images: `images\GHH399638.jpeg`, `images\GHH399639.jpeg`, `images\GHH399640.jpeg`
- Duplicate sources: `pages\1906.html`, `pages\25975.html`, `pages\13358.html`

### Full Text

````text
# Tuner Unit Connector for Inputs and Outputs

Connector Index

Tuner Unit Connector A (10P)

Tuner Unit Connector B (2P)

Tuner Unit Connector C (5P)

TUNER UNIT CONNECTOR A (10P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

A1 | TUNER 9V | Power source from audio-navigation unit or audio unit

A2 | TUNER GND | Ground for tuner unit

A3 | Not used | ---

A4 | Not used | ---

A5 | TUNER RS485+ | Communication signal for audio-navigation unit or audio unit

A6 | TUNER RS485 SH | Shield for terminals No. 5 and No. 7

A7 | TUNER RS485- | Communication signal for audio-navigation unit or audio unit

A8 | Not used | ---

A9 | Not used | ---

A10 | TUNER 6V | Power source from audio-navigation unit or audio unit

TUNER UNIT CONNECTOR B (2P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

B1 | SPDIF1 SIG | Communication signal for audio-navigation unit or audio unit

B2 | SPDIF1 SH | Shield for terminal No. 1

TUNER UNIT CONNECTOR C (5P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal Name | Description

C1 | ANT+B | Power source for AM/FM antenna amplifier

C2 | RF IN | Inputs AM/FM signal

C3 | Not used | ---

C4 | SH (RF IN) | Shield for terminal No. 2

C5 | Not used | ---
````

## Chunk 2496: How to Start LaneWatch Camera Aiming (2016 2017 2018): Procedure

- Title: How to Start LaneWatch Camera Aiming (2016 2017 2018): Procedure
- Source path: `pages\1457.html`
- Chunk ID: `chunk_9f70f7d83ac5`
- Images: `images\GHH172669.png`, `images\GHH29783.png`, `images\GHH399641.jpeg`, `images\GHH399642.jpeg`, `images\GHH399643.jpeg`, `images\GHH399644.jpeg`
- Duplicate sources: `pages\1907.html`, `pages\25976.html`, `pages\13359.html`

### Full Text

````text
# How to Start LaneWatch Camera Aiming (2016 2017 2018): Procedure

NOTE: Do not use this procedure before setting the LaneWatch camera aiming marker .

- LaneWatch Camera Aiming - Start 1. Do the LaneWatch camera aiming marker preparation 2. Turn the vehicle to the ON mode. 3. Press and hold the MENU button, the DISPLAY MODE ( Courtesy of HONDA, U.S.A., INC. ) button, and the AUDIO POWER ( Courtesy of HONDA, U.S.A., INC. ) button until the Select Diagnosis Items menu screen is displayed. Displaying Select Diagnosis Items Menu Screen Courtesy of HONDA, U.S.A., INC. 4. When the Select Diagnosis Items menu appears, select the Detail Information and Setting (A). 5. Select the Functional Setup icon (A). Courtesy of HONDA, U.S.A., INC. 6. Select the LaneWatch icon (A). Courtesy of HONDA, U.S.A., INC. 7. Select the Aiming Start icon (A). Courtesy of HONDA, U.S.A., INC.

1. Do the LaneWatch camera aiming marker preparation

2. Turn the vehicle to the ON mode.

3. Press and hold the MENU button, the DISPLAY MODE (

Courtesy of HONDA, U.S.A., INC.

) button, and the AUDIO POWER (

Courtesy of HONDA, U.S.A., INC.

) button until the Select Diagnosis Items menu screen is displayed.

Displaying Select Diagnosis Items Menu Screen

Courtesy of HONDA, U.S.A., INC.

4. When the Select Diagnosis Items menu appears, select the Detail Information and Setting (A).

5. Select the Functional Setup icon (A).

Courtesy of HONDA, U.S.A., INC.

6. Select the LaneWatch icon (A).

Courtesy of HONDA, U.S.A., INC.

7. Select the Aiming Start icon (A).

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2497: Audio Remote-HFL Switch Test: Test

- Title: Audio Remote-HFL Switch Test: Test
- Source path: `pages\1458.html`
- Chunk ID: `chunk_672ca019b7f6`
- Images: `images\GHH399645.jpeg`
- Duplicate sources: `pages\1908.html`, `pages\25977.html`, `pages\13360.html`

### Full Text

````text
# Audio Remote-HFL Switch Test: Test

- Steering Wheel Trim - Remove

- Audio Remote-HFL Switch - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 3 and No. 6 in each switch position according to the table. 2. Measure the resistance between terminals No. 6 and No. 9 in each switch position according to the table. 3. If the resistance is not as specified, replace the audio remote-HFL switch. Button Held Down Resistance No button pressed About 10 kΩ HANG-UP/BACK About 47 Ω PICK-UP About 222 Ω TALK About 2.25 kΩ Button Held Down Resistance No button pressed About 10 kΩ SOURCE About 3.7 kΩ Right (CH +) About 1.7 kΩ Left (CH -) About 775 Ω + (VOL.UP) About 357 Ω - (VOL.DOWN) About 99 Ω

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 3 and No. 6 in each switch position according to the table. 2. Measure the resistance between terminals No. 6 and No. 9 in each switch position according to the table. 3. If the resistance is not as specified, replace the audio remote-HFL switch.

2. Measure the resistance between terminals No. 6 and No. 9 in each switch position according to the table.

3. If the resistance is not as specified, replace the audio remote-HFL switch.

Button Held Down | Resistance

No button pressed | About 10 kΩ

HANG-UP/BACK | About 47 Ω

PICK-UP | About 222 Ω

TALK | About 2.25 kΩ

Button Held Down | Resistance

No button pressed | About 10 kΩ

SOURCE | About 3.7 kΩ

Right (CH +) | About 1.7 kΩ

Left (CH -) | About 775 Ω

+ (VOL.UP) | About 357 Ω

- (VOL.DOWN) | About 99 Ω

- All Removed Parts - Install 1. Install the audio remote-HFL switch in the reverse order of removal.

1. Install the audio remote-HFL switch in the reverse order of removal.
````

## Chunk 2498: AM radio reception changes at night (Display Audio Type (7-inch Screen))

- Title: AM radio reception changes at night (Display Audio Type (7-inch Screen))
- Source path: `pages\1459.html`
- Chunk ID: `chunk_1d91b477991f`
- Images: none
- Duplicate sources: `pages\1909.html`, `pages\25978.html`, `pages\13361.html`

### Full Text

````text
# AM radio reception changes at night (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- This is a system characteristic. AM radio stations are required by the government (FCC) to lower their power at night
````

## Chunk 2499: AM/FM radio display is blank or no station information is displayed (Display Audio Type (7-inch Screen))

- Title: AM/FM radio display is blank or no station information is displayed (Display Audio Type (7-inch Screen))
- Source path: `pages\1460.html`
- Chunk ID: `chunk_b15dd17564f7`
- Images: none
- Duplicate sources: `pages\1910.html`, `pages\25979.html`, `pages\13362.html`

### Full Text

````text
# AM/FM radio display is blank or no station information is displayed (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2500: AM/FM radio preset memory is lost (Color Audio Type (5-inch Screen))

- Title: AM/FM radio preset memory is lost (Color Audio Type (5-inch Screen))
- Source path: `pages\1461.html`
- Chunk ID: `chunk_538c576dcf58`
- Images: none
- Duplicate sources: `pages\1911.html`, `pages\25980.html`, `pages\13363.html`

### Full Text

````text
# AM/FM radio preset memory is lost (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Replace the audio unit

Also Check for

Internal error
````

## Chunk 2501: AM/FM radio preset memory is lost (Display Audio Type (7-inch Screen))

- Title: AM/FM radio preset memory is lost (Display Audio Type (7-inch Screen))
- Source path: `pages\1462.html`
- Chunk ID: `chunk_3f3215e13353`
- Images: none
- Duplicate sources: `pages\1912.html`, `pages\25981.html`, `pages\13364.html`

### Full Text

````text
# AM/FM radio preset memory is lost (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Replace the tuner unit

Also Check for

Internal error
````

## Chunk 2502: Active sound control does not work (Display Audio Type (7-inch Screen))

- Title: Active sound control does not work (Display Audio Type (7-inch Screen))
- Source path: `pages\1463.html`
- Chunk ID: `chunk_adac8b20600a`
- Images: none
- Duplicate sources: `pages\1913.html`, `pages\25982.html`, `pages\13365.html`

### Full Text

````text
# Active sound control does not work (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2503: Audio remote-HFL switch does not work properly (audio unit buttons work) (Color Audio Type (5-inch Screen))

- Title: Audio remote-HFL switch does not work properly (audio unit buttons work) (Color Audio Type (5-inch Screen))
- Source path: `pages\1464.html`
- Chunk ID: `chunk_1b97921bd9a7`
- Images: none
- Duplicate sources: `pages\1914.html`, `pages\25983.html`, `pages\13366.html`

### Full Text

````text
# Audio remote-HFL switch does not work properly (audio unit buttons work) (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2504: Audio remote-HFL switch does not work properly (audio unit buttons work) (Display Audio Type (7-inch Screen))

- Title: Audio remote-HFL switch does not work properly (audio unit buttons work) (Display Audio Type (7-inch Screen))
- Source path: `pages\1465.html`
- Chunk ID: `chunk_2e9c018594b5`
- Images: none
- Duplicate sources: `pages\1915.html`, `pages\25984.html`, `pages\13367.html`

### Full Text

````text
# Audio remote-HFL switch does not work properly (audio unit buttons work) (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2505: Audio system sound is weak or distorted (display is normal) (Color Audio Type (5-inch Screen))

- Title: Audio system sound is weak or distorted (display is normal) (Color Audio Type (5-inch Screen))
- Source path: `pages\1466.html`
- Chunk ID: `chunk_ad2fe39d8dbc`
- Images: none
- Duplicate sources: `pages\1916.html`, `pages\25985.html`, `pages\13368.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Fader and balance positions

- Aftermarket amplifier or speakers
````

## Chunk 2506: Audio system sound is weak or distorted (display is normal) (Display Audio Type (7-inch Screen))

- Title: Audio system sound is weak or distorted (display is normal) (Display Audio Type (7-inch Screen))
- Source path: `pages\1467.html`
- Chunk ID: `chunk_806deaa88be9`
- Images: none
- Duplicate sources: `pages\1917.html`, `pages\25986.html`, `pages\13369.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Fader and balance positions

- Aftermarket amplifier or speakers
````

## Chunk 2507: Audio unit button does not work (Color Audio Type (5-inch Screen))

- Title: Audio unit button does not work (Color Audio Type (5-inch Screen))
- Source path: `pages\1468.html`
- Chunk ID: `chunk_1e503b9a35fe`
- Images: none
- Duplicate sources: `pages\1918.html`, `pages\25987.html`, `pages\13370.html`

### Full Text

````text
# Audio unit button does not work (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Do the Knob Check in the System Diagnostic Mode

Also Check for

Check the connector for poor connections or loose terminals between the audio unit and the audio panel
````

## Chunk 2508: Audio unit button illumination does not work (Color Audio Type (5-inch Screen))

- Title: Audio unit button illumination does not work (Color Audio Type (5-inch Screen))
- Source path: `pages\1469.html`
- Chunk ID: `chunk_5c254ff32e5b`
- Images: none
- Duplicate sources: `pages\1919.html`, `pages\25988.html`, `pages\13371.html`

### Full Text

````text
# Audio unit button illumination does not work (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2509: Audio unit does not exit anti-theft mode (Color Audio Type (5-inch Screen))

- Title: Audio unit does not exit anti-theft mode (Color Audio Type (5-inch Screen))
- Source path: `pages\1470.html`
- Chunk ID: `chunk_8ba64ad35746`
- Images: none
- Duplicate sources: `pages\1920.html`, `pages\25989.html`, `pages\13372.html`

### Full Text

````text
# Audio unit does not exit anti-theft mode (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Anti-Theft Feature
````

## Chunk 2510: Audio unit does not exit anti-theft mode (Display Audio Type (7-inch Screen))

- Title: Audio unit does not exit anti-theft mode (Display Audio Type (7-inch Screen))
- Source path: `pages\1471.html`
- Chunk ID: `chunk_2e01848a8d32`
- Images: none
- Duplicate sources: `pages\1921.html`, `pages\25990.html`, `pages\13373.html`

### Full Text

````text
# Audio unit does not exit anti-theft mode (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Anti-Theft Feature
````

## Chunk 2511: Audio unit will not turn on (No information display) (Color Audio Type (5-inch Screen))

- Title: Audio unit will not turn on (No information display) (Color Audio Type (5-inch Screen))
- Source path: `pages\1472.html`
- Chunk ID: `chunk_e67426caee8a`
- Images: none
- Duplicate sources: `pages\1922.html`, `pages\25991.html`, `pages\13374.html`

### Full Text

````text
# Audio unit will not turn on (No information display) (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2512: Audio unit will not turn on (No information display) (Display Audio Type (7-inch Screen))

- Title: Audio unit will not turn on (No information display) (Display Audio Type (7-inch Screen))
- Source path: `pages\1473.html`
- Chunk ID: `chunk_6d8587ac975c`
- Images: none
- Duplicate sources: `pages\1923.html`, `pages\25992.html`, `pages\13375.html`

### Full Text

````text
# Audio unit will not turn on (No information display) (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2513: Audio-navigation unit power will not turn on (No information display)

- Title: Audio-navigation unit power will not turn on (No information display)
- Source path: `pages\1474.html`
- Chunk ID: `chunk_15b8e64e76c6`
- Images: none
- Duplicate sources: `pages\1924.html`, `pages\25993.html`, `pages\13376.html`

### Full Text

````text
# Audio-navigation unit power will not turn on (No information display)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Blown fuses

- Screen settings

- Error Messages

- Software not up to date
````

## Chunk 2514: Bluetooth audio does not work

- Title: Bluetooth audio does not work
- Source path: `pages\1475.html`
- Chunk ID: `chunk_877b3441e925`
- Images: none
- Duplicate sources: `pages\1925.html`, `pages\25994.html`, `pages\13377.html`

### Full Text

````text
# Bluetooth audio does not work

Diagnostic Procedure

Check the Bluetooth module:

- With display audio: Do the HFT/Mic in the System Diagnostic Mode

- With color audio: Do the Version Display in the System Diagnostic Mode

Also Check for

Bluetooth audio device compatibility (see the Owner's Manual)
````

## Chunk 2515: Bluetooth audio does not work (Color Audio Type (5-inch Screen))

- Title: Bluetooth audio does not work (Color Audio Type (5-inch Screen))
- Source path: `pages\1476.html`
- Chunk ID: `chunk_09ef5336f359`
- Images: none
- Duplicate sources: `pages\1926.html`, `pages\25995.html`, `pages\13378.html`

### Full Text

````text
# Bluetooth audio does not work (Color Audio Type (5-inch Screen))

Also Check for

Bluetooth phone compatibility (see the Owner's Manual)
````

## Chunk 2516: Bluetooth audio does not work (Display Audio Type (7-inch Screen))

- Title: Bluetooth audio does not work (Display Audio Type (7-inch Screen))
- Source path: `pages\1477.html`
- Chunk ID: `chunk_6b35a88dd39f`
- Images: none
- Duplicate sources: `pages\1927.html`, `pages\25996.html`, `pages\13379.html`

### Full Text

````text
# Bluetooth audio does not work (Display Audio Type (7-inch Screen))

Also Check for

Bluetooth phone compatibility (see the Owner's Manual)
````

## Chunk 2517: Center display unit button does not work (Display Audio Type (7-inch Screen))

- Title: Center display unit button does not work (Display Audio Type (7-inch Screen))
- Source path: `pages\1478.html`
- Chunk ID: `chunk_ad936fe5cab1`
- Images: none
- Duplicate sources: `pages\1928.html`, `pages\25997.html`, `pages\13380.html`

### Full Text

````text
# Center display unit button does not work (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Do the Hard Key in the System Diagnostic Mode

Also Check for

Check the Touch Panel Sensitivity in the System Settings
````

## Chunk 2518: Center display unit does not dim (Display Audio Type (7-inch Screen))

- Title: Center display unit does not dim (Display Audio Type (7-inch Screen))
- Source path: `pages\1479.html`
- Chunk ID: `chunk_b8f724403e85`
- Images: none
- Duplicate sources: `pages\1929.html`, `pages\25998.html`, `pages\13381.html`

### Full Text

````text
# Center display unit does not dim (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2519: Excessive transition between analog broadcast and digital HD Radio (TM) broadcast (Display Audio Type (7-inch Screen))

- Title: Excessive transition between analog broadcast and digital HD Radio (TM) broadcast (Display Audio Type (7-inch Screen))
- Source path: `pages\1481.html`
- Chunk ID: `chunk_d11b9b71ffb6`
- Images: none
- Duplicate sources: `pages\1931.html`, `pages\26000.html`, `pages\13383.html`

### Full Text

````text
# Excessive transition between analog broadcast and digital HD Radio (TM) broadcast (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Receiver is located near the edge of the digital HD Radio (TM) coverage area. Refer to www.hdradio.com to verify radio stations in your coverage area
````

## Chunk 2520: HD Radio (TM) changes HD channel on its own (Display Audio Type (7-inch Screen))

- Title: HD Radio (TM) changes HD channel on its own (Display Audio Type (7-inch Screen))
- Source path: `pages\1482.html`
- Chunk ID: `chunk_30804a81441e`
- Images: none
- Duplicate sources: `pages\1932.html`, `pages\26001.html`, `pages\13384.html`

### Full Text

````text
# HD Radio (TM) changes HD channel on its own (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- This is intended behavior. HD Radio (TM) is set to revert to main channel after extended loss of HD2/HD3 broadcast
````

## Chunk 2521: HFL does not work properly

- Title: HFL does not work properly
- Source path: `pages\1483.html`
- Chunk ID: `chunk_d400942e704b`
- Images: none
- Duplicate sources: `pages\1933.html`, `pages\26002.html`, `pages\13385.html`

### Full Text

````text
# HFL does not work properly

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Bluetooth cell phone compatibility (see the Owner's Manual)
````

## Chunk 2522: LaneWatch camera image does not come on

- Title: LaneWatch camera image does not come on
- Source path: `pages\1484.html`
- Chunk ID: `chunk_712921e58ba6`
- Images: none
- Duplicate sources: `pages\1934.html`, `pages\26003.html`, `pages\13386.html`

### Full Text

````text
# LaneWatch camera image does not come on

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Navigation DTCs
````

## Chunk 2523: LaneWatch camera image does not come on (Display Audio Type (7-inch Screen))

- Title: LaneWatch camera image does not come on (Display Audio Type (7-inch Screen))
- Source path: `pages\1485.html`
- Chunk ID: `chunk_d5d0531990f1`
- Images: none
- Duplicate sources: `pages\1935.html`, `pages\26004.html`, `pages\13387.html`

### Full Text

````text
# LaneWatch camera image does not come on (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Audio DTCs
````

## Chunk 2524: Navigation system stays on the CSF screen

- Title: Navigation system stays on the CSF screen
- Source path: `pages\1486.html`
- Chunk ID: `chunk_a1b2bd54df78`
- Images: none
- Duplicate sources: `pages\1936.html`, `pages\26005.html`, `pages\13388.html`

### Full Text

````text
# Navigation system stays on the CSF screen

Diagnostic Procedure

- Navigation DTCs

Also Check for

- GPS Initialization

- Aftermarket metallic window tint on the front window or electronic aftermarket accessories (possibly hidden) mounted near the GPS antenna or the audio-navigation unit

- Disconnected or defective GPS antenna
````

## Chunk 2525: Navigation touch panel does not work

- Title: Navigation touch panel does not work
- Source path: `pages\1487.html`
- Chunk ID: `chunk_45f76d9e4108`
- Images: none
- Duplicate sources: `pages\1937.html`, `pages\26006.html`, `pages\13389.html`

### Full Text

````text
# Navigation touch panel does not work

Diagnostic Procedure

- Do the Touch Panel Check in the System Diagnostic Mode

Also Check for

Forced Rebooting of Audio-Navigation Unit
````

## Chunk 2526: No HD traffic information

- Title: No HD traffic information
- Source path: `pages\1488.html`
- Chunk ID: `chunk_4e713fcf1c62`
- Images: none
- Duplicate sources: `pages\1938.html`, `pages\26007.html`, `pages\13390.html`

### Full Text

````text
# No HD traffic information

Diagnostic Procedure

- Go to AM/FM radio display is blank or no station information is displayed troubleshooting

Also Check for

Local outage or no local broadcast. Compare to a known-good vehicle of the same year and trim.
````

## Chunk 2527: No sound is heard from all the speakers (display is normal) (Color Audio Type (5-inch Screen))

- Title: No sound is heard from all the speakers (display is normal) (Color Audio Type (5-inch Screen))
- Source path: `pages\1489.html`
- Chunk ID: `chunk_7d7822eb8910`
- Images: none
- Duplicate sources: `pages\1939.html`, `pages\26008.html`, `pages\13391.html`

### Full Text

````text
# No sound is heard from all the speakers (display is normal) (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Aftermarket amplifier or speakers
````

## Chunk 2528: No sound is heard from all the speakers (display is normal) (Display Audio Type (7-inch Screen))

- Title: No sound is heard from all the speakers (display is normal) (Display Audio Type (7-inch Screen))
- Source path: `pages\1490.html`
- Chunk ID: `chunk_b4fedc099e8c`
- Images: none
- Duplicate sources: `pages\1940.html`, `pages\26009.html`, `pages\13392.html`

### Full Text

````text
# No sound is heard from all the speakers (display is normal) (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Aftermarket amplifier or speakers
````

## Chunk 2529: Pandora is not is displayed as an audio source (Display Audio Type (7-inch Screen))

- Title: Pandora is not is displayed as an audio source (Display Audio Type (7-inch Screen))
- Source path: `pages\1491.html`
- Chunk ID: `chunk_27fbe1cfd644`
- Images: none
- Duplicate sources: `pages\1941.html`, `pages\26010.html`, `pages\13393.html`

### Full Text

````text
# Pandora is not is displayed as an audio source (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Do the PANDORA in the System Diagnostic Mode to check the Pandora settings is abled
````

## Chunk 2530: Poor AM or FM radio reception or interference (Color Audio Type (5-inch Screen))

- Title: Poor AM or FM radio reception or interference (Color Audio Type (5-inch Screen))
- Source path: `pages\1492.html`
- Chunk ID: `chunk_347fc09e2885`
- Images: none
- Duplicate sources: `pages\1942.html`, `pages\26011.html`, `pages\13394.html`

### Full Text

````text
# Poor AM or FM radio reception or interference (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Check radio reception: Do the FM or AM in the System Diagnostic Mode

- Aftermarket FM modulator

- Loose antenna amplifier mounting bolt
````

## Chunk 2531: Poor GPS reception or interference

- Title: Poor GPS reception or interference
- Source path: `pages\1493.html`
- Chunk ID: `chunk_28666ae8d1da`
- Images: none
- Duplicate sources: `pages\1943.html`, `pages\26012.html`, `pages\13395.html`

### Full Text

````text
# Poor GPS reception or interference

Diagnostic Procedure

- Do the GPS Information in the System Diagnostic Mode

Also Check for

- Global Positioning System (GPS) Limitations

- Aftermarket metallic window tint on the front window or electronic aftermarket accessories (possibly hidden) mounted near the GPS antenna or the audio-navigation unit
````

## Chunk 2532: Poor or no sound with AM/FM radio (Display Audio Type (7-inch Screen))

- Title: Poor or no sound with AM/FM radio (Display Audio Type (7-inch Screen))
- Source path: `pages\1494.html`
- Chunk ID: `chunk_bf99c1a8cfd8`
- Images: none
- Duplicate sources: `pages\1944.html`, `pages\26013.html`, `pages\13396.html`

### Full Text

````text
# Poor or no sound with AM/FM radio (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Check radio reception: Do the Remote Tuner in the System Diagnostic Mode

- Aftermarket FM modulator

- Loose antenna mounting nut

- Loose antenna amplifier mounting bolt
````

## Chunk 2533: Rearview camera image does not change when selecting different views

- Title: Rearview camera image does not change when selecting different views
- Source path: `pages\1495.html`
- Chunk ID: `chunk_0e1a3b79f4cf`
- Images: none
- Duplicate sources: `pages\1945.html`, `pages\26014.html`, `pages\13397.html`

### Full Text

````text
# Rearview camera image does not change when selecting different views

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2534: Rearview camera image does not change when selecting different views (Color Audio Type (5-inch Screen))

- Title: Rearview camera image does not change when selecting different views (Color Audio Type (5-inch Screen))
- Source path: `pages\1496.html`
- Chunk ID: `chunk_31ef3f936365`
- Images: none
- Duplicate sources: `pages\1946.html`, `pages\26015.html`, `pages\13398.html`

### Full Text

````text
# Rearview camera image does not change when selecting different views (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2535: Rearview camera image does not change when selecting different views (Display Audio Type (7-inch Screen))

- Title: Rearview camera image does not change when selecting different views (Display Audio Type (7-inch Screen))
- Source path: `pages\1497.html`
- Chunk ID: `chunk_11f822c4ee97`
- Images: none
- Duplicate sources: `pages\1947.html`, `pages\26016.html`, `pages\13399.html`

### Full Text

````text
# Rearview camera image does not change when selecting different views (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2536: Rearview camera image does not come on (Color Audio Type (5-inch Screen))

- Title: Rearview camera image does not come on (Color Audio Type (5-inch Screen))
- Source path: `pages\1499.html`
- Chunk ID: `chunk_f0e71fe33238`
- Images: none
- Duplicate sources: `pages\1949.html`, `pages\26018.html`, `pages\13401.html`

### Full Text

````text
# Rearview camera image does not come on (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2537: Rearview camera image does not come on (Display Audio Type (7-inch Screen))

- Title: Rearview camera image does not come on (Display Audio Type (7-inch Screen))
- Source path: `pages\1500.html`
- Chunk ID: `chunk_9b416dcc09c8`
- Images: none
- Duplicate sources: `pages\1950.html`, `pages\26019.html`, `pages\13402.html`

### Full Text

````text
# Rearview camera image does not come on (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2538: System always comes up in-line diagnostic mode

- Title: System always comes up in-line diagnostic mode
- Source path: `pages\1501.html`
- Chunk ID: `chunk_58434c433db1`
- Images: none
- Duplicate sources: `pages\1951.html`, `pages\26020.html`, `pages\13403.html`

### Full Text

````text
# System always comes up in-line diagnostic mode

Diagnostic Procedure

- Factory diagnostic screen In Line Diagnostic mode
````

## Chunk 2539: System always comes up in-line diagnostic mode (without navigation) (Display Audio Type (7-inch Screen))

- Title: System always comes up in-line diagnostic mode (without navigation) (Display Audio Type (7-inch Screen))
- Source path: `pages\1502.html`
- Chunk ID: `chunk_f4dcf0e05804`
- Images: none
- Duplicate sources: `pages\1952.html`, `pages\26021.html`, `pages\13404.html`

### Full Text

````text
# System always comes up in-line diagnostic mode (without navigation) (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Factory diagnostic screen In Line Diag
````

## Chunk 2540: The Honda approved Bluetooth cell phone cannot use all its functions

- Title: The Honda approved Bluetooth cell phone cannot use all its functions
- Source path: `pages\1503.html`
- Chunk ID: `chunk_1bb4d77479ff`
- Images: none
- Duplicate sources: `pages\1953.html`, `pages\26022.html`, `pages\13405.html`

### Full Text

````text
# The Honda approved Bluetooth cell phone cannot use all its functions

Diagnostic Procedure

- HFL System Troubleshooting
````

## Chunk 2541: The Honda approved Bluetooth cell phone does not place or receive calls using the HFL system

- Title: The Honda approved Bluetooth cell phone does not place or receive calls using the HFL system
- Source path: `pages\1504.html`
- Chunk ID: `chunk_67e988eb383a`
- Images: none
- Duplicate sources: `pages\1954.html`, `pages\26023.html`, `pages\13406.html`

### Full Text

````text
# The Honda approved Bluetooth cell phone does not place or receive calls using the HFL system

Diagnostic Procedure

- HFL System Troubleshooting
````

## Chunk 2542: The Honda approved Bluetooth cell phone is having problems pairing to the vehicle

- Title: The Honda approved Bluetooth cell phone is having problems pairing to the vehicle
- Source path: `pages\1505.html`
- Chunk ID: `chunk_9da6e8a85207`
- Images: none
- Duplicate sources: `pages\1955.html`, `pages\26024.html`, `pages\13407.html`

### Full Text

````text
# The Honda approved Bluetooth cell phone is having problems pairing to the vehicle

Diagnostic Procedure

- HFL System Troubleshooting
````

## Chunk 2543: The MID does not display the audio unit information (Display Audio Type (7-inch Screen))

- Title: The MID does not display the audio unit information (Display Audio Type (7-inch Screen))
- Source path: `pages\1506.html`
- Chunk ID: `chunk_b8cbd5e4828a`
- Images: none
- Duplicate sources: `pages\1956.html`, `pages\26025.html`, `pages\13408.html`

### Full Text

````text
# The MID does not display the audio unit information (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2544: The MID does not display the audio-navigation unit information

- Title: The MID does not display the audio-navigation unit information
- Source path: `pages\1507.html`
- Chunk ID: `chunk_c17a32c67528`
- Images: none
- Duplicate sources: `pages\1957.html`, `pages\26026.html`, `pages\13409.html`

### Full Text

````text
# The MID does not display the audio-navigation unit information

Diagnostic Procedure

- Symptom Troubleshooting
````

## Chunk 2545: USB device does not function (Color Audio Type (5-inch Screen))

- Title: USB device does not function (Color Audio Type (5-inch Screen))
- Source path: `pages\1508.html`
- Chunk ID: `chunk_e63fd35b1b6a`
- Images: none
- Duplicate sources: `pages\1958.html`, `pages\26027.html`, `pages\13410.html`

### Full Text

````text
# USB device does not function (Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Error Messages

- USB device compatibility (see the Owner's Manual)
````

## Chunk 2546: USB device does not function (Display Audio Type (7-inch Screen))

- Title: USB device does not function (Display Audio Type (7-inch Screen))
- Source path: `pages\1509.html`
- Chunk ID: `chunk_6fe73c37de68`
- Images: none
- Duplicate sources: `pages\1959.html`, `pages\26028.html`, `pages\13411.html`

### Full Text

````text
# USB device does not function (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Error messages

- USB device compatibility (see the Owner's Manual)
````

## Chunk 2547: Vehicle position icon wanders across the map when driving (does not follow a displayed road) or map vehicle ICON spins

- Title: Vehicle position icon wanders across the map when driving (does not follow a displayed road) or map vehicle ICON spins
- Source path: `pages\1510.html`
- Chunk ID: `chunk_b8c5262ad01a`
- Images: none
- Duplicate sources: `pages\1960.html`, `pages\26029.html`, `pages\13412.html`

### Full Text

````text
# Vehicle position icon wanders across the map when driving (does not follow a displayed road) or map vehicle ICON spins

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Global Positioning System (GPS) Limitations

- Map Matching

- Sensor Calibration

- VSP missing

- Poor or no GPS reception

- Check for any related service bulletin software updates
````

## Chunk 2548: Voice control does not work/respond

- Title: Voice control does not work/respond
- Source path: `pages\1511.html`
- Chunk ID: `chunk_9e263eb0e639`
- Images: none
- Duplicate sources: `pages\1961.html`, `pages\26030.html`, `pages\13413.html`

### Full Text

````text
# Voice control does not work/respond

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Check for any related service bulletin software updates
````

## Chunk 2549: Voice guidance cannot be heard, is broken up, or there is static

- Title: Voice guidance cannot be heard, is broken up, or there is static
- Source path: `pages\1512.html`
- Chunk ID: `chunk_ca8190aae7c4`
- Images: none
- Duplicate sources: `pages\1962.html`, `pages\26031.html`, `pages\13414.html`

### Full Text

````text
# Voice guidance cannot be heard, is broken up, or there is static

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Volume or voice feedback setting (see the Navigation System Manual)
````

## Chunk 2550: Volume does not increase with speed(Color Audio Type (5-inch Screen))

- Title: Volume does not increase with speed(Color Audio Type (5-inch Screen))
- Source path: `pages\1513.html`
- Chunk ID: `chunk_b67cb6f64ea6`
- Images: none
- Duplicate sources: `pages\1963.html`, `pages\26032.html`, `pages\13415.html`

### Full Text

````text
# Volume does not increase with speed(Color Audio Type (5-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Speed-sensitive Volume Control settings (see the Owner's Manual)
````

## Chunk 2551: Volume does not increase with speed (Display Audio Type (7-inch Screen))

- Title: Volume does not increase with speed (Display Audio Type (7-inch Screen))
- Source path: `pages\1514.html`
- Chunk ID: `chunk_6e9489efd65d`
- Images: none
- Duplicate sources: `pages\1964.html`, `pages\26033.html`, `pages\13416.html`

### Full Text

````text
# Volume does not increase with speed (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

Speed-sensitive Volume Control settings (see the Owner's Manual)
````

## Chunk 2552: Volume is too high or too low when driving at freeway speeds (Color Audio Type (5-inch Screen))

- Title: Volume is too high or too low when driving at freeway speeds (Color Audio Type (5-inch Screen))
- Source path: `pages\1515.html`
- Chunk ID: `chunk_ae19ee298ea0`
- Images: none
- Duplicate sources: `pages\1965.html`, `pages\26034.html`, `pages\13417.html`

### Full Text

````text
# Volume is too high or too low when driving at freeway speeds (Color Audio Type (5-inch Screen))

Also Check for

Speed-sensitive Volume Control settings (see the Owner's Manual)
````

## Chunk 2553: Volume is too high or too low when driving at freeway speeds (Display Audio Type (7-inch Screen))

- Title: Volume is too high or too low when driving at freeway speeds (Display Audio Type (7-inch Screen))
- Source path: `pages\1516.html`
- Chunk ID: `chunk_bd009c2018f8`
- Images: none
- Duplicate sources: `pages\1966.html`, `pages\26035.html`, `pages\13418.html`

### Full Text

````text
# Volume is too high or too low when driving at freeway speeds (Display Audio Type (7-inch Screen))

Also Check for

Speed-sensitive Volume Control settings (see the Owner's Manual)
````

## Chunk 2554: XM radio display is blank and no station information is displayed (Display Audio Type (7-inch Screen))

- Title: XM radio display is blank and no station information is displayed (Display Audio Type (7-inch Screen))
- Source path: `pages\1517.html`
- Chunk ID: `chunk_e1cb9e3356c2`
- Images: none
- Duplicate sources: `pages\1967.html`, `pages\26036.html`, `pages\13419.html`

### Full Text

````text
# XM radio display is blank and no station information is displayed (Display Audio Type (7-inch Screen))

Diagnostic Procedure

- With navigation: Navigation DTCs

- Without navigation: Audio DTCs

Also Check for

Error messages
````

## Chunk 2555: Audio and Visual System Circuit Diagram (5-door with Navigation) (2017 2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (5-door with Navigation) (2017 2018 2019 2020 2021)
- Source path: `pages\1518.html`
- Chunk ID: `chunk_46ff660ff1ae`
- Images: `images\GHH399646.jpeg`, `images\GHH399647.jpeg`, `images\GHH399648.jpeg`, `images\GHH399649.jpeg`, `images\GHH399650.jpeg`, `images\GHH399651.jpeg`, `images\GHH399652.jpeg`, `images\GHH399653.jpeg`
- Duplicate sources: `pages\1968.html`, `pages\26037.html`, `pages\13420.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (5-door with Navigation) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2556: Audio and Visual System Circuit Diagram (5-door: Without Navigation, Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (5-door: Without Navigation, Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1519.html`
- Chunk ID: `chunk_260567b8c738`
- Images: `images\GHH399654.jpeg`, `images\GHH399655.jpeg`, `images\GHH399656.jpeg`, `images\GHH399657.jpeg`
- Duplicate sources: `pages\1969.html`, `pages\26038.html`, `pages\13421.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (5-door: Without Navigation, Color Audio Type (5-inch Screen)) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2557: Audio and Visual System Circuit Diagram (5-door: Without Navigation, Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (5-door: Without Navigation, Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)
- Source path: `pages\1520.html`
- Chunk ID: `chunk_63f7e766484f`
- Images: `images\GHH399658.jpeg`, `images\GHH399659.jpeg`, `images\GHH399660.jpeg`, `images\GHH399661.jpeg`, `images\GHH399662.jpeg`, `images\GHH399663.jpeg`, `images\GHH399664.jpeg`, `images\GHH399665.jpeg`
- Duplicate sources: `pages\1970.html`, `pages\26039.html`, `pages\13422.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (5-door: Without Navigation, Display Audio Type (7-inch Screen)) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2558: Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Color Audio Type (5-inch Screen)) (2016 2017 2018)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Color Audio Type (5-inch Screen)) (2016 2017 2018)
- Source path: `pages\1521.html`
- Chunk ID: `chunk_b92026318107`
- Images: `images\GHH399666.jpeg`, `images\GHH399667.jpeg`, `images\GHH399668.jpeg`
- Duplicate sources: `pages\1971.html`, `pages\26040.html`, `pages\13423.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Color Audio Type (5-inch Screen)) (2016 2017 2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2559: Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1522.html`
- Chunk ID: `chunk_58c57648d4cd`
- Images: `images\GHH399669.jpeg`, `images\GHH399670.jpeg`, `images\GHH399671.jpeg`, `images\GHH399672.jpeg`, `images\GHH399673.jpeg`, `images\GHH399674.jpeg`
- Duplicate sources: `pages\1972.html`, `pages\26041.html`, `pages\13424.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4 door: Without Navigation, Display Audio Type (7-inch Screen)) (2016 2017 2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2560: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2016 2017 2018)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2016 2017 2018)
- Source path: `pages\1523.html`
- Chunk ID: `chunk_b727c4a31c0d`
- Images: `images\GHH399675.jpeg`, `images\GHH399676.jpeg`, `images\GHH399677.jpeg`, `images\GHH399678.jpeg`, `images\GHH399679.jpeg`, `images\GHH399680.jpeg`
- Duplicate sources: `pages\1973.html`, `pages\26042.html`, `pages\13425.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2016 2017 2018)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2561: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2018 2019 2020 2021)
- Source path: `pages\1524.html`
- Chunk ID: `chunk_bf90c7e86475`
- Images: `images\GHH399681.jpeg`, `images\GHH399682.jpeg`, `images\GHH399683.jpeg`, `images\GHH399684.jpeg`, `images\GHH399685.jpeg`, `images\GHH399686.jpeg`, `images\GHH399687.jpeg`, `images\GHH399688.jpeg`
- Duplicate sources: `pages\1974.html`, `pages\26043.html`, `pages\13426.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: With Navigation) (2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2562: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1525.html`
- Chunk ID: `chunk_5532983b3d79`
- Images: `images\GHH399689.jpeg`, `images\GHH399690.jpeg`, `images\GHH399691.jpeg`
- Duplicate sources: `pages\1975.html`, `pages\26044.html`, `pages\13427.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2563: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1526.html`
- Chunk ID: `chunk_51452f633eae`
- Images: `images\GHH399692.jpeg`, `images\GHH399693.jpeg`, `images\GHH399694.jpeg`, `images\GHH399695.jpeg`, `images\GHH399696.jpeg`, `images\GHH399697.jpeg`, `images\GHH399698.jpeg`, `images\GHH399699.jpeg`
- Duplicate sources: `pages\1976.html`, `pages\26045.html`, `pages\13428.html`

### Full Text

````text
# Audio and Visual System Circuit Diagram (KA/KC models 2/4-door: Without Navigation, Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2564: Window Antenna Repair: Reconditioning

- Title: Window Antenna Repair: Reconditioning
- Source path: `pages\1527.html`
- Chunk ID: `chunk_57fa634b7fcc`
- Images: `images\GHH399700.jpeg`, `images\GHH399701.jpeg`
- Duplicate sources: `pages\1977.html`, `pages\26046.html`, `pages\13429.html`

### Full Text

````text
# Window Antenna Repair: Reconditioning

- Window Antenna - Repair Courtesy of HONDA, U.S.A., INC. NOTE: To make an effective repair, the broken section must be no longer than 25 mm (1.0 in). 1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol. 2. Carefully mask above and below the broken area of the window antenna wire (B) with cellophane tapes (C). Courtesy of HONDA, U.S.A., INC. 3. Using a small brush, apply a heavy coat of silver conductive paint (commercially available) (A) extending about 3.0 mm (0.1 in) on both sides of the break. Allow 25 minutes to dry. 4. Do the function test to confirm that the wire is repaired. 5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.

Courtesy of HONDA, U.S.A., INC. | NOTE: To make an effective repair, the broken section must be no longer than 25 mm (1.0 in). 1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol. 2. Carefully mask above and below the broken area of the window antenna wire (B) with cellophane tapes (C).

1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol.

2. Carefully mask above and below the broken area of the window antenna wire (B) with cellophane tapes (C).

Courtesy of HONDA, U.S.A., INC. | 3. Using a small brush, apply a heavy coat of silver conductive paint (commercially available) (A) extending about 3.0 mm (0.1 in) on both sides of the break. Allow 25 minutes to dry. 4. Do the function test to confirm that the wire is repaired. 5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.

4. Do the function test to confirm that the wire is repaired.

5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.
````

## Chunk 2565: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1528.html`
- Chunk ID: `chunk_5808a8f84ab5`
- Images: `images\GHH399702.jpeg`
- Duplicate sources: `pages\1978.html`, `pages\25940.html`, `pages\13167.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

- C-Pillar Trim - Remove

- AM/FM Antenna Amplifier - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connectors (A). 2. Remove the AM/FM antenna amplifier (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connectors (A). 2. Remove the AM/FM antenna amplifier (B).

2. Remove the AM/FM antenna amplifier (B).

- All Removed Parts - Install 1. Install the AM/FM antenna amplifier in the reverse order of removal.

1. Install the AM/FM antenna amplifier in the reverse order of removal.
````

## Chunk 2566: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\1529.html`
- Chunk ID: `chunk_b329d6a5873b`
- Images: none
- Duplicate sources: `pages\1979.html`, `pages\11361.html`, `pages\11363.html`, `pages\11365.html`, `pages\11368.html`, `pages\25941.html`, `pages\13168.html`, `pages\15432.html`, `pages\15434.html`, `pages\15436.html`, `pages\15439.html`

### Full Text

````text
# Removal and Installation: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.
````

## Chunk 2567: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\1530.html`
- Chunk ID: `chunk_d3fafdbf327f`
- Images: `images\GHH399703.jpeg`, `images\GHH399704.png`
- Duplicate sources: `pages\1980.html`, `pages\25942.html`, `pages\13169.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Courtesy of HONDA, U.S.A., INC.

Torque: N.m (kgf.m, lbf.ft)

- Glove Box Back Cover - Remove

- Active Sound Control Unit - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 2568: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1531.html`
- Chunk ID: `chunk_771c79d91735`
- Images: `images\GHH399705.jpeg`, `images\GHH399706.jpeg`, `images\GHH399707.jpeg`
- Duplicate sources: `pages\1981.html`, `pages\25943.html`, `pages\13170.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

- Driver's Airbag - Remove

- Steering Wheel Trim - Remove Mexico models (Type-R) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. USA and Canada models, or Mexico models (except Type-R) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Remove the screw(s) (A). 2. Remove the steering wheel trim (B). 3. Disconnect the connector(s) (C).

Mexico models (Type-R) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. USA and Canada models, or Mexico models (except Type-R) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Remove the screw(s) (A). 2. Remove the steering wheel trim (B). 3. Disconnect the connector(s) (C).

USA and Canada models, or Mexico models (except Type-R)

2. Remove the steering wheel trim (B).

3. Disconnect the connector(s) (C).

- Audio Remote-HFL Switch - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the audio remote-HFL switch in the reverse order of removal.

1. Install the audio remote-HFL switch in the reverse order of removal.
````

## Chunk 2569: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1532.html`
- Chunk ID: `chunk_d4902a4a8780`
- Images: `images\GHH399708.jpeg`, `images\GHH399709.jpeg`, `images\GHH399710.jpeg`, `images\GHH399711.jpeg`, `images\GHH399712.jpeg`
- Duplicate sources: `pages\1982.html`, `pages\25944.html`, `pages\13171.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE:

- When working on electronic components, make sure the work area is clean and dust free.

- Make sure your hands are clean and free of oils and grease.

- If you are replacing the audio unit, write down the audio presets (if possible), and enter them into the new audio unit.

- Center Console Side Trim (Both Side) - Remove

- Climate Control Panel - Remove

- Audio Unit Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolts (A). 2. Remove the harness clip (B). Courtesy of HONDA, U.S.A., INC. 3. Pull out the audio unit assembly (A) slightly. 4. Disconnect the connectors form the audio unit, and remove it.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolts (A). 2. Remove the harness clip (B).

2. Remove the harness clip (B).

Courtesy of HONDA, U.S.A., INC. | 3. Pull out the audio unit assembly (A) slightly. 4. Disconnect the connectors form the audio unit, and remove it.

4. Disconnect the connectors form the audio unit, and remove it.

- Audio Unit Bracket - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Audio Cover - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Audio Unit - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Discharge static electricity from your body before and during the work. Do not touch the circuit board(s) with your bare hands. Do not touch the flexible printed circuit connector of the audio panel and the audio unit with your bare hands (If you have touched it, wipe it off thoroughly). 1. Remove the audio unit (A) from the audio panel (B). 2. Disconnect the flexible printed circuit (C).

Courtesy of HONDA, U.S.A., INC. | NOTE: Discharge static electricity from your body before and during the work. Do not touch the circuit board(s) with your bare hands. Do not touch the flexible printed circuit connector of the audio panel and the audio unit with your bare hands (If you have touched it, wipe it off thoroughly). 1. Remove the audio unit (A) from the audio panel (B). 2. Disconnect the flexible printed circuit (C).

- Discharge static electricity from your body before and during the work.

- Do not touch the circuit board(s) with your bare hands.

- Do not touch the flexible printed circuit connector of the audio panel and the audio unit with your bare hands (If you have touched it, wipe it off thoroughly).

1. Remove the audio unit (A) from the audio panel (B).

2. Disconnect the flexible printed circuit (C).

- All Removed Parts - Install 1. Install the audio unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.

1. Install the audio unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.

- Make sure all the connectors are secure.

- After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.
````

## Chunk 2570: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1533.html`
- Chunk ID: `chunk_f20f3733eb91`
- Images: `images\GHH399713.jpeg`, `images\GHH399714.jpeg`, `images\GHH399715.jpeg`, `images\GHH399716.jpeg`
- Duplicate sources: `pages\1983.html`, `pages\25945.html`, `pages\13172.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE:

- When working on electronic components, make sure the work area is clean and dust free.

- Make sure your hands are clean and free of oils and grease.

- If you are replacing the audio unit, write down the audio presets (if possible), and enter them into the new audio unit.

- With XM: If you are replacing the audio unit, register the new XM I.D. number by calling 800-852-9696. The XM I.D can be found on a label attached to the audio unit.

- Center Console Side Trim (Both Side) - Remove

- Climate Control Panel - Remove

- Audio Unit Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolts (A). 2. Disconnect the connector (B) from the center display unit. 3. Remove the harness clip (C). Courtesy of HONDA, U.S.A., INC. 4. Pull out the audio unit assembly (A) slightly. NOTE: Do not grab the top edge of the center display unit (B) when removing the audio unit. 5. Disconnect the connectors form the audio unit, and remove it.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolts (A). 2. Disconnect the connector (B) from the center display unit. 3. Remove the harness clip (C).

2. Disconnect the connector (B) from the center display unit.

3. Remove the harness clip (C).

Courtesy of HONDA, U.S.A., INC. | 4. Pull out the audio unit assembly (A) slightly. NOTE: Do not grab the top edge of the center display unit (B) when removing the audio unit. 5. Disconnect the connectors form the audio unit, and remove it.

NOTE: Do not grab the top edge of the center display unit (B) when removing the audio unit.

5. Disconnect the connectors form the audio unit, and remove it.

- Center Display Unit - Remove

- Audio Unit Bracket - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the brackets (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the brackets (B).

2. Remove the brackets (B).

- Audio Cover - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the audio unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.

1. Install the audio unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.

- Make sure all the connectors are secure.

- After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system.
````

## Chunk 2571: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1534.html`
- Chunk ID: `chunk_acddba6d9d92`
- Images: `images\GHH399717.jpeg`, `images\GHH399718.jpeg`, `images\GHH399719.jpeg`, `images\GHH399720.jpeg`
- Duplicate sources: `pages\1984.html`, `pages\25946.html`, `pages\13173.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE:

- When working on electronic components, make sure the work area is clean and dust free.

- Make sure your hands are clean and free of oils and grease.

- If you are replacing the audio-navigation unit, write down the audio presets (if possible), and enter them into the new audio-navigation unit.

- With XM: If you are replacing the audio-navigation unit, register the new XM I.D. number by calling 800-852-9696. The XM I.D can be found on a label attached to the audio-navigation unit.

- When the audio-navigation unit is replaced or disconnected, do the Map Matching. This part of the initialization matches the GPS coordinates with a road on the map screen. To do this part of the procedure, make sure that the navigation system displays a map, and drive the vehicle on a mapped road shown on the map screen. Do not enter a destination at this time. When the name of the current road you are driving on appears at the bottom of the screen, the entire procedure is complete.

- Center Console Side Trim (Both Side) - Remove

- Climate Control Panel - Remove

- Audio-Navigation Unit Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolts (A). 2. Disconnect the connector (B) from the center display unit. 3. Remove the harness clip (C). Courtesy of HONDA, U.S.A., INC. 4. Pull out the audio-navigation unit assembly (A) slightly. NOTE: Do not grab the top edge of the center display unit (B) when removing the audio-navigation unit. 5. Disconnect the connectors form the audio-navigation unit, and remove it.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolts (A). 2. Disconnect the connector (B) from the center display unit. 3. Remove the harness clip (C).

2. Disconnect the connector (B) from the center display unit.

3. Remove the harness clip (C).

Courtesy of HONDA, U.S.A., INC. | 4. Pull out the audio-navigation unit assembly (A) slightly. NOTE: Do not grab the top edge of the center display unit (B) when removing the audio-navigation unit. 5. Disconnect the connectors form the audio-navigation unit, and remove it.

NOTE: Do not grab the top edge of the center display unit (B) when removing the audio-navigation unit.

5. Disconnect the connectors form the audio-navigation unit, and remove it.

- Center Display Unit - Remove

- Audio-Navigation Unit Bracket - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the brackets (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the brackets (B).

2. Remove the brackets (B).

- Audio Cover - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the audio-navigation unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. If the audio-navigation was replaced, it may take up to 30 minutes for the navigation system to calibrate and operate correctly. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system, then park the vehicle outside, and do the GPS initialization.

1. Install the audio-navigation unit in the reverse order of removal. NOTE: Make sure all the connectors are secure. If the audio-navigation was replaced, it may take up to 30 minutes for the navigation system to calibrate and operate correctly. After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system, then park the vehicle outside, and do the GPS initialization.

- Make sure all the connectors are secure.

- If the audio-navigation was replaced, it may take up to 30 minutes for the navigation system to calibrate and operate correctly.

- After Installation, do the System Links in the System Diagnostic Mode to confirm that there are no problems in the system, then park the vehicle outside, and do the GPS initialization.
````

## Chunk 2572: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1535.html`
- Chunk ID: `chunk_66a0c7f44918`
- Images: `images\GHH399721.jpeg`
- Duplicate sources: `pages\1985.html`, `pages\25947.html`, `pages\13174.html`

### Full Text

````text
# Removal and Installation

- Audio-Navigation Unit Assembly - Remove (With Navigation)

- Audio Unit Assembly - Remove (Without Navigation)

- Center Display Unit - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the center display unit (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the center display unit (B).

2. Remove the center display unit (B).

- All Removed Parts - Install 1. Install the center display unit in the reverse order of removal.

1. Install the center display unit in the reverse order of removal.
````

## Chunk 2573: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1536.html`
- Chunk ID: `chunk_e78254f3b0fc`
- Images: `images\GHH399722.jpeg`
- Duplicate sources: `pages\1986.html`, `pages\25948.html`, `pages\13175.html`

### Full Text

````text
# Removal and Installation

- Audio-Navigation Unit Assembly - Remove (With Navigation)

- Audio Unit Assembly - Remove (Without Navigation)

- Meter Upper Visor - Remove

- GPS Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the harness clips (A). 2. Pull out the cord carefully, and remove the GPS antenna (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the harness clips (A). 2. Pull out the cord carefully, and remove the GPS antenna (B).

2. Pull out the cord carefully, and remove the GPS antenna (B).

- All Removed Parts - Install 1. Install the GPS antenna in the reverse order of removal.

1. Install the GPS antenna in the reverse order of removal.
````

## Chunk 2574: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1537.html`
- Chunk ID: `chunk_41f98963574c`
- Images: `images\GHH399723.jpeg`, `images\GHH399724.jpeg`
- Duplicate sources: `pages\1987.html`, `pages\25949.html`, `pages\13176.html`

### Full Text

````text
# Removal and Installation

- Roof Console - Remove

- HFL Microphone - Remove With Display Audio Courtesy of HONDA, U.S.A., INC. With Color Audio Courtesy of HONDA, U.S.A., INC.

With Display Audio

Courtesy of HONDA, U.S.A., INC.

With Color Audio

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the HFL microphone in the reverse order of removal.

1. Install the HFL microphone in the reverse order of removal.
````

## Chunk 2575: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1538.html`
- Chunk ID: `chunk_c17fb4dc2b8d`
- Images: `images\GHH399725.jpeg`
- Duplicate sources: `pages\1988.html`, `pages\25950.html`, `pages\13177.html`

### Full Text

````text
# Removal and Installation

- Rear License Trim - Remove

- Rearview Camera - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the rearview camera in the reverse order of removal.

1. Install the rearview camera in the reverse order of removal.
````

## Chunk 2576: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1539.html`
- Chunk ID: `chunk_601795969b82`
- Images: `images\GHH399726.jpeg`
- Duplicate sources: `pages\1989.html`, `pages\25951.html`, `pages\13178.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

- Headliner - Remove

- Roof Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the harness clips (B). 3. Remove the roof antenna (C).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the harness clips (B). 3. Remove the roof antenna (C).

2. Remove the harness clips (B).

3. Remove the roof antenna (C).

- All Removed Parts - Install 1. Install the roof antenna in the reverse order of removal.

1. Install the roof antenna in the reverse order of removal.
````

## Chunk 2577: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1540.html`
- Chunk ID: `chunk_7cad8353ba79`
- Images: `images\GHH399727.jpeg`
- Duplicate sources: `pages\1990.html`, `pages\25952.html`, `pages\13179.html`

### Full Text

````text
# Removal and Installation

- Passenger's Dashboard Undercover - Remove

- Glove Box - Remove

- Kick Panel (Right Side) - Remove

- Stereo Amplifier - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the harness clip (A). 2. Disconnect the connectors (B). 3. Remove the bolts (C). 4. Remove the stereo amplifier (D).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the harness clip (A). 2. Disconnect the connectors (B). 3. Remove the bolts (C). 4. Remove the stereo amplifier (D).

2. Disconnect the connectors (B).

3. Remove the bolts (C).

4. Remove the stereo amplifier (D).

- All Removed Parts - Install 1. Install the stereo amplifier in the reverse order of removal.

1. Install the stereo amplifier in the reverse order of removal.
````

## Chunk 2578: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1541.html`
- Chunk ID: `chunk_a31505ec4066`
- Images: `images\GHH399728.jpeg`
- Duplicate sources: `pages\1991.html`, `pages\25953.html`, `pages\13180.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE: If you are replacing the tuner unit, write down the AM/FM radio presets (if possible), and enter them into the new audio-navigation unit or the new audio unit.

- Rear Side Trim Panel (Right Side) - Remove (2-door)

- Rear Seat Side Trim (Right Side) - Remove (Except 2-door)

- Tuner Unit - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connectors (A). 2. Loosen the nut (B). 3. Remove the nut (C). 4. Remove the tuner unit (D).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connectors (A). 2. Loosen the nut (B). 3. Remove the nut (C). 4. Remove the tuner unit (D).

2. Loosen the nut (B).

3. Remove the nut (C).

4. Remove the tuner unit (D).

- All Removed Parts - Install 1. Install the tuner unit in the reverse order of removal.

1. Install the tuner unit in the reverse order of removal.
````

## Chunk 2579: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\1542.html`
- Chunk ID: `chunk_600f60b586f2`
- Images: `images\GHH399729.jpeg`
- Duplicate sources: `pages\1992.html`, `pages\25954.html`, `pages\13181.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Courtesy of HONDA, U.S.A., INC.

- Volume Knob - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 2580: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1543.html`
- Chunk ID: `chunk_80381a89904a`
- Images: `images\GHH399730.jpeg`, `images\GHH399731.jpeg`, `images\GHH399732.jpeg`, `images\GHH399733.jpeg`, `images\GHH399734.jpeg`, `images\GHH399735.jpeg`, `images\GHH399736.jpeg`, `images\GHH399737.jpeg`
- Duplicate sources: `pages\1993.html`, `pages\25955.html`, `pages\13182.html`

### Full Text

````text
# Removal and Installation

Door Speaker

- Front Door Panel - Remove

- Door Speaker - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolt (A), then lift the door speaker (B) straight up to release the lower clips (C). 2. Disconnect the connector (D).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolt (A), then lift the door speaker (B) straight up to release the lower clips (C). 2. Disconnect the connector (D).

2. Disconnect the connector (D).

- All Removed Parts - Install 1. Install the door speaker in the reverse order of removal.

1. Install the door speaker in the reverse order of removal.

Front Tweeter

- Front Door Panel - Remove

- Tweeter Cover - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the tweeter cover (A). 2. Disconnect the connector (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the tweeter cover (A). 2. Disconnect the connector (B).

2. Disconnect the connector (B).

- Front Tweeter - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the front tweeter in the reverse order of removal.

1. Install the front tweeter in the reverse order of removal.

Front Center Speaker

- Center Speaker Trim - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the center speaker trim (A). 2. Disconnect the connector (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the center speaker trim (A). 2. Disconnect the connector (B).

2. Disconnect the connector (B).

- Front Center Speaker - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the front center speaker in the reverse order of removal.

1. Install the front center speaker in the reverse order of removal.

Rear Speaker

- Rear Shelf Trim - Remove

- Rear Speaker - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolt (A), then slide the rear speaker (B) to release the clips (C). 2. Disconnect the connector (D).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolt (A), then slide the rear speaker (B) to release the clips (C). 2. Disconnect the connector (D).

2. Disconnect the connector (D).

- All Removed Parts - Install 1. Install the rear speaker in the reverse order of removal.

1. Install the rear speaker in the reverse order of removal.

Rear Tweeter

- Rear Shelf Trim - Remove

- Rear Tweeter - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the rear tweeter in the reverse order of removal.

1. Install the rear tweeter in the reverse order of removal.

Subwoofer

- Rear Shelf Trim - Remove

- Subwoofer - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the subwoofer (A). 2. Disconnect the connector (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the subwoofer (A). 2. Disconnect the connector (B).

2. Disconnect the connector (B).

- All Removed Parts - Install 1. Install the subwoofer in the reverse order of removal.

1. Install the subwoofer in the reverse order of removal.
````

## Chunk 2581: Speaker Removal, Installation, and Test (2/4-Door): Test

- Title: Speaker Removal, Installation, and Test (2/4-Door): Test
- Source path: `pages\1544.html`
- Chunk ID: `chunk_8f5b38c00943`
- Images: `images\GHH399738.jpeg`, `images\GHH399739.jpeg`, `images\GHH399740.jpeg`, `images\GHH399741.jpeg`, `images\GHH399742.jpeg`
- Duplicate sources: `pages\1994.html`, `pages\25956.html`, `pages\13183.html`

### Full Text

````text
# Speaker Removal, Installation, and Test (2/4-Door): Test

Door Speaker, Rear Speaker

- Door Speaker, Rear Speaker - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the door speaker.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the door speaker.

2. If the resistance is not as specified, replace the door speaker.

Tweeter

- Tweeter - Test With Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Without Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Measure the resistance between the terminals as shown: With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω. Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage. 2. If the resistance is not as specified, replace the tweeter.

With Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Without Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Measure the resistance between the terminals as shown: With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω. Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage. 2. If the resistance is not as specified, replace the tweeter.

Without Stereo Amplifier

- With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω.

- Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage.

2. If the resistance is not as specified, replace the tweeter.

Front Center Speaker

- Front Center Speaker - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the speaker.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the speaker.

2. If the resistance is not as specified, replace the speaker.

Subwoofer

- Subwoofer - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between the terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the subwoofer.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between the terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the subwoofer.

2. If the resistance is not as specified, replace the subwoofer.
````

## Chunk 2582: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\1545.html`
- Chunk ID: `chunk_757cbb4e4c2f`
- Images: `images\GHH399743.jpeg`, `images\GHH399744.jpeg`, `images\GHH399745.jpeg`, `images\GHH399746.jpeg`, `images\GHH399747.jpeg`, `images\GHH399748.jpeg`, `images\GHH399749.jpeg`, `images\GHH399750.jpeg`
- Duplicate sources: `pages\1995.html`, `pages\25957.html`, `pages\13184.html`

### Full Text

````text
# Removal and Installation

Door Speaker

- Door Panel - Remove 1. Remove the door panel: Front door panel Rear door panel

1. Remove the door panel: Front door panel Rear door panel

- Front door panel

- Rear door panel

- Door Speaker - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the bolt (A), then lift the door speaker (B) straight up to release the lower clips (C). 2. Disconnect the connector (D).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the bolt (A), then lift the door speaker (B) straight up to release the lower clips (C). 2. Disconnect the connector (D).

2. Disconnect the connector (D).

- All Removed Parts - Install 1. Install the door speaker in the reverse order of removal.

1. Install the door speaker in the reverse order of removal.

Front Tweeter

- Front Door Panel - Remove

- Tweeter Cover - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the tweeter cover (A). 2. Disconnect the connector (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the tweeter cover (A). 2. Disconnect the connector (B).

2. Disconnect the connector (B).

- Front Tweeter - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the front tweeter in the reverse order of removal.

1. Install the front tweeter in the reverse order of removal.

Front Center Speaker

- Center Speaker Trim - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the center speaker trim (A). 2. Disconnect the connector (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the center speaker trim (A). 2. Disconnect the connector (B).

2. Disconnect the connector (B).

- Front Center Speaker - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the front center speaker in the reverse order of removal.

1. Install the front center speaker in the reverse order of removal.

Rear Door Tweeter

- Rear Door Panel - Remove

- Rear Door Tweeter - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the rear door tweeter in the reverse order of removal.

1. Install the rear door tweeter in the reverse order of removal.

Satellite Speaker

- C-Pillar Trim - Remove

- Satellite Speaker - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the satellite speaker in the reverse order of removal.

1. Install the satellite speaker in the reverse order of removal.

Subwoofer

- Rear Side Trim Panel (Right side) - Remove

- Subwoofer - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the nut (B). 3. Remove the bolts (C). 4. Remove the subwoofer (D).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the nut (B). 3. Remove the bolts (C). 4. Remove the subwoofer (D).

2. Remove the nut (B).

3. Remove the bolts (C).

4. Remove the subwoofer (D).

- All Removed Parts - Install 1. Install the subwoofer in the reverse order of removal.

1. Install the subwoofer in the reverse order of removal.
````

## Chunk 2583: Speaker Removal, Installation, and Test (5-door) (2017 2018 2019 2020 2021): Test

- Title: Speaker Removal, Installation, and Test (5-door) (2017 2018 2019 2020 2021): Test
- Source path: `pages\1546.html`
- Chunk ID: `chunk_0ade37f233ca`
- Images: `images\GHH399751.jpeg`, `images\GHH399752.jpeg`, `images\GHH399753.jpeg`, `images\GHH399754.jpeg`, `images\GHH399755.jpeg`, `images\GHH399756.jpeg`
- Duplicate sources: `pages\1996.html`, `pages\25958.html`, `pages\13185.html`

### Full Text

````text
# Speaker Removal, Installation, and Test (5-door) (2017 2018 2019 2020 2021): Test

Door Speaker

- Door Speaker - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the door speaker.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the door speaker.

2. If the resistance is not as specified, replace the door speaker.

Tweeter

- Tweeter - Test With Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Without Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Measure the resistance between the terminals as shown: With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω. Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage. 2. If the resistance is not as specified, replace the tweeter.

With Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Without Stereo Amplifier Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Measure the resistance between the terminals as shown: With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω. Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage. 2. If the resistance is not as specified, replace the tweeter.

Without Stereo Amplifier

- With stereo amplifier: Measure the resistance between terminal No. 1 and terminal No. 2. There should be about 3.2 Ω.

- Without stereo amplifier: Measure the resistance between terminal No. 1 and the outside terminal of the capacitor (A). There should be about 4 Ω. Also visually check the capacitor for damage.

2. If the resistance is not as specified, replace the tweeter.

Front Center Speaker

- Front Center Speaker - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the speaker.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the speaker.

2. If the resistance is not as specified, replace the speaker.

Satellite Speaker

- Satellite Speaker - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the speaker.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between terminals No. 1 and No. 2. There should be about 4 Ω. 2. If the resistance is not as specified, replace the speaker.

2. If the resistance is not as specified, replace the speaker.

Subwoofer

- Subwoofer - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between the terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the subwoofer.

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between the terminals No. 1 and No. 2. There should be about 2 Ω. 2. If the resistance is not as specified, replace the subwoofer.

2. If the resistance is not as specified, replace the subwoofer.
````

## Chunk 2584: Audio System Symptom Troubleshooting Index (Color Audio Type (5-inch Screen))

- Title: Audio System Symptom Troubleshooting Index (Color Audio Type (5-inch Screen))
- Source path: `pages\1547.html`
- Chunk ID: `chunk_d19a709ae8cb`
- Images: none
- Duplicate sources: `pages\1997.html`, `pages\25859.html`, `pages\13432.html`

### Full Text

````text
# Audio System Symptom Troubleshooting Index (Color Audio Type (5-inch Screen))

Symptom | Diagnostic Procedure | Also Check for

Poor AM or FM radio reception or interference | Symptom Troubleshooting | Check radio reception: Do the FM or AM in the System Diagnostic Mode Aftermarket FM modulator Loose antenna amplifier mounting bolt

- Check radio reception: Do the FM or AM in the System Diagnostic Mode

- Aftermarket FM modulator

- Loose antenna amplifier mounting bolt

Audio unit will not turn on (No information display) | Symptom Troubleshooting

No sound is heard from all the speakers (display is normal) | Symptom Troubleshooting | Aftermarket amplifier or speakers

Audio system sound is weak or distorted (display is normal) | Symptom Troubleshooting | Fader and balance positions Aftermarket amplifier or speakers

- Fader and balance positions

- Aftermarket amplifier or speakers

AM/FM radio preset memory is lost | Replace the audio unit | Internal error

Audio unit button does not work | Do the Knob Check in the System Diagnostic Mode | Check the connector for poor connections or loose terminals between the audio unit and the audio panel

Volume does not increase with speed | Symptom Troubleshooting | Speed-sensitive Volume Control settings (see the Owner's Manual)

Volume is too high or too low when driving at freeway speeds | Speed-sensitive Volume Control settings (see the Owner's Manual)

Audio remote-HFL switch does not work properly (audio unit buttons work) | Symptom Troubleshooting

Audio unit does not exit anti-theft mode | Anti-Theft Feature

USB device does not function | Symptom Troubleshooting | Error Messages USB device compatibility (see the Owner's Manual)

- Error Messages

- USB device compatibility (see the Owner's Manual)

Bluetooth audio does not work | Bluetooth phone compatibility (see the Owner's Manual)

Rearview camera image does not come on | Symptom Troubleshooting

Rearview camera image does not change when selecting different views | Symptom Troubleshooting

Audio unit button illumination does not work | Symptom Troubleshooting
````

## Chunk 2585: Audio System Symptom Troubleshooting Index (Display Audio Type (7-inch Screen))

- Title: Audio System Symptom Troubleshooting Index (Display Audio Type (7-inch Screen))
- Source path: `pages\1548.html`
- Chunk ID: `chunk_b7097b756396`
- Images: none
- Duplicate sources: `pages\1998.html`, `pages\25860.html`, `pages\13433.html`

### Full Text

````text
# Audio System Symptom Troubleshooting Index (Display Audio Type (7-inch Screen))

NOTE: Refer to Navigation System Symptom Troubleshooting for information about the symptom of audio-navigation unit which is not in the following table .

Symptom | Diagnostic Procedure | Also Check for

Poor or no sound with AM/FM radio | Symptom Troubleshooting | Check radio reception: Do the Remote Tuner in the System Diagnostic Mode Aftermarket FM modulator Loose antenna mounting nut Loose antenna amplifier mounting bolt

- Check radio reception: Do the Remote Tuner in the System Diagnostic Mode

- Aftermarket FM modulator

- Loose antenna mounting nut

- Loose antenna amplifier mounting bolt

AM/FM radio display is blank or no station information is displayed | Symptom Troubleshooting

Excessive transition between analog broadcast and digital HD Radio (TM) broadcast | Receiver is located near the edge of the digital HD Radio (TM) coverage area. Refer to www.hdradio.com to verify radio stations in your coverage area

HD Radio (TM) changes HD channel on its own | This is intended behavior. HD Radio (TM) is set to revert to main channel after extended loss of HD2/HD3 broadcast

AM radio reception changes at night | This is a system characteristic. AM radio stations are required by the government (FCC) to lower their power at night

Audio unit will not turn on (No information display) | Symptom Troubleshooting

No sound is heard from all the speakers (display is normal) | Symptom Troubleshooting | Aftermarket amplifier or speakers

Audio system sound is weak or distorted (display is normal) | Symptom Troubleshooting | Fader and balance positions Aftermarket amplifier or speakers

- Fader and balance positions

- Aftermarket amplifier or speakers

AM/FM radio preset memory is lost | Replace the tuner unit | Internal error

Volume does not increase with speed | Symptom Troubleshooting | Speed-sensitive Volume Control settings (see the Owner's Manual)

Volume is too high or too low when driving at freeway speeds | Speed-sensitive Volume Control settings (see the Owner's Manual)

Center display unit button does not work | Do the Hard Key in the System Diagnostic Mode | Check the Touch Panel Sensitivity in the System Settings

Center display unit does not dim | Symptom Troubleshooting

The MID does not display the audio unit information | Symptom Troubleshooting

Audio remote-HFL switch does not work properly (audio unit buttons work) | Symptom Troubleshooting

Audio unit does not exit anti-theft mode | Anti-Theft Feature

USB device does not function | Symptom Troubleshooting | Error messages USB device compatibility (see the Owner's Manual)

- Error messages

- USB device compatibility (see the Owner's Manual)

Bluetooth audio does not work | Bluetooth phone compatibility (see the Owner's Manual)

Pandora is not is displayed as an audio source | Do the PANDORA in the System Diagnostic Mode to check the Pandora settings is abled

Rearview camera image does not come on | Symptom Troubleshooting

Symptom | Diagnostic Procedure | Also Check for

Rearview camera image does not change when selecting different views | Symptom Troubleshooting

LaneWatch camera image does not come on | Symptom Troubleshooting | Audio DTCs

XM radio display is blank and no station information is displayed | With navigation: Navigation DTCs Without navigation: Audio DTCs | Error messages

- With navigation: Navigation DTCs

- Without navigation: Audio DTCs

Active sound control does not work | Symptom Troubleshooting

System always comes up in-line diagnostic mode (without navigation) | Factory diagnostic screen In Line Diag
````

## Chunk 2586: Audio System Component Location Index (2/4-door)

- Title: Audio System Component Location Index (2/4-door)
- Source path: `pages\1549.html`
- Chunk ID: `chunk_ca20289f4af2`
- Images: `images\GHH399307.jpeg`, `images\GHH399308.jpeg`, `images\GHH399309.jpeg`, `images\GHH399310.jpeg`, `images\GHH399311.jpeg`, `images\GHH399312.jpeg`, `images\GHH399313.jpeg`
- Duplicate sources: `pages\1999.html`, `pages\25861.html`, `pages\13434.html`

### Full Text

````text
# Audio System Component Location Index (2/4-door)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2587: Audio System Component Location Index (5-door: Color Audio Type (5-inch Screen))

- Title: Audio System Component Location Index (5-door: Color Audio Type (5-inch Screen))
- Source path: `pages\1550.html`
- Chunk ID: `chunk_6009c62fd448`
- Images: `images\GHH399314.jpeg`, `images\GHH399315.jpeg`
- Duplicate sources: `pages\2000.html`, `pages\25862.html`, `pages\13435.html`

### Full Text

````text
# Audio System Component Location Index (5-door: Color Audio Type (5-inch Screen))

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2588: Audio System Component Location Index (5-door: Display Audio Type (7-inch Screen))

- Title: Audio System Component Location Index (5-door: Display Audio Type (7-inch Screen))
- Source path: `pages\1551.html`
- Chunk ID: `chunk_a4badbc36ec8`
- Images: `images\GHH399316.jpeg`, `images\GHH399317.jpeg`, `images\GHH399318.jpeg`
- Duplicate sources: `pages\2001.html`, `pages\25863.html`, `pages\13436.html`

### Full Text

````text
# Audio System Component Location Index (5-door: Display Audio Type (7-inch Screen))

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2589: Audio System Component Location Index (Display Audio Type (7-inch Screen))

- Title: Audio System Component Location Index (Display Audio Type (7-inch Screen))
- Source path: `pages\1552.html`
- Chunk ID: `chunk_88b01dcbd108`
- Images: `images\GHH399319.jpeg`, `images\GHH399320.jpeg`, `images\GHH399321.jpeg`
- Duplicate sources: `pages\2002.html`, `pages\25864.html`, `pages\13301.html`

### Full Text

````text
# Audio System Component Location Index (Display Audio Type (7-inch Screen))

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 2590: Audio System DTC Troubleshooting Index

- Title: Audio System DTC Troubleshooting Index
- Source path: `pages\1553.html`
- Chunk ID: `chunk_e37262a04a3b`
- Images: none
- Duplicate sources: `pages\2003.html`, `pages\25865.html`, `pages\13437.html`

### Full Text

````text
# Audio System DTC Troubleshooting Index

NOTE: These DTCs cannot be read with the HDS. To view them, refer to How to Check for Error History (Audio DTCs) .

DTC | Description | Circuit

1102 | USB Diag | USB

1301 | GPS Antenna Error | GPS antenna

1302 | GPS Receiver Error 1 | GPS receiver

1702 | XM Antenna Error | XM antenna

2608 | R-Camera Diag | Rearview camera

2610 | DRAM Diag | Audio unit DRAM

2618 | LaneWatch Diag | LaneWatch camera

2701 | GPS Diag: Antenna | GPS antenna

2703 | Aircon Diag | Climate control unit
````

## Chunk 2591: Audio System Error Codes

- Title: Audio System Error Codes
- Source path: `pages\1554.html`
- Chunk ID: `chunk_25563517602c`
- Images: none
- Duplicate sources: `pages\2004.html`, `pages\25866.html`, `pages\13431.html`

### Full Text

````text
# Audio System Error Codes

NOTE: The audio system can display a few error codes when some problems are detected with the audio unit, USB, and the XM radio. This is not a complete list of audio error codes. Refer to symptom troubleshooting.

Audio Unit Error Messages (Display Audio Type)

Error Message Displayed | Possible Cause | Solution

The system is unable to start due to excessive heat. The system will start after the system cools. | This message appears when the display temperature is too high. | Park the vehicle in a cooler place for a while. If the high temperature status is cancelled, the audio unit turns on the display.

Sounds are restricted because the AMP is in protection mode. | This message appears when the stereo amplifier temperature is too high, and the stereo amplifier inhibits sound output. | Park the vehicle in a cooler place for a while. If the high temperature status is cancelled, the stereo amplifier outputs the sound again.

USB Error Messages

Error Message Displayed | Possible Cause | Solution

The connected USB device has a problem. See Owner's Manual *1 | Faulty power supply to USB device. | Check for hard error code: With navigation Without navigation

- With navigation

- Without navigation

Bad USB Device Please Check Owners Manual *2 | Faulty power supply to USB device. | Disconnect the USB device, and turn the vehicle to the OFF (LOCK) mode then the ON mode. Then connect a known-good USB device to the USB port. If the error message appears on the screen, replace the audio unit .

Connect Retry | The audio unit failed to synchronize with the iPod. | Appears when the system does not acknowledge the iPod. Reconnect the iPod.

No Data | No music file(s) can be found in a USB device. | Check the music files in the USB device.

USB Error | There is a internal problem with the audio unit. | Replace the audio-navigation unit or the audio unit .

Unplayable File | The audio unit cannot read the file (s). | Check the files in the USB device. There is a possibility that the files have been damaged The WMA files or the AAC file cannot be read with the (DRM) copy protection rights

- Check the files in the USB device. There is a possibility that the files have been damaged

- The WMA files or the AAC file cannot be read with the (DRM) copy protection rights

Unsupported | Unsupported USB device is connected Unsupported file system USB device communication error | Connect the applicable USB device (see the Owner's Manual).

- Unsupported USB device is connected

- Unsupported file system

- USB device communication error

Unsupported Version | Unsupported version iPod is connected. | Connect the applicable iPod (see the Owner's Manual).

*1: Display audio type

*2: Color audio type

XM Error Messages

NOTE: Do these checks with the vehicle parked outside with a clear view of the southern horizon.

Error Message Displayed | Possible Cause | Solution

Channel Not Subscribed | Selected XM channel is not subscribed. | Check the XM channel subscription status.

Channel Not Available | Selected XM channel is not in service. | Try another XM channel.

No Signal | Loss of signal. | Both terrestrial and satellite antennas have lost the signal. Park the vehicle outside with a clear view of the southern horizon.

Antenna Disconnected | XM antenna/antenna lead error. | Check for hard error code: With navigation Without navigation

- With navigation

- Without navigation
````

## Chunk 2592: How to Troubleshoot the Audio System: Notes

- Title: How to Troubleshoot the Audio System: Notes
- Source path: `pages\1555.html`
- Chunk ID: `chunk_8dabfedb64bd`
- Images: none
- Duplicate sources: `pages\2005.html`, `pages\25867.html`, `pages\13438.html`

### Full Text

````text
# How to Troubleshoot the Audio System: Notes

NOTE: Refer to How to Troubleshoot the Navigation System for information about the audio-navigation unit.
````

## Chunk 2593: How to Recognize Audio unit and Audio-Navigation Unit (Display Audio Type (7-inch Screen))

- Title: How to Recognize Audio unit and Audio-Navigation Unit (Display Audio Type (7-inch Screen))
- Source path: `pages\1556.html`
- Chunk ID: `chunk_73ddacd54baf`
- Images: none
- Duplicate sources: `pages\2006.html`, `pages\2145.html`, `pages\25868.html`, `pages\13439.html`, `pages\15907.html`

### Full Text

````text
# How to Recognize Audio unit and Audio-Navigation Unit (Display Audio Type (7-inch Screen))

There are two kinds of 7-inch display audio units according to a vehicle model. these units exist as an audio unit (without navigation) and an audio-navigation unit (with navigation), and look identical, but the audio-navigation unit displays a Honda Globe screen after displaying a Honda logo screen every time when you turn the vehicle to the ACCESSORY mode.
````

## Chunk 2594: Forced Rebooting of Audio Unit (Display Audio Type (7-inch Screen))

- Title: Forced Rebooting of Audio Unit (Display Audio Type (7-inch Screen))
- Source path: `pages\1557.html`
- Chunk ID: `chunk_921234c08d64`
- Images: `images\GHH29783.png`
- Duplicate sources: `pages\2007.html`, `pages\25869.html`, `pages\13440.html`

### Full Text

````text
# Forced Rebooting of Audio Unit (Display Audio Type (7-inch Screen))

If the system is frozen, and the screen does not respond, you can attempt rebooting the audio unit by pressing and holding the AUDIO POWER ( ) button for 5 seconds. When the function is effective, the confirmation screen appears.
````

## Chunk 2595: Anti-Theft Feature

- Title: Anti-Theft Feature
- Source path: `pages\1558.html`
- Chunk ID: `chunk_88d1e28348ae`
- Images: `images\GHH29783.png`
- Duplicate sources: `pages\2008.html`, `pages\25870.html`, `pages\13441.html`

### Full Text

````text
# Anti-Theft Feature

The audio unit has an anti-theft protection circuit. When one of the following occurs, the unit enters the anti-theft mode:

- Disconnecting the 12 volt battery.

- Disconnecting audio unit connector A (24P).

- Removing the No. A1-7 fuse or the No. A19 fuse .

After servicing or repairs, reconnect power to the audio unit, and turn the vehicle to the ON mode. There are two ways to exit the anti-theft mode:

- Press and hold the AUDIO POWER ( ) button for at least 2 seconds. The audio unit automatically exits the anti-theft mode. If the audio unit does not exit anti-theft mode, turn the vehicle to the OFF (LOCK) mode then the ON mode (if possible, start the engine), and try to release the anti-theft mode several times.

- Enter the 5-digit anti-theft code. If the input of code fails 10 times in a row, the screen is locked for 60 minutes.

If the code is unavailable, you can get the code from the iN using the audio unit serial number. The serial number can be found on a label attached to the audio unit.

When the audio unit is installed in another vehicle (same Year/Model/Trim), like in cases where a known-good unit was substituted for testing, do the Anti-Theft Skip mode in the System Diagnostic Mode (display audio type) , or do the Anti-Theft Temporary Cancellation in the System Diagnostic Mode (color audio type) . This mode will release the anti-theft code for 150 seconds.
````

## Chunk 2596: Global Positioning System (GPS) Limitations (Display Audio Type (7-inch Screen))

- Title: Global Positioning System (GPS) Limitations (Display Audio Type (7-inch Screen))
- Source path: `pages\1559.html`
- Chunk ID: `chunk_c672bdd719b0`
- Images: none
- Duplicate sources: `pages\2009.html`, `pages\25871.html`, `pages\13442.html`

### Full Text

````text
# Global Positioning System (GPS) Limitations (Display Audio Type (7-inch Screen))

The GPS signal is used for the HondaLink Assist function to communicate the customer's vehicle position to the emergency services. The GPS cannot detect the vehicle's position or elevation during the following instances:

- For the first 5 to 10 minutes after reconnecting the 12 volt battery (this process can take as long as 45 minutes).

- When the satellite signals are blocked by tall buildings, mountains, tunnels, large trees, inside parking structures or large trucks.

- When the GPS antenna is blocked by metallic window tinting or by an object placed above it in the vehicle. The GPS antenna requires a clear unobstructed view of the sky.

- When there is no satellite signal output (signal output is sometimes stopped for satellite servicing).

- When the satellite signals are blocked by the operation of some electronic aftermarket accessories including, but not limited to non-OEM in-dash entertainment units (amp, CD players/changers, radar detectors, theft recovery systems, etc.) and cell phones placed near the navigation system.

The accuracy of the GPS is reduced during these instances:

- Metallic window tinting above the GPS antenna.

- When only three or fewer satellite signals are received (Four satellite signals are required for accurate positioning).

- When driving near high tension power lines.

- When the satellite signals are blocked by the operation of some electronic aftermarket accessories including, but not limited to non-OEM in-dash entertainment units (amp, CD players/changers, radar detectors, theft recovery systems, etc.) and cell phones placed near the navigation system.

- When the satellite control centers are experiencing problems.
````

## Chunk 2597: LCD Unit Limitations (Display Audio Type (7-inch Screen))

- Title: LCD Unit Limitations (Display Audio Type (7-inch Screen))
- Source path: `pages\1560.html`
- Chunk ID: `chunk_74163c01976b`
- Images: none
- Duplicate sources: `pages\2010.html`, `pages\25872.html`, `pages\13443.html`

### Full Text

````text
# LCD Unit Limitations (Display Audio Type (7-inch Screen))

The center display unit is touch sensitive. Touch the display directly to select items on the screen.

- Heavy gloves, fingernails or pens cannot be used on the touch panel.

- In cold temperatures, the display may stay dark for the first minute until it warms up.

- When the display is too hot because of direct summer sunlight, it remains dark until the temperature drops (you may see an error message displayed stating this fact).

- Fingerprints on the screen may be noticeable. Clean the screen with a soft, damp cloth. You may use a mild cleaner intended for eye glasses or computer screens. To avoid scratching the panel, do not rub too hard or use abrasive cleaners or shop towels.
````

## Chunk 2598: How to Check Error History (Audio DTCs) (Display Audio Type (7-inch Screen))

- Title: How to Check Error History (Audio DTCs) (Display Audio Type (7-inch Screen))
- Source path: `pages\1561.html`
- Chunk ID: `chunk_8b341ff6b936`
- Images: `images\GHH172669.png`, `images\GHH29783.png`, `images\GHH399322.jpeg`, `images\GHH399323.jpeg`, `images\GHH399324.jpeg`, `images\GHH399325.jpeg`, `images\GHH399326.jpeg`, `images\GHH399327.jpeg`
- Duplicate sources: `pages\2011.html`, `pages\25873.html`, `pages\13444.html`

### Full Text

````text
# How to Check Error History (Audio DTCs) (Display Audio Type (7-inch Screen))

NOTE: The audio DTCs cannot be retrieved with the HDS.

The Error History feature is to record intermittent audio issues that occur while the customer is using the system. Sometimes the customer complaint cannot be duplicated. The error history may record the information needed to diagnose the problem. To check the error history:

1. Turn the vehicle to the ON mode.Press and hold these buttons until the Select Diagnosis Items menu screen is displayed:

- With volume knob: The PHONE button, DISPLAY MODE ( ) button, and the AUDIO POWER ( ) button.

- Without volume knob: The MENU button, DISPLAY MODE ( ) button, and the AUDIO POWER ( ) button.

Displaying Select Diagnosis Items Menu Screen (With Volume Knob)

Courtesy of HONDA, U.S.A., INC.

Displaying Select Diagnosis Items Menu Screen (Without Volume Knob)

Courtesy of HONDA, U.S.A., INC.

3. When the Select Diagnosis Items menu appears, select the Self-Diagnosis Mode.

4. If the audio unit has hard error codes, the Error History icon (A) turns yellow. When no hard error codes are stored, the icon is gray. To view the errors with their audio DTC, select the Error History icon.

Courtesy of HONDA, U.S.A., INC.

5. Select the Hard Error icon in the Error History menu.

NOTE: The Soft Error feature is for factory use only.

Courtesy of HONDA, U.S.A., INC.

The Hard Error screen displays the following information by selecting the Date_Time icon (A):

- The date and time when the error occurred. Swipe the screen to check the next items.

- The audio DTC for the error.

- A brief description of the audio DTC.

NOTE: The Save feature is for factory use only.

Courtesy of HONDA, U.S.A., INC.

7. Use the audio DTC Troubleshooting table to troubleshoot the error. Select the Return icon to exit the Error History main menu.

How to Clear Error History

NOTE: The audio DTCs cannot be deleted with the HDS.

8. Select the Clear icon in the Hard Error. The confirmation screen appears.

Courtesy of HONDA, U.S.A., INC.

9. Select the Yes icon. All Hard Error histories are cleared. Select the Return icon to exit the Error History.
````

## Chunk 2599: AM/FM radio display is blank or no station information is displayed (With Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (With Navigation)
- Source path: `pages\1562.html`
- Chunk ID: `chunk_57cf145a9330`
- Images: none
- Duplicate sources: `pages\2012.html`, `pages\25874.html`, `pages\13445.html`

### Full Text

````text
# AM/FM radio display is blank or no station information is displayed (With Navigation)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Turn on the audio system, and select AM or FM. Does the AM or FM radio station information display blankΩ YES The failure is duplicated, go to step 2. NO Intermittent failure, the system is OK at this time. If the AM or FM sound is not heard, go to Poor or no sound with AM/FM radio troubleshooting .

-1. Turn the vehicle to the ON mode.

-2. Turn on the audio system, and select AM or FM.

Does the AM or FM radio station information display blankΩ

YES

The failure is duplicated, go to step 2.

NO

Intermittent failure, the system is OK at this time. If the AM or FM sound is not heard, go to Poor or no sound with AM/FM radio troubleshooting .

- Determine possible failure area (TUNER 6V line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Tuner unit connector A (10P) -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 10 Test point 2 Body ground Is there about 6.0 V? YES The TUNER 6V wire is OK. Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Tuner unit connector A (10P)

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 10

Test point 2 | Body ground

Is there about 6.0 V?

YES

The TUNER 6V wire is OK. Go to step 5.

NO

Go to step 3.

- Open wire check (TUNER 6V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Audio-navigation unit connector E (16P) No. 1 Test point 2 Body ground Is there about 6.0 V? YES Repair an open in the wire between the audio-navigation unit and the tuner unit. NO The TUNER 6V wire is not open. Go to step 4.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 1

Test point 2 | Body ground

Is there about 6.0 V?

YES

Repair an open in the wire between the audio-navigation unit and the tuner unit.

NO

The TUNER 6V wire is not open. Go to step 4.

- Shorted wire check (TUNER 6V line) -1. Disconnect the following connector. Audio-navigation unit connector E (16P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Audio-navigation unit connector E (16P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the wire between the audio-navigation unit and the tuner unit. NO Replace the audio-navigation unit .

-1. Disconnect the following connector.

Audio-navigation unit connector E (16P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire between the audio-navigation unit and the tuner unit.

NO

Replace the audio-navigation unit .

- Determine possible failure area (TUNER GND line, others) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 2 Test point 2 Body ground Is there continuity? YES The TUNER GND wire is OK. Go to step 7. NO Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

The TUNER GND wire is OK. Go to step 7.

NO

Go to step 6.

- Open wire check (TUNER GND line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 2600: AM/FM radio display is blank or no station information is displayed (With Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (With Navigation)
- Source path: `pages\1562.html`
- Chunk ID: `chunk_be901b2333a4`
- Images: none
- Duplicate sources: `pages\2012.html`, `pages\25874.html`, `pages\13445.html`

### Full Text

````text
tuner unit.

NO

Replace the audio-navigation unit .

- Determine possible failure area (TUNER GND line, others) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 2 Test point 2 Body ground Is there continuity? YES The TUNER GND wire is OK. Go to step 7. NO Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

The TUNER GND wire is OK. Go to step 7.

NO

Go to step 6.

- Open wire check (TUNER GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Audio-navigation unit connector E (16P) No. 9 Test point 2 Body ground Is there continuity? YES Repair an open in the wire between the audio-navigation unit and the tuner unit. NO Replace the audio-navigation unit .

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 9

Test point 2 | Body ground

Is there continuity?

YES

Repair an open in the wire between the audio-navigation unit and the tuner unit.

NO

Replace the audio-navigation unit .

- Determine possible failure area (TUNER 9V line, others) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 1 Test point 2 Body ground Is there about 9.0 V? YES The TUNER 9V wire is OK. Go to step 10. NO Go to step 8.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 1

Test point 2 | Body ground

Is there about 9.0 V?

YES

The TUNER 9V wire is OK. Go to step 10.

NO

Go to step 8.

- Open wire check (TUNER 9V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Tuner unit connector A (10P): disconnected Test point 1 Audio-navigation unit connector E (16P) No. 2 Test point 2 Body ground Is there about 9.0 V? YES Repair an open in the wire between the audio-navigation unit and the tuner unit. NO The TUNER 9V wire is not open. Go to step 9.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 2

Test point 2 | Body ground

Is there about 9.0 V?

YES

Repair an open in the wire between the audio-navigation unit and the tuner unit.

NO

The TUNER 9V wire is not open. Go to step 9.

- Shorted wire check (TUNER 9V line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio-navigation unit connector E (16P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Audio-navigation unit connector E (16P) No. 2 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the wire between the audio-navigation unit and the tuner unit. NO Replace the audio-navigation unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio-navigation unit connector E (16P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire between the audio-navigation unit and the tuner unit.

NO

Replace the audio-navigation unit .

- Shorted wire check (TUNER RS485+ line, TUNER RS485- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio-navigation unit connector E (16P) -3. Check for continuity between test points 1 and 2.
````

## Chunk 2601: AM/FM radio display is blank or no station information is displayed (With Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (With Navigation)
- Source path: `pages\1562.html`
- Chunk ID: `chunk_2e9ff4e330bf`
- Images: none
- Duplicate sources: `pages\2012.html`, `pages\25874.html`, `pages\13445.html`

### Full Text

````text
cle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio-navigation unit connector E (16P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Audio-navigation unit connector E (16P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire between the audio-navigation unit and the tuner unit.

NO

Replace the audio-navigation unit .

- Shorted wire check (TUNER RS485+ line, TUNER RS485- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio-navigation unit connector E (16P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Body ground Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Body ground Is there continuity? YES There is a short to body ground in the wire(s) between the audio-navigation unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485+ and the TUNER RS485 - wires are not shorted to ground. Go to step 11.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio-navigation unit connector E (16P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Body ground

Test point 1 | Tuner unit connector A (10P) No. 7

Test point 2 | Body ground

Is there continuity?

YES

There is a short to body ground in the wire(s) between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485+ and the TUNER RS485 - wires are not shorted to ground. Go to step 11.

- Shorted wire check (TUNER RS485+ line to TUNER RS485- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Tuner unit connector A (10P) No. 7 Is there continuity? YES There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485+ wire and the TUNER RS485 - wire are not shorted. Go to step 12.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Tuner unit connector A (10P) No. 7

Is there continuity?

YES

There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485+ wire and the TUNER RS485 - wire are not shorted. Go to step 12.

- Shorted wire check (TUNER RS485 SH line to another lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Tuner unit connector A (10P) No. 6 Test point 1 Tuner unit connector A (10P) No. 6 Test point 2 Tuner unit connector A (10P) No. 7 Is there continuity? YES There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485 SH wire is not shorted. Go to step 13.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Tuner unit connector A (10P) No. 6

Test point 1 | Tuner unit connector A (10P) No. 6

Test point 2 | Tuner unit connector A (10P) No. 7

Is there continuity?

YES

There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485 SH wire is not shorted. Go to step 13.
````

## Chunk 2602: AM/FM radio display is blank or no station information is displayed (With Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (With Navigation)
- Source path: `pages\1562.html`
- Chunk ID: `chunk_9853ea82a579`
- Images: none
- Duplicate sources: `pages\2012.html`, `pages\25874.html`, `pages\13445.html`

### Full Text

````text
ty? YES There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485 SH wire is not shorted. Go to step 13.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Tuner unit connector A (10P) No. 6

Test point 1 | Tuner unit connector A (10P) No. 6

Test point 2 | Tuner unit connector A (10P) No. 7

Is there continuity?

YES

There is a short in the wires between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485 SH wire is not shorted. Go to step 13.

- Open wire check (TUNER RS485+ line, TUNER RS485- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio-navigation unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Audio-navigation unit connector E (16P) No. 15 Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Audio-navigation unit connector E (16P) No. 16 Is there continuity? YES The TUNER RS485+ and the TUNER RS485 - wires are OK. Go to step 14. NO There is an open in the wire(s) between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio-navigation unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Audio-navigation unit connector E (16P) No. 15

Test point 1 | Tuner unit connector A (10P) No. 7

Test point 2 | Audio-navigation unit connector E (16P) No. 16

Is there continuity?

YES

The TUNER RS485+ and the TUNER RS485 - wires are OK. Go to step 14.

NO

There is an open in the wire(s) between the audio-navigation unit and the tuner unit. Replace the affected shielded harness.

- Tuner unit check (substitution) -1. Substitute a known-good tuner unit. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original tuner unit. NO Replace the audio-navigation unit .

-1. Substitute a known-good tuner unit.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original tuner unit.

NO

Replace the audio-navigation unit .
````

## Chunk 2603: AM/FM radio display is blank or no station information is displayed (Without Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (Without Navigation)
- Source path: `pages\1563.html`
- Chunk ID: `chunk_f22e78895fc7`
- Images: none
- Duplicate sources: `pages\2013.html`, `pages\25875.html`, `pages\13446.html`

### Full Text

````text
# AM/FM radio display is blank or no station information is displayed (Without Navigation)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Turn on the audio system, and select AM or FM. Does the AM or FM radio station information display blankΩ YES The failure is duplicated, go to step 2. NO Intermittent failure, the system is OK at this time. If the AM or FM sound is not heard, go to Poor or no sound with AM/FM radio troubleshooting .

-1. Turn the vehicle to the ON mode.

-2. Turn on the audio system, and select AM or FM.

Does the AM or FM radio station information display blankΩ

YES

The failure is duplicated, go to step 2.

NO

Intermittent failure, the system is OK at this time. If the AM or FM sound is not heard, go to Poor or no sound with AM/FM radio troubleshooting .

- Determine possible failure area (TUNER 6V line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Tuner unit connector A (10P) -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 10 Test point 2 Body ground Is there about 6.0 V? YES The TUNER 6V wire is OK. Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Tuner unit connector A (10P)

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 10

Test point 2 | Body ground

Is there about 6.0 V?

YES

The TUNER 6V wire is OK. Go to step 5.

NO

Go to step 3.

- Open wire check (TUNER 6V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Audio unit connector E (16P) No. 1 Test point 2 Body ground Is there about 6.0 V? YES Repair an open in the wire between the audio unit and the tuner unit. NO The TUNER 6V wire is not open. Go to step 4.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio unit connector E (16P) No. 1

Test point 2 | Body ground

Is there about 6.0 V?

YES

Repair an open in the wire between the audio unit and the tuner unit.

NO

The TUNER 6V wire is not open. Go to step 4.

- Shorted wire check (TUNER 6V line) -1. Disconnect the following connector. Audio unit connector E (16P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the wire between the audio unit and the tuner unit. NO Replace the audio unit .

-1. Disconnect the following connector.

Audio unit connector E (16P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Audio unit connector E (16P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire between the audio unit and the tuner unit.

NO

Replace the audio unit .

- Determine possible failure area (TUNER GND line, others) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 2 Test point 2 Body ground Is there continuity? YES The TUNER GND wire is OK. Go to step 7. NO Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

The TUNER GND wire is OK. Go to step 7.

NO

Go to step 6.

- Open wire check (TUNER GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Audio unit connector E (16P) No.
````

## Chunk 2604: AM/FM radio display is blank or no station information is displayed (Without Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (Without Navigation)
- Source path: `pages\1563.html`
- Chunk ID: `chunk_37811ea98d0f`
- Images: none
- Duplicate sources: `pages\2013.html`, `pages\25875.html`, `pages\13446.html`

### Full Text

````text
ontinuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 2 Test point 2 Body ground Is there continuity? YES The TUNER GND wire is OK. Go to step 7. NO Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

The TUNER GND wire is OK. Go to step 7.

NO

Go to step 6.

- Open wire check (TUNER GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Test point 1 Audio unit connector E (16P) No. 9 Test point 2 Body ground Is there continuity? YES Repair an open in the wire between the audio unit and the tuner unit. NO Replace the audio unit .

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio unit connector E (16P) No. 9

Test point 2 | Body ground

Is there continuity?

YES

Repair an open in the wire between the audio unit and the tuner unit.

NO

Replace the audio unit .

- Determine possible failure area (TUNER 9V line, others) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Tuner unit connector A (10P): disconnected Test point 1 Tuner unit connector A (10P) No. 1 Test point 2 Body ground Is there about 9.0 V? YES The TUNER 9V wire is OK. Go to step 10. NO Go to step 8.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Tuner unit connector A (10P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 1

Test point 2 | Body ground

Is there about 9.0 V?

YES

The TUNER 9V wire is OK. Go to step 10.

NO

Go to step 8.

- Open wire check (TUNER 9V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Tuner unit connector A (10P): disconnected Test point 1 Audio unit connector E (16P) No. 2 Test point 2 Body ground Is there about 9.0 V? YES Repair an open in the wire between the audio unit and the tuner unit. NO The TUNER 9V wire is not open. Go to step 9.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Tuner unit connector A (10P): disconnected

Test point 1 | Audio unit connector E (16P) No. 2

Test point 2 | Body ground

Is there about 9.0 V?

YES

Repair an open in the wire between the audio unit and the tuner unit.

NO

The TUNER 9V wire is not open. Go to step 9.

- Shorted wire check (TUNER 9V line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector E (16P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 2 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the wire between the audio unit and the tuner unit. NO Replace the audio unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio unit connector E (16P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Audio unit connector E (16P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire between the audio unit and the tuner unit.

NO

Replace the audio unit .

- Shorted wire check (TUNER RS485+ line, TUNER RS485- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector E (16P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Body ground Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Body ground Is there continuity? YES There is a short to body ground in the wire(s) between the audio unit and the tuner unit. Replace the affected shielded harness.
````

## Chunk 2605: AM/FM radio display is blank or no station information is displayed (Without Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (Without Navigation)
- Source path: `pages\1563.html`
- Chunk ID: `chunk_bfc6adb501a3`
- Images: none
- Duplicate sources: `pages\2013.html`, `pages\25875.html`, `pages\13446.html`

### Full Text

````text
und

Is there continuity?

YES

Repair a short to body ground in the wire between the audio unit and the tuner unit.

NO

Replace the audio unit .

- Shorted wire check (TUNER RS485+ line, TUNER RS485- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector E (16P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Body ground Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Body ground Is there continuity? YES There is a short to body ground in the wire(s) between the audio unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485+ and the TUNER RS485 - wires are not shorted to ground. Go to step 11.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio unit connector E (16P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Body ground

Test point 1 | Tuner unit connector A (10P) No. 7

Test point 2 | Body ground

Is there continuity?

YES

There is a short to body ground in the wire(s) between the audio unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485+ and the TUNER RS485 - wires are not shorted to ground. Go to step 11.

- Shorted wire check (TUNER RS485+ line to TUNER RS485- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Tuner unit connector A (10P) No. 7 Is there continuity? YES There is a short in the wires between the audio unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485+ wire and the TUNER RS485 - wire are not shorted. Go to step 12.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Tuner unit connector A (10P) No. 7

Is there continuity?

YES

There is a short in the wires between the audio unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485+ wire and the TUNER RS485 - wire are not shorted. Go to step 12.

- Shorted wire check (TUNER RS485 SH line to another lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Tuner unit connector A (10P) No. 6 Test point 1 Tuner unit connector A (10P) No. 6 Test point 2 Tuner unit connector A (10P) No. 7 Is there continuity? YES There is a short in the wires between the audio unit and the tuner unit. Replace the affected shielded harness. NO The TUNER RS485 SH wire is not shorted. Go to step 13.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Tuner unit connector A (10P) No. 6

Test point 1 | Tuner unit connector A (10P) No. 6

Test point 2 | Tuner unit connector A (10P) No. 7

Is there continuity?

YES

There is a short in the wires between the audio unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485 SH wire is not shorted. Go to step 13.

- Open wire check (TUNER RS485+ line, TUNER RS485- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Audio unit connector E (16P) No. 15 Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Audio unit connector E (16P) No. 16 Is there continuity? YES The TUNER RS485+ and the TUNER RS485 - wires are OK. Go to step 14. NO There is an open in the wire(s) between the audio unit and the tuner unit.
````

## Chunk 2606: AM/FM radio display is blank or no station information is displayed (Without Navigation)

- Title: AM/FM radio display is blank or no station information is displayed (Without Navigation)
- Source path: `pages\1563.html`
- Chunk ID: `chunk_da691dfc067d`
- Images: none
- Duplicate sources: `pages\2013.html`, `pages\25875.html`, `pages\13446.html`

### Full Text

````text
Is there continuity?

YES

There is a short in the wires between the audio unit and the tuner unit. Replace the affected shielded harness.

NO

The TUNER RS485 SH wire is not shorted. Go to step 13.

- Open wire check (TUNER RS485+ line, TUNER RS485- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tuner unit connector A (10P): disconnected Audio unit connector E (16P): disconnected Test point 1 Tuner unit connector A (10P) No. 5 Test point 2 Audio unit connector E (16P) No. 15 Test point 1 Tuner unit connector A (10P) No. 7 Test point 2 Audio unit connector E (16P) No. 16 Is there continuity? YES The TUNER RS485+ and the TUNER RS485 - wires are OK. Go to step 14. NO There is an open in the wire(s) between the audio unit and the tuner unit. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Tuner unit connector A (10P): disconnected

Audio unit connector E (16P): disconnected

Test point 1 | Tuner unit connector A (10P) No. 5

Test point 2 | Audio unit connector E (16P) No. 15

Test point 1 | Tuner unit connector A (10P) No. 7

Test point 2 | Audio unit connector E (16P) No. 16

Is there continuity?

YES

The TUNER RS485+ and the TUNER RS485 - wires are OK. Go to step 14.

NO

There is an open in the wire(s) between the audio unit and the tuner unit. Replace the affected shielded harness.

- Tuner unit check (substitution) -1. Substitute a known-good tuner unit. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original tuner unit. NO Replace the audio unit .

-1. Substitute a known-good tuner unit.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original tuner unit.

NO

Replace the audio unit .
````

## Chunk 2607: Active sound control does not work (With Stereo Amplifier)

- Title: Active sound control does not work (With Stereo Amplifier)
- Source path: `pages\1564.html`
- Chunk ID: `chunk_a5e674ff4414`
- Images: `images\GHH399328.png`, `images\GHH399329.png`, `images\GHH399330.jpeg`
- Duplicate sources: `pages\2014.html`, `pages\25876.html`, `pages\13447.html`

### Full Text

````text
# Active sound control does not work (With Stereo Amplifier)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check for F-CAN and B-CAN DTCs and resolve them before troubleshooting.

- Check the connectors for poor connections or loose terminals.

- Determine possible failure area (speaker output circuit, others): Go into the System Diagnostic Mode, and use the speaker check mode in the Audio Check menu: With navigation Without navigation Is the sound quality normal at each speaker? YES Go to step 2. NO Go to No sound is heard from all the speakers (display is normal) troubleshooting .

Go into the System Diagnostic Mode, and use the speaker check mode in the Audio Check menu:

- With navigation

- Without navigation

Is the sound quality normal at each speaker?

YES

Go to step 2.

NO

Go to No sound is heard from all the speakers (display is normal) troubleshooting .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A18 Fuse No. B7 Are the fuses OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, check for a short in the No. A18 fuse and/or the No. B7 fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A18

Fuse | No. B7

Are the fuses OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, check for a short in the No. A18 fuse and/or the No. B7 fuse circuits.

- Open wire check (+B BACK UP line) -1. Disconnect the following connector. Active sound control unit 20P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 11 Test point 2 Body ground Is there battery voltage? YES The +B BACK UP wire is OK. Go to step 4. NO Repair an open in the wire.

-1. Disconnect the following connector.

Active sound control unit 20P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 11

Test point 2 | Body ground

Is there battery voltage?

YES

The +B BACK UP wire is OK. Go to step 4.

NO

Repair an open in the wire.

- Open wire check (IG1 METER line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 12 Test point 2 Body ground Is there battery voltage? YES The IG1 METER wire is OK. Go to step 5. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 12

Test point 2 | Body ground

Is there battery voltage?

YES

The IG1 METER wire is OK. Go to step 5.

NO

Repair an open in the wire.

- Open wire check (SWD+B line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 3 Test point 2 Body ground Is there battery voltage? YES The SWD+B wire is OK. Go to step 6. NO Repair an open in the wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

The SWD+B wire is OK. Go to step 6.

NO

Repair an open in the wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 1 Test point 2 Body ground Is there 1.0 Ω or less? YES The GND wire is OK. Go to step 7. NO Repair an open in the wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 1
````

## Chunk 2608: Active sound control does not work (With Stereo Amplifier)

- Title: Active sound control does not work (With Stereo Amplifier)
- Source path: `pages\1564.html`
- Chunk ID: `chunk_fbfe376bfbea`
- Images: `images\GHH399328.png`, `images\GHH399329.png`, `images\GHH399330.jpeg`
- Duplicate sources: `pages\2014.html`, `pages\25876.html`, `pages\13447.html`

### Full Text

````text
2 | Body ground

Is there battery voltage?

YES

The SWD+B wire is OK. Go to step 6.

NO

Repair an open in the wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 1 Test point 2 Body ground Is there 1.0 Ω or less? YES The GND wire is OK. Go to step 7. NO Repair an open in the wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 1

Test point 2 | Body ground

Is there 1.0 Ω or less?

YES

The GND wire is OK. Go to step 7.

NO

Repair an open in the wire or poor ground (G505).

- Determine possible failure area (ANC F MIC+8V circuit, others) -1. Reconnect the active sound control unit 20P connector. -2. Disconnect the following connector. HFL microphone 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 HFL microphone 8P connector No. 8 Test point 2 HFL microphone 8P connector No. 1 Is there about 8.0 V? YES Go to step 12. NO Go to step 8.

-1. Reconnect the active sound control unit 20P connector.

-2. Disconnect the following connector.

HFL microphone 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | HFL microphone 8P connector No. 8

Test point 2 | HFL microphone 8P connector No. 1

Is there about 8.0 V?

YES

Go to step 12.

NO

Go to step 8.

- Determine possible failure area (ANC F MIC+8V line, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 HFL microphone 8P connector No. 8 Test point 2 Body ground Is there about 8.0 V? YES There is an open in the MIC GND wire. Replace the affected shielded harness. NO Go to step 9.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | HFL microphone 8P connector No. 8

Test point 2 | Body ground

Is there about 8.0 V?

YES

There is an open in the MIC GND wire. Replace the affected shielded harness.

NO

Go to step 9.

- Open wire check (ANC F MIC+8V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 Active sound control unit 20P connector No. 18 Test point 2 Body ground Is there about 8.0 V? YES There is an open in the wire. Replace the affected shielded harness. NO The ANC F MIC+8V wire is not open. Go to step 10.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 18

Test point 2 | Body ground

Is there about 8.0 V?

YES

There is an open in the wire. Replace the affected shielded harness.

NO

The ANC F MIC+8V wire is not open. Go to step 10.

- Shorted wire check (ANC F MIC+8V line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Active sound control unit 20P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode HFL microphone 8P connector: disconnected Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 18 Test point 2 Body ground Is there 1 MΩ or more? YES The ANC F MIC+8V wire is not shorted to ground. Go to step 11. NO There is a short to body ground in the wire. Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Active sound control unit 20P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

HFL microphone 8P connector: disconnected

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 18

Test point 2 | Body ground

Is there 1 MΩ or more?

YES
````

## Chunk 2609: Active sound control does not work (With Stereo Amplifier)

- Title: Active sound control does not work (With Stereo Amplifier)
- Source path: `pages\1564.html`
- Chunk ID: `chunk_75b05eb3fd52`
- Images: `images\GHH399328.png`, `images\GHH399329.png`, `images\GHH399330.jpeg`
- Duplicate sources: `pages\2014.html`, `pages\25876.html`, `pages\13447.html`

### Full Text

````text
FL microphone 8P connector: disconnected Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 18 Test point 2 Body ground Is there 1 MΩ or more? YES The ANC F MIC+8V wire is not shorted to ground. Go to step 11. NO There is a short to body ground in the wire. Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Active sound control unit 20P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

HFL microphone 8P connector: disconnected

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 18

Test point 2 | Body ground

Is there 1 MΩ or more?

YES

The ANC F MIC+8V wire is not shorted to ground. Go to step 11.

NO

There is a short to body ground in the wire. Replace the affected shielded harness.

- Shorted wire check (ANC F MIC+8V line to SH ANC F MIC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode HFL microphone 8P connector: disconnected Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 7 Test point 2 Active sound control unit 20P connector No. 18 Is there 1 MΩ or more? YES Replace the active sound control unit . NO There is a short in the wires. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

HFL microphone 8P connector: disconnected

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 7

Test point 2 | Active sound control unit 20P connector No. 18

Is there 1 MΩ or more?

YES

Replace the active sound control unit .

NO

There is a short in the wires. Replace the affected shielded harness.

- Determine possible failure area (HFL microphone, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect the HFL microphone 8P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. NOTE: Use the voltmeter in AC range. Test condition Vehicle ON mode, make a loud noise like clapping your hands in front of the HFL microphone. Test point 1 Active sound control unit 20P connector No. 7 Test point 2 Active sound control unit 20P connector No. 18 Does the voltage change when making a loud noise in front of the microphone? YES Go to step 13. NO Replace the HFL microphone .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect the HFL microphone 8P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

NOTE: Use the voltmeter in AC range.

Test condition | Vehicle ON mode, make a loud noise like clapping your hands in front of the HFL microphone.

Test point 1 | Active sound control unit 20P connector No. 7

Test point 2 | Active sound control unit 20P connector No. 18

Does the voltage change when making a loud noise in front of the microphone?

YES

Go to step 13.

NO

Replace the HFL microphone .

- Shorted wire check (ANC lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Stereo amplifier connector C (16P) Active sound control unit 20P connector -3. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector C (16P): disconnected Active sound control unit 20P connector: disconnected Connector Terminal Active sound control unit 20P connector No. 9 No. 10 No. 19 No. 20 Is there 1 MΩ or more? YES The ANC wires are not shorted to ground. Go to step 14. NO There is a short to body ground in the wire(s). Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Stereo amplifier connector C (16P)

Active sound control unit 20P connector

-3. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

Connector | Terminal

Active sound control unit 20P connector | No. 9

No. 10

No. 19

No. 20

Is there 1 MΩ or more?

YES

The ANC wires are not shorted to ground. Go to step 14.

NO

There is a short to body ground in the wire(s).
````

## Chunk 2610: Active sound control does not work (With Stereo Amplifier)

- Title: Active sound control does not work (With Stereo Amplifier)
- Source path: `pages\1564.html`
- Chunk ID: `chunk_43150a767a3f`
- Images: `images\GHH399328.png`, `images\GHH399329.png`, `images\GHH399330.jpeg`
- Duplicate sources: `pages\2014.html`, `pages\25876.html`, `pages\13447.html`

### Full Text

````text
Is there 1 MΩ or more? YES The ANC wires are not shorted to ground. Go to step 14. NO There is a short to body ground in the wire(s). Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Stereo amplifier connector C (16P)

Active sound control unit 20P connector

-3. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

Connector | Terminal

Active sound control unit 20P connector | No. 9

No. 10

No. 19

No. 20

Is there 1 MΩ or more?

YES

The ANC wires are not shorted to ground. Go to step 14.

NO

There is a short to body ground in the wire(s). Replace the affected shielded harness.

- Shorted wire check (ANC lines) 2 -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector C (16P): disconnected Active sound control unit 20P connector: disconnected Test point 1: Active sound control unit 20P connector Test points 2: Active sound control unit 20P connector No. 8 No. 9, No. 10, No. 19, No. 20 No. 9 No. 10, No. 19, No. 20 No. 10 No. 19, No. 20 No. 19 No. 20 Is there 1 MΩ or more between all of the terminals? YES The ANC wires are not shorted. Go to step 15. NO There is a short in the wires. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

Test point 1: Active sound control unit 20P connector | Test points 2: Active sound control unit 20P connector

Active sound control unit 20P connector

Active sound control unit 20P connector

No. 8 | No. 9, No. 10, No. 19, No. 20

No. 9 | No. 10, No. 19, No. 20

No. 10 | No. 19, No. 20

No. 19 | No. 20

Is there 1 MΩ or more between all of the terminals?

YES

The ANC wires are not shorted. Go to step 15.

NO

There is a short in the wires. Replace the affected shielded harness.

- Open wire check (ANC lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector C (16P): disconnected Active sound control unit 20P connector: disconnected Test point 1: Stereo amplifier connector C (16P) Test point 2: Active sound control unit 20P connector No. 1 * No. 9 * No. 2 No. 10 No. 9 * No. 19 * No. 10 No. 20 *: Except 2-door Is there 1.0 Ω or less? YES: With CMBS The ANC wires are OK. Go to step 16. YES: Without CMBS The ANC wires are OK. Go to step 17. NO There is an open in the wire(s). Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

Test point 1: Stereo amplifier connector C (16P) | Test point 2: Active sound control unit 20P connector

Stereo amplifier connector C (16P)

Active sound control unit 20P connector

No. 1 * | No. 9 *

No. 2 | No. 10

No. 9 * | No. 19 *

No. 10 | No. 20

*: Except 2-door

Is there 1.0 Ω or less?

YES: With CMBS

The ANC wires are OK. Go to step 16.

YES: Without CMBS

The ANC wires are OK. Go to step 17.

NO

There is an open in the wire(s). Replace the affected shielded harness.

- Open wire check (F-CAN C_H, F-CAN C_L lines) -1. Disconnect the following connector. CAN gateway 16P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector C (16P): disconnected Active sound control unit 20P connector: disconnected CAN gateway 16P connector: disconnected Test point 1 CAN gateway 16P connector No. 5 (female terminals): Test point 2 Active sound control unit 20P connector No. 4 Test point 1 CAN gateway 16P connector No. 13 (female terminals): Test point 2 Active sound control unit 20P connector No. 5 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The F-CAN C_H and the F-CAN C_L wires are OK. Go to step 18. NO Repair an open in the wire(s).

-1. Disconnect the following connector.

CAN gateway 16P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected
````

## Chunk 2611: Active sound control does not work (With Stereo Amplifier)

- Title: Active sound control does not work (With Stereo Amplifier)
- Source path: `pages\1564.html`
- Chunk ID: `chunk_62c78370f2a3`
- Images: `images\GHH399328.png`, `images\GHH399329.png`, `images\GHH399330.jpeg`
- Duplicate sources: `pages\2014.html`, `pages\25876.html`, `pages\13447.html`

### Full Text

````text
connector C (16P): disconnected Active sound control unit 20P connector: disconnected CAN gateway 16P connector: disconnected Test point 1 CAN gateway 16P connector No. 5 (female terminals): Test point 2 Active sound control unit 20P connector No. 4 Test point 1 CAN gateway 16P connector No. 13 (female terminals): Test point 2 Active sound control unit 20P connector No. 5 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The F-CAN C_H and the F-CAN C_L wires are OK. Go to step 18. NO Repair an open in the wire(s).

-1. Disconnect the following connector.

CAN gateway 16P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

CAN gateway 16P connector: disconnected

Test point 1 | CAN gateway 16P connector No. 5 (female terminals):

Test point 2 | Active sound control unit 20P connector No. 4

Test point 1 | CAN gateway 16P connector No. 13 (female terminals):

Test point 2 | Active sound control unit 20P connector No. 5

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The F-CAN C_H and the F-CAN C_L wires are OK. Go to step 18.

NO

Repair an open in the wire(s).

- Open wire check (F-CAN_H, F-CAN_L lines) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector C (16P): disconnected Active sound control unit 20P connector: disconnected PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 15 Test point 2 Active sound control unit 20P connector No. 4 Test point 1 PCM connector A (50P) No. 2 (58P) No. 27 Test point 2 Active sound control unit 20P connector No. 5 Is there 1.0 Ω or less? YES The F-CAN_H and the F-CAN_L wires are OK. Go to step 18. NO Repair an open in the wire(s).

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector C (16P): disconnected

Active sound control unit 20P connector: disconnected

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 15

Test point 2 | Active sound control unit 20P connector No. 4

Test point 1 | PCM connector A (50P) No. 2 (58P) No. 27

Test point 2 | Active sound control unit 20P connector No. 5

Is there 1.0 Ω or less?

YES

The F-CAN_H and the F-CAN_L wires are OK. Go to step 18.

NO

Repair an open in the wire(s).

- Active sound control unit check -1. Substitute a known-good active sound control unit . -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original active sound control unit. NO Replace the stereo amplifier .

-1. Substitute a known-good active sound control unit .

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original active sound control unit.

NO

Replace the stereo amplifier .
````

## Chunk 2612: Active sound control does not work (Without Stereo Amplifier)

- Title: Active sound control does not work (Without Stereo Amplifier)
- Source path: `pages\1565.html`
- Chunk ID: `chunk_a558e18cc581`
- Images: `images\GHH399331.png`, `images\GHH399332.png`, `images\GHH399333.jpeg`
- Duplicate sources: `pages\2015.html`, `pages\25877.html`, `pages\13448.html`

### Full Text

````text
# Active sound control does not work (Without Stereo Amplifier)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check for F-CAN and B-CAN DTCs and resolve them before troubleshooting.

- Check the connectors for poor connections or loose terminals.

- Determine possible failure area (speaker output circuit, others) -1. Go into the System Diagnostic Mode, and use the speaker check mode in the Audio Check menu . Is the sound quality normal at each speaker? YES Go to step 2. NO Go to No sound is heard from all the speakers (display is normal) troubleshooting .

-1. Go into the System Diagnostic Mode, and use the speaker check mode in the Audio Check menu .

Is the sound quality normal at each speaker?

YES

Go to step 2.

NO

Go to No sound is heard from all the speakers (display is normal) troubleshooting .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A18 Fuse No. B7 Are the fuses OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, check for a short in the No. A18 fuse and/or the No. B7 fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A18

Fuse | No. B7

Are the fuses OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, check for a short in the No. A18 fuse and/or the No. B7 fuse circuits.

- Open wire check (+B BACK UP line) -1. Disconnect the following connector. Active sound control unit 20P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 11 Test point 2 Body ground Is there battery voltage? YES The +B BACK UP wire is OK. Go to step 4. NO Repair an open in the wire.

-1. Disconnect the following connector.

Active sound control unit 20P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 11

Test point 2 | Body ground

Is there battery voltage?

YES

The +B BACK UP wire is OK. Go to step 4.

NO

Repair an open in the wire.

- Open wire check (IG1 METER line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 12 Test point 2 Body ground Is there battery voltage? YES The IG1 METER wire is OK. Go to step 5. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 12

Test point 2 | Body ground

Is there battery voltage?

YES

The IG1 METER wire is OK. Go to step 5.

NO

Repair an open in the wire.

- Determine possible failure area (SWD+B line, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 3 Test point 2 Body ground Is there battery voltage? YES The SWD+B wire is OK. Go to step 8. NO Go to step 6.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

The SWD+B wire is OK. Go to step 8.

NO

Go to step 6.

- Open wire check (SWD+B line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Audio unit connector A (24P) No. 21 Test point 2 Body ground Is there battery voltage? YES Repair an open in the wire. NO The SWD+B wire is not open. Go to step 7.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Audio unit connector A (24P) No. 21

Test point 2 | Body ground

Is there battery voltage?

YES

Repair an open in the wire.

NO

The SWD+B wire is not open. Go to step 7.

- Shorted wire check (SWD+B line) -1. Turn the vehicle to the OFF (LOCK) mode. -2.
````

## Chunk 2613: Active sound control does not work (Without Stereo Amplifier)

- Title: Active sound control does not work (Without Stereo Amplifier)
- Source path: `pages\1565.html`
- Chunk ID: `chunk_c1ec01ce3d95`
- Images: `images\GHH399331.png`, `images\GHH399332.png`, `images\GHH399333.jpeg`
- Duplicate sources: `pages\2015.html`, `pages\25877.html`, `pages\13448.html`

### Full Text

````text
s OK. Go to step 8.

NO

Go to step 6.

- Open wire check (SWD+B line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Active sound control unit 20P connector: disconnected Test point 1 Audio unit connector A (24P) No. 21 Test point 2 Body ground Is there battery voltage? YES Repair an open in the wire. NO The SWD+B wire is not open. Go to step 7.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Active sound control unit 20P connector: disconnected

Test point 1 | Audio unit connector A (24P) No. 21

Test point 2 | Body ground

Is there battery voltage?

YES

Repair an open in the wire.

NO

The SWD+B wire is not open. Go to step 7.

- Shorted wire check (SWD+B line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector A (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 21 Test point 2 Body ground Is there 1 MΩ or more? YES Replace the audio unit . NO Repair a short to body ground in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio unit connector A (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 21

Test point 2 | Body ground

Is there 1 MΩ or more?

YES

Replace the audio unit .

NO

Repair a short to body ground in the wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 1 Test point 2 Body ground Is there 1.0 Ω or less? YES The GND wire is OK. Go to step 9. NO Repair an open in the wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 1

Test point 2 | Body ground

Is there 1.0 Ω or less?

YES

The GND wire is OK. Go to step 9.

NO

Repair an open in the wire or poor ground (G505).

- Determine possible failure area (ANC F MIC+8V circuit, others) -1. Reconnect the active sound control unit 20P connector. -2. Disconnect the following connector. HFL microphone 8P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 HFL microphone 8P connector No. 8 Test point 2 HFL microphone 8P connector No. 1 Is there about 8.0 V? YES Go to step 14. NO Go to step 10.

-1. Reconnect the active sound control unit 20P connector.

-2. Disconnect the following connector.

HFL microphone 8P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | HFL microphone 8P connector No. 8

Test point 2 | HFL microphone 8P connector No. 1

Is there about 8.0 V?

YES

Go to step 14.

NO

Go to step 10.

- Determine possible failure area (ANC F MIC+8V line, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 HFL microphone 8P connector No. 8 Test point 2 Body ground Is there about 8.0 V? YES There is an open in the MIC GND wire. Replace the affected shielded harness. NO Go to step 11.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | HFL microphone 8P connector No. 8

Test point 2 | Body ground

Is there about 8.0 V?

YES

There is an open in the MIC GND wire. Replace the affected shielded harness.

NO

Go to step 11.

- Open wire check (ANC F MIC+8V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 Active sound control unit 20P connector No.
````

## Chunk 2614: Active sound control does not work (Without Stereo Amplifier)

- Title: Active sound control does not work (Without Stereo Amplifier)
- Source path: `pages\1565.html`
- Chunk ID: `chunk_d59bce215f3c`
- Images: `images\GHH399331.png`, `images\GHH399332.png`, `images\GHH399333.jpeg`
- Duplicate sources: `pages\2015.html`, `pages\25877.html`, `pages\13448.html`

### Full Text

````text
ON mode HFL microphone 8P connector: disconnected Test point 1 HFL microphone 8P connector No. 8 Test point 2 Body ground Is there about 8.0 V? YES There is an open in the MIC GND wire. Replace the affected shielded harness. NO Go to step 11.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | HFL microphone 8P connector No. 8

Test point 2 | Body ground

Is there about 8.0 V?

YES

There is an open in the MIC GND wire. Replace the affected shielded harness.

NO

Go to step 11.

- Open wire check (ANC F MIC+8V line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode HFL microphone 8P connector: disconnected Test point 1 Active sound control unit 20P connector No. 18 Test point 2 Body ground Is there about 8.0 V? YES There is an open in the wire. Replace the affected shielded harness. NO The ANC F MIC+8V wire is not open. Go to step 12.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

HFL microphone 8P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 18

Test point 2 | Body ground

Is there about 8.0 V?

YES

There is an open in the wire. Replace the affected shielded harness.

NO

The ANC F MIC+8V wire is not open. Go to step 12.

- Shorted wire check (ANC F MIC+8V line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Active sound control unit 20P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode HFL microphone 8P connector: disconnected Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 18 Test point 2 Body ground Is there 1 MΩ or more? YES The ANC F MIC+8V wire is not shorted to ground. Go to step 13. NO There is a short to body ground in the wire. Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Active sound control unit 20P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

HFL microphone 8P connector: disconnected

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 18

Test point 2 | Body ground

Is there 1 MΩ or more?

YES

The ANC F MIC+8V wire is not shorted to ground. Go to step 13.

NO

There is a short to body ground in the wire. Replace the affected shielded harness.

- Shorted wire check (ANC F MIC+8V line to SH ANC F MIC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode HFL microphone 8P connector: disconnected Active sound control unit 20P connector: disconnected Test point 1 Active sound control unit 20P connector No. 7 Test point 2 Active sound control unit 20P connector No. 18 Is there 1 MΩ or more? YES Replace the active sound control unit . NO There is a short in the wires. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

HFL microphone 8P connector: disconnected

Active sound control unit 20P connector: disconnected

Test point 1 | Active sound control unit 20P connector No. 7

Test point 2 | Active sound control unit 20P connector No. 18

Is there 1 MΩ or more?

YES

Replace the active sound control unit .

NO

There is a short in the wires. Replace the affected shielded harness.

- Determine possible failure area (HFL microphone, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect the HFL microphone 8P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. NOTE: Use the voltmeter in AC range. Test condition Vehicle ON mode, make a loud noise like clapping your hands in front of the HFL microphone. Test point 1 Active sound control unit 20P connector No. 7 Test point 2 Active sound control unit 20P connector No. 18 Does the voltage change when making a loud noise in front of the microphone? YES Go to step 15. NO Replace the HFL microphone .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect the HFL microphone 8P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

NOTE: Use the voltmeter in AC range.
````

## Chunk 2615: Active sound control does not work (Without Stereo Amplifier)

- Title: Active sound control does not work (Without Stereo Amplifier)
- Source path: `pages\1565.html`
- Chunk ID: `chunk_987274cf0d98`
- Images: `images\GHH399331.png`, `images\GHH399332.png`, `images\GHH399333.jpeg`
- Duplicate sources: `pages\2015.html`, `pages\25877.html`, `pages\13448.html`

### Full Text

````text
s) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect the HFL microphone 8P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. NOTE: Use the voltmeter in AC range. Test condition Vehicle ON mode, make a loud noise like clapping your hands in front of the HFL microphone. Test point 1 Active sound control unit 20P connector No. 7 Test point 2 Active sound control unit 20P connector No. 18 Does the voltage change when making a loud noise in front of the microphone? YES Go to step 15. NO Replace the HFL microphone .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect the HFL microphone 8P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

NOTE: Use the voltmeter in AC range.

Test condition | Vehicle ON mode, make a loud noise like clapping your hands in front of the HFL microphone.

Test point 1 | Active sound control unit 20P connector No. 7

Test point 2 | Active sound control unit 20P connector No. 18

Does the voltage change when making a loud noise in front of the microphone?

YES

Go to step 15.

NO

Replace the HFL microphone .

- Shorted wire check (ANC lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector C (32P): disconnected Active sound control unit 20P connector -3. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode Audio unit connector C (32P): disconnected Active sound control unit 20P connector: disconnected Connector Terminal Active sound control unit 20P connector No. 9 No. 10 No. 19 No. 20 Is there 1 MΩ or more? YES The ANC wires are not shorted to ground. Go to step 16. NO There is a short to body ground in the wire(s). Replace the affected shielded harness.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector C (32P): disconnected

Active sound control unit 20P connector

-3. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector C (32P): disconnected

Active sound control unit 20P connector: disconnected

Connector | Terminal

Active sound control unit 20P connector | No. 9

No. 10

No. 19

No. 20

Is there 1 MΩ or more?

YES

The ANC wires are not shorted to ground. Go to step 16.

NO

There is a short to body ground in the wire(s). Replace the affected shielded harness.

- Shorted wire check (ANC lines) 2 -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector C (32P): disconnected Active sound control unit 20P connector: disconnected Test point 1: Active sound control unit 20P connector Test points 2: Active sound control unit 20P connector No. 8 No. 9, No. 10, No. 19, No. 20 No. 9 No. 10, No. 19, No. 20 No. 10 No. 19, No. 20 No. 19 No. 20 Is there 1 MΩ or more between all of the terminals? YES The ANC wires are not shorted. Go to step 17. NO There is a short in the wires. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector C (32P): disconnected

Active sound control unit 20P connector: disconnected

Test point 1: Active sound control unit 20P connector | Test points 2: Active sound control unit 20P connector

Active sound control unit 20P connector

Active sound control unit 20P connector

No. 8 | No. 9, No. 10, No. 19, No. 20

No. 9 | No. 10, No. 19, No. 20

No. 10 | No. 19, No. 20

No. 19 | No. 20

Is there 1 MΩ or more between all of the terminals?

YES

The ANC wires are not shorted. Go to step 17.

NO

There is a short in the wires. Replace the affected shielded harness.

- Open wire check (ANC lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector C (32P): disconnected Active sound control unit 20P connector: disconnected Test point 1: Audio unit connector C (32P) Test point 2: Active sound control unit 20P connector No. 2 No. 9 No. 18 No. 10 No. 1 No. 19 No. 7 No. 20 Is there 1.0 Ω or less? YES The ANC wires are OK. Go to step 18. NO There is an open in the wire(s). Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector C (32P): disconnected
````

## Chunk 2616: Active sound control does not work (Without Stereo Amplifier)

- Title: Active sound control does not work (Without Stereo Amplifier)
- Source path: `pages\1565.html`
- Chunk ID: `chunk_6741cc8e34f7`
- Images: `images\GHH399331.png`, `images\GHH399332.png`, `images\GHH399333.jpeg`
- Duplicate sources: `pages\2015.html`, `pages\25877.html`, `pages\13448.html`

### Full Text

````text
all of the terminals?

YES

The ANC wires are not shorted. Go to step 17.

NO

There is a short in the wires. Replace the affected shielded harness.

- Open wire check (ANC lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector C (32P): disconnected Active sound control unit 20P connector: disconnected Test point 1: Audio unit connector C (32P) Test point 2: Active sound control unit 20P connector No. 2 No. 9 No. 18 No. 10 No. 1 No. 19 No. 7 No. 20 Is there 1.0 Ω or less? YES The ANC wires are OK. Go to step 18. NO There is an open in the wire(s). Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector C (32P): disconnected

Active sound control unit 20P connector: disconnected

Test point 1: Audio unit connector C (32P) | Test point 2: Active sound control unit 20P connector

Audio unit connector C (32P)

Active sound control unit 20P connector

No. 2 | No. 9

No. 18 | No. 10

No. 1 | No. 19

No. 7 | No. 20

Is there 1.0 Ω or less?

YES

The ANC wires are OK. Go to step 18.

NO

There is an open in the wire(s). Replace the affected shielded harness.

- Open wire check (F-CAN C_H, F-CAN C_L lines) -1. Disconnect the following connector. CAN gateway 16P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector C (32P): disconnected Active sound control unit 20P connector: disconnected CAN gateway 16P connector: disconnected Test point 1 CAN gateway 16P connector No. 5 (female terminals): Test point 2 Active sound control unit 20P connector No. 4 Test point 1 CAN gateway 16P connector No. 13 (female terminals): Test point 2 Active sound control unit 20P connector No. 5 Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The F-CAN C_H and the F-CAN C_L wires are OK. Go to step 19. NO Repair an open in the wire(s).

-1. Disconnect the following connector.

CAN gateway 16P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector C (32P): disconnected

Active sound control unit 20P connector: disconnected

CAN gateway 16P connector: disconnected

Test point 1 | CAN gateway 16P connector No. 5 (female terminals):

Test point 2 | Active sound control unit 20P connector No. 4

Test point 1 | CAN gateway 16P connector No. 13 (female terminals):

Test point 2 | Active sound control unit 20P connector No. 5

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The F-CAN C_H and the F-CAN C_L wires are OK. Go to step 19.

NO

Repair an open in the wire(s).

- Active sound control unit check -1. Substitute a known-good active sound control unit . -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original active sound control unit. NO Replace the audio unit .

-1. Substitute a known-good active sound control unit .

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original active sound control unit.

NO

Replace the audio unit .
````

## Chunk 2617: Audio remote-HFL switch does not work properly (audio unit buttons work) (With Multi-Information Display)

- Title: Audio remote-HFL switch does not work properly (audio unit buttons work) (With Multi-Information Display)
- Source path: `pages\1566.html`
- Chunk ID: `chunk_a4ca45bf02dc`
- Images: none
- Duplicate sources: `pages\2016.html`, `pages\25878.html`, `pages\13449.html`

### Full Text

````text
# Audio remote-HFL switch does not work properly (audio unit buttons work) (With Multi-Information Display)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Using the audio remote-HFL switch buttons, check if the audio system and the HFL system operates properly. Are the audio system and the HFL system operation OK? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Using the audio remote-HFL switch buttons, check if the audio system and the HFL system operates properly.

Are the audio system and the HFL system operation OK?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (audio remote-HFL switch, others) -1. Go into the System Diagnostic Mode, and use the Hard Key test under the Unit Check menu . -2. Check the audio remote-HFL switch status. Do all of the buttons fail to respond? YES Go to step 3. NO Replace the audio remote-HFL switch .

-1. Go into the System Diagnostic Mode, and use the Hard Key test under the Unit Check menu .

-2. Check the audio remote-HFL switch status.

Do all of the buttons fail to respond?

YES

Go to step 3.

NO

Replace the audio remote-HFL switch .

- Gauge control module DTCs check -1. Check for gauge control module DTCs with the HDS . DTC Description DTC B1195 Gauge control module lost communication with Audio Remote Switch (LIN bus connected) Is DTC B1195 indicated? YES Go to the indicated DTC's troubleshooting . NO Go to step 4.

-1. Check for gauge control module DTCs with the HDS .

DTC Description | DTC

B1195 Gauge control module lost communication with Audio Remote Switch (LIN bus connected)

Is DTC B1195 indicated?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 4.

- Open wire check (B-CAN_H line, B-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Gauge control module connector A (32P) Audio-navigation unit connector A (24P) (with navigation) Audio unit connector A (24P) (without navigation) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Gauge control module connector A (32P): disconnected Audio-navigation unit connector A (24P): disconnected Audio unit connector A (24P): disconnected Test point 1 Gauge control module connector A (32P) No. 30 Test point 2 Audio-navigation unit connector A (24P) No. 14 Audio unit connector A (24P) No. 14 Test point 1 Gauge control module connector A (32P) No. 31 Test point 2 Audio-navigation unit connector A (24P) No. 24 Audio unit connector A (24P) No. 24 Is there continuity? YES: With navigation Replace the audio-navigation unit . YES: Without navigation Replace the audio unit . NO Repair an open in the wire(s) between the audio-navigation unit or the audio unit and the gauge control module.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Gauge control module connector A (32P)

Audio-navigation unit connector A (24P) (with navigation)

Audio unit connector A (24P) (without navigation)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Gauge control module connector A (32P): disconnected

Audio-navigation unit connector A (24P): disconnected

Audio unit connector A (24P): disconnected

Test point 1 | Gauge control module connector A (32P) No. 30

Test point 2 | Audio-navigation unit connector A (24P) No. 14

Audio unit connector A (24P) No. 14

Test point 1 | Gauge control module connector A (32P) No. 31

Test point 2 | Audio-navigation unit connector A (24P) No. 24

Audio unit connector A (24P) No. 24

Is there continuity?

YES: With navigation

Replace the audio-navigation unit .

YES: Without navigation

Replace the audio unit .

NO

Repair an open in the wire(s) between the audio-navigation unit or the audio unit and the gauge control module.
````

## Chunk 2618: Audio remote-HFL switch does not work properly (audio unit buttons work) (Without Multi-Information Display)

- Title: Audio remote-HFL switch does not work properly (audio unit buttons work) (Without Multi-Information Display)
- Source path: `pages\1567.html`
- Chunk ID: `chunk_7c9b89bb79b7`
- Images: none
- Duplicate sources: `pages\2017.html`, `pages\25879.html`, `pages\13450.html`

### Full Text

````text
# Audio remote-HFL switch does not work properly (audio unit buttons work) (Without Multi-Information Display)

NOTE:

- Check the vehicle 12 volt battery condition first .

- If any button of the audio remote-HFL switch does not work, do the Knob Check in the System Diagnostic Mode .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Using the audio remote-HFL switch buttons, check if the audio system and the HFL system operates properly. Are the audio system and the HFL system operation OK? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Using the audio remote-HFL switch buttons, check if the audio system and the HFL system operates properly.

Are the audio system and the HFL system operation OK?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Audio remote switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio remote-HFL switch 12P connector -3. Do the Audio Remote-HFL Switch Test . Is the audio remote-HFL switch OK? YES Go to step 3. NO Replace the audio remote-HFL switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio remote-HFL switch 12P connector

-3. Do the Audio Remote-HFL Switch Test .

Is the audio remote-HFL switch OK?

YES

Go to step 3.

NO

Replace the audio remote-HFL switch .

- Shorted wire check (AUDIO REMOTE SW line, HFT/NAVI REMOTE SW line) -1. Disconnect the following connector. Audio unit connector A (24P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio remote-HFL switch 12P connector: disconnected Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 9 Test point 2 Body ground Test point 1 Audio unit connector A (24P) No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the wire(s) between the audio unit and the audio remote-HFL switch. If the wires are OK, replace the cable reel . NO The AUDIO REMOTE SW and the HFT/NAVI REMOTE SW wires are not shorted to ground. Go to step 4.

-1. Disconnect the following connector.

Audio unit connector A (24P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio remote-HFL switch 12P connector: disconnected

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 9

Test point 2 | Body ground

Test point 1 | Audio unit connector A (24P) No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the wire(s) between the audio unit and the audio remote-HFL switch. If the wires are OK, replace the cable reel .

NO

The AUDIO REMOTE SW and the HFT/NAVI REMOTE SW wires are not shorted to ground. Go to step 4.

- Determine possible failure area (HFT/NAVI REMOTE SW line, others) -1. Reconnect the audio remote-HFL switch 12P connector. -2. Measure the resistance between test points 1 and 2 as specified in the table. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 9 Test point 2 Audio unit connector A (24P) No. 19 Button held down VOL DOWN (-) VOL UP(+) LEFT RIGHT SOURCE No button pressed Resistance About 99 Ω About 357 Ω About 775 Ω About 1.7 kΩ About 3.7 kΩ About 10 kΩ Is the resistance OK? YES Go to step 5. NO Go to step 6.

-1. Reconnect the audio remote-HFL switch 12P connector.

-2. Measure the resistance between test points 1 and 2 as specified in the table.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 9

Test point 2 | Audio unit connector A (24P) No. 19

Button held down | VOL DOWN (-) | VOL UP(+) | LEFT | RIGHT | SOURCE | No button pressed

Resistance | About 99 Ω | About 357 Ω | About 775 Ω | About 1.7 kΩ | About 3.7 kΩ | About 10 kΩ

Is the resistance OK?

YES

Go to step 5.

NO

Go to step 6.

- Open wire check (HFT/NAVI REMOTE SW line) -1. Measure the resistance between test points 1 and 2 as specified in the table. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 19 Test point 2 Audio unit connector A (24P) No.
````

## Chunk 2619: Audio remote-HFL switch does not work properly (audio unit buttons work) (Without Multi-Information Display)

- Title: Audio remote-HFL switch does not work properly (audio unit buttons work) (Without Multi-Information Display)
- Source path: `pages\1567.html`
- Chunk ID: `chunk_154959cb8835`
- Images: none
- Duplicate sources: `pages\2017.html`, `pages\25879.html`, `pages\13450.html`

### Full Text

````text
ance between test points 1 and 2 as specified in the table.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 9

Test point 2 | Audio unit connector A (24P) No. 19

Button held down | VOL DOWN (-) | VOL UP(+) | LEFT | RIGHT | SOURCE | No button pressed

Resistance | About 99 Ω | About 357 Ω | About 775 Ω | About 1.7 kΩ | About 3.7 kΩ | About 10 kΩ

Is the resistance OK?

YES

Go to step 5.

NO

Go to step 6.

- Open wire check (HFT/NAVI REMOTE SW line) -1. Measure the resistance between test points 1 and 2 as specified in the table. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 19 Test point 2 Audio unit connector A (24P) No. 20 Button held down HANG-UP/BACK PICK-UP TALK No button pressed Resistance About 47 Ω About 222 Ω About 2.25 kΩ About 10 kΩ Is the resistance OK? YES Replace the audio unit . NO Repair an open or high resistance in the wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel .

-1. Measure the resistance between test points 1 and 2 as specified in the table.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 19

Test point 2 | Audio unit connector A (24P) No. 20

Button held down | HANG-UP/BACK | PICK-UP | TALK | No button pressed

Resistance | About 47 Ω | About 222 Ω | About 2.25 kΩ | About 10 kΩ

Is the resistance OK?

YES

Replace the audio unit .

NO

Repair an open or high resistance in the wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel .

- Determine possible failure area (AUDIO REMOTE SW line, REMOTE SW GND line) -1. Measure the resistance between test points 1 and 2 as specified in the table. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 19 Test point 2 Audio unit connector A (24P) No. 20 Button held down HANG-UP/BACK PICK-UP TALK No button pressed Resistance About 47 Ω About 222 Ω About 2.25 kΩ About 10 kΩ Is the resistance OK? YES Repair an open or high resistance in the AUDIO REMOTE SW wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel . NO Repair an open or high resistance in the REMOTE SW GND wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel .

-1. Measure the resistance between test points 1 and 2 as specified in the table.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 19

Test point 2 | Audio unit connector A (24P) No. 20

Button held down | HANG-UP/BACK | PICK-UP | TALK | No button pressed

Resistance | About 47 Ω | About 222 Ω | About 2.25 kΩ | About 10 kΩ

Is the resistance OK?

YES

Repair an open or high resistance in the AUDIO REMOTE SW wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel .

NO

Repair an open or high resistance in the REMOTE SW GND wire between the audio unit and the audio remote-HFL switch. If the wire is OK, replace the cable reel .
````

## Chunk 2620: Audio system sound is weak or distorted (display is normal) (2/4-door: Without Stereo Amplifier, Without Navigation)

- Title: Audio system sound is weak or distorted (display is normal) (2/4-door: Without Stereo Amplifier, Without Navigation)
- Source path: `pages\1568.html`
- Chunk ID: `chunk_53053b45afaa`
- Images: `images\GHH399334.jpeg`
- Duplicate sources: `pages\2018.html`, `pages\25880.html`, `pages\13451.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (2/4-door: Without Stereo Amplifier, Without Navigation)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Open wire check (speaker lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector A (24P) Left front tweeter 2P connector (display audio type) Right front tweeter 2P connector (display audio type) Left rear tweeter 2P connector (display audio type) Right rear tweeter 2P connector (display audio type) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear tweeter 2P connector: disconnected Right rear tweeter 2P connector: disconnected Test point 1: Audio unit connector A (24P) Test point 2: Audio unit connector A (24P) Resistance No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 15 No. 16 About 4 Ω No. 17 No. 18 About 4 Ω Is the resistance OK? YES: Display audio type Go to step 4. YES: Color audio type Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector A (24P)

Left front tweeter 2P connector (display audio type)

Right front tweeter 2P connector (display audio type)

Left rear tweeter 2P connector (display audio type)

Right rear tweeter 2P connector (display audio type)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Test point 1: Audio unit connector A (24P) | Test point 2: Audio unit connector A (24P) | Resistance

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 15 | No. 16 | About 4 Ω

No. 17 | No. 18 | About 4 Ω

Is the resistance OK?

YES: Display audio type

Go to step 4.

YES: Color audio type

Go to step 6.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair an open in the wire between the audio unit and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair an open in the wire between the audio unit and the speaker.

NO

Replace the speaker .

- Open wire check (speaker lines) 2 -1. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear tweeter 2P connector: disconnected Right rear tweeter 2P connector: disconnected Speaker Test point 1:Tweeter 2P connector Test point 2:Tweeter 2P connector Resistance Left front tweeter No. 1 No. 2 About 4 Ω Right front tweeter No. 1 No. 2 About 4 Ω Left rear tweeter No. 1 No. 2 About 4 Ω Right rear tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector | Test point 2:Tweeter 2P connector | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear tweeter | No.
````

## Chunk 2621: Audio system sound is weak or distorted (display is normal) (2/4-door: Without Stereo Amplifier, Without Navigation)

- Title: Audio system sound is weak or distorted (display is normal) (2/4-door: Without Stereo Amplifier, Without Navigation)
- Source path: `pages\1568.html`
- Chunk ID: `chunk_8f825d34bb07`
- Images: `images\GHH399334.jpeg`
- Duplicate sources: `pages\2018.html`, `pages\25880.html`, `pages\13451.html`

### Full Text

````text
ont tweeter No. 1 No. 2 About 4 Ω Left rear tweeter No. 1 No. 2 About 4 Ω Right rear tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector | Test point 2:Tweeter 2P connector | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear tweeter | No. 1 | No. 2 | About 4 Ω

Right rear tweeter | No. 1 | No. 2 | About 4 Ω

Courtesy of HONDA, U.S.A., INC.

Is the resistance OK?

YES

Go to step 5.

NO

Repair an open in the wire between the speaker and the tweeter.

- Tweeter check -1. Test the tweeter . Is the tweeter OK? YES Go to step 6. NO Replace the tweeter .

-1. Test the tweeter .

Is the tweeter OK?

YES

Go to step 6.

NO

Replace the tweeter .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the audio unit .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the audio unit .
````

## Chunk 2622: Audio system sound is weak or distorted (display is normal) (5-door with Stereo Amplifier) (2017 2018 2019 2020 2021)

- Title: Audio system sound is weak or distorted (display is normal) (5-door with Stereo Amplifier) (2017 2018 2019 2020 2021)
- Source path: `pages\1569.html`
- Chunk ID: `chunk_b5bd78884ff1`
- Images: none
- Duplicate sources: `pages\2019.html`, `pages\25881.html`, `pages\13452.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (5-door with Stereo Amplifier) (2017 2018 2019 2020 2021)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Open wire check (speaker lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Stereo amplifier connector A (18P) Stereo amplifier connector B (8P) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector A (18P): disconnected Stereo amplifier connector B (8P): disconnected Test point 1: Stereo amplifier connector A (18P) Test point 2: Stereo amplifier connector A (18P) Resistance No. 2 No. 4 About 2 Ω No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 9 No. 10 About 4 Ω No. 11 No. 18 About 4 Ω No. 12 No. 13 About 4 Ω No. 14 No. 15 About 3.2 Ω No. 16 No. 17 About 3.2 Ω Test point 1: Stereo amplifier connector B (8P) Test point 2: Stereo amplifier connector B (8P) Resistance No. 1 No. 2 About 4 Ω No. 3 No. 4 About 4 Ω No. 5 No. 6 About 3.2 Ω No. 7 No. 8 About 3.2 Ω Is the resistance OK? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Stereo amplifier connector A (18P)

Stereo amplifier connector B (8P)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector A (18P): disconnected

Stereo amplifier connector B (8P): disconnected

Test point 1: Stereo amplifier connector A (18P) | Test point 2: Stereo amplifier connector A (18P) | Resistance

Stereo amplifier connector A (18P)

Stereo amplifier connector A (18P)

No. 2 | No. 4 | About 2 Ω

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 9 | No. 10 | About 4 Ω

No. 11 | No. 18 | About 4 Ω

No. 12 | No. 13 | About 4 Ω

No. 14 | No. 15 | About 3.2 Ω

No. 16 | No. 17 | About 3.2 Ω

Test point 1: Stereo amplifier connector B (8P) | Test point 2: Stereo amplifier connector B (8P) | Resistance

Stereo amplifier connector B (8P)

Stereo amplifier connector B (8P)

No. 1 | No. 2 | About 4 Ω

No. 3 | No. 4 | About 4 Ω

No. 5 | No. 6 | About 3.2 Ω

No. 7 | No. 8 | About 3.2 Ω

Is the resistance OK?

YES

Go to step 4.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair a faulty speaker wire(s) between the stereo amplifier and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair a faulty speaker wire(s) between the stereo amplifier and the speaker.

NO

Replace the speaker .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the stereo amplifier .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the stereo amplifier .
````

## Chunk 2623: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, With Navigation) (2017 2018 2019 2020 2021)

- Title: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, With Navigation) (2017 2018 2019 2020 2021)
- Source path: `pages\1570.html`
- Chunk ID: `chunk_a0007c347810`
- Images: `images\GHH399335.png`, `images\GHH399336.png`, `images\GHH399337.jpeg`
- Duplicate sources: `pages\2020.html`, `pages\25882.html`, `pages\13453.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, With Navigation) (2017 2018 2019 2020 2021)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Open wire check (speaker lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio-navigation unit connector A (24P) Left front tweeter 2P connector Right front tweeter 2P connector Left rear door tweeter 2P connector Right rear door tweeter 2P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear door tweeter 2P connector: disconnected Right rear door tweeter 2P connector: disconnected Test point 1: Audio-navigation unit connector A (24P) Test point 2: Audio-navigation unit connector A (24P) Resistance No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 15 No. 16 About 4 Ω No. 17 No. 18 About 4 Ω Is the resistance OK? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio-navigation unit connector A (24P)

Left front tweeter 2P connector

Right front tweeter 2P connector

Left rear door tweeter 2P connector

Right rear door tweeter 2P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected

Right rear door tweeter 2P connector: disconnected

Test point 1: Audio-navigation unit connector A (24P) | Test point 2: Audio-navigation unit connector A (24P) | Resistance

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 15 | No. 16 | About 4 Ω

No. 17 | No. 18 | About 4 Ω

Is the resistance OK?

YES

Go to step 4.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair an open in the wire between the audio-navigation unit and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair an open in the wire between the audio-navigation unit and the speaker.

NO

Replace the speaker .

- Open wire check (speaker lines) 2 -1. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear door tweeter 2P connector: disconnected Right rear door tweeter 2P connector: disconnected Speaker Test point 1:Tweeter 2P connector(female terminals): Test point 2:Tweeter 2P connector(female terminals): Resistance Left front tweeter No. 1 No. 2 About 4 Ω Right front tweeter No. 1 No. 2 About 4 Ω Left rear door tweeter No. 1 No. 2 About 4 Ω Right rear door tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected

Right rear door tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector(female terminals): | Test point 2:Tweeter 2P connector(female terminals): | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω
````

## Chunk 2624: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, With Navigation) (2017 2018 2019 2020 2021)

- Title: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, With Navigation) (2017 2018 2019 2020 2021)
- Source path: `pages\1570.html`
- Chunk ID: `chunk_60504f93de35`
- Images: `images\GHH399335.png`, `images\GHH399336.png`, `images\GHH399337.jpeg`
- Duplicate sources: `pages\2020.html`, `pages\25882.html`, `pages\13453.html`

### Full Text

````text
oor tweeter No. 1 No. 2 About 4 Ω Right rear door tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected

Right rear door tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector(female terminals): | Test point 2:Tweeter 2P connector(female terminals): | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear door tweeter | No. 1 | No. 2 | About 4 Ω

Right rear door tweeter | No. 1 | No. 2 | About 4 Ω

Courtesy of HONDA, U.S.A., INC.

Is the resistance OK?

YES

Go to step 5.

NO

Repair an open in the wire between the speaker and the tweeter.

- Tweeter check -1. Test the tweeter . Is the tweeter OK? YES Go to step 6. NO Replace the tweeter .

-1. Test the tweeter .

Is the tweeter OK?

YES

Go to step 6.

NO

Replace the tweeter .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the audio-navigation unit .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the audio-navigation unit .
````

## Chunk 2625: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, Without Navigation) (2017 2018 2019 2020 2021)

- Title: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, Without Navigation) (2017 2018 2019 2020 2021)
- Source path: `pages\1571.html`
- Chunk ID: `chunk_38bc077e1851`
- Images: `images\GHH399338.png`, `images\GHH399339.png`, `images\GHH399340.jpeg`
- Duplicate sources: `pages\2021.html`, `pages\25883.html`, `pages\13454.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, Without Navigation) (2017 2018 2019 2020 2021)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Open wire check (speaker lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector A (24P) Left front tweeter 2P connector (display audio type) Right front tweeter 2P connector (display audio type) Left rear door tweeter 2P connector (display audio type) Right rear door tweeter 2P connector (display audio type) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear door tweeter 2P connector: disconnected Right rear door tweeter 2P connector: disconnected Test point 1: Audio unit connector A (24P) Test point 2: Audio unit connector A (24P) Resistance No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 15 No. 16 About 4 Ω No. 17 No. 18 About 4 Ω Is the resistance OK? YES: Display audio type Go to step 4. YES: Color audio type Go to step 6. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector A (24P)

Left front tweeter 2P connector (display audio type)

Right front tweeter 2P connector (display audio type)

Left rear door tweeter 2P connector (display audio type)

Right rear door tweeter 2P connector (display audio type)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected

Right rear door tweeter 2P connector: disconnected

Test point 1: Audio unit connector A (24P) | Test point 2: Audio unit connector A (24P) | Resistance

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 15 | No. 16 | About 4 Ω

No. 17 | No. 18 | About 4 Ω

Is the resistance OK?

YES: Display audio type

Go to step 4.

YES: Color audio type

Go to step 6.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair an open in the wire between the audio unit and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair an open in the wire between the audio unit and the speaker.

NO

Replace the speaker .

- Open wire check (speaker lines) 2 -1. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear door tweeter 2P connector: disconnected Right rear door tweeter 2P connector: disconnected Speaker Test point 1:Tweeter 2P connector(female terminals): Test point 2:Tweeter 2P connector(female terminals): Resistance Left front tweeter No. 1 No. 2 About 4 Ω Right front tweeter No. 1 No. 2 About 4 Ω Left rear door tweeter No. 1 No. 2 About 4 Ω Speaker Test point 1:Tweeter 2P connector(female terminals): Test point 2:Tweeter 2P connector(female terminals): Resistance Right rear door tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected
````

## Chunk 2626: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, Without Navigation) (2017 2018 2019 2020 2021)

- Title: Audio system sound is weak or distorted (display is normal) (5-door: Without Stereo Amplifier, Without Navigation) (2017 2018 2019 2020 2021)
- Source path: `pages\1571.html`
- Chunk ID: `chunk_3b14b5250098`
- Images: `images\GHH399338.png`, `images\GHH399339.png`, `images\GHH399340.jpeg`
- Duplicate sources: `pages\2021.html`, `pages\25883.html`, `pages\13454.html`

### Full Text

````text
minals): Test point 2:Tweeter 2P connector(female terminals): Resistance Left front tweeter No. 1 No. 2 About 4 Ω Right front tweeter No. 1 No. 2 About 4 Ω Left rear door tweeter No. 1 No. 2 About 4 Ω Speaker Test point 1:Tweeter 2P connector(female terminals): Test point 2:Tweeter 2P connector(female terminals): Resistance Right rear door tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear door tweeter 2P connector: disconnected

Right rear door tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector(female terminals): | Test point 2:Tweeter 2P connector(female terminals): | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear door tweeter | No. 1 | No. 2 | About 4 Ω

Speaker | Test point 1:Tweeter 2P connector(female terminals): | Test point 2:Tweeter 2P connector(female terminals): | Resistance

Right rear door tweeter | No. 1 | No. 2 | About 4 Ω

Courtesy of HONDA, U.S.A., INC.

Is the resistance OK?

YES

Go to step 5.

NO

Repair an open in the wire between the speaker and the tweeter.

- Tweeter check -1. Test the tweeter . Is the tweeter OK? YES Go to step 6. NO Replace the tweeter .

-1. Test the tweeter .

Is the tweeter OK?

YES

Go to step 6.

NO

Replace the tweeter .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the audio unit .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the audio unit .
````

## Chunk 2627: Audio system sound is weak or distorted (display is normal) (With Stereo Amplifier)

- Title: Audio system sound is weak or distorted (display is normal) (With Stereo Amplifier)
- Source path: `pages\1572.html`
- Chunk ID: `chunk_1ba5750d6284`
- Images: none
- Duplicate sources: `pages\2022.html`, `pages\25884.html`, `pages\13455.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (With Stereo Amplifier)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (speaker lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Stereo amplifier connector A (18P) Stereo amplifier connector B (8P) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Stereo amplifier connector A (18P): disconnected Stereo amplifier connector B (8P): disconnected Test point 1: Stereo amplifier connector A (18P) Test point 2: Stereo amplifier connector A (18P) Resistance No. 2 No. 4 About 2 Ω No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 9 No. 10 About 4 Ω No. 11 No. 18 About 4 Ω No. 12 No. 13 About 4 Ω No. 14 No. 15 About 3.2 Ω No. 16 No. 17 About 3.2 Ω Test point 1: Stereo amplifier connector B (8P) Test point 2: Stereo amplifier connector B (8P) Resistance No. 5 No. 6 About 3.2 Ω No. 7 No. 8 About 3.2 Ω Is the resistance OK? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Stereo amplifier connector A (18P)

Stereo amplifier connector B (8P)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Stereo amplifier connector A (18P): disconnected

Stereo amplifier connector B (8P): disconnected

Test point 1: Stereo amplifier connector A (18P) | Test point 2: Stereo amplifier connector A (18P) | Resistance

Stereo amplifier connector A (18P)

Stereo amplifier connector A (18P)

No. 2 | No. 4 | About 2 Ω

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 9 | No. 10 | About 4 Ω

No. 11 | No. 18 | About 4 Ω

No. 12 | No. 13 | About 4 Ω

No. 14 | No. 15 | About 3.2 Ω

No. 16 | No. 17 | About 3.2 Ω

Test point 1: Stereo amplifier connector B (8P) | Test point 2: Stereo amplifier connector B (8P) | Resistance

Stereo amplifier connector B (8P)

Stereo amplifier connector B (8P)

No. 5 | No. 6 | About 3.2 Ω

No. 7 | No. 8 | About 3.2 Ω

Is the resistance OK?

YES

Go to step 4.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair a faulty speaker wire(s) between the stereo amplifier and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair a faulty speaker wire(s) between the stereo amplifier and the speaker.

NO

Replace the speaker .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the stereo amplifier .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the stereo amplifier .
````

## Chunk 2628: Audio system sound is weak or distorted (display is normal) (Without Stereo Amplifier, with Navigation)

- Title: Audio system sound is weak or distorted (display is normal) (Without Stereo Amplifier, with Navigation)
- Source path: `pages\1573.html`
- Chunk ID: `chunk_00af2d8e3cb8`
- Images: `images\GHH399341.jpeg`
- Duplicate sources: `pages\2023.html`, `pages\25885.html`, `pages\13456.html`

### Full Text

````text
# Audio system sound is weak or distorted (display is normal) (Without Stereo Amplifier, with Navigation)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Go into the System Diagnostic Mode, and use the speaker check mode . Is there tone from the speakers, and is the tone quality normal in each channel? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Go into the System Diagnostic Mode, and use the speaker check mode .

Is there tone from the speakers, and is the tone quality normal in each channel?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Open wire check (speaker lines) 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio-navigation unit connector A (24P) Left front tweeter 2P connector Right front tweeter 2P connector Left rear tweeter 2P connector Right rear tweeter 2P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear tweeter 2P connector: disconnected Right rear tweeter 2P connector: disconnected Test point 1: Audio-navigation unit connector A (24P) Test point 2: Audio-navigation unit connector A (24P) Resistance No. 5 No. 6 About 4 Ω No. 7 No. 8 About 4 Ω No. 15 No. 16 About 4 Ω No. 17 No. 18 About 4 Ω Is the resistance OK? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio-navigation unit connector A (24P)

Left front tweeter 2P connector

Right front tweeter 2P connector

Left rear tweeter 2P connector

Right rear tweeter 2P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Test point 1: Audio-navigation unit connector A (24P) | Test point 2: Audio-navigation unit connector A (24P) | Resistance

No. 5 | No. 6 | About 4 Ω

No. 7 | No. 8 | About 4 Ω

No. 15 | No. 16 | About 4 Ω

No. 17 | No. 18 | About 4 Ω

Is the resistance OK?

YES

Go to step 4.

NO

Go to step 3.

- Speaker check -1. Test the speaker on the faulty speaker lines . Is the speaker OK? YES Repair an open in the wire between the audio-navigation unit and the speaker. NO Replace the speaker .

-1. Test the speaker on the faulty speaker lines .

Is the speaker OK?

YES

Repair an open in the wire between the audio-navigation unit and the speaker.

NO

Replace the speaker .

- Open wire check (speaker lines) 2 -1. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Left front tweeter 2P connector: disconnected Right front tweeter 2P connector: disconnected Left rear tweeter 2P connector: disconnected Right rear tweeter 2P connector: disconnected Speaker Test point 1:Tweeter 2P connector Test point 2:Tweeter 2P connector Resistance Left front tweeter No. 1 No. 2 About 4 Ω Right front tweeter No. 1 No. 2 About 4 Ω Left rear tweeter No. 1 No. 2 About 4 Ω Right rear tweeter No. 1 No. 2 About 4 Ω Courtesy of HONDA, U.S.A., INC. Is the resistance OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector | Test point 2:Tweeter 2P connector | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear tweeter | No. 1 | No. 2 | About 4 Ω

Right rear tweeter | No. 1 | No. 2 | About 4 Ω

Courtesy of HONDA, U.S.A., INC.

Is the resistance OK?

YES

Go to step 5.

NO
````

## Chunk 2629: Audio system sound is weak or distorted (display is normal) (Without Stereo Amplifier, with Navigation)

- Title: Audio system sound is weak or distorted (display is normal) (Without Stereo Amplifier, with Navigation)
- Source path: `pages\1573.html`
- Chunk ID: `chunk_515b7dec8c8d`
- Images: `images\GHH399341.jpeg`
- Duplicate sources: `pages\2023.html`, `pages\25885.html`, `pages\13456.html`

### Full Text

````text
ce OK? YES Go to step 5. NO Repair an open in the wire between the speaker and the tweeter.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Left front tweeter 2P connector: disconnected

Right front tweeter 2P connector: disconnected

Left rear tweeter 2P connector: disconnected

Right rear tweeter 2P connector: disconnected

Speaker | Test point 1:Tweeter 2P connector | Test point 2:Tweeter 2P connector | Resistance

Left front tweeter | No. 1 | No. 2 | About 4 Ω

Right front tweeter | No. 1 | No. 2 | About 4 Ω

Left rear tweeter | No. 1 | No. 2 | About 4 Ω

Right rear tweeter | No. 1 | No. 2 | About 4 Ω

Courtesy of HONDA, U.S.A., INC.

Is the resistance OK?

YES

Go to step 5.

NO

Repair an open in the wire between the speaker and the tweeter.

- Tweeter check -1. Test the tweeter . Is the tweeter OK? YES Go to step 6. NO Replace the tweeter .

-1. Test the tweeter .

Is the tweeter OK?

YES

Go to step 6.

NO

Replace the tweeter .

- Speaker visual check -1. Remove the speaker that is duplicating the failure, and check the speaker for any damage. Is there any damage? YES Replace the speaker . NO Replace the audio-navigation unit .

-1. Remove the speaker that is duplicating the failure, and check the speaker for any damage.

Is there any damage?

YES

Replace the speaker .

NO

Replace the audio-navigation unit .
````

## Chunk 2630: Audio unit button illumination does not work

- Title: Audio unit button illumination does not work
- Source path: `pages\1574.html`
- Chunk ID: `chunk_f61120e6e05b`
- Images: `images\GHH29784.png`
- Duplicate sources: `pages\2024.html`, `pages\25886.html`, `pages\13457.html`

### Full Text

````text
# Audio unit button illumination does not work

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check for B-CAN DTCs and resolve them before troubleshooting.

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Turn the combination light switch to the parking light ( ) position. -3. Check the illumination of the audio unit buttons. Are the buttons illuminated? YES Intermittent failure, the audio unit is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Turn the combination light switch to the parking light ( ) position.

-3. Check the illumination of the audio unit buttons.

Are the buttons illuminated?

YES

Intermittent failure, the audio unit is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (interior lights circuit, others) -1. Check the illumination of several other buttons not related to the audio system. Are the buttons illuminated? YES Go to step 3. NO Troubleshoot the interior lights.

-1. Check the illumination of several other buttons not related to the audio system.

Are the buttons illuminated?

YES

Go to step 3.

NO

Troubleshoot the interior lights.

- Determine possible failure area (audio unit, others) -1. Go into the System Diagnostic Mode, and use the ILLUMI in the Vehicle Information to check the ILLUMI signal . Does the METER_ILL STATUS signal change from [0] to [1] when the combination light switch is turned to the parking light position? YES Replace the audio unit . NO Go to step 4.

-1. Go into the System Diagnostic Mode, and use the ILLUMI in the Vehicle Information to check the ILLUMI signal .

Does the METER_ILL STATUS signal change from [0] to [1] when the combination light switch is turned to the parking light position?

YES

Replace the audio unit .

NO

Go to step 4.

- Open wire check (B-CAN_H line, B-CAN_L line) -1. Turn the combination light switch off. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Disconnect the following connectors. Gauge control module connector A (32P) Audio unit connector A (24P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Gauge control module connector A (32P): disconnected Audio unit connector A (24P): disconnected Test point 1 Gauge control module connector A (32P) No. 30 Test point 2 Audio unit connector A (24P) No. 14 Test point 1 Gauge control module connector A (32P) No. 31 Test point 2 Audio unit connector A (24P) No. 24 Is there continuity? YES Replace the audio unit . NO Repair an open in the wire(s) between the audio unit and the gauge control module.

-1. Turn the combination light switch off.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Disconnect the following connectors.

Gauge control module connector A (32P)

Audio unit connector A (24P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Gauge control module connector A (32P): disconnected

Audio unit connector A (24P): disconnected

Test point 1 | Gauge control module connector A (32P) No. 30

Test point 2 | Audio unit connector A (24P) No. 14

Test point 1 | Gauge control module connector A (32P) No. 31

Test point 2 | Audio unit connector A (24P) No. 24

Is there continuity?

YES

Replace the audio unit .

NO

Repair an open in the wire(s) between the audio unit and the gauge control module.
````

## Chunk 2631: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2016 2017 2018)
- Source path: `pages\1575.html`
- Chunk ID: `chunk_6145fe85527d`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2025.html`, `pages\25887.html`, `pages\13458.html`

### Full Text

````text
# Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2016 2017 2018)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check if the Day/Night ( ) button has been pressed, and turned off the display (see the Owner's Manual for more information).

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check if the audio unit display indicates any information. Is any information displayed? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check if the audio unit display indicates any information.

Is any information displayed?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A19 (15 A) Location Under-hood fuse/relay box Fuse No. B1 (10 A) Location Under-dash fuse/relay box Are the fuses OK? YES Go to step 3. NO Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 (15 A) fuse and/or the No. B1 (10 A) fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A19 (15 A)

Location | Under-hood fuse/relay box

Fuse | No. B1 (10 A)

Location | Under-dash fuse/relay box

Are the fuses OK?

YES

Go to step 3.

NO

Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 (15 A) fuse and/or the No. B1 (10 A) fuse circuits.

- Open wire check (+B AUDIO line) -1. Disconnect the following connector. Audio unit connector A (24P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 3 Test point 2 Body ground Is there battery voltage? YES The +B AUDIO wire is OK. Go to step 4. NO Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the audio unit.

-1. Disconnect the following connector.

Audio unit connector A (24P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

The +B AUDIO wire is OK. Go to step 4.

NO

Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the audio unit.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The ACC wire is OK. Go to step 5. NO Repair an open in the wire between the No. B1 (10 A) fuse in the under-dash fuse/relay box and the audio unit.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The ACC wire is OK. Go to step 5.

NO

Repair an open in the wire between the No. B1 (10 A) fuse in the under-dash fuse/relay box and the audio unit.

- Open wire check (GND line) 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector A (24P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES The GND wire is OK. Go to step 6. NO Repair an open or high resistance in the wire between the audio unit and body ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector A (24P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector A (24P) No. 1

Test point 2 | Body ground

Is there less than 0.2 V?

YES

The GND wire is OK. Go to step 6.

NO

Repair an open or high resistance in the wire between the audio unit and body ground (G504).

- Audio panel check (substitution) -1.
````

## Chunk 2632: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2016 2017 2018)
- Source path: `pages\1575.html`
- Chunk ID: `chunk_3801819fedf7`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2025.html`, `pages\25887.html`, `pages\13458.html`

### Full Text

````text
oltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES The GND wire is OK. Go to step 6. NO Repair an open or high resistance in the wire between the audio unit and body ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector A (24P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector A (24P) No. 1

Test point 2 | Body ground

Is there less than 0.2 V?

YES

The GND wire is OK. Go to step 6.

NO

Repair an open or high resistance in the wire between the audio unit and body ground (G504).

- Audio panel check (substitution) -1. Substitute a known-good audio panel. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original audio panel. NO Replace the audio unit .

-1. Substitute a known-good audio panel.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original audio panel.

NO

Replace the audio unit .
````

## Chunk 2633: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1576.html`
- Chunk ID: `chunk_b79696d5fadb`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2026.html`, `pages\25888.html`, `pages\13459.html`

### Full Text

````text
# Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check if the Day/Night ( ) button has been pressed, and turned off the display (see the Owner's Manual for more information).

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check if the audio unit display indicates any information. Is any information displayed? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check if the audio unit display indicates any information.

Is any information displayed?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A19 Fuse No. B1 Are the fuses OK? YES Go to step 3. NO Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 fuse and/or the No. B1 fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A19

Fuse | No. B1

Are the fuses OK?

YES

Go to step 3.

NO

Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 fuse and/or the No. B1 fuse circuits.

- Open wire check (+B AUDIO line) -1. Disconnect the following connector. Audio unit connector A (24P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 3 Test point 2 Body ground Is there battery voltage? YES: With RR CAMERA ACC DIODE circuit The +B AUDIO wire is OK. Go to step 4. YES: Without RR CAMERA ACC DIODE circuit The +B AUDIO wire is OK. Go to step 5. NO Repair an open in the wire.

-1. Disconnect the following connector.

Audio unit connector A (24P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES: With RR CAMERA ACC DIODE circuit

The +B AUDIO wire is OK. Go to step 4.

YES: Without RR CAMERA ACC DIODE circuit

The +B AUDIO wire is OK. Go to step 5.

NO

Repair an open in the wire.

- Open wire check (RR CAMERA ACC DIODE/ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 6. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 6.

NO

Repair an open in the wire.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The ACC wire is OK. Go to step 6. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The ACC wire is OK. Go to step 6.

NO

Repair an open in the wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector A (24P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES The GND wire is OK. Go to step 7. NO Repair an open or high resistance in the wire or poor ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2.
````

## Chunk 2634: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Color Audio Type (5-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1576.html`
- Chunk ID: `chunk_bf2e2fa78906`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2026.html`, `pages\25888.html`, `pages\13459.html`

### Full Text

````text
e the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The ACC wire is OK. Go to step 6.

NO

Repair an open in the wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector A (24P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES The GND wire is OK. Go to step 7. NO Repair an open or high resistance in the wire or poor ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector A (24P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector A (24P) No. 1

Test point 2 | Body ground

Is there less than 0.2 V?

YES

The GND wire is OK. Go to step 7.

NO

Repair an open or high resistance in the wire or poor ground (G504).

- Audio panel check -1. Substitute a known-good audio panel. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original audio panel. NO Replace the audio unit .

-1. Substitute a known-good audio panel.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original audio panel.

NO

Replace the audio unit .
````

## Chunk 2635: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1577.html`
- Chunk ID: `chunk_89d1941838d5`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2027.html`, `pages\25889.html`, `pages\13460.html`

### Full Text

````text
# Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check if the Day/Night ( ) button has been pressed, and turned off the display (see the Owner's Manual for more information).

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check if the center display unit display indicates any information (indicates the Honda logo screen first). Is any information displayed? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check if the center display unit display indicates any information (indicates the Honda logo screen first).

Is any information displayed?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (LVDS1 circuit, others) -1. Shield the center display unit from the sun with your hand, and check that the display is back lit (only the back light is on). Can you see the back light? YES Go to step 12. NO Go to step 3.

-1. Shield the center display unit from the sun with your hand, and check that the display is back lit (only the back light is on).

Can you see the back light?

YES

Go to step 12.

NO

Go to step 3.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A19 (15 A) Location Under-hood fuse/relay box Fuse No. B1 (10 A) Location Under-dash fuse/relay box Are the fuses OK? YES Go to step 4. NO Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 (15 A) fuse and/or the No. B1 (10 A) fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A19 (15 A)

Location | Under-hood fuse/relay box

Fuse | No. B1 (10 A)

Location | Under-dash fuse/relay box

Are the fuses OK?

YES

Go to step 4.

NO

Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 (15 A) fuse and/or the No. B1 (10 A) fuse circuits.

- Open wire check (+B AUDIO line) 1 -1. Disconnect the following connector. Center display unit connector A (5P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Center display unit connector A (5P): disconnected Test point 1 Center display unit connector A (5P) No. 1 Test point 2 Body ground Is there battery voltage? YES The +B AUDIO wire is OK. Go to step 5. NO Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the center display unit.

-1. Disconnect the following connector.

Center display unit connector A (5P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

The +B AUDIO wire is OK. Go to step 5.

NO

Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the center display unit.

- Open wire check (GND line) 1 -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Center display unit connector A (5P): disconnected Test point 1 Center display unit connector A (5P) No. 5 Test point 2 Body ground Is there continuity? YES The GND wire is OK. Go to step 6. NO Repair an open in the wire between the center display unit and body ground (G504).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

The GND wire is OK. Go to step 6.

NO

Repair an open in the wire between the center display unit and body ground (G504).

- Determine possible failure area (DISP CONT line, others) -1. Reconnect center display unit connector A (5P). -2. Disconnect the following connector. Audio unit connector E (16P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES The DISP CONT wire is OK.
````

## Chunk 2636: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1577.html`
- Chunk ID: `chunk_b48d6312cd5a`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2027.html`, `pages\25889.html`, `pages\13460.html`

### Full Text

````text
Test condition | Vehicle OFF (LOCK) mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

The GND wire is OK. Go to step 6.

NO

Repair an open in the wire between the center display unit and body ground (G504).

- Determine possible failure area (DISP CONT line, others) -1. Reconnect center display unit connector A (5P). -2. Disconnect the following connector. Audio unit connector E (16P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES The DISP CONT wire is OK. Go to step 8. NO Go to step 7.

-1. Reconnect center display unit connector A (5P).

-2. Disconnect the following connector.

Audio unit connector E (16P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector E (16P): disconnected

Test point 1 | Audio unit connector E (16P) No. 4

Test point 2 | Body ground

Is there about 3.3 V?

YES

The DISP CONT wire is OK. Go to step 8.

NO

Go to step 7.

- Open wire check (DISP CONT line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Center display unit connector A (5P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES Repair an open in the wire between the audio unit and the center display unit. NO Replace the center display unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector E (16P): disconnected

Test point 1 | Center display unit connector A (5P) No. 4

Test point 2 | Body ground

Is there about 3.3 V?

YES

Repair an open in the wire between the audio unit and the center display unit.

NO

Replace the center display unit .

- Determine possible failure area (center display unit, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector E (16P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there less than 0.2 V? Yes Replace the center display unit . No Go to step 9.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector E (16P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector E (16P) No. 4

Test point 2 | Body ground

Is there less than 0.2 V?

Yes

Replace the center display unit .

No

Go to step 9.

- Open wire check (+B AUDIO line) 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector A (24P) -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 3 Test point 2 Body ground Is there battery voltage? YES The +B AUDIO wire is OK. Go to step 10. NO Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the audio unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio unit connector A (24P)

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

The +B AUDIO wire is OK. Go to step 10.

NO

Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the audio unit.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The ACC wire is OK. Go to step 11. NO Repair an open in the wire between the No. B1 (10 A) fuse in the under-dash fuse/relay box and the audio unit.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode
````

## Chunk 2637: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1577.html`
- Chunk ID: `chunk_a2e3a5689224`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2027.html`, `pages\25889.html`, `pages\13460.html`

### Full Text

````text
P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

The +B AUDIO wire is OK. Go to step 10.

NO

Repair an open in the wire between the No. A19 (15 A) fuse in the under-hood fuse/relay box and the audio unit.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The ACC wire is OK. Go to step 11. NO Repair an open in the wire between the No. B1 (10 A) fuse in the under-dash fuse/relay box and the audio unit.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The ACC wire is OK. Go to step 11.

NO

Repair an open in the wire between the No. B1 (10 A) fuse in the under-dash fuse/relay box and the audio unit.

- Open wire check (GND line) 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector A (24P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES Replace the audio unit . NO Repair an open or high resistance in the wire between the audio unit and body ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector A (24P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector A (24P) No. 1

Test point 2 | Body ground

Is there less than 0.2 V?

YES

Replace the audio unit .

NO

Repair an open or high resistance in the wire between the audio unit and body ground (G504).

- Shorted wire check (LVDS1+ line to LVDS1- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector H (3P) Center display unit connector B (3P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 2 Is there continuity? YES There is a short in the wires between the audio unit and the center display unit. Replace the affected shielded harness. NO The LVDS1+ wire and the LVDS1 - wire are not shorted. Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector H (3P)

Center display unit connector B (3P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 2

Is there continuity?

YES

There is a short in the wires between the audio unit and the center display unit. Replace the affected shielded harness.

NO

The LVDS1+ wire and the LVDS1 - wire are not shorted. Go to step 13.

- Shorted wire check (LVDS1 SH line to another lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 3 Test point 1 Center display unit connector B (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 3 Is there continuity? YES There is a short in the wires between the audio unit and the center display unit. Replace the affected shielded harness. NO The LVDS1 SH wire is not shorted. Go to step 14.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 3

Test point 1 | Center display unit connector B (3P) No. 2
````

## Chunk 2638: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2016 2017 2018)
- Source path: `pages\1577.html`
- Chunk ID: `chunk_c9266843df50`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2027.html`, `pages\25889.html`, `pages\13460.html`

### Full Text

````text
onnected Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 3 Test point 1 Center display unit connector B (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 3 Is there continuity? YES There is a short in the wires between the audio unit and the center display unit. Replace the affected shielded harness. NO The LVDS1 SH wire is not shorted. Go to step 14.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 3

Test point 1 | Center display unit connector B (3P) No. 2

Test point 2 | Center display unit connector B (3P) No. 3

Is there continuity?

YES

There is a short in the wires between the audio unit and the center display unit. Replace the affected shielded harness.

NO

The LVDS1 SH wire is not shorted. Go to step 14.

- Open wire check (LVDS1+ line, LVDS1- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Audio unit connector H (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 1 Test point 1 Audio unit connector H (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 2 Is there continuity? YES The LVDS1+ and the LVDS1 - wires are OK. Go to step 15. NO There is an open in the wire(s) between the audio unit and the center display unit. Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Audio unit connector H (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 1

Test point 1 | Audio unit connector H (3P) No. 2

Test point 2 | Center display unit connector B (3P) No. 2

Is there continuity?

YES

The LVDS1+ and the LVDS1 - wires are OK. Go to step 15.

NO

There is an open in the wire(s) between the audio unit and the center display unit. Replace the affected shielded harness.

- Center display unit check (substitution) -1. Substitute a known-good center display unit. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original center display unit. NO Replace the audio unit .

-1. Substitute a known-good center display unit.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original center display unit.

NO

Replace the audio unit .
````

## Chunk 2639: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1578.html`
- Chunk ID: `chunk_369798d6688a`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2028.html`, `pages\25890.html`, `pages\13461.html`

### Full Text

````text
# Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

NOTE:

- Check the vehicle 12 volt battery condition first .

- Check if the Day/Night ( ) button has been pressed, and turned off the display (see the Owner's Manual for more information).

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check if the center display unit display indicates any information (indicates the Honda logo screen first). Is any information displayed? YES Intermittent failure, the system is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check if the center display unit display indicates any information (indicates the Honda logo screen first).

Is any information displayed?

YES

Intermittent failure, the system is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (LVDS1 circuit, others) -1. Shield the center display unit from the sun with your hand, and check that the display is back lit (only the back light is on). Can you see the back light? YES Go to step 13. NO Go to step 3.

-1. Shield the center display unit from the sun with your hand, and check that the display is back lit (only the back light is on).

Can you see the back light?

YES

Go to step 13.

NO

Go to step 3.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuses. Fuse No. A19 Fuse No. B1 Are the fuses OK? YES Go to step 4. NO Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 fuse and/or the No. B1 fuse circuits.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuses.

Fuse | No. A19

Fuse | No. B1

Are the fuses OK?

YES

Go to step 4.

NO

Replace the fuse(s), and recheck. If the fuse(s) blows again, check for a short in the No. A19 fuse and/or the No. B1 fuse circuits.

- Open wire check (+B AUDIO line) 1 -1. Disconnect the following connector. Center display unit connector A (5P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Center display unit connector A (5P): disconnected Test point 1 Center display unit connector A (5P) No. 1 Test point 2 Body ground Is there battery voltage? YES The +B AUDIO wire is OK. Go to step 5. NO Repair an open in the wire.

-1. Disconnect the following connector.

Center display unit connector A (5P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 1

Test point 2 | Body ground

Is there battery voltage?

YES

The +B AUDIO wire is OK. Go to step 5.

NO

Repair an open in the wire.

- Open wire check (GND line) 1 -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Center display unit connector A (5P): disconnected Test point 1 Center display unit connector A (5P) No. 5 Test point 2 Body ground Is there continuity? YES The GND wire is OK. Go to step 6. NO Repair an open in the wire or poor ground (G504).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

The GND wire is OK. Go to step 6.

NO

Repair an open in the wire or poor ground (G504).

- Determine possible failure area (DISP CONT line, others) -1. Reconnect center display unit connector A (5P). -2. Disconnect the following connector. Audio unit connector E (16P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES The DISP CONT wire is OK. Go to step 8. NO Go to step 7.

-1. Reconnect center display unit connector A (5P).

-2. Disconnect the following connector.

Audio unit connector E (16P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector E (16P): disconnected

Test point 1 | Audio unit connector E (16P) No. 4

Test point 2 | Body ground

Is there about 3.3 V?

YES
````

## Chunk 2640: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1578.html`
- Chunk ID: `chunk_0666e11f0ead`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2028.html`, `pages\25890.html`, `pages\13461.html`

### Full Text

````text
r A (5P). -2. Disconnect the following connector. Audio unit connector E (16P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES The DISP CONT wire is OK. Go to step 8. NO Go to step 7.

-1. Reconnect center display unit connector A (5P).

-2. Disconnect the following connector.

Audio unit connector E (16P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector E (16P): disconnected

Test point 1 | Audio unit connector E (16P) No. 4

Test point 2 | Body ground

Is there about 3.3 V?

YES

The DISP CONT wire is OK. Go to step 8.

NO

Go to step 7.

- Open wire check (DISP CONT line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector E (16P): disconnected Test point 1 Center display unit connector A (5P) No. 4 Test point 2 Body ground Is there about 3.3 V? YES Repair an open in the wire. NO Replace the center display unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector E (16P): disconnected

Test point 1 | Center display unit connector A (5P) No. 4

Test point 2 | Body ground

Is there about 3.3 V?

YES

Repair an open in the wire.

NO

Replace the center display unit .

- Determine possible failure area (center display unit, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector E (16P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector E (16P) No. 4 Test point 2 Body ground Is there less than 0.2 V? Yes Replace the center display unit . No Go to step 9.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector E (16P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector E (16P) No. 4

Test point 2 | Body ground

Is there less than 0.2 V?

Yes

Replace the center display unit .

No

Go to step 9.

- Open wire check (+B AUDIO line) 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Audio unit connector A (24P) -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 3 Test point 2 Body ground Is there battery voltage? YES: With RR CAMERA ACC DIODE circuit The +B AUDIO wire is OK. Go to step 10. YES: Without RR CAMERA ACC DIODE circuit The +B AUDIO wire is OK. Go to step 11. NO Repair an open in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Audio unit connector A (24P)

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES: With RR CAMERA ACC DIODE circuit

The +B AUDIO wire is OK. Go to step 10.

YES: Without RR CAMERA ACC DIODE circuit

The +B AUDIO wire is OK. Go to step 11.

NO

Repair an open in the wire.

- Open wire check (RR CAMERA ACC DIODE/ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 12. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 12.

NO

Repair an open in the wire.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No.
````

## Chunk 2641: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1578.html`
- Chunk ID: `chunk_b5ed886c28ef`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2028.html`, `pages\25890.html`, `pages\13461.html`

### Full Text

````text
Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 12. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The RR CAMERA ACC DIODE/ACC wire is OK. Go to step 12.

NO

Repair an open in the wire.

- Open wire check (ACC line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Audio unit connector A (24P): disconnected Test point 1 Audio unit connector A (24P) No. 23 Test point 2 Body ground Is there battery voltage? YES The ACC wire is OK. Go to step 12. NO Repair an open in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Audio unit connector A (24P): disconnected

Test point 1 | Audio unit connector A (24P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

The ACC wire is OK. Go to step 12.

NO

Repair an open in the wire.

- Open wire check (GND line) 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect audio unit connector A (24P). -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Audio unit connector A (24P) No. 1 Test point 2 Body ground Is there less than 0.2 V? YES Replace the audio unit . NO Repair an open or high resistance in the wire or poor ground (G504).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect audio unit connector A (24P).

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Audio unit connector A (24P) No. 1

Test point 2 | Body ground

Is there less than 0.2 V?

YES

Replace the audio unit .

NO

Repair an open or high resistance in the wire or poor ground (G504).

- Shorted wire check (LVDS1+ line to LVDS1- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector H (3P) Center display unit connector B (3P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 2 Is there continuity? YES There is a short in the wires. Replace the affected shielded harness. NO The LVDS1+ wire and the LVDS1 - wire are not shorted. Go to step 14.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector H (3P)

Center display unit connector B (3P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 2

Is there continuity?

YES

There is a short in the wires. Replace the affected shielded harness.

NO

The LVDS1+ wire and the LVDS1 - wire are not shorted. Go to step 14.

- Shorted wire check (LVDS1 SH line to another lines) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 3 Test point 1 Center display unit connector B (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 3 Is there continuity? YES There is a short in the wires. Replace the affected shielded harness. NO The LVDS1 SH wire is not shorted. Go to step 15.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 3

Test point 1 | Center display unit connector B (3P) No. 2

Test point 2 | Center display unit connector B (3P) No. 3
````

## Chunk 2642: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)

- Title: Audio unit power will not turn on (No information display) (Display Audio Type (7-inch Screen)) (2018 2019 2020 2021)
- Source path: `pages\1578.html`
- Chunk ID: `chunk_27db255e2e38`
- Images: `images\GHH172669.png`
- Duplicate sources: `pages\2028.html`, `pages\25890.html`, `pages\13461.html`

### Full Text

````text
Test point 1 Center display unit connector B (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 3 Test point 1 Center display unit connector B (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 3 Is there continuity? YES There is a short in the wires. Replace the affected shielded harness. NO The LVDS1 SH wire is not shorted. Go to step 15.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Center display unit connector B (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 3

Test point 1 | Center display unit connector B (3P) No. 2

Test point 2 | Center display unit connector B (3P) No. 3

Is there continuity?

YES

There is a short in the wires. Replace the affected shielded harness.

NO

The LVDS1 SH wire is not shorted. Go to step 15.

- Open wire check (LVDS1+ line, LVDS1- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Audio unit connector H (3P): disconnected Center display unit connector B (3P): disconnected Test point 1 Audio unit connector H (3P) No. 1 Test point 2 Center display unit connector B (3P) No. 1 Test point 1 Audio unit connector H (3P) No. 2 Test point 2 Center display unit connector B (3P) No. 2 Is there continuity? YES The LVDS1+ and the LVDS1 - wires are OK. Go to step 16. NO There is an open in the wire(s). Replace the affected shielded harness.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector H (3P): disconnected

Center display unit connector B (3P): disconnected

Test point 1 | Audio unit connector H (3P) No. 1

Test point 2 | Center display unit connector B (3P) No. 1

Test point 1 | Audio unit connector H (3P) No. 2

Test point 2 | Center display unit connector B (3P) No. 2

Is there continuity?

YES

The LVDS1+ and the LVDS1 - wires are OK. Go to step 16.

NO

There is an open in the wire(s). Replace the affected shielded harness.

- Center display unit check -1. Substitute a known-good center display unit. -2. Reconnect all the connectors, and recheck. Does the symptom go away? YES Replace the original center display unit. NO Replace the audio unit .

-1. Substitute a known-good center display unit.

-2. Reconnect all the connectors, and recheck.

Does the symptom go away?

YES

Replace the original center display unit.

NO

Replace the audio unit .
````

## Chunk 2643: Center display unit does not dim

- Title: Center display unit does not dim
- Source path: `pages\1579.html`
- Chunk ID: `chunk_20889313fc21`
- Images: `images\GHH29784.png`
- Duplicate sources: `pages\2029.html`, `pages\25891.html`, `pages\13462.html`

### Full Text

````text
# Center display unit does not dim

NOTE:

- Check the vehicle 12 volt battery condition first .

- Turn the headlight on, and check that the dash brightness setting is not set to high.

- Check the connectors for poor connections or loose terminals.

- Problem verification -1. Turn the vehicle to the ON mode. -2. Turn the combination light switch to the parking light ( ) position. -3. Check the illumination of the center display unit screen and buttons. Does the center display brightness change? YES Intermittent failure, the audio unit is OK at this time. NO The failure is duplicated, go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Turn the combination light switch to the parking light ( ) position.

-3. Check the illumination of the center display unit screen and buttons.

Does the center display brightness change?

YES

Intermittent failure, the audio unit is OK at this time.

NO

The failure is duplicated, go to step 2.

- Determine possible failure area (interior lights circuit, others) -1. Check the illumination of several other buttons not related to the audio/navigation system. Are the buttons illuminated? YES Go to step 3. NO Troubleshoot the interior lights.

-1. Check the illumination of several other buttons not related to the audio/navigation system.

Are the buttons illuminated?

YES

Go to step 3.

NO

Troubleshoot the interior lights.

- Open wire check (ILLUMI+ line) -1. Turn the combination light switch off. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Disconnect the following connector. Center display unit connector A (5P) -4. Turn the combination lighting switch to the parking light ( ) position. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Center display unit connector A (5P): disconnected Test point 1 Center display unit connector A (5P) No. 3 Test point 2 Body ground Is there battery voltage? YES Replace the center display unit . NO Repair an open in the wire between the center display unit and the taillight relay.

-1. Turn the combination light switch off.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Disconnect the following connector.

Center display unit connector A (5P)

-4. Turn the combination lighting switch to the parking light ( ) position.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Center display unit connector A (5P): disconnected

Test point 1 | Center display unit connector A (5P) No. 3

Test point 2 | Body ground

Is there battery voltage?

YES

Replace the center display unit .

NO

Repair an open in the wire between the center display unit and the taillight relay.
````

## Sources Used

- `pages\1146.html`
- `pages\1147.html`
- `pages\1148.html`
- `pages\1149.html`
- `pages\1150.html`
- `pages\1151.html`
- `pages\1152.html`
- `pages\1153.html`
- `pages\1154.html`
- `pages\1155.html`
- `pages\1156.html`
- `pages\1158.html`
- `pages\1159.html`
- `pages\1160.html`
- `pages\1161.html`
- `pages\1162.html`
- `pages\1164.html`
- `pages\1165.html`
- `pages\1166.html`
- `pages\1167.html`
- `pages\1168.html`
- `pages\1169.html`
- `pages\1170.html`
- `pages\1171.html`
- `pages\1172.html`
- `pages\1173.html`
- `pages\1174.html`
- `pages\1175.html`
- `pages\1176.html`
- `pages\1177.html`
- `pages\1178.html`
- `pages\1179.html`
- `pages\1180.html`
- `pages\1181.html`
- `pages\1182.html`
- `pages\1183.html`
- `pages\1184.html`
- `pages\1185.html`
- `pages\1186.html`
- `pages\1188.html`
- `pages\1191.html`
- `pages\1192.html`
- `pages\1193.html`
- `pages\1194.html`
- `pages\1195.html`
- `pages\1196.html`
- `pages\1197.html`
- `pages\1198.html`
- `pages\1199.html`
- `pages\1200.html`
- `pages\1201.html`
- `pages\1202.html`
- `pages\1203.html`
- `pages\1204.html`
- `pages\1205.html`
- `pages\1206.html`
- `pages\1207.html`
- `pages\1208.html`
- `pages\1209.html`
- `pages\1210.html`
- `pages\1211.html`
- `pages\1212.html`
- `pages\1213.html`
- `pages\1214.html`
- `pages\1215.html`
- `pages\1216.html`
- `pages\1217.html`
- `pages\1218.html`
- `pages\1219.html`
- `pages\1220.html`
- `pages\1221.html`
- `pages\1222.html`
- `pages\1223.html`
- `pages\1224.html`
- `pages\1225.html`
- `pages\1226.html`
- `pages\1227.html`
- `pages\1228.html`
- `pages\1229.html`
- `pages\1230.html`
- `pages\1231.html`
- `pages\1232.html`
- `pages\1233.html`
- `pages\1234.html`
- `pages\1235.html`
- `pages\1236.html`
- `pages\1237.html`
- `pages\1238.html`
- `pages\1239.html`
- `pages\1240.html`
- `pages\1241.html`
- `pages\1242.html`
- `pages\1243.html`
- `pages\1244.html`
- `pages\1245.html`
- `pages\1246.html`
- `pages\1247.html`
- `pages\1248.html`
- `pages\1249.html`
- `pages\1250.html`
- `pages\1251.html`
- `pages\1252.html`
- `pages\1253.html`
- `pages\1254.html`
- `pages\1255.html`
- `pages\1256.html`
- `pages\1257.html`
- `pages\1258.html`
- `pages\1259.html`
- `pages\1260.html`
- `pages\1261.html`
- `pages\1262.html`
- `pages\1263.html`
- `pages\1264.html`
- `pages\1265.html`
- `pages\1266.html`
- `pages\1267.html`
- `pages\1268.html`
- `pages\1269.html`
- `pages\1270.html`
- `pages\1271.html`
- `pages\1272.html`
- `pages\1274.html`
- `pages\1275.html`
- `pages\1276.html`
- `pages\1277.html`
- `pages\1278.html`
- `pages\1279.html`
- `pages\1440.html`
- `pages\1441.html`
- `pages\1442.html`
- `pages\1443.html`
- `pages\1444.html`
- `pages\1445.html`
- `pages\1446.html`
- `pages\1447.html`
- `pages\1448.html`
- `pages\1449.html`
- `pages\1450.html`
- `pages\1451.html`
- `pages\1452.html`
- `pages\1453.html`
- `pages\1454.html`
- `pages\1455.html`
- `pages\1456.html`
- `pages\1457.html`
- `pages\1458.html`
- `pages\1459.html`
- `pages\1460.html`
- `pages\1461.html`
- `pages\1462.html`
- `pages\1463.html`
- `pages\1464.html`
- `pages\1465.html`
- `pages\1466.html`
- `pages\1467.html`
- `pages\1468.html`
- `pages\1469.html`
- `pages\1470.html`
- `pages\1471.html`
- `pages\1472.html`
- `pages\1473.html`
- `pages\1474.html`
- `pages\1475.html`
- `pages\1476.html`
- `pages\1477.html`
- `pages\1478.html`
- `pages\1479.html`
- `pages\1481.html`
- `pages\1482.html`
- `pages\1483.html`
- `pages\1484.html`
- `pages\1485.html`
- `pages\1486.html`
- `pages\1487.html`
- `pages\1488.html`
- `pages\1489.html`
- `pages\1490.html`
- `pages\1491.html`
- `pages\1492.html`
- `pages\1493.html`
- `pages\1494.html`
- `pages\1495.html`
- `pages\1496.html`
- `pages\1497.html`
- `pages\1499.html`
- `pages\1500.html`
- `pages\1501.html`
- `pages\1502.html`
- `pages\1503.html`
- `pages\1504.html`
- `pages\1505.html`
- `pages\1506.html`
- `pages\1507.html`
- `pages\1508.html`
- `pages\1509.html`
- `pages\1510.html`
- `pages\1511.html`
- `pages\1512.html`
- `pages\1513.html`
- `pages\1514.html`
- `pages\1515.html`
- `pages\1516.html`
- `pages\1517.html`
- `pages\1518.html`
- `pages\1519.html`
- `pages\1520.html`
- `pages\1521.html`
- `pages\1522.html`
- `pages\1523.html`
- `pages\1524.html`
- `pages\1525.html`
- `pages\1526.html`
- `pages\1527.html`
- `pages\1528.html`
- `pages\1529.html`
- `pages\1530.html`
- `pages\1531.html`
- `pages\1532.html`
- `pages\1533.html`
- `pages\1534.html`
- `pages\1535.html`
- `pages\1536.html`
- `pages\1537.html`
- `pages\1538.html`
- `pages\1539.html`
- `pages\1540.html`
- `pages\1541.html`
- `pages\1542.html`
- `pages\1543.html`
- `pages\1544.html`
- `pages\1545.html`
- `pages\1546.html`
- `pages\1547.html`
- `pages\1548.html`
- `pages\1549.html`
- `pages\1550.html`
- `pages\1551.html`
- `pages\1552.html`
- `pages\1553.html`
- `pages\1554.html`
- `pages\1555.html`
- `pages\1556.html`
- `pages\1557.html`
- `pages\1558.html`
- `pages\1559.html`
- `pages\1560.html`
- `pages\1561.html`
- `pages\1562.html`
- `pages\1563.html`
- `pages\1564.html`
- `pages\1565.html`
- `pages\1566.html`
- `pages\1567.html`
- `pages\1568.html`
- `pages\1569.html`
- `pages\1570.html`
- `pages\1571.html`
- `pages\1572.html`
- `pages\1573.html`
- `pages\1574.html`
- `pages\1575.html`
- `pages\1576.html`
- `pages\1577.html`
- `pages\1578.html`
- `pages\1579.html`
