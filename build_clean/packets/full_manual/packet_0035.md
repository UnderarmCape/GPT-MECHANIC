# Deep Research Manual Packet 0035

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0035
- Chunk count: 337
- Chunk range: 8726-9062
- Source count: 281
- Target maximum characters: 750000

## Manual Chunks

## Chunk 8726: Checking for DTCs

- Title: Checking for DTCs
- Source path: `pages\11317.html`
- Chunk ID: `chunk_f8f3a7a42858`
- Images: none
- Duplicate sources: `pages\16196.html`

### Full Text

````text
# Checking for DTCs

A/C Error Display Screen ID | Display No. | Parts Name | Contents | DTC | Detection Item

A | A1 | Ambient temperature Sensor | Open | B1227 | An open in the outside air temperature sensor circuit

A2 | Ambient temperature Sensor | Short | B1228 | A short in the outside air temperature sensor circuit

A3 | Solar radiation Sensor | Fail | B123F | Automatic lighting control unit/sunlight sensor error

A4 | Solar radiation Sensor Variation | Unknown | --- | Unknown sunlight sensor type

A5 | Evaporator Sensor | Open | B1231 | An open in the evaporator temperature sensor circuit

A6 | Evaporator Sensor | Short | B1232 | A short in the evaporator temperature sensor circuit

B1 | In-car temperature Sensor | Open | B1225 | An open in the in-car temperature sensor circuit

B2 | In-car temperature Sensor | Short | B1226 | A short in the in-car temperature sensor circuit

B | A1 | A/M motor (Dr) | Open | B1233 | An open in the air mix control motor circuit (driver's)

A2 | A/M motor (Dr) | Short | B1234 | A short in the air mix control motor circuit (driver's)

A3 | A/M motor (Dr) | Lock | B1235 | A problem in the air mix control motor circuit, linkage, door, or motor (driver's)

A4 *1 | A/M motor (As) | Open | B1236 | An open in the passenger's air mix control motor circuit

A5 *1 | A/M motor (As) | Short | B1237 | A short in the passenger's air mix control motor circuit

A6 *1 | A/M motor (As) | Lock | B1238 | A problem in the passenger's air mix control motor circuit, linkage, door, or motor

B4 | Mode motor(Dr) | Open | B121A | An open in the mode control motor circuit

B5 | Mode motor (Dr) | Short | B121B | A short in the mode control motor circuit

B6 | Mode motor(Dr) | Lock | B1240 | A problem in the mode control motor circuit, linkage, door, or motor

C | A4 | R/F motor | Open | B2986 | An open in the recirculation control motor circuit

A5 | R/F motor | Short | B1220 | A short in the recirculation control motor circuit

A6 | R/F motor | Lock | B2983 | A problem in the recirculation control motor circuit, linkage, door, or motor

A7 | Blower motor | Lock | B1241 | A problem in the blower motor circuit

B1 | Compressor solenoid | Open | B2988 | An open in the A/C compressor variable capacity control solenoid circuit

B2 | Compressor solenoid | Short | A short in the A/C compressor variable capacity control solenoid circuit

*1: With dual zone climate control

*2: With seat heater

A/C Error Display Screen ID | Display No. | Parts Name | Contents | DTC | Detection Item

D | A1 | B-CAN | BUS OFF | U1280 | Communication bus line error (BUS-OFF)

A2 | Lost Communication with | Meter (BCAN) | U128D | Climate control unit lost communication with gauge control module

A3 | Lost Communication with | MICU (BCAN) | U1281 | Climate control unit lost communication with MICU (body control module)

A4 | Lost Communication with | AHU (BCAN) | --- | Climate control unit lost communication with center display unit

A6 *2 | Lost Communication with | HCS (BCAN) | U1290 | Climate control unit lost communication with seat heater control unit (front)

B4 | LIN Communication | BUS OFF | B120A | Climate control unit LIN communication bus line error

B5 | Lost Communication with | Fr PANEL (LIN) | B2964 | Climate control unit lost communication with front panel (climate control panel)

B8 | EEPROM Data | Error | --- | Climate control unit internal error

*1: With dual zone climate control

*2: With seat heater
````

## Chunk 8727: How to Check for History DTCs

- Title: How to Check for History DTCs
- Source path: `pages\11318.html`
- Chunk ID: `chunk_c9c54e64834c`
- Images: none
- Duplicate sources: `pages\16197.html`

### Full Text

````text
# How to Check for History DTCs

The climate control unit can record history DTCs. To read the history DTCs, do the following:

1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

2. While pressing the WINDSHIELD DEFROST button, press and hold the ON/OFF button for 10 seconds or more. While pressing and holding both the WINDSHIELD DEFROST and ON/OFF buttons, the display screen goes directly to the A/C Error Display shown.

NOTE:

- If there are any problems in the system, the A/C Error Display screen will indicate them. Select the previous/next icon to confirm the DTCs. To determine the meaning of the indication, refer to the table that follows.

- If there are no problems detected, The error status shows Normal, and The number of Errors indicates "0".

Canceling the Read History DTCs

4. Turn the vehicle to the OFF (LOCK) mode to cancel reading the history DTCs. After completing the repair work, clear the DTCs.
````

## Chunk 8728: How to Clear the History DTCs

- Title: How to Clear the History DTCs
- Source path: `pages\11319.html`
- Chunk ID: `chunk_5aae82a367e6`
- Images: none
- Duplicate sources: `pages\16198.html`

### Full Text

````text
# How to Clear the History DTCs

1. Turn the vehicle to the OFF (LOCK) mode and then the vehicle ON mode.

2. While pressing the WINDSHIELD DEFROST button, press and hold the ON/OFF button for 10 seconds or more.

3. While pressing and holding both the WINDSHIELD DEFROST and ON/OFF buttons, the display screen goes directly to the A/C Error Display shown, touch and hold the Error Clear icon for 5 seconds.

4. Do the How to Check for History DTCs to verify DTCs have been cleared.
````

## Chunk 8729: Checks Before Using the Sensor Input Display Mode

- Title: Checks Before Using the Sensor Input Display Mode
- Source path: `pages\11321.html`
- Chunk ID: `chunk_ab03dd167362`
- Images: none
- Duplicate sources: `pages\16200.html`

### Full Text

````text
# Checks Before Using the Sensor Input Display Mode

1. Turn the vehicle to the ON mode, and check the recirculation door function; press the RECIRCULATION button to switch from FRESH to RECIRCLATE. The air volume and sound should change slightly. Set the TEMPERATURE CONTROL dial to the desired test temperature:

- "Lo" temperature setting will default to MAX COOL, VENT and RECIRCULATE (A/C on) or FRESH (A/C off).

- "Hi" temperature setting will default to MAX HOT, HEAT, HEAT/DEF, and FRESH.

3. Turn the vehicle to the OFF (LOCK) mode.
````

## Chunk 8730: Run the Sensor Input Display Mode

- Title: Run the Sensor Input Display Mode
- Source path: `pages\11322.html`
- Chunk ID: `chunk_fcd89342a565`
- Images: `images\GHH409261.jpeg`, `images\GHH409262.jpeg`, `images\GHH409263.jpeg`, `images\GHH409264.jpeg`, `images\GHH409265.jpeg`, `images\GHH409266.jpeg`
- Duplicate sources: `pages\16201.html`

### Full Text

````text
# Run the Sensor Input Display Mode

1. Press and hold both the AUTO and RECIRCULATION buttons, then start the engine.

2. Release both buttons. The display screen goes directly to the A/C sensor display mode shown. The display screen indicates the sensor ID and then the value for that sensor.

Courtesy of HONDA, U.S.A., INC.

3. To advance to the next sensor, touch the sensor ID previous/next icon or press the REAR WINDOW DEFOGGER/MIRROR DEFOGGER * button.*: With mirror defogger To cancel the sensor input display mode, press the AUTO button or turn the vehicle to the OFF (LOCK) mode.

NOTE:

- The sensor values will be displayed in degrees Celsius (deg.C) or an alphanumeric code. Use the chart to convert the value to degrees Fahrenheit (deg.F).

- If the sensor value displays "Error", this indicates there is an open or short in the circuit or sensor. Check for DTCs using the HDS, or use the climate control self-diagnostic function.

- If necessary, compare the sensor input display to a known-good vehicle under the same test conditions.

- If the sensor displayed value is out of the normal range, refer to the sensor test or substitute a known-good sensor, and recheck.

- Unsupported items shall be skipped.

Sensor ID | Sensor Name | Data Value

0 | In-car temperature sensor | deg.C

1 | Outside air temperature sensor | deg.C

2 | Sunlight sensor | 10 W/m 2.h

3 | Engine coolant temperature | deg.C

4 | Evaporator temperature sensor | deg.C

8 | Air mix opening (low value indicates cooler air distribution, higher value indicates warmer air distribution) | % of opening

9 | Passenger's air mix opening (low value indicates cooler air distribution, higher value indicates warmer air distribution) | % of opening

11 | Mode positioning | 0.1 V

13 | Recirculation control opening | % of opening

14 | Sunlight sensor type | Hard Wire BCAN Unknown

- Hard Wire

- BCAN

- Unknown

15 | Vehicle speed (vehicle must be driven to display speed) | km/h

16 | A/C compressor oil circulation | Finished Unfinished

- Finished

- Unfinished

19 | Not used | ---

Celsius to Fahrenheit Conversion Table

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

0 | 32 | 10 | 50 | 20 | 68 | 30 | 86 | 40 | 104

1 | 34 | 11 | 52 | 21 | 70 | 31 | 88 | 41 | 106

2 | 36 | 12 | 54 | 22 | 72 | 32 | 90 | 42 | 108

3 | 37 | 13 | 55 | 23 | 73 | 33 | 91 | 43 | 109

4 | 39 | 14 | 57 | 24 | 75 | 34 | 93 | 44 | 111

5 | 41 | 15 | 59 | 25 | 77 | 35 | 95 | 45 | 113

6 | 43 | 16 | 61 | 26 | 79 | 36 | 97 | 46 | 115

7 | 45 | 17 | 63 | 27 | 81 | 37 | 99 | 47 | 117

8 | 46 | 18 | 64 | 28 | 82 | 38 | 100 | 48 | 118

9 | 48 | 19 | 66 | 29 | 84 | 39 | 102 | 49 | 120

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

50 | 122 | 60 | 140 | 70 | 158 | 80 | 176 | 90 | 194

51 | 124 | 61 | 142 | 71 | 160 | 81 | 178 | 91 | 196

52 | 126 | 62 | 144 | 72 | 162 | 82 | 180 | 92 | 198

53 | 127 | 63 | 145 | 73 | 163 | 83 | 181 | 93 | 199

54 | 129 | 64 | 147 | 74 | 165 | 84 | 183 | 94 | 201

55 | 131 | 65 | 149 | 75 | 167 | 85 | 185 | 95 | 203

56 | 133 | 66 | 151 | 76 | 169 | 86 | 187 | 96 | 205

deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F | deg.C | deg.F

57 | 135 | 67 | 153 | 77 | 171 | 87 | 189 | 97 | 207

58 | 136 | 68 | 154 | 78 | 172 | 88 | 190 | 98 | 208

59 | 138 | 69 | 156 | 79 | 174 | 89 | 192 | 99 | 210

Alphanumeric Conversion Table (Mode Positioning)

Display Reading (Volt) | Mode Position

0.5 | Courtesy of HONDA, U.S.A., INC.

1.3 or 1.9 | Courtesy of HONDA, U.S.A., INC.

2.6 | Courtesy of HONDA, U.S.A., INC.

3.2 or 3.7 | Courtesy of HONDA, U.S.A., INC.

4.5 | Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8731: DTC A-A4, Cd

- Title: DTC A-A4, Cd
- Source path: `pages\11323.html`
- Chunk ID: `chunk_35a118420277`
- Images: none
- Duplicate sources: `pages\16202.html`

### Full Text

````text
# DTC A-A4, Cd

DTC screen A-A4 or DTC indicator Cd : Unknown Sunlight Sensor Type

- DTC check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B123F Automatic lighting control unit/sunlight sensor error Is DTC B123F or Error on the DTC screen A-A3 (climate control panel without display) or 17 (climate control panel with display) indicated? YES Go to climate control DTC B123F troubleshooting . NO Go to step 2.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B123F Automatic lighting control unit/sunlight sensor error

Is DTC B123F or Error on the DTC screen A-A3 (climate control panel without display) or 17 (climate control panel with display) indicated?

YES

Go to climate control DTC B123F troubleshooting .

NO

Go to step 2.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -2. Do the Self-Diagnostic Function with the climate control unit . -3. Check for DTCs. Is Error on the DTC screen A-A4 (climate control panel without display) or Cd (climate control panel with display) indicated? YES Go to step 3. NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-2. Do the Self-Diagnostic Function with the climate control unit .

-3. Check for DTCs.

Is Error on the DTC screen A-A4 (climate control panel without display) or Cd (climate control panel with display) indicated?

YES

Go to step 3.

NO

Intermittent failure, the system is OK at this time.

- Connector check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check connection of the following connectors. Sunlight sensor 2P connector (with automatic wiper or without automatic lighting) Automatic lighting control unit-sensor 5P connector (without automatic wiper and with automatic lighting) Climate control unit connector A (32P) Is the connection OK? YES Replace the climate control unit . NO Reconnect or repair the connector, then recheck the system.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check connection of the following connectors.

Sunlight sensor 2P connector (with automatic wiper or without automatic lighting)

Automatic lighting control unit-sensor 5P connector (without automatic wiper and with automatic lighting)

Climate control unit connector A (32P)

Is the connection OK?

YES

Replace the climate control unit .

NO

Reconnect or repair the connector, then recheck the system.
````

## Chunk 8732: DTC D-A4

- Title: DTC D-A4
- Source path: `pages\11324.html`
- Chunk ID: `chunk_844ddd68f644`
- Images: none
- Duplicate sources: `pages\16203.html`

### Full Text

````text
# DTC D-A4

DTC screen D-A4 : Climate Control Unit Lost Communication with Center Display Unit

NOTE: The DTC may be stored due to the grounding failure or the power source failure at the center display (the grounding inspection and the power source inspection on each control unit are required prior to this checking process).

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -2. Do the Self-Diagnostic Function with the climate control unit . -3. Check for DTCs. Is Error on the DTC screen D-A4 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for loose wires or poor connections.

-1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-2. Do the Self-Diagnostic Function with the climate control unit .

-3. Check for DTCs.

Is Error on the DTC screen D-A4 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for loose wires or poor connections.

- Open wire check (B-CAN_H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Audio unit connector A (24P) (without navigation) Audio-navigation unit connector A (24P) (with navigation) Climate control unit connector A (32P) -3. Check for continuity between test points 1 and 2. Without navigation Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Climate control unit connector A (32P): disconnected Test point 1 Audio unit connector A (24P) No. 14 Test point 2 Climate control unit connector A (32P) No. 25 With navigation Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Climate control unit connector A (32P): disconnected Test point 1 Audio-navigation unit connector A (24P) No. 14 Test point 2 Climate control unit connector A (32P) No. 25 Is there continuity? YES The B-CAN_H wire is OK. Go to step 3. NO Repair an open in the B-CAN_H wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Audio unit connector A (24P) (without navigation)

Audio-navigation unit connector A (24P) (with navigation)

Climate control unit connector A (32P)

-3. Check for continuity between test points 1 and 2.

Without navigation

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Audio unit connector A (24P) No. 14

Test point 2 | Climate control unit connector A (32P) No. 25

With navigation

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Audio-navigation unit connector A (24P) No. 14

Test point 2 | Climate control unit connector A (32P) No. 25

Is there continuity?

YES

The B-CAN_H wire is OK. Go to step 3.

NO

Repair an open in the B-CAN_H wire.

- Open wire check (B-CAN_L line) -1. Check for continuity between test points 1 and 2. Without navigation Test condition Vehicle OFF (LOCK) mode Audio unit connector A (24P): disconnected Climate control unit connector A (32P): disconnected Test point 1 Audio unit connector A (24P) No. 24 Test point 2 Climate control unit connector A (32P) No. 8 With navigation Test condition Vehicle OFF (LOCK) mode Audio-navigation unit connector A (24P): disconnected Climate control unit connector A (32P): disconnected Test point 1 Audio-navigation unit connector A (24P) No. 24 Test point 2 Climate control unit connector A (32P) No. 8 Is there continuity? YES Replace the audio unit (without navigation) or the audio-navigation unit (with navigation) . NO Repair an open in the B-CAN_L wire.

-1. Check for continuity between test points 1 and 2.

Without navigation

Test condition | Vehicle OFF (LOCK) mode

Audio unit connector A (24P): disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Audio unit connector A (24P) No. 24

Test point 2 | Climate control unit connector A (32P) No. 8

With navigation

Test condition | Vehicle OFF (LOCK) mode

Audio-navigation unit connector A (24P): disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Audio-navigation unit connector A (24P) No. 24

Test point 2 | Climate control unit connector A (32P) No. 8

Is there continuity?

YES

Replace the audio unit (without navigation) or the audio-navigation unit (with navigation) .

NO

Repair an open in the B-CAN_L wire.
````

## Chunk 8733: DTC D-B8, C0

- Title: DTC D-B8, C0
- Source path: `pages\11325.html`
- Chunk ID: `chunk_9ad354e46fd4`
- Images: none
- Duplicate sources: `pages\16204.html`

### Full Text

````text
# DTC D-B8, C0

DTC screen D-B8 or DTC indicator C0 : Climate Control Unit Internal Error

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -2. Do the Self-Diagnostic Function with the climate control unit . -3. Check for DTCs. Is Error on the DTC screen D-B8 (climate control panel without display) or C0 (climate control panel with display) indicated? YES Replace the climate control unit . NO Intermittent failure, the climate control unit is OK at this time.

-1. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-2. Do the Self-Diagnostic Function with the climate control unit .

-3. Check for DTCs.

Is Error on the DTC screen D-B8 (climate control panel without display) or C0 (climate control panel with display) indicated?

YES

Replace the climate control unit .

NO

Intermittent failure, the climate control unit is OK at this time.
````

## Chunk 8734: DTC B120A (D-B4), B120A (8A)

- Title: DTC B120A (D-B4), B120A (8A)
- Source path: `pages\11326.html`
- Chunk ID: `chunk_545b3ae85562`
- Images: `images\GHH409267.jpeg`, `images\GHH409268.jpeg`, `images\GHH409269.jpeg`
- Duplicate sources: `pages\13068.html`

### Full Text

````text
# DTC B120A (D-B4), B120A (8A)

DTC B120A, DTC screen D-B4, or DTC indicator 8A : Climate Control Unit LIN Communication bus Line Error

DTC Description | DTC

B120A Climate control unit LIN communication bus line error

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B120A Climate control unit LIN communication bus line error Is DTC B120A, Error on the DTC screen D-B4 (climate control panel without display), or DTC indicator 8A (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the climate control panel circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B120A Climate control unit LIN communication bus line error

Is DTC B120A, Error on the DTC screen D-B4 (climate control panel without display), or DTC indicator 8A (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the climate control panel circuit.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B9 Is the fuse OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B9

Is the fuse OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

- Determine possible failure area (BUS-DATA line, others) -1. Disconnect the following connector. Climate control panel 12P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control panel 12P connector: disconnected Test point 1 Climate control panel 12P connector No. 1 Test point 2 Climate control panel 12P connector No. 4 Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 4. NO Go to step 7.

-1. Disconnect the following connector.

Climate control panel 12P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control panel 12P connector: disconnected

Test point 1 | Climate control panel 12P connector No. 1

Test point 2 | Climate control panel 12P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 4.

NO

Go to step 7.

- Shorted wire check (BUS-DATA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the BUS-DATA wire. NO The BUS-DATA wire is not shorted. Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Climate control panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BUS-DATA wire.

NO

The BUS-DATA wire is not shorted. Go to step 5.

- Open wire check (BUS-DATA line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Climate control panel 12P connector No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BUS-DATA wire is OK. Go to step 6. NO Repair an open in the BUS-DATA wire.

-1. Check for continuity between test points 1 and 2.
````

## Chunk 8735: DTC B120A (D-B4), B120A (8A)

- Title: DTC B120A (D-B4), B120A (8A)
- Source path: `pages\11326.html`
- Chunk ID: `chunk_2e20afabfe99`
- Images: `images\GHH409267.jpeg`, `images\GHH409268.jpeg`, `images\GHH409269.jpeg`
- Duplicate sources: `pages\13068.html`

### Full Text

````text
ontrol panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BUS-DATA wire.

NO

The BUS-DATA wire is not shorted. Go to step 5.

- Open wire check (BUS-DATA line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Climate control panel 12P connector No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BUS-DATA wire is OK. Go to step 6. NO Repair an open in the BUS-DATA wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Climate control panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Climate control panel 12P connector No. 9

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The BUS-DATA wire is OK. Go to step 6.

NO

Repair an open in the BUS-DATA wire.

- Climate control panel check -1. Reconnect the following connector. Climate control unit connector A (32P) -2. Substitute a known-good climate control panel . -3. Clear the DTCs with the HDS. -4. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -5. Do the Self-Diagnostic Function with the HDS or the climate control unit . -6. Check for DTCs. DTC Description DTC B120A Climate control unit LIN communication bus line error Is DTC B120A, Error on the DTC screen D-B4 (climate control panel without display), or DTC indicator 8A (climate control panel with display) indicated? YES Replace the climate control unit . NO Replace the original climate control panel .

-1. Reconnect the following connector.

Climate control unit connector A (32P)

-2. Substitute a known-good climate control panel .

-3. Clear the DTCs with the HDS.

-4. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-5. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-6. Check for DTCs.

DTC Description | DTC

B120A Climate control unit LIN communication bus line error

Is DTC B120A, Error on the DTC screen D-B4 (climate control panel without display), or DTC indicator 8A (climate control panel with display) indicated?

YES

Replace the climate control unit .

NO

Replace the original climate control panel .

- Open wire check (IG2 A/C (L15B7/K20C2 engine) or IG2 OPTION (L15BA/K20C1/L15BY engine) line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control panel 12P connector: disconnected Test point 1 Climate control panel 12P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Check for an open in the GND wire between the climate control panel and body ground. If the wire is OK, check for poor ground at G503. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/K20C1/L15BY engine Repair an open in the IG2 OPTION wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control panel 12P connector: disconnected

Test point 1 | Climate control panel 12P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Check for an open in the GND wire between the climate control panel and body ground. If the wire is OK, check for poor ground at G503.

NO: L15B7/K20C2 engine

Repair an open in the IG2 A/C wire.

NO: L15BA/K20C1/L15BY engine

Repair an open in the IG2 OPTION wire.
````

## Chunk 8736: DTC B121A (B-B4), B121A (49)

- Title: DTC B121A (B-B4), B121A (49)
- Source path: `pages\11327.html`
- Chunk ID: `chunk_782129c2826a`
- Images: `images\GHH409270.jpeg`, `images\GHH409271.jpeg`
- Duplicate sources: `pages\13069.html`

### Full Text

````text
# DTC B121A (B-B4), B121A (49)

DTC B121A or DTC screen B-B4 or DTC indicator 49 : An Open in the Mode Control Motor Circuit

DTC Description | DTC

B121A An open in the mode control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B121A An open in the mode control motor circuit Is DTC B121A, Error on the DTC screen B-B4 (climate control panel without display) or 49 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B121A An open in the mode control motor circuit

Is DTC B121A, Error on the DTC screen B-B4 (climate control panel without display) or 49 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

- Determine possible failure area (MDD-P-DR line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Mode control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Mode control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The MDD-P-DR wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Mode control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Mode control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The MDD-P-DR wire is OK. Go to step 3.

NO

Go to step 4.

- Open wire check (SENS COM-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Mode control motor 5P connector No. 4 Test point 2 Mode control motor 5P connector No. 5 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the mode control motor . NO Repair an open in the SENS COM-H wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Mode control motor 5P connector No. 4

Test point 2 | Mode control motor 5P connector No. 5

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the mode control motor .

NO

Repair an open in the SENS COM-H wire.

- Open wire check (MDD-P-DR line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 5 Test point 2 Body ground Is there about 5 V? YES Repair an open in the MDD-P-DR wire. NO Replace the climate control unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 5

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the MDD-P-DR wire.

NO

Replace the climate control unit .
````

## Chunk 8737: DTC B121B (B-B5), B121B (4A)

- Title: DTC B121B (B-B5), B121B (4A)
- Source path: `pages\11328.html`
- Chunk ID: `chunk_4706803db405`
- Images: `images\GHH409272.jpeg`, `images\GHH409273.jpeg`
- Duplicate sources: `pages\13070.html`

### Full Text

````text
# DTC B121B (B-B5), B121B (4A)

DTC B121B or DTC screen B-B5 or DTC indicator 4A : A Short in the Mode Control Motor Circuit

NOTE: If other short circuit DTCs are indicated at the same time, there may be an open or short to body ground in the power (5 V) circuit.

DTC Description | DTC

B121B A short in the mode control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B121B A short in the mode control motor circuit Is DTC B121B or Error on the DTC screen B-B5 (climate control panel without display) or 4A (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B121B A short in the mode control motor circuit

Is DTC B121B or Error on the DTC screen B-B5 (climate control panel without display) or 4A (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

- Determine possible failure area (S5V-H line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Mode control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Mode control motor 5P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The S5V-H wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Mode control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Mode control motor 5P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The S5V-H wire is OK. Go to step 3.

NO

Go to step 4.

- Determine possible failure area (mode control motor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Mode control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the mode control motor . NO Go to step 6.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Mode control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the mode control motor .

NO

Go to step 6.

- Open wire check (S5V-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there about 5 V? YES Repair an open in the S5V-H wire. NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3.
````

## Chunk 8738: DTC B121B (B-B5), B121B (4A)

- Title: DTC B121B (B-B5), B121B (4A)
- Source path: `pages\11328.html`
- Chunk ID: `chunk_f582b8a4ab3f`
- Images: `images\GHH409272.jpeg`, `images\GHH409273.jpeg`
- Duplicate sources: `pages\13070.html`

### Full Text

````text
ector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the S5V-H wire.

NO

Replace the climate control unit .

- Shorted wire check (MDD-P-DR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 5 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the MDD-P-DR wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the MDD-P-DR wire.

NO

Replace the climate control unit .
````

## Chunk 8739: DTC B1220 (C-A5), B1220 (56)

- Title: DTC B1220 (C-A5), B1220 (56)
- Source path: `pages\11329.html`
- Chunk ID: `chunk_850119699fe2`
- Images: `images\GHH409274.jpeg`, `images\GHH409275.jpeg`
- Duplicate sources: `pages\13071.html`

### Full Text

````text
# DTC B1220 (C-A5), B1220 (56)

DTC B1220 or DTC screen C-A5 or DTC indicator 56 : A Short in the Recirculation Control Motor Circuit

NOTE: If other short circuit DTCs are indicated at the same time, there may be an open or short to body ground in the power (5 V) circuit.

DTC Description | DTC

B1220 A short in the recirculation control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1220 A short in the recirculation control motor circuit Is DTC B1220 or Error on the DTC screen C-A5 (climate control panel without display) or 56 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1220 A short in the recirculation control motor circuit

Is DTC B1220 or Error on the DTC screen C-A5 (climate control panel without display) or 56 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

- Determine possible failure area (S5V-H line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Recirculation control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Recirculation control motor 5P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The S5V-H wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Recirculation control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Recirculation control motor 5P connector No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The S5V-H wire is OK. Go to step 3.

NO

Go to step 4.

- Determine possible failure area (recirculation control motor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Recirculation control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the recirculation control motor . NO Go to step 6.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Recirculation control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the recirculation control motor .

NO

Go to step 6.

- Open wire check (S5V-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there about 5 V? YES Repair an open in the S5V-H wire. NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short in the S5V-H wire.
````

## Chunk 8740: DTC B1220 (C-A5), B1220 (56)

- Title: DTC B1220 (C-A5), B1220 (56)
- Source path: `pages\11329.html`
- Chunk ID: `chunk_651a1a7a7b0b`
- Images: `images\GHH409274.jpeg`, `images\GHH409275.jpeg`
- Duplicate sources: `pages\13071.html`

### Full Text

````text
he voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short in the S5V-H wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the S5V-H wire.

NO

Replace the climate control unit .

- Shorted wire check (RFD-P line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 4 Test point 2 Body ground Is there continuity? YES Repair a short in the RFD-P wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 4

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the RFD-P wire.

NO

Replace the climate control unit .
````

## Chunk 8741: DTC B1225 (A-B1), B1225 (01)

- Title: DTC B1225 (A-B1), B1225 (01)
- Source path: `pages\11330.html`
- Chunk ID: `chunk_22b856fe4d29`
- Images: `images\GHH409276.jpeg`, `images\GHH409277.jpeg`
- Duplicate sources: `pages\13072.html`

### Full Text

````text
# DTC B1225 (A-B1), B1225 (01)

DTC B1225 or DTC screen A-B1 or DTC indicator 01 : An Open in the In-Car Temperature Sensor Circuit

DTC Description | DTC

B1225 An open in the in-car temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1225 An open in the in-car temperature sensor circuit Is DTC B1225 or Error on the DTC screen A-B1 (climate control panel without display) or 01 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the in-car temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1225 An open in the in-car temperature sensor circuit

Is DTC B1225 or Error on the DTC screen A-B1 (climate control panel without display) or 01 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the in-car temperature sensor circuit.

- Open wire check (TR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector A (32P) In-car temperature sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 27 Test point 2 In-car temperature sensor 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TR wire is not open. Go to step 3. NO Repair an open in the TR wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector A (32P)

In-car temperature sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 27

Test point 2 | In-car temperature sensor 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TR wire is not open. Go to step 3.

NO

Repair an open in the TR wire.

- Open wire check (SENSOR COM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 In-car temperature sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SENSER COM wire is OK. Go to step 4. NO Repair an open in the SENSOR COM wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | In-car temperature sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SENSER COM wire is OK. Go to step 4.

NO

Repair an open in the SENSOR COM wire.

- Shorted wire check (TR line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control unit connector A (32P): disconnected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 27 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the TR wire. NO The TR wire is OK. Go to step 5.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control unit connector A (32P): disconnected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 27

Test point 2 | Body ground

Is there any voltage?

YES

Repair a short to power in the TR wire.

NO

The TR wire is OK. Go to step 5.

- In-car temperature sensor check -1.
````

## Chunk 8742: DTC B1225 (A-B1), B1225 (01)

- Title: DTC B1225 (A-B1), B1225 (01)
- Source path: `pages\11330.html`
- Chunk ID: `chunk_985beea83bf4`
- Images: `images\GHH409276.jpeg`, `images\GHH409277.jpeg`
- Duplicate sources: `pages\13072.html`

### Full Text

````text
and 2. Test condition Vehicle ON mode Climate control unit connector A (32P): disconnected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 27 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the TR wire. NO The TR wire is OK. Go to step 5.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control unit connector A (32P): disconnected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 27

Test point 2 | Body ground

Is there any voltage?

YES

Repair a short to power in the TR wire.

NO

The TR wire is OK. Go to step 5.

- In-car temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the in-car temperature sensor . Is the in-car temperature sensor OK? YES Replace the climate control unit . NO Replace the in-car temperature sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the in-car temperature sensor .

Is the in-car temperature sensor OK?

YES

Replace the climate control unit .

NO

Replace the in-car temperature sensor .
````

## Chunk 8743: DTC B1226 (A-B2), B1226 (02)

- Title: DTC B1226 (A-B2), B1226 (02)
- Source path: `pages\11331.html`
- Chunk ID: `chunk_4dab8169cc72`
- Images: none
- Duplicate sources: `pages\13073.html`

### Full Text

````text
# DTC B1226 (A-B2), B1226 (02)

DTC B1226 or DTC screen A-B2 or DTC indicator 02 : A Short in the In-Car Temperature Sensor Circuit

DTC Description | DTC

B1226 A short in the in-car temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1226 A short in the in-car temperature sensor circuit Is DTC B1226 or Error on the DTC screen A-B2 (climate control panel without display) or 02 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the in-car temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1226 A short in the in-car temperature sensor circuit

Is DTC B1226 or Error on the DTC screen A-B2 (climate control panel without display) or 02 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the in-car temperature sensor circuit.

- Shorted wire check (TR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector A (32P) In-car temperature sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 27 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TR wire. NO The TR wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector A (32P)

In-car temperature sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 27

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TR wire.

NO

The TR wire is not shorted. Go to step 3.

- Shorted wire check (TR line to SENSOR COM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected In-car temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 Climate control unit connector A (32P) No. 27 Is there continuity? YES Repair a short in the TR wire to SENSOR COM wire. NO The TR wire and SENSOR COM wire are OK. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

In-car temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | Climate control unit connector A (32P) No. 27

Is there continuity?

YES

Repair a short in the TR wire to SENSOR COM wire.

NO

The TR wire and SENSOR COM wire are OK. Go to step 4.

- In-car temperature sensor check -1. Test the in-car temperature sensor . Is the in-car temperature sensor OK? YES Replace the climate control unit . NO Replace the in-car temperature sensor .

-1. Test the in-car temperature sensor .

Is the in-car temperature sensor OK?

YES

Replace the climate control unit .

NO

Replace the in-car temperature sensor .
````

## Chunk 8744: DTC B1227 (A-A1), B1227 (05)

- Title: DTC B1227 (A-A1), B1227 (05)
- Source path: `pages\11332.html`
- Chunk ID: `chunk_cc97a82d2238`
- Images: `images\GHH409278.jpeg`, `images\GHH409279.jpeg`
- Duplicate sources: `pages\13074.html`

### Full Text

````text
# DTC B1227 (A-A1), B1227 (05)

DTC B1227, DTC screen A-A1, or DTC indicator 05 : An Open in the Outside Air Temperature Sensor Circuit

DTC Description | DTC

B1227 An open in the outside air temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1227 An open in the outside air temperature sensor circuit Is DTC B1227, Error on the DTC screen A-A1 (climate control panel without display), or DTC indicator 05 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the outside air temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1227 An open in the outside air temperature sensor circuit

Is DTC B1227, Error on the DTC screen A-A1 (climate control panel without display), or DTC indicator 05 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the outside air temperature sensor circuit.

- Open wire check (TAM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector A (32P) Outside air temperature sensor 2P connector -3. Check for continuity between test points 1 and 2. L15B7/K20C2 engine Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 11 Test point 2 Outside air temperature sensor 2P connector No. 1 L15BA/K20C1/L15BY engine Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 11 Test point 2 Outside air temperature sensor 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TAM wire is not open. Go to step 3. NO Repair an open in the TAM wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector A (32P)

Outside air temperature sensor 2P connector

-3. Check for continuity between test points 1 and 2.

L15B7/K20C2 engine

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 11

Test point 2 | Outside air temperature sensor 2P connector No. 1

L15BA/K20C1/L15BY engine

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 11

Test point 2 | Outside air temperature sensor 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TAM wire is not open. Go to step 3.

NO

Repair an open in the TAM wire.

- Open wire check (SENSOR COM line) -1. Check for continuity between test points 1 and 2. L15B7/K20C2 engine Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 Outside air temperature sensor 2P connector No. 2 L15BA/K20C1/L15BY engine Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 Outside air temperature sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SENSOR COM wire is OK. Go to step 4. NO Repair an open in the SENSOR COM wire.

-1. Check for continuity between test points 1 and 2.

L15B7/K20C2 engine

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12
````

## Chunk 8745: DTC B1227 (A-A1), B1227 (05)

- Title: DTC B1227 (A-A1), B1227 (05)
- Source path: `pages\11332.html`
- Chunk ID: `chunk_b820292155db`
- Images: `images\GHH409278.jpeg`, `images\GHH409279.jpeg`
- Duplicate sources: `pages\13074.html`

### Full Text

````text
No. 12 Test point 2 Outside air temperature sensor 2P connector No. 2 L15BA/K20C1/L15BY engine Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 Outside air temperature sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SENSOR COM wire is OK. Go to step 4. NO Repair an open in the SENSOR COM wire.

-1. Check for continuity between test points 1 and 2.

L15B7/K20C2 engine

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | Outside air temperature sensor 2P connector No. 2

L15BA/K20C1/L15BY engine

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | Outside air temperature sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SENSOR COM wire is OK. Go to step 4.

NO

Repair an open in the SENSOR COM wire.

- Shorted wire check (TAM line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 11 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the TAM wire. NO The TAM wire is OK. Go to step 5.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 11

Test point 2 | Body ground

Is there any voltage?

YES

Repair a short to power in the TAM wire.

NO

The TAM wire is OK. Go to step 5.

- Outside air temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the outside air temperature sensor . Is the outside air temperature sensor OK? YES Replace the climate control unit . NO Replace the outside air temperature sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the outside air temperature sensor .

Is the outside air temperature sensor OK?

YES

Replace the climate control unit .

NO

Replace the outside air temperature sensor .
````

## Chunk 8746: DTC B1228 (A-A2), B1228 (06)

- Title: DTC B1228 (A-A2), B1228 (06)
- Source path: `pages\11333.html`
- Chunk ID: `chunk_ab98697b4f9b`
- Images: none
- Duplicate sources: `pages\13075.html`

### Full Text

````text
# DTC B1228 (A-A2), B1228 (06)

DTC B1228 or DTC screen A-A2 or DTC indicator 06 : A Short in the Outside Air Temperature Sensor Circuit

DTC Description | DTC

B1228 A short in the outside air temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1228 A short in the outside air temperature sensor circuit Is DTC B1228 or Error on the DTC screen A-A2 (climate control panel without display) or 06 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the outside air temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1228 A short in the outside air temperature sensor circuit

Is DTC B1228 or Error on the DTC screen A-A2 (climate control panel without display) or 06 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the outside air temperature sensor circuit.

- Shorted wire check (TAM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector A (32P) Outside air temperature sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 11 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TAM wire. NO The TAM wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector A (32P)

Outside air temperature sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 11

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TAM wire.

NO

The TAM wire is not shorted. Go to step 3.

- Shorted wire check (TAM line to SENSOR COM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Outside air temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 11 Test point 2 Climate control unit connector A (32P) No. 12 Is there continuity? YES Repair a short in the TAM wire to SENSOR COM wire. NO The TAM wire and SENSOR COM wire are OK. Go to step 4.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Outside air temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 11

Test point 2 | Climate control unit connector A (32P) No. 12

Is there continuity?

YES

Repair a short in the TAM wire to SENSOR COM wire.

NO

The TAM wire and SENSOR COM wire are OK. Go to step 4.

- Outside air temperature sensor check -1. Test the outside air temperature sensor . Is the outside air temperature sensor OK? YES Replace the climate control unit . NO Replace the outside air temperature sensor .

-1. Test the outside air temperature sensor .

Is the outside air temperature sensor OK?

YES

Replace the climate control unit .

NO

Replace the outside air temperature sensor .
````

## Chunk 8747: DTC B1231 (A-A5), B1231 (09)

- Title: DTC B1231 (A-A5), B1231 (09)
- Source path: `pages\11334.html`
- Chunk ID: `chunk_6998a47598f1`
- Images: `images\GHH409280.jpeg`, `images\GHH409281.jpeg`, `images\GHH409282.jpeg`
- Duplicate sources: `pages\13076.html`

### Full Text

````text
# DTC B1231 (A-A5), B1231 (09)

DTC B1231 or DTC screen A-A5 or DTC indicator 09 : An Open in the Evaporator Temperature Sensor Circuit

DTC Description | DTC

B1231 An open in the evaporator temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1231 An open in the evaporator temperature sensor circuit Is DTC B1231 or Error on the DTC screen A-A5 (climate control panel without display) or 09 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the evaporator temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1231 An open in the evaporator temperature sensor circuit

Is DTC B1231 or Error on the DTC screen A-A5 (climate control panel without display) or 09 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the evaporator temperature sensor circuit.

- Shorted wire check (T-EVA line to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control unit connector B (24P): disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the T-EVA wire. NO The T-EVA wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control unit connector B (24P): disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Body ground

Is there any voltage?

YES

Repair a short to power in the T-EVA wire.

NO

The T-EVA wire is not shorted. Go to step 3.

- Determine possible failure area (climate control unit, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Climate control unit connector B (24P) No. 10 Courtesy of HONDA, U.S.A., INC. Is resistance value within the range? YES Replace the climate control unit . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Climate control unit connector B (24P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is resistance value within the range?

YES

Replace the climate control unit .

NO

Go to step 4.

- Open wire check (T-EVA line) -1. Disconnect the following connector. Evaporator temperature sensor 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Evaporator temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Evaporator temperature sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The T-EVA wire is OK. Go to step 5. NO Repair an open in the T-EVA wire.

-1. Disconnect the following connector.

Evaporator temperature sensor 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Evaporator temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Evaporator temperature sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The T-EVA wire is OK. Go to step 5.

NO

Repair an open in the T-EVA wire.
````

## Chunk 8748: DTC B1231 (A-A5), B1231 (09)

- Title: DTC B1231 (A-A5), B1231 (09)
- Source path: `pages\11334.html`
- Chunk ID: `chunk_69c57663b9d5`
- Images: `images\GHH409280.jpeg`, `images\GHH409281.jpeg`, `images\GHH409282.jpeg`
- Duplicate sources: `pages\13076.html`

### Full Text

````text
oint 1 Climate control unit connector B (24P) No. 8 Test point 2 Evaporator temperature sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The T-EVA wire is OK. Go to step 5. NO Repair an open in the T-EVA wire.

-1. Disconnect the following connector.

Evaporator temperature sensor 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Evaporator temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Evaporator temperature sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The T-EVA wire is OK. Go to step 5.

NO

Repair an open in the T-EVA wire.

- Open wire check (SENS COM-H line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Evaporator temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 10 Test point 2 Evaporator temperature sensor 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the evaporator temperature sensor . NO Repair an open in the SENS COM-H wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Evaporator temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 10

Test point 2 | Evaporator temperature sensor 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the evaporator temperature sensor .

NO

Repair an open in the SENS COM-H wire.
````

## Chunk 8749: DTC B1232 (A-A6), B1232 (0A)

- Title: DTC B1232 (A-A6), B1232 (0A)
- Source path: `pages\11335.html`
- Chunk ID: `chunk_6e1b0237b0ed`
- Images: `images\GHH409283.jpeg`
- Duplicate sources: `pages\13077.html`

### Full Text

````text
# DTC B1232 (A-A6), B1232 (0A)

DTC B1232 or DTC screen A-A6 or DTC indicator 0A : A Short in the Evaporator Temperature Sensor Circuit

DTC Description | DTC

B1232 A short in the evaporator temperature sensor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1232 A short in the evaporator temperature sensor circuit Is DTC B1232 or Error on the DTC screen A-A6 (climate control panel without display) or 0A (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the evaporator temperature sensor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1232 A short in the evaporator temperature sensor circuit

Is DTC B1232 or Error on the DTC screen A-A6 (climate control panel without display) or 0A (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the evaporator temperature sensor circuit.

- Shorted wire check (T-EVA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the T-EVA wire. NO The T-EVA wire is not shorted. Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the T-EVA wire.

NO

The T-EVA wire is not shorted. Go to step 3.

- Determine possible failure area (climate control unit, others) -1. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Climate control unit connector B (24P) No. 10 Courtesy of HONDA, U.S.A., INC. Is resistance value within the range? YES Replace the climate control unit . NO Go to step 4.

-1. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Climate control unit connector B (24P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is resistance value within the range?

YES

Replace the climate control unit .

NO

Go to step 4.

- Shorted wire check (T-EVA line to SENS COM-H line) -1. Disconnect the following connector. Evaporator temperature sensor 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Evaporator temperature sensor 2P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 8 Test point 2 Climate control unit connector B (24P) No. 10 Is there continuity? YES Repair a short in the T-EVA wire to SENS COM-H wire. NO Replace the evaporator temperature sensor .

-1. Disconnect the following connector.

Evaporator temperature sensor 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Evaporator temperature sensor 2P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 8

Test point 2 | Climate control unit connector B (24P) No. 10

Is there continuity?

YES

Repair a short in the T-EVA wire to SENS COM-H wire.

NO

Replace the evaporator temperature sensor .
````

## Chunk 8750: DTC B1233 (B-A1), B1233 (40)

- Title: DTC B1233 (B-A1), B1233 (40)
- Source path: `pages\11336.html`
- Chunk ID: `chunk_183007b0a275`
- Images: `images\GHH409284.jpeg`, `images\GHH409285.jpeg`
- Duplicate sources: `pages\13078.html`

### Full Text

````text
# DTC B1233 (B-A1), B1233 (40)

DTC B1233 or DTC screen B-A1 or DTC indicator 40 : An Open in the Air Mix Control Motor Circuit (Driver's)

DTC Description | DTC

B1233 An open in the air mix control motor circuit (driver's)

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1233 An open in the air mix control motor circuit (driver's) Is DTC B1233 or Error on the DTC screen B-A1 (climate control panel without display) or 40 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1233 An open in the air mix control motor circuit (driver's)

Is DTC B1233 or Error on the DTC screen B-A1 (climate control panel without display) or 40 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

- Determine possible failure area (AMD-P-DR line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Air mix control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Air mix control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The AMD-P-DR wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Air mix control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Air mix control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The AMD-P-DR wire is OK. Go to step 3.

NO

Go to step 4.

- Open wire check (SENS COM-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Air mix control motor 5P connector No. 4 Test point 2 Air mix control motor 5P connector No. 5 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the air mix control motor . NO Repair an open in the SENS COM-H wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Air mix control motor 5P connector No. 4

Test point 2 | Air mix control motor 5P connector No. 5

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the air mix control motor .

NO

Repair an open in the SENS COM-H wire.

- Open wire check (AMD-P-DR line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 2 Test point 2 Body ground Is there about 5 V? YES Repair an open in the AMD-P-DR wire. NO Replace the climate control unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 2

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the AMD-P-DR wire.

NO

Replace the climate control unit .
````

## Chunk 8751: DTC B1234 (B-A2), B1234 (41)

- Title: DTC B1234 (B-A2), B1234 (41)
- Source path: `pages\11337.html`
- Chunk ID: `chunk_02e2e3e00100`
- Images: `images\GHH409286.jpeg`, `images\GHH409287.jpeg`
- Duplicate sources: `pages\13079.html`

### Full Text

````text
# DTC B1234 (B-A2), B1234 (41)

DTC B1234 or DTC screen B-A2 or DTC indicator 41 : A Short in the Air Mix Control Motor Circuit (Driver's)

NOTE: If other short circuit DTCs are indicated at the same time, there may be an open or short to body ground in the power (5 V) circuit.

DTC Description | DTC

B1234 A short in the air mix control motor circuit (driver's)

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1234 A short in the air mix control motor circuit (driver's) Is DTC B1234 or Error on the DTC screen B-A2 (climate control panel without display) or 41 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1234 A short in the air mix control motor circuit (driver's)

Is DTC B1234 or Error on the DTC screen B-A2 (climate control panel without display) or 41 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

- Determine possible failure area (S5V-H line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Air mix control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Air mix control motor 5P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The S5V-H wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Air mix control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Air mix control motor 5P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The S5V-H wire is OK. Go to step 3.

NO

Go to step 4.

- Determine possible failure area (air mix control motor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Air mix control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the air mix control motor . NO Go to step 6.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Air mix control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the air mix control motor .

NO

Go to step 6.

- Open wire check (S5V-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there about 5 V? YES Repair an open in the S5V-H wire. NO The S5V-H wire is not open. Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

The S5V-H wire is not open. Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire. NO Replace the climate control unit .

-1.
````

## Chunk 8752: DTC B1234 (B-A2), B1234 (41)

- Title: DTC B1234 (B-A2), B1234 (41)
- Source path: `pages\11337.html`
- Chunk ID: `chunk_ee60a9fcc98d`
- Images: `images\GHH409286.jpeg`, `images\GHH409287.jpeg`
- Duplicate sources: `pages\13079.html`

### Full Text

````text
mode

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

The S5V-H wire is not open. Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the S5V-H wire.

NO

Replace the climate control unit .

- Shorted wire check (AMD-P-DR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 2 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the AMD-P-DR wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 2

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the AMD-P-DR wire.

NO

Replace the climate control unit .
````

## Chunk 8753: DTC B1235 (B-A3), B1235 (42)

- Title: DTC B1235 (B-A3), B1235 (42)
- Source path: `pages\11338.html`
- Chunk ID: `chunk_041c85353d6e`
- Images: `images\GHH409288.jpeg`, `images\GHH409289.jpeg`
- Duplicate sources: `pages\13080.html`

### Full Text

````text
# DTC B1235 (B-A3), B1235 (42)

DTC B1235 or DTC screen B-A3 or DTC indicator 42 : A Problem in the Air Mix Control Motor Circuit, Linkage, Door, or Motor (Driver's)

DTC Description | DTC

B1235 A problem in the air mix control motor circuit, linkage, door, or motor (driver's)

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1235 A problem in the air mix control motor circuit, linkage, door, or motor (driver's) Is DTC B1235 or Error on the DTC screen B-A3 (climate control panel without display) or 42 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1235 A problem in the air mix control motor circuit, linkage, door, or motor (driver's)

Is DTC B1235 or Error on the DTC screen B-A3 (climate control panel without display) or 42 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the air mix control motor circuit.

- Open wire check (M-HOT-DR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector B (24P) Air mix control motor 5P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 13 Test point 2 Air mix control motor 5P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-HOT-DR wire is not open. Go to step 3. NO Repair an open in the M-HOT-DR wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector B (24P)

Air mix control motor 5P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 13

Test point 2 | Air mix control motor 5P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-HOT-DR wire is not open. Go to step 3.

NO

Repair an open in the M-HOT-DR wire.

- Open wire check (M-COOL-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 14 Test point 2 Air mix control motor 5P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-COOL-DR wire is not open. Go to step 4. NO Repair an open in the M-COOL-DR wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 14

Test point 2 | Air mix control motor 5P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-COOL-DR wire is not open. Go to step 4.

NO

Repair an open in the M-COOL-DR wire.

- Shorted wire check (M-HOT-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 13 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-HOT-DR wire. NO The M-HOT-DR wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 13

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-HOT-DR wire.
````

## Chunk 8754: DTC B1235 (B-A3), B1235 (42)

- Title: DTC B1235 (B-A3), B1235 (42)
- Source path: `pages\11338.html`
- Chunk ID: `chunk_3b60e9a61862`
- Images: `images\GHH409288.jpeg`, `images\GHH409289.jpeg`
- Duplicate sources: `pages\13080.html`

### Full Text

````text
e.

- Shorted wire check (M-HOT-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 13 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-HOT-DR wire. NO The M-HOT-DR wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 13

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-HOT-DR wire.

NO

The M-HOT-DR wire is OK. Go to step 5.

- Shorted wire check (M-COOL-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-COOL-DR wire. NO The M-COOL-DR wire is OK. Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 14

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-COOL-DR wire.

NO

The M-COOL-DR wire is OK. Go to step 6.

- Air mix control motor check -1. Test the air mix control motor . Is the air mix control motor OK? YES Replace the climate control unit . NO Replace the air mix control motor , or repair the air mix control linkage or door.

-1. Test the air mix control motor .

Is the air mix control motor OK?

YES

Replace the climate control unit .

NO

Replace the air mix control motor , or repair the air mix control linkage or door.
````

## Chunk 8755: DTC B1236 (B-A4)

- Title: DTC B1236 (B-A4)
- Source path: `pages\11339.html`
- Chunk ID: `chunk_594af01d32b0`
- Images: `images\GHH409290.jpeg`, `images\GHH409291.jpeg`
- Duplicate sources: `pages\13081.html`

### Full Text

````text
# DTC B1236 (B-A4)

DTC B1236 or DTC screen B-A4 : An Open in the Passenger's Air Mix Control Motor Circuit

DTC Description | DTC

B1236 An open in the passenger's air mix control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1236 An open in the passenger's air mix control motor circuit Is DTC B1236 or Error on the DTC screen B-A4 indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1236 An open in the passenger's air mix control motor circuit

Is DTC B1236 or Error on the DTC screen B-A4 indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

- Determine possible failure area (AMD-P-AS line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's air mix control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Passenger's air mix control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The AMD-P-AS wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Passenger's air mix control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Passenger's air mix control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The AMD-P-AS wire is OK. Go to step 3.

NO

Go to step 4.

- Open wire check (SENS COM-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Passenger's air mix control motor 5P connector No. 3 Test point 2 Passenger's air mix control motor 5P connector No. 4 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the passenger's air mix control motor . NO Repair an open in the SENS COM-H wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Passenger's air mix control motor 5P connector No. 3

Test point 2 | Passenger's air mix control motor 5P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the passenger's air mix control motor .

NO

Repair an open in the SENS COM-H wire.

- Open wire check (AMD-P-AS line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 3 Test point 2 Body ground Is there about 5 V? YES Repair an open in the AMD-P-AS wire. NO Replace the climate control unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 3

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the AMD-P-AS wire.

NO

Replace the climate control unit .
````

## Chunk 8756: DTC B1237 (B-A5)

- Title: DTC B1237 (B-A5)
- Source path: `pages\11340.html`
- Chunk ID: `chunk_e035b630e8c8`
- Images: `images\GHH409292.jpeg`, `images\GHH409293.jpeg`
- Duplicate sources: `pages\13082.html`

### Full Text

````text
# DTC B1237 (B-A5)

DTC B1237 or DTC screen B-A5 : A Short in the Passenger's Air Mix Control Motor Circuit

NOTE: If other short circuit DTCs are indicated at the same time, there may be an open or short to body ground in the power (5 V) circuit.

DTC Description | DTC

B1237 A short in the passenger's air mix control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1237 A short in the passenger's air mix control motor circuit Is DTC B1237 or Error on the DTC screen B-A5 indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1237 A short in the passenger's air mix control motor circuit

Is DTC B1237 or Error on the DTC screen B-A5 indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

- Determine possible failure area (S5V-H line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's air mix control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Passenger's air mix control motor 5P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The S5V-H wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Passenger's air mix control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Passenger's air mix control motor 5P connector No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The S5V-H wire is OK. Go to step 3.

NO

Go to step 4.

- Determine possible failure area (passenger's air mix control motor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Passenger's air mix control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the passenger's air mix control motor . NO Go to step 6.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Passenger's air mix control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the passenger's air mix control motor .

NO

Go to step 6.

- Open wire check (S5V-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there about 5 V? YES Repair an open in the S5V-H wire. NO The S5V-H wire is not open. Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

The S5V-H wire is not open. Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire.
````

## Chunk 8757: DTC B1237 (B-A5)

- Title: DTC B1237 (B-A5)
- Source path: `pages\11340.html`
- Chunk ID: `chunk_e8915f44fea5`
- Images: `images\GHH409292.jpeg`, `images\GHH409293.jpeg`
- Duplicate sources: `pages\13082.html`

### Full Text

````text
ition | Vehicle ON mode

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the S5V-H wire.

NO

The S5V-H wire is not open. Go to step 5.

- Shorted wire check (S5V-H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the S5V-H wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the S5V-H wire.

NO

Replace the climate control unit .

- Shorted wire check (AMD-P-AS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector B (24P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 3 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the AMD-P-AS wire. NO Replace the climate control unit .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector B (24P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 3

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the AMD-P-AS wire.

NO

Replace the climate control unit .
````

## Chunk 8758: DTC B1238 (B-A6)

- Title: DTC B1238 (B-A6)
- Source path: `pages\11341.html`
- Chunk ID: `chunk_0693f769d03e`
- Images: `images\GHH409294.jpeg`, `images\GHH409295.jpeg`
- Duplicate sources: `pages\13083.html`

### Full Text

````text
# DTC B1238 (B-A6)

DTC B1238 or DTC screen B-A6 : A Problem in the Passenger's Air Mix Control Motor Circuit, Linkage, Door, or Motor

DTC Description | DTC

B1238 A problem in the passenger's air mix control motor circuit, linkage, door, or motor

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1238 A problem in the passenger's air mix control motor circuit, linkage, door, or motor Is DTC B1238 or Error on the DTC screen B-A6 indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1238 A problem in the passenger's air mix control motor circuit, linkage, door, or motor

Is DTC B1238 or Error on the DTC screen B-A6 indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the passenger's air mix control motor circuit.

- Open wire check (M-HOT-AS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector B (24P) Passenger's air mix control motor 5P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 15 Test point 2 Passenger's air mix control motor 5P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-HOT-AS wire is not open. Go to step 3. NO Repair an open in the M-HOT-AS wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector B (24P)

Passenger's air mix control motor 5P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 15

Test point 2 | Passenger's air mix control motor 5P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-HOT-AS wire is not open. Go to step 3.

NO

Repair an open in the M-HOT-AS wire.

- Open wire check (M-COOL-AS line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 16 Test point 2 Passenger's air mix control motor 5P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-COOL-AS wire is not open. Go to step 4. NO Repair an open in the M-COOL-AS wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 16

Test point 2 | Passenger's air mix control motor 5P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-COOL-AS wire is not open. Go to step 4.

NO

Repair an open in the M-COOL-AS wire.

- Shorted wire check (M-HOT-AS line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-HOT-AS wire. NO The M-HOT-AS wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-HOT-AS wire.

NO

The M-HOT-AS wire is OK.
````

## Chunk 8759: DTC B1238 (B-A6)

- Title: DTC B1238 (B-A6)
- Source path: `pages\11341.html`
- Chunk ID: `chunk_8402ebd569b7`
- Images: `images\GHH409294.jpeg`, `images\GHH409295.jpeg`
- Duplicate sources: `pages\13083.html`

### Full Text

````text
r continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-HOT-AS wire. NO The M-HOT-AS wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-HOT-AS wire.

NO

The M-HOT-AS wire is OK. Go to step 5.

- Shorted wire check (M-COOL-AS line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Passenger's air mix control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-COOL-AS wire. NO The M-COOL-AS wire is OK. Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Passenger's air mix control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-COOL-AS wire.

NO

The M-COOL-AS wire is OK. Go to step 6.

- Passenger's air mix control motor check -1. Test the passenger's air mix control motor check . Is the passenger's air mix control motor OK? YES Replace the climate control unit . NO Replace the passenger's air mix control motor , or repair the passenger's air mix control linkage or door.

-1. Test the passenger's air mix control motor check .

Is the passenger's air mix control motor OK?

YES

Replace the climate control unit .

NO

Replace the passenger's air mix control motor , or repair the passenger's air mix control linkage or door.
````

## Chunk 8760: DTC B123F (A-A3), B123F (17)

- Title: DTC B123F (A-A3), B123F (17)
- Source path: `pages\11342.html`
- Chunk ID: `chunk_68832766c76a`
- Images: `images\GHH409296.jpeg`, `images\GHH409297.jpeg`
- Duplicate sources: `pages\13084.html`

### Full Text

````text
# DTC B123F (A-A3), B123F (17)

DTC B123F, DTC screen A-A3, or DTC indicator 17 : Automatic Lighting Control Unit/Sunlight Sensor Error

NOTE: DTC screen A-A3 *1, D-A1 *1, and D-A2 *1 are for climate control panel without display, DTC indicator 17 *2, 80 *2, and 83 *2 are for climate control panel with display.

DTC Description | DTC

B123F Automatic lighting control unit/sunlight sensor error

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B123F Automatic lighting control unit/sunlight sensor error Is DTC B123F, Error on the DTC screen A-A3 *1, or DTC indicator 17 *2 indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B123F Automatic lighting control unit/sunlight sensor error

Is DTC B123F, Error on the DTC screen A-A3 *1, or DTC indicator 17 *2 indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time.

- Equipment check 1 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Confirm the vehicle have an automatic lighting system. Does the combination light switch have an AUTO position? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Confirm the vehicle have an automatic lighting system.

Does the combination light switch have an AUTO position?

YES

Go to step 3.

NO

Go to step 4.

- Equipment check 2 -1. Confirm the vehicle have an automatic wiper system. Does the wiper/washer switch have an AUTO position? YES Go to step 4. NO Go to step 9.

-1. Confirm the vehicle have an automatic wiper system.

Does the wiper/washer switch have an AUTO position?

YES

Go to step 4.

NO

Go to step 9.

- Open wire check (TSUN line) -1. Disconnect the following connectors. Climate control unit connector A (32P) Sunlight sensor 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Sunlight sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 10 Test point 2 Sunlight sensor 2P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TSUN wire is not open. Go to step 5. NO Repair an open in the TSUN wire.

-1. Disconnect the following connectors.

Climate control unit connector A (32P)

Sunlight sensor 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Sunlight sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 10

Test point 2 | Sunlight sensor 2P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TSUN wire is not open. Go to step 5.

NO

Repair an open in the TSUN wire.

- Open wire check (SENSOR COM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Sunlight sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 12 Test point 2 Sunlight sensor 2P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SENSOR COM wire is OK. Go to step 6. NO Repair an open in the SENSOR COM wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Sunlight sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | Sunlight sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SENSOR COM wire is OK. Go to step 6.

NO

Repair an open in the SENSOR COM wire.

- Shorted wire check (TSUN line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Sunlight sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 10 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the TSUN wire.
````

## Chunk 8761: DTC B123F (A-A3), B123F (17)

- Title: DTC B123F (A-A3), B123F (17)
- Source path: `pages\11342.html`
- Chunk ID: `chunk_a0f2e3c145bc`
- Images: `images\GHH409296.jpeg`, `images\GHH409297.jpeg`
- Duplicate sources: `pages\13084.html`

### Full Text

````text
test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Sunlight sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 12

Test point 2 | Sunlight sensor 2P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SENSOR COM wire is OK. Go to step 6.

NO

Repair an open in the SENSOR COM wire.

- Shorted wire check (TSUN line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Sunlight sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 10 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the TSUN wire. NO The TSUN wire is not shorted. Go to step 7.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Sunlight sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 10

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the TSUN wire.

NO

The TSUN wire is not shorted. Go to step 7.

- Shorted wire check (TSUN line to SENSOR COM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Sunlight sensor 2P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 10 Test point 2 Climate control unit connector A (32P) No. 12 Is there continuity? YES Repair a short in the TSUN wire to the SENSOR COM wire. NO The TSUN wire and the SENSOR COM wire are OK. Go to step 8.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Sunlight sensor 2P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 10

Test point 2 | Climate control unit connector A (32P) No. 12

Is there continuity?

YES

Repair a short in the TSUN wire to the SENSOR COM wire.

NO

The TSUN wire and the SENSOR COM wire are OK. Go to step 8.

- Sunlight sensor check -1. Reconnect the following connectors. Climate control unit connector A (32P) Sunlight sensor 2P connector -2. Test the sunlight sensor . Is the sunlight sensor OK? YES Replace the climate control unit . NO Replace the sunlight sensor .

-1. Reconnect the following connectors.

Climate control unit connector A (32P)

Sunlight sensor 2P connector

-2. Test the sunlight sensor .

Is the sunlight sensor OK?

YES

Replace the climate control unit .

NO

Replace the sunlight sensor .

- Fuse check: NOTE: Check for DTCs. If a DTC U1280, Error on the DTC screen D-A1 *1, or DTC indicator 80 *2 indicated, troubleshoot the DTC first.-1. Check the following fuse. Fuse No. A18 Is the fuse OK? YES Go to step 10. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A18 fuse circuit.

NOTE: Check for DTCs. If a DTC U1280, Error on the DTC screen D-A1 *1, or DTC indicator 80 *2 indicated, troubleshoot the DTC first.-1.

Check the following fuse.

Fuse | No. A18

Is the fuse OK?

YES

Go to step 10.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A18 fuse circuit.

- Determine possible failure area (B-CAN lines, others) -1. Disconnect the following connector. Automatic lighting control unit-sensor 5P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Automatic lighting control unit-sensor 5P connector: disconnected Test point 1 Automatic lighting control unit-sensor 5P connector No. 3 Test point 2 Automatic lighting control unit-sensor 5P connector No. 4 Is there battery voltage? YES Go to step 11. NO Go to step 14.

-1. Disconnect the following connector.

Automatic lighting control unit-sensor 5P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Automatic lighting control unit-sensor 5P connector: disconnected

Test point 1 | Automatic lighting control unit-sensor 5P connector No. 3

Test point 2 | Automatic lighting control unit-sensor 5P connector No. 4

Is there battery voltage?

YES

Go to step 11.

NO

Go to step 14.

- Open wire check (B-CAN_H line) -1. Disconnect the following connector. Climate control unit connector A (32P) -2.
````

## Chunk 8762: DTC B123F (A-A3), B123F (17)

- Title: DTC B123F (A-A3), B123F (17)
- Source path: `pages\11342.html`
- Chunk ID: `chunk_fdac2957606d`
- Images: `images\GHH409296.jpeg`, `images\GHH409297.jpeg`
- Duplicate sources: `pages\13084.html`

### Full Text

````text
ected Test point 1 Automatic lighting control unit-sensor 5P connector No. 3 Test point 2 Automatic lighting control unit-sensor 5P connector No. 4 Is there battery voltage? YES Go to step 11. NO Go to step 14.

-1. Disconnect the following connector.

Automatic lighting control unit-sensor 5P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Automatic lighting control unit-sensor 5P connector: disconnected

Test point 1 | Automatic lighting control unit-sensor 5P connector No. 3

Test point 2 | Automatic lighting control unit-sensor 5P connector No. 4

Is there battery voltage?

YES

Go to step 11.

NO

Go to step 14.

- Open wire check (B-CAN_H line) -1. Disconnect the following connector. Climate control unit connector A (32P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Automatic lighting control unit-sensor 5P connector: disconnected Climate control unit connector A (32P): disconnected Test point 1 Automatic lighting control unit-sensor 5P connector No. 1 Test point 2 Climate control unit connector A (32P) No. 25 Is there continuity? YES The B-CAN_H wire is OK. Go to step 12. NO Repair an open in the B-CAN_H wire.

-1. Disconnect the following connector.

Climate control unit connector A (32P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Automatic lighting control unit-sensor 5P connector: disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Automatic lighting control unit-sensor 5P connector No. 1

Test point 2 | Climate control unit connector A (32P) No. 25

Is there continuity?

YES

The B-CAN_H wire is OK. Go to step 12.

NO

Repair an open in the B-CAN_H wire.

- Open wire check (B-CAN_L line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Automatic lighting control unit-sensor 5P connector: disconnected Climate control unit connector A (32P): disconnected Test point 1 Automatic lighting control unit-sensor 5P connector No. 2 Test point 2 Climate control unit connector A (32P) No. 8 Is there continuity? YES The B-CAN_L wire is OK. Go to step 13. NO Repair an open in the B-CAN_L wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Automatic lighting control unit-sensor 5P connector: disconnected

Climate control unit connector A (32P): disconnected

Test point 1 | Automatic lighting control unit-sensor 5P connector No. 2

Test point 2 | Climate control unit connector A (32P) No. 8

Is there continuity?

YES

The B-CAN_L wire is OK. Go to step 13.

NO

Repair an open in the B-CAN_L wire.

- DTC check -1. Reconnect the following connectors. Automatic lighting control unit-sensor 5P connector Climate control unit connector A (32P) -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode then the ON mode. -4. Wait for at least 8 seconds. -5. Do the Self-Diagnostic Function with the climate control unit . -6. Check for DTCs. DTC Description DTC B123F Automatic lighting control unit/sunlight sensor error U128D Climate control unit lost communication with gauge control module Are DTC B123F, Error on the DTC screen A-A3 *1, or DTC indicator 17 *2 and DTC U128D, Error on the DTC screen D-A2 *1, or DTC indicator 83 *2 indicated? YES Replace the climate control unit . NO Replace the automatic lighting control unit-sensor .

-1. Reconnect the following connectors.

Automatic lighting control unit-sensor 5P connector

Climate control unit connector A (32P)

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode then the ON mode.

-4. Wait for at least 8 seconds.

-5. Do the Self-Diagnostic Function with the climate control unit .

-6. Check for DTCs.

DTC Description | DTC

B123F Automatic lighting control unit/sunlight sensor error

U128D Climate control unit lost communication with gauge control module

Are DTC B123F, Error on the DTC screen A-A3 *1, or DTC indicator 17 *2 and DTC U128D, Error on the DTC screen D-A2 *1, or DTC indicator 83 *2 indicated?

YES

Replace the climate control unit .

NO

Replace the automatic lighting control unit-sensor .

- Open wire check (+B BACK UP line) -1. Measure the voltage between test points 1 and 2.
````

## Chunk 8763: DTC B123F (A-A3), B123F (17)

- Title: DTC B123F (A-A3), B123F (17)
- Source path: `pages\11342.html`
- Chunk ID: `chunk_5c65527cdbec`
- Images: `images\GHH409296.jpeg`, `images\GHH409297.jpeg`
- Duplicate sources: `pages\13084.html`

### Full Text

````text
ighting control unit-sensor 5P connector

Climate control unit connector A (32P)

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode then the ON mode.

-4. Wait for at least 8 seconds.

-5. Do the Self-Diagnostic Function with the climate control unit .

-6. Check for DTCs.

DTC Description | DTC

B123F Automatic lighting control unit/sunlight sensor error

U128D Climate control unit lost communication with gauge control module

Are DTC B123F, Error on the DTC screen A-A3 *1, or DTC indicator 17 *2 and DTC U128D, Error on the DTC screen D-A2 *1, or DTC indicator 83 *2 indicated?

YES

Replace the climate control unit .

NO

Replace the automatic lighting control unit-sensor .

- Open wire check (+B BACK UP line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Automatic lighting control unit-sensor 5P connector: disconnected Test point 1 Automatic lighting control unit-sensor 5P connector No. 4 Test point 2 Body ground Is there battery voltage? YES: L15B7/K20C2 engine Check for an open in the GND wire between the automatic lighting control unit-sensor and body ground. If the wire is OK, check for poor ground at G505. YES: L15BA/K20C1/L15BY engine Check for an open in the GND wire between the automatic lighting control unit-sensor and body ground. If the wire is OK, check for poor ground at G503. NO Repair an open in the +B BACK UP wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Automatic lighting control unit-sensor 5P connector: disconnected

Test point 1 | Automatic lighting control unit-sensor 5P connector No. 4

Test point 2 | Body ground

Is there battery voltage?

YES: L15B7/K20C2 engine

Check for an open in the GND wire between the automatic lighting control unit-sensor and body ground. If the wire is OK, check for poor ground at G505.

YES: L15BA/K20C1/L15BY engine

Check for an open in the GND wire between the automatic lighting control unit-sensor and body ground. If the wire is OK, check for poor ground at G503.

NO

Repair an open in the +B BACK UP wire.
````

## Chunk 8764: DTC B1240 (B-B6), B1240 (4B)

- Title: DTC B1240 (B-B6), B1240 (4B)
- Source path: `pages\11343.html`
- Chunk ID: `chunk_2dc9fd6c6cda`
- Images: `images\GHH409298.jpeg`, `images\GHH409299.jpeg`
- Duplicate sources: `pages\13085.html`

### Full Text

````text
# DTC B1240 (B-B6), B1240 (4B)

DTC B1240 or DTC screen B-B6 or DTC indicator 4b : A Problem in the Mode Control Motor Circuit, Linkage, Door, or Motor

DTC Description | DTC

B1240 A problem in the mode control motor circuit, linkage, door, or motor

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1240 A problem in the mode control motor circuit, linkage, door, or motor Is DTC B1240 or Error on the DTC screen B-B6 (climate control panel without display) or 4b (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1240 A problem in the mode control motor circuit, linkage, door, or motor

Is DTC B1240 or Error on the DTC screen B-B6 (climate control panel without display) or 4b (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the mode control motor circuit.

- Open wire check (M-DEF-DR line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector B (24P) Mode control motor 5P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 20 Test point 2 Mode control motor 5P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-DEF-DR wire is not open. Go to step 3. NO Repair an open in the M-DEF-DR wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector B (24P)

Mode control motor 5P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 20

Test point 2 | Mode control motor 5P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-DEF-DR wire is not open. Go to step 3.

NO

Repair an open in the M-DEF-DR wire.

- Open wire check (M-VENT-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 19 Test point 2 Mode control motor 5P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-VENT-DR wire is not open. Go to step 4. NO Repair an open in the M-VENT-DR wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 19

Test point 2 | Mode control motor 5P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-VENT-DR wire is not open. Go to step 4.

NO

Repair an open in the M-VENT-DR wire.

- Shorted wire check (M-DEF-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-DEF-DR wire. NO The M-DEF-DR wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-DEF-DR wire.

NO

The M-DEF-DR wire is OK. Go to step 5.

- Shorted wire check (M-VENT-DR line) -1.
````

## Chunk 8765: DTC B1240 (B-B6), B1240 (4B)

- Title: DTC B1240 (B-B6), B1240 (4B)
- Source path: `pages\11343.html`
- Chunk ID: `chunk_77a6de39a320`
- Images: `images\GHH409298.jpeg`, `images\GHH409299.jpeg`
- Duplicate sources: `pages\13085.html`

### Full Text

````text
oints 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-DEF-DR wire. NO The M-DEF-DR wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-DEF-DR wire.

NO

The M-DEF-DR wire is OK. Go to step 5.

- Shorted wire check (M-VENT-DR line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Mode control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 19 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-VENT-DR wire. NO The M-VENT-DR wire is OK. Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Mode control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 19

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-VENT-DR wire.

NO

The M-VENT-DR wire is OK. Go to step 6.

- Mode control motor check -1. Test the mode control motor . Is the mode control motor OK? YES Replace the climate control unit . NO Replace the mode control motor , or repair the mode control linkage or door.

-1. Test the mode control motor .

Is the mode control motor OK?

YES

Replace the climate control unit .

NO

Replace the mode control motor , or repair the mode control linkage or door.
````

## Chunk 8766: DTC B1241 (C-A7), B1241 (59)

- Title: DTC B1241 (C-A7), B1241 (59)
- Source path: `pages\11344.html`
- Chunk ID: `chunk_b83f0c566757`
- Images: `images\GHH409300.jpeg`, `images\GHH409301.jpeg`, `images\GHH409302.jpeg`, `images\GHH409303.jpeg`, `images\GHH409304.jpeg`, `images\GHH409305.jpeg`, `images\GHH409306.jpeg`, `images\GHH409307.jpeg`, `images\GHH409308.jpeg`
- Duplicate sources: `pages\13086.html`

### Full Text

````text
# DTC B1241 (C-A7), B1241 (59)

DTC B1241, DTC screen C-A7, or DTC indicator 59 : A Problem in the Blower Motor Circuit

DTC Description | DTC

B1241 A problem in the blower motor circuit

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B1241 A problem in the blower motor circuit Is DTC B1241, Error on the DTC screen C-A7 (climate control panel without display), or DTC indicator 59 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the blower motor circuit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B1241 A problem in the blower motor circuit

Is DTC B1241, Error on the DTC screen C-A7 (climate control panel without display), or DTC indicator 59 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the blower motor circuit.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A3-1 Is the fuse OK? YES Go to step 3. NO Replace the fuse, and recheck. If fuse blows again, repair a short in the No. A3-1 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A3-1

Is the fuse OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If fuse blows again, repair a short in the No. A3-1 fuse circuit.

- Blower motor power circuit check -1. Disconnect the following connector. Blower motor 2P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Blower motor 2P connector: disconnected Test point 1 Blower motor 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 4. NO Go to step 12.

-1. Disconnect the following connector.

Blower motor 2P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Blower motor 2P connector: disconnected

Test point 1 | Blower motor 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 4.

NO

Go to step 12.

- Blower motor operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reconnect the blower motor 2P connector. -3. Connect terminals A and B with a jumper wire. Terminal A Blower motor 2P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. Does the blower motor run at high speed? YES Go to step 5. NO Replace the blower motor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reconnect the blower motor 2P connector.

-3. Connect terminals A and B with a jumper wire.

Terminal A | Blower motor 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

Does the blower motor run at high speed?

YES

Go to step 5.

NO

Replace the blower motor .

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the jumper wire. -3. Disconnect the following connector. Power transistor 4P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Power transistor 4P connector: disconnected Test point 1 Power transistor 4P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 6. NO Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the jumper wire.

-3. Disconnect the following connector.

Power transistor 4P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Power transistor 4P connector: disconnected

Test point 1 | Power transistor 4P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 6.

NO

Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.
````

## Chunk 8767: DTC B1241 (C-A7), B1241 (59)

- Title: DTC B1241 (C-A7), B1241 (59)
- Source path: `pages\11344.html`
- Chunk ID: `chunk_30c7eca48bf1`
- Images: `images\GHH409300.jpeg`, `images\GHH409301.jpeg`, `images\GHH409302.jpeg`, `images\GHH409303.jpeg`, `images\GHH409304.jpeg`, `images\GHH409305.jpeg`, `images\GHH409306.jpeg`, `images\GHH409307.jpeg`, `images\GHH409308.jpeg`
- Duplicate sources: `pages\13086.html`

### Full Text

````text
1 Power transistor 4P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 6. NO Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the jumper wire.

-3. Disconnect the following connector.

Power transistor 4P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Power transistor 4P connector: disconnected

Test point 1 | Power transistor 4P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 6.

NO

Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.

- Open wire check (BLOWER HI line) -1. Connect terminals A and B with a jumper wire. Terminal A Power transistor 4P connector No. 3 Terminal B Power transistor 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -2. Turn the vehicle to the ON mode. Does the blower motor run at high speed? YES The BLOWER HI wire is OK. Go to step 7. NO Repair an open in the BLOWER HI wire.

-1. Connect terminals A and B with a jumper wire.

Terminal A | Power transistor 4P connector No. 3

Terminal B | Power transistor 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-2. Turn the vehicle to the ON mode.

Does the blower motor run at high speed?

YES

The BLOWER HI wire is OK. Go to step 7.

NO

Repair an open in the BLOWER HI wire.

- Shorted wire check (BLOWER V line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the jumper wire. -3. Disconnect the following connector. Climate control unit connector B (24P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Power transistor 4P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 12 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the BLOWER V wire. NO The BLOWER V wire is not shorted. Go to step 8.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the jumper wire.

-3. Disconnect the following connector.

Climate control unit connector B (24P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Power transistor 4P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 12

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BLOWER V wire.

NO

The BLOWER V wire is not shorted. Go to step 8.

- Shorted wire check (BLOWER G line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Power transistor 4P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 11 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the BLOWER G wire. NO The BLOWER G wire is not shorted. Go to step 9.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Power transistor 4P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 11

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BLOWER G wire.

NO

The BLOWER G wire is not shorted. Go to step 9.

- Open wire check (BLOWER V line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Power transistor 4P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 12 Test point 2 Power transistor 4P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BLOWER V wire is OK. Go to step 10. NO Repair an open in the BLOWER V wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Power transistor 4P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 12

Test point 2 | Power transistor 4P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The BLOWER V wire is OK. Go to step 10.

NO

Repair an open in the BLOWER V wire.
````

## Chunk 8768: DTC B1241 (C-A7), B1241 (59)

- Title: DTC B1241 (C-A7), B1241 (59)
- Source path: `pages\11344.html`
- Chunk ID: `chunk_884b58a5afcb`
- Images: `images\GHH409300.jpeg`, `images\GHH409301.jpeg`, `images\GHH409302.jpeg`, `images\GHH409303.jpeg`, `images\GHH409304.jpeg`, `images\GHH409305.jpeg`, `images\GHH409306.jpeg`, `images\GHH409307.jpeg`, `images\GHH409308.jpeg`
- Duplicate sources: `pages\13086.html`

### Full Text

````text
mode Climate control unit connector B (24P): disconnected Power transistor 4P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 12 Test point 2 Power transistor 4P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BLOWER V wire is OK. Go to step 10. NO Repair an open in the BLOWER V wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Power transistor 4P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 12

Test point 2 | Power transistor 4P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The BLOWER V wire is OK. Go to step 10.

NO

Repair an open in the BLOWER V wire.

- Open wire check (BLOWER G line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Power transistor 4P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 11 Test point 2 Power transistor 4P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BLOWER G wire is OK. Go to step 11. NO Repair an open in the BLOWER G wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Power transistor 4P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 11

Test point 2 | Power transistor 4P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The BLOWER G wire is OK. Go to step 11.

NO

Repair an open in the BLOWER G wire.

- Power transistor check -1. Test the power transistor . Is the power transistor OK? YES Replace the climate control unit . NO Replace the power transistor .. NOTE: If the power transistor is faulty, check the blower motor for damage. If necessary, replace the blower motor

-1. Test the power transistor .

Is the power transistor OK?

YES

Replace the climate control unit .

NO

Replace the power transistor ..

NOTE: If the power transistor is faulty, check the blower motor for damage. If necessary, replace the blower motor

- Blower motor relay check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the blower motor relay from the under-hood fuse/relay box, and test it . Is the relay OK? YES Go to step 13. NO Replace the blower motor relay.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the blower motor relay from the under-hood fuse/relay box, and test it .

Is the relay OK?

YES

Go to step 13.

NO

Replace the blower motor relay.

- Open wire check (+B HTR MTR line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Blower motor relay: disconnected Test point 1 Blower motor relay 4P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HTR MTR wire is OK. Go to step 14. NO Repair an open in the +B HTR MTR wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Blower motor relay: disconnected

Test point 1 | Blower motor relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B HTR MTR wire is OK. Go to step 14.

NO

Repair an open in the +B HTR MTR wire.

- Open wire check (IG2 A/C (L15B7/K20C2 engine) or IG2 OPTION (L15BA/K20C1/L15BY engine) line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Blower motor relay: disconnected Test point 1 Blower motor relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 15. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/K20C1/L15BY engine Repair an open in the IG2 OPTION wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Blower motor relay: disconnected

Test point 1 | Blower motor relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 15.

NO: L15B7/K20C2 engine
````

## Chunk 8769: DTC B1241 (C-A7), B1241 (59)

- Title: DTC B1241 (C-A7), B1241 (59)
- Source path: `pages\11344.html`
- Chunk ID: `chunk_6ce5ffd2b95b`
- Images: `images\GHH409300.jpeg`, `images\GHH409301.jpeg`, `images\GHH409302.jpeg`, `images\GHH409303.jpeg`, `images\GHH409304.jpeg`, `images\GHH409305.jpeg`, `images\GHH409306.jpeg`, `images\GHH409307.jpeg`, `images\GHH409308.jpeg`
- Duplicate sources: `pages\13086.html`

### Full Text

````text
est point 1 Blower motor relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 15. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/K20C1/L15BY engine Repair an open in the IG2 OPTION wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Blower motor relay: disconnected

Test point 1 | Blower motor relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 15.

NO: L15B7/K20C2 engine

Repair an open in the IG2 A/C wire.

NO: L15BA/K20C1/L15BY engine

Repair an open in the IG2 OPTION wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Blower motor relay: disconnected Test point 1 Blower motor relay 4P socket No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair an open in the BLOWER MTR wire between the blower motor relay and the blower motor. NO: L15B7/K20C2 engine Check for an open in the GND wire. If the wire is OK, check for poor ground at G301. NO: L15BA/K20C1/L15BY engine Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Blower motor relay: disconnected

Test point 1 | Blower motor relay 4P socket No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair an open in the BLOWER MTR wire between the blower motor relay and the blower motor.

NO: L15B7/K20C2 engine

Check for an open in the GND wire. If the wire is OK, check for poor ground at G301.

NO: L15BA/K20C1/L15BY engine

Check for an open in the GND wire. If the wire is OK, check for poor ground at G305.
````

## Chunk 8770: DTC B2964 (D-B5), B2964 (93)

- Title: DTC B2964 (D-B5), B2964 (93)
- Source path: `pages\11345.html`
- Chunk ID: `chunk_3f81f41aa38b`
- Images: `images\GHH409309.jpeg`, `images\GHH409310.jpeg`, `images\GHH409311.jpeg`
- Duplicate sources: `pages\13087.html`

### Full Text

````text
# DTC B2964 (D-B5), B2964 (93)

DTC B2964, DTC screen D-B5, or DTC indicator 93 : Climate Control Unit Lost Communication with Front Panel (Climate Control Panel)

DTC Description | DTC

B2964 Climate control unit lost communication with front panel (climate control panel)

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B2964 Climate control unit lost communication with front panel (climate control panel) Is DTC B2964, Error on the DTC screen D-B5 (climate control panel without display), or DTC indicator 93 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the climate control panel circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B2964 Climate control unit lost communication with front panel (climate control panel)

Is DTC B2964, Error on the DTC screen D-B5 (climate control panel without display), or DTC indicator 93 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the climate control panel circuit.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B9 Is the fuse OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B9

Is the fuse OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

- Determine possible failure area (BUS-DATA line, others) -1. Disconnect the following connector. Climate control panel 12P connector -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control panel 12P connector: disconnected Test point 1 Climate control panel 12P connector No. 1 Test point 2 Climate control panel 12P connector No. 4 Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 4. NO Go to step 7.

-1. Disconnect the following connector.

Climate control panel 12P connector

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control panel 12P connector: disconnected

Test point 1 | Climate control panel 12P connector No. 1

Test point 2 | Climate control panel 12P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 4.

NO

Go to step 7.

- Shorted wire check (BUS-DATA line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Climate control unit connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Body ground Is there continuity? YES Repair a short to body ground in the BUS-DATA wire. NO The BUS-DATA wire is not shorted. Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Climate control unit connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Climate control panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BUS-DATA wire.

NO

The BUS-DATA wire is not shorted. Go to step 5.

- Open wire check (BUS-DATA line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Climate control panel 12P connector No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BUS-DATA wire is OK. Go to step 6.
````

## Chunk 8771: DTC B2964 (D-B5), B2964 (93)

- Title: DTC B2964 (D-B5), B2964 (93)
- Source path: `pages\11345.html`
- Chunk ID: `chunk_67e5c42d2586`
- Images: `images\GHH409309.jpeg`, `images\GHH409310.jpeg`, `images\GHH409311.jpeg`
- Duplicate sources: `pages\13087.html`

### Full Text

````text
ition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Climate control panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to body ground in the BUS-DATA wire.

NO

The BUS-DATA wire is not shorted. Go to step 5.

- Open wire check (BUS-DATA line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Climate control panel 12P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 29 Test point 2 Climate control panel 12P connector No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The BUS-DATA wire is OK. Go to step 6. NO Repair an open in the BUS-DATA wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Climate control panel 12P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 29

Test point 2 | Climate control panel 12P connector No. 9

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The BUS-DATA wire is OK. Go to step 6.

NO

Repair an open in the BUS-DATA wire.

- Climate control panel check -1. Reconnect the following connector. Climate control unit connector A (32P) -2. Substitute a known-good climate control panel . -3. Clear the DTCs with the HDS. -4. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -5. Do the Self-Diagnostic Function with the HDS or the climate control unit . -6. Check for DTCs. DTC Description DTC B2964 Climate control unit lost communication with front panel (climate control panel) Is DTC B2964, Error on the DTC screen D-B5 (climate control panel without display), or DTC indicator 93 (climate control panel with display) indicated? YES Replace the climate control unit . NO Replace the original climate control panel .

-1. Reconnect the following connector.

Climate control unit connector A (32P)

-2. Substitute a known-good climate control panel .

-3. Clear the DTCs with the HDS.

-4. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-5. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-6. Check for DTCs.

DTC Description | DTC

B2964 Climate control unit lost communication with front panel (climate control panel)

Is DTC B2964, Error on the DTC screen D-B5 (climate control panel without display), or DTC indicator 93 (climate control panel with display) indicated?

YES

Replace the climate control unit .

NO

Replace the original climate control panel .

- Open wire check (IG2 A/C (L15B7/K20C2 engine) or IG2 OPTION (L15BA/K20C1/L15BY engine) line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control panel 12P connector: disconnected Test point 1 Climate control panel 12P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Check for an open in the GND wire between the climate control panel and body ground. If the wire is OK, check for poor ground at G503. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/K20C1/lL15BY engine Repair an open in the IG2 OPTION wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control panel 12P connector: disconnected

Test point 1 | Climate control panel 12P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Check for an open in the GND wire between the climate control panel and body ground. If the wire is OK, check for poor ground at G503.

NO: L15B7/K20C2 engine

Repair an open in the IG2 A/C wire.

NO: L15BA/K20C1/lL15BY engine

Repair an open in the IG2 OPTION wire.
````

## Chunk 8772: DTC B2983 (C-A6), B2983 (57)

- Title: DTC B2983 (C-A6), B2983 (57)
- Source path: `pages\11346.html`
- Chunk ID: `chunk_14117f8470b7`
- Images: `images\GHH409312.jpeg`, `images\GHH409313.jpeg`
- Duplicate sources: `pages\13088.html`

### Full Text

````text
# DTC B2983 (C-A6), B2983 (57)

DTC B2983 or DTC screen C-A6 or DTC indicator 57 : A Problem in the Recirculation Control Motor Circuit, Linkage, Door, or Motor

DTC Description | DTC

B2983 A problem in the recirculation control motor circuit, linkage, door, or motor

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B2983 A problem in the recirculation control motor circuit, linkage, door, or motor Is DTC B2983 or Error on the DTC screen C-A6 (climate control panel without display) or 57 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B2983 A problem in the recirculation control motor circuit, linkage, door, or motor

Is DTC B2983 or Error on the DTC screen C-A6 (climate control panel without display) or 57 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

- Open wire check (M-REC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector B (24P) Recirculation control motor 5P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 17 Test point 2 Recirculation control motor 5P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-REC wire is not open. Go to step 3. NO Repair an open in the M-REC wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector B (24P)

Recirculation control motor 5P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 17

Test point 2 | Recirculation control motor 5P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-REC wire is not open. Go to step 3.

NO

Repair an open in the M-REC wire.

- Open wire check (M-FRS line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 18 Test point 2 Recirculation control motor 5P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The M-FRS wire is not open. Go to step 4. NO Repair an open in the M-FRS wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 18

Test point 2 | Recirculation control motor 5P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The M-FRS wire is not open. Go to step 4.

NO

Repair an open in the M-FRS wire.

- Shorted wire check (M-REC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 17 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-REC wire. NO The M-REC wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 17

Test point 2 | Body ground

Is there continuity?

YES
````

## Chunk 8773: DTC B2983 (C-A6), B2983 (57)

- Title: DTC B2983 (C-A6), B2983 (57)
- Source path: `pages\11346.html`
- Chunk ID: `chunk_efc7e3975d0a`
- Images: `images\GHH409312.jpeg`, `images\GHH409313.jpeg`
- Duplicate sources: `pages\13088.html`

### Full Text

````text
step 4.

NO

Repair an open in the M-FRS wire.

- Shorted wire check (M-REC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 17 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-REC wire. NO The M-REC wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 17

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-REC wire.

NO

The M-REC wire is OK. Go to step 5.

- Shorted wire check (M-FRS line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector B (24P): disconnected Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (24P) No. 18 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the M-FRS wire. NO The M-FRS wire is OK. Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector B (24P): disconnected

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (24P) No. 18

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the M-FRS wire.

NO

The M-FRS wire is OK. Go to step 6.

- Recirculation control motor check -1. Test the recirculation control motor . Is the recirculation control motor OK? YES Replace the climate control unit . NO Replace the recirculation control motor , or repair the recirculation control linkage or door.

-1. Test the recirculation control motor .

Is the recirculation control motor OK?

YES

Replace the climate control unit .

NO

Replace the recirculation control motor , or repair the recirculation control linkage or door.
````

## Chunk 8774: DTC B2986 (C-A4), B2986 (55)

- Title: DTC B2986 (C-A4), B2986 (55)
- Source path: `pages\11347.html`
- Chunk ID: `chunk_d88eff5dc32a`
- Images: `images\GHH409314.jpeg`, `images\GHH409315.jpeg`
- Duplicate sources: `pages\13089.html`

### Full Text

````text
# DTC B2986 (C-A4), B2986 (55)

DTC B2986 or DTC screen C-A4 or DTC indicator 55 : An Open in the Recirculation Control Motor Circuit

DTC Description | DTC

B2986 An open in the recirculation control motor circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Check for DTCs. DTC Description DTC B2986 An open in the recirculation control motor circuit Is DTC B2986 or Error on the DTC screen C-A4 (climate control panel without display) or 55 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Check for DTCs.

DTC Description | DTC

B2986 An open in the recirculation control motor circuit

Is DTC B2986 or Error on the DTC screen C-A4 (climate control panel without display) or 55 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the recirculation control motor circuit.

- Determine possible failure area (RFD-P line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Recirculation control motor 5P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Recirculation control motor 5P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The RFD-P wire is OK. Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Recirculation control motor 5P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Recirculation control motor 5P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The RFD-P wire is OK. Go to step 3.

NO

Go to step 4.

- Open wire check (SENS COM-H line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Recirculation control motor 5P connector No. 3 Test point 2 Recirculation control motor 5P connector No. 4 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the recirculation control motor . NO Repair an open in the SENS COM-H wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Recirculation control motor 5P connector No. 3

Test point 2 | Recirculation control motor 5P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the recirculation control motor .

NO

Repair an open in the SENS COM-H wire.

- Open wire check (RFD-P line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Recirculation control motor 5P connector: disconnected Test point 1 Climate control unit connector B (12P) No. 4 Test point 2 Body ground Is there about 5 V? YES Repair an open in the RFD-P wire. NO Replace the climate control unit .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Recirculation control motor 5P connector: disconnected

Test point 1 | Climate control unit connector B (12P) No. 4

Test point 2 | Body ground

Is there about 5 V?

YES

Repair an open in the RFD-P wire.

NO

Replace the climate control unit .
````

## Chunk 8775: DTC B2988 (C-B1), B2988 (C-B2), B2988 (61)

- Title: DTC B2988 (C-B1), B2988 (C-B2), B2988 (61)
- Source path: `pages\11348.html`
- Chunk ID: `chunk_69a102d6cd40`
- Images: `images\GHH409316.jpeg`, `images\GHH409317.jpeg`
- Duplicate sources: `pages\13090.html`

### Full Text

````text
# DTC B2988 (C-B1), B2988 (C-B2), B2988 (61)

DTC B2988 or DTC screen C-B1 : An Open in the A/C Compressor Variable Capacity Control Solenoid Circuit

DTC B2988 or DTC screen C-B2 : A Short in the A/C Compressor Variable Capacity Control Solenoid Circuit

DTC B2988 or DTC indicator 61 : A Problem in the A/C Compressor Variable Capacity Control Solenoid Circuit

DTC Description | DTC

B2988 A problem in the A/C compressor variable capacity control solenoid circuit

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the HDS or the climate control unit . -4. Wait for at least 1 minute. -5. Check for DTCs. DTC Description DTC B2988 A problem in the A/C compressor variable capacity control solenoid circuit Is DTC B2988 or Error on the DTC screen C-B1 (climate control panel without display) or C-B2 (climate control panel without display) or 61 (climate control panel with display) indicated? YES Go to step 2. NO Intermittent failure. Check for loose wires or poor connections on the A/C compressor variable capacity control solenoid circuit.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the HDS or the climate control unit .

-4. Wait for at least 1 minute.

-5. Check for DTCs.

DTC Description | DTC

B2988 A problem in the A/C compressor variable capacity control solenoid circuit

Is DTC B2988 or Error on the DTC screen C-B1 (climate control panel without display) or C-B2 (climate control panel without display) or 61 (climate control panel with display) indicated?

YES

Go to step 2.

NO

Intermittent failure. Check for loose wires or poor connections on the A/C compressor variable capacity control solenoid circuit.

- Open wire check (SOL OUT line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. Climate control unit connector A (32P) A/C compressor clutch 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected A/C compressor clutch 3P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 30 Test point 2 A/C compressor clutch 3P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SOL OUT wire is not open. Go to step 3. NO Repair an open in the SOL OUT wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

Climate control unit connector A (32P)

A/C compressor clutch 3P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

A/C compressor clutch 3P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 30

Test point 2 | A/C compressor clutch 3P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL OUT wire is not open. Go to step 3.

NO

Repair an open in the SOL OUT wire.

- Open wire check (SOL IN line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected A/C compressor clutch 3P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 14 Test point 2 A/C compressor clutch 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SOL IN wire is not open. Go to step 4. NO Repair an open in the SOL IN wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

A/C compressor clutch 3P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 14

Test point 2 | A/C compressor clutch 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL IN wire is not open. Go to step 4.

NO

Repair an open in the SOL IN wire.

- Shorted wire check (SOL OUT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected A/C compressor clutch 3P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 30 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL OUT wire. NO The SOL OUT wire is OK. Go to step 5.
````

## Chunk 8776: DTC B2988 (C-B1), B2988 (C-B2), B2988 (61)

- Title: DTC B2988 (C-B1), B2988 (C-B2), B2988 (61)
- Source path: `pages\11348.html`
- Chunk ID: `chunk_c8a04985e362`
- Images: `images\GHH409316.jpeg`, `images\GHH409317.jpeg`
- Duplicate sources: `pages\13090.html`

### Full Text

````text
mode

Climate control unit connector A (32P): disconnected

A/C compressor clutch 3P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 14

Test point 2 | A/C compressor clutch 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL IN wire is not open. Go to step 4.

NO

Repair an open in the SOL IN wire.

- Shorted wire check (SOL OUT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected A/C compressor clutch 3P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 30 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL OUT wire. NO The SOL OUT wire is OK. Go to step 5.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

A/C compressor clutch 3P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 30

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the SOL OUT wire.

NO

The SOL OUT wire is OK. Go to step 5.

- Shorted wire check (SOL IN line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected A/C compressor clutch 3P connector: disconnected Test point 1 Climate control unit connector A (32P) No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL IN wire. NO The SOL IN wire is OK. Go to step 6.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

A/C compressor clutch 3P connector: disconnected

Test point 1 | Climate control unit connector A (32P) No. 14

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the SOL IN wire.

NO

The SOL IN wire is OK. Go to step 6.

- A/C compressor variable capacity control solenoid check -1. Test the A/C compressor variable capacity control solenoid . Is the variable capacity control solenoid OK? YES Replace the climate control unit . NO Replace the A/C compressor .

-1. Test the A/C compressor variable capacity control solenoid .

Is the variable capacity control solenoid OK?

YES

Replace the climate control unit .

NO

Replace the A/C compressor .
````

## Chunk 8777: DTC U1280 (D-A1), U1280 (80) (Climate Control Unit)

- Title: DTC U1280 (D-A1), U1280 (80) (Climate Control Unit)
- Source path: `pages\11349.html`
- Chunk ID: `chunk_6bbdda5b5b54`
- Images: none
- Duplicate sources: `pages\13091.html`

### Full Text

````text
# DTC U1280 (D-A1), U1280 (80) (Climate Control Unit)

DTC U1280 or DTC screen D-A1 or DTC indicator 80 : Communication Bus Line Error (BUS-OFF)

DTC Description | DTC

U1280 Communication bus line error (BUS-OFF)

DTC (AC)

- Problem verification -1. Clear the DTCs with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Do the Self-Diagnostic Function with the climate control unit . -4. Wait for at least 6 seconds. -5. Check for DTCs. DTC Description DTC U1280 Communication bus line error (BUS-OFF) Is DTC U1280 or Error on the DTC screen D-A1 (climate control panel without display) or 80 (climate control panel with display) indicated? YES Go to body control module DTC U1280 troubleshooting . NO Intermittent failure, the system is OK at this time.

-1. Clear the DTCs with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Do the Self-Diagnostic Function with the climate control unit .

-4. Wait for at least 6 seconds.

-5. Check for DTCs.

DTC Description | DTC

U1280 Communication bus line error (BUS-OFF)

Is DTC U1280 or Error on the DTC screen D-A1 (climate control panel without display) or 80 (climate control panel with display) indicated?

YES

Go to body control module DTC U1280 troubleshooting .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 8778: DTC U1281 (D-A3), U1281 (91), U128D (D-A2), U128D (83), U1290 (D-A6) (Climate Control Unit)

- Title: DTC U1281 (D-A3), U1281 (91), U128D (D-A2), U128D (83), U1290 (D-A6) (Climate Control Unit)
- Source path: `pages\11350.html`
- Chunk ID: `chunk_f972af40e36d`
- Images: none
- Duplicate sources: `pages\13092.html`

### Full Text

````text
# DTC U1281 (D-A3), U1281 (91), U128D (D-A2), U128D (83), U1290 (D-A6) (Climate Control Unit)

DTC U1281 or DTC screen D-A3 or DTC indicator 91 : Climate Control Unit Lost Communication with MICU (Body Control Module)

DTC U128D or DTC screen D-A2 : Climate Control Unit Lost Communication with Gauge Control Module

DTC U128D or DTC indicator 83 : Climate Control Unit Lost Communication with Gauge Control Module (VSP message)

DTC U1290 or DTC screen D-A6 : Climate Control Unit Lost Communication with Seat Heater Control Unit (Front)

NOTE:

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the climate control unit.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

DTC Description | DTC

U1281 Climate control unit lost communication with MICU (body control module)

U128D Climate control unit lost communication with gauge control module

U1290 Climate control unit lost communication with seat heater control unit (front)

DTC (AC)

- Problem verification -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode. -3. Wait for at least 6 seconds. -4. Do the Self-Diagnostic Function with the climate control unit . -5. Check for DTCs. DTC Description DTC U1281 Climate control unit lost communication with MICU (body control module) U128D Climate control unit lost communication with gauge control module U1290 Climate control unit lost communication with seat heater control unit (front) Are any DTCs indicated? YES Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control units and the climate control unit.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode and then the ON mode.

-3. Wait for at least 6 seconds.

-4. Do the Self-Diagnostic Function with the climate control unit .

-5. Check for DTCs.

DTC Description | DTC

U1281 Climate control unit lost communication with MICU (body control module)

U128D Climate control unit lost communication with gauge control module

U1290 Climate control unit lost communication with seat heater control unit (front)

Are any DTCs indicated?

YES

Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control units and the climate control unit.

- Open wire check (B-CAN_H line, B-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the receiving control unit connector. Climate control unit connector A (32P) -3. Disconnect the transmitting control unit connector(s). Refer to the DTC shown on the display, then disconnect the connector(s) based on the instructions (see table). DTC Connector U1281 Body control module connector B (36P) U128D Gauge control module connector A (32P) U1290 Front seat heater control unit 14P connector -4. Check for continuity between the receiving control unit and the transmitting control unit on the B-CAN_H circuit and the B-CAN_L circuit. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Receiving control unit Transmitting control unit Connector Terminal Connector Terminal U1281 B-CAN_H Climate control unit connector A (32P) No. 25 Body control module connector B (36P) No. 20 B-CAN_L No. 8 No. 21 U128D B-CAN_H Climate control unit connector A (32P) No. 25 Gauge control module connector A (32P) No. 30 B-CAN_L No. 8 No. 31 U1290 B-CAN_H Climate control unit connector A (32P) No. 25 Front seat heater control unit 14P connector No. 11 B-CAN_L No. 8 No. 10 Is there continuity? YES The B-CAN_H wire and B-CAN_L wire is OK.Refer to the DTC shown on the display, then substitute or replace the control unit based on the instructions (see table). DTC Operation for transmitting control unit U1281 Substitute a known-good body control module , then recheck. If DTC U1281 goes away after substitution, replace the original body control module . U128D Substitute a known-good gauge control module , then recheck. If DTC U128D goes away after substitution, replace the original gauge control module .
````

## Chunk 8779: DTC U1281 (D-A3), U1281 (91), U128D (D-A2), U128D (83), U1290 (D-A6) (Climate Control Unit)

- Title: DTC U1281 (D-A3), U1281 (91), U128D (D-A2), U128D (83), U1290 (D-A6) (Climate Control Unit)
- Source path: `pages\11350.html`
- Chunk ID: `chunk_49a47177e879`
- Images: none
- Duplicate sources: `pages\13092.html`

### Full Text

````text
21 U128D B-CAN_H Climate control unit connector A (32P) No. 25 Gauge control module connector A (32P) No. 30 B-CAN_L No. 8 No. 31 U1290 B-CAN_H Climate control unit connector A (32P) No. 25 Front seat heater control unit 14P connector No. 11 B-CAN_L No. 8 No. 10 Is there continuity? YES The B-CAN_H wire and B-CAN_L wire is OK.Refer to the DTC shown on the display, then substitute or replace the control unit based on the instructions (see table). DTC Operation for transmitting control unit U1281 Substitute a known-good body control module , then recheck. If DTC U1281 goes away after substitution, replace the original body control module . U128D Substitute a known-good gauge control module , then recheck. If DTC U128D goes away after substitution, replace the original gauge control module . U1290 Substitute a known-good front seat heater control unit , then recheck. If DTC U1290 goes away after substitution, replace the original front seat heater control unit . NO Repair an open in the B-CAN_H wire and/or the B-CAN_L wire between the climate control unit and the transmitting control unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the receiving control unit connector.

Climate control unit connector A (32P)

-3. Disconnect the transmitting control unit connector(s).

Refer to the DTC shown on the display, then disconnect the connector(s) based on the instructions (see table).

DTC | Connector

U1281 | Body control module connector B (36P)

U128D | Gauge control module connector A (32P)

U1290 | Front seat heater control unit 14P connector

-4. Check for continuity between the receiving control unit and the transmitting control unit on the B-CAN_H circuit and the B-CAN_L circuit.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Receiving control unit | Transmitting control unit

Connector | Terminal | Connector | Terminal

U1281 | B-CAN_H | Climate control unit connector A (32P) | No. 25 | Body control module connector B (36P) | No. 20

B-CAN_L | No. 8 | No. 21

U128D | B-CAN_H | Climate control unit connector A (32P) | No. 25 | Gauge control module connector A (32P) | No. 30

B-CAN_L | No. 8 | No. 31

U1290 | B-CAN_H | Climate control unit connector A (32P) | No. 25 | Front seat heater control unit 14P connector | No. 11

B-CAN_L | No. 8 | No. 10

Is there continuity?

YES

The B-CAN_H wire and B-CAN_L wire is OK.Refer to the DTC shown on the display, then substitute or replace the control unit based on the instructions (see table).

DTC | Operation for transmitting control unit

U1281 | Substitute a known-good body control module , then recheck. If DTC U1281 goes away after substitution, replace the original body control module .

U128D | Substitute a known-good gauge control module , then recheck. If DTC U128D goes away after substitution, replace the original gauge control module .

U1290 | Substitute a known-good front seat heater control unit , then recheck. If DTC U1290 goes away after substitution, replace the original front seat heater control unit .

NO

Repair an open in the B-CAN_H wire and/or the B-CAN_L wire between the climate control unit and the transmitting control unit.
````

## Chunk 8780: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11351.html`
- Chunk ID: `chunk_50e2fe7e4756`
- Images: none
- Duplicate sources: `pages\15422.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE:

- If the A/C compressor relief valve released refrigerant to the atmosphere, determine and correct the cause of the excessive system pressure, then replace the relief valve.

- Plug the opening to keep moisture and foreign material from entering the system, and the A/C compressor oil from running out.
````

## Chunk 8781: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11352.html`
- Chunk ID: `chunk_5fc530e16745`
- Images: `images\GHH399704.png`, `images\GHH400684.png`, `images\GHH409318.jpeg`
- Duplicate sources: `pages\15423.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Courtesy of HONDA, U.S.A., INC.

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Refrigerant - Recover

- Engine Undercover - Remove

- A/C Compressor Relief Valve - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: If the A/C compressor relief valve released refrigerant to the atmosphere, determine and correct the cause of the excessive system pressure, then replace the relief valve. Clean the mating surfaces. A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage. Charge the system with the specified amount of refrigerant .

1. Install the parts in the reverse order of removal, and note these items:

- If the A/C compressor relief valve released refrigerant to the atmosphere, determine and correct the cause of the excessive system pressure, then replace the relief valve.

- Clean the mating surfaces.

- A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage.

- Charge the system with the specified amount of refrigerant .
````

## Chunk 8782: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11353.html`
- Chunk ID: `chunk_4dd14d79d511`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\15424.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Review the A/C refrigerant oil replacement before doing repairs or service.

- Do not install the A/C compressor into a system unless you are completely sure that the system is free of contamination. Installing the A/C compressor into a contaminated system can result in premature A/C compressor failure. Refer to the A/C System Contamination Inspection .

- If the A/C compressor is marginally operable, run the engine at idle speed, and let the air conditioning work for a few minutes, then shut the engine off.

- Plug or cap the lines immediately after disconnecting them to avoid moisture and dust contamination.

- Be careful not to damage the radiator fins when removing the A/C compressor.

- Apply to the compressor oil when install O-rings.
````

## Chunk 8783: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11354.html`
- Chunk ID: `chunk_8544f77443e3`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409319.jpeg`, `images\GHH409320.jpeg`, `images\GHH409321.jpeg`, `images\GHH409322.jpeg`, `images\GHH409323.jpeg`, `images\GHH409324.jpeg`
- Duplicate sources: `pages\15425.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

- A/C Refrigerant - Recover

- Drive Belt - Remove

- Engine Undercover - Remove

- A/C Condenser Fan Shroud Assembly - Remove (Type-R)

- Charge Air Cooler Inlet Hose - Remove (Type-R)

- Discharge Hose and Suction Hose - Disconnect Note for installation Inspect the A/C lines for any signs of contamination.

Note for installation

Inspect the A/C lines for any signs of contamination.

- A/C Compressor - Remove Note for installation If you are installing a new A/C compressor, you must calculate the amount of refrigerant oil to be removed from it . A new A/C compressor comes with a full charge of oil.

Note for installation

If you are installing a new A/C compressor, you must calculate the amount of refrigerant oil to be removed from it . A new A/C compressor comes with a full charge of oil.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8784: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11355.html`
- Chunk ID: `chunk_1c421316c956`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\15426.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Review the A/C refrigerant oil replacement before doing repairs or service.

- Be careful not to damage the radiator and A/C condenser fins, and the receiver line when removing the A/C condenser.

- Apply to the compressor oil when install O-rings.
````

## Chunk 8785: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11356.html`
- Chunk ID: `chunk_124bbdc9e75a`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409325.jpeg`, `images\GHH409326.jpeg`, `images\GHH409327.jpeg`
- Duplicate sources: `pages\15427.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Refrigerant - Recover (With A/C)

- Front Grille Cover - Remove

- Front Bumper - Remove

- Front Bumper Upper Beam - Remove

- Front Bumper Middle Induction Plate - Remove (If equipped)

- Discharge Hose - Disconnect (With A/C)

- Charge Air Cooler Bracket - Remove (Type-R)

- Charge Air Cooler - Move (Type-R)

- Receiver Pipe - Disconnect (With A/C)

- A/C Condenser - Remove Note for installation If you are installing a new A/C condenser, add the appropriate refrigerant oil for the A/C compressor which installed to the vehicle .

Note for installation

If you are installing a new A/C condenser, add the appropriate refrigerant oil for the A/C compressor which installed to the vehicle .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8786: Exploded View

- Title: Exploded View
- Source path: `pages\11357.html`
- Chunk ID: `chunk_0bb0eb5a57c3`
- Images: `images\GHH409328.jpeg`
- Duplicate sources: `pages\15428.html`

### Full Text

````text
# Exploded View

- A/C Line - Remove and Install Fig 1: A/C Line Components With Torque Specifications Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8787: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11359.html`
- Chunk ID: `chunk_ab7a2a504b58`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409329.jpeg`, `images\GHH409330.jpeg`
- Duplicate sources: `pages\15430.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

For some models

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Refrigerant - Recover

- Front Grille Cover - Remove

- Front Bumper - Remove

- A/C Pressure Sensor - Remove 1. Hold the A/C pressure sensor block with a wrench to prevent damaging the discharge hose, then remove the A/C pressure sensor.

1. Hold the A/C pressure sensor block with a wrench to prevent damaging the discharge hose, then remove the A/C pressure sensor.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage. Charge the system with the specified amount of refrigerant .

1. Install the parts in the reverse order of removal, and note these items:

- A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage.

- Charge the system with the specified amount of refrigerant .
````

## Chunk 8788: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\11360.html`
- Chunk ID: `chunk_4a9a97773e81`
- Images: `images\GHH409331.jpeg`, `images\GHH409332.jpeg`, `images\GHH409333.jpeg`
- Duplicate sources: `pages\15431.html`

### Full Text

````text
# Removal and Installation

SRS components are located near the mode control motor and the recirculation control motor. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE:

- Set the VENT position before removing the mode control motor.

- Set the FRESH position before removing the recirculation control motor.

- Set the MAX COOL position before removing the air mix control motor.

- The air mix control motor and the driver's air mix control motor are the same parts.

- Part Removal for Motor Access NOTE: Numbers in table indicate parts removal order. Remove Parts Test Motor Air Mix Control Motor Passenger's Air Mix Control Motor * Mode Control Motor Recirculation Control Motor Driver's Dashboard Lower Cover [1] --- --- --- Glove Box Back Cover --- [1] [1] [1] Passenger's Heater Duct --- [2] [2] --- *: With dual zone climate control

NOTE: Numbers in table indicate parts removal order.

Remove Parts | Test Motor

Air Mix Control Motor | Passenger's Air Mix Control Motor * | Mode Control Motor | Recirculation Control Motor

Driver's Dashboard Lower Cover | [1] | --- | --- | ---

Glove Box Back Cover | --- | [1] | [1] | [1]

Passenger's Heater Duct | --- | [2] | [2] | ---

*: With dual zone climate control

- Motors Location Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install Air mix control motor Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Passenger's air mix control motor (With dual zone climate control) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Install the parts in the reverse order of removal, and note these items: When you install the air mix control motor and the passenger's air mix control motor (A), align the position of the damper lever pins (B), then install control motor. After installation, do the Self-Diagnostic Function with the HDS or the climate control unit .

Air mix control motor Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Passenger's air mix control motor (With dual zone climate control) Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Install the parts in the reverse order of removal, and note these items: When you install the air mix control motor and the passenger's air mix control motor (A), align the position of the damper lever pins (B), then install control motor. After installation, do the Self-Diagnostic Function with the HDS or the climate control unit .

Passenger's air mix control motor (With dual zone climate control)

- When you install the air mix control motor and the passenger's air mix control motor (A), align the position of the damper lever pins (B), then install control motor.

- After installation, do the Self-Diagnostic Function with the HDS or the climate control unit .
````

## Chunk 8789: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11362.html`
- Chunk ID: `chunk_4c5af1f1fa4d`
- Images: `images\GHH409334.jpeg`
- Duplicate sources: `pages\15433.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Glove Box Back Cover - Remove

- Blower Motor - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8790: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11364.html`
- Chunk ID: `chunk_8f56814d2bc5`
- Images: `images\GHH409335.jpeg`
- Duplicate sources: `pages\15435.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Glove Box Back Cover - Remove

- Passenger's Heater Duct - Remove

- Blower Power Transistor - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8791: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11366.html`
- Chunk ID: `chunk_68733fa94467`
- Images: `images\GHH399704.png`, `images\GHH409336.jpeg`
- Duplicate sources: `pages\15437.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

- Glove Box Back Cover - Remove

- Passenger's Heater Duct - Remove

- Blower Unit - Remove

- Climate Control Unit - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8792: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11367.html`
- Chunk ID: `chunk_dd2683778b6c`
- Images: `images\GHH409337.jpeg`
- Duplicate sources: `pages\15438.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Numbered call-outs in figure pertain to list numbers in following procedure.

- Center Console Side Trim - Remove

- Climate Control Panel - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. 2. Run the self-diagnostic function to confirm that there are no problems in the system .

1. Install the parts in the reverse order of removal.

2. Run the self-diagnostic function to confirm that there are no problems in the system .
````

## Chunk 8793: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11369.html`
- Chunk ID: `chunk_94bb2e022bf6`
- Images: `images\GHH409338.jpeg`
- Duplicate sources: `pages\15440.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Glove Box Back Cover - Remove

- Climate Control Unit - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: After installing all the parts, run the self-diagnostic function to confirm that there are no problems in the system.

1. Install the parts in the reverse order of removal.

NOTE: After installing all the parts, run the self-diagnostic function to confirm that there are no problems in the system.
````

## Chunk 8794: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\11372.html`
- Chunk ID: `chunk_ba4c8f6c20b5`
- Images: `images\GHH409341.jpeg`
- Duplicate sources: `pages\15443.html`

### Full Text

````text
# Removal and Installation

- Right Front Wheel - Remove

- Engine Undercover - Remove

- Drive Belt - Remove Courtesy of HONDA, U.S.A., INC. 1. Attach a wrench to the drive belt auto-tensioner (A) and move it in the direction shown. Fix the drive belt auto-tensioner by aligning the water passage hole with drive belt auto-tensioner hole and inserting a 6 x 45 mm (15/64 x 1.77 in) pin (B) deep into the holes. NOTE: This is a hydraulic type auto-tensioner, so you must turn the wrench slowly for at least 3 seconds. 2. Remove the drive belt (C).

Courtesy of HONDA, U.S.A., INC. | 1. Attach a wrench to the drive belt auto-tensioner (A) and move it in the direction shown. Fix the drive belt auto-tensioner by aligning the water passage hole with drive belt auto-tensioner hole and inserting a 6 x 45 mm (15/64 x 1.77 in) pin (B) deep into the holes. NOTE: This is a hydraulic type auto-tensioner, so you must turn the wrench slowly for at least 3 seconds. 2. Remove the drive belt (C).

NOTE: This is a hydraulic type auto-tensioner, so you must turn the wrench slowly for at least 3 seconds.

2. Remove the drive belt (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8795: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11373.html`
- Chunk ID: `chunk_889c375c51c7`
- Images: `images\GHH409342.jpeg`
- Duplicate sources: `pages\15444.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Dust and Pollen Filter - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Make sure that there is no air leaking out of the blower unit.

1. Install the parts in the reverse order of removal.

NOTE: Make sure that there is no air leaking out of the blower unit.

- Maintenance Minder - Reset (With Maintenance Minder System) If the Maintenance Minder indicated that the dust and pollen filter needed replacement, reset the Maintenance Minder with the gauge . If the Maintenance Minder did not indicated that the dust and pollen filter needed replacement, reset the Maintenance Minder with the HDS .

If the Maintenance Minder indicated that the dust and pollen filter needed replacement, reset the Maintenance Minder with the gauge . If the Maintenance Minder did not indicated that the dust and pollen filter needed replacement, reset the Maintenance Minder with the HDS .
````

## Chunk 8796: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11374.html`
- Chunk ID: `chunk_26973774d8eb`
- Images: none
- Duplicate sources: `pages\15445.html`

### Full Text

````text
# Removal and Installation: Notes

NOTICE:

Vehicles equipped with R-744 or R-1234yf refrigerant system evaporator(s) shall include in their service information that only new and SAE J2842 certified evaporator(s) shall be used as replacement parts.

NOTE: Be careful not to damage the evaporator core.
````

## Chunk 8797: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11375.html`
- Chunk ID: `chunk_a36d0945b140`
- Images: `images\GHH400684.png`, `images\GHH409343.jpeg`
- Duplicate sources: `pages\11377.html`, `pages\15446.html`, `pages\15448.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Replace

- HVAC Unit - Remove

- Blower Unit - Remove

- Upper Heater Unit Case - Remove

- Evaporator Core - Remove

- Evaporator Temperature Sensor - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: Replace the seal washer with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct seal washer to avoid leakage. Charge the system with the specified amount of refrigerant . Make sure that there is no refrigerant leakage. Make sure that there is no air leakage.

1. Install the parts in the reverse order of removal, and note these items:

- Replace the seal washer with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct seal washer to avoid leakage.

- Charge the system with the specified amount of refrigerant .

- Make sure that there is no refrigerant leakage.

- Make sure that there is no air leakage.
````

## Chunk 8798: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11376.html`
- Chunk ID: `chunk_79dc4b4e445d`
- Images: none
- Duplicate sources: `pages\15447.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE: Be careful not to damage the evaporator core.
````

## Chunk 8799: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11378.html`
- Chunk ID: `chunk_2c655be9b5cc`
- Images: `images\GHH399704.png`, `images\GHH400684.png`, `images\GHH409345.jpeg`
- Duplicate sources: `pages\15449.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Refrigerant - Recover

- A/C Lines - Remove

- Expansion Valve - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: Replace the seal washer with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct seal washer to avoid leakage. Charge the system with the specified amount of refrigerant .

1. Install the parts in the reverse order of removal, and note these items:

- Replace the seal washer with new ones at each fitting, and apply a thin coat of refrigerant oil before installing them. Be sure to use the correct seal washer to avoid leakage.

- Charge the system with the specified amount of refrigerant .
````

## Chunk 8800: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11379.html`
- Chunk ID: `chunk_c7fa37643fc6`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\15450.html`

### Full Text

````text
# Removal and Installation: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE: Where icon is shown, for further information see below.
````

## Chunk 8801: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11380.html`
- Chunk ID: `chunk_a07dce789b7b`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409346.jpeg`, `images\GHH409347.jpeg`, `images\GHH409348.jpeg`
- Duplicate sources: `pages\15451.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

*1 | For some models

- 12 Volt Battery Terminal - Disconnect

- A/C Refrigerant - Recover (With A/C)

- Engine Coolant - Drain

- A/C Lines - Remove (With A/C) NOTE: Take care not to damage or bend the fuel lines or the brake lines.

NOTE: Take care not to damage or bend the fuel lines or the brake lines.

- Heater Hoses - Remove NOTE: Engine coolant will run out when the hoses are disconnected; drain it into a clean drip pan. Be sure not to let coolant spill on the electrical parts or the painted surfaces. If any coolant spills, rinse it off immediately. Note the layout of the hoses.

NOTE:

- Engine coolant will run out when the hoses are disconnected; drain it into a clean drip pan. Be sure not to let coolant spill on the electrical parts or the painted surfaces. If any coolant spills, rinse it off immediately.

- Note the layout of the hoses.

- Heater Unit Mounting Nut - Remove NOTE: Take care not to damage or bend the fuel lines or the brake lines.

NOTE: Take care not to damage or bend the fuel lines or the brake lines.

- Dashboard/Steering Hanger Beam - Remove

- Rear Center Ventilation Duct - Remove (For some models)

- Drain Hose - Disconnect

- HVAC Unit - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: Do not interchange the inlet and outlet heater hoses, and install the hose clamps securely. Make sure that there is no coolant leakage. Make sure that there is no air leakage. Make sure that there is no refrigerant leakage. Do the 12 volt battery terminal reconnection procedure . Refill the radiator with engine coolant, and bleed the air from the cooling system . A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage. Charge the system with the specified amount of refrigerant .

1. Install the parts in the reverse order of removal, and note these items:

- Do not interchange the inlet and outlet heater hoses, and install the hose clamps securely.

- Make sure that there is no coolant leakage.

- Make sure that there is no air leakage.

- Make sure that there is no refrigerant leakage.

- Do the 12 volt battery terminal reconnection procedure .

- Refill the radiator with engine coolant, and bleed the air from the cooling system .

- A new O-ring should be used at each fitting. Prior to installation, apply a thin coat of the same refrigerant oil used in the A/C compressor. Be sure to use the correct O-ring for refrigerant types to avoid leakage.

- Charge the system with the specified amount of refrigerant .
````

## Chunk 8802: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11381.html`
- Chunk ID: `chunk_4bd2a2349cb5`
- Images: none
- Duplicate sources: `pages\15452.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE: Be careful not to damage the heater core.
````

## Chunk 8803: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11382.html`
- Chunk ID: `chunk_a9a420463dbb`
- Images: `images\GHH409349.jpeg`
- Duplicate sources: `pages\15453.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- HVAC Unit - Remove

- Driver's Heater Duct - Remove

- Aspirator and Aspirator Hose - Remove

- Heater Pipe Cover - Remove

- Heater Pipe Bracket - Remove

- Grommet - Remove

- Heater Core - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Make sure that there is no air leakage.

1. Install the parts in the reverse order of removal.

NOTE: Make sure that there is no air leakage.
````

## Chunk 8804: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11383.html`
- Chunk ID: `chunk_cf1003e5f87b`
- Images: `images\GHH399704.png`, `images\GHH400684.png`, `images\GHH409350.jpeg`
- Duplicate sources: `pages\15454.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

Replace

- Front Grille Cover - Remove

- Front Bumper - Remove

- Front Bumper Upper Beam - Remove

- Desiccant - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: Install the desiccant as quickly as possible to prevent the system from absorbing moisture from the air. If you are installing a new desiccant, add refrigerant oil . Replace the O-rings with new ones, and apply a thin coat of refrigerant oil before installing them. Install the cap to the specified torque. It is made of resin and can be easily stripped.

1. Install the parts in the reverse order of removal, and note these items:

- Install the desiccant as quickly as possible to prevent the system from absorbing moisture from the air.

- If you are installing a new desiccant, add refrigerant oil .

- Replace the O-rings with new ones, and apply a thin coat of refrigerant oil before installing them.

- Install the cap to the specified torque. It is made of resin and can be easily stripped.
````

## Chunk 8805: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\11384.html`
- Chunk ID: `chunk_4266860dad51`
- Images: `images\GHH409351.jpeg`, `images\GHH409352.jpeg`
- Duplicate sources: `pages\15455.html`

### Full Text

````text
# Removal and Installation

- Side Defogger Vent Trim - Remove Driver's side Courtesy of HONDA, U.S.A., INC. Passenger's side Courtesy of HONDA, U.S.A., INC.

Driver's side

Courtesy of HONDA, U.S.A., INC.

Passenger's side

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8806: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\11385.html`
- Chunk ID: `chunk_d729864893d9`
- Images: none
- Duplicate sources: `pages\15456.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE: Be careful not to damage the sunlight sensor and the dashboard.
````

## Chunk 8807: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11386.html`
- Chunk ID: `chunk_0196bbd2c2ad`
- Images: `images\GHH409353.jpeg`
- Duplicate sources: `pages\15457.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Sunlight Sensor - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8808: A/C Compressor Clutch Overhaul: Notes

- Title: A/C Compressor Clutch Overhaul: Notes
- Source path: `pages\11387.html`
- Chunk ID: `chunk_66cbd16c641b`
- Images: `images\GHH178774.png`, `images\GHH18262.png`
- Duplicate sources: `pages\15458.html`

### Full Text

````text
# A/C Compressor Clutch Overhaul: Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | A/C Compressor Kit 07AAF-000A150*

Courtesy of HONDA, U.S.A., INC. | Delphi A/C Clutch Adapter 07AAC-TBAA100*

*These tools are available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8809: Disassembly and Reassembly: Notes

- Title: Disassembly and Reassembly: Notes
- Source path: `pages\11388.html`
- Chunk ID: `chunk_7e2311ac3b6c`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\12586.html`, `pages\15459.html`, `pages\13985.html`

### Full Text

````text
# Disassembly and Reassembly: Notes

NOTE: Where icon is shown, for further information see below.
````

## Chunk 8810: Disassembly and Reassembly: Procedure

- Title: Disassembly and Reassembly: Procedure
- Source path: `pages\11389.html`
- Chunk ID: `chunk_071c8ae9e49a`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409354.jpeg`, `images\GHH409355.jpeg`, `images\GHH409356.jpeg`, `images\GHH409357.jpeg`, `images\GHH409358.jpeg`
- Duplicate sources: `pages\15460.html`

### Full Text

````text
# Disassembly and Reassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes, and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Compressor Armature Plate - Remove 1. Remove the center bolt (A) while holding the armature plate (B) with the A/C clutch holder (C). Courtesy of HONDA, U.S.A., INC. 2. Remove the armature plate and the shim(s) (D). NOTE: The shims are available in three thicknesses: 0.3 mm, 0.4 mm, and 0.5 mm. Do not pry on the armature plate with screwdrivers or similar tools. Prying damages the armature plate and the pulley. Inspect the armature plate and pulley friction surfaces for wear. If there is excessive wear, roughness, or scoring, replace the clutch set. If compressor oil is found, replace the A/C compressor .

1. Remove the center bolt (A) while holding the armature plate (B) with the A/C clutch holder (C).

Courtesy of HONDA, U.S.A., INC.

2. Remove the armature plate and the shim(s) (D).

NOTE:

- The shims are available in three thicknesses: 0.3 mm, 0.4 mm, and 0.5 mm.

- Do not pry on the armature plate with screwdrivers or similar tools. Prying damages the armature plate and the pulley.

- Inspect the armature plate and pulley friction surfaces for wear. If there is excessive wear, roughness, or scoring, replace the clutch set.

- If compressor oil is found, replace the A/C compressor .

- A/C Compressor Pulley - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) with the snap ring pliers. Courtesy of HONDA, U.S.A., INC. 2. Remove the pulley (A). NOTE: Do not hammer or pry on the pulley to remove it. Using a hammer damages the A/C compressor. If the pulley is difficult to remove, use a commercially available pulley removing tool. Make sure the jaws of the pulling tool engage the back face of the pulley, not the pulley grooves. Be careful not to damage the pulley or the A/C compressor.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) with the snap ring pliers.

Courtesy of HONDA, U.S.A., INC. | 2. Remove the pulley (A). NOTE: Do not hammer or pry on the pulley to remove it. Using a hammer damages the A/C compressor. If the pulley is difficult to remove, use a commercially available pulley removing tool. Make sure the jaws of the pulling tool engage the back face of the pulley, not the pulley grooves. Be careful not to damage the pulley or the A/C compressor.

- Do not hammer or pry on the pulley to remove it. Using a hammer damages the A/C compressor. If the pulley is difficult to remove, use a commercially available pulley removing tool. Make sure the jaws of the pulling tool engage the back face of the pulley, not the pulley grooves.

- Be careful not to damage the pulley or the A/C compressor.

- A/C Compressor Field Coil - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) with the snap ring pliers. 2. Remove the field coil (B). Be careful not to damage the field coil or the A/C compressor. NOTE: Inspect the friction surfaces and the compressor shaft hub for excess oil. If excess oil is present, and it is not from the engine, then the compressor shaft seal is leaking. Replace the A/C compressor .

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) with the snap ring pliers. 2. Remove the field coil (B). Be careful not to damage the field coil or the A/C compressor. NOTE: Inspect the friction surfaces and the compressor shaft hub for excess oil. If excess oil is present, and it is not from the engine, then the compressor shaft seal is leaking. Replace the A/C compressor .

2. Remove the field coil (B). Be careful not to damage the field coil or the A/C compressor.

NOTE: Inspect the friction surfaces and the compressor shaft hub for excess oil. If excess oil is present, and it is not from the engine, then the compressor shaft seal is leaking. Replace the A/C compressor .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: When replacing the field coil, check that the new coil has the correct resistance . Install the field coil with the wire side facing down, and align the boss on the field coil with the hole in the A/C compressor. If the clutch surface is oil soaked, check the compressor front seal for leakage. Installing a new clutch assembly on a leaking compressor will damage the new clutch assembly friction surfaces.
````

## Chunk 8811: Disassembly and Reassembly: Procedure

- Title: Disassembly and Reassembly: Procedure
- Source path: `pages\11389.html`
- Chunk ID: `chunk_20c63158be8e`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH409354.jpeg`, `images\GHH409355.jpeg`, `images\GHH409356.jpeg`, `images\GHH409357.jpeg`, `images\GHH409358.jpeg`
- Duplicate sources: `pages\15460.html`

### Full Text

````text
ld coil (B). Be careful not to damage the field coil or the A/C compressor.

NOTE: Inspect the friction surfaces and the compressor shaft hub for excess oil. If excess oil is present, and it is not from the engine, then the compressor shaft seal is leaking. Replace the A/C compressor .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal, and note these items: When replacing the field coil, check that the new coil has the correct resistance . Install the field coil with the wire side facing down, and align the boss on the field coil with the hole in the A/C compressor. If the clutch surface is oil soaked, check the compressor front seal for leakage. Installing a new clutch assembly on a leaking compressor will damage the new clutch assembly friction surfaces. Clean the pulley and the A/C compressor friction surfaces with contact cleaner or other non-petroleum solvent. Install new snap rings, note the installation direction, and make sure they are fully seated in the grooves. Make sure that the pulley turns smoothly after it's reassembled. Route and clamp the wires properly to prevent damage by the pulley. After reinstallation, cycle the A/C compressor clutch approximately 20 times by running the engine at 1500-2000 RPM and setting the A/C system to MAX COOL. This procedure seats the clutch sliding surfaces, and increases clutch torque capacity.

1. Install the parts in the reverse order of removal, and note these items:

- When replacing the field coil, check that the new coil has the correct resistance .

- Install the field coil with the wire side facing down, and align the boss on the field coil with the hole in the A/C compressor.

- If the clutch surface is oil soaked, check the compressor front seal for leakage. Installing a new clutch assembly on a leaking compressor will damage the new clutch assembly friction surfaces.

- Clean the pulley and the A/C compressor friction surfaces with contact cleaner or other non-petroleum solvent.

- Install new snap rings, note the installation direction, and make sure they are fully seated in the grooves.

- Make sure that the pulley turns smoothly after it's reassembled.

- Route and clamp the wires properly to prevent damage by the pulley.

- After reinstallation, cycle the A/C compressor clutch approximately 20 times by running the engine at 1500-2000 RPM and setting the A/C system to MAX COOL. This procedure seats the clutch sliding surfaces, and increases clutch torque capacity.
````

## Chunk 8812: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11390.html`
- Chunk ID: `chunk_6ee091efbc34`
- Images: `images\GHH409359.jpeg`, `images\GHH409360.jpeg`
- Duplicate sources: `pages\15461.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- HVAC Unit - Remove

- Evaporator Core - Remove

- Evaporator Temperature Sensor - Remove

- All Removed Parts - Install Courtesy of HONDA, U.S.A., INC. 1. Install the evaporator temperature sensor (A) in the evaporator core. Refer to the following position list. *: Measure from end of aluminum evaporator tank. *: Measure from end of aluminum evaporator tank. B C * Row mm (in) New Position 2nd or 4th 128 (5.04) B C * Row mm (in) Factory-Preset Position 3rd 128 (5.04)

Courtesy of HONDA, U.S.A., INC. | 1. Install the evaporator temperature sensor (A) in the evaporator core. Refer to the following position list. *: Measure from end of aluminum evaporator tank. *: Measure from end of aluminum evaporator tank.

*: Measure from end of aluminum evaporator tank.

*: Measure from end of aluminum evaporator tank.

B | C *

Row | mm (in)

New Position | 2nd or 4th | 128 (5.04)

B | C *

Row | mm (in)

Factory-Preset Position | 3rd | 128 (5.04)
````

## Chunk 8813: Evaporator Temperature Sensor Removal, Installation, and Test: Test

- Title: Evaporator Temperature Sensor Removal, Installation, and Test: Test
- Source path: `pages\11391.html`
- Chunk ID: `chunk_18660f320ee9`
- Images: `images\GHH409361.jpeg`, `images\GHH409362.jpeg`
- Duplicate sources: `pages\15462.html`

### Full Text

````text
# Evaporator Temperature Sensor Removal, Installation, and Test: Test

- Evaporator Temperature Sensor - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Dip the sensor in ice water, and measure the resistance between terminals No. 1 and No. 2. 2. Then pour warm water on the sensor, and check for a change in resistance. 3. Compare the resistance readings with the specifications shown in the graph; the resistance should be within the specifications. 4. If the resistance is not as specified, replace the evaporator temperature sensor.

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Dip the sensor in ice water, and measure the resistance between terminals No. 1 and No. 2. 2. Then pour warm water on the sensor, and check for a change in resistance. 3. Compare the resistance readings with the specifications shown in the graph; the resistance should be within the specifications. 4. If the resistance is not as specified, replace the evaporator temperature sensor.

2. Then pour warm water on the sensor, and check for a change in resistance.

3. Compare the resistance readings with the specifications shown in the graph; the resistance should be within the specifications.

4. If the resistance is not as specified, replace the evaporator temperature sensor.
````

## Chunk 8814: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\11392.html`
- Chunk ID: `chunk_40f82c8bd73c`
- Images: `images\GHH409363.jpeg`
- Duplicate sources: `pages\15463.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

- Driver's Dashboard Lower Cover - Remove

- In-Car Temperature Sensor - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8815: In-Car Temperature Sensor Removal, Installation, and Test: Test

- Title: In-Car Temperature Sensor Removal, Installation, and Test: Test
- Source path: `pages\11393.html`
- Chunk ID: `chunk_6fd4b8beb70c`
- Images: `images\GHH409364.jpeg`, `images\GHH409365.jpeg`
- Duplicate sources: `pages\15464.html`

### Full Text

````text
# In-Car Temperature Sensor Removal, Installation, and Test: Test

NOTE: Before testing the sensor, check for climate control DTCs .

- In-Car Temperature Sensor - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Test the in-car temperature sensor while holding it in front of the dashboard center vent. Measure the resistance with the system set to MAX COOL. Measure the resistance with the system set to MAX HOT. 2. Compare the resistance readings with the specifications shown in the graph, the resistance should be within the specifications. 3. If the resistance is not as specified, replace the in-car temperature sensor.

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Test the in-car temperature sensor while holding it in front of the dashboard center vent. Measure the resistance with the system set to MAX COOL. Measure the resistance with the system set to MAX HOT. 2. Compare the resistance readings with the specifications shown in the graph, the resistance should be within the specifications. 3. If the resistance is not as specified, replace the in-car temperature sensor.

- Measure the resistance with the system set to MAX COOL.

- Measure the resistance with the system set to MAX HOT.

2. Compare the resistance readings with the specifications shown in the graph, the resistance should be within the specifications.

3. If the resistance is not as specified, replace the in-car temperature sensor.
````

## Chunk 8816: Exploded View

- Title: Exploded View
- Source path: `pages\11394.html`
- Chunk ID: `chunk_739b833358e0`
- Images: `images\GHH409366.jpeg`, `images\GHH409367.jpeg`
- Duplicate sources: `pages\15465.html`

### Full Text

````text
# Exploded View

- Climate Control Panel Without Display Courtesy of HONDA, U.S.A., INC. With Display Courtesy of HONDA, U.S.A., INC.

Without Display

Courtesy of HONDA, U.S.A., INC.

With Display

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8817: Exploded View

- Title: Exploded View
- Source path: `pages\11395.html`
- Chunk ID: `chunk_b9f7ad9f5bf6`
- Images: `images\GHH409368.jpeg`, `images\GHH409369.jpeg`, `images\GHH409370.jpeg`
- Duplicate sources: `pages\15466.html`

### Full Text

````text
# Exploded View

NOTE: If the packings and seals are damaged or torn, replace it with a new one.

- HVAC Unit Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8818: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11396.html`
- Chunk ID: `chunk_b2a29f399690`
- Images: none
- Duplicate sources: `pages\14624.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)

Symptom | Diagnostic Procedure | Also Check for

The blower and the heater controls and the A/C system do not work | Symptom Troubleshooting | Blown fuse No. B9 (10 A) in the under-dash fuse/relay box Poor ground at G505 Climate control unit Harness/connections

- Blown fuse No. B9 (10 A) in the under-dash fuse/relay box

- Poor ground at G505

- Climate control unit

- Harness/connections

The A/C compressor clutch and the A/C condenser/radiator fans are inoperative, but the blower and heater controls work | Probable cause: A/C pressure sensor circuit malfunction or evaporator temperature sensor circuit malfunction Troubleshoot the A/C pressure sensor circuit: A/C pressure sensor circuit low voltage A/C pressure sensor circuit high voltage NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC | Climate control DTCs PGM-FI DTCs Abnormal A/C system pressures Evaporator temperature sensor Harness/connections

Troubleshoot the A/C pressure sensor circuit:

- A/C pressure sensor circuit low voltage

- A/C pressure sensor circuit high voltage

NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC

- Climate control DTCs

- PGM-FI DTCs

- Abnormal A/C system pressures

- Evaporator temperature sensor

- Harness/connections

The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work | Symptom Troubleshooting | Climate control DTCs Blown fuse No. A23 (10 A) in the under-hood fuse/relay box A/C compressor clutch relay PCM Abnormal A/C system pressures Harness/connections

- Climate control DTCs

- Blown fuse No. A23 (10 A) in the under-hood fuse/relay box

- A/C compressor clutch relay

- PCM

- Abnormal A/C system pressures

- Harness/connections

The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally | Symptom Troubleshooting | Climate control DTCs PGM-FI DTCs Blown fuse No. A1-3 (30 A) in the under-hood fuse/relay box Poor ground at G401 Radiator fan relay Fan control relay Radiator fan motor A/C condenser fan motor PCM Harness/connections

- Climate control DTCs

- PGM-FI DTCs

- Blown fuse No. A1-3 (30 A) in the under-hood fuse/relay box

- Poor ground at G401

- Radiator fan relay

- Fan control relay

- Radiator fan motor

- A/C condenser fan motor

- PCM

- Harness/connections

The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on | Probable cause: Malfunction in the fan(s) high speed circuit Do the following troubleshooting as needed: Symptom Troubleshooting Radiator fan high speed circuit troubleshooting | Climate control DTCs PGM-FI DTCs Blown fuse No. A10 (20 A) in the under-hood fuse/relay box Blown fuse No. A11 (5 A) in the under-hood fuse/relay box A/C condenser fan relay PCM Harness/connections

Do the following troubleshooting as needed:

- Symptom Troubleshooting

- Radiator fan high speed circuit troubleshooting

- Climate control DTCs

- PGM-FI DTCs

- Blown fuse No. A10 (20 A) in the under-hood fuse/relay box

- Blown fuse No. A11 (5 A) in the under-hood fuse/relay box

- A/C condenser fan relay

- PCM

- Harness/connections

Blower fan runs slower than expected in cold weather (when in AUTO mode) NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode | Probable cause: Engine coolant temperature (ECT) circuit malfunction Troubleshoot the ECT sensor circuit: ECT sensor 1 circuit low voltage ECT sensor 1 circuit high voltage | Climate control DTCs PGM-FI DTCs Blower motor operation

NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode

Troubleshoot the ECT sensor circuit:

- ECT sensor 1 circuit low voltage

- ECT sensor 1 circuit high voltage

- Climate control DTCs

- PGM-FI DTCs

- Blower motor operation

*1: Without navigation

*2: With navigation

Symptom | Diagnostic Procedure | Also Check for
````

## Chunk 8819: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11396.html`
- Chunk ID: `chunk_88849fd6f189`
- Images: none
- Duplicate sources: `pages\14624.html`

### Full Text

````text
nnections

Blower fan runs slower than expected in cold weather (when in AUTO mode) NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode | Probable cause: Engine coolant temperature (ECT) circuit malfunction Troubleshoot the ECT sensor circuit: ECT sensor 1 circuit low voltage ECT sensor 1 circuit high voltage | Climate control DTCs PGM-FI DTCs Blower motor operation

NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode

Troubleshoot the ECT sensor circuit:

- ECT sensor 1 circuit low voltage

- ECT sensor 1 circuit high voltage

- Climate control DTCs

- PGM-FI DTCs

- Blower motor operation

*1: Without navigation

*2: With navigation

Symptom | Diagnostic Procedure | Also Check for

The A/C compressor clutch cycles rapidly on and off | Probable cause: A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off) Radiator and/or A/C condenser fan inoperative Low idle speed Evaporator temperature sensor malfunction Do the evaporator temperature sensor test | Climate control DTCs If there is no leak and the refrigerant level is normal, do the symptom troubleshooting , and look for an intermittent problem A/C pressure sensor

- A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off)

- Radiator and/or A/C condenser fan inoperative

- Low idle speed

- Evaporator temperature sensor malfunction Do the evaporator temperature sensor test

Do the evaporator temperature sensor test

- Climate control DTCs

- If there is no leak and the refrigerant level is normal, do the symptom troubleshooting , and look for an intermittent problem

- A/C pressure sensor

The A/C compressor clutch does not disengage when the A/C switch is off | Probable cause: The A/C compressor clutch circuit is on (energized) continuously, shorted to ground, stuck A/C compressor clutch relay, or the A/C compressor clutch is mechanically jammed Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch | The A/C compressor relief valve. If it has vented refrigerant to the atmosphere, correct the problem with the A/C compressor clutch or the A/C compressor clutch circuit, then replace the A/C compressor relief valve

Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch

The A/C compressor relief valve has vented refrigerant NOTE: This indicates the A/C system high side pressure was high | Probable cause: A high-side restriction, the A/C condenser/radiator fans are inoperative, or the A/C compressor clutch is not disengaging If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection If the A/C compressor clutch will not disengage, do the symptom troubleshooting , and check for mechanical problems If the fans is inoperative, do the symptom troubleshooting | PGM-FI DTCs

NOTE: This indicates the A/C system high side pressure was high

- If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection

Do the A/C system contamination inspection

- If the A/C compressor clutch will not disengage, do the symptom troubleshooting , and check for mechanical problems

- If the fans is inoperative, do the symptom troubleshooting

Driver's and passenger's side vent temperatures vary by more than 20 deg.F (11 deg.C) | Probable cause: The air mix doors are malfunctioning Do the following troubleshooting: - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control) Low refrigerant charge | Climate control DTCs Harness/connections

- The air mix doors are malfunctioning Do the following troubleshooting:

Do the following troubleshooting:

- - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control)

- - Air mix control motor test

Air mix control motor test

- - Passenger's air mix control motor test (with dual zone climate control)

Passenger's air mix control motor test (with dual zone climate control)

- Low refrigerant charge

- Climate control DTCs

- Harness/connections

HDS does not communicate with the climate control unit or the vehicle | Troubleshoot the DLC circuit
````

## Chunk 8820: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting Index (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11396.html`
- Chunk ID: `chunk_805723414160`
- Images: none
- Duplicate sources: `pages\14624.html`

### Full Text

````text
the following troubleshooting: - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control) Low refrigerant charge | Climate control DTCs Harness/connections

- The air mix doors are malfunctioning Do the following troubleshooting:

Do the following troubleshooting:

- - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control)

- - Air mix control motor test

Air mix control motor test

- - Passenger's air mix control motor test (with dual zone climate control)

Passenger's air mix control motor test (with dual zone climate control)

- Low refrigerant charge

- Climate control DTCs

- Harness/connections

HDS does not communicate with the climate control unit or the vehicle | Troubleshoot the DLC circuit

A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) | Probable cause: Communication malfunction between the audio unit *1 or the audio-navigation unit *2 and the climate control unit Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit | Climate control DTCs

Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Insufficient heating | Check the coolant level Check the expansion tank cap Check the engine coolant temperature (ECT) during normal operation with the HDS Check the heater core inlet hose temperature: If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core Check the operation of the air mix doors: Air mix control motor test Passenger's air mix control motor test (with dual zone climate control) Check the blower motor unit for obstructions Check for air leaks around the ducts and vents | Climate control DTCs

- Check the coolant level

- Check the expansion tank cap

- Check the engine coolant temperature (ECT) during normal operation with the HDS

- Check the heater core inlet hose temperature:

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump

- If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- Check the operation of the air mix doors:

- Air mix control motor test Passenger's air mix control motor test (with dual zone climate control)

- Air mix control motor test

- Passenger's air mix control motor test (with dual zone climate control)

- Check the blower motor unit for obstructions

- Check for air leaks around the ducts and vents

*1: Without navigation

*2: With navigation
````

## Chunk 8821: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)

- Title: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)
- Source path: `pages\11397.html`
- Chunk ID: `chunk_677265bd1c28`
- Images: none
- Duplicate sources: `pages\15297.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)

Symptom | Diagnostic Procedure | Also Check for

The blower and the heater controls and the A/C system do not work | Symptom Troubleshooting | Climate control DTCs Blown fuse No. B9 (10 A) in the under-dash fuse/relay box Poor ground at G505 Poor or loose connections at the terminals

- Climate control DTCs

- Blown fuse No. B9 (10 A) in the under-dash fuse/relay box

- Poor ground at G505

- Poor or loose connections at the terminals

The A/C compressor clutch and the cooling fan are inoperative, but the blower and heater controls work | Probable cause: A/C pressure sensor circuit malfunction or evaporator temperature sensor circuit malfunction Troubleshoot the A/C pressure sensor circuit: A/C pressure sensor circuit low voltage A/C pressure sensor circuit high voltage NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC | Climate control DTCs PGM-FI DTCs Abnormal A/C system pressures Faulty evaporator temperature sensor Poor or loose connections at the terminals

Troubleshoot the A/C pressure sensor circuit:

- A/C pressure sensor circuit low voltage

- A/C pressure sensor circuit high voltage

NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC

- Climate control DTCs

- PGM-FI DTCs

- Abnormal A/C system pressures

- Faulty evaporator temperature sensor

- Poor or loose connections at the terminals

The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work | Symptom Troubleshooting | Climate control DTCs Blown fuse No. A23 (10 A) in the under-hood fuse/relay box Abnormal A/C system pressures Poor or loose connections at the terminals

- Climate control DTCs

- Blown fuse No. A23 (10 A) in the under-hood fuse/relay box

- Abnormal A/C system pressures

- Poor or loose connections at the terminals

Blower fan runs slower than expected in cold weather (when in AUTO mode) NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode | Probable cause: Engine coolant temperature (ECT) circuit malfunction Troubleshoot the ECT sensor circuit: USA and Canada models - ECT sensor 2 circuit range/performance problem - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage Mexico models - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage | Climate control DTCs PGM-FI DTCs Blower motor operation

NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode

Troubleshoot the ECT sensor circuit:

- USA and Canada models

- - ECT sensor 2 circuit range/performance problem - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage

- - ECT sensor 2 circuit range/performance problem

ECT sensor 2 circuit range/performance problem

- - ECT sensor 2 circuit low voltage

ECT sensor 2 circuit low voltage

- - ECT sensor 2 circuit high voltage

ECT sensor 2 circuit high voltage

- Mexico models

- - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage

- - ECT sensor 2 circuit low voltage

ECT sensor 2 circuit low voltage

- - ECT sensor 2 circuit high voltage

ECT sensor 2 circuit high voltage

- Climate control DTCs

- PGM-FI DTCs

- Blower motor operation

The A/C compressor clutch cycles rapidly on and off | Probable cause: A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off) Cooling fan inoperative Low idle speed Evaporator temperature sensor malfunction Do the evaporator temperature sensor test | Climate control DTCs If there is no leak and the refrigerant level is normal, do the A/C compressor clutch circuit troubleshooting , and look for an intermittent problem Faulty A/C pressure sensor

- A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off)

- Cooling fan inoperative

- Low idle speed

- Evaporator temperature sensor malfunction Do the evaporator temperature sensor test

Do the evaporator temperature sensor test

- Climate control DTCs

- If there is no leak and the refrigerant level is normal, do the A/C compressor clutch circuit troubleshooting , and look for an intermittent problem

- Faulty A/C pressure sensor

*1: Without navigation

*2: With navigation

Symptom | Diagnostic Procedure | Also Check for
````

## Chunk 8822: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)

- Title: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)
- Source path: `pages\11397.html`
- Chunk ID: `chunk_ae77ff42a804`
- Images: none
- Duplicate sources: `pages\15297.html`

### Full Text

````text
t | Climate control DTCs If there is no leak and the refrigerant level is normal, do the A/C compressor clutch circuit troubleshooting , and look for an intermittent problem Faulty A/C pressure sensor

- A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off)

- Cooling fan inoperative

- Low idle speed

- Evaporator temperature sensor malfunction Do the evaporator temperature sensor test

Do the evaporator temperature sensor test

- Climate control DTCs

- If there is no leak and the refrigerant level is normal, do the A/C compressor clutch circuit troubleshooting , and look for an intermittent problem

- Faulty A/C pressure sensor

*1: Without navigation

*2: With navigation

Symptom | Diagnostic Procedure | Also Check for

The A/C compressor clutch does not disengage when the A/C switch is off | Probable cause: The A/C compressor clutch circuit is on (energized) continuously, shorted to ground, stuck A/C compressor clutch relay, or the A/C compressor clutch is mechanically jammed Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch | The A/C compressor relief valve. If it has vented refrigerant to the atmosphere, correct the problem with the A/C compressor clutch or the A/C compressor clutch circuit, then replace the A/C compressor relief valve

Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch

The A/C compressor relief valve has vented refrigerant NOTE: This indicates the A/C system high side pressure was high | Probable cause: A high-side restriction, the cooling fan is inoperative, or the A/C compressor clutch is not disengaging If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection If the A/C compressor clutch will not disengage, troubleshoot the A/C compressor clutch circuit , and check for mechanical problems If the cooling fan is inoperative, troubleshoot the RFC system malfunction | PGM-FI DTCs

NOTE: This indicates the A/C system high side pressure was high

- If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection

Do the A/C system contamination inspection

- If the A/C compressor clutch will not disengage, troubleshoot the A/C compressor clutch circuit , and check for mechanical problems

- If the cooling fan is inoperative, troubleshoot the RFC system malfunction

Driver's and passenger's side vent temperatures vary by more than 20 deg.F (11 deg.C) | Probable cause: The air mix doors are malfunctioning Do the following troubleshooting: - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control) Low refrigerant charge | Climate control DTCs Poor or loose connections at the terminals

- The air mix doors are malfunctioning Do the following troubleshooting:

Do the following troubleshooting:

- - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control)

- - Air mix control motor test

Air mix control motor test

- - Passenger's air mix control motor test (with dual zone climate control)

Passenger's air mix control motor test (with dual zone climate control)

- Low refrigerant charge

- Climate control DTCs

- Poor or loose connections at the terminals

HDS does not communicate with the climate control unit or the vehicle | Troubleshoot the DLC circuit

A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) | Probable cause: Communication malfunction between the audio unit *1 or the audio-navigation unit *2 and the climate control unit Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit | Climate control DTCs

Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Insufficient heating | Check the coolant level Check the expansion tank cap Check the engine coolant temperature (ECT) during normal operation with the HDS Check the heater core inlet hose temperature: If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core.
````

## Chunk 8823: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)

- Title: Climate Control System Symptom Troubleshooting Index (L15B7/K20C2/L15BA)
- Source path: `pages\11397.html`
- Chunk ID: `chunk_3689c44ed042`
- Images: none
- Duplicate sources: `pages\15297.html`

### Full Text

````text
trols work (climate control panel without display) | Probable cause: Communication malfunction between the audio unit *1 or the audio-navigation unit *2 and the climate control unit Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit | Climate control DTCs

Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Insufficient heating | Check the coolant level Check the expansion tank cap Check the engine coolant temperature (ECT) during normal operation with the HDS Check the heater core inlet hose temperature: If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core Check the operation of the air mix doors: Air mix control motor test Passenger's air mix control motor test (with dual zone climate control) Check the blower motor unit for obstructions Check for air leaks around the ducts and vents | Climate control DTCs

- Check the coolant level

- Check the expansion tank cap

- Check the engine coolant temperature (ECT) during normal operation with the HDS

- Check the heater core inlet hose temperature:

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump

- If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- Check the operation of the air mix doors:

- Air mix control motor test Passenger's air mix control motor test (with dual zone climate control)

- Air mix control motor test

- Passenger's air mix control motor test (with dual zone climate control)

- Check the blower motor unit for obstructions

- Check for air leaks around the ducts and vents

*1: Without navigation

*2: With navigation
````

## Chunk 8824: Climate Control System Component Location Index

- Title: Climate Control System Component Location Index
- Source path: `pages\11398.html`
- Chunk ID: `chunk_068f774a5172`
- Images: `images\GHH409114.jpeg`, `images\GHH409115.jpeg`, `images\GHH409116.jpeg`, `images\GHH409117.jpeg`
- Duplicate sources: `pages\13528.html`

### Full Text

````text
# Climate Control System Component Location Index

Courtesy of HONDA, U.S.A., INC.

Single Fan Type

Courtesy of HONDA, U.S.A., INC.

Dual Fan Type

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8825: Rear Window Defogger Component Location Index (2/4-door)

- Title: Rear Window Defogger Component Location Index (2/4-door)
- Source path: `pages\11399.html`
- Chunk ID: `chunk_c91bd8d62f83`
- Images: `images\GHH409118.jpeg`, `images\GHH409119.jpeg`, `images\GHH409120.jpeg`
- Duplicate sources: `pages\15802.html`

### Full Text

````text
# Rear Window Defogger Component Location Index (2/4-door)

2-door

Courtesy of HONDA, U.S.A., INC.

4-door

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8826: Rear Window Defogger Component Location Index (5-door) (2017 2018 2019 2020 2021)

- Title: Rear Window Defogger Component Location Index (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\11400.html`
- Chunk ID: `chunk_8bd537d20f51`
- Images: `images\GHH409121.jpeg`, `images\GHH409122.jpeg`
- Duplicate sources: `pages\15803.html`

### Full Text

````text
# Rear Window Defogger Component Location Index (5-door) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8827: A/C Refrigerant Oil Replacement (1234yf): Notes

- Title: A/C Refrigerant Oil Replacement (1234yf): Notes
- Source path: `pages\11401.html`
- Chunk ID: `chunk_cd8f44989d15`
- Images: `images\GHH178985.png`
- Duplicate sources: `pages\15804.html`

### Full Text

````text
# A/C Refrigerant Oil Replacement (1234yf): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R-1234yf POE Oil Injector ROB18470*

*Available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8828: A/C Refrigerant Oil Replacement (1234yf): Replacement

- Title: A/C Refrigerant Oil Replacement (1234yf): Replacement
- Source path: `pages\11402.html`
- Chunk ID: `chunk_33060c1ccd6f`
- Images: `images\GHH409123.jpeg`, `images\GHH409124.jpeg`, `images\GHH409125.jpeg`
- Duplicate sources: `pages\15805.html`

### Full Text

````text
# A/C Refrigerant Oil Replacement (1234yf): Replacement

- A/C Refrigerant Oil - Replace Recommended POE oil: RL85HM P/N 38899-RLV-A01: 40 m L(1 1/3 fl oz) It is important to have the correct amount of refrigerant oil in the A/C system to ensure proper lubrication of the A/C compressor. Too little oil damages the A/C compressor; too much oil reduces the cooling capacity of the system, and can produce high vent temperatures. To avoid contamination, do not return the oil to the container once dispensed, and never mix it with other refrigerant oils. Use the refrigerant oil immediately after opening the container, and dispose of any unused oil. The oil rapidly absorbs moisture, which damages its electrical insulating and lubricating properties. Do not spill the refrigerant oil on the vehicle, because it may damage painted surfaces. If refrigerant oil contacts the paint, wash it off with water immediately. Add the recommended refrigerant oil in the amount listed if you replace any of the following parts: Parts Oil Amount A/C condenser (USA and Canada production models) 50 mL (1 2/3 fl oz) A/C condenser (except USA and Canada production models) 25 mL (5/6 fl oz) Evaporator 40 mL (1 1/3 fl oz) Line or hose 10 mL (1/3 fl oz) Receiver/dryer 10 mL (1/3 fl oz) Leakage repair 25 mL (5/6 fl oz) A/C compressor 77-103 mL (2 3/5-3 1/2 fl oz)

Recommended POE oil: RL85HM

P/N 38899-RLV-A01: 40 m L(1 1/3 fl oz)

It is important to have the correct amount of refrigerant oil in the A/C system to ensure proper lubrication of the A/C compressor. Too little oil damages the A/C compressor; too much oil reduces the cooling capacity of the system, and can produce high vent temperatures.

- To avoid contamination, do not return the oil to the container once dispensed, and never mix it with other refrigerant oils.

- Use the refrigerant oil immediately after opening the container, and dispose of any unused oil. The oil rapidly absorbs moisture, which damages its electrical insulating and lubricating properties.

- Do not spill the refrigerant oil on the vehicle, because it may damage painted surfaces. If refrigerant oil contacts the paint, wash it off with water immediately.

Add the recommended refrigerant oil in the amount listed if you replace any of the following parts:

Parts | Oil Amount

A/C condenser (USA and Canada production models) | 50 mL (1 2/3 fl oz)

A/C condenser (except USA and Canada production models) | 25 mL (5/6 fl oz)

Evaporator | 40 mL (1 1/3 fl oz)

Line or hose | 10 mL (1/3 fl oz)

Receiver/dryer | 10 mL (1/3 fl oz)

Leakage repair | 25 mL (5/6 fl oz)

A/C compressor | 77-103 mL (2 3/5-3 1/2 fl oz)

- A/C Compressor Oil - Adjustment NOTE: Cover the pulley and clutch with plastic bag to prevent from spilling the oil. If no oil was drained from the removed A/C compressor, do not drain more than 50 mL (1 2/3 fl oz) from the new A/C compressor. Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. *1 Courtesy of HONDA, U.S.A., INC.

NOTE:

- Cover the pulley and clutch with plastic bag to prevent from spilling the oil.

- If no oil was drained from the removed A/C compressor, do not drain more than 50 mL (1 2/3 fl oz) from the new A/C compressor.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

*1

Courtesy of HONDA, U.S.A., INC.

- A/C Compressor Oil - Refill 1. Refill the oil from suction port.

1. Refill the oil from suction port.
````

## Chunk 8829: A/C Refrigerant Oil Replacement (134a): Notes

- Title: A/C Refrigerant Oil Replacement (134a): Notes
- Source path: `pages\11403.html`
- Chunk ID: `chunk_69c34b12c8a5`
- Images: `images\GHH17867.png`
- Duplicate sources: `pages\15806.html`

### Full Text

````text
# A/C Refrigerant Oil Replacement (134a): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Oil Injector Tool Robinair ROB16256, commercially available
````

## Chunk 8830: A/C Refrigerant Oil Replacement (134a): Replacement

- Title: A/C Refrigerant Oil Replacement (134a): Replacement
- Source path: `pages\11404.html`
- Chunk ID: `chunk_448a426c9e51`
- Images: `images\GHH399704.png`, `images\GHH400684.png`, `images\GHH409126.jpeg`, `images\GHH409127.jpeg`
- Duplicate sources: `pages\15807.html`

### Full Text

````text
# A/C Refrigerant Oil Replacement (134a): Replacement

- A/C Refrigerant Oil - Replace Recommended PAG oil: DENSO ND-OIL 8 P/N 38897-PR7-A01AH: 120 mL (4 fl oz) It is important to have the correct amount of refrigerant oil in the A/C system to ensure proper lubrication of the A/C compressor. Too little oil damages the A/C compressor; too much oil reduces the cooling capacity of the system, and can produce high vent temperatures. To avoid contamination, do not return the oil to the container once dispensed, and never mix it with other refrigerant oils. Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption. Do not spill the refrigerant oil on the vehicle, because it may damage painted surfaces. If refrigerant oil contacts the paint, wash it off with water immediately. Add the recommended refrigerant oil in the amount listed if you replace any of the following parts: Parts Oil Amount A/C condenser 50 mL (1 2/3 fl oz) Evaporator 40 mL (1 1/3 fl oz) Line or hose 10 mL (1/3 fl oz) Desiccant 10 mL (1/3 fl oz) Leakage repair 25 mL (5/6 fl oz) A/C compressor 77-103 mL (2 3/5-3 1/2 fl oz)

Recommended PAG oil: DENSO ND-OIL 8

P/N 38897-PR7-A01AH: 120 mL (4 fl oz)

It is important to have the correct amount of refrigerant oil in the A/C system to ensure proper lubrication of the A/C compressor. Too little oil damages the A/C compressor; too much oil reduces the cooling capacity of the system, and can produce high vent temperatures.

- To avoid contamination, do not return the oil to the container once dispensed, and never mix it with other refrigerant oils.

- Immediately after using the oil, reinstall the cap on the container, and seal it to avoid moisture absorption.

- Do not spill the refrigerant oil on the vehicle, because it may damage painted surfaces. If refrigerant oil contacts the paint, wash it off with water immediately.

Add the recommended refrigerant oil in the amount listed if you replace any of the following parts:

Parts | Oil Amount

A/C condenser | 50 mL (1 2/3 fl oz)

Evaporator | 40 mL (1 1/3 fl oz)

Line or hose | 10 mL (1/3 fl oz)

Desiccant | 10 mL (1/3 fl oz)

Leakage repair | 25 mL (5/6 fl oz)

A/C compressor | 77-103 mL (2 3/5-3 1/2 fl oz)

- A/C Compressor Oil - Adjustment NOTE: Cover the pulley and clutch with plastic bag to prevent from spilling the oil. If no oil was drained from the removed A/C compressor, do not drain more than 50 mL (1 2/3 fl oz) from the new A/C compressor. Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Torque: N.m (kgf.m, lbf.ft) Replace

NOTE:

- Cover the pulley and clutch with plastic bag to prevent from spilling the oil.

- If no oil was drained from the removed A/C compressor, do not drain more than 50 mL (1 2/3 fl oz) from the new A/C compressor.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Torque: N.m (kgf.m, lbf.ft)

Replace

- A/C Compressor Oil - Refill 1. Refill the oil from suction port.

1. Refill the oil from suction port.
````

## Chunk 8831: A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Notes

- Title: A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Notes
- Source path: `pages\11405.html`
- Chunk ID: `chunk_48d6e4097ad0`
- Images: `images\GHH178783.png`, `images\GHH178985.png`
- Duplicate sources: `pages\15808.html`

### Full Text

````text
# A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R-1234yf A/C Recover/Recycle/Recharge Machine ROB421234*

Courtesy of HONDA, U.S.A., INC. | R-1234yf POE Oil Injector ROB18470*

*These tools are available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8832: A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Procedure

- Title: A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Procedure
- Source path: `pages\11406.html`
- Chunk ID: `chunk_b6c4f841f225`
- Images: `images\GHH409128.jpeg`
- Duplicate sources: `pages\15809.html`

### Full Text

````text
# A/C Refrigerant Recovery/Evacuation/Charging (1234yf): Procedure

WARNING:

- Compressed air mixed with the HFO-1234yf (R-1234yf) forms a combustible vapor.

- The vapor can burn or explode causing serious injury.

- Never use compressed air to pressure test HFO-1234yf (R-1234yf) service equipment or vehicle air conditioning systems.

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

- Do not allow moisture to contaminate the A/C system oil. Moisture in the oil is difficult to remove, and it can damage the A/C compressor.

- Using an electronic vacuum gauge may decrease the required evacuation time because you can measure actual moisture level with this tool.

When an A/C System has been opened to the atmosphere, such as during installation or repair, it must be evacuated using an A/C recover/recycle/recharge machine. If the system has been open for several days, replace the receiver/dryer or the desiccant, drain the refrigerant oil , and add fresh oil. Then evacuate the system for several hours before charging it.

- A/C Recover/Recycle/Recharge Machine - Connect 1. Connect an A/C recover/recycle/recharge machine to the high-pressure service port (A) and the low-pressure service port (B), as shown, following the equipment manufacturer's instructions. Courtesy of HONDA, U.S.A., INC.

1. Connect an A/C recover/recycle/recharge machine to the high-pressure service port (A) and the low-pressure service port (B), as shown, following the equipment manufacturer's instructions.

Courtesy of HONDA, U.S.A., INC.

- A/C Refrigerant - Recover 1. Recover the refrigerant from the A/C system. 2. Measure the amount of refrigerant oil removed from the A/C system after the recovery process is completed. Be sure to put the same amount of new refrigerant oil back into the A/C system before charging.

1. Recover the refrigerant from the A/C system.

2. Measure the amount of refrigerant oil

removed from the A/C system after the recovery process is completed. Be sure to put the same amount of new refrigerant oil back into the A/C system before charging.

- A/C System - Evacuate 1. Evacuate the system. The vacuum pump should run for a minimum of 30 minutes or until the moisture vacuum test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump. 2. If the suction gauge does not reach approximately -93.3 kPa (-700 mmHg, -27.55 inHg) in 15 minutes or the moisture vacuum test fails, there is probably a leak in the system. Partially charge the system, and check for leaks.

1. Evacuate the system. The vacuum pump should run for a minimum of 30 minutes or until the moisture vacuum test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump.

2. If the suction gauge does not reach approximately -93.3 kPa (-700 mmHg, -27.55 inHg) in 15 minutes or the moisture vacuum test fails, there is probably a leak in the system. Partially charge the system, and check for leaks.

- A/C Refrigerant - Leak Check

- A/C Refrigerant - Charge 1. Charge the system with the specified amount of R-1234yf refrigerant. Do not overcharge the system; the A/C compressor will be damaged.Select the appropriate units of measure for your refrigerant A/C recover/recycle/recharge machine. Refrigerant Capacity: 375 to 425 g 13.23 to 14.99 oz 0.375 to 0.425 kg 0.827 to 0.937 lbs

1. Charge the system with the specified amount of R-1234yf refrigerant. Do not overcharge the system; the A/C compressor will be damaged.Select the appropriate units of measure for your refrigerant A/C recover/recycle/recharge machine.

Refrigerant Capacity:

375 to 425 g

13.23 to 14.99 oz

0.375 to 0.425 kg

0.827 to 0.937 lbs

- A/C Refrigerant - Leak Check

- A/C System - Test
````

## Chunk 8833: A/C Refrigerant Recovery/Evacuation/Charging (134a): Notes

- Title: A/C Refrigerant Recovery/Evacuation/Charging (134a): Notes
- Source path: `pages\11407.html`
- Chunk ID: `chunk_122bcfe48c76`
- Images: `images\GHH17868.png`, `images\GHH184360.png`, `images\GHH184432.png`
- Duplicate sources: `pages\15810.html`

### Full Text

````text
# A/C Refrigerant Recovery/Evacuation/Charging (134a): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Compact Electronic Vacuum Gauge Robinair ROB14777, commercially available

Courtesy of HONDA, U.S.A., INC. | R134a A/C Automatic Recover/Recycle/Recharge Machine ROB48920T, commercially available

Courtesy of HONDA, U.S.A., INC. | PAG Oil Injector Robinair ROB18480, commercially available

The tool ROB14777 is only required if you are not using the ROB48920T A/C recover/recycle/recharge machine which has a built-in thermistor (compact electronic) vacuum gauge.
````

## Chunk 8834: A/C Refrigerant Recovery/Evacuation/Charging (134a): Procedure

- Title: A/C Refrigerant Recovery/Evacuation/Charging (134a): Procedure
- Source path: `pages\11408.html`
- Chunk ID: `chunk_1b219affbae1`
- Images: `images\GHH409129.jpeg`
- Duplicate sources: `pages\15811.html`

### Full Text

````text
# A/C Refrigerant Recovery/Evacuation/Charging (134a): Procedure

WARNING:

- Compressed air mixed with the R-134a forms a combustible vapor.

- The vapor can burn or explode causing serious injury.

- Never use compressed air to pressure test R-134a service equipment or vehicle air conditioning systems.

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

- Do not allow moisture to contaminate the A/C system oil. Moisture in the oil is difficult to remove, and it can damage the A/C compressor.

- Using a thermistor (compact electronic) vacuum gauge may decrease the required evacuation time because you can measure actual moisture level with this tool.

A more efficient way to measure moisture removal is with a special tool called a thermistor (compact electronic) vacuum gauge, measuring vacuum levels in microns. The robinair 48920T (ROB48920T) A/C recover/recycle/recharge machine has a built-in thermistor (compact electronic) vacuum gauge. If you are using a different A/C recover/recycle/recharge machine, a separate gauge, such as the ROB14777 may be used.

Connect the tool according to the manufacturers instructions and allow the vacuum pump to run until the gauge reads 750 microns.

Shut off and isolate the vacuum pump, then observe the gauge reading:

- If the vacuum level remains stable at 750 microns for at least three minutes, all moisture in the system has been removed.

- A slow increase in the micron reading means there is still moisture boiling out of the system. Restart the vacuum pump and continue evacuating.

- A quick increase of micron levels indicates a leak is present in the system or your service equipment. Determine the cause and correct the leak before continuing.

When an A/C System has been opened to the atmosphere, such as during installation or repair, it must be evacuated using an A/C recover/recycle/recharge machine. If the system has been open for several days, replace the receiver/dryer or the desiccant, drain the refrigerant oil , and add fresh oil. Then evacuate the system for several hours before charging it.

- A/C Recover/Recycle/Recharge Machine - Connect 1. Connect an A/C recover/recycle/recharge machine to the high-pressure service port (A) and the low-pressure service port (B), as shown, following the equipment manufacturer's instructions. Courtesy of HONDA, U.S.A., INC.

1. Connect an A/C recover/recycle/recharge machine to the high-pressure service port (A) and the low-pressure service port (B), as shown, following the equipment manufacturer's instructions.

Courtesy of HONDA, U.S.A., INC.

- A/C Refrigerant - Recover 1. Recover the refrigerant from the A/C system. 2. Measure the amount of refrigerant oil removed from the A/C system after the recovery process is completed. Be sure to put the same amount of new refrigerant oil back into the A/C system before charging.

1. Recover the refrigerant from the A/C system.

2. Measure the amount of refrigerant oil

removed from the A/C system after the recovery process is completed. Be sure to put the same amount of new refrigerant oil back into the A/C system before charging.

- A/C System - Evacuate 1. Evacuate the system. The vacuum pump should run for a minimum of 30 minutes or until the moisture vacuum test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump. 2. If the suction gauge does not reach approximately -93.3 kPa (-700 mmHg, -27.55 inHg) in 15 minutes or the moisture vacuum test fails, there is probably a leak in the system. Partially charge the system, and check for leaks.

1. Evacuate the system. The vacuum pump should run for a minimum of 30 minutes or until the moisture vacuum test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump.

2.
````

## Chunk 8835: A/C Refrigerant Recovery/Evacuation/Charging (134a): Procedure

- Title: A/C Refrigerant Recovery/Evacuation/Charging (134a): Procedure
- Source path: `pages\11408.html`
- Chunk ID: `chunk_9f5d1390f05b`
- Images: `images\GHH409129.jpeg`
- Duplicate sources: `pages\15811.html`

### Full Text

````text
um test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump. 2. If the suction gauge does not reach approximately -93.3 kPa (-700 mmHg, -27.55 inHg) in 15 minutes or the moisture vacuum test fails, there is probably a leak in the system. Partially charge the system, and check for leaks.

1. Evacuate the system. The vacuum pump should run for a minimum of 30 minutes or until the moisture vacuum test passes, to eliminate all moisture from the system. When the suction gauge reads -93.3 kPa (-700 mmHg, -27.55 inHg) for at least 30 minutes, or the moisture vacuum test passes, close all valves, and turn off the vacuum pump.

2. If the suction gauge does not reach approximately -93.3 kPa (-700 mmHg, -27.55 inHg) in 15 minutes or the moisture vacuum test fails, there is probably a leak in the system. Partially charge the system, and check for leaks.

- A/C Refrigerant - Leak Check

- A/C Refrigerant - Charge 1. Charge the system with the specified amount of R-134a refrigerant. Do not overcharge the system; the A/C compressor will be damaged.Select the appropriate units of measure for your refrigerant A/C recover/recycle/recharge machine. Refrigerant Capacity: 405 to 455 g 14.29 to 16.05 oz 0.405 to 0.455 kg 0.893 to 1.003 lbs

1. Charge the system with the specified amount of R-134a refrigerant. Do not overcharge the system; the A/C compressor will be damaged.Select the appropriate units of measure for your refrigerant A/C recover/recycle/recharge machine.

Refrigerant Capacity:

405 to 455 g

14.29 to 16.05 oz

0.405 to 0.455 kg

0.893 to 1.003 lbs

- A/C Refrigerant - Leak Check

- A/C System - Test
````

## Chunk 8836: Climate Control Unit Connector for Inputs and Outputs

- Title: Climate Control Unit Connector for Inputs and Outputs
- Source path: `pages\11409.html`
- Chunk ID: `chunk_37a41ff1a180`
- Images: `images\GHH409130.jpeg`, `images\GHH409131.jpeg`
- Duplicate sources: `pages\13094.html`

### Full Text

````text
# Climate Control Unit Connector for Inputs and Outputs

Connector Index

Climate Control Unit Connector A (32P)

Climate Control Unit Connector B (24P)

Climate Control Unit Connector A (32P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal name | Description | Signal

1 | Not used | ---- | ----

2 | Not used | ---- | ----

3 | Not used | ---- | ----

4 | Not used | ---- | ----

5 | Not used | ---- | ----

6 | Not used | ---- | ----

7 | Not used | ---- | ----

8 | B-CAN_L | B-CAN communication signal | With vehicle in ON mode: pulses

9 | Not used | ---- | ----

10 *4 | TSUN | Detects sunlight sensor signal | With vehicle in ON mode, and no sunlight or the sensor covered up: 3.56 V With vehicle in ON mode, and sunlight on the sensor: less than 3.56 V

With vehicle in ON mode, and sunlight on the sensor: less than 3.56 V

11 | TAM | Detects outside air temperature sensor signal | With vehicle in ON mode: about 1.0-4.0 V (depending on outside air temperature)

12 | SENSOR COM | Sensor ground | With vehicle in ON mode: less than 0.2 V

13 | Not used | ---- | ----

14 *3 | SOL IN | Ground for A/C compressor variable capacity control solenoid | With vehicle in ON mode: less than 0.2 V

15 | Not used | ---- | ----

16 | Not used | ---- | ----

17 | Not used | ---- | ----

18 | Not used | ---- | ----

19 | Not used | ---- | ----

20 | Not used | ---- | ----

21 | RR DEF RLY CL- | Signal for rear window defogger relay | With vehicle in ON mode and rear window defogger/mirror defogger *5 switch ON: less than 0.2 V With vehicle in ON mode and rear window defogger/mirror defogger *5 switch OFF: battery voltage

With vehicle in ON mode and rear window defogger/mirror defogger *5 switch OFF: battery voltage

22 | Not used | ---- | ----

23 | Not used | ---- | ----

24 | Not used | ---- | ----

*1: L15B7/K20C2 engine

*2: L15BA/L15BY/K20C1 engine

*3: With A/C

*4: With automatic wiper or without automatic lighting

*5: With mirror defogger

Cavity | Terminal name | Description | Signal

25 | B-CAN_H | B-CAN communication signal | With vehicle in ON mode: pulses

26 | Not used | ---- | ----

27 | TR | Detects in-car temperature sensor signal | With vehicle in ON mode: about 1.0-4.0 V (depending on in-car temperature)

28 | GND | Ground for climate control unit (G505) | With vehicle in ON mode: less than 0.2 V

29 | BUS-DATA | BUS-DATA communication signal | ----

30 *3 | SOL OUT | Outputs 12 V to A/C compressor variable capacity control solenoid | Variable voltage based on cooling load. With A/C compressor at maximum: battery voltage

31 | Not used | ---- | ----

32 | IG2 A/C *1 | IG2 power source | With vehicle in ON mode: battery voltage

IG2 OPTION *2

*1: L15B7/K20C2 engine

*2: L15BA/L15BY/K20C1 engine

*3: With A/C

*4: With automatic wiper or without automatic lighting

*5: With mirror defogger

Climate Control Unit Connector B (24P)

Courtesy of HONDA, U.S.A., INC.

Cavity | Terminal name | Description | Signal

1 | S5V-H | Outputs sensor 5 V | With vehicle in ON mode: about 5.0 V

2 | AMD-P-DR | Detects potentiometer signal of air mix control motor (door position) | With vehicle in ON mode: about 0.5-4.5 V (depending on air mix control motor position)

3 *3 | AMD-P-AS | Detects potentiometer signal of passenger's air mix control motor (door position) | With vehicle in ON mode: about 0.5-4.5 V (depending on passenger's air mix control motor position)

4 | RFD-P | Detects potentiometer signal of recirculation control motor (door position) | With vehicle in ON mode: about 0.5-3.5 V (depending on recirculation control motor position

5 | MDD-P-DR | Detects potentiometer signal of mode control motor (door position) | With vehicle in ON mode: about 0.5-4.5 V (depending on mode control motor position)

6 | Not used | ---- | ----

7 | Not used | ---- | ----

8 *1 | T-EVA | Detects evaporator temperature sensor signal | With vehicle in ON mode: about 1.0-4.0 V (depending on evaporator temperature)

9 | Not used | ---- | ----

10 | SENS COM-H | Sensor ground | With vehicle in ON mode: less than 0.2 V

11 | BLOWER G | Outputs power transistor gate voltage | With vehicle in ON mode and fan control icon *4, fan control dial *2, or fan control button *3*4 OFF: less than 0.2 V With vehicle in ON mode and fan control icon *4, fan control dial *2, or fan control button *3*4 ON: about 4.0 V-battery voltage (depending on blower motor control)
````

## Chunk 8837: Climate Control Unit Connector for Inputs and Outputs

- Title: Climate Control Unit Connector for Inputs and Outputs
- Source path: `pages\11409.html`
- Chunk ID: `chunk_57cc2a86db50`
- Images: `images\GHH409130.jpeg`, `images\GHH409131.jpeg`
- Duplicate sources: `pages\13094.html`

### Full Text

````text
DR | Detects potentiometer signal of mode control motor (door position) | With vehicle in ON mode: about 0.5-4.5 V (depending on mode control motor position)

6 | Not used | ---- | ----

7 | Not used | ---- | ----

8 *1 | T-EVA | Detects evaporator temperature sensor signal | With vehicle in ON mode: about 1.0-4.0 V (depending on evaporator temperature)

9 | Not used | ---- | ----

10 | SENS COM-H | Sensor ground | With vehicle in ON mode: less than 0.2 V

11 | BLOWER G | Outputs power transistor gate voltage | With vehicle in ON mode and fan control icon *4, fan control dial *2, or fan control button *3*4 OFF: less than 0.2 V With vehicle in ON mode and fan control icon *4, fan control dial *2, or fan control button *3*4 ON: about 4.0 V-battery voltage (depending on blower motor control)

With vehicle in ON mode and fan control icon *4, fan control dial *2, or fan control button *3*4 ON: about 4.0 V-battery voltage (depending on blower motor control)

*1: With A/C

*2: Without dual zone climate control

*3: With dual zone climate control

*4: Climate control panel without display

Cavity | Terminal name | Description | Signal

12 | BLOWER V | Feedback signal of power transistor drain voltage | With vehicle in ON mode: about 0 V-battery voltage (depending on blower motor speed)

13 | M-HOT-DR | Output to drive air mix control motor to HOT side | With vehicle in ON mode and air mix control motor moving to HOT: battery voltage

14 | M-COOL-DR | Output to drive air mix control motor to COOL side | With vehicle in ON mode and air mix control motor moving to COOL: battery voltage

15 *3 | M-HOT-AS | Output to drive passenger'sair mix control motor to HOT side | With vehicle in ON mode and passenger's air mix control motor moving to HOT: battery voltage

16 *3 | M-COOL-AS | Output to drive passenger's air mix control motor to COOL side | With vehicle in ON mode and passenger's air mix control motor moving to COOL: battery voltage

17 | M-REC | Output to drive recirculation control motor to RECIRCULATE side | With vehicle in ON mode and recirculation control motor moving to RECIRCULATE: battery voltage

18 | M-FRS | Output to drive recirculation control motor to FRESH side | With vehicle in ON mode and recirculation control motor moving to FRESH: battery voltage

19 | M-VENT-DR | Outputs to drive mode control motor to VENT side | With vehicle in ON mode and mode control motor moving to VENT: battery voltage

20 | M-DEF-DR | Outputs to drive mode control motor to DEF side | With vehicle in ON mode and mode control motor moving to DEF: battery voltage

21 | Not used | ---- | ----

22 | Not used | ---- | ----

23 | Not used | ---- | ----

24 | Not used | ---- | ----

*1: With A/C

*2: Without dual zone climate control

*3: With dual zone climate control

*4: Climate control panel without display
````

## Chunk 8838: A/C Compressor Clutch Check: Check

- Title: A/C Compressor Clutch Check: Check
- Source path: `pages\11410.html`
- Chunk ID: `chunk_6e826a126343`
- Images: `images\GHH409132.jpeg`, `images\GHH409133.jpeg`, `images\GHH409134.jpeg`
- Duplicate sources: `pages\15812.html`

### Full Text

````text
# A/C Compressor Clutch Check: Check

- A/C Compressor Clutch Clearance - Check Courtesy of HONDA, U.S.A., INC. 1. Check the armature plate (A) for discoloration, peeling, or other damage. If there is damage, replace the clutch set . 2. Check the pulley (B) bearing play and drag by rotating the pulley by hand. Also check for grease leakage from the bearing. Replace the clutch set with a new one if it is noisy, has excessive play/drag, or has bearing grease contamination on the clutch faces. NOTE: The pulley and the armature plate were mated at the factory by a burnishing operation. Always replace the pulley and the plate as a set. Replacing only one part of the clutch set will cause clutch slippage. Courtesy of HONDA, U.S.A., INC. 3. Measure the clearance between the pulley (A) and the armature plate (B) all the way around. If the clearance is not within specified limits, remove the armature plate and add or remove shims as needed to increase or decrease clearance. Clearance: 0.30-0.60 mm (0.012-0.024 in) NOTE: The shims are available in three thicknesses: 0.3 mm, 0.4 mm, and 0.5 mm.

Courtesy of HONDA, U.S.A., INC. | 1. Check the armature plate (A) for discoloration, peeling, or other damage. If there is damage, replace the clutch set . 2. Check the pulley (B) bearing play and drag by rotating the pulley by hand. Also check for grease leakage from the bearing. Replace the clutch set with a new one if it is noisy, has excessive play/drag, or has bearing grease contamination on the clutch faces. NOTE: The pulley and the armature plate were mated at the factory by a burnishing operation. Always replace the pulley and the plate as a set. Replacing only one part of the clutch set will cause clutch slippage.

NOTE: The pulley and the armature plate were mated at the factory by a burnishing operation. Always replace the pulley and the plate as a set. Replacing only one part of the clutch set will cause clutch slippage.

Courtesy of HONDA, U.S.A., INC. | 3. Measure the clearance between the pulley (A) and the armature plate (B) all the way around. If the clearance is not within specified limits, remove the armature plate and add or remove shims as needed to increase or decrease clearance. Clearance: 0.30-0.60 mm (0.012-0.024 in) NOTE: The shims are available in three thicknesses: 0.3 mm, 0.4 mm, and 0.5 mm.

NOTE: The shims are available in three thicknesses: 0.3 mm, 0.4 mm, and 0.5 mm.

- A/C Compressor Clutch Field Coil - Check Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance of the field coil. If resistance is not within specifications, replace the field coil . Field Coil Resistance: 3.35-3.61 Ω at 68 deg.F (20 deg.C)

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance of the field coil. If resistance is not within specifications, replace the field coil . Field Coil Resistance: 3.35-3.61 Ω at 68 deg.F (20 deg.C)

- A/C Compressor Clutch Oil Leak Check 1. Remove the armature plate , and inspect the armature plate and pulley friction surface for wear. If there is excessive wear, roughness, or scoring, replace the clutch set . 2. Inspect the friction surfaces and the A/C compressor shaft hub for excess oil. If excess oil is present and it is not from the engine or other system, the A/C compressor shaft seal is leaking. In that case, replace the A/C compressor

1. Remove the armature plate , and inspect the armature plate and pulley friction surface for wear. If there is excessive wear, roughness, or scoring, replace the clutch set .

2. Inspect the friction surfaces and the A/C compressor shaft hub for excess oil. If excess oil is present and it is not from the engine or other system, the A/C compressor shaft seal is leaking. In that case, replace the A/C compressor
````

## Chunk 8839: A/C System Noise Check: Check

- Title: A/C System Noise Check: Check
- Source path: `pages\11411.html`
- Chunk ID: `chunk_3f09be471b4a`
- Images: none
- Duplicate sources: `pages\15813.html`

### Full Text

````text
# A/C System Noise Check: Check

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

The A/C system noise check will help you determine the source of abnormal A/C system noise.

NOTE:

- If an accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

- Identify the conditions when the noise occurs. The weather, the vehicle speed, the vehicle being in gear or in neutral, the engine temperature, or other conditions may be factors in determining the noise source.

- Do the A/C system inspection , and correct any problems found prior to diagnosing abnormal noises.

- Abnormal A/C noises can be misleading. For example, a sound similar to a failed bearing may be caused by loose fasteners or a faulty A/C compressor clutch assembly.

- Other System - Noise Check 1. Turn the vehicle to the OFF (LOCK) mode, and check the following. Correct any problems found. Drive belt - Excessive wear - Oil contamination - Improper belt routing Faulty belt tensioner Air inlet grille (in the cowl cover) for debris 2. Start the engine, run the A/C system, and check if the noise is coming from the following. Repair or replace any faulty components. Drive belt Belt tensioner Any of the pulleys

1. Turn the vehicle to the OFF (LOCK) mode, and check the following. Correct any problems found.

- Drive belt

- - Excessive wear - Oil contamination - Improper belt routing

- - Excessive wear

Excessive wear

- - Oil contamination

Oil contamination

- - Improper belt routing

Improper belt routing

- Faulty belt tensioner

- Air inlet grille (in the cowl cover) for debris

2. Start the engine, run the A/C system, and check if the noise is coming from the following. Repair or replace any faulty components.

- Drive belt

- Belt tensioner

- Any of the pulleys

- A/C System (Cabin) - Noise Check 1. Cycle the HVAC system through all blower speeds and all air distribution modes, and check for unusual noises and excessive vibration. If noise and/or vibration are present, do the following checks. NOTE: During this inspection, close the doors and windows, and do not start the engine. Check for Result Also Check for Conditions when the noise occurs The noise or vibration occurs only in a specific mode or setting. Check the operation of the air mix control motor, door, and linkage. Check the operation of the mode control motor, door, and linkage. Check the operation of the recirculation control motor, door, and linkage. There is a squeaking or chirping noise, but no unusual vibration. Replace the blower motor . Foreign material in the blower motor and fan Foreign material (leaves or twigs, for example) is present. Remove it, and recheck for noise. No foreign material (leaves or twigs, for example) is present. Remove the blower motor , and check these items below. Replace the blower motor if any problems are present. Damage on the fan blades Tightness of the fan retainer Fan alignment on the blower motor shaft

1. Cycle the HVAC system through all blower speeds and all air distribution modes, and check for unusual noises and excessive vibration. If noise and/or vibration are present, do the following checks.

NOTE: During this inspection, close the doors and windows, and do not start the engine.

Check for | Result | Also Check for

Conditions when the noise occurs | The noise or vibration occurs only in a specific mode or setting. | Check the operation of the air mix control motor, door, and linkage. Check the operation of the mode control motor, door, and linkage. Check the operation of the recirculation control motor, door, and linkage.

- Check the operation of the air mix control motor, door, and linkage.

- Check the operation of the mode control motor, door, and linkage.

- Check the operation of the recirculation control motor, door, and linkage.

There is a squeaking or chirping noise, but no unusual vibration. | Replace the blower motor .

Foreign material in the blower motor and fan | Foreign material (leaves or twigs, for example) is present. | Remove it, and recheck for noise.

No foreign material (leaves or twigs, for example) is present. | Remove the blower motor , and check these items below. Replace the blower motor if any problems are present.
````

## Chunk 8840: A/C System Noise Check: Check

- Title: A/C System Noise Check: Check
- Source path: `pages\11411.html`
- Chunk ID: `chunk_a8bf61c15aaa`
- Images: none
- Duplicate sources: `pages\15813.html`

### Full Text

````text
motor, door, and linkage. Check the operation of the mode control motor, door, and linkage. Check the operation of the recirculation control motor, door, and linkage.

- Check the operation of the air mix control motor, door, and linkage.

- Check the operation of the mode control motor, door, and linkage.

- Check the operation of the recirculation control motor, door, and linkage.

There is a squeaking or chirping noise, but no unusual vibration. | Replace the blower motor .

Foreign material in the blower motor and fan | Foreign material (leaves or twigs, for example) is present. | Remove it, and recheck for noise.

No foreign material (leaves or twigs, for example) is present. | Remove the blower motor , and check these items below. Replace the blower motor if any problems are present. Damage on the fan blades Tightness of the fan retainer Fan alignment on the blower motor shaft

- Damage on the fan blades

- Tightness of the fan retainer

- Fan alignment on the blower motor shaft

- A/C System (Under-Hood) - Noise Check 1. Set up the vehicle for the running A/C checks: Select a quiet area for testing. Apply the parking brake. Shift the vehicle to P, N position/mode, or Neutral. Start the engine. Set the A/C system to the following conditions: - Temperature control: MAX COOL - Mode control: VENT - Fan control: minimum (but not OFF) - A/C: ON 2. Switch the A/C compressor on and off several times to clearly identify the sound during A/C compressor operation. Listen to the noise while the A/C compressor clutch is engaged and disengaged. Probe the A/C system with a stethoscope to pinpoint the noise. NOTE: If the noise does not change when the A/C compressor clutch engages or disengages, the noise may be caused by an engine-related component. Probe the engine area with a stethoscope to pinpoint the noise. 3. Listen for noises coming from the A/C lines, the A/C hoses, the A/C condenser, the evaporator, the receiver/dryer, or the expansion valve, and check these items: Check for Result Also Check for Noises caused by A/C components touching other components or the body The noise is present Reroute or insulate the A/C component(s) as needed, and recheck for noise. Loose, damaged or excessively worn A/C components or mounting hardware Loose, damaged or excessively worn item is present Repair or replace the faulty component(s) or hardware, and recheck for noise. A moaning noise coming from the suction pipe and suction hose A moaning noise is present Check the system refrigerant charge. If the refrigerant charge is OK, replace the receiver/dryer . A whistling or hissing noise from the expansion valve A whistling or hissing noise is present Evacuate the system for 3 hours, then recheck. If the noise is still present, replace the expansion valve . 4. Check the operation of the A/C compressor clutch: Check for Result Also Check for The A/C compressor clutch engages without slipping when the A/C is switched on. Does slip Replace the A/C compressor clutch . Replace the A/C compressor also if there is a leak from the shaft seal. Does not engage Troubleshoot the A/C compressor clutch circuit . The A/C compressor clutch disengages when the A/C is switched off. Does not disengage Do the A/C compressor clutch check . If the A/C compressor clutch is OK, replace the A/C compressor . The A/C compressor clutch cycles on/off normally. Rapid on/off cycle Do the refrigerant leak check . If the refrigerant charge is OK, and there are no leaks, troubleshoot the A/C compressor clutch circuit . 5. Listen with a stethoscope for noises coming from the A/C compressor, and check these items: Check for Result Also Check for The noise changes when the A/C compressor clutch disengages (off). Does not change Check for the noise coming from the engine-related components. The A/C system operating pressures are normal. Abnormal Troubleshoot the problem using the pressure test table in the A/C system test . Correct the pressure-related problem(s), and recheck for noise. The A/C compressor hose connections and fasteners are in good condition. Loose, damaged, or excessively worn. Repair or replace the faulty component(s) or hardware, and recheck for noise. In good condition Replace the A/C compressor .

1. Set up the vehicle for the running A/C checks:

- Select a quiet area for testing.

- Apply the parking brake.

- Shift the vehicle to P, N position/mode, or Neutral.

- Start the engine.

- Set the A/C system to the following conditions:
````

## Chunk 8841: A/C System Noise Check: Check

- Title: A/C System Noise Check: Check
- Source path: `pages\11411.html`
- Chunk ID: `chunk_cfd31deebebe`
- Images: none
- Duplicate sources: `pages\15813.html`

### Full Text

````text
he A/C compressor clutch disengages (off). Does not change Check for the noise coming from the engine-related components. The A/C system operating pressures are normal. Abnormal Troubleshoot the problem using the pressure test table in the A/C system test . Correct the pressure-related problem(s), and recheck for noise. The A/C compressor hose connections and fasteners are in good condition. Loose, damaged, or excessively worn. Repair or replace the faulty component(s) or hardware, and recheck for noise. In good condition Replace the A/C compressor .

1. Set up the vehicle for the running A/C checks:

- Select a quiet area for testing.

- Apply the parking brake.

- Shift the vehicle to P, N position/mode, or Neutral.

- Start the engine.

- Set the A/C system to the following conditions:

- - Temperature control: MAX COOL - Mode control: VENT - Fan control: minimum (but not OFF) - A/C: ON

- - Temperature control: MAX COOL

Temperature control: MAX COOL

- - Mode control: VENT

Mode control: VENT

- - Fan control: minimum (but not OFF)

Fan control: minimum (but not OFF)

- - A/C: ON

A/C: ON

2. Switch the A/C compressor on and off several times to clearly identify the sound during A/C compressor operation. Listen to the noise while the A/C compressor clutch is engaged and disengaged. Probe the A/C system with a stethoscope to pinpoint the noise.

NOTE: If the noise does not change when the A/C compressor clutch engages or disengages, the noise may be caused by an engine-related component. Probe the engine area with a stethoscope to pinpoint the noise.

3. Listen for noises coming from the A/C lines, the A/C hoses, the A/C condenser, the evaporator, the receiver/dryer, or the expansion valve, and check these items:

Check for | Result | Also Check for

Noises caused by A/C components touching other components or the body | The noise is present | Reroute or insulate the A/C component(s) as needed, and recheck for noise.

Loose, damaged or excessively worn A/C components or mounting hardware | Loose, damaged or excessively worn item is present | Repair or replace the faulty component(s) or hardware, and recheck for noise.

A moaning noise coming from the suction pipe and suction hose | A moaning noise is present | Check the system refrigerant charge. If the refrigerant charge is OK, replace the receiver/dryer .

A whistling or hissing noise from the expansion valve | A whistling or hissing noise is present | Evacuate the system for 3 hours, then recheck. If the noise is still present, replace the expansion valve .

4. Check the operation of the A/C compressor clutch:

Check for | Result | Also Check for

The A/C compressor clutch engages without slipping when the A/C is switched on. | Does slip | Replace the A/C compressor clutch . Replace the A/C compressor also if there is a leak from the shaft seal.

- Replace the A/C compressor clutch .

- Replace the A/C compressor also if there is a leak from the shaft seal.

Does not engage | Troubleshoot the A/C compressor clutch circuit .

The A/C compressor clutch disengages when the A/C is switched off. | Does not disengage | Do the A/C compressor clutch check . If the A/C compressor clutch is OK, replace the A/C compressor .

The A/C compressor clutch cycles on/off normally. | Rapid on/off cycle | Do the refrigerant leak check . If the refrigerant charge is OK, and there are no leaks, troubleshoot the A/C compressor clutch circuit .

- Do the refrigerant leak check .

- If the refrigerant charge is OK, and there are no leaks, troubleshoot the A/C compressor clutch circuit .

5. Listen with a stethoscope for noises coming from the A/C compressor, and check these items:

Check for | Result | Also Check for

The noise changes when the A/C compressor clutch disengages (off). | Does not change | Check for the noise coming from the engine-related components.

The A/C system operating pressures are normal. | Abnormal | Troubleshoot the problem using the pressure test table in the A/C system test . Correct the pressure-related problem(s), and recheck for noise.

The A/C compressor hose connections and fasteners are in good condition. | Loose, damaged, or excessively worn. | Repair or replace the faulty component(s) or hardware, and recheck for noise.

In good condition | Replace the A/C compressor .
````

## Chunk 8842: A/C Service Tips and Precautions (1234yf)

- Title: A/C Service Tips and Precautions (1234yf)
- Source path: `pages\11412.html`
- Chunk ID: `chunk_99f5a3ea57d1`
- Images: `images\GHH409135.jpeg`, `images\GHH409136.jpeg`, `images\GHH409137.jpeg`, `images\GHH409138.jpeg`, `images\GHH409139.jpeg`
- Duplicate sources: `pages\15814.html`

### Full Text

````text
# A/C Service Tips and Precautions (1234yf)

WARNING:

- Compressed air mixed with the HFO-1234yf (R-1234yf) forms a combustible vapor.

- The vapor can burn or explode causing serious injury.

- Never use compressed air to pressure test HFO-1234yf (R-1234yf) service equipment or vehicle air conditioning systems.

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

The air conditioning system uses HFO-1234yf (R-1234yf) refrigerant and polyolester (POE) refrigerant oil .

Use only service equipment that is U.L.-listed and is certified to meet the requirements of SAE J639 to remove R-1234yf from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

R-1234yf service equipment or vehicle air conditioning systems should not be pressure tested or leak tested with compressed air.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

NOTE:

- The following label is found under the hood.

- The following illustration is an example. The value and the oil type of the actual vehicle may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.

Symbol | Symbol name

Courtesy of HONDA, U.S.A., INC. | Caution

Courtesy of HONDA, U.S.A., INC. | Inflammable refrigerant

Symbol | Symbol name

Courtesy of HONDA, U.S.A., INC. | Requires properly trained technician to service mobile A/C systems

Courtesy of HONDA, U.S.A., INC. | A/C system

- Always disconnect the negative cable from the 12 volt battery whenever replacing air conditioning parts.

- Keep moisture and dirt out of the system. When disconnecting any lines, plug or cap the fittings immediately; do not remove the caps or plugs until just before you reconnect each line.

- Before connecting any hose or line, apply a few drops of refrigerant oil to the O-ring.

- When tightening or loosening a fitting, use a second wrench to support the matching fitting.

- When discharging the system, use an R-1234yf refrigerant A/C recover/recycle/recharge machine; do not release refrigerant into the atmosphere.

- Servicing of an R-1234yf system should be done in well-ventilated work area.

- To ensure proper and safe operation, the Society of Automotive Engineers (SAE J2845) recommends that the refrigerant system only be serviced by trained and certified technicians.

- Never repair or replace the air conditioning evaporator (cooling coil) with one removed from a used or salvaged vehicle.

- New replacement mobile air conditioning evaporator must be certified (and labeled) as meeting SAE Standard J2842.

- Vented refrigerant is harmful to the environment.

- To avoid refrigerant from venting, never replace the evaporator with one removed from a used or salvaged vehicle.

- Refrigerant in your vehicle's air conditioning system is flammable and can be ignited during servicing if proper procedures are not followed.

- Requires a qualified technician to service.

- For safety system components should be replaced shall not be repaired or salvaged for reuse.
````

## Chunk 8843: A/C Service Tips and Precautions (134a)

- Title: A/C Service Tips and Precautions (134a)
- Source path: `pages\11413.html`
- Chunk ID: `chunk_ec015cbe9caa`
- Images: none
- Duplicate sources: `pages\15815.html`

### Full Text

````text
# A/C Service Tips and Precautions (134a)

WARNING:

- Compressed air mixed with the R-134a forms a combustible vapor.

- The vapor can burn or explode causing serious injury.

- Never use compressed air to pressure test R-134a service equipment or vehicle air conditioning systems.

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

The air conditioning system uses HFC-134a (R-134a) refrigerant and polyalkylene glycol (PAG) refrigerant oil .

Use only service equipment that is U.L.-listed and is certified to meet the requirements of SAE J2788 to remove R-134a from the air conditioning system.

If accidental system discharge occurs, ventilate the work area before resuming service.

R-134a service equipment or vehicle air conditioning systems should not be pressure tested or leak tested with compressed air.

Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

- Always disconnect the negative cable from the 12 volt battery whenever replacing air conditioning parts.

- Keep moisture and dirt out of the system. When disconnecting any lines, plug or cap the fittings immediately; do not remove the caps or plugs until just before you reconnect each line.

- Before connecting any hose or line, apply a few drops of refrigerant oil to the O-ring.

- When tightening or loosening a fitting, use a second wrench to support the matching fitting.

- When discharging the system, use an R-134a refrigerant A/C recover/recycle/recharge machine; do not release refrigerant into the atmosphere.
````

## Chunk 8844: A/C Compressor Variable Capacity Control Solenoid Test: Test

- Title: A/C Compressor Variable Capacity Control Solenoid Test: Test
- Source path: `pages\11414.html`
- Chunk ID: `chunk_f7d833d31e45`
- Images: `images\GHH409140.jpeg`
- Duplicate sources: `pages\15816.html`

### Full Text

````text
# A/C Compressor Variable Capacity Control Solenoid Test: Test

- A/C Compressor Variable Capacity Control Solenoid - Test Courtesy of HONDA, U.S.A., INC. 1. Measure the resistance between A/C compressor clutch 3P connector terminals No. 2 and No. 3. If the resistance is not within specifications, replace the A/C compressor . Variable Capacity Control Solenoid Resistance: 9.6-11.6 Ω at 68 deg.F(20 deg.C)

Courtesy of HONDA, U.S.A., INC. | 1. Measure the resistance between A/C compressor clutch 3P connector terminals No. 2 and No. 3. If the resistance is not within specifications, replace the A/C compressor .

Variable Capacity Control Solenoid Resistance: | 9.6-11.6 Ω at 68 deg.F(20 deg.C)
````

## Chunk 8845: A/C System Test (Except Type-R (1234yf)): Notes

- Title: A/C System Test (Except Type-R (1234yf)): Notes
- Source path: `pages\11415.html`
- Chunk ID: `chunk_63322c137770`
- Images: `images\GHH17873.png`, `images\GHH17874.png`, `images\GHH178783.png`
- Duplicate sources: `pages\15817.html`

### Full Text

````text
# A/C System Test (Except Type-R (1234yf)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R-1234yf A/C Recover/Recycle/Recharge Machine ROB421234*

Courtesy of HONDA, U.S.A., INC. | Big Digit Hygro-Thermometer PYR445703, commercially available

Courtesy of HONDA, U.S.A., INC. | Throttle Pedal Depressor Tool B240B, commercially available

*Available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8846: A/C System Test (Except Type-R (1234yf)): Test

- Title: A/C System Test (Except Type-R (1234yf)): Test
- Source path: `pages\11416.html`
- Chunk ID: `chunk_7866dcda9bfb`
- Images: `images\GHH409141.jpeg`, `images\GHH409142.jpeg`, `images\GHH409143.jpeg`, `images\GHH409144.jpeg`, `images\GHH409145.jpeg`, `images\GHH409146.jpeg`, `images\GHH409147.jpeg`
- Duplicate sources: `pages\15818.html`

### Full Text

````text
# A/C System Test (Except Type-R (1234yf)): Test

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

The performance test will help determine if the A/C system is operating within specifications.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

Performance Test

- A/C System - Inspect 1. Do the A/C system inspection , and correct any problems found.

1. Do the A/C system inspection , and correct any problems found.

- A/C Recover/Recycle/Recharge Machine - Connect

- Glove Box Back Cover - Remove

- A/C System - Test 1. Determine the relative humidity and air temperature. Courtesy of HONDA, U.S.A., INC. 2. Insert a thermometer (A) in the dashboard center vent. 3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct. 4. Test conditions: The blower intake temperature must be at least 68 deg.F (20 deg.C). Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly. Open the hood. Open the front doors. Apply the parking brake. Shift the vehicle to P, N position/mode, or Neutral. Start the engine. Set the A/C system to the following conditions. - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm. No driver or passengers in the vehicle. 5. Inspect the A/C components for the following conditions: A/C compressor clutch not engaged. Abnormal frost areas. Unusual noises. If you observe any of these conditions, refer to the Symptom Troubleshooting Index. 6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges. 7. To complete the vent (delivery)/blower intake temperature chart: Mark the vent (delivery) temperature on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line. NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. 8. To complete the high side (discharge) pressure/blower intake temperature chart: Mark the high side (discharge) pressure on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line. NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. 9. To complete the low side (suction) pressure/blower intake temperature chart: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.
````

## Chunk 8847: A/C System Test (Except Type-R (1234yf)): Test

- Title: A/C System Test (Except Type-R (1234yf)): Test
- Source path: `pages\11416.html`
- Chunk ID: `chunk_1f4dd1d5fd33`
- Images: `images\GHH409141.jpeg`, `images\GHH409142.jpeg`, `images\GHH409143.jpeg`, `images\GHH409144.jpeg`, `images\GHH409145.jpeg`, `images\GHH409146.jpeg`, `images\GHH409147.jpeg`
- Duplicate sources: `pages\15818.html`

### Full Text

````text
chart: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4. Test conditions:

- The blower intake temperature must be at least 68 deg.F (20 deg.C).

- Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly.

- Open the hood.

- Open the front doors.

- Apply the parking brake.

- Shift the vehicle to P, N position/mode, or Neutral.

- Start the engine.

- Set the A/C system to the following conditions.

- - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open

- - A/C: ON

A/C: ON

- - Temperature control: MAX COOL (Lo)

Temperature control: MAX COOL (Lo)

- - Mode control: VENT

Mode control: VENT

- - Recirculation control: RECIRCULATE

Recirculation control: RECIRCULATE

- - Fan control: Max

Fan control: Max

- - All vents: Open

All vents: Open

- Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm.

- No driver or passengers in the vehicle.

5. Inspect the A/C components for the following conditions:

- A/C compressor clutch not engaged.

- Abnormal frost areas.

- Unusual noises.

If you observe any of these conditions, refer to the Symptom Troubleshooting Index.

6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges.

7. To complete the vent (delivery)/blower intake temperature chart:

- Mark the vent (delivery) temperature on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line.

NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

8. To complete the high side (discharge) pressure/blower intake temperature chart:

- Mark the high side (discharge) pressure on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line.

NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

9. To complete the low side (suction) pressure/blower intake temperature chart:

- Mark the low side (suction) pressure along the vertical line.

- Mark the blower intake temperature along the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line.

NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

Pressure Test
````

## Chunk 8848: A/C System Test (Except Type-R (1234yf)): Test

- Title: A/C System Test (Except Type-R (1234yf)): Test
- Source path: `pages\11416.html`
- Chunk ID: `chunk_a2a70746f16d`
- Images: `images\GHH409141.jpeg`, `images\GHH409142.jpeg`, `images\GHH409143.jpeg`, `images\GHH409144.jpeg`, `images\GHH409145.jpeg`, `images\GHH409146.jpeg`, `images\GHH409147.jpeg`
- Duplicate sources: `pages\11418.html`, `pages\15818.html`, `pages\15820.html`

### Full Text

````text
side the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

9. To complete the low side (suction) pressure/blower intake temperature chart:

- Mark the low side (suction) pressure along the vertical line.

- Mark the blower intake temperature along the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line.

NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

Pressure Test

- A/C System Pressure - Test Test results Related symptoms Probable cause Driver and passenger's side A/C vent temperatures may vary by approximately 20 deg.F (11 deg.C) or more Suction pressure may be low Low refrigerant charge Expansion valve not opening sufficiently Driver's or passenger's air mix door DTCs present One air mix door stuck or inoperative Test results Related symptoms Probable cause Discharge pressure abnormally High Discharge pressure reduced when A/C condenser cooled with water spray Significant refrigerant overcharge Restricted/weak airflow through A/C condenser With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) Dirty A/C condenser or damaged fins Debris between A/C condenser and radiator RFC unit malfunctioning Discharge pressure abnormally Low Suction and discharge pressures equalize rapidly after stopping A/C compressor Suction pressure higher than normal Faulty A/C compressor Suction pressure abnormally Low Weak or insufficient airflow across evaporator Restricted blower intake or dust and pollen filter Suction pressure varies from near normal to a vacuum, as moisture freezes in expansion valve orifice Moisture in the system Faulty expansion valve Reduced airflow from vents Vent temperature is very low Evaporator freezing Faulty evaporator temperature sensor (check DTC) Faulty expansion valve or A/C compressor clutch relay stuck in the on position Suction pressure abnormally High Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Discharge pressure near normal Expansion valve stuck open or open too long Suction and Discharge pressures abnormally High Sheet of paper does not stick to front of A/C condenser surface with cooling fans on With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) RFC unit inoperative or wires reversed A/C compressor clutch remains engaged during off cycle Pressure relief valve may open Insufficient A/C compressor clutch clearance A/C compressor clutch relay stuck in the on position or circuit problem Excessive air in system Suction and Discharge pressures abnormally Low Suction line from expansion valve to A/C compressor is not cold Excessively low refrigerant charge Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Expansion valve clogged with debris/desiccant, stuck closed, or not opening sufficiently More than 18-29 deg.F (10-16 deg.C) temperature drop across A/C condenser inlet to outlet pipes Blocked or restricted A/C condenser internal passages or lines/components restricting refrigerant flow Significant temperature difference along high or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm Restriction in A/C suction or discharge lines or components (check temperatures to isolate) Test results Related symptoms Probable cause Suction pressure High and Discharge pressure Low Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off A/C compressor internal damage (Check for A/C system debris contamination) Suction and discharge pressures slightly low Vent temperature too high Slightly low refrigerant charge Excessive refrigerant oil in system Static pressures high with A/C system equalized. (After engine is off 4-12 hours) Air/Non-condensable gasses in system Contaminated or incorrect refrigerant

Test results | Related symptoms | Probable cause
````

## Chunk 8849: A/C System Test (Except Type-R (1234yf)): Test

- Title: A/C System Test (Except Type-R (1234yf)): Test
- Source path: `pages\11416.html`
- Chunk ID: `chunk_da2dad882284`
- Images: `images\GHH409141.jpeg`, `images\GHH409142.jpeg`, `images\GHH409143.jpeg`, `images\GHH409144.jpeg`, `images\GHH409145.jpeg`, `images\GHH409146.jpeg`, `images\GHH409147.jpeg`
- Duplicate sources: `pages\11418.html`, `pages\15818.html`, `pages\15820.html`

### Full Text

````text
or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm Restriction in A/C suction or discharge lines or components (check temperatures to isolate) Test results Related symptoms Probable cause Suction pressure High and Discharge pressure Low Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off A/C compressor internal damage (Check for A/C system debris contamination) Suction and discharge pressures slightly low Vent temperature too high Slightly low refrigerant charge Excessive refrigerant oil in system Static pressures high with A/C system equalized. (After engine is off 4-12 hours) Air/Non-condensable gasses in system Contaminated or incorrect refrigerant

Test results | Related symptoms | Probable cause

Driver and passenger's side A/C vent temperatures may vary by approximately 20 deg.F (11 deg.C) or more | Suction pressure may be low | Low refrigerant charge Expansion valve not opening sufficiently

- Low refrigerant charge

- Expansion valve not opening sufficiently

Driver's or passenger's air mix door DTCs present | One air mix door stuck or inoperative

Test results | Related symptoms | Probable cause

Discharge pressure abnormally High | Discharge pressure reduced when A/C condenser cooled with water spray | Significant refrigerant overcharge

Restricted/weak airflow through A/C condenser With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) | Dirty A/C condenser or damaged fins Debris between A/C condenser and radiator RFC unit malfunctioning

- Restricted/weak airflow through A/C condenser

- With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)

- Dirty A/C condenser or damaged fins

- Debris between A/C condenser and radiator

- RFC unit malfunctioning

Discharge pressure abnormally Low | Suction and discharge pressures equalize rapidly after stopping A/C compressor Suction pressure higher than normal | Faulty A/C compressor

- Suction and discharge pressures equalize rapidly after stopping A/C compressor

- Suction pressure higher than normal

Suction pressure abnormally Low | Weak or insufficient airflow across evaporator | Restricted blower intake or dust and pollen filter

Suction pressure varies from near normal to a vacuum, as moisture freezes in expansion valve orifice | Moisture in the system Faulty expansion valve

- Moisture in the system

- Faulty expansion valve

Reduced airflow from vents Vent temperature is very low | Evaporator freezing Faulty evaporator temperature sensor (check DTC) Faulty expansion valve or A/C compressor clutch relay stuck in the on position

- Reduced airflow from vents

- Vent temperature is very low

- Evaporator freezing

- Faulty evaporator temperature sensor (check DTC)

- Faulty expansion valve or A/C compressor clutch relay stuck in the on position

Suction pressure abnormally High | Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Discharge pressure near normal | Expansion valve stuck open or open too long

- Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air"

- Discharge pressure near normal

Suction and Discharge pressures abnormally High | Sheet of paper does not stick to front of A/C condenser surface with cooling fans on With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) | RFC unit inoperative or wires reversed

- Sheet of paper does not stick to front of A/C condenser surface with cooling fans on

- With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)

A/C compressor clutch remains engaged during off cycle Pressure relief valve may open | Insufficient A/C compressor clutch clearance A/C compressor clutch relay stuck in the on position or circuit problem Excessive air in system

- A/C compressor clutch remains engaged during off cycle

- Pressure relief valve may open

- Insufficient A/C compressor clutch clearance

- A/C compressor clutch relay stuck in the on position or circuit problem

- Excessive air in system
````

## Chunk 8850: A/C System Test (Except Type-R (1234yf)): Test

- Title: A/C System Test (Except Type-R (1234yf)): Test
- Source path: `pages\11416.html`
- Chunk ID: `chunk_5cb587cfa900`
- Images: `images\GHH409141.jpeg`, `images\GHH409142.jpeg`, `images\GHH409143.jpeg`, `images\GHH409144.jpeg`, `images\GHH409145.jpeg`, `images\GHH409146.jpeg`, `images\GHH409147.jpeg`
- Duplicate sources: `pages\11418.html`, `pages\15818.html`, `pages\15820.html`

### Full Text

````text
less than about 9 deg.F (5 deg.C) | RFC unit inoperative or wires reversed

- Sheet of paper does not stick to front of A/C condenser surface with cooling fans on

- With doors open, fresh air selected and cooling fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)

A/C compressor clutch remains engaged during off cycle Pressure relief valve may open | Insufficient A/C compressor clutch clearance A/C compressor clutch relay stuck in the on position or circuit problem Excessive air in system

- A/C compressor clutch remains engaged during off cycle

- Pressure relief valve may open

- Insufficient A/C compressor clutch clearance

- A/C compressor clutch relay stuck in the on position or circuit problem

- Excessive air in system

Suction and Discharge pressures abnormally Low | Suction line from expansion valve to A/C compressor is not cold | Excessively low refrigerant charge

Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" | Expansion valve clogged with debris/desiccant, stuck closed, or not opening sufficiently

More than 18-29 deg.F (10-16 deg.C) temperature drop across A/C condenser inlet to outlet pipes | Blocked or restricted A/C condenser internal passages or lines/components restricting refrigerant flow

Significant temperature difference along high or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm | Restriction in A/C suction or discharge lines or components (check temperatures to isolate)

NOTE: Some restrictions may not show up until 3, 000 rpm

Test results | Related symptoms | Probable cause

Suction pressure High and Discharge pressure Low | Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off | A/C compressor internal damage (Check for A/C system debris contamination)

- Excessive A/C compressor noise

- Pressures equalize quickly and noise after A/C compressor turns off

Suction and discharge pressures slightly low | Vent temperature too high | Slightly low refrigerant charge Excessive refrigerant oil in system

- Slightly low refrigerant charge

- Excessive refrigerant oil in system

Static pressures high with A/C system equalized. (After engine is off 4-12 hours) | Air/Non-condensable gasses in system Contaminated or incorrect refrigerant

- Air/Non-condensable gasses in system

- Contaminated or incorrect refrigerant
````

## Chunk 8851: A/C System Test (Except Type-R (134a)): Notes

- Title: A/C System Test (Except Type-R (134a)): Notes
- Source path: `pages\11417.html`
- Chunk ID: `chunk_8ac0813d237d`
- Images: `images\GHH17873.png`, `images\GHH17874.png`, `images\GHH184360.png`
- Duplicate sources: `pages\15819.html`

### Full Text

````text
# A/C System Test (Except Type-R (134a)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R134a A/C Automatic Recover/Recycle/Recharge Machine ROB48920T, commercially available

Courtesy of HONDA, U.S.A., INC. | Big Digit Hygro-Thermometer PYR445703, commercially available

Courtesy of HONDA, U.S.A., INC. | Throttle Pedal Depressor Tool B240B, commercially available

*Available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8852: A/C System Test (Except Type-R (134a)): Test

- Title: A/C System Test (Except Type-R (134a)): Test
- Source path: `pages\11418.html`
- Chunk ID: `chunk_47c68a149f77`
- Images: `images\GHH409148.jpeg`, `images\GHH409149.jpeg`, `images\GHH409150.jpeg`, `images\GHH409151.jpeg`, `images\GHH409152.jpeg`, `images\GHH409153.jpeg`, `images\GHH409154.jpeg`
- Duplicate sources: `pages\15820.html`

### Full Text

````text
# A/C System Test (Except Type-R (134a)): Test

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

The performance test will help determine if the A/C system is operating within specifications.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

Performance Test

- A/C System - Inspect 1. Do the A/C system inspection , and correct any problems found.

1. Do the A/C system inspection , and correct any problems found.

- A/C Recover/Recycle/Recharge Machine - Connect

- Glove Box Back Cover - Remove

- A/C System - Test 1. Determine the relative humidity and air temperature. Courtesy of HONDA, U.S.A., INC. 2. Insert a thermometer (A) in the dashboard center vent. 3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct. 4. Test conditions: The blower intake temperature must be at least 68 deg.F (20 deg.C). Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly. Open the hood. Open the front doors. Apply the parking brake. Shift the vehicle to P, N position/mode, or Neutral. Start the engine. Set the A/C system to the following conditions. - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm. No driver or passengers in the vehicle. 5. Inspect the A/C components for the following conditions: A/C compressor clutch not engaged. Abnormal frost areas. Unusual noises. If you observe any of these conditions, refer to the Symptom Troubleshooting Index. 6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges. 7. To complete the vent (delivery)/blower intake temperature chart: Mark the vent (delivery) temperature on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line. NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. 8. To complete the high side (discharge) pressure/blower intake temperature chart: Mark the high side (discharge) pressure on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line. NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. 9. To complete the low side (suction) pressure/blower intake temperature chart: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4.
````

## Chunk 8853: A/C System Test (Except Type-R (134a)): Test

- Title: A/C System Test (Except Type-R (134a)): Test
- Source path: `pages\11418.html`
- Chunk ID: `chunk_fe74d9bbc550`
- Images: `images\GHH409148.jpeg`, `images\GHH409149.jpeg`, `images\GHH409150.jpeg`, `images\GHH409151.jpeg`, `images\GHH409152.jpeg`, `images\GHH409153.jpeg`, `images\GHH409154.jpeg`
- Duplicate sources: `pages\15820.html`

### Full Text

````text
rt: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. 1.5 L Courtesy of HONDA, U.S.A., INC. 2.0 L Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4. Test conditions:

- The blower intake temperature must be at least 68 deg.F (20 deg.C).

- Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly.

- Open the hood.

- Open the front doors.

- Apply the parking brake.

- Shift the vehicle to P, N position/mode, or Neutral.

- Start the engine.

- Set the A/C system to the following conditions.

- - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open

- - A/C: ON

A/C: ON

- - Temperature control: MAX COOL (Lo)

Temperature control: MAX COOL (Lo)

- - Mode control: VENT

Mode control: VENT

- - Recirculation control: RECIRCULATE

Recirculation control: RECIRCULATE

- - Fan control: Max

Fan control: Max

- - All vents: Open

All vents: Open

- Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm.

- No driver or passengers in the vehicle.

5. Inspect the A/C components for the following conditions:

- A/C compressor clutch not engaged.

- Abnormal frost areas.

- Unusual noises.

If you observe any of these conditions, refer to the Symptom Troubleshooting Index.

6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges.

7. To complete the vent (delivery)/blower intake temperature chart:

- Mark the vent (delivery) temperature on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line.

NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

8. To complete the high side (discharge) pressure/blower intake temperature chart:

- Mark the high side (discharge) pressure on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line.

NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

9. To complete the low side (suction) pressure/blower intake temperature chart:

- Mark the low side (suction) pressure along the vertical line.

- Mark the blower intake temperature along the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line.

NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

1.5 L

Courtesy of HONDA, U.S.A., INC.

2.0 L

Courtesy of HONDA, U.S.A., INC.

Pressure Test
````

## Chunk 8854: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Notes

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Notes
- Source path: `pages\11419.html`
- Chunk ID: `chunk_d184c692cb0c`
- Images: `images\GHH17873.png`, `images\GHH17874.png`, `images\GHH178783.png`
- Duplicate sources: `pages\15821.html`

### Full Text

````text
# A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R-1234yf A/C Recover/Recycle/Recharge Machine ROB421234*

Courtesy of HONDA, U.S.A., INC. | Big Digit Hygro-Thermometer PYR445703, commercially available

Courtesy of HONDA, U.S.A., INC. | Throttle Pedal Depressor Tool B240B, commercially available

*Available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8855: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11420.html`
- Chunk ID: `chunk_1ce934f52db4`
- Images: `images\GHH409155.jpeg`, `images\GHH409156.jpeg`, `images\GHH409157.jpeg`, `images\GHH409158.jpeg`
- Duplicate sources: `pages\15822.html`

### Full Text

````text
# A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

The performance test will help determine if the A/C system is operating within specifications.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

Performance Test

- A/C System - Inspect 1. Do the A/C system inspection , and correct any problems found.

1. Do the A/C system inspection , and correct any problems found.

- A/C Recover/Recycle/Recharge Machine - Connect

- Glove Box Back Cover - Remove

- A/C System - Test 1. Determine the relative humidity and air temperature. Courtesy of HONDA, U.S.A., INC. 2. Insert a thermometer (A) in the dashboard center vent. 3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct. 4. Test conditions: The blower intake temperature must be at least 59 deg.F (15 deg.C). Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly. Open the hood. Open the front doors. Apply the parking brake. Shift the vehicle to Neutral. Start the engine. Set the A/C system to the following conditions. - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm. No driver or passengers in the vehicle. 5. Inspect the A/C components for the following conditions: A/C compressor clutch not engaged. Abnormal frost areas. Unusual noises. If you observe any of these conditions, refer to the Symptom Troubleshooting Index 6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges. 7. To complete the vent (delivery)/blower intake temperature chart: Mark the vent (delivery) temperature on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line. NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. 8. To complete the high side (discharge) pressure/blower intake temperature chart: Mark the high side (discharge) pressure on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line. NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. 9. To complete the low side (suction) pressure/blower intake temperature chart: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4. Test conditions:

- The blower intake temperature must be at least 59 deg.F (15 deg.C).
````

## Chunk 8856: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11420.html`
- Chunk ID: `chunk_b9f628c8e5d3`
- Images: `images\GHH409155.jpeg`, `images\GHH409156.jpeg`, `images\GHH409157.jpeg`, `images\GHH409158.jpeg`
- Duplicate sources: `pages\11422.html`, `pages\15822.html`, `pages\15824.html`

### Full Text

````text
g the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4. Test conditions:

- The blower intake temperature must be at least 59 deg.F (15 deg.C).

- Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly.

- Open the hood.

- Open the front doors.

- Apply the parking brake.

- Shift the vehicle to Neutral.

- Start the engine.

- Set the A/C system to the following conditions.

- - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open

- - A/C: ON

A/C: ON

- - Temperature control: MAX COOL (Lo)

Temperature control: MAX COOL (Lo)

- - Mode control: VENT

Mode control: VENT

- - Recirculation control: RECIRCULATE

Recirculation control: RECIRCULATE

- - Fan control: Max

Fan control: Max

- - All vents: Open

All vents: Open

- Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm.

- No driver or passengers in the vehicle.

5. Inspect the A/C components for the following conditions:

- A/C compressor clutch not engaged.

- Abnormal frost areas.

- Unusual noises.

If you observe any of these conditions, refer to the Symptom Troubleshooting Index

6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges.

7. To complete the vent (delivery)/blower intake temperature chart:

- Mark the vent (delivery) temperature on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line.

NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

Courtesy of HONDA, U.S.A., INC.

8. To complete the high side (discharge) pressure/blower intake temperature chart:

- Mark the high side (discharge) pressure on the vertical line.

- Mark the blower intake temperature on the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line.

NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

Courtesy of HONDA, U.S.A., INC.

9. To complete the low side (suction) pressure/blower intake temperature chart:

- Mark the low side (suction) pressure along the vertical line.

- Mark the blower intake temperature along the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line.

NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

Courtesy of HONDA, U.S.A., INC.

Pressure Test
````

## Chunk 8857: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11420.html`
- Chunk ID: `chunk_8295fbfb8b13`
- Images: `images\GHH409155.jpeg`, `images\GHH409156.jpeg`, `images\GHH409157.jpeg`, `images\GHH409158.jpeg`
- Duplicate sources: `pages\11422.html`, `pages\15822.html`, `pages\15824.html`

### Full Text

````text
essure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

Courtesy of HONDA, U.S.A., INC.

9. To complete the low side (suction) pressure/blower intake temperature chart:

- Mark the low side (suction) pressure along the vertical line.

- Mark the blower intake temperature along the bottom line.

- Draw a vertical line from the blower intake temperature mark.

- Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line.

NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection.

Courtesy of HONDA, U.S.A., INC.

Pressure Test

- A/C System Pressure - Test Test results Related symptoms Probable cause Driver and passenger's side A/C vent temperatures may vary by approximately 20 deg.F (11 deg.C) or more Suction pressure may be low Low refrigerant charge Expansion valve not opening sufficiently Driver's or passenger's air mix door DTCs present One air mix door stuck or inoperative Test results Related symptoms Probable cause Discharge pressure abnormally High Discharge pressure reduced when A/C condenser cooled with water spray Significant refrigerant overcharge Restricted/weak airflow through A/C condenser With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) Dirty A/C condenser or damaged fins Debris between A/C condenser and radiator Radiator and/or A/C condenser fan motor(s) malfunctioning Discharge pressure abnormally Low Suction and discharge pressures equalize rapidly after stopping A/C compressor Suction pressure higher than normal Faulty A/C compressor Suction pressure abnormally Low Weak or insufficient airflow across evaporator Restricted blower intake or dust and pollen filter Suction pressure varies from near normal to a vacuum, as moisture freezes in expansion valve orifice Moisture in the system Faulty expansion valve Reduced airflow from vents Vent temperature is very low Evaporator freezing Faulty evaporator temperature sensor (check DTC) Faulty expansion valve or A/C compressor clutch relay stuck in the on position Suction pressure abnormally High Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Discharge pressure near normal Expansion valve stuck open or open too long Suction and Discharge pressures abnormally High Sheet of paper does not stick to front of A/C condenser surface with cooling fans on With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) Radiator and/or A/C condenser fan motor(s) inoperative or wires reversed A/C compressor clutch remains engaged during off cycle Pressure relief valve may open Insufficient A/C compressor clutch clearance A/C compressor clutch relay stuck in the on position or circuit problem Excessive air in system Suction and Discharge pressures abnormally Low Suction line from expansion valve to A/C compressor is not cold Excessively low refrigerant charge Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Expansion valve clogged with debris/desiccant, stuck closed, or not opening sufficiently More than 18-29 deg.F (10-16 deg.C) temperature drop across A/C condenser inlet to outlet pipes Blocked or restricted A/C condenser internal passages or lines/components restricting refrigerant flow Significant temperature difference along high or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm Restriction in A/C suction or discharge lines or components (check temperatures to isolate) Test results Related symptoms Probable cause Suction pressure High and Discharge pressure Low Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off A/C compressor internal damage (Check for A/C system debris contamination) Suction and Discharge pressures slightly Low Vent temperature too high Slightly low refrigerant charge Excessive refrigerant oil in system Static pressures high with A/C system equalized.
````

## Chunk 8858: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11420.html`
- Chunk ID: `chunk_977e64ed24d3`
- Images: `images\GHH409155.jpeg`, `images\GHH409156.jpeg`, `images\GHH409157.jpeg`, `images\GHH409158.jpeg`
- Duplicate sources: `pages\11422.html`, `pages\15822.html`, `pages\15824.html`

### Full Text

````text
tlet pipes Blocked or restricted A/C condenser internal passages or lines/components restricting refrigerant flow Significant temperature difference along high or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm Restriction in A/C suction or discharge lines or components (check temperatures to isolate) Test results Related symptoms Probable cause Suction pressure High and Discharge pressure Low Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off A/C compressor internal damage (Check for A/C system debris contamination) Suction and Discharge pressures slightly Low Vent temperature too high Slightly low refrigerant charge Excessive refrigerant oil in system Static pressures high with A/C system equalized. (After engine is off 4-12 hours) Air/Non-condensable gasses in system Contaminated or incorrect refrigerant

Test results | Related symptoms | Probable cause

Driver and passenger's side A/C vent temperatures may vary by approximately 20 deg.F (11 deg.C) or more | Suction pressure may be low | Low refrigerant charge Expansion valve not opening sufficiently

- Low refrigerant charge

- Expansion valve not opening sufficiently

Driver's or passenger's air mix door DTCs present | One air mix door stuck or inoperative

Test results | Related symptoms | Probable cause

Discharge pressure abnormally High | Discharge pressure reduced when A/C condenser cooled with water spray | Significant refrigerant overcharge

Restricted/weak airflow through A/C condenser With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) | Dirty A/C condenser or damaged fins Debris between A/C condenser and radiator Radiator and/or A/C condenser fan motor(s) malfunctioning

- Restricted/weak airflow through A/C condenser

- With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)

- Dirty A/C condenser or damaged fins

- Debris between A/C condenser and radiator

- Radiator and/or A/C condenser fan motor(s) malfunctioning

Discharge pressure abnormally Low | Suction and discharge pressures equalize rapidly after stopping A/C compressor Suction pressure higher than normal | Faulty A/C compressor

- Suction and discharge pressures equalize rapidly after stopping A/C compressor

- Suction pressure higher than normal

Suction pressure abnormally Low | Weak or insufficient airflow across evaporator | Restricted blower intake or dust and pollen filter

Suction pressure varies from near normal to a vacuum, as moisture freezes in expansion valve orifice | Moisture in the system Faulty expansion valve

- Moisture in the system

- Faulty expansion valve

Reduced airflow from vents Vent temperature is very low | Evaporator freezing Faulty evaporator temperature sensor (check DTC) Faulty expansion valve or A/C compressor clutch relay stuck in the on position

- Reduced airflow from vents

- Vent temperature is very low

- Evaporator freezing

- Faulty evaporator temperature sensor (check DTC)

- Faulty expansion valve or A/C compressor clutch relay stuck in the on position

Suction pressure abnormally High | Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" Discharge pressure near normal | Expansion valve stuck open or open too long

- Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air"

- Discharge pressure near normal

Suction and Discharge pressures abnormally High | Sheet of paper does not stick to front of A/C condenser surface with cooling fans on With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) | Radiator and/or A/C condenser fan motor(s) inoperative or wires reversed

- Sheet of paper does not stick to front of A/C condenser surface with cooling fans on

- With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)
````

## Chunk 8859: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (1234yf)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11420.html`
- Chunk ID: `chunk_425e9e0dd1ac`
- Images: `images\GHH409155.jpeg`, `images\GHH409156.jpeg`, `images\GHH409157.jpeg`, `images\GHH409158.jpeg`
- Duplicate sources: `pages\11422.html`, `pages\15822.html`, `pages\15824.html`

### Full Text

````text
light suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air"

- Discharge pressure near normal

Suction and Discharge pressures abnormally High | Sheet of paper does not stick to front of A/C condenser surface with cooling fans on With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C) | Radiator and/or A/C condenser fan motor(s) inoperative or wires reversed

- Sheet of paper does not stick to front of A/C condenser surface with cooling fans on

- With doors open, fresh air selected and radiator and A/C condenser fan run on high speed, temperature drop across A/C condenser inlet to outlet is less than about 9 deg.F (5 deg.C)

A/C compressor clutch remains engaged during off cycle Pressure relief valve may open | Insufficient A/C compressor clutch clearance A/C compressor clutch relay stuck in the on position or circuit problem Excessive air in system

- A/C compressor clutch remains engaged during off cycle

- Pressure relief valve may open

- Insufficient A/C compressor clutch clearance

- A/C compressor clutch relay stuck in the on position or circuit problem

- Excessive air in system

Suction and Discharge pressures abnormally Low | Suction line from expansion valve to A/C compressor is not cold | Excessively low refrigerant charge

Lack of slight suction pressure variation at 1, 500 rpm when "Recirculated" airflow is switched to "Fresh Air" | Expansion valve clogged with debris/desiccant, stuck closed, or not opening sufficiently

More than 18-29 deg.F (10-16 deg.C) temperature drop across A/C condenser inlet to outlet pipes | Blocked or restricted A/C condenser internal passages or lines/components restricting refrigerant flow

Significant temperature difference along high or low side A/C lines or components NOTE: Some restrictions may not show up until 3, 000 rpm | Restriction in A/C suction or discharge lines or components (check temperatures to isolate)

NOTE: Some restrictions may not show up until 3, 000 rpm

Test results | Related symptoms | Probable cause

Suction pressure High and Discharge pressure Low | Excessive A/C compressor noise Pressures equalize quickly and noise after A/C compressor turns off | A/C compressor internal damage (Check for A/C system debris contamination)

- Excessive A/C compressor noise

- Pressures equalize quickly and noise after A/C compressor turns off

Suction and Discharge pressures slightly Low | Vent temperature too high | Slightly low refrigerant charge Excessive refrigerant oil in system

- Slightly low refrigerant charge

- Excessive refrigerant oil in system

Static pressures high with A/C system equalized. (After engine is off 4-12 hours) | Air/Non-condensable gasses in system Contaminated or incorrect refrigerant

- Air/Non-condensable gasses in system

- Contaminated or incorrect refrigerant
````

## Chunk 8860: A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Notes

- Title: A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Notes
- Source path: `pages\11421.html`
- Chunk ID: `chunk_e1125bd2f126`
- Images: `images\GHH17873.png`, `images\GHH17874.png`, `images\GHH184360.png`
- Duplicate sources: `pages\15823.html`

### Full Text

````text
# A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | R134a A/C Automatic Recover/Recycle/Recharge Machine ROB48920T, commercially available

Courtesy of HONDA, U.S.A., INC. | Big Digit Hygro-Thermometer PYR445703, commercially available

Courtesy of HONDA, U.S.A., INC. | Throttle Pedal Depressor Tool B240B, commercially available
````

## Chunk 8861: A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Test

- Title: A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11422.html`
- Chunk ID: `chunk_cf64cacbe53b`
- Images: `images\GHH409159.jpeg`, `images\GHH409160.jpeg`, `images\GHH409161.jpeg`, `images\GHH409162.jpeg`
- Duplicate sources: `pages\15824.html`

### Full Text

````text
# A/C System Test (Type-R (134a)) (2017 2018 2019 2020 2021): Test

WARNING:

- Air conditioning refrigerant or lubricant vapor can irritate your eyes, nose, or throat.

- Be careful when connecting service equipment.

- Do not breathe refrigerant or vapor.

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

The performance test will help determine if the A/C system is operating within specifications.

NOTE:

- If accidental system discharge occurs, ventilate the work area before resuming service.

- Additional health and safety information may be obtained from the refrigerant and lubricant manufacturers.

Performance Test

- A/C System - Inspect 1. Do the A/C system inspection , and correct any problems found.

1. Do the A/C system inspection , and correct any problems found.

- A/C Recover/Recycle/Recharge Machine - Connect

- Glove Box Back Cover - Remove

- A/C System - Test 1. Determine the relative humidity and air temperature. Courtesy of HONDA, U.S.A., INC. 2. Insert a thermometer (A) in the dashboard center vent. 3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct. 4. Test conditions: The blower intake temperature must be at least 59 deg.F (15 deg.C). Move the vehicle out of direct sunlight and let it cool down to the surrounding (ambient) temperature. If necessary, wash the vehicle to cool it down more quickly. Open the hood. Open the front doors. Apply the parking brake. Shift the vehicle to Neutral. Start the engine. Set the A/C system to the following conditions. - A/C: ON - Temperature control: MAX COOL (Lo) - Mode control: VENT - Recirculation control: RECIRCULATE - Fan control: Max - All vents: Open Use the throttle pedal depressor tool to run the engine at a steady 1, 500 rpm. No driver or passengers in the vehicle. 5. Inspect the A/C components for the following conditions: A/C compressor clutch not engaged. Abnormal frost areas. Unusual noises. If you observe any of these conditions, refer to the Symptom Troubleshooting Index 6. After running the air conditioning for 10 minutes under the test conditions, read the delivery temperature from the thermometer in the center vent, the blower intake temperature near the blower unit, and the discharge (high) and suction (low) pressures on the A/C gauges. 7. To complete the vent (delivery)/blower intake temperature chart: Mark the vent (delivery) temperature on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the vent (delivery) temperature mark until it intersects the vertical line. NOTE: The vent (delivery) temperature and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. 8. To complete the high side (discharge) pressure/blower intake temperature chart: Mark the high side (discharge) pressure on the vertical line. Mark the blower intake temperature on the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the high side (discharge) pressure mark until it intersects the vertical line. NOTE: The high side (discharge) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. 9. To complete the low side (suction) pressure/blower intake temperature chart: Mark the low side (suction) pressure along the vertical line. Mark the blower intake temperature along the bottom line. Draw a vertical line from the blower intake temperature mark. Draw a horizontal line from the low side (suction) pressure mark until it intersects the vertical line. NOTE: The low side (suction) pressure and blower intake temperature should intersect in the shaded area. Any measurements outside the line may indicate the need for further inspection. Courtesy of HONDA, U.S.A., INC. Pressure Test

1. Determine the relative humidity and air temperature.

Courtesy of HONDA, U.S.A., INC.

2. Insert a thermometer (A) in the dashboard center vent.

3. Place a hygro-thermometer (B) near the blower unit's recirculation inlet duct.

4. Test conditions:

- The blower intake temperature must be at least 59 deg.F (15 deg.C).
````

## Chunk 8862: Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Notes

- Title: Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Notes
- Source path: `pages\11423.html`
- Chunk ID: `chunk_cf19afe9aada`
- Images: `images\GHH17953.png`
- Duplicate sources: `pages\15825.html`

### Full Text

````text
# Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Backprobe Set 07SAZ-001000A*

*Available through the Honda Tool and Equipment Program; call 888-424-6857.
````

## Chunk 8863: Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Test

- Title: Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Test
- Source path: `pages\11424.html`
- Chunk ID: `chunk_e3a7a6bf50df`
- Images: `images\GHH409163.jpeg`, `images\GHH409164.jpeg`, `images\GHH409165.jpeg`, `images\GHH409166.jpeg`
- Duplicate sources: `pages\15826.html`

### Full Text

````text
# Air Mix Control Motor/Mode Control Motor/Recirculation Control Motor Test: Test

SRS components are located near the mode control motor and the recirculation control motor. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE:

- Before testing the motor, check for climate control DTCs .

- The air mix control motor and the driver's air mix control motor are the same parts.

- Part Removal for Motor Access NOTE: Numbers in table indicate parts removal order. Remove Parts Test Motor Air Mix Control Motor Passenger's Air Mix Control Motor * Mode Control Motor Recirculation Control Motor Driver's Dashboard Lower Cover [1] --- --- --- Glove Box Back Cover --- [1] [1] [1] Passenger's Heater Duct --- [2] [2] --- *: With dual zone climate control

NOTE: Numbers in table indicate parts removal order.

Remove Parts | Test Motor

Air Mix Control Motor | Passenger's Air Mix Control Motor * | Mode Control Motor | Recirculation Control Motor

Driver's Dashboard Lower Cover | [1] | --- | --- | ---

Glove Box Back Cover | --- | [1] | [1] | [1]

Passenger's Heater Duct | --- | [2] | [2] | ---

*: With dual zone climate control

- Connector Type The diagram below details the motor connector design used on this vehicle. Courtesy of HONDA, U.S.A., INC.

The diagram below details the motor connector design used on this vehicle.

Courtesy of HONDA, U.S.A., INC.

- Air Mix Control Motor, Passenger's Air Mix Control Motor, Mode Control Motor, and Recirculation Control Motor - Test 1. Disconnect the connector for necessary inspections. NOTICE: Incorrectly applying power and ground to the HVAC control motors will damage it. Follow the instructions carefully. 2. Test the motor in each direction by connecting a 12 volt battery power and ground at the connector according to the table. The motor should run smoothly, then stop. As soon as the motor stops, disconnect the 12 volt battery power immediately. Courtesy of HONDA, U.S.A., INC. 3. If any of the HVAC control motors did not run in step 2, remove it, then check the control linkage and door for smooth movement. If the linkage and doors move smoothly, go to step 4. If the linkage or door sticks or binds, repair them as needed. 4. Measure the resistance between terminals according to the table. Courtesy of HONDA, U.S.A., INC. 5. Reconnect the connector , which was removed in the step 1. 6. Turn the vehicle to the ON mode. 7. Using the backprobe set, measure the voltage between terminals according to the table. Courtesy of HONDA, U.S.A., INC. 8. If either the resistance or the voltage readings are not as specified, replace the faulty motor .

1. Disconnect the connector for necessary inspections.

NOTICE: Incorrectly applying power and ground to the HVAC control motors will damage it. Follow the instructions carefully.

2. Test the motor in each direction by connecting a 12 volt battery power and ground at the connector according to the table. The motor should run smoothly, then stop. As soon as the motor stops, disconnect the 12 volt battery power immediately.

Courtesy of HONDA, U.S.A., INC.

3. If any of the HVAC control motors did not run in step 2, remove it, then check the control linkage and door for smooth movement.

- If the linkage and doors move smoothly, go to step 4.

- If the linkage or door sticks or binds, repair them as needed.

4. Measure the resistance between terminals according to the table.

Courtesy of HONDA, U.S.A., INC.

5. Reconnect the connector

, which was removed in the step 1.

6. Turn the vehicle to the ON mode.

7. Using the backprobe set, measure the voltage between terminals according to the table.

Courtesy of HONDA, U.S.A., INC.

8. If either the resistance or the voltage readings are not as specified, replace the faulty motor .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8864: Blower Power Transistor Test: Test

- Title: Blower Power Transistor Test: Test
- Source path: `pages\11425.html`
- Chunk ID: `chunk_cd99232e021f`
- Images: `images\GHH409167.jpeg`, `images\GHH409168.jpeg`
- Duplicate sources: `pages\15827.html`

### Full Text

````text
# Blower Power Transistor Test: Test

NOTE: Before testing the power transistor, check for climate control DTCs .

- Glove Box - Remove

- Blower Power Transistor - Test Courtesy of HONDA, U.S.A., INC. 1. Disconnect the blower power transistor connector. 2. Measure the resistance between terminals No. 2 and No. 4 of the blower power transistor. It should be about 1.5 kΩ. If the resistance is within the specifications, go to step 3. If the resistance is not within the specifications, replace the blower power transistor . NOTE: Also check the blower motor. Blower power transistor failure can be caused by a defective blower motor. 3. Reconnect the blower power transistor connector. Courtesy of HONDA, U.S.A., INC. 4. Disconnect the following connectors. 5. Connect climate control unit connector A (32P) terminal No. 32 and climate control unit connector B (24P) terminal No. 11 with a jumper wire. 6. Turn the vehicle to the ON mode. 7. Check that the blower motor runs. If the blower motor does not run, replace the blower power transistor . NOTE: A faulty blower motor can cause the blower power transistor to fail. Before replacing the blower power transistor, check the blower motor for binding, and replace the blower motor if necessary . If the blower motor runs, the blower power transistor is OK. Climate control unit connector A (32P) Climate control unit connector B (24P)

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the blower power transistor connector. 2. Measure the resistance between terminals No. 2 and No. 4 of the blower power transistor. It should be about 1.5 kΩ. If the resistance is within the specifications, go to step 3. If the resistance is not within the specifications, replace the blower power transistor . NOTE: Also check the blower motor. Blower power transistor failure can be caused by a defective blower motor. 3. Reconnect the blower power transistor connector.

2. Measure the resistance between terminals No. 2 and No. 4 of the blower power transistor. It should be about 1.5 kΩ.

- If the resistance is within the specifications, go to step 3.

- If the resistance is not within the specifications, replace the blower power transistor . NOTE: Also check the blower motor. Blower power transistor failure can be caused by a defective blower motor.

NOTE: Also check the blower motor. Blower power transistor failure can be caused by a defective blower motor.

3. Reconnect the blower power transistor connector.

Courtesy of HONDA, U.S.A., INC. | 4. Disconnect the following connectors. 5. Connect climate control unit connector A (32P) terminal No. 32 and climate control unit connector B (24P) terminal No. 11 with a jumper wire. 6. Turn the vehicle to the ON mode. 7. Check that the blower motor runs. If the blower motor does not run, replace the blower power transistor . NOTE: A faulty blower motor can cause the blower power transistor to fail. Before replacing the blower power transistor, check the blower motor for binding, and replace the blower motor if necessary . If the blower motor runs, the blower power transistor is OK.

5. Connect climate control unit connector A (32P) terminal No. 32 and climate control unit connector B (24P) terminal No. 11 with a jumper wire.

6. Turn the vehicle to the ON mode.

7. Check that the blower motor runs.

- If the blower motor does not run, replace the blower power transistor . NOTE: A faulty blower motor can cause the blower power transistor to fail. Before replacing the blower power transistor, check the blower motor for binding, and replace the blower motor if necessary .

NOTE: A faulty blower motor can cause the blower power transistor to fail. Before replacing the blower power transistor, check the blower motor for binding, and replace the blower motor if necessary .

- If the blower motor runs, the blower power transistor is OK.

Climate control unit connector A (32P)

Climate control unit connector B (24P)

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8865: Radiator and A/C Condenser Fan Motor Test (K20C1) (2017 2018 2019 2020 2021): Test

- Title: Radiator and A/C Condenser Fan Motor Test (K20C1) (2017 2018 2019 2020 2021): Test
- Source path: `pages\11426.html`
- Chunk ID: `chunk_900071691e5b`
- Images: `images\GHH409169.jpeg`
- Duplicate sources: `pages\15828.html`

### Full Text

````text
# Radiator and A/C Condenser Fan Motor Test (K20C1) (2017 2018 2019 2020 2021): Test

- Fan Motor - Test Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connectors from the radiator fan motor (A) and the A/C condenser fan motor (B). 2. Test each motor by connecting 12 volt battery power to fan motor 2P connector (male terminals) terminal No. 1 and ground to fan motor 2P connector (male terminals) terminal No. 23. If a motor fails to run or does not run smoothly, replace it .

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connectors from the radiator fan motor (A) and the A/C condenser fan motor (B). 2. Test each motor by connecting 12 volt battery power to fan motor 2P connector (male terminals) terminal No. 1 and ground to fan motor 2P connector (male terminals) terminal No. 23. If a motor fails to run or does not run smoothly, replace it .

2. Test each motor by connecting 12 volt battery power to fan motor 2P connector (male terminals) terminal No. 1 and ground to fan motor 2P connector (male terminals) terminal No. 23. If a motor fails to run or does not run smoothly, replace it

.
````

## Chunk 8866: Sunlight Sensor Test: Test

- Title: Sunlight Sensor Test: Test
- Source path: `pages\11427.html`
- Chunk ID: `chunk_f7e12fa4757b`
- Images: `images\GHH409170.jpeg`
- Duplicate sources: `pages\15829.html`

### Full Text

````text
# Sunlight Sensor Test: Test

NOTE:

- Before testing the sensor, check for climate control DTCs .

- Be careful not to damage the sunlight sensor and the dashboard.

- Sunlight Sensor - Test Courtesy of HONDA, U.S.A., INC. 1. Pull out the sunlight sensor (A). 2. Turn the vehicle to the ON mode. 3. Measure the voltage between (+) probe on terminal No. 2 and (-) probe on terminal No. 1 with the connector connected. NOTE: The voltage readings will not change under the light of a flashlight or a fluorescent lamp. Voltage should be: 3.56 V with no sunlight or the sensor covered up Less than 3.56 V with sunlight on the sensor (depending on sunlight intensity) 4. If the voltage is not as specified, replace the sunlight sensor .

Courtesy of HONDA, U.S.A., INC. | 1. Pull out the sunlight sensor (A). 2. Turn the vehicle to the ON mode. 3. Measure the voltage between (+) probe on terminal No. 2 and (-) probe on terminal No. 1 with the connector connected. NOTE: The voltage readings will not change under the light of a flashlight or a fluorescent lamp. Voltage should be: 3.56 V with no sunlight or the sensor covered up Less than 3.56 V with sunlight on the sensor (depending on sunlight intensity) 4. If the voltage is not as specified, replace the sunlight sensor .

2. Turn the vehicle to the ON mode.

3. Measure the voltage between (+) probe on terminal No. 2 and (-) probe on terminal No. 1 with the connector connected.

NOTE: The voltage readings will not change under the light of a flashlight or a fluorescent lamp. Voltage should be:

- 3.56 V with no sunlight or the sensor covered up

- Less than 3.56 V with sunlight on the sensor (depending on sunlight intensity)

4. If the voltage is not as specified, replace the sunlight sensor .
````

## Chunk 8867: A/C System Contamination Inspection: Inspection

- Title: A/C System Contamination Inspection: Inspection
- Source path: `pages\11428.html`
- Chunk ID: `chunk_64175937a3a3`
- Images: `images\GHH409171.jpeg`
- Duplicate sources: `pages\15830.html`

### Full Text

````text
# A/C System Contamination Inspection: Inspection

NOTE:

- If the A/C compressor failure is diagnosed, always use this inspection to check the extent of contamination in the A/C system.

- The parts illustrations are sample. External appearance may vary from model to model.

- A/C System Contamination - Inspect Remove a part from the related parts as described in the table. Then, swab inside the part with a cotton swab to see if there is metal, dark grey or black residue. Courtesy of HONDA, U.S.A., INC. Step Part to Remove Inspection Area Metal, Dark Grey or Black Residue Contamination No Contamination Found 1 Discharge hose (A/C compressor side) Discharge port (A) Go to step 2. No contamination is present from the A/C compressor. Replace only the A/C compressor . 2 Suction hose (A/C compressor side) Suction port (B) Replace the components in Repair Procedure D. Go to step 3. 3 Receiver line (A/C condenser outlet) A/C condenser outlet port (C) Go to step 4. Go to step 5. 4 Receiver line and suction pipe (Both are expansion valve side) Expansion valve port (D) Replace the components in Repair Procedure D. Replace the components in Repair Procedure C. 5 Discharge hose (A/C condenser inlet) A/C condenser inlet port (E) Replace the components in Repair Procedure B. Replace the components in Repair Procedure A.

Remove a part from the related parts as described in the table. Then, swab inside the part with a cotton swab to see if there is metal, dark grey or black residue.

Courtesy of HONDA, U.S.A., INC.

Step | Part to Remove | Inspection Area | Metal, Dark Grey or Black Residue

Contamination | No Contamination Found

1 | Discharge hose (A/C compressor side) | Discharge port (A) | Go to step 2. | No contamination is present from the A/C compressor. Replace only the A/C compressor .

2 | Suction hose (A/C compressor side) | Suction port (B) | Replace the components in Repair Procedure D. | Go to step 3.

3 | Receiver line (A/C condenser outlet) | A/C condenser outlet port (C) | Go to step 4. | Go to step 5.

4 | Receiver line and suction pipe (Both are expansion valve side) | Expansion valve port (D) | Replace the components in Repair Procedure D. | Replace the components in Repair Procedure C.

5 | Discharge hose (A/C condenser inlet) | A/C condenser inlet port (E) | Replace the components in Repair Procedure B. | Replace the components in Repair Procedure A.
````

## Chunk 8868: A/C System Contamination Inspection: Replacement

- Title: A/C System Contamination Inspection: Replacement
- Source path: `pages\11429.html`
- Chunk ID: `chunk_8d51b8b00dd8`
- Images: `images\GHH409172.jpeg`, `images\GHH409173.jpeg`, `images\GHH409174.jpeg`, `images\GHH409175.jpeg`
- Duplicate sources: `pages\15831.html`

### Full Text

````text
# A/C System Contamination Inspection: Replacement

NOTE: The parts illustrations are sample. External appearance may vary from model to model.

- A/C Components - Replace Courtesy of HONDA, U.S.A., INC. Repair Procedure A Replace the following parts: A/C compressor (A) Discharge hose (B) Courtesy of HONDA, U.S.A., INC. Repair Procedure B Replace the following parts: A/C compressor (A) Discharge hose (B) A/C condenser (C) Courtesy of HONDA, U.S.A., INC. Repair Procedure C Replace the following parts: A/C compressor (A) Discharge hose (B) A/C condenser (C) Receiver line (D) Courtesy of HONDA, U.S.A., INC. Repair Procedure D Replace the following parts: A/C compressor (A) A/C condenser (B) Expansion valve (C) Evaporator core (D) All A/C hoses and lines

Courtesy of HONDA, U.S.A., INC.

Repair Procedure A

Replace the following parts:

- A/C compressor (A)

- Discharge hose (B)

Courtesy of HONDA, U.S.A., INC.

Repair Procedure B

Replace the following parts:

- A/C compressor (A)

- Discharge hose (B)

- A/C condenser (C)

Courtesy of HONDA, U.S.A., INC.

Repair Procedure C

Replace the following parts:

- A/C compressor (A)

- Discharge hose (B)

- A/C condenser (C)

- Receiver line (D)

Courtesy of HONDA, U.S.A., INC.

Repair Procedure D

Replace the following parts:

- A/C compressor (A)

- A/C condenser (B)

- Expansion valve (C)

- Evaporator core (D)

- All A/C hoses and lines
````

## Chunk 8869: A/C System Inspection: Inspection

- Title: A/C System Inspection: Inspection
- Source path: `pages\11430.html`
- Chunk ID: `chunk_290f14086539`
- Images: none
- Duplicate sources: `pages\15832.html`

### Full Text

````text
# A/C System Inspection: Inspection

NOTE:

- For A/C system noise, go to the A/C System Noise Check .

- Check for climate control DTCs using the Self-Diagnostic Function. If there are any DTCs, go to the appropriate troubleshooting .

- A/C System - Inspect Before troubleshooting any problem with the A/C system, do the following to check if there is anything wrong with the A/C system. If any malfunctions are found while performing the checks, correct them referring to "Actions to take" in the table given below. Inspection Area Check for Actions to Take Fresh air intake for the HVAC unit (at the base of the windshield) Leaves or debris blocking the air intake Remove any blockage. A/C lines and hoses Kinks or sharp bends Replace the A/C lines and hoses that are kinked or bent. A/C components A/C lines and hoses Stains at the components or joints that may indicate a refrigerant or an A/C compressor oil leak Do the Refrigerant Leak Check to confirm the leak(s). Drive belt Signs of slippage Damage Inspect the drive belt . A/C condenser Dirt in the fins, or material clogging the fins (dirt, insects, etc.) Clean the fins NOTE: Carefully clean any material from the A/C condenser fins with water and detergent. Do not perform pressure test until the condenser is completely dry. Fin damage, bent fins Try to comb them straight NOTE: If the fins cannot be straightened, replace the A/C condenser . Visible damage to the A/C condenser Do the Refrigerant Leak Check to check for leaks. If the A/C condenser is leaking, replace the A/C condenser . A/C compressor clutch armature plate engagement Check that the A/C compressor clutch armature plate engages and is rotating at the same speed as the clutch pulley. Refer to the symptom troubleshooting . Do the A/C Compressor Clutch Check . Cooling fan *1 Check that the cooling fan operates when the A/C compressor clutch is engaged and blow air toward the engine compartment. Refer to the symptom troubleshooting . A/C condenser fan and radiator fan *2 Check that the radiator and A/C condenser fans operate when the A/C compressor clutch is engaged and blow air toward the engine compartment. Refer to the symptom troubleshooting . Do the fan motor test . *1: Single fan type *2: Dual fan type Inspection Area Check for Actions to Take Dust and pollen filter The dust and pollen filter is clogged or restricted. Replace the dust and pollen filter . Blower fan Check that the A/C operates at each position of the fan control icon (except OFF). If the A/C does not operate at all fan control icon positions, refer to the symptom troubleshooting. NOTE: Start the engine, turn the A/C system on, and allow it to run for a few minutes and reach stable operation. Refer to the symptom troubleshooting . *1: Single fan type *2: Dual fan type

Before troubleshooting any problem with the A/C system, do the following to check if there is anything wrong with the A/C system. If any malfunctions are found while performing the checks, correct them referring to "Actions to take" in the table given below.

Inspection Area | Check for | Actions to Take

Fresh air intake for the HVAC unit (at the base of the windshield) | Leaves or debris blocking the air intake | Remove any blockage.

A/C lines and hoses | Kinks or sharp bends | Replace the A/C lines and hoses that are kinked or bent.

A/C components A/C lines and hoses | Stains at the components or joints that may indicate a refrigerant or an A/C compressor oil leak | Do the Refrigerant Leak Check to confirm the leak(s).

- A/C components

- A/C lines and hoses

Drive belt | Signs of slippage Damage | Inspect the drive belt .

- Signs of slippage

- Damage

A/C condenser | Dirt in the fins, or material clogging the fins (dirt, insects, etc.) | Clean the fins NOTE: Carefully clean any material from the A/C condenser fins with water and detergent. Do not perform pressure test until the condenser is completely dry.

NOTE:

- Carefully clean any material from the A/C condenser fins with water and detergent.

- Do not perform pressure test until the condenser is completely dry.

Fin damage, bent fins | Try to comb them straight NOTE: If the fins cannot be straightened, replace the A/C condenser .

NOTE: If the fins cannot be straightened, replace the A/C condenser .

Visible damage to the A/C condenser | Do the Refrigerant Leak Check to check for leaks. If the A/C condenser is leaking, replace the A/C condenser .
````

## Chunk 8870: A/C System Inspection: Inspection

- Title: A/C System Inspection: Inspection
- Source path: `pages\11430.html`
- Chunk ID: `chunk_f5bb866df257`
- Images: none
- Duplicate sources: `pages\15832.html`

### Full Text

````text
.

- Signs of slippage

- Damage

A/C condenser | Dirt in the fins, or material clogging the fins (dirt, insects, etc.) | Clean the fins NOTE: Carefully clean any material from the A/C condenser fins with water and detergent. Do not perform pressure test until the condenser is completely dry.

NOTE:

- Carefully clean any material from the A/C condenser fins with water and detergent.

- Do not perform pressure test until the condenser is completely dry.

Fin damage, bent fins | Try to comb them straight NOTE: If the fins cannot be straightened, replace the A/C condenser .

NOTE: If the fins cannot be straightened, replace the A/C condenser .

Visible damage to the A/C condenser | Do the Refrigerant Leak Check to check for leaks. If the A/C condenser is leaking, replace the A/C condenser .

A/C compressor clutch armature plate engagement | Check that the A/C compressor clutch armature plate engages and is rotating at the same speed as the clutch pulley. | Refer to the symptom troubleshooting . Do the A/C Compressor Clutch Check .

- Refer to the symptom troubleshooting .

- Do the A/C Compressor Clutch Check .

Cooling fan *1 | Check that the cooling fan operates when the A/C compressor clutch is engaged and blow air toward the engine compartment. | Refer to the symptom troubleshooting .

A/C condenser fan and radiator fan *2 | Check that the radiator and A/C condenser fans operate when the A/C compressor clutch is engaged and blow air toward the engine compartment. | Refer to the symptom troubleshooting . Do the fan motor test .

- Refer to the symptom troubleshooting .

- Do the fan motor test .

*1: Single fan type

*2: Dual fan type

Inspection Area | Check for | Actions to Take

Dust and pollen filter | The dust and pollen filter is clogged or restricted. | Replace the dust and pollen filter .

Blower fan | Check that the A/C operates at each position of the fan control icon (except OFF). If the A/C does not operate at all fan control icon positions, refer to the symptom troubleshooting. NOTE: Start the engine, turn the A/C system on, and allow it to run for a few minutes and reach stable operation. | Refer to the symptom troubleshooting .

NOTE: Start the engine, turn the A/C system on, and allow it to run for a few minutes and reach stable operation.

*1: Single fan type

*2: Dual fan type
````

## Chunk 8871: Drive Belt Inspection (K20C2): Inspection

- Title: Drive Belt Inspection (K20C2): Inspection
- Source path: `pages\11431.html`
- Chunk ID: `chunk_4cd1ba0600ee`
- Images: `images\GHH409176.jpeg`
- Duplicate sources: `pages\15833.html`

### Full Text

````text
# Drive Belt Inspection (K20C2): Inspection

- Drive Belt - Inspect Courtesy of HONDA, U.S.A., INC. 1. Inspect the belt for cracks or damage. If the belt is cracked or damaged, replace it . 2. Check the position of the drive belt auto-tensioner indicator's pointer (A) is within the standard range (B) as shown. If it is out of the standard range, replace the drive belt NOTE: When replacing a new drive belt, check the position of the drive belt auto-tensioner indicator's pointer is within the standard range (C) as shown.

Courtesy of HONDA, U.S.A., INC. | 1. Inspect the belt for cracks or damage. If the belt is cracked or damaged, replace it . 2. Check the position of the drive belt auto-tensioner indicator's pointer (A) is within the standard range (B) as shown. If it is out of the standard range, replace the drive belt NOTE: When replacing a new drive belt, check the position of the drive belt auto-tensioner indicator's pointer is within the standard range (C) as shown.

NOTE: When replacing a new drive belt, check the position of the drive belt auto-tensioner indicator's pointer is within the standard range (C) as shown.
````

## Chunk 8872: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11432.html`
- Chunk ID: `chunk_735b37eaf127`
- Images: `images\GHH409177.jpeg`, `images\GHH409178.jpeg`, `images\GHH409179.jpeg`, `images\GHH409180.jpeg`, `images\GHH409181.jpeg`
- Duplicate sources: `pages\14629.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

NOTE:

- It is normal for the A/C compressor to turn off under certain conditions, such as low idle, high engine coolant temperature, hard acceleration, or high/low refrigerant pressure.

- Do not use this troubleshooting procedure if the fans are also inoperative with the A/C on. Refer to the symptom troubleshooting index .

- Before doing symptom troubleshooting, check for PGM-FI DTCs .

- PGM-FI system parameter check -1. Connect the HDS to the DLC. -2. Start the engine. -3. Climate control panel without display: Set the A/C icon and the fan control icon, the fan control dial *1, or the fan control button *2 to ON. Climate control panel with display: Set the A/C button and the fan control dial to ON. *1: Without dual zone climate control *2: With dual zone climate control -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit A/C SWITCH ON A/C CLUTCH ON Do the current condition(s) match the threshold? YES Go to step 2. NO: A/C SWITCH is OFF A/C SWITCH is OFF, replace the climate control unit . NO: A/C SWITCH is ON and A/C CLUTCH is OFF A/C SWITCH is ON and A/C CLUTCH is OFF, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

-1. Connect the HDS to the DLC.

-2. Start the engine.

-3. Climate control panel without display: Set the A/C icon and the fan control icon, the fan control dial *1, or the fan control button *2 to ON.

Climate control panel with display: Set the A/C button and the fan control dial to ON.

*1: Without dual zone climate control

*2: With dual zone climate control

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

A/C SWITCH | ON

A/C CLUTCH | ON

Do the current condition(s) match the threshold?

YES

Go to step 2.

NO: A/C SWITCH is OFF

A/C SWITCH is OFF, replace the climate control unit .

NO: A/C SWITCH is ON and A/C CLUTCH is OFF

A/C SWITCH is ON and A/C CLUTCH is OFF, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A23 Is the fuse OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A23 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A23

Is the fuse OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A23 fuse circuit.

- A/C compressor clutch relay check -1. Remove the A/C compressor clutch relay from the under-hood fuse/relay box, and test it . Is the relay OK? YES Go to step 4. NO Replace the A/C compressor clutch relay.

-1. Remove the A/C compressor clutch relay from the under-hood fuse/relay box, and test it .

Is the relay OK?

YES

Go to step 4.

NO

Replace the A/C compressor clutch relay.

- Open wire check (+B MG CLUTCH line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode A/C compressor clutch relay: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MG CLUTCH wire is OK. Go to step 5. NO Repair an open in the +B MG CLUTCH wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MG CLUTCH wire is OK. Go to step 5.

NO

Repair an open in the +B MG CLUTCH wire.

- Determine possible failure area (A/C compressor clutch relay switch side circuit, A/C compressor clutch relay coil side circuit) -1. Connect terminals A and B with a jumper wire. Terminal A A/C compressor clutch relay 4P socket No.
````

## Chunk 8873: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11432.html`
- Chunk ID: `chunk_af107356de9e`
- Images: `images\GHH409177.jpeg`, `images\GHH409178.jpeg`, `images\GHH409179.jpeg`, `images\GHH409180.jpeg`, `images\GHH409181.jpeg`
- Duplicate sources: `pages\14629.html`

### Full Text

````text
ket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MG CLUTCH wire is OK. Go to step 5. NO Repair an open in the +B MG CLUTCH wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MG CLUTCH wire is OK. Go to step 5.

NO

Repair an open in the +B MG CLUTCH wire.

- Determine possible failure area (A/C compressor clutch relay switch side circuit, A/C compressor clutch relay coil side circuit) -1. Connect terminals A and B with a jumper wire. Terminal A A/C compressor clutch relay 4P socket No. 1 Terminal B A/C compressor clutch relay 4P socket No. 2 Courtesy of HONDA, U.S.A., INC. Does the A/C compressor clutch clickΩ YES Go to step 6. NO Go to step 8.

-1. Connect terminals A and B with a jumper wire.

Terminal A | A/C compressor clutch relay 4P socket No. 1

Terminal B | A/C compressor clutch relay 4P socket No. 2

Courtesy of HONDA, U.S.A., INC.

Does the A/C compressor clutch clickΩ

YES

Go to step 6.

NO

Go to step 8.

- Open wire check (IG2 OPTION line) -1. Disconnect the jumper wire. -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode A/C compressor clutch relay: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG2 OPTION wire is OK. Go to step 7. NO Repair an open in the IG2 OPTION wire.

-1. Disconnect the jumper wire.

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG2 OPTION wire is OK. Go to step 7.

NO

Repair an open in the IG2 OPTION wire.

- Open wire check (A/C MG CLUTCH RLY CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reinstall the A/C compressor clutch relay. -3. Jump the SCS line with the HDS, and wait more than 1 minute. NOTE: This step must be done to protect the PCM from damage. -4. Disconnect the following connector. PCM connector No. 2 (58P) -5. Connect terminals A and B with a jumper wire. Terminal A PCM connector No. 2 (58P) No. 48 Terminal B Body ground -6. Turn the vehicle to the ON mode. Does the A/C compressor clutch clickΩ YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the A/C MG CLUTCH RLY CL- wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reinstall the A/C compressor clutch relay.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

NOTE: This step must be done to protect the PCM from damage.

-4. Disconnect the following connector.

PCM connector No. 2 (58P)

-5. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector No. 2 (58P) No. 48

Terminal B | Body ground

-6. Turn the vehicle to the ON mode.

Does the A/C compressor clutch clickΩ

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the A/C MG CLUTCH RLY CL- wire.

- Open wire check (A/C MG CLUTCH/MG CLUTCH line) -1. Disconnect the jumper wire. -2. Disconnect the following connector. A/C compressor 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode A/C compressor clutch relay: disconnected A/C compressor 3P connector: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 2 Test point 2 A/C compressor 3P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The A/C MG CLUTCH/MG CLUTCH wire is OK. Check the A/C compressor clutch clearance and the A/C compressor clutch field coil . Repair as needed. NO Repair an open in the A/C MG CLUTCH/MG CLUTCH wire.

-1.
````

## Chunk 8874: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11432.html`
- Chunk ID: `chunk_eb0907efbfdc`
- Images: `images\GHH409177.jpeg`, `images\GHH409178.jpeg`, `images\GHH409179.jpeg`, `images\GHH409180.jpeg`, `images\GHH409181.jpeg`
- Duplicate sources: `pages\14629.html`

### Full Text

````text
ace the original PCM .

NO

Repair an open in the A/C MG CLUTCH RLY CL- wire.

- Open wire check (A/C MG CLUTCH/MG CLUTCH line) -1. Disconnect the jumper wire. -2. Disconnect the following connector. A/C compressor 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode A/C compressor clutch relay: disconnected A/C compressor 3P connector: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 2 Test point 2 A/C compressor 3P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The A/C MG CLUTCH/MG CLUTCH wire is OK. Check the A/C compressor clutch clearance and the A/C compressor clutch field coil . Repair as needed. NO Repair an open in the A/C MG CLUTCH/MG CLUTCH wire.

-1. Disconnect the jumper wire.

-2. Disconnect the following connector.

A/C compressor 3P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

A/C compressor 3P connector: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 2

Test point 2 | A/C compressor 3P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The A/C MG CLUTCH/MG CLUTCH wire is OK. Check the A/C compressor clutch clearance and the A/C compressor clutch field coil . Repair as needed.

NO

Repair an open in the A/C MG CLUTCH/MG CLUTCH wire.
````

## Chunk 8875: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)
- Source path: `pages\11433.html`
- Chunk ID: `chunk_3d2a71388ae0`
- Images: `images\GHH409182.jpeg`, `images\GHH409183.jpeg`, `images\GHH409184.jpeg`, `images\GHH409185.jpeg`, `images\GHH409186.jpeg`
- Duplicate sources: `pages\15298.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

NOTE:

- It is normal for the A/C compressor to turn off under certain conditions, such as low idle, high engine coolant temperature, hard acceleration, or high/low refrigerant pressure.

- Do not use this troubleshooting procedure if the cooling fan is also inoperative with the A/C on. Refer to the symptom troubleshooting index .

- Before doing symptom troubleshooting, check for PGM-FI DTCs .

- PGM-FI system parameter check -1. Connect the HDS to the DLC. -2. Start the engine. -3. Climate control panel without display: Set the A/C icon and the fan control icon, the fan control dial *1, or the fan control button *2 to ON. Climate control panel with display: Set the A/C button and the fan control dial to ON. *1: Without dual zone climate control *2: With dual zone climate control -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit A/C SWITCH ON A/C CLUTCH ON Do the current condition(s) match the threshold? YES Go to step 2. NO: A/C SWITCH is OFF A/C SWITCH is OFF, replace the climate control unit . NO: A/C SWITCH is ON and A/C CLUTCH is OFF A/C SWITCH is ON and A/C CLUTCH is OFF, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

-1. Connect the HDS to the DLC.

-2. Start the engine.

-3. Climate control panel without display: Set the A/C icon and the fan control icon, the fan control dial *1, or the fan control button *2 to ON.

Climate control panel with display: Set the A/C button and the fan control dial to ON.

*1: Without dual zone climate control *2: With dual zone climate control

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

A/C SWITCH | ON

A/C CLUTCH | ON

Do the current condition(s) match the threshold?

YES

Go to step 2.

NO: A/C SWITCH is OFF

A/C SWITCH is OFF, replace the climate control unit .

NO: A/C SWITCH is ON and A/C CLUTCH is OFF

A/C SWITCH is ON and A/C CLUTCH is OFF, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A23 Is the fuse OK? YES Go to step 3. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A23 fuse circuit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A23

Is the fuse OK?

YES

Go to step 3.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A23 fuse circuit.

- A/C compressor clutch relay check -1. Remove the A/C compressor clutch relay from the under-hood fuse/relay box, and test it . Is the relay OK? YES Go to step 4. NO Replace the A/C compressor clutch relay.

-1. Remove the A/C compressor clutch relay from the under-hood fuse/relay box, and test it .

Is the relay OK?

YES

Go to step 4.

NO

Replace the A/C compressor clutch relay.

- Open wire check (+B MG CLUTCH line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode A/C compressor clutch relay: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MG CLUTCH wire is OK. Go to step 5. NO Repair an open in the +B MG CLUTCH wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MG CLUTCH wire is OK. Go to step 5.

NO

Repair an open in the +B MG CLUTCH wire.

- Determine possible failure area (A/C compressor clutch relay switch side circuit, A/C compressor clutch relay coil side circuit) -1. Connect terminals A and B with a jumper wire. Terminal A A/C compressor clutch relay 4P socket No.
````

## Chunk 8876: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)
- Source path: `pages\11433.html`
- Chunk ID: `chunk_36a494d9f883`
- Images: `images\GHH409182.jpeg`, `images\GHH409183.jpeg`, `images\GHH409184.jpeg`, `images\GHH409185.jpeg`, `images\GHH409186.jpeg`
- Duplicate sources: `pages\15298.html`

### Full Text

````text
ket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MG CLUTCH wire is OK. Go to step 5. NO Repair an open in the +B MG CLUTCH wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MG CLUTCH wire is OK. Go to step 5.

NO

Repair an open in the +B MG CLUTCH wire.

- Determine possible failure area (A/C compressor clutch relay switch side circuit, A/C compressor clutch relay coil side circuit) -1. Connect terminals A and B with a jumper wire. Terminal A A/C compressor clutch relay 4P socket No. 1 Terminal B A/C compressor clutch relay 4P socket No. 2 Courtesy of HONDA, U.S.A., INC. Does the A/C compressor clutch clickΩ YES Go to step 6. NO Go to step 8.

-1. Connect terminals A and B with a jumper wire.

Terminal A | A/C compressor clutch relay 4P socket No. 1

Terminal B | A/C compressor clutch relay 4P socket No. 2

Courtesy of HONDA, U.S.A., INC.

Does the A/C compressor clutch clickΩ

YES

Go to step 6.

NO

Go to step 8.

- Open wire check (IG2 A/C (L15B7/K20C2 engine) or IG2 OPTION (L15BA/L15BY engine) line) -1. Disconnect the jumper wire. -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode A/C compressor clutch relay: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/L15BY engine) wire is OK. Go to step 7. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/L15BY engine Repair an open in the IG2 OPTION wire.

-1. Disconnect the jumper wire.

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

A/C compressor clutch relay: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/L15BY engine) wire is OK. Go to step 7.

NO: L15B7/K20C2 engine

Repair an open in the IG2 A/C wire.

NO: L15BA/L15BY engine

Repair an open in the IG2 OPTION wire.

- Open wire check (A/C MG CLUTCH RLY CL-/ACC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reinstall the A/C compressor clutch relay. -3. Jump the SCS line with the HDS, and wait more than 1 minute. NOTE: This step must be done to protect the PCM from damage. -4. Disconnect the following connector. PCM connector E (80P) -5. Connect terminals A and B with a jumper wire. Terminal A PCM connector E (80P) No. 31 Terminal B Body ground -6. Turn the vehicle to the ON mode. Does the A/C compressor clutch clickΩ YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the A/C MG CLUTCH RLY CL-/ACC wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reinstall the A/C compressor clutch relay.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

NOTE: This step must be done to protect the PCM from damage.

-4. Disconnect the following connector.

PCM connector E (80P)

-5. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector E (80P) No. 31

Terminal B | Body ground

-6. Turn the vehicle to the ON mode.

Does the A/C compressor clutch clickΩ

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the A/C MG CLUTCH RLY CL-/ACC wire.

- Open wire check (A/C MG CLUTCH/MG CLUTCH (except K20C2 engine) or A/C MG CLUTCH/AC MG CLUTCH (K20C2 engine) line) -1. Disconnect the jumper wire. -2. Disconnect the following connector. A/C compressor 3P connector -3. Check for continuity between test points 1 and 2.
````

## Chunk 8877: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

- Title: Climate Control System Symptom Troubleshooting - The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)
- Source path: `pages\11433.html`
- Chunk ID: `chunk_72cb7732c7a6`
- Images: `images\GHH409182.jpeg`, `images\GHH409183.jpeg`, `images\GHH409184.jpeg`, `images\GHH409185.jpeg`, `images\GHH409186.jpeg`
- Duplicate sources: `pages\15298.html`

### Full Text

````text
or.

PCM connector E (80P)

-5. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector E (80P) No. 31

Terminal B | Body ground

-6. Turn the vehicle to the ON mode.

Does the A/C compressor clutch clickΩ

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the A/C MG CLUTCH RLY CL-/ACC wire.

- Open wire check (A/C MG CLUTCH/MG CLUTCH (except K20C2 engine) or A/C MG CLUTCH/AC MG CLUTCH (K20C2 engine) line) -1. Disconnect the jumper wire. -2. Disconnect the following connector. A/C compressor 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode A/C compressor clutch relay: disconnected A/C compressor 3P connector: disconnected Test point 1 A/C compressor clutch relay 4P socket No. 2 Test point 2 A/C compressor 3P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The A/C MG CLUTCH/MG CLUTCH (except K20C2 engine) or the A/C MG CLUTCH/AC MG CLUTCH (K20C2 engine) wire is OK. Check the A/C compressor clutch clearance and the A/C compressor clutch field coil . Repair as needed. NO: Except K20C2 engine Repair an open in the A/C MG CLUTCH/MG CLUTCH wire. NO: K20C2 engine Repair an open in the A/C MG CLUTCH/AC MG CLUTCH wire.

-1. Disconnect the jumper wire.

-2. Disconnect the following connector.

A/C compressor 3P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

A/C compressor clutch relay: disconnected

A/C compressor 3P connector: disconnected

Test point 1 | A/C compressor clutch relay 4P socket No. 2

Test point 2 | A/C compressor 3P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The A/C MG CLUTCH/MG CLUTCH (except K20C2 engine) or the A/C MG CLUTCH/AC MG CLUTCH (K20C2 engine) wire is OK. Check the A/C compressor clutch clearance and the A/C compressor clutch field coil . Repair as needed.

NO: Except K20C2 engine

Repair an open in the A/C MG CLUTCH/MG CLUTCH wire.

NO: K20C2 engine

Repair an open in the A/C MG CLUTCH/AC MG CLUTCH wire.
````

## Chunk 8878: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11434.html`
- Chunk ID: `chunk_997873b82c6d`
- Images: `images\GHH409187.jpeg`, `images\GHH409188.jpeg`, `images\GHH409189.jpeg`
- Duplicate sources: `pages\14623.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)

NOTE:

- Do not use this troubleshooting procedure if the A/C compressor is inoperative. Refer to the symptom troubleshooting index .

- If A/C refrigerant pressure is abnormal, the radiator and A/C condenser fans are controlled based only on engine coolant temperature.

- Before doing symptom troubleshooting, check for PGM-FI DTCs .

- Fuse check -1. Check the following fuses. Fuse No. A10 (20 A) No. A11 (5 A) Location Under-hood fuse/relay box Are the fuses OK? YES Go to step 2. NO Replace the fuse(s), and recheck. If the fuse(s) blows again, repair a short in the No. A10 (20 A) and/or No. A11 (5 A) fuse circuit(s).

-1. Check the following fuses.

Fuse | No. A10 (20 A)

No. A11 (5 A)

Location | Under-hood fuse/relay box

Are the fuses OK?

YES

Go to step 2.

NO

Replace the fuse(s), and recheck. If the fuse(s) blows again, repair a short in the No. A10 (20 A) and/or No. A11 (5 A) fuse circuit(s).

- A/C condenser fan low speed operation check -1. Jump the SCS line with the HDS, and wait more than 1 minute. NOTE: This step must be done to protect the PCM from damage. -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Connect terminals A and B with a jumper wire. Terminal A PCM connector No. 2 (58P) No. 12 Terminal B Body ground -4. Turn the vehicle to the ON mode. Do the A/C condenser and radiator fans run on low? YES Go to step 3. NO Go to climate control system symptom troubleshooting .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

NOTE: This step must be done to protect the PCM from damage.

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector No. 2 (58P) No. 12

Terminal B | Body ground

-4. Turn the vehicle to the ON mode.

Do the A/C condenser and radiator fans run on low?

YES

Go to step 3.

NO

Go to climate control system symptom troubleshooting .

- A/C condenser fan high speed operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Connect terminals A and B with jumper wires. Terminal A PCM connector No. 2 (58P) No. 36 Terminal B Body ground Terminal A PCM connector No. 2 (58P) No. 47 Terminal B Body ground -3. Turn the vehicle to the ON mode. Do the A/C condenser and radiator fans run on high? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Connect terminals A and B with jumper wires.

Terminal A | PCM connector No. 2 (58P) No. 36

Terminal B | Body ground

Terminal A | PCM connector No. 2 (58P) No. 47

Terminal B | Body ground

-3. Turn the vehicle to the ON mode.

Do the A/C condenser and radiator fans run on high?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 4.

- A/C condenser fan relay check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the jumper wires. -3. Remove the A/C condenser fan relay from the under-hood fuse/relay box, and test it . Is the relay OK? YES Go to step 5. NO Replace the A/C condenser fan relay.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the jumper wires.

-3. Remove the A/C condenser fan relay from the under-hood fuse/relay box, and test it .

Is the relay OK?

YES

Go to step 5.

NO

Replace the A/C condenser fan relay.

- Open wire check (+B SUB FAN line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected A/C condenser fan relay: disconnected Test point 1 A/C condenser fan relay 4P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B SUB FAN wire is OK. Go to step 6. NO Repair an open in the +B SUB FAN wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

A/C condenser fan relay: disconnected
````

## Chunk 8879: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11434.html`
- Chunk ID: `chunk_eedacf57ada3`
- Images: `images\GHH409187.jpeg`, `images\GHH409188.jpeg`, `images\GHH409189.jpeg`
- Duplicate sources: `pages\14623.html`

### Full Text

````text
nnect the jumper wires.

-3. Remove the A/C condenser fan relay from the under-hood fuse/relay box, and test it .

Is the relay OK?

YES

Go to step 5.

NO

Replace the A/C condenser fan relay.

- Open wire check (+B SUB FAN line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected A/C condenser fan relay: disconnected Test point 1 A/C condenser fan relay 4P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B SUB FAN wire is OK. Go to step 6. NO Repair an open in the +B SUB FAN wire.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

A/C condenser fan relay: disconnected

Test point 1 | A/C condenser fan relay 4P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B SUB FAN wire is OK. Go to step 6.

NO

Repair an open in the +B SUB FAN wire.

- Open wire check (SUB FAN MOTOR line) -1. Connect terminals A and B with a jumper wire. Terminal A A/C condenser fan relay 4P socket No. 1 Terminal B A/C condenser fan relay 4P socket No. 2 Courtesy of HONDA, U.S.A., INC. Does the A/C condenser fan run on high? YES The SUB FAN MOTOR wire is not open. Go to step 7. NO Repair an open in the SUB FAN MOTOR wire.

-1. Connect terminals A and B with a jumper wire.

Terminal A | A/C condenser fan relay 4P socket No. 1

Terminal B | A/C condenser fan relay 4P socket No. 2

Courtesy of HONDA, U.S.A., INC.

Does the A/C condenser fan run on high?

YES

The SUB FAN MOTOR wire is not open. Go to step 7.

NO

Repair an open in the SUB FAN MOTOR wire.

- Open wire check (IGPS(LAF) line) -1. Disconnect the jumper wire. -2. Connect terminals A and B with jumper wires. Terminal A PCM connector No. 2 (58P) No. 36 Terminal B Body ground Terminal A PCM connector No. 2 (58P) No. 47 Terminal B Body ground -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected A/C condenser fan relay: disconnected PCM connector No. 2 (58P) No. 36: jumped to body ground PCM connector No. 2 (58P) No. 47: jumped to body ground Test point 1 A/C condenser fan relay 4P socket No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Repair an open in the FAN HI SIGNAL wire between the A/C condenser fan relay and the PCM. NO Repair an open in the IGPS (LAF) wire.

-1. Disconnect the jumper wire.

-2. Connect terminals A and B with jumper wires.

Terminal A | PCM connector No. 2 (58P) No. 36

Terminal B | Body ground

Terminal A | PCM connector No. 2 (58P) No. 47

Terminal B | Body ground

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

A/C condenser fan relay: disconnected

PCM connector No. 2 (58P) No. 36: jumped to body ground

PCM connector No. 2 (58P) No. 47: jumped to body ground

Test point 1 | A/C condenser fan relay 4P socket No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Repair an open in the FAN HI SIGNAL wire between the A/C condenser fan relay and the PCM.

NO

Repair an open in the IGPS (LAF) wire.
````

## Chunk 8880: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11435.html`
- Chunk ID: `chunk_59de55ca6d4b`
- Images: `images\GHH409190.jpeg`, `images\GHH409191.jpeg`, `images\GHH409192.jpeg`, `images\GHH409193.jpeg`, `images\GHH409194.jpeg`, `images\GHH409195.jpeg`
- Duplicate sources: `pages\14625.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

NOTE:

- Do not use this troubleshooting procedure if the A/C compressor is inoperative. Refer to the symptom troubleshooting index .

- If A/C refrigerant pressure is abnormal, the radiator and A/C condenser fans are controlled based only on engine coolant temperature.

- Before doing symptom troubleshooting, check for PGM-FI DTCs .

- Fuse check -1. Check the following fuse. Fuse No. A1-3 Is the fuse OK? YES Go to step 2. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A1-3 fuse circuit.

-1. Check the following fuse.

Fuse | No. A1-3

Is the fuse OK?

YES

Go to step 2.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. A1-3 fuse circuit.

- Radiator fan and fan control relays check -1. Remove the radiator fan relay and the fan control relay from the under-hood fuse/relay box, and test it . Are the relays OK? YES Go to step 3. NO Replace the radiator fan relay and/or the fan control relay.

-1. Remove the radiator fan relay and the fan control relay from the under-hood fuse/relay box, and test it .

Are the relays OK?

YES

Go to step 3.

NO

Replace the radiator fan relay and/or the fan control relay.

- PGM-FI system parameter check -1. Connect the HDS to the DLC. -2. Turn the vehicle to the ON mode. Make sure the A/C system is OFF, then start the engine. -3. Climate control panel without display: Turn the fan control icon, the fan control dial *1, or the fan control button *2 ON, then momentarily turn on the A/C with the A/C icon. Climate control panel with display: Turn the fan control dial ON, then momentarily turn on the A/C with the A/C button. *1: Without dual zone climate control *2: With dual zone climate control NOTE: Do not run the A/C for more than a few seconds with the engine running or damage to the A/C system will result. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FAN LOW CTRL ON Is the FAN LOW CTRL on with the A/C on? YES Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

-1. Connect the HDS to the DLC.

-2. Turn the vehicle to the ON mode. Make sure the A/C system is OFF, then start the engine.

-3. Climate control panel without display: Turn the fan control icon, the fan control dial *1, or the fan control button *2 ON, then momentarily turn on the A/C with the A/C icon.

Climate control panel with display: Turn the fan control dial ON, then momentarily turn on the A/C with the A/C button.

*1: Without dual zone climate control

*2: With dual zone climate control

NOTE: Do not run the A/C for more than a few seconds with the engine running or damage to the A/C system will result.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FAN LOW CTRL | ON

Is the FAN LOW CTRL on with the A/C on?

YES

Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

- Open wire check (+B MAIN FAN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected Fan control relay: disconnected Test point 1 Radiator fan relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MAIN FAN wire is OK. Go to step 5. NO Repair an open in the +B MAIN FAN wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Radiator fan relay: disconnected

Fan control relay: disconnected

Test point 1 | Radiator fan relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MAIN FAN wire is OK. Go to step 5.

NO

Repair an open in the +B MAIN FAN wire.
````

## Chunk 8881: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11435.html`
- Chunk ID: `chunk_10ed33f2ff5e`
- Images: `images\GHH409190.jpeg`, `images\GHH409191.jpeg`, `images\GHH409192.jpeg`, `images\GHH409193.jpeg`, `images\GHH409194.jpeg`, `images\GHH409195.jpeg`
- Duplicate sources: `pages\14625.html`

### Full Text

````text
ltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected Fan control relay: disconnected Test point 1 Radiator fan relay 4P socket No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B MAIN FAN wire is OK. Go to step 5. NO Repair an open in the +B MAIN FAN wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Radiator fan relay: disconnected

Fan control relay: disconnected

Test point 1 | Radiator fan relay 4P socket No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B MAIN FAN wire is OK. Go to step 5.

NO

Repair an open in the +B MAIN FAN wire.

- Determine possible failure area (radiator fan relay switch side circuit, radiator fan relay coil side circuit) -1. Reinstall the fan control relay. -2. Connect terminals A and B with a jumper wire. Terminal A Radiator fan relay 4P socket No. 3 Terminal B Radiator fan relay 4P socket No. 4 Courtesy of HONDA, U.S.A., INC. Do the A/C condenser and radiator fans run on low? YES Go to step 6. NO Go to step 8.

-1. Reinstall the fan control relay.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Radiator fan relay 4P socket No. 3

Terminal B | Radiator fan relay 4P socket No. 4

Courtesy of HONDA, U.S.A., INC.

Do the A/C condenser and radiator fans run on low?

YES

Go to step 6.

NO

Go to step 8.

- Radiator fan relay coil side power circuit check -1. Disconnect the jumper wire. -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Radiator fan relay: disconnected Test point 1 Radiator fan relay 4P socket No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG2 OPTION wire is OK. Go to step 7. NO Repair an open in the IG2 OPTION wire.

-1. Disconnect the jumper wire.

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Radiator fan relay: disconnected

Test point 1 | Radiator fan relay 4P socket No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG2 OPTION wire is OK. Go to step 7.

NO

Repair an open in the IG2 OPTION wire.

- Open wire check (RFC RLY CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reinstall the radiator fan relay. -3. Jump the SCS line with the HDS, and wait more than 1 minute. NOTE: This step must be done to protect the PCM from damage. -4. Disconnect the following connector. PCM connector No. 2 (58P) -5. Connect terminals A and B with a jumper wire. Terminal A PCM connector No. 2 (58P) No. 12 Terminal B Body ground -6. Turn the vehicle to the ON mode. Do the A/C condenser and radiator fans run on low? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the RFC RLY CL- wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reinstall the radiator fan relay.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

NOTE: This step must be done to protect the PCM from damage.

-4. Disconnect the following connector.

PCM connector No. 2 (58P)

-5. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector No. 2 (58P) No. 12

Terminal B | Body ground

-6. Turn the vehicle to the ON mode.

Do the A/C condenser and radiator fans run on low?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the RFC RLY CL- wire.

- Open wire check (MAIN FAN MOTOR line) -1. Disconnect the following connector. Radiator fan motor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected Radiator fan motor 2P connector: disconnected Radiator fan relay 4P socket No. 3 and No. 4: jumped Test point 1 Radiator fan motor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The MAIN FAN MOTOR wire is OK.
````

## Chunk 8882: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Symptom Troubleshooting - The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11435.html`
- Chunk ID: `chunk_8bb21f0907d1`
- Images: `images\GHH409190.jpeg`, `images\GHH409191.jpeg`, `images\GHH409192.jpeg`, `images\GHH409193.jpeg`, `images\GHH409194.jpeg`, `images\GHH409195.jpeg`
- Duplicate sources: `pages\14625.html`

### Full Text

````text
w?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the RFC RLY CL- wire.

- Open wire check (MAIN FAN MOTOR line) -1. Disconnect the following connector. Radiator fan motor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected Radiator fan motor 2P connector: disconnected Radiator fan relay 4P socket No. 3 and No. 4: jumped Test point 1 Radiator fan motor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The MAIN FAN MOTOR wire is OK. Go to step 9. NO Repair an open in the MAIN FAN MOTOR wire.

-1. Disconnect the following connector.

Radiator fan motor 2P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Radiator fan relay: disconnected

Radiator fan motor 2P connector: disconnected

Radiator fan relay 4P socket No. 3 and No. 4: jumped

Test point 1 | Radiator fan motor 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The MAIN FAN MOTOR wire is OK. Go to step 9.

NO

Repair an open in the MAIN FAN MOTOR wire.

- Radiator and A/C condenser fan motors test -1. Test the radiator and the A/C condenser fan motors . Are the radiator and A/C condenser fan motors OK? YES Go to step 10. NO Replace the radiator fan motor and/or the A/C condenser fan motor .

-1. Test the radiator and the A/C condenser fan motors .

Are the radiator and A/C condenser fan motors OK?

YES

Go to step 10.

NO

Replace the radiator fan motor and/or the A/C condenser fan motor .

- Open wire check (FAN HI/LO RLY COM line) -1. Reconnect the radiator fan motor 2P connector. -2. Remove the fan control relay from the under-hood fuse/relay box. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected Fan control relay: disconnected A/C condenser fan motor 2P connector: disconnected Radiator fan relay 4P socket No. 3 and No. 4: jumped Test point 1 Fan control relay 5P socket No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The FAN HI/LO RLY COM wire is OK. Go to step 11. NO Repair an open in the FAN HI/LO RLY COM wire.

-1. Reconnect the radiator fan motor 2P connector.

-2. Remove the fan control relay from the under-hood fuse/relay box.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Radiator fan relay: disconnected

Fan control relay: disconnected

A/C condenser fan motor 2P connector: disconnected

Radiator fan relay 4P socket No. 3 and No. 4: jumped

Test point 1 | Fan control relay 5P socket No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The FAN HI/LO RLY COM wire is OK. Go to step 11.

NO

Repair an open in the FAN HI/LO RLY COM wire.

- Open wire check (SUB FAN MOTOR line) -1. Reinstall the fan control relay. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Radiator fan relay: disconnected A/C condenser fan motor 2P connector: disconnected Radiator fan relay 4P socket No. 3 and No. 4: jumped Test point 1 A/C condenser fan motor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Check for an open in the GND wire between the A/C condenser fan motor and body ground. If the wire is OK, check for poor ground at G401. NO Repair an open in the SUB FAN MOTOR wire.

-1. Reinstall the fan control relay.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Radiator fan relay: disconnected

A/C condenser fan motor 2P connector: disconnected

Radiator fan relay 4P socket No. 3 and No. 4: jumped

Test point 1 | A/C condenser fan motor 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Check for an open in the GND wire between the A/C condenser fan motor and body ground. If the wire is OK, check for poor ground at G401.

NO

Repair an open in the SUB FAN MOTOR wire.
````

## Chunk 8883: Climate Control System Symptom Troubleshooting - The blower and the heater controls and the A/C system do not work

- Title: Climate Control System Symptom Troubleshooting - The blower and the heater controls and the A/C system do not work
- Source path: `pages\11436.html`
- Chunk ID: `chunk_8717a3779d9c`
- Images: none
- Duplicate sources: `pages\14626.html`

### Full Text

````text
# Climate Control System Symptom Troubleshooting - The blower and the heater controls and the A/C system do not work

NOTE: Do this troubleshooting procedure only if sent here by symptom troubleshooting index .

- Fuse check -1. Check the following fuse. Fuse No. B9 Is the fuse OK? YES Go to step 2. NO Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

-1. Check the following fuse.

Fuse | No. B9

Is the fuse OK?

YES

Go to step 2.

NO

Replace the fuse, and recheck. If the fuse blows again, repair a short in the No. B9 fuse circuit.

- Open wire check (IG2 A/C (L15B7/K20C2 engine) or IG2 OPTION (L15BA/K20C1/L15BY engine) line) -1. Disconnect the following connector. Climate control unit connector A (32P) -2. Turn the vehicle to the ON mode. -3. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Climate control unit connector A (32P): disconnected Test point 1 Climate control unit connector A (32P) No. 32 Test point 2 Body ground Is there battery voltage? YES The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 3. NO: L15B7/K20C2 engine Repair an open in the IG2 A/C wire. NO: L15BA/K20C1/L15BY engine Repair an open in the IG2 OPTION wire.

-1. Disconnect the following connector.

Climate control unit connector A (32P)

-2. Turn the vehicle to the ON mode.

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Climate control unit connector A (32P): disconnected

Test point 1 | Climate control unit connector A (32P) No. 32

Test point 2 | Body ground

Is there battery voltage?

YES

The IG2 A/C (L15B7/K20C2 engine) or the IG2 OPTION (L15BA/K20C1/L15BY engine) wire is OK. Go to step 3.

NO: L15B7/K20C2 engine

Repair an open in the IG2 A/C wire.

NO: L15BA/K20C1/L15BY engine

Repair an open in the IG2 OPTION wire.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Climate control unit connector A (32P): disconnected Test point 1 Climate control unit connector A (32P) No. 28 Test point 2 Body ground Is there continuity? YES Replace the climate control unit . NO Check for an open in the GND wire. If the wire is OK, check for poor ground at G505.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Climate control unit connector A (32P): disconnected

Test point 1 | Climate control unit connector A (32P) No. 28

Test point 2 | Body ground

Is there continuity?

YES

Replace the climate control unit .

NO

Check for an open in the GND wire. If the wire is OK, check for poor ground at G505.
````

## Chunk 8884: A/C System Description - A/C Pressure Sensor

- Title: A/C System Description - A/C Pressure Sensor
- Source path: `pages\11437.html`
- Chunk ID: `chunk_e02e422aa673`
- Images: `images\GHH409196.jpeg`
- Duplicate sources: `pages\15834.html`

### Full Text

````text
# A/C System Description - A/C Pressure Sensor

The A/C pressure sensor is attached to the discharge line on the inlet side of the A/C condenser. The sensor's output voltage changes in response to changes in A/C discharge pressure. The PCM receives the voltage signal and is used to drive the A/C compressor. The PCM controls the cooling fan(s). When the A/C system pressure rises to the upper limit, or decreases to the lower limit, the PCM stops the A/C compressor to protect the system.

- Upper limit: 2, 950 kPa (30.08 kgf/cm 2, 427.9 psi)

- Lower limit: 196 kPa (2.00 kgf/cm 2, 28.4 psi)

- High speed fans switch point (dual fan type): 1, 600 kPa (16.32 kgf/cm 2, 232.1 psi)

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8885: A/C System Description - Compressor

- Title: A/C System Description - Compressor
- Source path: `pages\11438.html`
- Chunk ID: `chunk_1f8e01d7d431`
- Images: `images\GHH409197.jpeg`
- Duplicate sources: `pages\15835.html`

### Full Text

````text
# A/C System Description - Compressor

A/C Compressor

The A/C compressor is a pump that compresses refrigerant. It is driven by the engine accessory drive belt. When the compressor clutch is OFF, the pulley and armature plate are disconnected and the A/C compressor does not operate. When the compressor clutch is ON, the field coil is energized, creating a strong magnetic field. This magnetic field locks the pulley and armature plate together, driving the compressor. The compressed refrigerant becomes a high pressure and temperature vapor that is sent to the A/C condenser.

The A/C compressor has a mechanical relief valve, and the valve opens when refrigerant pressure exceeds the rated value. It cannot be reused, and should be replaced.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.

Variable Capacity Control

The climate control unit operates the variable capacity control solenoid on the A/C compressor. The solenoid controls the cooling capacity by adjusting the flow of refrigerant pumped through the A/C system. The climate control unit determines the solenoid circuit's current flow based on the outside air temperature sensor, the in-car temperature sensor, and solar radiation values.
````

## Chunk 8886: A/C System Description - Condenser

- Title: A/C System Description - Condenser
- Source path: `pages\11439.html`
- Chunk ID: `chunk_355b4ad20800`
- Images: `images\GHH409198.jpeg`
- Duplicate sources: `pages\15836.html`

### Full Text

````text
# A/C System Description - Condenser

Sub Cool Cycle Condenser System

The condenser and receiver/dryer are integrated. The main A/C condenser changes the high pressure and high temperature refrigerant vapor from the A/C compressor into a high pressure and high temperature liquid. This allows the refrigerant to release heat to the outside air. The receiver/dryer acts as a reservoir of liquid refrigerant for the expansion valve. It also removes debris and moisture from the refrigerant. The sub A/C condenser cools the high pressure and high temperature liquid refrigerant even further to improve A/C performance.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8887: A/C System Description - Evaporator Temperature Sensor

- Title: A/C System Description - Evaporator Temperature Sensor
- Source path: `pages\11440.html`
- Chunk ID: `chunk_f81c6191ba6b`
- Images: `images\GHH409199.jpeg`
- Duplicate sources: `pages\15837.html`

### Full Text

````text
# A/C System Description - Evaporator Temperature Sensor

The evaporator temperature sensor is a clip-type thermistor, with a sensing element that is directly mounted to the evaporator core fins. The sensor is connected to the climate control unit and constantly monitors the evaporator temperature. The A/C compressor and fans are cycled off briefly if the temperature approaches the freezing point of water. If the evaporator temperature goes too low, the moisture condensing on its cold surfaces will freeze, causing restricted evaporator airflow and poor A/C performance.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8888: A/C System Description - In-Car Temperature Sensor

- Title: A/C System Description - In-Car Temperature Sensor
- Source path: `pages\11441.html`
- Chunk ID: `chunk_64071f50736f`
- Images: `images\GHH409200.jpeg`
- Duplicate sources: `pages\15838.html`

### Full Text

````text
# A/C System Description - In-Car Temperature Sensor

The in-car temperature sensor is attached to the center face of the dashboard and reads in-car temperature. The sensor uses a chip type thermistor-type temperature sensor that decreases resistance when temperature rises and increases resistance when temperature is drops. The climate control unit reads the resistance fluctuation in response to changes in in-car temperature and control the A/C.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8889: A/C System Description - Overview

- Title: A/C System Description - Overview
- Source path: `pages\11442.html`
- Chunk ID: `chunk_198ecb91fd98`
- Images: `images\GHH409201.jpeg`, `images\GHH409202.jpeg`, `images\GHH409203.jpeg`
- Duplicate sources: `pages\15839.html`

### Full Text

````text
# A/C System Description - Overview

The air conditioning system regulates temperature air outlet by mixing cold and warm air in an appropriate ratio. The heater core and evaporator core are installed in the heater unit that has the air mix control damper and the mode control damper. The blower unit is composed of a blower motor, the recirculation control damper and the dust and pollen filter. The blower unit is connected to the heater unit by the duct integral with the blower unit.

System Diagram

Courtesy of HONDA, U.S.A., INC.

Air Flow Diagram

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.

Refrigerant Cycle

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8890: Climate Control System Description - Customize Function

- Title: Climate Control System Description - Customize Function
- Source path: `pages\11443.html`
- Chunk ID: `chunk_7f9d968cea64`
- Images: `images\GHH409204.jpeg`, `images\GHH409205.jpeg`, `images\GHH409206.jpeg`, `images\GHH409207.jpeg`, `images\GHH409208.jpeg`, `images\GHH409209.jpeg`, `images\GHH409210.jpeg`, `images\GHH409211.jpeg`, `images\GHH409212.jpeg`, `images\GHH409213.jpeg`, `images\GHH409214.jpeg`, `images\GHH409215.jpeg`, `images\GHH409216.jpeg`, `images\GHH409217.jpeg`
- Duplicate sources: `pages\15840.html`

### Full Text

````text
# Climate Control System Description - Customize Function

How to Change the Set Temperature (Climate Control Panel with Display)

The climate control unit has a function to change the set temperature +2.7 deg.F (+1.5 deg.C) or -2.7 deg.F (-1.5 deg.C) degrees in case customers feel the temperature is too warm or too cold for the displayed temperature.

NOTE: Verify that the climate control and A/C system is working properly before enabling the customize function to offset the set temperature.

- Turn the vehicle to the ON mode, then based on the desired temperature change, set the temperature condition on the temperature control dial according to the table.

- Turn the climate control system OFF then turn the vehicle to the OFF (LOCK) mode.

- Depending on desired setting change, press and hold the pair of buttons according to the table.

- While holding the buttons, turn the vehicle to the ON mode.

- Keep the buttons pressed for 10 seconds.

Setting | Temperature Condition | Buttons

+2.7 deg.F (+1.5 deg.C) Change | Hi | Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC. | or | Courtesy of HONDA, U.S.A., INC.

-2.7 deg.F (-1.5 deg.C) Change | Lo | Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC. | or | Courtesy of HONDA, U.S.A., INC.

Changing back to 0 deg.F (0 deg.C) | Except Hi or Lo | Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC. | or | Courtesy of HONDA, U.S.A., INC.

- Indication of the change The climate control unit displays the following during each change.

The climate control unit displays the following during each change.

- - Displays nothing from the vehicle ON mode for 5 seconds. - Blinks the current setting for the next 5 seconds. - The display will indicate a Hi, Lo or two dashes depending on the set temperature change.

- - Displays nothing from the vehicle ON mode for 5 seconds.

Displays nothing from the vehicle ON mode for 5 seconds.

- - Blinks the current setting for the next 5 seconds.

Blinks the current setting for the next 5 seconds.

- - The display will indicate a Hi, Lo or two dashes depending on the set temperature change.

The display will indicate a Hi, Lo or two dashes depending on the set temperature change.

Courtesy of HONDA, U.S.A., INC.

How to Change the Set Temperature (Climate Control Panel without Display)

The climate control unit has a function to change the set temperature +2.7 deg.F (+1.5 deg.C) or -2.7 deg.F (-1.5 deg.C) in case customers feel the temperature is too warm or too cold for the displayed temperature.

NOTE: Verify that the climate control and A/C system is working properly before enabling the customize function to offset the set temperature.

The setting temperature is only displayed in degrees centigrade (deg.C).

- Turn the vehicle to the ON mode, then turn the vehicle to the OFF (LOCK) mode after confirming the climate control system is OFF.

- Press and hold the pair of buttons according to the table.

- While holding the buttons, turn the vehicle to the ON mode.

- Release the buttons, then select the desired temperature shift icon on the display.

Buttons

Courtesy of HONDA, U.S.A., INC. | Courtesy of HONDA, U.S.A., INC. | or | Courtesy of HONDA, U.S.A., INC.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.

- How to cancel A/C User Customizing

- - Turn the vehicle to the OFF (LOCK) mode.

- - Turn the vehicle to the OFF (LOCK) mode.

Turn the vehicle to the OFF (LOCK) mode.
````

## Chunk 8891: Climate Control System Description - Overview

- Title: Climate Control System Description - Overview
- Source path: `pages\11444.html`
- Chunk ID: `chunk_ee37aa246029`
- Images: `images\GHH409218.jpeg`, `images\GHH409219.jpeg`
- Duplicate sources: `pages\15841.html`

### Full Text

````text
# Climate Control System Description - Overview

For locations of each component on vehicle, refer to Component Location Index .

System Diagram

Courtesy of HONDA, U.S.A., INC.

Climate Control

Courtesy of HONDA, U.S.A., INC.

The climate control system transmits appropriate signals to each motor based on the information (sunlight, in-car temperature, outside air temperature) received from each sensor. See below for details.

- Air Mix Control Motor: The system controls the temperature of air coming into the cabin by the air mix control motor adjusting the air mix control damper position in order to change the mixing ratio of warm and cold air.

- Mode Control Motor: The system directs the airflow to the specified area by the mode control motor switching the mode control damper position to the "VENT", "HEAT/VENT", "HEAT", "HEAT/DEF", or "DEF".

- Recirculation Control Motor: The recirculation control motor switches the recirculation control damper position to the "FRESH" or "RECIRCULATION".

- Blower Motor: The blower motor changes the air volume based on the voltage adjusted by the blower power transistor.

The climate control unit optimizes these controls in order to maintain passenger comfort.

Relationship Between Vent (Air Outlet) Temperature and Actual In-Car Temperature

The climate control unit can automatically control vent temperature (air mix position), blower motor speed, blower intake, and A/C compressor operation to raise or lower the vehicle's interior temperature to match the customer's setting temperature. The actual vent outlet temperature largely depends upon the difference between the in-car temperature sensor reading and the customer's setting temperature.

Warm-Up Control

If heating is desired, and there is no available heat due to low engine coolant temperature, the climate control unit will slow the fan speed to avoid ventilating cold air. The climate control unit will gradually increase the fan speed as the engine coolant temperature rises.

The conditions that this control becomes effective are as follows:

- Fan speed "AUTO"

- Air outlet position "AUTO", "HEAT", "HEAT/DEF", or "DEF"

- Outside air temperature is less than 68 deg.F (20 deg.C)

- Engine coolant temperature sensor is normal.

- Except Type-R: Engine coolant temperature is less than 149 deg.F (65 deg.C)

- Type-R: Engine coolant temperature is less than 131 deg.F (55 deg.C)

Low Engine Coolant Temperature Control

When engine coolant temperature is low, the climate control system changes an air outlet position to the "DEF". When the engine coolant temperature increases, the climate control system controls the air outlet position and outlet air temperature automatically.

Relationship Between Vehicle Speed and Blower Intake Mode

Because the air resistance is different between fresh air and recirculated air, the volume of air coming through the vents would be different if the fan speed was constant. When the recirculation control damper is set to "FRESH", the fresh air flow increases as the vehicle speed increases. The climate control unit regulates the fan speed so that the air volume is the same when "FRESH" or "RECIRCULATION" mode is selected.

A/C Control

To prevent the evaporator from freezing, the climate control unit switches the A/C compressor ON and OFF based on the evaporator temperature sensor value. While in the automatic operation mode, the climate control unit automatically varies the A/C compressor operation time based on the evaporator temperature sensor value, as well as the outside air temperature.

MAX Control

When the temperature setting is adjusted to "MAX COOL (Lo)" or "MAX HOT (Hi)", the climate control unit overrides automatic control and defaults to the following operation:

- MAX COOL "RECIRCULATION", "VENT", blower fan maximum speed, and A/C system ON.

"RECIRCULATION", "VENT", blower fan maximum speed, and A/C system ON.

- MAX HOT "FRESH", "HEAT*", blower fan maximum speed, and A/C system ON.*: If the sensor information indicates that the windshield may fog, the air outlet switches to "HEAT/DEF" automatically.

"FRESH", "HEAT*", blower fan maximum speed, and A/C system ON.*: If the sensor information indicates that the windshield may fog, the air outlet switches to "HEAT/DEF" automatically.

ECON Control

- A/C compressor load control Reduces load on A/C compressor by slightly raising the target temperature of the evaporator.
````

## Chunk 8892: Climate Control System Description - Overview

- Title: Climate Control System Description - Overview
- Source path: `pages\11444.html`
- Chunk ID: `chunk_955a3e4cf01f`
- Images: `images\GHH409218.jpeg`, `images\GHH409219.jpeg`
- Duplicate sources: `pages\15841.html`

### Full Text

````text
o "MAX COOL (Lo)" or "MAX HOT (Hi)", the climate control unit overrides automatic control and defaults to the following operation:

- MAX COOL "RECIRCULATION", "VENT", blower fan maximum speed, and A/C system ON.

"RECIRCULATION", "VENT", blower fan maximum speed, and A/C system ON.

- MAX HOT "FRESH", "HEAT*", blower fan maximum speed, and A/C system ON.*: If the sensor information indicates that the windshield may fog, the air outlet switches to "HEAT/DEF" automatically.

"FRESH", "HEAT*", blower fan maximum speed, and A/C system ON.*: If the sensor information indicates that the windshield may fog, the air outlet switches to "HEAT/DEF" automatically.

ECON Control

- A/C compressor load control Reduces load on A/C compressor by slightly raising the target temperature of the evaporator.

Reduces load on A/C compressor by slightly raising the target temperature of the evaporator.

- Blower fan speed control Control the blower fan speed low compared to normal operation for an energy-saving operation with low air volume.

Control the blower fan speed low compared to normal operation for an energy-saving operation with low air volume.
````

## Chunk 8893: Climate Control System Description - Sunlight Sensor

- Title: Climate Control System Description - Sunlight Sensor
- Source path: `pages\11445.html`
- Chunk ID: `chunk_d3f8dc8b74b6`
- Images: `images\GHH409220.jpeg`
- Duplicate sources: `pages\15842.html`

### Full Text

````text
# Climate Control System Description - Sunlight Sensor

The sunlight sensor is attached to the upper face of the dashboard. The sunlight sensor uses a photodiode-type optical sensor which changes current in proportion to the sunlight intensity. The climate control unit reads the voltage fluctuation of the sunlight sensor.

NOTE: This illustration is an example only. The appearance and structure of the actual parts may vary depending on the model.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8894: Rear Window Defogger System Description - Control/Function

- Title: Rear Window Defogger System Description - Control/Function
- Source path: `pages\11446.html`
- Chunk ID: `chunk_65103aa718f6`
- Images: `images\GHH409221.jpeg`
- Duplicate sources: `pages\15843.html`

### Full Text

````text
# Rear Window Defogger System Description - Control/Function

The Timer Function

The rear window defogger provides the timer control function that is controlled by the climate control unit. The timer control is operated by turning the vehicle to the ON mode, then turning on the rear window defogger/mirror defogger switch*. The timer operating time varies according to ambient temperature. If the rear window defogger/mirror defogger* switch is turned on when the timer is active, it toggles between ON and OFF every time the switch is pressed.*: With Mirror Defogger

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8895: Rear Window Defogger System Description - System Diagram

- Title: Rear Window Defogger System Description - System Diagram
- Source path: `pages\11447.html`
- Chunk ID: `chunk_7eeb32d0dcf1`
- Images: `images\GHH409222.jpeg`
- Duplicate sources: `pages\15844.html`

### Full Text

````text
# Rear Window Defogger System Description - System Diagram

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8896: A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (Except K20C1)

- Title: A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (Except K20C1)
- Source path: `pages\11448.html`
- Chunk ID: `chunk_6b8aa2e1dd8c`
- Images: none
- Duplicate sources: `pages\15845.html`

### Full Text

````text
# A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (Except K20C1)

Diagnostic Procedure

Probable cause: Communication malfunction between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Also Check for

Climate control DTCs
````

## Chunk 8897: A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (K20C1) (2017 2018 2019 2020 2021)

- Title: A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11449.html`
- Chunk ID: `chunk_8f20d1865081`
- Images: none
- Duplicate sources: `pages\15846.html`

### Full Text

````text
# A/C information does not display on the center display unit, but the blower, heater and A/C system controls work (climate control panel without display) (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause: Communication malfunction between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Check the B-CAN line between the audio unit *1 or the audio-navigation unit *2 and the climate control unit

Also Check for

Climate control DTCs
````

## Chunk 8898: Blower fan runs slower than expected in cold weather (when in AUTO mode) (Except K20C1)

- Title: Blower fan runs slower than expected in cold weather (when in AUTO mode) (Except K20C1)
- Source path: `pages\11450.html`
- Chunk ID: `chunk_69afbd056fdd`
- Images: none
- Duplicate sources: `pages\15847.html`

### Full Text

````text
# Blower fan runs slower than expected in cold weather (when in AUTO mode) (Except K20C1)

NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode

Diagnostic Procedure

Probable cause: Engine coolant temperature (ECT) circuit malfunction

Troubleshoot the ECT sensor circuit:

- USA and Canada models

- - ECT sensor 2 circuit range/performance problem - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage

- - ECT sensor 2 circuit range/performance problem

ECT sensor 2 circuit range/performance problem

- - ECT sensor 2 circuit low voltage

ECT sensor 2 circuit low voltage

- - ECT sensor 2 circuit high voltage

ECT sensor 2 circuit high voltage

- Mexico models

- - ECT sensor 2 circuit low voltage - ECT sensor 2 circuit high voltage

- - ECT sensor 2 circuit low voltage

ECT sensor 2 circuit low voltage

- - ECT sensor 2 circuit high voltage

ECT sensor 2 circuit high voltage

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Blower motor operation
````

## Chunk 8899: Blower fan runs slower than expected in cold weather (when in AUTO mode) (K20C1) (2017 2018 2019 2020 2021)

- Title: Blower fan runs slower than expected in cold weather (when in AUTO mode) (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11451.html`
- Chunk ID: `chunk_1a2471f42102`
- Images: none
- Duplicate sources: `pages\15848.html`

### Full Text

````text
# Blower fan runs slower than expected in cold weather (when in AUTO mode) (K20C1) (2017 2018 2019 2020 2021)

NOTE: It is normal for the blower fan to run slowly until the coolant temperature rises when in AUTO mode

Diagnostic Procedure

Probable cause: Engine coolant temperature (ECT) circuit malfunction

Troubleshoot the ECT sensor circuit:

- ECT sensor 1 circuit low voltage

- ECT sensor 1 circuit high voltage

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Blower motor operation
````

## Chunk 8900: Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (Except K20C1)

- Title: Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (Except K20C1)
- Source path: `pages\11452.html`
- Chunk ID: `chunk_9fb64393e220`
- Images: none
- Duplicate sources: `pages\15849.html`

### Full Text

````text
# Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (Except K20C1)

Diagnostic Procedure

Probable cause:

- The air mix doors are malfunctioning Do the following troubleshooting:

Do the following troubleshooting:

- - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control)

- - Air mix control motor test

Air mix control motor test

- - Passenger's air mix control motor test (with dual zone climate control)

Passenger's air mix control motor test (with dual zone climate control)

- Low refrigerant charge

Also Check for

- Climate control DTCs

- Poor or loose connections at the terminals
````

## Chunk 8901: Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (K20C1) (2017 2018 2019 2020 2021)

- Title: Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11453.html`
- Chunk ID: `chunk_e5ce4dc5de66`
- Images: none
- Duplicate sources: `pages\15850.html`

### Full Text

````text
# Driver's and passenger's side vent temperatures vary by more than 20 °F (11 °C) (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause:

- The air mix doors are malfunctioning Do the following troubleshooting:

Do the following troubleshooting:

- - Air mix control motor test - Passenger's air mix control motor test (with dual zone climate control)

- - Air mix control motor test

Air mix control motor test

- - Passenger's air mix control motor test (with dual zone climate control)

Passenger's air mix control motor test (with dual zone climate control)

- Low refrigerant charge

Also Check for

- Climate control DTCs

- Harness/connections
````

## Chunk 8902: HDS does not communicate with the climate control unit or the vehicle (Except K20C1)

- Title: HDS does not communicate with the climate control unit or the vehicle (Except K20C1)
- Source path: `pages\11454.html`
- Chunk ID: `chunk_3bc3b41ace30`
- Images: none
- Duplicate sources: `pages\15851.html`

### Full Text

````text
# HDS does not communicate with the climate control unit or the vehicle (Except K20C1)

Diagnostic Procedure

- Troubleshoot the DLC circuit
````

## Chunk 8903: HDS does not communicate with the climate control unit or the vehicle (K20C1) (2017 2018 2019 2020 2021)

- Title: HDS does not communicate with the climate control unit or the vehicle (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11455.html`
- Chunk ID: `chunk_8deb03b65b24`
- Images: none
- Duplicate sources: `pages\15852.html`

### Full Text

````text
# HDS does not communicate with the climate control unit or the vehicle (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

- Troubleshoot the DLC circuit
````

## Chunk 8904: Insufficient heating (Except K20C1)

- Title: Insufficient heating (Except K20C1)
- Source path: `pages\11456.html`
- Chunk ID: `chunk_218257c9bb0a`
- Images: none
- Duplicate sources: `pages\15853.html`

### Full Text

````text
# Insufficient heating (Except K20C1)

Diagnostic Procedure

- Check the coolant level

- Check the expansion tank cap

- Check the engine coolant temperature (ECT) during normal operation with the HDS

- Check the heater core inlet hose temperature:

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump

- If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- Check the operation of the air mix doors:

- Air mix control motor test Passenger's air mix control motor test (with dual zone climate control)

- Air mix control motor test

- Passenger's air mix control motor test (with dual zone climate control)

- Check the blower motor unit for obstructions

- Check for air leaks around the ducts and vents

Also Check for

Climate control DTCs
````

## Chunk 8905: Insufficient heating (K20C1) (2017 2018 2019 2020 2021)

- Title: Insufficient heating (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11457.html`
- Chunk ID: `chunk_95e9db2e74d7`
- Images: none
- Duplicate sources: `pages\15854.html`

### Full Text

````text
# Insufficient heating (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

- Check the coolant level

- Check the expansion tank cap

- Check the engine coolant temperature (ECT) during normal operation with the HDS

- Check the heater core inlet hose temperature:

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- If it is COLD, check for restrictions in the hose, a damaged or leaking thermostat, or a damaged or leaking water pump

- If it is HOT, check for restrictions in the heater core. Back flush or replace the heater core

- Check the operation of the air mix doors:

- Air mix control motor test Passenger's air mix control motor test (with dual zone climate control)

- Air mix control motor test

- Passenger's air mix control motor test (with dual zone climate control)

- Check the blower motor unit for obstructions

- Check for air leaks around the ducts and vents

Also Check for

Climate control DTCs
````

## Chunk 8906: The A/C compressor clutch and the A/C condenser/radiator fans are inoperative, but the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C compressor clutch and the A/C condenser/radiator fans are inoperative, but the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11458.html`
- Chunk ID: `chunk_ac9f7df85383`
- Images: none
- Duplicate sources: `pages\15855.html`

### Full Text

````text
# The A/C compressor clutch and the A/C condenser/radiator fans are inoperative, but the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause: A/C pressure sensor circuit malfunction or evaporator temperature sensor circuit malfunction

Troubleshoot the A/C pressure sensor circuit:

- A/C pressure sensor circuit low voltage

- A/C pressure sensor circuit high voltage

NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Abnormal A/C system pressures

- Evaporator temperature sensor

- Harness/connections
````

## Chunk 8907: The A/C compressor clutch and the cooling fan are inoperative, but the blower and heater controls work (Except K20C1)

- Title: The A/C compressor clutch and the cooling fan are inoperative, but the blower and heater controls work (Except K20C1)
- Source path: `pages\11459.html`
- Chunk ID: `chunk_f88236795300`
- Images: none
- Duplicate sources: `pages\15856.html`

### Full Text

````text
# The A/C compressor clutch and the cooling fan are inoperative, but the blower and heater controls work (Except K20C1)

Diagnostic Procedure

Probable cause: A/C pressure sensor circuit malfunction or evaporator temperature sensor circuit malfunction

Troubleshoot the A/C pressure sensor circuit:

- A/C pressure sensor circuit low voltage

- A/C pressure sensor circuit high voltage

NOTE: The A/C pressure sensor circuit can malfunction without setting a DTC

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Abnormal A/C system pressures

- Faulty evaporator temperature sensor

- Poor or loose connections at the terminals
````

## Chunk 8908: The A/C compressor clutch cycles rapidly on and off (Except K20C1)

- Title: The A/C compressor clutch cycles rapidly on and off (Except K20C1)
- Source path: `pages\11460.html`
- Chunk ID: `chunk_73db732e7b0b`
- Images: none
- Duplicate sources: `pages\15857.html`

### Full Text

````text
# The A/C compressor clutch cycles rapidly on and off (Except K20C1)

Diagnostic Procedure

Probable cause:

- A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off)

- Cooling fan inoperative

- Low idle speed

- Evaporator temperature sensor malfunction Do the evaporator temperature sensor test

Do the evaporator temperature sensor test

Also Check for

- Climate control DTCs

- If there is no leak and the refrigerant level is normal, do the A/C compressor clutch circuit troubleshooting , and look for an intermittent problem

- Faulty A/C pressure sensor
````

## Chunk 8909: The A/C compressor clutch cycles rapidly on and off (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C compressor clutch cycles rapidly on and off (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11461.html`
- Chunk ID: `chunk_3efd7f048c5f`
- Images: none
- Duplicate sources: `pages\15858.html`

### Full Text

````text
# The A/C compressor clutch cycles rapidly on and off (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause:

- A/C system is overcharged (Excessive pressure on high side of system causing pressure sensor to turn A/C compressor off)

- Radiator and/or A/C condenser fan inoperative

- Low idle speed

- Evaporator temperature sensor malfunction Do the evaporator temperature sensor test

Do the evaporator temperature sensor test

Also Check for

- Climate control DTCs

- If there is no leak and the refrigerant level is normal, do the symptom troubleshooting , and look for an intermittent problem

- A/C pressure sensor
````

## Chunk 8910: The A/C compressor clutch does not disengage when the A/C switch is off (Except K20C1)

- Title: The A/C compressor clutch does not disengage when the A/C switch is off (Except K20C1)
- Source path: `pages\11462.html`
- Chunk ID: `chunk_42708a0a0b6a`
- Images: none
- Duplicate sources: `pages\15859.html`

### Full Text

````text
# The A/C compressor clutch does not disengage when the A/C switch is off (Except K20C1)

Diagnostic Procedure

Probable cause: The A/C compressor clutch circuit is on (energized) continuously, shorted to ground, stuck A/C compressor clutch relay, or the A/C compressor clutch is mechanically jammed

Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch

Also Check for

The A/C compressor relief valve. If it has vented refrigerant to the atmosphere, correct the problem with the A/C compressor clutch or the A/C compressor clutch circuit, then replace the A/C compressor relief valve
````

## Chunk 8911: The A/C compressor clutch does not disengage when the A/C switch is off (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C compressor clutch does not disengage when the A/C switch is off (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11463.html`
- Chunk ID: `chunk_5cc7191381b4`
- Images: none
- Duplicate sources: `pages\15860.html`

### Full Text

````text
# The A/C compressor clutch does not disengage when the A/C switch is off (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause: The A/C compressor clutch circuit is on (energized) continuously, shorted to ground, stuck A/C compressor clutch relay, or the A/C compressor clutch is mechanically jammed

Do the A/C compressor clutch check , and repair any problems with the A/C compressor clutch

Also Check for

The A/C compressor relief valve. If it has vented refrigerant to the atmosphere, correct the problem with the A/C compressor clutch or the A/C compressor clutch circuit, then replace the A/C compressor relief valve
````

## Chunk 8912: The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11464.html`
- Chunk ID: `chunk_05774494a48d`
- Images: none
- Duplicate sources: `pages\15861.html`

### Full Text

````text
# The A/C compressor clutch does not engage, but the A/C condenser/radiator fans operate, and the blower and heater controls work (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Climate control DTCs

- Blown fuse No. A23 (10 A) in the under-hood fuse/relay box

- A/C compressor clutch relay

- PCM

- Abnormal A/C system pressures

- Harness/connections
````

## Chunk 8913: The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

- Title: The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)
- Source path: `pages\11465.html`
- Chunk ID: `chunk_75c8c09c44af`
- Images: none
- Duplicate sources: `pages\15862.html`

### Full Text

````text
# The A/C compressor clutch does not engage, but the cooling fan operate, and the blower and heater controls work (Except K20C1)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Climate control DTCs

- Blown fuse No. A23 (10 A) in the under-hood fuse/relay box

- Abnormal A/C system pressures

- Poor or loose connections at the terminals
````

## Chunk 8914: The A/C compressor relief valve has vented refrigerant (Except K20C1)

- Title: The A/C compressor relief valve has vented refrigerant (Except K20C1)
- Source path: `pages\11466.html`
- Chunk ID: `chunk_6483709345ea`
- Images: none
- Duplicate sources: `pages\15863.html`

### Full Text

````text
# The A/C compressor relief valve has vented refrigerant (Except K20C1)

NOTE: This indicates the A/C system high side pressure was high

Diagnostic Procedure

Probable cause: A high-side restriction, the cooling fan is inoperative, or the A/C compressor clutch is not disengaging

- If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection

Do the A/C system contamination inspection

- If the A/C compressor clutch will not disengage, troubleshoot the A/C compressor clutch circuit , and check for mechanical problems

- If the cooling fan is inoperative, troubleshoot the RFC system malfunction

Also Check for

PGM-FI DTCs
````

## Chunk 8915: The A/C compressor relief valve has vented refrigerant (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C compressor relief valve has vented refrigerant (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11467.html`
- Chunk ID: `chunk_ec884f83c2ed`
- Images: none
- Duplicate sources: `pages\15864.html`

### Full Text

````text
# The A/C compressor relief valve has vented refrigerant (K20C1) (2017 2018 2019 2020 2021)

NOTE: This indicates the A/C system high side pressure was high

Diagnostic Procedure

Probable cause: A high-side restriction, the A/C condenser/radiator fans are inoperative, or the A/C compressor clutch is not disengaging

- If the fans and A/C compressor clutch operate normally, feel the lines for restrictions Do the A/C system contamination inspection

Do the A/C system contamination inspection

- If the A/C compressor clutch will not disengage, do the symptom troubleshooting , and check for mechanical problems

- If the fans is inoperative, do the symptom troubleshooting

Also Check for

PGM-FI DTCs
````

## Chunk 8916: The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11468.html`
- Chunk ID: `chunk_e2c80d5372c7`
- Images: none
- Duplicate sources: `pages\15865.html`

### Full Text

````text
# The A/C condenser/radiator fans do not run at high speed, but do run at low speed with the A/C on (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

Probable cause: Malfunction in the fan(s) high speed circuit

Do the following troubleshooting as needed:

- Symptom Troubleshooting

- Radiator fan high speed circuit troubleshooting

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Blown fuse No. A10 (20 A) in the under-hood fuse/relay box

- Blown fuse No. A11 (5 A) in the under-hood fuse/relay box

- A/C condenser fan relay

- PCM

- Harness/connections
````

## Chunk 8917: The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

- Title: The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11469.html`
- Chunk ID: `chunk_6980fc1b38be`
- Images: none
- Duplicate sources: `pages\15866.html`

### Full Text

````text
# The A/C condenser/radiator fans do not run at low speed with the A/C on, but the blower and heater controls work normally (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Climate control DTCs

- PGM-FI DTCs

- Blown fuse No. A1-3 (30 A) in the under-hood fuse/relay box

- Poor ground at G401

- Radiator fan relay

- Fan control relay

- Radiator fan motor

- A/C condenser fan motor

- PCM

- Harness/connections
````

## Chunk 8918: The blower and the heater controls and the A/C system do not work (Except K20C1)

- Title: The blower and the heater controls and the A/C system do not work (Except K20C1)
- Source path: `pages\11470.html`
- Chunk ID: `chunk_f40e947b4161`
- Images: none
- Duplicate sources: `pages\15867.html`

### Full Text

````text
# The blower and the heater controls and the A/C system do not work (Except K20C1)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Climate control DTCs

- Blown fuse No. B9 (10 A) in the under-dash fuse/relay box

- Poor ground at G505

- Poor or loose connections at the terminals
````

## Chunk 8919: The blower and the heater controls and the A/C system do not work (K20C1) (2017 2018 2019 2020 2021)

- Title: The blower and the heater controls and the A/C system do not work (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11471.html`
- Chunk ID: `chunk_5170f9886272`
- Images: none
- Duplicate sources: `pages\15868.html`

### Full Text

````text
# The blower and the heater controls and the A/C system do not work (K20C1) (2017 2018 2019 2020 2021)

Diagnostic Procedure

- Symptom Troubleshooting

Also Check for

- Blown fuse No. B9 (10 A) in the under-dash fuse/relay box

- Poor ground at G505

- Climate control unit

- Harness/connections
````

## Chunk 8920: A/C Signal Circuit Troubleshooting (K20C1) (2017 2018 2019 2020 2021)

- Title: A/C Signal Circuit Troubleshooting (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11472.html`
- Chunk ID: `chunk_f483f7381c1b`
- Images: none
- Duplicate sources: `pages\15869.html`

### Full Text

````text
# A/C Signal Circuit Troubleshooting (K20C1) (2017 2018 2019 2020 2021)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Are any Pending or Confirmed DTCs indicated? YES Go to the indicated DTC's troubleshooting. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

Are any Pending or Confirmed DTCs indicated?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to step 2.

- A/C compressor clutch condition check -1. Start the engine, and let it idle. -2. Turn the blower switch on. -3. Turn the A/C switch on. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit A/C CLUTCH ON Do the current condition(s) match the threshold? YES Go to step 3. NO Do the A/C system test .

-1. Start the engine, and let it idle.

-2. Turn the blower switch on.

-3. Turn the A/C switch on.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

A/C CLUTCH | ON

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Do the A/C system test .

- A/C system check -1. Check the A/C system . Does the A/C system operate? YES The A/C system circuit is OK. NO Go to step 4.

-1. Check the A/C system .

Does the A/C system operate?

YES

The A/C system circuit is OK.

NO

Go to step 4.

- A/C compressor clutch circuit check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Activate the A/C CLUTCH in the INSPECTION MENU with the HDS. A/C CLUTCH Is there a clicking noise from the A/C compressor clutch? YES The A/C compressor clutch circuit is OK. Do the A/C system test . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Activate the A/C CLUTCH in the INSPECTION MENU with the HDS.

A/C CLUTCH

Is there a clicking noise from the A/C compressor clutch?

YES

The A/C compressor clutch circuit is OK. Do the A/C system test .

NO

Go to step 5.

- Open wire check (A/C MG CLUTCH RLY CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Turn the vehicle to the ON mode. -5. Connect terminals A and B with a jumper wire. Terminal A PCM connector No. 2 (58P) No. 48 Terminal B Body ground Is there a clicking noise from the A/C compressor clutch? YES The A/C MG CLUTCH RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM . NO Check for poor connections or loose terminals at the A/C compressor clutch relay and the PCM. If the connections and terminals are OK, check the A/C compressor clutch relay. If needed, repair an open in the A/C MG CLUTCH RLY CL- wire between PCM connector No. 2 terminal No. 48 and the A/C compressor clutch relay, or other parts in the A/C systems.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Turn the vehicle to the ON mode.

-5. Connect terminals A and B with a jumper wire.

Terminal A | PCM connector No. 2 (58P) No. 48

Terminal B | Body ground

Is there a clicking noise from the A/C compressor clutch?

YES

The A/C MG CLUTCH RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If the symptom/indication goes away and the PCM was substituted, replace the original PCM .

NO

Check for poor connections or loose terminals at the A/C compressor clutch relay and the PCM. If the connections and terminals are OK, check the A/C compressor clutch relay. If needed, repair an open in the A/C MG CLUTCH RLY CL- wire between PCM connector No. 2 terminal No. 48 and the A/C compressor clutch relay, or other parts in the A/C systems.
````

## Chunk 8921: A/C Diagnostic Process

- Title: A/C Diagnostic Process
- Source path: `pages\11473.html`
- Chunk ID: `chunk_4139c745777b`
- Images: none
- Duplicate sources: `pages\15870.html`

### Full Text

````text
# A/C Diagnostic Process

When a customer presents an A/C concern, do the following procedure to identify the cause of the problem.

Confirm the type of concern.

- If a customer complains about an A/C performance problem, go to step 2.

- If a customer complains about an A/C noise problem, do the A/C system noise check .

2. Do the A/C system inspection and repair any problems. If no problems are found, go to step 3. Recover the refrigerant from the A/C system and measure the refrigerant charge from the A/C system using an A/C recover/recycle/recharge machine.

- If the refrigerant charge is within specifications, go to step 5.

- If the refrigerant charge is significantly under specifications, go to step 4.

- If the refrigerant charge is significantly over specifications, go to step 5.

4. Do the refrigerant leak check and repair any leaks. If no leaks are found, go to step 5. Evacuate and recharge the system and do the A/C system test .

- If vent temperature or suction/discharge pressures are within specifications, the repair is confirmed and the A/C diagnostic process is complete.

- If vent temperature or suction/discharge pressures are not within specifications, a problem may still exist. Return to step 2, and recheck your test procedures.
````

## Chunk 8922: Climate Control System Circuit Diagram (Except K20C1)

- Title: Climate Control System Circuit Diagram (Except K20C1)
- Source path: `pages\11474.html`
- Chunk ID: `chunk_1c1f0ff2feee`
- Images: `images\GHH409223.jpeg`, `images\GHH409224.jpeg`, `images\GHH409225.jpeg`, `images\GHH409226.jpeg`, `images\GHH409227.jpeg`, `images\GHH409228.jpeg`, `images\GHH409229.jpeg`
- Duplicate sources: `pages\15871.html`

### Full Text

````text
# Climate Control System Circuit Diagram (Except K20C1)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8923: Climate Control System Circuit Diagram (K20C1) (2017 2018 2019 2020 2021)

- Title: Climate Control System Circuit Diagram (K20C1) (2017 2018 2019 2020 2021)
- Source path: `pages\11475.html`
- Chunk ID: `chunk_678e43a618f3`
- Images: `images\GHH409230.jpeg`, `images\GHH409231.jpeg`, `images\GHH409232.jpeg`, `images\GHH409233.jpeg`, `images\GHH409234.jpeg`, `images\GHH409235.jpeg`
- Duplicate sources: `pages\15872.html`

### Full Text

````text
# Climate Control System Circuit Diagram (K20C1) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8924: Rear Window Defogger Circuit Diagram (2/4-door with Keyless Access System)

- Title: Rear Window Defogger Circuit Diagram (2/4-door with Keyless Access System)
- Source path: `pages\11476.html`
- Chunk ID: `chunk_b97ff63fea4e`
- Images: `images\GHH409236.jpeg`
- Duplicate sources: `pages\15873.html`

### Full Text

````text
# Rear Window Defogger Circuit Diagram (2/4-door with Keyless Access System)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8925: Rear Window Defogger Circuit Diagram (2/4-door without Keyless Access System)

- Title: Rear Window Defogger Circuit Diagram (2/4-door without Keyless Access System)
- Source path: `pages\11477.html`
- Chunk ID: `chunk_3b2248affde9`
- Images: `images\GHH409237.jpeg`
- Duplicate sources: `pages\15874.html`

### Full Text

````text
# Rear Window Defogger Circuit Diagram (2/4-door without Keyless Access System)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8926: Rear Window Defogger Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)

- Title: Rear Window Defogger Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)
- Source path: `pages\11478.html`
- Chunk ID: `chunk_67b7a931ac32`
- Images: `images\GHH409238.jpeg`
- Duplicate sources: `pages\15875.html`

### Full Text

````text
# Rear Window Defogger Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8927: Rear Window Defogger Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)

- Title: Rear Window Defogger Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)
- Source path: `pages\11479.html`
- Chunk ID: `chunk_79e09611e9d9`
- Images: `images\GHH409239.jpeg`
- Duplicate sources: `pages\15876.html`

### Full Text

````text
# Rear Window Defogger Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8928: Drive Belt Auto-Tensioner Air Bleeding (L15B7): Bleeding

- Title: Drive Belt Auto-Tensioner Air Bleeding (L15B7): Bleeding
- Source path: `pages\11480.html`
- Chunk ID: `chunk_3d672d4f0168`
- Images: `images\GHH409240.jpeg`
- Duplicate sources: `pages\15877.html`

### Full Text

````text
# Drive Belt Auto-Tensioner Air Bleeding (L15B7): Bleeding

- Drive Belt - Remove

- Drive Belt Auto-Tensioner - Air Bleed Courtesy of HONDA, U.S.A., INC. 1. Attach a socket wrench to the drive belt auto-tensioner from above the engine. Slowly (at least 3 seconds) compress the auto-tensioner in the direction shown, the full length of its stroke, then slowly (at least 3 seconds) move the auto-tensioner in the opposite direction, the full length of its stroke. Repeat this operation three times.

Courtesy of HONDA, U.S.A., INC. | 1. Attach a socket wrench to the drive belt auto-tensioner from above the engine. Slowly (at least 3 seconds) compress the auto-tensioner in the direction shown, the full length of its stroke, then slowly (at least 3 seconds) move the auto-tensioner in the opposite direction, the full length of its stroke. Repeat this operation three times.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 8929: Rear Window Defogger Wire Repair: Reconditioning

- Title: Rear Window Defogger Wire Repair: Reconditioning
- Source path: `pages\11481.html`
- Chunk ID: `chunk_55c9c4e5c517`
- Images: `images\GHH409241.jpeg`, `images\GHH409242.jpeg`
- Duplicate sources: `pages\15878.html`

### Full Text

````text
# Rear Window Defogger Wire Repair: Reconditioning

- Defogger Wire - Repair Courtesy of HONDA, U.S.A., INC. NOTE: To make an effective repair, the broken section must be no longer than 25 mm (1.0 in). 1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol. 2. Carefully mask above and below the broken area of the rear window defogger wire (B) with cellophane tapes (C). Courtesy of HONDA, U.S.A., INC. 3. Using a small brush, apply a heavy coat of silver conductive paint (commercially available) (A) extending about 3.0 mm (0.1 in) on both sides of the break. Allow 25 minutes to dry. 4. Do the function test to confirm that the wire is repaired. 5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.

Courtesy of HONDA, U.S.A., INC. | NOTE: To make an effective repair, the broken section must be no longer than 25 mm (1.0 in). 1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol. 2. Carefully mask above and below the broken area of the rear window defogger wire (B) with cellophane tapes (C).

1. Lightly rub the area around the broken section (A) with fine steel wool, then clean it with isopropyl alcohol.

2. Carefully mask above and below the broken area of the rear window defogger wire (B) with cellophane tapes (C).

Courtesy of HONDA, U.S.A., INC. | 3. Using a small brush, apply a heavy coat of silver conductive paint (commercially available) (A) extending about 3.0 mm (0.1 in) on both sides of the break. Allow 25 minutes to dry. 4. Do the function test to confirm that the wire is repaired. 5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.

4. Do the function test to confirm that the wire is repaired.

5. Apply a second coat of paint in the same way. Let it dry 3 hours before removing the tape.
````

## Chunk 8930: Lubricants and Fluids (USA/Canada models Type-R/Si)

- Title: Lubricants and Fluids (USA/Canada models Type-R/Si)
- Source path: `pages\11483.html`
- Chunk ID: `chunk_dab2c530127b`
- Images: `images\GHH409876.jpeg`, `images\GHH409877.jpeg`
- Duplicate sources: `pages\14145.html`

### Full Text

````text
# Lubricants and Fluids (USA/Canada models Type-R/Si)

Application | Lubricant or Fluid

Engine | Honda Motor Oil: 0W-20 Look for the API certification seal on the oil container. Make sure it says "For Gasoline Engines." SAE Viscosity: See chart.

Manual transmission | Honda Manual Transmission Fluid (MTF): Always use Honda MTF. Using motor oil can cause stiffer shifting because it does not contain the proper additives.

Brake system (including VSA lines) Clutch system (manual transmission) | Honda DOT 3 Brake Fluid: Always use Honda DOT 3 Brake Fluid. Using a non-Honda brake fluid can cause corrosion and decrease the life of the system.

Cooling system | Always use Honda Long Life Antifreeze/Coolant Type 2. NOTE: For prolonged cold temperatures below -22°F (-30°C), add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) .

Courtesy of HONDA, U.S.A., INC.

For the details of the lubrication points and the type of lubricants to be applied, refer to the illustrated index and the various work procedures (such as Assembly/Reassembly, Replacement, Overhaul, Installation, etc.) contained in each section.

Application | Lubricant or Fluid

A | Brake booster clevis pin | Multipurpose grease

B | 12 volt battery terminals

C | Clutch master cylinder clevis and clevis pin

D | Fuel fill door

E | Hood hinges

F | Tailgate hinges (Type-R)

G | Front brake caliper pistons, boots, and seals (Type-R) | Honda DOT 3 Brake Fluid

Front brake caliper pins and pin boots (Si) | Honda silicone grease (P/N 08C30-B0234M) or service set grease (NIGLUBE RM)

Front brake caliper piston seals (Si) | Honda silicone grease (P/N 08C30-B0234M) or service set grease (silicone grease)

Front brake caliper piston boots (Si) | Honda silicone grease (P/N 08C30-B0234M) or service set grease (rubber grease)

Front brake caliper pistons (Si) | Honda DOT 3 Brake Fluid

H | Rear brake caliper piston boots | Honda silicone grease (P/N 08C30-B0234M) or ATE brake cylinder paste

I | Slave cylinder push rod | Super high temp urea grease (P/N 08798-9002)

Application | Lubricant or Fluid

J | Air conditioning compressor | Compressor Oil: RL85HM (POE oil: P/N 38899-RLV-A01) for refrigerant HFO-1234yf (R-1234yf)

NOTE: Lubricate the following areas using the recommended lubricants and fluids. In corrosive areas, more frequent lubrication is necessary.

- Lubricate the following areas using the recommended lubricants and fluids.

- In corrosive areas, more frequent lubrication is necessary.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8931: Lubricants and Fluids (USA/Canada models except Type-R/Si)

- Title: Lubricants and Fluids (USA/Canada models except Type-R/Si)
- Source path: `pages\11484.html`
- Chunk ID: `chunk_9ea76ca9e05b`
- Images: `images\GHH409878.jpeg`, `images\GHH409879.jpeg`, `images\GHH409880.jpeg`
- Duplicate sources: `pages\14146.html`

### Full Text

````text
# Lubricants and Fluids (USA/Canada models except Type-R/Si)

NOTE: Unless otherwise indicated, the illustration shows the 4-door model.

Application | Lubricant or Fluid

Engine | Honda Motor Oil: 0W-20 Look for the API certification seal on the oil container. Make sure it says "For Gasoline Engines." SAE Viscosity: See chart.

Manual transmission | Honda Manual Transmission Fluid (MTF): Always use Honda MTF. Using motor oil can cause stiffer shifting because it does not contain the proper additives.

CVT | Always use Honda HCF-2. NOTE: Using the wrong type of fluid will damage the transmission.

Brake system (including VSA lines) Clutch system (manual transmission) | Honda DOT 3 Brake Fluid: Always use Honda DOT 3 Brake Fluid. Using a non-Honda brake fluid can cause corrosion and decrease the life of the system.

Cooling system | Always use Honda Long Life Antifreeze/Coolant Type 2. NOTE: For prolonged cold temperatures below -22°F (-30°C), add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) .

Courtesy of HONDA, U.S.A., INC.

For the details of the lubrication points and the type of lubricants to be applied, refer to the illustrated index and the various work procedures (such as Assembly/Reassembly, Replacement, Overhaul, Installation, etc.) contained in each section.

Application | Lubricant or Fluid

A | Brake booster clevis pin | Multipurpose grease

B | 12 volt battery terminals

C | Clutch master cylinder clevis and clevis pin (manual transmission)

D | Fuel fill door

E | Hood hinges

F | Tailgate hinges (5-door)

G | Front brake caliper pins, pin bushings, and pin boots | Honda silicone grease (P/N 08C30-B0234M) or service set grease (NIGLUBE RM)

Front brake caliper piston boots | Honda silicone grease (P/N 08C30-B0234M) or service set grease (rubber grease)

Front brake caliper pistons and piston seals | Honda DOT 3 Brake Fluid

H | Rear brake caliper piston boots | Honda silicone grease (P/N 08C30-B0234M) or ATE brake cylinder paste

Application | Lubricant or Fluid

I | Slave cylinder push rod (manual transmission) | Super high temp urea grease (P/N 08798-9002)

J | Air conditioning compressor | Compressor Oil: RL85HM (POE oil: P/N 38899-RLV-A01) for refrigerant HFO-1234yf (R-1234yf)

NOTE: Lubricate the following areas using the recommended lubricants and fluids. In corrosive areas, more frequent lubrication is necessary.

- Lubricate the following areas using the recommended lubricants and fluids.

- In corrosive areas, more frequent lubrication is necessary.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8932: Maintenance Minder™ General Information (USA/Canada models with Multi-Information Display): Notes

- Title: Maintenance Minder™ General Information (USA/Canada models with Multi-Information Display): Notes
- Source path: `pages\11485.html`
- Chunk ID: `chunk_bd1718682349`
- Images: none
- Duplicate sources: `pages\14147.html`

### Full Text

````text
# Maintenance Minder™ General Information (USA/Canada models with Multi-Information Display): Notes

Maintenance Minder™ General Information
````

## Chunk 8933: Maintenance Minder

- Title: Maintenance Minder
- Source path: `pages\11486.html`
- Chunk ID: `chunk_3db281e41f6a`
- Images: `images\GHH409881.jpeg`, `images\GHH409882.jpeg`
- Duplicate sources: `pages\14148.html`

### Full Text

````text
# Maintenance Minder

The Maintenance Minder is an important feature of the multi-information display. Based on engine and transmission operating conditions, and accumulated engine revolutions, the Civic's onboard computer (PCM) calculates the remaining engine oil and the transmission fluid life. The system also displays the remaining engine oil life along with the code(s) for other scheduled maintenance items needing service.

Gauges:

Courtesy of HONDA, U.S.A., INC.

Steering Wheel:

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8934: Service Information

- Title: Service Information
- Source path: `pages\11487.html`
- Chunk ID: `chunk_230dd8753631`
- Images: `images\GHH409883.jpeg`, `images\GHH409884.jpeg`, `images\GHH409885.jpeg`, `images\GHH409886.jpeg`, `images\GHH409887.jpeg`, `images\GHH409888.jpeg`
- Duplicate sources: `pages\14149.html`

### Full Text

````text
# Service Information

1. The remaining engine oil life is shown as a percentage on the multi-information display. To see the current engine oil life, turn the vehicle to the ON mode, then press the INFORMATION switch repeatedly until "Maintenance Minder (A)" appears on the multi-information display. Press the Source/Enter button to show the current engine oil life (B) on the display.

Courtesy of HONDA, U.S.A., INC.

2. When the vehicle is in the ON mode, and the remaining engine oil life is 15% to 6%, the remaining engine oil life and other scheduled maintenance item(s) needing service are displayed.

The Maintenance Minder message "Maintenance Due Soon" (A) also comes on. To cancel the message, press the INFORMATION switch or Audio Remote/Multi-Information Display Switch. The display continues to show the remaining engine oil life (B) and the message indicator (C) until it is reset.

- Complete list of maintenance main items (D) .

- Complete list of maintenance sub items (E) .

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

3. When the vehicle is in the ON mode, and the remaining engine oil life is 5% to 1%, the Maintenance Minder message "Maintenance Due Now" (A) is displayed along with the same maintenance item code(s).

Courtesy of HONDA, U.S.A., INC.

4. When the vehicle is in the ON mode, and the remaining engine oil life is 0%, the Maintenance Minder message "Maintenance Past Due" is displayed along with the same maintenance item code(s).

Courtesy of HONDA, U.S.A., INC.

5. If the indicated maintenance is not done, the Maintenance Minder shows a negative distance traveled (A), for example "-10 miles," on the display. If the negative distance traveled is between 0 and 9, the message is displayed for only a few seconds when turning the vehicle to the ON mode. The negative distance traveled remains displayed after the vehicle is driven more than 10 miles (for USA models) or 10 km (for Canada models) after 0% oil life is reached, and the display cannot be canceled. This means the indicated maintenance item(s) should have been done more than 10 miles (or 10 km) ago.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8935: Resetting the Maintenance Minder

- Title: Resetting the Maintenance Minder
- Source path: `pages\11488.html`
- Chunk ID: `chunk_38f17a069afd`
- Images: `images\GHH409889.jpeg`, `images\GHH409890.jpeg`
- Duplicate sources: `pages\14150.html`

### Full Text

````text
# Resetting the Maintenance Minder

NOTE:

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

1. Turn the vehicle to the ON mode.

2. If system message(s) are displayed, press the INFORMATION switch or Audio Remote/Multi-Information Display Switch to cancel the display until the "Maintenance Minder" icon is displayed, then press the Source/Enter button.

3. Display shows the remaining engine oil life, and then press and hold the Source/Enter button for 10 seconds or more. The "Maintenance Reset" mode appears on the multi-information display.

NOTE:

- If you are resetting the Maintenance Minder when the engine oil life is more than 15%, make sure any maintenance item(s) requiring service are done before resetting the display.

- To cancel the "Maintenance Reset" mode, press the Audio Remote/Multi-Information Display Switch to select the "Cancel," then press the Source/Enter button.

4. If you reset all the maintenance items shown on the display "A23 (for example)", select "All Due Items" by pressing the Audio Remote/Multi-Information Display Switch and press the Source/Enter button. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s) ) you wish to reset by pressing the Audio Remote/Multi-Information Display Switch and press the Source/Enter button.

Courtesy of HONDA, U.S.A., INC.

5. The maintenance item code(s) will disappear, and the engine oil life will reset to "100%."

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8936: Resetting Individual Maintenance Items by HDS

- Title: Resetting Individual Maintenance Items by HDS
- Source path: `pages\11489.html`
- Chunk ID: `chunk_09b427781d2a`
- Images: none
- Duplicate sources: `pages\11494.html`, `pages\14151.html`, `pages\14156.html`

### Full Text

````text
# Resetting Individual Maintenance Items by HDS

1. Connect the Honda Diagnostic System (HDS) to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. Make sure the HDS communicates with the vehicle and the powertrain control module (PCM). If it doesn't communicate, troubleshoot the DLC circuit

4. Select GAUGES in the BODY ELECTRICAL with the HDS.

5. Select ADJUSTMENT in the GAUGES with the HDS.

6. Select MAINTENANCE INFORMATION in the ADJUSTMENT with the HDS.

7. Select MAINTENANCE MINDER in the MAINTENANCE INFORMATION with the HDS.

8. Select the individual maintenance item you wish to reset with the HDS.
````

## Chunk 8937: Maintenance Minder™ General Information (USA/Canada models without Multi-Information Display): Notes

- Title: Maintenance Minder™ General Information (USA/Canada models without Multi-Information Display): Notes
- Source path: `pages\11490.html`
- Chunk ID: `chunk_40acca25bc96`
- Images: none
- Duplicate sources: `pages\14152.html`

### Full Text

````text
# Maintenance Minder™ General Information (USA/Canada models without Multi-Information Display): Notes

Maintenance Minder™ General Information
````

## Chunk 8938: Maintenance Minder

- Title: Maintenance Minder
- Source path: `pages\11491.html`
- Chunk ID: `chunk_7bb9837b2eee`
- Images: `images\GHH409891.jpeg`
- Duplicate sources: `pages\14153.html`

### Full Text

````text
# Maintenance Minder

The Maintenance Minder is an important feature of the information display. Based on engine and transmission operating conditions, and accumulated engine revolutions, the Civic's onboard computer (PCM) calculates the remaining engine oil and the transmission fluid life. The system also displays the remaining engine oil life along with the code(s) for other scheduled maintenance items needing service.

Gauges:

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8939: Service Information

- Title: Service Information
- Source path: `pages\11492.html`
- Chunk ID: `chunk_b3ee4ad32107`
- Images: `images\GHH409892.jpeg`, `images\GHH409893.jpeg`, `images\GHH409894.jpeg`, `images\GHH409895.jpeg`
- Duplicate sources: `pages\14154.html`

### Full Text

````text
# Service Information

1. The remaining engine oil life (A) is shown as a percentage on the information display. To see the current engine oil life, turn the vehicle to the ON mode, then push and release the SEL/RESET knob repeatedly until the engine oil life appears on the information display.

Courtesy of HONDA, U.S.A., INC.

2. When the vehicle is in the ON mode, and the remaining engine oil life is 15% or less, the remaining engine oil life (A) and other scheduled maintenance item(s) needing service are displayed. The maintenance minder indicator (B) also comes on. To cancel the display and the indicator, press the SEL/RESET knob.

- Complete list of maintenance main items (C) .

- Complete list of maintenance sub items (D) .

Courtesy of HONDA, U.S.A., INC.

3. When the vehicle is in the ON mode, and the remaining engine oil life is 0%, the engine oil life indicator (A) blinks. Pressing the SEL/RESET knob cancels the display, but the Maintenance Minder indicator stays on.

Courtesy of HONDA, U.S.A., INC.

4. If the indicated maintenance is not done, the engine oil life indicator shows a negative distance traveled (A), for example "-10" on the display. If the negative distance traveled is between 0 and -9, the indicator is displayed for only a few seconds when turning the vehicle to the ON mode. The negative distance traveled remains displayed after the vehicle is driven more than 10 miles (for USA models) or 10 km (for Canada models) after 0% oil life is reached, and the display cannot be canceled.

This means the indicated maintenance item(s) should have been done more than 10 miles (or 10 km) ago.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8940: Resetting the Maintenance Minder

- Title: Resetting the Maintenance Minder
- Source path: `pages\11493.html`
- Chunk ID: `chunk_80c61d0902b3`
- Images: `images\GHH409896.jpeg`
- Duplicate sources: `pages\14155.html`

### Full Text

````text
# Resetting the Maintenance Minder

NOTE:

- The vehicle must be stopped to reset the Maintenance Minder.

- If a required service is done and the Maintenance Minder is not reset, or if the Maintenance Minder is reset without doing the service, the system will not show the proper maintenance timing. This can lead to serious mechanical problems because there will be no accurate record of when the required maintenance is needed.

- You can reset all maintenance items by batch, or you can select and reset each maintenance item individually on the display.

- The engine oil life and maintenance item(s) can be independently reset with the HDS.

1. Turn the vehicle to the ON mode.

2. Push the SEL/RESET knob repeatedly until the engine oil life is displayed.

3. Press and hold the SEL/RESET knob for 10 seconds or more. The engine oil life and the maintenance item code(s) will blink to show it is in reset mode.

NOTE: If you are resetting the Maintenance Minder when the engine oil life is more than 15%, make sure any maintenance item(s) requiring service are done before resetting the display.

4. If you reset all the maintenance items shown on the display "A23 (for example)", press and hold the SEL/RESET knob for 5 seconds or more. If you reset each maintenance item individually, select an item (complete list of maintenance main item(s) and sub item(s) ) you wish to reset by rotating the SEL/RESET knob, and press and hold the knob for 5 seconds or more.

5. The maintenance item code(s) will disappear, and the engine oil life returns to "100%."

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 8941: Maintenance Main Items (2/4-door: USA model) (2018 2019 2020 2021)

- Title: Maintenance Main Items (2/4-door: USA model) (2018 2019 2020 2021)
- Source path: `pages\11495.html`
- Chunk ID: `chunk_95c17e2430a8`
- Images: `images\GHH409897.png`
- Duplicate sources: `pages\14157.html`

### Full Text

````text
# Maintenance Main Items (2/4-door: USA model) (2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Symbol | Maintenance Main Items

A | Replace engine oil

Engine oil capacity without oil filter 1.5L engine models: 3.2 L (3.4 US qt) 2.0L engine models: 4.0 L (4.2 US qt)

- Engine oil capacity without oil filter

- 1.5L engine models: 3.2 L (3.4 US qt) 2.0L engine models: 4.0 L (4.2 US qt)

- 1.5L engine models: 3.2 L (3.4 US qt)

- 2.0L engine models: 4.0 L (4.2 US qt)

B | Replace engine oil and oil filter

Engine oil capacity with oil filter 1.5L engine models: 3.5 L (3.7 US qt) 2.0L engine models: 4.2 L (4.4 US qt)

- Engine oil capacity with oil filter

- 1.5L engine models: 3.5 L (3.7 US qt) 2.0L engine models: 4.2 L (4.4 US qt)

- 1.5L engine models: 3.5 L (3.7 US qt)

- 2.0L engine models: 4.2 L (4.4 US qt)

Inspect front and rear brakes

Check pads and discs for wear (thickness), damage, and cracks. Check calipers for damage, leaks, and tightness of mounting bolts.

- Check pads and discs for wear (thickness), damage, and cracks.

- Check calipers for damage, leaks, and tightness of mounting bolts.

Check expiration date for temporary tire repair kit bottle (if equipped)

Inspect tie-rod ends, steering gearbox, and gearbox boots

Check steering linkage. Check boots for damage and leaking grease.

- Check steering linkage.

- Check boots for damage and leaking grease.

Inspect suspension components

Check bolts for tightness. Check condition of ball joint boots for deterioration and damage.

- Check bolts for tightness.

- Check condition of ball joint boots for deterioration and damage.

Inspect driveshaft boots

Check boots for cracks and boot bands for tightness.

- Check boots for cracks and boot bands for tightness.

Inspect brake hoses and lines including VSA lines

Check master cylinder and VSA modulator-control unit for damage and leakage.

- Check master cylinder and VSA modulator-control unit for damage and leakage.

Inspect all fluid levels and condition of fluids

Engine coolant M/T fluid CVT fluid Clutch fluid Brake fluid Windshield washer fluid

- Engine coolant

- M/T fluid

- CVT fluid

- Clutch fluid

- Brake fluid

- Windshield washer fluid

Inspect exhaust system

Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

- Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

Inspect fuel lines and connections

Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

- Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

NOTE: According to state and federal regulations, failure to do the maintenance items marked with an asterisk ( ) will not void the customer's emissions warranties. However, Honda recommends that all maintenance services be done at the recommended interval, to ensure long-term reliability.
````

## Chunk 8942: Maintenance Main Items (5-door: USA model) (2018 2019 2020 2021)

- Title: Maintenance Main Items (5-door: USA model) (2018 2019 2020 2021)
- Source path: `pages\11496.html`
- Chunk ID: `chunk_c6a2505a2b50`
- Images: `images\GHH409898.png`
- Duplicate sources: `pages\14158.html`

### Full Text

````text
# Maintenance Main Items (5-door: USA model) (2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Symbol | Maintenance Main Items

A | Replace engine oil

Engine oil capacity without oil filter: 3.2 L (3.4 US qt)

- Engine oil capacity without oil filter: 3.2 L (3.4 US qt)

B | Replace engine oil and oil filter

Engine oil capacity with oil filter: 3.5 L (3.7 US qt)

- Engine oil capacity with oil filter: 3.5 L (3.7 US qt)

Inspect front and rear brakes

Check pads and discs for wear (thickness), damage, and cracks. Check calipers for damage, leaks, and tightness of mounting bolts.

- Check pads and discs for wear (thickness), damage, and cracks.

- Check calipers for damage, leaks, and tightness of mounting bolts.

Inspect tie-rod ends, steering gearbox, and gearbox boots

Check steering linkage. Check boots for damage and leaking grease.

- Check steering linkage.

- Check boots for damage and leaking grease.

Inspect suspension components

Check bolts for tightness. Check condition of ball joint boots for deterioration and damage.

- Check bolts for tightness.

- Check condition of ball joint boots for deterioration and damage.

Inspect driveshaft boots

Check boots for cracks and boot bands for tightness.

- Check boots for cracks and boot bands for tightness.

Inspect brake hoses and lines including VSA lines

Check master cylinder and VSA modulator-control unit for damage and leakage.

- Check master cylinder and VSA modulator-control unit for damage and leakage.

Inspect all fluid levels and condition of fluids

Engine coolant M/T fluid CVT fluid Clutch fluid Brake fluid Windshield washer fluid

- Engine coolant

- M/T fluid

- CVT fluid

- Clutch fluid

- Brake fluid

- Windshield washer fluid

Inspect exhaust system

Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

- Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

Inspect fuel lines and connections

Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

- Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

NOTE: According to state and federal regulations, failure to do the maintenance items marked with an asterisk ( ) will not void the customer's emissions warranties. However, Honda recommends that all maintenance services be done at the recommended interval, to ensure long-term reliability.
````

## Chunk 8943: Maintenance Main Items (5-door: USA model) (2017)

- Title: Maintenance Main Items (5-door: USA model) (2017)
- Source path: `pages\11497.html`
- Chunk ID: `chunk_caefdcebe951`
- Images: `images\GHH409899.png`
- Duplicate sources: `pages\14159.html`

### Full Text

````text
# Maintenance Main Items (5-door: USA model) (2017)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE: Inspect idle speed every 160000 miles (256000 km). Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

- Inspect idle speed every 160000 miles (256000 km).

- Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Symbol | Maintenance Main Items

A | Replace engine oil

Engine oil capacity without oil filter: 3.2 L (3.4 US qt)

- Engine oil capacity without oil filter: 3.2 L (3.4 US qt)

B | Replace engine oil and oil filter

Engine oil capacity with oil filter: 3.5 L (3.7 US qt)

- Engine oil capacity with oil filter: 3.5 L (3.7 US qt)

Inspect front and rear brakes

Check pads and discs for wear (thickness), damage, and cracks. Check calipers for damage, leaks, and tightness of mounting bolts.

- Check pads and discs for wear (thickness), damage, and cracks.

- Check calipers for damage, leaks, and tightness of mounting bolts.

Inspect tie-rod ends, steering gearbox, and gearbox boots

Check steering linkage. Check boots for damage and leaking grease.

- Check steering linkage.

- Check boots for damage and leaking grease.

Inspect suspension components

Check bolts for tightness. Check condition of ball joint boots for deterioration and damage.

- Check bolts for tightness.

- Check condition of ball joint boots for deterioration and damage.

Inspect driveshaft boots

Check boots for cracks and boot bands for tightness.

- Check boots for cracks and boot bands for tightness.

Inspect brake hoses and lines including VSA lines

Check master cylinder and VSA modulator-control unit for damage and leakage.

- Check master cylinder and VSA modulator-control unit for damage and leakage.

Inspect all fluid levels and condition of fluids

Engine coolant M/T fluid CVT fluid Clutch fluid Brake fluid Windshield washer fluid

- Engine coolant

- M/T fluid

- CVT fluid

- Clutch fluid

- Brake fluid

- Windshield washer fluid

Inspect exhaust system

Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

- Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

Inspect fuel lines and connections

Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

- Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

NOTE: According to state and federal regulations, failure to do the maintenance items marked with an asterisk ( ) will not void the customer's emissions warranties. However, Honda recommends that all maintenance services be done at the recommended interval, to ensure long-term reliability.
````

## Chunk 8944: Maintenance Main Items (USA models Type-R) (2017 2018 2019 2020 2021)

- Title: Maintenance Main Items (USA models Type-R) (2017 2018 2019 2020 2021)
- Source path: `pages\11498.html`
- Chunk ID: `chunk_c934372b38cb`
- Images: `images\GHH409900.png`
- Duplicate sources: `pages\14160.html`

### Full Text

````text
# Maintenance Main Items (USA models Type-R) (2017 2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Symbol | Maintenance Main Items

A | Replace engine oil

Engine oil capacity without oil filter: 5.0 L (5.3 US qt)

- Engine oil capacity without oil filter: 5.0 L (5.3 US qt)

B | Replace engine oil and oil filter

Engine oil capacity with oil filter: 5.4 L (5.7 US qt)

- Engine oil capacity with oil filter: 5.4 L (5.7 US qt)

Inspect front and rear brakes

Check pads and discs for wear (thickness), damage, and cracks. Check calipers for damage, leaks, and tightness of mounting bolts.

- Check pads and discs for wear (thickness), damage, and cracks.

- Check calipers for damage, leaks, and tightness of mounting bolts.

Check expiry date for tire repair kit bottle (if equipped)

Inspect tie-rod ends, steering gearbox, and gearbox boots

Check steering linkage. Check boots for damage and leaking grease.

- Check steering linkage.

- Check boots for damage and leaking grease.

Inspect suspension components

Check bolts for tightness. Check condition of ball joint boots for deterioration and damage.

- Check bolts for tightness.

- Check condition of ball joint boots for deterioration and damage.

Inspect driveshaft boots

Check boots for cracks and boot bands for tightness.

- Check boots for cracks and boot bands for tightness.

Inspect brake hoses and lines including VSA lines

Check master cylinder and VSA modulator-control unit for damage and leakage.

- Check master cylinder and VSA modulator-control unit for damage and leakage.

Inspect all fluid levels and condition of fluids

Engine coolant M/T fluid Clutch fluid Brake fluid Windshield washer fluid

- Engine coolant

- M/T fluid

- Clutch fluid

- Brake fluid

- Windshield washer fluid

Inspect exhaust system

Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

- Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

Inspect fuel lines and connections

Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

- Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

NOTE: According to state and federal regulations, failure to do the maintenance items marked with an asterisk ( ) will not void the customer's emissions warranties. However, Honda recommends that all maintenance services be done at the recommended interval, to ensure long-term reliability.
````

## Chunk 8945: Maintenance Main Items (USA/Canada models) (2016 2017)

- Title: Maintenance Main Items (USA/Canada models) (2016 2017)
- Source path: `pages\11499.html`
- Chunk ID: `chunk_5d13ea096bf0`
- Images: `images\GHH409901.png`
- Duplicate sources: `pages\14161.html`

### Full Text

````text
# Maintenance Main Items (USA/Canada models) (2016 2017)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE:

Inspect idle speed every 160000 miles (256000 km). Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

- Inspect idle speed every 160000 miles (256000 km).

- Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Symbol | Maintenance Main Items

A | Replace engine oil

Engine oil capacity without oil filter 1.5L engine models: 3.2 L (3.4 US qt) 2.0L engine models: 4.0 L (4.2 US qt)

- Engine oil capacity without oil filter

- 1.5L engine models: 3.2 L (3.4 US qt) 2.0L engine models: 4.0 L (4.2 US qt)

- 1.5L engine models: 3.2 L (3.4 US qt)

- 2.0L engine models: 4.0 L (4.2 US qt)

B | Replace engine oil and oil filter

Engine oil capacity with oil filter 1.5L engine models: 3.5 L (3.7 US qt) 2.0L engine models: 4.2 L (4.4 US qt)

- Engine oil capacity with oil filter

- 1.5L engine models: 3.5 L (3.7 US qt) 2.0L engine models: 4.2 L (4.4 US qt)

- 1.5L engine models: 3.5 L (3.7 US qt)

- 2.0L engine models: 4.2 L (4.4 US qt)

Inspect front and rear brakes

Check pads and discs for wear (thickness), damage, and cracks. Check calipers for damage, leaks, and tightness of mounting bolts.

- Check pads and discs for wear (thickness), damage, and cracks.

- Check calipers for damage, leaks, and tightness of mounting bolts.

Inspect tie-rod ends, steering gearbox, and gearbox boots

Check steering linkage. Check boots for damage and leaking grease.

- Check steering linkage.

- Check boots for damage and leaking grease.

Inspect suspension components

Check bolts for tightness. Check condition of ball joint boots for deterioration and damage.

- Check bolts for tightness.

- Check condition of ball joint boots for deterioration and damage.

Inspect driveshaft boots

Check boots for cracks and boot bands for tightness.

- Check boots for cracks and boot bands for tightness.

Inspect brake hoses and lines including VSA lines

Check master cylinder and VSA modulator-control unit for damage and leakage.

- Check master cylinder and VSA modulator-control unit for damage and leakage.

Inspect all fluid levels and condition of fluids

Engine coolant M/T fluid CVT fluid Clutch fluid Brake fluid Windshield washer fluid

- Engine coolant

- M/T fluid

- CVT fluid

- Clutch fluid

- Brake fluid

- Windshield washer fluid

Inspect exhaust system

Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

- Check catalytic converter heat shields, exhaust pipes, and muffler for damage, leaks, and tightness.

Inspect fuel lines and connections

Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

- Check for loose connections, cracks, and deterioration; retighten loose connections and replace damaged parts.

NOTE: According to state and federal regulations, failure to do the maintenance items marked with an asterisk ( ) will not void the customer's emissions warranties. However, Honda recommends that all maintenance services be done at the recommended interval, to ensure long-term reliability.
````

## Chunk 8946: Maintenance Sub Items (2/4-door: USA model) (2016 2017)

- Title: Maintenance Sub Items (2/4-door: USA model) (2016 2017)
- Source path: `pages\11500.html`
- Chunk ID: `chunk_e55d90bd4c93`
- Images: none
- Duplicate sources: `pages\14162.html`

### Full Text

````text
# Maintenance Sub Items (2/4-door: USA model) (2016 2017)

If a Maintenance Minder indicator does not appear more than 36 months after the item 7 is reset, change the brake fluid every 3 years.

NOTE:

Inspect idle speed every 160000 miles (256000 km). Adjust the valves during services A, B, 0, 1, 2, 3, or 9 if they are noisy.

- Inspect idle speed every 160000 miles (256000 km).

- Adjust the valves during services A, B, 0, 1, 2, 3, or 9 if they are noisy.

Number | Maintenance Sub Items

1 | Rotate tires, and check tire inflation and condition

Follow the pattern shown in the Owner's Manual.

- Follow the pattern shown in the Owner's Manual.

2 | Replace air cleaner element

If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

- If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

Replace dust and pollen filter

Replace filter whenever airflow from the heating and air conditioning system is less than normal. If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

- Replace filter whenever airflow from the heating and air conditioning system is less than normal.

- If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

Inspect drive belt

Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

- Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

3 | Replace M/T fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda MTF. Capacity: 1.9 L (2.0 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda MTF.

- Capacity: 1.9 L (2.0 US qt)

Replace CVT fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda HCF-2. NOTE: Using the wrong type of fluid will damage the transmission. Capacity 1.5L engine models: 3.7 L (3.9 US qt) 2.0L engine models: 3.5 L (3.7 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda HCF-2.

NOTE: Using the wrong type of fluid will damage the transmission.

- Capacity

- 1.5L engine models: 3.7 L (3.9 US qt) 2.0L engine models: 3.5 L (3.7 US qt)

- 1.5L engine models: 3.7 L (3.9 US qt)

- 2.0L engine models: 3.5 L (3.7 US qt)

4 | Replace spark plugs

Inspect valve clearance (cold)

Intake: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) 1.5L engine models: 5.1 L (1.35 US gal) 2.0L engine models: 5.3 L (1.40 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- 1.5L engine models: 5.1 L (1.35 US gal) 2.0L engine models: 5.3 L (1.40 US gal)
````

## Chunk 8947: Maintenance Sub Items (2/4-door: USA model) (2016 2017)

- Title: Maintenance Sub Items (2/4-door: USA model) (2016 2017)
- Source path: `pages\11500.html`
- Chunk ID: `chunk_a0e490080feb`
- Images: none
- Duplicate sources: `pages\14162.html`

### Full Text

````text
ke: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) 1.5L engine models: 5.1 L (1.35 US gal) 2.0L engine models: 5.3 L (1.40 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- 1.5L engine models: 5.1 L (1.35 US gal) 2.0L engine models: 5.3 L (1.40 US gal)

- 1.5L engine models: 5.1 L (1.35 US gal)

- 2.0L engine models: 5.3 L (1.40 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.

- Use Honda DOT 3 Brake Fluid.

We recommend genuine Honda Brake Fluid.

- Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8948: Maintenance Sub Items (2/4-door: USA model) (2018 2019 2020 2021)

- Title: Maintenance Sub Items (2/4-door: USA model) (2018 2019 2020 2021)
- Source path: `pages\11501.html`
- Chunk ID: `chunk_474e03dfae27`
- Images: none
- Duplicate sources: `pages\14163.html`

### Full Text

````text
# Maintenance Sub Items (2/4-door: USA model) (2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 36 months after the item 7 is reset, change the brake fluid every 3 years.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Number | Maintenance Sub Items

1 | Rotate tires, and check tire inflation and condition

Follow the pattern shown in the Owner's Manual.

- Follow the pattern shown in the Owner's Manual.

2 | Replace air cleaner element

If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

- If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

Replace dust and pollen filter

Replace filter whenever airflow from the heating and air conditioning system is less than normal. If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

- Replace filter whenever airflow from the heating and air conditioning system is less than normal.

- If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

Inspect drive belt

Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

- Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

3 | Replace M/T fluid

Use Honda MTF. Capacity: 1.9 L (2.0 US qt)

- Use Honda MTF.

- Capacity: 1.9 L (2.0 US qt)

Replace CVT fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda HCF-2. NOTE: Using the wrong type of fluid will damage the transmission. Capacity 1.5L engine models: 3.7 L (3.9 US qt) - 2.0L engine models: 3.5 L (3.7 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda HCF-2.

NOTE: Using the wrong type of fluid will damage the transmission.

- Capacity

- 1.5L engine models: 3.7 L (3.9 US qt) - 2.0L engine models: 3.5 L (3.7 US qt)

- 1.5L engine models: 3.7 L (3.9 US qt) -

- 2.0L engine models: 3.5 L (3.7 US qt)

4 | Replace spark plugs

Inspect valve clearance (cold)

Intake: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) L15B7 engine model: 5.1 L (1.35 US gal) L15BY engine model: 5.0 L (1.32 US gal) K20C2 engine model: 5.3 L (1.40 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- L15B7 engine model: 5.1 L (1.35 US gal) L15BY engine model: 5.0 L (1.32 US gal) K20C2 engine model: 5.3 L (1.40 US gal)

- L15B7 engine model: 5.1 L (1.35 US gal)

- L15BY engine model: 5.0 L (1.32 US gal)

- K20C2 engine model: 5.3 L (1.40 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.

- Use Honda DOT 3 Brake Fluid.

We recommend genuine Honda Brake Fluid.

- Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8949: Maintenance Sub Items (5-door: USA model) (2017)

- Title: Maintenance Sub Items (5-door: USA model) (2017)
- Source path: `pages\11502.html`
- Chunk ID: `chunk_4dcc6d4ae0e1`
- Images: none
- Duplicate sources: `pages\14164.html`

### Full Text

````text
# Maintenance Sub Items (5-door: USA model) (2017)

If a Maintenance Minder indicator does not appear more than 12 months after the display is reset, change the engine oil every year.

NOTE: Inspect idle speed every 160000 miles (256000 km). Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

- Inspect idle speed every 160000 miles (256000 km).

- Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Number | Maintenance Sub Items

1 | Rotate tires, and check tire inflation and condition

Follow the pattern shown in the Owner's Manual.

- Follow the pattern shown in the Owner's Manual.

2 | Replace air cleaner element

If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

- If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

Replace dust and pollen filter

Replace filter whenever airflow from the heating and air conditioning system is less than normal. If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

- Replace filter whenever airflow from the heating and air conditioning system is less than normal.

- If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

Inspect drive belt

Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

- Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

3 | Replace M/T fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda MTF. Capacity: 1.9 L (2.0 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda MTF.

- Capacity: 1.9 L (2.0 US qt)

Replace CVT fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda HCF-2. NOTE: Using the wrong type of fluid will damage the transmission. Capacity: 3.7 L (3.9 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda HCF-2.

NOTE: Using the wrong type of fluid will damage the transmission.

- Capacity: 3.7 L (3.9 US qt)

4 | Replace spark plugs

Inspect valve clearance (cold)

Intake: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- M/T model: 4.9 L (1.29 US gal)

- CVT model: 5.0 L (1.32 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8950: Maintenance Sub Items (5-door: USA model) (2017)

- Title: Maintenance Sub Items (5-door: USA model) (2017)
- Source path: `pages\11502.html`
- Chunk ID: `chunk_0b58a69ef44f`
- Images: none
- Duplicate sources: `pages\14164.html`

### Full Text

````text
reeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- M/T model: 4.9 L (1.29 US gal)

- CVT model: 5.0 L (1.32 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.

- Use Honda DOT 3 Brake Fluid.

We recommend genuine Honda Brake Fluid.

- Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8951: Maintenance Sub Items (5-door: USA model) (2018 2019 2020 2021)

- Title: Maintenance Sub Items (5-door: USA model) (2018 2019 2020 2021)
- Source path: `pages\11503.html`
- Chunk ID: `chunk_43456793951c`
- Images: none
- Duplicate sources: `pages\14165.html`

### Full Text

````text
# Maintenance Sub Items (5-door: USA model) (2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 36 months after the item 7 is reset, change the brake fluid every 3 years.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Number | Maintenance Sub Items

1 | Rotate tires, and check tire inflation and condition

Follow the pattern shown in the Owner's Manual.

- Follow the pattern shown in the Owner's Manual.

2 | Replace air cleaner element

If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

- If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

Replace dust and pollen filter

Replace filter whenever airflow from the heating and air conditioning system is less than normal. If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

- Replace filter whenever airflow from the heating and air conditioning system is less than normal.

- If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

Inspect drive belt

Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

- Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

3 | Replace M/T fluid

Use Honda MTF. Capacity: 1.9 L (2.0 US qt)

- Use Honda MTF.

- Capacity: 1.9 L (2.0 US qt)

Replace CVT fluid

Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km). Use Honda HCF-2. NOTE: Using the wrong type of fluid will damage the transmission. Capacity: 3.7 L (3.9 US qt)

- Driving in mountainous areas at very low vehicle speeds or trailer towing results in higher transmission temperatures. This requires transmission fluid changes more frequently than recommended by the Maintenance Minder. If the vehicle is regularly driven under these conditions, have the transmission fluid changed every 25000 miles (40000 km).

- Use Honda HCF-2.

NOTE: Using the wrong type of fluid will damage the transmission.

- Capacity: 3.7 L (3.9 US qt)

4 | Replace spark plugs

Inspect valve clearance (cold)

Intake: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir) M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir)

- M/T model: 4.9 L (1.29 US gal) CVT model: 5.0 L (1.32 US gal)

- M/T model: 4.9 L (1.29 US gal)

- CVT model: 5.0 L (1.32 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.

- Use Honda DOT 3 Brake Fluid.

We recommend genuine Honda Brake Fluid.

- Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8952: Maintenance Sub Items (USA models Type-R) (2017 2018 2019 2020 2021)

- Title: Maintenance Sub Items (USA models Type-R) (2017 2018 2019 2020 2021)
- Source path: `pages\11504.html`
- Chunk ID: `chunk_7567ca40bab8`
- Images: none
- Duplicate sources: `pages\14166.html`

### Full Text

````text
# Maintenance Sub Items (USA models Type-R) (2017 2018 2019 2020 2021)

If a Maintenance Minder indicator does not appear more than 36 months after the item 7 is reset, change the brake fluid every 3 years.

NOTE: Adjust the valves during services A, B, 1, 2, or 3 if they are noisy.

Number | Maintenance Sub Items

1 | Rotate tires, and check tire inflation and condition

Follow the pattern shown in the Owner's Manual.

- Follow the pattern shown in the Owner's Manual.

2 | Replace air cleaner element

If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

- If the vehicle is driven primarily in dusty conditions, replace every 15000 miles (24000 km).

Replace dust and pollen filter

Replace filter whenever airflow from the heating and air conditioning system is less than normal. If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

- Replace filter whenever airflow from the heating and air conditioning system is less than normal.

- If the vehicle is driven mostly in urban areas that have high concentrations of soot in the air from industry and from diesel-powered vehicles, replace every 15000 miles (24000 km).

Inspect drive belt

Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

- Look for cracks and damage, then check the position of drive belt auto-tensioner indicator.

3 | Replace M/T fluid

Use Honda MTF. Capacity: 2.2 L (2.3 US qt)

- Use Honda MTF.

- Capacity: 2.2 L (2.3 US qt)

4 | Replace spark plugs

Inspect valve clearance (cold)

Intake: 0.21-0.25 mm (0.009 in) Exhaust: 0.25-0.29 mm (0.010-0.011 in)

- Intake: 0.21-0.25 mm (0.009 in)

- Exhaust: 0.25-0.29 mm (0.010-0.011 in)

5 | Replace engine coolant

Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C). Capacity (including reservoir): 4.7 L (1.24 US gal)

- Use Honda Long Life Antifreeze/Coolant Type 2, and if necessary add Honda Extreme Cold Weather Antifreeze/Coolant Type 2 (concentrate) as needed for prolonged cold temperatures below -22°F (-30°C).

- Capacity (including reservoir): 4.7 L (1.24 US gal)

7 | Replace brake fluid

Use Honda DOT 3 Brake Fluid. We recommend genuine Honda Brake Fluid. Check brake fluid level is between upper and lower marks on reservoir.

- Use Honda DOT 3 Brake Fluid.

We recommend genuine Honda Brake Fluid.

- Check brake fluid level is between upper and lower marks on reservoir.
````

## Chunk 8953: DTC SRS related DTCs (With CAN gateway): Notes

- Title: DTC SRS related DTCs (With CAN gateway): Notes
- Source path: `pages\11571.html`
- Chunk ID: `chunk_dd6532e82760`
- Images: none
- Duplicate sources: `pages\19750.html`

### Full Text

````text
# DTC SRS related DTCs (With CAN gateway): Notes

NOTE

- Always check "How to troubleshoot the SRS system" and proceed along each "DTC Troubleshooting" procedure.

- Make sure the 12 volt battery is fully charged. If not, the results of tests may not be accurate.

- The SRS indicator will turn on when the 12 volt battery voltage becomes below 10 volts.

- The possible causes shown may not be a complete list of all potential problems, and it is possible that there may be other causes.
````

## Chunk 8954: DTC B0001-11: Short to Ground in the Driver's Airbag First Inflator

- Title: DTC B0001-11: Short to Ground in the Driver's Airbag First Inflator
- Source path: `pages\11572.html`
- Chunk ID: `chunk_83ac8869f7a8`
- Images: none
- Duplicate sources: `pages\19751.html`

### Full Text

````text
# DTC B0001-11: Short to Ground in the Driver's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines) Driver's airbag internal failure (Driver's airbag first inflator) SRS unit internal failure

- Short to ground between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines)

- Driver's airbag internal failure (Driver's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8955: DTC B0001-12: Short to Power in the Driver's Airbag First Inflator

- Title: DTC B0001-12: Short to Power in the Driver's Airbag First Inflator
- Source path: `pages\11573.html`
- Chunk ID: `chunk_f6b3e4954f39`
- Images: none
- Duplicate sources: `pages\19752.html`

### Full Text

````text
# DTC B0001-12: Short to Power in the Driver's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines) Driver's airbag internal failure (Driver's airbag first inflator) SRS unit internal failure

- Short to power between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines)

- Driver's airbag internal failure (Driver's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8956: DTC B0001-13: Open or Increased Resistance in the Driver's Airbag First Inflator

- Title: DTC B0001-13: Open or Increased Resistance in the Driver's Airbag First Inflator
- Source path: `pages\11574.html`
- Chunk ID: `chunk_ab6ceefa97d2`
- Images: none
- Duplicate sources: `pages\19753.html`

### Full Text

````text
# DTC B0001-13: Open or Increased Resistance in the Driver's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines) Driver's airbag internal failure (Driver's airbag first inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines)

- Driver's airbag internal failure (Driver's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8957: DTC B0001-1A: Decreased Resistance in the Driver's Airbag First Inflator

- Title: DTC B0001-1A: Decreased Resistance in the Driver's Airbag First Inflator
- Source path: `pages\11575.html`
- Chunk ID: `chunk_426f12c71122`
- Images: none
- Duplicate sources: `pages\19754.html`

### Full Text

````text
# DTC B0001-1A: Decreased Resistance in the Driver's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines) Driver's airbag internal failure (Driver's airbag first inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the driver's airbag first inflator (LA1+, LA1- lines)

- Driver's airbag internal failure (Driver's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8958: DTC B0002-11: Short to Ground in the Driver's Airbag Second Inflator

- Title: DTC B0002-11: Short to Ground in the Driver's Airbag Second Inflator
- Source path: `pages\11576.html`
- Chunk ID: `chunk_b4fbe0b51fd2`
- Images: none
- Duplicate sources: `pages\19755.html`

### Full Text

````text
# DTC B0002-11: Short to Ground in the Driver's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines) Driver's airbag internal failure (Driver's airbag second inflator) SRS unit internal failure

- Short to ground between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines)

- Driver's airbag internal failure (Driver's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8959: DTC B0002-12: Short to Power in the Driver's Airbag Second Inflator

- Title: DTC B0002-12: Short to Power in the Driver's Airbag Second Inflator
- Source path: `pages\11577.html`
- Chunk ID: `chunk_b259c7eb1d4b`
- Images: none
- Duplicate sources: `pages\19756.html`

### Full Text

````text
# DTC B0002-12: Short to Power in the Driver's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines) Driver's airbag internal failure (Driver's airbag second inflator) SRS unit internal failure

- Short to power between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines)

- Driver's airbag internal failure (Driver's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8960: DTC B0002-13: Open or Increased Resistance in the Driver's Airbag Second Inflator

- Title: DTC B0002-13: Open or Increased Resistance in the Driver's Airbag Second Inflator
- Source path: `pages\11578.html`
- Chunk ID: `chunk_512291f55e4b`
- Images: none
- Duplicate sources: `pages\19757.html`

### Full Text

````text
# DTC B0002-13: Open or Increased Resistance in the Driver's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines) Driver's airbag internal failure (Driver's airbag second inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines)

- Driver's airbag internal failure (Driver's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8961: DTC B0002-1A: Decreased Resistance in the Driver's Airbag Second Inflator

- Title: DTC B0002-1A: Decreased Resistance in the Driver's Airbag Second Inflator
- Source path: `pages\11579.html`
- Chunk ID: `chunk_c75e1ec236d4`
- Images: none
- Duplicate sources: `pages\19758.html`

### Full Text

````text
# DTC B0002-1A: Decreased Resistance in the Driver's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines) Driver's airbag internal failure (Driver's airbag second inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the driver's airbag second inflator (LA2+, LA2- lines)

- Driver's airbag internal failure (Driver's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8962: DTC B0010-11: Short to Ground in the Front Passenger's Airbag First Inflator

- Title: DTC B0010-11: Short to Ground in the Front Passenger's Airbag First Inflator
- Source path: `pages\11580.html`
- Chunk ID: `chunk_60d1310c3d7e`
- Images: none
- Duplicate sources: `pages\19759.html`

### Full Text

````text
# DTC B0010-11: Short to Ground in the Front Passenger's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines) Front passenger's airbag internal failure (Front passenger's airbag first inflator) SRS unit internal failure

- Short to ground between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines)

- Front passenger's airbag internal failure (Front passenger's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8963: DTC B0010-12: Short to Power in the Front Passenger's Airbag First Inflator

- Title: DTC B0010-12: Short to Power in the Front Passenger's Airbag First Inflator
- Source path: `pages\11581.html`
- Chunk ID: `chunk_5cf5466f38dc`
- Images: none
- Duplicate sources: `pages\19760.html`

### Full Text

````text
# DTC B0010-12: Short to Power in the Front Passenger's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines) SRS unit internal failure

- Short to power between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines)

- SRS unit internal failure
````

## Chunk 8964: DTC B0010-13: Open or Increased Resistance in the Front Passenger's Airbag First Inflator

- Title: DTC B0010-13: Open or Increased Resistance in the Front Passenger's Airbag First Inflator
- Source path: `pages\11582.html`
- Chunk ID: `chunk_81b5b40a43c1`
- Images: none
- Duplicate sources: `pages\19761.html`

### Full Text

````text
# DTC B0010-13: Open or Increased Resistance in the Front Passenger's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines) Front passenger's airbag internal failure (Front passenger's airbag first inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines)

- Front passenger's airbag internal failure (Front passenger's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8965: DTC B0010-1A: Decreased Resistance in the Front Passenger's Airbag First Inflator

- Title: DTC B0010-1A: Decreased Resistance in the Front Passenger's Airbag First Inflator
- Source path: `pages\11583.html`
- Chunk ID: `chunk_def8edaa0ef0`
- Images: none
- Duplicate sources: `pages\19762.html`

### Full Text

````text
# DTC B0010-1A: Decreased Resistance in the Front Passenger's Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines) Front passenger's airbag internal failure (Front passenger's airbag first inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the front passenger's airbag first inflator (RA1+, RA1- lines)

- Front passenger's airbag internal failure (Front passenger's airbag first inflator)

- SRS unit internal failure
````

## Chunk 8966: DTC B0011-11: Short to Ground in the Front Passenger's Airbag Second Inflator

- Title: DTC B0011-11: Short to Ground in the Front Passenger's Airbag Second Inflator
- Source path: `pages\11584.html`
- Chunk ID: `chunk_ddb9c04e9ae7`
- Images: none
- Duplicate sources: `pages\19763.html`

### Full Text

````text
# DTC B0011-11: Short to Ground in the Front Passenger's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines) Front passenger's airbag internal failure (Front passenger's airbag second inflator) SRS unit internal failure

- Short to ground between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines)

- Front passenger's airbag internal failure (Front passenger's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8967: DTC B0011-12: Short to Power in the Front Passenger's Airbag Second Inflator

- Title: DTC B0011-12: Short to Power in the Front Passenger's Airbag Second Inflator
- Source path: `pages\11585.html`
- Chunk ID: `chunk_264f46e2e1b0`
- Images: none
- Duplicate sources: `pages\19764.html`

### Full Text

````text
# DTC B0011-12: Short to Power in the Front Passenger's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines) SRS unit internal failure

- Short to power between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines)

- SRS unit internal failure
````

## Chunk 8968: DTC B0011-13: Open or Increased Resistance in the Front Passenger's Airbag Second Inflator

- Title: DTC B0011-13: Open or Increased Resistance in the Front Passenger's Airbag Second Inflator
- Source path: `pages\11586.html`
- Chunk ID: `chunk_8c4f612ae2e5`
- Images: none
- Duplicate sources: `pages\19765.html`

### Full Text

````text
# DTC B0011-13: Open or Increased Resistance in the Front Passenger's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines) Front passenger's airbag internal failure (Front passenger's airbag second inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines)

- Front passenger's airbag internal failure (Front passenger's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8969: DTC B0011-1A: Decreased Resistance in the Front Passenger's Airbag Second Inflator

- Title: DTC B0011-1A: Decreased Resistance in the Front Passenger's Airbag Second Inflator
- Source path: `pages\11587.html`
- Chunk ID: `chunk_c12085b8dcf2`
- Images: none
- Duplicate sources: `pages\19766.html`

### Full Text

````text
# DTC B0011-1A: Decreased Resistance in the Front Passenger's Airbag Second Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines) Front passenger's airbag internal failure (Front passenger's airbag second inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the front passenger's airbag second inflator (RA2+, RA2- lines)

- Front passenger's airbag internal failure (Front passenger's airbag second inflator)

- SRS unit internal failure
````

## Chunk 8970: DTC B0020-11: Short to Ground in the Driver's Side Airbag Inflator

- Title: DTC B0020-11: Short to Ground in the Driver's Side Airbag Inflator
- Source path: `pages\11588.html`
- Chunk ID: `chunk_ddb25f4cba8d`
- Images: none
- Duplicate sources: `pages\19767.html`

### Full Text

````text
# DTC B0020-11: Short to Ground in the Driver's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines) Driver's side airbag internal failure (Driver's side airbag inflator) SRS unit internal failure

- Short to ground between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines)

- Driver's side airbag internal failure (Driver's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8971: DTC B0020-12: Short to Power in the Driver's Side Airbag Inflator

- Title: DTC B0020-12: Short to Power in the Driver's Side Airbag Inflator
- Source path: `pages\11589.html`
- Chunk ID: `chunk_00c01925575a`
- Images: none
- Duplicate sources: `pages\19768.html`

### Full Text

````text
# DTC B0020-12: Short to Power in the Driver's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines) SRS unit internal failure

- Short to power between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines)

- SRS unit internal failure
````

## Chunk 8972: DTC B0020-13: Open or Increased Resistance in the Driver's Side Airbag Inflator

- Title: DTC B0020-13: Open or Increased Resistance in the Driver's Side Airbag Inflator
- Source path: `pages\11590.html`
- Chunk ID: `chunk_4d8b720ccaee`
- Images: none
- Duplicate sources: `pages\19769.html`

### Full Text

````text
# DTC B0020-13: Open or Increased Resistance in the Driver's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines) Driver's side airbag internal failure (Driver's side airbag inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines)

- Driver's side airbag internal failure (Driver's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8973: DTC B0020-1A: Decreased Resistance in the Driver's Side Airbag Inflator

- Title: DTC B0020-1A: Decreased Resistance in the Driver's Side Airbag Inflator
- Source path: `pages\11591.html`
- Chunk ID: `chunk_eae81db58c55`
- Images: none
- Duplicate sources: `pages\19770.html`

### Full Text

````text
# DTC B0020-1A: Decreased Resistance in the Driver's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines) Driver's side airbag internal failure (Driver's side airbag inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the driver's side airbag inflator (LSA+, LSA- lines)

- Driver's side airbag internal failure (Driver's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8974: DTC B0021-11: Short to Ground in the Left Side Curtain Airbag First Inflator

- Title: DTC B0021-11: Short to Ground in the Left Side Curtain Airbag First Inflator
- Source path: `pages\11592.html`
- Chunk ID: `chunk_50f862c60d39`
- Images: none
- Duplicate sources: `pages\19771.html`

### Full Text

````text
# DTC B0021-11: Short to Ground in the Left Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines) Left side curtain airbag internal failure (Left side curtain airbag inflator) SRS unit internal failure

- Short to ground between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines)

- Left side curtain airbag internal failure (Left side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8975: DTC B0021-12: Short to Power in the Left Side Curtain Airbag First Inflator

- Title: DTC B0021-12: Short to Power in the Left Side Curtain Airbag First Inflator
- Source path: `pages\11593.html`
- Chunk ID: `chunk_461152a0a10d`
- Images: none
- Duplicate sources: `pages\19772.html`

### Full Text

````text
# DTC B0021-12: Short to Power in the Left Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines) SRS unit internal failure

- Short to power between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines)

- SRS unit internal failure
````

## Chunk 8976: DTC B0021-13: Open or Increased Resistance in the Left Side Curtain Airbag First Inflator

- Title: DTC B0021-13: Open or Increased Resistance in the Left Side Curtain Airbag First Inflator
- Source path: `pages\11594.html`
- Chunk ID: `chunk_775e6fbfcd7f`
- Images: none
- Duplicate sources: `pages\19773.html`

### Full Text

````text
# DTC B0021-13: Open or Increased Resistance in the Left Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines) Left side curtain airbag internal failure (Left side curtain airbag inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines)

- Left side curtain airbag internal failure (Left side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8977: DTC B0021-1A: Decreased Resistance in the Left Side Curtain Airbag First Inflator

- Title: DTC B0021-1A: Decreased Resistance in the Left Side Curtain Airbag First Inflator
- Source path: `pages\11595.html`
- Chunk ID: `chunk_45f111e52212`
- Images: none
- Duplicate sources: `pages\19774.html`

### Full Text

````text
# DTC B0021-1A: Decreased Resistance in the Left Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines) Left side curtain airbag internal failure (Left side curtain airbag inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the left side curtain airbag inflator (LCA+, LCA- lines)

- Left side curtain airbag internal failure (Left side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8978: DTC B0028-11: Short to Ground in the Front Passenger's Side Airbag Inflator

- Title: DTC B0028-11: Short to Ground in the Front Passenger's Side Airbag Inflator
- Source path: `pages\11596.html`
- Chunk ID: `chunk_50fa5f680b58`
- Images: none
- Duplicate sources: `pages\19775.html`

### Full Text

````text
# DTC B0028-11: Short to Ground in the Front Passenger's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines) Front passenger's side airbag internal failure (Front passenger's side airbag inflator) SRS unit internal failure

- Short to ground between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines)

- Front passenger's side airbag internal failure (Front passenger's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8979: DTC B0028-12: Short to Power in the Front Passenger's Side Airbag Inflator

- Title: DTC B0028-12: Short to Power in the Front Passenger's Side Airbag Inflator
- Source path: `pages\11597.html`
- Chunk ID: `chunk_44e2dd403dcc`
- Images: none
- Duplicate sources: `pages\19776.html`

### Full Text

````text
# DTC B0028-12: Short to Power in the Front Passenger's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines) SRS unit internal failure

- Short to power between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines)

- SRS unit internal failure
````

## Chunk 8980: DTC B0028-13: Open or Increased Resistance in the Front Passenger's Side Airbag Inflator

- Title: DTC B0028-13: Open or Increased Resistance in the Front Passenger's Side Airbag Inflator
- Source path: `pages\11598.html`
- Chunk ID: `chunk_3067a555c2e0`
- Images: none
- Duplicate sources: `pages\19777.html`

### Full Text

````text
# DTC B0028-13: Open or Increased Resistance in the Front Passenger's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines) Front passenger's side airbag internal failure (Front passenger's side airbag inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines)

- Front passenger's side airbag internal failure (Front passenger's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8981: DTC B0028-1A: Decreased Resistance in the Front Passenger's Side Airbag Inflator

- Title: DTC B0028-1A: Decreased Resistance in the Front Passenger's Side Airbag Inflator
- Source path: `pages\11599.html`
- Chunk ID: `chunk_84eeb4282ddd`
- Images: none
- Duplicate sources: `pages\19778.html`

### Full Text

````text
# DTC B0028-1A: Decreased Resistance in the Front Passenger's Side Airbag Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines) Front passenger's side airbag internal failure (Front passenger's side airbag inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the front passenger's side airbag inflator (RSA+, RSA- lines)

- Front passenger's side airbag internal failure (Front passenger's side airbag inflator)

- SRS unit internal failure
````

## Chunk 8982: DTC B0029-11: Short to Ground in the Right Side Curtain Airbag First Inflator

- Title: DTC B0029-11: Short to Ground in the Right Side Curtain Airbag First Inflator
- Source path: `pages\11600.html`
- Chunk ID: `chunk_3e3633b9ac75`
- Images: none
- Duplicate sources: `pages\19779.html`

### Full Text

````text
# DTC B0029-11: Short to Ground in the Right Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines) Right side curtain airbag internal failure (Right side curtain airbag inflator) SRS unit internal failure

- Short to ground between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines)

- Right side curtain airbag internal failure (Right side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8983: DTC B0029-12: Short to Power in the Right Side Curtain Airbag First Inflator

- Title: DTC B0029-12: Short to Power in the Right Side Curtain Airbag First Inflator
- Source path: `pages\11601.html`
- Chunk ID: `chunk_00c9c0d343eb`
- Images: none
- Duplicate sources: `pages\19780.html`

### Full Text

````text
# DTC B0029-12: Short to Power in the Right Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines) SRS unit internal failure

- Short to power between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines)

- SRS unit internal failure
````

## Chunk 8984: DTC B0029-13: Open or Increased Resistance in the Right Side Curtain Airbag First Inflator

- Title: DTC B0029-13: Open or Increased Resistance in the Right Side Curtain Airbag First Inflator
- Source path: `pages\11602.html`
- Chunk ID: `chunk_ab2fc773bdd7`
- Images: none
- Duplicate sources: `pages\19781.html`

### Full Text

````text
# DTC B0029-13: Open or Increased Resistance in the Right Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines) Right side curtain airbag internal failure (Right side curtain airbag inflator) SRS unit internal failure

- Open or Poor connection between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines)

- Right side curtain airbag internal failure (Right side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8985: DTC B0029-1A: Decreased Resistance in the Right Side Curtain Airbag First Inflator

- Title: DTC B0029-1A: Decreased Resistance in the Right Side Curtain Airbag First Inflator
- Source path: `pages\11603.html`
- Chunk ID: `chunk_e05e06fb6354`
- Images: none
- Duplicate sources: `pages\19782.html`

### Full Text

````text
# DTC B0029-1A: Decreased Resistance in the Right Side Curtain Airbag First Inflator

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines) Right side curtain airbag internal failure (Right side curtain airbag inflator) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the right side curtain airbag inflator (RCA+, RCA- lines)

- Right side curtain airbag internal failure (Right side curtain airbag inflator)

- SRS unit internal failure
````

## Chunk 8986: DTC B0050-11: Short or Decreased Resistance in the Driver's Seat Belt Buckle Switch

- Title: DTC B0050-11: Short or Decreased Resistance in the Driver's Seat Belt Buckle Switch
- Source path: `pages\11604.html`
- Chunk ID: `chunk_8f76d86d3762`
- Images: none
- Duplicate sources: `pages\19783.html`

### Full Text

````text
# DTC B0050-11: Short or Decreased Resistance in the Driver's Seat Belt Buckle Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground or Short to power between the SRS unit and the driver's seat belt buckle switch (FLBC line) Driver's seat belt buckle assembly internal failure (Driver's seat belt buckle switch) SRS unit internal failure

- Short to ground or Short to power between the SRS unit and the driver's seat belt buckle switch (FLBC line)

- Driver's seat belt buckle assembly internal failure (Driver's seat belt buckle switch)

- SRS unit internal failure
````

## Chunk 8987: DTC B0050-13: Open or Increased Resistance in the Driver's Seat Belt Buckle Switch

- Title: DTC B0050-13: Open or Increased Resistance in the Driver's Seat Belt Buckle Switch
- Source path: `pages\11605.html`
- Chunk ID: `chunk_32b9aeb89e18`
- Images: none
- Duplicate sources: `pages\19784.html`

### Full Text

````text
# DTC B0050-13: Open or Increased Resistance in the Driver's Seat Belt Buckle Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's seat belt buckle switch (FLBC line) Open or Poor connection between the driver's seat belt buckle switch and the body ground (GND line) Driver's seat belt buckle assembly internal failure (Driver's seat belt buckle switch) SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's seat belt buckle switch (FLBC line)

- Open or Poor connection between the driver's seat belt buckle switch and the body ground (GND line)

- Driver's seat belt buckle assembly internal failure (Driver's seat belt buckle switch)

- SRS unit internal failure
````

## Chunk 8988: DTC B0052-11: Short or Decreased Resistance in the Front Passenger's Seat Belt Buckle Switch

- Title: DTC B0052-11: Short or Decreased Resistance in the Front Passenger's Seat Belt Buckle Switch
- Source path: `pages\11606.html`
- Chunk ID: `chunk_7ad734cf4761`
- Images: none
- Duplicate sources: `pages\19785.html`

### Full Text

````text
# DTC B0052-11: Short or Decreased Resistance in the Front Passenger's Seat Belt Buckle Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground or Short to power between the SRS unit and the front passenger's seat belt buckle switch (FRBC line) Front passenger's seat belt buckle assembly internal failure (Front passenger's seat belt buckle switch) SRS unit internal failure

- Short to ground or Short to power between the SRS unit and the front passenger's seat belt buckle switch (FRBC line)

- Front passenger's seat belt buckle assembly internal failure (Front passenger's seat belt buckle switch)

- SRS unit internal failure
````

## Chunk 8989: DTC B0052-13: Open or Increased Resistance in the Front Passenger's Seat Belt Buckle Switch

- Title: DTC B0052-13: Open or Increased Resistance in the Front Passenger's Seat Belt Buckle Switch
- Source path: `pages\11607.html`
- Chunk ID: `chunk_85cd3d305c7d`
- Images: none
- Duplicate sources: `pages\19786.html`

### Full Text

````text
# DTC B0052-13: Open or Increased Resistance in the Front Passenger's Seat Belt Buckle Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's seat belt buckle switch (FRBC line) Open or Poor connection between the front passenger's seat belt buckle switch and the body ground (GND line) Front passenger's seat belt buckle assembly internal failure (Front passenger's seat belt buckle switch) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's seat belt buckle switch (FRBC line)

- Open or Poor connection between the front passenger's seat belt buckle switch and the body ground (GND line)

- Front passenger's seat belt buckle assembly internal failure (Front passenger's seat belt buckle switch)

- SRS unit internal failure
````

## Chunk 8990: DTC B0070-11: Short to Ground in the Driver's Seat Belt Tensioner

- Title: DTC B0070-11: Short to Ground in the Driver's Seat Belt Tensioner
- Source path: `pages\11608.html`
- Chunk ID: `chunk_7c80f9a571e4`
- Images: none
- Duplicate sources: `pages\19787.html`

### Full Text

````text
# DTC B0070-11: Short to Ground in the Driver's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines) Driver's seat belt internal failure (Driver's seat belt tensioner) SRS unit internal failure

- Short to ground between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines)

- Driver's seat belt internal failure (Driver's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8991: DTC B0070-12: Short to Power in the Driver's Seat Belt Tensioner

- Title: DTC B0070-12: Short to Power in the Driver's Seat Belt Tensioner
- Source path: `pages\11609.html`
- Chunk ID: `chunk_bf7fab573b60`
- Images: none
- Duplicate sources: `pages\19788.html`

### Full Text

````text
# DTC B0070-12: Short to Power in the Driver's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines) SRS unit internal failure

- Short to power between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines)

- SRS unit internal failure
````

## Chunk 8992: DTC B0070-13: Open or Increased Resistance in the Driver's Seat Belt Tensioner

- Title: DTC B0070-13: Open or Increased Resistance in the Driver's Seat Belt Tensioner
- Source path: `pages\11610.html`
- Chunk ID: `chunk_33974bfa3af9`
- Images: none
- Duplicate sources: `pages\19789.html`

### Full Text

````text
# DTC B0070-13: Open or Increased Resistance in the Driver's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines) Driver's seat belt internal failure (Driver's seat belt tensioner) SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines)

- Driver's seat belt internal failure (Driver's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8993: DTC B0070-1A: Decreased Resistance in the Driver's Seat Belt Tensioner

- Title: DTC B0070-1A: Decreased Resistance in the Driver's Seat Belt Tensioner
- Source path: `pages\11611.html`
- Chunk ID: `chunk_53bd8345bdb2`
- Images: none
- Duplicate sources: `pages\19790.html`

### Full Text

````text
# DTC B0070-1A: Decreased Resistance in the Driver's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines) Driver's seat belt internal failure (Driver's seat belt tensioner) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the driver's seat belt tensioner (LRP+, LRP- lines)

- Driver's seat belt internal failure (Driver's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8994: DTC B0072-11: Short to Ground in the Front Passenger's Seat Belt Tensioner

- Title: DTC B0072-11: Short to Ground in the Front Passenger's Seat Belt Tensioner
- Source path: `pages\11612.html`
- Chunk ID: `chunk_f1e601198da2`
- Images: none
- Duplicate sources: `pages\19791.html`

### Full Text

````text
# DTC B0072-11: Short to Ground in the Front Passenger's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines) Front passenger's seat belt internal failure (Front passenger's seat belt tensioner) SRS unit internal failure

- Short to ground between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines)

- Front passenger's seat belt internal failure (Front passenger's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8995: DTC B0072-12: Short to Power in the Front Passenger's Seat Belt Tensioner

- Title: DTC B0072-12: Short to Power in the Front Passenger's Seat Belt Tensioner
- Source path: `pages\11613.html`
- Chunk ID: `chunk_6a6a9d829ef2`
- Images: none
- Duplicate sources: `pages\19792.html`

### Full Text

````text
# DTC B0072-12: Short to Power in the Front Passenger's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines) SRS unit internal failure

- Short to power between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines)

- SRS unit internal failure
````

## Chunk 8996: DTC B0072-13: Open or Increased Resistance in the Front Passenger's Seat Belt Tensioner

- Title: DTC B0072-13: Open or Increased Resistance in the Front Passenger's Seat Belt Tensioner
- Source path: `pages\11614.html`
- Chunk ID: `chunk_9381c075d008`
- Images: none
- Duplicate sources: `pages\19793.html`

### Full Text

````text
# DTC B0072-13: Open or Increased Resistance in the Front Passenger's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines) Front passenger's seat belt internal failure (Front passenger's seat belt tensioner) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines)

- Front passenger's seat belt internal failure (Front passenger's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8997: DTC B0072-1A: Decreased Resistance in the Front Passenger's Seat Belt Tensioner

- Title: DTC B0072-1A: Decreased Resistance in the Front Passenger's Seat Belt Tensioner
- Source path: `pages\11615.html`
- Chunk ID: `chunk_f3d6e2d7551d`
- Images: none
- Duplicate sources: `pages\19794.html`

### Full Text

````text
# DTC B0072-1A: Decreased Resistance in the Front Passenger's Seat Belt Tensioner

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to another line or Poor connection between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines) Front passenger's seat belt internal failure (Front passenger's seat belt tensioner) SRS unit internal failure

- Short to another line or Poor connection between the SRS unit and the front passenger's seat belt tensioner (RRP+, RRP- lines)

- Front passenger's seat belt internal failure (Front passenger's seat belt tensioner)

- SRS unit internal failure
````

## Chunk 8998: DTC B0090-4A: Internal Failure of the Left Front Impact Sensor

- Title: DTC B0090-4A: Internal Failure of the Left Front Impact Sensor
- Source path: `pages\11616.html`
- Chunk ID: `chunk_1a9c863108c9`
- Images: none
- Duplicate sources: `pages\19795.html`

### Full Text

````text
# DTC B0090-4A: Internal Failure of the Left Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Left front impact sensor internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Left front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 8999: DTC B0090-87: No Signal From the Left Front Impact Sensor

- Title: DTC B0090-87: No Signal From the Left Front Impact Sensor
- Source path: `pages\11617.html`
- Chunk ID: `chunk_8d06523c8175`
- Images: none
- Duplicate sources: `pages\19796.html`

### Full Text

````text
# DTC B0090-87: No Signal From the Left Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left front impact sensor (LFS+, LFS- lines) Left front impact sensor internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left front impact sensor (LFS+, LFS- lines)

- Left front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 9000: DTC B0090-92: Internal Failure of the Left Front Impact Sensor

- Title: DTC B0090-92: Internal Failure of the Left Front Impact Sensor
- Source path: `pages\11618.html`
- Chunk ID: `chunk_f59b098dd042`
- Images: none
- Duplicate sources: `pages\19797.html`

### Full Text

````text
# DTC B0090-92: Internal Failure of the Left Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Left front impact sensor internal failure SRS unit internal failure

- Left front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 9001: DTC B0091-4A: Internal Failure of the Left Side Impact Sensor (first)

- Title: DTC B0091-4A: Internal Failure of the Left Side Impact Sensor (first)
- Source path: `pages\11619.html`
- Chunk ID: `chunk_7b55497ca0a1`
- Images: none
- Duplicate sources: `pages\19798.html`

### Full Text

````text
# DTC B0091-4A: Internal Failure of the Left Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Left side impact sensor (first) internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Left side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9002: DTC B0091-87: No Signal From the Left Side Impact Sensor (first)

- Title: DTC B0091-87: No Signal From the Left Side Impact Sensor (first)
- Source path: `pages\11620.html`
- Chunk ID: `chunk_379c96b65335`
- Images: none
- Duplicate sources: `pages\19799.html`

### Full Text

````text
# DTC B0091-87: No Signal From the Left Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left side impact sensor (first) (LS1+, LS1- lines) Left side impact sensor (first) internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left side impact sensor (first) (LS1+, LS1- lines)

- Left side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9003: DTC B0091-92: Internal Failure of the Left Side Impact Sensor (first)

- Title: DTC B0091-92: Internal Failure of the Left Side Impact Sensor (first)
- Source path: `pages\11621.html`
- Chunk ID: `chunk_881cf0bb0449`
- Images: none
- Duplicate sources: `pages\19800.html`

### Full Text

````text
# DTC B0091-92: Internal Failure of the Left Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Left side impact sensor (first) internal failure SRS unit internal failure

- Left side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9004: DTC B0092-4A: Internal Failure of the Left Side Impact Sensor (second)

- Title: DTC B0092-4A: Internal Failure of the Left Side Impact Sensor (second)
- Source path: `pages\11622.html`
- Chunk ID: `chunk_1be71fc997ff`
- Images: none
- Duplicate sources: `pages\19801.html`

### Full Text

````text
# DTC B0092-4A: Internal Failure of the Left Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Left side impact sensor (second) internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Left side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9005: DTC B0092-87: No Signal From the Left Side Impact Sensor (second)

- Title: DTC B0092-87: No Signal From the Left Side Impact Sensor (second)
- Source path: `pages\11623.html`
- Chunk ID: `chunk_73a251f48c66`
- Images: none
- Duplicate sources: `pages\19802.html`

### Full Text

````text
# DTC B0092-87: No Signal From the Left Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left side impact sensor (second) (LS2+, LS2- lines) Left side impact sensor (second) internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the left side impact sensor (second) (LS2+, LS2- lines)

- Left side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9006: DTC B0092-92: Internal Failure of the Left Side Impact Sensor (second)

- Title: DTC B0092-92: Internal Failure of the Left Side Impact Sensor (second)
- Source path: `pages\11624.html`
- Chunk ID: `chunk_5d3a21e5b91b`
- Images: none
- Duplicate sources: `pages\19803.html`

### Full Text

````text
# DTC B0092-92: Internal Failure of the Left Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Left side impact sensor (second) internal failure SRS unit internal failure

- Left side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9007: DTC B0095-4A: Internal Failure of the Right Front Impact Sensor

- Title: DTC B0095-4A: Internal Failure of the Right Front Impact Sensor
- Source path: `pages\11625.html`
- Chunk ID: `chunk_6d3b88d28d53`
- Images: none
- Duplicate sources: `pages\19804.html`

### Full Text

````text
# DTC B0095-4A: Internal Failure of the Right Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Right front impact sensor internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Right front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 9008: DTC B0095-87: No Signal From the Right Front Impact Sensor

- Title: DTC B0095-87: No Signal From the Right Front Impact Sensor
- Source path: `pages\11626.html`
- Chunk ID: `chunk_043c36e2da1d`
- Images: none
- Duplicate sources: `pages\19805.html`

### Full Text

````text
# DTC B0095-87: No Signal From the Right Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right front impact sensor (RFS+, RFS- lines) Right front impact sensor internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right front impact sensor (RFS+, RFS- lines)

- Right front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 9009: DTC B0095-92: Internal Failure of the Right Front Impact Sensor

- Title: DTC B0095-92: Internal Failure of the Right Front Impact Sensor
- Source path: `pages\11627.html`
- Chunk ID: `chunk_8a49c8a5916a`
- Images: none
- Duplicate sources: `pages\19806.html`

### Full Text

````text
# DTC B0095-92: Internal Failure of the Right Front Impact Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Right front impact sensor internal failure SRS unit internal failure

- Right front impact sensor internal failure

- SRS unit internal failure
````

## Chunk 9010: DTC B0096-4A: Internal Failure of the Right Side Impact Sensor (first)

- Title: DTC B0096-4A: Internal Failure of the Right Side Impact Sensor (first)
- Source path: `pages\11628.html`
- Chunk ID: `chunk_b45cd2573a07`
- Images: none
- Duplicate sources: `pages\19807.html`

### Full Text

````text
# DTC B0096-4A: Internal Failure of the Right Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Right side impact sensor (first) internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Right side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9011: DTC B0096-87: No Signal From the Right Side Impact Sensor (first)

- Title: DTC B0096-87: No Signal From the Right Side Impact Sensor (first)
- Source path: `pages\11629.html`
- Chunk ID: `chunk_08e99517fe92`
- Images: none
- Duplicate sources: `pages\19808.html`

### Full Text

````text
# DTC B0096-87: No Signal From the Right Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right side impact sensor (first) (RS1+, RS1- lines) Right side impact sensor (first) internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right side impact sensor (first) (RS1+, RS1- lines)

- Right side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9012: DTC B0096-92: Internal Failure of the Right Side Impact Sensor (first)

- Title: DTC B0096-92: Internal Failure of the Right Side Impact Sensor (first)
- Source path: `pages\11630.html`
- Chunk ID: `chunk_be5f4397eafe`
- Images: none
- Duplicate sources: `pages\19809.html`

### Full Text

````text
# DTC B0096-92: Internal Failure of the Right Side Impact Sensor (first)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Right side impact sensor (first) internal failure SRS unit internal failure

- Right side impact sensor (first) internal failure

- SRS unit internal failure
````

## Chunk 9013: DTC B0097-4A: Internal Failure of the Right Side Impact Sensor (second)

- Title: DTC B0097-4A: Internal Failure of the Right Side Impact Sensor (second)
- Source path: `pages\11631.html`
- Chunk ID: `chunk_a95be161080b`
- Images: none
- Duplicate sources: `pages\19810.html`

### Full Text

````text
# DTC B0097-4A: Internal Failure of the Right Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Incorrect impact sensor installed Incorrect SRS unit installed Right side impact sensor (second) internal failure SRS unit internal failure

- Incorrect impact sensor installed

- Incorrect SRS unit installed

- Right side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9014: DTC B0097-87: No Signal From the Right Side Impact Sensor (second)

- Title: DTC B0097-87: No Signal From the Right Side Impact Sensor (second)
- Source path: `pages\11632.html`
- Chunk ID: `chunk_f2eaa3d9ce46`
- Images: none
- Duplicate sources: `pages\19811.html`

### Full Text

````text
# DTC B0097-87: No Signal From the Right Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right side impact sensor (second) (RS2+, RS2- lines) Right side impact sensor (second) internal failure SRS unit internal failure

- Open, Short to another line, Short to ground, Short to power, or Poor connection between the SRS unit and the right side impact sensor (second) (RS2+, RS2- lines)

- Right side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9015: DTC B0097-92: Internal Failure of the Right Side Impact Sensor (second)

- Title: DTC B0097-92: Internal Failure of the Right Side Impact Sensor (second)
- Source path: `pages\11633.html`
- Chunk ID: `chunk_b5c48537b258`
- Images: none
- Duplicate sources: `pages\19812.html`

### Full Text

````text
# DTC B0097-92: Internal Failure of the Right Side Impact Sensor (second)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Right side impact sensor (second) internal failure SRS unit internal failure

- Right side impact sensor (second) internal failure

- SRS unit internal failure
````

## Chunk 9016: DTC B00A0-54: Front Passenger's Weight Sensor not Calibrated

- Title: DTC B00A0-54: Front Passenger's Weight Sensor not Calibrated
- Source path: `pages\11634.html`
- Chunk ID: `chunk_f7add9e1d65e`
- Images: none
- Duplicate sources: `pages\19813.html`

### Full Text

````text
# DTC B00A0-54: Front Passenger's Weight Sensor not Calibrated

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor not initialized

- Front passenger's weight sensor not initialized
````

## Chunk 9017: DTC B00B5-11: Short or Decreased Resistance in the Driver's Seat Position Sensor

- Title: DTC B00B5-11: Short or Decreased Resistance in the Driver's Seat Position Sensor
- Source path: `pages\11635.html`
- Chunk ID: `chunk_6e8e2aaa2dd2`
- Images: none
- Duplicate sources: `pages\19814.html`

### Full Text

````text
# DTC B00B5-11: Short or Decreased Resistance in the Driver's Seat Position Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the driver's seat position sensor (SPS/SS+ SPS line) Driver's seat position sensor internal failure SRS unit internal failure

- Short to ground between the SRS unit and the driver's seat position sensor (SPS/SS+ SPS line)

- Driver's seat position sensor internal failure

- SRS unit internal failure
````

## Chunk 9018: DTC B00B5-13: Open or Increased Resistance in the Driver's Seat Position Sensor

- Title: DTC B00B5-13: Open or Increased Resistance in the Driver's Seat Position Sensor
- Source path: `pages\11636.html`
- Chunk ID: `chunk_5fcb89684ffb`
- Images: none
- Duplicate sources: `pages\19815.html`

### Full Text

````text
# DTC B00B5-13: Open or Increased Resistance in the Driver's Seat Position Sensor

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the driver's seat position sensor (SPS/SS+ SPS line) Open or Poor connection between the driver's seat position sensor and the body ground (GND/GND SPS line) Driver's seat position sensor internal failure SRS unit internal failure

- Open or Poor connection between the SRS unit and the driver's seat position sensor (SPS/SS+ SPS line)

- Open or Poor connection between the driver's seat position sensor and the body ground (GND/GND SPS line)

- Driver's seat position sensor internal failure

- SRS unit internal failure
````

## Chunk 9019: DTC B00C0-16: Internal Failure of the Front Passenger's Weight Sensor (front inner side)

- Title: DTC B00C0-16: Internal Failure of the Front Passenger's Weight Sensor (front inner side)
- Source path: `pages\11637.html`
- Chunk ID: `chunk_89223c154656`
- Images: none
- Duplicate sources: `pages\19816.html`

### Full Text

````text
# DTC B00C0-16: Internal Failure of the Front Passenger's Weight Sensor (front inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (front inner side)

- Front passenger's weight sensor internal failure (front inner side)
````

## Chunk 9020: DTC B00C0-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (front inner side)

- Title: DTC B00C0-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (front inner side)
- Source path: `pages\11638.html`
- Chunk ID: `chunk_d45f37d175dc`
- Images: none
- Duplicate sources: `pages\19817.html`

### Full Text

````text
# DTC B00C0-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (front inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (front inner side)

- Front passenger's weight sensor internal failure (front inner side)
````

## Chunk 9021: DTC B00C0-54: Different Serial ID of the Front Passenger's Weight Sensor (front inner side)

- Title: DTC B00C0-54: Different Serial ID of the Front Passenger's Weight Sensor (front inner side)
- Source path: `pages\11639.html`
- Chunk ID: `chunk_f85a948c01b9`
- Images: none
- Duplicate sources: `pages\19818.html`

### Full Text

````text
# DTC B00C0-54: Different Serial ID of the Front Passenger's Weight Sensor (front inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (front inner side)

- Front passenger's weight sensor internal failure (front inner side)
````

## Chunk 9022: DTC B00C0-87: No Signal From the Front Passenger's Weight Sensor (front inner side)

- Title: DTC B00C0-87: No Signal From the Front Passenger's Weight Sensor (front inner side)
- Source path: `pages\11640.html`
- Chunk ID: `chunk_4c86be238d9e`
- Images: none
- Duplicate sources: `pages\19819.html`

### Full Text

````text
# DTC B00C0-87: No Signal From the Front Passenger's Weight Sensor (front inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS, SWS-/GND SWS, SWSS/LIN SWS lines) Short to power or Short to ground between the SRS unit and the front passenger's weight sensor (front inner side) (SWSS/LIN SWS line) Short to another line or Poor connection between the SRS unit and the front passenger's weight sensor (front inner side) (SWSS/LIN SWS line to SWS-/GND SWS line, SWSS/LIN SWS line to SWS+/PWR SWS line) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS, SWS-/GND SWS, SWSS/LIN SWS lines)

- Short to power or Short to ground between the SRS unit and the front passenger's weight sensor (front inner side) (SWSS/LIN SWS line)

- Short to another line or Poor connection between the SRS unit and the front passenger's weight sensor (front inner side) (SWSS/LIN SWS line to SWS-/GND SWS line, SWSS/LIN SWS line to SWS+/PWR SWS line)

- SRS unit internal failure
````

## Chunk 9023: DTC B00C0-96: Internal Failure of the Front Passenger's Weight Sensor (front inner side)

- Title: DTC B00C0-96: Internal Failure of the Front Passenger's Weight Sensor (front inner side)
- Source path: `pages\11641.html`
- Chunk ID: `chunk_2141aef591dc`
- Images: none
- Duplicate sources: `pages\19820.html`

### Full Text

````text
# DTC B00C0-96: Internal Failure of the Front Passenger's Weight Sensor (front inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (front inner side)

- Front passenger's weight sensor internal failure (front inner side)
````

## Chunk 9024: DTC B00C2-16: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)

- Title: DTC B00C2-16: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)
- Source path: `pages\11642.html`
- Chunk ID: `chunk_2ed06f9e3f26`
- Images: none
- Duplicate sources: `pages\19821.html`

### Full Text

````text
# DTC B00C2-16: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (rear inner side)

- Front passenger's weight sensor internal failure (rear inner side)
````

## Chunk 9025: DTC B00C2-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (rear inner side)

- Title: DTC B00C2-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (rear inner side)
- Source path: `pages\11643.html`
- Chunk ID: `chunk_b4888fd5f43d`
- Images: none
- Duplicate sources: `pages\19822.html`

### Full Text

````text
# DTC B00C2-4A: Different Supplier ID/Function ID of the Front Passenger's Weight Sensor (rear inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (rear inner side)

- Front passenger's weight sensor internal failure (rear inner side)
````

## Chunk 9026: DTC B00C2-54: Different Serial ID of the Front Passenger's Weight Sensor (rear inner side)

- Title: DTC B00C2-54: Different Serial ID of the Front Passenger's Weight Sensor (rear inner side)
- Source path: `pages\11644.html`
- Chunk ID: `chunk_d68a5f7d5c76`
- Images: none
- Duplicate sources: `pages\19823.html`

### Full Text

````text
# DTC B00C2-54: Different Serial ID of the Front Passenger's Weight Sensor (rear inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (rear inner side)

- Front passenger's weight sensor internal failure (rear inner side)
````

## Chunk 9027: DTC B00C2-87: No Signal From the Front Passenger's Weight Sensor (rear inner side)

- Title: DTC B00C2-87: No Signal From the Front Passenger's Weight Sensor (rear inner side)
- Source path: `pages\11645.html`
- Chunk ID: `chunk_135c2dce308f`
- Images: none
- Duplicate sources: `pages\19824.html`

### Full Text

````text
# DTC B00C2-87: No Signal From the Front Passenger's Weight Sensor (rear inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS, SWS-/GND SWS, SWSS/LIN SWS lines) SRS unit internal failure

- Open or Poor connection between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS, SWS-/GND SWS, SWSS/LIN SWS lines)

- SRS unit internal failure
````

## Chunk 9028: DTC B00C2-96: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)

- Title: DTC B00C2-96: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)
- Source path: `pages\11646.html`
- Chunk ID: `chunk_c49f9194647c`
- Images: none
- Duplicate sources: `pages\19825.html`

### Full Text

````text
# DTC B00C2-96: Internal Failure of the Front Passenger's Weight Sensor (rear inner side)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Front passenger's weight sensor internal failure (rear inner side)

- Front passenger's weight sensor internal failure (rear inner side)
````

## Chunk 9029: DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)

- Title: DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)
- Source path: `pages\11647.html`
- Chunk ID: `chunk_ea1b94551e24`
- Images: none
- Duplicate sources: `pages\19826.html`

### Full Text

````text
# DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Short to ground between the SRS unit and the front passenger's airbag cutoff indicator (OFF PTT line) Open or Short to ground between the 12 volt battery and the front passenger's airbag cutoff indicator Front passenger's airbag cutoff indicator internal failure SRS unit internal failure

- Open or Short to ground between the SRS unit and the front passenger's airbag cutoff indicator (OFF PTT line)

- Open or Short to ground between the 12 volt battery and the front passenger's airbag cutoff indicator

- Front passenger's airbag cutoff indicator internal failure

- SRS unit internal failure
````

## Chunk 9030: DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)

- Title: DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)
- Source path: `pages\11648.html`
- Chunk ID: `chunk_e36d6a381a67`
- Images: none
- Duplicate sources: `pages\19827.html`

### Full Text

````text
# DTC B00D5-14: Open or Short to Ground in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Short to ground between the SRS unit and the front passenger's airbag ON/OFF indicator (OFF PTT line) Open or Short to ground between the 12 volt battery and the front passenger's airbag ON/OFF indicator Front passenger's airbag ON/OFF indicator internal failure SRS unit internal failure

- Open or Short to ground between the SRS unit and the front passenger's airbag ON/OFF indicator (OFF PTT line)

- Open or Short to ground between the 12 volt battery and the front passenger's airbag ON/OFF indicator

- Front passenger's airbag ON/OFF indicator internal failure

- SRS unit internal failure
````

## Chunk 9031: DTC B00D5-17: Short to Power in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)

- Title: DTC B00D5-17: Short to Power in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)
- Source path: `pages\11649.html`
- Chunk ID: `chunk_8f97d7ccdee4`
- Images: none
- Duplicate sources: `pages\19828.html`

### Full Text

````text
# DTC B00D5-17: Short to Power in the Front Passenger's Airbag Cutoff Indicator (USA and Canada models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's airbag cutoff indicator (OFF PTT line) Front passenger's airbag cutoff indicator internal failure SRS unit internal failure

- Short to power between the SRS unit and the front passenger's airbag cutoff indicator (OFF PTT line)

- Front passenger's airbag cutoff indicator internal failure

- SRS unit internal failure
````

## Chunk 9032: DTC B00D5-17: Short to Power in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)

- Title: DTC B00D5-17: Short to Power in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)
- Source path: `pages\11650.html`
- Chunk ID: `chunk_be0e0d7e507c`
- Images: none
- Duplicate sources: `pages\19829.html`

### Full Text

````text
# DTC B00D5-17: Short to Power in the Front Passenger's Airbag ON/OFF Indicator (Mexico models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to power between the SRS unit and the front passenger's airbag ON/OFF indicator (OFF PTT line) Front passenger's airbag ON/OFF indicator internal failure SRS unit internal failure

- Short to power between the SRS unit and the front passenger's airbag ON/OFF indicator (OFF PTT line)

- Front passenger's airbag ON/OFF indicator internal failure

- SRS unit internal failure
````

## Chunk 9033: DTC B00DF-11: Short in the Front Passenger's Airbag ON/OFF Switch

- Title: DTC B00DF-11: Short in the Front Passenger's Airbag ON/OFF Switch
- Source path: `pages\11651.html`
- Chunk ID: `chunk_9cca4f328c2a`
- Images: none
- Duplicate sources: `pages\19830.html`

### Full Text

````text
# DTC B00DF-11: Short in the Front Passenger's Airbag ON/OFF Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground between the SRS unit and the front passenger's airbag ON/OFF switch (ACS line) Front passenger's airbag ON/OFF switch internal failure SRS unit internal failure

- Short to ground between the SRS unit and the front passenger's airbag ON/OFF switch (ACS line)

- Front passenger's airbag ON/OFF switch internal failure

- SRS unit internal failure
````

## Chunk 9034: DTC B00DF-13: Open in the Front Passenger's Airbag ON/OFF Switch

- Title: DTC B00DF-13: Open in the Front Passenger's Airbag ON/OFF Switch
- Source path: `pages\11652.html`
- Chunk ID: `chunk_81e618dbe59f`
- Images: none
- Duplicate sources: `pages\19831.html`

### Full Text

````text
# DTC B00DF-13: Open in the Front Passenger's Airbag ON/OFF Switch

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 9 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 9 seconds.

Duration | About 9 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Short to power between the SRS unit and the front passenger's airbag ON/OFF switch (ACS line) Open or Short to power between the front passenger's airbag ON/OFF switch and the body ground (GND line) Front passenger's airbag ON/OFF switch internal failure SRS unit internal failure

- Open or Short to power between the SRS unit and the front passenger's airbag ON/OFF switch (ACS line)

- Open or Short to power between the front passenger's airbag ON/OFF switch and the body ground (GND line)

- Front passenger's airbag ON/OFF switch internal failure

- SRS unit internal failure
````

## Chunk 9035: DTC B2800-49: Internal Failure of the SRS Unit

- Title: DTC B2800-49: Internal Failure of the SRS Unit
- Source path: `pages\11653.html`
- Chunk ID: `chunk_daf341727acf`
- Images: none
- Duplicate sources: `pages\19832.html`

### Full Text

````text
# DTC B2800-49: Internal Failure of the SRS Unit

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit internal failure

- SRS unit internal failure
````

## Chunk 9036: DTC B2801-49: Internal Failure of the SRS Unit

- Title: DTC B2801-49: Internal Failure of the SRS Unit
- Source path: `pages\11654.html`
- Chunk ID: `chunk_69bd887423a1`
- Images: none
- Duplicate sources: `pages\19833.html`

### Full Text

````text
# DTC B2801-49: Internal Failure of the SRS Unit

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit internal failure

- SRS unit internal failure
````

## Chunk 9037: DTC B2802-49: Internal failure of the SRS unit

- Title: DTC B2802-49: Internal failure of the SRS unit
- Source path: `pages\11655.html`
- Chunk ID: `chunk_21b994b1e99f`
- Images: none
- Duplicate sources: `pages\19834.html`

### Full Text

````text
# DTC B2802-49: Internal failure of the SRS unit

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit internal failure

- SRS unit internal failure
````

## Chunk 9038: DTC B2840-13: SRS Unit Connector A Not Properly Installed and DTC B2841-13: SRS Unit Connector B Not Properly Installed

- Title: DTC B2840-13: SRS Unit Connector A Not Properly Installed and DTC B2841-13: SRS Unit Connector B Not Properly Installed
- Source path: `pages\11656.html`
- Chunk ID: `chunk_22749a046cc7`
- Images: none
- Duplicate sources: `pages\19835.html`

### Full Text

````text
# DTC B2840-13: SRS Unit Connector A Not Properly Installed and DTC B2841-13: SRS Unit Connector B Not Properly Installed

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Poor connection between the SRS unit and connector A or poor connection between the SRS unit and connector B SRS unit internal failure

- Poor connection between the SRS unit and connector A or poor connection between the SRS unit and connector B

- SRS unit internal failure

NOTE: If a loose connection failure occurs, DTC B2840-13 and B2841-13 are stored at same time to the SRS unit.
````

## Chunk 9039: DTC C0061-96: Internal Failure of the SRS Unit

- Title: DTC C0061-96: Internal Failure of the SRS Unit
- Source path: `pages\11657.html`
- Chunk ID: `chunk_587dd90ac91d`
- Images: none
- Duplicate sources: `pages\19836.html`

### Full Text

````text
# DTC C0061-96: Internal Failure of the SRS Unit

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit internal failure

- SRS unit internal failure
````

## Chunk 9040: DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (Without CAN Gateway)

- Title: DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (Without CAN Gateway)
- Source path: `pages\11658.html`
- Chunk ID: `chunk_c80cda9f0f97`
- Images: none
- Duplicate sources: `pages\19837.html`

### Full Text

````text
# DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (Without CAN Gateway)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the VSA modulator-control unit and the SRS unit (F-CAN_H, F-CAN_L lines) VSA modulator-control unit internal failure

- Open or Poor connection between the VSA modulator-control unit and the SRS unit (F-CAN_H, F-CAN_L lines)

- VSA modulator-control unit internal failure
````

## Chunk 9041: DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (With CAN Gateway)

- Title: DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (With CAN Gateway)
- Source path: `pages\11659.html`
- Chunk ID: `chunk_973ce684abe3`
- Images: none
- Duplicate sources: `pages\19838.html`

### Full Text

````text
# DTC U0122-00: Lost Communication With the VSA Modulator-Control Unit (wheel speed sensor signal error) (With CAN Gateway)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Open or Poor connection between the CAN gateway and the SRS unit (F-CAN B_H, F-CAN B_L lines) Open or Poor connection between the CAN gateway and the VSA modulator-control unit (F-CAN A_H, F-CAN A_L, F-CAN B_H, F-CAN B_L lines) VSA modulator-control unit internal failure SRS unit internal failure

- Open or Poor connection between the CAN gateway and the SRS unit (F-CAN B_H, F-CAN B_L lines)

- Open or Poor connection between the CAN gateway and the VSA modulator-control unit (F-CAN A_H, F-CAN A_L, F-CAN B_H, F-CAN B_L lines)

- VSA modulator-control unit internal failure

- SRS unit internal failure
````

## Chunk 9042: DTC U3000-49: Internal Failure of the SRS Unit (USA and Canada models)

- Title: DTC U3000-49: Internal Failure of the SRS Unit (USA and Canada models)
- Source path: `pages\11660.html`
- Chunk ID: `chunk_63c419968e52`
- Images: none
- Duplicate sources: `pages\19839.html`

### Full Text

````text
# DTC U3000-49: Internal Failure of the SRS Unit (USA and Canada models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | Short to ground or Short to power between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS line) Short to another line between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS line to SWS-/GND SWS line) Short to ground or Short to power between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS line) Short to another line between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS line to SWS-/GND SWS line) SRS unit internal failure

- Short to ground or Short to power between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS line)

- Short to another line between the SRS unit and the front passenger's weight sensor (front inner side) (SWS+/PWR SWS line to SWS-/GND SWS line)

- Short to ground or Short to power between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS line)

- Short to another line between the SRS unit and the front passenger's weight sensor (rear inner side) (SWS+/PWR SWS line to SWS-/GND SWS line)

- SRS unit internal failure
````

## Chunk 9043: DTC U3000-49: Internal Failure of the SRS Unit (Mexico models)

- Title: DTC U3000-49: Internal Failure of the SRS Unit (Mexico models)
- Source path: `pages\11661.html`
- Chunk ID: `chunk_676d64d1d10a`
- Images: none
- Duplicate sources: `pages\19840.html`

### Full Text

````text
# DTC U3000-49: Internal Failure of the SRS Unit (Mexico models)

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit internal failure

- SRS unit internal failure
````

## Chunk 9044: DTC U3000-51: SRS Unit Programming Error

- Title: DTC U3000-51: SRS Unit Programming Error
- Source path: `pages\11662.html`
- Chunk ID: `chunk_c3ab576a288b`
- Images: none
- Duplicate sources: `pages\19841.html`

### Full Text

````text
# DTC U3000-51: SRS Unit Programming Error

Confirmation Procedure | Basic Condition: 12 volt battery voltage 10 - 16 V Operating Condition: Turn the vehicle to the ON mode, and wait 6 seconds.

- 12 volt battery voltage 10 - 16 V

Operating Condition:

- Turn the vehicle to the ON mode, and wait 6 seconds.

Duration | About 6 seconds

DTC Type | 1 drive cycle SRS indicator on

- 1 drive cycle

- SRS indicator on

Fail Safe Action | None

- None

Possible Cause | SRS unit update is not completed properly SRS unit internal failure

- SRS unit update is not completed properly

- SRS unit internal failure
````

## Chunk 9045: SRS Indicator

- Title: SRS Indicator
- Source path: `pages\11663.html`
- Chunk ID: `chunk_0ffba90e6c94`
- Images: `images\GHH412274.jpeg`
- Duplicate sources: `pages\16884.html`

### Full Text

````text
# SRS Indicator

The SRS indicator (A) on the gauge control module indicates problems related with SRS function.

Courtesy of HONDA, U.S.A., INC.

If the system is OK, the SRS indicator should come on when you turn the vehicle to the ON mode, and then go off 6 seconds later. If it does not, there is a problem with the system.

NOTE: If the SRS indicator comes on, and SRS DTCs are not indicated, do the SRS symptom troubleshooting.
````

## Chunk 9046: How to Troubleshoot Circuits at the Connectors Especially for Connectors with Terminal Test Ports

- Title: How to Troubleshoot Circuits at the Connectors Especially for Connectors with Terminal Test Ports
- Source path: `pages\11664.html`
- Chunk ID: `chunk_48437feb6c65`
- Images: `images\GHH412275.jpeg`, `images\GHH412276.jpeg`
- Duplicate sources: `pages\16885.html`

### Full Text

````text
# How to Troubleshoot Circuits at the Connectors Especially for Connectors with Terminal Test Ports

Special Tools Required

Male Pin Probe 07ZAJ-RDJA110

NOTE:

- Make sure the 12 volt battery is fully charged when doing an electrical test. If the 12 volt battery is not fully charged, the results of the tests may not be accurate.

- To prevent damage to the connector terminals, do not insert test equipment probes, paper clips, or other substitutes. Damaged terminals cause a poor connection and an incorrect measurement.

1. When diagnosing or troubleshooting the circuits at the connectors (A), use the appropriate terminal test port as shown. Gently insert the pin probe of the tester or jumper wire at the terminal test port from the terminal side.

Courtesy of HONDA, U.S.A., INC.

NOTE:

- Do not insert the pin probes of the tester or a jumper wire at the terminal or the SRS short canceller terminal port.

- To prevent damage to the connector terminals, do not insert the test equipment probes, paper clips, or other substitutes as they can damage the terminals. Damaged terminals cause a poor connection and an incorrect measurement.

2. Connect one side of the patch cord terminals (A) to a commercially available digital multimeter (B), and connect the other side of the terminals (C) to the male pin probe.

Courtesy of HONDA, U.S.A., INC.

3. Gently contact the male pin probe at the terminal test port from the terminal side. Do not force the tips into the terminals.

NOTE:

- For accurate results, always use the male pin probe.

- To prevent damage to the connector terminals, do not insert test equipment probes, paper clips, or other substitutes. Damaged terminals cause a poor connection and an incorrect measurement.

- Do not puncture the insulation on a wire. Punctures can cause poor or intermittent electrical connections.
````

## Chunk 9047: How to Troubleshoot Circuits at the Connectors Except for Connectors with Terminal Test Ports

- Title: How to Troubleshoot Circuits at the Connectors Except for Connectors with Terminal Test Ports
- Source path: `pages\11665.html`
- Chunk ID: `chunk_4edd1033f71c`
- Images: `images\GHH412277.jpeg`
- Duplicate sources: `pages\16886.html`

### Full Text

````text
# How to Troubleshoot Circuits at the Connectors Except for Connectors with Terminal Test Ports

Special Tools Required

Back Probe Adapter, 17 mm 07TAZ-001020A

When using electrical test equipment, insert the back probe adapter, 17 mm of the tester into the wire side of the connector (except for connectors with terminal test ports).

NOTE:

- Make sure the 12 volt battery is fully charged when doing an electrical test. If the 12 volt battery is not fully charged, the results of the tests may not be accurate.

- Do not insert the probe of the tester into the terminal side of the connector, and do not tamper with the connector.

- To prevent damage to the connector, do not insert test equipment probes, paper clips, or other substitutes. Damaged terminals cause a poor connection and an incorrect measurement.

- Do not puncture the insulation on a wire. Punctures can cause poor or intermittent electrical connections.

- Do not insert the probe forcibly.

- Use specified service connectors in troubleshooting. Using improper tools could cause a diagnostic error due to poor metal-to-metal contact.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9048: Opening the SRS Unit Shorting Connectors for Diagnosis

- Title: Opening the SRS Unit Shorting Connectors for Diagnosis
- Source path: `pages\11666.html`
- Chunk ID: `chunk_5db64dd4739f`
- Images: `images\GHH412278.jpeg`, `images\GHH412279.jpeg`, `images\GHH412280.jpeg`
- Duplicate sources: `pages\16887.html`

### Full Text

````text
# Opening the SRS Unit Shorting Connectors for Diagnosis

Special Tools Required

- SRS Short Canceller 070AZ-SAA0100

NOTE:

- To prevent damage to the connector cavity, insert an SRS short canceller straight into the cavity from the terminal side.

- Before installing an SRS short canceller, wash it with electrical contact cleaner, then dry it with compressed air.

- Do not use an SRS short canceller if it is damaged.

- Make sure to remove an SRS short canceller before reconnecting the SRS unit connector.

- Some systems store data in memory that is lost when the 12 volt battery is disconnected. Before disconnecting the 12 volt battery, refer to 12 Volt Battery Terminal Disconnection and Reconnection .

When SRS unit connectors A (39P) and B (39P) are disconnected, short circuits are automatically created in the connector to prevent accidental deployment of an airbag. The circuit may need to be opened sometimes when diagnosing the system. Insert an SRS short canceller in the specified cavities when necessary to keep the circuit open for diagnosis.

Courtesy of HONDA, U.S.A., INC.

Terminal numbers are shown on the terminal side of the female terminals. Insert the SRS short canceller(s) into the cavities on the terminal side of the connector.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9049: DTC (Diagnostic Trouble Codes)

- Title: DTC (Diagnostic Trouble Codes)
- Source path: `pages\11667.html`
- Chunk ID: `chunk_7b8ee96fdb6c`
- Images: none
- Duplicate sources: `pages\16888.html`

### Full Text

````text
# DTC (Diagnostic Trouble Codes)

The self-diagnostic function of the SRS unit allows it to locate the causes of system problems and store this information in memory. For easier troubleshooting, this data can be retrieved with the HDS via the data link circuit.

- When you turn the vehicle to the ON mode, the SRS indicator should come on. If it goes off after 6 seconds, the system is normal and is not currently detecting any problems.

- If there is a problem, the system locates and defines the problem, stores this information in the memory, and turns on the SRS indicator. The data remains in the memory even if the vehicle is turned to the OFF (LOCK) mode or the 12 volt battery is disconnected.

- The data is stored in memory as a diagnostic trouble code (DTC).

- DTCs are either latching or resetting depending on the malfunction. With resetting DTCs, the SRS indicator goes off the next time the vehicle is turned to the ON mode, and the system is normal, but the DTC is still stored. With latching DTCs, the SRS indicator does not turn off until the malfunction is repaired and the DTC is cleared.

- When you connect the HDS to the data link connector (DLC), you can retrieve a more detailed DTC in the HDS "SRS" menu.

- After reading and recording the DTC, go to the troubleshooting procedure for that code.

Precautions

- Make sure the 12 volt battery is fully charged. If the 12 volt battery is dead or low, electrical measurement values may not be correct.

- Use only a digital multimeter to check the system. Make sure its output is 10 mA (0.01 A) or less when switched to the smallest value in the ohmmeter range. A tester with a higher output could damage the airbag circuit or cause accidental airbag deployment and possible injury.

- Whenever the vehicle is turned to the ON mode, or the vehicle is in the OFF (LOCK) mode for less than 3 minutes, be careful not to bump the SRS unit; the airbags could accidentally deploy and cause damage or injuries.

- Before removing the dashboard wire harness or floor wire harness, disconnect the driver's airbag inflator connector, the front passenger's airbag inflator connector, both side airbag inflator connectors, both side curtain airbag inflator connectors, and both front seat belt tensioner connectors.
````

## Chunk 9050: How to Read DTCs

- Title: How to Read DTCs
- Source path: `pages\11668.html`
- Chunk ID: `chunk_b788f8396c1b`
- Images: none
- Duplicate sources: `pages\16889.html`

### Full Text

````text
# How to Read DTCs

NOTE: Make sure the 12 volt battery is fully charged before you begin.

1. Turn the vehicle to the OFF (LOCK) mode, then wait for 10 seconds.

2. Connect the HDS to the data link connector (DLC)

3. Use the HDS to check for SRS DTCs.

4. Read and record the DTC.

NOTE: Do not clear the DTC until instructed by the troubleshooting procedure.

5. Turn the vehicle to the OFF (LOCK) mode, then wait for 10 seconds.

6. Do the troubleshooting procedure for the DTC.
````

## Chunk 9051: How to Clear DTCs

- Title: How to Clear DTCs
- Source path: `pages\11669.html`
- Chunk ID: `chunk_50ad3d15363a`
- Images: none
- Duplicate sources: `pages\16890.html`

### Full Text

````text
# How to Clear DTCs

NOTE: Make sure the 12 volt battery is fully charged before you begin.

1. Turn the vehicle to the OFF (LOCK) mode, then wait for 10 seconds.

2. Connect the HDS to the data link connector (DLC)

3. Clear the DTC(s) by following the screen prompts on the HDS.

4. Turn the vehicle to the OFF (LOCK) mode, then wait for 10 seconds.
````

## Chunk 9052: Troubleshooting Intermittent Failures

- Title: Troubleshooting Intermittent Failures
- Source path: `pages\11670.html`
- Chunk ID: `chunk_56809e07f1b6`
- Images: none
- Duplicate sources: `pages\16891.html`

### Full Text

````text
# Troubleshooting Intermittent Failures

If there was a malfunction that sets a DTC, but it does not recur, a DTC will be stored in the memory, and the SRS indicator may come on depending on the malfunction detected.

NOTE:

- Check the condition of the 12 volt battery . Low battery voltage may cause some intermittent failures.

- A faulty or damaged cable reel can cause intermittent problems related to the driver's airbag inflator DTCs.

After checking the DTC, troubleshoot as follows:

1. Check for DTCs with the HDS.

2. Clear the DTCs with the HDS.

3. Set the parking brake, then start the engine, and let it idle.

4. The SRS indicator comes on for about 6 seconds and then goes off.

5. Shake the related wire harnesses and the connectors, and look for loose connections, poor pin fits, and poor grounds.

6. Take a test-drive (quick acceleration, quick braking, and cornering), turn the steering wheel fully left and right, and hold it there for 5 to 10 seconds. If the problem recurs, the SRS indicator will come on.

7. If you cannot duplicate the concern, ask the customer about the conditions when it occurred, or ask the customer to demonstrate the concern.

8. If you cannot duplicate the intermittent failure, the system is OK at this time.
````

## Chunk 9053: DTC B0001-11

- Title: DTC B0001-11
- Source path: `pages\11671.html`
- Chunk ID: `chunk_97b9c670fb2a`
- Images: `images\GHH412281.jpeg`, `images\GHH412282.jpeg`, `images\GHH412283.jpeg`, `images\GHH412284.jpeg`
- Duplicate sources: `pages\16819.html`

### Full Text

````text
# DTC B0001-11

DTC B0001-11 : Short to Ground in the Driver's Airbag First Inflator

Special Tools Required

- SRS Inflator Simulator 07SAZ-TB4011A

- SRS Simulator Lead J 070AZ-SNAA100

NOTE:

- Before doing this troubleshooting procedure, find out if the vehicle was in a collision. If so, verify that all the required components were replaced with new components of the correct part number and were properly installed .

- Before doing this troubleshooting procedure, review SRS Precautions and Procedures , General Troubleshooting Information , and 12 Volt Battery Terminal Disconnection and Reconnection .

DTC Description | DTC

B0001-11 Short to ground in the driver's airbag first inflator

DTC (SRS)

- Problem verification -1. Clear the DTCs with the HDS. Clear DTCs -2. Turn the vehicle to the ON mode, then wait for 10 seconds. -3. Check for DTCs with the HDS. DTC Description DTC B0001-11 Short to ground in the driver's airbag first inflator Is DTC B0001-11 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

-1. Clear the DTCs with the HDS.

Clear DTCs

-2. Turn the vehicle to the ON mode, then wait for 10 seconds.

-3. Check for DTCs with the HDS.

DTC Description | DTC

B0001-11 Short to ground in the driver's airbag first inflator

Is DTC B0001-11 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

- Driver's airbag inflator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the driver's airbag . -4. Disconnect the following connector. Driver's airbag first inflator 2P connector (on the cable reel harness) NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown. Courtesy of HONDA, U.S.A., INC. -5. Connect terminals A and B with a jumper wire. Terminal A Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness) Terminal B Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness) Courtesy of HONDA, U.S.A., INC. -6. Reconnect the negative cable to the 12 volt battery. -7. Clear the DTCs with the HDS. Clear DTCs -8. Turn the vehicle to the ON mode, then wait for 10 seconds. -9. Check for DTCs with the HDS. DTC Description DTC B0001-11 Short to ground in the driver's airbag first inflator Is DTC B0001-11 indicated? YES Go to step 3. NO Short to ground in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the driver's airbag .

-4. Disconnect the following connector.

Driver's airbag first inflator 2P connector (on the cable reel harness)

NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown.

Courtesy of HONDA, U.S.A., INC.

-5. Connect terminals A and B with a jumper wire.

Terminal A | Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness)

Terminal B | Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness)

Courtesy of HONDA, U.S.A., INC.

-6. Reconnect the negative cable to the 12 volt battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-11 Short to ground in the driver's airbag first inflator

Is DTC B0001-11 indicated?

YES

Go to step 3.

NO

Short to ground in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6.
````

## Chunk 9054: DTC B0001-11

- Title: DTC B0001-11
- Source path: `pages\11671.html`
- Chunk ID: `chunk_63f871f606c1`
- Images: `images\GHH412281.jpeg`, `images\GHH412282.jpeg`, `images\GHH412283.jpeg`, `images\GHH412284.jpeg`
- Duplicate sources: `pages\16819.html`

### Full Text

````text
battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-11 Short to ground in the driver's airbag first inflator

Is DTC B0001-11 indicated?

YES

Go to step 3.

NO

Short to ground in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness. -7. Reconnect the negative cable to the 12 volt battery. -8. Clear the DTCs with the HDS. Clear DTCs -9. Turn the vehicle to the ON mode, then wait for 10 seconds. -10. Check for DTCs with the HDS. DTC Description DTC B0001-11 Short to ground in the driver's airbag first inflator Is DTC B0001-11 indicated? YES Go to step 4. NO Short to ground in the cable reel; replace the cable reel , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness.

-4. Remove the column covers .

-5. Disconnect cable reel connector B (4P) on the dashboard wire harness.

Courtesy of HONDA, U.S.A., INC.

-6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness.

-7. Reconnect the negative cable to the 12 volt battery.

-8. Clear the DTCs with the HDS.

Clear DTCs

-9. Turn the vehicle to the ON mode, then wait for 10 seconds.

-10. Check for DTCs with the HDS.

DTC Description | DTC

B0001-11 Short to ground in the driver's airbag first inflator

Is DTC B0001-11 indicated?

YES

Go to step 4.

NO

Short to ground in the cable reel; replace the cable reel , then clear the DTC.

- Shorted wire check (LA1+, LA1- lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Disconnect the following connector. SRS unit connector A (39P) -4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness. -5. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected Cable reel connector B (4P) (on the dashboard wire harness): disconnected SRS unit connector A (39P): disconnected Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J Test point 1 SRS simulator lead J black terminal Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there an open circuit, or at least 1 MΩ? YES The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness. NO Short to ground in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): disconnected
````

## Chunk 9055: DTC B0001-11

- Title: DTC B0001-11
- Source path: `pages\11671.html`
- Chunk ID: `chunk_a5cdfa422835`
- Images: `images\GHH412281.jpeg`, `images\GHH412282.jpeg`, `images\GHH412283.jpeg`, `images\GHH412284.jpeg`
- Duplicate sources: `pages\16819.html`

### Full Text

````text
C does not clear, replace the dashboard wire harness. NO Short to ground in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): disconnected

SRS unit connector A (39P): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J

Test point 1 | SRS simulator lead J black terminal

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there an open circuit, or at least 1 MΩ?

YES

The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness.

NO

Short to ground in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.
````

## Chunk 9056: DTC B0001-12

- Title: DTC B0001-12
- Source path: `pages\11672.html`
- Chunk ID: `chunk_78a5c5ee7909`
- Images: `images\GHH412285.jpeg`, `images\GHH412286.jpeg`, `images\GHH412287.jpeg`, `images\GHH412288.jpeg`
- Duplicate sources: `pages\16820.html`

### Full Text

````text
# DTC B0001-12

DTC B0001-12 : Short to Power in the Driver's Airbag First Inflator

Special Tools Required

- SRS Inflator Simulator 07SAZ-TB4011A

- SRS Simulator Lead J 070AZ-SNAA100

NOTE:

- Before doing this troubleshooting procedure, find out if the vehicle was in a collision. If so, verify that all the required components were replaced with new components of the correct part number and were properly installed .

- Before doing this troubleshooting procedure, review SRS Precautions and Procedures , General Troubleshooting Information , and 12 Volt Battery Terminal Disconnection and Reconnection .

DTC Description | DTC

B0001-12 Short to power in the driver's airbag first inflator

DTC (SRS)

- Problem verification -1. Clear the DTCs with the HDS. Clear DTCs -2. Turn the vehicle to the ON mode, then wait for 10 seconds. -3. Check for DTCs with the HDS. DTC Description DTC B0001-12 Short to power in the driver's airbag first inflator Is DTC B0001-12 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

-1. Clear the DTCs with the HDS.

Clear DTCs

-2. Turn the vehicle to the ON mode, then wait for 10 seconds.

-3. Check for DTCs with the HDS.

DTC Description | DTC

B0001-12 Short to power in the driver's airbag first inflator

Is DTC B0001-12 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

- Driver's airbag inflator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the driver's airbag . -4. Disconnect the following connector. Driver's airbag first inflator 2P connector (on the cable reel harness) NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown. Courtesy of HONDA, U.S.A., INC. -5. Connect terminals A and B with a jumper wire. Terminal A Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness) Terminal B Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness) Courtesy of HONDA, U.S.A., INC. -6. Reconnect the negative cable to the 12 volt battery. -7. Clear the DTCs with the HDS. Clear DTCs -8. Turn the vehicle to the ON mode, then wait for 10 seconds. -9. Check for DTCs with the HDS. DTC Description DTC B0001-12 Short to power in the driver's airbag first inflator Is DTC B0001-12 indicated? YES Go to step 3. NO Short to power in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the driver's airbag .

-4. Disconnect the following connector.

Driver's airbag first inflator 2P connector (on the cable reel harness)

NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown.

Courtesy of HONDA, U.S.A., INC.

-5. Connect terminals A and B with a jumper wire.

Terminal A | Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness)

Terminal B | Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness)

Courtesy of HONDA, U.S.A., INC.

-6. Reconnect the negative cable to the 12 volt battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-12 Short to power in the driver's airbag first inflator

Is DTC B0001-12 indicated?

YES

Go to step 3.

NO

Short to power in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6.
````

## Chunk 9057: DTC B0001-12

- Title: DTC B0001-12
- Source path: `pages\11672.html`
- Chunk ID: `chunk_ff1fd4438d8e`
- Images: `images\GHH412285.jpeg`, `images\GHH412286.jpeg`, `images\GHH412287.jpeg`, `images\GHH412288.jpeg`
- Duplicate sources: `pages\16820.html`

### Full Text

````text
t battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-12 Short to power in the driver's airbag first inflator

Is DTC B0001-12 indicated?

YES

Go to step 3.

NO

Short to power in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness. -7. Reconnect the negative cable to the 12 volt battery. -8. Clear the DTCs with the HDS. Clear DTCs -9. Turn the vehicle to the ON mode, then wait for 10 seconds. -10. Check for DTCs with the HDS. DTC Description DTC B0001-12 Short to power in the driver's airbag first inflator Is DTC B0001-12 indicated? YES Go to step 4. NO Short to power in the cable reel; replace the cable reel , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness.

-4. Remove the column covers .

-5. Disconnect cable reel connector B (4P) on the dashboard wire harness.

Courtesy of HONDA, U.S.A., INC.

-6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness.

-7. Reconnect the negative cable to the 12 volt battery.

-8. Clear the DTCs with the HDS.

Clear DTCs

-9. Turn the vehicle to the ON mode, then wait for 10 seconds.

-10. Check for DTCs with the HDS.

DTC Description | DTC

B0001-12 Short to power in the driver's airbag first inflator

Is DTC B0001-12 indicated?

YES

Go to step 4.

NO

Short to power in the cable reel; replace the cable reel , then clear the DTC.

- Shorted wire check (LA1+, LA1- lines to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Disconnect the following connector. SRS unit connector A (39P) -4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness. -5. Reconnect the negative cable to the 12 volt battery. -6. Turn the vehicle to the ON mode. -7. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected Cable reel connector B (4P) (on the dashboard wire harness): disconnected SRS unit connector A (39P): disconnected Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J Test point 1 SRS simulator lead J black terminal Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there 0.2 V or less? YES The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness. NO Short to power in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Reconnect the negative cable to the 12 volt battery.

-6. Turn the vehicle to the ON mode.

-7. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode
````

## Chunk 9058: DTC B0001-12

- Title: DTC B0001-12
- Source path: `pages\11672.html`
- Chunk ID: `chunk_2b2ad6ef7377`
- Images: `images\GHH412285.jpeg`, `images\GHH412286.jpeg`, `images\GHH412287.jpeg`, `images\GHH412288.jpeg`
- Duplicate sources: `pages\16820.html`

### Full Text

````text
e DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness. NO Short to power in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Reconnect the negative cable to the 12 volt battery.

-6. Turn the vehicle to the ON mode.

-7. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): disconnected

SRS unit connector A (39P): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J

Test point 1 | SRS simulator lead J black terminal

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there 0.2 V or less?

YES

The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness.

NO

Short to power in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.
````

## Chunk 9059: DTC B0001-13

- Title: DTC B0001-13
- Source path: `pages\11673.html`
- Chunk ID: `chunk_4e65dd29555f`
- Images: `images\GHH412289.jpeg`, `images\GHH412290.jpeg`, `images\GHH412291.jpeg`, `images\GHH412292.jpeg`
- Duplicate sources: `pages\16821.html`

### Full Text

````text
# DTC B0001-13

DTC B0001-13 : Open or Increased Resistance in the Driver's Airbag First Inflator

Special Tools Required

- SRS Inflator Simulator 07SAZ-TB4011A

- SRS Simulator Lead J 070AZ-SNAA100

NOTE:

- Before doing this troubleshooting procedure, find out if the vehicle was in a collision. If so, verify that all the required components were replaced with new components of the correct part number and were properly installed .

- Before doing this troubleshooting procedure, review SRS Precautions and Procedures , General Troubleshooting Information , and 12 Volt Battery Terminal Disconnection and Reconnection .

DTC Description | DTC

B0001-13 Open or increased resistance in the driver's airbag first inflator

DTC (SRS)

- Problem verification -1. Clear the DTCs with the HDS. Clear DTCs -2. Turn the vehicle to the ON mode, then wait for 10 seconds. -3. Check for DTCs with the HDS. DTC Description DTC B0001-13 Open or increased resistance in the driver's airbag first inflator Is DTC B0001-13 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

-1. Clear the DTCs with the HDS.

Clear DTCs

-2. Turn the vehicle to the ON mode, then wait for 10 seconds.

-3. Check for DTCs with the HDS.

DTC Description | DTC

B0001-13 Open or increased resistance in the driver's airbag first inflator

Is DTC B0001-13 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

- Driver's airbag inflator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the driver's airbag . -4. Disconnect the following connector. Driver's airbag first inflator 2P connector (on the cable reel harness) NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown. Courtesy of HONDA, U.S.A., INC. -5. Connect terminals A and B with a jumper wire. Terminal A Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness) Terminal B Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness) Courtesy of HONDA, U.S.A., INC. -6. Reconnect the negative cable to the 12 volt battery. -7. Clear the DTCs with the HDS. Clear DTCs -8. Turn the vehicle to the ON mode, then wait for 10 seconds. -9. Check for DTCs with the HDS. DTC Description DTC B0001-13 Open or increased resistance in the driver's airbag first inflator Is DTC B0001-13 indicated? YES Go to step 3. NO Open in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the driver's airbag .

-4. Disconnect the following connector.

Driver's airbag first inflator 2P connector (on the cable reel harness)

NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown.

Courtesy of HONDA, U.S.A., INC.

-5. Connect terminals A and B with a jumper wire.

Terminal A | Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness)

Terminal B | Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness)

Courtesy of HONDA, U.S.A., INC.

-6. Reconnect the negative cable to the 12 volt battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-13 Open or increased resistance in the driver's airbag first inflator

Is DTC B0001-13 indicated?

YES

Go to step 3.

NO

Open in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6.
````

## Chunk 9060: DTC B0001-13

- Title: DTC B0001-13
- Source path: `pages\11673.html`
- Chunk ID: `chunk_a2555c23786f`
- Images: `images\GHH412289.jpeg`, `images\GHH412290.jpeg`, `images\GHH412291.jpeg`, `images\GHH412292.jpeg`
- Duplicate sources: `pages\16821.html`

### Full Text

````text
ttery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-13 Open or increased resistance in the driver's airbag first inflator

Is DTC B0001-13 indicated?

YES

Go to step 3.

NO

Open in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness. Courtesy of HONDA, U.S.A., INC. -6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness. -7. Reconnect the negative cable to the 12 volt battery. -8. Clear the DTCs with the HDS. Clear DTCs -9. Turn the vehicle to the ON mode, then wait for 10 seconds. -10. Check for DTCs with the HDS. DTC Description DTC B0001-13 Open or increased resistance in the driver's airbag first inflator Is DTC B0001-13 indicated? YES Go to step 4. NO Open in the cable reel; replace the cable reel , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness.

-4. Remove the column covers .

-5. Disconnect cable reel connector B (4P) on the dashboard wire harness.

Courtesy of HONDA, U.S.A., INC.

-6. Connect the terminals of SRS simulator lead J to the SRS inflator simulator (2 Ω connectors), then connect SRS simulator lead J to cable reel connector B (4P) on the dashboard wire harness.

-7. Reconnect the negative cable to the 12 volt battery.

-8. Clear the DTCs with the HDS.

Clear DTCs

-9. Turn the vehicle to the ON mode, then wait for 10 seconds.

-10. Check for DTCs with the HDS.

DTC Description | DTC

B0001-13 Open or increased resistance in the driver's airbag first inflator

Is DTC B0001-13 indicated?

YES

Go to step 4.

NO

Open in the cable reel; replace the cable reel , then clear the DTC.

- Open wire check (LA1+, LA1- lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Disconnect the following connector. SRS unit connector A (39P) -4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness. -5. Measure the resistance of the test point. Test condition Vehicle OFF (LOCK) mode Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected Cable reel connector B (4P) (on the dashboard wire harness): disconnected SRS unit connector A (39P): disconnected Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J Test point SRS simulator lead J black terminal Courtesy of HONDA, U.S.A., INC. Is there 1.0 Ω or less? YES The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness. NO Open in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Measure the resistance of the test point.

Test condition | Vehicle OFF (LOCK) mode

Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): disconnected

SRS unit connector A (39P): disconnected
````

## Chunk 9061: DTC B0001-13

- Title: DTC B0001-13
- Source path: `pages\11673.html`
- Chunk ID: `chunk_1c7c3e704a9c`
- Images: `images\GHH412289.jpeg`, `images\GHH412290.jpeg`, `images\GHH412291.jpeg`, `images\GHH412292.jpeg`
- Duplicate sources: `pages\16821.html`

### Full Text

````text
lace the dashboard wire harness. NO Open in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Disconnect the following connector.

SRS unit connector A (39P)

-4. Disconnect the SRS inflator simulator from SRS simulator lead J. Do not disconnect SRS simulator lead J from cable reel connector B (4P) on the dashboard wire harness.

-5. Measure the resistance of the test point.

Test condition | Vehicle OFF (LOCK) mode

Driver's airbag first inflator 2P connector (on the cable reel harness): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): disconnected

SRS unit connector A (39P): disconnected

Cable reel connector B (4P) (on the dashboard wire harness): connected to SRS simulator lead J

Test point | SRS simulator lead J black terminal

Courtesy of HONDA, U.S.A., INC.

Is there 1.0 Ω or less?

YES

The LA1+ and LA1-wires are OK. Faulty SRS unit or poor connection at SRS unit connector A (39P) and the SRS unit. Check the connection; if the connection is OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting or replace the SRS unit . If the DTC does not clear, replace the dashboard wire harness.

NO

Open in the dashboard wire harness; replace the dashboard wire harness, then clear the DTC.
````

## Chunk 9062: DTC B0001-1A

- Title: DTC B0001-1A
- Source path: `pages\11674.html`
- Chunk ID: `chunk_e0daa1db267d`
- Images: `images\GHH412293.jpeg`, `images\GHH412294.jpeg`, `images\GHH412295.jpeg`, `images\GHH412296.jpeg`
- Duplicate sources: `pages\16822.html`

### Full Text

````text
# DTC B0001-1A

DTC B0001-1A : Decreased Resistance in the Driver's Airbag First Inflator

Special Tools Required

- SRS Inflator Simulator 07SAZ-TB4011A

- SRS Simulator Lead J 070AZ-SNAA100

- SRS Short Canceller 070AZ-SAA0100

NOTE:

- Before doing this troubleshooting procedure, find out if the vehicle was in a collision. If so, verify that all the required components were replaced with new components of the correct part number and were properly installed .

- Before doing this troubleshooting procedure, review SRS Precautions and Procedures , General Troubleshooting Information , and 12 Volt Battery Terminal Disconnection and Reconnection .

DTC Description | DTC

B0001-1A Decreased resistance in the driver's airbag first inflator

DTC (SRS)

- Problem verification -1. Clear the DTCs with the HDS. Clear DTCs -2. Turn the vehicle to the ON mode, then wait for 10 seconds. -3. Check for DTCs with the HDS. DTC Description DTC B0001-1A Decreased resistance in the driver's airbag first inflator Is DTC B0001-1A indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

-1. Clear the DTCs with the HDS.

Clear DTCs

-2. Turn the vehicle to the ON mode, then wait for 10 seconds.

-3. Check for DTCs with the HDS.

DTC Description | DTC

B0001-1A Decreased resistance in the driver's airbag first inflator

Is DTC B0001-1A indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Go to Troubleshooting Intermittent Failures. If another DTC is indicated, troubleshoot the DTC.

- Driver's airbag inflator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the driver's airbag . -4. Disconnect the following connector. Driver's airbag first inflator 2P connector (on the cable reel harness) NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown. Courtesy of HONDA, U.S.A., INC. -5. Connect terminals A and B with a jumper wire. Terminal A Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness) Terminal B Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness) Courtesy of HONDA, U.S.A., INC. -6. Reconnect the negative cable to the 12 volt battery. -7. Clear the DTCs with the HDS. Clear DTCs -8. Turn the vehicle to the ON mode, then wait for 10 seconds. -9. Check for DTCs with the HDS. DTC Description DTC B0001-1A Decreased resistance in the driver's airbag first inflator Is DTC B0001-1A indicated? YES Go to step 3. NO Short to another wire in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes.

-3. Remove the driver's airbag .

-4. Disconnect the following connector.

Driver's airbag first inflator 2P connector (on the cable reel harness)

NOTE: Make sure to work with the driver's airbag first inflator 2P connector (A) that has a guide tab (B) on the right side of the No. 2 terminal as shown.

Courtesy of HONDA, U.S.A., INC.

-5. Connect terminals A and B with a jumper wire.

Terminal A | Driver's airbag first inflator 2P connector No. 1 (on the cable reel harness)

Terminal B | Driver's airbag first inflator 2P connector No. 2 (on the cable reel harness)

Courtesy of HONDA, U.S.A., INC.

-6. Reconnect the negative cable to the 12 volt battery.

-7. Clear the DTCs with the HDS.

Clear DTCs

-8. Turn the vehicle to the ON mode, then wait for 10 seconds.

-9. Check for DTCs with the HDS.

DTC Description | DTC

B0001-1A Decreased resistance in the driver's airbag first inflator

Is DTC B0001-1A indicated?

YES

Go to step 3.

NO

Short to another wire in the driver's airbag first inflator; replace the driver's airbag , then clear the DTC.

- Cable reel check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the negative cable from the 12 volt battery, then wait at least 3 minutes. -3. Remove the jumper wire from the driver's airbag first inflator 2P connector on the cable reel harness. -4. Remove the column covers . -5. Disconnect cable reel connector B (4P) on the dashboard wire harness.
````

## Sources Used

- `pages\11317.html`
- `pages\11318.html`
- `pages\11319.html`
- `pages\11321.html`
- `pages\11322.html`
- `pages\11323.html`
- `pages\11324.html`
- `pages\11325.html`
- `pages\11326.html`
- `pages\11327.html`
- `pages\11328.html`
- `pages\11329.html`
- `pages\11330.html`
- `pages\11331.html`
- `pages\11332.html`
- `pages\11333.html`
- `pages\11334.html`
- `pages\11335.html`
- `pages\11336.html`
- `pages\11337.html`
- `pages\11338.html`
- `pages\11339.html`
- `pages\11340.html`
- `pages\11341.html`
- `pages\11342.html`
- `pages\11343.html`
- `pages\11344.html`
- `pages\11345.html`
- `pages\11346.html`
- `pages\11347.html`
- `pages\11348.html`
- `pages\11349.html`
- `pages\11350.html`
- `pages\11351.html`
- `pages\11352.html`
- `pages\11353.html`
- `pages\11354.html`
- `pages\11355.html`
- `pages\11356.html`
- `pages\11357.html`
- `pages\11359.html`
- `pages\11360.html`
- `pages\11362.html`
- `pages\11364.html`
- `pages\11366.html`
- `pages\11367.html`
- `pages\11369.html`
- `pages\11372.html`
- `pages\11373.html`
- `pages\11374.html`
- `pages\11375.html`
- `pages\11376.html`
- `pages\11378.html`
- `pages\11379.html`
- `pages\11380.html`
- `pages\11381.html`
- `pages\11382.html`
- `pages\11383.html`
- `pages\11384.html`
- `pages\11385.html`
- `pages\11386.html`
- `pages\11387.html`
- `pages\11388.html`
- `pages\11389.html`
- `pages\11390.html`
- `pages\11391.html`
- `pages\11392.html`
- `pages\11393.html`
- `pages\11394.html`
- `pages\11395.html`
- `pages\11396.html`
- `pages\11397.html`
- `pages\11398.html`
- `pages\11399.html`
- `pages\11400.html`
- `pages\11401.html`
- `pages\11402.html`
- `pages\11403.html`
- `pages\11404.html`
- `pages\11405.html`
- `pages\11406.html`
- `pages\11407.html`
- `pages\11408.html`
- `pages\11409.html`
- `pages\11410.html`
- `pages\11411.html`
- `pages\11412.html`
- `pages\11413.html`
- `pages\11414.html`
- `pages\11415.html`
- `pages\11416.html`
- `pages\11417.html`
- `pages\11418.html`
- `pages\11419.html`
- `pages\11420.html`
- `pages\11421.html`
- `pages\11422.html`
- `pages\11423.html`
- `pages\11424.html`
- `pages\11425.html`
- `pages\11426.html`
- `pages\11427.html`
- `pages\11428.html`
- `pages\11429.html`
- `pages\11430.html`
- `pages\11431.html`
- `pages\11432.html`
- `pages\11433.html`
- `pages\11434.html`
- `pages\11435.html`
- `pages\11436.html`
- `pages\11437.html`
- `pages\11438.html`
- `pages\11439.html`
- `pages\11440.html`
- `pages\11441.html`
- `pages\11442.html`
- `pages\11443.html`
- `pages\11444.html`
- `pages\11445.html`
- `pages\11446.html`
- `pages\11447.html`
- `pages\11448.html`
- `pages\11449.html`
- `pages\11450.html`
- `pages\11451.html`
- `pages\11452.html`
- `pages\11453.html`
- `pages\11454.html`
- `pages\11455.html`
- `pages\11456.html`
- `pages\11457.html`
- `pages\11458.html`
- `pages\11459.html`
- `pages\11460.html`
- `pages\11461.html`
- `pages\11462.html`
- `pages\11463.html`
- `pages\11464.html`
- `pages\11465.html`
- `pages\11466.html`
- `pages\11467.html`
- `pages\11468.html`
- `pages\11469.html`
- `pages\11470.html`
- `pages\11471.html`
- `pages\11472.html`
- `pages\11473.html`
- `pages\11474.html`
- `pages\11475.html`
- `pages\11476.html`
- `pages\11477.html`
- `pages\11478.html`
- `pages\11479.html`
- `pages\11480.html`
- `pages\11481.html`
- `pages\11483.html`
- `pages\11484.html`
- `pages\11485.html`
- `pages\11486.html`
- `pages\11487.html`
- `pages\11488.html`
- `pages\11489.html`
- `pages\11490.html`
- `pages\11491.html`
- `pages\11492.html`
- `pages\11493.html`
- `pages\11495.html`
- `pages\11496.html`
- `pages\11497.html`
- `pages\11498.html`
- `pages\11499.html`
- `pages\11500.html`
- `pages\11501.html`
- `pages\11502.html`
- `pages\11503.html`
- `pages\11504.html`
- `pages\11571.html`
- `pages\11572.html`
- `pages\11573.html`
- `pages\11574.html`
- `pages\11575.html`
- `pages\11576.html`
- `pages\11577.html`
- `pages\11578.html`
- `pages\11579.html`
- `pages\11580.html`
- `pages\11581.html`
- `pages\11582.html`
- `pages\11583.html`
- `pages\11584.html`
- `pages\11585.html`
- `pages\11586.html`
- `pages\11587.html`
- `pages\11588.html`
- `pages\11589.html`
- `pages\11590.html`
- `pages\11591.html`
- `pages\11592.html`
- `pages\11593.html`
- `pages\11594.html`
- `pages\11595.html`
- `pages\11596.html`
- `pages\11597.html`
- `pages\11598.html`
- `pages\11599.html`
- `pages\11600.html`
- `pages\11601.html`
- `pages\11602.html`
- `pages\11603.html`
- `pages\11604.html`
- `pages\11605.html`
- `pages\11606.html`
- `pages\11607.html`
- `pages\11608.html`
- `pages\11609.html`
- `pages\11610.html`
- `pages\11611.html`
- `pages\11612.html`
- `pages\11613.html`
- `pages\11614.html`
- `pages\11615.html`
- `pages\11616.html`
- `pages\11617.html`
- `pages\11618.html`
- `pages\11619.html`
- `pages\11620.html`
- `pages\11621.html`
- `pages\11622.html`
- `pages\11623.html`
- `pages\11624.html`
- `pages\11625.html`
- `pages\11626.html`
- `pages\11627.html`
- `pages\11628.html`
- `pages\11629.html`
- `pages\11630.html`
- `pages\11631.html`
- `pages\11632.html`
- `pages\11633.html`
- `pages\11634.html`
- `pages\11635.html`
- `pages\11636.html`
- `pages\11637.html`
- `pages\11638.html`
- `pages\11639.html`
- `pages\11640.html`
- `pages\11641.html`
- `pages\11642.html`
- `pages\11643.html`
- `pages\11644.html`
- `pages\11645.html`
- `pages\11646.html`
- `pages\11647.html`
- `pages\11648.html`
- `pages\11649.html`
- `pages\11650.html`
- `pages\11651.html`
- `pages\11652.html`
- `pages\11653.html`
- `pages\11654.html`
- `pages\11655.html`
- `pages\11656.html`
- `pages\11657.html`
- `pages\11658.html`
- `pages\11659.html`
- `pages\11660.html`
- `pages\11661.html`
- `pages\11662.html`
- `pages\11663.html`
- `pages\11664.html`
- `pages\11665.html`
- `pages\11666.html`
- `pages\11667.html`
- `pages\11668.html`
- `pages\11669.html`
- `pages\11670.html`
- `pages\11671.html`
- `pages\11672.html`
- `pages\11673.html`
- `pages\11674.html`
