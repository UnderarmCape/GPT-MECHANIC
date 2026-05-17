# Deep Research Manual Packet 0008

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0008
- Chunk count: 243
- Chunk range: 1414-1656
- Source count: 155
- Target maximum characters: 750000

## Manual Chunks

## Chunk 1414: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_0a5eaa08530c`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
disconnected Power window master switch 37P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 49. NO Go to step 50.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 49.

NO

Go to step 50.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch . NO Repair an open or high resistance in the wire or poor ground (G501).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Repair an open or high resistance in the wire or poor ground (G501).

- Open wire check (DR SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 20 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 20

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information indicator ON? YES Go to step 52. NO Go to step 54.

-1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 52.

NO

Go to step 54.

- Determine possible failure area (front passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Go to step 53.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.
````

## Chunk 1415: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_f25fe424380e`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
ck knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 52.

NO

Go to step 54.

- Determine possible failure area (front passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Go to step 53.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Go to step 53.

- Shorted wire check (AS SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's power window switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Front passenger's power window switch 37P connector: disconnected Test point 1 Front passenger's power window switch 37P connector No. 36 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's power window switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Front passenger's power window switch 37P connector: disconnected

Test point 1 | Front passenger's power window switch 37P connector No. 36

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Front passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 55. NO Go to step 56.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 55.

NO

Go to step 56.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK.
````

## Chunk 1416: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_c9adffc7ea09`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G505).

- Open wire check (AS SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Front passenger's power window switch 37P connector No. 36 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's power window switch 37P connector No. 36

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 1 -1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 58. NO Go to step 60.

-1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 58.

NO

Go to step 60.

- Determine possible failure area (left rear door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty left rear door lock knob switch; replace the left rear door latch . NO Go to step 59.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 59.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Disconnect the following connector. Body control module connector C (28P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector C (28P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1.
````

## Chunk 1417: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_d14326d883b6`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
ector: disconnected Test point 1 Body control module connector C (28P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector C (28P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Left rear door latch 10P connector No. 9 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 61. NO Go to step 62.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Left rear door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 61.

NO

Go to step 62.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected Test point 1 Left rear door latch 10P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G601).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected

Test point 1 | Left rear door latch 10P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G601).

- Open wire check (RR L SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 15 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 15

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 64. NO Go to step 66.

-1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 64.

NO

Go to step 66.

- Determine possible failure area (right rear door lock knob switch, others) -1. Disconnect the following connector.
````

## Chunk 1418: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_498ca913d209`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
r an open or high resistance in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 64. NO Go to step 66.

-1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 64.

NO

Go to step 66.

- Determine possible failure area (right rear door lock knob switch, others) -1. Disconnect the following connector. Right rear door latch 10P connector -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value OFF? YES Faulty right rear door lock knob switch; replace the right rear door latch . NO Go to step 65.

-1. Disconnect the following connector.

Right rear door latch 10P connector

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value OFF?

YES

Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Go to step 65.

- Shorted wire check (RR R SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Right rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Right rear door latch 10P connector No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 67. NO Go to step 68.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Right rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Right rear door latch 10P connector No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 67.

NO

Go to step 68.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected Test point 1 Right rear door latch 10P connector No. 9 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G602).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected

Test point 1 | Right rear door latch 10P connector No. 9

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1419: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (4-door)
- Source path: `pages\625.html`
- Chunk ID: `chunk_c016defac73c`
- Images: `images\GHH411630.jpeg`, `images\GHH411631.jpeg`, `images\GHH411632.jpeg`, `images\GHH411633.jpeg`, `images\GHH411634.jpeg`, `images\GHH411635.jpeg`, `images\GHH411636.jpeg`, `images\GHH411637.jpeg`, `images\GHH411638.jpeg`, `images\GHH411639.jpeg`, `images\GHH411640.jpeg`, `images\GHH411641.jpeg`, `images\GHH411642.jpeg`, `images\GHH411643.jpeg`, `images\GHH411644.jpeg`, `images\GHH411645.jpeg`, `images\GHH411646.jpeg`, `images\GHH411647.jpeg`, `images\GHH411648.jpeg`, `images\GHH411649.jpeg`, `images\GHH411650.jpeg`, `images\GHH411651.jpeg`, `images\GHH411652.jpeg`, `images\GHH411653.jpeg`, `images\GHH411654.jpeg`, `images\GHH411655.jpeg`, `images\GHH411656.jpeg`, `images\GHH411657.jpeg`, `images\GHH411658.jpeg`, `images\GHH411659.jpeg`, `images\GHH411660.jpeg`, `images\GHH411661.jpeg`, `images\GHH411662.jpeg`, `images\GHH411663.jpeg`, `images\GHH411664.jpeg`, `images\GHH411665.jpeg`, `images\GHH411666.jpeg`, `images\GHH411667.jpeg`, `images\GHH411668.jpeg`, `images\GHH411669.jpeg`, `images\GHH411670.jpeg`, `images\GHH411671.jpeg`, `images\GHH411672.jpeg`, `images\GHH411673.jpeg`, `images\GHH411674.jpeg`, `images\GHH411675.jpeg`, `images\GHH411676.jpeg`, `images\GHH411677.jpeg`, `images\GHH411678.jpeg`, `images\GHH411679.jpeg`, `images\GHH411680.jpeg`, `images\GHH411681.jpeg`, `images\GHH411682.jpeg`
- Duplicate sources: `pages\2667.html`, `pages\26315.html`, `pages\14316.html`

### Full Text

````text
e. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected Test point 1 Right rear door latch 10P connector No. 9 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G602).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected

Test point 1 | Right rear door latch 10P connector No. 9

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G602).

- Open wire check (RR R SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 16 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 16

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .
````

## Chunk 1420: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_e93ae05eaebe`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

NOTE:

- Before testing, make sure the No. A1-5 (30 A) *2, No. A2-2 (30 A) *2/(50 A) *1, and No. A18 (10 A) fuses in the under-hood fuse/relay box are OK.

- Check if Auto Door Unlock feature selected OFF, under MID customized settings for each remote: Driver 1 and 2. Make sure to test operation of each Auto Door Unlock setting to check function.

Make sure to test operation of each Auto Door Unlock setting to check function.

- Before testing, make sure the No. B8 (15 A) *3/(20 A) *4, No. B9 (10 A), No. B12 (10 A), No. B13 (10 A), No. B15 (20 A), No. B16 (20 A), No. B25 (10 A), No. B26 (10 A), No. B28 (20 A), No. B38 (10 A), and No. B39 (10 A) fuses in the under-dash fuse/relay box are OK.

- There are two pairs of fuses in the same circuit (No. B25 and No. B39 fuses, No. B12 and No. B26 fuses, No. B13 and No. B38 fuses, No. B38 and No. B39 fuses). If one fuse is blown, make sure to check the other fuse in the same circuit. If necessary, replace the blown fuse(s). *1: Without keyless access *2: With keyless access *3: Except K20C1 engine *4: K20C1 engine

*1: Without keyless access

*2: With keyless access

*3: Except K20C1 engine

*4: K20C1 engine

- Abnormal circuit check 1 -1. Connect the HDS to the data link connector (DLC) . -2. Select DOOR LOCKS from the BODY ELECTRICAL SYSTEM SELECT menu with the HDS, and enter FUNCTIONAL TESTS. BODY ELECTRICAL - DOOR LOCKS - Functional Tests - Inspection -3. Select UNLOCK ALL DOORS with the HDS. Do the door lock actuators work normally? YES Go to step 27. NO: Driver's door lock circuit Driver's door lock circuit: go to step 2. NO: Front passenger's door lock circuit Front passenger's door lock circuit: go to step 9. NO: Left rear door lock circuit Left rear door lock circuit: go to step 15. NO: Right rear door lock circuit Right rear door lock circuit: go to step 21.

-1. Connect the HDS to the data link connector (DLC) .

-2. Select DOOR LOCKS from the BODY ELECTRICAL SYSTEM SELECT menu with the HDS, and enter FUNCTIONAL TESTS.

BODY ELECTRICAL - DOOR LOCKS - Functional Tests - Inspection

-3. Select UNLOCK ALL DOORS with the HDS.

Do the door lock actuators work normally?

YES

Go to step 27.

NO: Driver's door lock circuit

Driver's door lock circuit: go to step 2.

NO: Front passenger's door lock circuit

Front passenger's door lock circuit: go to step 9.

NO: Left rear door lock circuit

Left rear door lock circuit: go to step 15.

NO: Right rear door lock circuit

Right rear door lock circuit: go to step 21.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 3. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B F/BOX MAIN wire is OK. Go to step 3.

NO

Repair an open or high resistance in the wire.

- Open wire check (GND line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Test point 1 Under-dash fuse/relay box connector C (27P) No. 7 Test point 2 Body ground Test point 1 Under-dash fuse/relay box connector E (18P) No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 4. NO Repair an open or high resistance in the ground wire or poor ground (G305, G501).

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P)

-2. Check for continuity between test points 1 and 2.
````

## Chunk 1421: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_d7e1521e1f63`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
ox connector E (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Test point 1 Under-dash fuse/relay box connector C (27P) No. 7 Test point 2 Body ground Test point 1 Under-dash fuse/relay box connector E (18P) No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 4. NO Repair an open or high resistance in the ground wire or poor ground (G305, G501).

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 7

Test point 2 | Body ground

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 4.

NO

Repair an open or high resistance in the ground wire or poor ground (G305, G501).

- Determine possible failure area (driver's door lock actuator, others) -1. Disconnect the following connector. Driver's door latch 10P connector -2. Test the door lock actuator . Is the door lock actuator OK? YES Go to step 5. NO Faulty door lock actuator; replace the driver's door latch .

-1. Disconnect the following connector.

Driver's door latch 10P connector

-2. Test the door lock actuator .

Is the door lock actuator OK?

YES

Go to step 5.

NO

Faulty door lock actuator; replace the driver's door latch .

- Open wire check (DR DOOR UNLOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Driver's door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector E (18P) No. 16 Test point 2 Driver's door latch 10P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DR DOOR UNLOCK wire is OK. Go to step 6. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 16

Test point 2 | Driver's door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DR DOOR UNLOCK wire is OK. Go to step 6.

NO

Repair an open or high resistance in the wire.

- Open wire check (DR DOOR LOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Driver's door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector E (18P) No. 15 Test point 2 Driver's door latch 10P connector No. 4 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES: Without keyless access system The DR DOOR LOCK wire is OK. Go to step 7. YES: With keyless access system The DR DOOR LOCK wire is OK. Go to step 8. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 15

Test point 2 | Driver's door latch 10P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES: Without keyless access system

The DR DOOR LOCK wire is OK. Go to step 7.

YES: With keyless access system

The DR DOOR LOCK wire is OK. Go to step 8.

NO

Repair an open or high resistance in the wire.

- Open wire check (DR DOOR UNLOCK RELAY CL- line) -1.
````

## Chunk 1422: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_a4c93744e589`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
Go to step 8. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 15

Test point 2 | Driver's door latch 10P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES: Without keyless access system

The DR DOOR LOCK wire is OK. Go to step 7.

YES: With keyless access system

The DR DOOR LOCK wire is OK. Go to step 8.

NO

Repair an open or high resistance in the wire.

- Open wire check (DR DOOR UNLOCK RELAY CL- line) -1. Disconnect the following connectors. Body control module connector B (36P) Under-dash fuse/relay box connector G (20P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector G (20P): disconnected Body control module connector B (36P): disconnected Driver's door latch 10P connector: disconnected Test point 1 Body control module connector B (36P) No. 31 Test point 2 Under-dash fuse/relay box connector G (20P) No. 8 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DR DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module . NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Body control module connector B (36P) Under-dash fuse/relay box connector G (20P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector G (20P): disconnected Body control module connector B (36P): disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 31

Test point 2 | Under-dash fuse/relay box connector G (20P) No. 8

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DR DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (DR DOOR UNLOCK RELAY CL- line) -1. Disconnect the following connectors. Body control module connector B (36P) Under-dash fuse/relay box connector G (20P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector G (20P): disconnected Body control module connector B (36P): disconnected Driver's door latch 10P connector: disconnected Test point 1 Body control module connector B (36P) No. 31 Test point 2 Under-dash fuse/relay box connector G (20P) No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DR DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module . NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Body control module connector B (36P) Under-dash fuse/relay box connector G (20P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector G (20P): disconnected Body control module connector B (36P): disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 31

Test point 2 | Under-dash fuse/relay box connector G (20P) No. 9

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DR DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 10. NO Repair an open or high resistance in the wire.

-1.
````

## Chunk 1423: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_9849cbd4887b`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
sconnected Driver's door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 31

Test point 2 | Under-dash fuse/relay box connector G (20P) No. 9

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DR DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 10. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B F/BOX MAIN wire is OK. Go to step 10.

NO

Repair an open or high resistance in the wire.

- Open wire check (GND line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Test point 1 Under-dash fuse/relay box connector C (27P) No. 7 Test point 2 Body ground Test point 1 Under-dash fuse/relay box connector E (18P) No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 11. NO Repair an open or high resistance in the ground wire or poor ground (G305, G501).

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 7

Test point 2 | Body ground

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 11.

NO

Repair an open or high resistance in the ground wire or poor ground (G305, G501).

- Determine possible failure area (front passenger's door lock actuator, others) -1. Disconnect the following connector. Front passenger's door latch 10P connector -2. Test the door lock actuator . Is the door lock actuator OK? YES Go to step 12. NO Faulty door lock actuator; replace the front passenger's door latch .

-1. Disconnect the following connector.

Front passenger's door latch 10P connector

-2. Test the door lock actuator .

Is the door lock actuator OK?

YES

Go to step 12.

NO

Faulty door lock actuator; replace the front passenger's door latch .

- Open wire check (R SIDE DOOR UNLOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Front passenger's door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector E (18P) No. 9 Test point 2 Front passenger's door latch 10P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The R SIDE DOOR UNLOCK wire is OK. Go to step 13. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Front passenger's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 9

Test point 2 | Front passenger's door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR UNLOCK wire is OK. Go to step 13.

NO

Repair an open or high resistance in the wire.
````

## Chunk 1424: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_97a54b4748d8`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
nnector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The R SIDE DOOR UNLOCK wire is OK. Go to step 13. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Front passenger's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 9

Test point 2 | Front passenger's door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR UNLOCK wire is OK. Go to step 13.

NO

Repair an open or high resistance in the wire.

- Open wire check (R SIDE DOOR LOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Front passenger's door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector E (18P) No. 18 Test point 2 Front passenger's door latch 10P connector No. 4 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The R SIDE DOOR LOCK wire is OK. Go to step 14. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Front passenger's door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 18

Test point 2 | Front passenger's door latch 10P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR LOCK wire is OK. Go to step 14.

NO

Repair an open or high resistance in the wire.

- Open wire check (DOOR UNLOCK RELAY CL- line) -1. Disconnect the following connectors. Body control module connector B (36P) Under-dash fuse/relay box connector F (12P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Front passenger's door latch 10P connector: disconnected Test point 1 Body control module connector B (36P) No. 32 Test point 2 Under-dash fuse/relay box connector F (12P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module . NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Body control module connector B (36P) Under-dash fuse/relay box connector F (12P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Front passenger's door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 32

Test point 2 | Under-dash fuse/relay box connector F (12P) No. 5

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 16. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B F/BOX MAIN wire is OK. Go to step 16.

NO
````

## Chunk 1425: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_98b4ee943906`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
gh resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 16. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B F/BOX MAIN wire is OK. Go to step 16.

NO

Repair an open or high resistance in the wire.

- Open wire check (GND line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Test point 1 Under-dash fuse/relay box connector C (27P) No. 7 Test point 2 Body ground Test point 1 Under-dash fuse/relay box connector E (18P) No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 17. NO Repair an open or high resistance in the ground wire or poor ground (G305, G501).

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 7

Test point 2 | Body ground

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 17.

NO

Repair an open or high resistance in the ground wire or poor ground (G305, G501).

- Determine possible failure area (left rear door lock actuator, others) -1. Disconnect the following connector. Left rear door latch 10P connector -2. Test the door lock actuator . Is the door lock actuator OK? YES Go to step 18. NO Faulty door lock actuator; replace the left rear door latch .

-1. Disconnect the following connector.

Left rear door latch 10P connector

-2. Test the door lock actuator .

Is the door lock actuator OK?

YES

Go to step 18.

NO

Faulty door lock actuator; replace the left rear door latch .

- Open wire check (L SIDE DOOR UNLOCK line) -1. Disconnect the following connector. Under-dash fuse/relay box connector B (22P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector B (22P) No. 16 Test point 2 Left rear door latch 10P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The L SIDE DOOR UNLOCK wire is OK. Go to step 19. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connector.

Under-dash fuse/relay box connector B (22P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 16

Test point 2 | Left rear door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The L SIDE DOOR UNLOCK wire is OK. Go to step 19.

NO

Repair an open or high resistance in the wire.

- Open wire check (L SIDE DOOR LOCK line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 1426: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_78dcb2c91191`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
llowing connector.

Under-dash fuse/relay box connector B (22P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 16

Test point 2 | Left rear door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The L SIDE DOOR UNLOCK wire is OK. Go to step 19.

NO

Repair an open or high resistance in the wire.

- Open wire check (L SIDE DOOR LOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector B (22P) No. 18 Test point 2 Left rear door latch 10P connector No. 4 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The L SIDE DOOR LOCK wire is OK. Go to step 20. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 18

Test point 2 | Left rear door latch 10P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The L SIDE DOOR LOCK wire is OK. Go to step 20.

NO

Repair an open or high resistance in the wire.

- Open wire check (DOOR UNLOCK RELAY CL- line) -1. Disconnect the following connectors. Body control module connector B (36P) Under-dash fuse/relay box connector F (12P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Body control module connector B (36P) No. 32 Test point 2 Under-dash fuse/relay box connector F (12P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module . NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Body control module connector B (36P) Under-dash fuse/relay box connector F (12P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 32

Test point 2 | Under-dash fuse/relay box connector F (12P) No. 5

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 22. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES
````

## Chunk 1427: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_0aeb2e995752`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
he body control module .

NO

Repair an open or high resistance in the wire.

- Open wire check (+B F/BOX MAIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Test point 1 Under-dash fuse/relay box connector C (27P) No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B F/BOX MAIN wire is OK. Go to step 22. NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B F/BOX MAIN wire is OK. Go to step 22.

NO

Repair an open or high resistance in the wire.

- Open wire check (GND line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Test point 1 Under-dash fuse/relay box connector C (27P) No. 7 Test point 2 Body ground Test point 1 Under-dash fuse/relay box connector E (18P) No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 23. NO Repair an open or high resistance in the ground wire or poor ground (G305, G501).

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P) Under-dash fuse/relay box connector E (18P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected

Test point 1 | Under-dash fuse/relay box connector C (27P) No. 7

Test point 2 | Body ground

Test point 1 | Under-dash fuse/relay box connector E (18P) No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 23.

NO

Repair an open or high resistance in the ground wire or poor ground (G305, G501).

- Determine possible failure area (right rear door lock actuator, others) -1. Disconnect the following connector. Right rear door latch 10P connector -2. Test the door lock actuator . Is the door lock actuator OK? YES Go to step 24. NO Faulty door lock actuator; replace the right rear door latch .

-1. Disconnect the following connector.

Right rear door latch 10P connector

-2. Test the door lock actuator .

Is the door lock actuator OK?

YES

Go to step 24.

NO

Faulty door lock actuator; replace the right rear door latch .

- Open wire check (R SIDE DOOR UNLOCK line) -1. Disconnect the following connector. Under-dash fuse/relay box connector B (22P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector B (22P) No. 12 Test point 2 Right rear door latch 10P connector No. 1 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The R SIDE DOOR UNLOCK wire is OK. Go to step 25. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connector.

Under-dash fuse/relay box connector B (22P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 12

Test point 2 | Right rear door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR UNLOCK wire is OK. Go to step 25.

NO

Repair an open or high resistance in the wire.

- Open wire check (R SIDE DOOR LOCK line) -1.
````

## Chunk 1428: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_4208c511f0ab`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
h resistance in the wire.

-1. Disconnect the following connector.

Under-dash fuse/relay box connector B (22P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 12

Test point 2 | Right rear door latch 10P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR UNLOCK wire is OK. Go to step 25.

NO

Repair an open or high resistance in the wire.

- Open wire check (R SIDE DOOR LOCK line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Under-dash fuse/relay box connector B (22P) No. 1 Test point 2 Right rear door latch 10P connector No. 4 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The R SIDE DOOR LOCK wire is OK. Go to step 26. NO Repair an open or high resistance in the wire.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Under-dash fuse/relay box connector B (22P) No. 1

Test point 2 | Right rear door latch 10P connector No. 4

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The R SIDE DOOR LOCK wire is OK. Go to step 26.

NO

Repair an open or high resistance in the wire.

- Open wire check (DOOR UNLOCK RELAY CL- line) -1. Disconnect the following connectors. Body control module connector B (36P) Under-dash fuse/relay box connector F (12P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Body control module connector B (36P) No. 32 Test point 2 Under-dash fuse/relay box connector F (12P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module . NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Body control module connector B (36P) Under-dash fuse/relay box connector F (12P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Under-dash fuse/relay box connector B (22P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector E (18P): disconnected Under-dash fuse/relay box connector F (12P): disconnected Body control module connector B (36P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Body control module connector B (36P) No. 32

Test point 2 | Under-dash fuse/relay box connector F (12P) No. 5

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Abnormal circuit check 2 -1. Check the parameter(s) below with the HDS when each switch is operating. Door Multiplex Control Unit Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Passenger's Door Lock Knob Switch (UNLOCK) Body Control Module Signal Current conditions Value Unit A/T Gear Position Switch (P) Driver's Door Switch Driver's Rear Door Lock Knob Switch (UNLOCK) Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is each switch information OK? YES Replace the body control module . NO: Transmission range switch P position circuit troubleshooting Transmission range switch P position circuit troubleshooting: go to step 28.
````

## Chunk 1429: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_7334c6b0c881`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
ntinuity?

YES

The DOOR UNLOCK RELAY CL- wire is OK. Replace the body control module .

NO

Repair an open or high resistance in the wire.

- Abnormal circuit check 2 -1. Check the parameter(s) below with the HDS when each switch is operating. Door Multiplex Control Unit Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Passenger's Door Lock Knob Switch (UNLOCK) Body Control Module Signal Current conditions Value Unit A/T Gear Position Switch (P) Driver's Door Switch Driver's Rear Door Lock Knob Switch (UNLOCK) Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is each switch information OK? YES Replace the body control module . NO: Transmission range switch P position circuit troubleshooting Transmission range switch P position circuit troubleshooting: go to step 28. NO Driver's door switch circuit troubleshooting: go to step 34. NO Driver's door lock knob switch circuit troubleshooting: go to step 36. NO Front passenger's door lock knob switch circuit troubleshooting: go to step 42. NO Left rear door lock knob switch circuit troubleshooting: go to step 48. NO Right rear door lock knob switch circuit troubleshooting: go to step 54.

-1. Check the parameter(s) below with the HDS when each switch is operating.

Door Multiplex Control Unit

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Passenger's Door Lock Knob Switch (UNLOCK)

Body Control Module

Signal | Current conditions

Value | Unit

A/T Gear Position Switch (P)

Driver's Door Switch

Driver's Rear Door Lock Knob Switch (UNLOCK)

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is each switch information OK?

YES

Replace the body control module .

NO: Transmission range switch P position circuit troubleshooting

Transmission range switch P position circuit troubleshooting: go to step 28.

NO

Driver's door switch circuit troubleshooting: go to step 34.

NO

Driver's door lock knob switch circuit troubleshooting: go to step 36.

NO

Front passenger's door lock knob switch circuit troubleshooting: go to step 42.

NO

Left rear door lock knob switch circuit troubleshooting: go to step 48.

NO

Right rear door lock knob switch circuit troubleshooting: go to step 54.

- Keyless/power door locks/security system check 1 -1. With the shift position in P position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit A/T Gear Position Switch (P) Is information value ON? YES Go to step 29. NO Go to step 31.

-1. With the shift position in P position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

A/T Gear Position Switch (P)

Is information value ON?

YES

Go to step 29.

NO

Go to step 31.

- Determine possible failure area (Transmission range switch, others) -1. Disconnect the following connector. Transmission range switch 10P connector -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit A/T Gear Position Switch (P) Is information value OFF? YES Replace the transmission range switch . NO Go to step 30.

-1. Disconnect the following connector.

Transmission range switch 10P connector

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

A/T Gear Position Switch (P)

Is information value OFF?

YES

Replace the transmission range switch .

NO

Go to step 30.

- Shorted wire check (ATP-P line) -1. Disconnect the following connector. TCM 50P connector Body control module connector C (28P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected TCM 50P connector: disconnected Body control module connector C (28P): disconnected Test point 1 Body control module connector C (28P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The ATP-P wire is OK. Replace the body control module .

-1. Disconnect the following connector.

TCM 50P connector Body control module connector C (28P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected TCM 50P connector: disconnected Body control module connector C (28P): disconnected

Test point 1 | Body control module connector C (28P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The ATP-P wire is OK. Replace the body control module .
````

## Chunk 1430: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_bcec14acafde`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
control module connector C (28P): disconnected Test point 1 Body control module connector C (28P) No. 1 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The ATP-P wire is OK. Replace the body control module .

-1. Disconnect the following connector.

TCM 50P connector Body control module connector C (28P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected TCM 50P connector: disconnected Body control module connector C (28P): disconnected

Test point 1 | Body control module connector C (28P) No. 1

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The ATP-P wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Disconnect the following connector. Transmission range switch 10P connector -2. Connect terminals A and B with a jumper wire. Terminal A Transmission range switch 10P connector No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit A/T Gear Position Switch (P) Is information value ON? YES Go to step 32. NO Go to step 33.

-1. Disconnect the following connector.

Transmission range switch 10P connector

-2. Connect terminals A and B with a jumper wire.

Terminal A | Transmission range switch 10P connector No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

A/T Gear Position Switch (P)

Is information value ON?

YES

Go to step 32.

NO

Go to step 33.

- Open wire check (PG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PG1 wire is OK. Replace the transmission range switch . NO Repair an open or high resistance in the wire or poor ground (G201).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PG1 wire is OK. Replace the transmission range switch .

NO

Repair an open or high resistance in the wire or poor ground (G201).

- Open wire check (ATP-P line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 1 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit A/T Gear Position Switch (P) Is information value ON? YES Repair an open or high resistance in the wire. NO The ATP-P wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 1

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

A/T Gear Position Switch (P)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The ATP-P wire is OK. Replace the body control module .

- Driver's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 35. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1431: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_68d7af180cea`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 35. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 35.

NO

Replace the driver's door switch.

- Shorted wire check (FL DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 37. NO Go to step 39.

-1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 37.

NO

Go to step 39.

- Determine possible failure area (driver's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty driver's door lock knob switch; replace the driver's door latch . NO Go to step 38.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Go to step 38.

- Shorted wire check (DR SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Power window master switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Power window master switch 37P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Power window master switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Power window master switch 37P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK.
````

## Chunk 1432: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_3a89a4dfd57d`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
window master switch 37P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Power window master switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Power window master switch 37P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 40. NO Go to step 41.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 40.

NO

Go to step 41.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch . NO Repair an open or high resistance in the wire or poor ground (G501).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Repair an open or high resistance in the wire or poor ground (G501).

- Open wire check (DR SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 20 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 20

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information indicator ON? YES Go to step 43. NO Go to step 45.

-1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 43.

NO

Go to step 45.
````

## Chunk 1433: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_22c3d15cc904`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
s

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information indicator ON? YES Go to step 43. NO Go to step 45.

-1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 43.

NO

Go to step 45.

- Determine possible failure area (front passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Go to step 44.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Go to step 44.

- Shorted wire check (AS SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's power window switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Front passenger's power window switch 37P connector: disconnected Test point 1 Front passenger's power window switch 37P connector No. 36 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's power window switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Front passenger's power window switch 37P connector: disconnected

Test point 1 | Front passenger's power window switch 37P connector No. 36

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Front passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 46. NO Go to step 47.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 46.

NO

Go to step 47.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK.
````

## Chunk 1434: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_61e9f1309e80`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
onnector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 46.

NO

Go to step 47.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G505).

- Open wire check (AS SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Front passenger's power window switch 37P connector No. 36 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's power window switch 37P connector No. 36

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 1 -1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 49. NO Go to step 51.

-1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 49.

NO

Go to step 51.

- Determine possible failure area (left rear door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty left rear door lock knob switch; replace the left rear door latch . NO Go to step 50.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 50.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Disconnect the following connector. Body control module connector C (28P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1.
````

## Chunk 1435: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_d0145bab38a1`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
eck the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 50.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Disconnect the following connector. Body control module connector C (28P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector C (28P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Left rear door latch 10P connector No. 9 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 52. NO Go to step 53.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Left rear door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 52.

NO

Go to step 53.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected Test point 1 Left rear door latch 10P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G601).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected

Test point 1 | Left rear door latch 10P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G601).

- Open wire check (RR L SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 15 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 15

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1.
````

## Chunk 1436: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_771f81e297e6`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 15

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 55. NO Go to step 57.

-1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 55.

NO

Go to step 57.

- Determine possible failure area (right rear door lock knob switch, others) -1. Disconnect the following connector. Right rear door latch 10P connector -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value OFF? YES Faulty right rear door lock knob switch; replace the right rear door latch . NO Go to step 56.

-1. Disconnect the following connector.

Right rear door latch 10P connector

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value OFF?

YES

Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Go to step 56.

- Shorted wire check (RR R SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Right rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Right rear door latch 10P connector No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 58. NO Go to step 59.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Right rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Right rear door latch 10P connector No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 58.

NO

Go to step 59.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2.
````

## Chunk 1437: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - AUTO DOOR UNLOCK does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\626.html`
- Chunk ID: `chunk_7da61225ae9e`
- Images: `images\GHH411683.jpeg`, `images\GHH411684.jpeg`, `images\GHH411685.jpeg`, `images\GHH411686.jpeg`, `images\GHH411687.jpeg`, `images\GHH411688.jpeg`, `images\GHH411689.jpeg`, `images\GHH411690.jpeg`, `images\GHH411691.jpeg`, `images\GHH411692.jpeg`, `images\GHH411693.jpeg`, `images\GHH411694.jpeg`, `images\GHH411695.jpeg`, `images\GHH411696.jpeg`, `images\GHH411697.jpeg`, `images\GHH411698.jpeg`, `images\GHH411699.jpeg`, `images\GHH411700.jpeg`, `images\GHH411701.jpeg`, `images\GHH411702.jpeg`, `images\GHH411703.jpeg`, `images\GHH411704.jpeg`, `images\GHH411705.jpeg`, `images\GHH411706.jpeg`, `images\GHH411707.jpeg`, `images\GHH411708.jpeg`, `images\GHH411709.jpeg`, `images\GHH411710.jpeg`, `images\GHH411711.jpeg`, `images\GHH411712.jpeg`, `images\GHH411713.jpeg`, `images\GHH411714.jpeg`, `images\GHH411715.jpeg`, `images\GHH411716.jpeg`, `images\GHH411717.jpeg`, `images\GHH411718.jpeg`, `images\GHH411719.jpeg`, `images\GHH411720.jpeg`, `images\GHH411721.jpeg`, `images\GHH411722.jpeg`, `images\GHH411723.jpeg`, `images\GHH411724.jpeg`, `images\GHH411725.jpeg`, `images\GHH411726.jpeg`
- Duplicate sources: `pages\2668.html`, `pages\26316.html`, `pages\14317.html`

### Full Text

````text
HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 58. NO Go to step 59.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Right rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Right rear door latch 10P connector No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 58.

NO

Go to step 59.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected Test point 1 Right rear door latch 10P connector No. 9 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G602).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected

Test point 1 | Right rear door latch 10P connector No. 9

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G602).

- Open wire check (RR R SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 16 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 16

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .
````

## Chunk 1438: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\627.html`
- Chunk ID: `chunk_254ff5ea1779`
- Images: `images\GHH411727.jpeg`, `images\GHH411728.jpeg`, `images\GHH411729.jpeg`, `images\GHH411730.jpeg`
- Duplicate sources: `pages\2669.html`, `pages\26317.html`, `pages\14318.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Determine possible failure area (body control module, others) -1. Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module. Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed? YES Replace the body control module . NO Go to step 2.

-1. Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module.

Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed?

YES

Replace the body control module .

NO

Go to step 2.

- Open wire check (FL DOOR SW, FR DOOR SW, TRUNK SW lines) -1. Disconnect the following connectors. Body control module connector D (40P) Each door switch 1P connector Trunk lid latch 3P connector -2. Check for continuity between test points 1 and 2 respectively. Driver's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Driver's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Passenger's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 23 Test point 2 Passenger's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Trunk lid latch switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Trunk lid latch 3P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FL DOOR SW and FR DOOR SW wires are OK. Replace the bad door switch. YES The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3. NO Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

-1. Disconnect the following connectors.

Body control module connector D (40P) Each door switch 1P connector Trunk lid latch 3P connector

-2. Check for continuity between test points 1 and 2 respectively.

Driver's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Driver's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Passenger's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 23

Test point 2 | Passenger's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Trunk lid latch switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Trunk lid latch 3P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FL DOOR SW and FR DOOR SW wires are OK. Replace the bad door switch.

YES

The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3.

NO

Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

- Open wire check (GND line) -1.
````

## Chunk 1439: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\627.html`
- Chunk ID: `chunk_ece66c259fa2`
- Images: `images\GHH411727.jpeg`, `images\GHH411728.jpeg`, `images\GHH411729.jpeg`, `images\GHH411730.jpeg`
- Duplicate sources: `pages\2669.html`, `pages\26317.html`, `pages\14318.html`

### Full Text

````text
) No. 23

Test point 2 | Passenger's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Trunk lid latch switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Trunk lid latch 3P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FL DOOR SW and FR DOOR SW wires are OK. Replace the bad door switch.

YES

The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3.

NO

Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Trunk lid latch 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch . NO Repair an open or high resistance in the ground wire or poor ground (G701).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Trunk lid latch 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G701).
````

## Chunk 1440: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)
- Source path: `pages\628.html`
- Chunk ID: `chunk_9b19a33f3412`
- Images: `images\GHH411731.jpeg`, `images\GHH411732.jpeg`, `images\GHH411733.jpeg`, `images\GHH411734.jpeg`, `images\GHH411735.jpeg`, `images\GHH411736.jpeg`
- Duplicate sources: `pages\2670.html`, `pages\26318.html`, `pages\14319.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Determine possible failure area (body control module, others) -1. Without moonroof: Turn the ceiling light switch to the MIDDLE position. -2. With moonroof: Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module. Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed? YES Replace the body control module . NO Go to step 2.

-1. Without moonroof: Turn the ceiling light switch to the MIDDLE position.

-2. With moonroof: Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module.

Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed?

YES

Replace the body control module .

NO

Go to step 2.

- Open wire check (FL DOOR SW, FR DOOR SW, RL DOOR SW, RR DOOR SW, TRUNK SW lines) -1. Disconnect the following connectors. Body control module connector D (40P) Each door switch 1P connector Trunk lid latch 3P connector -2. Check for continuity between test points 1 and 2 respectively. Driver's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Driver's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Front passenger's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 23 Test point 2 Front passenger's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Left rear door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 24 Test point 2 Left rear door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Right rear door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 28 Test point 2 Right rear door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Trunk lid latch switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Trunk lid latch 3P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FL DOOR SW, FR DOOR SW, RL DOOR SW, and RR DOOR SW wires are OK. Replace the bad door switch. YES The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3. NO Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

-1. Disconnect the following connectors.

Body control module connector D (40P) Each door switch 1P connector Trunk lid latch 3P connector

-2. Check for continuity between test points 1 and 2 respectively.

Driver's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Driver's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Front passenger's door switch
````

## Chunk 1441: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)
- Source path: `pages\628.html`
- Chunk ID: `chunk_8ec9c6d89884`
- Images: `images\GHH411731.jpeg`, `images\GHH411732.jpeg`, `images\GHH411733.jpeg`, `images\GHH411734.jpeg`, `images\GHH411735.jpeg`, `images\GHH411736.jpeg`
- Duplicate sources: `pages\2670.html`, `pages\26318.html`, `pages\14319.html`

### Full Text

````text
The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3. NO Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

-1. Disconnect the following connectors.

Body control module connector D (40P) Each door switch 1P connector Trunk lid latch 3P connector

-2. Check for continuity between test points 1 and 2 respectively.

Driver's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Driver's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Front passenger's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 23

Test point 2 | Front passenger's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Left rear door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 24

Test point 2 | Left rear door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Right rear door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 28

Test point 2 | Right rear door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Trunk lid latch switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Trunk lid latch 3P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FL DOOR SW, FR DOOR SW, RL DOOR SW, and RR DOOR SW wires are OK. Replace the bad door switch.

YES

The TRUNK SW wire is OK. Faulty trunk lid latch switch or GND line, go to step 3.

NO

Repair an open or high resistance in the wire between the body control module and the door switch/trunk lid latch switch.

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected Test point 1 Trunk lid latch 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch . NO Repair an open or high resistance in the ground wire or poor ground (G701).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Trunk lid latch 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G701).
````

## Chunk 1442: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\629.html`
- Chunk ID: `chunk_69a0e2331bea`
- Images: `images\GHH411737.jpeg`, `images\GHH411738.jpeg`, `images\GHH411739.jpeg`, `images\GHH411740.jpeg`, `images\GHH411741.jpeg`, `images\GHH411742.jpeg`
- Duplicate sources: `pages\2671.html`, `pages\26319.html`, `pages\14320.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Determine possible failure area (body control module, others) -1. Without moonroof: Turn the ceiling light switch to the MIDDLE position. -2. With moonroof: Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module. Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed? YES Replace the body control module . NO Go to step 2.

-1. Without moonroof: Turn the ceiling light switch to the MIDDLE position.

-2. With moonroof: Turn the interior light switch to the DOOR position and ceiling light switch to the MIDDLE position.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Watch the individual map lights, the ceiling light, and the door indicators on the gauge control module.

Do the individual map lights and door indicators come on when the door is open, and go off when the door is closed?

YES

Replace the body control module .

NO

Go to step 2.

- Open wire check (FL DOOR SW, FR DOOR SW, RL DOOR SW, RR DOOR SW, TRUNK SW lines) -1. Disconnect the following connectors. Body control module connector D (40P) Each door switch 1P connector Tailgate latch 4P connector -2. Check for continuity between test points 1 and 2 respectively. Driver's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Driver's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Front passenger's door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 23 Test point 2 Front passenger's door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Left rear door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 24 Test point 2 Left rear door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Right rear door switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 28 Test point 2 Right rear door switch 1P connector No. 1 Courtesy of HONDA, U.S.A., INC. Tailgate latch switch Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Tailgate latch 4P connector No. 1 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FL DOOR SW, FR DOOR SW, RL DOOR SW, and RR DOOR SW wires are OK. Replace the bad door switch. YES The TRUNK SW wire is OK. Faulty tailgate latch switch or GND line, go to step 3. NO Repair an open or high resistance in the wire between the body control module and the door switch/tailgate latch switch.

-1. Disconnect the following connectors.

Body control module connector D (40P) Each door switch 1P connector Tailgate latch 4P connector

-2. Check for continuity between test points 1 and 2 respectively.

Driver's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Driver's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Front passenger's door switch
````

## Chunk 1443: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\629.html`
- Chunk ID: `chunk_1b08006c1b09`
- Images: `images\GHH411737.jpeg`, `images\GHH411738.jpeg`, `images\GHH411739.jpeg`, `images\GHH411740.jpeg`, `images\GHH411741.jpeg`, `images\GHH411742.jpeg`
- Duplicate sources: `pages\2671.html`, `pages\26319.html`, `pages\14320.html`

### Full Text

````text
YES The TRUNK SW wire is OK. Faulty tailgate latch switch or GND line, go to step 3. NO Repair an open or high resistance in the wire between the body control module and the door switch/tailgate latch switch.

-1. Disconnect the following connectors.

Body control module connector D (40P) Each door switch 1P connector Tailgate latch 4P connector

-2. Check for continuity between test points 1 and 2 respectively.

Driver's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Driver's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Front passenger's door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 23

Test point 2 | Front passenger's door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Left rear door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 24

Test point 2 | Left rear door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Right rear door switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 28

Test point 2 | Right rear door switch 1P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Tailgate latch switch

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Tailgate latch 4P connector No. 1

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FL DOOR SW, FR DOOR SW, RL DOOR SW, and RR DOOR SW wires are OK. Replace the bad door switch.

YES

The TRUNK SW wire is OK. Faulty tailgate latch switch or GND line, go to step 3.

NO

Repair an open or high resistance in the wire between the body control module and the door switch/tailgate latch switch.

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected Test point 1 Tailgate latch 4P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty tailgate latch switch; replace the tailgate latch . NO Repair an open or high resistance in the ground wire or poor ground (G603).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Each door switch 1P connector: disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Tailgate latch 4P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty tailgate latch switch; replace the tailgate latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G603).
````

## Chunk 1444: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_a53490a6cc4b`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Switch information check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Door Multiplex Control Unit Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Passenger's Door Lock Knob Switch (UNLOCK) Driver's Door Key Cylinder Switch (LOCK) Body Control Module Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Driver's Door Switch Front Passenger's Door Switch Security Hood Switch Is each switch information value OK? YES Intermittent failure, the system is OK at this time. NG Trunk lid latch switch circuit troubleshooting: go to step 2. NG Hood latch switch circuit troubleshooting: go to step 8. NG Driver's door lock knob switch circuit troubleshooting: go to step 14. NG Passenger's door lock knob switch circuit troubleshooting: go to step 20. NG Driver's door switch circuit troubleshooting: go to step 26. NG Passenger's door switch circuit troubleshooting: go to step 31. NG Driver's door key cylinder switch circuit troubleshooting: go to step 36.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Door Multiplex Control Unit

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Passenger's Door Lock Knob Switch (UNLOCK)

Driver's Door Key Cylinder Switch (LOCK)

Body Control Module

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Driver's Door Switch

Front Passenger's Door Switch

Security Hood Switch

Is each switch information value OK?

YES

Intermittent failure, the system is OK at this time.

NG

Trunk lid latch switch circuit troubleshooting: go to step 2.

NG

Hood latch switch circuit troubleshooting: go to step 8.

NG

Driver's door lock knob switch circuit troubleshooting: go to step 14.

NG

Passenger's door lock knob switch circuit troubleshooting: go to step 20.

NG

Driver's door switch circuit troubleshooting: go to step 26.

NG

Passenger's door switch circuit troubleshooting: go to step 31.

NG

Driver's door key cylinder switch circuit troubleshooting: go to step 36.

- Keyless/power door locks/security system check 1 -1. With the trunk closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 3. NO Go to step 5.

-1. With the trunk closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (trunk lid latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Trunk lid latch 3P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value OFF? YES Faulty trunk lid latch switch; replace the trunk lid latch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Trunk lid latch 3P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value OFF?

YES

Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Go to step 4.

- Shorted wire check (TRUNK SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector D (40P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector D (40P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Body ground
````

## Chunk 1445: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_09fa724a37da`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector D (40P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Trunk lid latch 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A Trunk lid latch 3P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 6. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Trunk lid latch 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Trunk lid latch 3P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 6.

NO

Go to step 7.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Trunk lid latch 3P connector: disconnected Test point 1 Trunk lid latch 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch . NO Repair an open or high resistance in the ground wire or poor ground (G701).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Trunk lid latch 3P connector: disconnected

Test point 1 | Trunk lid latch 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G701).

- Open wire check (TRUNK SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 27 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 27

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the hood opened, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 9. NO Go to step 11.

-1. With the hood opened, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 9.

NO

Go to step 11.

- Determine possible failure area (hood latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Check the parameter(s) below with the HDS.
````

## Chunk 1446: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_ecd83fad6080`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
tion value ON?

YES

Repair an open or high resistance in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the hood opened, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 9. NO Go to step 11.

-1. With the hood opened, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 9.

NO

Go to step 11.

- Determine possible failure area (hood latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value ON? YES Faulty hood latch switch; replace the hood latch . NO Go to step 10.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value ON?

YES

Faulty hood latch switch; replace the hood latch .

NO

Go to step 10.

- Shorted wire check (HOOD SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected Test point 1 Body control module connector C (28P) No. 19 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 19

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A Hood latch switch 2P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 12. NO Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Hood latch switch 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 12.

NO

Go to step 13.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected Test point 1 Hood latch switch 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty hood latch switch; replace the hood latch . NO Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3). *1: L15B7 engine *2: K20C2 engine (type A) *3: K20C2 engine (type B)

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected

Test point 1 | Hood latch switch 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty hood latch switch; replace the hood latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3).

*1: L15B7 engine
````

## Chunk 1447: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_654296831a9f`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
there continuity? YES The GND wire is OK. Faulty hood latch switch; replace the hood latch . NO Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3). *1: L15B7 engine *2: K20C2 engine (type A) *3: K20C2 engine (type B)

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected

Test point 1 | Hood latch switch 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty hood latch switch; replace the hood latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3).

*1: L15B7 engine

*2: K20C2 engine (type A)

*3: K20C2 engine (type B)

- Open wire check (HOOD SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 19 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Repair an open or high resistance in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 19

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Repair an open or high resistance in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 15. NO Go to step 17.

-1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 15.

NO

Go to step 17.

- Determine possible failure area (driver's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty driver's door lock knob switch; replace the driver's door latch . NO Go to step 16.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Go to step 16.

- Shorted wire check (DR SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Power window master switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Power window master switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire.
````

## Chunk 1448: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_37cef320afdd`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
ster switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Power window master switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 18. NO Go to step 19.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 18.

NO

Go to step 19.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G501).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G501).

- Open wire check (DR SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 20 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 20

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1. With the passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 21. NO Go to step 23.

-1. With the passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 21.

NO

Go to step 23.

- Determine possible failure area (passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS.
````

## Chunk 1449: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_265d1a384492`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
ower door locks/security system check 1 -1. With the passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 21. NO Go to step 23.

-1. With the passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 21.

NO

Go to step 23.

- Determine possible failure area (passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty passenger's door lock knob switch; replace the passenger's door latch . NO Go to step 22.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Passenger's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty passenger's door lock knob switch; replace the passenger's door latch .

NO

Go to step 22.

- Shorted wire check (AS SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's power window switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Passenger's power window switch 37P connector: disconnected Passenger's door latch 10P connector: disconnected Test point 1 Passenger's power window switch 37P connector No. 36 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the passenger's power window switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Passenger's power window switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Passenger's power window switch 37P connector: disconnected Passenger's door latch 10P connector: disconnected

Test point 1 | Passenger's power window switch 37P connector No. 36

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the passenger's power window switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Passenger's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 24. NO Go to step 25.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 24.

NO

Go to step 25.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Passenger's door latch 10P connector: disconnected Test point 1 Passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty passenger's door lock knob switch; replace the passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Passenger's door latch 10P connector: disconnected

Test point 1 | Passenger's door latch 10P connector No. 8

Test point 2 | Body ground
````

## Chunk 1450: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_ae9b17eeebf4`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Passenger's door latch 10P connector: disconnected Test point 1 Passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty passenger's door lock knob switch; replace the passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Passenger's door latch 10P connector: disconnected

Test point 1 | Passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty passenger's door lock knob switch; replace the passenger's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G505).

- Open wire check (AS SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Passenger's power window switch 37P connector No. 36 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the passenger's power window switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Passenger's power window switch 37P connector No. 36

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the passenger's power window switch .

- Keyless/power door locks/security system check -1. With the driver's door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Switch Is information value ON? YES Go to step 27. NO Go to step 29.

-1. With the driver's door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Switch

Is information value ON?

YES

Go to step 27.

NO

Go to step 29.

- Driver's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 28. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 28.

NO

Replace the driver's door switch.

- Shorted wire check (FL DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .
````

## Chunk 1451: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_f48a10be534e`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
trol module connector D (40P): disconnected Driver's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .

- Driver's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 30. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 30.

NO

Replace the driver's door switch.

- Open wire check (FL DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 22 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 22

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. With the passenger's door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Go to step 32. NO Go to step 34.

-1. With the passenger's door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Go to step 32.

NO

Go to step 34.

- Passenger's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the passenger's door switch. -3. Disconnect the following connector. Passenger's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Passenger's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 33. NO Replace the passenger's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the passenger's door switch.

-3. Disconnect the following connector.

Passenger's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Passenger's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 33.

NO

Replace the passenger's door switch.

- Shorted wire check (FR DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Passenger's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No.
````

## Chunk 1452: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_a3af6c49edec`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
r's door switch.

-3. Disconnect the following connector.

Passenger's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Passenger's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 33.

NO

Replace the passenger's door switch.

- Shorted wire check (FR DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Passenger's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 23 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FR DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Passenger's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 23

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FR DOOR SW wire is OK. Replace the body control module .

- Passenger's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the passenger's door switch. -3. Disconnect the following connector. Passenger's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Passenger's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 35. NO Replace the passenger's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the passenger's door switch.

-3. Disconnect the following connector.

Passenger's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Passenger's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 35.

NO

Replace the passenger's door switch.

- Open wire check (FR DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 23 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The FR DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 23

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The FR DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 9 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Key Cylinder Switch (LOCK) Is information value ON? YES Go to step 37. NO Go to step 39.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Key Cylinder Switch (LOCK)

Is information value ON?

YES

Go to step 37.

NO

Go to step 39.

- Driver's door key cylinder switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the driver's door key cylinder switch . Is the switch OK? YES Go to step 38.
````

## Chunk 1453: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\630.html`
- Chunk ID: `chunk_44c859ca1803`
- Images: `images\GHH411743.jpeg`, `images\GHH411744.jpeg`, `images\GHH411745.jpeg`, `images\GHH411746.jpeg`, `images\GHH411747.jpeg`, `images\GHH411748.jpeg`, `images\GHH411749.jpeg`, `images\GHH411750.jpeg`, `images\GHH411751.jpeg`, `images\GHH411752.jpeg`, `images\GHH411753.jpeg`, `images\GHH411754.jpeg`, `images\GHH411755.jpeg`, `images\GHH411756.jpeg`
- Duplicate sources: `pages\2672.html`, `pages\26320.html`, `pages\14321.html`

### Full Text

````text
rrent conditions Value Unit Driver's Door Key Cylinder Switch (LOCK) Is information value ON? YES Go to step 37. NO Go to step 39.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Key Cylinder Switch (LOCK)

Is information value ON?

YES

Go to step 37.

NO

Go to step 39.

- Driver's door key cylinder switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the driver's door key cylinder switch . Is the switch OK? YES Go to step 38. NO Faulty driver's door key cylinder switch; replace the driver's door latch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the driver's door key cylinder switch .

Is the switch OK?

YES

Go to step 38.

NO

Faulty driver's door key cylinder switch; replace the driver's door latch .

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Replace the power window master switch . NO Repair an open or high resistance in the ground wire or poor ground (G501).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Replace the power window master switch .

NO

Repair an open or high resistance in the ground wire or poor ground (G501).

- Open wire check (DR KEY CYL LOCK line) -1. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 7 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Key Cylinder Switch (LOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR KEY CYL LOCK wire is OK. Replace the power window master switch .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 7

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Key Cylinder Switch (LOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR KEY CYL LOCK wire is OK. Replace the power window master switch .
````

## Chunk 1454: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_134a2f3c1f4a`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\2673.html`, `pages\26321.html`, `pages\14322.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Switch information check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Door Multiplex Control Unit Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Passenger's Door Lock Knob Switch (UNLOCK) Driver's Door Key Cylinder Switch (LOCK) Body Control Module Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Driver's Rear Door Lock Knob Switch (UNLOCK) Passenger's Rear Door Lock Knob Sw. (UNLOCK) Driver's Door Switch Front Passenger's Door Switch Driver's Rear Door Switch Passenger's Rear Door Switch Security Hood Switch Is each switch information value OK? YES Intermittent failure, the system is OK at this time. NG Trunk lid latch switch circuit troubleshooting: go to step 2. NG Hood latch switch circuit troubleshooting: go to step 8. NG Driver's door lock knob switch circuit troubleshooting: go to step 14. NG Front passenger's door lock knob switch circuit troubleshooting: go to step 20. NG Left rear door lock knob switch circuit troubleshooting: go to step 26. NG Right rear door lock knob switch circuit troubleshooting: go to step 32. NG Driver's door switch circuit troubleshooting: go to step 38. NG Front passenger's door switch circuit troubleshooting: go to step 43. NG Left rear door switch circuit troubleshooting: go to step 48. NG Right rear door switch circuit troubleshooting: go to step 53. NG Driver's door key cylinder switch circuit troubleshooting: go to step 58.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Door Multiplex Control Unit

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Passenger's Door Lock Knob Switch (UNLOCK)

Driver's Door Key Cylinder Switch (LOCK)

Body Control Module

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Driver's Rear Door Lock Knob Switch (UNLOCK)

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Driver's Door Switch

Front Passenger's Door Switch

Driver's Rear Door Switch

Passenger's Rear Door Switch

Security Hood Switch

Is each switch information value OK?

YES

Intermittent failure, the system is OK at this time.

NG

Trunk lid latch switch circuit troubleshooting: go to step 2.

NG

Hood latch switch circuit troubleshooting: go to step 8.

NG

Driver's door lock knob switch circuit troubleshooting: go to step 14.

NG

Front passenger's door lock knob switch circuit troubleshooting: go to step 20.

NG

Left rear door lock knob switch circuit troubleshooting: go to step 26.

NG

Right rear door lock knob switch circuit troubleshooting: go to step 32.

NG

Driver's door switch circuit troubleshooting: go to step 38.

NG

Front passenger's door switch circuit troubleshooting: go to step 43.

NG

Left rear door switch circuit troubleshooting: go to step 48.

NG

Right rear door switch circuit troubleshooting: go to step 53.

NG

Driver's door key cylinder switch circuit troubleshooting: go to step 58.

- Keyless/power door locks/security system check 1 -1. With the trunk closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 3. NO Go to step 5.

-1. With the trunk closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (trunk lid latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Trunk lid latch 3P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value OFF? YES Faulty trunk lid latch switch; replace the trunk lid latch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Trunk lid latch 3P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value OFF?

YES

Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Go to step 4.

- Shorted wire check (TRUNK SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2.
````

## Chunk 1455: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_0b83181b4bb5`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\2673.html`, `pages\26321.html`, `pages\14322.html`

### Full Text

````text
(trunk lid latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Trunk lid latch 3P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value OFF? YES Faulty trunk lid latch switch; replace the trunk lid latch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Trunk lid latch 3P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value OFF?

YES

Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Go to step 4.

- Shorted wire check (TRUNK SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector D (40P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector D (40P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Trunk lid latch 3P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Trunk lid latch 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A Trunk lid latch 3P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 6. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Trunk lid latch 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Trunk lid latch 3P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 6.

NO

Go to step 7.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Trunk lid latch 3P connector: disconnected Test point 1 Trunk lid latch 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch . NO Repair an open or high resistance in the ground wire or poor ground (G701).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Trunk lid latch 3P connector: disconnected

Test point 1 | Trunk lid latch 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty trunk lid latch switch; replace the trunk lid latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G701).

- Open wire check (TRUNK SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 27 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 27

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit
````

## Chunk 1456: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_fee8f63e3952`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\2673.html`, `pages\26321.html`, `pages\14322.html`

### Full Text

````text
the trunk lid latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G701).

- Open wire check (TRUNK SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 27 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 27

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the hood opened, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 9. NO Go to step 11.

-1. With the hood opened, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 9.

NO

Go to step 11.

- Determine possible failure area (hood latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value ON? YES Faulty hood latch switch; replace the hood latch . NO Go to step 10.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value ON?

YES

Faulty hood latch switch; replace the hood latch .

NO

Go to step 10.

- Shorted wire check (HOOD SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected Test point 1 Body control module connector C (28P) No. 19 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 19

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A Hood latch switch 2P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 12. NO Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Hood latch switch 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 12.

NO

Go to step 13.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected Test point 1 Hood latch switch 2P connector No.
````

## Chunk 1457: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_277f38803830`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\2673.html`, `pages\26321.html`, `pages\14322.html`

### Full Text

````text
on value OFF? YES Go to step 12. NO Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Hood latch switch 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 12.

NO

Go to step 13.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected Test point 1 Hood latch switch 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty hood latch switch; replace the hood latch . NO Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3). *1: L15B7 engine *2: K20C2 engine (type A) *3: K20C2 engine (type B)

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected

Test point 1 | Hood latch switch 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty hood latch switch; replace the hood latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G401 *1/*2, G402 *3).

*1: L15B7 engine

*2: K20C2 engine (type A)

*3: K20C2 engine (type B)

- Open wire check (HOOD SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 19 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Repair an open or high resistance in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 19

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Repair an open or high resistance in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 15. NO Go to step 17.

-1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 15.

NO

Go to step 17.

- Determine possible failure area (driver's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty driver's door lock knob switch; replace the driver's door latch . NO Go to step 16.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Go to step 16.

- Shorted wire check (DR SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Power window master switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK.
````

## Chunk 1458: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_fbb3b7332aa0`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Go to step 16.

- Shorted wire check (DR SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Power window master switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Power window master switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected

Test point 1 | Power window master switch 37P connector No. 20

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 18. NO Go to step 19.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 18.

NO

Go to step 19.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G501).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G501).

- Open wire check (DR SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 20 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 20

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1.
````

## Chunk 1459: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_a26ae5769b8f`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
dy ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 20

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR SILCON UNLOCK wire is OK. Replace the power window master switch .

- Keyless/power door locks/security system check 1 -1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 21. NO Go to step 23.

-1. With the front passenger's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 21.

NO

Go to step 23.

- Determine possible failure area (front passenger's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Go to step 22.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Go to step 22.

- Shorted wire check (AS SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's power window switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's power window switch 37P connector: disconnected Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's power window switch 37P connector No. 36 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's power window switch 37P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's power window switch 37P connector: disconnected Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's power window switch 37P connector No. 36

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Front passenger's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Front passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 24. NO Go to step 25.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 24.
````

## Chunk 1460: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_4800305c8cea`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\2673.html`, `pages\26321.html`, `pages\14322.html`

### Full Text

````text
per wire. Terminal A Front passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 24. NO Go to step 25.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 24.

NO

Go to step 25.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G505).

- Open wire check (AS SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Front passenger's power window switch 37P connector No. 29 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's power window switch 37P connector No. 29

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 1 -1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information indicator ON? YES Go to step 27. NO Go to step 29.

-1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 27.

NO

Go to step 29.

- Determine possible failure area (left rear door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information indicator OFF? YES Faulty left rear door lock knob switch; replace the left rear door latch . NO Go to step 28.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information indicator OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 28.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2.
````

## Chunk 1461: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_502393eab3ce`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
following connector. Left rear door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information indicator OFF? YES Faulty left rear door lock knob switch; replace the left rear door latch . NO Go to step 28.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information indicator OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 28.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Left rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Left rear door latch 10P connector No. 9 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 30. NO Go to step 31.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Left rear door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 30.

NO

Go to step 31.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected Test point 1 Left rear door latch 10P connector No. 6 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G601).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Left rear door latch 10P connector: disconnected

Test point 1 | Left rear door latch 10P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G601).

- Open wire check (RR L SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 15 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2.
````

## Chunk 1462: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_f1f1bde7181c`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
ch 10P connector No. 6

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G601).

- Open wire check (RR L SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 15 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR L SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 15

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR L SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 33. NO Go to step 35.

-1. With the right rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 33.

NO

Go to step 35.

- Determine possible failure area (right rear door lock knob switch, others) -1. Disconnect the following connector. Right rear door latch 10P connector -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value OFF? YES Faulty right rear door lock knob switch; replace the right rear door latch . NO Go to step 34.

-1. Disconnect the following connector.

Right rear door latch 10P connector

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value OFF?

YES

Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Go to step 34.

- Shorted wire check (RR R SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected Test point 1 Body control module connector C (28P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Right rear door latch 10P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Right rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Right rear door latch 10P connector No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 36. NO Go to step 37.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Right rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Right rear door latch 10P connector No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4.
````

## Chunk 1463: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_b7a0bd9c80b4`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Right rear door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Right rear door latch 10P connector No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Go to step 36. NO Go to step 37.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Right rear door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Right rear door latch 10P connector No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Go to step 36.

NO

Go to step 37.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected Test point 1 Right rear door latch 10P connector No. 9 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch . NO Repair an open or high resistance in the ground wire or poor ground (G602).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Right rear door latch 10P connector: disconnected

Test point 1 | Right rear door latch 10P connector No. 9

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty right rear door lock knob switch; replace the right rear door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G602).

- Open wire check (RR R SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 16 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Lock Knob Sw. (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The RR R SILCON UNLOCK wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 16

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR R SILCON UNLOCK wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. With the driver's door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Switch Is information value ON? YES Go to step 39. NO Go to step 41.

-1. With the driver's door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Switch

Is information value ON?

YES

Go to step 39.

NO

Go to step 41.

- Driver's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 40. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 40.

NO
````

## Chunk 1464: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_102d4acc4e0b`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 40. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 40.

NO

Replace the driver's door switch.

- Shorted wire check (FL DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Driver's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .

- Driver's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the driver's door switch. -3. Disconnect the following connector. Driver's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Driver's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 42. NO Replace the driver's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the driver's door switch.

-3. Disconnect the following connector.

Driver's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Driver's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 42.

NO

Replace the driver's door switch.

- Open wire check (FL DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 22 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The FL DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 22

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The FL DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. With the front passenger's door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Go to step 44. NO Go to step 46.

-1. With the front passenger's door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Go to step 44.

NO

Go to step 46.

- Front passenger's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the front passenger's door switch. -3. Disconnect the following connector. Front passenger's door switch 1P connector -4. Check for continuity between test points 1 and 2.
````

## Chunk 1465: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_8b3e18a79638`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
ce the body control module .

- Keyless/power door locks/security system check -1. With the front passenger's door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Go to step 44. NO Go to step 46.

-1. With the front passenger's door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Go to step 44.

NO

Go to step 46.

- Front passenger's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the front passenger's door switch. -3. Disconnect the following connector. Front passenger's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Front passenger's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 45. NO Replace the front passenger's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the front passenger's door switch.

-3. Disconnect the following connector.

Front passenger's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Front passenger's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 45.

NO

Replace the front passenger's door switch.

- Shorted wire check (FR DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Front passenger's door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 23 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The FR DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Front passenger's door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 23

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The FR DOOR SW wire is OK. Replace the body control module .

- Front passenger's door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the front passenger's door switch. -3. Disconnect the following connector. Front passenger's door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Front passenger's door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 47. NO Replace the front passenger's door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the front passenger's door switch.

-3. Disconnect the following connector.

Front passenger's door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Front passenger's door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 47.

NO

Replace the front passenger's door switch.

- Open wire check (FR DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 23 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The FR DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 23

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO
````

## Chunk 1466: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_2e7b67449aec`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
ace the front passenger's door switch.

- Open wire check (FR DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 23 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Front Passenger's Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The FR DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 23

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Front Passenger's Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The FR DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. With the left rear door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Switch Is information value ON? YES Go to step 49. NO Go to step 51.

-1. With the left rear door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Switch

Is information value ON?

YES

Go to step 49.

NO

Go to step 51.

- Left rear door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the left rear door switch. -3. Disconnect the following connector. Left rear door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Left rear door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 50. NO Replace the left rear door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the left rear door switch.

-3. Disconnect the following connector.

Left rear door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Left rear door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 50.

NO

Replace the left rear door switch.

- Shorted wire check (RL DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Left rear door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 24 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RL DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Left rear door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 24

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RL DOOR SW wire is OK. Replace the body control module .

- Left rear door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the left rear door switch. -3. Disconnect the following connector. Left rear door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Left rear door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 52. NO Replace the left rear door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the left rear door switch.

-3. Disconnect the following connector.

Left rear door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Left rear door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 52.

NO

Replace the left rear door switch.

- Open wire check (RL DOOR SW line) -1. Connect terminals A and B with a jumper wire.
````

## Chunk 1467: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_1079615f94a8`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
or Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 52. NO Replace the left rear door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the left rear door switch.

-3. Disconnect the following connector.

Left rear door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Left rear door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 52.

NO

Replace the left rear door switch.

- Open wire check (RL DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 24 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The RL DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 24

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RL DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. With the right rear door closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Switch Is information value ON? YES Go to step 54. NO Go to step 56.

-1. With the right rear door closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Switch

Is information value ON?

YES

Go to step 54.

NO

Go to step 56.

- Right rear door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the right rear door switch. -3. Disconnect the following connector. Right rear door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Right rear door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 55. NO Replace the right rear door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the right rear door switch.

-3. Disconnect the following connector.

Right rear door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Right rear door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 55.

NO

Replace the right rear door switch.

- Shorted wire check (RR DOOR SW line) -1. Disconnect the following connector. Body control module connector D (40P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Right rear door switch 1P connector: disconnected Test point 1 Body control module connector D (40P) No. 28 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The RR DOOR SW wire is OK. Replace the body control module .

-1. Disconnect the following connector.

Body control module connector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Right rear door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 28

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR DOOR SW wire is OK. Replace the body control module .

- Right rear door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the right rear door switch. -3. Disconnect the following connector. Right rear door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Right rear door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1468: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_8b3d7aa12d9e`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
onnector D (40P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Right rear door switch 1P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 28

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The RR DOOR SW wire is OK. Replace the body control module .

- Right rear door switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the right rear door switch. -3. Disconnect the following connector. Right rear door switch 1P connector -4. Check for continuity between test points 1 and 2. Test point 1 Right rear door switch 1P connector Test point 2 Switch ground Courtesy of HONDA, U.S.A., INC. Is there no continuity when you push the switch and is there continuity when you release the switch? YES Go to step 57. NO Replace the right rear door switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the right rear door switch.

-3. Disconnect the following connector.

Right rear door switch 1P connector

-4. Check for continuity between test points 1 and 2.

Test point 1 | Right rear door switch 1P connector

Test point 2 | Switch ground

Courtesy of HONDA, U.S.A., INC.

Is there no continuity when you push the switch and is there continuity when you release the switch?

YES

Go to step 57.

NO

Replace the right rear door switch.

- Open wire check (RR DOOR SW line) -1. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 28 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Rear Door Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The RR DOOR SW wire is OK. Replace the body control module .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 28

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Rear Door Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The RR DOOR SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Connect terminals A and B with a jumper wire. Terminal A Driver's door latch 10P connector No. 9 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Key Cylinder Switch (LOCK) Is information value ON? YES Go to step 59. NO Go to step 61.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Driver's door latch 10P connector No. 9

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Key Cylinder Switch (LOCK)

Is information value ON?

YES

Go to step 59.

NO

Go to step 61.

- Driver's door key cylinder switch operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Test the driver's door key cylinder switch . Is the switch OK? YES Go to step 60. NO Faulty driver's door key cylinder switch; replace the driver's door latch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Test the driver's door key cylinder switch .

Is the switch OK?

YES

Go to step 60.

NO

Faulty driver's door key cylinder switch; replace the driver's door latch .

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Replace the power window master switch . NO Repair an open or high resistance in the ground wire or poor ground (G501).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES
````

## Chunk 1469: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (4-door)
- Source path: `pages\631.html`
- Chunk ID: `chunk_f85e17a43ff1`
- Images: `images\GHH411757.jpeg`, `images\GHH411758.jpeg`, `images\GHH411759.jpeg`, `images\GHH411760.jpeg`, `images\GHH411761.jpeg`, `images\GHH411762.jpeg`, `images\GHH411763.jpeg`, `images\GHH411764.jpeg`, `images\GHH411765.jpeg`, `images\GHH411766.jpeg`, `images\GHH411767.jpeg`, `images\GHH411768.jpeg`, `images\GHH411769.jpeg`, `images\GHH411770.jpeg`, `images\GHH411771.jpeg`, `images\GHH411772.jpeg`, `images\GHH411773.jpeg`, `images\GHH411774.jpeg`, `images\GHH411775.jpeg`, `images\GHH411776.jpeg`, `images\GHH411777.jpeg`, `images\GHH411778.jpeg`
- Duplicate sources: `pages\632.html`, `pages\2673.html`, `pages\2674.html`, `pages\26321.html`, `pages\26322.html`, `pages\14322.html`, `pages\14323.html`

### Full Text

````text
er's door key cylinder switch; replace the driver's door latch .

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected Test point 1 Driver's door latch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Replace the power window master switch . NO Repair an open or high resistance in the ground wire or poor ground (G501).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Driver's door latch 10P connector: disconnected

Test point 1 | Driver's door latch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Replace the power window master switch .

NO

Repair an open or high resistance in the ground wire or poor ground (G501).

- Open wire check (DR KEY CYL LOCK line) -1. Connect terminals A and B with a jumper wire. Terminal A Power window master switch 37P connector No. 7 Terminal B Body ground -2. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Key Cylinder Switch (LOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The DR KEY CYL LOCK wire is OK. Replace the power window master switch .

-1. Connect terminals A and B with a jumper wire.

Terminal A | Power window master switch 37P connector No. 7

Terminal B | Body ground

-2. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Key Cylinder Switch (LOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The DR KEY CYL LOCK wire is OK. Replace the power window master switch .
````

## Chunk 1470: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\632.html`
- Chunk ID: `chunk_41c2bb7eb432`
- Images: `images\GHH411779.jpeg`, `images\GHH411780.jpeg`, `images\GHH411781.jpeg`, `images\GHH411782.jpeg`, `images\GHH411783.jpeg`, `images\GHH411784.jpeg`, `images\GHH411785.jpeg`, `images\GHH411786.jpeg`, `images\GHH411787.jpeg`, `images\GHH411788.jpeg`, `images\GHH411789.jpeg`, `images\GHH411790.jpeg`, `images\GHH411791.jpeg`, `images\GHH411792.jpeg`, `images\GHH411793.jpeg`, `images\GHH411794.jpeg`, `images\GHH411795.jpeg`, `images\GHH411796.jpeg`, `images\GHH411797.jpeg`, `images\GHH411798.jpeg`, `images\GHH411799.jpeg`, `images\GHH411800.jpeg`
- Duplicate sources: `pages\2674.html`, `pages\26322.html`, `pages\14323.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Switch information check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Door Multiplex Control Unit Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Passenger's Door Lock Knob Switch (UNLOCK) Driver's Door Key Cylinder Switch (LOCK) Body Control Module Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Driver's Rear Door Lock Knob Switch (UNLOCK) Passenger's Rear Door Lock Knob Sw. (UNLOCK) Driver's Door Switch Front Passenger's Door Switch Driver's Rear Door Switch Passenger's Rear Door Switch Security Hood Switch Is each switch information value OK? YES Intermittent failure, the system is OK at this time. NG Tailgate latch switch circuit troubleshooting: go to step 2. NG Hood latch switch circuit troubleshooting: go to step 8. NG Driver's door lock knob switch circuit troubleshooting: go to step 14. NG Front passenger's door lock knob switch circuit troubleshooting: go to step 20. NG Left rear door lock knob switch circuit troubleshooting: go to step 26. NG Right rear door lock knob switch circuit troubleshooting: go to step 32. NG Driver's door switch circuit troubleshooting: go to step 38. NG Front passenger's door switch circuit troubleshooting: go to step 43. NG Left rear door switch circuit troubleshooting: go to step 48. NG Right rear door switch circuit troubleshooting: go to step 53. NG Driver's door key cylinder switch circuit troubleshooting: go to step 58.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Door Multiplex Control Unit

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Passenger's Door Lock Knob Switch (UNLOCK)

Driver's Door Key Cylinder Switch (LOCK)

Body Control Module

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Driver's Rear Door Lock Knob Switch (UNLOCK)

Passenger's Rear Door Lock Knob Sw. (UNLOCK)

Driver's Door Switch

Front Passenger's Door Switch

Driver's Rear Door Switch

Passenger's Rear Door Switch

Security Hood Switch

Is each switch information value OK?

YES

Intermittent failure, the system is OK at this time.

NG

Tailgate latch switch circuit troubleshooting: go to step 2.

NG

Hood latch switch circuit troubleshooting: go to step 8.

NG

Driver's door lock knob switch circuit troubleshooting: go to step 14.

NG

Front passenger's door lock knob switch circuit troubleshooting: go to step 20.

NG

Left rear door lock knob switch circuit troubleshooting: go to step 26.

NG

Right rear door lock knob switch circuit troubleshooting: go to step 32.

NG

Driver's door switch circuit troubleshooting: go to step 38.

NG

Front passenger's door switch circuit troubleshooting: go to step 43.

NG

Left rear door switch circuit troubleshooting: go to step 48.

NG

Right rear door switch circuit troubleshooting: go to step 53.

NG

Driver's door key cylinder switch circuit troubleshooting: go to step 58.

- Keyless/power door locks/security system check 1 -1. With the tailgate closed, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 3. NO Go to step 5.

-1. With the tailgate closed, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (tailgate latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Tailgate latch 4P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value OFF? YES Faulty tailgate latch switch; replace the tailgate latch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Tailgate latch 4P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value OFF?

YES

Faulty tailgate latch switch; replace the tailgate latch .

NO

Go to step 4.

- Shorted wire check (TRUNK SW line) -1.
````

## Chunk 1471: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\632.html`
- Chunk ID: `chunk_1677d29649f1`
- Images: `images\GHH411779.jpeg`, `images\GHH411780.jpeg`, `images\GHH411781.jpeg`, `images\GHH411782.jpeg`, `images\GHH411783.jpeg`, `images\GHH411784.jpeg`, `images\GHH411785.jpeg`, `images\GHH411786.jpeg`, `images\GHH411787.jpeg`, `images\GHH411788.jpeg`, `images\GHH411789.jpeg`, `images\GHH411790.jpeg`, `images\GHH411791.jpeg`, `images\GHH411792.jpeg`, `images\GHH411793.jpeg`, `images\GHH411794.jpeg`, `images\GHH411795.jpeg`, `images\GHH411796.jpeg`, `images\GHH411797.jpeg`, `images\GHH411798.jpeg`, `images\GHH411799.jpeg`, `images\GHH411800.jpeg`
- Duplicate sources: `pages\2674.html`, `pages\26322.html`, `pages\14323.html`

### Full Text

````text
NO

Go to step 5.

- Determine possible failure area (tailgate latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Tailgate latch 4P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value OFF? YES Faulty tailgate latch switch; replace the tailgate latch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Tailgate latch 4P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value OFF?

YES

Faulty tailgate latch switch; replace the tailgate latch .

NO

Go to step 4.

- Shorted wire check (TRUNK SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector D (40P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Tailgate latch 4P connector: disconnected Test point 1 Body control module connector D (40P) No. 27 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector D (40P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector D (40P): disconnected Tailgate latch 4P connector: disconnected

Test point 1 | Body control module connector D (40P) No. 27

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Tailgate latch 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Tailgate latch 4P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Go to step 6. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Tailgate latch 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Tailgate latch 4P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Go to step 6.

NO

Go to step 7.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Tailgate latch 4P connector: disconnected Test point 1 Tailgate latch 4P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty tailgate latch switch; replace the tailgate latch . NO Repair an open or high resistance in the ground wire or poor ground (G603).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Tailgate latch 4P connector: disconnected

Test point 1 | Tailgate latch 4P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty tailgate latch switch; replace the tailgate latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G603).

- Open wire check (TRUNK SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 27 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 27

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.
````

## Chunk 1472: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\632.html`
- Chunk ID: `chunk_6ecadf340af3`
- Images: `images\GHH411779.jpeg`, `images\GHH411780.jpeg`, `images\GHH411781.jpeg`, `images\GHH411782.jpeg`, `images\GHH411783.jpeg`, `images\GHH411784.jpeg`, `images\GHH411785.jpeg`, `images\GHH411786.jpeg`, `images\GHH411787.jpeg`, `images\GHH411788.jpeg`, `images\GHH411789.jpeg`, `images\GHH411790.jpeg`, `images\GHH411791.jpeg`, `images\GHH411792.jpeg`, `images\GHH411793.jpeg`, `images\GHH411794.jpeg`, `images\GHH411795.jpeg`, `images\GHH411796.jpeg`, `images\GHH411797.jpeg`, `images\GHH411798.jpeg`, `images\GHH411799.jpeg`, `images\GHH411800.jpeg`
- Duplicate sources: `pages\2674.html`, `pages\26322.html`, `pages\14323.html`

### Full Text

````text
is OK. Faulty tailgate latch switch; replace the tailgate latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G603).

- Open wire check (TRUNK SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector D (40P) No. 27 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Trunk Lid/Tailgate Switch Is information value ON? YES Repair an open or high resistance in the wire. NO The TRUNK SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector D (40P) No. 27

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Trunk Lid/Tailgate Switch

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The TRUNK SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the hood opened, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 9. NO Go to step 11.

-1. With the hood opened, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 9.

NO

Go to step 11.

- Determine possible failure area (hood latch switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value ON? YES Faulty hood latch switch; replace the hood latch . NO Go to step 10.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value ON?

YES

Faulty hood latch switch; replace the hood latch .

NO

Go to step 10.

- Shorted wire check (HOOD SW line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Body control module connector C (28P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected Test point 1 Body control module connector C (28P) No. 19 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Body control module connector C (28P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Body control module connector C (28P): disconnected Hood latch switch 2P connector: disconnected

Test point 1 | Body control module connector C (28P) No. 19

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Hood latch switch 2P connector -3. Connect terminals A and B with a jumper wire. Terminal A Hood latch switch 2P connector No. 1 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 12. NO Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Hood latch switch 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 12.

NO

Go to step 13.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2.
````

## Chunk 1473: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\632.html`
- Chunk ID: `chunk_c43bfc8344fa`
- Images: `images\GHH411779.jpeg`, `images\GHH411780.jpeg`, `images\GHH411781.jpeg`, `images\GHH411782.jpeg`, `images\GHH411783.jpeg`, `images\GHH411784.jpeg`, `images\GHH411785.jpeg`, `images\GHH411786.jpeg`, `images\GHH411787.jpeg`, `images\GHH411788.jpeg`, `images\GHH411789.jpeg`, `images\GHH411790.jpeg`, `images\GHH411791.jpeg`, `images\GHH411792.jpeg`, `images\GHH411793.jpeg`, `images\GHH411794.jpeg`, `images\GHH411795.jpeg`, `images\GHH411796.jpeg`, `images\GHH411797.jpeg`, `images\GHH411798.jpeg`, `images\GHH411799.jpeg`, `images\GHH411800.jpeg`
- Duplicate sources: `pages\2674.html`, `pages\26322.html`, `pages\14323.html`

### Full Text

````text
, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Go to step 12. NO Go to step 13.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Hood latch switch 2P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Hood latch switch 2P connector No. 1

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Go to step 12.

NO

Go to step 13.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected Test point 1 Hood latch switch 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty hood latch switch; replace the hood latch . NO Repair an open or high resistance in the ground wire or poor ground (G401).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Hood latch switch 2P connector: disconnected

Test point 1 | Hood latch switch 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty hood latch switch; replace the hood latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G401).

- Open wire check (HOOD SW line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Body control module connector C (28P) No. 19 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Security Hood Switch Is information value OFF? YES Repair an open or high resistance in the wire. NO The HOOD SW wire is OK. Replace the body control module .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Body control module connector C (28P) No. 19

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Security Hood Switch

Is information value OFF?

YES

Repair an open or high resistance in the wire.

NO

The HOOD SW wire is OK. Replace the body control module .

- Keyless/power door locks/security system check 1 -1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 15. NO Go to step 17.

-1. With the driver's door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 15.

NO

Go to step 17.

- Determine possible failure area (driver's door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Driver's door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Door Lock Knob Switch (UNLOCK) Is information value OFF? YES Faulty driver's door lock knob switch; replace the driver's door latch . NO Go to step 16.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Driver's door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Door Lock Knob Switch (UNLOCK)

Is information value OFF?

YES

Faulty driver's door lock knob switch; replace the driver's door latch .

NO

Go to step 16.

- Shorted wire check (DR SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Power window master switch 37P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Power window master switch 37P connector: disconnected Driver's door latch 10P connector: disconnected Test point 1 Power window master switch 37P connector No. 20 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The DR SILCON UNLOCK wire is OK.
````

## Chunk 1474: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\632.html`
- Chunk ID: `chunk_859a0931d41e`
- Images: `images\GHH411779.jpeg`, `images\GHH411780.jpeg`, `images\GHH411781.jpeg`, `images\GHH411782.jpeg`, `images\GHH411783.jpeg`, `images\GHH411784.jpeg`, `images\GHH411785.jpeg`, `images\GHH411786.jpeg`, `images\GHH411787.jpeg`, `images\GHH411788.jpeg`, `images\GHH411789.jpeg`, `images\GHH411790.jpeg`, `images\GHH411791.jpeg`, `images\GHH411792.jpeg`, `images\GHH411793.jpeg`, `images\GHH411794.jpeg`, `images\GHH411795.jpeg`, `images\GHH411796.jpeg`, `images\GHH411797.jpeg`, `images\GHH411798.jpeg`, `images\GHH411799.jpeg`, `images\GHH411800.jpeg`
- Duplicate sources: `pages\2674.html`, `pages\26322.html`, `pages\14323.html`

### Full Text

````text
per wire. Terminal A Front passenger's door latch 10P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Go to step 24. NO Go to step 25.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Front passenger's door latch 10P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's door latch 10P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Go to step 24.

NO

Go to step 25.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected Test point 1 Front passenger's door latch 10P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch . NO Repair an open or high resistance in the ground wire or poor ground (G505).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Front passenger's door latch 10P connector: disconnected

Test point 1 | Front passenger's door latch 10P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Faulty front passenger's door lock knob switch; replace the front passenger's door latch .

NO

Repair an open or high resistance in the ground wire or poor ground (G505).

- Open wire check (AS SILCON UNLOCK line) -1. Remove the jumper wire. -2. Connect terminals A and B with a jumper wire. Terminal A Front passenger's power window switch 37P connector No. 36 Terminal B Body ground -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Passenger's Door Lock Knob Switch (UNLOCK) Is information value ON? YES Repair an open or high resistance in the wire. NO The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

-1. Remove the jumper wire.

-2. Connect terminals A and B with a jumper wire.

Terminal A | Front passenger's power window switch 37P connector No. 36

Terminal B | Body ground

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Passenger's Door Lock Knob Switch (UNLOCK)

Is information value ON?

YES

Repair an open or high resistance in the wire.

NO

The AS SILCON UNLOCK wire is OK. Replace the front passenger's power window switch .

- Keyless/power door locks/security system check 1 -1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information indicator ON? YES Go to step 27. NO Go to step 29.

-1. With the left rear door lock knob switch in LOCK position, check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information indicator ON?

YES

Go to step 27.

NO

Go to step 29.

- Determine possible failure area (left rear door lock knob switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Left rear door latch 10P connector -3. Check the parameter(s) below with the HDS. Signal Current conditions Value Unit Driver's Rear Door Lock Knob Switch (UNLOCK) Is information indicator OFF? YES Faulty left rear door lock knob switch; replace the left rear door latch . NO Go to step 28.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Left rear door latch 10P connector

-3. Check the parameter(s) below with the HDS.

Signal | Current conditions

Value | Unit

Driver's Rear Door Lock Knob Switch (UNLOCK)

Is information indicator OFF?

YES

Faulty left rear door lock knob switch; replace the left rear door latch .

NO

Go to step 28.

- Shorted wire check (RR L SILCON UNLOCK line) -1. Turn the vehicle to the OFF (LOCK) mode. -2.
````

## Chunk 1475: Keyless/Power Door Locks/Security System Symptom Troubleshooting - The horn does not sound and/or the headlights do not flash when the PANIC button on the remote is pressed

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting - The horn does not sound and/or the headlights do not flash when the PANIC button on the remote is pressed
- Source path: `pages\633.html`
- Chunk ID: `chunk_cddd1732e4d0`
- Images: none
- Duplicate sources: `pages\2675.html`, `pages\26323.html`, `pages\14324.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting - The horn does not sound and/or the headlights do not flash when the PANIC button on the remote is pressed

NOTE: Before troubleshooting, check the B-CAN DTCs. If any DTC is indicated, troubleshoot the indicated DTC first.

- Determine possible failure area (body control module, others) -1. Press the PANIC button. Do the horns sound? YES Go to step 3. NO Go to step 2.

-1. Press the PANIC button.

Do the horns sound?

YES

Go to step 3.

NO

Go to step 2.

- Horn operation check -1. Press the horn button. Do the horns sound? YES Replace the keyless remote, then register the new remote . NO Check the horn circuit.

-1. Press the horn button.

Do the horns sound?

YES

Replace the keyless remote, then register the new remote .

NO

Check the horn circuit.

- Body control module check -1. Turn the headlight switch ON. Do the headlights come on? YES Intermittent failure, the system is OK at this time. Check for loose or poor connections. NO Check the lighting circuit. Do the body control module input test .

-1. Turn the headlight switch ON.

Do the headlights come on?

YES

Intermittent failure, the system is OK at this time. Check for loose or poor connections.

NO

Check the lighting circuit. Do the body control module input test .
````

## Chunk 1476: Immobilizer System Description - Components

- Title: Immobilizer System Description - Components
- Source path: `pages\634.html`
- Chunk ID: `chunk_0e03e004af96`
- Images: none
- Duplicate sources: `pages\2676.html`, `pages\26324.html`, `pages\14325.html`

### Full Text

````text
# Immobilizer System Description - Components

Security Indicator

When vehicle ON mode is entered, the authentication of the immobilizer key starts and the indicator is off. When the key is successfully authenticated, the indicator stays off. When the key is not successfully authenticated, the indicator blinks, the vehicle is turned to the OFF (LOCK) mode, and then the indicator goes off after blinking several times. For details on the illumination pattern, refer to immobilizer system symptom troubleshooting information .

Ignition Key

Vehicles equipped with the immobilizer system have an identification marking on the mechanical key. Consider this identification marking as a proof of the vehicle having the immobilizer system.
````

## Chunk 1477: Immobilizer System Description - Control/Function

- Title: Immobilizer System Description - Control/Function
- Source path: `pages\635.html`
- Chunk ID: `chunk_39443e87f8b2`
- Images: `images\GHH411801.jpeg`
- Duplicate sources: `pages\2677.html`, `pages\26325.html`, `pages\14326.html`

### Full Text

````text
# Immobilizer System Description - Control/Function

Immobilizer Function

An immobilizer system adds a second electronic layer of security to the vehicle. If the key matches mechanically, but the electronic check does not match, the PCM suspends fuel delivery and shuts down the engine. Refer to the keyless access system description for assistance, because the immobilizer function is merged into the remote when a vehicle has the keyless access system.

The system provides mutual authentication between the immobilizer-keyless control unit, the PCM, and the body control module when turning the vehicle to the ON mode. The engine stays running after the engine start-up if the correct key is inserted. The body control module authenticates the VSA modulator-control unit and the immobilizer signal only one time by request of the immobilizer-keyless control unit, when the vehicle is turned to the ON mode after resetting of the battery, removal and installation of the back-up fuse, or removal and installation of the VSA modulator-control unit.

For some model*, the brake pedal must be depressed to perform the immobilizer authentication.

*: Canada models

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1478: Immobilizer System Description - System Diagram

- Title: Immobilizer System Description - System Diagram
- Source path: `pages\636.html`
- Chunk ID: `chunk_cfa2ce98a68e`
- Images: `images\GHH411802.jpeg`
- Duplicate sources: `pages\2678.html`, `pages\26326.html`, `pages\14327.html`

### Full Text

````text
# Immobilizer System Description - System Diagram

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1479: Keyless Access System Description - Components (2/4-door)

- Title: Keyless Access System Description - Components (2/4-door)
- Source path: `pages\637.html`
- Chunk ID: `chunk_f7f34d331642`
- Images: `images\GHH411803.jpeg`
- Duplicate sources: `pages\2679.html`, `pages\26327.html`, `pages\14328.html`

### Full Text

````text
# Keyless Access System Description - Components (2/4-door)

Engine Start/Stop Switch

Pressing the engine start/stop button changes the vehicle mode to OFF (LOCK), ACCESSORY, ON, or START mode. The engine start/stop switch also includes an LF antenna. When operating the backup function, engine start/stop switch receives the immobilizer signal from the remote, and sends an immobilizer signal to the body control module.

LF (Low Frequency) Antennas

The front interior, rear interior, left/right-front, trunk, and rear bumper LF antennas send the signals to the remote inside and outside of the vehicle.

Door Touch Sensors and Outer Handle Lock Switches

The door touch sensors are built in the each door outer handles, also the outer handle lock switches are built in the driver's and front passenger's door outer handles. To operate the door locks without the built-in key while carrying the remote, grip the door outer handle to unlock the doors and press the outer handle lock switch on the door outer handle to lock the doors.

Remote

The remote is equipped with a keyless transmitter, and all the doors can be locked and unlocked by a lock/unlock button operation, even from a remote distance from the vehicle. When the lock button or unlock button is pressed, the keyless transmitter sends the applicable switch signal to the body control module. After receiving authentication, the body control module controls the door lock/unlock actuator.

Courtesy of HONDA, U.S.A., INC.

Keyless Buzzer

The keyless buzzer located inside the rear bumper sounds when smart entry functions.
````

## Chunk 1480: Keyless Access System Description - Components (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System Description - Components (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\638.html`
- Chunk ID: `chunk_8d50c10e3d74`
- Images: `images\GHH411804.jpeg`
- Duplicate sources: `pages\2680.html`, `pages\26328.html`, `pages\14329.html`

### Full Text

````text
# Keyless Access System Description - Components (5-door) (2017 2018 2019 2020 2021)

Engine Start/Stop Switch

Pressing the engine start/stop button changes the vehicle mode to OFF (LOCK), ACCESSORY, ON, or START mode. The engine start/stop switch also includes an LF antenna. When operating the backup function, the engine start/stop switch receives the immobilizer signal from the remote, and sends an immobilizer signal to the body control module.

LF (Low Frequency) Antennas

The front interior, middle interior, and rear interior LF antennas send the signals to the remote placed in the interior. The driver's door outer handle, front passenger's door outer handle, and rear bumper LF antennas send the signals to the remotes when they are outside of the vehicle.

Door Touch Sensors and Outer Handle Lock Switches

The door touch sensors and the outer handle lock switches are built in the driver's and front passenger's door outer handles. To operate the door locks without the built-in key while carrying the remote, grip the door outer handle to unlock the doors and press the outer handle lock switch on the door outer handle to lock the doors.

Tailgate Outer Handle Switch and Tailgate Outer Handle Lock Switch

The tailgate outer handle switch and the tailgate outer handle lock switch are built in the tailgate outer handle/lock switch. To operate the door locks without the built-in key while carrying the remote, press the tailgate outer handle switch to unlock the tailgate and press the tailgate outer handle lock switch on the tailgate outer handle to lock the doors

Remote

The remote is equipped with a keyless transmitter and all the doors can be locked and unlocked by a lock/unlock button operation, even from a remote distance from the vehicle. When the lock button or unlock button is pressed, the keyless transmitter sends the applicable switch signal to the body control module. After receiving authentication, the body control module controls the door lock/unlock actuator.

Courtesy of HONDA, U.S.A., INC.

Keyless Buzzer

The keyless buzzer, located behind the rear bumper, sounds when smart entry functions.
````

## Chunk 1481: Keyless Access System Description - Control/Function (2/4-door)

- Title: Keyless Access System Description - Control/Function (2/4-door)
- Source path: `pages\639.html`
- Chunk ID: `chunk_5d8599e5a174`
- Images: `images\GHH411805.jpeg`, `images\GHH411806.jpeg`, `images\GHH411807.jpeg`, `images\GHH411808.jpeg`, `images\GHH411809.jpeg`, `images\GHH411810.jpeg`, `images\GHH411811.jpeg`, `images\GHH411812.jpeg`
- Duplicate sources: `pages\2681.html`, `pages\26329.html`, `pages\14330.html`

### Full Text

````text
# Keyless Access System Description - Control/Function (2/4-door)

Smart Entry Function

The body control module detects the input signal of the door outer handle touch sensor, the outer handle lock switch, or the trunk lid outer handle switch, and authenticates 2-way communication with the remote. Then the body control module activates the door lock/unlock actuator or trunk lid release actuator and an answer back. For details on the illumination patterns of the warning lights and the functional check of the system, refer to keyless access system symptom troubleshooting information .

Courtesy of HONDA, U.S.A., INC.

Keyless Entry Function

The body control module receives keyless transmitter LOCK/UNLOCK signals from the remote. The body control module authenticates the RF signal from the remote, then the body control module activates the door lock actuators and the turn signal lights.

Courtesy of HONDA, U.S.A., INC.

Remote Search Function

Determines if the remote is present inside the vehicle during some operation or function. Detects the door open and close with the vehicle in the ACCESSORY/ON mode situation. When the remote is taken out of the vehicle, the keyless buzzer will sound and the gauge control module (Only when the vehicle in the ON mode) will show a warning.

Lighting and Indicator Function

The body control module controls the engine start/stop switch light, displays information in the information display *2 or the multi-information display (MID) *1, and illuminates the keyless access indicators in the gauge control module.

*1: With multi-information display

*2: Without multi-information display

Backup Communication Function

When key authentication between the remote and the body control module is not possible because of a system abnormality or a drop of the battery voltage of the remote, the immobilizer function can be canceled by pressing the engine start/stop switch button once and bringing the remote close to the engine start/stop switch while the engine start/stop switch indicator is flashing. This causes the immobilizer signal to be send to the body control module via LF antenna of the engine start/stop switch.

Courtesy of HONDA, U.S.A., INC.

Remote Engine Start System (With Remote Engine Start)

Start the Engine

The remote engine start feature is initiated by first pressing the lock button, then pressing and holding the "START" button within 5 seconds on the remote transmitter. An RF signal from the remote transmitter is received by the body control module, which then sends the request to start the engine to the PCM. At the same time, the body control module authenticates the key for the immobilizer system. The PCM starts the engine and sends feedback to the body control module indicating the status of the engine.

Courtesy of HONDA, U.S.A., INC.

Electric Steering Lock (With Electric Steering Lock)

The electric steering lock control unit is built into the electric steering lock, and it controls the steering lock motor. When the remote code is identified, the electric steering lock control unit unlocks the steering lock by controlling the steering lock motor.

Courtesy of HONDA, U.S.A., INC.

Key Lockout Prevent Function

The body control module monitors whether or not there is the remote in the vehicle. If the remote is in the vehicle, the system will not lock the doors. If the driver manually locks and closes the doors with the remote in the vehicle, the body control module energizes the driver's door lock actuator and unlocks the driver's door. When the trunk is closed with the remote left in the trunk, the body control module detects the location of the remote unit and does not lock the trunk.

Courtesy of HONDA, U.S.A., INC.

Immobilizer Function

The immobilizer function provides mutual authentication between the body control module, the PCM, and the VSA modulator-control unit when the vehicle is turned to the ON mode. The engine stays running after the engine start-up if the immobilizer signal matches. The body control module authenticates the VSA modulator-control unit and the immobilizer signal only one time, when the vehicle is turned to the ON mode after resetting of the 12 volt battery, removal and installation of the back-up fuse, or removal and installation of the VSA modulator-control unit.

For some models*, the brake pedal must be depressed to perform the immobilizer authentication.

*: Canada models

Courtesy of HONDA, U.S.A., INC.

Alarm Function
````

## Chunk 1482: Keyless Access System Description - Control/Function (2/4-door)

- Title: Keyless Access System Description - Control/Function (2/4-door)
- Source path: `pages\639.html`
- Chunk ID: `chunk_6df5371d2330`
- Images: `images\GHH411805.jpeg`, `images\GHH411806.jpeg`, `images\GHH411807.jpeg`, `images\GHH411808.jpeg`, `images\GHH411809.jpeg`, `images\GHH411810.jpeg`, `images\GHH411811.jpeg`, `images\GHH411812.jpeg`
- Duplicate sources: `pages\2681.html`, `pages\26329.html`, `pages\14330.html`

### Full Text

````text
lock the trunk.

Courtesy of HONDA, U.S.A., INC.

Immobilizer Function

The immobilizer function provides mutual authentication between the body control module, the PCM, and the VSA modulator-control unit when the vehicle is turned to the ON mode. The engine stays running after the engine start-up if the immobilizer signal matches. The body control module authenticates the VSA modulator-control unit and the immobilizer signal only one time, when the vehicle is turned to the ON mode after resetting of the 12 volt battery, removal and installation of the back-up fuse, or removal and installation of the VSA modulator-control unit.

For some models*, the brake pedal must be depressed to perform the immobilizer authentication.

*: Canada models

Courtesy of HONDA, U.S.A., INC.

Alarm Function

Detects the door open or close with the vehicle in the ACCESSORY/ON mode. When the remote is taken out of the vehicle, the keyless buzzer will sound and the gauge control module (Only when the vehicle is in the ON mode) will show a warning. Before the remote battery level falls to the point where the remote cannot be detected, the gauge control module will show a warning and an alarm will sound. Command to display shift to P warning should be transmitted via B-CAN.

Registration Facility

The body control module can store up to 6 remotes with the HDS.

Fault Diagnosis Function

The system has a fault diagnosis function. If any malfunction occurs, the keyless access indicator comes on in the gauge control module.

Customer Emergency

When the engine start/stop button is pressed continuously at least two times*, three times*, or once for 1.5 seconds or longer in an emergency while driving, the engine turns off, and the vehicle mode switches to ACCESSORY. In this mode, the steering wheel remains unlocked (with steering lock).

*: Control is different depending on the specifications.

Panic Function

When you press the PANIC button on the remote, the body control module sounds the horn and activates the exterior lights.

Walk Away Auto Lock Function

The walk away auto lock system detects where the remote is and locks all doors on the vehicle when all the doors are closed and the remote is outside of the vehicle and out of the range.

To operate the walk away auto lock system, it is necessary to enter the auto lock mode.

To enter the auto lock mode, all the following conditions must be met:

- The vehicle is in the OFF (LOCK) mode.

- Any door is closed, and then all the doors become closed.

- The remote is not inside of the vehicle.

- The remote is outside and within 2 m (7 ft) from the vehicle.

The vehicle's buzzer beeps once to confirm that the auto lock mode is engaged.

After the auto lock mode is engaged and the remote is away more than 2 m (7 ft) from the vehicle for 2 seconds or more, all the doors become locked. At that time, the vehicle's buzzer beeps once and some exterior lights blink once to confirm that the walk away lock system is engaged.

After the auto lock mode is engaged, if the remote is within 2 m (7 ft) from the vehicle for 30 seconds or more, the doors automatically lock.

The walk away auto lock system does not work under the following conditions:

- The remote is inside of the vehicle.

- Any door is closed when the remote is more than 2 m (7 ft) away from the vehicle.

- Any door is opened after the auto lock mode is engaged.

The walk away auto lock system does not work and the vehicle's buzzer beeps under the following conditions:

- The remote is away more than 2 m (7 ft) from the vehicle while closing the door.

- A communication error occurs between the remote and the vehicle.

The walk away auto lock system can be cancelled temporarily by customization.

Keyless Access System Operation Manual Customize

The keyless access system can be enabled and disabled by the operation shown in the table. The system is enabled and disabled each time the unlock button is pressed on the remote in the customize mode.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1483: Keyless Access System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\640.html`
- Chunk ID: `chunk_4650a982a350`
- Images: `images\GHH411813.jpeg`, `images\GHH411814.jpeg`, `images\GHH411815.jpeg`, `images\GHH411816.jpeg`, `images\GHH411817.jpeg`, `images\GHH411818.jpeg`, `images\GHH411819.jpeg`, `images\GHH411820.jpeg`
- Duplicate sources: `pages\2682.html`, `pages\26330.html`, `pages\14331.html`

### Full Text

````text
# Keyless Access System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

Smart Entry Function

The body control module detects the input signal of the door outer handle touch sensor, the outer handle lock switch, or the tailgate outer handle lock switch, and authenticates 2-way communication with the remote. The body control module then activates the door lock actuator and an answer back. The body control module also activates the tailgate release actuator when the tailgate outer handle switch is pressed. For details on the illumination patterns of the warning lights and the functional check of the system, refer to keyless access system symptom troubleshooting information .

Courtesy of HONDA, U.S.A., INC.

Keyless Entry Function

The body control module receives the keyless transmitter LOCK/UNLOCK signals from the remote. The body control module authenticates the RF signal from the remote, then activates the door lock actuators and the turn signal lights.

Courtesy of HONDA, U.S.A., INC.

Remote Search Function

Every time the doors are detected as opened or closed with the vehicle in the ACCESSORY/ON mode, the remote search function determines if the remote is present inside the vehicle. When the remote is taken out of the vehicle, the keyless buzzer sounds, and the gauge control module, (Only when the vehicle in the ON mode) shows a warning.

Lighting and Indicator Function

The body control module controls the engine start/stop switch light, displays information in the information display *1 or the multi-information display (MID) *2, and illuminates the keyless access indicators in the gauge control module.

*1: Without multi-information display

*2: With multi-information display

Backup Communication Function

When key authentication between the remote and the body control module is not possible because of a system abnormality or a drop of the battery voltage of the remote, the immobilizer function can be canceled by pressing the engine start/stop switch button once and bringing the remote close to the engine start/stop switch while the engine start/stop switch indicator is flashing. This causes the immobilizer signal to be sent to the body control module via the LF antenna of the engine start/stop switch.

Courtesy of HONDA, U.S.A., INC.

Remote Engine Start System (With Remote Engine Start)

The remote engine start feature is initiated by first pressing the lock button, then pressing and holding the "START" button within 5 seconds on the remote. A RF signal from the remote is received by the body control module, which then sends the request to start the engine to the PCM. At the same time, the body control module authenticates the key for the immobilizer system. The PCM starts the engine and sends feedback to the body control module indicating the status of the engine.

Courtesy of HONDA, U.S.A., INC.

Electric Steering Lock (With Electric Steering Lock)

The electric steering lock control unit is built into the electric steering lock and controls the steering lock motor. When the remote code is identified, the electric steering lock control unit unlocks the steering lock by controlling the steering lock motor.

Courtesy of HONDA, U.S.A., INC.

Key Lockout Prevent Function

The body control module monitors whether or not there is the remote in the vehicle. If the remote is in the vehicle, the system will not lock the doors. If the driver manually locks and closes the doors with the remote in the vehicle, the body control module energizes the door lock actuator and unlocks the driver's door. When the tailgate is closed, the body control module detects the location of the remote and the body control module energizes the tailgate release actuator, and unlocks the tailgate.

Courtesy of HONDA, U.S.A., INC.

Immobilizer Function

The immobilizer function provides mutual authentication between the body control module, the PCM, and the VSA modulator-control unit when the vehicle is turned to the ON mode. The engine stays running after engine start-up if the immobilizer signal matches. The body control module authenticates the VSA modulator-control unit and the immobilizer signal only one time, when the vehicle is turned to the ON mode after resetting of the 12 volt battery, removing and installing the back-up fuse or removing and installing the VSA modulator-control unit.

For some model*, the brake pedal must be depressed to perform the immobilizer authentication.

*: Canada models
````

## Chunk 1484: Keyless Access System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\640.html`
- Chunk ID: `chunk_86a41a2200c2`
- Images: `images\GHH411813.jpeg`, `images\GHH411814.jpeg`, `images\GHH411815.jpeg`, `images\GHH411816.jpeg`, `images\GHH411817.jpeg`, `images\GHH411818.jpeg`, `images\GHH411819.jpeg`, `images\GHH411820.jpeg`
- Duplicate sources: `pages\2682.html`, `pages\26330.html`, `pages\14331.html`

### Full Text

````text
ntrol module energizes the tailgate release actuator, and unlocks the tailgate.

Courtesy of HONDA, U.S.A., INC.

Immobilizer Function

The immobilizer function provides mutual authentication between the body control module, the PCM, and the VSA modulator-control unit when the vehicle is turned to the ON mode. The engine stays running after engine start-up if the immobilizer signal matches. The body control module authenticates the VSA modulator-control unit and the immobilizer signal only one time, when the vehicle is turned to the ON mode after resetting of the 12 volt battery, removing and installing the back-up fuse or removing and installing the VSA modulator-control unit.

For some model*, the brake pedal must be depressed to perform the immobilizer authentication.

*: Canada models

Courtesy of HONDA, U.S.A., INC.

Alarm Function

Detects if the doors are opened or closed with the vehicle in the ACCESSORY/ON mode. When the remote is taken out of the vehicle, the keyless buzzer will sound and the gauge control module (Only when the vehicle is in the ON mode) will show a warning. Before the remote battery level falls to the point where the remote cannot be detected, the gauge control module will show a warning and an alarm will sound. Command to display shift to P warning should be transmitted via B-CAN.

Registration Facility

The body control module can store up to 6 remotes using the HDS.

Fault Diagnosis Function

The system has a fault diagnosis function. If any malfunction occurs, the keyless access indicator comes on in the gauge control module.

Customer Emergency

When the engine start/stop button is pressed continuously at least three times or once for 1.5 seconds or longer in an emergency while driving, the engine turns off, and the vehicle mode switches to ACCESSORY. In this mode, the steering wheel remains unlocked (with steering lock).

Panic Function

When you press the PANIC button on the remote, the body control module sounds the horn and activates the exterior lights.

Walk Away Auto Lock Function (If Equipped)

The walk away auto lock system detects where the remote is and locks all doors and the tailgate (if equipped) on the vehicle when all the doors and tailgate are closed and the remote is outside of the vehicle and out of the range.

To operate the walk away auto lock system, it is necessary to enter the auto lock mode.

To enter the auto lock mode, all of the following conditions must be met:

- The vehicle is in the OFF (LOCK) mode.

- All doors including the tailgate (if equipped) are closed.

- The remote is not inside of the vehicle.

- The remote is outside and within 2 m (7 ft) from the vehicle.

The vehicle's buzzer beeps once to confirm that the auto lock mode is engaged.

When the remote is carried beyond 2 m (7 ft) from the vehicle and remains outside of this range for more than 2 seconds, the system engages and locks all of the doors including the tailgate (if equipped). At that time, the keyless buzzer sounds and some exterior lights will flash. However, if the remote remains within 2 m (7 ft) from the vehicle for 30 seconds or more after entering the auto lock mode, the doors and tailgate will automatically lock.

The system does not work under the following conditions:

- The remote is inside of the vehicle.

- If the remote is away more than 2 m (7 ft) from the vehicle after closing all the doors and tailgate (if equipped).

- If a communication error occurs between the remote and the vehicle.

The walk away auto lock system can be cancelled temporarily by customization.

Keyless Access System Operation Manual Customize

The keyless access system can be enabled and disabled by the operation shown in the table. The system is enabled and disabled each time the unlock button is pressed on the remote in the customize mode.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1485: Keyless Access System Description - Failsafe Function

- Title: Keyless Access System Description - Failsafe Function
- Source path: `pages\641.html`
- Chunk ID: `chunk_f9963e1cdc3b`
- Images: none
- Duplicate sources: `pages\2683.html`, `pages\26331.html`, `pages\14332.html`

### Full Text

````text
# Keyless Access System Description - Failsafe Function

If there is a failure in the keyless access system that terminates the keyless access features, the system enters the failsafe mode and displays the keyless access system indicator.
````

## Chunk 1486: Keyless Access System Description - System Diagram (2/4-door)

- Title: Keyless Access System Description - System Diagram (2/4-door)
- Source path: `pages\642.html`
- Chunk ID: `chunk_749b12c179fc`
- Images: `images\GHH411821.jpeg`
- Duplicate sources: `pages\2684.html`, `pages\26332.html`, `pages\14333.html`

### Full Text

````text
# Keyless Access System Description - System Diagram (2/4-door)

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1487: Keyless Access System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\643.html`
- Chunk ID: `chunk_e8062207a3b6`
- Images: `images\GHH411822.jpeg`
- Duplicate sources: `pages\2685.html`, `pages\26333.html`, `pages\14334.html`

### Full Text

````text
# Keyless Access System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1488: Keyless/Power Door Locks/Security System Description - Components (2/4-door)

- Title: Keyless/Power Door Locks/Security System Description - Components (2/4-door)
- Source path: `pages\644.html`
- Chunk ID: `chunk_07c2a3ed63cb`
- Images: `images\GHH411823.jpeg`, `images\GHH411824.jpeg`, `images\GHH411825.jpeg`, `images\GHH411826.jpeg`
- Duplicate sources: `pages\2686.html`, `pages\26334.html`, `pages\14335.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - Components (2/4-door)

Door Lock Switches

The door lock switches are integrated into one unit to the power window master switch, and the front passenger's power window switch.

Door Lock Knob Switch/Door Lock Actuator/Driver's Door Key Cylinder Switch

The door lock knob switch and the door lock actuator are built into the door latch of each door. The door lock knob switch detects the lock and unlock states of the lock mechanism. The door lock actuator moves the lock mechanism back and forth between the lock and unlock position. The actuator receives lock and unlock commands from the body control module. The driver's door key cylinder switch is included in the driver's door latch assembly. In conjunction with the key cylinder, it detects the lock/unlock of the key cylinder.

Front Door Latch

Courtesy of HONDA, U.S.A., INC.

Driver's Door Key Cylinder Switch* | Door Lock Knob Switch

LOCK | UNLOCK | LOCK * | UNLOCK

LOCK | ON | OFF | ON | OFF

Neutral | OFF | OFF | --- | ---

UNLOCK | OFF | ON | OFF | ON

*: Only Driver's Door

Rear Door Latch

Courtesy of HONDA, U.S.A., INC.

Door Lock Knob Switch

LOCK | UNLOCK

LOCK | --- | OFF

UNLOCK | --- | ON

Trunk Lid Release Actuator/Trunk Lid Latch Switch

The body control module receives an ON signal from the trunk lid opener switch or the trunk lid outer handle switch *, then the body control module outputs a signal to the trunk lid release actuator, and the trunk lid release actuator unlocks the trunk latch. The trunk lid latch switch is the ON/OFF switch that detects the opening/closing of the trunk. If the trunk lid release actuator is abnormal, the trunk lid may be opened manually with the release lever.

*: With Keyless Access System

Courtesy of HONDA, U.S.A., INC.

Trunk Lid | Trunk Lid Latch Switch

Open | ON

Close | OFF

Hood Latch Switch

The hood latch switch is built into the hood latch, and it detects the opening/closing of the hood.

Courtesy of HONDA, U.S.A., INC.

Hood | Hood Latch Switch

Open | OFF

Close | ON

Door Switch

The door switch is the ON/OFF switch that detects the opening/closing of the door.

Door | Door Switch

Open | ON

Close | OFF
````

## Chunk 1489: Keyless/Power Door Locks/Security System Description - Components (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Description - Components (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\645.html`
- Chunk ID: `chunk_15065255660f`
- Images: `images\GHH411827.jpeg`, `images\GHH411828.jpeg`, `images\GHH411829.jpeg`, `images\GHH411830.jpeg`
- Duplicate sources: `pages\2687.html`, `pages\26335.html`, `pages\14336.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - Components (5-door) (2017 2018 2019 2020 2021)

Door Lock Switches

The door lock switches are integrated into one unit to the power window master switch, and the front passenger's power window switch.

Door Lock Knob Switch/Door Lock Actuator/Driver's Door Key Cylinder Switch

The door lock knob switch and the door lock actuator are built into the door latch of each door. The door lock knob switch detects the lock and unlock states of the lock mechanism. The door lock actuator moves the lock mechanism back and forth between the lock and unlock position. The actuator receives lock and unlock commands from the body control module. The driver's door key cylinder switch is included in the driver's door latch assembly. In conjunction with the key cylinder, it detects the lock/unlock of the key cylinder.

Front Door Latch

Courtesy of HONDA, U.S.A., INC.

Driver's Door Key Cylinder Switch* | Door Lock Knob Switch

LOCK | UNLOCK | LOCK * | UNLOCK

LOCK | ON | OFF | ON | OFF

Neutral | OFF | OFF | --- | ---

UNLOCK | OFF | ON | OFF | ON

*: Only Driver's Door

Rear Door Latch

Courtesy of HONDA, U.S.A., INC.

Door Lock Knob Switch

LOCK | UNLOCK

LOCK | --- | OFF

UNLOCK | --- | ON

Tailgate Release Actuator/Tailgate Latch Switch

The body control module receives an ON signal from the tailgate outer handle switch, which then outputs a signal to the tailgate release actuator, and unlocks the tailgate latch. The tailgate latch switch is the ON/OFF switch that detects the opening/closing of the tailgate.

Courtesy of HONDA, U.S.A., INC.

Tailgate | Tailgate Latch Switch

Open | ON

Close | OFF

Hood Latch Switch

The hood latch switch is built into the hood latch and it detects the opening/closing of the hood.

Courtesy of HONDA, U.S.A., INC.

Hood | Hood Latch Switch

Open | OFF

Close | ON

Door Switch

The door switch is a ON/OFF type that detects the opening/closing of the door.

Door | Door Switch

Open | ON

Close | OFF
````

## Chunk 1490: Keyless/Power Door Locks/Security System Description - Control/Function (2/4-door)

- Title: Keyless/Power Door Locks/Security System Description - Control/Function (2/4-door)
- Source path: `pages\646.html`
- Chunk ID: `chunk_4758e17f19d7`
- Images: `images\GHH411831.jpeg`, `images\GHH411832.jpeg`, `images\GHH411833.jpeg`, `images\GHH411834.jpeg`, `images\GHH411835.jpeg`, `images\GHH411836.jpeg`, `images\GHH411837.jpeg`, `images\GHH411838.jpeg`, `images\GHH411839.jpeg`, `images\GHH411840.jpeg`, `images\GHH411841.jpeg`
- Duplicate sources: `pages\2688.html`, `pages\26336.html`, `pages\14337.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - Control/Function (2/4-door)

Door Lock Control

The door lock control function allows the body control module to detect the status of various switch signals and control each actuator in order to lock and unlock the doors.

The system has three circuits between door lock actuators and the body control module to improve safety of the system. One is for the driver's door lock actuator, and others are for the left rear door lock actuator and passenger's side door lock actuators. The door lock actuator circuit has two fuses. When one fuse is blown, another fuse in the same circuit must be checked.

Courtesy of HONDA, U.S.A., INC.

Trunk Lid Control

The trunk lid control function allows the body control module to detect the status of various switch signals and control the trunk lid release actuator in order to lock and unlock the trunk.

Courtesy of HONDA, U.S.A., INC.

Keyless Door Lock Control

The keyless transmitter or the remote can transmit a lock or unlock signal to the immobilizer-keyless control unit or the body control module, then the body control module controls the door lock actuator by the B-CAN signal and various switch signal. The customization menu can also set the relock timer value.

Courtesy of HONDA, U.S.A., INC.

Keyless Door Lock Control (Trunk Lid)

The keyless transmitter *1 or the remote *2 can transmit an unlock signal to the immobilizer keyless control unit *1 or the body control module *2, then the body control module controls the trunk lid release actuator.

*1: Without keyless access system

*2: With keyless access system

Courtesy of HONDA, U.S.A., INC.

Key Lockout Prevent Function

The body control module monitors whether or not there is a remote in the vehicle or if there is a key inserted to the ignition key cylinder. If the remote is in the vehicle or if the key is inserted to the ignition key cylinder, the system will not lock the doors. If the driver manually locks and closes the doors with the remote in the vehicle or if the key is inserted to the ignition key cylinder, the body control module energizes the driver's door lock actuator and unlocks the driver's door.

Courtesy of HONDA, U.S.A., INC.

Automatic Door Lock/Unlock Control

The automatic door lock/unlock control function allows the body control module to detect the status of B-CAN signals and various switch signals and controls each actuator in order to automatically lock/unlock the doors.

Automatic Door Lock Function:

- When the vehicle speed exceeds 9 mph (15 km/h). (Default setting)

- When the shift position/mode is out of the P position/mode. (CVT)

Automatic Door Unlock Function:

- When the driver's door switch is ON (door open). (Default setting)

- When the vehicle mode is changed to the OFF (LOCK) mode from the ON mode.

- When the shift position/mode is moved to the P position/mode from other than P position/mode. (CVT)

Customizing Function:

The locking method can be set as non-link, link to vehicle speed, link to shift position/mode, or link to ignition switch or engine start/stop switch by the customizing function. For more information about customize options, refer to the Owner's manual.

Security Control

When the security alarm is set, the body control module sends the security set signal using the B-CAN.

Courtesy of HONDA, U.S.A., INC.

Security system operating term

Start setting | Lock the door using a mechanical key Lock the door by using the keyless transmitter *1 or the remote *2 Lock the door by pressing the door outer handle lock switch while having the remote *2 Operate a keyless relock

- Lock the door using a mechanical key

- Lock the door by using the keyless transmitter *1 or the remote *2

- Lock the door by pressing the door outer handle lock switch while having the remote *2

- Operate a keyless relock

Cancellation | Unlock the door by using the keyless transmitter *1 or the remote *2 Unlock the door by smart function *2 Press the engine start/stop switch button while having the remote

- Unlock the door by using the keyless transmitter *1 or the remote *2

- Unlock the door by smart function *2

- Press the engine start/stop switch button while having the remote
````

## Chunk 1491: Keyless/Power Door Locks/Security System Description - Control/Function (2/4-door)

- Title: Keyless/Power Door Locks/Security System Description - Control/Function (2/4-door)
- Source path: `pages\646.html`
- Chunk ID: `chunk_dcf41fee684d`
- Images: `images\GHH411831.jpeg`, `images\GHH411832.jpeg`, `images\GHH411833.jpeg`, `images\GHH411834.jpeg`, `images\GHH411835.jpeg`, `images\GHH411836.jpeg`, `images\GHH411837.jpeg`, `images\GHH411838.jpeg`, `images\GHH411839.jpeg`, `images\GHH411840.jpeg`, `images\GHH411841.jpeg`
- Duplicate sources: `pages\2688.html`, `pages\26336.html`, `pages\14337.html`

### Full Text

````text
using a mechanical key Lock the door by using the keyless transmitter *1 or the remote *2 Lock the door by pressing the door outer handle lock switch while having the remote *2 Operate a keyless relock

- Lock the door using a mechanical key

- Lock the door by using the keyless transmitter *1 or the remote *2

- Lock the door by pressing the door outer handle lock switch while having the remote *2

- Operate a keyless relock

Cancellation | Unlock the door by using the keyless transmitter *1 or the remote *2 Unlock the door by smart function *2 Press the engine start/stop switch button while having the remote

- Unlock the door by using the keyless transmitter *1 or the remote *2

- Unlock the door by smart function *2

- Press the engine start/stop switch button while having the remote

Setting conditions (related systems are normally operated) | Door switch OFF (Door close) Door unlock knob switch OFF (Lock) Trunk lid latch switch OFF (Trunk close) Driver's door key cylinder switch OFF Hood latch switch ON (Hood close) Vehicle OFF (LOCK) mode Shift P position/mode (CVT)

- Door switch OFF (Door close)

- Door unlock knob switch OFF (Lock)

- Trunk lid latch switch OFF (Trunk close)

- Driver's door key cylinder switch OFF

- Hood latch switch ON (Hood close)

- Vehicle OFF (LOCK) mode

- Shift P position/mode (CVT)

Start the alarm | When any of the monitoring switch signal inputs are received without the signal for cancelling setting

Cancel the alarm | Compliant with the conditions for cancelling setting

*1: Without keyless access system

*2: With keyless access system

Security Setting

When the security alarm is set, the body control module sends the security set signal using the B-CAN. When the gauge control module receives a security set signal from the body control module, the security indicator flashes at a slower pace to indicate the system has armed.

Courtesy of HONDA, U.S.A., INC.

Security Alarm

With the security system armed, manually opening the hood, the trunk, moving the door lock knob to the unlock position, or shifting to other than the P position/mode activates the security alarm. Alternatively, the security alarm sounds, the headlights low beam, the front parking lights, the taillights, the license plate light, and the side marker lights blink, repeating this alarm (one cycle is 120 seconds). Even if you remove the 12 volt battery, the alarming state cannot be changed. The alarm starts again when reinstalling the 12 volt battery.

Courtesy of HONDA, U.S.A., INC.

Answer Back Control

When using the remote, the body control module provides an answer back function to alert the customer that the body control module received a lock or unlock command from the remote or the immobilizer-keyless control unit. When the body control module receives a lock signal, the body control module outputs once to turn on the turn signal lights, and the horn or the keyless buzzer to sound. When the body control module receives an unlock signal, the body control module outputs two times to turn on the turn signal lights, and the horn or the keyless buzzer to sound.

Courtesy of HONDA, U.S.A., INC.

When the body control module receives a lock signal, the body control module sends signals once to the turn signal lights, and the horn or the keyless buzzer will sound once when you press the lock button again within 5 seconds.

Courtesy of HONDA, U.S.A., INC.

When the body control module receives an unlock signal, the body control module sends signals two times to the turn signal lights.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1492: Keyless/Power Door Locks/Security System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\647.html`
- Chunk ID: `chunk_dc9fcddb21c9`
- Images: `images\GHH411842.jpeg`, `images\GHH411843.jpeg`, `images\GHH411844.jpeg`, `images\GHH411845.jpeg`, `images\GHH411846.jpeg`, `images\GHH411847.jpeg`, `images\GHH411848.jpeg`, `images\GHH411849.jpeg`, `images\GHH411850.jpeg`, `images\GHH411851.jpeg`, `images\GHH411852.jpeg`
- Duplicate sources: `pages\2689.html`, `pages\26337.html`, `pages\14338.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

Door Lock Control

The door lock control function allows the body control module to detect the status of various switch signals and controls each actuator in order to lock and unlock the doors.

The system has three circuits between door lock actuators and the body control module to improve safety of the system. One is for the driver's door lock actuator, and others are for the left rear door lock actuator and passenger's side door lock actuators. The door lock actuator circuit has two fuses. When one fuse is blown, another fuse in the same circuit must be checked.

Courtesy of HONDA, U.S.A., INC.

Tailgate Release Control

In the tailgate release function, the body control module activates the tailgate release actuator by the tailgate outer handle switch operation when the vehicle runs at a speed less than 1.2 mph (2 km/h). The tailgate can be unlocked by the tailgate outer handle switch operation without having the remote if all the doors are unlocked.

Courtesy of HONDA, U.S.A., INC.

Keyless Door Lock Control

The keyless transmitter or the remote can transmit a lock or unlock signal to the immobilizer-keyless control unit or the body control module. The body control module then controls the door lock actuator by the B-CAN signal and various switch signals. The customization menu can also set the relock timer value.

Courtesy of HONDA, U.S.A., INC.

Keyless Door Lock Control (Tailgate)

The keyless transmitter or the remote can transmit an unlock signal to the immobilizer-keyless control unit or the body control module. The body control module then activates the tailgate release actuator when the tailgate outer handle switch is operated.

Courtesy of HONDA, U.S.A., INC.

Key Lockout Prevent Function

The body control module monitors whether or not there is a remote in the vehicle or if there is a key inserted to the ignition key cylinder. If the remote is in the vehicle or if the key is inserted to the ignition key cylinder, the system will not lock the doors. If the driver manually locks and closes the doors with the remote in the vehicle or if the key is inserted to the ignition key cylinder, the body control module energizes the driver's door lock actuator and unlocks the driver's door.

Courtesy of HONDA, U.S.A., INC.

Automatic Door Lock/Unlock Control

The automatic door lock/unlock control function allows the body control module to detect the status of B-CAN signals and various switch signals and controls each actuator in order to automatically lock/unlock the doors.

Automatic Door Lock Function:

- When the vehicle speed exceeds 9 mph (15 km/h). (Default setting)

- When the shift position/mode is out of the P position/mode. (CVT)

Automatic Door Unlock Function:

- When the driver's door switch is ON (door open). (Default setting)

- When the vehicle mode is changed to the OFF (LOCK) mode from the ON mode.

- When the shift position/mode is moved to the P position/mode from other than P position/mode. (CVT)

Customizing Function:

The locking method can be set as non-link, link to vehicle speed, link to shift position/mode, or link to ignition switch or engine start/stop switch by the customizing function. For more information about customize options, refer to the Owner's manual.

Security Control

When the security alarm is set, the body control module sends the security set signal using the B-CAN.

Courtesy of HONDA, U.S.A., INC.

Security system operating term

Start setting | Lock the door using a mechanical key Lock the door by using the keyless transmitter *1 or the remote *2 Lock the door by pressing the door outer handle lock switch while having the remote *2 Operate a keyless relock

- Lock the door using a mechanical key

- Lock the door by using the keyless transmitter *1 or the remote *2

- Lock the door by pressing the door outer handle lock switch while having the remote *2

- Operate a keyless relock

Cancellation | Unlock the door by using the mechanical key Unlock the door or tailgate by using the keyless transmitter *1 or the remote *2 Unlock the door or tailgate by smart function *2 Press the engine start/stop switch button while having the remote

- Unlock the door by using the mechanical key

- Unlock the door or tailgate by using the keyless transmitter *1 or the remote *2

- Unlock the door or tailgate by smart function *2
````

## Chunk 1493: Keyless/Power Door Locks/Security System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Description - Control/Function (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\647.html`
- Chunk ID: `chunk_d529accdd1e1`
- Images: `images\GHH411842.jpeg`, `images\GHH411843.jpeg`, `images\GHH411844.jpeg`, `images\GHH411845.jpeg`, `images\GHH411846.jpeg`, `images\GHH411847.jpeg`, `images\GHH411848.jpeg`, `images\GHH411849.jpeg`, `images\GHH411850.jpeg`, `images\GHH411851.jpeg`, `images\GHH411852.jpeg`
- Duplicate sources: `pages\2689.html`, `pages\26337.html`, `pages\14338.html`

### Full Text

````text
*1 or the remote *2 Lock the door by pressing the door outer handle lock switch while having the remote *2 Operate a keyless relock

- Lock the door using a mechanical key

- Lock the door by using the keyless transmitter *1 or the remote *2

- Lock the door by pressing the door outer handle lock switch while having the remote *2

- Operate a keyless relock

Cancellation | Unlock the door by using the mechanical key Unlock the door or tailgate by using the keyless transmitter *1 or the remote *2 Unlock the door or tailgate by smart function *2 Press the engine start/stop switch button while having the remote

- Unlock the door by using the mechanical key

- Unlock the door or tailgate by using the keyless transmitter *1 or the remote *2

- Unlock the door or tailgate by smart function *2

- Press the engine start/stop switch button while having the remote

Setting conditions (related systems are normally operated) | Door switch OFF (Door close) Door unlock knob switch OFF (Lock) Tailgate latch switch OFF (Tailgate close) Driver's door key cylinder switch OFF Hood latch switch ON (Hood close) Vehicle OFF (LOCK) mode Shift P position/mode (CVT)

- Door switch OFF (Door close)

- Door unlock knob switch OFF (Lock)

- Tailgate latch switch OFF (Tailgate close)

- Driver's door key cylinder switch OFF

- Hood latch switch ON (Hood close)

- Vehicle OFF (LOCK) mode

- Shift P position/mode (CVT)

Start the alarm | When any of the monitoring switch signal inputs are received without the signal for cancelling setting

Cancel the alarm | Compliant with the conditions for cancelling setting

*1: Without keyless access system

*2: With keyless access system

Security Setting

When the security alarm is set, the body control module sends the security set signal using the B-CAN. When the gauge control module receives a security set signal from the body control module, the security indicator flashes at a slower pace to indicate the system has armed.

Courtesy of HONDA, U.S.A., INC.

Security Alarm

With the security system armed, manually opening the hood, the tailgate, moving the door lock knob to the unlock position, or shifting to other than the P position/mode activates the security alarm. During activation, the security alarm sounds, the headlights low beam, the front parking lights, the taillights, the license plate light, and the side marker lights blink, repeating this alarm (one cycle is 120 seconds). Even if you remove the 12 volt battery, the alarming state cannot be changed. The alarm starts again when reinstalling the 12 volt battery.

Courtesy of HONDA, U.S.A., INC.

Answer Back Control

When using the remote or the keyless transmitter, the body control module provides an answer back function to alert the customer that the body control module received a lock or unlock command. When the body control module receives a lock signal, the body control module outputs once to turn on the turn signal lights, and the horn or the keyless buzzer to sound. When the body control module receives an unlock signal, the body control module outputs two times to turn on the turn signal lights, and the horn or the keyless buzzer to sound.

Courtesy of HONDA, U.S.A., INC.

When the body control module receives a lock signal, the body control module sends signals once to the turn signal lights, and the horn or the keyless buzzer will sound once when you press the lock button again within 5 seconds.

Courtesy of HONDA, U.S.A., INC.

When the body control module receives an unlock signal, the body control module sends signals two times to the turn signal lights.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1494: Keyless/Power Door Locks/Security System Description - Overview

- Title: Keyless/Power Door Locks/Security System Description - Overview
- Source path: `pages\648.html`
- Chunk ID: `chunk_e42f9c456ce3`
- Images: none
- Duplicate sources: `pages\2690.html`, `pages\26338.html`, `pages\14339.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - Overview

Keyless Entry System

The keyless entry system allows you to lock and unlock the vehicle with the transmitter. When you press the LOCK button, all doors lock. When you press the UNLOCK button once, only the driver's door unlocks. The other doors will unlock when you press the button a second time. (Depending on the settings in the multi-information display (MID) *1, or center display *2 all the doors may unlock when you press the button the first time). The doors will not lock with the transmitter if a door is not fully closed, or if the vehicle is in the ON mode.

When the switch for the interior light is in the DOOR position, it comes on when the UNLOCK button is pressed.

If a door is not opened, the light goes off and the doors will relock in about 30 seconds. If the doors are locked with the transmitter within 30 seconds, the light goes off immediately.

NOTE: The keyless entry system can be customized in the multi-information display (MID) *1 or center display *2 to suit the customer's needs. For more information about keyless/security system options, refer to the Owner's Manual.

*1: With color audio type (5-inch screen)

*2: With display audio type (7-inch screen)
````

## Chunk 1495: Keyless/Power Door Locks/Security System Description - System Diagram (2/4-door)

- Title: Keyless/Power Door Locks/Security System Description - System Diagram (2/4-door)
- Source path: `pages\649.html`
- Chunk ID: `chunk_2003236355ea`
- Images: `images\GHH411853.jpeg`
- Duplicate sources: `pages\2691.html`, `pages\26339.html`, `pages\14340.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - System Diagram (2/4-door)

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1496: Keyless/Power Door Locks/Security System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\650.html`
- Chunk ID: `chunk_f4098ecdc7e1`
- Images: `images\GHH411854.jpeg`
- Duplicate sources: `pages\2692.html`, `pages\26340.html`, `pages\14341.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Description - System Diagram (5-door) (2017 2018 2019 2020 2021)

For locations of each component on the vehicle, refer to the Component Location Index

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1497: All the doors will not lock and unlock

- Title: All the doors will not lock and unlock
- Source path: `pages\651.html`
- Chunk ID: `chunk_013f6f9ce6ca`
- Images: none
- Duplicate sources: `pages\2693.html`, `pages\26341.html`, `pages\14342.html`

### Full Text

````text
# All the doors will not lock and unlock

Diagnostic procedure

- Symptom troubleshooting

Also check for

- Body control module

- LF antenna

- Driver's door lock knob switch

- Door outer handle touch sensor/lock switch

- Door lock actuators

- Keyless remote

- Low or weak keyless remote battery

- Not registered
````

## Chunk 1498: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (2-door) (2016 2017 2018 2019 2020)

- Title: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\652.html`
- Chunk ID: `chunk_588d6c0f0874`
- Images: none
- Duplicate sources: `pages\2694.html`, `pages\26342.html`, `pages\14343.html`

### Full Text

````text
# All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (2-door) (2016 2017 2018 2019 2020)

Check Items

- Poor ground (G501)

- Blown No. B16 (20 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test
````

## Chunk 1499: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (4-door)

- Title: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (4-door)
- Source path: `pages\653.html`
- Chunk ID: `chunk_ccab8c2e9c02`
- Images: none
- Duplicate sources: `pages\2695.html`, `pages\26343.html`, `pages\14344.html`

### Full Text

````text
# All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (4-door)

Check Items

- Poor ground (G501, G305 *)

- Blown No. B16 fuse

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test
````

## Chunk 1500: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (5-door) (2017 2018 2019 2020 2021)

- Title: All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\654.html`
- Chunk ID: `chunk_3d5f7d7ad7aa`
- Images: none
- Duplicate sources: `pages\2696.html`, `pages\26344.html`, `pages\14345.html`

### Full Text

````text
# All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote (5-door) (2017 2018 2019 2020 2021)

Check Items

- Poor ground (G305, G501)

- Blown No. B16 (20 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test
````

## Chunk 1501: Auto door unlock does not work (2-door) (2016 2017 2018 2019 2020)

- Title: Auto door unlock does not work (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\655.html`
- Chunk ID: `chunk_07e472179317`
- Images: none
- Duplicate sources: `pages\2697.html`, `pages\26345.html`, `pages\14346.html`

### Full Text

````text
# Auto door unlock does not work (2-door) (2016 2017 2018 2019 2020)

Check Items

- Symptom troubleshooting
````

## Chunk 1502: Auto door unlock does not work (5-door) (2017 2018 2019 2020 2021)

- Title: Auto door unlock does not work (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\657.html`
- Chunk ID: `chunk_c08b5473f663`
- Images: none
- Duplicate sources: `pages\2699.html`, `pages\26347.html`, `pages\14348.html`

### Full Text

````text
# Auto door unlock does not work (5-door) (2017 2018 2019 2020 2021)

Check Items

- Symptom troubleshooting
````

## Chunk 1503: Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch

- Title: Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch
- Source path: `pages\658.html`
- Chunk ID: `chunk_2e55b42bc52f`
- Images: none
- Duplicate sources: `pages\2700.html`, `pages\26348.html`, `pages\14349.html`

### Full Text

````text
# Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch

Diagnostic procedure

- Symptom troubleshooting (Without electric steering lock)

- Symptom troubleshooting (With electric steering lock)

Also check for

- Check the No. A1-7 (125 A), No. A1-5 (30 A), No. A2-2 (30 A), No. A2-4 (60 A), and No. A18 (10 A) fuses in the under-hood fuse/relay box

- Check the No. B30 (10 A) fuse in the under-dash fuse/relay box

- Poor connections at the body control module

- Keyless remote

- Body control module

- Electric steering lock *2

- Engine start/stop switch

- Harness/connections
````

## Chunk 1504: Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch

- Title: Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch
- Source path: `pages\659.html`
- Chunk ID: `chunk_d52ccf4b08bf`
- Images: none
- Duplicate sources: `pages\2701.html`, `pages\26349.html`, `pages\14350.html`

### Full Text

````text
# Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch

Diagnostic procedure

- Symptom troubleshooting

Also check for

- Body control module

- LF antenna

- Keyless remote

- Low or weak keyless remote battery

- Harness/connections
````

## Chunk 1505: Cannot select ON mode with the keyless remote touching the engine start/stop switch, but can select ON mode with keyless access

- Title: Cannot select ON mode with the keyless remote touching the engine start/stop switch, but can select ON mode with keyless access
- Source path: `pages\660.html`
- Chunk ID: `chunk_296e150c8b85`
- Images: none
- Duplicate sources: `pages\2702.html`, `pages\26350.html`, `pages\14351.html`

### Full Text

````text
# Cannot select ON mode with the keyless remote touching the engine start/stop switch, but can select ON mode with keyless access

Diagnostic procedure

- Check the body control module

Also check for

- Body control module is not registered

- Body control module

- MTR CONT line power short *2

- ESL ID mismatch *2

- MTR CONT line open/short *2

- IGN TRX line open/short *2

- Not registered

- Harness/connections
````

## Chunk 1506: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)

- Title: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\661.html`
- Chunk ID: `chunk_89dcb64391d4`
- Images: none
- Duplicate sources: `pages\2703.html`, `pages\26351.html`, `pages\14352.html`

### Full Text

````text
# Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (2-door) (2016 2017 2018 2019 2020)

Check Items

- Symptom troubleshooting
````

## Chunk 1507: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)

- Title: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)
- Source path: `pages\662.html`
- Chunk ID: `chunk_83a89bcd7c7e`
- Images: none
- Duplicate sources: `pages\2704.html`, `pages\26352.html`, `pages\14353.html`

### Full Text

````text
# Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (4-door)

Check Items

- Symptom troubleshooting
````

## Chunk 1508: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)

- Title: Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\663.html`
- Chunk ID: `chunk_f17b1d10f3d1`
- Images: none
- Duplicate sources: `pages\2705.html`, `pages\26353.html`, `pages\14354.html`

### Full Text

````text
# Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened (5-door) (2017 2018 2019 2020 2021)

Check Items

- Symptom troubleshooting
````

## Chunk 1509: Driver's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)

- Title: Driver's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\664.html`
- Chunk ID: `chunk_e0848b730863`
- Images: none
- Duplicate sources: `pages\2706.html`, `pages\26354.html`, `pages\14355.html`

### Full Text

````text
# Driver's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)

Check Items

- Poor ground (G501)

- Blown No. B25 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B39 (10 A) fuse in the under-dash fuse/relay box

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test
````

## Chunk 1510: Driver's door will not lock or unlock (4-door)

- Title: Driver's door will not lock or unlock (4-door)
- Source path: `pages\665.html`
- Chunk ID: `chunk_58a05f36215c`
- Images: none
- Duplicate sources: `pages\2707.html`, `pages\26355.html`, `pages\14356.html`

### Full Text

````text
# Driver's door will not lock or unlock (4-door)

Check Items

- Poor ground (G501)

- Blown No. B25 fuse

- Blown No. B39 fuse

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test
````

## Chunk 1511: Driver's door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

- Title: Driver's door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\666.html`
- Chunk ID: `chunk_679dcde57712`
- Images: none
- Duplicate sources: `pages\2708.html`, `pages\26356.html`, `pages\14357.html`

### Full Text

````text
# Driver's door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

Check Items

- Poor ground (G501)

- Blown No. B25 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B39 (10 A) fuse in the under-dash fuse/relay box

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test
````

## Chunk 1512: Engine does not crank (power supply is normal)

- Title: Engine does not crank (power supply is normal)
- Source path: `pages\667.html`
- Chunk ID: `chunk_81c009b3a2a4`
- Images: none
- Duplicate sources: `pages\2709.html`, `pages\26357.html`, `pages\14358.html`

### Full Text

````text
# Engine does not crank (power supply is normal)

Diagnostic procedure

- Check the brake pedal position switch

- Check the body control module

Also check for

- Body control module

- STS line open/short

- Brake pedal position switch

- STOP SW line open/short
````

## Chunk 1513: Engine start/stop switch does not work

- Title: Engine start/stop switch does not work
- Source path: `pages\668.html`
- Chunk ID: `chunk_bfa3611dd197`
- Images: none
- Duplicate sources: `pages\2710.html`, `pages\26358.html`, `pages\14359.html`

### Full Text

````text
# Engine start/stop switch does not work

Diagnostic procedure

- Check for DTCs. If any DTC is indicated, go to the DTC troubleshooting

Also check for

- ACC relay circuit

- Body control module

- Engine start/stop switch

- SS1(+) line short

- SS2(-) line short

- Harness
````

## Chunk 1514: Front passenger's and right rear doors will not lock or unlock (4-door)

- Title: Front passenger's and right rear doors will not lock or unlock (4-door)
- Source path: `pages\669.html`
- Chunk ID: `chunk_32e41f4e69eb`
- Images: none
- Duplicate sources: `pages\2711.html`, `pages\26359.html`, `pages\14360.html`

### Full Text

````text
# Front passenger's and right rear doors will not lock or unlock (4-door)

Check Items

- Poor ground (G505, G602)

- Blown No. B12 fuse

- Blown No. B26 fuse

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test
````

## Chunk 1515: Front passenger's and right rear doors will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

- Title: Front passenger's and right rear doors will not lock or unlock (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\670.html`
- Chunk ID: `chunk_dd2245c7d5c4`
- Images: none
- Duplicate sources: `pages\2712.html`, `pages\26360.html`, `pages\14361.html`

### Full Text

````text
# Front passenger's and right rear doors will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

Check Items

- Poor ground (G505, G602)

- Blown No. B12 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B26 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test
````

## Chunk 1516: Left rear door will not lock or unlock (4-door)

- Title: Left rear door will not lock or unlock (4-door)
- Source path: `pages\671.html`
- Chunk ID: `chunk_6be885f202fb`
- Images: none
- Duplicate sources: `pages\2713.html`, `pages\26361.html`, `pages\14362.html`

### Full Text

````text
# Left rear door will not lock or unlock (4-door)

Check Items

- Poor ground (G601)

- Blown No. B13 fuse

- Blown No. B38 fuse

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Left rear door lock actuator test
````

## Chunk 1517: Left rear door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

- Title: Left rear door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\672.html`
- Chunk ID: `chunk_8dbb93e3298f`
- Images: none
- Duplicate sources: `pages\2714.html`, `pages\26362.html`, `pages\14363.html`

### Full Text

````text
# Left rear door will not lock or unlock (5-door) (2017 2018 2019 2020 2021)

Check Items

- Poor ground (G601)

- Blown No. B13 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B38 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Left rear door lock actuator test
````

## Chunk 1518: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (2-door) (2016 2017 2018 2019 2020)

- Title: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\673.html`
- Chunk ID: `chunk_1543b785d58e`
- Images: none
- Duplicate sources: `pages\2715.html`, `pages\26363.html`, `pages\14364.html`

### Full Text

````text
# Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (2-door) (2016 2017 2018 2019 2020)

Check Items

- Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)
````

## Chunk 1519: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (4-door)

- Title: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (4-door)
- Source path: `pages\674.html`
- Chunk ID: `chunk_c03b81789d4a`
- Images: none
- Duplicate sources: `pages\2716.html`, `pages\26364.html`, `pages\14365.html`

### Full Text

````text
# Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (4-door)

Check Items

- Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)
````

## Chunk 1520: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (5-door) (2017 2018 2019 2020 2021)

- Title: Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\675.html`
- Chunk ID: `chunk_61126c828074`
- Images: none
- Duplicate sources: `pages\2717.html`, `pages\26365.html`, `pages\14366.html`

### Full Text

````text
# Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch (5-door) (2017 2018 2019 2020 2021)

Check Items

- Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)
````

## Chunk 1521: Passenger's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)

- Title: Passenger's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\676.html`
- Chunk ID: `chunk_5a2dfedd939e`
- Images: none
- Duplicate sources: `pages\2718.html`, `pages\26366.html`, `pages\14367.html`

### Full Text

````text
# Passenger's door will not lock or unlock (2-door) (2016 2017 2018 2019 2020)

Check Items

- Poor ground (G505)

- Blown No. B12 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B26 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test
````

## Chunk 1522: Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

- Title: Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\677.html`
- Chunk ID: `chunk_16eb05a90f55`
- Images: none
- Duplicate sources: `pages\2719.html`, `pages\26367.html`, `pages\14368.html`

### Full Text

````text
# Security alarm system will not arm (2-door) (2016 2017 2018 2019 2020)

Check Items

- Symptom troubleshooting
````

## Chunk 1523: Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

- Title: Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\679.html`
- Chunk ID: `chunk_5c9cedf4fada`
- Images: none
- Duplicate sources: `pages\2721.html`, `pages\26369.html`, `pages\14370.html`

### Full Text

````text
# Security alarm system will not arm (5-door) (2017 2018 2019 2020 2021)

Check Items

- Symptom troubleshooting
````

## Chunk 1524: Security indicator blinks

- Title: Security indicator blinks
- Source path: `pages\680.html`
- Chunk ID: `chunk_5f7b6096413d`
- Images: none
- Duplicate sources: `pages\2722.html`, `pages\26370.html`, `pages\14371.html`

### Full Text

````text
# Security indicator blinks

Diagnostic procedure

- Symptom troubleshooting

Also check for

- Gauge control module

- Body control module

- PCM

- Harness/connections
````

## Chunk 1525: The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote

- Title: The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote
- Source path: `pages\681.html`
- Chunk ID: `chunk_b2fd351552be`
- Images: none
- Duplicate sources: `pages\2723.html`, `pages\26371.html`, `pages\14372.html`

### Full Text

````text
# The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote

Diagnostic procedure

- Symptom troubleshooting

Also check for

- Door outer handle touch sensor/lock switch

- Body control module

- Keyless remote

- Not registered

- Harness/connections
````

## Chunk 1526: The doors will not unlock or lock with the keyless remote, but will unlock or lock with the door outer handles

- Title: The doors will not unlock or lock with the keyless remote, but will unlock or lock with the door outer handles
- Source path: `pages\682.html`
- Chunk ID: `chunk_0700873fe437`
- Images: none
- Duplicate sources: `pages\2724.html`, `pages\26372.html`, `pages\14373.html`

### Full Text

````text
# The doors will not unlock or lock with the keyless remote, but will unlock or lock with the door outer handles

Diagnostic procedure

- Symptom troubleshooting

Also check for

- Keyless remote battery dead

- Keyless remote

- Body control module

- Harness/connections

- B-CAN communication line
````

## Chunk 1527: The engine starts, but stalls immediately

- Title: The engine starts, but stalls immediately
- Source path: `pages\683.html`
- Chunk ID: `chunk_868f4bb429a4`
- Images: none
- Duplicate sources: `pages\2725.html`, `pages\26373.html`, `pages\14374.html`

### Full Text

````text
# The engine starts, but stalls immediately

Diagnostic procedure

- Symptom troubleshooting

Also check for

- No power to PCM

- No power to body control module

- Body control module

- Gauge control module

- Electric steering lock *2

- Harness/connections
````

## Chunk 1528: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (2-door) (2016 2017 2018 2019 2020)

- Title: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\684.html`
- Chunk ID: `chunk_4e9f63a0ae16`
- Images: none
- Duplicate sources: `pages\2726.html`, `pages\26374.html`, `pages\14375.html`

### Full Text

````text
# The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (2-door) (2016 2017 2018 2019 2020)

Check Items

- Symptom troubleshooting
````

## Chunk 1529: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (4-door)

- Title: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (4-door)
- Source path: `pages\685.html`
- Chunk ID: `chunk_666db8253845`
- Images: none
- Duplicate sources: `pages\2727.html`, `pages\26375.html`, `pages\14376.html`

### Full Text

````text
# The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (4-door)

Check Items

- Symptom troubleshooting
````

## Chunk 1530: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (5-door) (2017 2018 2019 2020 2021)

- Title: The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\686.html`
- Chunk ID: `chunk_cc3065e48292`
- Images: none
- Duplicate sources: `pages\2728.html`, `pages\26376.html`, `pages\14377.html`

### Full Text

````text
# The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed (5-door) (2017 2018 2019 2020 2021)

Check Items

- Symptom troubleshooting
````

## Chunk 1531: The mode changes between ACCESSORY and ON, but it does not change to OFF

- Title: The mode changes between ACCESSORY and ON, but it does not change to OFF
- Source path: `pages\687.html`
- Chunk ID: `chunk_7cb1caf87975`
- Images: none
- Duplicate sources: `pages\2729.html`, `pages\26377.html`, `pages\14378.html`

### Full Text

````text
# The mode changes between ACCESSORY and ON, but it does not change to OFF

Diagnostic procedure

- Check the body control module

- Check the park pin switch

- Check the transmission range switch *1

Also check for

- Body control module

- ATP-P line open *1

- Transmission range switch *1

- Park pin switch *1

- P-PIN SW line open *1
````

## Chunk 1532: The mode changes between ACCESSORY and ON, but it is difficult to change to OFF

- Title: The mode changes between ACCESSORY and ON, but it is difficult to change to OFF
- Source path: `pages\688.html`
- Chunk ID: `chunk_42493ca5eaba`
- Images: none
- Duplicate sources: `pages\2730.html`, `pages\26378.html`, `pages\14379.html`

### Full Text

````text
# The mode changes between ACCESSORY and ON, but it is difficult to change to OFF

Diagnostic procedure

- Check the body control module

- Check the gauge control module

- Check the park pin switch *1

Also check for

- Gauge control module

- Body control module

- PCM

- B-CAN communication line open/short

- F-CAN communication line open/short

- Speed signal line open

- Park pin switch *1

- P-PIN SW line open *1
````

## Chunk 1533: The security system sounds randomly while the doors are locked (2-door) (2016 2017 2018 2019 2020)

- Title: The security system sounds randomly while the doors are locked (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\689.html`
- Chunk ID: `chunk_cc3108cb5468`
- Images: none
- Duplicate sources: `pages\2731.html`, `pages\26379.html`, `pages\14380.html`

### Full Text

````text
# The security system sounds randomly while the doors are locked (2-door) (2016 2017 2018 2019 2020)

Check Items

- Tripped sensor recall
````

## Chunk 1534: The security system sounds randomly while the doors are locked (4-door)

- Title: The security system sounds randomly while the doors are locked (4-door)
- Source path: `pages\690.html`
- Chunk ID: `chunk_185ffc5135c0`
- Images: none
- Duplicate sources: `pages\2732.html`, `pages\26380.html`, `pages\14381.html`

### Full Text

````text
# The security system sounds randomly while the doors are locked (4-door)

Check Items

- Tripped sensor recall
````

## Chunk 1535: The security system sounds randomly while the doors are locked (5-door) (2017 2018 2019 2020 2021)

- Title: The security system sounds randomly while the doors are locked (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\691.html`
- Chunk ID: `chunk_cd2612fd4094`
- Images: none
- Duplicate sources: `pages\2733.html`, `pages\26381.html`, `pages\14382.html`

### Full Text

````text
# The security system sounds randomly while the doors are locked (5-door) (2017 2018 2019 2020 2021)

Check Items

- Tripped sensor recall
````

## Chunk 1536: Keyless Access System Touch Sensor Circuit Troubleshooting

- Title: Keyless Access System Touch Sensor Circuit Troubleshooting
- Source path: `pages\692.html`
- Chunk ID: `chunk_adcb465ccd87`
- Images: `images\GHH411855.jpeg`, `images\GHH411856.jpeg`, `images\GHH411857.jpeg`, `images\GHH411858.jpeg`, `images\GHH411859.jpeg`, `images\GHH411860.jpeg`
- Duplicate sources: `pages\2734.html`, `pages\26382.html`, `pages\14383.html`

### Full Text

````text
# Keyless Access System Touch Sensor Circuit Troubleshooting

NOTE: Front passenger's *1 is for 4-door, passenger's *2 is for 2-door.

- Keyless access system check -1. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter HISTORY DATA. One-Push - KEYLESS ACCESS CONTROL UNIT- HISTORY DATA -2. Select HISTORY CLEAR, and back to TEST MODE menu: NOTE: When the freeze data is cleared, the information indicates "NOT CONFIRMED". DRIVER DOOR UNLOCK SWITCH DRIVER DOOR LOCK SWITCH FRONT PASSENGER DOOR UNLOCK SWITCH FRONT PASSENGER DOOR LOCK SWITCH -3. Turn the vehicle to the OFF (LOCK) mode. -4. Get out of the vehicle with the keyless remote, and touch the each door outer handle touch sensor and push the lock button. -5. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter HISTORY DATA. One-Push - KEYLESS ACCESS CONTROL UNIT- HISTORY DATA -6. Recheck HISTORY DATA. DRIVER DOOR UNLOCK SWITCH DRIVER DOOR LOCK SWITCH FRONT PASSENGER DOOR UNLOCK SWITCH FRONT PASSENGER DOOR LOCK SWITCH Is all the information OK? YES Intermittent failure, the system is OK at this time. NO Go to step 2.

-1. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter HISTORY DATA.

One-Push - KEYLESS ACCESS CONTROL UNIT- HISTORY DATA

-2. Select HISTORY CLEAR, and back to TEST MODE menu:

NOTE: When the freeze data is cleared, the information indicates "NOT CONFIRMED".

- DRIVER DOOR UNLOCK SWITCH

- DRIVER DOOR LOCK SWITCH

- FRONT PASSENGER DOOR UNLOCK SWITCH

- FRONT PASSENGER DOOR LOCK SWITCH

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Get out of the vehicle with the keyless remote, and touch the each door outer handle touch sensor and push the lock button.

-5. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter HISTORY DATA.

One-Push - KEYLESS ACCESS CONTROL UNIT- HISTORY DATA

-6. Recheck HISTORY DATA.

- DRIVER DOOR UNLOCK SWITCH

- DRIVER DOOR LOCK SWITCH

- FRONT PASSENGER DOOR UNLOCK SWITCH

- FRONT PASSENGER DOOR LOCK SWITCH

Is all the information OK?

YES

Intermittent failure, the system is OK at this time.

NO

Go to step 2.

- Open wire check (GND line) -1. Disconnect the following connectors. Each door outer handle 8P connectors -2. Check for continuity between test points 1 and 2 individually. Driver's door Test condition Vehicle OFF (LOCK) mode Driver's door outer handle 8P connector: disconnected Test point 1 Driver's door outer handle 8P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Front passenger's *1/passenger's *2 door Test condition Vehicle OFF (LOCK) mode Front passenger's *1/passenger's *2 door outer handle 8P connector: disconnected Test point 1 Front passenger's *1/passenger's *2 door outer handle 8P connector No. 8 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wires are OK. Go to step 3. NO Repair an open or high resistance in the ground wire or poor ground (G501, G505).

-1. Disconnect the following connectors.

Each door outer handle 8P connectors

-2. Check for continuity between test points 1 and 2 individually.

Driver's door

Test condition | Vehicle OFF (LOCK) mode Driver's door outer handle 8P connector: disconnected

Test point 1 | Driver's door outer handle 8P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Front passenger's *1/passenger's *2 door

Test condition | Vehicle OFF (LOCK) mode Front passenger's *1/passenger's *2 door outer handle 8P connector: disconnected

Test point 1 | Front passenger's *1/passenger's *2 door outer handle 8P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wires are OK. Go to step 3.

NO

Repair an open or high resistance in the ground wire or poor ground (G501, G505).

- Determine possible failure area (TS line, VOUT line) -1. Measure the voltage between test points 1 and 2 individually. Driver's door Test condition Vehicle OFF (LOCK) mode Driver's door outer handle 8P connector: disconnected Test point 1 Driver's door outer handle 8P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1537: Keyless Access System Touch Sensor Circuit Troubleshooting

- Title: Keyless Access System Touch Sensor Circuit Troubleshooting
- Source path: `pages\692.html`
- Chunk ID: `chunk_3ecb49ef8b88`
- Images: `images\GHH411855.jpeg`, `images\GHH411856.jpeg`, `images\GHH411857.jpeg`, `images\GHH411858.jpeg`, `images\GHH411859.jpeg`, `images\GHH411860.jpeg`
- Duplicate sources: `pages\2734.html`, `pages\26382.html`, `pages\14383.html`

### Full Text

````text
senger's *1/passenger's *2 door

Test condition | Vehicle OFF (LOCK) mode Front passenger's *1/passenger's *2 door outer handle 8P connector: disconnected

Test point 1 | Front passenger's *1/passenger's *2 door outer handle 8P connector No. 8

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wires are OK. Go to step 3.

NO

Repair an open or high resistance in the ground wire or poor ground (G501, G505).

- Determine possible failure area (TS line, VOUT line) -1. Measure the voltage between test points 1 and 2 individually. Driver's door Test condition Vehicle OFF (LOCK) mode Driver's door outer handle 8P connector: disconnected Test point 1 Driver's door outer handle 8P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Front passenger's *1/passenger's *2 door Test condition Vehicle OFF (LOCK) mode Front passenger's *1/passenger's *2 door outer handle 8P connector: disconnected Test point 1 Front passenger's *1/passenger's *2 door outer handle 8P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 4. NO Go to step 7.

-1. Measure the voltage between test points 1 and 2 individually.

Driver's door

Test condition | Vehicle OFF (LOCK) mode Driver's door outer handle 8P connector: disconnected

Test point 1 | Driver's door outer handle 8P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Front passenger's *1/passenger's *2 door

Test condition | Vehicle OFF (LOCK) mode Front passenger's *1/passenger's *2 door outer handle 8P connector: disconnected

Test point 1 | Front passenger's *1/passenger's *2 door outer handle 8P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 4.

NO

Go to step 7.

- Open wire check (TS FR DR, TS FR AS lines) -1. Disconnect the following connector. Body control module connector G (32P) -2. Connect terminals A and B with jumper wires. Driver's door Terminal A Driver's door outer handle 8P connector No. 3 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. Front passenger's *1/passenger's *2 door Terminal A Front passenger's *1/passenger's *2 door outer handle 8P connector No. 3 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2 individually. Test condition Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Each door outer handle 8P connectors: jumped to body ground Body control module connector G (32P): disconnected Test point 1 Body control module connector G (32P) No. 22 Test point 2 Body ground Test point 1 Body control module connector G (32P) No. 25 Test point 2 Body ground Is there continuity? YES The TS FR DR and TS FR AS wires are not open. Go to step 5. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connector.

Body control module connector G (32P)

-2. Connect terminals A and B with jumper wires.

Driver's door

Terminal A | Driver's door outer handle 8P connector No. 3

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

Front passenger's *1/passenger's *2 door

Terminal A | Front passenger's *1/passenger's *2 door outer handle 8P connector No. 3

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2 individually.

Test condition | Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Each door outer handle 8P connectors: jumped to body ground Body control module connector G (32P): disconnected

Test point 1 | Body control module connector G (32P) No. 22

Test point 2 | Body ground

Test point 1 | Body control module connector G (32P) No. 25

Test point 2 | Body ground

Is there continuity?

YES

The TS FR DR and TS FR AS wires are not open. Go to step 5.

NO

Repair an open or high resistance in the wire.

- Shorted wire check (TS FR DR, TS FR AS lines) -1. Remove the jumper wires from the door outer handle connectors. -2. Check for continuity between test points 1 and 2 individually. Test condition Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Body control module connector G (32P): disconnected Test point 1 Body control module connector G (32P) No. 22 Test point 2 Body ground Test point 1 Body control module connector G (32P) No. 25 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire.
````

## Chunk 1538: Keyless Access System Touch Sensor Circuit Troubleshooting

- Title: Keyless Access System Touch Sensor Circuit Troubleshooting
- Source path: `pages\692.html`
- Chunk ID: `chunk_a2a4ef181b53`
- Images: `images\GHH411855.jpeg`, `images\GHH411856.jpeg`, `images\GHH411857.jpeg`, `images\GHH411858.jpeg`, `images\GHH411859.jpeg`, `images\GHH411860.jpeg`
- Duplicate sources: `pages\2734.html`, `pages\26382.html`, `pages\14383.html`

### Full Text

````text
t 2 | Body ground

Test point 1 | Body control module connector G (32P) No. 25

Test point 2 | Body ground

Is there continuity?

YES

The TS FR DR and TS FR AS wires are not open. Go to step 5.

NO

Repair an open or high resistance in the wire.

- Shorted wire check (TS FR DR, TS FR AS lines) -1. Remove the jumper wires from the door outer handle connectors. -2. Check for continuity between test points 1 and 2 individually. Test condition Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Body control module connector G (32P): disconnected Test point 1 Body control module connector G (32P) No. 22 Test point 2 Body ground Test point 1 Body control module connector G (32P) No. 25 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The TS FR DR and TS FR AS wires are OK. Go to step 6.

-1. Remove the jumper wires from the door outer handle connectors.

-2. Check for continuity between test points 1 and 2 individually.

Test condition | Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Body control module connector G (32P): disconnected

Test point 1 | Body control module connector G (32P) No. 22

Test point 2 | Body ground

Test point 1 | Body control module connector G (32P) No. 25

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The TS FR DR and TS FR AS wires are OK. Go to step 6.

- Door outer handle touch sensor check (substitution) -1. Substitute a known-good door outer handle touch sensor, and recheck. Is the system OK? YES Faulty the original door outer handle touch sensor; replace the door outer handle . NO Replace the body control module .

-1. Substitute a known-good door outer handle touch sensor, and recheck.

Is the system OK?

YES

Faulty the original door outer handle touch sensor; replace the door outer handle .

NO

Replace the body control module .

- Open wire check (VOUT FR DR, VOUT FR AS lines) -1. Measure the voltage between test points 1 and 2 individually. Test condition Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected Test point 1 Body control module connector G (32P) No. 31 Test point 2 Body ground Test point 1 Body control module connector G (32P) No. 30 Test point 2 Body ground Is there battery voltage? YES Repair an open or high resistance in the wire. NO The VOUT FR DR and VOUT FR AS wires are OK. Replace the body control module .

-1. Measure the voltage between test points 1 and 2 individually.

Test condition | Vehicle OFF (LOCK) mode Each door outer handle 8P connectors: disconnected

Test point 1 | Body control module connector G (32P) No. 31

Test point 2 | Body ground

Test point 1 | Body control module connector G (32P) No. 30

Test point 2 | Body ground

Is there battery voltage?

YES

Repair an open or high resistance in the wire.

NO

The VOUT FR DR and VOUT FR AS wires are OK. Replace the body control module .
````

## Chunk 1539: Keyless Buzzer Circuit Troubleshooting (2/4-door)

- Title: Keyless Buzzer Circuit Troubleshooting (2/4-door)
- Source path: `pages\693.html`
- Chunk ID: `chunk_eb7e2792cebc`
- Images: `images\GHH411861.jpeg`, `images\GHH411862.jpeg`
- Duplicate sources: `pages\2735.html`, `pages\26383.html`, `pages\14384.html`

### Full Text

````text
# Keyless Buzzer Circuit Troubleshooting (2/4-door)

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Keyless buzzer 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Test point 1 Keyless buzzer 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 2. NO Repair an open or high resistance in the ground wire or poor ground (G701).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Keyless buzzer 3P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected

Test point 1 | Keyless buzzer 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 2.

NO

Repair an open or high resistance in the ground wire or poor ground (G701).

- Open wire check (SMART BUZZER line) -1. Disconnect the following connector. Body control module connector E (24P) -2. Connect terminals A and B with a jumper wire. Terminal A Keyless buzzer 3P connector No. 2 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Keyless buzzer 3P connector: jumped to body ground Body control module connector E (24P): disconnected Test point 1 Body control module connector E (24P) No. 22 Test point 2 Body ground Is there continuity? YES The SMART BUZZER wire is not open. Go to step 3. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connector.

Body control module connector E (24P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Keyless buzzer 3P connector No. 2

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Keyless buzzer 3P connector: jumped to body ground Body control module connector E (24P): disconnected

Test point 1 | Body control module connector E (24P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

The SMART BUZZER wire is not open. Go to step 3.

NO

Repair an open or high resistance in the wire.

- Shorted wire check (SMART BUZZER line) -1. Remove the jumper wire from the keyless buzzer 3P connector. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Body control module connector E (24P): disconnected Test point 1 Body control module connector E (24P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The SMART BUZZER wire is OK. Go to step 4.

-1. Remove the jumper wire from the keyless buzzer 3P connector.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Body control module connector E (24P): disconnected

Test point 1 | Body control module connector E (24P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The SMART BUZZER wire is OK. Go to step 4.

- Keyless buzzer check (substitution) -1. Substitute a known-good keyless buzzer. -2. Check the keyless buzzer function. Does the keyless buzzer sound? YES Replace the original keyless buzzer . NO Replace the body control module .

-1. Substitute a known-good keyless buzzer.

-2. Check the keyless buzzer function.

Does the keyless buzzer sound?

YES

Replace the original keyless buzzer .

NO

Replace the body control module .
````

## Chunk 1540: Keyless Buzzer Circuit Troubleshooting (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Buzzer Circuit Troubleshooting (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\694.html`
- Chunk ID: `chunk_fb4e94c47f15`
- Images: `images\GHH411863.jpeg`, `images\GHH411864.jpeg`
- Duplicate sources: `pages\2736.html`, `pages\26384.html`, `pages\14385.html`

### Full Text

````text
# Keyless Buzzer Circuit Troubleshooting (5-door) (2017 2018 2019 2020 2021)

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Keyless buzzer 3P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Test point 1 Keyless buzzer 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 2. NO Repair an open or high resistance in the ground wire or poor ground (G604).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Keyless buzzer 3P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected

Test point 1 | Keyless buzzer 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 2.

NO

Repair an open or high resistance in the ground wire or poor ground (G604).

- Open wire check (SMART BUZZER line) -1. Disconnect the following connector. Body control module connector E (24P) -2. Connect terminals A and B with a jumper wire. Terminal A Keyless buzzer 3P connector No. 2 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Keyless buzzer 3P connector: jumped to body ground Body control module connector E (24P): disconnected Test point 1 Body control module connector E (24P) No. 22 Test point 2 Body ground Is there continuity? YES The SMART BUZZER wire is not open. Go to step 3. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connector.

Body control module connector E (24P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Keyless buzzer 3P connector No. 2

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Keyless buzzer 3P connector: jumped to body ground Body control module connector E (24P): disconnected

Test point 1 | Body control module connector E (24P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

The SMART BUZZER wire is not open. Go to step 3.

NO

Repair an open or high resistance in the wire.

- Shorted wire check (SMART BUZZER line) -1. Remove the jumper wire from the keyless buzzer 3P connector. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Body control module connector E (24P): disconnected Test point 1 Body control module connector E (24P) No. 22 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the wire. NO The SMART BUZZER wire is OK. Go to step 4.

-1. Remove the jumper wire from the keyless buzzer 3P connector.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Keyless buzzer 3P connector: disconnected Body control module connector E (24P): disconnected

Test point 1 | Body control module connector E (24P) No. 22

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the wire.

NO

The SMART BUZZER wire is OK. Go to step 4.

- Keyless buzzer check (substitution) -1. Substitute a known-good keyless buzzer. -2. Check the keyless buzzer function. Does the keyless buzzer sound? YES Replace the original keyless buzzer . NO Replace the body control module .

-1. Substitute a known-good keyless buzzer.

-2. Check the keyless buzzer function.

Does the keyless buzzer sound?

YES

Replace the original keyless buzzer .

NO

Replace the body control module .
````

## Chunk 1541: Immobilizer System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)

- Title: Immobilizer System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\697.html`
- Chunk ID: `chunk_3ea2c2539bfd`
- Images: `images\GHH411867.jpeg`
- Duplicate sources: `pages\2739.html`, `pages\26387.html`, `pages\14388.html`

### Full Text

````text
# Immobilizer System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1542: Keyless Access System Circuit Diagram (2/4-door)

- Title: Keyless Access System Circuit Diagram (2/4-door)
- Source path: `pages\698.html`
- Chunk ID: `chunk_aeb0750ef4bf`
- Images: `images\GHH411868.jpeg`, `images\GHH411869.jpeg`, `images\GHH411870.jpeg`, `images\GHH411871.jpeg`, `images\GHH411872.jpeg`
- Duplicate sources: `pages\2740.html`, `pages\26388.html`, `pages\14389.html`

### Full Text

````text
# Keyless Access System Circuit Diagram (2/4-door)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1543: Keyless Access System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\699.html`
- Chunk ID: `chunk_440cec95bbc4`
- Images: `images\GHH411873.jpeg`, `images\GHH411874.jpeg`, `images\GHH411875.jpeg`, `images\GHH411876.jpeg`, `images\GHH411877.jpeg`
- Duplicate sources: `pages\2741.html`, `pages\26389.html`, `pages\14390.html`

### Full Text

````text
# Keyless Access System Circuit Diagram (5-door) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1544: Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door with Keyless Access System)

- Title: Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door with Keyless Access System)
- Source path: `pages\700.html`
- Chunk ID: `chunk_c3276e9228cf`
- Images: `images\GHH411878.jpeg`, `images\GHH411879.jpeg`, `images\GHH411880.jpeg`, `images\GHH411881.jpeg`, `images\GHH411882.jpeg`
- Duplicate sources: `pages\2742.html`, `pages\26390.html`, `pages\14391.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door with Keyless Access System)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1545: Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door without Keyless Access System)

- Title: Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door without Keyless Access System)
- Source path: `pages\701.html`
- Chunk ID: `chunk_b884f1997411`
- Images: `images\GHH411883.jpeg`, `images\GHH411884.jpeg`, `images\GHH411885.jpeg`, `images\GHH411886.jpeg`, `images\GHH411887.jpeg`
- Duplicate sources: `pages\2743.html`, `pages\26391.html`, `pages\14392.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Circuit Diagram (2/4-door without Keyless Access System)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1546: Keyless/Power Door Locks/Security System Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)
- Source path: `pages\702.html`
- Chunk ID: `chunk_968a707536b6`
- Images: `images\GHH411888.jpeg`, `images\GHH411889.jpeg`, `images\GHH411890.jpeg`, `images\GHH411891.jpeg`, `images\GHH411892.jpeg`
- Duplicate sources: `pages\2744.html`, `pages\26392.html`, `pages\14393.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Circuit Diagram (5-door with Keyless Access System) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1547: Keyless/Power Door Locks/Security System Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)
- Source path: `pages\703.html`
- Chunk ID: `chunk_8c5ff9551234`
- Images: `images\GHH411893.jpeg`, `images\GHH411894.jpeg`, `images\GHH411895.jpeg`, `images\GHH411896.jpeg`, `images\GHH411897.jpeg`
- Duplicate sources: `pages\2745.html`, `pages\26393.html`, `pages\14394.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Circuit Diagram (5-door without Keyless Access System) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1548: Emergency Access to Fuel Fill Door Lock Actuator (2/4-door): Procedure

- Title: Emergency Access to Fuel Fill Door Lock Actuator (2/4-door): Procedure
- Source path: `pages\704.html`
- Chunk ID: `chunk_b3fe252f3ed9`
- Images: `images\GHH411898.jpeg`, `images\GHH411899.jpeg`
- Duplicate sources: `pages\2746.html`, `pages\26394.html`, `pages\14395.html`

### Full Text

````text
# Emergency Access to Fuel Fill Door Lock Actuator (2/4-door): Procedure

- Emergency Access to Fuel Fill Door Lock Actuator - Procedure 2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Pull the emergency access wire (A) by hand in the direction of the arrow to release the lock.

2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Pull the emergency access wire (A) by hand in the direction of the arrow to release the lock.

4-door
````

## Chunk 1549: Emergency Access to Fuel Fill Door Lock Actuator (5-door) (2017 2018 2019 2020 2021): Procedure

- Title: Emergency Access to Fuel Fill Door Lock Actuator (5-door) (2017 2018 2019 2020 2021): Procedure
- Source path: `pages\705.html`
- Chunk ID: `chunk_559f4b14eeec`
- Images: `images\GHH411900.jpeg`
- Duplicate sources: `pages\2747.html`, `pages\26395.html`, `pages\14396.html`

### Full Text

````text
# Emergency Access to Fuel Fill Door Lock Actuator (5-door) (2017 2018 2019 2020 2021): Procedure

- Emergency Access to Fuel Fill Door Lock Actuator - Procedure Courtesy of HONDA, U.S.A., INC. 1. Remove the side lid (left side) (A). 2. Pull the emergency access wire (B) by hand in the direction of the arrow to release the lock.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the side lid (left side) (A). 2. Pull the emergency access wire (B) by hand in the direction of the arrow to release the lock.

2. Pull the emergency access wire (B) by hand in the direction of the arrow to release the lock.
````

## Chunk 1550: Emergency Access to Tailgate Latch (2017 2018 2019 2020 2021): Procedure

- Title: Emergency Access to Tailgate Latch (2017 2018 2019 2020 2021): Procedure
- Source path: `pages\706.html`
- Chunk ID: `chunk_a9ad4d1d9a57`
- Images: `images\GHH411901.jpeg`
- Duplicate sources: `pages\2748.html`, `pages\26396.html`, `pages\14397.html`

### Full Text

````text
# Emergency Access to Tailgate Latch (2017 2018 2019 2020 2021): Procedure

- Emergency Access to Tailgate Latch - Procedure 1. Remove the tailgate maintenance lid (A). Courtesy of HONDA, U.S.A., INC. 2. Operate the emergency access lever (B) with a small screwdriver in the direction of the arrow to release the lock.

1. Remove the tailgate maintenance lid (A).

Courtesy of HONDA, U.S.A., INC.

2. Operate the emergency access lever (B) with a small screwdriver in the direction of the arrow to release the lock.
````

## Chunk 1551: Immobilizer Key Registration: Procedure

- Title: Immobilizer Key Registration: Procedure
- Source path: `pages\707.html`
- Chunk ID: `chunk_887f85409614`
- Images: none
- Duplicate sources: `pages\2749.html`, `pages\26397.html`, `pages\14398.html`

### Full Text

````text
# Immobilizer Key Registration: Procedure

- Immobilizer Key - Register NOTE: The HDS is required for registration of the immobilizer keys. Programming the immobilizer also programs the keyless transmitter. Check for aftermarket electrical equipment that can cause problems with transponder operation. The immobilizer-keyless control unit can store up to 6 immobilizer keys. Add One New Key/Keyless Transmitter 1. Have a registered key, a new immobilizer key, and the first password from the iN system. 2. Connect the HDS to the data link connector (DLC) 3. Turn the vehicle to the ON mode. 4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP. 5. Select ADD AND DELETE KEYS, then ADD 1 KEY. 6. Do the registration according to the instructions on the HDS screen. 7. Check if the engine can be started with the newly registered key. 8. When prompted by the HDS, do the keyless transmitter programming. 9. Make sure the keyless transmitter's operation works properly. Add and Delete Keys/Keyless Transmitters, Then Select Delete or Add Keys 1. Have all registered keys, all new keys, and the first password from the iN system. 2. Connect the HDS to the data link connector (DLC) 3. Turn the vehicle to the ON mode. 4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP. 5. Select ADD AND DELETE KEYS, or DELETE OR ADD MULTIPLE KEYS. 6. Do the registration according to the instructions on the HDS screen. 7. Check if the engine can be started with all the registered keys. 8. When prompted by the HDS, do the keyless transmitter programming. 9. Make sure the keyless transmitter's operation works properly. All Keys are Lost 1. Prepare all new keys and have the immobilizer PCM code. 2. Connect the HDS to the data link connector (DLC) 3. Turn the vehicle to the ON mode. 4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP. 5. Select ADD AND DELETE KEYS, then ALL KEYS LOST. 6. Do the registration according to the instructions on the HDS screen. 7. Check if the engine can be started using all the registered keys. 8. When prompted by the HDS, do the keyless transmitter programming. 9. Make sure the keyless transmitter's operation works properly.

NOTE:

- The HDS is required for registration of the immobilizer keys.

- Programming the immobilizer also programs the keyless transmitter.

- Check for aftermarket electrical equipment that can cause problems with transponder operation.

- The immobilizer-keyless control unit can store up to 6 immobilizer keys.

Add One New Key/Keyless Transmitter

1. Have a registered key, a new immobilizer key, and the first password from the iN system.

2. Connect the HDS to the data link connector (DLC)

3. Turn the vehicle to the ON mode.

4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP.

5. Select ADD AND DELETE KEYS, then ADD 1 KEY.

6. Do the registration according to the instructions on the HDS screen.

7. Check if the engine can be started with the newly registered key.

8. When prompted by the HDS, do the keyless transmitter programming.

9. Make sure the keyless transmitter's operation works properly.

Add and Delete Keys/Keyless Transmitters, Then Select Delete or Add Keys

1. Have all registered keys, all new keys, and the first password from the iN system.

2. Connect the HDS to the data link connector (DLC)

3. Turn the vehicle to the ON mode.

4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP.

5. Select ADD AND DELETE KEYS, or DELETE OR ADD MULTIPLE KEYS.

6. Do the registration according to the instructions on the HDS screen.

7. Check if the engine can be started with all the registered keys.

8. When prompted by the HDS, do the keyless transmitter programming.

9. Make sure the keyless transmitter's operation works properly.

All Keys are Lost

1. Prepare all new keys and have the immobilizer PCM code.

2. Connect the HDS to the data link connector (DLC)

3. Turn the vehicle to the ON mode.

4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP.

5. Select ADD AND DELETE KEYS, then ALL KEYS LOST.

6. Do the registration according to the instructions on the HDS screen.

7. Check if the engine can be started using all the registered keys.

8. When prompted by the HDS, do the keyless transmitter programming.

9. Make sure the keyless transmitter's operation works properly.
````

## Chunk 1552: Immobilizer System Registration: Procedure

- Title: Immobilizer System Registration: Procedure
- Source path: `pages\708.html`
- Chunk ID: `chunk_c721af2649d4`
- Images: none
- Duplicate sources: `pages\2750.html`, `pages\26398.html`, `pages\14399.html`

### Full Text

````text
# Immobilizer System Registration: Procedure

- Immobilizer-Keyless Control Unit - Register NOTE: The HDS is required for registration of the immobilizer keys. Programming the immobilizer also programs the keyless transmitter. Check for aftermarket electrical equipment that can cause problems with transponder operation. The immobilizer-keyless control unit can store up to 6 immobilizer keys. 1. Have all keys to be registered and the PCM code. 2. Connect the HDS to the data link connector (DLC) 3. Turn the vehicle to the ON mode. 4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP. 5. Select REPLACE IMMOBILIZER RECEIVER/CONTROL UNIT. 6. Do the registration according to the instructions on the HDS screen. NOTE: Program all of the customer's keys. 7. Check that the engine can be started with all registered keys. 8. When prompted by the HDS, do the keyless transmitter programming. 9. Make sure the keyless transmitter's operation works properly.

NOTE: The HDS is required for registration of the immobilizer keys. Programming the immobilizer also programs the keyless transmitter. Check for aftermarket electrical equipment that can cause problems with transponder operation. The immobilizer-keyless control unit can store up to 6 immobilizer keys. 1. Have all keys to be registered and the PCM code. 2. Connect the HDS to the data link connector (DLC) 3. Turn the vehicle to the ON mode. 4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP. 5. Select REPLACE IMMOBILIZER RECEIVER/CONTROL UNIT. 6. Do the registration according to the instructions on the HDS screen. NOTE: Program all of the customer's keys. 7. Check that the engine can be started with all registered keys. 8. When prompted by the HDS, do the keyless transmitter programming. 9. Make sure the keyless transmitter's operation works properly.

- The HDS is required for registration of the immobilizer keys.

- Programming the immobilizer also programs the keyless transmitter.

- Check for aftermarket electrical equipment that can cause problems with transponder operation.

- The immobilizer-keyless control unit can store up to 6 immobilizer keys.

1. Have all keys to be registered and the PCM code.

2. Connect the HDS to the data link connector (DLC)

3. Turn the vehicle to the ON mode.

4. Select IMMOBI from the SYSTEM SELECTION MENU, then select IMMOBILIZER SETUP.

5. Select REPLACE IMMOBILIZER RECEIVER/CONTROL UNIT.

6. Do the registration according to the instructions on the HDS screen.

NOTE: Program all of the customer's keys.

7. Check that the engine can be started with all registered keys.

8. When prompted by the HDS, do the keyless transmitter programming.

9. Make sure the keyless transmitter's operation works properly.
````

## Chunk 1553: Keyless Access System Registration: Procedure

- Title: Keyless Access System Registration: Procedure
- Source path: `pages\709.html`
- Chunk ID: `chunk_ee31d52590de`
- Images: none
- Duplicate sources: `pages\2751.html`, `pages\26399.html`, `pages\14400.html`

### Full Text

````text
# Keyless Access System Registration: Procedure

NOTE: If you replace the body control module or electric steering lock, the vehicle will not turn to the ON mode. Follow the registration procedure of the corresponding unit.

- Keyless Access System - Register NOTE: Check for aftermarket electrical equipment that could cause problems with keyless access operation. While doing the registration, keep the remote away from computers. While doing the registration, make sure the doors are closed. Programming the remote also programs the keyless transmitter. The body control module can store codes up to 6 remotes. When Replacing the Body Control Module or the Electric Steering Lock Control Unit 1. Connect the HDS to the data link connector (DLC) 2. Do the registration according to the instructions on the HDS screen. 3. After registration, verify all remote related systems work normally with all remotes. When Replacing the PCM, VSA Modulator-Control Unit or Registration of the Remote(s) NOTE: If replacing the body control module, register the body control module first. 1. Connect the HDS to the data link connector (DLC) 2. When replacing the body control module, touch the remote to the engine start/stop button. 3. When all remotes are lost, select the ON mode according to the instructions on the HDS screen, then go to step 5. 4. Turn the vehicle to the ON mode. 5. Select ONE-PUSH START from the SYSTEM SELECTION MENU, then enter REGISTRATION. 6. Select the appropriate items, and do the registration according to the instructions on the HDS screen. 7. After registration, verify systems work normally with all remotes. If the PCM is replaced, do the procedure after replacing PCM .

NOTE:

- Check for aftermarket electrical equipment that could cause problems with keyless access operation.

- While doing the registration, keep the remote away from computers.

- While doing the registration, make sure the doors are closed.

- Programming the remote also programs the keyless transmitter.

- The body control module can store codes up to 6 remotes.

When Replacing the Body Control Module or the Electric Steering Lock Control Unit

1. Connect the HDS to the data link connector (DLC)

2. Do the registration according to the instructions on the HDS screen.

3. After registration, verify all remote related systems work normally with all remotes.

When Replacing the PCM, VSA Modulator-Control Unit or Registration of the Remote(s)

NOTE: If replacing the body control module, register the body control module first.

1. Connect the HDS to the data link connector (DLC)

2. When replacing the body control module, touch the remote to the engine start/stop button.

3. When all remotes are lost, select the ON mode according to the instructions on the HDS screen, then go to step 5.

4. Turn the vehicle to the ON mode.

5. Select ONE-PUSH START from the SYSTEM SELECTION MENU, then enter REGISTRATION.

6. Select the appropriate items, and do the registration according to the instructions on the HDS screen.

7. After registration, verify systems work normally with all remotes. If the PCM is replaced, do the procedure after replacing PCM

.
````

## Chunk 1554: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\710.html`
- Chunk ID: `chunk_fa57c56a0fd1`
- Images: `images\GHH411446.jpeg`
- Duplicate sources: `pages\2752.html`, `pages\26298.html`, `pages\14298.html`

### Full Text

````text
# Removal and Installation

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repairs or service.

NOTE: If the immobilizer-keyless control unit is replaced, do the immobilizer-keyless control unit registration . If the original immobilizer-keyless control unit is installed, confirm that all systems work properly.

- Column Covers - Remove

- Immobilizer-Keyless Control Unit - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the immobilizer-keyless control unit (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the immobilizer-keyless control unit (B).

2. Remove the immobilizer-keyless control unit (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.

- Immobilizer-Keyless Control Unit - Register
````

## Chunk 1555: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\711.html`
- Chunk ID: `chunk_de0360f2225b`
- Images: `images\GHH411447.jpeg`
- Duplicate sources: `pages\2753.html`, `pages\26299.html`, `pages\14299.html`

### Full Text

````text
# Removal and Installation

- Dashboard Center Lower Cover - Remove

- Front Interior LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the front interior LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the front interior LF antenna (B).

2. Remove the front interior LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1556: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\712.html`
- Chunk ID: `chunk_6214db0ac100`
- Images: `images\GHH411448.jpeg`
- Duplicate sources: `pages\2754.html`, `pages\26300.html`, `pages\14300.html`

### Full Text

````text
# Removal and Installation

- Center Console Rear Trim - Remove

- Middle Interior LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the middle interior LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the middle interior LF antenna (B).

2. Remove the middle interior LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1557: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\713.html`
- Chunk ID: `chunk_0e5270404268`
- Images: `images\GHH411449.jpeg`
- Duplicate sources: `pages\2755.html`, `pages\26301.html`, `pages\14301.html`

### Full Text

````text
# Removal and Installation

- Rear Bumper - Remove

- Rear Bumper LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Illustrations used in the procedure are for 4-door. 1. Disconnect the connector (A). 2. Remove the rear bumper LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | NOTE: Illustrations used in the procedure are for 4-door. 1. Disconnect the connector (A). 2. Remove the rear bumper LF antenna (B).

1. Disconnect the connector (A).

2. Remove the rear bumper LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1558: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\714.html`
- Chunk ID: `chunk_31dc2f2441c4`
- Images: `images\GHH411450.jpeg`
- Duplicate sources: `pages\2756.html`, `pages\26302.html`, `pages\14302.html`

### Full Text

````text
# Removal and Installation

- Rear Bumper - Remove

- Rear Bumper LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the rear bumper LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the rear bumper LF antenna (B).

2. Remove the rear bumper LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1559: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\715.html`
- Chunk ID: `chunk_3618e8cb154f`
- Images: `images\GHH411451.jpeg`
- Duplicate sources: `pages\2757.html`, `pages\26303.html`, `pages\14303.html`

### Full Text

````text
# Removal and Installation

- Center Console Rear Trim - Remove

- Rear Interior LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the rear interior LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the rear interior LF antenna (B).

2. Remove the rear interior LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1560: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\716.html`
- Chunk ID: `chunk_1251ab1a5bf0`
- Images: `images\GHH411452.jpeg`
- Duplicate sources: `pages\2758.html`, `pages\26304.html`, `pages\14304.html`

### Full Text

````text
# Removal and Installation

- Cargo Floor Cover - Remove 1. Remove the cargo floor cover as needed .

1. Remove the cargo floor cover as needed .

- Rear Interior LF Antenna - Remove 1. Disconnect the connector (A). Courtesy of HONDA, U.S.A., INC. 2. Remove the rear interior LF antenna (B).

1. Disconnect the connector (A).

Courtesy of HONDA, U.S.A., INC.

2. Remove the rear interior LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1561: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\717.html`
- Chunk ID: `chunk_589b88f9541f`
- Images: `images\GHH411453.jpeg`
- Duplicate sources: `pages\2759.html`, `pages\26305.html`, `pages\14305.html`

### Full Text

````text
# Removal and Installation

- Rear Shelf LF Antenna - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Illustrations used in the procedure are for 4-door. 1. Disconnect the connector (A). 2. Remove the rear shelf LF antenna (B).

Courtesy of HONDA, U.S.A., INC. | NOTE: Illustrations used in the procedure are for 4-door. 1. Disconnect the connector (A). 2. Remove the rear shelf LF antenna (B).

1. Disconnect the connector (A).

2. Remove the rear shelf LF antenna (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1562: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\718.html`
- Chunk ID: `chunk_532c46400e9a`
- Images: `images\GHH411454.jpeg`
- Duplicate sources: `pages\2760.html`, `pages\26306.html`, `pages\14306.html`

### Full Text

````text
# Removal and Installation

- Keyless Buzzer - Remove Courtesy of HONDA, U.S.A., INC. 1. Pull back the rear bumper (A) as needed to access the keyless buzzer (B). 2. Disconnect the connector (C). 3. Remove the keyless buzzer. 4. Remove the clip (D).

Courtesy of HONDA, U.S.A., INC. | 1. Pull back the rear bumper (A) as needed to access the keyless buzzer (B). 2. Disconnect the connector (C). 3. Remove the keyless buzzer. 4. Remove the clip (D).

2. Disconnect the connector (C).

3. Remove the keyless buzzer.

4. Remove the clip (D).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1563: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\719.html`
- Chunk ID: `chunk_aa59346785e4`
- Images: `images\GHH411455.jpeg`
- Duplicate sources: `pages\2761.html`, `pages\26307.html`, `pages\14307.html`

### Full Text

````text
# Removal and Installation

- Rear Bumper - Remove

- Keyless Buzzer - Remove Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the keyless buzzer (B). 3. Remove the clip (C).

Courtesy of HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Remove the keyless buzzer (B). 3. Remove the clip (C).

2. Remove the keyless buzzer (B).

3. Remove the clip (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1564: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\720.html`
- Chunk ID: `chunk_8aed64105f17`
- Images: `images\GHH411456.jpeg`
- Duplicate sources: `pages\2762.html`, `pages\26308.html`, `pages\14308.html`

### Full Text

````text
# Removal and Installation

- Rear License Trim - Remove

- Tailgate Outer Handle Switch - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1565: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\721.html`
- Chunk ID: `chunk_3e389cd503d3`
- Images: `images\GHH411457.jpeg`
- Duplicate sources: `pages\2763.html`, `pages\26309.html`, `pages\14309.html`

### Full Text

````text
# Removal and Installation

- Rear License Trim - Remove

- Tailgate Outer Handle/Lock Switch - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1566: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\722.html`
- Chunk ID: `chunk_f42055c92968`
- Images: `images\GHH411458.jpeg`
- Duplicate sources: `pages\2764.html`, `pages\26310.html`, `pages\14310.html`

### Full Text

````text
# Removal and Installation

- Rear License Trim - Remove

- Trunk Lid Outer Handle Switch - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Illustrations used in the procedure are for 4-door.

Courtesy of HONDA, U.S.A., INC.

NOTE: Illustrations used in the procedure are for 4-door.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1567: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\723.html`
- Chunk ID: `chunk_d1c24367db9a`
- Images: `images\GHH411459.jpeg`, `images\GHH411460.jpeg`, `images\GHH411461.jpeg`, `images\GHH411462.jpeg`
- Duplicate sources: `pages\2765.html`, `pages\26311.html`, `pages\14311.html`

### Full Text

````text
# Removal and Installation

- Left Rear Inner Fender - Remove 1. Remove the left rear inner fender as needed .

1. Remove the left rear inner fender as needed .

- Trunk Rear Side Trim Panel (Left Side) - Remove 1. Remove the trunk rear side trim panel (left side) as needed .

1. Remove the trunk rear side trim panel (left side) as needed .

- Fuel Fill Door Lock Actuator - Remove 2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Remove the clip(s) (A). 2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 2. Remove the grommet (A). 3. Disconnect the connector (B). 4. While pressing the tabs (C), remove the fuel fill door lock actuator (D). 5. Remove the fuel fill door release lock (E).

2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Remove the clip(s) (A).

4-door

2-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 4-door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 2. Remove the grommet (A). 3. Disconnect the connector (B). 4. While pressing the tabs (C), remove the fuel fill door lock actuator (D). 5. Remove the fuel fill door release lock (E).

4-door

3. Disconnect the connector (B).

4. While pressing the tabs (C), remove the fuel fill door lock actuator (D).

5. Remove the fuel fill door release lock (E).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1568: Fuel Fill Door Lock Actuator Removal, Installation, and Test (2/4-door): Test

- Title: Fuel Fill Door Lock Actuator Removal, Installation, and Test (2/4-door): Test
- Source path: `pages\724.html`
- Chunk ID: `chunk_93237b156108`
- Images: `images\GHH411463.jpeg`, `images\GHH411464.jpeg`
- Duplicate sources: `pages\2766.html`, `pages\26312.html`, `pages\14312.html`

### Full Text

````text
# Fuel Fill Door Lock Actuator Removal, Installation, and Test (2/4-door): Test

- Fuel Fill Door Lock Actuator - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Check the fuel fill door lock actuator (A) operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 2. If the actuator does not operate as specified, replace the fuel fill door lock actuator.

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Check the fuel fill door lock actuator (A) operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 2. If the actuator does not operate as specified, replace the fuel fill door lock actuator.

NOTE: To prevent damage to the actuator, apply battery voltage only momentarily.

2. If the actuator does not operate as specified, replace the fuel fill door lock actuator.
````

## Chunk 1569: Keyless Access Remote Removal, Installation, and Test: Test

- Title: Keyless Access Remote Removal, Installation, and Test: Test
- Source path: `pages\725.html`
- Chunk ID: `chunk_69d94fc4f994`
- Images: `images\GHH411465.jpeg`
- Duplicate sources: `pages\2767.html`, `pages\26313.html`, `pages\14313.html`

### Full Text

````text
# Keyless Access Remote Removal, Installation, and Test: Test

NOTE:

- If the doors do not lock or unlock with the remote, check the LED on the remote by pressing the lock or unlock button. If the LED does not come on, replace the remote battery.

- If the doors unlock or lock with the remote, but the LED on the remote does not come on, the LED is faulty; replace the remote.

- If any door is open, you cannot lock the doors with the remote.

- If you unlocked the doors with the remote, but do not open any of the doors within 30 seconds, the doors relock automatically.

- The doors will only lock or unlock with the remote if the power is in the OFF (LOCK) mode.

- Remote - Test Courtesy of HONDA, U.S.A., INC. 1. Open the remote and check for water damage. If you find any water damage, replace the remote and register the new remote . If there is no water damage, go to step 2. 2. Replace the remote battery (A) with a new one (CR2032), and try to lock and unlock the doors with the remote by pressing the lock or unlock button at least 10 times: If the doors lock and unlock, the remote is OK. If the remote does not work after replacing the remote battery, verify that the correct battery was installed and the polarity is correct. If the doors do not lock and unlock, go to step 3. 3. Reprogram and register the remote , then try to lock and unlock the doors. If the doors do not lock and unlock, substitute a known-good remote and recheck. If it still does not operating, replace the body control module. If the doors lock and unlock, the remote is OK. If the doors do not lock and unlock, try to program another vehicle using the remote. If the remote programs another vehicle, go to B-CAN System Diagnosis Test Mode A . If the remote will not program another vehicle, replace it.

Courtesy of HONDA, U.S.A., INC. | 1. Open the remote and check for water damage. If you find any water damage, replace the remote and register the new remote . If there is no water damage, go to step 2. 2. Replace the remote battery (A) with a new one (CR2032), and try to lock and unlock the doors with the remote by pressing the lock or unlock button at least 10 times: If the doors lock and unlock, the remote is OK. If the remote does not work after replacing the remote battery, verify that the correct battery was installed and the polarity is correct. If the doors do not lock and unlock, go to step 3. 3. Reprogram and register the remote , then try to lock and unlock the doors. If the doors do not lock and unlock, substitute a known-good remote and recheck. If it still does not operating, replace the body control module. If the doors lock and unlock, the remote is OK. If the doors do not lock and unlock, try to program another vehicle using the remote. If the remote programs another vehicle, go to B-CAN System Diagnosis Test Mode A . If the remote will not program another vehicle, replace it.

- If you find any water damage, replace the remote and register the new remote .

- If there is no water damage, go to step 2.

2. Replace the remote battery (A) with a new one (CR2032), and try to lock and unlock the doors with the remote by pressing the lock or unlock button at least 10 times:

- If the doors lock and unlock, the remote is OK.

- If the remote does not work after replacing the remote battery, verify that the correct battery was installed and the polarity is correct.

- If the doors do not lock and unlock, go to step 3.

3. Reprogram and register the remote , then try to lock and unlock the doors.

- If the doors do not lock and unlock, substitute a known-good remote and recheck. If it still does not operating, replace the body control module.

- If the doors lock and unlock, the remote is OK.

- If the doors do not lock and unlock, try to program another vehicle using the remote.

- If the remote programs another vehicle, go to B-CAN System Diagnosis Test Mode A . If the remote will not program another vehicle, replace it.

- If the remote programs another vehicle, go to B-CAN System Diagnosis Test Mode A .

- If the remote will not program another vehicle, replace it.
````

## Chunk 1570: Keyless Entry Transmitter Removal, Installation, and Test: Test

- Title: Keyless Entry Transmitter Removal, Installation, and Test: Test
- Source path: `pages\726.html`
- Chunk ID: `chunk_7f0800105a79`
- Images: `images\GHH411466.jpeg`, `images\GHH411467.jpeg`
- Duplicate sources: `pages\2768.html`, `pages\26314.html`, `pages\14314.html`

### Full Text

````text
# Keyless Entry Transmitter Removal, Installation, and Test: Test

NOTE:

- If the doors do not lock or unlock with the transmitter, check the LED on the transmitter by pressing the lock or unlock button. If the LED does not come on, replace the transmitter battery.

- If the doors unlock or lock with the transmitter, but the LED on the transmitter does not come on, the LED is faulty; replace the transmitter.

- If any door is open, you cannot lock the doors with the transmitter.

- If you unlocked the doors with the transmitter, but do not open any of the doors within 30 seconds, the doors relock automatically.

- The doors will only lock or unlock with the transmitter if the ignition key is inserted in the ignition key cylinder.

Without HDS

- Transmitter - Test Courtesy of HONDA, U.S.A., INC. 1. Open the keyless transmitter and check for water damage. If you find any water damage, replace the transmitter and register the new transmitter . If there is no water damage, go to step 2. 2. Replace the transmitter battery (A) with a new one (CR1620), and try to lock and unlock the doors with the transmitter by pressing the lock or unlock button at least 10 times: If the doors lock and unlock, the transmitter is OK. If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct. If the doors do not lock and unlock, go to step 3. 3. Reprogram and register the transmitter , then try to lock and unlock the doors. If the doors lock and unlock, the transmitter is OK. If the doors do not lock and unlock, substitute a known-good transmitter, register it and recheck. If still not operating, replace the immobilizer-keyless control unit .

Courtesy of HONDA, U.S.A., INC. | 1. Open the keyless transmitter and check for water damage. If you find any water damage, replace the transmitter and register the new transmitter . If there is no water damage, go to step 2. 2. Replace the transmitter battery (A) with a new one (CR1620), and try to lock and unlock the doors with the transmitter by pressing the lock or unlock button at least 10 times: If the doors lock and unlock, the transmitter is OK. If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct. If the doors do not lock and unlock, go to step 3. 3. Reprogram and register the transmitter , then try to lock and unlock the doors. If the doors lock and unlock, the transmitter is OK. If the doors do not lock and unlock, substitute a known-good transmitter, register it and recheck. If still not operating, replace the immobilizer-keyless control unit .

- If you find any water damage, replace the transmitter and register the new transmitter .

- If there is no water damage, go to step 2.

2. Replace the transmitter battery (A) with a new one (CR1620), and try to lock and unlock the doors with the transmitter by pressing the lock or unlock button at least 10 times:

- If the doors lock and unlock, the transmitter is OK.

- If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct.

- If the doors do not lock and unlock, go to step 3.

3. Reprogram and register the transmitter , then try to lock and unlock the doors.

- If the doors lock and unlock, the transmitter is OK.

- If the doors do not lock and unlock, substitute a known-good transmitter, register it and recheck. If still not operating, replace the immobilizer-keyless control unit .

With HDS

- Transmitter - Test Courtesy of HONDA, U.S.A., INC. 1. Press the transmitter lock or unlock button at least 10 times to reset the transmitter. If the locks work, the transmitter is OK. If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct. If any of the transmitter buttons do not work, replace the transmitter, then register the transmitter . If the locks don't work, go to step 2. 2. Connect the HDS to the data link connector (DLC) 3. Select KEYLESS TRANSMITTER from the BODY ELECTRICAL menu, then select INSPECTION, then KEYLESS CHECK. 4. Press the lock, unlock, or HOLD button and check the response on the screen of the HDS. NOTE: The door lock actuators may or may not cycle when receiving input from the transmitter.
````

## Chunk 1571: Keyless Entry Transmitter Removal, Installation, and Test: Test

- Title: Keyless Entry Transmitter Removal, Installation, and Test: Test
- Source path: `pages\726.html`
- Chunk ID: `chunk_ac97b7da5e39`
- Images: `images\GHH411466.jpeg`, `images\GHH411467.jpeg`
- Duplicate sources: `pages\2768.html`, `pages\26314.html`, `pages\14314.html`

### Full Text

````text
ourtesy of HONDA, U.S.A., INC. 1. Press the transmitter lock or unlock button at least 10 times to reset the transmitter. If the locks work, the transmitter is OK. If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct. If any of the transmitter buttons do not work, replace the transmitter, then register the transmitter . If the locks don't work, go to step 2. 2. Connect the HDS to the data link connector (DLC) 3. Select KEYLESS TRANSMITTER from the BODY ELECTRICAL menu, then select INSPECTION, then KEYLESS CHECK. 4. Press the lock, unlock, or HOLD button and check the response on the screen of the HDS. NOTE: The door lock actuators may or may not cycle when receiving input from the transmitter. If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK. If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is working but indicated, the transmitter is not registered to the vehicle. If necessary, register the transmitter . If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 5. 5. Open the transmitter and check for water damage. If you find any water damage, replace the transmitter, then register the new transmitter . If there is no water damage, go to step 6. 6. Replace the transmitter battery (A) with a new one (CR1620), and press the transmitter lock or unlock button and check the response on the screen of the HDS. If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK. If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 7. 7. Use a different known-good transmitter assembly and repeat steps 3 and 4. NOTE: The transmitter does not need to be programmed to the vehicle for this test. If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE WAS RECEIVED is indicated, replace the transmitter and, do the transmitter registration . If KEYLESS ENTRY TRANSMITTER CODE WAS NOT RECEIVED is indicated, the immobilizer-keyless control unit is faulty, replace it and do the transmitter registration . NOTE: The transmitter is combined with the immobilizer transponder, so when the transponder is registered by the HDS, the transmitter programming is completed automatically.

Courtesy of HONDA, U.S.A., INC. | 1. Press the transmitter lock or unlock button at least 10 times to reset the transmitter. If the locks work, the transmitter is OK. If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct. If any of the transmitter buttons do not work, replace the transmitter, then register the transmitter . If the locks don't work, go to step 2. 2. Connect the HDS to the data link connector (DLC) 3. Select KEYLESS TRANSMITTER from the BODY ELECTRICAL menu, then select INSPECTION, then KEYLESS CHECK. 4. Press the lock, unlock, or HOLD button and check the response on the screen of the HDS. NOTE: The door lock actuators may or may not cycle when receiving input from the transmitter. If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK. If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is working but indicated, the transmitter is not registered to the vehicle. If necessary, register the transmitter . If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 5. 5. Open the transmitter and check for water damage. If you find any water damage, replace the transmitter, then register the new transmitter . If there is no water damage, go to step 6. 6. Replace the transmitter battery (A) with a new one (CR1620), and press the transmitter lock or unlock button and check the response on the screen of the HDS. If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK. If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 7. 7. Use a different known-good transmitter assembly and repeat steps 3 and 4. NOTE: The transmitter does not need to be programmed to the vehicle for this test. If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE WAS RECEIVED is indicated, replace the transmitter and, do the transmitter registration . If KEYLESS ENTRY TRANSMITTER CODE WAS NOT RECEIVED is indicated, the immobilizer-keyless control unit is faulty, replace it and do the transmitter registration .
````

## Chunk 1572: Keyless Entry Transmitter Removal, Installation, and Test: Test

- Title: Keyless Entry Transmitter Removal, Installation, and Test: Test
- Source path: `pages\726.html`
- Chunk ID: `chunk_79da9b28fade`
- Images: `images\GHH411466.jpeg`, `images\GHH411467.jpeg`
- Duplicate sources: `pages\2768.html`, `pages\26314.html`, `pages\14314.html`

### Full Text

````text
damage, go to step 6. 6. Replace the transmitter battery (A) with a new one (CR1620), and press the transmitter lock or unlock button and check the response on the screen of the HDS. If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK. If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 7. 7. Use a different known-good transmitter assembly and repeat steps 3 and 4. NOTE: The transmitter does not need to be programmed to the vehicle for this test. If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE WAS RECEIVED is indicated, replace the transmitter and, do the transmitter registration . If KEYLESS ENTRY TRANSMITTER CODE WAS NOT RECEIVED is indicated, the immobilizer-keyless control unit is faulty, replace it and do the transmitter registration . NOTE: The transmitter is combined with the immobilizer transponder, so when the transponder is registered by the HDS, the transmitter programming is completed automatically.

- If the locks work, the transmitter is OK.

- If the transmitter does not work after replacing the transmitter battery, verify that the correction battery was installed and the polarity is correct.

- If any of the transmitter buttons do not work, replace the transmitter, then register the transmitter .

- If the locks don't work, go to step 2.

2. Connect the HDS to the data link connector (DLC)

3. Select KEYLESS TRANSMITTER from the BODY ELECTRICAL menu, then select INSPECTION, then KEYLESS CHECK.

4. Press the lock, unlock, or HOLD button and check the response on the screen of the HDS.

NOTE: The door lock actuators may or may not cycle when receiving input from the transmitter.

- If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK.

- If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is working but indicated, the transmitter is not registered to the vehicle. If necessary, register the transmitter .

- If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 5.

5. Open the transmitter and check for water damage.

- If you find any water damage, replace the transmitter, then register the new transmitter .

- If there is no water damage, go to step 6.

6. Replace the transmitter battery (A) with a new one (CR1620), and press the transmitter lock or unlock button and check the response on the screen of the HDS.

- If KEYLESS ENTRY TRANSMITTER CODE IS RECEIVED is indicated, the transmitter is OK.

- If KEYLESS ENTRY TRANSMITTER CODE IS NOT RECEIVED is indicated, go to step 7.

7. Use a different known-good transmitter assembly and repeat steps 3 and 4.

NOTE: The transmitter does not need to be programmed to the vehicle for this test.

- If DIFFERENT KEYLESS ENTRY TRANSMITTER CODE WAS RECEIVED is indicated, replace the transmitter and, do the transmitter registration .

- If KEYLESS ENTRY TRANSMITTER CODE WAS NOT RECEIVED is indicated, the immobilizer-keyless control unit is faulty, replace it and do the transmitter registration .

NOTE: The transmitter is combined with the immobilizer transponder, so when the transponder is registered by the HDS, the transmitter programming is completed automatically.
````

## Chunk 1573: Immobilizer System Symptom Troubleshooting Index

- Title: Immobilizer System Symptom Troubleshooting Index
- Source path: `pages\727.html`
- Chunk ID: `chunk_b7adbce2c972`
- Images: none
- Duplicate sources: `pages\2769.html`, `pages\26224.html`, `pages\12911.html`

### Full Text

````text
# Immobilizer System Symptom Troubleshooting Index

Troubleshoot the immobilizer system in the order shown:

Order of Priority | Symptom | Possible cause

1 | Security indicator blinks. | Symptom troubleshooting .

2 | Engine does not start with the immobilizer key. | Symptom troubleshooting .

3 | Security indicator turns on. | Symptom troubleshooting .
````

## Chunk 1574: Keyless Access System Symptom Troubleshooting Index

- Title: Keyless Access System Symptom Troubleshooting Index
- Source path: `pages\728.html`
- Chunk ID: `chunk_06847dd57419`
- Images: none
- Duplicate sources: `pages\2770.html`, `pages\26225.html`, `pages\12913.html`

### Full Text

````text
# Keyless Access System Symptom Troubleshooting Index

Symptom | Diagnostic procedure | Also check for

Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch | Symptom troubleshooting (Without electric steering lock) Symptom troubleshooting (With electric steering lock) | Check the No. A1-7 (125 A), No. A1-5 (30 A), No. A2-2 (30 A), No. A2-4 (60 A), and No. A18 (10 A) fuses in the under-hood fuse/relay box Check the No. B30 (10 A) fuse in the under-dash fuse/relay box Poor connections at the body control module Keyless remote Body control module Electric steering lock *2 Engine start/stop switch Harness/connections

- Symptom troubleshooting (Without electric steering lock)

- Symptom troubleshooting (With electric steering lock)

- Check the No. A1-7 (125 A), No. A1-5 (30 A), No. A2-2 (30 A), No. A2-4 (60 A), and No. A18 (10 A) fuses in the under-hood fuse/relay box

- Check the No. B30 (10 A) fuse in the under-dash fuse/relay box

- Poor connections at the body control module

- Keyless remote

- Body control module

- Electric steering lock *2

- Engine start/stop switch

- Harness/connections

Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch | Symptom troubleshooting | Body control module LF antenna Keyless remote Low or weak keyless remote battery Harness/connections

- Body control module

- LF antenna

- Keyless remote

- Low or weak keyless remote battery

- Harness/connections

Cannot select ON mode with the keyless remote touching the engine start/stop switch, but can select ON mode with keyless access | Check the body control module | Body control module is not registered Body control module MTR CONT line power short *2 ESL ID mismatch *2 MTR CONT line open/short *2 IGN TRX line open/short *2 Not registered Harness/connections

- Body control module is not registered

- Body control module

- MTR CONT line power short *2

- ESL ID mismatch *2

- MTR CONT line open/short *2

- IGN TRX line open/short *2

- Not registered

- Harness/connections

The mode changes between ACCESSORY and ON, but it does not change to OFF | Check the body control module Check the park pin switch Check the transmission range switch *1 | Body control module ATP-P line open *1 Transmission range switch *1 Park pin switch *1 P-PIN SW line open *1

- Check the body control module

- Check the park pin switch

- Check the transmission range switch *1

- Body control module

- ATP-P line open *1

- Transmission range switch *1

- Park pin switch *1

- P-PIN SW line open *1

The mode changes between ACCESSORY and ON, but it is difficult to change to OFF | Check the body control module Check the gauge control module Check the park pin switch *1 | Gauge control module Body control module PCM B-CAN communication line open/short F-CAN communication line open/short Speed signal line open Park pin switch *1 P-PIN SW line open *1

- Check the body control module

- Check the gauge control module

- Check the park pin switch *1

- Gauge control module

- Body control module

- PCM

- B-CAN communication line open/short

- F-CAN communication line open/short

- Speed signal line open

- Park pin switch *1

- P-PIN SW line open *1

Symptom | Diagnostic procedure | Also check for

Engine start/stop switch does not work | Check for DTCs. If any DTC is indicated, go to the DTC troubleshooting | ACC relay circuit Body control module Engine start/stop switch SS1(+) line short SS2(-) line short Harness

- ACC relay circuit

- Body control module

- Engine start/stop switch

- SS1(+) line short

- SS2(-) line short

- Harness

Engine does not crank (power supply is normal) | Check the brake pedal position switch Check the body control module | Body control module STS line open/short Brake pedal position switch STOP SW line open/short

- Check the brake pedal position switch

- Check the body control module

- Body control module

- STS line open/short

- Brake pedal position switch

- STOP SW line open/short

The engine starts, but stalls immediately | Symptom troubleshooting | No power to PCM No power to body control module Body control module Gauge control module Electric steering lock *2 Harness/connections

- No power to PCM

- No power to body control module

- Body control module

- Gauge control module

- Electric steering lock *2

- Harness/connections
````

## Chunk 1575: Keyless Access System Symptom Troubleshooting Index

- Title: Keyless Access System Symptom Troubleshooting Index
- Source path: `pages\728.html`
- Chunk ID: `chunk_322258ba754d`
- Images: none
- Duplicate sources: `pages\2770.html`, `pages\26225.html`, `pages\12913.html`

### Full Text

````text
SS1(+) line short

- SS2(-) line short

- Harness

Engine does not crank (power supply is normal) | Check the brake pedal position switch Check the body control module | Body control module STS line open/short Brake pedal position switch STOP SW line open/short

- Check the brake pedal position switch

- Check the body control module

- Body control module

- STS line open/short

- Brake pedal position switch

- STOP SW line open/short

The engine starts, but stalls immediately | Symptom troubleshooting | No power to PCM No power to body control module Body control module Gauge control module Electric steering lock *2 Harness/connections

- No power to PCM

- No power to body control module

- Body control module

- Gauge control module

- Electric steering lock *2

- Harness/connections

Security indicator blinks | Symptom troubleshooting | Gauge control module Body control module PCM Harness/connections

- Gauge control module

- Body control module

- PCM

- Harness/connections

All the doors will not lock and unlock | Symptom troubleshooting | Body control module LF antenna Driver's door lock knob switch Door outer handle touch sensor/lock switch Door lock actuators Keyless remote Low or weak keyless remote battery Not registered

- Body control module

- LF antenna

- Driver's door lock knob switch

- Door outer handle touch sensor/lock switch

- Door lock actuators

- Keyless remote

- Low or weak keyless remote battery

- Not registered

The doors will not unlock or lock with the keyless remote, but will unlock or lock with the door outer handles | Symptom troubleshooting | Keyless remote battery dead Keyless remote Body control module Harness/connections B-CAN communication line

- Keyless remote battery dead

- Keyless remote

- Body control module

- Harness/connections

- B-CAN communication line

The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote | Symptom troubleshooting | Door outer handle touch sensor/lock switch Body control module Keyless remote Not registered Harness/connections

- Door outer handle touch sensor/lock switch

- Body control module

- Keyless remote

- Not registered

- Harness/connections

*1: CVT

*2: With electric steering lock
````

## Chunk 1576: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\729.html`
- Chunk ID: `chunk_7a907dee680c`
- Images: none
- Duplicate sources: `pages\2771.html`, `pages\26226.html`, `pages\17173.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (2-door) (2016 2017 2018 2019 2020)

NOTE: If the door lock system and the keyless operation do not work, troubleshoot the door locks first. The system does not function when turn the vehicle to the ON mode.

Symptom | Check Items | Also check for

The security system sounds randomly while the doors are locked | Tripped sensor recall

The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed | Symptom troubleshooting

Security alarm system will not arm | Symptom troubleshooting

All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote | Poor ground (G501) Blown No. B16 (20 A) fuse in the under-dash fuse/relay box Body control module input test Power window master switch input test Keyless transmitter test Remote test

- Poor ground (G501)

- Blown No. B16 (20 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test

Driver's door will not lock or unlock | Poor ground (G501) Blown No. B25 (10 A) fuse in the under-dash fuse/relay box Blown No. B39 (10 A) fuse in the under-dash fuse/relay box Door switch test (check the door switch ON/OFF information with the HDS) Body control module input test Power window master switch input test Driver's door lock actuator test

- Poor ground (G501)

- Blown No. B25 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B39 (10 A) fuse in the under-dash fuse/relay box

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test

Passenger's door will not lock or unlock | Poor ground (G505) Blown No. B12 (10 A) fuse in the under-dash fuse/relay box Blown No. B26 (10 A) fuse in the under-dash fuse/relay box Body control module input test Door switch test (check the door switch ON/OFF information with the HDS) Door lock actuator test

- Poor ground (G505)

- Blown No. B12 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B26 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test

Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch | Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)

Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened | Symptom troubleshooting

Auto door unlock does not work | Symptom troubleshooting
````

## Chunk 1577: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (4-door)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (4-door)
- Source path: `pages\730.html`
- Chunk ID: `chunk_12baa39140f6`
- Images: none
- Duplicate sources: `pages\2772.html`, `pages\26227.html`, `pages\17174.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (4-door)

NOTE: If the door lock system and the keyless operation do not work, troubleshoot the door locks first. The system does not function when turn the vehicle to the ON mode.

Symptom | Check Items | Also check for

The security system sounds randomly while the doors are locked | Tripped sensor recall

The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed | Symptom troubleshooting

Security alarm system will not arm | Symptom troubleshooting

All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote | Poor ground (G501, G305 *) Blown No. B16 fuse Body control module input test Power window master switch input test Keyless transmitter test Remote test

- Poor ground (G501, G305 *)

- Blown No. B16 fuse

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test

Driver's door will not lock or unlock | Poor ground (G501) Blown No. B25 fuse Blown No. B39 fuse Door switch test (check the door switch ON/OFF information with the HDS) Body control module input test Power window master switch input test Driver's door lock actuator test

- Poor ground (G501)

- Blown No. B25 fuse

- Blown No. B39 fuse

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test

Left rear door will not lock or unlock | Poor ground (G601) Blown No. B13 fuse Blown No. B38 fuse Body control module input test Door switch test (check the door switch ON/OFF information with the HDS) Left rear door lock actuator test

- Poor ground (G601)

- Blown No. B13 fuse

- Blown No. B38 fuse

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Left rear door lock actuator test

Front passenger's and right rear doors will not lock or unlock | Poor ground (G505, G602) Blown No. B12 fuse Blown No. B26 fuse Body control module input test Door switch test (check the door switch ON/OFF information with the HDS) Door lock actuator test

- Poor ground (G505, G602)

- Blown No. B12 fuse

- Blown No. B26 fuse

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test

Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch | Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)

Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened | Symptom troubleshooting

Auto door unlock does not work | Symptom troubleshooting

*: L15BY engine
````

## Chunk 1578: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\731.html`
- Chunk ID: `chunk_079b2de0c28c`
- Images: none
- Duplicate sources: `pages\2773.html`, `pages\26228.html`, `pages\17175.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Symptom Troubleshooting Index (5-door) (2017 2018 2019 2020 2021)

NOTE: If the door lock system and the keyless operation do not work, troubleshoot the door locks first. The system does not function when turn the vehicle to the ON mode.

Symptom | Check Items | Also check for

The security system sounds randomly while the doors are locked | Tripped sensor recall

The horn does not sound and/or the headlights do not flash when the PANIC button on the keyless transmitter/remote is pressed | Symptom troubleshooting

Security alarm system will not arm | Symptom troubleshooting

All the doors will not lock or unlock with driver's door key cylinder or door lock switch or keyless transmitter/remote | Poor ground (G305, G501) Blown No. B16 (20 A) fuse in the under-dash fuse/relay box Body control module input test Power window master switch input test Keyless transmitter test Remote test

- Poor ground (G305, G501)

- Blown No. B16 (20 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Power window master switch input test

- Keyless transmitter test

- Remote test

Driver's door will not lock or unlock | Poor ground (G501) Blown No. B25 (10 A) fuse in the under-dash fuse/relay box Blown No. B39 (10 A) fuse in the under-dash fuse/relay box Door switch test (check the door switch ON/OFF information with the HDS) Body control module input test Power window master switch input test Driver's door lock actuator test

- Poor ground (G501)

- Blown No. B25 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B39 (10 A) fuse in the under-dash fuse/relay box

- Door switch test (check the door switch ON/OFF information with the HDS)

- Body control module input test

- Power window master switch input test

- Driver's door lock actuator test

Left rear door will not lock or unlock | Poor ground (G601) Blown No. B13 (10 A) fuse in the under-dash fuse/relay box Blown No. B38 (10 A) fuse in the under-dash fuse/relay box Body control module input test Door switch test (check the door switch ON/OFF information with the HDS) Left rear door lock actuator test

- Poor ground (G601)

- Blown No. B13 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B38 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Left rear door lock actuator test

Front passenger's and right rear doors will not lock or unlock | Poor ground (G505, G602) Blown No. B12 (10 A) fuse in the under-dash fuse/relay box Blown No. B26 (10 A) fuse in the under-dash fuse/relay box Body control module input test Door switch test (check the door switch ON/OFF information with the HDS) Door lock actuator test

- Poor ground (G505, G602)

- Blown No. B12 (10 A) fuse in the under-dash fuse/relay box

- Blown No. B26 (10 A) fuse in the under-dash fuse/relay box

- Body control module input test

- Door switch test (check the door switch ON/OFF information with the HDS)

- Door lock actuator test

Passenger doors will not unlock with the remote or key cylinder switch, but will unlock with the inside door unlock switch | Driver's door lock knob switch test (check for door lock knob switch ON/OFF information with the HDS)

Symptom | Check Items | Also check for

Doors automatically relock 30 seconds after being unlocked with the remote even though a door has been opened | Symptom troubleshooting

Auto door unlock does not work | Symptom troubleshooting
````

## Chunk 1579: Immobilizer System Component Location Index (2/4-door)

- Title: Immobilizer System Component Location Index (2/4-door)
- Source path: `pages\733.html`
- Chunk ID: `chunk_491cb85521c5`
- Images: `images\GHH411469.jpeg`, `images\GHH411470.jpeg`, `images\GHH411471.jpeg`
- Duplicate sources: `pages\2775.html`, `pages\26230.html`, `pages\14441.html`

### Full Text

````text
# Immobilizer System Component Location Index (2/4-door)

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1580: Keyless Access System Component Location Index (Except K20C1 (M/T))

- Title: Keyless Access System Component Location Index (Except K20C1 (M/T))
- Source path: `pages\734.html`
- Chunk ID: `chunk_f428ab8c0212`
- Images: `images\GHH411472.jpeg`, `images\GHH411473.jpeg`, `images\GHH411474.jpeg`, `images\GHH411475.jpeg`, `images\GHH411476.jpeg`, `images\GHH411477.jpeg`
- Duplicate sources: `pages\2776.html`, `pages\26231.html`, `pages\17177.html`

### Full Text

````text
# Keyless Access System Component Location Index (Except K20C1 (M/T))

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1581: Keyless Access System Component Location Index (L15B7/L15BA (CVT))

- Title: Keyless Access System Component Location Index (L15B7/L15BA (CVT))
- Source path: `pages\735.html`
- Chunk ID: `chunk_ff381c0c8b45`
- Images: `images\GHH411478.jpeg`, `images\GHH411479.jpeg`, `images\GHH411480.jpeg`, `images\GHH411481.jpeg`, `images\GHH411482.jpeg`, `images\GHH411483.jpeg`, `images\GHH411484.jpeg`, `images\GHH411485.jpeg`, `images\GHH411486.jpeg`, `images\GHH411487.jpeg`, `images\GHH411488.jpeg`, `images\GHH411489.jpeg`
- Duplicate sources: `pages\2777.html`, `pages\26232.html`, `pages\14440.html`

### Full Text

````text
# Keyless Access System Component Location Index (L15B7/L15BA (CVT))

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1582: Keyless/Power Door Locks/Security System Component Location Index (2-door)

- Title: Keyless/Power Door Locks/Security System Component Location Index (2-door)
- Source path: `pages\736.html`
- Chunk ID: `chunk_9dc8fc9a7716`
- Images: `images\GHH411490.jpeg`, `images\GHH411491.jpeg`, `images\GHH411492.jpeg`, `images\GHH411493.jpeg`, `images\GHH411494.jpeg`, `images\GHH411495.jpeg`, `images\GHH411496.jpeg`, `images\GHH411497.jpeg`, `images\GHH411498.jpeg`
- Duplicate sources: `pages\2778.html`, `pages\26233.html`, `pages\17178.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Component Location Index (2-door)

Without Keyless Access System

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System Without Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System and Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1583: Keyless/Power Door Locks/Security System Component Location Index (4-door)

- Title: Keyless/Power Door Locks/Security System Component Location Index (4-door)
- Source path: `pages\737.html`
- Chunk ID: `chunk_c04a00faae59`
- Images: `images\GHH411499.jpeg`, `images\GHH411500.jpeg`, `images\GHH411501.jpeg`, `images\GHH411502.jpeg`, `images\GHH411503.jpeg`, `images\GHH411504.jpeg`, `images\GHH411505.jpeg`, `images\GHH411506.jpeg`, `images\GHH411507.jpeg`
- Duplicate sources: `pages\2779.html`, `pages\26234.html`, `pages\14439.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Component Location Index (4-door)

Without Keyless Access System

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System Without Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System and Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1584: Keyless/Power Door Locks/Security System Component Location Index (4/5-door)

- Title: Keyless/Power Door Locks/Security System Component Location Index (4/5-door)
- Source path: `pages\738.html`
- Chunk ID: `chunk_0f85b4604448`
- Images: `images\GHH411508.jpeg`, `images\GHH411509.jpeg`, `images\GHH411510.jpeg`, `images\GHH411511.jpeg`, `images\GHH411512.jpeg`, `images\GHH411513.jpeg`, `images\GHH411514.jpeg`, `images\GHH411515.jpeg`, `images\GHH411516.jpeg`
- Duplicate sources: `pages\2780.html`, `pages\26235.html`, `pages\17179.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Component Location Index (4/5-door)

Without Keyless Access System

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System Without Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

With Keyless Access System and Remote Engine Start

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1585: HomeLink Unit Connector for Inputs and Outputs

- Title: HomeLink Unit Connector for Inputs and Outputs
- Source path: `pages\739.html`
- Chunk ID: `chunk_dd3fd064b0f5`
- Images: `images\GHH411517.jpeg`
- Duplicate sources: `pages\2781.html`, `pages\26236.html`, `pages\17180.html`

### Full Text

````text
# HomeLink Unit Connector for Inputs and Outputs

Courtesy of HONDA, U.S.A., INC.

Terminal number | Terminal name | Description | Signal

1 | +B BACK UP | Power source for HomeLink unit | About battery voltage at all time

2 | ILLUMI+ | Detects ILLUMI+ signal | With parking lights are ON: about battery voltage With parking lights are OFF: less than 0.2 V

3 | Not used | --- | ---

4 | Not used | --- | ---

5 | BACK LT | Detects BACK LT signal | With the vehicle in the ON mode and R position/mode: about battery voltage If none of the above conditions are met: less than 0.2 V

6 | GND | Ground for HomeLink unit | Less than 0.2 V at all times

7 | IG2 A/C | IG2 power source | With the vehicle in the ON mode: about battery voltage
````

## Chunk 1586: Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (2/4-door)

- Title: Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (2/4-door)
- Source path: `pages\740.html`
- Chunk ID: `chunk_a293e8d2fde0`
- Images: `images\GHH411518.jpeg`
- Duplicate sources: `pages\2782.html`, `pages\26237.html`, `pages\13547.html`

### Full Text

````text
# Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (2/4-door)

Courtesy of HONDA, U.S.A., INC.

Terminal number | Terminal name | Description | Signal

1 | GND | Ground for immobilizer-keyless control unit | Less than 0.2 V at all times

2 | S-NET | Communication line | ---

3 | K LINE | Communication line | ---

4 | B-CAN_H | Communication line | ---

5 | B-CAN_L | Communication line | ---

6 | IG1 MON | IG1 power source | With vehicle in ON or START mode: about battery voltage

7 | +B BACK UP | Power source for immobilizer-keyless control unit | About battery voltage at all times
````

## Chunk 1587: Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

- Title: Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\741.html`
- Chunk ID: `chunk_60a41214e7fc`
- Images: `images\GHH411519.jpeg`
- Duplicate sources: `pages\2783.html`, `pages\26238.html`, `pages\17181.html`

### Full Text

````text
# Immobilizer-Keyless Control Unit Connector for Inputs and Outputs (5-door) (2017 2018 2019 2020 2021)

Courtesy of HONDA, U.S.A., INC.

Terminal number | Terminal name | Description | Signal

1 | GND | Ground for immobilizer-keyless control unit | Less than 0.2 V at all times

2 | S-NET | Communication line | ---

3 | K LINE | Communication line | ---

4 | B-CAN_H | Communication line | ---

5 | B-CAN_L | Communication line | ---

6 | IG1 FUEL PUMP | IG1 power source | With the vehicle in the ON or the START mode: about battery voltage

7 | +B BACK UP | Power source for immobilizer-keyless control unit | About battery voltage at all times
````

## Chunk 1588: Immobilizer-Keyless Control Unit Input Test (2/4-door)

- Title: Immobilizer-Keyless Control Unit Input Test (2/4-door)
- Source path: `pages\742.html`
- Chunk ID: `chunk_30d1b302093c`
- Images: `images\GHH411520.jpeg`
- Duplicate sources: `pages\2784.html`, `pages\26239.html`, `pages\17182.html`

### Full Text

````text
# Immobilizer-Keyless Control Unit Input Test (2/4-door)

NOTE:

- SRS components are located in this area. Review the SRS component locations , and precautions and procedures before performing repairs or servicing.

- Before testing, make sure the No. A18 (10 A) fuse in the under-hood fuse/relay box is OK.

- Before testing, make sure the No. B11 (5 A) fuse in the under-dash fuse/relay box is OK.

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect the immobilizer-keyless control unit 7P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals are OK, go to step 4.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 5.

Cavity | Wire | Terminal name | Test condition | Test: Desired result | Possible cause if desired result is not obtained

2 | RED | S-NET | Jump the SCS line with the HDS, disconnect PCM connector A (50P) | Measure the voltage to ground: There should be about 5 V. | An open or high resistance in the wire A short to ground in the wire

- An open or high resistance in the wire

- A short to ground in the wire

Check for continuity between the terminal and PCM connector A (50P) terminal No. 40: There should be continuity. | An open or high resistance in the wire

Disconnect the 12 volt battery negative terminal | Measure the resistance between the terminal and body ground: There should be more than 50 kΩ. | Poor ground (G503) An open or high resistance in the ground wire

- Poor ground (G503)

- An open or high resistance in the ground wire

Reconnect the connector to the immobilizer-keyless control unit, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, replace the immobilizer-keyless control unit .

NOTE: After replacing the immobilizer-keyless control unit, and do the immobilizer key registration .

Cavity | Wire | Terminal name | Test condition | Test: Desired result | Possible cause if desired result is not obtained

7 | RED | +B BACK UP | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

6 | PUR | IG1 MON | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B11 (5 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B11 (5 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

1 | BRN | GND | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G503) An open or high resistance in the ground wire

- Poor ground (G503)

- An open or high resistance in the ground wire

3 | LT BLU | K LINE | Under all conditions | Measure the voltage to ground: There should be pulse voltage (digital signal). | Faulty control unit on the K LINE Short to ground in the K LINE wire

- Faulty control unit on the K LINE

- Short to ground in the K LINE wire
````

## Chunk 1589: Immobilizer-Keyless Control Unit Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Immobilizer-Keyless Control Unit Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\743.html`
- Chunk ID: `chunk_8f698edc8da6`
- Images: `images\GHH411521.jpeg`
- Duplicate sources: `pages\2785.html`, `pages\26240.html`, `pages\17183.html`

### Full Text

````text
# Immobilizer-Keyless Control Unit Input Test (5-door) (2017 2018 2019 2020 2021)

NOTE:

- SRS components are located in this area. Review the SRS component locations , and precautions and procedures before performing repairs or servicing.

- Before testing, make sure the No. A18 (10 A) fuse in the under-hood fuse/relay box is OK.

- Before testing, make sure the No. B8 (15 A) fuse in the under-dash fuse/relay box is OK.

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect the immobilizer-keyless control unit 7P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals are OK, go to step 4.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 5.

Cavity | Wire | Terminal name | Test condition | Test: Desired result | Possible cause if desired result is not obtained

2 | RED | S-NET | Jump the SCS line with the HDS, disconnect PCM connector A (50P) | Measure the voltage to ground: There should be about 5 V. | An open or high resistance in the wire A short to ground in the wire

- An open or high resistance in the wire

- A short to ground in the wire

Check for continuity between the terminal and PCM connector A (50P) terminal No. 40: There should be continuity. | An open or high resistance in the wire

Disconnect the 12 volt battery negative terminal | Measure the resistance between the terminal and body ground: There should be more than 50 kΩ. | Poor ground (G503) An open or high resistance in the ground wire

- Poor ground (G503)

- An open or high resistance in the ground wire

Reconnect the connector to the immobilizer-keyless control unit, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, replace the immobilizer-keyless control unit .

NOTE: After replacing the immobilizer-keyless control unit, and do the immobilizer key registration .

Cavity | Wire | Terminal name | Test condition | Test: Desired result | Possible cause if desired result is not obtained

7 | RED | +B BACK UP | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

6 | BLU | IG1 FUEL PUMP | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 (15 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B8 (15 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

1 | BRN | GND | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G503) An open or high resistance in the ground wire

- Poor ground (G503)

- An open or high resistance in the ground wire

3 | LT BLU | K LINE | Under all conditions | Measure the voltage to ground: There should be pulse voltage (digital signal). | Faulty control unit on the K LINE Short to ground in the K LINE wire

- Faulty control unit on the K LINE

- Short to ground in the K LINE wire
````

## Chunk 1590: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)
- Source path: `pages\744.html`
- Chunk ID: `chunk_33d65040fd00`
- Images: `images\GHH411522.jpeg`, `images\GHH411523.jpeg`
- Duplicate sources: `pages\2786.html`, `pages\26241.html`, `pages\17184.html`

### Full Text

````text
# Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)

NOTE:

- Before testing, check for DTCs. If any DTCs are indicated, troubleshoot those DTCs first.

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

- Before testing, make sure the No. A1-5, No. A2-2, and No. A18 fuses are OK.

- Before testing, make sure the No. B8, No. B11*, and No. B30 fuses are OK. *: Except L15BY engine

*: Except L15BY engine

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect the body control module connectors.

NOTE: All connector views are shown from the wire side of the female terminals.

Courtesy of HONDA, U.S.A., INC.

Inspect the connectors and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 4.

With the connectors still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, then go to step 5.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

D36 | LT BLU | Under all conditions | Check for continuity between terminal D36 and data link connector (DLC) terminal No. 7: There should be continuity. | An open or high resistance in the K LINE wire

Check for continuity between terminal D36 and body ground: There should be no continuity. | A short to ground in the K LINE wire

F21 | YEL | Under all conditions | Check for continuity between terminal F21 and data link connector (DLC) terminal No. 15: There should be continuity. | An open or high resistance in the L-LINE wire

Check for continuity between terminal F21 and body ground: There should be no continuity. | A short to ground in the L-LINE wire

G18 | WHT | Press the engine start/stop switch button | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 fuse Faulty engine start/stop switch An open or high resistance in the wire

- Blown No. B30 fuse

- Faulty engine start/stop switch

- An open or high resistance in the wire

G9 | BLK | Press the engine start/stop switch button | Check for continuity to ground: There should be continuity. | Faulty engine start/stop switch Poor ground (G503) or an open in the ground wire An open or high resistance in the wire

- Faulty engine start/stop switch

- Poor ground (G503) or an open in the ground wire

- An open or high resistance in the wire

D35 | RED | Jump the SCS line with the HDS, disconnect PCM connector A (50P) | Check for continuity between terminal D35 and PCM connector A (50P) terminal No. 40: There should be continuity. | An open in the S-NET wire PCM

- An open in the S-NET wire

- PCM

Check for continuity between terminal D5 and body ground: There should be no continuity. | A short to ground in the S-NET wire

Reconnect the connectors, and do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, then go to step 6.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B16 | YEL | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 fuse An open or high resistance in the wire

- Blown No. B30 fuse

- An open or high resistance in the wire

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 fuse An open or high resistance in the wire

- Blown No. A18 fuse

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained
````

## Chunk 1591: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)
- Source path: `pages\744.html`
- Chunk ID: `chunk_afbb6c9d0525`
- Images: `images\GHH411522.jpeg`, `images\GHH411523.jpeg`
- Duplicate sources: `pages\2786.html`, `pages\26241.html`, `pages\17184.html`

### Full Text

````text
se An open or high resistance in the wire

- Blown No. A18 fuse

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

G27 | RED | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A2-2 fuse An open or high resistance in the wire

- Blown No. A2-2 fuse

- An open or high resistance in the wire

E1 | PUR *6BLU *7 | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 fuse Blown No. B11*6 fuse An open or high resistance in the wire

- Blown No. B8 fuse

- Blown No. B11*6 fuse

- An open or high resistance in the wire

G10 | YEL | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A1-5 fuse An open or high resistance in the wire

- Blown No. A1-5 fuse

- An open or high resistance in the wire

G11 | LT BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A1-5 fuse An open or high resistance in the wire

- Blown No. A1-5 fuse

- An open or high resistance in the wire

G19 | YEL | Driver's door outer handle lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door outer handle Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door outer handle

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door outer handle lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty driver's door outer handle A short to ground in the wire

- Faulty driver's door outer handle

- A short to ground in the wire

G1 *1 | LT GRN | Front passenger's door outer handle lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door outer handle Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Faulty front passenger's door outer handle

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Front passenger's door outer handle lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty front passenger's door outer handle A short to ground in the wire

- Faulty front passenger's door outer handle

- A short to ground in the wire

G1 *2 | LT GRN | Passenger's door outer handle lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty passenger's door outer handle Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Faulty passenger's door outer handle

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Passenger's door outer handle lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty passenger's door outer handle A short to ground in the wire

- Faulty passenger's door outer handle

- A short to ground in the wire

G23 | BRN | Electric parking brake switch applied | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric parking brake switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty electric parking brake switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

Brake pedal pressed and electric parking brake switch released | Measure the voltage to ground: There should be about 5 V. | Faulty electric parking brake switch A short to ground in the wire

- Faulty electric parking brake switch

- A short to ground in the wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine
````

## Chunk 1592: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)
- Source path: `pages\744.html`
- Chunk ID: `chunk_73f85b878d98`
- Images: `images\GHH411522.jpeg`, `images\GHH411523.jpeg`
- Duplicate sources: `pages\2786.html`, `pages\26241.html`, `pages\17184.html`

### Full Text

````text
ndle

- A short to ground in the wire

G23 | BRN | Electric parking brake switch applied | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric parking brake switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty electric parking brake switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

Brake pedal pressed and electric parking brake switch released | Measure the voltage to ground: There should be about 5 V. | Faulty electric parking brake switch A short to ground in the wire

- Faulty electric parking brake switch

- A short to ground in the wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

C4 | WHT | Trunk lid outer handle switch pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty trunk lid outer handle switch Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid outer handle switch

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

Trunk lid outer handle switch released | Measure the voltage to ground: There should be battery voltage. | Faulty trunk lid outer handle switch A short to ground in the wire

- Faulty trunk lid outer handle switch

- A short to ground in the wire

C1 *3 | GRN | Shift lever in P position/mode | Measure the voltage to ground: There should be less than 0.2 V. | Faulty transmission range switch Poor ground (G201) or an open in the ground wire An open or high resistance in the wire

- Faulty transmission range switch

- Poor ground (G201) or an open in the ground wire

- An open or high resistance in the wire

Shift lever in any other position/mode other than P | Measure the voltage to ground: There should be battery voltage. | Faulty transmission range switch A short to ground in the wire

- Faulty transmission range switch

- A short to ground in the wire

C26 *3 | LT BLU | Shift lever in P position/mode | Measure the voltage to ground: There should be battery voltage. | Faulty park pin switch A short to ground in the wire

- Faulty park pin switch

- A short to ground in the wire

Shift lever in any other position/mode than P | Measure the voltage to ground: There should be less than 0.2 V. | Faulty park pin switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty park pin switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

C26 *4 | YEL | Clutch pedal released | Measure the voltage to ground: There should be battery voltage. | Faulty clutch pedal position switch A A short to ground in the wire

- Faulty clutch pedal position switch A

- A short to ground in the wire

Clutch pedal pressed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty clutch pedal position switch A Poor ground (G305) or an open in the ground wire An open or high resistance in the wire

- Faulty clutch pedal position switch A

- Poor ground (G305) or an open in the ground wire

- An open or high resistance in the wire

C25 | TAN *6GRY *7 | Brake pedal pressed | Measure the voltage to ground: There should be battery voltage. | Blown No. A8*7 fuse Blown No. A9*6 fuse Faulty brake pedal position switch An open or high resistance in the wire

- Blown No. A8*7 fuse

- Blown No. A9*6 fuse

- Faulty brake pedal position switch

- An open or high resistance in the wire

G3 *5 | PUR | Electric steering lock (LOCK) | Measure the voltage to ground: There should be about 5 V. | Faulty electric steering lock A short to ground in the wire

- Faulty electric steering lock

- A short to ground in the wire

Electric steering lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine

Electric Steering Lock

NOTE:

- SRS components are located in this area. Review the SRS component locations , and precautions and procedures before doing repairs or servicing.

- Before testing, check for DTCs.
````

## Chunk 1593: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (2/4-door)
- Source path: `pages\744.html`
- Chunk ID: `chunk_40c70792914b`
- Images: `images\GHH411522.jpeg`, `images\GHH411523.jpeg`
- Duplicate sources: `pages\2786.html`, `pages\26241.html`, `pages\17184.html`

### Full Text

````text
PUR | Electric steering lock (LOCK) | Measure the voltage to ground: There should be about 5 V. | Faulty electric steering lock A short to ground in the wire

- Faulty electric steering lock

- A short to ground in the wire

Electric steering lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

*1: 4-door

*2: 2-door

*3: CVT

*4: M/T

*5: With electric steering lock

*6: Except L15BY engine

*7: L15BY engine

Electric Steering Lock

NOTE:

- SRS components are located in this area. Review the SRS component locations , and precautions and procedures before doing repairs or servicing.

- Before testing, check for DTCs. If any DTCs are indicated, troubleshoot those DTCs first.

6. Turn the vehicle to the OFF (LOCK) mode.

7. Disconnect the electric steering lock 12P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, then go to step 9.

Reconnect the connector, and do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 10.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

3 | YEL | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 fuse An open or high resistance in the wire

- Blown No. B30 fuse

- An open or high resistance in the wire

12 | BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 fuse An open or high resistance in the wire

- Blown No. B8 fuse

- An open or high resistance in the wire

7 | BRN | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G503) An open or high resistance in the ground wire

- Poor ground (G503)

- An open or high resistance in the ground wire

8 | PUR | Electric steering lock (LOCK) | Measure the voltage to ground: There should be about 5 V. | Faulty body control module A short to ground in the wire

- Faulty body control module

- A short to ground in the wire

Electric steering lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

5 | YEL | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Faulty body control module An open or high resistance in the wire A short to ground in the wire

- Faulty body control module

- An open or high resistance in the wire

- A short to ground in the wire

10. If multiple failures are found on more than one control unit, replace the body control module . If input failures are related to a particular control unit, replace the control unit.
````

## Chunk 1594: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\745.html`
- Chunk ID: `chunk_2f79c88adaf4`
- Images: `images\GHH411524.jpeg`, `images\GHH411525.jpeg`
- Duplicate sources: `pages\2787.html`, `pages\26242.html`, `pages\17185.html`

### Full Text

````text
# Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)

NOTE:

- Before testing, check for DTCs. If any DTCs are indicated, troubleshoot those DTCs first.

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

- Before testing, make sure the No. A1-5 (30 A), No. A2-2 (30 A), and No. A18 (10 A) fuses in the under-hood fuse/relay box are OK.

- Before testing, make sure the No. B8 (15 A) *1/(20 A) *2 and No. B30 (10 A) fuses in the under-dash fuse/relay box are OK.

*1: Except K20C1 engine

*2: K20C1 engine

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect the body control module connectors.

NOTE: All connector views are shown from the wire side of the female terminals.

Courtesy of HONDA, U.S.A., INC.

Inspect the connectors and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 4.

With the connectors still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, then go to step 5.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

D36 | LT BLU | Under all conditions | Check for continuity between terminal D36 and data link connector (DLC) terminal No. 7: There should be continuity. | An open or high resistance in the K LINE wire

Check for continuity between terminal D36 and body ground: There should be no continuity. | A short to ground in the K LINE wire

F21 | YEL | Under all conditions | Check for continuity between terminal F21 and data link connector (DLC) terminal No. 15: There should be continuity. | An open or high resistance in the L-LINE wire

Check for continuity between terminal F21 and body ground: There should be no continuity. | A short to ground in the L-LINE wire

G18 | WHT | Press the engine start/stop switch button | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 (10 A) fuse in the under-dash fuse/relay box Faulty engine start/stop switch An open or high resistance in the wire

- Blown No. B30 (10 A) fuse in the under-dash fuse/relay box

- Faulty engine start/stop switch

- An open or high resistance in the wire

G9 | BLK | Press the engine start/stop switch button | Check for continuity to ground: There should be continuity. | Faulty engine start/stop switch Poor ground (G503) or an open in the ground wire An open or high resistance in the wire

- Faulty engine start/stop switch

- Poor ground (G503) or an open in the ground wire

- An open or high resistance in the wire

D35 | RED | Jump the SCS line with the HDS, disconnect PCM connector A (50P) | Check for continuity between terminal D35 and PCM connector A (50P) terminal No. 40: There should be continuity. | An open in the S-NET wire PCM

- An open in the S-NET wire

- PCM

Check for continuity between terminal D5 and body ground: There should be no continuity. | A short to ground in the S-NET wire

Reconnect the connectors, and do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, then go to step 6.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B16 | YEL | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 (10 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B30 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V.
````

## Chunk 1595: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\745.html`
- Chunk ID: `chunk_feb8e8b79802`
- Images: `images\GHH411524.jpeg`, `images\GHH411525.jpeg`
- Duplicate sources: `pages\2787.html`, `pages\26242.html`, `pages\17185.html`

### Full Text

````text
r-dash fuse/relay box An open or high resistance in the wire

- Blown No. B30 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

G27 | RED | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A2-2 (30 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A2-2 (30 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

E1 | BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 (15 A) *4/(20 A) *5 fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B8 (15 A) *4/(20 A) *5 fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

G10 | YEL | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A1-5 (30 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A1-5 (30 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

G11 | LT BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. A1-5 (30 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A1-5 (30 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

G19 | YEL | Driver's door outer handle lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door outer handle Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door outer handle

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door outer handle lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty driver's door outer handle A short to ground in the wire

- Faulty driver's door outer handle

- A short to ground in the wire

G1 | LT GRN | Front passenger's door outer handle lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door outer handle Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Faulty front passenger's door outer handle

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Front passenger's door outer handle lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty front passenger's door outer handle A short to ground in the wire

- Faulty front passenger's door outer handle

- A short to ground in the wire

G23 | BRN | Electric parking brake switch applied | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric parking brake switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty electric parking brake switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

Brake pedal pressed and electric parking brake switch released | Measure the voltage to ground: There should be about 5 V. | Faulty electric parking brake switch A short to ground in the wire

- Faulty electric parking brake switch

- A short to ground in the wire

C4 | WHT | Tailgate outer handle switch pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty tailgate outer handle switch Poor ground (G603) or an open in the ground wire An open or high resistance in the wire
````

## Chunk 1596: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\745.html`
- Chunk ID: `chunk_dba0d2601f84`
- Images: `images\GHH411524.jpeg`, `images\GHH411525.jpeg`
- Duplicate sources: `pages\2787.html`, `pages\26242.html`, `pages\17185.html`

### Full Text

````text
There should be less than 0.2 V. | Faulty electric parking brake switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty electric parking brake switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

Brake pedal pressed and electric parking brake switch released | Measure the voltage to ground: There should be about 5 V. | Faulty electric parking brake switch A short to ground in the wire

- Faulty electric parking brake switch

- A short to ground in the wire

C4 | WHT | Tailgate outer handle switch pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty tailgate outer handle switch Poor ground (G603) or an open in the ground wire An open or high resistance in the wire

- Faulty tailgate outer handle switch

- Poor ground (G603) or an open in the ground wire

- An open or high resistance in the wire

Tailgate outer handle switch released | Measure the voltage to ground: There should be about 5 V. | Faulty tailgate outer handle switch A short to ground in the wire

- Faulty tailgate outer handle switch

- A short to ground in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

C1 *1 | GRN | Shift lever in P position/mode | Measure the voltage to ground: There should be less than 0.2 V. | Faulty transmission range switch Poor ground (G201) or an open in the ground wire An open or high resistance in the wire

- Faulty transmission range switch

- Poor ground (G201) or an open in the ground wire

- An open or high resistance in the wire

Shift lever in any other position/mode other than P | Measure the voltage to ground: There should be battery voltage. | Faulty transmission range switch A short to ground in the wire

- Faulty transmission range switch

- A short to ground in the wire

C26 *1 | LT BLU | Shift lever in P position/mode | Measure the voltage to ground: There should be battery voltage. | Faulty park pin switch A short to ground in the wire

- Faulty park pin switch

- A short to ground in the wire

Shift lever in any other position/mode than P | Measure the voltage to ground: There should be less than 0.2 V. | Faulty park pin switch Poor ground (G502) or an open in the ground wire An open or high resistance in the wire

- Faulty park pin switch

- Poor ground (G502) or an open in the ground wire

- An open or high resistance in the wire

C26 *2 | YEL | Clutch pedal released | Measure the voltage to ground: There should be battery voltage. | Faulty clutch pedal position switch A A short to ground in the wire

- Faulty clutch pedal position switch A

- A short to ground in the wire

Clutch pedal pressed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty clutch pedal position switch A Poor ground (G302) or an open in the ground wire An open or high resistance in the wire

- Faulty clutch pedal position switch A

- Poor ground (G302) or an open in the ground wire

- An open or high resistance in the wire

C25 | GRY | Brake pedal pressed | Measure the voltage to ground: There should be battery voltage. | Blown No. A8 (10 A) fuse in the under-hood fuse/relay box Faulty brake pedal position switch An open or high resistance in the wire

- Blown No. A8 (10 A) fuse in the under-hood fuse/relay box

- Faulty brake pedal position switch

- An open or high resistance in the wire

G3 *3 | PUR | Electric steering lock (LOCK) | Measure the voltage to ground: There should be about 5 V. | Faulty electric steering lock A short to ground in the wire

- Faulty electric steering lock

- A short to ground in the wire

Electric steering lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

G21 | WHT | Tailgate lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty tailgate outer handle Poor ground (G603) or an open in the ground wire An open or high resistance in the wire

- Faulty tailgate outer handle

- Poor ground (G603) or an open in the ground wire

- An open or high resistance in the wire

Tailgate lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty tailgate outer handle A short to ground in the wire

- Faulty tailgate outer handle

- A short to ground in the wire
````

## Chunk 1597: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access System (Body Control Module and Electric Steering Lock) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\745.html`
- Chunk ID: `chunk_238d4c331a79`
- Images: `images\GHH411524.jpeg`, `images\GHH411525.jpeg`
- Duplicate sources: `pages\2787.html`, `pages\26242.html`, `pages\17185.html`

### Full Text

````text
ring lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

G21 | WHT | Tailgate lock button pushed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty tailgate outer handle Poor ground (G603) or an open in the ground wire An open or high resistance in the wire

- Faulty tailgate outer handle

- Poor ground (G603) or an open in the ground wire

- An open or high resistance in the wire

Tailgate lock button released | Measure the voltage to ground: There should be about 5 V. | Faulty tailgate outer handle A short to ground in the wire

- Faulty tailgate outer handle

- A short to ground in the wire

*1: CVT

*2: M/T

*3: With electric steering lock

*4: Except K20C1 engine

*5: K20C1 engine

Electric Steering Lock

NOTE:

- SRS components are located in this area. Review the SRS component locations , and precautions and procedures before doing repairs or servicing.

- Before testing, check for DTCs. If any DTCs are indicated, troubleshoot those DTCs first.

6. Turn the vehicle to the OFF (LOCK) mode.

7. Disconnect the electric steering lock 12P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, then go to step 9.

Reconnect the connector, and do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 10.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

3 | YEL | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B30 (10 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B30 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

12 | BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

7 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G505) An open or high resistance in the ground wire

- Poor ground (G505)

- An open or high resistance in the ground wire

8 | PUR | Electric steering lock (LOCK) | Measure the voltage to ground: There should be about 5 V. | Faulty body control module A short to ground in the wire

- Faulty body control module

- A short to ground in the wire

Electric steering lock (UNLOCK) | Measure the voltage to ground: There should be less than 0.2 V. | Faulty electric steering lock An open or high resistance in the wire

- Faulty electric steering lock

- An open or high resistance in the wire

5 | YEL | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Faulty body control module An open or high resistance in the wire A short to ground in the wire

- Faulty body control module

- An open or high resistance in the wire

- A short to ground in the wire

*1: Except K20C1 engine

*2: K20C1 engine

10. If multiple failures are found on more than one control unit, replace the body control module . If input failures are related to a particular control unit, replace the control unit.
````

## Chunk 1598: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\746.html`
- Chunk ID: `chunk_554bd52b44d2`
- Images: `images\GHH411526.jpeg`, `images\GHH411527.jpeg`, `images\GHH411528.jpeg`
- Duplicate sources: `pages\2788.html`, `pages\26243.html`, `pages\17186.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

NOTE:

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

- Before testing, make sure the No. A18 (10 A) and No. A24 (10 A) fuses in the under-hood fuse/relay box are OK.

- Before testing, make sure the No. B9 (10 A), No. B11 (5 A), No. B12 (10 A), No. B15 (20 A), No. B16 (20 A), No. B25 (10 A), No. B26 (10 A), No. B28 (20 A), and No. B39 (10 A) fuses in the under-dash fuse/relay box are OK.

- Before testing, make sure the headlights, parking lights, side marker lights, taillights, and horns work properly.

- There are two pairs of fuses in the same circuit (No. B25 and No. B39 fuses, No. B12 and No. B26 fuses). If one fuse is blown, make sure to check the other fuse in the same circuit. If necessary, replace the blown fuse(s).

Body Control Module

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect body control module connectors A, B, C, D, and E .

NOTE: All connector views are shown from the wire side of the female terminals.

Courtesy of HONDA, U.S.A., INC.

Inspect the connectors and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 4.

With the connectors still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 5.

NOTE: These are door lock actuator operation tests for keyless entry.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B28 | GRY | Under all conditions | Connect to ground with a jumper wire: The horns should sound. | Blown No. A24 (10 A) fuse in the under-hood fuse/relay box Faulty horn relay Faulty horn An open or high resistance in the wire

- Blown No. A24 (10 A) fuse in the under-hood fuse/relay box

- Faulty horn relay

- Faulty horn

- An open or high resistance in the wire

D26 * | PNK | Ignition key inserted into the ignition key switch | Measure the voltage to ground: There should be less than 0.2 V. | Faulty ignition key switch An open or high resistance in the wire Poor ground (G503)

- Faulty ignition key switch

- An open or high resistance in the wire

- Poor ground (G503)

Ignition key removed from the ignition key switch | Measure the voltage to ground: There should be battery voltage. | Faulty ignition key switch A short to ground in the wire

- Faulty ignition key switch

- A short to ground in the wire

*: Without keyless access system

Reconnect the connectors to the body control module, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 6.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

E1 | PUR | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B11 (5 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B11 (5 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

B27 | BLU | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator, the passenger's door lock actuator, and the fuel fill door lock actuator should LOCK.
````

## Chunk 1599: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\746.html`
- Chunk ID: `chunk_3524d7a7eb2d`
- Images: `images\GHH411526.jpeg`, `images\GHH411527.jpeg`, `images\GHH411528.jpeg`
- Duplicate sources: `pages\2788.html`, `pages\26243.html`, `pages\17186.html`

### Full Text

````text
open or high resistance in the wire

- Blown No. B11 (5 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

B27 | BLU | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator, the passenger's door lock actuator, and the fuel fill door lock actuator should LOCK. | Faulty power door lock relay circuit (LOCK) Faulty driver's door lock actuator Faulty passenger's door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (LOCK)

- Faulty driver's door lock actuator

- Faulty passenger's door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

B31 | GRN | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator and the fuel fill door lock actuator should UNLOCK. | Faulty power door lock relay circuit (DR UNLOCK) Faulty driver's door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (DR UNLOCK)

- Faulty driver's door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

*1: CVT

*2: L15B7 engine

*3: K20C2 engine (type A)

*4: K20C2 engine (type B)

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B32 | PUR | In all power modes | Connect to ground with a jumper wire: The passenger's door lock actuator should UNLOCK. | Faulty power door lock relay circuit (UNLOCK) Faulty passenger's door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (UNLOCK)

- Faulty passenger's door lock actuator

- An open or high resistance in the wire

B29 | LT BLU | In all power modes | Connect to ground with a jumper wire: The trunk lid release actuator should work. | Faulty trunk lid release actuator relay circuit Faulty trunk lid release actuator Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid release actuator relay circuit

- Faulty trunk lid release actuator

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

D22 | GRN | Driver's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door switch Faulty driver's door switch ground An open or high resistance in the wire

- Faulty driver's door switch

- Faulty driver's door switch ground

- An open or high resistance in the wire

Driver's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door switch A short to ground in the wire

- Faulty driver's door switch

- A short to ground in the wire

D23 | LT GRN | Passenger's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty passenger's door switch Faulty passenger's door switch ground An open or high resistance in the wire

- Faulty passenger's door switch

- Faulty passenger's door switch ground

- An open or high resistance in the wire

Passenger's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty passenger's door switch A short to ground in the wire

- Faulty passenger's door switch

- A short to ground in the wire

D27 | WHT | Trunk lid open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty trunk lid latch switch Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid latch switch

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

Trunk lid closed | Measure the voltage to ground: There should be battery voltage. | Faulty trunk lid latch switch A short to ground in the wire

- Faulty trunk lid latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V.
````

## Chunk 1600: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\746.html`
- Chunk ID: `chunk_c528ab507cd5`
- Images: `images\GHH411526.jpeg`, `images\GHH411527.jpeg`, `images\GHH411528.jpeg`
- Duplicate sources: `pages\2788.html`, `pages\26243.html`, `pages\17186.html`

### Full Text

````text
should be battery voltage. | Faulty passenger's door switch A short to ground in the wire

- Faulty passenger's door switch

- A short to ground in the wire

D27 | WHT | Trunk lid open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty trunk lid latch switch Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid latch switch

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

Trunk lid closed | Measure the voltage to ground: There should be battery voltage. | Faulty trunk lid latch switch A short to ground in the wire

- Faulty trunk lid latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty hood latch switch Poor ground (G401 *2/*3, G402 *4) or an open in the ground wire An open or high resistance in the wire

- Faulty hood latch switch

- Poor ground (G401 *2/*3, G402 *4) or an open in the ground wire

- An open or high resistance in the wire

Hood open | Measure the voltage to ground: There should be battery voltage. | Faulty hood latch switch A short to ground in the wire

- Faulty hood latch switch

- A short to ground in the wire

C1 *1 | GRN | Shift lever in P position/mode | Measure the voltage to ground: There should be less than 0.2 V. | Faulty transmission range switch Poor ground (G201) or an open in the ground wire An open or high resistance in the wire

- Faulty transmission range switch

- Poor ground (G201) or an open in the ground wire

- An open or high resistance in the wire

Shift lever in any other position/mode than P | Measure the voltage to ground: There should be battery voltage. | Faulty transmission range switch A short to ground in the wire

- Faulty transmission range switch

- A short to ground in the wire

*1: CVT

*2: L15B7 engine

*3: K20C2 engine (type A)

*4: K20C2 engine (type B)

Door Multiplex Control Unit

6. Turn the vehicle to the OFF (LOCK) mode.

7. Disconnect the power window master switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 9.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 10.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | WHT | Disconnect these connectors: Passenger's power window switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 36 and passenger's power window switch 37P connector terminal No. 34: There should be continuity. | An open in the LIN(P/W) wire

- Passenger's power window switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 36 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 11.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

18 | BRN | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B9 (10 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B9 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

37 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No.
````

## Chunk 1601: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\746.html`
- Chunk ID: `chunk_15742c04f758`
- Images: `images\GHH411526.jpeg`, `images\GHH411527.jpeg`, `images\GHH411528.jpeg`
- Duplicate sources: `pages\2788.html`, `pages\26243.html`, `pages\17186.html`

### Full Text

````text
hicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B9 (10 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B9 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

37 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B28 (20 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B28 (20 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G502) An open or high resistance in the ground wire

- Poor ground (G502)

- An open or high resistance in the ground wire

29 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

7 | PUR | Driver's door key cylinder switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch A short to ground in the wire

- Faulty driver's door key cylinder switch

- A short to ground in the wire

8 | RED | Driver's door key cylinder switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- An open or high resistance in the wire

21 | YEL | Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

20 | LT BLU | Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

Passenger's Power Window Switch

11. Turn the vehicle to the OFF (LOCK) mode, open and close the driver's door.

12. Disconnect the passenger's power window switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.
````

## Chunk 1602: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (2-door) (2016 2017 2018 2019 2020)
- Source path: `pages\746.html`
- Chunk ID: `chunk_0020b90d3222`
- Images: `images\GHH411526.jpeg`, `images\GHH411527.jpeg`, `images\GHH411528.jpeg`
- Duplicate sources: `pages\2788.html`, `pages\26243.html`, `pages\17186.html`

### Full Text

````text
in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

Passenger's Power Window Switch

11. Turn the vehicle to the OFF (LOCK) mode, open and close the driver's door.

12. Disconnect the passenger's power window switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 14.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 15.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

34 | WHT | Disconnect these connectors: Power window master switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 34 and power window master switch 37P connector terminal No. 36: There should be continuity. | An open in the LIN(P/W) wire

- Power window master switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 34 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 16.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

1 | GRN | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B15 (20 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B15 (20 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G505) An open or high resistance in the ground wire

- Poor ground (G505)

- An open or high resistance in the ground wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | TAN | Passenger's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Passenger's door lock knob switch Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Passenger's door lock knob switch

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Passenger's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Passenger's door lock knob switch A short to ground in the wire

- Passenger's door lock knob switch

- A short to ground in the wire

16. If multiple failures are found on more than one control unit, replace the body control module . If input failures are related to a particular control unit, replace the control unit.
````

## Chunk 1603: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_485a04855800`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

NOTE:

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

- Before testing, make sure the No. A18 and No. A24 fuses are OK.

- Before testing, make sure the No. B8, No. B9, No. B11*, No. B12, No. B13, No. B15, No. B16, No. B25, No. B26, No. B28, No. B38, and No. B39 fuses are OK.

- Before testing, make sure the headlights, parking lights, side marker lights, taillights, and horns work properly.

- There are two pairs of fuses in the same circuit ( No. B25 and No. B39 fuses , No. B12 and No. B26 fuses , No. B13 and No. B38 fuses ). If one fuse is blown, make sure to check the other fuse in the same circuit. If necessary, replace the blown fuse(s). *: Except L15BY engine

*: Except L15BY engine

Body Control Module

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect body control module connectors A, B, C, D, and E .

NOTE: All connector views are shown from the wire side of the female terminals.

Courtesy of HONDA, U.S.A., INC.

Inspect the connectors and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 4.

With the connectors still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 5.

NOTE: These are door lock actuator operation tests for keyless entry.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B28 | GRY *2GRN *3 | Under all conditions | Connect to ground with a jumper wire: The horns should sound. | Blown No. A24 fuse Faulty horn relay Faulty horn An open or high resistance in the wire

- Blown No. A24 fuse

- Faulty horn relay

- Faulty horn

- An open or high resistance in the wire

D26 *1 | PNK | Ignition key inserted into the ignition key switch | Measure the voltage to ground: There should be less than 0.2 V. | Faulty ignition key switch An open or high resistance in the wire Poor ground (G503)

- Faulty ignition key switch

- An open or high resistance in the wire

- Poor ground (G503)

Ignition key removed from the ignition key switch | Measure the voltage to ground: There should be battery voltage. | Faulty ignition key switch A short to ground in the wire

- Faulty ignition key switch

- A short to ground in the wire

*1: Without keyless access system

*2: Except L15BY engine

*3: L15BY engine

Reconnect the connectors to the body control module, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 6.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 fuse An open or high resistance in the wire

- Blown No. A18 fuse

- An open or high resistance in the wire

E1 | PUR *5BLU *6 | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8*6 fuse Blown No. B11*5 fuse An open or high resistance in the wire

- Blown No. B8*6 fuse

- Blown No. B11*5 fuse

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

B27 | BLU | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator, the front passenger's door lock actuator, the left rear door lock actuator, the right rear door lock actuator, and the fuel fill door lock actuator should LOCK.
````

## Chunk 1604: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_0a7dc5df5d53`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
- Blown No. B11*5 fuse

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

B27 | BLU | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator, the front passenger's door lock actuator, the left rear door lock actuator, the right rear door lock actuator, and the fuel fill door lock actuator should LOCK. | Faulty power door lock relay circuit (LOCK) Faulty driver's door lock actuator Faulty front passenger's door lock actuator Faulty left rear door lock actuator Faulty right rear door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (LOCK)

- Faulty driver's door lock actuator

- Faulty front passenger's door lock actuator

- Faulty left rear door lock actuator

- Faulty right rear door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

*1: CVT

*2: L15B7 engine

*3: K20C2 engine (type A)

*4: K20C2 engine (type B)

*5: Except L15BY engine

*6: L15BY engine

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B31 | GRN | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator and the fuel fill door lock actuator should UNLOCK. | Faulty power door lock relay circuit (DR UNLOCK) Faulty driver's door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (DR UNLOCK)

- Faulty driver's door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

B32 | PUR | In all power modes | Connect to ground with a jumper wire: The front passenger's door lock actuator, the left rear door lock actuator, and the right rear door lock actuator should UNLOCK. | Faulty power door lock relay circuit (UNLOCK) Faulty front passenger's door lock actuator Faulty left rear door lock actuator Faulty right rear door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (UNLOCK)

- Faulty front passenger's door lock actuator

- Faulty left rear door lock actuator

- Faulty right rear door lock actuator

- An open or high resistance in the wire

B29 | LT BLU | In all power modes | Connect to ground with a jumper wire: The trunk lid release actuator should work. | Faulty trunk lid release actuator relay circuit Faulty trunk lid release actuator Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid release actuator relay circuit

- Faulty trunk lid release actuator

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

D22 | GRN | Driver's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door switch Faulty driver's door switch ground An open or high resistance in the wire

- Faulty driver's door switch

- Faulty driver's door switch ground

- An open or high resistance in the wire

Driver's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door switch A short to ground in the wire

- Faulty driver's door switch

- A short to ground in the wire

D23 | LT GRN | Front passenger's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door switch Faulty front passenger's door switch ground An open or high resistance in the wire

- Faulty front passenger's door switch

- Faulty front passenger's door switch ground

- An open or high resistance in the wire

Front passenger's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty front passenger's door switch A short to ground in the wire

- Faulty front passenger's door switch

- A short to ground in the wire

D24 | BRN | Left rear door open | Measure the voltage to ground: There should be less than 0.2 V.
````

## Chunk 1605: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_368d78246d3d`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
switch A short to ground in the wire

- Faulty driver's door switch

- A short to ground in the wire

D23 | LT GRN | Front passenger's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door switch Faulty front passenger's door switch ground An open or high resistance in the wire

- Faulty front passenger's door switch

- Faulty front passenger's door switch ground

- An open or high resistance in the wire

Front passenger's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty front passenger's door switch A short to ground in the wire

- Faulty front passenger's door switch

- A short to ground in the wire

D24 | BRN | Left rear door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty left rear door switch Faulty left rear door switch ground An open or high resistance in the wire

- Faulty left rear door switch

- Faulty left rear door switch ground

- An open or high resistance in the wire

Left rear door closed | Measure the voltage to ground: There should be battery voltage. | Faulty left rear door switch A short to ground in the wire

- Faulty left rear door switch

- A short to ground in the wire

*1: CVT

*2: L15B7 engine

*3: K20C2 engine (type A)

*4: K20C2 engine (type B)

*5: Except L15BY engine

*6: L15BY engine

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

D28 | GRY | Right rear door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty right rear door switch Faulty right rear door switch ground An open or high resistance in the wire

- Faulty right rear door switch

- Faulty right rear door switch ground

- An open or high resistance in the wire

Right rear door closed | Measure the voltage to ground: There should be battery voltage. | Faulty right rear door switch A short to ground in the wire

- Faulty right rear door switch

- A short to ground in the wire

C15 | LT BLU | Left rear door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty left rear door lock knob switch Poor ground (G601) or an open in the ground wire An open or high resistance in the wire

- Faulty left rear door lock knob switch

- Poor ground (G601) or an open in the ground wire

- An open or high resistance in the wire

Left rear door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty left rear door lock knob switch A short to ground in the wire

- Faulty left rear door lock knob switch

- A short to ground in the wire

C16 | GRY | Right rear door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty right rear door lock knob switch Poor ground (G602) or an open in the ground wire An open or high resistance in the wire

- Faulty right rear door lock knob switch

- Poor ground (G602) or an open in the ground wire

- An open or high resistance in the wire

Right rear door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty right rear door lock knob switch A short to ground in the wire

- Faulty right rear door lock knob switch

- A short to ground in the wire

D27 | WHT | Trunk lid open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty trunk lid latch switch Poor ground (G701) or an open in the ground wire An open or high resistance in the wire

- Faulty trunk lid latch switch

- Poor ground (G701) or an open in the ground wire

- An open or high resistance in the wire

Trunk lid closed | Measure the voltage to ground: There should be battery voltage. | Faulty trunk lid latch switch A short to ground in the wire

- Faulty trunk lid latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty hood latch switch Poor ground (G401 *2/*3/*6, G402 *4) or an open in the ground wire An open or high resistance in the wire

- Faulty hood latch switch

- Poor ground (G401 *2/*3/*6, G402 *4) or an open in the ground wire

- An open or high resistance in the wire

Hood open | Measure the voltage to ground: There should be battery voltage. | Faulty hood latch switch A short to ground in the wire

- Faulty hood latch switch

- A short to ground in the wire
````

## Chunk 1606: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_b1aba06432e6`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
high resistance in the wire

Trunk lid closed | Measure the voltage to ground: There should be battery voltage. | Faulty trunk lid latch switch A short to ground in the wire

- Faulty trunk lid latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty hood latch switch Poor ground (G401 *2/*3/*6, G402 *4) or an open in the ground wire An open or high resistance in the wire

- Faulty hood latch switch

- Poor ground (G401 *2/*3/*6, G402 *4) or an open in the ground wire

- An open or high resistance in the wire

Hood open | Measure the voltage to ground: There should be battery voltage. | Faulty hood latch switch A short to ground in the wire

- Faulty hood latch switch

- A short to ground in the wire

C1 *1 | GRN | Shift lever in P position/mode | Measure the voltage to ground: There should be less than 0.2 V. | Faulty transmission range switch Poor ground (G201) or an open in the ground wire An open or high resistance in the wire

- Faulty transmission range switch

- Poor ground (G201) or an open in the ground wire

- An open or high resistance in the wire

Shift lever in any other position/mode than P | Measure the voltage to ground: There should be battery voltage. | Faulty transmission range switch A short to ground in the wire

- Faulty transmission range switch

- A short to ground in the wire

*1: CVT

*2: L15B7 engine

*3: K20C2 engine (type A)

*4: K20C2 engine (type B)

*5: Except L15BY engine

*6: L15BY engine

Door Multiplex Control Unit

6. Turn the vehicle to the OFF (LOCK) mode.

7. Disconnect the power window master switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 9.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 10.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | WHT | Disconnect these connectors: Front passenger's power window switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 36 and front passenger's power window switch 37P connector terminal No. 34: There should be continuity. | An open in the LIN(P/W) wire

- Front passenger's power window switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 36 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 11.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

18 | BRN | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B9 fuse An open or high resistance in the wire

- Blown No. B9 fuse

- An open or high resistance in the wire

37 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 fuse An open or high resistance in the wire

- Blown No. A18 fuse

- An open or high resistance in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B28 fuse An open or high resistance in the wire

- Blown No. B28 fuse

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G502) An open or high resistance in the ground wire

- Poor ground (G502)

- An open or high resistance in the ground wire

29 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire
````

## Chunk 1607: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_24196ea071e7`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
re

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B28 fuse An open or high resistance in the wire

- Blown No. B28 fuse

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G502) An open or high resistance in the ground wire

- Poor ground (G502)

- An open or high resistance in the ground wire

29 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

7 | PUR | Driver's door key cylinder switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch A short to ground in the wire

- Faulty driver's door key cylinder switch

- A short to ground in the wire

8 | RED | Driver's door key cylinder switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- An open or high resistance in the wire

21 | YEL | Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

20 | LT BLU | Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

Front Passenger's Power Window Switch

11. Disconnect the front passenger's power window switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 13.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 14.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

34 | WHT | Disconnect these connectors: Power window master switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 34 and power window master switch 37P connector terminal No. 36: There should be continuity. | An open in the LIN(P/W) wire

- Power window master switch 37P connector

- Moonroof motor-control unit 14P connector *
````

## Chunk 1608: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (4-door)
- Source path: `pages\747.html`
- Chunk ID: `chunk_98da8d0f3a5b`
- Images: `images\GHH411529.jpeg`, `images\GHH411530.jpeg`, `images\GHH411531.jpeg`
- Duplicate sources: `pages\2789.html`, `pages\26244.html`, `pages\17187.html`

### Full Text

````text
ded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 13.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 14.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

34 | WHT | Disconnect these connectors: Power window master switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 34 and power window master switch 37P connector terminal No. 36: There should be continuity. | An open in the LIN(P/W) wire

- Power window master switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 34 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 15.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

1 | GRN | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B15 fuse An open or high resistance in the wire

- Blown No. B15 fuse

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G505) An open or high resistance in the ground wire

- Poor ground (G505)

- An open or high resistance in the ground wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | TAN | Front passenger's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Front passenger's door lock knob switch Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Front passenger's door lock knob switch

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Front passenger's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Front passenger's door lock knob switch A short to ground in the wire

- Front passenger's door lock knob switch

- A short to ground in the wire

15. If multiple failures are found on more than one control unit, replace the body control module . If input failures are related to a particular control unit, replace the control unit.
````

## Chunk 1609: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_dfb9f93e03fb`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

NOTE:

- If you are troubleshooting multiple DTCs, be sure to follow the instructions in B-CAN System Diagnosis Test Mode A .

- Before testing, make sure the No. A18 (10 A) and No. A24 (10 A) fuses in the under-hood fuse/relay box are OK.

- Before testing, make sure the No. B8 (15 A) *1/(20 A) *2, No. B9 (10 A), No. B12 (10 A), No. B13 (10 A), No. B15 (20 A), No. B16 (20 A), No. B25 (10 A), No. B26 (10 A), No. B28 (20 A), No. B38 (10 A), and No. B39 (10 A) fuses in the under-dash fuse/relay box are OK.

- Before testing, make sure the headlights, parking lights, side marker lights, taillights, and horns work properly.

- There are two pairs of fuses in the same circuit (No. B25 and No. B39 fuses, No. B12 and No. B26 fuses, No. B13 and No. B38 fuses, No. B38 and No. B39 fuses). If one fuse is blown, make sure to check the other fuse in the same circuit. If necessary, replace the blown fuse(s).

*1: Except K20C1 engine

*2: K20C1 engine

Body Control Module

1. Turn the vehicle to the OFF (LOCK) mode.

2. Disconnect body control module connectors A, B, C, D, and E.

NOTE: All connector views are shown from the wire side of the female terminals.

Courtesy of HONDA, U.S.A., INC.

Inspect the connectors and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 4.

With the connectors still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 5.

NOTE: These are door lock actuator operation tests for keyless entry.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B28 | GRY | Under all conditions | Connect to ground with a jumper wire: The horns should sound. | Blown No. A24 (10 A) fuse in the under-hood fuse/relay box Faulty horn relay Faulty horn An open or high resistance in the wire

- Blown No. A24 (10 A) fuse in the under-hood fuse/relay box

- Faulty horn relay

- Faulty horn

- An open or high resistance in the wire

D26 * | PNK | Ignition key inserted into the ignition key switch | Measure the voltage to ground: There should be less than 0.2 V. | Faulty ignition key switch An open or high resistance in the wire Poor ground (G505)

- Faulty ignition key switch

- An open or high resistance in the wire

- Poor ground (G505)

Ignition key removed from the ignition key switch | Measure the voltage to ground: There should be battery voltage. | Faulty ignition key switch A short to ground in the wire

- Faulty ignition key switch

- A short to ground in the wire

*: Without keyless access system

Reconnect the connectors to the body control module, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 6.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

C27 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

E1 | BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire
````

## Chunk 1610: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_f75eef9a2ba8`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
he wire

E1 | BLU | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B8 (15 A) *1/(20 A) *2 fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

A2 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

A8 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

B27 | BLU | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator, the front passenger's door lock actuator, the left rear door lock actuator, the right rear door lock actuator, and the fuel fill door lock actuator should LOCK. | Faulty power door lock relay circuit (LOCK) Faulty driver's door lock actuator Faulty front passenger's door lock actuator Faulty left rear door lock actuator Faulty right rear door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (LOCK)

- Faulty driver's door lock actuator

- Faulty front passenger's door lock actuator

- Faulty left rear door lock actuator

- Faulty right rear door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

*1: Except K20C1 engine

*2: K20C1 engine

*3: CVT

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

B31 | GRN | In all power modes | Connect to ground with a jumper wire: The driver's door lock actuator and the fuel fill door lock actuator should UNLOCK. | Faulty power door lock relay circuit (DR UNLOCK) Faulty driver's door lock actuator Faulty fuel fill door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (DR UNLOCK)

- Faulty driver's door lock actuator

- Faulty fuel fill door lock actuator

- An open or high resistance in the wire

B32 | PUR | In all power modes | Connect to ground with a jumper wire: The front passenger's door lock actuator, the left rear door lock actuator, and the right rear door lock actuator should UNLOCK. | Faulty power door lock relay circuit (UNLOCK) Faulty front passenger's door lock actuator Faulty left rear door lock actuator Faulty right rear door lock actuator An open or high resistance in the wire

- Faulty power door lock relay circuit (UNLOCK)

- Faulty front passenger's door lock actuator

- Faulty left rear door lock actuator

- Faulty right rear door lock actuator

- An open or high resistance in the wire

B29 | LT BLU | In all power modes | Connect to ground with a jumper wire: The tailgate release actuator should work. | Faulty tailgate release actuator relay circuit Faulty tailgate release actuator Poor ground (G603) or an open in the ground wire An open or high resistance in the wire

- Faulty tailgate release actuator relay circuit

- Faulty tailgate release actuator

- Poor ground (G603) or an open in the ground wire

- An open or high resistance in the wire

D22 | GRN | Driver's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door switch Faulty driver's door switch ground An open or high resistance in the wire

- Faulty driver's door switch

- Faulty driver's door switch ground

- An open or high resistance in the wire

Driver's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door switch A short to ground in the wire

- Faulty driver's door switch

- A short to ground in the wire

D23 | LT GRN | Front passenger's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door switch Faulty front passenger's door switch ground An open or high resistance in the wire

- Faulty front passenger's door switch

- Faulty front passenger's door switch ground

- An open or high resistance in the wire

Front passenger's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty front passenger's door switch A short to ground in the wire

- Faulty front passenger's door switch

- A short to ground in the wire
````

## Chunk 1611: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_e4a3cfca574b`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
or closed | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door switch A short to ground in the wire

- Faulty driver's door switch

- A short to ground in the wire

D23 | LT GRN | Front passenger's door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty front passenger's door switch Faulty front passenger's door switch ground An open or high resistance in the wire

- Faulty front passenger's door switch

- Faulty front passenger's door switch ground

- An open or high resistance in the wire

Front passenger's door closed | Measure the voltage to ground: There should be battery voltage. | Faulty front passenger's door switch A short to ground in the wire

- Faulty front passenger's door switch

- A short to ground in the wire

D24 | BRN | Left rear door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty left rear door switch Faulty left rear door switch ground An open or high resistance in the wire

- Faulty left rear door switch

- Faulty left rear door switch ground

- An open or high resistance in the wire

Left rear door closed | Measure the voltage to ground: There should be battery voltage. | Faulty left rear door switch A short to ground in the wire

- Faulty left rear door switch

- A short to ground in the wire

*1: Except K20C1 engine

*2: K20C1 engine

*3: CVT

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

D28 | GRY | Right rear door open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty right rear door switch Faulty right rear door switch ground An open or high resistance in the wire

- Faulty right rear door switch

- Faulty right rear door switch ground

- An open or high resistance in the wire

Right rear door closed | Measure the voltage to ground: There should be battery voltage. | Faulty right rear door switch A short to ground in the wire

- Faulty right rear door switch

- A short to ground in the wire

C15 | LT BLU | Left rear door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty left rear door lock knob switch Poor ground (G601) or an open in the ground wire An open or high resistance in the wire

- Faulty left rear door lock knob switch

- Poor ground (G601) or an open in the ground wire

- An open or high resistance in the wire

Left rear door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty left rear door lock knob switch A short to ground in the wire

- Faulty left rear door lock knob switch

- A short to ground in the wire

C16 | GRY | Right rear door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty right rear door lock knob switch Poor ground (G602) or an open in the ground wire An open or high resistance in the wire

- Faulty right rear door lock knob switch

- Poor ground (G602) or an open in the ground wire

- An open or high resistance in the wire

Right rear door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty right rear door lock knob switch A short to ground in the wire

- Faulty right rear door lock knob switch

- A short to ground in the wire

D27 | WHT | Tailgate open | Measure the voltage to ground: There should be less than 0.2 V. | Faulty tailgate latch switch Poor ground (G603) or an open in the ground wire An open or high resistance in the wire

- Faulty tailgate latch switch

- Poor ground (G603) or an open in the ground wire

- An open or high resistance in the wire

Tailgate closed | Measure the voltage to ground: There should be battery voltage. | Faulty tailgate latch switch A short to ground in the wire

- Faulty tailgate latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty hood latch switch Poor ground (G401) or an open in the ground wire An open or high resistance in the wire

- Faulty hood latch switch

- Poor ground (G401) or an open in the ground wire

- An open or high resistance in the wire

Hood open | Measure the voltage to ground: There should be battery voltage. | Faulty hood latch switch A short to ground in the wire

- Faulty hood latch switch

- A short to ground in the wire
````

## Chunk 1612: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_627d9805d2d5`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
n open in the ground wire

- An open or high resistance in the wire

Tailgate closed | Measure the voltage to ground: There should be battery voltage. | Faulty tailgate latch switch A short to ground in the wire

- Faulty tailgate latch switch

- A short to ground in the wire

C19 | BLU | Hood closed | Measure the voltage to ground: There should be less than 0.2 V. | Faulty hood latch switch Poor ground (G401) or an open in the ground wire An open or high resistance in the wire

- Faulty hood latch switch

- Poor ground (G401) or an open in the ground wire

- An open or high resistance in the wire

Hood open | Measure the voltage to ground: There should be battery voltage. | Faulty hood latch switch A short to ground in the wire

- Faulty hood latch switch

- A short to ground in the wire

C1 *3 | GRN | Shift lever in P position/mode | Measure the voltage to ground: There should be less than 0.2 V. | Faulty transmission range switch Poor ground (G201) or an open in the ground wire An open or high resistance in the wire

- Faulty transmission range switch

- Poor ground (G201) or an open in the ground wire

- An open or high resistance in the wire

Shift lever in any other position/mode than P | Measure the voltage to ground: There should be battery voltage. | Faulty transmission range switch A short to ground in the wire

- Faulty transmission range switch

- A short to ground in the wire

*1: Except K20C1 engine

*2: K20C1 engine

*3: CVT

Door Multiplex Control Unit

6. Turn the vehicle to the OFF (LOCK) mode.

7. Disconnect the power window master switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 9.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 10.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | WHT | Disconnect these connectors: Front passenger's power window switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 36 and front passenger's power window switch 37P connector terminal No. 34: There should be continuity. | An open in the LIN(P/W) wire

- Front passenger's power window switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 36 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 11.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

18 | BRN | Vehicle ON mode | Measure the voltage to ground: There should be battery voltage. | Blown No. B9 (10 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B9 (10 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

37 | RED | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. A18 (10 A) fuse in the under-hood fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B28 (20 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B28 (20 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G502) An open or high resistance in the ground wire

- Poor ground (G502)

- An open or high resistance in the ground wire
````

## Chunk 1613: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_cc2363ac7dc1`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
fuse/relay box An open or high resistance in the wire

- Blown No. A18 (10 A) fuse in the under-hood fuse/relay box

- An open or high resistance in the wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

4 | WHT | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B28 (20 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B28 (20 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G502) An open or high resistance in the ground wire

- Poor ground (G502)

- An open or high resistance in the ground wire

29 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G501) An open or high resistance in the ground wire

- Poor ground (G501)

- An open or high resistance in the ground wire

7 | PUR | Driver's door key cylinder switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch A short to ground in the wire

- Faulty driver's door key cylinder switch

- A short to ground in the wire

8 | RED | Driver's door key cylinder switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door key cylinder switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door key cylinder switch in neutral or LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door key cylinder switch An open or high resistance in the wire

- Faulty driver's door key cylinder switch

- An open or high resistance in the wire

21 | YEL | Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

20 | LT BLU | Driver's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Faulty driver's door lock knob switch Poor ground (G501) or an open in the ground wire An open or high resistance in the wire

- Faulty driver's door lock knob switch

- Poor ground (G501) or an open in the ground wire

- An open or high resistance in the wire

Driver's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Faulty driver's door lock knob switch A short to ground in the wire

- Faulty driver's door lock knob switch

- A short to ground in the wire

Front Passenger's Power Window Switch

11. Turn the vehicle to the OFF (LOCK) mode, open and close the driver's door.

12. Disconnect the front passenger's power window switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 14.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 15.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained
````

## Chunk 1614: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless/Power Door Locks/Security System (Body Control Module, Door Multiplex Control Unit, and Front Passenger's Power Window Switch) Input Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\748.html`
- Chunk ID: `chunk_ba63e21efcf1`
- Images: `images\GHH411532.jpeg`, `images\GHH411533.jpeg`, `images\GHH411534.jpeg`
- Duplicate sources: `pages\2790.html`, `pages\26245.html`, `pages\17188.html`

### Full Text

````text
ort to ground in the wire

Front Passenger's Power Window Switch

11. Turn the vehicle to the OFF (LOCK) mode, open and close the driver's door.

12. Disconnect the front passenger's power window switch 37P connector.

Courtesy of HONDA, U.S.A., INC.

Inspect the connector and socket terminals to be sure they are all making good contact:

- If the terminals are bent, loose, or corroded, repair them as necessary, and recheck the system.

- If the terminals look OK, go to step 14.

With the connector still disconnected, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 15.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

34 | WHT | Disconnect these connectors: Power window master switch 37P connector Moonroof motor-control unit 14P connector * | Check for continuity between terminal No. 34 and power window master switch 37P connector terminal No. 36: There should be continuity. | An open in the LIN(P/W) wire

- Power window master switch 37P connector

- Moonroof motor-control unit 14P connector *

Check for continuity between terminal No. 34 and moonroof motor-control unit 14P connector terminal No. 12: There should be continuity. | An open in the LIN(P/W) wire

Check for continuity to ground: There should be no continuity. | A short to ground in the LIN(P/W) wire

*: With moonroof

Reconnect the connector, do the following input tests:

- If any test indicates a problem, find and correct the cause, then recheck the system.

- If all the input tests prove OK, go to step 16.

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

1 | GRN | Under all conditions | Measure the voltage to ground: There should be battery voltage. | Blown No. B15 (20 A) fuse in the under-dash fuse/relay box An open or high resistance in the wire

- Blown No. B15 (20 A) fuse in the under-dash fuse/relay box

- An open or high resistance in the wire

3 | BLK | In all power modes | Measure the voltage to ground: There should be less than 0.2 V. | Poor ground (G505) An open or high resistance in the ground wire

- Poor ground (G505)

- An open or high resistance in the ground wire

Cavity | Wire | Test condition | Test: Desired result | Possible cause if desired result is not obtained

36 | TAN | Front passenger's door lock knob switch in UNLOCK | Measure the voltage to ground: There should be less than 0.2 V. | Front passenger's door lock knob switch Poor ground (G505) or an open in the ground wire An open or high resistance in the wire

- Front passenger's door lock knob switch

- Poor ground (G505) or an open in the ground wire

- An open or high resistance in the wire

Front passenger's door lock knob switch in LOCK | Measure the voltage to ground: There should be battery voltage. | Front passenger's door lock knob switch A short to ground in the wire

- Front passenger's door lock knob switch

- A short to ground in the wire

16. If multiple failures are found on more than one control unit, replace the body control module . If input failures are related to a particular control unit, replace the control unit.
````

## Chunk 1615: Immobilizer System Check

- Title: Immobilizer System Check
- Source path: `pages\749.html`
- Chunk ID: `chunk_7625d95eea10`
- Images: none
- Duplicate sources: `pages\2791.html`, `pages\26246.html`, `pages\12909.html`

### Full Text

````text
# Immobilizer System Check

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. Monitor the SYSTEM CHECK in IMMOBILIZER INFO with the HDS.

NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K LINE connections. If the HDS displays NORMAL N-1, the immobilizer system is OK at this time. If the HDS displays any messages, check as follows:

System Check No. | System Check | Possible Cause

A-1 | The key is not registered(Incorrect key code) | This key is not registered in the immobilizer-keyless control unit. Try to register keys using the HDS. No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys. Low 12 volt battery voltage.

- This key is not registered in the immobilizer-keyless control unit. Try to register keys using the HDS.

- No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys.

- Low 12 volt battery voltage.

A-2 | Communication error between the key and immobilizer-keyless control unit(Incorrect key code format) | Intermittent interruption between transponder and immobilizer-keyless control unit. The immobilizer key type is different. It is not for this vehicle but for another vehicle or for another company's vehicle. Key failure (transponder failure) No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys. Low 12 volt battery voltage.

- Intermittent interruption between transponder and immobilizer-keyless control unit.

- The immobilizer key type is different. It is not for this vehicle but for another vehicle or for another company's vehicle.

- Key failure (transponder failure)

- No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys.

- Low 12 volt battery voltage.

A-3 | No communication between the key and immobilizer-keyless control unit(No transponder detected) | The vehicle was turned to the ON mode with a non-immobilizer key. The immobilizer key type is different. It is not for this vehicle but for another vehicle or for another company's vehicle. Key failure (transponder failure) No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys. Low 12 volt battery voltage. Immobilizer-keyless control unit failure

- The vehicle was turned to the ON mode with a non-immobilizer key.

- The immobilizer key type is different. It is not for this vehicle but for another vehicle or for another company's vehicle.

- Key failure (transponder failure)

- No communication between the antenna and the immobilizer key because of interference from metal such as key chains/key rings/other keys.

- Low 12 volt battery voltage.

- Immobilizer-keyless control unit failure

B-1 | The PCM is not registered | The PCM was not registered. Try to register the PCM using the HDS. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference. Open in the IG1 line

- The PCM was not registered. Try to register the PCM using the HDS.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

- Open in the IG1 line

B-2 | Error of communication format in PCM(Incorrect registration format) | The PCM was not registered. Try to register the PCM using the HDS. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

- The PCM was not registered. Try to register the PCM using the HDS.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

System Check No. | System Check | Possible Cause

C-1 | Imoes unit is not registered | Imoes unit was not registered.
````

## Chunk 1616: Immobilizer System Check

- Title: Immobilizer System Check
- Source path: `pages\749.html`
- Chunk ID: `chunk_3626cf03f953`
- Images: none
- Duplicate sources: `pages\2791.html`, `pages\26246.html`, `pages\12909.html`

### Full Text

````text
the IG1 line

B-2 | Error of communication format in PCM(Incorrect registration format) | The PCM was not registered. Try to register the PCM using the HDS. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

- The PCM was not registered. Try to register the PCM using the HDS.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

System Check No. | System Check | Possible Cause

C-1 | Imoes unit is not registered | Imoes unit was not registered. No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the imoes unit and the immobilizer-keyless control unit because of interference. Try to register the imoes unit with the HDS.

- Imoes unit was not registered.

- No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the imoes unit and the immobilizer-keyless control unit because of interference.

- Try to register the imoes unit with the HDS.

C-2 | Error of communication format in imoes unit | Imoes unit was not registered. No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the imoes unit and the immobilizer-keyless control unit because of electrical interference. Try to register the imoes unit with the HDS.

- Imoes unit was not registered.

- No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the imoes unit and the immobilizer-keyless control unit because of electrical interference.

- Try to register the imoes unit with the HDS.

D-1 | S-NET line short | S-NET line short from the PCM to the imoes unit or the immobilizer-keyless control unit. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference. Immobilizer-keyless control unit failure PCM failure

- S-NET line short from the PCM to the imoes unit or the immobilizer-keyless control unit.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

- Immobilizer-keyless control unit failure

- PCM failure

D-2 | No communication between imoes unit and immobilizer-keyless control unit(S-NET line) | Blown fuse S-NET line open from the imoes unit to the immobilizer-keyless control unit. No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the imoes unit and the immobilizer-keyless control unit because of electrical interference. Immobilizer-keyless control unit failure Imoes unit failure

- Blown fuse

- S-NET line open from the imoes unit to the immobilizer-keyless control unit.

- No communication between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the imoes unit and the immobilizer-keyless control unit because of electrical interference.

- Immobilizer-keyless control unit failure

- Imoes unit failure

D-3 | No communication between PCM and immobilizer-keyless control unit(S-NET line) | Blown fuse S-NET line open from the PCM to the immobilizer-keyless control unit. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference. Immobilizer-keyless control unit failure PCM failure

- Blown fuse

- S-NET line open from the PCM to the immobilizer-keyless control unit.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.
````

## Chunk 1617: Immobilizer System Check

- Title: Immobilizer System Check
- Source path: `pages\749.html`
- Chunk ID: `chunk_4d48d9377456`
- Images: none
- Duplicate sources: `pages\2791.html`, `pages\26246.html`, `pages\12909.html`

### Full Text

````text
es unit and the immobilizer-keyless control unit because of electrical interference.

- Immobilizer-keyless control unit failure

- Imoes unit failure

D-3 | No communication between PCM and immobilizer-keyless control unit(S-NET line) | Blown fuse S-NET line open from the PCM to the immobilizer-keyless control unit. No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage. No communication between the immobilizer-keyless control unit and the PCM because of electrical interference. Immobilizer-keyless control unit failure PCM failure

- Blown fuse

- S-NET line open from the PCM to the immobilizer-keyless control unit.

- No communication between the PCM and the immobilizer-keyless control unit because of low 12 volt battery voltage.

- No communication between the immobilizer-keyless control unit and the PCM because of electrical interference.

- Immobilizer-keyless control unit failure

- PCM failure

E-1 | Initial registration of immobilizer-keyless control unit is not completed | The immobilizer-keyless control unit is not registered. Try to register the immobilizer-keyless control unit using the HDS.

E-2

E-3

E-4

E-5

F-1 | Special Mode | The vehicle is turned to the ON mode and to the OFF (LOCK) mode with the registered key.

F-2

F-3

F-4

F-5
````

## Chunk 1618: Keyless Access System Check

- Title: Keyless Access System Check
- Source path: `pages\750.html`
- Chunk ID: `chunk_79b875e747e7`
- Images: none
- Duplicate sources: `pages\2792.html`, `pages\26247.html`, `pages\12912.html`

### Full Text

````text
# Keyless Access System Check

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. On the HDS screen, at SYSTEM SELECTION MENU, enter ONE-PUSH START, then select KEYLESS ACCESS CONTROL UNIT or BACKUP CONTROL UNIT.

NOTE: If the HDS does not communicate, check the body control module power, ground, K line, and L-line connectors.

4. At KEYLESS ACCESS CONTROL UNIT, enter KEYLESS ACCESS SYSTEM INFORMATION, then select SYSTEM CHECK 1 or SYSTEM CHECK 2.

5. At BACKUP CONTROL UNIT, enter SYSTEM INFORMATION, then select SYSTEM CHECK.If the HDS displays NORMAL N-1, the immobilizer system is OK at this time, refer to the STATUS LOG. If the HDS displays any other messages, check as follows:

System Check 1 (Keyless Access Control Unit)

System Check No. | Possible cause | Check items

A-1A-2A-3G-4 | Keyless remote is mismatched No communication between body control module and keyless remote Keyless remote is not registered | Register the keyless remote LF antenna test Check antenna level with the HDS

- Keyless remote is mismatched

- No communication between body control module and keyless remote

- Keyless remote is not registered

- Register the keyless remote

- LF antenna test

- Check antenna level with the HDS

B-1B-2G-1 | PCM is not registered No communication between body control module and PCM Body control module is replaced | Register the PCM Check PCM Check for an open in the S-NET lines Register the body control module

- PCM is not registered

- No communication between body control module and PCM

- Body control module is replaced

- Register the PCM

- Check PCM

- Check for an open in the S-NET lines

- Register the body control module

C-1C-2G-2G-3 | Body control module is not registered Body control module is replaced | Register the body control module Check body control module Check for an open in the S-NET lines

- Body control module is not registered

- Body control module is replaced

- Register the body control module

- Check body control module

- Check for an open in the S-NET lines

C-3C-4G-5 | Body control module is replaced Communication error between body control module and electric steering lock * Electric steering lock is not registered * | Register the body control module Check for an open or short in the IGN TRX line * Check electric steering lock * Register the electric steering lock *

- Body control module is replaced

- Communication error between body control module and electric steering lock *

- Electric steering lock is not registered *

- Register the body control module

- Check for an open or short in the IGN TRX line *

- Check electric steering lock *

- Register the electric steering lock *

*: With electric steering lock

System Check 2 (Keyless Access Control Unit)

System Check No. | Possible cause | Check items

D-1D-2D-3 | S-NET line is open or short No communication between body control module and PCM | Check for an open or short in the S-NET lines Check body control module Check PCM

- S-NET line is open or short

- No communication between body control module and PCM

- Check for an open or short in the S-NET lines

- Check body control module

- Check PCM

D-4D-5 | IGN TRX line is open or short * | Check for an open or short in the IGN TRX line *

*: With electric steering lock

System Check (Backup Control Unit)

System Check No. | Possible cause | Check items

A-1A-2A-3 | Keyless remote is mismatched Keyless remote is not registered Engine start/stop switch failure | Register the keyless remote Check engine start/stop switch

- Keyless remote is mismatched

- Keyless remote is not registered

- Engine start/stop switch failure

- Register the keyless remote

- Check engine start/stop switch

B-1B-2 | PCM is replaced Communication error between body control module and PCM | Register the PCM Check PCM

- PCM is replaced

- Communication error between body control module and PCM

- Register the PCM

- Check PCM

C-1C-2 | Body control module is replaced | Register the body control module Check body control module Check for an open in the S-NET lines

- Register the body control module

- Check body control module

- Check for an open in the S-NET lines

D-1D-2D-3 | S-NET line is open or short No communication between body control module and PCM | Check for an open or short in the S-NET lines Check body control module Check PCM

- S-NET line is open or short

- No communication between body control module and PCM
````

## Chunk 1619: Keyless Access System Check

- Title: Keyless Access System Check
- Source path: `pages\750.html`
- Chunk ID: `chunk_b82e5b5c90aa`
- Images: none
- Duplicate sources: `pages\2792.html`, `pages\26247.html`, `pages\12912.html`

### Full Text

````text
re

- Register the keyless remote

- Check engine start/stop switch

B-1B-2 | PCM is replaced Communication error between body control module and PCM | Register the PCM Check PCM

- PCM is replaced

- Communication error between body control module and PCM

- Register the PCM

- Check PCM

C-1C-2 | Body control module is replaced | Register the body control module Check body control module Check for an open in the S-NET lines

- Register the body control module

- Check body control module

- Check for an open in the S-NET lines

D-1D-2D-3 | S-NET line is open or short No communication between body control module and PCM | Check for an open or short in the S-NET lines Check body control module Check PCM

- S-NET line is open or short

- No communication between body control module and PCM

- Check for an open or short in the S-NET lines

- Check body control module

- Check PCM

E-1E-2E-3E-4E-5 | Body control module is not registered PCM is not registered Keyless remote is not registered | Register the body control module Register the PCM Register the keyless remote

- Body control module is not registered

- PCM is not registered

- Keyless remote is not registered

- Register the body control module

- Register the PCM

- Register the keyless remote

F-1F-2F-3F-4F-5 | Special mode | Turn the vehicle to the ON mode and then select the OFF (LOCK) mode with a registered keyless remote
````

## Chunk 1620: General Check Before Troubleshooting

- Title: General Check Before Troubleshooting
- Source path: `pages\751.html`
- Chunk ID: `chunk_315e3c12eb9b`
- Images: none
- Duplicate sources: `pages\755.html`, `pages\2793.html`, `pages\2797.html`, `pages\26248.html`, `pages\26252.html`, `pages\17189.html`, `pages\17193.html`

### Full Text

````text
# General Check Before Troubleshooting

Before troubleshooting the immobilizer system, check the following general items and resolve any issues, if applicable:

- The 12 volt battery is low; charge the 12 volt battery fully, then troubleshoot the immobilizer system.

- The ignition key is not a genuine Honda part; use a Honda-approved key blank, register the key, then troubleshoot the immobilizer system.

- If a key ring or a key case is used; remove the key from it, and troubleshoot the immobilizer system with the key only.

- An aftermarket electrical part is installed; remove it, then troubleshoot the immobilizer system.
````

## Chunk 1621: Symptom Troubleshooting Using the Security Indicator Lighting Pattern

- Title: Symptom Troubleshooting Using the Security Indicator Lighting Pattern
- Source path: `pages\752.html`
- Chunk ID: `chunk_9b30913a1f6f`
- Images: none
- Duplicate sources: `pages\756.html`, `pages\2794.html`, `pages\2798.html`, `pages\26249.html`, `pages\26253.html`, `pages\17190.html`, `pages\17194.html`

### Full Text

````text
# Symptom Troubleshooting Using the Security Indicator Lighting Pattern

The pattern of the security indicator can help troubleshoot the condition of the immobilizer system. Here are descriptions of the four possible patterns:

Normal operation:

When turning the vehicle to the ON mode and the immobilizer code is identified, the security indicator is OFF.

Immobilizer code is not identified:

When turning the vehicle to the ON mode when the immobilizer code has not been identified, the security indicator blink until the OFF (LOCK) mode is selected. Then security indicator will come on for 1 second. The state of the keyless registration and the S-NET line can be checked by doing a SYSTEM CHECK and STATUS LOG with the HDS.

Security indicator turns on:

If the security indicator turns on, do the gauge control module self-diagnostic function . If the indicator drive circuit is OK, do the SYSTEM CHECK and STATUS LOG with the HDS.
````

## Chunk 1622: Symptom Troubleshooting Using Malfunctioning Circuit Functions

- Title: Symptom Troubleshooting Using Malfunctioning Circuit Functions
- Source path: `pages\753.html`
- Chunk ID: `chunk_e42dca428c9e`
- Images: `images\GHH411535.jpeg`
- Duplicate sources: `pages\757.html`, `pages\2795.html`, `pages\2799.html`, `pages\26250.html`, `pages\26254.html`, `pages\17191.html`, `pages\17195.html`

### Full Text

````text
# Symptom Troubleshooting Using Malfunctioning Circuit Functions

If a malfunction occurs in the immobilizer circuit, use the table to cross-reference the malfunction criteria to the line(s) that should be checked in the table:

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1623: System Check

- Title: System Check
- Source path: `pages\754.html`
- Chunk ID: `chunk_ee6e47f156c3`
- Images: none
- Duplicate sources: `pages\758.html`, `pages\2796.html`, `pages\2800.html`, `pages\26251.html`, `pages\26255.html`, `pages\17192.html`, `pages\17196.html`

### Full Text

````text
# System Check

NOTE: The HDS can be used to check the state of the immobilizer key registration and the S-NET line by doing a SYSTEM CHECK.

1. Connect the HDS to the data link connector (DLC) .

NOTE: If the HDS does not communicate with the vehicle, go to the DLC Circuit Troubleshooting

2. The vehicle is turned to the ON mode and follow the prompts to the SYSTEM SELECTION MENU.

3. At SYSTEM SELECTION MENU, enter IMMOBI, then select the IMMOBILIZER SETUP.

4. Do the SYSTEM CHECK

If there is a system check number, do the troubleshooting for the item indicated.
````

## Chunk 1624: General Check Before Troubleshooting

- Title: General Check Before Troubleshooting
- Source path: `pages\759.html`
- Chunk ID: `chunk_b4223de4a5f4`
- Images: none
- Duplicate sources: `pages\2801.html`, `pages\26256.html`, `pages\17197.html`

### Full Text

````text
# General Check Before Troubleshooting

Before troubleshooting the keyless access system, check the following items and solve any applicable issues.

- Before starting the troubleshooting procedure, make sure that keyless access system is not disabled by the customization.

- Check the No. A1-5, No. A1-7, No. A2-2, No. A2-4, and No. A18 fuses .

- Check the No. B8, No. B11*, and No. B30 fuses .

- Check for poor connection at the body control module.

- Check for DTCs with the HDS; if a DTC is indicated, troubleshoot the DTC first.

- Before testing, troubleshoot the keyless access system first using SELF CHECK, and if any malfunction is found, troubleshoot it first.

- Make sure the keyless remote is not in a purse with coins, wrapped with any metallic material, placed near a mobile phone or computer.

- Make sure the vehicle 12 volt battery is fully charged.

- Make sure the keyless remote batteries are not low; if they are, replace keyless remote battery.

- Make sure a different keyless remote is not being used; only use a Honda-approved keyless remote.

- Make sure the keyless remote is not attached to a key ring or key case; if it is, remove the key from it.

- Make sure aftermarket accessories are not installed; remove any aftermarket accessories.

- Make sure aftermarket accessories are not connected to the S-NET or IGN TRX line; disconnect any aftermarket accessories from the S-NET or IGN TRX line.

- Make sure there is no electrical interference nearby; avoid areas with electrical or radio interference. *: Except L15BY engine

*: Except L15BY engine
````

## Chunk 1625: Symptom Troubleshooting Using the Security Indicator Lighting Pattern: Notes

- Title: Symptom Troubleshooting Using the Security Indicator Lighting Pattern: Notes
- Source path: `pages\760.html`
- Chunk ID: `chunk_d02d7dd26951`
- Images: none
- Duplicate sources: `pages\766.html`, `pages\2802.html`, `pages\2808.html`, `pages\26257.html`, `pages\26263.html`, `pages\17198.html`, `pages\17204.html`

### Full Text

````text
# Symptom Troubleshooting Using the Security Indicator Lighting Pattern: Notes

The immobilizer and keyless access system condition can be checked by the security indicator lighting pattern.
````

## Chunk 1626: Normal operation:

- Title: Normal operation:
- Source path: `pages\761.html`
- Chunk ID: `chunk_61565e39cdd5`
- Images: none
- Duplicate sources: `pages\767.html`, `pages\2803.html`, `pages\2809.html`, `pages\26258.html`, `pages\26264.html`, `pages\17199.html`, `pages\17205.html`

### Full Text

````text
# Normal operation:

When turning the vehicle to the ON mode and the immobilizer code is identified, the security indicator is OFF.
````

## Chunk 1627: Immobilizer code is not identified:

- Title: Immobilizer code is not identified:
- Source path: `pages\762.html`
- Chunk ID: `chunk_e00a2499ac17`
- Images: none
- Duplicate sources: `pages\768.html`, `pages\2804.html`, `pages\2810.html`, `pages\26259.html`, `pages\26265.html`, `pages\17200.html`, `pages\17206.html`

### Full Text

````text
# Immobilizer code is not identified:

When turning the vehicle to the ON mode when the immobilizer code has not been identified, the security indicator blink until the OFF (LOCK) mode is selected. Then security indicator will come on for 1 second. The state of the keyless registration and the S-NET line can be checked by doing a SYSTEM CHECK and STATUS LOG with the HDS.
````

## Chunk 1628: Security indicator turns on:

- Title: Security indicator turns on:
- Source path: `pages\763.html`
- Chunk ID: `chunk_96876a915b95`
- Images: none
- Duplicate sources: `pages\769.html`, `pages\2805.html`, `pages\2811.html`, `pages\26260.html`, `pages\26266.html`, `pages\17201.html`, `pages\17207.html`

### Full Text

````text
# Security indicator turns on:

If the security indicator turns on, do the gauge control module self-diagnostic function procedures . If the indicator drive circuit is OK, do the SYSTEM CHECK and STATUS LOG procedures with the HDS.
````

## Chunk 1629: System Check and Status Log

- Title: System Check and Status Log
- Source path: `pages\764.html`
- Chunk ID: `chunk_4cbd49da1057`
- Images: none
- Duplicate sources: `pages\2806.html`, `pages\26261.html`, `pages\17202.html`

### Full Text

````text
# System Check and Status Log

NOTE: The HDS can be used to:

- Check the state of the keyless remote registration and the S-NET line by doing a SYSTEM CHECK .

- Check the number of times the keyless access control unit or the backup control unit did not permit the engine to start by checking the STATUS LOG .

1. Connect the HDS to the data link connector (DLC), then turn the vehicle to the ON mode and follow the prompts to the SYSTEM SELECTION MENU.

NOTE: If the HDS does not communicate with the vehicle, go to the DLC circuit troubleshooting

2. At SYSTEM SELECTION MENU, enter ONE-PUSH START, then select KEYLESS ACCESS CONTROL UNIT or BACKUP CONTROL UNIT.

3. At KEYLESS ACCESS CONTROL UNIT, enter KEYLESS ACCESS SYSTEM INFORMATION, then select SYSTEM CHECK 1 or SYSTEM CHECK 2.

4. At BACKUP CONTROL UNIT, enter SYSTEM INFORMATION, then select SYSTEM CHECK.

5. Do the SYSTEM CHECK. If there is a system check number, do the troubleshooting for the item indicated.

6. Check the STATUS LOG using the HDS

Troubleshoot the line with the highest counts first. If all the lines are 0 (zero), the problem may not be caused by the immobilizer system or keyless access system, check for ignition or fuel problems.

NOTE: Once repaired, clear the status log by removing the No. A18 fuse or disconnecting the 12 volt battery.
````

## Chunk 1630: General Check Before Troubleshooting

- Title: General Check Before Troubleshooting
- Source path: `pages\765.html`
- Chunk ID: `chunk_5af780292824`
- Images: none
- Duplicate sources: `pages\2807.html`, `pages\26262.html`, `pages\17203.html`

### Full Text

````text
# General Check Before Troubleshooting

Before troubleshooting the keyless access system, check the following items and solve any applicable issues.

- Before starting the troubleshooting procedure, make sure that keyless access system is not disabled by the customization.

- Check the No. A1-7 (125 A), No. A1-5 (30 A), No. A2-2 (30 A), No. A2-4 (60 A), and No. A18 (10 A) fuses in the under-hood fuse/relay box.

- Check the No. B8 (15 A) *1/(20 A) *2 and No. B30 (10 A) fuses in the under-dash fuse/relay box.

- Check for poor connection at the body control module.

- Check for DTCs with the HDS; if a DTC is indicated, troubleshoot the DTC first.

- Before testing, troubleshoot the keyless access system first using SELF CHECK, and if any malfunction is found, troubleshoot it first.

- Make sure the keyless remote is not in a purse with coins, wrapped with any metallic material, placed near a mobile phone or computer.

- Make sure the vehicle 12 volt battery is fully charged.

- Make sure the keyless remote batteries are not low; if they are, replace keyless remote battery.

- Make sure a different keyless remote is not being used; only use a Honda-approved keyless remote.

- Make sure the keyless remote is not attached to a key ring or key case; if it is, remove the key from it.

- Make sure aftermarket accessories are not installed; remove any aftermarket accessories.

- Make sure aftermarket accessories are not connected to the S-NET or IGN TRX line; disconnect any aftermarket accessories from the S-NET or IGN TRX line.

- Make sure there is no electrical interference nearby; avoid areas with electrical or radio interference. *1: Except K20C1 engine *2: K20C1 engine

*1: Except K20C1 engine

*2: K20C1 engine
````

## Chunk 1631: System Check and Status Log

- Title: System Check and Status Log
- Source path: `pages\770.html`
- Chunk ID: `chunk_a50e5ddf25b0`
- Images: none
- Duplicate sources: `pages\2812.html`, `pages\26267.html`, `pages\17208.html`

### Full Text

````text
# System Check and Status Log

NOTE: The HDS can be used to:

- Check the state of the keyless remote registration and the S-NET line by doing a SYSTEM CHECK .

- Check the number of times the keyless access control unit or the backup control unit did not permit the engine to start by checking the STATUS LOG .

1. Connect the HDS to the data link connector (DLC), then turn the vehicle to the ON mode and follow the prompts to the SYSTEM SELECTION MENU.

NOTE: If the HDS does not communicate with the vehicle, go to the DLC circuit troubleshooting

2. At SYSTEM SELECTION MENU, enter ONE-PUSH START, then select KEYLESS ACCESS CONTROL UNIT or BACKUP CONTROL UNIT.

3. At KEYLESS ACCESS CONTROL UNIT, enter KEYLESS ACCESS SYSTEM INFORMATION, then select SYSTEM CHECK 1 or SYSTEM CHECK 2.

4. At BACKUP CONTROL UNIT, enter SYSTEM INFORMATION, then select SYSTEM CHECK.

5. Do the SYSTEM CHECK. If there is a system check number, do the troubleshooting for the item indicated.

6. Check the STATUS LOG using the HDS .

Troubleshoot the line with the highest counts first. If all the lines are 0 (zero), the problem may not be caused by the immobilizer system or keyless access system, check for ignition or fuel problems.

NOTE: Once repaired, clear the status log by removing the No. A18 (10 A) fuse in the under-hood fuse/relay box or disconnecting the 12 volt battery.
````

## Chunk 1632: Keyless/Power Door Locks/Security System Tripped Sensor Recall

- Title: Keyless/Power Door Locks/Security System Tripped Sensor Recall
- Source path: `pages\771.html`
- Chunk ID: `chunk_de4e6166aabf`
- Images: none
- Duplicate sources: `pages\2813.html`, `pages\26268.html`, `pages\14401.html`

### Full Text

````text
# Keyless/Power Door Locks/Security System Tripped Sensor Recall

The security system stores information on the last tripped sensor if the security system has been actuated. The information can be retrieved using the HDS.

To retrieve the last tripped sensor data, do this:

1. Select HISTORY DATA from the SECURITY MODE MENU.Scroll through the data list.

- Sensors that were actuated will indicate DETECT.

- Sensors that were not actuated will indicate NONE.

Inspect the DETECT circuit for:

- Misadjusted or damaged switch.

- Loose or corroded connections.

- Intermittent short to ground.

NOTE: If PANIC FRAME RECEPTION is indicated ON, inform the customer that it could have been set by something pressing the panic button of one of the registered remotes (in a pocket or purse, under a stack of papers, etc.).
````

## Chunk 1633: Door Key Cylinder Switch Test (2-door) (2016 2017 2018 2019 2020): Test

- Title: Door Key Cylinder Switch Test (2-door) (2016 2017 2018 2019 2020): Test
- Source path: `pages\772.html`
- Chunk ID: `chunk_adea5eb49e5d`
- Images: `images\GHH411537.jpeg`, `images\GHH411538.jpeg`
- Duplicate sources: `pages\2814.html`, `pages\26269.html`, `pages\17209.html`

### Full Text

````text
# Door Key Cylinder Switch Test (2-door) (2016 2017 2018 2019 2020): Test

- Driver's Door Panel - Remove

- Driver's Door Key Cylinder Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1634: Door Key Cylinder Switch Test (4/5-door): Test

- Title: Door Key Cylinder Switch Test (4/5-door): Test
- Source path: `pages\773.html`
- Chunk ID: `chunk_229093bbdd6f`
- Images: `images\GHH411539.jpeg`, `images\GHH411540.jpeg`
- Duplicate sources: `pages\2815.html`, `pages\26270.html`, `pages\17210.html`

### Full Text

````text
# Door Key Cylinder Switch Test (4/5-door): Test

- Driver's Door Panel - Remove

- Driver's Door Key Cylinder Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the driver's door key cylinder switch is faulty; replace the driver's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1635: Door Lock Actuator Test (2-door) (2016 2017 2018 2019 2020): Test

- Title: Door Lock Actuator Test (2-door) (2016 2017 2018 2019 2020): Test
- Source path: `pages\774.html`
- Chunk ID: `chunk_b48abcbb9465`
- Images: `images\GHH411541.jpeg`, `images\GHH411542.jpeg`, `images\GHH411543.jpeg`
- Duplicate sources: `pages\2816.html`, `pages\26271.html`, `pages\17211.html`

### Full Text

````text
# Door Lock Actuator Test (2-door) (2016 2017 2018 2019 2020): Test

- Front Door Panel - Remove

- Front Door Lock Actuator - Test Driver's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Passenger's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch (B).

Driver's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Passenger's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch (B).

Passenger's door

2. Check the actuator operation by connecting power and ground according to the table.

NOTE: To prevent damage to the actuator, apply battery voltage only momentarily.

3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1636: Door Lock Actuator Test (4/5-door): Test

- Title: Door Lock Actuator Test (4/5-door): Test
- Source path: `pages\775.html`
- Chunk ID: `chunk_be941ce3e992`
- Images: `images\GHH411544.jpeg`, `images\GHH411545.jpeg`, `images\GHH411546.jpeg`, `images\GHH411547.jpeg`, `images\GHH411548.jpeg`
- Duplicate sources: `pages\2817.html`, `pages\26272.html`, `pages\17212.html`

### Full Text

````text
# Door Lock Actuator Test (4/5-door): Test

Front Door

- Front Door Panel - Remove

- Front Door Lock Actuator - Test Driver's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Front passenger's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch (B).

Driver's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Front passenger's door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch (B).

Front passenger's door

2. Check the actuator operation by connecting power and ground according to the table.

NOTE: To prevent damage to the actuator, apply battery voltage only momentarily.

3. If the actuator does not operate as specified, the front door lock actuator is faulty; replace the front door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. Rear Door

1. Install the parts in the reverse order of removal.

Rear Door

- Rear Door Panel - Remove

- Rear Door Lock Actuator - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Left and Right Rear Door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the rear door lock actuator is faulty; replace the rear door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Left and Right Rear Door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check the actuator operation by connecting power and ground according to the table. NOTE: To prevent damage to the actuator, apply battery voltage only momentarily. 3. If the actuator does not operate as specified, the rear door lock actuator is faulty; replace the rear door latch (B).

2. Check the actuator operation by connecting power and ground according to the table.

NOTE: To prevent damage to the actuator, apply battery voltage only momentarily.

3. If the actuator does not operate as specified, the rear door lock actuator is faulty; replace the rear door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1637: Door Lock Knob Switch Test (2-door) (2016 2017 2018 2019 2020): Test

- Title: Door Lock Knob Switch Test (2-door) (2016 2017 2018 2019 2020): Test
- Source path: `pages\776.html`
- Chunk ID: `chunk_0a3248773baf`
- Images: `images\GHH411549.jpeg`, `images\GHH411550.jpeg`, `images\GHH411551.jpeg`, `images\GHH411552.jpeg`
- Duplicate sources: `pages\2818.html`, `pages\26273.html`, `pages\17213.html`

### Full Text

````text
# Door Lock Knob Switch Test (2-door) (2016 2017 2018 2019 2020): Test

Driver's Door

- Driver's Door Panel - Remove

- Driver's Door Lock Knob Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. Passenger's Door

1. Install the parts in the reverse order of removal.

Passenger's Door

- Passenger's Door Panel - Remove

- Passenger's Door Lock Knob Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the passenger's door lock knob switch is faulty; replace the passenger's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the passenger's door lock knob switch is faulty; replace the passenger's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the passenger's door lock knob switch is faulty; replace the passenger's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1638: Door Lock Knob Switch Test (4/5-door): Test

- Title: Door Lock Knob Switch Test (4/5-door): Test
- Source path: `pages\777.html`
- Chunk ID: `chunk_b1d7a3b49e1e`
- Images: `images\GHH411553.jpeg`, `images\GHH411554.jpeg`, `images\GHH411555.jpeg`, `images\GHH411556.jpeg`, `images\GHH411557.jpeg`, `images\GHH411558.jpeg`
- Duplicate sources: `pages\2819.html`, `pages\26274.html`, `pages\17214.html`

### Full Text

````text
# Door Lock Knob Switch Test (4/5-door): Test

Driver's Door

- Driver's Door Panel - Remove

- Driver's Door Lock Knob Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the driver's door lock knob switch is faulty; replace the driver's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. Front Passenger's Door

1. Install the parts in the reverse order of removal.

Front Passenger's Door

- Front Passenger's Door Panel - Remove

- Front Passenger's Door Lock Knob Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the front passenger's door lock knob switch is faulty; replace the front passenger's door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the front passenger's door lock knob switch is faulty; replace the front passenger's door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the front passenger's door lock knob switch is faulty; replace the front passenger's door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. Rear Door

1. Install the parts in the reverse order of removal.

Rear Door

- Rear Door Panel - Remove

- Rear Door Lock Knob Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Left and Right Rear Door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the rear door lock knob switch is faulty; replace the rear door latch (B).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Left and Right Rear Door Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each switch position according to the table. 3. If the continuity is not as specified, the rear door lock knob switch is faulty; replace the rear door latch (B).

2. Check for continuity between the terminals in each switch position according to the table.

3. If the continuity is not as specified, the rear door lock knob switch is faulty; replace the rear door latch

(B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1639: Engine Start/Stop Switch Test: Test

- Title: Engine Start/Stop Switch Test: Test
- Source path: `pages\778.html`
- Chunk ID: `chunk_e33ae0ea3c81`
- Images: `images\GHH411559.jpeg`, `images\GHH411560.jpeg`, `images\GHH411561.jpeg`
- Duplicate sources: `pages\2820.html`, `pages\26275.html`, `pages\17215.html`

### Full Text

````text
# Engine Start/Stop Switch Test: Test

- Driver's Dashboard Switch Panel - Remove

- Engine Start/Stop Switch - Test Switch Test 1. Check the engine start/stop switch (A) according to the table. NOTE: When an LED is located between terminals, check if the LED illuminates by connecting power and ground to the LED. Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse). Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. 2. If the result is not as specified, replace the engine start/stop switch . LF Antenna Test 3. Check for continuity between the terminals according to the table. There should be continuity. Courtesy of HONDA, U.S.A., INC. 4. If the continuity is not as specified, replace the engine start/stop switch .

Switch Test

1. Check the engine start/stop switch (A) according to the table.

- When an LED is located between terminals, check if the LED illuminates by connecting power and ground to the LED.

- Note this important operating characteristic; diode bias causes a diode to fully conduct electricity in one direction (forward), while not at all in the opposite direction (reverse).

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

2. If the result is not as specified, replace the engine start/stop switch .

LF Antenna Test

3. Check for continuity between the terminals according to the table. There should be continuity.

Courtesy of HONDA, U.S.A., INC.

4. If the continuity is not as specified, replace the engine start/stop switch .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1640: Hood Latch Switch Test: Test

- Title: Hood Latch Switch Test: Test
- Source path: `pages\779.html`
- Chunk ID: `chunk_bf336db4882d`
- Images: `images\GHH411562.jpeg`, `images\GHH411563.jpeg`
- Duplicate sources: `pages\2821.html`, `pages\26276.html`, `pages\17216.html`

### Full Text

````text
# Hood Latch Switch Test: Test

- Hood Latch - Remove

- Hood Latch Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, the hood latch switch is faulty; replace the hood latch (A).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, the hood latch switch is faulty; replace the hood latch (A).

2. If the continuity is not as specified, the hood latch switch is faulty; replace the hood latch

(A).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1641: Immobilizer System Status Log

- Title: Immobilizer System Status Log
- Source path: `pages\780.html`
- Chunk ID: `chunk_35261f80ccca`
- Images: none
- Duplicate sources: `pages\2822.html`, `pages\26277.html`, `pages\15587.html`

### Full Text

````text
# Immobilizer System Status Log

If you suspect there is an immobilizer system problem, check the status log in the HDS.

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. On the HDS screen, at SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER SETUP, select SYSTEM CHECK, NUMBER of KEYS and STATUS LOG, then select STATUS LOG.Check the STATUS LOG count. Troubleshoot the status with the highest count first. If no counts are listed, the immobilizer system is OK. Continue with normal symptom troubleshooting.

Status Log No. | Detected Item | Probable Cause

A-1 | KEY CODE MISMATCH 1(Code format correct, but code data does not match) | The key was not registered Interference from metal such as key chains Low 12 volt battery voltage

- The key was not registered

- Interference from metal such as key chains

- Low 12 volt battery voltage

A-2 | KEY CODE MISMATCH 2(Incorrect code format) | The vehicle was turned to ON mode with another type of immobilizer key or aftermarket key Interference from metal such as key chains Low 12 volt battery voltage

- The vehicle was turned to ON mode with another type of immobilizer key or aftermarket key

- Interference from metal such as key chains

- Low 12 volt battery voltage

A-3 | KEY CODE MISMATCH 3(No transponder detected) | The vehicle was turned to ON mode with another type of immobilizer key or aftermarket key Interference from metal such as key chains Low 12 volt battery voltage Key failure Immobilizer-keyless control unit failure

- The vehicle was turned to ON mode with another type of immobilizer key or aftermarket key

- Interference from metal such as key chains

- Low 12 volt battery voltage

- Key failure

- Immobilizer-keyless control unit failure

B-1 | PCM CODE MISMATCH 1(Code format correct, but code data does not match) | PCM was not registered correctly Low 12 volt battery voltage Poor or loose terminal connections at the immobilizer-keyless control unit Communication line electrical noise

- PCM was not registered correctly

- Low 12 volt battery voltage

- Poor or loose terminal connections at the immobilizer-keyless control unit

- Communication line electrical noise

B-2 | PCM MISMATCH 2(Incorrect code format) | PCM was not registered correctly Low 12 volt battery voltage Poor or loose terminal connections at the immobilizer-keyless control unit Communication line electrical noise

- PCM was not registered correctly

- Low 12 volt battery voltage

- Poor or loose terminal connections at the immobilizer-keyless control unit

- Communication line electrical noise

C-1 | IMOES UNIT MISMATCH 1(Code format correct, but data does not match) | Imoes unit was not registered correctly Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical noise

- Imoes unit was not registered correctly

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical noise

C-2 | IMOES UNIT MISMATCH 2(Incorrect code format) | Imoes unit was not registered correctly Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical noise

- Imoes unit was not registered correctly

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical noise

Status Log No. | Detected Item | Probable Cause

D-1 | S-NET LINE PROBLEM 1(Short to ground) | Low 12 volt battery voltage Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM Communication line electrical noise

- Low 12 volt battery voltage

- Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM

- Communication line electrical noise
````

## Chunk 1642: Immobilizer System Status Log

- Title: Immobilizer System Status Log
- Source path: `pages\780.html`
- Chunk ID: `chunk_a132cd407688`
- Images: none
- Duplicate sources: `pages\2822.html`, `pages\26277.html`, `pages\15587.html`

### Full Text

````text
od between the imoes unit and the immobilizer-keyless control unit because of electrical noise

- Imoes unit was not registered correctly

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical noise

Status Log No. | Detected Item | Probable Cause

D-1 | S-NET LINE PROBLEM 1(Short to ground) | Low 12 volt battery voltage Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM Communication line electrical noise

- Low 12 volt battery voltage

- Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM

- Communication line electrical noise

D-2 | S-NET LINE PROBLEM 2(No communication) | Blown fuse Harness open from imoes unit to immobilizer-keyless control unit Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical interference Imoes unit failure Immobilizer-keyless control unit failure

- Blown fuse

- Harness open from imoes unit to immobilizer-keyless control unit

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of low 12 volt battery voltage

- Communication was not good between the imoes unit and the immobilizer-keyless control unit because of electrical interference

- Imoes unit failure

- Immobilizer-keyless control unit failure

D-3 | S-NET LINE PROBLEM 3(Open line or PCM failure) | Open or short in the harness from the PCM to the immobilizer-keyless control unit Low 12 volt battery voltage Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM Poor S-NET data communication due to electrical interference

- Open or short in the harness from the PCM to the immobilizer-keyless control unit

- Low 12 volt battery voltage

- Poor or loose terminal connections at the immobilizer-keyless control unit and the PCM

- Poor S-NET data communication due to electrical interference
````

## Chunk 1643: Keyless Access LF Antenna Function Test

- Title: Keyless Access LF Antenna Function Test
- Source path: `pages\781.html`
- Chunk ID: `chunk_bf640a85fe8c`
- Images: `images\GHH411564.jpeg`, `images\GHH411565.jpeg`
- Duplicate sources: `pages\2823.html`, `pages\26278.html`, `pages\17217.html`

### Full Text

````text
# Keyless Access LF Antenna Function Test

NOTE: Before testing, check for DTCs. If any DTCs are indicated, troubleshoot the indicated DTCs first.

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS.

4. Select the SELF CHECK and if any malfunction is found, troubleshoot it first. Select the FUNCTIONAL TESTS, and do the antenna driving test by checking the transmitting areas (A) between the LF antenna and the keyless remote.

LF Antenna Location | HDS Indication (Functional Tests)

Driver's door LF Antenna | Driver (Door) Antenna Driving

Front passenger's door LF Antenna *1 | Front Passenger (Door) Antenna Driving

Passenger's door LF Antenna *2 | Front Passenger (Door) Antenna Driving

Rear bumper LF Antenna | Trunk/Tailgate/Rear Bumper Antenna Driving

*1: 4-door

*2: 2-door

NOTE:

- Functional Tests cannot operate at the same time, check the LF antennas one at a time.

- Test the transmitting area at about 90 cm (35.4 in) height from the ground.

- The LED will blink when the keyless remote is within the shaded areas.

Courtesy of HONDA, U.S.A., INC.

6. Select the FUNCTIONAL TESTS, and do the antenna driving test by checking the transmitting areas (A) between the LF antenna and the keyless remote (except on the dashboard, in the glove box, door pockets, console box, and other enclosed areas).

LF Antenna Location | HDS Indication (Functional Tests)

Front interior LF antenna | Front Interior Antenna Driving

Rear interior LF antenna | Rear Interior Antenna Driving

Rear shelf LF antenna | Trunk/Rear Shelf Antenna Driving

NOTE: Functional Tests cannot operate at the same time, check the LF antennas one at a time.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1644: Keyless Access LF Antenna Function Test (5-door) (2017 2018 2019 2020 2021)

- Title: Keyless Access LF Antenna Function Test (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\782.html`
- Chunk ID: `chunk_0d2be114b3a8`
- Images: `images\GHH411566.jpeg`, `images\GHH411567.jpeg`
- Duplicate sources: `pages\2824.html`, `pages\26279.html`, `pages\17218.html`

### Full Text

````text
# Keyless Access LF Antenna Function Test (5-door) (2017 2018 2019 2020 2021)

NOTE: Before testing, check for DTCs. If any DTCs are indicated, troubleshoot the indicated DTCs first.

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS.

4. Select the SELF CHECK and if any malfunction is found, troubleshoot it first. Select the FUNCTIONAL TESTS, and do the antenna driving test by checking the transmitting areas (A) between the LF antenna and the keyless remote.

LF Antenna Location | HDS Indication (Functional Tests)

Driver's door LF Antenna | Driver (Door) Antenna Driving

Front passenger's door LF Antenna | Front Passenger (Door) Antenna Driving

Rear bumper LF Antenna | Trunk/Tailgate/Rear Bumper Antenna Driving

NOTE:

- Functional Tests cannot operate at the same time, check the LF antennas one at a time.

- Test the transmitting area at about 90 cm (35.4 in) height from the ground.

- The LED will blink when the keyless remote is within the shaded areas.

Courtesy of HONDA, U.S.A., INC.

6. Select the FUNCTIONAL TESTS, and do the antenna driving test by checking the transmitting areas (A) between the LF antenna and the keyless remote (except on the dashboard, in the glove box, door pockets, console box, and other enclosed areas).

LF Antenna Location | HDS Indication (Functional Tests)

Front interior LF antenna | Front Interior Antenna Driving

Middle interior LF antenna | Middle Interior Shelf Antenna Driving

Rear interior LF antenna | Rear Interior Antenna Driving

NOTE: Functional Tests cannot operate at the same time, check the LF antennas one at a time.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 1645: Keyless Access System Status Log

- Title: Keyless Access System Status Log
- Source path: `pages\783.html`
- Chunk ID: `chunk_aa5ca6081e6a`
- Images: none
- Duplicate sources: `pages\2825.html`, `pages\26280.html`, `pages\15588.html`

### Full Text

````text
# Keyless Access System Status Log

If you suspect there is an immobilizer system problem, check the status log in the HDS.

1. Connect the HDS to the data link connector (DLC)

2. Turn the vehicle to the ON mode.

3. On the HDS screen, at SYSTEM SELECTION MENU, enter ONE-PUSH START, then select KEYLESS ACCESS CONTROL UNIT or BACKUP CONTROL UNIT.

NOTE: If the HDS does not communicate, check the body control module power, ground, K line, and L-line connectors.

4. At KEYLESS ACCESS CONTROL UNIT, enter KEYLESS ACCESS SYSTEM INFORMATION, then select KEYLESS ACCESS STATUS LOG.

5. At BACKUP CONTROL UNIT, enter SYSTEM INFORMATION, then select STATUS LOG. Check the STATUS LOG count. Troubleshoot the status with the highest count first. If no counts are listed, the immobilizer system is OK. Continue with normal symptom troubleshooting.

Status Log (Keyless Access Control Unit)

Status Log No. | Possible cause

B-1B-2 | PCM was not registered correctly Body control module was registered correctly Poor connections or loose terminals between body control module and PCM Poor connections or loose terminals in the IG1 line Low 12 volt battery voltage Electrical noise

- PCM was not registered correctly

- Body control module was registered correctly

- Poor connections or loose terminals between body control module and PCM

- Poor connections or loose terminals in the IG1 line

- Low 12 volt battery voltage

- Electrical noise

C-1C-2 | Poor connections or loose terminals in the IG1 line Body control module was not registered Low 12 volt battery voltage Electrical noise

- Poor connections or loose terminals in the IG1 line

- Body control module was not registered

- Low 12 volt battery voltage

- Electrical noise

D-1D-2D-3 | Poor connections or loose terminals between body control module and PCM Low 12 volt battery voltage Electrical noise Blown fuse

- Poor connections or loose terminals between body control module and PCM

- Low 12 volt battery voltage

- Electrical noise

- Blown fuse

Status Log (Backup Control Unit)

Status Log No. | Possible cause

A-1A-2A-3 | Keyless remote was not registered correctly Engine start/stop switch failure

- Keyless remote was not registered correctly

- Engine start/stop switch failure

B-1B-2 | PCM was not registered correctly Communication error between body control module and PCM Low 12 volt battery voltage Electrical noise

- PCM was not registered correctly

- Communication error between body control module and PCM

- Low 12 volt battery voltage

- Electrical noise

C-1C-2 | Body control module was not registered correctly Poor connections or loose terminals in the IG1 line Low 12 volt battery voltage Electrical noise

- Body control module was not registered correctly

- Poor connections or loose terminals in the IG1 line

- Low 12 volt battery voltage

- Electrical noise

Status Log No. | Possible cause

D-1D-2D-3 | Poor connections or loose terminals between body control module and PCM S-NET line short Low 12 volt battery voltage Electrical noise Blown fuse

- Poor connections or loose terminals between body control module and PCM

- S-NET line short

- Low 12 volt battery voltage

- Electrical noise

- Blown fuse
````

## Chunk 1646: Park Pin Switch Test: Test

- Title: Park Pin Switch Test: Test
- Source path: `pages\784.html`
- Chunk ID: `chunk_a2856f349d8c`
- Images: `images\GHH411568.jpeg`, `images\GHH411569.jpeg`
- Duplicate sources: `pages\2826.html`, `pages\26281.html`, `pages\17219.html`

### Full Text

````text
# Park Pin Switch Test: Test

- Center Console - Remove

- Park Pin Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each shift lever condition according to the table. 3. If the continuity is not as specified, check the shift cable adjustment If the cable adjustment is OK, the park pin switch is faulty; replace the shift lock solenoid/park pin switch .

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Disconnect the connector (A). 2. Check for continuity between the terminals in each shift lever condition according to the table. 3. If the continuity is not as specified, check the shift cable adjustment If the cable adjustment is OK, the park pin switch is faulty; replace the shift lock solenoid/park pin switch .

2. Check for continuity between the terminals in each shift lever condition according to the table.

3. If the continuity is not as specified, check the shift cable adjustment

If the cable adjustment is OK, the park pin switch is faulty; replace the shift lock solenoid/park pin switch .

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1647: Tailgate Outer Handle Switch Test (5-door) (2017 2018 2019 2020 2021): Test

- Title: Tailgate Outer Handle Switch Test (5-door) (2017 2018 2019 2020 2021): Test
- Source path: `pages\785.html`
- Chunk ID: `chunk_9c9b410251e8`
- Images: `images\GHH411570.jpeg`, `images\GHH411571.jpeg`
- Duplicate sources: `pages\2827.html`, `pages\26282.html`, `pages\17220.html`

### Full Text

````text
# Tailgate Outer Handle Switch Test (5-door) (2017 2018 2019 2020 2021): Test

- Rear License Trim - Remove

- Tailgate Outer Handle Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, replace the tailgate outer handle switch (A).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, replace the tailgate outer handle switch (A).

2. If the continuity is not as specified, replace the tailgate outer handle switch

(A).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1648: Trunk Lid Outer Handle Switch Test: Test

- Title: Trunk Lid Outer Handle Switch Test: Test
- Source path: `pages\786.html`
- Chunk ID: `chunk_d5cd2cceb744`
- Images: `images\GHH411572.jpeg`, `images\GHH411573.jpeg`
- Duplicate sources: `pages\2828.html`, `pages\26283.html`, `pages\17221.html`

### Full Text

````text
# Trunk Lid Outer Handle Switch Test: Test

- Rear License Trim - Remove

- Trunk Lid Outer Handle Switch - Test Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. NOTE: Illustrations used in the procedure are for 4-door. 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, replace the trunk lid outer handle switch (A).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | NOTE: Illustrations used in the procedure are for 4-door. 1. Check for continuity between the terminals in each switch position according to the table. 2. If the continuity is not as specified, replace the trunk lid outer handle switch (A).

1. Check for continuity between the terminals in each switch position according to the table.

2. If the continuity is not as specified, replace the trunk lid outer handle switch

(A).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.
````

## Chunk 1649: Immobilizer System Symptom Troubleshooting - Engine does not start with the immobilizer key

- Title: Immobilizer System Symptom Troubleshooting - Engine does not start with the immobilizer key
- Source path: `pages\787.html`
- Chunk ID: `chunk_0ff199e88d90`
- Images: none
- Duplicate sources: `pages\2829.html`, `pages\26284.html`, `pages\17171.html`

### Full Text

````text
# Immobilizer System Symptom Troubleshooting - Engine does not start with the immobilizer key

NOTE: Before troubleshooting, check the items listed in General Check before Troubleshooting .

- Problem verification -1. Try to start the engine. Does the engine start? YES Intermittent failure, the vehicle is OK at this time. NO Go to step 2.

-1. Try to start the engine.

Does the engine start?

YES

Intermittent failure, the vehicle is OK at this time.

NO

Go to step 2.

- Immobilizer system check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode, and check the security indicator. Does the indicator off? YES Go to step 3. NO Go to the security indicator blinks troubleshooting .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode, and check the security indicator.

Does the indicator off?

YES

Go to step 3.

NO

Go to the security indicator blinks troubleshooting .

- Starting system check -1. Turn the vehicle to the START mode. Does the starter motor run? YES Go to step 4. NO Go to starting system, and check the starter motor .

-1. Turn the vehicle to the START mode.

Does the starter motor run?

YES

Go to step 4.

NO

Go to starting system, and check the starter motor .

- PGM-FI system check 1 -1. Try to start the engine with the immobilizer key. Does the engine start? YES Go to step 5. NO Go to the PGM-FI system symptom troubleshooting .

-1. Try to start the engine with the immobilizer key.

Does the engine start?

YES

Go to step 5.

NO

Go to the PGM-FI system symptom troubleshooting .

- PGM-FI system check 2 -1. Wait for a few minutes with the engine running. Does the engine stop? YES Go to the PGM-FI system symptom troubleshooting . NO The system is OK at this time.

-1. Wait for a few minutes with the engine running.

Does the engine stop?

YES

Go to the PGM-FI system symptom troubleshooting .

NO

The system is OK at this time.
````

## Chunk 1650: Immobilizer System Symptom Troubleshooting - Security indicator blinks (2/4-door)

- Title: Immobilizer System Symptom Troubleshooting - Security indicator blinks (2/4-door)
- Source path: `pages\788.html`
- Chunk ID: `chunk_e0ec470f6f0d`
- Images: none
- Duplicate sources: `pages\2830.html`, `pages\26285.html`, `pages\17170.html`

### Full Text

````text
# Immobilizer System Symptom Troubleshooting - Security indicator blinks (2/4-door)

NOTE: Before troubleshooting, check the items listed in General Check before Troubleshooting .

- Immobilizer system check -1. Connect the HDS to the data link connector (DLC) . -2. Turn the vehicle to the ON mode. -3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER SETUP. NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K line connections. Immobilizer - Information/Record Data/History Data - Immobilizer Information Select the SYSTEM CHECK from the IMMOBILIZER INFO. Is SYSTEM CHECK indicated? YES Troubleshoot the immobilizer system according to the results of the SYSTEM CHECK . NO Go to step 2.

-1. Connect the HDS to the data link connector (DLC) .

-2. Turn the vehicle to the ON mode.

-3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER SETUP.

NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K line connections.

Immobilizer - Information/Record Data/History Data - Immobilizer Information

Select the SYSTEM CHECK from the IMMOBILIZER INFO.

Is SYSTEM CHECK indicated?

YES

Troubleshoot the immobilizer system according to the results of the SYSTEM CHECK .

NO

Go to step 2.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Enter the vehicle, and remove the ignition key from the ignition switch, then close all the doors. -3. Operate the keyless transmitter LOCK and UNLOCK several times in the vehicle. Do the door lock actuators work normally? YES The GND wire is OK. Go to step 3. NO Repair an open or high resistance in the ground wire or poor ground (G503).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Enter the vehicle, and remove the ignition key from the ignition switch, then close all the doors.

-3. Operate the keyless transmitter LOCK and UNLOCK several times in the vehicle.

Do the door lock actuators work normally?

YES

The GND wire is OK. Go to step 3.

NO

Repair an open or high resistance in the ground wire or poor ground (G503).

- Open wire check (IG1 MON line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Immobilizer-keyless control unit 7P connector No. 6 Test point 2 Body ground Is there battery voltage? YES The IG1 MON wire is OK. Replace the immobilizer-keyless control unit . NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Immobilizer-keyless control unit 7P connector No. 6

Test point 2 | Body ground

Is there battery voltage?

YES

The IG1 MON wire is OK. Replace the immobilizer-keyless control unit .

NO

Repair an open or high resistance in the wire.
````

## Chunk 1651: Immobilizer System Symptom Troubleshooting - Security indicator blinks (5-door) (2017 2018 2019 2020 2021)

- Title: Immobilizer System Symptom Troubleshooting - Security indicator blinks (5-door) (2017 2018 2019 2020 2021)
- Source path: `pages\789.html`
- Chunk ID: `chunk_a8f697f6a60f`
- Images: none
- Duplicate sources: `pages\2831.html`, `pages\26286.html`, `pages\17222.html`

### Full Text

````text
# Immobilizer System Symptom Troubleshooting - Security indicator blinks (5-door) (2017 2018 2019 2020 2021)

NOTE: Before troubleshooting, check the items listed in General Check before Troubleshooting .

- Immobilizer system check -1. Connect the HDS to the data link connector (DLC) . -2. Turn the vehicle to the ON mode. -3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER SETUP. NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K line connections. Immobilizer - Information/Record Data/History Data - Immobilizer Information Select the SYSTEM CHECK from the IMMOBILIZER INFO. Is SYSTEM CHECK indicated? YES Troubleshoot the immobilizer system according to the results of the SYSTEM CHECK . NO Go to step 2.

-1. Connect the HDS to the data link connector (DLC) .

-2. Turn the vehicle to the ON mode.

-3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER SETUP.

NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K line connections.

Immobilizer - Information/Record Data/History Data - Immobilizer Information

Select the SYSTEM CHECK from the IMMOBILIZER INFO.

Is SYSTEM CHECK indicated?

YES

Troubleshoot the immobilizer system according to the results of the SYSTEM CHECK .

NO

Go to step 2.

- Open wire check (GND line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Enter the vehicle, and remove the ignition key from the ignition switch, then close all the doors. -3. Operate the keyless transmitter LOCK and UNLOCK several times in the vehicle. Do the door lock actuators work normally? YES The GND wire is OK. Go to step 3. NO Repair an open or high resistance in the ground wire or poor ground (G503).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Enter the vehicle, and remove the ignition key from the ignition switch, then close all the doors.

-3. Operate the keyless transmitter LOCK and UNLOCK several times in the vehicle.

Do the door lock actuators work normally?

YES

The GND wire is OK. Go to step 3.

NO

Repair an open or high resistance in the ground wire or poor ground (G503).

- Open wire check (IG1 FUEL PUMP line) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Test point 1 Immobilizer-keyless control unit 7P connector No. 6 Test point 2 Body ground Is there battery voltage? YES The IG1 FUEL PUMP wire is OK. Replace the immobilizer-keyless control unit . NO Repair an open or high resistance in the wire.

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Test point 1 | Immobilizer-keyless control unit 7P connector No. 6

Test point 2 | Body ground

Is there battery voltage?

YES

The IG1 FUEL PUMP wire is OK. Replace the immobilizer-keyless control unit .

NO

Repair an open or high resistance in the wire.
````

## Chunk 1652: Immobilizer System Symptom Troubleshooting - Security indicator turns on

- Title: Immobilizer System Symptom Troubleshooting - Security indicator turns on
- Source path: `pages\790.html`
- Chunk ID: `chunk_4d818487b5a7`
- Images: none
- Duplicate sources: `pages\2832.html`, `pages\26287.html`, `pages\17172.html`

### Full Text

````text
# Immobilizer System Symptom Troubleshooting - Security indicator turns on

- Immobilizer system check -1. Connect the HDS to the data link connector (DLC) . -2. Turn the vehicle to the ON mode. -3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER INFO. NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K-line connections. Immobilizer - Information/Record Data/History Data - Immobilizer Information Do the SYSTEM CHECK from the IMMOBILIZER INFO. Is N-1 OK indicated? YES Replace the gauge control module . NO Replace the immobilizer-keyless control unit .

-1. Connect the HDS to the data link connector (DLC) .

-2. Turn the vehicle to the ON mode.

-3. From the SYSTEM SELECTION MENU, enter IMMOBI, then select IMMOBILIZER INFO.

NOTE: If the HDS does not communicate with the immobilizer-keyless control unit, check the power, ground, and K-line connections.

Immobilizer - Information/Record Data/History Data - Immobilizer Information

Do the SYSTEM CHECK from the IMMOBILIZER INFO.

Is N-1 OK indicated?

YES

Replace the gauge control module .

NO

Replace the immobilizer-keyless control unit .
````

## Chunk 1653: Keyless Access System Symptom Troubleshooting - All the doors will not lock and unlock

- Title: Keyless Access System Symptom Troubleshooting - All the doors will not lock and unlock
- Source path: `pages\791.html`
- Chunk ID: `chunk_459a0e17ad2c`
- Images: none
- Duplicate sources: `pages\2833.html`, `pages\26288.html`, `pages\14438.html`

### Full Text

````text
# Keyless Access System Symptom Troubleshooting - All the doors will not lock and unlock

- Door lock actuator operation check 1 -1. Remove all the keyless remotes from inside the vehicle, and close all doors. -2. Push each LOCK and UNLOCK buttons of the keyless remote, at least 10 times. Do the door lock actuators work normally? YES Go to step 2. NO Go to step 3.

-1. Remove all the keyless remotes from inside the vehicle, and close all doors.

-2. Push each LOCK and UNLOCK buttons of the keyless remote, at least 10 times.

Do the door lock actuators work normally?

YES

Go to step 2.

NO

Go to step 3.

- Door lock actuator operation check 2 -1. Lock and unlock the doors with touching the door outer handle. Do the door lock actuators work normally? YES Intermittent failure, the system is OK at this time. Check for loose or poor connections. NO Go to symptom trouble shooting "The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote" .

-1. Lock and unlock the doors with touching the door outer handle.

Do the door lock actuators work normally?

YES

Intermittent failure, the system is OK at this time. Check for loose or poor connections.

NO

Go to symptom trouble shooting "The doors will not unlock or lock with the door outer handle touch sensor or lock switch, but will unlock or lock with the keyless remote" .

- Determine possible failure area (keyless remote, others) -1. Push the LOCK and the UNLOCK buttons of the keyless remote, and check if the LED on the keyless remote comes on. Does the LED come on? YES Go to step 4. NO Replace the keyless remote battery and recheck the system. If the symptom does not go away, replace the keyless remote.

-1. Push the LOCK and the UNLOCK buttons of the keyless remote, and check if the LED on the keyless remote comes on.

Does the LED come on?

YES

Go to step 4.

NO

Replace the keyless remote battery and recheck the system. If the symptom does not go away, replace the keyless remote.

- Door lock actuator operation check 2 -1. Lock and unlock the doors with touching the door outer handle. Do the door lock actuators work normally? YES Register the keyless remote , and recheck. If the symptom does not go away, replace the keyless remote. NO Go to step 5.

-1. Lock and unlock the doors with touching the door outer handle.

Do the door lock actuators work normally?

YES

Register the keyless remote , and recheck. If the symptom does not go away, replace the keyless remote.

NO

Go to step 5.

- Door lock actuator operation check 3 -1. Lock and unlock the doors with the driver's door lock switch. Do the door lock actuators work normally? YES Go to step 6. NO Check the B-CAN system DTCs. If not, check the door lock system.

-1. Lock and unlock the doors with the driver's door lock switch.

Do the door lock actuators work normally?

YES

Go to step 6.

NO

Check the B-CAN system DTCs. If not, check the door lock system.

- Keyless access system check -1. Do the keyless access remote check using the all keyless remotes . Are the all keyless remotes OK? YES Do the SYSTEM CHECK 1 and SYSTEM CHECK 2 with the HDS . If the result is indicated, troubleshoot the items based on the SYSTEM CHECK table. NO Replace the keyless remote and recheck.

-1. Do the keyless access remote check using the all keyless remotes .

Are the all keyless remotes OK?

YES

Do the SYSTEM CHECK 1 and SYSTEM CHECK 2 with the HDS . If the result is indicated, troubleshoot the items based on the SYSTEM CHECK table.

NO

Replace the keyless remote and recheck.
````

## Chunk 1654: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)

- Title: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)
- Source path: `pages\792.html`
- Chunk ID: `chunk_b3fe6d64c286`
- Images: `images\GHH411574.jpeg`, `images\GHH411575.jpeg`, `images\GHH411576.jpeg`, `images\GHH411577.jpeg`, `images\GHH411578.jpeg`, `images\GHH411579.jpeg`, `images\GHH411580.jpeg`
- Duplicate sources: `pages\2834.html`, `pages\26289.html`, `pages\14406.html`

### Full Text

````text
# Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)

- Keyless access system check 1 -1. Do this procedure 10 times: Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right. Does the system change to ON mode? YES Intermittent failure, the system is OK at this time. Check for loose or poor connection. NO Go to step 2.

-1. Do this procedure 10 times: Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right.

Does the system change to ON mode?

YES

Intermittent failure, the system is OK at this time. Check for loose or poor connection.

NO

Go to step 2.

- Keyless access system check 2 -1. Touch the engine start/stop switch with the keyless remote. The buttons on the keyless remote should be facing you. -2. Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right. Does the system change to ON mode? YES Go to keyless access system symptom troubleshooting "Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch" . NO Go to step 3.

-1. Touch the engine start/stop switch with the keyless remote. The buttons on the keyless remote should be facing you.

-2. Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right.

Does the system change to ON mode?

YES

Go to keyless access system symptom troubleshooting "Cannot select ON mode with keyless access, but can select ON mode with the keyless remote touching the engine start/stop switch" .

NO

Go to step 3.

- Keyless access system check 3 -1. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter SELF CHECK. One-Push - KEYLESS ACCESS CONTROL UNIT - SELF CHECK Does the system communicate with the HDS? YES Go to step 4. NO Go to step 11.

-1. Select KEYLESS ACCESS CONTROL UNIT from the ONE-PUSH START system select menu with the HDS, and enter SELF CHECK.

One-Push - KEYLESS ACCESS CONTROL UNIT - SELF CHECK

Does the system communicate with the HDS?

YES

Go to step 4.

NO

Go to step 11.

- Keyless access system check 4 -1. Reboot the HDS. -2. Select model on the HDS screen. -3. When prompted by the HDS, select YES when asked if the vehicle has keyless access system, then press and hold the engine start/stop button for at least 2 minutes. This selects the forced ON mode. Does the system change to forced ON mode? YES Go to step 5. NO Go to step 16.

-1. Reboot the HDS.

-2. Select model on the HDS screen.

-3. When prompted by the HDS, select YES when asked if the vehicle has keyless access system, then press and hold the engine start/stop button for at least 2 minutes. This selects the forced ON mode.

Does the system change to forced ON mode?

YES

Go to step 5.

NO

Go to step 16.

- PCU DTC check -1. Check for PCU DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Troubleshoot the PCU DTCs. NO Go to step 6.

-1. Check for PCU DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Troubleshoot the PCU DTCs.

NO

Go to step 6.

- Keyless access DTC check -1. Check for keyless access control unit DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Troubleshoot the keyless access control unit DTCs. NO Go to step 7.

-1. Check for keyless access control unit DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Troubleshoot the keyless access control unit DTCs.

NO

Go to step 7.

- Backup DTC check -1. Check for backup control unit DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Troubleshoot the backup control unit DTCs. NO Go to step 8.

-1. Check for backup control unit DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Troubleshoot the backup control unit DTCs.

NO

Go to step 8.

- Keyless access system check 5 -1. Do the keyless access remote check using the all keyless remotes . Are the all keyless remotes OK? YES Go to step 9. NO Replace the keyless remote and recheck.

-1. Do the keyless access remote check using the all keyless remotes .

Are the all keyless remotes OK?

YES

Go to step 9.

NO

Replace the keyless remote and recheck.

- Keyless access system check 6 -1. Turn the vehicle to the OFF (LOCK) mode. -2.
````

## Chunk 1655: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)

- Title: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)
- Source path: `pages\792.html`
- Chunk ID: `chunk_8f1ad3ebf910`
- Images: `images\GHH411574.jpeg`, `images\GHH411575.jpeg`, `images\GHH411576.jpeg`, `images\GHH411577.jpeg`, `images\GHH411578.jpeg`, `images\GHH411579.jpeg`, `images\GHH411580.jpeg`
- Duplicate sources: `pages\793.html`, `pages\2834.html`, `pages\2835.html`, `pages\26289.html`, `pages\26290.html`, `pages\14406.html`, `pages\17223.html`

### Full Text

````text
- Backup DTC check -1. Check for backup control unit DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Troubleshoot the backup control unit DTCs. NO Go to step 8.

-1. Check for backup control unit DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Troubleshoot the backup control unit DTCs.

NO

Go to step 8.

- Keyless access system check 5 -1. Do the keyless access remote check using the all keyless remotes . Are the all keyless remotes OK? YES Go to step 9. NO Replace the keyless remote and recheck.

-1. Do the keyless access remote check using the all keyless remotes .

Are the all keyless remotes OK?

YES

Go to step 9.

NO

Replace the keyless remote and recheck.

- Keyless access system check 6 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove all the keyless remotes from inside the vehicle. Place the keyless remotes more than 1.5 m (5.0 ft) away from the vehicle. -3. Disconnect the electric steering lock 12P connector. -4. Reboot the HDS without pressing the engine start/stop button. -5. Do the registration of the body control module according to the instructions on the HDS screen. -6. Select REGISTRATION from the ONE-PUSH START system select menu with the HDS, then select REPLACE PCU/BACKUP CONTROL/KEYLESS ACCESS CONTROL UNIT. -7. Reconnect the electric steering lock 12P connector. -8. Take the keyless remote into the vehicle, and clear the PCU DTCs with the HDS. -9. Do this procedure 10 times: Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right. Does the system change to ON mode? YES Intermittent failure, the system is OK at this time. Check for loose or poor connection. NO Go to step 10.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove all the keyless remotes from inside the vehicle. Place the keyless remotes more than 1.5 m (5.0 ft) away from the vehicle.

-3. Disconnect the electric steering lock 12P connector.

-4. Reboot the HDS without pressing the engine start/stop button.

-5. Do the registration of the body control module according to the instructions on the HDS screen.

-6. Select REGISTRATION from the ONE-PUSH START system select menu with the HDS, then select REPLACE PCU/BACKUP CONTROL/KEYLESS ACCESS CONTROL UNIT.

-7. Reconnect the electric steering lock 12P connector.

-8. Take the keyless remote into the vehicle, and clear the PCU DTCs with the HDS.

-9. Do this procedure 10 times: Turn the vehicle to the ON mode while turning the steering wheel to the left and to the right.

Does the system change to ON mode?

YES

Intermittent failure, the system is OK at this time. Check for loose or poor connection.

NO

Go to step 10.

- Body control module check (substitution) -1. Substitute a known-good body control module. -2. Do the registration of the body control module according to the instructions on the HDS screen. -3. Select REGISTRATION from the ONE-PUSH START system select menu with the HDS, then select REPLACE PCU/BACKUP CONTROL/KEYLESS ACCESS CONTROL UNIT. -4. Recheck the system. Is the system normal? YES Replace the original body control module . NO Replace the steering lock .

-1. Substitute a known-good body control module.

-2. Do the registration of the body control module according to the instructions on the HDS screen.

-3. Select REGISTRATION from the ONE-PUSH START system select menu with the HDS, then select REPLACE PCU/BACKUP CONTROL/KEYLESS ACCESS CONTROL UNIT.

-4. Recheck the system.

Is the system normal?

YES

Replace the original body control module .

NO

Replace the steering lock .

- L-line check -1. Do the DLC circuit troubleshooting . Is L-line OK? YES Go to step 12. NO Repair an L-line wire circuit.

-1. Do the DLC circuit troubleshooting .

Is L-line OK?

YES

Go to step 12.

NO

Repair an L-line wire circuit.

- Engine start/stop switch operation check -1. Do the engine start/stop switch test . Is the engine start/stop switch OK? YES Go to step 13. NO Replace the engine start/stop switch .

-1. Do the engine start/stop switch test .

Is the engine start/stop switch OK?

YES

Go to step 13.

NO

Replace the engine start/stop switch .

- Open wire check (SS1(+), SS2(-) lines) -1. Disconnect the following connectors. Engine start/stop switch 10P connector Body control module connector G (32P) -2. Check for continuity between test points 1 and 2 respectively.
````

## Chunk 1656: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)

- Title: Keyless Access System Symptom Troubleshooting - Cannot select ON mode with keyless access and with the keyless remote touching the engine start/stop switch(2/4-door with Electric Steering Lock)
- Source path: `pages\792.html`
- Chunk ID: `chunk_ea327d30897d`
- Images: `images\GHH411574.jpeg`, `images\GHH411575.jpeg`, `images\GHH411576.jpeg`, `images\GHH411577.jpeg`, `images\GHH411578.jpeg`, `images\GHH411579.jpeg`, `images\GHH411580.jpeg`
- Duplicate sources: `pages\2834.html`, `pages\26289.html`, `pages\14406.html`

### Full Text

````text
ock .

- L-line check -1. Do the DLC circuit troubleshooting . Is L-line OK? YES Go to step 12. NO Repair an L-line wire circuit.

-1. Do the DLC circuit troubleshooting .

Is L-line OK?

YES

Go to step 12.

NO

Repair an L-line wire circuit.

- Engine start/stop switch operation check -1. Do the engine start/stop switch test . Is the engine start/stop switch OK? YES Go to step 13. NO Replace the engine start/stop switch .

-1. Do the engine start/stop switch test .

Is the engine start/stop switch OK?

YES

Go to step 13.

NO

Replace the engine start/stop switch .

- Open wire check (SS1(+), SS2(-) lines) -1. Disconnect the following connectors. Engine start/stop switch 10P connector Body control module connector G (32P) -2. Check for continuity between test points 1 and 2 respectively. Test condition Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected Test point 1 Engine start/stop switch 10P connector No. 6 Test point 2 Body control module connector G (32P) No. 18 Test point 1 Engine start/stop switch 10P connector No. 10 Test point 2 Body control module connector G (32P) No. 9 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SS1(+) and SS2(-) wires are OK. Go to step 14. NO Repair an open or high resistance in the wire.

-1. Disconnect the following connectors.

Engine start/stop switch 10P connector

Body control module connector G (32P)

-2. Check for continuity between test points 1 and 2 respectively.

Test condition | Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected

Test point 1 | Engine start/stop switch 10P connector No. 6

Test point 2 | Body control module connector G (32P) No. 18

Test point 1 | Engine start/stop switch 10P connector No. 10

Test point 2 | Body control module connector G (32P) No. 9

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SS1(+) and SS2(-) wires are OK. Go to step 14.

NO

Repair an open or high resistance in the wire.

- Open wire check (+B SMART line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected Test point 1 Engine start/stop switch 10P connector No. 5 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B SMART wire is OK. Go to step 15. NO Repair an open or high resistance in the wire. If wire is OK, check the under-dash fuse/relay box No. B30 (10 A) fuse circuit.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected

Test point 1 | Engine start/stop switch 10P connector No. 5

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B SMART wire is OK. Go to step 15.

NO

Repair an open or high resistance in the wire. If wire is OK, check the under-dash fuse/relay box No. B30 (10 A) fuse circuit.

- Open wire check (GND line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected Test point 1 Engine start/stop switch 10P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The GND wire is OK. Go to step 17. NO Repair an open or high resistance in the ground wire or poor ground (G503).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode Engine start/stop switch 10P connector: disconnected Body control module connector G (32P): disconnected

Test point 1 | Engine start/stop switch 10P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The GND wire is OK. Go to step 17.

NO

Repair an open or high resistance in the ground wire or poor ground (G503).

- PCU DTC check -1. Check for PCU DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Troubleshoot the PCU DTCs. NO Go to step 17.

-1. Check for PCU DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Troubleshoot the PCU DTCs.

NO

Go to step 17.

- Open wire check (+B BACK UP, +B SMART lines) -1. Disconnect the following connector.
````

## Sources Used

- `pages\625.html`
- `pages\626.html`
- `pages\627.html`
- `pages\628.html`
- `pages\629.html`
- `pages\630.html`
- `pages\631.html`
- `pages\632.html`
- `pages\633.html`
- `pages\634.html`
- `pages\635.html`
- `pages\636.html`
- `pages\637.html`
- `pages\638.html`
- `pages\639.html`
- `pages\640.html`
- `pages\641.html`
- `pages\642.html`
- `pages\643.html`
- `pages\644.html`
- `pages\645.html`
- `pages\646.html`
- `pages\647.html`
- `pages\648.html`
- `pages\649.html`
- `pages\650.html`
- `pages\651.html`
- `pages\652.html`
- `pages\653.html`
- `pages\654.html`
- `pages\655.html`
- `pages\657.html`
- `pages\658.html`
- `pages\659.html`
- `pages\660.html`
- `pages\661.html`
- `pages\662.html`
- `pages\663.html`
- `pages\664.html`
- `pages\665.html`
- `pages\666.html`
- `pages\667.html`
- `pages\668.html`
- `pages\669.html`
- `pages\670.html`
- `pages\671.html`
- `pages\672.html`
- `pages\673.html`
- `pages\674.html`
- `pages\675.html`
- `pages\676.html`
- `pages\677.html`
- `pages\679.html`
- `pages\680.html`
- `pages\681.html`
- `pages\682.html`
- `pages\683.html`
- `pages\684.html`
- `pages\685.html`
- `pages\686.html`
- `pages\687.html`
- `pages\688.html`
- `pages\689.html`
- `pages\690.html`
- `pages\691.html`
- `pages\692.html`
- `pages\693.html`
- `pages\694.html`
- `pages\697.html`
- `pages\698.html`
- `pages\699.html`
- `pages\700.html`
- `pages\701.html`
- `pages\702.html`
- `pages\703.html`
- `pages\704.html`
- `pages\705.html`
- `pages\706.html`
- `pages\707.html`
- `pages\708.html`
- `pages\709.html`
- `pages\710.html`
- `pages\711.html`
- `pages\712.html`
- `pages\713.html`
- `pages\714.html`
- `pages\715.html`
- `pages\716.html`
- `pages\717.html`
- `pages\718.html`
- `pages\719.html`
- `pages\720.html`
- `pages\721.html`
- `pages\722.html`
- `pages\723.html`
- `pages\724.html`
- `pages\725.html`
- `pages\726.html`
- `pages\727.html`
- `pages\728.html`
- `pages\729.html`
- `pages\730.html`
- `pages\731.html`
- `pages\733.html`
- `pages\734.html`
- `pages\735.html`
- `pages\736.html`
- `pages\737.html`
- `pages\738.html`
- `pages\739.html`
- `pages\740.html`
- `pages\741.html`
- `pages\742.html`
- `pages\743.html`
- `pages\744.html`
- `pages\745.html`
- `pages\746.html`
- `pages\747.html`
- `pages\748.html`
- `pages\749.html`
- `pages\750.html`
- `pages\751.html`
- `pages\752.html`
- `pages\753.html`
- `pages\754.html`
- `pages\759.html`
- `pages\760.html`
- `pages\761.html`
- `pages\762.html`
- `pages\763.html`
- `pages\764.html`
- `pages\765.html`
- `pages\770.html`
- `pages\771.html`
- `pages\772.html`
- `pages\773.html`
- `pages\774.html`
- `pages\775.html`
- `pages\776.html`
- `pages\777.html`
- `pages\778.html`
- `pages\779.html`
- `pages\780.html`
- `pages\781.html`
- `pages\782.html`
- `pages\783.html`
- `pages\784.html`
- `pages\785.html`
- `pages\786.html`
- `pages\787.html`
- `pages\788.html`
- `pages\789.html`
- `pages\790.html`
- `pages\791.html`
- `pages\792.html`
