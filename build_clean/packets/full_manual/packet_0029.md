# Deep Research Manual Packet 0029

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0029
- Chunk count: 199
- Chunk range: 6837-7035
- Source count: 111
- Target maximum characters: 750000

## Manual Chunks

## Chunk 6837: DTC P0615 (L15B7/L15BA/L15BY)

- Title: DTC P0615 (L15B7/L15BA/L15BY)
- Source path: `pages\7580.html`
- Chunk ID: `chunk_30bb5adcaa6e`
- Images: `images\GHH405071.jpeg`, `images\GHH405072.jpeg`, `images\GHH405073.jpeg`
- Duplicate sources: `pages\9167.html`, `pages\22229.html`, `pages\15271.html`

### Full Text

````text
. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector A (8P): disconnected

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector A (8P) No. 8

Test point 2 | PCM connector A (50P) No. 19

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0615 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 6. NO Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board. If the wire is OK, replace the under-dash fuse/relay box . Also replace the No. B21 (10 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 6.

NO

Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board. If the wire is OK, replace the under-dash fuse/relay box . Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Relay circuit board connector B (6P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 7. NO Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P)

Relay circuit board connector B (6P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector B (6P): disconnected

Under-dash fuse/relay box connector C (27P): disconnected

Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground

Test point 1 | Relay circuit board connector B (6P) No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 7.

NO

Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Replace the under-dash fuse/relay box . NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Replace the under-dash fuse/relay box .

NO

Replace the relay circuit board .
````

## Chunk 6838: DTC P0616 (K20C1) (17-21)

- Title: DTC P0616 (K20C1) (17-21)
- Source path: `pages\7581.html`
- Chunk ID: `chunk_2a711188dcef`
- Images: none
- Duplicate sources: `pages\9168.html`, `pages\22230.html`, `pages\14856.html`

### Full Text

````text
# DTC P0616 (K20C1) (17-21)

DTC P0616 : Starter Cut Relay Diagnosis Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0616 Starter Cut Relay Diagnosis Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0616 Starter Cut Relay Diagnosis Circuit Low Voltage Is DTC P0616 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit and starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0616 Starter Cut Relay Diagnosis Circuit Low Voltage

Is DTC P0616 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit and starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 52 Test point 2 Body ground Is there 1.0 MΩ or more? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM . NO Repair a short in the ST RLY 1 TO 2 wire between PCM connector No. 2 terminal No. 52 and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 52

Test point 2 | Body ground

Is there 1.0 MΩ or more?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short in the ST RLY 1 TO 2 wire between PCM connector No. 2 terminal No. 52 and the relay circuit board.
````

## Chunk 6839: DTC P0616 (K20C2)

- Title: DTC P0616 (K20C2)
- Source path: `pages\7582.html`
- Chunk ID: `chunk_188a6254bce2`
- Images: none
- Duplicate sources: `pages\9169.html`, `pages\22231.html`, `pages\15272.html`

### Full Text

````text
# DTC P0616 (K20C2)

DTC P0616 : Starter Cut Relay Diagnosis Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0616 Starter Cut Relay Diagnosis Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit STARTER CUT RELAY Less than 2.2 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

STARTER CUT RELAY | Less than 2.2 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 19 Test point 2 Body ground Is there 1.0 MΩ or more? YES The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM . NO Repair a short in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 19

Test point 2 | Body ground

Is there 1.0 MΩ or more?

YES

The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.
````

## Chunk 6840: DTC P0616 (L15B7/L15BA/L15BY)

- Title: DTC P0616 (L15B7/L15BA/L15BY)
- Source path: `pages\7583.html`
- Chunk ID: `chunk_481a8ca39ccf`
- Images: none
- Duplicate sources: `pages\9170.html`, `pages\22232.html`, `pages\15273.html`

### Full Text

````text
# DTC P0616 (L15B7/L15BA/L15BY)

DTC P0616 : Starter Cut Relay Diagnosis Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0616 Starter Cut Relay Diagnosis Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit STARTER CUT RELAY Less than 2.2 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

STARTER CUT RELAY | Less than 2.2 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 19 Test point 2 Body ground Is there 1.0 MΩ or more? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM . NO Repair a short in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 19

Test point 2 | Body ground

Is there 1.0 MΩ or more?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0616 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.
````

## Chunk 6841: DTC P0617 (K20C1) (17-21)

- Title: DTC P0617 (K20C1) (17-21)
- Source path: `pages\7584.html`
- Chunk ID: `chunk_0a3a2b4b146b`
- Images: none
- Duplicate sources: `pages\9171.html`, `pages\22233.html`, `pages\14857.html`

### Full Text

````text
# DTC P0617 (K20C1) (17-21)

DTC P0617 : Starter Cut Relay Diagnosis Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0617 Starter Cut Relay Diagnosis Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0617 Starter Cut Relay Diagnosis Circuit High Voltage Is DTC P0617 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit and starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0617 Starter Cut Relay Diagnosis Circuit High Voltage

Is DTC P0617 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit and starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 52 Test point 2 Body ground Is there about 0.1 V or less? YES The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST RLY 1 TO 2 wire between PCM connector No. 2 terminal No. 52 and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 52

Test point 2 | Body ground

Is there about 0.1 V or less?

YES

The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST RLY 1 TO 2 wire between PCM connector No. 2 terminal No. 52 and the relay circuit board.
````

## Chunk 6842: DTC P0617 (K20C2)

- Title: DTC P0617 (K20C2)
- Source path: `pages\7585.html`
- Chunk ID: `chunk_1bf58e780c7b`
- Images: none
- Duplicate sources: `pages\9172.html`, `pages\22234.html`, `pages\15274.html`

### Full Text

````text
# DTC P0617 (K20C2)

DTC P0617 : Starter Cut Relay Diagnosis Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0617 Starter Cut Relay Diagnosis Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit STARTER CUT RELAY More than 3.2 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

STARTER CUT RELAY | More than 3.2 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 19 Test point 2 Body ground Is there about 0.1 V or less? YES The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 19

Test point 2 | Body ground

Is there about 0.1 V or less?

YES

The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.
````

## Chunk 6843: DTC P0617 (L15B7/L15BA/L15BY)

- Title: DTC P0617 (L15B7/L15BA/L15BY)
- Source path: `pages\7586.html`
- Chunk ID: `chunk_4b5fc11f87a5`
- Images: none
- Duplicate sources: `pages\9173.html`, `pages\22235.html`, `pages\15275.html`

### Full Text

````text
# DTC P0617 (L15B7/L15BA/L15BY)

DTC P0617 : Starter Cut Relay Diagnosis Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0617 Starter Cut Relay Diagnosis Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit STARTER CUT RELAY More than 3.2 V Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

STARTER CUT RELAY | More than 3.2 | V

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST RLY 1 TO 2 line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 19 Test point 2 Body ground Is there about 0.1 V or less? YES The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 19

Test point 2 | Body ground

Is there about 0.1 V or less?

YES

The ST RLY 1 TO 2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0617 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST RLY 1 TO 2 wire between the PCM (A19) and the relay circuit board.
````

## Chunk 6844: DTC P061B (K20C2)

- Title: DTC P061B (K20C2)
- Source path: `pages\7587.html`
- Chunk ID: `chunk_935fabbd5fa2`
- Images: none
- Duplicate sources: `pages\9174.html`, `pages\22236.html`, `pages\15276.html`

### Full Text

````text
# DTC P061B (K20C2)

DTC P061B : PCM Internal Malfunction (Torque Calculation)

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P061B PCM Internal Malfunction (Torque Calculation)

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters: ENGINE SPEED APP SENSOR On-board Snapshot -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P061B PCM Internal Malfunction (Torque Calculation) Is DTC P061B indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P061B goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the APP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameters:

- ENGINE SPEED

- APP SENSOR

On-board Snapshot

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P061B PCM Internal Malfunction (Torque Calculation)

Is DTC P061B indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P061B goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the APP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6845: DTC P061B (L15B7/L15BA/L15BY)

- Title: DTC P061B (L15B7/L15BA/L15BY)
- Source path: `pages\7588.html`
- Chunk ID: `chunk_b78167de06d5`
- Images: none
- Duplicate sources: `pages\9175.html`, `pages\22237.html`, `pages\15277.html`

### Full Text

````text
# DTC P061B (L15B7/L15BA/L15BY)

DTC P061B : PCM Internal Malfunction (Torque Calculation)

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P061B PCM Internal Malfunction (Torque Calculation)

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Start the engine, then let it idle. Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameter. Engine speed APP Sensor On-board Snapshot -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P061B PCM Internal Malfunction (Torque Calculation) Is DTC P061B indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P061B goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Start the engine, then let it idle.

Test-drive the vehicle for several minutes in the range of these recorded on-board snapshot parameter.

- Engine speed

- APP Sensor

On-board Snapshot

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P061B PCM Internal Malfunction (Torque Calculation)

Is DTC P061B indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P061B goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6846: DTC P062B (L15B7/L15BA/L15BY)

- Title: DTC P062B (L15B7/L15BA/L15BY)
- Source path: `pages\7589.html`
- Chunk ID: `chunk_e15d541edcca`
- Images: none
- Duplicate sources: `pages\9176.html`, `pages\22238.html`, `pages\15278.html`

### Full Text

````text
# DTC P062B (L15B7/L15BA/L15BY)

DTC P062B : PCM Internal Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P062B PCM Internal Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Start the engine. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P062B PCM Internal Circuit Malfunction Is DTC P062B indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062B goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Start the engine.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P062B PCM Internal Circuit Malfunction

Is DTC P062B indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062B goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 6847: DTC P062F (K20C2)

- Title: DTC P062F (K20C2)
- Source path: `pages\7590.html`
- Chunk ID: `chunk_d26aad36a718`
- Images: none
- Duplicate sources: `pages\9177.html`, `pages\22239.html`, `pages\15279.html`

### Full Text

````text
# DTC P062F (K20C2)

DTC P062F : PCM Internal Control Module Keep Alive Memory (KAM) Error

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P062F PCM Internal Control Module Keep Alive Memory (KAM) Error Is DTC P062F indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062F goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

Is DTC P062F indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062F goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6848: DTC P062F (L15B7/L15BA/L15BY)

- Title: DTC P062F (L15B7/L15BA/L15BY)
- Source path: `pages\7591.html`
- Chunk ID: `chunk_f94f075e382a`
- Images: none
- Duplicate sources: `pages\9178.html`, `pages\22240.html`, `pages\15280.html`

### Full Text

````text
# DTC P062F (L15B7/L15BA/L15BY)

DTC P062F : PCM Internal Control Module Keep Alive Memory (KAM) Error

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P062F PCM Internal Control Module Keep Alive Memory (KAM) Error Is DTC P062F indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062F goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

Is DTC P062F indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P062F goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6849: DTC P0630 (K20C1) (17-21)

- Title: DTC P0630 (K20C1) (17-21)
- Source path: `pages\7592.html`
- Chunk ID: `chunk_6ebbd27523fc`
- Images: none
- Duplicate sources: `pages\9179.html`, `pages\22241.html`, `pages\14858.html`

### Full Text

````text
# DTC P0630 (K20C1) (17-21)

DTC P0630 : VIN Not Programmed or Mismatch

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored only when the PCM does not have the VIN information of the vehicle. Use the HDS to input the missing VIN information.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

DTC (PGM-FI)

- VIN check -1. Turn the vehicle to the ON mode. -2. Check the VIN with the HDS. Does the HDS show the vehicle's VIN? YES Go to step 3. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the VIN with the HDS.

Does the HDS show the vehicle's VIN?

YES

Go to step 3.

NO

Go to step 2.

- VIN check (rewrite) -1. Input the correct VIN to the PCM with the HDS. Does the HDS show COMPLETE? YES Go to step 3. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM .

-1. Input the correct VIN to the PCM with the HDS.

Does the HDS show COMPLETE?

YES

Go to step 3.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM .

- PCM check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Turn the vehicle to the ON mode, and wait 5 seconds. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0630 VIN Not Programmed or Mismatch Is DTC P0630 indicated? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Turn the vehicle to the ON mode, and wait 5 seconds.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

Is DTC P0630 indicated?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.
````

## Chunk 6850: DTC P0630 (K20C2)

- Title: DTC P0630 (K20C2)
- Source path: `pages\7593.html`
- Chunk ID: `chunk_70e1d54d8ae0`
- Images: none
- Duplicate sources: `pages\9180.html`, `pages\22242.html`, `pages\15281.html`

### Full Text

````text
# DTC P0630 (K20C2)

DTC P0630 : VIN Not Programmed or Mismatch

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored only when the PCM does not have the VIN information of the vehicle. Use the HDS to input the missing VIN information.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

DTC (PGM-FI)

- VIN check -1. Turn the vehicle to the ON mode. -2. Check the VIN with the HDS. Does the HDS show the vehicle's VIN? YES Go to step 4. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the VIN with the HDS.

Does the HDS show the vehicle's VIN?

YES

Go to step 4.

NO

Go to step 2.

- VIN check (rewrite) -1. Input the correct VIN to the PCM with the HDS. Does the HDS show COMPLETE? YES Go to step 4. NO Go to step 3.

-1. Input the correct VIN to the PCM with the HDS.

Does the HDS show COMPLETE?

YES

Go to step 4.

NO

Go to step 3.

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P062F PCM Internal Control Module Keep Alive Memory (KAM) Error Is DTC P062F indicated? YES Go to the troubleshooting for DTC P062F . NO Go to step 4.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

Is DTC P062F indicated?

YES

Go to the troubleshooting for DTC P062F .

NO

Go to step 4.

- PCM check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Turn the vehicle to the ON mode, and wait 5 seconds. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0630 VIN Not Programmed or Mismatch Is DTC P0630 indicated? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Turn the vehicle to the ON mode, and wait 5 seconds.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

Is DTC P0630 indicated?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.
````

## Chunk 6851: DTC P0630 (L15B7/L15BA/L15BY)

- Title: DTC P0630 (L15B7/L15BA/L15BY)
- Source path: `pages\7594.html`
- Chunk ID: `chunk_ac9a4a0cd4da`
- Images: none
- Duplicate sources: `pages\9181.html`, `pages\22243.html`, `pages\15282.html`

### Full Text

````text
# DTC P0630 (L15B7/L15BA/L15BY)

DTC P0630 : VIN Not Programmed or Mismatch

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored only when the PCM does not have the VIN information of the vehicle. Use the HDS to input the missing VIN information.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

DTC (PGM-FI)

- VIN check -1. Turn the vehicle to the ON mode. -2. Check the VIN with the HDS. Does the HDS show the vehicle's VIN? YES Go to step 4. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the VIN with the HDS.

Does the HDS show the vehicle's VIN?

YES

Go to step 4.

NO

Go to step 2.

- VIN check (rewrite) -1. Input the correct VIN to the PCM with the HDS. Does the HDS show COMPLETE? YES Go to step 4. NO Go to step 3.

-1. Input the correct VIN to the PCM with the HDS.

Does the HDS show COMPLETE?

YES

Go to step 4.

NO

Go to step 3.

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P062F PCM Internal Control Module Keep Alive Memory (KAM) Error Is DTC P062F indicated? YES Go to the troubleshooting for DTC P062F . NO Go to step 4.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P062F PCM Internal Control Module Keep Alive Memory (KAM) Error

Is DTC P062F indicated?

YES

Go to the troubleshooting for DTC P062F .

NO

Go to step 4.

- PCM check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Turn the vehicle to the ON mode, and wait 5 seconds. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0630 VIN Not Programmed or Mismatch Is DTC P0630 indicated? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Turn the vehicle to the ON mode, and wait 5 seconds.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0630 VIN Not Programmed or Mismatch

Is DTC P0630 indicated?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0630 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time. If any other Pending or Confirmed DTCs are indicated, go to the indicated DTC's troubleshooting.
````

## Chunk 6852: DTC P0641 (K20C1) (17-21)

- Title: DTC P0641 (K20C1) (17-21)
- Source path: `pages\7595.html`
- Chunk ID: `chunk_500e08648ba0`
- Images: none
- Duplicate sources: `pages\9182.html`, `pages\22244.html`, `pages\14859.html`

### Full Text

````text
# DTC P0641 (K20C1) (17-21)

DTC P0641 : Sensor Reference Voltage A Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CKP sensor CMP sensor A CMP sensor B Output shaft (countershaft) speed sensor Fuel rail pressure sensor MAF sensor/IAT sensor 1 MAP sensor/IAT sensor 2 Rocker arm oil pressure sensor Turbocharger boost sensor Turbocharger Throttle body APP sensor Input shaft (mainshaft) speed sensor Neutral position sensor A/C pressure sensor FTP sensor (KA/KC)

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CKP sensor

- CMP sensor A

- CMP sensor B

- Output shaft (countershaft) speed sensor

- Fuel rail pressure sensor

- MAF sensor/IAT sensor 1

- MAP sensor/IAT sensor 2

- Rocker arm oil pressure sensor

- Turbocharger boost sensor

- Turbocharger

- Throttle body

- APP sensor

- Input shaft (mainshaft) speed sensor

- Neutral position sensor

- A/C pressure sensor

- FTP sensor (KA/KC)

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CKP sensor 3P connector CMP sensor A 3P connector CMP sensor B 3P connector Output shaft (countershaft) speed sensor 3P connector Fuel rail pressure sensor 5P connector MAF sensor/IAT sensor 1 5P connector MAP sensor/IAT sensor 2 4P connector Rocker arm oil pressure sensor 3P connector Turbocharger boost sensor 3P connector Turbocharger 5P connector Throttle body 6P connector APP sensor 6P connector Input shaft (mainshaft) speed sensor 3P connector Neutral position sensor 4P connector A/C pressure sensor 3P connector FTP sensor 3P connector (KA/KC) -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CKP sensor 3P connector

CMP sensor A 3P connector

CMP sensor B 3P connector

Output shaft (countershaft) speed sensor 3P connector

Fuel rail pressure sensor 5P connector

MAF sensor/IAT sensor 1 5P connector

MAP sensor/IAT sensor 2 4P connector

Rocker arm oil pressure sensor 3P connector

Turbocharger boost sensor 3P connector

Turbocharger 5P connector

Throttle body 6P connector

APP sensor 6P connector

Input shaft (mainshaft) speed sensor 3P connector

Neutral position sensor 4P connector

A/C pressure sensor 3P connector

FTP sensor 3P connector (KA/KC)

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Go to step 4.

NO

Go to step 3.
````

## Chunk 6853: DTC P0641 (K20C1) (17-21)

- Title: DTC P0641 (K20C1) (17-21)
- Source path: `pages\7595.html`
- Chunk ID: `chunk_c82001dbe455`
- Images: none
- Duplicate sources: `pages\9182.html`, `pages\22244.html`, `pages\14859.html`

### Full Text

````text
MP sensor B 3P connector

Output shaft (countershaft) speed sensor 3P connector

Fuel rail pressure sensor 5P connector

MAF sensor/IAT sensor 1 5P connector

MAP sensor/IAT sensor 2 4P connector

Rocker arm oil pressure sensor 3P connector

Turbocharger boost sensor 3P connector

Turbocharger 5P connector

Throttle body 6P connector

APP sensor 6P connector

Input shaft (mainshaft) speed sensor 3P connector

Neutral position sensor 4P connector

A/C pressure sensor 3P connector

FTP sensor 3P connector (KA/KC)

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CKP sensor CMP sensor A CMP sensor B Output shaft (countershaft) speed sensor Fuel rail pressure sensor MAF sensor/IAT sensor 1 MAP sensor/IAT sensor 2 Rocker arm oil pressure sensor Turbocharger boost sensor Turbocharger Throttle body APP sensor Input shaft (mainshaft) speed sensor Neutral position sensor A/C pressure sensor FTP sensor (KA/KC) DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CKP sensor CMP sensor A CMP sensor B Output shaft (countershaft) speed sensor Fuel rail pressure sensor MAF sensor/IAT sensor 1 MAP sensor/IAT sensor 2 Rocker arm oil pressure sensor Turbocharger boost sensor Turbocharger Throttle body APP sensor Input shaft (mainshaft) speed sensor Neutral position sensor A/C pressure sensor FTP sensor (KA/KC)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CKP sensor

- CMP sensor A

- CMP sensor B

- Output shaft (countershaft) speed sensor

- Fuel rail pressure sensor

- MAF sensor/IAT sensor 1

- MAP sensor/IAT sensor 2

- Rocker arm oil pressure sensor

- Turbocharger boost sensor

- Turbocharger

- Throttle body

- APP sensor

- Input shaft (mainshaft) speed sensor

- Neutral position sensor

- A/C pressure sensor

- FTP sensor (KA/KC)

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CKP sensor

- CMP sensor A

- CMP sensor B

- Output shaft (countershaft) speed sensor

- Fuel rail pressure sensor

- MAF sensor/IAT sensor 1

- MAP sensor/IAT sensor 2

- Rocker arm oil pressure sensor

- Turbocharger boost sensor

- Turbocharger

- Throttle body

- APP sensor

- Input shaft (mainshaft) speed sensor

- Neutral position sensor

- A/C pressure sensor

- FTP sensor (KA/KC)

- Shorted wire check (VCC lines) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector No. 1 (96P) PCM connector No. 2 (58P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode CKP sensor 3P connector: disconnected CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Output shaft (countershaft) speed sensor 3P connector: disconnected Fuel rail pressure sensor 5P connector: disconnected MAF sensor/IAT sensor 1 5P connector: disconnected MAP sensor/IAT sensor 2 4P connector: disconnected Rocker arm oil pressure sensor 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected Input shaft (mainshaft) speed sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (KA/KC): disconnected PCM connector No. 1 (96P): disconnected PCM connector No. 2 (58P): disconnected Connector Terminal PCM connector No. 1 (96P) No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83 PCM connector No. 2 (58P) No. 41, No. 46, No. 55, and No.
````

## Chunk 6854: DTC P0641 (K20C1) (17-21)

- Title: DTC P0641 (K20C1) (17-21)
- Source path: `pages\7595.html`
- Chunk ID: `chunk_0555250ea1a4`
- Images: none
- Duplicate sources: `pages\9182.html`, `pages\22244.html`, `pages\14859.html`

### Full Text

````text
T sensor 1 5P connector: disconnected MAP sensor/IAT sensor 2 4P connector: disconnected Rocker arm oil pressure sensor 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected Input shaft (mainshaft) speed sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (KA/KC): disconnected PCM connector No. 1 (96P): disconnected PCM connector No. 2 (58P): disconnected Connector Terminal PCM connector No. 1 (96P) No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83 PCM connector No. 2 (58P) No. 41, No. 46, No. 55, and No. 58 Is there continuity? YES Repair a short in the VCC wire (s) between PCM connector No. 1 terminal (s) (No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and/or No. 83), PCM connector No. 2 terminal (s) (No. 41, No. 46, No. 55, and/or No. 58) and each part that was disconnected in step 2. NO The VCC wires are not shorted to ground. Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector No. 1 (96P)

PCM connector No. 2 (58P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

CKP sensor 3P connector: disconnected

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector: disconnected

Fuel rail pressure sensor 5P connector: disconnected

MAF sensor/IAT sensor 1 5P connector: disconnected

MAP sensor/IAT sensor 2 4P connector: disconnected

Rocker arm oil pressure sensor 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

Input shaft (mainshaft) speed sensor 3P connector: disconnected

Neutral position sensor 4P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector (KA/KC): disconnected

PCM connector No. 1 (96P): disconnected

PCM connector No. 2 (58P): disconnected

Connector | Terminal

PCM connector No. 1 (96P) | No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83

PCM connector No. 2 (58P) | No. 41, No. 46, No. 55, and No. 58

Is there continuity?

YES

Repair a short in the VCC wire (s) between PCM connector No. 1 terminal (s) (No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and/or No. 83), PCM connector No. 2 terminal (s) (No. 41, No. 46, No. 55, and/or No. 58) and each part that was disconnected in step 2.

NO

The VCC wires are not shorted to ground. Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CKP sensor 3P connector: disconnected CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Output shaft (countershaft) speed sensor 3P connector: disconnected Fuel rail pressure sensor 5P connector: disconnected MAF sensor/IAT sensor 1 5P connector: disconnected MAP sensor/IAT sensor 2 4P connector: disconnected Rocker arm oil pressure sensor 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected Input shaft (mainshaft) speed sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (KA/KC): disconnected PCM connector No. 1 (96P): disconnected PCM connector No. 2 (58P): disconnected Connector Terminal PCM connector No. 1 (96P) No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83 PCM connector No. 2 (58P) No. 41, No. 46, No. 55, and No. 58 Is there any voltage? YES Repair a short to power in the VCC wire (s) between PCM connector No. 1 terminals (No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and/or No. 83), PCM connector No. 2 terminals (No. 41, No. 46, No. 55, and/or No.
````

## Chunk 6855: DTC P0641 (K20C1) (17-21)

- Title: DTC P0641 (K20C1) (17-21)
- Source path: `pages\7595.html`
- Chunk ID: `chunk_ecc381827675`
- Images: none
- Duplicate sources: `pages\9182.html`, `pages\22244.html`, `pages\14859.html`

### Full Text

````text
nected APP sensor 6P connector: disconnected Input shaft (mainshaft) speed sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (KA/KC): disconnected PCM connector No. 1 (96P): disconnected PCM connector No. 2 (58P): disconnected Connector Terminal PCM connector No. 1 (96P) No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83 PCM connector No. 2 (58P) No. 41, No. 46, No. 55, and No. 58 Is there any voltage? YES Repair a short to power in the VCC wire (s) between PCM connector No. 1 terminals (No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and/or No. 83), PCM connector No. 2 terminals (No. 41, No. 46, No. 55, and/or No. 58) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CKP sensor 3P connector: disconnected

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector: disconnected

Fuel rail pressure sensor 5P connector: disconnected

MAF sensor/IAT sensor 1 5P connector: disconnected

MAP sensor/IAT sensor 2 4P connector: disconnected

Rocker arm oil pressure sensor 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

Input shaft (mainshaft) speed sensor 3P connector: disconnected

Neutral position sensor 4P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector (KA/KC): disconnected

PCM connector No. 1 (96P): disconnected

PCM connector No. 2 (58P): disconnected

Connector | Terminal

PCM connector No. 1 (96P) | No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and No. 83

PCM connector No. 2 (58P) | No. 41, No. 46, No. 55, and No. 58

Is there any voltage?

YES

Repair a short to power in the VCC wire (s) between PCM connector No. 1 terminals (No. 61, No. 62, No. 63, No. 64, No. 65, No. 66, No. 67, No. 80, No. 81, No. 82, and/or No. 83), PCM connector No. 2 terminals (No. 41, No. 46, No. 55, and/or No. 58) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6856: DTC P0641 (K20C2)

- Title: DTC P0641 (K20C2)
- Source path: `pages\7596.html`
- Chunk ID: `chunk_b5970bcc1d71`
- Images: none
- Duplicate sources: `pages\9183.html`, `pages\22245.html`, `pages\15283.html`

### Full Text

````text
# DTC P0641 (K20C2)

DTC P0641 : Sensor Reference Voltage A Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CKP sensor MAP sensor Output shaft (countershaft) speed sensor (M/T) Throttle body APP sensor

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CKP sensor

- MAP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Throttle body

- APP sensor

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CKP sensor 3P connector MAP sensor 3P connector Output shaft (countershaft) speed sensor 3P connector (M/T) Throttle body 6P connector APP sensor 6P connector -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CKP sensor 3P connector

MAP sensor 3P connector

Output shaft (countershaft) speed sensor 3P connector (M/T)

Throttle body 6P connector

APP sensor 6P connector

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CKP sensor MAP sensor Output shaft (countershaft) speed sensor (M/T) Throttle body APP sensor DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CKP sensor MAP sensor Output shaft (countershaft) speed sensor (M/T) Throttle body APP sensor

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CKP sensor

- MAP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Throttle body

- APP sensor

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CKP sensor

- MAP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Throttle body

- APP sensor

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually.
````

## Chunk 6857: DTC P0641 (K20C2)

- Title: DTC P0641 (K20C2)
- Source path: `pages\7596.html`
- Chunk ID: `chunk_970ffddc3346`
- Images: none
- Duplicate sources: `pages\9183.html`, `pages\22245.html`, `pages\15283.html`

### Full Text

````text
- Output shaft (countershaft) speed sensor (M/T)

- Throttle body

- APP sensor

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CKP sensor

- MAP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Throttle body

- APP sensor

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode CKP sensor 3P connector: disconnected MAP sensor 3P connector: disconnected Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 45 PCM connector E (80P) No. 70 and No. 75 Is there continuity? YES Repair a short to ground in the VCC wire (s) between the PCM (A45, E70, E75) and each part that was disconnected in step 2. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

PCM connector E (80P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

CKP sensor 3P connector: disconnected

MAP sensor 3P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 45

PCM connector E (80P) | No. 70 and No. 75

Is there continuity?

YES

Repair a short to ground in the VCC wire (s) between the PCM (A45, E70, E75) and each part that was disconnected in step 2.

NO

Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CKP sensor 3P connector: disconnected MAP sensor 3P connector: disconnected Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 45 PCM connector E (80P) No. 70 and No. 75 Is there any voltage? YES Repair a short to power in the VCC wire (s) between the PCM (A45, E70, E75) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CKP sensor 3P connector: disconnected

MAP sensor 3P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 45

PCM connector E (80P) | No. 70 and No. 75

Is there any voltage?

YES

Repair a short to power in the VCC wire (s) between the PCM (A45, E70, E75) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6858: DTC P0641 (L15B7/L15BA/L15BY)

- Title: DTC P0641 (L15B7/L15BA/L15BY)
- Source path: `pages\7597.html`
- Chunk ID: `chunk_ee973409d1c5`
- Images: none
- Duplicate sources: `pages\9184.html`, `pages\22246.html`, `pages\15284.html`

### Full Text

````text
# DTC P0641 (L15B7/L15BA/L15BY)

DTC P0641 : Sensor Reference Voltage A Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CKP sensor MAP sensor Fuel rail pressure sensor Throttle body APP sensor Output shaft (countershaft) speed sensor (M/T)

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CKP sensor

- MAP sensor

- Fuel rail pressure sensor

- Throttle body

- APP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CKP sensor 3P connector MAP sensor 3P connector Fuel rail pressure sensor 3P connector Throttle body 6P connector APP sensor 6P connector Output shaft (countershaft) speed sensor 3P connector (M/T) -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CKP sensor 3P connector

MAP sensor 3P connector

Fuel rail pressure sensor 3P connector

Throttle body 6P connector

APP sensor 6P connector

Output shaft (countershaft) speed sensor 3P connector (M/T)

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CKP sensor MAP sensor Fuel rail pressure sensor Throttle body APP sensor Output shaft (countershaft) speed sensor (M/T) DTC Description Confirmed DTC Pending DTC P0641 Sensor Reference Voltage A Malfunction Is DTC P0641 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CKP sensor MAP sensor Fuel rail pressure sensor Throttle body APP sensor Output shaft (countershaft) speed sensor (M/T)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CKP sensor

- MAP sensor

- Fuel rail pressure sensor

- Throttle body

- APP sensor

- Output shaft (countershaft) speed sensor (M/T)

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CKP sensor

- MAP sensor

- Fuel rail pressure sensor

- Throttle body

- APP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually.
````

## Chunk 6859: DTC P0641 (L15B7/L15BA/L15BY)

- Title: DTC P0641 (L15B7/L15BA/L15BY)
- Source path: `pages\7597.html`
- Chunk ID: `chunk_e0c298102264`
- Images: none
- Duplicate sources: `pages\9184.html`, `pages\22246.html`, `pages\15284.html`

### Full Text

````text
- Output shaft (countershaft) speed sensor (M/T)

DTC Description | Confirmed DTC | Pending DTC

P0641 Sensor Reference Voltage A Malfunction

Is DTC P0641 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CKP sensor

- MAP sensor

- Fuel rail pressure sensor

- Throttle body

- APP sensor

- Output shaft (countershaft) speed sensor (M/T)

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode CKP sensor 3P connector: disconnected MAP sensor 3P connector: disconnected Fuel rail pressure sensor 3P connector: disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 45 PCM connector E (80P) No. 70 and No. 75 Is there continuity? YES Repair a short to ground in the VCC wire between the PCM (A45, E70, E75) and each part that was disconnected in step 2. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

PCM connector E (80P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

CKP sensor 3P connector: disconnected

MAP sensor 3P connector: disconnected

Fuel rail pressure sensor 3P connector: disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 45

PCM connector E (80P) | No. 70 and No. 75

Is there continuity?

YES

Repair a short to ground in the VCC wire between the PCM (A45, E70, E75) and each part that was disconnected in step 2.

NO

Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CKP sensor 3P connector: disconnected MAP sensor 3P connector: disconnected Fuel rail pressure sensor 3P connector: disconnected Throttle body 6P connector: disconnected APP sensor 6P connector: disconnected Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 45 PCM connector E (80P) No. 70 and No. 75 Is there any voltage? YES Repair a short to power in the VCC wire between the PCM (A45, E70, E75) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CKP sensor 3P connector: disconnected

MAP sensor 3P connector: disconnected

Fuel rail pressure sensor 3P connector: disconnected

Throttle body 6P connector: disconnected

APP sensor 6P connector: disconnected

Output shaft (countershaft) speed sensor 3P connector (M/T): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 45

PCM connector E (80P) | No. 70 and No. 75

Is there any voltage?

YES

Repair a short to power in the VCC wire between the PCM (A45, E70, E75) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0641 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6860: DTC P0651 (K20C2)

- Title: DTC P0651 (K20C2)
- Source path: `pages\7598.html`
- Chunk ID: `chunk_cbfdfb20734e`
- Images: none
- Duplicate sources: `pages\9185.html`, `pages\22247.html`, `pages\15285.html`

### Full Text

````text
# DTC P0651 (K20C2)

DTC P0651 : Sensor Reference Voltage B Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CMP sensor A CMP sensor B MAF sensor/IAT sensor Neutral position sensor (M/T) APP sensor A/C pressure sensor (with A/C) FTP sensor (USA and Canada models)

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CMP sensor A

- CMP sensor B

- MAF sensor/IAT sensor

- Neutral position sensor (M/T)

- APP sensor

- A/C pressure sensor (with A/C)

- FTP sensor (USA and Canada models)

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CMP sensor A 3P connector CMP sensor B 3P connector MAF sensor/IAT sensor 4P connector Neutral position sensor 4P connector (M/T) APP sensor 6P connector A/C pressure sensor 3P connector (with A/C) FTP sensor 3P connector (USA and Canada models) -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CMP sensor A 3P connector

CMP sensor B 3P connector

MAF sensor/IAT sensor 4P connector

Neutral position sensor 4P connector (M/T)

APP sensor 6P connector

A/C pressure sensor 3P connector (with A/C)

FTP sensor 3P connector (USA and Canada models)

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CMP sensor A CMP sensor B MAF sensor/IAT sensor Neutral position sensor (M/T) APP sensor A/C pressure sensor (with A/C) FTP sensor (USA and Canada models) DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CMP sensor A CMP sensor B MAF sensor/IAT sensor Neutral position sensor (M/T) APP sensor A/C pressure sensor (with A/C) FTP sensor (USA and Canada models)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- MAF sensor/IAT sensor

- Neutral position sensor (M/T)

- APP sensor

- A/C pressure sensor (with A/C)

- FTP sensor (USA and Canada models)

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- MAF sensor/IAT sensor

- Neutral position sensor (M/T)

- APP sensor

- A/C pressure sensor (with A/C)

- FTP sensor (USA and Canada models)

- Shorted wire check (VCC lines to ground) -1.
````

## Chunk 6861: DTC P0651 (K20C2)

- Title: DTC P0651 (K20C2)
- Source path: `pages\7598.html`
- Chunk ID: `chunk_faf036480e40`
- Images: none
- Duplicate sources: `pages\9185.html`, `pages\22247.html`, `pages\15285.html`

### Full Text

````text
ada models)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- MAF sensor/IAT sensor

- Neutral position sensor (M/T)

- APP sensor

- A/C pressure sensor (with A/C)

- FTP sensor (USA and Canada models)

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- MAF sensor/IAT sensor

- Neutral position sensor (M/T)

- APP sensor

- A/C pressure sensor (with A/C)

- FTP sensor (USA and Canada models)

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected MAF sensor/IAT sensor 4P connector: disconnected Neutral position sensor 4P connector (M/T): disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector (with A/C): disconnected FTP sensor 3P connector (USA and Canada models): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there continuity? YES Repair a short to ground in the VCC wire (s) between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

PCM connector E (80P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

MAF sensor/IAT sensor 4P connector: disconnected

Neutral position sensor 4P connector (M/T): disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector (with A/C): disconnected

FTP sensor 3P connector (USA and Canada models): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there continuity?

YES

Repair a short to ground in the VCC wire (s) between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected MAF sensor/IAT sensor 4P connector: disconnected Neutral position sensor 4P connector (M/T): disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector (with A/C): disconnected FTP sensor 3P connector (USA and Canada models): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there any voltage? YES Repair a short to power in the VCC wire (s) between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

MAF sensor/IAT sensor 4P connector: disconnected

Neutral position sensor 4P connector (M/T): disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector (with A/C): disconnected

FTP sensor 3P connector (USA and Canada models): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal
````

## Chunk 6862: DTC P0651 (K20C2)

- Title: DTC P0651 (K20C2)
- Source path: `pages\7598.html`
- Chunk ID: `chunk_c38e34f3e36d`
- Images: none
- Duplicate sources: `pages\9185.html`, `pages\22247.html`, `pages\15285.html`

### Full Text

````text
vice information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

MAF sensor/IAT sensor 4P connector: disconnected

Neutral position sensor 4P connector (M/T): disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector (with A/C): disconnected

FTP sensor 3P connector (USA and Canada models): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there any voltage?

YES

Repair a short to power in the VCC wire (s) between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6863: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7599.html`
- Chunk ID: `chunk_1c0d51cec61a`
- Images: none
- Duplicate sources: `pages\9186.html`, `pages\22248.html`, `pages\15286.html`

### Full Text

````text
# DTC P0651 (L15B7 (except Si)/L15BA/L15BY)

DTC P0651 : Sensor Reference Voltage B Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger APP sensor A/C pressure sensor FTP sensor (USA and Canada models) Neutral position sensor (M/T)

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- APP sensor

- A/C pressure sensor

- FTP sensor (USA and Canada models)

- Neutral position sensor (M/T)

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CMP sensor A 3P connector CMP sensor B 3P connector Turbocharger boost sensor 3P connector Turbocharger 5P connector APP sensor 6P connector A/C pressure sensor 3P connector FTP sensor 3P connector (USA and Canada models) Neutral position sensor 4P connector (M/T) -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CMP sensor A 3P connector

CMP sensor B 3P connector

Turbocharger boost sensor 3P connector

Turbocharger 5P connector

APP sensor 6P connector

A/C pressure sensor 3P connector

FTP sensor 3P connector (USA and Canada models)

Neutral position sensor 4P connector (M/T)

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger APP sensor A/C pressure sensor FTP sensor (USA and Canada models) Neutral position sensor (M/T) DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger APP sensor A/C pressure sensor FTP sensor (USA and Canada models) Neutral position sensor (M/T)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- APP sensor

- A/C pressure sensor

- FTP sensor (USA and Canada models)

- Neutral position sensor (M/T)

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- APP sensor

- A/C pressure sensor
````

## Chunk 6864: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7599.html`
- Chunk ID: `chunk_8aefdcd11603`
- Images: none
- Duplicate sources: `pages\9186.html`, `pages\22248.html`, `pages\15286.html`

### Full Text

````text
or Turbocharger APP sensor A/C pressure sensor FTP sensor (USA and Canada models) Neutral position sensor (M/T)

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- APP sensor

- A/C pressure sensor

- FTP sensor (USA and Canada models)

- Neutral position sensor (M/T)

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- APP sensor

- A/C pressure sensor

- FTP sensor (USA and Canada models)

- Neutral position sensor (M/T)

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle OFF (LOCK) mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (USA and Canada models): disconnected Neutral position sensor 4P connector (M/T): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there continuity? YES Repair a short to ground in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

PCM connector E (80P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector (USA and Canada models): disconnected

Neutral position sensor 4P connector (M/T): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there continuity?

YES

Repair a short to ground in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector (USA and Canada models): disconnected Neutral position sensor 4P connector (M/T): disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there any voltage? YES Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

APP sensor 6P connector: disconnected
````

## Chunk 6865: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)

- Title: DTC P0651 (L15B7 (except Si)/L15BA/L15BY)
- Source path: `pages\7599.html`
- Chunk ID: `chunk_6a6c0a825884`
- Images: none
- Duplicate sources: `pages\9186.html`, `pages\22248.html`, `pages\15286.html`

### Full Text

````text
nector E (80P) No. 63 and No. 77 Is there any voltage? YES Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector (USA and Canada models): disconnected

Neutral position sensor 4P connector (M/T): disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there any voltage?

YES

Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6866: DTC P0651 (Si) (17-21)

- Title: DTC P0651 (Si) (17-21)
- Source path: `pages\7600.html`
- Chunk ID: `chunk_3a1b8c691f56`
- Images: none
- Duplicate sources: `pages\9187.html`, `pages\22249.html`, `pages\15287.html`

### Full Text

````text
# DTC P0651 (Si) (17-21)

DTC P0651 : Sensor Reference Voltage B Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger MAF sensor/IAT sensor 1 APP sensor A/C pressure sensor FTP sensor Neutral position sensor

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the PCM and these parts. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- MAF sensor/IAT sensor 1

- APP sensor

- A/C pressure sensor

- FTP sensor

- Neutral position sensor

- Determine possible failure area (VCC lines, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CMP sensor A 3P connector CMP sensor B 3P connector Turbocharger boost sensor 3P connector Turbocharger 5P connector MAF sensor/IAT sensor 1 4P connector APP sensor 6P connector A/C pressure sensor 3P connector FTP sensor 3P connector Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Clear the DTC with the HDS. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CMP sensor A 3P connector

CMP sensor B 3P connector

Turbocharger boost sensor 3P connector

Turbocharger 5P connector

MAF sensor/IAT sensor 1 4P connector

APP sensor 6P connector

A/C pressure sensor 3P connector

FTP sensor 3P connector

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Clear the DTC with the HDS.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Go to step 4.

NO

Go to step 3.

- Shorted part check: Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time: CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger MAF sensor/IAT sensor 1 APP sensor A/C pressure sensor FTP sensor Neutral position sensor DTC Description Confirmed DTC Pending DTC P0651 Sensor Reference Voltage B Malfunction Is DTC P0651 indicated? YES Replace the part that caused the DTC when it was reconnected. NO Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1. CMP sensor A CMP sensor B Turbocharger boost sensor Turbocharger MAF sensor/IAT sensor 1 APP sensor A/C pressure sensor FTP sensor Neutral position sensor

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- MAF sensor/IAT sensor 1

- APP sensor

- A/C pressure sensor

- FTP sensor

- Neutral position sensor

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- MAF sensor/IAT sensor 1

- APP sensor

- A/C pressure sensor

- FTP sensor
````

## Chunk 6867: DTC P0651 (Si) (17-21)

- Title: DTC P0651 (Si) (17-21)
- Source path: `pages\7600.html`
- Chunk ID: `chunk_c1d28a45789a`
- Images: none
- Duplicate sources: `pages\9187.html`, `pages\22249.html`, `pages\15287.html`

### Full Text

````text
ensor 1 APP sensor A/C pressure sensor FTP sensor Neutral position sensor

Check for Pending or Confirmed DTCs with the HDS while reconnecting these parts, one at a time:

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- MAF sensor/IAT sensor 1

- APP sensor

- A/C pressure sensor

- FTP sensor

- Neutral position sensor

DTC Description | Confirmed DTC | Pending DTC

P0651 Sensor Reference Voltage B Malfunction

Is DTC P0651 indicated?

YES

Replace the part that caused the DTC when it was reconnected.

NO

Check for poor connections or loose terminals at the PCM and the following parts, then go to step 1.

- CMP sensor A

- CMP sensor B

- Turbocharger boost sensor

- Turbocharger

- MAF sensor/IAT sensor 1

- APP sensor

- A/C pressure sensor

- FTP sensor

- Neutral position sensor

- Shorted wire check (VCC lines to ground) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) PCM connector E (80P) -4. Check for continuity between these test points and body ground individually. Test condition Vehicle ON mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected MAF sensor/IAT sensor 1 4P connector: disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there continuity? YES Repair a short to ground in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

PCM connector E (80P)

-4. Check for continuity between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

MAF sensor/IAT sensor 1 4P connector: disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector: disconnected

Neutral position sensor 4P connector: disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there continuity?

YES

Repair a short to ground in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

Go to step 5.

- Shorted wire check (VCC lines to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between these test points and body ground individually. Test condition Vehicle ON mode CMP sensor A 3P connector: disconnected CMP sensor B 3P connector: disconnected Turbocharger boost sensor 3P connector: disconnected Turbocharger 5P connector: disconnected MAF sensor/IAT sensor 1 4P connector: disconnected APP sensor 6P connector: disconnected A/C pressure sensor 3P connector: disconnected FTP sensor 3P connector: disconnected Neutral position sensor 4P connector: disconnected PCM connector A (50P): disconnected PCM connector E (80P): disconnected Connector Terminal PCM connector A (50P) No. 44 PCM connector E (80P) No. 63 and No. 77 Is there any voltage? YES Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

MAF sensor/IAT sensor 1 4P connector: disconnected
````

## Chunk 6868: DTC P0651 (Si) (17-21)

- Title: DTC P0651 (Si) (17-21)
- Source path: `pages\7600.html`
- Chunk ID: `chunk_3eb2782cd399`
- Images: none
- Duplicate sources: `pages\9187.html`, `pages\22249.html`, `pages\15287.html`

### Full Text

````text
) No. 63 and No. 77 Is there any voltage? YES Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2. NO The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between these test points and body ground individually.

Test condition | Vehicle ON mode

CMP sensor A 3P connector: disconnected

CMP sensor B 3P connector: disconnected

Turbocharger boost sensor 3P connector: disconnected

Turbocharger 5P connector: disconnected

MAF sensor/IAT sensor 1 4P connector: disconnected

APP sensor 6P connector: disconnected

A/C pressure sensor 3P connector: disconnected

FTP sensor 3P connector: disconnected

Neutral position sensor 4P connector: disconnected

PCM connector A (50P): disconnected

PCM connector E (80P): disconnected

Connector | Terminal

PCM connector A (50P) | No. 44

PCM connector E (80P) | No. 63 and No. 77

Is there any voltage?

YES

Repair a short to power in the VCC wire between the PCM (A44, E63, E77) and each part that was disconnected in step 2.

NO

The VCC wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0651 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6869: DTC P0657 (K20C2)

- Title: DTC P0657 (K20C2)
- Source path: `pages\7601.html`
- Chunk ID: `chunk_fc372a90638e`
- Images: `images\GHH405074.jpeg`, `images\GHH405075.jpeg`, `images\GHH405076.jpeg`, `images\GHH405077.jpeg`, `images\GHH405078.jpeg`, `images\GHH405079.jpeg`
- Duplicate sources: `pages\9188.html`, `pages\22250.html`, `pages\15288.html`

### Full Text

````text
# DTC P0657 (K20C2)

DTC P0657 : PCM Power Supply Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Try to start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0657 PCM Power Supply Circuit Malfunction Is DTC P0657 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Try to start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

Is DTC P0657 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Check the following fuse. Fuse No. A7 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 7. NO Go to step 4.

-1. Check the following fuse.

Fuse | No. A7 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Go to step 4.

- Determine possible failure area (+B IGP line, others) -1. Remove the blown No. A7 (15 A) fuse from the under-hood fuse/relay box. -2. Check for continuity the between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 18 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair short in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. Also replace the No. A7 (15 A) fuse. NO Go to step 5.

-1. Remove the blown No. A7 (15 A) fuse from the under-hood fuse/relay box.

-2. Check for continuity the between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 18

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair short in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. Also replace the No. A7 (15 A) fuse.

NO

Go to step 5.

- Parts internal circuit check -1. Jump the SCS line with the HDS, and wait more than 1 minute. Check for continuity between test points 1 and 2 while disconnecting these parts or connectors, one at a time: PCM connector A (50P) PGM-FI main relay 2 Each injector 2P connector Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 17 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is continuity goes away with the part (s) removed? YES Replace the part that continuity goes away when it was disconnected. If the part is PCM, substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse. NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Check for continuity between test points 1 and 2 while disconnecting these parts or connectors, one at a time:

- PCM connector A (50P)

- PGM-FI main relay 2

- Each injector 2P connector

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 17
````

## Chunk 6870: DTC P0657 (K20C2)

- Title: DTC P0657 (K20C2)
- Source path: `pages\7601.html`
- Chunk ID: `chunk_28cd98a88ca1`
- Images: `images\GHH405074.jpeg`, `images\GHH405075.jpeg`, `images\GHH405076.jpeg`, `images\GHH405077.jpeg`, `images\GHH405078.jpeg`, `images\GHH405079.jpeg`
- Duplicate sources: `pages\9188.html`, `pages\22250.html`, `pages\15288.html`

### Full Text

````text
t board connector C (18P) No. 17 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is continuity goes away with the part (s) removed? YES Replace the part that continuity goes away when it was disconnected. If the part is PCM, substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse. NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Check for continuity between test points 1 and 2 while disconnecting these parts or connectors, one at a time:

- PCM connector A (50P)

- PGM-FI main relay 2

- Each injector 2P connector

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 17

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is continuity goes away with the part (s) removed?

YES

Replace the part that continuity goes away when it was disconnected. If the part is PCM, substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse.

NO

Go to step 6.

- Shorted wire check (FI MAIN RLY OUT line) -1. Disconnect the following parts and connectors. PCM connector A (50P) PGM-FI main relay 2 Each injector 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected PGM-FI main relay 2: disconnected Each injector 2P connector: disconnected Test point 1 Relay circuit board connector C (18P) No. 17 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair short in the FI MAIN RLY OUT line between the PCM (A8), the relay circuit board, PGM-FI main relay 2, and the injectors. Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box. NO Replace the relay circuit board . Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box.

-1. Disconnect the following parts and connectors.

PCM connector A (50P)

PGM-FI main relay 2

Each injector 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

PGM-FI main relay 2: disconnected

Each injector 2P connector: disconnected

Test point 1 | Relay circuit board connector C (18P) No. 17

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair short in the FI MAIN RLY OUT line between the PCM (A8), the relay circuit board, PGM-FI main relay 2, and the injectors. Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box.

NO

Replace the relay circuit board . Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box.

- Open wire check (+B IGP line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 18 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B IGP wire is OK. Go to step 8. NO Repair an open in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 18

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B IGP wire is OK. Go to step 8.

NO

Repair an open in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board.

- Open wire check (FI MAIN RLY CL- line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 5 Test point 2 PCM connector A (50P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI MAIN RLY CL- wire is OK. Go to step 9. NO Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.
````

## Chunk 6871: DTC P0657 (K20C2)

- Title: DTC P0657 (K20C2)
- Source path: `pages\7601.html`
- Chunk ID: `chunk_71aa51bd79f9`
- Images: `images\GHH405074.jpeg`, `images\GHH405075.jpeg`, `images\GHH405076.jpeg`, `images\GHH405077.jpeg`, `images\GHH405078.jpeg`, `images\GHH405079.jpeg`
- Duplicate sources: `pages\9188.html`, `pages\22250.html`, `pages\15288.html`

### Full Text

````text
) fuse in the under-hood fuse/relay box and the relay circuit board.

- Open wire check (FI MAIN RLY CL- line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 5 Test point 2 PCM connector A (50P) No. 5 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI MAIN RLY CL- wire is OK. Go to step 9. NO Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 5

Test point 2 | PCM connector A (50P) No. 5

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI MAIN RLY CL- wire is OK. Go to step 9.

NO

Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

- Open wire check (FI MAIN RLY OUT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 17 Test point 2 PCM connector A (50P) No. 8 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and the relay circuit board.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 17

Test point 2 | PCM connector A (50P) No. 8

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and the relay circuit board.
````

## Chunk 6872: DTC P0657 (L15B7/L15BA/L15BY)

- Title: DTC P0657 (L15B7/L15BA/L15BY)
- Source path: `pages\7602.html`
- Chunk ID: `chunk_9685b397f9ae`
- Images: `images\GHH405080.jpeg`, `images\GHH405081.jpeg`, `images\GHH405082.jpeg`, `images\GHH405083.jpeg`, `images\GHH405084.jpeg`, `images\GHH405085.jpeg`
- Duplicate sources: `pages\9189.html`, `pages\22251.html`, `pages\15289.html`

### Full Text

````text
# DTC P0657 (L15B7/L15BA/L15BY)

DTC P0657 : PCM Power Supply Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0657 PCM Power Supply Circuit Malfunction Is DTC P0657 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

Is DTC P0657 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Check the following fuse. Fuse No. A7 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 7. NO Go to step 4.

-1. Check the following fuse.

Fuse | No. A7 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Go to step 4.

- Determine possible failure area (+B IGP line, others) -1. Remove the blown No. A7 (15 A) fuse from the under-hood fuse/relay box. -2. Remove the injector relay . -3. Check for continuity the between following test points and body ground individually. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Injector relay: disconnected Connector Terminal Relay circuit board connector C (18P) No. 18 Injector relay 4P socket No. 7 Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board and the injector relay. Also replace the No. A7 (15 A) fuse. NO Go to step 5.

-1. Remove the blown No. A7 (15 A) fuse from the under-hood fuse/relay box.

-2. Remove the injector relay .

-3. Check for continuity the between following test points and body ground individually.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Injector relay: disconnected

Connector | Terminal

Relay circuit board connector C (18P) | No. 18

Injector relay 4P socket | No. 7

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board and the injector relay. Also replace the No. A7 (15 A) fuse.

NO

Go to step 5.

- Parts internal circuit check -1. Jump the SCS line with the HDS, and wait more than 1 minute. Check for continuity between test points 1 and 2 while disconnecting these parts, one at a time: PGM-FI main relay 2 PCM connector A (50P) Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 17 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Does continuity go away with the part (s) removed? YES Replace the part that continuity goes away when it was disconnected. If the part is PCM, Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse. NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.
````

## Chunk 6873: DTC P0657 (L15B7/L15BA/L15BY)

- Title: DTC P0657 (L15B7/L15BA/L15BY)
- Source path: `pages\7602.html`
- Chunk ID: `chunk_7eccb431a37b`
- Images: `images\GHH405080.jpeg`, `images\GHH405081.jpeg`, `images\GHH405082.jpeg`, `images\GHH405083.jpeg`, `images\GHH405084.jpeg`, `images\GHH405085.jpeg`
- Duplicate sources: `pages\9189.html`, `pages\22251.html`, `pages\15289.html`

### Full Text

````text
inuity between test points 1 and 2 while disconnecting these parts, one at a time: PGM-FI main relay 2 PCM connector A (50P) Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 17 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Does continuity go away with the part (s) removed? YES Replace the part that continuity goes away when it was disconnected. If the part is PCM, Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse. NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Check for continuity between test points 1 and 2 while disconnecting these parts, one at a time:

- PGM-FI main relay 2

- PCM connector A (50P)

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 17

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Does continuity go away with the part (s) removed?

YES

Replace the part that continuity goes away when it was disconnected. If the part is PCM, Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 (15 A) fuse.

NO

Go to step 6.

- Shorted wire check (FI MAIN RLY OUT line) -1. Disconnect the following connectors. PGM-FI main relay 2 PCM connector A (50P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PGM-FI main relay 2: disconnected PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 8 Test point 2 Body ground Is there continuity? YES Repair a short in the FI MAIN RLY OUT line between the relay circuit board, PGM-FI main relay 2, and the PCM (A8). Also replace the No. A7 (15 A) fuse. NO Replace the relay circuit board. Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box.

-1. Disconnect the following connectors.

PGM-FI main relay 2

PCM connector A (50P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PGM-FI main relay 2: disconnected

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 8

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI MAIN RLY OUT line between the relay circuit board, PGM-FI main relay 2, and the PCM (A8). Also replace the No. A7 (15 A) fuse.

NO

Replace the relay circuit board. Also replace the No. A7 (15 A) fuse in the under-hood fuse/relay box.

- Determine possible failure area (PGM-FI main relay 1 control circuit, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Install the relay circuit board . -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector A (50P) -5. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 5 Test point 2 Body ground Is there battery voltage? YES Go to step 10. NO Go to step 8.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Install the relay circuit board .

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector A (50P)

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 5

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 10.

NO

Go to step 8.

- Determine possible failure area (+B IGP line, others) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Test point 1 Relay circuit board connector C (18P) No. 18 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 9. NO Repair an open in the +B IGP wire between the No.
````

## Chunk 6874: DTC P0657 (L15B7/L15BA/L15BY)

- Title: DTC P0657 (L15B7/L15BA/L15BY)
- Source path: `pages\7602.html`
- Chunk ID: `chunk_56da4c1a71ae`
- Images: `images\GHH405080.jpeg`, `images\GHH405081.jpeg`, `images\GHH405082.jpeg`, `images\GHH405083.jpeg`, `images\GHH405084.jpeg`, `images\GHH405085.jpeg`
- Duplicate sources: `pages\9189.html`, `pages\22251.html`, `pages\15289.html`

### Full Text

````text
)

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 5

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 10.

NO

Go to step 8.

- Determine possible failure area (+B IGP line, others) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Test point 1 Relay circuit board connector C (18P) No. 18 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 9. NO Repair an open in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 18

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 9.

NO

Repair an open in the +B IGP wire between the No. A7 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board.

- Open wire check (FI MAIN RLY CL- line) -1. Connect terminals A and B with a jumper wire. Terminal A Relay circuit board connector C (18P) No. 5 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Relay circuit board connector C (18P) No. 5: jumped to body ground Test point 1 PCM connector A (50P) No. 5 Test point 2 Body ground Is there continuity? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

-1. Connect terminals A and B with a jumper wire.

Terminal A | Relay circuit board connector C (18P) No. 5

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Relay circuit board connector C (18P) No. 5: jumped to body ground

Test point 1 | PCM connector A (50P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

- Open wire check (FI MAIN RLY OUT line) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Connect terminals A and B with a jumper wire. Terminal A Relay circuit board connector C (18P) No. 17 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Relay circuit board connector C (18P) No. 17: jumped to body ground Test point 1 PCM connector A (50P) No. 8 Test point 2 Body ground Is there continuity? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Relay circuit board connector C (18P) No. 17

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected
````

## Chunk 6875: DTC P0657 (L15B7/L15BA/L15BY)

- Title: DTC P0657 (L15B7/L15BA/L15BY)
- Source path: `pages\7602.html`
- Chunk ID: `chunk_9698bdf96d80`
- Images: `images\GHH405080.jpeg`, `images\GHH405081.jpeg`, `images\GHH405082.jpeg`, `images\GHH405083.jpeg`, `images\GHH405084.jpeg`, `images\GHH405085.jpeg`
- Duplicate sources: `pages\9189.html`, `pages\22251.html`, `pages\15289.html`

### Full Text

````text
round Test point 1 PCM connector A (50P) No. 8 Test point 2 Body ground Is there continuity? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Relay circuit board connector C (18P) No. 17

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Relay circuit board connector C (18P) No. 17: jumped to body ground

Test point 1 | PCM connector A (50P) No. 8

Test point 2 | Body ground

Is there continuity?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and relay circuit board.
````

## Chunk 6876: DTC P0657 (L15BY) (18-20)

- Title: DTC P0657 (L15BY) (18-20)
- Source path: `pages\7603.html`
- Chunk ID: `chunk_cf3d5fd20ca8`
- Images: `images\GHH405086.png`, `images\GHH405087.jpeg`, `images\GHH405088.png`, `images\GHH405089.jpeg`, `images\GHH405090.png`, `images\GHH405091.jpeg`, `images\GHH405092.png`, `images\GHH405093.jpeg`, `images\GHH405094.png`, `images\GHH405095.jpeg`
- Duplicate sources: `pages\9190.html`, `pages\22252.html`, `pages\15290.html`

### Full Text

````text
# DTC P0657 (L15BY) (18-20)

DTC P0657 : PCM Power Supply Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0657 PCM Power Supply Circuit Malfunction Is DTC P0657 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0657 PCM Power Supply Circuit Malfunction

Is DTC P0657 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Check the following fuse. Fuse No. A7 Is the fuse OK? YES Go to step 7. NO Go to step 4.

-1. Check the following fuse.

Fuse | No. A7

Is the fuse OK?

YES

Go to step 7.

NO

Go to step 4.

- Determine possible failure area (+B IGP line, others) -1. Remove the blown No. A7 fuse . -2. Check for continuity the between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 18: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the +B IGP wire between the No. A7 fuse and the relay circuit board. Also replace the No. A7 fuse. NO Go to step 5.

-1. Remove the blown No. A7 fuse .

-2. Check for continuity the between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 18:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the +B IGP wire between the No. A7 fuse and the relay circuit board. Also replace the No. A7 fuse.

NO

Go to step 5.

- Parts internal circuit check -1. Jump the SCS line with the HDS, and wait more than 1 minute. Check for continuity between test points 1 and 2 while disconnecting these parts, one at a time: PGM-FI main relay 2 PCM connector A (50P) Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 17: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Does continuity go away with the part (s) removed? YES Replace the part that continuity goes away when it was disconnected. If the part is PCM, Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 fuse . NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Check for continuity between test points 1 and 2 while disconnecting these parts, one at a time:

- PGM-FI main relay 2

- PCM connector A (50P)

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 17:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Does continuity go away with the part (s) removed?

YES

Replace the part that continuity goes away when it was disconnected.
````

## Chunk 6877: DTC P0657 (L15BY) (18-20)

- Title: DTC P0657 (L15BY) (18-20)
- Source path: `pages\7603.html`
- Chunk ID: `chunk_5723782bb108`
- Images: `images\GHH405086.png`, `images\GHH405087.jpeg`, `images\GHH405088.png`, `images\GHH405089.jpeg`, `images\GHH405090.png`, `images\GHH405091.jpeg`, `images\GHH405092.png`, `images\GHH405093.jpeg`, `images\GHH405094.png`, `images\GHH405095.jpeg`
- Duplicate sources: `pages\9190.html`, `pages\22252.html`, `pages\15290.html`

### Full Text

````text
vice information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 fuse . NO Go to step 6.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Check for continuity between test points 1 and 2 while disconnecting these parts, one at a time:

- PGM-FI main relay 2

- PCM connector A (50P)

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 17:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Does continuity go away with the part (s) removed?

YES

Replace the part that continuity goes away when it was disconnected. If the part is PCM, Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A7 fuse .

NO

Go to step 6.

- Shorted wire check (FI MAIN RLY OUT line) -1. Disconnect the following parts and connectors. PGM-FI main relay 2 PCM connector A (50P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PGM-FI main relay 2: disconnected PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 8 Test point 2 Body ground Is there continuity? YES Repair a short in the FI MAIN RLY OUT wire between the relay circuit board, PGM-FI main relay 2, and the PCM (A8). Also replace the No. A7 fuse . NO Replace the relay circuit board . Also replace the No. A7 fuse .

-1. Disconnect the following parts and connectors.

PGM-FI main relay 2

PCM connector A (50P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PGM-FI main relay 2: disconnected

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 8

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI MAIN RLY OUT wire between the relay circuit board, PGM-FI main relay 2, and the PCM (A8). Also replace the No. A7 fuse .

NO

Replace the relay circuit board . Also replace the No. A7 fuse .

- Determine possible failure area (PGM-FI main relay 1 control circuit, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Reinstall the relay circuit board . -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector A (50P) -5. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 5 Test point 2 Body ground Is there battery voltage? YES Go to step 10. NO Go to step 8.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Reinstall the relay circuit board .

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector A (50P)

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 5

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 10.

NO

Go to step 8.

- Determine possible failure area (+B IGP line, others) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 18: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 9. NO Repair an open in the +B IGP wire between the No. A7 fuse and the relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 18:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 9.

NO

Repair an open in the +B IGP wire between the No.
````

## Chunk 6878: DTC P0657 (L15BY) (18-20)

- Title: DTC P0657 (L15BY) (18-20)
- Source path: `pages\7603.html`
- Chunk ID: `chunk_98e800810ac4`
- Images: `images\GHH405086.png`, `images\GHH405087.jpeg`, `images\GHH405088.png`, `images\GHH405089.jpeg`, `images\GHH405090.png`, `images\GHH405091.jpeg`, `images\GHH405092.png`, `images\GHH405093.jpeg`, `images\GHH405094.png`, `images\GHH405095.jpeg`
- Duplicate sources: `pages\9190.html`, `pages\22252.html`, `pages\15290.html`

### Full Text

````text
C (18P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 18: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 9. NO Repair an open in the +B IGP wire between the No. A7 fuse and the relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 18:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 9.

NO

Repair an open in the +B IGP wire between the No. A7 fuse and the relay circuit board.

- Open wire check (FI MAIN RLY CL- line) -1. Connect terminals A and B with a jumper wire. Terminal A Relay circuit board connector C (18P) (female terminals) No. 5: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Relay circuit board connector C (18P) No. 5: jumped to body ground Test point 1 PCM connector A (50P) No. 5 Test point 2 Body ground Is there continuity? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

-1. Connect terminals A and B with a jumper wire.

Terminal A | Relay circuit board connector C (18P) (female terminals) No. 5:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Relay circuit board connector C (18P) No. 5: jumped to body ground

Test point 1 | PCM connector A (50P) No. 5

Test point 2 | Body ground

Is there continuity?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY CL- wire between the PCM (A5) and the relay circuit board.

- Open wire check (FI MAIN RLY OUT line) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Connect terminals A and B with a jumper wire. Terminal A Relay circuit board connector C (18P) (female terminals) No. 17: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector C (18P): disconnected Relay circuit board connector C (18P) No. 17: jumped to body ground Test point 1 PCM connector A (50P) No. 8 Test point 2 Body ground Is there continuity? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and relay circuit board.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Relay circuit board connector C (18P) (female terminals) No. 17:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector C (18P): disconnected

Relay circuit board connector C (18P) No. 17: jumped to body ground

Test point 1 | PCM connector A (50P) No. 8

Test point 2 | Body ground

Is there continuity?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0657 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY OUT wire between the PCM (A8) and relay circuit board.
````

## Chunk 6879: DTC P065A (K20C1) (17-21)

- Title: DTC P065A (K20C1) (17-21)
- Source path: `pages\7604.html`
- Chunk ID: `chunk_55a0feb122d6`
- Images: none
- Duplicate sources: `pages\9191.html`, `pages\22253.html`, `pages\14860.html`

### Full Text

````text
# DTC P065A (K20C1) (17-21)

DTC P065A : ACG No Charging Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

DTC (PGM-FI)

- DTC check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle for 1 minute. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0562 Charging System Low Voltage Is DTC P0562 indicated? YES Go to the troubleshooting for DTC P0562 . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle for 1 minute.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0562 Charging System Low Voltage

Is DTC P0562 indicated?

YES

Go to the troubleshooting for DTC P0562 .

NO

Go to step 2.

- Problem verification -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P065A ACG No Charging Malfunction Is DTC P065A indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

Is DTC P065A indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Drive belt check -1. Inspect the drive belt . Is the drive belt OK? YES Repair or replace the alternator . NO Replace the drive belt .

-1. Inspect the drive belt .

Is the drive belt OK?

YES

Repair or replace the alternator .

NO

Replace the drive belt .
````

## Chunk 6880: DTC P065A (K20C2)

- Title: DTC P065A (K20C2)
- Source path: `pages\7605.html`
- Chunk ID: `chunk_680416788496`
- Images: none
- Duplicate sources: `pages\9192.html`, `pages\22254.html`, `pages\15291.html`

### Full Text

````text
# DTC P065A (K20C2)

DTC P065A : ACG No Charging Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

DTC (PGM-FI)

- DTC check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle for 1 minute. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0562 Charging System Low Voltage Is DTC P0562 indicated? YES Go to the troubleshooting for DTC P0562 . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle for 1 minute.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0562 Charging System Low Voltage

Is DTC P0562 indicated?

YES

Go to the troubleshooting for DTC P0562 .

NO

Go to step 2.

- Problem verification -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P065A ACG No Charging Malfunction Is DTC P065A indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

Is DTC P065A indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Drive belt check -1. Inspect the drive belt . Is the drive belt OK? YES Repair or replace the alternator . NO Replace the drive belt .

-1. Inspect the drive belt .

Is the drive belt OK?

YES

Repair or replace the alternator .

NO

Replace the drive belt .
````

## Chunk 6881: DTC P065A (L15B7/L15BA/L15BY)

- Title: DTC P065A (L15B7/L15BA/L15BY)
- Source path: `pages\7606.html`
- Chunk ID: `chunk_70b7e88d7dc1`
- Images: none
- Duplicate sources: `pages\9193.html`, `pages\22255.html`, `pages\15292.html`

### Full Text

````text
# DTC P065A (L15B7/L15BA/L15BY)

DTC P065A : ACG No Charging Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

DTC (PGM-FI)

- DTC check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle for 1 minute. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0562 Charging System Low Voltage Is DTC P0562 indicated? YES Go to the troubleshooting for DTC P0562 . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle for 1 minute.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0562 Charging System Low Voltage

Is DTC P0562 indicated?

YES

Go to the troubleshooting for DTC P0562 .

NO

Go to step 2.

- Problem verification -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P065A ACG No Charging Malfunction Is DTC P065A indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P065A ACG No Charging Malfunction

Is DTC P065A indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check the alternator and the drive belt. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Drive belt check -1. Inspect the drive belt . Is the drive belt OK? YES Repair or replace the alternator . NO Replace the drive belt .

-1. Inspect the drive belt .

Is the drive belt OK?

YES

Repair or replace the alternator .

NO

Replace the drive belt .
````

## Chunk 6882: DTC P0685 (K20C1) (17-21)

- Title: DTC P0685 (K20C1) (17-21)
- Source path: `pages\7607.html`
- Chunk ID: `chunk_720fbfd30667`
- Images: `images\GHH405096.png`, `images\GHH405097.jpeg`, `images\GHH405098.png`, `images\GHH405099.png`, `images\GHH405100.jpeg`, `images\GHH405101.jpeg`, `images\GHH405102.png`, `images\GHH405103.jpeg`
- Duplicate sources: `pages\9194.html`, `pages\22256.html`, `pages\14861.html`

### Full Text

````text
# DTC P0685 (K20C1) (17-21)

DTC P0685 : A/F Sensor (Sensor 1) Heater Power Source Circuit Open

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0685 A/F Sensor (Sensor 1) Heater Power Source Circuit Open

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0685 A/F Sensor (Sensor 1) Heater Power Source Circuit Open Is DTC P0685 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0685 A/F Sensor (Sensor 1) Heater Power Source Circuit Open

Is DTC P0685 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A9 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the No. A9 (15 A) fuse circuit. Also replace the No. A9 (15 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A9 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the No. A9 (15 A) fuse circuit. Also replace the No. A9 (15 A) fuse.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 4. NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 4.

NO

Replace the relay circuit board .

- Open wire check (+B DBW line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 14: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B DBW wire is OK. Go to step 5. NO Repair an open in the +B DBW wire between the relay circuit board and the No. A9 (15 A) fuse in the under-hood fuse/relay box.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 14:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B DBW wire is OK. Go to step 5.

NO

Repair an open in the +B DBW wire between the relay circuit board and the No. A9 (15 A) fuse in the under-hood fuse/relay box.

- Open wire check (FI SUB RLY OUT/IGPS (LAF) line) -1. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 A/F sensor (Sensor 1) 6P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1).

-1. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 1:
````

## Chunk 6883: DTC P0685 (K20C1) (17-21)

- Title: DTC P0685 (K20C1) (17-21)
- Source path: `pages\7607.html`
- Chunk ID: `chunk_2d21a6932805`
- Images: `images\GHH405096.png`, `images\GHH405097.jpeg`, `images\GHH405098.png`, `images\GHH405099.png`, `images\GHH405100.jpeg`, `images\GHH405101.jpeg`, `images\GHH405102.png`, `images\GHH405103.jpeg`
- Duplicate sources: `pages\9194.html`, `pages\22256.html`, `pages\14861.html`

### Full Text

````text
d A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 A/F sensor (Sensor 1) 6P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1).

-1. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 1:

Test point 2 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1).

- Open wire check (AFHT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 A/F sensor (Sensor 1) 6P connector (female terminals) No. 5: Test point 2 PCM connector No. 1 (96P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0685 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | A/F sensor (Sensor 1) 6P connector (female terminals) No. 5:

Test point 2 | PCM connector No. 1 (96P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0685 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).
````

## Chunk 6884: DTC P0686 (K20C1) (17-21)

- Title: DTC P0686 (K20C1) (17-21)
- Source path: `pages\7608.html`
- Chunk ID: `chunk_190386fc5dfb`
- Images: `images\GHH405104.png`, `images\GHH405105.jpeg`
- Duplicate sources: `pages\9195.html`, `pages\22257.html`, `pages\14862.html`

### Full Text

````text
# DTC P0686 (K20C1) (17-21)

DTC P0686 : A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0686 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0686 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground Is DTC P0686 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0686 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Ground

Is DTC P0686 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A9 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 3. NO Repair a short in the No. A9 (15 A) fuse circuit. Also replace the No. A9 (15 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A9 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 3.

NO

Repair a short in the No. A9 (15 A) fuse circuit. Also replace the No. A9 (15 A) fuse.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 4. NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 4.

NO

Replace the relay circuit board .

- Shorted wire check (FI SUB RLY OUT/IGPS (LAF) line) -1. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1). NO The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 5.

-1. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1).

NO

The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 5.

- Shorted wire check (AFHT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1). NO The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6885: DTC P0686 (K20C1) (17-21)

- Title: DTC P0686 (K20C1) (17-21)
- Source path: `pages\7608.html`
- Chunk ID: `chunk_ddbbfbd959d8`
- Images: `images\GHH405104.png`, `images\GHH405105.jpeg`
- Duplicate sources: `pages\9195.html`, `pages\22257.html`, `pages\14862.html`

### Full Text

````text
SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 5.

- Shorted wire check (AFHT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1). NO The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0686 goes away and the PCM was substituted, replace the original PCM .

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

The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0686 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6886: DTC P0687 (K20C1) (17-21)

- Title: DTC P0687 (K20C1) (17-21)
- Source path: `pages\7609.html`
- Chunk ID: `chunk_5713bdff6a5f`
- Images: `images\GHH405106.png`, `images\GHH405107.jpeg`
- Duplicate sources: `pages\9196.html`, `pages\22258.html`, `pages\14863.html`

### Full Text

````text
# DTC P0687 (K20C1) (17-21)

DTC P0687 : A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0687 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0687 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power Is DTC P0687 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0687 A/F Sensor (Sensor 1) Heater Power Source Circuit Short to Power

Is DTC P0687 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit), the A/F sensor (Sensor 1), and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (FI SUB RLY OUT/IGPS (LAF) line to power) -1. Disconnect the following connector. A/F sensor (Sensor 1) 6P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1). NO The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 4.

-1. Disconnect the following connector.

A/F sensor (Sensor 1) 6P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the FI SUB RLY OUT/IGPS (LAF) wire between the relay circuit board and the A/F sensor (Sensor 1).

NO

The FI SUB RLY OUT/IGPS (LAF) wire is OK. Go to step 4.

- Shorted wire check (AFHT line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed A/F sensor (Sensor 1) 6P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 16 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1). NO The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0687 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

A/F sensor (Sensor 1) 6P connector: disconnected
````

## Chunk 6887: DTC P0687 (K20C1) (17-21)

- Title: DTC P0687 (K20C1) (17-21)
- Source path: `pages\7609.html`
- Chunk ID: `chunk_f6e8dfb6635f`
- Images: `images\GHH405106.png`, `images\GHH405107.jpeg`
- Duplicate sources: `pages\9196.html`, `pages\22258.html`, `pages\14863.html`

### Full Text

````text
. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 16 Test point 2 Body ground Is there any voltage? YES Repair a short to power in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1). NO The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0687 goes away and the PCM was substituted, replace the original PCM .

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

Is there any voltage?

YES

Repair a short to power in the AFHT wire between PCM connector No. 1 terminal No. 16 and the A/F sensor (Sensor 1).

NO

The AFHT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0687 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6888: DTC P068A (K20C1) (17-21)

- Title: DTC P068A (K20C1) (17-21)
- Source path: `pages\7610.html`
- Chunk ID: `chunk_cca8fe89ae7a`
- Images: `images\GHH405108.png`, `images\GHH405109.jpeg`, `images\GHH405110.png`, `images\GHH405111.jpeg`, `images\GHH405112.png`, `images\GHH405113.jpeg`, `images\GHH405114.png`, `images\GHH405115.jpeg`, `images\GHH405116.png`, `images\GHH405117.jpeg`
- Duplicate sources: `pages\9197.html`, `pages\22259.html`, `pages\14864.html`

### Full Text

````text
# DTC P068A (K20C1) (17-21)

DTC P068A : PCM Power Source Circuit Unexpected Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P068A PCM Power Source Circuit Unexpected Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P068A PCM Power Source Circuit Unexpected Voltage Is DTC P068A indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P068A PCM Power Source Circuit Unexpected Voltage

Is DTC P068A indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Check the following fuse. Fuse No. A7 (20 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 6. NO Go to step 4.

-1. Check the following fuse.

Fuse | No. A7 (20 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 6.

NO

Go to step 4.

- Shorted wire check (+B IGP line) -1. Remove the blown No. A7 (20 A) fuse from the under-hood fuse/relay box. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 18: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the +B IGP wire between the relay circuit board and the No. A7 (20 A) fuse in the under-hood fuse/relay box. NO Go to step 5.

-1. Remove the blown No. A7 (20 A) fuse from the under-hood fuse/relay box.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 18:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the +B IGP wire between the relay circuit board and the No. A7 (20 A) fuse in the under-hood fuse/relay box.

NO

Go to step 5.

- Shorted wire check (FI MAIN RLY OUT line) -1. Remove PGM-FI main relay 2 . -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PGM-FI main relay 2: disconnected PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 17: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6), the relay circuit board, and PGM-FI main relay 2. NO The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068A goes away and the PCM was substituted, replace the original PCM .

-1. Remove PGM-FI main relay 2 .

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3.
````

## Chunk 6889: DTC P068A (K20C1) (17-21)

- Title: DTC P068A (K20C1) (17-21)
- Source path: `pages\7610.html`
- Chunk ID: `chunk_a6c805a127c3`
- Images: `images\GHH405108.png`, `images\GHH405109.jpeg`, `images\GHH405110.png`, `images\GHH405111.jpeg`, `images\GHH405112.png`, `images\GHH405113.jpeg`, `images\GHH405114.png`, `images\GHH405115.jpeg`, `images\GHH405116.png`, `images\GHH405117.jpeg`
- Duplicate sources: `pages\9197.html`, `pages\22259.html`, `pages\14864.html`

### Full Text

````text
OFF (LOCK) mode Relay circuit board: removed PGM-FI main relay 2: disconnected PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 17: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6), the relay circuit board, and PGM-FI main relay 2. NO The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068A goes away and the PCM was substituted, replace the original PCM .

-1. Remove PGM-FI main relay 2 .

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PGM-FI main relay 2: disconnected

PCM connector No. 2 (58P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 17:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6), the relay circuit board, and PGM-FI main relay 2.

NO

The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068A goes away and the PCM was substituted, replace the original PCM .

- Open wire check (+B IGP line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 18: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES Go to step 7. NO Repair an open in the +B IGP wire between the relay circuit board and the No. A7 (20 A) fuse in the under-hood fuse/relay box.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 18:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

Go to step 7.

NO

Repair an open in the +B IGP wire between the relay circuit board and the No. A7 (20 A) fuse in the under-hood fuse/relay box.

- Open wire check (FI MAIN RLY CL- line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 5: Test point 2 PCM connector No. 2 (58P) No. 26 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 8. NO Repair an open in the FI MAIN RLY CL- wire between PCM connector No. 2 terminal No. 26 and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector No. 2 (58P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 5:

Test point 2 | PCM connector No. 2 (58P) No. 26

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 8.

NO

Repair an open in the FI MAIN RLY CL- wire between PCM connector No. 2 terminal No. 26 and the relay circuit board.

- Open wire check (FI MAIN RLY OUT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 17: Test point 2 PCM connector No. 2 (58P) No. 2, No. 4, and No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6890: DTC P068A (K20C1) (17-21)

- Title: DTC P068A (K20C1) (17-21)
- Source path: `pages\7610.html`
- Chunk ID: `chunk_3a8279956eb7`
- Images: `images\GHH405108.png`, `images\GHH405109.jpeg`, `images\GHH405110.png`, `images\GHH405111.jpeg`, `images\GHH405112.png`, `images\GHH405113.jpeg`, `images\GHH405114.png`, `images\GHH405115.jpeg`, `images\GHH405116.png`, `images\GHH405117.jpeg`
- Duplicate sources: `pages\9197.html`, `pages\22259.html`, `pages\14864.html`

### Full Text

````text
or No. 2 (58P) No. 26

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 8.

NO

Repair an open in the FI MAIN RLY CL- wire between PCM connector No. 2 terminal No. 26 and the relay circuit board.

- Open wire check (FI MAIN RLY OUT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 17: Test point 2 PCM connector No. 2 (58P) No. 2, No. 4, and No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068A goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6) and the relay circuit board.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector No. 2 (58P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 17:

Test point 2 | PCM connector No. 2 (58P) No. 2, No. 4, and No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI MAIN RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068A goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6) and the relay circuit board.
````

## Chunk 6891: DTC P068B (K20C1) (17-21)

- Title: DTC P068B (K20C1) (17-21)
- Source path: `pages\7611.html`
- Chunk ID: `chunk_27044823ed9e`
- Images: none
- Duplicate sources: `pages\9198.html`, `pages\22260.html`, `pages\14865.html`

### Full Text

````text
# DTC P068B (K20C1) (17-21)

DTC P068B : PCM Power Source Circuit Unexpected Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P068B PCM Power Source Circuit Unexpected Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Wait 10 seconds. -5. Turn the vehicle to the ON mode. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P068B PCM Power Source Circuit Unexpected Voltage Is DTC P068B indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Wait 10 seconds.

-5. Turn the vehicle to the ON mode.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P068B PCM Power Source Circuit Unexpected Voltage

Is DTC P068B indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI main relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (FI MAIN RLY CL- line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 26 Test point 2 Body ground Is there battery voltage? YES Go to step 5. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 26

Test point 2 | Body ground

Is there battery voltage?

YES

Go to step 5.

NO

Go to step 3.

- Shorted wire check (FI MAIN RLY CL- line) -1. Disconnect the following connector. Relay circuit board connector C (18P) -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector C (18P): disconnected Test point 1 PCM connector No. 2 (58P) No. 26 Test point 2 Body ground Is there continuity? YES Repair a short in the FI MAIN RLY CL- wire between PCM connector No. 2 terminal No. 26 and the relay circuit board. NO The FI MAIN RLY CL- wire is OK. Go to step 4.

-1. Disconnect the following connector.

Relay circuit board connector C (18P)

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector C (18P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 26

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI MAIN RLY CL- wire between PCM connector No. 2 terminal No. 26 and the relay circuit board.

NO

The FI MAIN RLY CL- wire is OK. Go to step 4.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM . NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM .

NO
````

## Chunk 6892: DTC P068B (K20C1) (17-21)

- Title: DTC P068B (K20C1) (17-21)
- Source path: `pages\7611.html`
- Chunk ID: `chunk_89c4b409bfdd`
- Images: none
- Duplicate sources: `pages\9198.html`, `pages\22260.html`, `pages\14865.html`

### Full Text

````text
ector No. 2 terminal No. 26 and the relay circuit board.

NO

The FI MAIN RLY CL- wire is OK. Go to step 4.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM . NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM .

NO

Replace the relay circuit board .

- Shorted wire check (FI MAIN RLY OUT line to power) -1. Remove PGM-FI main relay 2 . -2. Disconnect the following connector. Relay circuit board connector C (18P) -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected PGM-FI main relay 2: disconnected Relay circuit board connector C (18P): disconnected Test point 1 PCM connector No. 2 (58P) No. 2, No. 4, and No. 6 Test point 2 Body ground Is there battery voltage? YES Repair a short to power in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6), PGM-FI main relay 2, and the relay circuit board. NO The FI MAIN RLY OUT wire is OK. Go to step 6.

-1. Remove PGM-FI main relay 2 .

-2. Disconnect the following connector.

Relay circuit board connector C (18P)

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

PGM-FI main relay 2: disconnected

Relay circuit board connector C (18P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 2, No. 4, and No. 6

Test point 2 | Body ground

Is there battery voltage?

YES

Repair a short to power in the FI MAIN RLY OUT wire between PCM connector No. 2 terminals (No. 2, No. 4, No. 6), PGM-FI main relay 2, and the relay circuit board.

NO

The FI MAIN RLY OUT wire is OK. Go to step 6.

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM . NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P068B goes away and the PCM was substituted, replace the original PCM .

NO

Replace the relay circuit board .
````

## Chunk 6893: DTC P06A8 (K20C2)

- Title: DTC P06A8 (K20C2)
- Source path: `pages\7612.html`
- Chunk ID: `chunk_e83747007105`
- Images: none
- Duplicate sources: `pages\9199.html`, `pages\22261.html`, `pages\15293.html`

### Full Text

````text
# DTC P06A8 (K20C2)

DTC P06A8 : Internal VCC Power Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P06A8 Internal VCC Power Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Reset the PCM with the HDS . Reset PCM -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P06A8 Internal VCC Power Malfunction Is DTC P06A8 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P06A8 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the ON mode.

-2. Reset the PCM with the HDS .

Reset PCM

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P06A8 Internal VCC Power Malfunction

Is DTC P06A8 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P06A8 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 6894: DTC P06A8 (L15B7/L15BA/L15BY)

- Title: DTC P06A8 (L15B7/L15BA/L15BY)
- Source path: `pages\7613.html`
- Chunk ID: `chunk_7ab53cfab0a3`
- Images: none
- Duplicate sources: `pages\9200.html`, `pages\22262.html`, `pages\15294.html`

### Full Text

````text
# DTC P06A8 (L15B7/L15BA/L15BY)

DTC P06A8 : Internal VCC Power Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P06A8 Internal VCC Power Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Reset the PCM with the HDS . Reset PCM -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P06A8 Internal VCC Power Malfunction Is DTC P06A8 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P06A8 goes away and the PCM was substituted, replace the original PCM . NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the ON mode.

-2. Reset the PCM with the HDS .

Reset PCM

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P06A8 Internal VCC Power Malfunction

Is DTC P06A8 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P06A8 goes away and the PCM was substituted, replace the original PCM .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 6895: DTC P0703 (K20C1) (17-21)

- Title: DTC P0703 (K20C1) (17-21)
- Source path: `pages\7614.html`
- Chunk ID: `chunk_513ce33722cf`
- Images: `images\GHH405118.png`, `images\GHH405119.png`, `images\GHH405120.jpeg`, `images\GHH405121.png`, `images\GHH405122.jpeg`, `images\GHH405123.png`, `images\GHH405124.png`, `images\GHH405125.jpeg`
- Duplicate sources: `pages\9201.html`, `pages\22263.html`, `pages\14866.html`

### Full Text

````text
# DTC P0703 (K20C1) (17-21)

DTC P0703 : Brake Pedal Position Switch (NC) Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the accelerator pedal is pressed with pressing the brake pedal lightly and continuously for 5 minutes or more, this DTC will be stored.

DTC Description | Confirmed DTC | Pending DTC

P0703 Brake Pedal Position Switch (NC) Malfunction

DTC (PGM-FI)

- Brake pedal position switch signal (BKSWNC) check 1 -1. Turn the vehicle to the ON mode. -2. Check the parameter (s) below with the HDS without pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Go to step 7. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter (s) below with the HDS without pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Go to step 7.

NO

Go to step 2.

- Brake pedal position switch installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Adjust the brake pedal and the brake pedal position switch . -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS without pressing the brake pedal position switch. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES The failure is not duplicated. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Adjust the brake pedal and the brake pedal position switch .

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS without pressing the brake pedal position switch.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is not duplicated.

NO

Go to step 3.

- Determine possible failure area (brake pedal position switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Brake pedal position switch 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector (female terminals) No. 3: Terminal B Brake pedal position switch 4P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Replace the brake pedal position switch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Brake pedal position switch 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector (female terminals) No. 3:

Terminal B | Brake pedal position switch 4P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Replace the brake pedal position switch .

NO

Go to step 4.

- Determine possible failure area (IG1 ACG line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the brake pedal position switch 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector (female terminals) No. 4:

Test point 2 | Body ground
````

## Chunk 6896: DTC P0703 (K20C1) (17-21)

- Title: DTC P0703 (K20C1) (17-21)
- Source path: `pages\7614.html`
- Chunk ID: `chunk_8a749f745e6f`
- Images: `images\GHH405118.png`, `images\GHH405119.png`, `images\GHH405120.jpeg`, `images\GHH405121.png`, `images\GHH405122.jpeg`, `images\GHH405123.png`, `images\GHH405124.png`, `images\GHH405125.jpeg`
- Duplicate sources: `pages\9201.html`, `pages\22263.html`, `pages\14866.html`

### Full Text

````text
icle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG wire is OK. Go to step 5.

NO

Go to step 6.

- Open wire check (BKSWNC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector (female terminals) No. 3: Terminal B Brake pedal position switch 4P connector (female terminals) No. 4: Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected PCM connector No. 2 (58P): disconnected Brake pedal position switch 4P connector No. 3 and No. 4: jumped Test point 1 PCM connector No. 2 (58P) No. 18 Test point 2 Body ground Is there battery voltage? YES The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the BKSWNC wire between PCM connector No. 2 terminal No. 18 and the brake pedal position switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector (female terminals) No. 3:

Terminal B | Brake pedal position switch 4P connector (female terminals) No. 4:

Courtesy of HONDA, U.S.A., INC.

-5. Turn the vehicle to the ON mode.

-6. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

PCM connector No. 2 (58P): disconnected

Brake pedal position switch 4P connector No. 3 and No. 4: jumped

Test point 1 | PCM connector No. 2 (58P) No. 18

Test point 2 | Body ground

Is there battery voltage?

YES

The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the BKSWNC wire between PCM connector No. 2 terminal No. 18 and the brake pedal position switch.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the brake pedal position switch. NO Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the brake pedal position switch.

NO

Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

- Brake pedal position switch signal (BKSWNC) check 2 -1. Press the brake pedal. -2. Check the parameter (s) below with the HDS while pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW OPEN Do the current condition (s) match the threshold? YES Intermittent failure, the system is OK at this time.
````

## Chunk 6897: DTC P0703 (K20C1) (17-21)

- Title: DTC P0703 (K20C1) (17-21)
- Source path: `pages\7614.html`
- Chunk ID: `chunk_f73602e9bb9c`
- Images: `images\GHH405118.png`, `images\GHH405119.png`, `images\GHH405120.jpeg`, `images\GHH405121.png`, `images\GHH405122.jpeg`, `images\GHH405123.png`, `images\GHH405124.png`, `images\GHH405125.jpeg`
- Duplicate sources: `pages\9201.html`, `pages\22263.html`, `pages\14866.html`

### Full Text

````text
ound on the No. B21 (10 A) fuse circuit if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the brake pedal position switch.

NO

Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

- Brake pedal position switch signal (BKSWNC) check 2 -1. Press the brake pedal. -2. Check the parameter (s) below with the HDS while pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW OPEN Do the current condition (s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 8.

-1. Press the brake pedal.

-2. Check the parameter (s) below with the HDS while pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | OPEN

Do the current condition (s) match the threshold?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Go to step 8.

- Brake pedal position switch check -1. Test the brake pedal position switch . Is the brake pedal position switch OK? YES The brake pedal position switch is OK. Repair a short to power in the BKSWNC wire between PCM connector No. 2 terminal No. 18 and the brake pedal position switch. NO Replace the brake pedal position switch .

-1. Test the brake pedal position switch .

Is the brake pedal position switch OK?

YES

The brake pedal position switch is OK. Repair a short to power in the BKSWNC wire between PCM connector No. 2 terminal No. 18 and the brake pedal position switch.

NO

Replace the brake pedal position switch .
````

## Chunk 6898: DTC P0703 (K20C2)

- Title: DTC P0703 (K20C2)
- Source path: `pages\7615.html`
- Chunk ID: `chunk_2c18d04b6b78`
- Images: `images\GHH405126.jpeg`, `images\GHH405127.jpeg`, `images\GHH405128.jpeg`
- Duplicate sources: `pages\9202.html`, `pages\22264.html`, `pages\15295.html`

### Full Text

````text
# DTC P0703 (K20C2)

DTC P0703 : Brake Pedal Position Switch (NC) Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the accelerator pedal is pressed with pressing the brake pedal lightly and continuously for 5 minutes or more, this DTC will be stored.

DTC Description | Confirmed DTC | Pending DTC

P0703 Brake Pedal Position Switch (NC) Malfunction

DTC (PGM-FI)

- Brake pedal position switch signal (BKSWNC) check 1 -1. Turn the vehicle to the ON mode. -2. Check the parameter (s) below with the HDS without pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Go to step 7. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter (s) below with the HDS without pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Go to step 7.

NO

Go to step 2.

- Brake pedal position switch installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Adjust the brake pedal and the brake pedal position switch . -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS without pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES The failure is not duplicated. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Adjust the brake pedal and the brake pedal position switch .

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS without pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is not duplicated.

NO

Go to step 3.

- Determine possible failure area (brake pedal position switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Brake pedal position switch 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector No. 3 Terminal B Brake pedal position switch 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Replace the brake pedal position switch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Brake pedal position switch 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector No. 3

Terminal B | Brake pedal position switch 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Replace the brake pedal position switch .

NO

Go to step 4.

- Determine possible failure area (IG1 ACG line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the brake pedal position switch 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG wire is OK. Go to step 5.

NO

Go to step 6.

- Open wire check (BKSWNC line) -1.
````

## Chunk 6899: DTC P0703 (K20C2)

- Title: DTC P0703 (K20C2)
- Source path: `pages\7615.html`
- Chunk ID: `chunk_0f0830328d09`
- Images: `images\GHH405126.jpeg`, `images\GHH405127.jpeg`, `images\GHH405128.jpeg`
- Duplicate sources: `pages\9202.html`, `pages\22264.html`, `pages\15295.html`

### Full Text

````text
sition switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG wire is OK. Go to step 5.

NO

Go to step 6.

- Open wire check (BKSWNC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector A (50P) -4. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector No. 3 Terminal B Brake pedal position switch 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected PCM connector A (50P): disconnected Brake pedal position switch 4P connector No. 3 and No. 4: jumped Test point 1 PCM connector A (50P) No. 49 Test point 2 Body ground Is there battery voltage? YES The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the BKSWNC wire between the PCM (A49) and the brake pedal position switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector No. 3

Terminal B | Brake pedal position switch 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-5. Turn the vehicle to the ON mode.

-6. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

PCM connector A (50P): disconnected

Brake pedal position switch 4P connector No. 3 and No. 4: jumped

Test point 1 | PCM connector A (50P) No. 49

Test point 2 | Body ground

Is there battery voltage?

YES

The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the BKSWNC wire between the PCM (A49) and the brake pedal position switch.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Repair an open in the IG1 ACG wire between the No. B21 (10 A) fuse and the brake pedal position switch. NO Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Repair an open in the IG1 ACG wire between the No. B21 (10 A) fuse and the brake pedal position switch.

NO

Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

- Brake pedal position switch signal (BKSWNC) check 2 -1. Turn the vehicle to the ON mode. -2. Press the brake pedal. -3. Check the parameter (s) below with the HDS while pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW OPEN Do the current condition (s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 8.

-1. Turn the vehicle to the ON mode.

-2. Press the brake pedal.

-3.
````

## Chunk 6900: DTC P0703 (K20C2)

- Title: DTC P0703 (K20C2)
- Source path: `pages\7615.html`
- Chunk ID: `chunk_3a8fe7cba2f8`
- Images: `images\GHH405126.jpeg`, `images\GHH405127.jpeg`, `images\GHH405128.jpeg`
- Duplicate sources: `pages\7616.html`, `pages\9202.html`, `pages\9203.html`, `pages\22264.html`, `pages\22265.html`, `pages\15295.html`, `pages\15296.html`

### Full Text

````text
fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

- Brake pedal position switch signal (BKSWNC) check 2 -1. Turn the vehicle to the ON mode. -2. Press the brake pedal. -3. Check the parameter (s) below with the HDS while pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW OPEN Do the current condition (s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 8.

-1. Turn the vehicle to the ON mode.

-2. Press the brake pedal.

-3. Check the parameter (s) below with the HDS while pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | OPEN

Do the current condition (s) match the threshold?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Go to step 8.

- Brake pedal position switch check -1. Test the brake pedal position switch . Is the brake pedal position switch OK? YES The brake pedal position switch is OK. Repair a short to power in the BKSWNC wire between the PCM (A49) and the brake pedal position switch. NO Replace the brake pedal position switch .

-1. Test the brake pedal position switch .

Is the brake pedal position switch OK?

YES

The brake pedal position switch is OK. Repair a short to power in the BKSWNC wire between the PCM (A49) and the brake pedal position switch.

NO

Replace the brake pedal position switch .
````

## Chunk 6901: DTC P0703 (L15B7/L15BA/L15BY)

- Title: DTC P0703 (L15B7/L15BA/L15BY)
- Source path: `pages\7616.html`
- Chunk ID: `chunk_209669ffac64`
- Images: `images\GHH405129.jpeg`, `images\GHH405130.jpeg`, `images\GHH405131.jpeg`
- Duplicate sources: `pages\9203.html`, `pages\22265.html`, `pages\15296.html`

### Full Text

````text
# DTC P0703 (L15B7/L15BA/L15BY)

DTC P0703 : Brake Pedal Position Switch (NC) Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If the accelerator pedal is pressed with pressing the brake pedal lightly and continuously for 5 minutes or more, this DTC will be stored.

DTC Description | Confirmed DTC | Pending DTC

P0703 Brake Pedal Position Switch (NC) Malfunction

DTC (PGM-FI)

- Brake pedal position switch signal (BKSWNC) check 1 -1. Turn the vehicle to the ON mode. -2. Check the parameter (s) below with the HDS without pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Go to step 7. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter (s) below with the HDS without pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Go to step 7.

NO

Go to step 2.

- Brake pedal position switch installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Adjust the brake pedal and the brake pedal position switch . -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS without pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES The failure is not duplicated. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Adjust the brake pedal and the brake pedal position switch .

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS without pressing the brake pedal.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is not duplicated.

NO

Go to step 3.

- Determine possible failure area (brake pedal position switch, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Brake pedal position switch 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector No. 3 Terminal B Brake pedal position switch 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW CLOSE Do the current condition (s) match the threshold? YES Replace the brake pedal position switch . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Brake pedal position switch 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector No. 3

Terminal B | Brake pedal position switch 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CRUISE BRAKE SW/IDLE STOP SW | CLOSE

Do the current condition (s) match the threshold?

YES

Replace the brake pedal position switch .

NO

Go to step 4.

- Determine possible failure area (IG1 ACG line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the brake pedal position switch 4P connector. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG wire is OK. Go to step 5.

NO

Go to step 6.

- Open wire check (BKSWNC line) -1.
````

## Chunk 6902: DTC P0703 (L15B7/L15BA/L15BY)

- Title: DTC P0703 (L15B7/L15BA/L15BY)
- Source path: `pages\7616.html`
- Chunk ID: `chunk_92d943b0b523`
- Images: `images\GHH405129.jpeg`, `images\GHH405130.jpeg`, `images\GHH405131.jpeg`
- Duplicate sources: `pages\9203.html`, `pages\22265.html`, `pages\15296.html`

### Full Text

````text
sition switch 4P connector: disconnected Test point 1 Brake pedal position switch 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The IG1 ACG wire is OK. Go to step 5. NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the brake pedal position switch 4P connector.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Test point 1 | Brake pedal position switch 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The IG1 ACG wire is OK. Go to step 5.

NO

Go to step 6.

- Open wire check (BKSWNC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector A (50P) -4. Connect terminals A and B with a jumper wire. Terminal A Brake pedal position switch 4P connector No. 3 Terminal B Brake pedal position switch 4P connector No. 4 Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Brake pedal position switch 4P connector: disconnected Brake pedal position switch 4P connector No. 3 and No. 4: jumped PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 49 Test point 2 Body ground Is there battery voltage? YES The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the BKSWNC wire between the PCM (A49) and the brake pedal position switch.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Connect terminals A and B with a jumper wire.

Terminal A | Brake pedal position switch 4P connector No. 3

Terminal B | Brake pedal position switch 4P connector No. 4

Courtesy of HONDA, U.S.A., INC.

-5. Turn the vehicle to the ON mode.

-6. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Brake pedal position switch 4P connector: disconnected

Brake pedal position switch 4P connector No. 3 and No. 4: jumped

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 49

Test point 2 | Body ground

Is there battery voltage?

YES

The BKSWNC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0703 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the BKSWNC wire between the PCM (A49) and the brake pedal position switch.

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Repair an open in the IG1 ACG wire between the No. B21 (10 A) fuse and the brake pedal position switch. NO Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Repair an open in the IG1 ACG wire between the No. B21 (10 A) fuse and the brake pedal position switch.

NO

Replace the No. B21 (10 A) fuse. Also check for a short to ground on the No. B21 (10 A) fuse circuit if needed.

- Brake pedal position switch signal (BKSWNC) check 2 -1. Turn the vehicle to the ON mode. -2. Press the brake pedal. -3. Check the parameter (s) below with the HDS while pressing the brake pedal. Signal Threshold Current conditions Values Unit Values Unit CRUISE BRAKE SW/IDLE STOP SW OPEN Do the current condition (s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the brake pedal position switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 8.

-1. Turn the vehicle to the ON mode.

-2. Press the brake pedal.

-3.
````

## Chunk 6903: DTC P0715 (K20C1) (17-21)

- Title: DTC P0715 (K20C1) (17-21)
- Source path: `pages\7617.html`
- Chunk ID: `chunk_328dd75ecec3`
- Images: `images\GHH405132.png`, `images\GHH405133.png`, `images\GHH405134.jpeg`, `images\GHH405135.png`, `images\GHH405136.jpeg`, `images\GHH405137.png`, `images\GHH405138.jpeg`
- Duplicate sources: `pages\9204.html`, `pages\22266.html`, `pages\14867.html`

### Full Text

````text
# DTC P0715 (K20C1) (17-21)

DTC P0715 : Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0715 Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on. -3. Test-drive at a steady speed of 9 mph (15 km/h) or more for several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit M SHAFT SPD Is the mainshaft speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the input shaft (mainshaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on.

-3. Test-drive at a steady speed of 9 mph (15 km/h) or more for several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

M SHAFT SPD

Is the mainshaft speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the input shaft (mainshaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Determine possible failure area (VCC2 5 line or SG2 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Input shaft (mainshaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Input shaft (mainshaft) speed sensor 3P connector: disconnected Test point 1 Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 1: Test point 2 Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Input shaft (mainshaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Input shaft (mainshaft) speed sensor 3P connector: disconnected

Test point 1 | Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 1:

Test point 2 | Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC2 5 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Input shaft (mainshaft) speed sensor 3P connector: disconnected Test point 1 Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC2 5 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the input shaft (mainshaft) speed sensor. NO Repair an open in the VCC2 5 wire between PCM connector No. 1 terminal No. 83 and the input shaft (mainshaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Input shaft (mainshaft) speed sensor 3P connector: disconnected

Test point 1 | Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC2 5 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the input shaft (mainshaft) speed sensor.

NO

Repair an open in the VCC2 5 wire between PCM connector No. 1 terminal No. 83 and the input shaft (mainshaft) speed sensor.

- Shorted wire check (NM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2.
````

## Chunk 6904: DTC P0715 (K20C1) (17-21)

- Title: DTC P0715 (K20C1) (17-21)
- Source path: `pages\7617.html`
- Chunk ID: `chunk_0207dfdeccb0`
- Images: `images\GHH405132.png`, `images\GHH405133.png`, `images\GHH405134.jpeg`, `images\GHH405135.png`, `images\GHH405136.jpeg`, `images\GHH405137.png`, `images\GHH405138.jpeg`
- Duplicate sources: `pages\9204.html`, `pages\22266.html`, `pages\14867.html`

### Full Text

````text
| Vehicle ON mode

Input shaft (mainshaft) speed sensor 3P connector: disconnected

Test point 1 | Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC2 5 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the input shaft (mainshaft) speed sensor.

NO

Repair an open in the VCC2 5 wire between PCM connector No. 1 terminal No. 83 and the input shaft (mainshaft) speed sensor.

- Shorted wire check (NM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Input shaft (mainshaft) speed sensor 3P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 69 Test point 2 Body ground Is there continuity? YES Repair a short in the NM wire between PCM connector No. 1 terminal No. 69 and the input shaft (mainshaft) speed sensor. NO The NM wire is not shorted. Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Input shaft (mainshaft) speed sensor 3P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | PCM connector No. 1 (96P) No. 69

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NM wire between PCM connector No. 1 terminal No. 69 and the input shaft (mainshaft) speed sensor.

NO

The NM wire is not shorted. Go to step 5.

- Open wire check (NM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Input shaft (mainshaft) speed sensor 3P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 69 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 6. NO Repair an open in the NM wire between PCM connector No. 1 terminal No. 69 and the input shaft (mainshaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Input shaft (mainshaft) speed sensor 3P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Input shaft (mainshaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 69

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 6.

NO

Repair an open in the NM wire between PCM connector No. 1 terminal No. 69 and the input shaft (mainshaft) speed sensor.

- Input shaft (mainshaft) speed sensor check -1. Substitute a known-good input shaft (mainshaft) speed sensor . -2. Reconnect all connectors. -3. Clear the DTC with the HDS. -4. Start the engine. -5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on. -6. Test-drive at a steady speed of 9 mph (15 km/h) or more for several minutes. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0715 Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction Is DTC P0715 indicated? YES The input shaft (mainshaft) speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0715 goes away and the PCM was substituted, replace the original PCM . NO Replace the original input shaft (mainshaft) speed sensor .

-1. Substitute a known-good input shaft (mainshaft) speed sensor .

-2. Reconnect all connectors.

-3. Clear the DTC with the HDS.

-4. Start the engine.

-5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on.

-6. Test-drive at a steady speed of 9 mph (15 km/h) or more for several minutes.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0715 Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

Is DTC P0715 indicated?

YES

The input shaft (mainshaft) speed sensor is OK.
````

## Chunk 6905: DTC P0715 (K20C1) (17-21)

- Title: DTC P0715 (K20C1) (17-21)
- Source path: `pages\7617.html`
- Chunk ID: `chunk_f9e8c4e2cecb`
- Images: `images\GHH405132.png`, `images\GHH405133.png`, `images\GHH405134.jpeg`, `images\GHH405135.png`, `images\GHH405136.jpeg`, `images\GHH405137.png`, `images\GHH405138.jpeg`
- Duplicate sources: `pages\9204.html`, `pages\22266.html`, `pages\14867.html`

### Full Text

````text
ymptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0715 goes away and the PCM was substituted, replace the original PCM . NO Replace the original input shaft (mainshaft) speed sensor .

-1. Substitute a known-good input shaft (mainshaft) speed sensor .

-2. Reconnect all connectors.

-3. Clear the DTC with the HDS.

-4. Start the engine.

-5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on.

-6. Test-drive at a steady speed of 9 mph (15 km/h) or more for several minutes.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0715 Input Shaft (Mainshaft) Speed Sensor Circuit Malfunction

Is DTC P0715 indicated?

YES

The input shaft (mainshaft) speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0715 goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original input shaft (mainshaft) speed sensor .
````

## Chunk 6906: DTC P0720 (K20C1) (17-21)

- Title: DTC P0720 (K20C1) (17-21)
- Source path: `pages\7618.html`
- Chunk ID: `chunk_38c6d7b189c2`
- Images: `images\GHH405139.png`, `images\GHH405140.png`, `images\GHH405141.jpeg`, `images\GHH405142.png`, `images\GHH405143.jpeg`, `images\GHH405144.png`, `images\GHH405145.jpeg`, `images\GHH405146.png`, `images\GHH405147.jpeg`
- Duplicate sources: `pages\9205.html`, `pages\22267.html`, `pages\14868.html`

### Full Text

````text
# DTC P0720 (K20C1) (17-21)

DTC P0720 : Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0720 Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -3. Test-drive the vehicle for several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit C SHAFT SPD Is any vehicle speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-3. Test-drive the vehicle for several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

C SHAFT SPD

Is any vehicle speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

Go to step 2.

- Determine possible failure area (VCC2 1 line or SG2 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Output shaft (countershaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1: Test point 2 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Output shaft (countershaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1:

Test point 2 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC2 1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC2 1 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the output shaft (countershaft) speed sensor. NO Repair an open in the VCC2 1 wire between PCM connector No. 1 terminal No. 67 and the output shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC2 1 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC2 1 wire between PCM connector No. 1 terminal No. 67 and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2.
````

## Chunk 6907: DTC P0720 (K20C1) (17-21)

- Title: DTC P0720 (K20C1) (17-21)
- Source path: `pages\7618.html`
- Chunk ID: `chunk_aecf87288321`
- Images: `images\GHH405139.png`, `images\GHH405140.png`, `images\GHH405141.jpeg`, `images\GHH405142.png`, `images\GHH405143.jpeg`, `images\GHH405144.png`, `images\GHH405145.jpeg`, `images\GHH405146.png`, `images\GHH405147.jpeg`
- Duplicate sources: `pages\9205.html`, `pages\22267.html`, `pages\14868.html`

### Full Text

````text
ut shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC2 1 wire is OK. Repair an open in the SG2 wire between PCM connector No. 1 terminal No. 58 and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC2 1 wire between PCM connector No. 1 terminal No. 67 and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the output shaft (countershaft) speed sensor .

NO

Go to step 5.

- Shorted wire check (NC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 38 Test point 2 Body ground Is there continuity? YES Repair a short in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor. NO The NC wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | PCM connector No. 1 (96P) No. 38

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor.

NO

The NC wire is not shorted. Go to step 6.

- Open wire check (NC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 38 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 38

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor.
````

## Chunk 6908: DTC P0720 (K20C2)

- Title: DTC P0720 (K20C2)
- Source path: `pages\7619.html`
- Chunk ID: `chunk_105d7b0bd9b9`
- Images: `images\GHH405148.jpeg`, `images\GHH405149.jpeg`, `images\GHH405150.jpeg`, `images\GHH405151.jpeg`
- Duplicate sources: `pages\9206.html`, `pages\22085.html`, `pages\15104.html`

### Full Text

````text
# DTC P0720 (K20C2)

DTC P0720 : Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0720 Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -3. Test-drive the vehicle several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit C SHAFT SPD Is any vehicle speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-3. Test-drive the vehicle several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

C SHAFT SPD

Is any vehicle speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Determine possible failure area (VCC1 line or SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Output shaft (countershaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector No. 1 Test point 2 Output shaft (countershaft) speed sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Output shaft (countershaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector No. 1

Test point 2 | Output shaft (countershaft) speed sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor. NO Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V ? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1.
````

## Chunk 6909: DTC P0720 (K20C2)

- Title: DTC P0720 (K20C2)
- Source path: `pages\7619.html`
- Chunk ID: `chunk_a2ec1dd04057`
- Images: `images\GHH405148.jpeg`, `images\GHH405149.jpeg`, `images\GHH405150.jpeg`, `images\GHH405151.jpeg`
- Duplicate sources: `pages\9206.html`, `pages\22085.html`, `pages\15104.html`

### Full Text

````text
No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V ? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V ?

YES

Replace the output shaft (countershaft) speed sensor .

NO

Go to step 5.

- Shorted wire check (NC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 66 Test point 2 Body ground Is there continuity? YES Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor. NO The NC wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 66

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

NO

The NC wire is not shorted. Go to step 6.

- Open wire check (NC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector No. 2 Test point 2 PCM connector E (80P) No. 66 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector No. 2

Test point 2 | PCM connector E (80P) No. 66

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.
````

## Chunk 6910: DTC P0720 (L15B7/L15BA/L15BY)

- Title: DTC P0720 (L15B7/L15BA/L15BY)
- Source path: `pages\7620.html`
- Chunk ID: `chunk_7d8b760f7ef3`
- Images: `images\GHH405152.png`, `images\GHH405153.png`, `images\GHH405154.jpeg`, `images\GHH405155.png`, `images\GHH405156.jpeg`, `images\GHH405157.png`, `images\GHH405158.jpeg`, `images\GHH405159.png`, `images\GHH405160.jpeg`
- Duplicate sources: `pages\9207.html`, `pages\22086.html`, `pages\15105.html`

### Full Text

````text
# DTC P0720 (L15B7/L15BA/L15BY)

DTC P0720 : Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0720 Output Shaft (Countershaft) Speed Sensor Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -3. Test-drive the vehicle several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit C SHAFT SPD Is any vehicle speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-3. Test-drive the vehicle several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

C SHAFT SPD

Is any vehicle speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Determine possible failure area (VCC1 line or SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Output shaft (countershaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1: Test point 2 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Output shaft (countershaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1:

Test point 2 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor. NO Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No.
````

## Chunk 6911: DTC P0720 (L15B7/L15BA/L15BY)

- Title: DTC P0720 (L15B7/L15BA/L15BY)
- Source path: `pages\7620.html`
- Chunk ID: `chunk_dcec8e0d59fe`
- Images: `images\GHH405152.png`, `images\GHH405153.png`, `images\GHH405154.jpeg`, `images\GHH405155.png`, `images\GHH405156.jpeg`, `images\GHH405157.png`, `images\GHH405158.jpeg`, `images\GHH405159.png`, `images\GHH405160.jpeg`
- Duplicate sources: `pages\9207.html`, `pages\22086.html`, `pages\15105.html`

### Full Text

````text
countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V ? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V ?

YES

Replace the output shaft (countershaft) speed sensor .

NO

Go to step 5.

- Shorted wire check (NC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 66 Test point 2 Body ground Is there continuity? YES Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor. NO The NC wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 66

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

NO

The NC wire is not shorted. Go to step 6.

- Open wire check (NC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 66 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 66

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0720 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.
````

## Chunk 6912: DTC P0721 (K20C1) (20-21)

- Title: DTC P0721 (K20C1) (20-21)
- Source path: `pages\7621.html`
- Chunk ID: `chunk_a868cb1fbd08`
- Images: `images\GHH405161.png`, `images\GHH405162.jpeg`
- Duplicate sources: `pages\9208.html`, `pages\22087.html`, `pages\15106.html`

### Full Text

````text
# DTC P0721 (K20C1) (20-21)

DTC P0721 : Output Shaft (Countershaft) Speed Sensor Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0721 Output Shaft (Countershaft) Speed Sensor Out of Range

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Vehicle Speed More than 315 km/h Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Vehicle Speed | More than 315 | km/h

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Output shaft (countershaft) speed sensor circuit connectors and terminals condition check -1. Turn the vehicle to the OFF (LOCK) mode. Check for poor connections or loose terminals at these locations: Output shaft (countershaft) speed sensor PCM Engine ground Body ground Are the connections and terminals OK? YES Go to step 3. NO Repair the connections or terminals.

-1. Turn the vehicle to the OFF (LOCK) mode.

Check for poor connections or loose terminals at these locations:

- Output shaft (countershaft) speed sensor

- PCM

- Engine ground

- Body ground

Are the connections and terminals OK?

YES

Go to step 3.

NO

Repair the connections or terminals.

- Shorted wire check (NC line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. Output shaft (countershaft) speed sensor 3P connector PCM connector No. 1 (96P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor. NO The NC wire is OK. Replace the output shaft (countershaft) speed sensor .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Output shaft (countershaft) speed sensor 3P connector

PCM connector No. 1 (96P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the NC wire between PCM connector No. 1 terminal No. 38 and the output shaft (countershaft) speed sensor.

NO

The NC wire is OK. Replace the output shaft (countershaft) speed sensor .
````

## Chunk 6913: DTC P0721 (K20C2) (19-21)

- Title: DTC P0721 (K20C2) (19-21)
- Source path: `pages\7622.html`
- Chunk ID: `chunk_364e177a04af`
- Images: `images\GHH405163.png`, `images\GHH405164.png`, `images\GHH405165.jpeg`, `images\GHH405166.png`, `images\GHH405167.jpeg`, `images\GHH405168.png`, `images\GHH405169.jpeg`, `images\GHH405170.png`, `images\GHH405171.jpeg`
- Duplicate sources: `pages\9209.html`, `pages\22088.html`, `pages\15107.html`

### Full Text

````text
# DTC P0721 (K20C2) (19-21)

DTC P0721 : Output Shaft (Countershaft) Speed Sensor Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0721 Output Shaft (Countershaft) Speed Sensor Out of Range

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -3. Test-drive the vehicle several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit C SHAFT SPD Is any vehicle speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-3. Test-drive the vehicle several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

C SHAFT SPD

Is any vehicle speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Determine possible failure area (VCC1 line or SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Output shaft (countershaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1: Test point 2 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Output shaft (countershaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1:

Test point 2 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor. NO Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6914: DTC P0721 (K20C2) (19-21)

- Title: DTC P0721 (K20C2) (19-21)
- Source path: `pages\7622.html`
- Chunk ID: `chunk_48d956388b3d`
- Images: `images\GHH405163.png`, `images\GHH405164.png`, `images\GHH405165.jpeg`, `images\GHH405166.png`, `images\GHH405167.jpeg`, `images\GHH405168.png`, `images\GHH405169.jpeg`, `images\GHH405170.png`, `images\GHH405171.jpeg`
- Duplicate sources: `pages\9209.html`, `pages\22088.html`, `pages\15107.html`

### Full Text

````text
point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V ? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V ?

YES

Replace the output shaft (countershaft) speed sensor .

NO

Go to step 5.

- Shorted wire check (NC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 66 Test point 2 Body ground Is there continuity? YES Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor. NO The NC wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 66

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

NO

The NC wire is not shorted. Go to step 6.

- Open wire check (NC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 66 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0721 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 66

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0721 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.
````

## Chunk 6915: DTC P0721 (L15B7/L15BA/L15BY) (19-21)

- Title: DTC P0721 (L15B7/L15BA/L15BY) (19-21)
- Source path: `pages\7623.html`
- Chunk ID: `chunk_baad97c7f5e2`
- Images: `images\GHH405172.png`, `images\GHH405173.png`, `images\GHH405174.jpeg`, `images\GHH405175.png`, `images\GHH405176.jpeg`, `images\GHH405177.png`, `images\GHH405178.jpeg`, `images\GHH405179.png`, `images\GHH405180.jpeg`
- Duplicate sources: `pages\9210.html`, `pages\22089.html`, `pages\15108.html`

### Full Text

````text
# DTC P0721 (L15B7/L15BA/L15BY) (19-21)

DTC P0721 : Output Shaft (Countershaft) Speed Sensor Out of Range

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0721 Output Shaft (Countershaft) Speed Sensor Out of Range

DTC (PGM-FI)

- Problem verification -1. Start the engine. -2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -3. Test-drive the vehicle several minutes. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit C SHAFT SPD Is any vehicle speed indicated? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Start the engine.

-2. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-3. Test-drive the vehicle several minutes.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

C SHAFT SPD

Is any vehicle speed indicated?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the output shaft (countershaft) speed sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Determine possible failure area (VCC1 line or SG1 line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Output shaft (countershaft) speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1: Test point 2 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Output shaft (countershaft) speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 1:

Test point 2 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Go to step 4.

NO

Go to step 3.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor. NO Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No.
````

## Chunk 6916: DTC P0721 (L15B7/L15BA/L15BY) (19-21)

- Title: DTC P0721 (L15B7/L15BA/L15BY) (19-21)
- Source path: `pages\7623.html`
- Chunk ID: `chunk_11f440080bfc`
- Images: `images\GHH405172.png`, `images\GHH405173.png`, `images\GHH405174.jpeg`, `images\GHH405175.png`, `images\GHH405176.jpeg`, `images\GHH405177.png`, `images\GHH405178.jpeg`, `images\GHH405179.png`, `images\GHH405180.jpeg`
- Duplicate sources: `pages\9210.html`, `pages\22089.html`, `pages\15108.html`

### Full Text

````text
countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

The VCC1 wire is OK. Repair an open in the SG1 wire between the PCM (E71) and the output shaft (countershaft) speed sensor.

NO

Repair an open in the VCC1 wire between the PCM (E70) and the output shaft (countershaft) speed sensor.

- Determine possible failure area (output shaft (countershaft) speed sensor, others) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Output shaft (countershaft) speed sensor 3P connector: disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V ? YES Replace the output shaft (countershaft) speed sensor . NO Go to step 5.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V ?

YES

Replace the output shaft (countershaft) speed sensor .

NO

Go to step 5.

- Shorted wire check (NC line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 66 Test point 2 Body ground Is there continuity? YES Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor. NO The NC wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 66

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

NO

The NC wire is not shorted. Go to step 6.

- Open wire check (NC line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Output shaft (countershaft) speed sensor 3P connector: disconnected PCM connector E (80P): disconnected Test point 1 Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 66 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0721 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Output shaft (countershaft) speed sensor 3P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Output shaft (countershaft) speed sensor 3P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 66

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NC wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0721 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NC wire between the PCM (E66) and the output shaft (countershaft) speed sensor.
````

## Chunk 6917: DTC P0831 (K20C1) (17-21)

- Title: DTC P0831 (K20C1) (17-21)
- Source path: `pages\7624.html`
- Chunk ID: `chunk_091b99e107cc`
- Images: `images\GHH405181.png`, `images\GHH405182.jpeg`
- Duplicate sources: `pages\9211.html`, `pages\22090.html`, `pages\14869.html`

### Full Text

````text
# DTC P0831 (K20C1) (17-21)

DTC P0831 : Clutch Pedal Position Switch A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0831 Clutch Pedal Position Switch A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A CLOSE Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Clutch pedal position switch A installation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check clutch pedal position switch A and its installation . Is it damaged or is its installation loose? YES Repair or replace clutch pedal position switch A . NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check clutch pedal position switch A and its installation .

Is it damaged or is its installation loose?

YES

Repair or replace clutch pedal position switch A .

NO

Go to step 3.

- Determine possible failure area (clutch pedal position switch A, others) -1. Disconnect the following connector. Clutch pedal position switch A 4P connector -2. Turn the vehicle to the ON mode. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A OPEN Do the current condition (s) match the threshold? YES Replace clutch pedal position switch A . NO Go to step 4.

-1. Disconnect the following connector.

Clutch pedal position switch A 4P connector

-2. Turn the vehicle to the ON mode.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | OPEN

Do the current condition (s) match the threshold?

YES

Replace clutch pedal position switch A .

NO

Go to step 4.

- Shorted wire check (CLUTCH SW (SA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Clutch pedal position switch A 4P connector: disconnected PCM connector No. 2 (58P): disconnected Test point 1 Clutch pedal position switch A 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the CLUTCH SW (SA) wire between PCM connector No. 2 terminal No. 22 and clutch pedal position switch A. NO The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector No. 2 (58P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6918: DTC P0831 (K20C1) (17-21)

- Title: DTC P0831 (K20C1) (17-21)
- Source path: `pages\7624.html`
- Chunk ID: `chunk_830857925684`
- Images: `images\GHH405181.png`, `images\GHH405182.jpeg`
- Duplicate sources: `pages\9211.html`, `pages\22090.html`, `pages\14869.html`

### Full Text

````text
ion switch A. NO The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector No. 2 (58P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the CLUTCH SW (SA) wire between PCM connector No. 2 terminal No. 22 and clutch pedal position switch A.

NO

The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6919: DTC P0831 (K20C2)

- Title: DTC P0831 (K20C2)
- Source path: `pages\7625.html`
- Chunk ID: `chunk_cb3cd55ae6b1`
- Images: `images\GHH405183.jpeg`
- Duplicate sources: `pages\9212.html`, `pages\22091.html`, `pages\15109.html`

### Full Text

````text
# DTC P0831 (K20C2)

DTC P0831 : Clutch Pedal Position Switch A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0831 Clutch Pedal Position Switch A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A CLOSE Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Clutch pedal position switch A check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check clutch pedal position switch A and its installation . Is it damaged, or is its installation loose? YES Repair or replace clutch pedal position switch A . NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check clutch pedal position switch A and its installation .

Is it damaged, or is its installation loose?

YES

Repair or replace clutch pedal position switch A .

NO

Go to step 3.

- Determine possible failure area (clutch pedal position switch A, others) -1. Disconnect the following connector. Clutch pedal position switch A 4P connector -2. Turn the vehicle to the ON mode. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A OPEN Do the current condition (s) match the threshold? YES Replace clutch pedal position switch A . NO Go to step 4.

-1. Disconnect the following connector.

Clutch pedal position switch A 4P connector

-2. Turn the vehicle to the ON mode.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | OPEN

Do the current condition (s) match the threshold?

YES

Replace clutch pedal position switch A .

NO

Go to step 4.

- Shorted wire check (CLUTCH SW (SA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector A (50P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Clutch pedal position switch A 4P connector: disconnected PCM connector A (50P): disconnected Test point 1 Clutch pedal position switch A 4P connector No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the CLUTCH SW (SA) wire between the PCM (A21) and clutch pedal position switch A. NO The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES
````

## Chunk 6920: DTC P0831 (K20C2)

- Title: DTC P0831 (K20C2)
- Source path: `pages\7625.html`
- Chunk ID: `chunk_692ac1260438`
- Images: `images\GHH405183.jpeg`
- Duplicate sources: `pages\9212.html`, `pages\22091.html`, `pages\15109.html`

### Full Text

````text
tion switch A. NO The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the CLUTCH SW (SA) wire between the PCM (A21) and clutch pedal position switch A.

NO

The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6921: DTC P0831 (L15B7/L15BA/L15BY)

- Title: DTC P0831 (L15B7/L15BA/L15BY)
- Source path: `pages\7626.html`
- Chunk ID: `chunk_84bd9da478c4`
- Images: `images\GHH405184.png`, `images\GHH405185.jpeg`
- Duplicate sources: `pages\9213.html`, `pages\22092.html`, `pages\15110.html`

### Full Text

````text
# DTC P0831 (L15B7/L15BA/L15BY)

DTC P0831 : Clutch Pedal Position Switch A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0831 Clutch Pedal Position Switch A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A CLOSE Do the current condition (s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | CLOSE

Do the current condition (s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at clutch pedal position switch A and the PCM, and check the installation of clutch pedal position switch A. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Clutch pedal position switch A check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check clutch pedal position switch A and its installation . Is it damaged, or is its installation loose? YES Repair or replace clutch pedal position switch A . NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check clutch pedal position switch A and its installation .

Is it damaged, or is its installation loose?

YES

Repair or replace clutch pedal position switch A .

NO

Go to step 3.

- Determine possible failure area (clutch pedal position switch A, others) -1. Disconnect the following connector. Clutch pedal position switch A 4P connector -2. Turn the vehicle to the ON mode. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CLUTCH PEDAL POSITION SWITCH A OPEN Do the current condition (s) match the threshold? YES Replace clutch pedal position switch A . NO Go to step 4.

-1. Disconnect the following connector.

Clutch pedal position switch A 4P connector

-2. Turn the vehicle to the ON mode.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CLUTCH PEDAL POSITION SWITCH A | OPEN

Do the current condition (s) match the threshold?

YES

Replace clutch pedal position switch A .

NO

Go to step 4.

- Shorted wire check (CLUTCH SW (SA) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector A (50P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Clutch pedal position switch A 4P connector: disconnected PCM connector A (50P): disconnected Test point 1 Clutch pedal position switch A 4P connector (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the CLUTCH SW (SA) wire between the PCM (A21) and clutch pedal position switch A. NO The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES
````

## Chunk 6922: DTC P0831 (L15B7/L15BA/L15BY)

- Title: DTC P0831 (L15B7/L15BA/L15BY)
- Source path: `pages\7626.html`
- Chunk ID: `chunk_2edc959faf65`
- Images: `images\GHH405184.png`, `images\GHH405185.jpeg`
- Duplicate sources: `pages\9213.html`, `pages\22092.html`, `pages\15110.html`

### Full Text

````text
e CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Clutch pedal position switch A 4P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Clutch pedal position switch A 4P connector (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the CLUTCH SW (SA) wire between the PCM (A21) and clutch pedal position switch A.

NO

The CLUTCH SW (SA) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0831 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6923: DTC P0850 (K20C1) (17-21)

- Title: DTC P0850 (K20C1) (17-21)
- Source path: `pages\7627.html`
- Chunk ID: `chunk_066aed2b60ad`
- Images: none
- Duplicate sources: `pages\9214.html`, `pages\22093.html`, `pages\14870.html`

### Full Text

````text
# DTC P0850 (K20C1) (17-21)

DTC P0850 : Neutral Position Sensor A/B Incorrect Voltage Correlation

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Move the shift lever to all driving position, then move it to the neutral position. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation Is DTC P0850 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Move the shift lever to all driving position, then move it to the neutral position.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

Is DTC P0850 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (neutral position sensor, others) -1. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit NEUTRAL POSITION SENSOR 1 NEUTRAL POSITION SENSOR 2 Are they the same voltage? YES Go to step 3. NO Replace the neutral position sensor .

-1. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

NEUTRAL POSITION SENSOR 1

NEUTRAL POSITION SENSOR 2

Are they the same voltage?

YES

Go to step 3.

NO

Replace the neutral position sensor .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Test point 1 PCM connector No. 1 (96P) No. 28 Test point 2 PCM connector No. 1 (96P) No. 30 Is there continuity? YES Go to step 4. NO The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Test point 1 | PCM connector No. 1 (96P) No. 28

Test point 2 | PCM connector No. 1 (96P) No. 30

Is there continuity?

YES

Go to step 4.

NO

The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (NSS1 line to NSS2 line) -1. Disconnect the following connector. Neutral position sensor 4P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Neutral position sensor 4P connector: disconnected Test point 1 PCM connector No. 1 (96P) No. 28 Test point 2 PCM connector No. 1 (96P) No. 30 Is there continuity? YES Repair a short in the NSS1 wire to the NSS2 wire between PCM and the neutral position sensor. NO The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .

-1. Disconnect the following connector.

Neutral position sensor 4P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No.
````

## Chunk 6924: DTC P0850 (K20C1) (17-21)

- Title: DTC P0850 (K20C1) (17-21)
- Source path: `pages\7627.html`
- Chunk ID: `chunk_e48cc9cf1b2a`
- Images: none
- Duplicate sources: `pages\9214.html`, `pages\22093.html`, `pages\14870.html`

### Full Text

````text
PCM .

- Shorted wire check (NSS1 line to NSS2 line) -1. Disconnect the following connector. Neutral position sensor 4P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 1 (96P): disconnected Neutral position sensor 4P connector: disconnected Test point 1 PCM connector No. 1 (96P) No. 28 Test point 2 PCM connector No. 1 (96P) No. 30 Is there continuity? YES Repair a short in the NSS1 wire to the NSS2 wire between PCM and the neutral position sensor. NO The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .

-1. Disconnect the following connector.

Neutral position sensor 4P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 1 (96P): disconnected

Neutral position sensor 4P connector: disconnected

Test point 1 | PCM connector No. 1 (96P) No. 28

Test point 2 | PCM connector No. 1 (96P) No. 30

Is there continuity?

YES

Repair a short in the NSS1 wire to the NSS2 wire between PCM and the neutral position sensor.

NO

The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .
````

## Chunk 6925: DTC P0850 (K20C2)

- Title: DTC P0850 (K20C2)
- Source path: `pages\7628.html`
- Chunk ID: `chunk_400a21a970e7`
- Images: none
- Duplicate sources: `pages\9215.html`, `pages\22094.html`, `pages\15111.html`

### Full Text

````text
# DTC P0850 (K20C2)

DTC P0850 : Neutral Position Sensor A/B Incorrect Voltage Correlation

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Move the shift lever to all driving position, then move it to the neutral position. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation Is DTC P0850 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Move the shift lever to all driving position, then move it to the neutral position.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

Is DTC P0850 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (neutral position sensor, others) -1. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Neutral Position Sensor 2 Are they the same voltage? YES Go to step 3. NO Replace the neutral position sensor .

-1. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Neutral Position Sensor 2

Are they the same voltage?

YES

Go to step 3.

NO

Replace the neutral position sensor .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 PCM connector E (80P) No. 68 Is there continuity? YES Go to step 4. NO The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 67

Test point 2 | PCM connector E (80P) No. 68

Is there continuity?

YES

Go to step 4.

NO

The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (NSS1 line to NSS2 line) -1. Disconnect the following connector. Neutral position sensor 4P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Neutral position sensor 4P connector: disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 PCM connector E (80P) No. 68 Is there continuity? YES Repair a short in the NSS1 wire to NSS2 wire between the PCM and the neutral position sensor. NO The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .

-1. Disconnect the following connector.

Neutral position sensor 4P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected
````

## Chunk 6926: DTC P0850 (K20C2)

- Title: DTC P0850 (K20C2)
- Source path: `pages\7628.html`
- Chunk ID: `chunk_4061f96d731f`
- Images: none
- Duplicate sources: `pages\7629.html`, `pages\9215.html`, `pages\9216.html`, `pages\22094.html`, `pages\22095.html`, `pages\15111.html`, `pages\15112.html`

### Full Text

````text
- Shorted wire check (NSS1 line to NSS2 line) -1. Disconnect the following connector. Neutral position sensor 4P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Neutral position sensor 4P connector: disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 PCM connector E (80P) No. 68 Is there continuity? YES Repair a short in the NSS1 wire to NSS2 wire between the PCM and the neutral position sensor. NO The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .

-1. Disconnect the following connector.

Neutral position sensor 4P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Neutral position sensor 4P connector: disconnected

Test point 1 | PCM connector E (80P) No. 67

Test point 2 | PCM connector E (80P) No. 68

Is there continuity?

YES

Repair a short in the NSS1 wire to NSS2 wire between the PCM and the neutral position sensor.

NO

The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .
````

## Chunk 6927: DTC P0850 (L15B7/L15BA/L15BY)

- Title: DTC P0850 (L15B7/L15BA/L15BY)
- Source path: `pages\7629.html`
- Chunk ID: `chunk_6f3454644341`
- Images: none
- Duplicate sources: `pages\9216.html`, `pages\22095.html`, `pages\15112.html`

### Full Text

````text
# DTC P0850 (L15B7/L15BA/L15BY)

DTC P0850 : Neutral Position Sensor A/B Incorrect Voltage Correlation

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Move the shift lever to all driving position, then move it to the neutral position. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation Is DTC P0850 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Move the shift lever to all driving position, then move it to the neutral position.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0850 Neutral Position Sensor A/B Incorrect Voltage Correlation

Is DTC P0850 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (neutral position sensor, others) -1. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Neutral Position Sensor 2 Are they the same voltage? YES Go to step 3. NO Replace the neutral position sensor .

-1. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Neutral Position Sensor 2

Are they the same voltage?

YES

Go to step 3.

NO

Replace the neutral position sensor .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 PCM connector E (80P) No. 68 Is there continuity? YES Go to step 4. NO The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 67

Test point 2 | PCM connector E (80P) No. 68

Is there continuity?

YES

Go to step 4.

NO

The NSS1 wire and the NSS2 wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0850 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (NSS1 line to NSS2 line) -1. Disconnect the following connector. Neutral position sensor 4P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector E (80P): disconnected Neutral position sensor 4P connector: disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 PCM connector E (80P) No. 68 Is there continuity? YES Repair a short in the NSS1 wire to NSS2 wire between the PCM and the neutral position sensor. NO The NSS1 wire and the NSS2 wire are OK. Replace the neutral position sensor .

-1. Disconnect the following connector.

Neutral position sensor 4P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector E (80P): disconnected
````

## Chunk 6928: DTC P0851 (K20C1) (17-21)

- Title: DTC P0851 (K20C1) (17-21)
- Source path: `pages\7630.html`
- Chunk ID: `chunk_13c4196ade36`
- Images: `images\GHH405186.png`, `images\GHH405187.jpeg`, `images\GHH405188.png`, `images\GHH405189.jpeg`, `images\GHH405190.png`, `images\GHH405191.png`, `images\GHH405192.jpeg`, `images\GHH405193.png`, `images\GHH405194.jpeg`, `images\GHH405195.png`, `images\GHH405196.jpeg`
- Duplicate sources: `pages\9217.html`, `pages\22096.html`, `pages\14871.html`

### Full Text

````text
# DTC P0851 (K20C1) (17-21)

DTC P0851 : Neutral Position Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage Is DTC P0851 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

Is DTC P0851 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage P1707 Neutral Position Sensor B Circuit Low Voltage Are DTC P0851 and P1707 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

P1707 Neutral Position Sensor B Circuit Low Voltage

Are DTC P0851 and P1707 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (VCC1 NSS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 62 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC1 NSS wire between PCM connector No. 1 terminal No. 62 and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected
````

## Chunk 6929: DTC P0851 (K20C1) (17-21)

- Title: DTC P0851 (K20C1) (17-21)
- Source path: `pages\7630.html`
- Chunk ID: `chunk_4a5152ff5971`
- Images: `images\GHH405186.png`, `images\GHH405187.jpeg`, `images\GHH405188.png`, `images\GHH405189.jpeg`, `images\GHH405190.png`, `images\GHH405191.png`, `images\GHH405192.jpeg`, `images\GHH405193.png`, `images\GHH405194.jpeg`, `images\GHH405195.png`, `images\GHH405196.jpeg`
- Duplicate sources: `pages\9217.html`, `pages\22096.html`, `pages\14871.html`

### Full Text

````text
62 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC1 NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC1 NSS wire between PCM connector No. 1 terminal No. 62 and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 62

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC1 NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC1 NSS wire between PCM connector No. 1 terminal No. 62 and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Neutral position sensor 4P connector (female terminals) No. 1: Terminal B Neutral position sensor 4P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit NEUTRAL POSITION SENSOR 1 Is about 5 V indicated? YES Replace the neutral position sensor . NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Neutral position sensor 4P connector (female terminals) No. 1:

Terminal B | Neutral position sensor 4P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

NEUTRAL POSITION SENSOR 1

Is about 5 V indicated?

YES

Replace the neutral position sensor .

NO

Go to step 6.

- Open wire check (NSS1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 PCM connector No. 1 (96P) No. 30 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NSS1 wire is not open. Go to step 7. NO Repair an open in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | PCM connector No. 1 (96P) No. 30

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NSS1 wire is not open. Go to step 7.

NO

Repair an open in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor.

- Shorted wire check (NSS1 wire) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the NSS1 wire between PCM connector No.
````

## Chunk 6930: DTC P0851 (K20C1) (17-21)

- Title: DTC P0851 (K20C1) (17-21)
- Source path: `pages\7630.html`
- Chunk ID: `chunk_602d181df212`
- Images: `images\GHH405186.png`, `images\GHH405187.jpeg`, `images\GHH405188.png`, `images\GHH405189.jpeg`, `images\GHH405190.png`, `images\GHH405191.png`, `images\GHH405192.jpeg`, `images\GHH405193.png`, `images\GHH405194.jpeg`, `images\GHH405195.png`, `images\GHH405196.jpeg`
- Duplicate sources: `pages\9217.html`, `pages\22096.html`, `pages\14871.html`

### Full Text

````text
1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | PCM connector No. 1 (96P) No. 30

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NSS1 wire is not open. Go to step 7.

NO

Repair an open in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor.

- Shorted wire check (NSS1 wire) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor. NO The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor.

NO

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6931: DTC P0851 (K20C2)

- Title: DTC P0851 (K20C2)
- Source path: `pages\7631.html`
- Chunk ID: `chunk_976ef749fc4c`
- Images: `images\GHH405197.jpeg`, `images\GHH405198.jpeg`, `images\GHH405199.jpeg`, `images\GHH405200.jpeg`, `images\GHH405201.jpeg`
- Duplicate sources: `pages\9218.html`, `pages\22097.html`, `pages\15113.html`

### Full Text

````text
# DTC P0851 (K20C2)

DTC P0851 : Neutral Position Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage Is DTC P0851 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

Is DTC P0851 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage P1707 Neutral Position Sensor B Circuit Low Voltage Are DTC P0851 and P1707 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

P1707 Neutral Position Sensor B Circuit Low Voltage

Are DTC P0851 and P1707 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (VCC2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 1 Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 1

Test point 2 | PCM connector E (80P) No. 77

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 6932: DTC P0851 (K20C2)

- Title: DTC P0851 (K20C2)
- Source path: `pages\7631.html`
- Chunk ID: `chunk_fb6506639fed`
- Images: `images\GHH405197.jpeg`, `images\GHH405198.jpeg`, `images\GHH405199.jpeg`, `images\GHH405200.jpeg`, `images\GHH405201.jpeg`
- Duplicate sources: `pages\9218.html`, `pages\22097.html`, `pages\15113.html`

### Full Text

````text
horized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 1

Test point 2 | PCM connector E (80P) No. 77

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Neutral position sensor 4P connector No. 1 Terminal B Neutral position sensor 4P connector No. 3 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Is about 5.0 V indicated? YES Replace the neutral position sensor . NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Neutral position sensor 4P connector No. 1

Terminal B | Neutral position sensor 4P connector No. 3

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Is about 5.0 V indicated?

YES

Replace the neutral position sensor .

NO

Go to step 6.

- Shorted wire check (NSS1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the neutral position sensor 4P connector. -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector E (80P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor. NO The NSS1 wire is not shorted. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the neutral position sensor 4P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector E (80P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is not shorted. Go to step 7.

- Open wire check (NSS1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 3 Test point 2 PCM connector E (80P) No. 67 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6933: DTC P0851 (K20C2)

- Title: DTC P0851 (K20C2)
- Source path: `pages\7631.html`
- Chunk ID: `chunk_da3a34354125`
- Images: `images\GHH405197.jpeg`, `images\GHH405198.jpeg`, `images\GHH405199.jpeg`, `images\GHH405200.jpeg`, `images\GHH405201.jpeg`
- Duplicate sources: `pages\9218.html`, `pages\22097.html`, `pages\15113.html`

### Full Text

````text
f HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is not shorted. Go to step 7.

- Open wire check (NSS1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 3 Test point 2 PCM connector E (80P) No. 67 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NSS1 wire between the PCM (E67) and the neutral position sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 3

Test point 2 | PCM connector E (80P) No. 67

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NSS1 wire between the PCM (E67) and the neutral position sensor.
````

## Chunk 6934: DTC P0851 (L15B7/L15BA/L15BY)

- Title: DTC P0851 (L15B7/L15BA/L15BY)
- Source path: `pages\7632.html`
- Chunk ID: `chunk_77e87286dd5f`
- Images: `images\GHH405202.png`, `images\GHH405203.jpeg`, `images\GHH405204.png`, `images\GHH405205.jpeg`, `images\GHH405206.png`, `images\GHH405207.png`, `images\GHH405208.jpeg`, `images\GHH405209.png`, `images\GHH405210.jpeg`, `images\GHH405211.png`, `images\GHH405212.jpeg`
- Duplicate sources: `pages\9219.html`, `pages\22098.html`, `pages\15114.html`

### Full Text

````text
# DTC P0851 (L15B7/L15BA/L15BY)

DTC P0851 : Neutral Position Sensor A Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage Is DTC P0851 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

Is DTC P0851 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0851 Neutral Position Sensor A Circuit Low Voltage P1707 Neutral Position Sensor B Circuit Low Voltage Are DTC P0851 and P1707 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0851 Neutral Position Sensor A Circuit Low Voltage

P1707 Neutral Position Sensor B Circuit Low Voltage

Are DTC P0851 and P1707 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (VCC2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 PCM connector E (80P) No. 77 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The VCC2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No.
````

## Chunk 6935: DTC P0851 (L15B7/L15BA/L15BY)

- Title: DTC P0851 (L15B7/L15BA/L15BY)
- Source path: `pages\7632.html`
- Chunk ID: `chunk_f9ee884b8a66`
- Images: `images\GHH405202.png`, `images\GHH405203.jpeg`, `images\GHH405204.png`, `images\GHH405205.jpeg`, `images\GHH405206.png`, `images\GHH405207.png`, `images\GHH405208.jpeg`, `images\GHH405209.png`, `images\GHH405210.jpeg`, `images\GHH405211.png`, `images\GHH405212.jpeg`
- Duplicate sources: `pages\9219.html`, `pages\22098.html`, `pages\15114.html`

### Full Text

````text
s there continuity? YES The VCC2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | PCM connector E (80P) No. 77

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The VCC2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the VCC2 wire between the PCM (E77) and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Connect terminals A and B with a jumper wire. Terminal A Neutral position sensor 4P connector (female terminals) No. 1: Terminal B Neutral position sensor 4P connector female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Is about 5.0 V indicated? YES Replace the neutral position sensor . NO Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Neutral position sensor 4P connector (female terminals) No. 1:

Terminal B | Neutral position sensor 4P connector female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Is about 5.0 V indicated?

YES

Replace the neutral position sensor .

NO

Go to step 6.

- Shorted wire check (NSS1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire from the neutral position sensor 4P connector. -3. Jump the SCS line with the HDS, and wait more than 1 minute. -4. Disconnect the following connector. PCM connector E (80P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor. NO The NSS1 wire is not shorted. Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire from the neutral position sensor 4P connector.

-3. Jump the SCS line with the HDS, and wait more than 1 minute.

-4. Disconnect the following connector.

PCM connector E (80P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is not shorted. Go to step 7.

- Open wire check (NSS1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 67 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NSS1 wire is OK.
````

## Chunk 6936: DTC P0851 (L15B7/L15BA/L15BY)

- Title: DTC P0851 (L15B7/L15BA/L15BY)
- Source path: `pages\7632.html`
- Chunk ID: `chunk_439e549c8065`
- Images: `images\GHH405202.png`, `images\GHH405203.jpeg`, `images\GHH405204.png`, `images\GHH405205.jpeg`, `images\GHH405206.png`, `images\GHH405207.png`, `images\GHH405208.jpeg`, `images\GHH405209.png`, `images\GHH405210.jpeg`, `images\GHH405211.png`, `images\GHH405212.jpeg`
- Duplicate sources: `pages\9219.html`, `pages\22098.html`, `pages\15114.html`

### Full Text

````text
Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is not shorted. Go to step 7.

- Open wire check (NSS1 line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 PCM connector E (80P) No. 67 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the NSS1 wire between the PCM (E67) and the neutral position sensor.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | PCM connector E (80P) No. 67

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0851 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the NSS1 wire between the PCM (E67) and the neutral position sensor.
````

## Chunk 6937: DTC P0852 (K20C1) (17-21)

- Title: DTC P0852 (K20C1) (17-21)
- Source path: `pages\7633.html`
- Chunk ID: `chunk_6b69d3506a05`
- Images: `images\GHH405213.png`, `images\GHH405214.png`, `images\GHH405215.jpeg`, `images\GHH405216.png`, `images\GHH405217.jpeg`, `images\GHH405218.png`, `images\GHH405219.jpeg`
- Duplicate sources: `pages\9220.html`, `pages\22099.html`, `pages\14872.html`

### Full Text

````text
# DTC P0852 (K20C1) (17-21)

DTC P0852 : Neutral Position Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage Is DTC P0852 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

Is DTC P0852 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage P1708 Neutral Position Sensor B Circuit High Voltage Are DTC P0852 and P1708 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

P1708 Neutral Position Sensor B Circuit High Voltage

Are DTC P0852 and P1708 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 Neutral position sensor 4P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | Neutral position sensor 4P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (SG NSS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 84 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG NSS wire between PCM connector No. 1 terminal No. 84 and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode
````

## Chunk 6938: DTC P0852 (K20C1) (17-21)

- Title: DTC P0852 (K20C1) (17-21)
- Source path: `pages\7633.html`
- Chunk ID: `chunk_dd0728468efb`
- Images: `images\GHH405213.png`, `images\GHH405214.png`, `images\GHH405215.jpeg`, `images\GHH405216.png`, `images\GHH405217.jpeg`, `images\GHH405218.png`, `images\GHH405219.jpeg`
- Duplicate sources: `pages\9220.html`, `pages\22099.html`, `pages\14872.html`

### Full Text

````text
position sensor 4P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 84 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG NSS wire between PCM connector No. 1 terminal No. 84 and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 84

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG NSS wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG NSS wire between PCM connector No. 1 terminal No. 84 and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit NEUTRAL POSITION SENSOR 1 Is any voltage indicated? YES Go to step 6. NO Replace the neutral position sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

NEUTRAL POSITION SENSOR 1

Is any voltage indicated?

YES

Go to step 6.

NO

Replace the neutral position sensor .

- Shorted wire check (NSS1 line to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector No. 1 (96P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor. NO The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector No. 1 (96P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the NSS1 wire between PCM connector No. 1 terminal No. 30 and the neutral position sensor.

NO

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6939: DTC P0852 (K20C2)

- Title: DTC P0852 (K20C2)
- Source path: `pages\7634.html`
- Chunk ID: `chunk_2213b9375cd5`
- Images: `images\GHH405220.jpeg`, `images\GHH405221.jpeg`, `images\GHH405222.jpeg`
- Duplicate sources: `pages\9221.html`, `pages\22100.html`, `pages\15115.html`

### Full Text

````text
# DTC P0852 (K20C2)

DTC P0852 : Neutral Position Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage Is DTC P0852 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

Is DTC P0852 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage P1708 Neutral Position Sensor B Circuit High Voltage Are DTC P0852 and P1708 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

P1708 Neutral Position Sensor B Circuit High Voltage

Are DTC P0852 and P1708 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector No. 1 Test point 2 Neutral position sensor 4P connector No. 2 Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector No. 1

Test point 2 | Neutral position sensor 4P connector No. 2

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 2 Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 2
````

## Chunk 6940: DTC P0852 (K20C2)

- Title: DTC P0852 (K20C2)
- Source path: `pages\7634.html`
- Chunk ID: `chunk_5922c02e5aa7`
- Images: `images\GHH405220.jpeg`, `images\GHH405221.jpeg`, `images\GHH405222.jpeg`
- Duplicate sources: `pages\9221.html`, `pages\22100.html`, `pages\15115.html`

### Full Text

````text
DA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 2

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Is any voltage indicated? YES Go to step 6. NO Replace the neutral position sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Is any voltage indicated?

YES

Go to step 6.

NO

Replace the neutral position sensor .

- Shorted wire check (NSS1 line to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the NSS1 wire between the PCM (E67) and the neutral position sensor. NO The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6941: DTC P0852 (L15B7/L15BA/L15BY)

- Title: DTC P0852 (L15B7/L15BA/L15BY)
- Source path: `pages\7635.html`
- Chunk ID: `chunk_17cb267182bd`
- Images: `images\GHH405223.png`, `images\GHH405224.png`, `images\GHH405225.jpeg`, `images\GHH405226.png`, `images\GHH405227.jpeg`, `images\GHH405228.png`, `images\GHH405229.jpeg`
- Duplicate sources: `pages\9222.html`, `pages\22101.html`, `pages\15116.html`

### Full Text

````text
# DTC P0852 (L15B7/L15BA/L15BY)

DTC P0852 : Neutral Position Sensor A Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage Is DTC P0852 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

Is DTC P0852 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the neutral position sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0852 Neutral Position Sensor A Circuit High Voltage P1708 Neutral Position Sensor B Circuit High Voltage Are DTC P0852 and P1708 indicated at the same time? YES Go to step 3. NO Go to step 5.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0852 Neutral Position Sensor A Circuit High Voltage

P1708 Neutral Position Sensor B Circuit High Voltage

Are DTC P0852 and P1708 indicated at the same time?

YES

Go to step 3.

NO

Go to step 5.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 1: Test point 2 Neutral position sensor 4P connector (female terminals) No. 2: Courtesy of HONDA, U.S.A., INC. Is there about 5.0 V? YES Replace the neutral position sensor . NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 1:

Test point 2 | Neutral position sensor 4P connector (female terminals) No. 2:

Courtesy of HONDA, U.S.A., INC.

Is there about 5.0 V?

YES

Replace the neutral position sensor .

NO

Go to step 4.

- Open wire check (SG2 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected
````

## Chunk 6942: DTC P0852 (L15B7/L15BA/L15BY)

- Title: DTC P0852 (L15B7/L15BA/L15BY)
- Source path: `pages\7635.html`
- Chunk ID: `chunk_f263989fda54`
- Images: `images\GHH405223.png`, `images\GHH405224.png`, `images\GHH405225.jpeg`, `images\GHH405226.png`, `images\GHH405227.jpeg`, `images\GHH405228.png`, `images\GHH405229.jpeg`
- Duplicate sources: `pages\9222.html`, `pages\22101.html`, `pages\15116.html`

### Full Text

````text
4P connector (female terminals) No. 2: Test point 2 PCM connector E (80P) No. 78 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 2:

Test point 2 | PCM connector E (80P) No. 78

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SG2 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the SG2 wire between the PCM (E78) and the neutral position sensor.

- Determine possible failure area (neutral position sensor, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Neutral position sensor 4P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit Neutral Position Sensor 1 Is any voltage indicated? YES Go to step 6. NO Replace the neutral position sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Neutral position sensor 4P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Neutral Position Sensor 1

Is any voltage indicated?

YES

Go to step 6.

NO

Replace the neutral position sensor .

- Shorted wire check (NSS1 line to power) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connector. PCM connector E (80P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Neutral position sensor 4P connector: disconnected PCM connector E (80P): disconnected Test point 1 Neutral position sensor 4P connector (female terminals) No. 3: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there any voltage? YES Repair a short to power in the NSS1 wire between the PCM (E67) and the neutral position sensor. NO The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connector.

PCM connector E (80P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Neutral position sensor 4P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | Neutral position sensor 4P connector (female terminals) No. 3:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there any voltage?

YES

Repair a short to power in the NSS1 wire between the PCM (E67) and the neutral position sensor.

NO

The NSS1 wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0852 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6943: DTC P0864 (K20C2) (19-21)

- Title: DTC P0864 (K20C2) (19-21)
- Source path: `pages\7636.html`
- Chunk ID: `chunk_7a353b1e6b87`
- Images: none
- Duplicate sources: `pages\9223.html`, `pages\22102.html`, `pages\15117.html`

### Full Text

````text
# DTC P0864 (K20C2) (19-21)

DTC P0864 : PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- According to the detected DTC (s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the PCM.

DTC Description | Confirmed DTC | Pending DTC

P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM)) Is DTC P0864 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the TCM and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

Is DTC P0864 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the TCM and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CVT system check -1. Check for communication to the CVT system with the HDS. Does the HDS communicate with the CVT system? YES Go to step 3. NO Go to the symptom troubleshooting for CVT system .

-1. Check for communication to the CVT system with the HDS.

Does the HDS communicate with the CVT system?

YES

Go to step 3.

NO

Go to the symptom troubleshooting for CVT system .

- Open wire check (TM-CAN_H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 4 Test point 2 PCM connector A (50P) No. 21 Is there continuity? YES The TM-CAN_H wire is OK. Go to step 4. NO Repair an open in the TM-CAN_H wire between the PCM (A21) and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 4

Test point 2 | PCM connector A (50P) No. 21

Is there continuity?

YES

The TM-CAN_H wire is OK. Go to step 4.

NO

Repair an open in the TM-CAN_H wire between the PCM (A21) and the TCM.

- Open wire check (TM-CAN_L line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 12 Test point 2 PCM connector A (50P) No. 20 Is there continuity? YES The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0864 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TM-CAN_L wire between the PCM (A20) and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | PCM connector A (50P) No. 20

Is there continuity?

YES

The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6944: DTC P0864 (K20C2) (19-21)

- Title: DTC P0864 (K20C2) (19-21)
- Source path: `pages\7636.html`
- Chunk ID: `chunk_1ff2dae519f4`
- Images: none
- Duplicate sources: `pages\7637.html`, `pages\9223.html`, `pages\9224.html`, `pages\22102.html`, `pages\22103.html`, `pages\15117.html`, `pages\15118.html`

### Full Text

````text
re continuity? YES The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0864 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TM-CAN_L wire between the PCM (A20) and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | PCM connector A (50P) No. 20

Is there continuity?

YES

The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0864 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the TM-CAN_L wire between the PCM (A20) and the TCM.
````

## Chunk 6945: DTC P0864 (L15B7/L15BA/L15BY) (19-21)

- Title: DTC P0864 (L15B7/L15BA/L15BY) (19-21)
- Source path: `pages\7637.html`
- Chunk ID: `chunk_c93e790713d1`
- Images: none
- Duplicate sources: `pages\9224.html`, `pages\22103.html`, `pages\15118.html`

### Full Text

````text
# DTC P0864 (L15B7/L15BA/L15BY) (19-21)

DTC P0864 : PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- According to the detected DTC (s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the PCM.

DTC Description | Confirmed DTC | Pending DTC

P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM)) Is DTC P0864 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the TCM and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0864 PT-CAN Malfunction (PCM-Transmission Control Module (TCM))

Is DTC P0864 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the TCM and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- CVT system check -1. Check for communication to the CVT system with the HDS. Does the HDS communicate with the CVT system? YES Go to step 3. NO Go to the symptom troubleshooting for CVT system .

-1. Check for communication to the CVT system with the HDS.

Does the HDS communicate with the CVT system?

YES

Go to step 3.

NO

Go to the symptom troubleshooting for CVT system .

- Open wire check (TM-CAN_H line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. PCM connector A (50P) TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 4 Test point 2 PCM connector A (50P) No. 21 Is there continuity? YES The TM-CAN_H wire is OK. Go to step 4. NO Repair an open in the TM-CAN_H wire between the PCM (A21) and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

PCM connector A (50P)

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 4

Test point 2 | PCM connector A (50P) No. 21

Is there continuity?

YES

The TM-CAN_H wire is OK. Go to step 4.

NO

Repair an open in the TM-CAN_H wire between the PCM (A21) and the TCM.

- Open wire check (TM-CAN_L line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 12 Test point 2 PCM connector A (50P) No. 20 Is there continuity? YES The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P0864 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the TM-CAN_L wire between the PCM (A20) and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | PCM connector A (50P) No. 20

Is there continuity?

YES

The TM-CAN_L wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6946: DTC P1009 (K20C2)

- Title: DTC P1009 (K20C2)
- Source path: `pages\7638.html`
- Chunk ID: `chunk_46c60e948566`
- Images: none
- Duplicate sources: `pages\9225.html`, `pages\22104.html`, `pages\15119.html`

### Full Text

````text
# DTC P1009 (K20C2)

DTC P1009 : VTC A Advance Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0341 is stored at the same time as DTC P1009, troubleshoot DTC P1009 first, then recheck for DTC P0341.

- If DTC P1009 set after replacing the VTC actuator, verify that the correct timing marks on the crank pulley were used.

DTC Description | Confirmed DTC | Pending DTC

P1009 VTC A Advance Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1009 VTC A Advance Malfunction Is DTC P1009 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1009 VTC A Advance Malfunction

Is DTC P1009 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- VTC oil control solenoid valve A operation check -1. Test VTC oil control solenoid valve A . Is the solenoid valve OK? YES Go to step 3. NO Replace VTC oil control solenoid valve A .

-1. Test VTC oil control solenoid valve A .

Is the solenoid valve OK?

YES

Go to step 3.

NO

Replace VTC oil control solenoid valve A .

- VTC actuator A check -1. Inspect VTC actuator A . Is the actuator OK? YES Check the VTC system oil passages and clean them if needed. NO Replace VTC actuator A .

-1. Inspect VTC actuator A .

Is the actuator OK?

YES

Check the VTC system oil passages and clean them if needed.

NO

Replace VTC actuator A .
````

## Chunk 6947: DTC P1009 (L15B7/L15BA/L15BY)

- Title: DTC P1009 (L15B7/L15BA/L15BY)
- Source path: `pages\7639.html`
- Chunk ID: `chunk_8519549a7493`
- Images: none
- Duplicate sources: `pages\9226.html`, `pages\22105.html`, `pages\15120.html`

### Full Text

````text
# DTC P1009 (L15B7/L15BA/L15BY)

DTC P1009 : VTC A Advance Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0341 is stored at the same time as DTC P1009, troubleshoot DTC P1009 first, then recheck for DTC P0341.

- If DTC P1009 set after replacing the VTC actuator, verify that the correct timing marks on the crank pulley were used.

DTC Description | Confirmed DTC | Pending DTC

P1009 VTC A Advance Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1009 VTC A Advance Malfunction Is DTC P1009 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1009 VTC A Advance Malfunction

Is DTC P1009 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- VTC oil control solenoid valve operation check -1. Test VTC oil control solenoid valve A . Is the solenoid valve OK? YES Go to step 3. NO Replace VTC oil control solenoid valve A .

-1. Test VTC oil control solenoid valve A .

Is the solenoid valve OK?

YES

Go to step 3.

NO

Replace VTC oil control solenoid valve A .

- VTC actuator A check -1. Inspect VTC actuator A . Is the actuator OK? YES Check the VTC system oil passages and clean them if needed. NO Replace VTC actuator A .

-1. Inspect VTC actuator A .

Is the actuator OK?

YES

Check the VTC system oil passages and clean them if needed.

NO

Replace VTC actuator A .
````

## Chunk 6948: DTC P101A (K20C2)

- Title: DTC P101A (K20C2)
- Source path: `pages\7640.html`
- Chunk ID: `chunk_d8dea481e7d4`
- Images: none
- Duplicate sources: `pages\9227.html`, `pages\22106.html`, `pages\15121.html`

### Full Text

````text
# DTC P101A (K20C2)

DTC P101A : VTC B Advance Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0366 is stored at the same time as DTC P101A, troubleshoot DTC P101A first, then recheck for DTC P0366.

- If DTC P101A set after replacing the VTC actuator, verify that the correct timing marks on the crank pulley were used.

DTC Description | Confirmed DTC | Pending DTC

P101A VTC B Advance Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P101A VTC B Advance Malfunction Is DTC P101A indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P101A VTC B Advance Malfunction

Is DTC P101A indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- VTC oil control solenoid valve B operation check -1. Test VTC oil control solenoid valve B . Is the solenoid valve OK? YES Go to step 3. NO Replace VTC oil control solenoid valve B .

-1. Test VTC oil control solenoid valve B .

Is the solenoid valve OK?

YES

Go to step 3.

NO

Replace VTC oil control solenoid valve B .

- VTC actuator B check -1. Inspect VTC actuator B . Is the actuator OK? YES Check the VTC system oil passages and clean them if needed. NO Replace VTC actuator B .

-1. Inspect VTC actuator B .

Is the actuator OK?

YES

Check the VTC system oil passages and clean them if needed.

NO

Replace VTC actuator B .
````

## Chunk 6949: DTC P101A (L15B7/L15BA/L15BY)

- Title: DTC P101A (L15B7/L15BA/L15BY)
- Source path: `pages\7641.html`
- Chunk ID: `chunk_a4fc6f729296`
- Images: none
- Duplicate sources: `pages\9228.html`, `pages\22107.html`, `pages\15122.html`

### Full Text

````text
# DTC P101A (L15B7/L15BA/L15BY)

DTC P101A : VTC B Advance Malfunction

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P0366 is stored at the same time as DTC P101A, troubleshoot DTC P101A first, then recheck for DTC P0366.

- If DTC P101A set after replacing the VTC actuator, verify that the correct timing marks on the crank pulley were used.

DTC Description | Confirmed DTC | Pending DTC

P101A VTC B Advance Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P101A VTC B Advance Malfunction Is DTC P101A indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P101A VTC B Advance Malfunction

Is DTC P101A indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- VTC oil control solenoid valve B operation check -1. Test VTC oil control solenoid valve B . Is the solenoid valve OK? YES Go to step 3. NO Replace VTC oil control solenoid valve B .

-1. Test VTC oil control solenoid valve B .

Is the solenoid valve OK?

YES

Go to step 3.

NO

Replace VTC oil control solenoid valve B .

- VTC actuator B check -1. Inspect VTC actuator B . Is the actuator OK? YES Check the VTC system oil passages and clean them if needed. NO Replace VTC actuator B .

-1. Inspect VTC actuator B .

Is the actuator OK?

YES

Check the VTC system oil passages and clean them if needed.

NO

Replace VTC actuator B .
````

## Chunk 6950: DTC P1172 (K20C2)

- Title: DTC P1172 (K20C2)
- Source path: `pages\7642.html`
- Chunk ID: `chunk_b3fb72c0bb9b`
- Images: none
- Duplicate sources: `pages\9229.html`, `pages\22108.html`, `pages\15123.html`

### Full Text

````text
# DTC P1172 (K20C2)

DTC P1172 : A/F Sensor (Sensor 1) Circuit Out of Range High

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1172 A/F Sensor (Sensor 1) Circuit Out of Range High

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Monitor the OBD STATUS for P1172 in the DTCs MENU with the HDS. DTC Description OBD STATUS P1172 A/F Sensor (Sensor 1) Circuit Out of Range High Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Monitor the OBD STATUS for P1172 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P1172 A/F Sensor (Sensor 1) Circuit Out of Range High

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.
````

## Chunk 6951: DTC P1172 (L15B7/L15BA/L15BY)

- Title: DTC P1172 (L15B7/L15BA/L15BY)
- Source path: `pages\7643.html`
- Chunk ID: `chunk_e25cb9bae58f`
- Images: none
- Duplicate sources: `pages\9230.html`, `pages\22109.html`, `pages\15124.html`

### Full Text

````text
# DTC P1172 (L15B7/L15BA/L15BY)

DTC P1172 : A/F Sensor (Sensor 1) Circuit Out of Range High

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1172 A/F Sensor (Sensor 1) Circuit Out of Range High

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Monitor the OBD STATUS for P1172 in the DTCs MENU with the HDS. DTC Description OBD STATUS P1172 A/F Sensor (Sensor 1) Circuit Out of Range High Does the HDS indicate FAILED? YES The failure is duplicated. Replace the A/F sensor (Sensor 1) . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Monitor the OBD STATUS for P1172 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P1172 A/F Sensor (Sensor 1) Circuit Out of Range High

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the A/F sensor (Sensor 1) .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the A/F Sensor (Sensor 1) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates EXECUTING, keep driving until a result comes on. If the HDS indicates OUT OF CONDITION, go to step 1-4 and recheck.
````

## Chunk 6952: DTC P134B (K20C1) (17-21)

- Title: DTC P134B (K20C1) (17-21)
- Source path: `pages\7644.html`
- Chunk ID: `chunk_fc1f763139da`
- Images: none
- Duplicate sources: `pages\9231.html`, `pages\22110.html`, `pages\14873.html`

### Full Text

````text
# DTC P134B (K20C1) (17-21)

DTC P134B : Crankshaft Signal Diagnose

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P134B Crankshaft Signal Diagnose

DTC (PGM-FI)

- Problem verification (idling) -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Start the engine, and let it idle for 10 seconds. -5. Monitor the OBD STATUS for DTC P134B in the DTCs MENU with the HDS. DTC Description OBD STATUS P134B Crankshaft Signal Diagnose Does the HDS indicate FAILED? YES The failure is duplicated. Go to step 3. NO If the HDS indicates PASSED, go to step 2. If the HDS indicates NOT COMPLETED, keep idling until a result comes on.

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Start the engine, and let it idle for 10 seconds.

-5. Monitor the OBD STATUS for DTC P134B in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P134B Crankshaft Signal Diagnose

Does the HDS indicate FAILED?

YES

The failure is duplicated. Go to step 3.

NO

If the HDS indicates PASSED, go to step 2. If the HDS indicates NOT COMPLETED, keep idling until a result comes on.

- Problem verification (test-drive): Test-drive the vehicle for several minutes in the range of these on-board snapshot parameters recorded in step 1-1: ENGINE SPEED VEHICLE SPEED On-board Snapshot -2. Monitor the OBD STATUS for DTC P134B in the DTCs MENU with the HDS. DTC Description OBD STATUS P134B Crankshaft Signal Diagnose Does the HDS indicate FAILED? YES The failure is duplicated. Go to step 3. NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, retest and check the OBD STATUS again.

Test-drive the vehicle for several minutes in the range of these on-board snapshot parameters recorded in step 1-1:

- ENGINE SPEED

- VEHICLE SPEED

On-board Snapshot

-2. Monitor the OBD STATUS for DTC P134B in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P134B Crankshaft Signal Diagnose

Does the HDS indicate FAILED?

YES

The failure is duplicated. Go to step 3.

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CKP sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . If the HDS indicates NOT COMPLETED, retest and check the OBD STATUS again.

- CKP sensor circuit connectors and terminals condition check -1. Turn the vehicle to the OFF (LOCK) mode. Check for poor connections or loose terminals at these locations: CKP sensor PCM Engine ground Body ground Are the connections and terminals OK? YES Go to step 4. NO Repair the connections or terminals.

-1. Turn the vehicle to the OFF (LOCK) mode.

Check for poor connections or loose terminals at these locations:

- CKP sensor

- PCM

- Engine ground

- Body ground

Are the connections and terminals OK?

YES

Go to step 4.

NO

Repair the connections or terminals.

- CKP pulse plate visual check -1. Remove the CKP sensor , and check for damage to the CKP pulse plate. Is the pulse plate damaged? YES Replace the CKP pulse plate . NO Go to step 5.

-1. Remove the CKP sensor , and check for damage to the CKP pulse plate.

Is the pulse plate damaged?

YES

Replace the CKP pulse plate .

NO

Go to step 5.

- CKP sensor check -1. Substitute a known-good CKP sensor . -2. Reconnect all connectors. -3. Clear the DTC with the HDS. -4. Start the engine. -5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on. Test-drive the vehicle for several minutes in the range of these on-board snapshot parameters recorded in step 1-1: ENGINE SPEED VEHICLE SPEED On-board Snapshot -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P134B Crankshaft Signal Diagnose Is DTC P134B indicated? YES The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 6953: DTC P134B (K20C1) (17-21)

- Title: DTC P134B (K20C1) (17-21)
- Source path: `pages\7644.html`
- Chunk ID: `chunk_16cc15771809`
- Images: none
- Duplicate sources: `pages\9231.html`, `pages\22110.html`, `pages\14873.html`

### Full Text

````text
plate damaged?

YES

Replace the CKP pulse plate .

NO

Go to step 5.

- CKP sensor check -1. Substitute a known-good CKP sensor . -2. Reconnect all connectors. -3. Clear the DTC with the HDS. -4. Start the engine. -5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on. Test-drive the vehicle for several minutes in the range of these on-board snapshot parameters recorded in step 1-1: ENGINE SPEED VEHICLE SPEED On-board Snapshot -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P134B Crankshaft Signal Diagnose Is DTC P134B indicated? YES The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P134B goes away and the PCM was substituted, replace the original PCM . NO Replace the original CKP sensor .

-1. Substitute a known-good CKP sensor .

-2. Reconnect all connectors.

-3. Clear the DTC with the HDS.

-4. Start the engine.

-5. Hold the engine speed 3, 000 rpm without load (in neutral) until the radiator fan comes on.

Test-drive the vehicle for several minutes in the range of these on-board snapshot parameters recorded in step 1-1:

- ENGINE SPEED

- VEHICLE SPEED

On-board Snapshot

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P134B Crankshaft Signal Diagnose

Is DTC P134B indicated?

YES

The CKP sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P134B goes away and the PCM was substituted, replace the original PCM .

NO

Replace the original CKP sensor .
````

## Chunk 6954: DTC P1454, P2422 (K20C2)

- Title: DTC P1454, P2422 (K20C2)
- Source path: `pages\7645.html`
- Chunk ID: `chunk_8e501db513b6`
- Images: `images\GHH405230.jpeg`, `images\GHH405231.jpeg`, `images\GHH405232.jpeg`, `images\GHH405233.jpeg`
- Duplicate sources: `pages\9232.html`, `pages\22111.html`, `pages\15125.html`

### Full Text

````text
# DTC P1454, P2422 (K20C2)

DTC P1454 : FTP Sensor Circuit Range/Performance Problem

DTC P2422 : EVAP Canister Vent Shut Valve Stuck Closed Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1454 FTP Sensor Circuit Range/Performance Problem

P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction

DTC (PGM-FI)

- EVAP system check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Insert the emergency fuel funnel into the fuel filler neck . NOTE: The emergency fuel funnel is stored in the trunk tool box. -5. Turn the vehicle to the ON mode. -6. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Go to step 2. NO Go to step 5.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Insert the emergency fuel funnel into the fuel filler neck .

NOTE: The emergency fuel funnel is stored in the trunk tool box.

-5. Turn the vehicle to the ON mode.

-6. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 2.

NO

Go to step 5.

- Problem verification -1. Remove the emergency fuel funnel from the fuel filler neck. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) until the radiator fan comes on. -4. Monitor the EVAP PC DUTY (purge control duty) in the DATA LIST with the HDS, while holding the engine speed at 3, 000 rpm with the EVAP PC DUTY at 20 % or more for at least 4 minutes, then let the engine idle. Signal Current conditions Values Unit EVAP PC DUTY -5. Monitor the OBD STATUS for DTC P1454 and/or P2422 in the DTCs MENU with the HDS. DTC Description OBD STATUS P1454 FTP Sensor Circuit Range/Performance Problem P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction Does the HDS indicate FAILED? YES The failure is duplicated. Go to step 3. NO If the HDS indicates PASSED, there might be an intermittent failure, and the system is OK at this time. Check the on-board snapshot , and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

-1. Remove the emergency fuel funnel from the fuel filler neck.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

-4. Monitor the EVAP PC DUTY (purge control duty) in the DATA LIST with the HDS, while holding the engine speed at 3, 000 rpm with the EVAP PC DUTY at 20 % or more for at least 4 minutes, then let the engine idle.

Signal | Current conditions

Values | Unit

EVAP PC DUTY

-5. Monitor the OBD STATUS for DTC P1454 and/or P2422 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P1454 FTP Sensor Circuit Range/Performance Problem

P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction

Does the HDS indicate FAILED?

YES

The failure is duplicated. Go to step 3.

NO

If the HDS indicates PASSED, there might be an intermittent failure, and the system is OK at this time. Check the on-board snapshot , and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

- EVAP canister vent line check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Remove the right front floor undercover . -4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B). Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6.
````

## Chunk 6955: DTC P1454, P2422 (K20C2)

- Title: DTC P1454, P2422 (K20C2)
- Source path: `pages\7645.html`
- Chunk ID: `chunk_c4abd1c4039b`
- Images: `images\GHH405230.jpeg`, `images\GHH405231.jpeg`, `images\GHH405232.jpeg`, `images\GHH405233.jpeg`
- Duplicate sources: `pages\9232.html`, `pages\22111.html`, `pages\15125.html`

### Full Text

````text
re, and the system is OK at this time. Check the on-board snapshot , and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

- EVAP canister vent line check -1. Clear the DTC with the HDS. -2. Turn the vehicle to the OFF (LOCK) mode. -3. Remove the right front floor undercover . -4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B). Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Check for a blockage in the EVAP canister vent hose or drain tube joint. NO Go to step 4.

-1. Clear the DTC with the HDS.

-2. Turn the vehicle to the OFF (LOCK) mode.

-3. Remove the right front floor undercover .

-4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B).

Courtesy of HONDA, U.S.A., INC.

-5. Turn the vehicle to the ON mode.

-6. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Check for a blockage in the EVAP canister vent hose or drain tube joint.

NO

Go to step 4.

- EVAP canister vent shut valve operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the EVAP canister vent shut valve . -3. Connect the 2P connector to the EVAP canister vent shut valve. -4. Turn the vehicle to the ON mode. -5. Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Check the EVAP canister vent shut valve (A) operation. Courtesy of HONDA, U.S.A., INC. Is the valve free of corrosion, and does it operate properly? YES The EVAP canister vent shut valve is OK. Go to step 5. NO Replace the EVAP canister vent shut valve .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the EVAP canister vent shut valve .

-3. Connect the 2P connector to the EVAP canister vent shut valve.

-4. Turn the vehicle to the ON mode.

-5. Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Check the EVAP canister vent shut valve (A) operation.

Courtesy of HONDA, U.S.A., INC.

Is the valve free of corrosion, and does it operate properly?

YES

The EVAP canister vent shut valve is OK. Go to step 5.

NO

Replace the EVAP canister vent shut valve .

- FTP sensor hose restriction check -1. Disconnect the hose (A) from the FTP sensor (B). Courtesy of HONDA, U.S.A., INC. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Check for a blockage in the FTP sensor hose. NO Go to step 6.

-1. Disconnect the hose (A) from the FTP sensor (B).

Courtesy of HONDA, U.S.A., INC.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Check for a blockage in the FTP sensor hose.

NO

Go to step 6.

- FTP sensor port restriction check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor (A) from the EVAP canister (B) with its connector connected. Courtesy of HONDA, U.S.A., INC. -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister . NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor (A) from the EVAP canister (B) with its connector connected.

Courtesy of HONDA, U.S.A., INC.

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit
````

## Chunk 6956: DTC P1454, P2422 (K20C2)

- Title: DTC P1454, P2422 (K20C2)
- Source path: `pages\7645.html`
- Chunk ID: `chunk_e65a3d8802a8`
- Images: `images\GHH405230.jpeg`, `images\GHH405231.jpeg`, `images\GHH405232.jpeg`, `images\GHH405233.jpeg`
- Duplicate sources: `pages\9232.html`, `pages\22111.html`, `pages\15125.html`

### Full Text

````text
e. -2. Remove the FTP sensor (A) from the EVAP canister (B) with its connector connected. Courtesy of HONDA, U.S.A., INC. -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister . NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor (A) from the EVAP canister (B) with its connector connected.

Courtesy of HONDA, U.S.A., INC.

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister .

NO

Replace the FTP sensor .
````

## Chunk 6957: DTC P1454, P2422 (L15B7/L15BA/L15BY)

- Title: DTC P1454, P2422 (L15B7/L15BA/L15BY)
- Source path: `pages\7646.html`
- Chunk ID: `chunk_b955be14f426`
- Images: `images\GHH405234.jpeg`, `images\GHH405235.jpeg`, `images\GHH405236.jpeg`, `images\GHH405237.jpeg`
- Duplicate sources: `pages\9233.html`, `pages\22112.html`, `pages\15126.html`

### Full Text

````text
# DTC P1454, P2422 (L15B7/L15BA/L15BY)

DTC P1454 : FTP Sensor Circuit Range/Performance Problem

DTC P2422 : EVAP Canister Vent Shut Valve Stuck Closed Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1454 FTP Sensor Circuit Range/Performance Problem

P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction

DTC (PGM-FI)

- EVAP system check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Insert the emergency fuel funnel into the fuel filler neck . NOTE: The emergency fuel funnel is stored in the trunk tool box. -5. Turn the vehicle to the ON mode. -6. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Go to step 2. NO Go to step 5.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Insert the emergency fuel funnel into the fuel filler neck .

NOTE: The emergency fuel funnel is stored in the trunk tool box.

-5. Turn the vehicle to the ON mode.

-6. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 2.

NO

Go to step 5.

- Problem verification -1. Remove the emergency fuel funnel from the fuel filler neck. -2. Clear the DTC with the HDS. -3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) until the radiator fan comes on. -4. Monitor the EVAP PC DUTY (purge control duty) in the DATA LIST with the HDS, while holding the engine speed at 3, 000 rpm with the EVAP PC DUTY at 20 % or more for at least 4 minutes, then let the engine idle. Signal Current conditions Values Unit EVAP PC DUTY -5. Monitor the OBD STATUS for DTC P1454 and/or P2422 in the DTCs MENU with the HDS. DTC Description OBD STATUS P1454 FTP Sensor Circuit Range/Performance Problem P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction Does the HDS indicate FAILED? YES The failure is duplicated. Go to step 3. NO If the HDS indicates PASSED, there might be an intermittent failure, and the system is OK at this time. Check the on-board snapshot, and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

-1. Remove the emergency fuel funnel from the fuel filler neck.

-2. Clear the DTC with the HDS.

-3. Start the engine, and let it idle without load (CVT in P or N, M/T in neutral) until the radiator fan comes on.

-4. Monitor the EVAP PC DUTY (purge control duty) in the DATA LIST with the HDS, while holding the engine speed at 3, 000 rpm with the EVAP PC DUTY at 20 % or more for at least 4 minutes, then let the engine idle.

Signal | Current conditions

Values | Unit

EVAP PC DUTY

-5. Monitor the OBD STATUS for DTC P1454 and/or P2422 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P1454 FTP Sensor Circuit Range/Performance Problem

P2422 EVAP Canister Vent Shut Valve Stuck Closed Malfunction

Does the HDS indicate FAILED?

YES

The failure is duplicated. Go to step 3.

NO

If the HDS indicates PASSED, there might be an intermittent failure, and the system is OK at this time. Check the on-board snapshot, and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

- EVAP canister vent line check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Clear the DTC with the HDS. -3. Remove the right front floor undercover . -4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B). Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode.
````

## Chunk 6958: DTC P1454, P2422 (L15B7/L15BA/L15BY)

- Title: DTC P1454, P2422 (L15B7/L15BA/L15BY)
- Source path: `pages\7646.html`
- Chunk ID: `chunk_e73c56a24c8e`
- Images: `images\GHH405234.jpeg`, `images\GHH405235.jpeg`, `images\GHH405236.jpeg`, `images\GHH405237.jpeg`
- Duplicate sources: `pages\9233.html`, `pages\22112.html`, `pages\15126.html`

### Full Text

````text
failure, and the system is OK at this time. Check the on-board snapshot, and repeat the driving conditions when the DTC set (fuel level, engine speed, vehicle speed, and outside air temperature). If no problem is found, check for poor connections or loose terminals between the FTP sensor and the PCM. Also check for a blockage in the FTP sensor vent port and vent hose, and the EVAP canister vent hose and drain joint. If the HDS indicates NOT COMPLETED, let the engine idle until a result comes on.

- EVAP canister vent line check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Clear the DTC with the HDS. -3. Remove the right front floor undercover . -4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B). Courtesy of HONDA, U.S.A., INC. -5. Turn the vehicle to the ON mode. -6. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Check for a blockage in the EVAP canister vent hose or drain tube joint. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Clear the DTC with the HDS.

-3. Remove the right front floor undercover .

-4. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B).

Courtesy of HONDA, U.S.A., INC.

-5. Turn the vehicle to the ON mode.

-6. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Check for a blockage in the EVAP canister vent hose or drain tube joint.

NO

Go to step 4.

- EVAP canister vent shut valve operation check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the EVAP canister vent shut valve . -3. Connect the 2P connector to the EVAP canister vent shut valve. -4. Turn the vehicle to the ON mode. -5. Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Check the EVAP canister vent shut valve (A) operation. Courtesy of HONDA, U.S.A., INC. Is the valve free of corrosion, and does it operate properly? YES The EVAP canister vent shut valve is OK. Go to step 5. NO Replace the EVAP canister vent shut valve .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the EVAP canister vent shut valve .

-3. Connect the 2P connector to the EVAP canister vent shut valve.

-4. Turn the vehicle to the ON mode.

-5. Select the EVAP TEST in the INSPECTION MENU, and do the EVAP CVS ON in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Check the EVAP canister vent shut valve (A) operation.

Courtesy of HONDA, U.S.A., INC.

Is the valve free of corrosion, and does it operate properly?

YES

The EVAP canister vent shut valve is OK. Go to step 5.

NO

Replace the EVAP canister vent shut valve .

- FTP sensor vent hose restriction check -1. Disconnect the hose (A) from the FTP sensor (B). Courtesy of HONDA, U.S.A., INC. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES Check for a blockage in the FTP sensor vent hose. NO Go to step 6.

-1. Disconnect the hose (A) from the FTP sensor (B).

Courtesy of HONDA, U.S.A., INC.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

Check for a blockage in the FTP sensor vent hose.

NO

Go to step 6.

- FTP sensor port restriction check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor (A) from the EVAP canister with its connector connected. Courtesy of HONDA, U.S.A., INC. -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister . NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor (A) from the EVAP canister with its connector connected.

Courtesy of HONDA, U.S.A., INC.

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit
````

## Chunk 6959: DTC P1454, P2422 (L15B7/L15BA/L15BY)

- Title: DTC P1454, P2422 (L15B7/L15BA/L15BY)
- Source path: `pages\7646.html`
- Chunk ID: `chunk_116f964aaea9`
- Images: `images\GHH405234.jpeg`, `images\GHH405235.jpeg`, `images\GHH405236.jpeg`, `images\GHH405237.jpeg`
- Duplicate sources: `pages\9233.html`, `pages\22112.html`, `pages\15126.html`

### Full Text

````text
OCK) mode. -2. Remove the FTP sensor (A) from the EVAP canister with its connector connected. Courtesy of HONDA, U.S.A., INC. -3. Turn the vehicle to the ON mode. -4. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR -0.67-0.67 kPa Do the current condition (s) match the threshold? YES The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister . NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor (A) from the EVAP canister with its connector connected.

Courtesy of HONDA, U.S.A., INC.

-3. Turn the vehicle to the ON mode.

-4. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR | -0.67-0.67 | kPa

Do the current condition (s) match the threshold?

YES

The FTP sensor port is OK. The EVAP canister has an internal blockage; replace the EVAP canister .

NO

Replace the FTP sensor .
````

## Chunk 6960: DTC P1458 (K20C2)

- Title: DTC P1458 (K20C2)
- Source path: `pages\7647.html`
- Chunk ID: `chunk_c5270fcd8bff`
- Images: `images\GHH405238.jpeg`, `images\GHH405239.jpeg`, `images\GHH405240.jpeg`, `images\GHH405241.jpeg`
- Duplicate sources: `pages\9234.html`, `pages\22113.html`, `pages\15127.html`

### Full Text

````text
# DTC P1458 (K20C2)

DTC P1458 : FTP Sensor Circuit Range/Performance Problem

Special Tools Required

Vacuum Pump/Gauge, 0-30 inHg Snap-on YA4000A or equivalent, commercially available

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If any of DTCs listed below are indicated at the same time as DTC P1458, troubleshoot those DTCs first, then recheck for P1458. P0451, P0452, P0453, P1454: FTP sensor P2422: EVAP canister vent shut valve

P0451, P0452, P0453, P1454: FTP sensor

P2422: EVAP canister vent shut valve

- Do not start the engine during this troubleshooting.

DTC Description | Confirmed DTC | Pending DTC

P1458 FTP Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Fuel level check -1. Turn the vehicle to the ON mode. Note these recorded on-board snapshot parameters with the HDS: MAX Value of FTP SENSOR MIN Value of FTP SENSOR FUEL LEVEL On-board Snapshot Courtesy of HONDA, U.S.A., INC. -3. Check the FUEL LEVEL in the DATA LIST with the HDS. Signal Current conditions Values Unit FUEL LEVEL Is the current FUEL LEVEL less than it is on the on-board snapshot? YES Go to step 2. NO Drain the fuel until the FUEL LEVEL is less than it is on the on-board snapshot, then go to step 2.

-1. Turn the vehicle to the ON mode.

Note these recorded on-board snapshot parameters with the HDS:

- MAX Value of FTP SENSOR

- MIN Value of FTP SENSOR

- FUEL LEVEL

On-board Snapshot

Courtesy of HONDA, U.S.A., INC.

-3. Check the FUEL LEVEL in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

FUEL LEVEL

Is the current FUEL LEVEL less than it is on the on-board snapshot?

YES

Go to step 2.

NO

Drain the fuel until the FUEL LEVEL is less than it is on the on-board snapshot, then go to step 2.

- Determine possible failure area (FTP sensor, others) -1. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Take a snapshot with the HDS for 3 minutes without starting the engine. Check the recorded snapshot parameter with the HDS: MAX Value of FTP SENSOR (FINE) MIN Value of FTP SENSOR (FINE) Courtesy of HONDA, U.S.A., INC. Are the MAX and MIN values of the FTP SENSOR (FINE) within the range of +/-0.67 kPa (0.2 inHg, 5 mmHg)? YES Go to step 3. NO Go to step 5.

-1. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Take a snapshot with the HDS for 3 minutes without starting the engine.

Check the recorded snapshot parameter with the HDS:

- MAX Value of FTP SENSOR (FINE)

- MIN Value of FTP SENSOR (FINE)

Courtesy of HONDA, U.S.A., INC.

Are the MAX and MIN values of the FTP SENSOR (FINE) within the range of +/-0.67 kPa (0.2 inHg, 5 mmHg)?

YES

Go to step 3.

NO

Go to step 5.

- FTP sensor performance check 1 -1. Check the FTP SENSOR (FINE) in the recorded snapshot with the HDS. Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Go to step 4. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check the FTP SENSOR (FINE) in the recorded snapshot with the HDS.

Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds?

YES

Go to step 4.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- FTP sensor performance check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR (FINE) Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Replace the FTP sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM.
````

## Chunk 6961: DTC P1458 (K20C2)

- Title: DTC P1458 (K20C2)
- Source path: `pages\7647.html`
- Chunk ID: `chunk_9eadbfd16d6a`
- Images: `images\GHH405238.jpeg`, `images\GHH405239.jpeg`, `images\GHH405240.jpeg`, `images\GHH405241.jpeg`
- Duplicate sources: `pages\9234.html`, `pages\22113.html`, `pages\15127.html`

### Full Text

````text
anister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- FTP sensor performance check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR (FINE) Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Replace the FTP sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor .

-3. Reconnect the following connector.

FTP sensor 3P connector

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

FTP SENSOR (FINE)

Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds?

YES

Replace the FTP sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (EVAP canister vent line, others) -1. Insert the emergency fuel funnel into the fuel filler neck , and wait 1 minute. NOTE: The emergency fuel funnel is stored in the trunk tool box. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR (FINE) More than 0.67 kPa Less than -0.67 kPa Do the current condition (s) match the threshold? YES Go to step 6. NO Remove the emergency fuel funnel from the fuel filler neck, then go to step 8.

-1. Insert the emergency fuel funnel into the fuel filler neck , and wait 1 minute.

NOTE: The emergency fuel funnel is stored in the trunk tool box.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR (FINE) | More than 0.67 | kPa

Less than -0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 6.

NO

Remove the emergency fuel funnel from the fuel filler neck, then go to step 8.

- FTP sensor hose check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR (FINE) More than 0.67 kPa Less than -0.67 kPa Do the current condition (s) match the threshold? YES Go to step 7. NO Remove the blockage in the FTP sensor hose. Replace the hose if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor .

-3. Reconnect the following connector.

FTP sensor 3P connector

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR (FINE) | More than 0.67 | kPa

Less than -0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 7.

NO

Remove the blockage in the FTP sensor hose. Replace the hose if needed.

- FTP sensor port visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. FTP sensor 3P connector -3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and hose side). Courtesy of HONDA, U.S.A., INC. Is there any blockage or damage? YES Remove the blockage, or replace the FTP sensor if needed. NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

FTP sensor 3P connector

-3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and hose side).

Courtesy of HONDA, U.S.A., INC.

Is there any blockage or damage?

YES
````

## Chunk 6962: DTC P1458 (K20C2)

- Title: DTC P1458 (K20C2)
- Source path: `pages\7647.html`
- Chunk ID: `chunk_fb57f0a2c4e6`
- Images: `images\GHH405238.jpeg`, `images\GHH405239.jpeg`, `images\GHH405240.jpeg`, `images\GHH405241.jpeg`
- Duplicate sources: `pages\9234.html`, `pages\22113.html`, `pages\15127.html`

### Full Text

````text
dition (s) match the threshold?

YES

Go to step 7.

NO

Remove the blockage in the FTP sensor hose. Replace the hose if needed.

- FTP sensor port visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. FTP sensor 3P connector -3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and hose side). Courtesy of HONDA, U.S.A., INC. Is there any blockage or damage? YES Remove the blockage, or replace the FTP sensor if needed. NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

FTP sensor 3P connector

-3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and hose side).

Courtesy of HONDA, U.S.A., INC.

Is there any blockage or damage?

YES

Remove the blockage, or replace the FTP sensor if needed.

NO

Replace the FTP sensor .

- EVAP canister vent shut valve check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the right front floor undercover . -3. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B), then connect a vacuum pump/gauge, 0-30 inHg, to the EVAP canister vent shut valve port as shown. Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Try to apply vacuum to the valve (not more than 5.3 kPa (1.6 inHg, 40 mmHg)) while checking the FTP SENSOR (FINE) in the DATA LIST with the HDS. NOTE: To avoid damaging the FTP sensor, do not apply more than 5.3 kPa (1.6 inHg, 40 mmHg) of vacuum. Signal Current conditions Values Unit FTP SENSOR (FINE) Does the EVAP canister vent shut valve hold more than 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum? YES Replace the EVAP canister vent shut valve . NO The EVAP canister vent shut valve is OK. Remove the blockage in the EVAP canister vent hose. Replace the hose if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the right front floor undercover .

-3. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B), then connect a vacuum pump/gauge, 0-30 inHg, to the EVAP canister vent shut valve port as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Try to apply vacuum to the valve (not more than 5.3 kPa (1.6 inHg, 40 mmHg)) while checking the FTP SENSOR (FINE) in the DATA LIST with the HDS.

NOTE: To avoid damaging the FTP sensor, do not apply more than 5.3 kPa (1.6 inHg, 40 mmHg) of vacuum.

Signal | Current conditions

Values | Unit

FTP SENSOR (FINE)

Does the EVAP canister vent shut valve hold more than 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum?

YES

Replace the EVAP canister vent shut valve .

NO

The EVAP canister vent shut valve is OK. Remove the blockage in the EVAP canister vent hose. Replace the hose if needed.
````

## Chunk 6963: DTC P1458 (L15B7/L15BA/L15BY)

- Title: DTC P1458 (L15B7/L15BA/L15BY)
- Source path: `pages\7648.html`
- Chunk ID: `chunk_c2b87277ef97`
- Images: `images\GHH405242.jpeg`, `images\GHH405243.jpeg`, `images\GHH405244.jpeg`, `images\GHH405245.jpeg`
- Duplicate sources: `pages\9235.html`, `pages\22114.html`, `pages\15128.html`

### Full Text

````text
# DTC P1458 (L15B7/L15BA/L15BY)

DTC P1458 : FTP Sensor Circuit Range/Performance Problem

Special Tools Required

Vacuum Pump/Gauge, 0-30 inHg Snap-on YA4000A or equivalent, commercially available

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If any of DTCs listed below are indicated at the same time as DTC P1458, troubleshoot those DTCs first, then recheck for P1458. P0451, P0452, P0453, P1454: FTP sensor P2422: EVAP canister vent shut valve

P0451, P0452, P0453, P1454: FTP sensor

P2422: EVAP canister vent shut valve

- Do not start the engine during this troubleshooting.

DTC Description | Confirmed DTC | Pending DTC

P1458 FTP Sensor Circuit Range/Performance Problem

DTC (PGM-FI)

- Fuel level check -1. Turn the vehicle to the ON mode. Note these recorded on-board snapshot parameters with the HDS: MAX Value of FTP SENSOR MIN Value of FTP SENSOR FUEL LEVEL On-board Snapshot Courtesy of HONDA, U.S.A., INC. -3. Check the FUEL LEVEL in the DATA LIST with the HDS. Signal Current conditions Values Unit FUEL LEVEL Is the current FUEL LEVEL less than it is on the on-board snapshot? YES Go to step 2. NO Drain the fuel until the FUEL LEVEL is less than it is on the on-board snapshot, then go to step 2.

-1. Turn the vehicle to the ON mode.

Note these recorded on-board snapshot parameters with the HDS:

- MAX Value of FTP SENSOR

- MIN Value of FTP SENSOR

- FUEL LEVEL

On-board Snapshot

Courtesy of HONDA, U.S.A., INC.

-3. Check the FUEL LEVEL in the DATA LIST with the HDS.

Signal | Current conditions

Values | Unit

FUEL LEVEL

Is the current FUEL LEVEL less than it is on the on-board snapshot?

YES

Go to step 2.

NO

Drain the fuel until the FUEL LEVEL is less than it is on the on-board snapshot, then go to step 2.

- Determine possible failure area (FTP sensor, others) -1. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Take a snapshot with the HDS for 3 minutes without starting the engine. Check the recorded snapshot parameter with the HDS: MAX Value of FTP SENSOR (FINE) MIN Value of FTP SENSOR (FINE) Courtesy of HONDA, U.S.A., INC. Are the MAX and MIN values of the FTP SENSOR (FINE) within the range of +/-0.67 kPa (0.2 inHg, 5 mmHg)? YES Go to step 3. NO Go to step 5.

-1. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Take a snapshot with the HDS for 3 minutes without starting the engine.

Check the recorded snapshot parameter with the HDS:

- MAX Value of FTP SENSOR (FINE)

- MIN Value of FTP SENSOR (FINE)

Courtesy of HONDA, U.S.A., INC.

Are the MAX and MIN values of the FTP SENSOR (FINE) within the range of +/-0.67 kPa (0.2 inHg, 5 mmHg)?

YES

Go to step 3.

NO

Go to step 5.

- FTP sensor performance check 1 -1. Check the FTP SENSOR (FINE) in the recorded snapshot with the HDS. Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Go to step 4. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Check the FTP SENSOR (FINE) in the recorded snapshot with the HDS.

Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds?

YES

Go to step 4.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- FTP sensor performance check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR (FINE) Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Replace the FTP sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM.
````

## Chunk 6964: DTC P1458 (L15B7/L15BA/L15BY)

- Title: DTC P1458 (L15B7/L15BA/L15BY)
- Source path: `pages\7648.html`
- Chunk ID: `chunk_19345b5de664`
- Images: `images\GHH405242.jpeg`, `images\GHH405243.jpeg`, `images\GHH405244.jpeg`, `images\GHH405245.jpeg`
- Duplicate sources: `pages\9235.html`, `pages\22114.html`, `pages\15128.html`

### Full Text

````text
anister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- FTP sensor performance check 2 -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Current conditions Values Unit FTP SENSOR (FINE) Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds? YES Replace the FTP sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor .

-3. Reconnect the following connector.

FTP sensor 3P connector

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

FTP SENSOR (FINE)

Does it vary 0.067 kPa (0.02 inHg, 0.5 mmHg) or more within 3 seconds?

YES

Replace the FTP sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the FTP sensor, the EVAP canister vent shut valve, and the PCM. Also check for a blockage in the EVAP vent hose. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (EVAP canister vent line, others) -1. Insert the emergency fuel funnel into the fuel filler neck , and wait 1 minute. NOTE: The emergency fuel funnel is stored in the trunk tool box. -2. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR (FINE) More than 0.67 kPa Less than -0.67 kPa Do the current condition (s) match the threshold? YES Go to step 6. NO Remove the emergency fuel funnel from the fuel filler neck, then go to step 8.

-1. Insert the emergency fuel funnel into the fuel filler neck , and wait 1 minute.

NOTE: The emergency fuel funnel is stored in the trunk tool box.

-2. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR (FINE) | More than 0.67 | kPa

Less than -0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 6.

NO

Remove the emergency fuel funnel from the fuel filler neck, then go to step 8.

- FTP sensor vent hose check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the FTP sensor . -3. Reconnect the following connector. FTP sensor 3P connector -4. Turn the vehicle to the ON mode. -5. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit FTP SENSOR (FINE) More than 0.67 kPa Less than -0.67 kPa Do the current condition (s) match the threshold? YES Go to step 7. NO Remove the blockage in the FTP sensor vent hose. Replace the hose if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the FTP sensor .

-3. Reconnect the following connector.

FTP sensor 3P connector

-4. Turn the vehicle to the ON mode.

-5. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

FTP SENSOR (FINE) | More than 0.67 | kPa

Less than -0.67 | kPa

Do the current condition (s) match the threshold?

YES

Go to step 7.

NO

Remove the blockage in the FTP sensor vent hose. Replace the hose if needed.

- FTP sensor port visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. FTP sensor 3P connector -3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and vent side). Courtesy of HONDA, U.S.A., INC. Is there any blockage or damage? YES Remove the blockage, or replace the FTP sensor if needed. NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

FTP sensor 3P connector

-3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and vent side).

Courtesy of HONDA, U.S.A., INC.

Is there any blockage or damage?

YES
````

## Chunk 6965: DTC P1458 (L15B7/L15BA/L15BY)

- Title: DTC P1458 (L15B7/L15BA/L15BY)
- Source path: `pages\7648.html`
- Chunk ID: `chunk_3e74f7d0ae52`
- Images: `images\GHH405242.jpeg`, `images\GHH405243.jpeg`, `images\GHH405244.jpeg`, `images\GHH405245.jpeg`
- Duplicate sources: `pages\9235.html`, `pages\22114.html`, `pages\15128.html`

### Full Text

````text
n (s) match the threshold?

YES

Go to step 7.

NO

Remove the blockage in the FTP sensor vent hose. Replace the hose if needed.

- FTP sensor port visual check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. FTP sensor 3P connector -3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and vent side). Courtesy of HONDA, U.S.A., INC. Is there any blockage or damage? YES Remove the blockage, or replace the FTP sensor if needed. NO Replace the FTP sensor .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

FTP sensor 3P connector

-3. Check for a blockage or damage at the FTP sensor ports (EVAP canister side and vent side).

Courtesy of HONDA, U.S.A., INC.

Is there any blockage or damage?

YES

Remove the blockage, or replace the FTP sensor if needed.

NO

Replace the FTP sensor .

- EVAP canister vent shut valve check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the right front floor undercover . -3. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B), then connect a vacuum pump/gauge, 0-30 inHg, to the EVAP canister vent shut valve port as shown. Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS. SINGLE SOLENOID Try to apply vacuum to the valve (not more than 5.3 kPa (1.6 inHg, 40 mmHg)) while checking the FTP SENSOR (FINE) in the DATA LIST with the HDS. NOTE: To avoid damaging the FTP sensor, do not apply more than 5.3 kPa (1.6 inHg, 40 mmHg) of vacuum. Signal Current conditions Values Unit FTP SENSOR (FINE) Does the EVAP canister vent shut valve hold more than 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum? YES Replace the EVAP canister vent shut valve . NO The EVAP canister vent shut valve is OK. Remove the blockage in the EVAP canister vent hose. Replace the hose if needed.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the right front floor undercover .

-3. Disconnect the EVAP canister vent hose (A) from the EVAP canister (B), then connect a vacuum pump/gauge, 0-30 inHg, to the EVAP canister vent shut valve port as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Select the EVAP TEST in the INSPECTION MENU, then select the EVAP CVS OFF in the SINGLE SOLENOID with the HDS.

SINGLE SOLENOID

Try to apply vacuum to the valve (not more than 5.3 kPa (1.6 inHg, 40 mmHg)) while checking the FTP SENSOR (FINE) in the DATA LIST with the HDS.

NOTE: To avoid damaging the FTP sensor, do not apply more than 5.3 kPa (1.6 inHg, 40 mmHg) of vacuum.

Signal | Current conditions

Values | Unit

FTP SENSOR (FINE)

Does the EVAP canister vent shut valve hold more than 1.3 kPa (0.4 inHg, 10 mmHg) of vacuum?

YES

Replace the EVAP canister vent shut valve .

NO

The EVAP canister vent shut valve is OK. Remove the blockage in the EVAP canister vent hose. Replace the hose if needed.
````

## Chunk 6966: DTC P145D (L15B7/L15BA/L15BY)

- Title: DTC P145D (L15B7/L15BA/L15BY)
- Source path: `pages\7649.html`
- Chunk ID: `chunk_22082dee264f`
- Images: none
- Duplicate sources: `pages\9236.html`, `pages\22115.html`, `pages\15129.html`

### Full Text

````text
# DTC P145D (L15B7/L15BA/L15BY)

DTC P145D : EVAP System Purge Flow Malfunction at turbocharging

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If DTC P145D is indicated alone, do the troubleshooting for DTC P04DF and P04F0 using the on-board snapshot for P145D.

- If DTC P0441, P04F0, P04F1, and P145D are stored at the same time, check for a poor connection, a blockage, or damage at the EVAP canister purge line between the EVAP canister purge valve and the EVAP canister. Also check for a stuck closed EVAP canister purge valve.

- If any of the DTCs listed below are indicated at the same time as DTC P145D, troubleshoot those DTCs first, then recheck for P145D. P04DF, P04F0, P04F1: EVAP system purge flow

P04DF, P04F0, P04F1: EVAP system purge flow

DTC Description | Confirmed DTC | Pending DTC

P145D EVAP System Purge Flow Malfunction at turbocharging

DTC (PGM-FI)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P04DF EVAP System High Purge Flow Detected P04F0 EVAP System Incorrect Purge Flow Detected P04F1 EVAP System Low Purge Flow Detected P145D EVAP System Purge Flow Malfunction at turbocharging Are DTC P04DF, P04F0, or P04F1 and P145D indicated at the same time? YES Go to the indicated DTC's troubleshooting. NO Go to the troubleshooting for DTC P04DF , DTC P04F0 , and DTC P04F1 .

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P04DF EVAP System High Purge Flow Detected

P04F0 EVAP System Incorrect Purge Flow Detected

P04F1 EVAP System Low Purge Flow Detected

P145D EVAP System Purge Flow Malfunction at turbocharging

Are DTC P04DF, P04F0, or P04F1 and P145D indicated at the same time?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to the troubleshooting for DTC P04DF , DTC P04F0 , and DTC P04F1 .
````

## Chunk 6967: DTC P1549 (K20C1) (17-21)

- Title: DTC P1549 (K20C1) (17-21)
- Source path: `pages\7650.html`
- Chunk ID: `chunk_afdb161120a2`
- Images: none
- Duplicate sources: `pages\9237.html`, `pages\22116.html`, `pages\14874.html`

### Full Text

````text
# DTC P1549 (K20C1) (17-21)

DTC P1549 : Charging System High Voltage

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If a high voltage battery (24 V, etc.) is connected to the vehicle, this DTC can be stored.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. Check under these conditions: A/C off Headlights off Rear window defogger off -5. Hold the engine speed at 3, 000 rpm without load (in neutral) for 1 minute. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1549 Charging System High Voltage Is DTC P1549 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

Check under these conditions:

- A/C off

- Headlights off

- Rear window defogger off

-5. Hold the engine speed at 3, 000 rpm without load (in neutral) for 1 minute.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

Is DTC P1549 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6968: DTC P1549 (K20C2)

- Title: DTC P1549 (K20C2)
- Source path: `pages\7651.html`
- Chunk ID: `chunk_1690ba522bad`
- Images: none
- Duplicate sources: `pages\9238.html`, `pages\22117.html`, `pages\15130.html`

### Full Text

````text
# DTC P1549 (K20C2)

DTC P1549 : Charging System High Voltage

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If a high voltage battery (24 V, etc.) is connected to the vehicle, this DTC can be stored.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. Check under these conditions: A/C off Headlights off Rear window defogger off -5. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1549 Charging System High Voltage Is DTC P1549 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

Check under these conditions:

- A/C off

- Headlights off

- Rear window defogger off

-5. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

Is DTC P1549 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6969: DTC P1549 (L15B7/L15BA/L15BY)

- Title: DTC P1549 (L15B7/L15BA/L15BY)
- Source path: `pages\7652.html`
- Chunk ID: `chunk_752c433aef5e`
- Images: none
- Duplicate sources: `pages\9239.html`, `pages\22118.html`, `pages\15131.html`

### Full Text

````text
# DTC P1549 (L15B7/L15BA/L15BY)

DTC P1549 : Charging System High Voltage

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- If a high voltage battery (24 V, etc.) is connected to the vehicle, this DTC can be stored.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. Check under these conditions: A/C off Headlights off Rear window defogger off -5. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1549 Charging System High Voltage Is DTC P1549 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

Check under these conditions:

- A/C off

- Headlights off

- Rear window defogger off

-5. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1549 Charging System High Voltage

Is DTC P1549 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6970: DTC P154A (K20C1) (17-21)

- Title: DTC P154A (K20C1) (17-21)
- Source path: `pages\7653.html`
- Chunk ID: `chunk_30f5673821ed`
- Images: none
- Duplicate sources: `pages\9240.html`, `pages\22119.html`, `pages\14875.html`

### Full Text

````text
# DTC P154A (K20C1) (17-21)

DTC P154A : Battery Sensor Internal Failure

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait 5 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P154A Battery Sensor Internal Failure Is DTC P154A indicated? YES The failure is duplicated. Replace the 12 volt battery sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait 5 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

Is DTC P154A indicated?

YES

The failure is duplicated. Replace the 12 volt battery sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6971: DTC P154A (K20C2)

- Title: DTC P154A (K20C2)
- Source path: `pages\7654.html`
- Chunk ID: `chunk_4418d5bc835f`
- Images: none
- Duplicate sources: `pages\9241.html`, `pages\22120.html`, `pages\15132.html`

### Full Text

````text
# DTC P154A (K20C2)

DTC P154A : Battery Sensor Internal Failure

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait 5 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P154A Battery Sensor Internal Failure Is DTC P154A indicated? YES The failure is duplicated. Replace the 12 volt battery sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait 5 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

Is DTC P154A indicated?

YES

The failure is duplicated. Replace the 12 volt battery sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6972: DTC P154A (L15B7/L15BA/L15BY)

- Title: DTC P154A (L15B7/L15BA/L15BY)
- Source path: `pages\7655.html`
- Chunk ID: `chunk_1111e83101a4`
- Images: none
- Duplicate sources: `pages\9242.html`, `pages\22121.html`, `pages\15133.html`

### Full Text

````text
# DTC P154A (L15B7/L15BA/L15BY)

DTC P154A : Battery Sensor Internal Failure

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait 5 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P154A Battery Sensor Internal Failure Is DTC P154A indicated? YES Replace the 12 volt battery sensor . NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait 5 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P154A Battery Sensor Internal Failure

Is DTC P154A indicated?

YES

Replace the 12 volt battery sensor .

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6973: DTC P154B (K20C1) (17-21)

- Title: DTC P154B (K20C1) (17-21)
- Source path: `pages\7656.html`
- Chunk ID: `chunk_346535e96235`
- Images: none
- Duplicate sources: `pages\9243.html`, `pages\22122.html`, `pages\15134.html`

### Full Text

````text
# DTC P154B (K20C1) (17-21)

DTC P154B : Battery Sensor Characteristic Abnormal

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P154B Battery Sensor Characteristic Abnormal

- DTC check -1. Turn the vehicle to the ON mode. -2. Check the Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P0112 IAT Sensor Circuit Low Voltage P0113 IAT Sensor Circuit High Voltage Is DTC P0112 and/or P0113 indicated? YES Do the indicated DTCs troubleshooting. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P0112 IAT Sensor Circuit Low Voltage

P0113 IAT Sensor Circuit High Voltage

Is DTC P0112 and/or P0113 indicated?

YES

Do the indicated DTCs troubleshooting.

NO

Go to step 2.

- 12 volt battery temperature check -1. Open the hood, and measure the temperature around the 12 volt battery sensor with a thermometer. -2. Start the engine, and let it idle for 10 seconds, then check the parameter (s) below with the HDS. Signal Current conditions Values Unit Estimated Battery Temperature Does the value of Estimated Battery Temperature differ 41 deg.F (23 deg.C) or more from the value of the thermometer? YES Replace the 12 volt battery sensor . NO Go to step 3.

-1. Open the hood, and measure the temperature around the 12 volt battery sensor with a thermometer.

-2. Start the engine, and let it idle for 10 seconds, then check the parameter (s) below with the HDS.

Signal | Current conditions

Values | Unit

Estimated Battery Temperature

Does the value of Estimated Battery Temperature differ 41 deg.F (23 deg.C) or more from the value of the thermometer?

YES

Replace the 12 volt battery sensor .

NO

Go to step 3.

- 12 volt battery sensor signal check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Check the parameter (s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Battery Current (Battery Sensor) More than 0 A Do the current condition (s) match the threshold? YES Replace the 12 volt battery sensor . NO Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Check the parameter (s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Battery Current (Battery Sensor) | More than 0 | A

Do the current condition (s) match the threshold?

YES

Replace the 12 volt battery sensor .

NO

Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .
````

## Chunk 6974: DTC P1658 (K20C2)

- Title: DTC P1658 (K20C2)
- Source path: `pages\7657.html`
- Chunk ID: `chunk_876b31a2284b`
- Images: none
- Duplicate sources: `pages\9244.html`, `pages\22123.html`, `pages\15135.html`

### Full Text

````text
# DTC P1658 (K20C2)

DTC P1658 : ETCS Control Relay ON Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1658 ETCS Control Relay ON Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Select the ETCS TEST in the INSPECTION MENU with the HDS. ETCS TEST Is the RELAY circuit OK? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Select the ETCS TEST in the INSPECTION MENU with the HDS.

ETCS TEST

Is the RELAY circuit OK?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (FI SUB RLY CL- line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector B (6P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector B (6P): disconnected Test point 1 PCM connector A (50P) No. 25 Test point 2 Body ground Is there continuity? YES Repair a short in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board. NO The FI SUB RLY CL- wire is OK. Go to step 4.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector B (6P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector B (6P): disconnected

Test point 1 | PCM connector A (50P) No. 25

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

NO

The FI SUB RLY CL- wire is OK. Go to step 4.

- Shorted wire check (FI SUB RLY OUT line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Relay circuit board connector B (6P): disconnected Test point 1 PCM connector A (50P) No. 16 Test point 2 Body ground Is there battery voltage? YES Repair a short to power in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. NO The FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1658 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector A (50P): disconnected

Relay circuit board connector B (6P): disconnected

Test point 1 | PCM connector A (50P) No. 16

Test point 2 | Body ground

Is there battery voltage?

YES

Repair a short to power in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

NO

The FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1658 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6975: DTC P1658 (L15B7/L15BA/L15BY)

- Title: DTC P1658 (L15B7/L15BA/L15BY)
- Source path: `pages\7658.html`
- Chunk ID: `chunk_2d9b0ae39d6f`
- Images: none
- Duplicate sources: `pages\9245.html`, `pages\22124.html`, `pages\15136.html`

### Full Text

````text
# DTC P1658 (L15B7/L15BA/L15BY)

DTC P1658 : ETCS Control Relay ON Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1658 ETCS Control Relay ON Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Select the ETCS TEST in the INSPECTION MENU with the HDS. ETCS TEST Is the RELAY circuit OK? YES Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . NO The failure is duplicated. Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Select the ETCS TEST in the INSPECTION MENU with the HDS.

ETCS TEST

Is the RELAY circuit OK?

YES

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

NO

The failure is duplicated. Go to step 2.

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (FI SUB RLY CL- line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 25 Test point 2 Body ground Is there continuity? YES Repair a short in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board. NO The FI SUB RLY CL- wire is OK. Go to step 4.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 25

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

NO

The FI SUB RLY CL- wire is OK. Go to step 4.

- Shorted wire check (FI SUB RLY OUT line to power) -1. Turn the vehicle to the ON mode. -2. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 16 Test point 2 Body ground Is there battery voltage? YES Repair a short to power in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. NO The FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1658 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the ON mode.

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 16

Test point 2 | Body ground

Is there battery voltage?

YES

Repair a short to power in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

NO

The FI SUB RLY OUT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1658 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 6976: DTC P1659 (K20C2)

- Title: DTC P1659 (K20C2)
- Source path: `pages\7659.html`
- Chunk ID: `chunk_4a333f63266c`
- Images: `images\GHH405246.jpeg`, `images\GHH405247.jpeg`, `images\GHH405248.jpeg`, `images\GHH405249.jpeg`
- Duplicate sources: `pages\9246.html`, `pages\22125.html`, `pages\15137.html`

### Full Text

````text
# DTC P1659 (K20C2)

DTC P1659 : ETCS Control Relay OFF Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1659 ETCS Control Relay OFF Malfunction Is DTC P1659 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

Is DTC P1659 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (PGM-FI subrelay circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Check the following fuse. Fuse No. A8 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Go to step 7.

-1. Check the following fuse.

Fuse | No. A8 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Go to step 7.

- Open wire check (+B DBW line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 14 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B DBW wire is OK. Go to step 5. NO Repair an open in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 14

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B DBW wire is OK. Go to step 5.

NO

Repair an open in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

- Open wire check (FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 11 Test point 2 PCM connector A (50P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 11

Test point 2 | PCM connector A (50P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

- Open wire check (FI SUB RLY CL- line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6977: DTC P1659 (K20C2)

- Title: DTC P1659 (K20C2)
- Source path: `pages\7659.html`
- Chunk ID: `chunk_9a1b5745a741`
- Images: `images\GHH405246.jpeg`, `images\GHH405247.jpeg`, `images\GHH405248.jpeg`, `images\GHH405249.jpeg`
- Duplicate sources: `pages\9246.html`, `pages\22125.html`, `pages\15137.html`

### Full Text

````text
ep 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 11

Test point 2 | PCM connector A (50P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

- Open wire check (FI SUB RLY CL- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector B (6P) No. 2 Test point 2 PCM connector A (50P) No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector B (6P) No. 2

Test point 2 | PCM connector A (50P) No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

- Shorted wire check (FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box. NO The FI SUB RLY OUT wire is OK. Go to step 8.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.

NO

The FI SUB RLY OUT wire is OK. Go to step 8.

- Shorted wire check (+B DBW line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 14 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board, or between the No. A8 (15 A) fuse and the No. A5 (5 A) fuse in the under-hood fuse/relay box. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse. NO The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected
````

## Chunk 6978: DTC P1659 (K20C2)

- Title: DTC P1659 (K20C2)
- Source path: `pages\7659.html`
- Chunk ID: `chunk_9ed7d7896f2b`
- Images: `images\GHH405246.jpeg`, `images\GHH405247.jpeg`, `images\GHH405248.jpeg`, `images\GHH405249.jpeg`
- Duplicate sources: `pages\9246.html`, `pages\22125.html`, `pages\15137.html`

### Full Text

````text
ES Repair a short in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board, or between the No. A8 (15 A) fuse and the No. A5 (5 A) fuse in the under-hood fuse/relay box. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse. NO The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 14

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board, or between the No. A8 (15 A) fuse and the No. A5 (5 A) fuse in the under-hood fuse/relay box. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse.

NO

The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.
````

## Chunk 6979: DTC P1659 (L15B7/L15BY)

- Title: DTC P1659 (L15B7/L15BY)
- Source path: `pages\7660.html`
- Chunk ID: `chunk_2ded0960dabe`
- Images: `images\GHH405250.jpeg`, `images\GHH405251.jpeg`, `images\GHH405252.jpeg`, `images\GHH405253.jpeg`
- Duplicate sources: `pages\9247.html`, `pages\22126.html`, `pages\15138.html`

### Full Text

````text
# DTC P1659 (L15B7/L15BY)

DTC P1659 : ETCS Control Relay OFF Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1659 ETCS Control Relay OFF Malfunction Is DTC P1659 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

Is DTC P1659 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A8 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A8 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Go to step 7.

- Open wire check (+B DBW line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) No. 14 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B DBW wire is OK. Go to step 5. NO Repair an open in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) No. 14

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B DBW wire is OK. Go to step 5.

NO

Repair an open in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

- Open wire check (FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 11 Test point 2 PCM connector A (50P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 11

Test point 2 | PCM connector A (50P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

- Open wire check (FI SUB RLY CL- line) -1. Check for continuity between test points 1 and 2.
````

## Chunk 6980: DTC P1659 (L15B7/L15BY)

- Title: DTC P1659 (L15B7/L15BY)
- Source path: `pages\7660.html`
- Chunk ID: `chunk_be223fae09a7`
- Images: `images\GHH405250.jpeg`, `images\GHH405251.jpeg`, `images\GHH405252.jpeg`, `images\GHH405253.jpeg`
- Duplicate sources: `pages\9247.html`, `pages\22126.html`, `pages\15138.html`

### Full Text

````text
ep 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 11

Test point 2 | PCM connector A (50P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

- Open wire check (FI SUB RLY CL- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector B (6P) No. 2 Test point 2 PCM connector A (50P) No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector B (6P) No. 2

Test point 2 | PCM connector A (50P) No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

- Shorted wire check (FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 16 Test point 2 Body ground Is there continuity? YES Repair a short in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A8 (15 A) in the under-hood fuse/relay box. NO The FI SUB RLY OUT wire is OK. Go to step 8.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A8 (15 A) in the under-hood fuse/relay box.

NO

The FI SUB RLY OUT wire is OK. Go to step 8.

- Shorted wire check (+B DBW line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) No. 14 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse under-hood fuse/relay box. NO The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 14

Test point 2 | Body ground
````

## Chunk 6981: DTC P1659 (L15B7/L15BY)

- Title: DTC P1659 (L15B7/L15BY)
- Source path: `pages\7660.html`
- Chunk ID: `chunk_cbfae62c319e`
- Images: `images\GHH405250.jpeg`, `images\GHH405251.jpeg`, `images\GHH405252.jpeg`, `images\GHH405253.jpeg`
- Duplicate sources: `pages\9247.html`, `pages\22126.html`, `pages\15138.html`

### Full Text

````text
the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse under-hood fuse/relay box. NO The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) No. 14

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short in the +B DBW wire between the No. A8 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box . Also replace the No. A8 (15 A) fuse under-hood fuse/relay box.

NO

The +B DBW wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . Also replace the No. A8 (15 A) fuse in the under-hood fuse/relay box.
````

## Chunk 6982: DTC P1659 (L15BA) (17-21)

- Title: DTC P1659 (L15BA) (17-21)
- Source path: `pages\7661.html`
- Chunk ID: `chunk_499cd71844fd`
- Images: `images\GHH405254.png`, `images\GHH405255.jpeg`, `images\GHH405256.png`, `images\GHH405257.jpeg`, `images\GHH405258.png`, `images\GHH405259.jpeg`
- Duplicate sources: `pages\9248.html`, `pages\22127.html`, `pages\15139.html`

### Full Text

````text
# DTC P1659 (L15BA) (17-21)

DTC P1659 : ETCS Control Relay OFF Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1659 ETCS Control Relay OFF Malfunction Is DTC P1659 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1659 ETCS Control Relay OFF Malfunction

Is DTC P1659 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Fuse check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check the following fuse. Fuse No. A9 (15 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 4. NO Repair a short in the +B DBW wire between the relay circuit board and the No. A9 (15 A) fuse or in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A9 (15 A) fuse.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check the following fuse.

Fuse | No. A9 (15 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 4.

NO

Repair a short in the +B DBW wire between the relay circuit board and the No. A9 (15 A) fuse or in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board. Also replace the No. A9 (15 A) fuse.

- Open wire check (+B DBW line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed Test point 1 Relay circuit board connector C (18P) (female terminals) No. 14: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B DBW wire is OK. Go to step 5. NO Repair an open in the +B DBW wire between the No. A9 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 14:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B DBW wire is OK. Go to step 5.

NO

Repair an open in the +B DBW wire between the No. A9 (15 A) fuse in the under-hood fuse/relay box and the relay circuit board. If needed, replace the under-hood fuse/relay box .

- Open wire check (FI SUB RLY OUT line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 PCM connector A (50P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected
````

## Chunk 6983: DTC P1659 (L15BA) (17-21)

- Title: DTC P1659 (L15BA) (17-21)
- Source path: `pages\7661.html`
- Chunk ID: `chunk_16b25deeb1b8`
- Images: `images\GHH405254.png`, `images\GHH405255.jpeg`, `images\GHH405256.png`, `images\GHH405257.jpeg`, `images\GHH405258.png`, `images\GHH405259.jpeg`
- Duplicate sources: `pages\9248.html`, `pages\22127.html`, `pages\15139.html`

### Full Text

````text
nnector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector C (18P) (female terminals) No. 1: Test point 2 PCM connector A (50P) No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY OUT wire is OK. Go to step 6. NO Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector C (18P) (female terminals) No. 1:

Test point 2 | PCM connector A (50P) No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY OUT wire is OK. Go to step 6.

NO

Repair an open in the FI SUB RLY OUT wire between the PCM (A16) and the relay circuit board.

- Open wire check (FI SUB RLY CL- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 Relay circuit board connector B (6P) (female terminals) No. 2: Test point 2 PCM connector A (50P) No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | Relay circuit board connector B (6P) (female terminals) No. 2:

Test point 2 | PCM connector A (50P) No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The FI SUB RLY CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P1659 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the FI SUB RLY CL- wire between the PCM (A25) and the relay circuit board.
````

## Chunk 6984: DTC P1683 (K20C1) (17-21)

- Title: DTC P1683 (K20C1) (17-21)
- Source path: `pages\7662.html`
- Chunk ID: `chunk_efde62e12863`
- Images: `images\GHH405260.jpeg`
- Duplicate sources: `pages\9249.html`, `pages\22128.html`, `pages\14876.html`

### Full Text

````text
# DTC P1683 (K20C1) (17-21)

DTC P1683 : Throttle Valve Default Position Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1683 Throttle Valve Default Position Spring Performance Problem Is DTC P1683 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

Is DTC P1683 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body default position spring check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body . -3. Push the throttle valve closed as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1683 is indicated, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body .

-3. Push the throttle valve closed as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1683 is indicated, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6985: DTC P1683 (K20C2)

- Title: DTC P1683 (K20C2)
- Source path: `pages\7663.html`
- Chunk ID: `chunk_92506b956021`
- Images: `images\GHH405261.jpeg`
- Duplicate sources: `pages\9250.html`, `pages\22129.html`, `pages\15140.html`

### Full Text

````text
# DTC P1683 (K20C2)

DTC P1683 : Throttle Valve Default Position Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1683 Throttle Valve Default Position Spring Performance Problem Is DTC P1683 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

Is DTC P1683 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body default position spring check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the intake air duct from the throttle body . -3. Push the throttle valve closed as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1683 is indicated, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the intake air duct from the throttle body .

-3. Push the throttle valve closed as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1683 is indicated, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6986: DTC P1683 (L15B7/L15BA/L15BY)

- Title: DTC P1683 (L15B7/L15BA/L15BY)
- Source path: `pages\7664.html`
- Chunk ID: `chunk_138298d0f789`
- Images: `images\GHH405262.jpeg`
- Duplicate sources: `pages\9251.html`, `pages\22130.html`, `pages\15101.html`

### Full Text

````text
# DTC P1683 (L15B7/L15BA/L15BY)

DTC P1683 : Throttle Valve Default Position Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1683 Throttle Valve Default Position Spring Performance Problem Is DTC P1683 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1683 Throttle Valve Default Position Spring Performance Problem

Is DTC P1683 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body default position spring check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect intake air duct F from the throttle body . -3. Push the throttle valve closed as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1683 is indicated, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect intake air duct F from the throttle body .

-3. Push the throttle valve closed as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1683 is indicated, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6987: DTC P1684 (K20C1) (17-21)

- Title: DTC P1684 (K20C1) (17-21)
- Source path: `pages\7665.html`
- Chunk ID: `chunk_e800c3d78198`
- Images: `images\GHH405263.jpeg`
- Duplicate sources: `pages\9252.html`, `pages\22131.html`, `pages\14877.html`

### Full Text

````text
# DTC P1684 (K20C1) (17-21)

DTC P1684 : Throttle Valve Return Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1684 Throttle Valve Return Spring Performance Problem Is DTC P1684 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

Is DTC P1684 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body condition check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body . -3. Push the throttle valve open as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the throttle body inlet pipe and the throttle body connector tube from the throttle body .

-3. Push the throttle valve open as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6988: DTC P1684 (K20C2)

- Title: DTC P1684 (K20C2)
- Source path: `pages\7666.html`
- Chunk ID: `chunk_50580457823c`
- Images: `images\GHH405264.jpeg`
- Duplicate sources: `pages\9253.html`, `pages\22132.html`, `pages\15141.html`

### Full Text

````text
# DTC P1684 (K20C2)

DTC P1684 : Throttle Valve Return Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1684 Throttle Valve Return Spring Performance Problem Is DTC P1684 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

Is DTC P1684 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body condition check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the intake air duct from the throttle body . -3. Push the throttle valve open as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the intake air duct from the throttle body .

-3. Push the throttle valve open as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6989: DTC P1684 (L15B7/L15BA/L15BY)

- Title: DTC P1684 (L15B7/L15BA/L15BY)
- Source path: `pages\7667.html`
- Chunk ID: `chunk_04c8ed1de80e`
- Images: `images\GHH405265.jpeg`
- Duplicate sources: `pages\9254.html`, `pages\22133.html`, `pages\15102.html`

### Full Text

````text
# DTC P1684 (L15B7/L15BA/L15BY)

DTC P1684 : Throttle Valve Return Spring Performance Problem

WARNING: Do not insert your fingers into the installed throttle body when you turn the vehicle to the ON mode, or while the vehicle is in ON mode. If you do, you will seriously injure your fingers if the throttle valve is activated.

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle. -5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds. -6. Turn the vehicle to the ON mode. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P1684 Throttle Valve Return Spring Performance Problem Is DTC P1684 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Hold the engine speed at 3, 000 rpm without load (CVT in P or N, M/T in neutral) until the radiator fan comes on, then let it idle.

-5. Turn the vehicle to the OFF (LOCK) mode, and wait 10 seconds.

-6. Turn the vehicle to the ON mode.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P1684 Throttle Valve Return Spring Performance Problem

Is DTC P1684 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the throttle body and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Throttle body condition check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect intake air duct F from the throttle body . -3. Push the throttle valve open as shown. Courtesy of HONDA, U.S.A., INC. -4. Release the throttle valve. Does the throttle valve return? YES Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body . NO Replace the throttle body .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect intake air duct F from the throttle body .

-3. Push the throttle valve open as shown.

Courtesy of HONDA, U.S.A., INC.

-4. Release the throttle valve.

Does the throttle valve return?

YES

Clean the throttle body . If DTC P1684 is indicated again, replace the throttle body .

NO

Replace the throttle body .
````

## Chunk 6990: DTC P16BB (K20C1) (17-21)

- Title: DTC P16BB (K20C1) (17-21)
- Source path: `pages\7668.html`
- Chunk ID: `chunk_69f33c96d592`
- Images: none
- Duplicate sources: `pages\9255.html`, `pages\22134.html`, `pages\14878.html`

### Full Text

````text
# DTC P16BB (K20C1) (17-21)

DTC P16BB : Alternator B Terminal Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Record all the on-board snapshots with the HDS. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Start the engine. Check under these conditions: A/C on Temperature control at maximum cool Blower fan at maximum speed Headlights on high beam Rear window defogger on -6. Hold the engine speed at 2, 000 rpm for 1 minute. -7. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16BB Alternator B Terminal Circuit Low Voltage Is DTC P16BB indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

-1. Record all the on-board snapshots with the HDS.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Start the engine.

Check under these conditions:

- A/C on

- Temperature control at maximum cool

- Blower fan at maximum speed

- Headlights on high beam

- Rear window defogger on

-6. Hold the engine speed at 2, 000 rpm for 1 minute.

-7. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

Is DTC P16BB indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

- +B terminal check -1. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box (+B line). Are the connections and terminals OK? YES Go to step 3. NO Repair the connections or the terminals.

-1. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box (+B line).

Are the connections and terminals OK?

YES

Go to step 3.

NO

Repair the connections or the terminals.

- Open wire check (+B line) -1. Check for an open in the wire between the alternator and the under-hood fuse/relay box at the engine wire harness. Is the harness OK? YES Replace the alternator . NO Repair an open in the +B wire between the alternator and the under-hood fuse/relay box.

-1. Check for an open in the wire between the alternator and the under-hood fuse/relay box at the engine wire harness.

Is the harness OK?

YES

Replace the alternator .

NO

Repair an open in the +B wire between the alternator and the under-hood fuse/relay box.
````

## Chunk 6991: DTC P16BB (K20C2)

- Title: DTC P16BB (K20C2)
- Source path: `pages\7669.html`
- Chunk ID: `chunk_34431b879dcb`
- Images: none
- Duplicate sources: `pages\9256.html`, `pages\22135.html`, `pages\15142.html`

### Full Text

````text
# DTC P16BB (K20C2)

DTC P16BB : Alternator B Terminal Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. Check under these conditions: A/C on Temperature control at maximum cool Blower fan at maximum speed Headlights on high beam Rear window defogger on -5. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16BB Alternator B Terminal Circuit Low Voltage Is DTC P16BB indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and 12 volt battery terminal fuse box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

Check under these conditions:

- A/C on

- Temperature control at maximum cool

- Blower fan at maximum speed

- Headlights on high beam

- Rear window defogger on

-5. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

Is DTC P16BB indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and 12 volt battery terminal fuse box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

- +B terminal check -1. Check for poor connections or loose terminals at the alternator and the 12 volt battery terminal fuse box (+B line). Are the connections and terminals OK? YES Go to step 3. NO Repair the connections or the terminals.

-1. Check for poor connections or loose terminals at the alternator and the 12 volt battery terminal fuse box (+B line).

Are the connections and terminals OK?

YES

Go to step 3.

NO

Repair the connections or the terminals.

- Open wire check (+B line) -1. Check for an open in the wire between the alternator and the 12 volt battery terminal fuse box at the engine harness. Is the harness OK? YES Replace the alternator . NO Repair an open in the +B wire between the alternator and the 12 volt battery terminal fuse box.

-1. Check for an open in the wire between the alternator and the 12 volt battery terminal fuse box at the engine harness.

Is the harness OK?

YES

Replace the alternator .

NO

Repair an open in the +B wire between the alternator and the 12 volt battery terminal fuse box.
````

## Chunk 6992: DTC P16BB (L15B7/L15BA/L15BY)

- Title: DTC P16BB (L15B7/L15BA/L15BY)
- Source path: `pages\7670.html`
- Chunk ID: `chunk_4801bb2b7c11`
- Images: none
- Duplicate sources: `pages\9257.html`, `pages\22136.html`, `pages\15143.html`

### Full Text

````text
# DTC P16BB (L15B7/L15BA/L15BY)

DTC P16BB : Alternator B Terminal Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. Check under these conditions: A/C on Temperature control at maximum cool Blower fan at maximum speed Headlights on high beam Rear window defogger on -5. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16BB Alternator B Terminal Circuit Low Voltage Is DTC P16BB indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

Check under these conditions:

- A/C on

- Temperature control at maximum cool

- Blower fan at maximum speed

- Headlights on high beam

- Rear window defogger on

-5. Hold the engine speed at 2, 000 rpm without load (CVT in P or N, M/T in neutral) for 1 minute.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16BB Alternator B Terminal Circuit Low Voltage

Is DTC P16BB indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and under-hood fuse/relay box. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot . Also check the 12 volt battery performance .

- +B terminal check -1. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box (+B line). Are the connections and terminals OK? YES Go to step 3. NO Repair the connections or the terminals.

-1. Check for poor connections or loose terminals at the alternator and the under-hood fuse/relay box (+B line).

Are the connections and terminals OK?

YES

Go to step 3.

NO

Repair the connections or the terminals.

- Open wire check (+B line) -1. Check for an open in the wire between the alternator and the under-hood fuse/relay box at the engine harness. Is the harness OK? YES Replace the alternator . NO Repair an open in the +B wire between the alternator and the under-hood fuse/relay box.

-1. Check for an open in the wire between the alternator and the under-hood fuse/relay box at the engine harness.

Is the harness OK?

YES

Replace the alternator .

NO

Repair an open in the +B wire between the alternator and the under-hood fuse/relay box.
````

## Chunk 6993: DTC P16E2 (K20C1) (17-21)

- Title: DTC P16E2 (K20C1) (17-21)
- Source path: `pages\7671.html`
- Chunk ID: `chunk_c4443191b27b`
- Images: `images\GHH405266.png`, `images\GHH405267.jpeg`, `images\GHH405268.png`, `images\GHH405269.jpeg`, `images\GHH405270.png`, `images\GHH405271.jpeg`, `images\GHH405272.png`, `images\GHH405273.jpeg`
- Duplicate sources: `pages\9258.html`, `pages\22137.html`, `pages\14879.html`

### Full Text

````text
# DTC P16E2 (K20C1) (17-21)

DTC P16E2 : PGM-FI-ACG LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for a loose terminal on the alternator (+B terminal). If the alternator +B terminal was loose, DTC P16E2 will be stored.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode, and wait 10 seconds. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode, and wait 10 seconds.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (short in LIN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Alternator 1P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time: 12 volt battery sensor 2P connector PCM connector No. 1 (96P) Does continuity go away when one of the above connectors is disconnected? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time:

- 12 volt battery sensor 2P connector

- PCM connector No. 1 (96P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

- Determine possible failure area (alternator, others) -1. Reconnect the alternator 1P connector. -2. Disconnect the following connector.
````

## Chunk 6994: DTC P16E2 (K20C1) (17-21)

- Title: DTC P16E2 (K20C1) (17-21)
- Source path: `pages\7671.html`
- Chunk ID: `chunk_d7f8e7025e30`
- Images: `images\GHH405266.png`, `images\GHH405267.jpeg`, `images\GHH405268.png`, `images\GHH405269.jpeg`, `images\GHH405270.png`, `images\GHH405271.jpeg`, `images\GHH405272.png`, `images\GHH405273.jpeg`
- Duplicate sources: `pages\9258.html`, `pages\22137.html`, `pages\14879.html`

### Full Text

````text
, the 12 volt battery sensor, and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time:

- 12 volt battery sensor 2P connector

- PCM connector No. 1 (96P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

- Determine possible failure area (alternator, others) -1. Reconnect the alternator 1P connector. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the alternator . NO Go to step 6.

-1. Reconnect the alternator 1P connector.

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the alternator .

NO

Go to step 6.

- Open wire check (LIN line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. Alternator 1P connector PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Alternator 1P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Alternator 1P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 94 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN wire between PCM connector No. 1 terminal No. 94 and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Alternator 1P connector

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Alternator 1P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Alternator 1P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 94

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN wire between PCM connector No. 1 terminal No. 94 and the alternator.

- Open wire check (LIN line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. Alternator 1P connector PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Alternator 1P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 94 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN wire is OK. Replace the alternator . NO Repair an open in the LIN wire between PCM connector No. 1 terminal No. 94 and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Alternator 1P connector

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector No. 1 (96P): disconnected
````

## Chunk 6995: DTC P16E2 (K20C1) (17-21)

- Title: DTC P16E2 (K20C1) (17-21)
- Source path: `pages\7671.html`
- Chunk ID: `chunk_42dbfb972183`
- Images: `images\GHH405266.png`, `images\GHH405267.jpeg`, `images\GHH405268.png`, `images\GHH405269.jpeg`, `images\GHH405270.png`, `images\GHH405271.jpeg`, `images\GHH405272.png`, `images\GHH405273.jpeg`
- Duplicate sources: `pages\9258.html`, `pages\22137.html`, `pages\14879.html`

### Full Text

````text
tinuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 Alternator 1P connector (female terminals) No. 1: Test point 2 PCM connector No. 1 (96P) No. 94 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN wire is OK. Replace the alternator . NO Repair an open in the LIN wire between PCM connector No. 1 terminal No. 94 and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Alternator 1P connector

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | Alternator 1P connector (female terminals) No. 1:

Test point 2 | PCM connector No. 1 (96P) No. 94

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN wire is OK. Replace the alternator .

NO

Repair an open in the LIN wire between PCM connector No. 1 terminal No. 94 and the alternator.
````

## Chunk 6996: DTC P16E2 (K20C2)

- Title: DTC P16E2 (K20C2)
- Source path: `pages\7672.html`
- Chunk ID: `chunk_fae359e81cc3`
- Images: `images\GHH405274.jpeg`, `images\GHH405275.jpeg`, `images\GHH405276.jpeg`, `images\GHH405277.jpeg`
- Duplicate sources: `pages\9259.html`, `pages\22138.html`, `pages\15144.html`

### Full Text

````text
# DTC P16E2 (K20C2)

DTC P16E2 : PGM-FI-ACG LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for a loose terminal on the alternator (+B terminal). If the alternator +B terminal was loose, DTC P16E2 will be stored.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait 10 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait 10 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (short in LIN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Alternator 1P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time: PCM connector A (50P) 12 volt battery sensor 2P connector Does continuity go away when one of the above connectors is disconnected? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time:

- PCM connector A (50P)

- 12 volt battery sensor 2P connector

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

- Determine possible failure area (alternator, others) -1. Reconnect the following connector. Alternator 1P connector -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No.
````

## Chunk 6997: DTC P16E2 (K20C2)

- Title: DTC P16E2 (K20C2)
- Source path: `pages\7672.html`
- Chunk ID: `chunk_19b3880e7066`
- Images: `images\GHH405274.jpeg`, `images\GHH405275.jpeg`, `images\GHH405276.jpeg`, `images\GHH405277.jpeg`
- Duplicate sources: `pages\9259.html`, `pages\22138.html`, `pages\15144.html`

### Full Text

````text
cting these connectors, one at a time:

- PCM connector A (50P)

- 12 volt battery sensor 2P connector

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

- Determine possible failure area (alternator, others) -1. Reconnect the following connector. Alternator 1P connector -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the alternator . NO Go to step 6.

-1. Reconnect the following connector.

Alternator 1P connector

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the alternator .

NO

Go to step 6.

- Open wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. Alternator 1P connector PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Alternator 1P connector: disconnected PCM connector A (50P): disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN/LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN/LIN (BATT SENSOR) wire between the PCM (A10) and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN/LIN (BATT SENSOR) wire between the PCM (A10) and the alternator.

- Open wire check (LIN/LIN (BATT SENSOR) line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. Alternator 1P connector PCM connector A (50P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected PCM connector A (50P): disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the alternator . NO Repair an open in the LIN/LIN (BATT SENSOR) wire between the PCM (A10) and the alternator.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN/LIN (BATT SENSOR) wire is OK.
````

## Chunk 6998: DTC P16E2 (K20C2)

- Title: DTC P16E2 (K20C2)
- Source path: `pages\7672.html`
- Chunk ID: `chunk_9815c4e37a14`
- Images: `images\GHH405274.jpeg`, `images\GHH405275.jpeg`, `images\GHH405276.jpeg`, `images\GHH405277.jpeg`
- Duplicate sources: `pages\9259.html`, `pages\22138.html`, `pages\15144.html`

### Full Text

````text
nector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the alternator . NO Repair an open in the LIN/LIN (BATT SENSOR) wire between the PCM (A10) and the alternator.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the alternator .

NO

Repair an open in the LIN/LIN (BATT SENSOR) wire between the PCM (A10) and the alternator.
````

## Chunk 6999: DTC P16E2 (L15B7/L15BA/L15BY)

- Title: DTC P16E2 (L15B7/L15BA/L15BY)
- Source path: `pages\7673.html`
- Chunk ID: `chunk_9711882379ab`
- Images: `images\GHH405278.jpeg`, `images\GHH405279.jpeg`, `images\GHH405280.jpeg`, `images\GHH405281.jpeg`
- Duplicate sources: `pages\9260.html`, `pages\22139.html`, `pages\15145.html`

### Full Text

````text
# DTC P16E2 (L15B7/L15BA/L15BY)

DTC P16E2 : PGM-FI-ACG LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for a loose terminal on the alternator (+B terminal). If the alternator +B terminal was loose, DTC P16E2 will be stored.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode, and wait 10 seconds. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode, and wait 10 seconds.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the alternator and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (LIN (BATT SENSOR)/LIN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Alternator 1P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN (BATT SENSOR)/LIN line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time: PCM connector A (50P) 12 volt battery sensor 2P connector Does continuity go away when one of the above connectors is disconnected? YES The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN (BATT SENSOR)/LIN wire between the PCM (A10), the alternator, the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time:

- PCM connector A (50P)

- 12 volt battery sensor 2P connector

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN (BATT SENSOR)/LIN wire between the PCM (A10), the alternator, the 12 volt battery sensor.

- Determine possible failure area (alternator, others) -1. Reconnect the alternator 1P connector. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2.
````

## Chunk 7000: DTC P16E2 (L15B7/L15BA/L15BY)

- Title: DTC P16E2 (L15B7/L15BA/L15BY)
- Source path: `pages\7673.html`
- Chunk ID: `chunk_3726cabfa6df`
- Images: `images\GHH405278.jpeg`, `images\GHH405279.jpeg`, `images\GHH405280.jpeg`, `images\GHH405281.jpeg`
- Duplicate sources: `pages\9260.html`, `pages\22139.html`, `pages\15145.html`

### Full Text

````text
the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between the alternator 1P connector terminal and body ground, while disconnecting these connectors, one at a time:

- PCM connector A (50P)

- 12 volt battery sensor 2P connector

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN (BATT SENSOR)/LIN wire between the PCM (A10), the alternator, the 12 volt battery sensor.

- Determine possible failure area (alternator, others) -1. Reconnect the alternator 1P connector. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the alternator . NO Go to step 6.

-1. Reconnect the alternator 1P connector.

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the alternator .

NO

Go to step 6.

- Open wire check (LIN (BATT SENSOR)/LIN line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. Alternator 1P connector PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Alternator 1P connector: disconnected PCM connector A (50P): disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR)/LIN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN (BATT SENSOR)/LIN wire between the PCM (A10) and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E2 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN (BATT SENSOR)/LIN wire between the PCM (A10) and the alternator.

- Open wire check (LIN (BATT SENSOR)/LIN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. Alternator 1P connector PCM connector A (50P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected PCM connector A (50P): disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR)/LIN wire is OK. Replace the alternator . NO Repair an open in the LIN (BATT SENSOR)/LIN wire between the PCM (A10) and the alternator.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1
````

## Chunk 7001: DTC P16E2 (L15B7/L15BA/L15BY)

- Title: DTC P16E2 (L15B7/L15BA/L15BY)
- Source path: `pages\7673.html`
- Chunk ID: `chunk_3b6123abd881`
- Images: `images\GHH405278.jpeg`, `images\GHH405279.jpeg`, `images\GHH405280.jpeg`, `images\GHH405281.jpeg`
- Duplicate sources: `pages\9260.html`, `pages\22139.html`, `pages\15145.html`

### Full Text

````text
mode Alternator 1P connector: disconnected PCM connector A (50P): disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR)/LIN wire is OK. Replace the alternator . NO Repair an open in the LIN (BATT SENSOR)/LIN wire between the PCM (A10) and the alternator.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

Alternator 1P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Replace the alternator .

NO

Repair an open in the LIN (BATT SENSOR)/LIN wire between the PCM (A10) and the alternator.
````

## Chunk 7002: DTC P16E3 (K20C1) (17-21)

- Title: DTC P16E3 (K20C1) (17-21)
- Source path: `pages\7674.html`
- Chunk ID: `chunk_9b4596f70540`
- Images: `images\GHH405282.png`, `images\GHH405283.jpeg`, `images\GHH405284.png`, `images\GHH405285.jpeg`, `images\GHH405286.png`, `images\GHH405287.jpeg`, `images\GHH405288.png`, `images\GHH405289.jpeg`, `images\GHH405290.png`, `images\GHH405291.jpeg`
- Duplicate sources: `pages\9261.html`, `pages\22140.html`, `pages\14880.html`

### Full Text

````text
# DTC P16E3 (K20C1) (17-21)

DTC P16E3 : PGM-FI-Battery Sensor LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for loose terminals on the 12 volt battery sensor (12 volt battery negative (-) terminal).

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait for 5 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait for 5 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (short in LIN/LIN (BATT SENSOR) line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No. 2: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector (female terminals) No. 2:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time: Alternator 1P connector PCM connector No. 1 (96P) Does continuity go away when one of the above connectors is disconnected? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector No. 1 (96P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3.
````

## Chunk 7003: DTC P16E3 (K20C1) (17-21)

- Title: DTC P16E3 (K20C1) (17-21)
- Source path: `pages\7674.html`
- Chunk ID: `chunk_3949760bd33d`
- Images: `images\GHH405282.png`, `images\GHH405283.jpeg`, `images\GHH405284.png`, `images\GHH405285.jpeg`, `images\GHH405286.png`, `images\GHH405287.jpeg`, `images\GHH405288.png`, `images\GHH405289.jpeg`, `images\GHH405290.png`, `images\GHH405291.jpeg`
- Duplicate sources: `pages\9261.html`, `pages\22140.html`, `pages\14880.html`

### Full Text

````text
Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector No. 1 (96P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94, the 12 volt battery sensor, and the alternator.

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the 12 volt battery sensor . NO Go to step 6.

-1. Reconnect the 12 volt battery sensor 2P connector.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the 12 volt battery sensor .

NO

Go to step 6.

- Open wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. 12 volt battery sensor 2P connector PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected 12 volt battery sensor 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 94 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN/LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94 and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

12 volt battery sensor 2P connector

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

12 volt battery sensor 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | 12 volt battery sensor 2P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 94

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94 and the 12 volt battery sensor.

- Fuse check -1. Check the following fuse. Fuse No. A24 (10 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 8. NO Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No.
````

## Chunk 7004: DTC P16E3 (K20C1) (17-21)

- Title: DTC P16E3 (K20C1) (17-21)
- Source path: `pages\7674.html`
- Chunk ID: `chunk_c8f7978cc016`
- Images: `images\GHH405282.png`, `images\GHH405283.jpeg`, `images\GHH405284.png`, `images\GHH405285.jpeg`, `images\GHH405286.png`, `images\GHH405287.jpeg`, `images\GHH405288.png`, `images\GHH405289.jpeg`, `images\GHH405290.png`, `images\GHH405291.jpeg`
- Duplicate sources: `pages\9261.html`, `pages\22140.html`, `pages\14880.html`

### Full Text

````text
ation Under-hood fuse/relay box Is the fuse OK? YES Go to step 8. NO Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No. 1: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HORN wire is OK. Go to step 9. NO Repair an open in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse in the under-hood fuse/relay box.

-1. Disconnect the following connector.

12 volt battery sensor 2P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector (female terminals) No. 1:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B HORN wire is OK. Go to step 9.

NO

Repair an open in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse in the under-hood fuse/relay box.

- Open wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector No. 1 (96P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected PCM connector No. 1 (96P): disconnected Test point 1 12 volt battery sensor 2P connector (female terminals) No. 2: Test point 2 PCM connector No. 1 (96P) No. 94 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor . NO Repair an open in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94 and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector No. 1 (96P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

PCM connector No. 1 (96P): disconnected

Test point 1 | 12 volt battery sensor 2P connector (female terminals) No. 2:

Test point 2 | PCM connector No. 1 (96P) No. 94

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor .

NO

Repair an open in the LIN/LIN (BATT SENSOR) wire between PCM connector No. 1 terminal No. 94 and the 12 volt battery sensor.
````

## Chunk 7005: DTC P16E3 (K20C2)

- Title: DTC P16E3 (K20C2)
- Source path: `pages\7675.html`
- Chunk ID: `chunk_460e7c3b3089`
- Images: `images\GHH405292.jpeg`, `images\GHH405293.jpeg`, `images\GHH405294.jpeg`, `images\GHH405295.jpeg`, `images\GHH405296.jpeg`
- Duplicate sources: `pages\9262.html`, `pages\22141.html`, `pages\15146.html`

### Full Text

````text
# DTC P16E3 (K20C2)

DTC P16E3 : PGM-FI-Battery Sensor LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for loose terminals on the 12 volt battery sensor (12 volt battery negative (-) terminal).

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait for 10 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait for 10 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (short in LIN (BATT SENSOR) line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN/LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time: Alternator 1P connector PCM connector A (50P) Does continuity go away when one of the above connectors is disconnected? YES The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector A (50P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3. Measure the voltage between test points 1 and 2.
````

## Chunk 7006: DTC P16E3 (K20C2)

- Title: DTC P16E3 (K20C2)
- Source path: `pages\7675.html`
- Chunk ID: `chunk_095e74b04756`
- Images: `images\GHH405292.jpeg`, `images\GHH405293.jpeg`, `images\GHH405294.jpeg`, `images\GHH405295.jpeg`, `images\GHH405296.jpeg`
- Duplicate sources: `pages\9262.html`, `pages\22141.html`, `pages\15146.html`

### Full Text

````text
the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector A (50P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN/LIN (BATT SENSOR) wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN/LIN (BATT SENSOR) wire between the PCM (A10), the alternator, and the 12 volt battery sensor.

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the 12 volt battery sensor . NO Go to step 6.

-1. Reconnect the 12 volt battery sensor 2P connector.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the 12 volt battery sensor .

NO

Go to step 6.

- Open wire check (LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. 12 volt battery sensor 2P connector PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected 12 volt battery sensor 2P connector: disconnected PCM connector A (50P): disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

12 volt battery sensor 2P connector

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

12 volt battery sensor 2P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

- Fuse check -1. Check the following fuse. Fuse No. A24 (10 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 8. NO Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HORN wire is OK. Go to step 9. NO Repair an open in the +B HORN wire between the No. A24 (10 A) fuse in the under-hood fuse/relay box and the 12 volt battery sensor.

-1.
````

## Chunk 7007: DTC P16E3 (K20C2)

- Title: DTC P16E3 (K20C2)
- Source path: `pages\7675.html`
- Chunk ID: `chunk_29b218279e82`
- Images: `images\GHH405292.jpeg`, `images\GHH405293.jpeg`, `images\GHH405294.jpeg`, `images\GHH405295.jpeg`, `images\GHH405296.jpeg`
- Duplicate sources: `pages\9262.html`, `pages\22141.html`, `pages\15146.html`

### Full Text

````text
A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HORN wire is OK. Go to step 9. NO Repair an open in the +B HORN wire between the No. A24 (10 A) fuse in the under-hood fuse/relay box and the 12 volt battery sensor.

-1. Disconnect the following connector.

12 volt battery sensor 2P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B HORN wire is OK. Go to step 9.

NO

Repair an open in the +B HORN wire between the No. A24 (10 A) fuse in the under-hood fuse/relay box and the 12 volt battery sensor.

- Open wire check (LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected PCM connector A (50P): disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor . NO Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor .

NO

Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.
````

## Chunk 7008: DTC P16E3 (L15B7)

- Title: DTC P16E3 (L15B7)
- Source path: `pages\7676.html`
- Chunk ID: `chunk_499802fe728b`
- Images: `images\GHH405297.jpeg`, `images\GHH405298.jpeg`, `images\GHH405299.jpeg`, `images\GHH405300.jpeg`, `images\GHH405301.jpeg`
- Duplicate sources: `pages\9263.html`, `pages\22142.html`, `pages\15147.html`

### Full Text

````text
# DTC P16E3 (L15B7)

DTC P16E3 : PGM-FI-Battery Sensor LIN Communication Error

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- Check for loose terminals on the 12 volt battery sensor (12 volt battery negative (-) terminal).

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS, and wait for 5 seconds. -3. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E3 PGM-FI-Battery Sensor LIN Communication Error Is DTC P16E3 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS, and wait for 5 seconds.

-3. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E3 PGM-FI-Battery Sensor LIN Communication Error

Is DTC P16E3 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the 12 volt battery sensor and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- DTC check -1. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E2 PGM-FI-ACG LIN Communication Error Is DTC P16E2 indicated? YES Go to step 3. NO Go to step 7.

-1. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E2 PGM-FI-ACG LIN Communication Error

Is DTC P16E2 indicated?

YES

Go to step 3.

NO

Go to step 7.

- Determine possible failure area (LIN (BATT SENSOR) line shorted, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. 12 volt battery sensor 2P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

12 volt battery sensor 2P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 5.

- Shorted wire check (LIN (BATT SENSOR)/LIN line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time: Alternator 1P connector PCM connector A (50P) Does continuity go away when one of the above connectors is disconnected? YES The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected. NO Repair a short in the LIN (BATT SENSOR)/LIN wire between the 12 volt battery sensor, the alternator, and the PCM (A10).

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector A (50P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN (BATT SENSOR)/LIN wire between the 12 volt battery sensor, the alternator, and the PCM (A10).

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3. Measure the voltage between test points 1 and 2.
````

## Chunk 7009: DTC P16E3 (L15B7)

- Title: DTC P16E3 (L15B7)
- Source path: `pages\7676.html`
- Chunk ID: `chunk_9ca40410b122`
- Images: `images\GHH405297.jpeg`, `images\GHH405298.jpeg`, `images\GHH405299.jpeg`, `images\GHH405300.jpeg`, `images\GHH405301.jpeg`
- Duplicate sources: `pages\9263.html`, `pages\22142.html`, `pages\15147.html`

### Full Text

````text
the HDS, and wait more than 1 minute.

Continue to check for continuity between 12 volt battery sensor 2P connector terminal No. 2 and body ground, while disconnecting these connectors, one at a time:

- Alternator 1P connector

- PCM connector A (50P)

Does continuity go away when one of the above connectors is disconnected?

YES

The LIN (BATT SENSOR)/LIN wire is OK. Replace the part that caused an open when it was disconnected.

NO

Repair a short in the LIN (BATT SENSOR)/LIN wire between the 12 volt battery sensor, the alternator, and the PCM (A10).

- Determine possible failure area (12 volt battery sensor, others) -1. Reconnect the 12 volt battery sensor 2P connector. -2. Disconnect the following connector. Alternator 1P connector -3. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected Test point 1 Alternator 1P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the 12 volt battery sensor . NO Go to step 6.

-1. Reconnect the 12 volt battery sensor 2P connector.

-2. Disconnect the following connector.

Alternator 1P connector

-3. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

Test point 1 | Alternator 1P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the 12 volt battery sensor .

NO

Go to step 6.

- Open wire check (LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connectors. 12 volt battery sensor 2P connector PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Alternator 1P connector: disconnected 12 volt battery sensor 2P connector: disconnected PCM connector A (50P): disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM . NO Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connectors.

12 volt battery sensor 2P connector

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Alternator 1P connector: disconnected

12 volt battery sensor 2P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR) wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E3 goes away and the PCM was substituted, replace the original PCM .

NO

Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

- Fuse check -1. Check the following fuse. Fuse No. A24 (10 A) Location Under-hood fuse/relay box Is the fuse OK? YES Go to step 8. NO Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HORN wire is OK. Go to step 9. NO Repair an open in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse in the under-hood fuse/relay box.

-1.
````

## Chunk 7010: DTC P16E3 (L15B7)

- Title: DTC P16E3 (L15B7)
- Source path: `pages\7676.html`
- Chunk ID: `chunk_75bc26c29ac9`
- Images: `images\GHH405297.jpeg`, `images\GHH405298.jpeg`, `images\GHH405299.jpeg`, `images\GHH405300.jpeg`, `images\GHH405301.jpeg`
- Duplicate sources: `pages\9263.html`, `pages\22142.html`, `pages\15147.html`

### Full Text

````text
A24 (10 A)

Location | Under-hood fuse/relay box

Is the fuse OK?

YES

Go to step 8.

NO

Repair a short in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse. Also replace the No. A24 (10 A) fuse.

- Open wire check (+B HORN line) -1. Disconnect the following connector. 12 volt battery sensor 2P connector -2. Measure the voltage between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected Test point 1 12 volt battery sensor 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there battery voltage? YES The +B HORN wire is OK. Go to step 9. NO Repair an open in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse in the under-hood fuse/relay box.

-1. Disconnect the following connector.

12 volt battery sensor 2P connector

-2. Measure the voltage between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there battery voltage?

YES

The +B HORN wire is OK. Go to step 9.

NO

Repair an open in the +B HORN wire between the 12 volt battery sensor and the No. A24 (10 A) fuse in the under-hood fuse/relay box.

- Open wire check (LIN (BATT SENSOR) line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector A (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode 12 volt battery sensor 2P connector: disconnected PCM connector A (50P): disconnected Test point 1 12 volt battery sensor 2P connector No. 2 Test point 2 PCM connector A (50P) No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor . NO Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

12 volt battery sensor 2P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | 12 volt battery sensor 2P connector No. 2

Test point 2 | PCM connector A (50P) No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LIN (BATT SENSOR) wire is OK. Replace the 12 volt battery sensor .

NO

Repair an open in the LIN (BATT SENSOR) wire between the PCM (A10) and the 12 volt battery sensor.
````

## Chunk 7011: DTC P16E4 (K20C1) (17-21)

- Title: DTC P16E4 (K20C1) (17-21)
- Source path: `pages\7677.html`
- Chunk ID: `chunk_b3b2ba68b39e`
- Images: none
- Duplicate sources: `pages\9264.html`, `pages\22143.html`, `pages\14881.html`

### Full Text

````text
# DTC P16E4 (K20C1) (17-21)

DTC P16E4 : ACG High-temperature

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored when the alternator temperature is high.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

DTC (PGM-FI)

- Problem verification -1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E4 ACG High-temperature DTC (PGM-FI) Is DTC P16E4 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.

-1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

DTC (PGM-FI)

Is DTC P16E4 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.
````

## Chunk 7012: DTC P16E4 (K20C2)

- Title: DTC P16E4 (K20C2)
- Source path: `pages\7678.html`
- Chunk ID: `chunk_2604c542417a`
- Images: none
- Duplicate sources: `pages\9265.html`, `pages\22144.html`, `pages\15148.html`

### Full Text

````text
# DTC P16E4 (K20C2)

DTC P16E4 : ACG High-temperature

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored when the alternator temperature is high.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

DTC (PGM-FI)

- Problem verification -1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS, and wait 1 minute or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E4 ACG High-temperature Is DTC P16E4 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.

-1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS, and wait 1 minute or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

Is DTC P16E4 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.
````

## Chunk 7013: DTC P16E4 (L15B7/L15BA/L15BY)

- Title: DTC P16E4 (L15B7/L15BA/L15BY)
- Source path: `pages\7679.html`
- Chunk ID: `chunk_d3ee2136e316`
- Images: none
- Duplicate sources: `pages\9266.html`, `pages\22145.html`, `pages\15149.html`

### Full Text

````text
# DTC P16E4 (L15B7/L15BA/L15BY)

DTC P16E4 : ACG High-temperature

NOTE:

- Before you troubleshoot, review the general troubleshooting information .

- This DTC is stored when the alternator temperature is high.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

DTC (PGM-FI)

- Problem verification -1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS, and wait 1 minute or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E4 ACG High-temperature Is DTC P16E4 indicated? YES The failure is duplicated. Replace the alternator . NO Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.

-1. If the temperature of the engine and the alternator is high, open the hood to cool the engine compartment.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS, and wait 1 minute or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E4 ACG High-temperature

Is DTC P16E4 indicated?

YES

The failure is duplicated. Replace the alternator .

NO

Intermittent failure, the system is OK at this time. Check the cause of the high temperature, and repair it.
````

## Chunk 7014: DTC P16E6 (K20C2)

- Title: DTC P16E6 (K20C2)
- Source path: `pages\7680.html`
- Chunk ID: `chunk_9b7f22e249dd`
- Images: `images\GHH405302.jpeg`, `images\GHH405303.jpeg`
- Duplicate sources: `pages\9267.html`, `pages\22146.html`, `pages\15150.html`

### Full Text

````text
# DTC P16E6 (K20C2)

DTC P16E6 : Transmission Range Switch START Switch Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16E6 Transmission Range Switch START Switch Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Shift the transmission to other than P or N position/mode, and wait 5 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E6 Transmission Range Switch START Switch Circuit Malfunction Is DTC P16E6 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmission range switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Shift the transmission to other than P or N position/mode, and wait 5 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E6 Transmission Range Switch START Switch Circuit Malfunction

Is DTC P16E6 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmission range switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (short in ATP ST/ATP-ST wire, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 9 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 9

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 3.

- Transmission range switch check -1. Shift the transmission to other than P or N position. -2. At the transmission range switch side, check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 5 (transmission range switch side) Test point 2 Transmission range switch 10P connector No. 9 (transmission range switch side) Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the transmission range switch . NO Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

-1. Shift the transmission to other than P or N position.

-2. At the transmission range switch side, check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 5 (transmission range switch side)

Test point 2 | Transmission range switch 10P connector No. 9 (transmission range switch side)

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the transmission range switch .

NO

Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck.
````

## Chunk 7015: DTC P16E6 (K20C2)

- Title: DTC P16E6 (K20C2)
- Source path: `pages\7680.html`
- Chunk ID: `chunk_7205df56f81f`
- Images: `images\GHH405302.jpeg`, `images\GHH405303.jpeg`
- Duplicate sources: `pages\9267.html`, `pages\22146.html`, `pages\15150.html`

### Full Text

````text
or N position.

-2. At the transmission range switch side, check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 5 (transmission range switch side)

Test point 2 | Transmission range switch 10P connector No. 9 (transmission range switch side)

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the transmission range switch .

NO

Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (ATP ST/ATP-ST line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 Body ground Is there continuity? YES Repair a short in the ATP ST/ATP-ST wire between the PCM (E67) and the transmission range switch. NO The ATP ST/ATP-ST wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 67

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ATP ST/ATP-ST wire between the PCM (E67) and the transmission range switch.

NO

The ATP ST/ATP-ST wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 7016: DTC P16E6 (L15B7/L15BA/L15BY)

- Title: DTC P16E6 (L15B7/L15BA/L15BY)
- Source path: `pages\7681.html`
- Chunk ID: `chunk_2fff694a1b65`
- Images: `images\GHH405304.jpeg`, `images\GHH405305.jpeg`
- Duplicate sources: `pages\9268.html`, `pages\22147.html`, `pages\15151.html`

### Full Text

````text
# DTC P16E6 (L15B7/L15BA/L15BY)

DTC P16E6 : Transmission Range Switch START Switch Circuit Malfunction

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16E6 Transmission Range Switch START Switch Circuit Malfunction

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Shift the transmission to other than P or N position/mode, and wait 5 seconds or more. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16E6 Transmission Range Switch START Switch Circuit Malfunction Is DTC P16E6 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmission range switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Shift the transmission to other than P or N position/mode, and wait 5 seconds or more.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16E6 Transmission Range Switch START Switch Circuit Malfunction

Is DTC P16E6 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmission range switch and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Determine possible failure area (short in ATPST/ATP-ST wire, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 7 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 4. NO Go to step 3.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 7

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 4.

NO

Go to step 3.

- Transmission range switch check -1. Shift the transmission to other than P or N position. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 7 (transmission range switch side) Test point 2 Transmission range switch 10P connector No. 1 (transmission range switch side) Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the transmission range switch . NO Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

-1. Shift the transmission to other than P or N position.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 7 (transmission range switch side)

Test point 2 | Transmission range switch 10P connector No. 1 (transmission range switch side)

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the transmission range switch .

NO

Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 7017: DTC P16E6 (L15B7/L15BA/L15BY)

- Title: DTC P16E6 (L15B7/L15BA/L15BY)
- Source path: `pages\7681.html`
- Chunk ID: `chunk_16125e8d02de`
- Images: `images\GHH405304.jpeg`, `images\GHH405305.jpeg`
- Duplicate sources: `pages\9268.html`, `pages\22147.html`, `pages\15151.html`

### Full Text

````text
between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 7 (transmission range switch side)

Test point 2 | Transmission range switch 10P connector No. 1 (transmission range switch side)

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the transmission range switch .

NO

Check for poor connections or loose terminals at the transmission range switch and the PCM, and test the transmission range switch . If they are OK, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

- Shorted wire check (ATPST/ATP-ST line) -1. Jump the SCS line with the HDS, and wait more than 1 minute. -2. Disconnect the following connector. PCM connector E (80P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected PCM connector E (80P): disconnected Test point 1 PCM connector E (80P) No. 67 Test point 2 Body ground Is there continuity? YES Repair a short in the ATPST/ATP-ST wire between the PCM (E67) and the transmission range switch. NO The ATPST/ATP-ST wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

-2. Disconnect the following connector.

PCM connector E (80P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

PCM connector E (80P): disconnected

Test point 1 | PCM connector E (80P) No. 67

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ATPST/ATP-ST wire between the PCM (E67) and the transmission range switch.

NO

The ATPST/ATP-ST wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16E6 goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 7018: DTC P16F3 (K20C1) (17-21)

- Title: DTC P16F3 (K20C1) (17-21)
- Source path: `pages\7682.html`
- Chunk ID: `chunk_27349ebf4ae8`
- Images: `images\GHH405306.png`, `images\GHH405307.jpeg`, `images\GHH405308.png`, `images\GHH405309.jpeg`, `images\GHH405310.png`, `images\GHH405311.jpeg`
- Duplicate sources: `pages\9269.html`, `pages\22148.html`, `pages\14882.html`

### Full Text

````text
# DTC P16F3 (K20C1) (17-21)

DTC P16F3 : Starter Cut Relay 1 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Try to start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Try to start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F3 Starter Cut Relay 1 Control Circuit Low Voltage Is DTC P16F3 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

Is DTC P16F3 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector No. 2 (58P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 PCM connector No. 2 (58P) No. 49 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board. NO The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector No. 2 (58P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 49

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board.

NO

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 49 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.
````

## Chunk 7019: DTC P16F3 (K20C1) (17-21)

- Title: DTC P16F3 (K20C1) (17-21)
- Source path: `pages\7682.html`
- Chunk ID: `chunk_a71619260f65`
- Images: `images\GHH405306.png`, `images\GHH405307.jpeg`, `images\GHH405308.png`, `images\GHH405309.jpeg`, `images\GHH405310.png`, `images\GHH405311.jpeg`
- Duplicate sources: `pages\9269.html`, `pages\22148.html`, `pages\14882.html`

### Full Text

````text
urn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 49 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 49

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 6. NO Repair an open in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 6.

NO

Repair an open in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the No. B21 (10 A) fuse circuit, and repair it if needed. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the No. B21 (10 A) fuse circuit, and repair it if needed. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Relay circuit board connector B (6P) Under-dash fuse/relay box connector C (27P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) (female terminals) No. 6: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) (female terminals) No. 6:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3.
````

## Chunk 7020: DTC P16F3 (K20C1) (17-21)

- Title: DTC P16F3 (K20C1) (17-21)
- Source path: `pages\7682.html`
- Chunk ID: `chunk_daa8ad5c8241`
- Images: `images\GHH405306.png`, `images\GHH405307.jpeg`, `images\GHH405308.png`, `images\GHH405309.jpeg`, `images\GHH405310.png`, `images\GHH405311.jpeg`
- Duplicate sources: `pages\7685.html`, `pages\9269.html`, `pages\9272.html`, `pages\22148.html`, `pages\22151.html`, `pages\14882.html`, `pages\14883.html`

### Full Text

````text
rcuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) (female terminals) No. 6:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector A (8P): disconnected

Relay circuit board connector B (6P): disconnected

Under-dash fuse/relay box connector C (27P): disconnected

Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground

Test point 1 | Relay circuit board connector B (6P) (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Replace the under-dash fuse/relay box .

NO

Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.
````

## Chunk 7021: DTC P16F3 (K20C2)

- Title: DTC P16F3 (K20C2)
- Source path: `pages\7683.html`
- Chunk ID: `chunk_545db262ea73`
- Images: `images\GHH405312.jpeg`, `images\GHH405313.jpeg`, `images\GHH405314.jpeg`
- Duplicate sources: `pages\9270.html`, `pages\22149.html`, `pages\15152.html`

### Full Text

````text
# DTC P16F3 (K20C2)

DTC P16F3 : Starter Cut Relay 1 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Try to start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Try to start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F3 Starter Cut Relay 1 Control Circuit Low Voltage Is DTC P16F3 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

Is DTC P16F3 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board. NO The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

NO

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4.
````

## Chunk 7022: DTC P16F3 (K20C2)

- Title: DTC P16F3 (K20C2)
- Source path: `pages\7683.html`
- Chunk ID: `chunk_b371772d8e0c`
- Images: `images\GHH405312.jpeg`, `images\GHH405313.jpeg`, `images\GHH405314.jpeg`
- Duplicate sources: `pages\9270.html`, `pages\22149.html`, `pages\15152.html`

### Full Text

````text
the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) No. 5 Test point 2 PCM connector A (50P) No. 15 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ST CUT RLY1 CL- wire is OK. Go to step 6. NO Repair an open in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) No. 5

Test point 2 | PCM connector A (50P) No. 15

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ST CUT RLY1 CL- wire is OK. Go to step 6.

NO

Repair an open in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Relay circuit board connector B (6P) Under-dash fuse/relay box connector C (27P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3.
````

## Chunk 7023: DTC P16F3 (K20C2)

- Title: DTC P16F3 (K20C2)
- Source path: `pages\7683.html`
- Chunk ID: `chunk_26abd96c75bd`
- Images: `images\GHH405312.jpeg`, `images\GHH405313.jpeg`, `images\GHH405314.jpeg`
- Duplicate sources: `pages\7686.html`, `pages\9270.html`, `pages\9273.html`, `pages\22149.html`, `pages\22152.html`, `pages\15152.html`, `pages\15154.html`

### Full Text

````text
nnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Relay circuit board connector B (6P): disconnected

Under-dash fuse/relay box connector C (27P): disconnected

Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground

Test point 1 | Relay circuit board connector B (6P) No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The IG1 ACG wire is OK. Replace the under-dash fuse/relay box .

NO

Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.
````

## Chunk 7024: DTC P16F3 (L15B7/L15BA/L15BY)

- Title: DTC P16F3 (L15B7/L15BA/L15BY)
- Source path: `pages\7684.html`
- Chunk ID: `chunk_643755387e20`
- Images: `images\GHH405315.jpeg`, `images\GHH405316.jpeg`, `images\GHH405317.jpeg`
- Duplicate sources: `pages\9271.html`, `pages\22150.html`, `pages\15153.html`

### Full Text

````text
# DTC P16F3 (L15B7/L15BA/L15BY)

DTC P16F3 : Starter Cut Relay 1 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F3 Starter Cut Relay 1 Control Circuit Low Voltage DTC (PGM-FI) Is DTC P16F3 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F3 Starter Cut Relay 1 Control Circuit Low Voltage

DTC (PGM-FI)

Is DTC P16F3 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board connector A (8P): disconnected PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board. NO The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector A (8P): disconnected

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

NO

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5.
````

## Chunk 7025: DTC P16F3 (L15B7/L15BA/L15BY)

- Title: DTC P16F3 (L15B7/L15BA/L15BY)
- Source path: `pages\7684.html`
- Chunk ID: `chunk_ebacbe5309a4`
- Images: `images\GHH405315.jpeg`, `images\GHH405316.jpeg`, `images\GHH405317.jpeg`
- Duplicate sources: `pages\9271.html`, `pages\22150.html`, `pages\15153.html`

### Full Text

````text
SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F3 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY1 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) No. 5 Test point 2 PCM connector A (50P) No. 15 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ST CUT RLY1 CL- wire is OK. Go to step 6. NO Repair an open in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) No. 5

Test point 2 | PCM connector A (50P) No. 15

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ST CUT RLY1 CL- wire is OK. Go to step 6.

NO

Repair an open in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the IG1 ACG wire between the B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the IG1 ACG wire between the B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Relay circuit board connector B (6P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P)

Relay circuit board connector B (6P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.
````

## Chunk 7026: DTC P16F3 (L15B7/L15BA/L15BY)

- Title: DTC P16F3 (L15B7/L15BA/L15BY)
- Source path: `pages\7684.html`
- Chunk ID: `chunk_1c5bca1f08b0`
- Images: `images\GHH405315.jpeg`, `images\GHH405316.jpeg`, `images\GHH405317.jpeg`
- Duplicate sources: `pages\7687.html`, `pages\9271.html`, `pages\9274.html`, `pages\22150.html`, `pages\22153.html`, `pages\15153.html`, `pages\15155.html`

### Full Text

````text
nnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P)

Relay circuit board connector B (6P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Relay circuit board connector B (6P): disconnected

Under-dash fuse/relay box connector C (27P): disconnected

Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground

Test point 1 | Relay circuit board connector B (6P) No. 4

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The IG1 ACG wire is OK. Replace the under-dash fuse/relay box .

NO

Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.
````

## Chunk 7027: DTC P16F4 (K20C1) (17-21)

- Title: DTC P16F4 (K20C1) (17-21)
- Source path: `pages\7685.html`
- Chunk ID: `chunk_ec0e916d0ed3`
- Images: `images\GHH405318.png`, `images\GHH405319.jpeg`, `images\GHH405320.png`, `images\GHH405321.jpeg`, `images\GHH405322.png`, `images\GHH405323.jpeg`
- Duplicate sources: `pages\9272.html`, `pages\22151.html`, `pages\14883.html`

### Full Text

````text
# DTC P16F4 (K20C1) (17-21)

DTC P16F4 : Starter Cut Relay 2 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Try to start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Try to start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F4 Starter Cut Relay 2 Control Circuit Low Voltage Is DTC P16F4 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

Is DTC P16F4 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector No. 2 (58P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 PCM connector No. 2 (58P) No. 38 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY2 CL- wire between PCM connector No. 2 terminal No. 38 and the relay circuit board. NO The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector No. 2 (58P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 38

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY2 CL- wire between PCM connector No. 2 terminal No. 38 and the relay circuit board.

NO

The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 38 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.
````

## Chunk 7028: DTC P16F4 (K20C1) (17-21)

- Title: DTC P16F4 (K20C1) (17-21)
- Source path: `pages\7685.html`
- Chunk ID: `chunk_0fc4c3b5b52c`
- Images: `images\GHH405318.png`, `images\GHH405319.jpeg`, `images\GHH405320.png`, `images\GHH405321.jpeg`, `images\GHH405322.png`, `images\GHH405323.jpeg`
- Duplicate sources: `pages\9272.html`, `pages\22151.html`, `pages\14883.html`

### Full Text

````text
urn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector No. 2 (58P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 38 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector No. 2 (58P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 38

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Go to step 6. NO Repair an open in the ST CUT RLY2 CL- wire Between PCM connector No. 2 terminal No. 38 and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector No. 2 (58P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) (female terminals) No. 4:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Go to step 6.

NO

Repair an open in the ST CUT RLY2 CL- wire Between PCM connector No. 2 terminal No. 38 and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the No. B21 (10 A) fuse circuit, and repair it if needed. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the No. B21 (10 A) fuse circuit, and repair it if needed. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Relay circuit board connector B (6P) Under-dash fuse/relay box connector C (27P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) (female terminals) No. 6: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector No. 2 (58P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) (female terminals) No. 4: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the relay circuit board and the under-dash fuse/relay box.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) (female terminals) No. 6:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3.
````

## Chunk 7029: DTC P16F4 (K20C2)

- Title: DTC P16F4 (K20C2)
- Source path: `pages\7686.html`
- Chunk ID: `chunk_53c4148a5d6e`
- Images: `images\GHH405324.jpeg`, `images\GHH405325.jpeg`, `images\GHH405326.jpeg`
- Duplicate sources: `pages\9273.html`, `pages\22152.html`, `pages\15154.html`

### Full Text

````text
# DTC P16F4 (K20C2)

DTC P16F4 : Starter Cut Relay 2 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Try to start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Try to start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F4 Starter Cut Relay 2 Control Circuit Low Voltage Is DTC P16F4 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

Is DTC P16F4 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 2 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board. NO The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | PCM connector A (50P) No. 23

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

NO

The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4.
````

## Chunk 7030: DTC P16F4 (K20C2)

- Title: DTC P16F4 (K20C2)
- Source path: `pages\7686.html`
- Chunk ID: `chunk_35debaa6648b`
- Images: `images\GHH405324.jpeg`, `images\GHH405325.jpeg`, `images\GHH405326.jpeg`
- Duplicate sources: `pages\9273.html`, `pages\22152.html`, `pages\15154.html`

### Full Text

````text
the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) No. 4 Test point 2 PCM connector A (50P) No. 23 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ST CUT RLY2 CL- wire is OK. Go to step 6. NO Repair an open in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) No. 4

Test point 2 | PCM connector A (50P) No. 23

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ST CUT RLY2 CL- wire is OK. Go to step 6.

NO

Repair an open in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Relay circuit board connector B (6P) Under-dash fuse/relay box connector C (27P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Relay circuit board connector B (6P)

Under-dash fuse/relay box connector C (27P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3.
````

## Chunk 7031: DTC P16F4 (L15B7/L15BA/L15BY)

- Title: DTC P16F4 (L15B7/L15BA/L15BY)
- Source path: `pages\7687.html`
- Chunk ID: `chunk_8ca2f6fc2882`
- Images: `images\GHH405327.jpeg`, `images\GHH405328.jpeg`, `images\GHH405329.jpeg`
- Duplicate sources: `pages\9274.html`, `pages\22153.html`, `pages\15155.html`

### Full Text

````text
# DTC P16F4 (L15B7/L15BA/L15BY)

DTC P16F4 : Starter Cut Relay 2 Control Circuit Low Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

DTC (PGM-FI)

- Engine starting check -1. Start the engine. Does the engine start? YES Go to step 2. NO Go to step 4.

-1. Start the engine.

Does the engine start?

YES

Go to step 2.

NO

Go to step 4.

- Problem verification -1. Turn the vehicle to the OFF (LOCK) mode. -2. Turn the vehicle to the ON mode. -3. Clear the DTC with the HDS. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F4 Starter Cut Relay 2 Control Circuit Low Voltage Is DTC P16F4 indicated? YES The failure is duplicated. Go to step 3. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Turn the vehicle to the ON mode.

-3. Clear the DTC with the HDS.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F4 Starter Cut Relay 2 Control Circuit Low Voltage

Is DTC P16F4 indicated?

YES

The failure is duplicated. Go to step 3.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Shorted wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connectors. PCM connector A (50P) Relay circuit board connector A (8P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Relay circuit board connector A (8P): disconnected PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there continuity? YES Repair a short in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board. NO The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connectors.

PCM connector A (50P)

Relay circuit board connector A (8P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Relay circuit board connector A (8P): disconnected

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 23

Test point 2 | Body ground

Is there continuity?

YES

Repair a short in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

NO

The ST CUT RLY2 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

- Determine possible failure area (PCM, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5.
````

## Chunk 7032: DTC P16F4 (L15B7/L15BA/L15BY)

- Title: DTC P16F4 (L15B7/L15BA/L15BY)
- Source path: `pages\7687.html`
- Chunk ID: `chunk_b9eb282c45fd`
- Images: `images\GHH405327.jpeg`, `images\GHH405328.jpeg`, `images\GHH405329.jpeg`
- Duplicate sources: `pages\9274.html`, `pages\22153.html`, `pages\15155.html`

### Full Text

````text
SCS short -3. Disconnect the following connector. PCM connector A (50P) -4. Turn the vehicle to the ON mode. -5. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 23 Test point 2 Body ground Is there battery voltage? YES Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM . NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-3. Disconnect the following connector.

PCM connector A (50P)

-4. Turn the vehicle to the ON mode.

-5. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 23

Test point 2 | Body ground

Is there battery voltage?

YES

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F4 goes away and the PCM was substituted, replace the original PCM .

NO

Go to step 5.

- Open wire check (ST CUT RLY2 CL- line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Relay circuit board connector A (8P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Test point 1 Relay circuit board connector A (8P) No. 4 Test point 2 PCM connector A (50P) No. 23 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The ST CUT RLY2 CL- wire is OK. Go to step 6. NO Repair an open in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Relay circuit board connector A (8P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

PCM connector A (50P): disconnected

Relay circuit board connector A (8P): disconnected

Test point 1 | Relay circuit board connector A (8P) No. 4

Test point 2 | PCM connector A (50P) No. 23

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The ST CUT RLY2 CL- wire is OK. Go to step 6.

NO

Repair an open in the ST CUT RLY2 CL- wire between the PCM (A23) and the relay circuit board.

- Fuse check -1. Check the following fuse. Fuse No. B21 (10 A) Location Under-dash fuse/relay box Is the fuse OK? YES Go to step 7. NO Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

-1. Check the following fuse.

Fuse | No. B21 (10 A)

Location | Under-dash fuse/relay box

Is the fuse OK?

YES

Go to step 7.

NO

Check for a short in the IG1 ACG wire between the No. B21 (10 A) fuse and the relay circuit board, and repair it as needed. Also replace the No. B21 (10 A) fuse.

- Open wire check (IG1 ACG line) -1. Disconnect the following connectors. Under-dash fuse/relay box connector C (27P) Relay circuit board connector B (6P) -2. Connect terminals A and B with a jumper wire. Terminal A Under-dash fuse/relay box connector C (27P) No. 6 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode PCM connector A (50P): disconnected Relay circuit board connector A (8P): disconnected Relay circuit board connector B (6P): disconnected Under-dash fuse/relay box connector C (27P): disconnected Under-dash fuse/relay box connector C (27P) No. 6: jumped to body ground Test point 1 Relay circuit board connector B (6P) No. 4 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The IG1 ACG wire is OK. Replace the under-dash fuse/relay box . NO Repair an open in the IG1 ACG wire between the under-dash fuse/relay box and the relay circuit board.

-1. Disconnect the following connectors.

Under-dash fuse/relay box connector C (27P)

Relay circuit board connector B (6P)

-2. Connect terminals A and B with a jumper wire.

Terminal A | Under-dash fuse/relay box connector C (27P) No. 6

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-3. Check for continuity between test points 1 and 2.
````

## Chunk 7033: DTC P16F5 (K20C1) (17-21)

- Title: DTC P16F5 (K20C1) (17-21)
- Source path: `pages\7688.html`
- Chunk ID: `chunk_be1309067313`
- Images: none
- Duplicate sources: `pages\9275.html`, `pages\22154.html`, `pages\14884.html`

### Full Text

````text
# DTC P16F5 (K20C1) (17-21)

DTC P16F5 : Starter Cut Relay 1 Control Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F5 Starter Cut Relay 1 Control Circuit High Voltage Is DTC P16F5 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

Is DTC P16F5 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST CUT RLY1 CL- line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -2. Disconnect the following connector. PCM connector No. 2 (58P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector No. 2 (58P): disconnected Test point 1 PCM connector No. 2 (58P) No. 49 Test point 2 Body ground Is there 0.1 V or less? YES The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-2. Disconnect the following connector.

PCM connector No. 2 (58P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector No. 2 (58P): disconnected

Test point 1 | PCM connector No. 2 (58P) No. 49

Test point 2 | Body ground

Is there 0.1 V or less?

YES

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST CUT RLY1 CL- wire between PCM connector No. 2 terminal No. 49 and the relay circuit board.
````

## Chunk 7034: DTC P16F5 (K20C2)

- Title: DTC P16F5 (K20C2)
- Source path: `pages\7689.html`
- Chunk ID: `chunk_f1ebfdae9174`
- Images: none
- Duplicate sources: `pages\9276.html`, `pages\22155.html`, `pages\15156.html`

### Full Text

````text
# DTC P16F5 (K20C2)

DTC P16F5 : Starter Cut Relay 1 Control Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F5 Starter Cut Relay 1 Control Circuit High Voltage Is DTC P16F5 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

Is DTC P16F5 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board (starter cut relay 1 circuit) and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST CUT RLY1 CL- line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -2. Disconnect the following connector. PCM connector A (50P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there 0.1 V or less? YES The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there 0.1 V or less?

YES

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.
````

## Chunk 7035: DTC P16F5 (L15B7)

- Title: DTC P16F5 (L15B7)
- Source path: `pages\7690.html`
- Chunk ID: `chunk_9c5f82c74de5`
- Images: none
- Duplicate sources: `pages\9277.html`, `pages\22156.html`, `pages\15157.html`

### Full Text

````text
# DTC P16F5 (L15B7)

DTC P16F5 : Starter Cut Relay 1 Control Circuit High Voltage

NOTE: Before you troubleshoot, review the general troubleshooting information .

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

DTC (PGM-FI)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC P16F5 Starter Cut Relay 1 Control Circuit High Voltage Is DTC P16F5 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC

P16F5 Starter Cut Relay 1 Control Circuit High Voltage

Is DTC P16F5 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the relay circuit board and the PCM. If the on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the on-board snapshot .

- Relay circuit board check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove and test the relay circuit board . Is the relay circuit board OK? YES Go to step 3. NO Replace the relay circuit board .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove and test the relay circuit board .

Is the relay circuit board OK?

YES

Go to step 3.

NO

Replace the relay circuit board .

- Shorted wire check (ST CUT RLY1 CL- line to power) -1. Jump the SCS line with the HDS, and wait more than 1 minute. SCS short -2. Disconnect the following connector. PCM connector A (50P) -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Relay circuit board: removed PCM connector A (50P): disconnected Test point 1 PCM connector A (50P) No. 15 Test point 2 Body ground Is there 0.1 V or less? YES The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM . NO Repair a short to power in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.

-1. Jump the SCS line with the HDS, and wait more than 1 minute.

SCS short

-2. Disconnect the following connector.

PCM connector A (50P)

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Relay circuit board: removed

PCM connector A (50P): disconnected

Test point 1 | PCM connector A (50P) No. 15

Test point 2 | Body ground

Is there 0.1 V or less?

YES

The ST CUT RLY1 CL- wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If DTC P16F5 goes away and the PCM was substituted, replace the original PCM .

NO

Repair a short to power in the ST CUT RLY1 CL- wire between the PCM (A15) and the relay circuit board.
````

## Sources Used

- `pages\7580.html`
- `pages\7581.html`
- `pages\7582.html`
- `pages\7583.html`
- `pages\7584.html`
- `pages\7585.html`
- `pages\7586.html`
- `pages\7587.html`
- `pages\7588.html`
- `pages\7589.html`
- `pages\7590.html`
- `pages\7591.html`
- `pages\7592.html`
- `pages\7593.html`
- `pages\7594.html`
- `pages\7595.html`
- `pages\7596.html`
- `pages\7597.html`
- `pages\7598.html`
- `pages\7599.html`
- `pages\7600.html`
- `pages\7601.html`
- `pages\7602.html`
- `pages\7603.html`
- `pages\7604.html`
- `pages\7605.html`
- `pages\7606.html`
- `pages\7607.html`
- `pages\7608.html`
- `pages\7609.html`
- `pages\7610.html`
- `pages\7611.html`
- `pages\7612.html`
- `pages\7613.html`
- `pages\7614.html`
- `pages\7615.html`
- `pages\7616.html`
- `pages\7617.html`
- `pages\7618.html`
- `pages\7619.html`
- `pages\7620.html`
- `pages\7621.html`
- `pages\7622.html`
- `pages\7623.html`
- `pages\7624.html`
- `pages\7625.html`
- `pages\7626.html`
- `pages\7627.html`
- `pages\7628.html`
- `pages\7629.html`
- `pages\7630.html`
- `pages\7631.html`
- `pages\7632.html`
- `pages\7633.html`
- `pages\7634.html`
- `pages\7635.html`
- `pages\7636.html`
- `pages\7637.html`
- `pages\7638.html`
- `pages\7639.html`
- `pages\7640.html`
- `pages\7641.html`
- `pages\7642.html`
- `pages\7643.html`
- `pages\7644.html`
- `pages\7645.html`
- `pages\7646.html`
- `pages\7647.html`
- `pages\7648.html`
- `pages\7649.html`
- `pages\7650.html`
- `pages\7651.html`
- `pages\7652.html`
- `pages\7653.html`
- `pages\7654.html`
- `pages\7655.html`
- `pages\7656.html`
- `pages\7657.html`
- `pages\7658.html`
- `pages\7659.html`
- `pages\7660.html`
- `pages\7661.html`
- `pages\7662.html`
- `pages\7663.html`
- `pages\7664.html`
- `pages\7665.html`
- `pages\7666.html`
- `pages\7667.html`
- `pages\7668.html`
- `pages\7669.html`
- `pages\7670.html`
- `pages\7671.html`
- `pages\7672.html`
- `pages\7673.html`
- `pages\7674.html`
- `pages\7675.html`
- `pages\7676.html`
- `pages\7677.html`
- `pages\7678.html`
- `pages\7679.html`
- `pages\7680.html`
- `pages\7681.html`
- `pages\7682.html`
- `pages\7683.html`
- `pages\7684.html`
- `pages\7685.html`
- `pages\7686.html`
- `pages\7687.html`
- `pages\7688.html`
- `pages\7689.html`
- `pages\7690.html`
