# Deep Research Manual Packet 0039

## Suggested Deep Research Prompt

> You are analyzing a 2016 Honda Civic LX 4D Sedan CVT service manual packet. Use only the manual excerpts in this packet as evidence. When answering, cite the relevant source_path and chunk_id. If this packet does not contain enough information, say what is missing and ask for another packet or targeted retrieval.

## Packet Metadata

- Vehicle: 2016 Honda Civic LX 4D Sedan CVT
- Packet number: 0039
- Chunk count: 220
- Chunk range: 9814-10033
- Source count: 150
- Target maximum characters: 750000

## Manual Chunks

## Chunk 9814: DTC P06A8 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P06A8 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12416.html`
- Chunk ID: `chunk_bb83a6171ef4`
- Images: none
- Duplicate sources: `pages\15561.html`

### Full Text

````text
# DTC P06A8 (L15B7/L15BA/L15BY (CVT))

DTC P06A8 : Internal VCC Power Malfunction

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P06A8 Internal VCC Power Malfunction

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P06A8 Internal VCC Power Malfunction Is DTC P06A8 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P06A8 Internal VCC Power Malfunction

Is DTC P06A8 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9815: DTC P0705 (K20C2, CVT model)

- Title: DTC P0705 (K20C2, CVT model)
- Source path: `pages\12417.html`
- Chunk ID: `chunk_7b3f3eac02de`
- Images: `images\GHH399984.png`, `images\GHH399985.jpeg`, `images\GHH399986.png`, `images\GHH399987.jpeg`
- Duplicate sources: `pages\15479.html`

### Full Text

````text
# DTC P0705 (K20C2, CVT model)

DTC P0705 : Transmission Range Switch Multiple Shift Position Input

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0705 Transmission Range Switch Multiple Shift Position Input

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Do the transmission range switch signals match? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do the transmission range switch signals match?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Transmission range switch signal check -1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Are any transmission range switch signals ON in all shift lever positions/modes? YES Record the abnormal circuit, then go to step 5. NO Go to step 3.

-1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are any transmission range switch signals ON in all shift lever positions/modes?

YES

Record the abnormal circuit, then go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire.
````

## Chunk 9816: DTC P0705 (K20C2, CVT model)

- Title: DTC P0705 (K20C2, CVT model)
- Source path: `pages\12417.html`
- Chunk ID: `chunk_3ff91ef6682b`
- Images: `images\GHH399984.png`, `images\GHH399985.jpeg`, `images\GHH399986.png`, `images\GHH399987.jpeg`
- Duplicate sources: `pages\15479.html`

### Full Text

````text
F | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are any transmission range switch signals ON in all shift lever positions/modes?

YES

Record the abnormal circuit, then go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire. Signal Transmission range switch 10P connector (female terminals): Terminal number Terminal name A/T P Switch 4 ATP-P A/T R Switch 3 ATP-R A/T N Switch 8 ATP-N A/T D Switch 2 ATP-D A/T S Switch 7 ATP-S A/T L Switch* 1 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Compare the transmission range switch signal inputs with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do multiple transmission range switch signals indicate ON? YES The transmission range switch is OK. Go to step 4 NO Replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire.

Signal | Transmission range switch 10P connector (female terminals):

Terminal number | Terminal name

A/T P Switch | 4 | ATP-P

A/T R Switch | 3 | ATP-R

A/T N Switch | 8 | ATP-N

A/T D Switch | 2 | ATP-D

A/T S Switch | 7 | ATP-S

A/T L Switch* | 1 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The transmission range switch is OK. Go to step 4

NO

Replace the transmission range switch .

- Shift position indicator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the shift position indicator panel . -3. Turn the vehicle to the ON mode. -4. Compare the transmission range switch signal inputs with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do multiple transmission range switch signals indicate ON? YES The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table. ATP-P ATP-R ATP-N ATP-D ATP-S ATP-L* ATP-FWD ATP-RVS TCM No. 48 No. 47 No. 46 No. 37 No. 36 No. 35 No. 44 No. 43 Transmission range switch 4 3 8 2 7 1 6 10 *: Without paddle shifter NO Replace the shift position indicator panel .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43
````

## Chunk 9817: DTC P0705 (K20C2, CVT model)

- Title: DTC P0705 (K20C2, CVT model)
- Source path: `pages\12417.html`
- Chunk ID: `chunk_0a45cf9e5c32`
- Images: `images\GHH399984.png`, `images\GHH399985.jpeg`, `images\GHH399986.png`, `images\GHH399987.jpeg`
- Duplicate sources: `pages\15479.html`

### Full Text

````text
OCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch | 4 | 3 | 8 | 2 | 7 | 1 | 6 | 10

*: Without paddle shifter

NO

Replace the shift position indicator panel .

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Turn the vehicle to the ON mode. -4. Check the transmission range switch signal input that remained ON with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do any transmission range switch signals remain ON? YES The transmission range switch is OK. Go to step 6. NO Replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Turn the vehicle to the ON mode.

-4. Check the transmission range switch signal input that remained ON with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do any transmission range switch signals remain ON?

YES

The transmission range switch is OK. Go to step 6.

NO

Replace the transmission range switch .

- Shift position indicator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the shift position indicator panel . -3. Turn the vehicle to the ON mode. -4. Check the transmission range switch signal input that remained ON with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do any transmission range switch signals remain ON? YES The shift position indicator is OK. Go to step 7. NO Replace the shift position indicator panel .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Check the transmission range switch signal input that remained ON with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do any transmission range switch signals remain ON?

YES

The shift position indicator is OK. Go to step 7.

NO

Replace the shift position indicator panel .

- Shorted wire check (corresponding line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between the connector terminal on the circuit that remained ON in step 5 and ground; refer to the following table. Signal Transmission range switch 10P connector (female terminals): Terminal number Terminal name A/T P Switch 4 ATP-P A/T R Switch 3 ATP-R A/T N Switch 8 ATP-N A/T D Switch 2 ATP-D A/T S Switch 7 ATP-S A/T L Switch* 1 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Does the circuit that indicated ON have continuity to ground? YES Repair a short to ground in the wire between the corresponding transmission range switch connector terminal and the TCM. NO The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2.
````

## Chunk 9818: DTC P0705 (K20C2, CVT model)

- Title: DTC P0705 (K20C2, CVT model)
- Source path: `pages\12417.html`
- Chunk ID: `chunk_0c6f9132970d`
- Images: `images\GHH399984.png`, `images\GHH399985.jpeg`, `images\GHH399986.png`, `images\GHH399987.jpeg`
- Duplicate sources: `pages\15479.html`

### Full Text

````text
n range switch 10P connector (female terminals): Terminal number Terminal name A/T P Switch 4 ATP-P A/T R Switch 3 ATP-R A/T N Switch 8 ATP-N A/T D Switch 2 ATP-D A/T S Switch 7 ATP-S A/T L Switch* 1 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Does the circuit that indicated ON have continuity to ground? YES Repair a short to ground in the wire between the corresponding transmission range switch connector terminal and the TCM. NO The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between the connector terminal on the circuit that remained ON in step 5 and ground; refer to the following table.

Signal | Transmission range switch 10P connector (female terminals):

Terminal number | Terminal name

A/T P Switch | 4 | ATP-P

A/T R Switch | 3 | ATP-R

A/T N Switch | 8 | ATP-N

A/T D Switch | 2 | ATP-D

A/T S Switch | 7 | ATP-S

A/T L Switch* | 1 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Does the circuit that indicated ON have continuity to ground?

YES

Repair a short to ground in the wire between the corresponding transmission range switch connector terminal and the TCM.

NO

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9819: DTC P0705 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0705 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12418.html`
- Chunk ID: `chunk_41fc60b5b850`
- Images: `images\GHH399988.jpeg`, `images\GHH399989.jpeg`
- Duplicate sources: `pages\15562.html`

### Full Text

````text
# DTC P0705 (L15B7/L15BA/L15BY (CVT))

DTC P0705 : Transmission Range Switch Multiple Shift Position Input

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0705 Transmission Range Switch Multiple Shift Position Input

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Do the transmission range switch signals match? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do the transmission range switch signals match?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Transmission range switch signal check -1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Are any transmission range switch signals ON in all shift lever positions/modes? YES Record the abnormal circuit, then go to step 5. NO Go to step 3.

-1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are any transmission range switch signals ON in all shift lever positions/modes?

YES

Record the abnormal circuit, then go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire.
````

## Chunk 9820: DTC P0705 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0705 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12418.html`
- Chunk ID: `chunk_cbc77490f2c5`
- Images: `images\GHH399988.jpeg`, `images\GHH399989.jpeg`
- Duplicate sources: `pages\15562.html`

### Full Text

````text
F | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are any transmission range switch signals ON in all shift lever positions/modes?

YES

Record the abnormal circuit, then go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire. Signal Transmission range switch 10P connector Terminal number Terminal name A/T P Switch 5 ATP-P A/T R Switch 4 ATP-R A/T N Switch 9 ATP-N A/T D Switch 3 ATP-D A/T S Switch 8 ATP-S A/T L Switch* 2 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Compare the transmission range switch signal inputs with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do multiple transmission range switch signals indicate ON? YES The transmission range switch is OK. Go to step 4. NO Replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Connect the transmission range switch connector terminal that incorrectly indicates ON in step 2 to ground with a jumper wire.

Signal | Transmission range switch 10P connector

Terminal number | Terminal name

A/T P Switch | 5 | ATP-P

A/T R Switch | 4 | ATP-R

A/T N Switch | 9 | ATP-N

A/T D Switch | 3 | ATP-D

A/T S Switch | 8 | ATP-S

A/T L Switch* | 2 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The transmission range switch is OK. Go to step 4.

NO

Replace the transmission range switch .

- Shift position indicator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the shift position indicator panel . -3. Turn the vehicle to the ON mode. -4. Compare the transmission range switch signal inputs with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do multiple transmission range switch signals indicate ON? YES The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table. ATP-P ATP-R ATP-N ATP-D ATP-S ATP-L* ATP-FWD ATP-RVS TCM No. 48 No. 47 No. 46 No. 37 No. 36 No. 35 No. 44 No. 43 Transmission range switch 5 4 9 3 8 2 6 10 *: Without paddle shifter NO Replace the shift position indicator panel .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43
````

## Chunk 9821: DTC P0705 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0705 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12418.html`
- Chunk ID: `chunk_eab35cdcdb8f`
- Images: `images\GHH399988.jpeg`, `images\GHH399989.jpeg`
- Duplicate sources: `pages\15562.html`

### Full Text

````text
OCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Compare the transmission range switch signal inputs with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do multiple transmission range switch signals indicate ON?

YES

The shift position indicator is OK. Repair a short in the wires between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch | 5 | 4 | 9 | 3 | 8 | 2 | 6 | 10

*: Without paddle shifter

NO

Replace the shift position indicator panel .

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Turn the vehicle to the ON mode. -4. Check the transmission range switch signal input that remained ON with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do any transmission range switch signals remain ON? YES The transmission range switch is OK. Go to step 6. NO Replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Turn the vehicle to the ON mode.

-4. Check the transmission range switch signal input that remained ON with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do any transmission range switch signals remain ON?

YES

The transmission range switch is OK. Go to step 6.

NO

Replace the transmission range switch .

- Shift position indicator check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the shift position indicator panel . -3. Turn the vehicle to the ON mode. -4. Check the transmission range switch signal input that remained ON with the HDS to the following table. Signal Current conditions Values Unit A/T P Switch A/T R Switch A/T N Switch A/T D Switch A/T S Switch A/T L Switch* Forward Switch Reverse Switch *: Without paddle shifter Do any transmission range switch signals remain ON? YES The shift position indicator is OK. Go to step 7. NO Replace the shift position indicator panel .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the shift position indicator panel .

-3. Turn the vehicle to the ON mode.

-4. Check the transmission range switch signal input that remained ON with the HDS to the following table.

Signal | Current conditions

Values | Unit

A/T P Switch

A/T R Switch

A/T N Switch

A/T D Switch

A/T S Switch

A/T L Switch*

Forward Switch

Reverse Switch

*: Without paddle shifter

Do any transmission range switch signals remain ON?

YES

The shift position indicator is OK. Go to step 7.

NO

Replace the shift position indicator panel .

- Shorted wire check (corresponding line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between the connector terminal on the circuit that remained ON in step 5 and ground; refer to the following table. Signal Transmission range switch 10P connector Terminal number Terminal name A/T P Switch 5 ATP-P A/T R Switch 4 ATP-R A/T N Switch 9 ATP-N A/T D Switch 3 ATP-D A/T S Switch 8 ATP-S A/T L Switch* 2 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Does the circuit that indicated ON have continuity to ground? YES Repair a short to ground in the wire between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. NO The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2.
````

## Chunk 9822: DTC P0705 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0705 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12418.html`
- Chunk ID: `chunk_a88d5868ea28`
- Images: `images\GHH399988.jpeg`, `images\GHH399989.jpeg`
- Duplicate sources: `pages\15562.html`

### Full Text

````text
tch 10P connector Terminal number Terminal name A/T P Switch 5 ATP-P A/T R Switch 4 ATP-R A/T N Switch 9 ATP-N A/T D Switch 3 ATP-D A/T S Switch 8 ATP-S A/T L Switch* 2 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Does the circuit that indicated ON have continuity to ground? YES Repair a short to ground in the wire between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM. NO The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between the connector terminal on the circuit that remained ON in step 5 and ground; refer to the following table.

Signal | Transmission range switch 10P connector

Terminal number | Terminal name

A/T P Switch | 5 | ATP-P

A/T R Switch | 4 | ATP-R

A/T N Switch | 9 | ATP-N

A/T D Switch | 3 | ATP-D

A/T S Switch | 8 | ATP-S

A/T L Switch* | 2 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Does the circuit that indicated ON have continuity to ground?

YES

Repair a short to ground in the wire between the corresponding transmission range switch connector terminal, the shift position indicator, and the TCM.

NO

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9823: DTC P0706 (K20C2 (CVT))

- Title: DTC P0706 (K20C2 (CVT))
- Source path: `pages\12419.html`
- Chunk ID: `chunk_ad432b28e9cb`
- Images: `images\GHH399990.png`, `images\GHH399991.jpeg`, `images\GHH399992.png`, `images\GHH399993.jpeg`, `images\GHH399994.png`, `images\GHH399995.jpeg`
- Duplicate sources: `pages\15480.html`

### Full Text

````text
# DTC P0706 (K20C2 (CVT))

DTC P0706 : Transmission Range Switch Open

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0706 Transmission Range Switch Open

DTC (CVT)

- Problem verification -1. Make sure the shift cable is properly adjusted . -2. Turn the vehicle to the ON mode. -3. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF *: Without paddle shifter Signal Threshold Current conditions P R N D S L* Values Unit A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Are the transmission range switch signals OK? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Make sure the shift cable is properly adjusted .

-2. Turn the vehicle to the ON mode.

-3. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

*: Without paddle shifter

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are the transmission range switch signals OK?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Transmission range switch signal check -1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Do all transmission range switch signals remain OFF? YES Go to step 5. NO Go to step 3.

-1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do all transmission range switch signals remain OFF?

YES

Go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table.
````

## Chunk 9824: DTC P0706 (K20C2 (CVT))

- Title: DTC P0706 (K20C2 (CVT))
- Source path: `pages\12419.html`
- Chunk ID: `chunk_417b6f704b0d`
- Images: `images\GHH399990.png`, `images\GHH399991.jpeg`, `images\GHH399992.png`, `images\GHH399993.jpeg`, `images\GHH399994.png`, `images\GHH399995.jpeg`
- Duplicate sources: `pages\15480.html`

### Full Text

````text
| OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do all transmission range switch signals remain OFF?

YES

Go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table. Signal Transmission range switch 10P connector (female terminals): Terminal number Terminal name A/T P Switch 4 ATP-P A/T R Switch 3 ATP-R A/T N Switch 8 ATP-N A/T D Switch 2 ATP-D *: Without paddle shifter Signal Transmission range switch 10P connector (female terminals): Terminal number Terminal name A/T S Switch 7 ATP-S A/T L Switch* 1 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the transmission range switch signal that did not indicate ON with the HDS. Does the transmission range switch signal indicate ON? YES Replace the transmission range switch . NO The transmission range switch is OK. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table.

Signal | Transmission range switch 10P connector (female terminals):

Terminal number | Terminal name

A/T P Switch | 4 | ATP-P

A/T R Switch | 3 | ATP-R

A/T N Switch | 8 | ATP-N

A/T D Switch | 2 | ATP-D

*: Without paddle shifter

Signal | Transmission range switch 10P connector (female terminals):

Terminal number | Terminal name

A/T S Switch | 7 | ATP-S

A/T L Switch* | 1 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the transmission range switch signal that did not indicate ON with the HDS.

Does the transmission range switch signal indicate ON?

YES

Replace the transmission range switch .

NO

The transmission range switch is OK. Go to step 4.

- Open wire check (corresponding line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between the transmission range switch connector terminal and the TCM terminal of the input which indicated OFF. Refer to the following table. ATP-P ATP-R ATP-N ATP-D ATP-S ATP-L* ATP-FWD ATP-RVS TCM 50P connector No. 48 No. 47 No. 46 No. 37 No. 36 No. 35 No. 44 No. 43 Transmission range switch 10P connector (female terminals): 4 3 8 2 7 1 6 10 *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the wire between the corresponding transmission range switch connector terminal and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between the transmission range switch connector terminal and the TCM terminal of the input which indicated OFF. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM 50P connector | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch 10P connector (female terminals): | 4 | 3 | 8 | 2 | 7 | 1 | 6 | 10

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO
````

## Chunk 9825: DTC P0706 (K20C2 (CVT))

- Title: DTC P0706 (K20C2 (CVT))
- Source path: `pages\12419.html`
- Chunk ID: `chunk_63b4de9ec617`
- Images: `images\GHH399990.png`, `images\GHH399991.jpeg`, `images\GHH399992.png`, `images\GHH399993.jpeg`, `images\GHH399994.png`, `images\GHH399995.jpeg`
- Duplicate sources: `pages\15480.html`

### Full Text

````text
e following connector.

TCM 50P connector

-3. Check for continuity between the transmission range switch connector terminal and the TCM terminal of the input which indicated OFF. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM 50P connector | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch 10P connector (female terminals): | 4 | 3 | 8 | 2 | 7 | 1 | 6 | 10

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the wire between the corresponding transmission range switch connector terminal and the TCM.

- Open wire check (PG3 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector (female terminals) No. 5: Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PG3 wire is OK, replace the transmission range switch . NO Repair an open in the PG3 wire between the transmission range switch and ground (G201), or repair poor ground (G201).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector (female terminals) No. 5:

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PG3 wire is OK, replace the transmission range switch .

NO

Repair an open in the PG3 wire between the transmission range switch and ground (G201), or repair poor ground (G201).
````

## Chunk 9826: DTC P0706 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0706 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12420.html`
- Chunk ID: `chunk_3d754607f997`
- Images: `images\GHH399996.jpeg`, `images\GHH399997.jpeg`, `images\GHH399998.jpeg`
- Duplicate sources: `pages\15563.html`

### Full Text

````text
# DTC P0706 (L15B7/L15BA/L15BY (CVT))

DTC P0706 : Transmission Range Switch Open

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0706 Transmission Range Switch Open

DTC (CVT)

- Problem verification -1. Make sure the shift cable is properly adjusted . -2. Turn the vehicle to the ON mode. -3. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF *: Without paddle shifter Signal Threshold Current conditions P R N D S L* Values Unit A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Are the transmission range switch signals OK? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Make sure the shift cable is properly adjusted .

-2. Turn the vehicle to the ON mode.

-3. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

*: Without paddle shifter

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Are the transmission range switch signals OK?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Transmission range switch signal check -1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode. Signal Threshold Current conditions P R N D S L* Values Unit A/T P Switch ON OFF OFF OFF OFF OFF A/T R Switch OFF ON OFF OFF OFF OFF A/T N Switch OFF OFF ON OFF OFF OFF A/T D Switch OFF OFF OFF ON OFF OFF A/T S Switch OFF OFF OFF OFF ON OFF A/T L Switch* OFF OFF OFF OFF OFF ON Forward Switch OFF OFF OFF ON ON ON Reverse Switch OFF ON OFF OFF OFF OFF *: Without paddle shifter Do all transmission range switch signals remain OFF? YES Go to step 5. NO Go to step 3.

-1. Compare the transmission range switch signal inputs with the HDS to the following table, in each shift lever position/mode.

Signal | Threshold | Current conditions

P | R | N | D | S | L* | Values | Unit

A/T P Switch | ON | OFF | OFF | OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do all transmission range switch signals remain OFF?

YES

Go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table.
````

## Chunk 9827: DTC P0706 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0706 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12420.html`
- Chunk ID: `chunk_d222a5c6427d`
- Images: `images\GHH399996.jpeg`, `images\GHH399997.jpeg`, `images\GHH399998.jpeg`
- Duplicate sources: `pages\15563.html`

### Full Text

````text
| OFF | OFF | OFF

A/T R Switch | OFF | ON | OFF | OFF | OFF | OFF

A/T N Switch | OFF | OFF | ON | OFF | OFF | OFF

A/T D Switch | OFF | OFF | OFF | ON | OFF | OFF

A/T S Switch | OFF | OFF | OFF | OFF | ON | OFF

A/T L Switch* | OFF | OFF | OFF | OFF | OFF | ON

Forward Switch | OFF | OFF | OFF | ON | ON | ON

Reverse Switch | OFF | ON | OFF | OFF | OFF | OFF

*: Without paddle shifter

Do all transmission range switch signals remain OFF?

YES

Go to step 5.

NO

Go to step 3.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table. Signal Transmission range switch 10P connector Terminal number Terminal name A/T P Switch 5 ATP-P A/T R Switch 4 ATP-R A/T N Switch 9 ATP-N A/T D Switch 3 ATP-D A/T S Switch 8 ATP-S *: Without paddle shifter Signal Transmission range switch 10P connector Terminal number Terminal name A/T L Switch* 2 ATP-L Forward Switch 6 ATP-FWD Reverse Switch 10 ATP-RVS *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the transmission range switch signal that did not indicate ON with the HDS. Does the transmission range switch signal indicate ON? YES Replace the transmission range switch . NO The transmission range switch is OK. Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Connect the transmission range switch connector terminal that did not indicate ON in step 2 to ground with a jumper wire; refer to the following table.

Signal | Transmission range switch 10P connector

Terminal number | Terminal name

A/T P Switch | 5 | ATP-P

A/T R Switch | 4 | ATP-R

A/T N Switch | 9 | ATP-N

A/T D Switch | 3 | ATP-D

A/T S Switch | 8 | ATP-S

*: Without paddle shifter

Signal | Transmission range switch 10P connector

Terminal number | Terminal name

A/T L Switch* | 2 | ATP-L

Forward Switch | 6 | ATP-FWD

Reverse Switch | 10 | ATP-RVS

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the transmission range switch signal that did not indicate ON with the HDS.

Does the transmission range switch signal indicate ON?

YES

Replace the transmission range switch .

NO

The transmission range switch is OK. Go to step 4.

- Open wire check (corresponding line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between the transmission range switch connector terminal and the TCM terminal of the input which indicated OFF. Refer to the following table. ATP-P ATP-R ATP-N ATP-D ATP-S ATP-L* ATP-FWD ATP-RVS TCM No. 48 No. 47 No. 46 No. 37 No. 36 No. 35 No. 44 No. 43 Transmission range switch 5 4 9 3 8 2 6 10 *: Without paddle shifter Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the wire between the corresponding transmission range switch connector terminal and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between the transmission range switch connector terminal and the TCM terminal of the input which indicated OFF. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch | 5 | 4 | 9 | 3 | 8 | 2 | 6 | 10

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the wire between the corresponding transmission range switch connector terminal and the TCM.

- Open wire check (PG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector.
````

## Chunk 9828: DTC P0706 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0706 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12420.html`
- Chunk ID: `chunk_4105efdb3987`
- Images: `images\GHH399996.jpeg`, `images\GHH399997.jpeg`, `images\GHH399998.jpeg`
- Duplicate sources: `pages\15563.html`

### Full Text

````text
. Refer to the following table.

ATP-P | ATP-R | ATP-N | ATP-D | ATP-S | ATP-L* | ATP-FWD | ATP-RVS

TCM | No. 48 | No. 47 | No. 46 | No. 37 | No. 36 | No. 35 | No. 44 | No. 43

Transmission range switch | 5 | 4 | 9 | 3 | 8 | 2 | 6 | 10

*: Without paddle shifter

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The wires are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the wire between the corresponding transmission range switch connector terminal and the TCM.

- Open wire check (PG1 line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PG1 wire is OK, replace the transmission range switch . NO Repair an open in the PG1 wire between the transmission range switch and ground (G201), or repair poor ground (G201).

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PG1 wire is OK, replace the transmission range switch .

NO

Repair an open in the PG1 wire between the transmission range switch and ground (G201), or repair poor ground (G201).
````

## Chunk 9829: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12421.html`
- Chunk ID: `chunk_21f67521198a`
- Images: `images\GHH399999.png`, `images\GHH400000.jpeg`, `images\GHH400001.png`, `images\GHH400002.png`, `images\GHH400003.jpeg`, `images\GHH400004.png`, `images\GHH400005.jpeg`
- Duplicate sources: `pages\15481.html`

### Full Text

````text
# DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)

DTC P0710 : CVT Fluid Temperature Sensor (Out of Range)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0710 CVT Fluid Temperature Sensor (Out of Range)

DTC (CVT)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for other Pending or Confirmed DTCs indicated along with DTC P0710 with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0712 CVT Fluid Temperature Sensor (Short) P0713 CVT Fluid Temperature Sensor (Open) Are there other DTCs indicated at the same time? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for other Pending or Confirmed DTCs indicated along with DTC P0710 with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0712 CVT Fluid Temperature Sensor (Short)

P0713 CVT Fluid Temperature Sensor (Open)

Are there other DTCs indicated at the same time?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- Problem verification -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) 0.05-0.09 V 4.83-4.92 V Do the current condition(s) match the threshold? YES (0.05-0.09 V) The failure is duplicated. Go to step 3. YES (4.83-4.92 V) The failure is duplicated. Go to step 5. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | 0.05-0.09 | V

4.83-4.92 | V

Do the current condition(s) match the threshold?

YES (0.05-0.09 V)

The failure is duplicated. Go to step 3.

YES (4.83-4.92 V)

The failure is duplicated. Go to step 5.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness 8P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.09 V Do the current condition(s) match the threshold? YES The transmission fluid temperature sensor is OK. Go to step 4. NO Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness 8P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.09 | V

Do the current condition(s) match the threshold?

YES

The transmission fluid temperature sensor is OK. Go to step 4.

NO

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

- Shorted wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between the solenoid wire harness and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3.
````

## Chunk 9830: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12421.html`
- Chunk ID: `chunk_021f9b81e843`
- Images: `images\GHH399999.png`, `images\GHH400000.jpeg`, `images\GHH400001.png`, `images\GHH400002.png`, `images\GHH400003.jpeg`, `images\GHH400004.png`, `images\GHH400005.jpeg`
- Duplicate sources: `pages\15481.html`

### Full Text

````text
hicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between the solenoid wire harness and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 33

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TATF wire between the solenoid wire harness and the TCM.

NO

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Determine possible failure area (TATF line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness 8P connector -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness 8P connector (female terminals) No. 3: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Go to step 6. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness 8P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness 8P connector (female terminals) No. 3:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Go to step 6.

NO

Go to step 7.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness 8P connector (female terminals) No. 2: Terminal B Solenoid wire harness 8P connector (female terminals) No. 3: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Faulty transmission fluid temperature sensor. Replace the solenoid wire harness . NO The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between the solenoid wire harness and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness 8P connector (female terminals) No. 2:

Terminal B | Solenoid wire harness 8P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between the solenoid wire harness and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2.
````

## Chunk 9831: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (K20C2 (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12421.html`
- Chunk ID: `chunk_02e305da524d`
- Images: `images\GHH399999.png`, `images\GHH400000.jpeg`, `images\GHH400001.png`, `images\GHH400002.png`, `images\GHH400003.jpeg`, `images\GHH400004.png`, `images\GHH400005.jpeg`
- Duplicate sources: `pages\15481.html`

### Full Text

````text
o. 2:

Terminal B | Solenoid wire harness 8P connector (female terminals) No. 3:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between the solenoid wire harness and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness 8P connector: disconnected TCM 50P connector: disconnected Test point 1 Solenoid wire harness 8P connector (female terminals) No. 3: Test point 2 TCM 50P connector No. 33 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the TATF wire between the solenoid wire harness and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Solenoid wire harness 8P connector (female terminals) No. 3:

Test point 2 | TCM 50P connector No. 33

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the TATF wire between the solenoid wire harness and the TCM.
````

## Chunk 9832: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12422.html`
- Chunk ID: `chunk_8ade067fbe6a`
- Images: `images\GHH400006.png`, `images\GHH400007.jpeg`, `images\GHH400008.png`, `images\GHH400009.png`, `images\GHH400010.jpeg`, `images\GHH400011.png`, `images\GHH400012.jpeg`
- Duplicate sources: `pages\15564.html`

### Full Text

````text
# DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)

DTC P0710 : CVT Fluid Temperature Sensor (Out of Range)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0710 CVT Fluid Temperature Sensor (Out of Range)

DTC (CVT)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for other Pending or Confirmed DTCs indicated along with DTC P0710 with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0712 CVT Fluid Temperature Sensor (Short) P0713 CVT Fluid Temperature Sensor (Open) Are there other DTCs indicated at the same time? YES Go to the indicated DTC's troubleshooting . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for other Pending or Confirmed DTCs indicated along with DTC P0710 with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0712 CVT Fluid Temperature Sensor (Short)

P0713 CVT Fluid Temperature Sensor (Open)

Are there other DTCs indicated at the same time?

YES

Go to the indicated DTC's troubleshooting .

NO

Go to step 2.

- Problem verification -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) 0.05-0.09 V 4.83-4.92 V Do the current condition(s) match the threshold? YES (0.05-0.09 V) The failure is duplicated. Go to step 3. YES (4.83-4.92 V) The failure is duplicated. Go to step 5. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | 0.05-0.09 | V

4.83-4.92 | V

Do the current condition(s) match the threshold?

YES (0.05-0.09 V)

The failure is duplicated. Go to step 3.

YES (4.83-4.92 V)

The failure is duplicated. Go to step 5.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness A 8P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.09 V Do the current condition(s) match the threshold? YES The transmission fluid temperature sensor is OK. Go to step 4. NO Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness A 8P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.09 | V

Do the current condition(s) match the threshold?

YES

The transmission fluid temperature sensor is OK. Go to step 4.

NO

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

- Shorted wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness A 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between solenoid wire harness A and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector
````

## Chunk 9833: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12422.html`
- Chunk ID: `chunk_5bec850e0acb`
- Images: `images\GHH400006.png`, `images\GHH400007.jpeg`, `images\GHH400008.png`, `images\GHH400009.png`, `images\GHH400010.jpeg`, `images\GHH400011.png`, `images\GHH400012.jpeg`
- Duplicate sources: `pages\15564.html`

### Full Text

````text
e vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness A 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between solenoid wire harness A and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness A 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 33

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TATF wire between solenoid wire harness A and the TCM.

NO

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Determine possible failure area (TATF line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness A 8P connector -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness A 8P connector (female terminals) No. 7: Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Go to step 6. NO Go to step 7.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness A 8P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness A 8P connector (female terminals) No. 7:

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Go to step 6.

NO

Go to step 7.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness A 8P connector (female terminals) No. 6: Terminal B Solenoid wire harness A 8P connector (female terminals) No. 7: Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Faulty transmission fluid temperature sensor. Replace solenoid wire harness A . NO The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness A 8P connector (female terminals) No. 6:

Terminal B | Solenoid wire harness A 8P connector (female terminals) No. 7:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2.
````

## Chunk 9834: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)

- Title: DTC P0710 (L15B7/L15BA/L15BY (CVT)) (2018 2019 2020 2021)
- Source path: `pages\12422.html`
- Chunk ID: `chunk_4ead87dc0cf8`
- Images: `images\GHH400006.png`, `images\GHH400007.jpeg`, `images\GHH400008.png`, `images\GHH400009.png`, `images\GHH400010.jpeg`, `images\GHH400011.png`, `images\GHH400012.jpeg`
- Duplicate sources: `pages\15564.html`

### Full Text

````text
No. 6:

Terminal B | Solenoid wire harness A 8P connector (female terminals) No. 7:

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness A 8P connector: disconnected TCM 50P connector: disconnected Test point 1 Solenoid wire harness A 8P connector (female terminals) No. 7: Test point 2 TCM 50P connector No. 33 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the TATF wire between solenoid wire harness A and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness A 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Solenoid wire harness A 8P connector (female terminals) No. 7:

Test point 2 | TCM 50P connector No. 33

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the TATF wire between solenoid wire harness A and the TCM.
````

## Chunk 9835: DTC P0711 (K20C2 (CVT))

- Title: DTC P0711 (K20C2 (CVT))
- Source path: `pages\12423.html`
- Chunk ID: `chunk_d6ac930a2665`
- Images: none
- Duplicate sources: `pages\15482.html`

### Full Text

````text
# DTC P0711 (K20C2 (CVT))

DTC P0711 : CVT Fluid Temperature Sensor (Range/Performance)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0711 CVT Fluid Temperature Sensor (Range/Performance)

DTC (CVT)

- Current transmission fluid temperature check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 14 or less deg.F -10 or less deg.C Do the current condition(s) match the threshold? YES Go to step 2. NO Go to step 3.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 14 or less | deg.F

-10 or less | deg.C

Do the current condition(s) match the threshold?

YES

Go to step 2.

NO

Go to step 3.

- Transmission fluid temperature sensor check (after warm up) -1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 14 or less deg.F -10 or less deg.C Do the current condition(s) match the threshold? 14 deg.F (-10 deg.C) or below Faulty transmission fluid temperature sensor. Replace the solenoid wire harness . Abnormal temperature rise If there is an abnormal temperature rise in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . 14 deg.F (-10 deg.C) or higher The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 14 or less | deg.F

-10 or less | deg.C

Do the current condition(s) match the threshold?

14 deg.F (-10 deg.C) or below

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

Abnormal temperature rise

If there is an abnormal temperature rise in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

14 deg.F (-10 deg.C) or higher

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Problem verification -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck.
````

## Chunk 9836: DTC P0711 (K20C2 (CVT))

- Title: DTC P0711 (K20C2 (CVT))
- Source path: `pages\12423.html`
- Chunk ID: `chunk_6953bf8dfa39`
- Images: none
- Duplicate sources: `pages\15482.html`

### Full Text

````text
perature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Transmission fluid temperature sensor check (after cool down) -1. Let the engine cool until the Engine Coolant Temperature reads 122 deg.F (50 deg.C) or below with the HDS. Signal Current conditions Values Unit Engine Coolant Temperature -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? 230 deg.F (110 deg.C) or higher Faulty transmission fluid temperature sensor. Replace the solenoid wire harness . Abnormal temperature decrease If there is an abnormal temperature decrease in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . 230 deg.F (110 deg.C) or below The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Let the engine cool until the Engine Coolant Temperature reads 122 deg.F (50 deg.C) or below with the HDS.

Signal | Current conditions

Values | Unit

Engine Coolant Temperature

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

230 deg.F (110 deg.C) or higher

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

Abnormal temperature decrease

If there is an abnormal temperature decrease in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

230 deg.F (110 deg.C) or below

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9837: DTC P0711 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0711 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12424.html`
- Chunk ID: `chunk_369e387a9059`
- Images: none
- Duplicate sources: `pages\15565.html`

### Full Text

````text
# DTC P0711 (L15B7/L15BA/L15BY (CVT))

DTC P0711 : CVT Fluid Temperature Sensor (Range/Performance)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0711 CVT Fluid Temperature Sensor (Range/Performance)

DTC (CVT)

- Current transmission fluid temperature check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 14 or less deg.F -10 or less deg.C Do the current condition(s) match the threshold? YES Go to step 2. NO Go to step 3.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 14 or less | deg.F

-10 or less | deg.C

Do the current condition(s) match the threshold?

YES

Go to step 2.

NO

Go to step 3.

- Transmission fluid temperature sensor check (after warm up) -1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 14 or less deg.F -10 or less deg.C Do the current condition(s) match the threshold? 14 deg.F (-10 deg.C) or below Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A . Abnormal temperature rise If there is an abnormal temperature rise in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . 14 deg.F (-10 deg.C) or higher The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 14 or less | deg.F

-10 or less | deg.C

Do the current condition(s) match the threshold?

14 deg.F (-10 deg.C) or below

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A .

Abnormal temperature rise

If there is an abnormal temperature rise in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

14 deg.F (-10 deg.C) or higher

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Problem verification -1. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck.
````

## Chunk 9838: DTC P0711 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0711 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12424.html`
- Chunk ID: `chunk_42ddec7fa54f`
- Images: none
- Duplicate sources: `pages\15565.html`

### Full Text

````text
perature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 4. NO Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 4.

NO

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Transmission fluid temperature sensor check (after cool down) -1. Let the engine cool until the Engine Coolant Temperature reads 122 deg.F (50 deg.C) or below with the HDS. Signal Current conditions Values Unit Engine Coolant Temperature -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temperature 230 or more deg.F 110 or more deg.C Do the current condition(s) match the threshold? 230 deg.F (110 deg.C) or higher Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A . Abnormal temperature decrease If there is an abnormal temperature decrease in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . 230 deg.F (110 deg.C) or below The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Let the engine cool until the Engine Coolant Temperature reads 122 deg.F (50 deg.C) or below with the HDS.

Signal | Current conditions

Values | Unit

Engine Coolant Temperature

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temperature | 230 or more | deg.F

110 or more | deg.C

Do the current condition(s) match the threshold?

230 deg.F (110 deg.C) or higher

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A .

Abnormal temperature decrease

If there is an abnormal temperature decrease in temperature of the transmission fluid temperature sensor, check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

230 deg.F (110 deg.C) or below

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9839: DTC P0712 (K20C2 (CVT))

- Title: DTC P0712 (K20C2 (CVT))
- Source path: `pages\12425.html`
- Chunk ID: `chunk_fab548949161`
- Images: none
- Duplicate sources: `pages\15483.html`

### Full Text

````text
# DTC P0712 (K20C2 (CVT))

DTC P0712 : CVT Fluid Temperature Sensor (Short)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0712 CVT Fluid Temperature Sensor (Short)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness 8P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES The transmission fluid temperature sensor is OK. Go to step 3. NO Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness 8P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

The transmission fluid temperature sensor is OK. Go to step 3.

NO

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

- Shorted wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between solenoid wire harness and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 33

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TATF wire between solenoid wire harness and the TCM.

NO

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9840: DTC P0712 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0712 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12426.html`
- Chunk ID: `chunk_1ea455f0f5af`
- Images: none
- Duplicate sources: `pages\15566.html`

### Full Text

````text
# DTC P0712 (L15B7/L15BA/L15BY (CVT))

DTC P0712 : CVT Fluid Temperature Sensor (Short)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0712 CVT Fluid Temperature Sensor (Short)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness A 8P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES The transmission fluid temperature sensor is OK. Go to step 3. NO Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness A 8P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

The transmission fluid temperature sensor is OK. Go to step 3.

NO

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

- Shorted wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness A 8P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 33 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the TATF wire between solenoid wire harness A and the TCM. NO The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness A 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 33

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the TATF wire between solenoid wire harness A and the TCM.

NO

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9841: DTC P0713 (K20C2 (CVT))

- Title: DTC P0713 (K20C2 (CVT))
- Source path: `pages\12427.html`
- Chunk ID: `chunk_17c012490f15`
- Images: `images\GHH400013.jpeg`, `images\GHH400014.jpeg`, `images\GHH400015.jpeg`
- Duplicate sources: `pages\15484.html`

### Full Text

````text
# DTC P0713 (K20C2 (CVT))

DTC P0713 : CVT Fluid Temperature Sensor (Open)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0713 CVT Fluid Temperature Sensor (Open)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) More than 4.93 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | More than 4.93 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (TATF line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness 8P connector -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness 8P connector No. 3 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness 8P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness 8P connector No. 3

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness 8P connector No. 2 Terminal B Solenoid wire harness 8P connector No. 3 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Faulty transmission fluid temperature sensor. Replace the solenoid wire harness . NO The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness 8P connector No. 2

Terminal B | Solenoid wire harness 8P connector No. 3

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4.
````

## Chunk 9842: DTC P0713 (K20C2 (CVT))

- Title: DTC P0713 (K20C2 (CVT))
- Source path: `pages\12427.html`
- Chunk ID: `chunk_42c7c830b4f5`
- Images: `images\GHH400013.jpeg`, `images\GHH400014.jpeg`, `images\GHH400015.jpeg`
- Duplicate sources: `pages\15484.html`

### Full Text

````text
nd B with a jumper wire.

Terminal A | Solenoid wire harness 8P connector No. 2

Terminal B | Solenoid wire harness 8P connector No. 3

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness 8P connector: disconnected TCM 50P connector: disconnected Test point 1 Solenoid wire harness 8P connector No. 3 Test point 2 TCM 50P connector No. 33 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the TATF wire between solenoid wire harness and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Solenoid wire harness 8P connector No. 3

Test point 2 | TCM 50P connector No. 33

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the TATF wire between solenoid wire harness and the TCM.
````

## Chunk 9843: DTC P0713 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0713 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12428.html`
- Chunk ID: `chunk_c3f129e4b08e`
- Images: `images\GHH400016.jpeg`, `images\GHH400017.jpeg`, `images\GHH400018.jpeg`
- Duplicate sources: `pages\15567.html`

### Full Text

````text
# DTC P0713 (L15B7/L15BA/L15BY (CVT))

DTC P0713 : CVT Fluid Temperature Sensor (Open)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0713 CVT Fluid Temperature Sensor (Open)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) More than 4.93 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | More than 4.93 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (TATF line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Solenoid wire harness A 8P connector -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness A 8P connector No. 7 Terminal B Body ground Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Solenoid wire harness A 8P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness A 8P connector No. 7

Terminal B | Body ground

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Transmission fluid temperature sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Connect terminals A and B with a jumper wire. Terminal A Solenoid wire harness A 8P connector No. 6 Terminal B Solenoid wire harness A 8P connector No. 7 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit CVTF Temp Sensor (V) Less than 0.07 V Do the current condition(s) match the threshold? YES Faulty transmission fluid temperature sensor. Replace solenoid wire harness A . NO The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Connect terminals A and B with a jumper wire.

Terminal A | Solenoid wire harness A 8P connector No. 6

Terminal B | Solenoid wire harness A 8P connector No. 7

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4.
````

## Chunk 9844: DTC P0713 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0713 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12428.html`
- Chunk ID: `chunk_ee1379f3001e`
- Images: `images\GHH400016.jpeg`, `images\GHH400017.jpeg`, `images\GHH400018.jpeg`
- Duplicate sources: `pages\15567.html`

### Full Text

````text
with a jumper wire.

Terminal A | Solenoid wire harness A 8P connector No. 6

Terminal B | Solenoid wire harness A 8P connector No. 7

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

CVTF Temp Sensor (V) | Less than 0.07 | V

Do the current condition(s) match the threshold?

YES

Faulty transmission fluid temperature sensor. Replace solenoid wire harness A .

NO

The transmission fluid temperature sensor is OK. Repair an open in the SG5 wire between solenoid wire harness A and the TCM.

- Open wire check (TATF line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Solenoid wire harness A 8P connector: disconnected TCM 50P connector: disconnected Test point 1 Solenoid wire harness A 8P connector No. 7 Test point 2 TCM 50P connector No. 33 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the TATF wire between solenoid wire harness A and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Solenoid wire harness A 8P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Solenoid wire harness A 8P connector No. 7

Test point 2 | TCM 50P connector No. 33

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The TATF wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the TATF wire between solenoid wire harness A and the TCM.
````

## Chunk 9845: DTC P0714 (K20C2 (CVT))

- Title: DTC P0714 (K20C2 (CVT))
- Source path: `pages\12429.html`
- Chunk ID: `chunk_b375a2d8bfa7`
- Images: none
- Duplicate sources: `pages\15485.html`

### Full Text

````text
# DTC P0714 (K20C2 (CVT))

DTC P0714 : CVT Fluid Temperature Sensor (Intermittent Failure)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0714 CVT Fluid Temperature Sensor (Intermittent Failure)

DTC (CVT)

- Current transmission fluid temperature check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. CVT System Signal Current conditions Values Unit CVTF Temperature PGM-FI System Signal Current conditions Values Unit ECT SENSOR 2 Are the CVTF Temperature and ECT SENSOR 2 equal to the ambient air temperature? YES Go to step 3. NO Record the values of the CVTF Temperature, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

CVT System

Signal | Current conditions

Values | Unit

CVTF Temperature

PGM-FI System

Signal | Current conditions

Values | Unit

ECT SENSOR 2

Are the CVTF Temperature and ECT SENSOR 2 equal to the ambient air temperature?

YES

Go to step 3.

NO

Record the values of the CVTF Temperature, then go to step 2.

- Transmission fluid temperature difference check -1. Turn the vehicle to the OFF (LOCK) mode, and wait for at least 30 minutes. -2. Turn the vehicle to the ON mode. -3. Compare the current CVTF Temperature to the CVTF Temperature recorded in step 1 Signal Current conditions Values Unit CVTF Temperature Did the CVTF Temperature change? YES Leave the engine off for at least 6 hours, then go to step 3. NO Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

-1. Turn the vehicle to the OFF (LOCK) mode, and wait for at least 30 minutes.

-2. Turn the vehicle to the ON mode.

-3. Compare the current CVTF Temperature to the CVTF Temperature recorded in step 1

Signal | Current conditions

Values | Unit

CVTF Temperature

Did the CVTF Temperature change?

YES

Leave the engine off for at least 6 hours, then go to step 3.

NO

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

- Transmission fluid temperature sensor check -1. Compare the values of the CVTF Temperature and ECT SENSOR 2 in the Data List with the HDS. CVT System Signal Current conditions Values Unit CVTF Temperature PGM-FI System Signal Current conditions Values Unit ECT SENSOR 2 Is the value of the CVTF Temperature higher than the value of ECT SENSOR 2 by 58 deg.F (32 deg.C), or is the value of the CVTF Temperature lower than the value of ECT SENSOR 2 by 43 deg.F (24 deg.C)? YES Faulty transmission fluid temperature sensor. Replace the solenoid wire harness . NO The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Compare the values of the CVTF Temperature and ECT SENSOR 2 in the Data List with the HDS.

CVT System

Signal | Current conditions

Values | Unit

CVTF Temperature

PGM-FI System

Signal | Current conditions

Values | Unit

ECT SENSOR 2

Is the value of the CVTF Temperature higher than the value of ECT SENSOR 2 by 58 deg.F (32 deg.C), or is the value of the CVTF Temperature lower than the value of ECT SENSOR 2 by 43 deg.F (24 deg.C)?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness .

NO

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.
````

## Chunk 9846: DTC P0714 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0714 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12430.html`
- Chunk ID: `chunk_12926132d350`
- Images: none
- Duplicate sources: `pages\15568.html`

### Full Text

````text
# DTC P0714 (L15B7/L15BA/L15BY (CVT))

DTC P0714 : CVT Fluid Temperature Sensor (Intermittent Failure)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0714 CVT Fluid Temperature Sensor (Intermittent Failure)

DTC (CVT)

- Current transmission fluid temperature check -1. Turn the vehicle to the ON mode. -2. Check the parameter(s) below with the HDS. CVT System Signal Current conditions Values Unit CVTF Temperature PGM-FI System Signal Current conditions Values Unit ECT SENSOR 2 Are the CVTF Temperature and ECT SENSOR 2 equal to the ambient air temperature? YES Go to step 3. NO Record the values of the CVTF Temperature, then go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check the parameter(s) below with the HDS.

CVT System

Signal | Current conditions

Values | Unit

CVTF Temperature

PGM-FI System

Signal | Current conditions

Values | Unit

ECT SENSOR 2

Are the CVTF Temperature and ECT SENSOR 2 equal to the ambient air temperature?

YES

Go to step 3.

NO

Record the values of the CVTF Temperature, then go to step 2.

- Transmission fluid temperature difference check -1. Turn the vehicle to the OFF (LOCK) mode, and wait for at least 30 minutes. -2. Turn the vehicle to the ON mode. -3. Compare the current CVTF Temperature to the CVTF Temperature recorded in step 1 Signal Current conditions Values Unit CVTF Temperature Did the CVTF Temperature change? YES Leave the engine off for at least 6 hours, then go to step 3. NO Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A .

-1. Turn the vehicle to the OFF (LOCK) mode, and wait for at least 30 minutes.

-2. Turn the vehicle to the ON mode.

-3. Compare the current CVTF Temperature to the CVTF Temperature recorded in step 1

Signal | Current conditions

Values | Unit

CVTF Temperature

Did the CVTF Temperature change?

YES

Leave the engine off for at least 6 hours, then go to step 3.

NO

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A .

- Transmission fluid temperature sensor check -1. Compare the values of the CVTF Temperature and ECT SENSOR 2 in the Data List with the HDS. CVT System Signal Current conditions Values Unit CVTF Temperature PGM-FI System Signal Current conditions Values Unit ECT SENSOR 2 Is the value of the CVTF Temperature higher than the value of ECT SENSOR 2 by 58 deg.F (32 deg.C), or is the value of the CVTF Temperature lower than the value of ECT SENSOR 2 by 43 deg.F (24 deg.C)? YES Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A . NO The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Compare the values of the CVTF Temperature and ECT SENSOR 2 in the Data List with the HDS.

CVT System

Signal | Current conditions

Values | Unit

CVTF Temperature

PGM-FI System

Signal | Current conditions

Values | Unit

ECT SENSOR 2

Is the value of the CVTF Temperature higher than the value of ECT SENSOR 2 by 58 deg.F (32 deg.C), or is the value of the CVTF Temperature lower than the value of ECT SENSOR 2 by 43 deg.F (24 deg.C)?

YES

Faulty transmission fluid temperature sensor. Replace the solenoid wire harness A .

NO

The transmission fluid temperature sensor is OK. Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission fluid temperature sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.
````

## Chunk 9847: DTC P0716 (K20C2, CVT model)

- Title: DTC P0716 (K20C2, CVT model)
- Source path: `pages\12431.html`
- Chunk ID: `chunk_dd5069626d66`
- Images: none
- Duplicate sources: `pages\15486.html`

### Full Text

````text
# DTC P0716 (K20C2, CVT model)

DTC P0716 : Input/Turbine Speed Sensor "A" Circuit Range/Performance

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance Is DTC P0716 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance

Is DTC P0716 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Torque converter turbine speed sensor check -1. Rotate the front wheels with the shift lever in D position/mode, and compare the Torque Converter Turbine Speed and the Input Shaft (Drive Pulley) Speed rpm in the Data List with the HDS. Signal Current conditions Values Unit Torque Converter Turbine Speed Input Shaft (Drive Pulley) Speed rpm Are the speeds about the same? YES The torque converter turbine speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the torque converter turbine speed sensor .

-1. Rotate the front wheels with the shift lever in D position/mode, and compare the Torque Converter Turbine Speed and the Input Shaft (Drive Pulley) Speed rpm in the Data List with the HDS.

Signal | Current conditions

Values | Unit

Torque Converter Turbine Speed

Input Shaft (Drive Pulley) Speed rpm

Are the speeds about the same?

YES

The torque converter turbine speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the torque converter turbine speed sensor .
````

## Chunk 9848: DTC P0716 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0716 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12432.html`
- Chunk ID: `chunk_b476e85a6c55`
- Images: none
- Duplicate sources: `pages\15569.html`

### Full Text

````text
# DTC P0716 (L15B7/L15BA/L15BY (CVT))

DTC P0716 : Input/Turbine Speed Sensor "A" Circuit Range/Performance

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance Is DTC P0716 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0716 Input/Turbine Speed Sensor "A" Circuit Range/Performance

Is DTC P0716 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Torque converter turbine speed sensor check -1. Rotate the front wheels with the shift lever in D position/mode, and compare the Torque Converter Turbine Speed and the Input Shaft (Drive Pulley) Speed rpm in the Data List with the HDS. Signal Current conditions Values Unit Torque Converter Turbine Speed Input Shaft (Drive Pulley) Speed rpm Are the speeds about the same? YES The torque converter turbine speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the torque converter turbine speed sensor .

-1. Rotate the front wheels with the shift lever in D position/mode, and compare the Torque Converter Turbine Speed and the Input Shaft (Drive Pulley) Speed rpm in the Data List with the HDS.

Signal | Current conditions

Values | Unit

Torque Converter Turbine Speed

Input Shaft (Drive Pulley) Speed rpm

Are the speeds about the same?

YES

The torque converter turbine speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the torque converter turbine speed sensor .
````

## Chunk 9849: DTC P0717 (K20C2 (CVT))

- Title: DTC P0717 (K20C2 (CVT))
- Source path: `pages\12433.html`
- Chunk ID: `chunk_c0bbe3d38b79`
- Images: `images\GHH400019.jpeg`, `images\GHH400020.jpeg`, `images\GHH400021.jpeg`, `images\GHH400022.jpeg`, `images\GHH400023.jpeg`
- Duplicate sources: `pages\15487.html`

### Full Text

````text
# DTC P0717 (K20C2 (CVT))

DTC P0717 : Input/Turbine Speed Sensor "A" Circuit No Signal

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0717 Input/Turbine Speed Sensor "A" Circuit No Signal

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0717 Input/Turbine Speed Sensor "A" Circuit No Signal Is DTC P0717 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0717 Input/Turbine Speed Sensor "A" Circuit No Signal

Is DTC P0717 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (NT line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Torque converter turbine speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Go to step 3. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Torque converter turbine speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Go to step 3.

NO

Go to step 5.

- Open wire check (VCC2 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC2 wire is OK. Go to step 4. NO Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC2 wire is OK. Go to step 4.

NO

Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.
````

## Chunk 9850: DTC P0717 (K20C2 (CVT))

- Title: DTC P0717 (K20C2 (CVT))
- Source path: `pages\12433.html`
- Chunk ID: `chunk_bbc138d86a56`
- Images: `images\GHH400019.jpeg`, `images\GHH400020.jpeg`, `images\GHH400021.jpeg`, `images\GHH400022.jpeg`, `images\GHH400023.jpeg`
- Duplicate sources: `pages\12434.html`, `pages\15487.html`, `pages\15570.html`

### Full Text

````text
Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC2 wire is OK. Go to step 4. NO Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC2 wire is OK. Go to step 4.

NO

Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.

- Torque converter turbine speed sensor check -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 1 Test point 2 Torque converter turbine speed sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the torque converter turbine speed sensor . NO The torque converter turbine speed sensor is OK. Repair an open in the SG2 wire between the torque converter turbine speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 1

Test point 2 | Torque converter turbine speed sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the torque converter turbine speed sensor .

NO

The torque converter turbine speed sensor is OK. Repair an open in the SG2 wire between the torque converter turbine speed sensor and the TCM.

- Shorted wire check (NT line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Torque converter turbine speed sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short to ground in the NT wire between the torque converter turbine speed sensor and the TCM. NO The NT wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Torque converter turbine speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short to ground in the NT wire between the torque converter turbine speed sensor and the TCM.

NO

The NT wire is not shorted. Go to step 6.

- Open wire check (NT line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Torque converter turbine speed sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 2 Test point 2 TCM 50P connector No. 49 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the NT wire between the torque converter turbine speed sensor and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Torque converter turbine speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 2

Test point 2 | TCM 50P connector No. 49

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck.
````

## Chunk 9851: DTC P0717 (K20C2 (CVT))

- Title: DTC P0717 (K20C2 (CVT))
- Source path: `pages\12433.html`
- Chunk ID: `chunk_851b78807bcb`
- Images: `images\GHH400019.jpeg`, `images\GHH400020.jpeg`, `images\GHH400021.jpeg`, `images\GHH400022.jpeg`, `images\GHH400023.jpeg`
- Duplicate sources: `pages\12434.html`, `pages\15487.html`, `pages\15570.html`

### Full Text

````text
TCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the NT wire between the torque converter turbine speed sensor and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Torque converter turbine speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 2

Test point 2 | TCM 50P connector No. 49

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NT wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the NT wire between the torque converter turbine speed sensor and the TCM.
````

## Chunk 9852: DTC P0717 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0717 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12434.html`
- Chunk ID: `chunk_2c3505e7d47d`
- Images: `images\GHH400024.jpeg`, `images\GHH400025.jpeg`, `images\GHH400026.jpeg`, `images\GHH400027.jpeg`, `images\GHH400028.jpeg`
- Duplicate sources: `pages\15570.html`

### Full Text

````text
# DTC P0717 (L15B7/L15BA/L15BY (CVT))

DTC P0717 : Input/Turbine Speed Sensor "A" Circuit No Signal

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0717 Input/Turbine Speed Sensor "A" Circuit No Signal

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0717 Input/Turbine Speed Sensor "A" Circuit No Signal Is DTC P0717 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down, and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0717 Input/Turbine Speed Sensor "A" Circuit No Signal

Is DTC P0717 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the torque converter turbine speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (NT line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Torque converter turbine speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Go to step 3. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Torque converter turbine speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Go to step 3.

NO

Go to step 5.

- Open wire check (VCC2 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Torque converter turbine speed sensor 3P connector: disconnected Test point 1 Torque converter turbine speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC2 wire is OK. Go to step 4. NO Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Torque converter turbine speed sensor 3P connector: disconnected

Test point 1 | Torque converter turbine speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC2 wire is OK. Go to step 4.

NO

Repair an open in the VCC2 wire between the torque converter turbine speed sensor and the TCM.
````

## Chunk 9853: DTC P0741 (K20C2 (CVT))

- Title: DTC P0741 (K20C2 (CVT))
- Source path: `pages\12435.html`
- Chunk ID: `chunk_764914c0b43a`
- Images: none
- Duplicate sources: `pages\15488.html`

### Full Text

````text
# DTC P0741 (K20C2 (CVT))

DTC P0741 : Torque Converter Clutch Circuit Performance or Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0741 Torque Converter Clutch Circuit Performance or Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). -4. Test-drive the vehicle at speeds about 37 mph (60 km/h) on a flat road for at least 1 minute. Slow down and stop the wheels. -5. Repeat step 1 -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0741 Torque Converter Clutch Circuit Performance or Stuck OFF Is DTC P0741 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

-4. Test-drive the vehicle at speeds about 37 mph (60 km/h) on a flat road for at least 1 minute. Slow down and stop the wheels.

-5. Repeat step 1

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0741 Torque Converter Clutch Circuit Performance or Stuck OFF

Is DTC P0741 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Shift solenoid valve B check -1. Do the shift solenoid valve B test . Does shift solenoid valve B work properly? YES Shift solenoid valve B is OK. Go to step 3. NO Faulty shift solenoid valve B. Replace the valve body assembly .

-1. Do the shift solenoid valve B test .

Does shift solenoid valve B work properly?

YES

Shift solenoid valve B is OK. Go to step 3.

NO

Faulty shift solenoid valve B. Replace the valve body assembly .

- CVT lock-up clutch control solenoid valve check -1. Do the CVT lock-up clutch control solenoid valve test . Does the CVT lock-up clutch control solenoid valve work properly? YES The CVT lock-up clutch control solenoid valve is OK. Replace the transmission, or the torque converter . NO Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

-1. Do the CVT lock-up clutch control solenoid valve test .

Does the CVT lock-up clutch control solenoid valve work properly?

YES

The CVT lock-up clutch control solenoid valve is OK. Replace the transmission, or the torque converter .

NO

Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .
````

## Chunk 9854: DTC P0741 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0741 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12436.html`
- Chunk ID: `chunk_42b01fce8a05`
- Images: none
- Duplicate sources: `pages\15571.html`

### Full Text

````text
# DTC P0741 (L15B7/L15BA/L15BY (CVT))

DTC P0741 : Torque Converter Clutch Circuit Performance or Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0741 Torque Converter Clutch Circuit Performance or Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). -4. Test-drive the vehicle at speeds about 37 mph (60 km/h) on a flat road for at least 1 minute. Slow down and stop the wheels. -5. Repeat step 1 -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0741 Torque Converter Clutch Circuit Performance or Stuck OFF Is DTC P0741 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

-4. Test-drive the vehicle at speeds about 37 mph (60 km/h) on a flat road for at least 1 minute. Slow down and stop the wheels.

-5. Repeat step 1

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0741 Torque Converter Clutch Circuit Performance or Stuck OFF

Is DTC P0741 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Shift solenoid valve B check -1. Do the shift solenoid valve B test . Does shift solenoid valve B work properly? YES Shift solenoid valve B is OK. Go to step 3. NO Faulty shift solenoid valve B. Replace the valve body assembly .

-1. Do the shift solenoid valve B test .

Does shift solenoid valve B work properly?

YES

Shift solenoid valve B is OK. Go to step 3.

NO

Faulty shift solenoid valve B. Replace the valve body assembly .

- CVT lock-up clutch control solenoid valve check -1. Do the CVT lock-up clutch control solenoid valve test . Does the CVT lock-up clutch control solenoid valve work properly? YES The CVT lock-up clutch control solenoid valve is OK. Replace the transmission, or the torque converter . NO Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

-1. Do the CVT lock-up clutch control solenoid valve test .

Does the CVT lock-up clutch control solenoid valve work properly?

YES

The CVT lock-up clutch control solenoid valve is OK. Replace the transmission, or the torque converter .

NO

Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .
````

## Chunk 9855: DTC P0746 (K20C2, CVT model)

- Title: DTC P0746 (K20C2, CVT model)
- Source path: `pages\12437.html`
- Chunk ID: `chunk_3a0ba9f61986`
- Images: none
- Duplicate sources: `pages\15489.html`

### Full Text

````text
# DTC P0746 (K20C2, CVT model)

DTC P0746 : CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF Is DTC P0746 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

Is DTC P0746 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9856: DTC P0746 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0746 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12438.html`
- Chunk ID: `chunk_6c2798617d62`
- Images: none
- Duplicate sources: `pages\15572.html`

### Full Text

````text
# DTC P0746 (L15B7/L15BA/L15BY (CVT))

DTC P0746 : CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF Is DTC P0746 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0746 CVT Drive Pulley Pressure Control Solenoid Valve Stuck OFF

Is DTC P0746 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9857: DTC P0777 (K20C2, CVT model)

- Title: DTC P0777 (K20C2, CVT model)
- Source path: `pages\12439.html`
- Chunk ID: `chunk_2204f30dde01`
- Images: none
- Duplicate sources: `pages\15490.html`

### Full Text

````text
# DTC P0777 (K20C2, CVT model)

DTC P0777 : CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON Is DTC P0777 indicated? YES The failure is duplicated. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

Is DTC P0777 indicated?

YES

The failure is duplicated. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9858: DTC P0777 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0777 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12440.html`
- Chunk ID: `chunk_d4007005c56e`
- Images: none
- Duplicate sources: `pages\15573.html`

### Full Text

````text
# DTC P0777 (L15B7/L15BA/L15BY (CVT))

DTC P0777 : CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON Is DTC P0777 indicated? YES The failure is duplicated. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0777 CVT Driven Pulley Pressure Control Solenoid Valve Stuck ON

Is DTC P0777 indicated?

YES

The failure is duplicated. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9859: DTC P0780 (K20C2 (CVT))

- Title: DTC P0780 (K20C2 (CVT))
- Source path: `pages\12441.html`
- Chunk ID: `chunk_a55464cb5752`
- Images: none
- Duplicate sources: `pages\15491.html`

### Full Text

````text
# DTC P0780 (K20C2 (CVT))

DTC P0780 : Shift Error

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is stored whenever DTCs P1898 and P1899 are detected.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for other Pending or Confirmed DTCs indicated along with DTC P0780 with the HDS. NOTE: P0780 means there is one or more CVT DTCs regarding the shift control system. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON Are there other DTCs? YES The failure is duplicated. Go to the indicated DTC's troubleshooting. P1898 P1899 NO There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for other Pending or Confirmed DTCs indicated along with DTC P0780 with the HDS.

NOTE: P0780 means there is one or more CVT DTCs regarding the shift control system.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

Are there other DTCs?

- YES The failure is duplicated. Go to the indicated DTC's troubleshooting. P1898 P1899 NO There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

YES

The failure is duplicated. Go to the indicated DTC's troubleshooting.

- P1898

- P1899

NO

There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9860: DTC P0780 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0780 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12442.html`
- Chunk ID: `chunk_76155743c6c4`
- Images: none
- Duplicate sources: `pages\15574.html`

### Full Text

````text
# DTC P0780 (L15B7/L15BA/L15BY (CVT))

DTC P0780 : Shift Error

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is stored whenever DTCs P1898 and P1899 are detected.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for other Pending or Confirmed DTCs indicated along with DTC P0780 with the HDS. NOTE: P0780 means there is one or more CVT DTCs regarding the shift control system. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON Are there other DTCs? YES The failure is duplicated. Go to the indicated DTC's troubleshooting. P1898 P1899 NO There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for other Pending or Confirmed DTCs indicated along with DTC P0780 with the HDS.

NOTE: P0780 means there is one or more CVT DTCs regarding the shift control system.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

Are there other DTCs?

- YES The failure is duplicated. Go to the indicated DTC's troubleshooting. P1898 P1899 NO There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

YES

The failure is duplicated. Go to the indicated DTC's troubleshooting.

- P1898

- P1899

NO

There are no DTCs along with DTC P0780. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .
````

## Chunk 9861: DTC P0792 (K20C2 (CVT))

- Title: DTC P0792 (K20C2 (CVT))
- Source path: `pages\12443.html`
- Chunk ID: `chunk_a0f217ef7c5b`
- Images: none
- Duplicate sources: `pages\15492.html`

### Full Text

````text
# DTC P0792 (K20C2 (CVT))

DTC P0792 : Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance Is DTC P0792 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

Is DTC P0792 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- CVT drive pulley speed sensor check -1. Rotate the front wheels with the shift lever in D position/mode, and compare the Input Shaft (Drive Pulley) Speed rpm and the Torque Converter Turbine Speed in the Data List with the HDS. Signal Current conditions Values Unit Input Shaft (Drive Pulley) Speed rpm Torque Converter Turbine Speed Are the speeds about the same? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Rotate the front wheels with the shift lever in D position/mode, and compare the Input Shaft (Drive Pulley) Speed rpm and the Torque Converter Turbine Speed in the Data List with the HDS.

Signal | Current conditions

Values | Unit

Input Shaft (Drive Pulley) Speed rpm

Torque Converter Turbine Speed

Are the speeds about the same?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9862: DTC P0792 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0792 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12444.html`
- Chunk ID: `chunk_fcffe873660a`
- Images: none
- Duplicate sources: `pages\15575.html`

### Full Text

````text
# DTC P0792 (L15B7/L15BA/L15BY (CVT))

DTC P0792 : Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance Is DTC P0792 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0792 Intermediate Shaft Speed Sensor "A" Circuit Range/Performance

Is DTC P0792 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- CVT drive pulley speed sensor check -1. Rotate the front wheels with the shift lever in D position/mode, and compare the Input Shaft (Drive Pulley) Speed rpm and the Torque Converter Turbine Speed in the Data List with the HDS. Signal Current conditions Values Unit Input Shaft (Drive Pulley) Speed rpm Torque Converter Turbine Speed Are the speeds about the same? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Rotate the front wheels with the shift lever in D position/mode, and compare the Input Shaft (Drive Pulley) Speed rpm and the Torque Converter Turbine Speed in the Data List with the HDS.

Signal | Current conditions

Values | Unit

Input Shaft (Drive Pulley) Speed rpm

Torque Converter Turbine Speed

Are the speeds about the same?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9863: DTC P0793 (K20C2 (CVT))

- Title: DTC P0793 (K20C2 (CVT))
- Source path: `pages\12445.html`
- Chunk ID: `chunk_fe5dec336e80`
- Images: `images\GHH400029.jpeg`, `images\GHH400030.jpeg`, `images\GHH400031.jpeg`, `images\GHH400032.jpeg`, `images\GHH400033.jpeg`
- Duplicate sources: `pages\15493.html`

### Full Text

````text
# DTC P0793 (K20C2 (CVT))

DTC P0793 : Intermediate Shaft Speed Sensor "A" Circuit No Signal

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal Is DTC P0793 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal

Is DTC P0793 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (NDR-PWM line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT drive pulley speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Go to step 3. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT drive pulley speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Go to step 3.

NO

Go to step 5.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC1 wire is OK. Go to step 4. NO Repair an open in the VCC1 wire between the CVT drive pulley speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC1 wire is OK. Go to step 4.

NO
````

## Chunk 9864: DTC P0793 (K20C2 (CVT))

- Title: DTC P0793 (K20C2 (CVT))
- Source path: `pages\12445.html`
- Chunk ID: `chunk_89616e6b5a33`
- Images: `images\GHH400029.jpeg`, `images\GHH400030.jpeg`, `images\GHH400031.jpeg`, `images\GHH400032.jpeg`, `images\GHH400033.jpeg`
- Duplicate sources: `pages\12446.html`, `pages\15493.html`, `pages\15576.html`

### Full Text

````text
3.

NO

Go to step 5.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC1 wire is OK. Go to step 4. NO Repair an open in the VCC1 wire between the CVT drive pulley speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC1 wire is OK. Go to step 4.

NO

Repair an open in the VCC1 wire between the CVT drive pulley speed sensor and the TCM.

- CVT drive pulley speed sensor check -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 2 Test point 2 CVT drive pulley speed sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the CVT drive pulley speed sensor . NO The CVT drive pulley speed sensor is OK. Repair an open in the SG1 wire between the CVT drive pulley speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 2

Test point 2 | CVT drive pulley speed sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the CVT drive pulley speed sensor .

NO

The CVT drive pulley speed sensor is OK. Repair an open in the SG1 wire between the CVT drive pulley speed sensor and the TCM.

- Shorted wire check (NDR-PWM line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley speed sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short to ground in the NDR-PWM wire between the CVT drive pulley speed sensor and the TCM. NO The NDR-PWM wire is not shorted. Go to step 6.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short to ground in the NDR-PWM wire between the CVT drive pulley speed sensor and the TCM.

NO

The NDR-PWM wire is not shorted. Go to step 6.

- Open wire check (NDR-PWM line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley speed sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 1 Test point 2 TCM 50P connector No. 28 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The NDR-PWM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the NDR-PWM wire between the CVT drive pulley speed sensor and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 1

Test point 2 | TCM 50P connector No. 28

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NDR-PWM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO
````

## Chunk 9865: DTC P0793 (K20C2 (CVT))

- Title: DTC P0793 (K20C2 (CVT))
- Source path: `pages\12445.html`
- Chunk ID: `chunk_d4accd49a0f6`
- Images: `images\GHH400029.jpeg`, `images\GHH400030.jpeg`, `images\GHH400031.jpeg`, `images\GHH400032.jpeg`, `images\GHH400033.jpeg`
- Duplicate sources: `pages\12446.html`, `pages\15493.html`, `pages\15576.html`

### Full Text

````text
CM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the NDR-PWM wire between the CVT drive pulley speed sensor and the TCM.

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley speed sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 1

Test point 2 | TCM 50P connector No. 28

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The NDR-PWM wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the NDR-PWM wire between the CVT drive pulley speed sensor and the TCM.
````

## Chunk 9866: DTC P0793 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0793 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12446.html`
- Chunk ID: `chunk_d9788279bbb8`
- Images: `images\GHH400034.jpeg`, `images\GHH400035.jpeg`, `images\GHH400036.jpeg`, `images\GHH400037.jpeg`, `images\GHH400038.jpeg`
- Duplicate sources: `pages\15576.html`

### Full Text

````text
# DTC P0793 (L15B7/L15BA/L15BY (CVT))

DTC P0793 : Intermediate Shaft Speed Sensor "A" Circuit No Signal

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal Is DTC P0793 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Run the vehicle with the shift lever in D position/mode, and keep the vehicle at speeds over 19 mph (30 km/h) for at least 30 seconds. Slow down and stop the wheels.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0793 Intermediate Shaft Speed Sensor "A" Circuit No Signal

Is DTC P0793 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley speed sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (NDR-PWM line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT drive pulley speed sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Go to step 3. NO Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT drive pulley speed sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Go to step 3.

NO

Go to step 5.

- Open wire check (VCC1 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT drive pulley speed sensor 3P connector: disconnected Test point 1 CVT drive pulley speed sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC1 wire is OK. Go to step 4. NO Repair an open in the VCC1 wire between the CVT drive pulley speed sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT drive pulley speed sensor 3P connector: disconnected

Test point 1 | CVT drive pulley speed sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC1 wire is OK. Go to step 4.

NO
````

## Chunk 9867: DTC P0796 (K20C2 (CVT))

- Title: DTC P0796 (K20C2 (CVT))
- Source path: `pages\12447.html`
- Chunk ID: `chunk_8498c57eebda`
- Images: none
- Duplicate sources: `pages\15494.html`

### Full Text

````text
# DTC P0796 (K20C2 (CVT))

DTC P0796 : Pressure Control Solenoid Valve "C" Performance or Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine in P position/mode. Shift the transmission to N position/mode, then to D position/mode while pressing the brake pedal, and wait for at least 30 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF Is DTC P0796 indicated? YES The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine in P position/mode. Shift the transmission to N position/mode, then to D position/mode while pressing the brake pedal, and wait for at least 30 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF

Is DTC P0796 indicated?

YES

The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9868: DTC P0796 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0796 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12448.html`
- Chunk ID: `chunk_2a0f4067c481`
- Images: none
- Duplicate sources: `pages\15577.html`

### Full Text

````text
# DTC P0796 (L15B7/L15BA/L15BY (CVT))

DTC P0796 : Pressure Control Solenoid Valve "C" Performance or Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine in P position/mode. Shift the transmission to N position/mode, then to D position/mode while pressing the brake pedal, and wait for at least 30 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF Is DTC P0796 indicated? YES The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine in P position/mode. Shift the transmission to N position/mode, then to D position/mode while pressing the brake pedal, and wait for at least 30 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0796 Pressure Control Solenoid Valve "C" Performance or Stuck OFF

Is DTC P0796 indicated?

YES

The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9869: DTC P0797 (K20C2 (CVT))

- Title: DTC P0797 (K20C2 (CVT))
- Source path: `pages\12449.html`
- Chunk ID: `chunk_0530e4a76030`
- Images: none
- Duplicate sources: `pages\15495.html`

### Full Text

````text
# DTC P0797 (K20C2 (CVT))

DTC P0797 : Pressure Control Solenoid Valve "C" Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0797 Pressure Control Solenoid Valve "C" Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. With the brake pedal pressed, do the following operational mode of the shift lever five times: -1. Shift the transmission to N position/mode, then to D position/mode, and wait for at least 1 second. -2. Shift the transmission to N position/mode, and wait for at least 2 seconds. -3. Shift the transmission to D position/mode, and wait for at least 1 second. -5. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-4 five times. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0797 Pressure Control Solenoid Valve "C" Stuck ON Is DTC P0797 indicated? YES The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. With the brake pedal pressed, do the following operational mode of the shift lever five times:

-1. Shift the transmission to N position/mode, then to D position/mode, and wait for at least 1 second.

-2. Shift the transmission to N position/mode, and wait for at least 2 seconds.

-3. Shift the transmission to D position/mode, and wait for at least 1 second.

-5. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-4 five times.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0797 Pressure Control Solenoid Valve "C" Stuck ON

Is DTC P0797 indicated?

YES

The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9870: DTC P0797 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0797 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12450.html`
- Chunk ID: `chunk_dbef628b378f`
- Images: none
- Duplicate sources: `pages\15578.html`

### Full Text

````text
# DTC P0797 (L15B7/L15BA/L15BY (CVT))

DTC P0797 : Pressure Control Solenoid Valve "C" Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0797 Pressure Control Solenoid Valve "C" Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. With the brake pedal pressed, do the following operational mode of the shift lever five times: -1. Shift the transmission to N position/mode, then to D position/mode, and wait for at least 1 second. -2. Shift the transmission to N position/mode, and wait for at least 2 seconds. -3. Shift the transmission to D position/mode, and wait for at least 1 second. -5. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-4 five times. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0797 Pressure Control Solenoid Valve "C" Stuck ON Is DTC P0797 indicated? YES The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. With the brake pedal pressed, do the following operational mode of the shift lever five times:

-1. Shift the transmission to N position/mode, then to D position/mode, and wait for at least 1 second.

-2. Shift the transmission to N position/mode, and wait for at least 2 seconds.

-3. Shift the transmission to D position/mode, and wait for at least 1 second.

-5. Turn the vehicle to the OFF (LOCK) mode. Repeat the shift lever operational mode in step 1-4 five times.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0797 Pressure Control Solenoid Valve "C" Stuck ON

Is DTC P0797 indicated?

YES

The failure is duplicated. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9871: DTC P0842 (K20C2 (CVT))

- Title: DTC P0842 (K20C2 (CVT))
- Source path: `pages\12451.html`
- Chunk ID: `chunk_bfbd03c47891`
- Images: `images\GHH400039.jpeg`, `images\GHH400040.jpeg`
- Duplicate sources: `pages\15496.html`

### Full Text

````text
# DTC P0842 (K20C2 (CVT))

DTC P0842 : Transmission Fluid Pressure Sensor/Switch "A" Circuit Low

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0842 Transmission Fluid Pressure Sensor/Switch "A" Circuit Low

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) Less than 0.21 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | Less than 0.21 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (PDN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT driven pulley pressure sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) Less than 0.21 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT driven pulley pressure sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | Less than 0.21 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Shorted wire check (PDN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short to ground in the PDN wire between the CVT driven pulley pressure sensor and the TCM. NO The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short to ground in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

NO

The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Open wire check (VCC4 line) -1. Measure the voltage between test points 1 and 2.
````

## Chunk 9872: DTC P0842 (K20C2 (CVT))

- Title: DTC P0842 (K20C2 (CVT))
- Source path: `pages\12451.html`
- Chunk ID: `chunk_a2c8f3ab0607`
- Images: `images\GHH400039.jpeg`, `images\GHH400040.jpeg`
- Duplicate sources: `pages\12452.html`, `pages\15496.html`, `pages\15519.html`

### Full Text

````text
50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short to ground in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

NO

The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Open wire check (VCC4 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT driven pulley pressure sensor 3P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The VCC4 wire is OK. Replace the CVT driven pulley pressure sensor . NO Repair an open in the VCC4 wire between the CVT driven pulley pressure sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT driven pulley pressure sensor 3P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The VCC4 wire is OK. Replace the CVT driven pulley pressure sensor .

NO

Repair an open in the VCC4 wire between the CVT driven pulley pressure sensor and the TCM.
````

## Chunk 9873: DTC P0842 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0842 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12452.html`
- Chunk ID: `chunk_df51c6f4da6b`
- Images: `images\GHH400041.jpeg`, `images\GHH400042.jpeg`
- Duplicate sources: `pages\15519.html`

### Full Text

````text
# DTC P0842 (L15B7/L15BA/L15BY (CVT))

DTC P0842 : Transmission Fluid Pressure Sensor/Switch "A" Circuit Low

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0842 Transmission Fluid Pressure Sensor/Switch "A" Circuit Low

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) Less than 0.21 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | Less than 0.21 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (PDN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT driven pulley pressure sensor 3P connector -3. Turn the vehicle to the ON mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) Less than 0.21 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT driven pulley pressure sensor 3P connector

-3. Turn the vehicle to the ON mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | Less than 0.21 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Shorted wire check (PDN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 2 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES Repair a short to ground in the PDN wire between the CVT driven pulley pressure sensor and the TCM. NO The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

Repair a short to ground in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

NO

The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

- Open wire check (VCC4 line) -1. Measure the voltage between test points 1 and 2.
````

## Chunk 9874: DTC P0843 (K20C2 (CVT))

- Title: DTC P0843 (K20C2 (CVT))
- Source path: `pages\12453.html`
- Chunk ID: `chunk_0970b2aad2f3`
- Images: `images\GHH400043.jpeg`, `images\GHH400044.jpeg`, `images\GHH400045.jpeg`, `images\GHH400046.jpeg`
- Duplicate sources: `pages\15497.html`

### Full Text

````text
# DTC P0843 (K20C2 (CVT))

DTC P0843 : Transmission Fluid Pressure Sensor/Switch "A" Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0843 Transmission Fluid Pressure Sensor/Switch "A" Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) More than 4.84 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | More than 4.84 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (PDN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT driven pulley pressure sensor 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A CVT driven pulley pressure sensor 3P connector No. 1 Terminal B CVT driven pulley pressure sensor 3P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) More than 4.84 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT driven pulley pressure sensor 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | CVT driven pulley pressure sensor 3P connector No. 1

Terminal B | CVT driven pulley pressure sensor 3P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | More than 4.84 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Open wire check (PDN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 2 Test point 2 TCM 50P connector No. 31 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | TCM 50P connector No. 31

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PDN wire is OK.
````

## Chunk 9875: DTC P0843 (K20C2 (CVT))

- Title: DTC P0843 (K20C2 (CVT))
- Source path: `pages\12453.html`
- Chunk ID: `chunk_0afc6e9a40bc`
- Images: `images\GHH400043.jpeg`, `images\GHH400044.jpeg`, `images\GHH400045.jpeg`, `images\GHH400046.jpeg`
- Duplicate sources: `pages\12454.html`, `pages\15497.html`, `pages\15520.html`

### Full Text

````text
rmation related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | TCM 50P connector No. 31

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

- CVT driven pulley pressure sensor check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT driven pulley pressure sensor 3P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 1 Test point 2 CVT driven pulley pressure sensor 3P connector No. 3 Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Replace the CVT driven pulley pressure sensor . NO The CVT driven pulley pressure sensor is OK. Go to step 5.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT driven pulley pressure sensor 3P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 1

Test point 2 | CVT driven pulley pressure sensor 3P connector No. 3

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Replace the CVT driven pulley pressure sensor .

NO

The CVT driven pulley pressure sensor is OK. Go to step 5.

- Open wire check (VCC4 line) -1. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode CVT driven pulley pressure sensor 3P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 3 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES Repair an open in the SG4 wire between the CVT driven pulley pressure sensor and the TCM. NO Repair an open in the VCC4 wire between the CVT driven pulley pressure sensor and the TCM.

-1. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

CVT driven pulley pressure sensor 3P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 3

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

Repair an open in the SG4 wire between the CVT driven pulley pressure sensor and the TCM.

NO

Repair an open in the VCC4 wire between the CVT driven pulley pressure sensor and the TCM.
````

## Chunk 9876: DTC P0843 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0843 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12454.html`
- Chunk ID: `chunk_4f7c61ade171`
- Images: `images\GHH400047.jpeg`, `images\GHH400048.jpeg`, `images\GHH400049.jpeg`, `images\GHH400050.jpeg`
- Duplicate sources: `pages\15520.html`

### Full Text

````text
# DTC P0843 (L15B7/L15BA/L15BY (CVT))

DTC P0843 : Transmission Fluid Pressure Sensor/Switch "A" Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0843 Transmission Fluid Pressure Sensor/Switch "A" Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) More than 4.84 V Do the current condition(s) match the threshold? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | More than 4.84 | V

Do the current condition(s) match the threshold?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure sensor and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/onboard snapshot.

- Determine possible failure area (PDN line, others) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CVT driven pulley pressure sensor 3P connector -3. Connect terminals A and B with a jumper wire. Terminal A CVT driven pulley pressure sensor 3P connector No. 1 Terminal B CVT driven pulley pressure sensor 3P connector No. 2 Courtesy of HONDA, U.S.A., INC. -4. Turn the vehicle to the ON mode. -5. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit Driven Pulley Pressure Sensor(V) More than 4.84 V Do the current condition(s) match the threshold? YES Go to step 3. NO Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CVT driven pulley pressure sensor 3P connector

-3. Connect terminals A and B with a jumper wire.

Terminal A | CVT driven pulley pressure sensor 3P connector No. 1

Terminal B | CVT driven pulley pressure sensor 3P connector No. 2

Courtesy of HONDA, U.S.A., INC.

-4. Turn the vehicle to the ON mode.

-5. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Driven Pulley Pressure Sensor(V) | More than 4.84 | V

Do the current condition(s) match the threshold?

YES

Go to step 3.

NO

Go to step 4.

- Open wire check (PDN line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Remove the jumper wire. -3. Disconnect the following connector. TCM 50P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure sensor 3P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure sensor 3P connector No. 2 Test point 2 TCM 50P connector No. 31 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The PDN wire is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the PDN wire between the CVT driven pulley pressure sensor and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Remove the jumper wire.

-3. Disconnect the following connector.

TCM 50P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure sensor 3P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure sensor 3P connector No. 2

Test point 2 | TCM 50P connector No. 31

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The PDN wire is OK.
````

## Chunk 9877: DTC P0962, P0963 (K20C2 (CVT))

- Title: DTC P0962, P0963 (K20C2 (CVT))
- Source path: `pages\12455.html`
- Chunk ID: `chunk_529880422670`
- Images: `images\GHH400051.jpeg`, `images\GHH400052.jpeg`
- Duplicate sources: `pages\15498.html`

### Full Text

````text
# DTC P0962, P0963 (K20C2 (CVT))

DTC P0962 : CVT Drive Pulley Pressure Control Valve Circuit Low

DTC P0963 : CVT Drive Pulley Pressure Control Valve Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0962 CVT Drive Pulley Pressure Control Valve Circuit Low

P0963 CVT Drive Pulley Pressure Control Valve Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0962 CVT Drive Pulley Pressure Control Valve Circuit Low P0963 CVT Drive Pulley Pressure Control Valve Circuit High Is DTC P0962 or P0963 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0962 CVT Drive Pulley Pressure Control Valve Circuit Low

P0963 CVT Drive Pulley Pressure Control Valve Circuit High

Is DTC P0962 or P0963 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in DRLS line, open in DRLS/DRC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there 4.6-6.3 Ω ? 4.6-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 4.6 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15

Test point 2 | Body ground

Is there 4.6-6.3 Ω ?

4.6-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 4.6 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (DRLS line) -1. Disconnect the following connector. CVT drive pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM. NO The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15

Test point 2 | Body ground
````

## Chunk 9878: DTC P0962, P0963 (K20C2 (CVT))

- Title: DTC P0962, P0963 (K20C2 (CVT))
- Source path: `pages\12455.html`
- Chunk ID: `chunk_a7495685fc20`
- Images: `images\GHH400051.jpeg`, `images\GHH400052.jpeg`
- Duplicate sources: `pages\15498.html`

### Full Text

````text
ve pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM. NO The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM.

NO

The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

- Open wire check (DRLS/DRC+ line) -1. Disconnect the following connector. CVT drive pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley pressure control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 15 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DRLS/DRC+ wire is OK. Go to step 5. NO Repair an open in the DRLS/DRC+ wire between the CVT drive pulley pressure control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley pressure control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 15

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DRLS/DRC+ wire is OK. Go to step 5.

NO

Repair an open in the DRLS/DRC+ wire between the CVT drive pulley pressure control solenoid valve and the TCM.

- Open wire check (DRC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley pressure control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DRC- wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly . NO Repair an open in the DRC- wire between the CVT drive pulley pressure control solenoid valve and ground (G251), or repair poor ground (G251).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley pressure control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DRC- wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the DRC- wire between the CVT drive pulley pressure control solenoid valve and ground (G251), or repair poor ground (G251).
````

## Chunk 9879: DTC P0962, P0963 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0962, P0963 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12456.html`
- Chunk ID: `chunk_be8077ba4fae`
- Images: `images\GHH400053.jpeg`, `images\GHH400054.jpeg`
- Duplicate sources: `pages\15521.html`

### Full Text

````text
# DTC P0962, P0963 (L15B7/L15BA/L15BY (CVT))

DTC P0962 : CVT Drive Pulley Pressure Control Valve Circuit Low

DTC P0963 : CVT Drive Pulley Pressure Control Valve Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0962 CVT Drive Pulley Pressure Control Valve Circuit Low

P0963 CVT Drive Pulley Pressure Control Valve Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0962 CVT Drive Pulley Pressure Control Valve Circuit Low P0963 CVT Drive Pulley Pressure Control Valve Circuit High Is DTC P0962 or P0963 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0962 CVT Drive Pulley Pressure Control Valve Circuit Low

P0963 CVT Drive Pulley Pressure Control Valve Circuit High

Is DTC P0962 or P0963 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT drive pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in DRLS line, open in DRLS/DRC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there 5.0-6.3 Ω ? 5.0-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 5.0 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15

Test point 2 | Body ground

Is there 5.0-6.3 Ω ?

5.0-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 5.0 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (DRLS line) -1. Disconnect the following connector. CVT drive pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM. NO The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15
````

## Chunk 9880: DTC P0962, P0963 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0962, P0963 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12456.html`
- Chunk ID: `chunk_701a1ff42fd9`
- Images: `images\GHH400053.jpeg`, `images\GHH400054.jpeg`
- Duplicate sources: `pages\15521.html`

### Full Text

````text
icle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 15 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM. NO The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 15

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the DRLS wire between the CVT drive pulley pressure control solenoid valve and the TCM.

NO

The DRLS wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

- Open wire check (DRLS/DRC+ line) -1. Disconnect the following connector. CVT drive pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley pressure control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 15 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DRLS/DRC+ wire is OK. Go to step 5. NO Repair an open in the DRLS/DRC+ wire between the CVT drive pulley pressure control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT drive pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley pressure control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 15

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DRLS/DRC+ wire is OK. Go to step 5.

NO

Repair an open in the DRLS/DRC+ wire between the CVT drive pulley pressure control solenoid valve and the TCM.

- Open wire check (DRC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT drive pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT drive pulley pressure control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DRC- wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly . NO Repair an open in the DRC- wire between the CVT drive pulley pressure control solenoid valve and ground (G252), or repair poor ground (G252).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT drive pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT drive pulley pressure control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DRC- wire is OK. Faulty CVT drive pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the DRC- wire between the CVT drive pulley pressure control solenoid valve and ground (G252), or repair poor ground (G252).
````

## Chunk 9881: DTC P0966, P0967 (K20C2 (CVT))

- Title: DTC P0966, P0967 (K20C2 (CVT))
- Source path: `pages\12457.html`
- Chunk ID: `chunk_16dafe4d8040`
- Images: `images\GHH400055.jpeg`, `images\GHH400056.jpeg`
- Duplicate sources: `pages\15499.html`

### Full Text

````text
# DTC P0966, P0967 (K20C2 (CVT))

DTC P0966 : CVT Driven Pulley Pressure Control Valve Circuit Low

DTC P0967 : CVT Driven Pulley Pressure Control Valve Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0966 CVT Driven Pulley Pressure Control Valve Circuit Low

P0967 CVT Driven Pulley Pressure Control Valve Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0966 CVT Driven Pulley Pressure Control Valve Circuit Low P0967 CVT Driven Pulley Pressure Control Valve Circuit High Is DTC P0966 or P0967 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0966 CVT Driven Pulley Pressure Control Valve Circuit Low

P0967 CVT Driven Pulley Pressure Control Valve Circuit High

Is DTC P0966 or P0967 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in DNLS line, open in DNLS/DNC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there 4.6-6.3 Ω ? 4.6-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 4.6 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14

Test point 2 | Body ground

Is there 4.6-6.3 Ω ?

4.6-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 4.6 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (DNLS line) -1. Disconnect the following connector. CVT driven pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM. NO The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14
````

## Chunk 9882: DTC P0966, P0967 (K20C2 (CVT))

- Title: DTC P0966, P0967 (K20C2 (CVT))
- Source path: `pages\12457.html`
- Chunk ID: `chunk_725b66682ae4`
- Images: `images\GHH400055.jpeg`, `images\GHH400056.jpeg`
- Duplicate sources: `pages\15499.html`

### Full Text

````text
OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM. NO The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM.

NO

The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

- Open wire check (DNLS/DNC+ line) -1. Disconnect the following connector. CVT driven pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 14 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DNLS/DNC+ wire is OK. Go to step 5. NO Repair an open in the DNLS/DNC+ wire between the CVT driven pulley pressure control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 14

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DNLS/DNC+ wire is OK. Go to step 5.

NO

Repair an open in the DNLS/DNC+ wire between the CVT driven pulley pressure control solenoid valve and the TCM.

- Open wire check (DNC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DNC- wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Repair an open in the DNC- wire between the CVT driven pulley pressure control solenoid valve and ground (G251), or repair poor ground (G251).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DNC- wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the DNC- wire between the CVT driven pulley pressure control solenoid valve and ground (G251), or repair poor ground (G251).
````

## Chunk 9883: DTC P0966, P0967 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0966, P0967 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12458.html`
- Chunk ID: `chunk_74a21403c1a8`
- Images: `images\GHH400057.jpeg`, `images\GHH400058.jpeg`
- Duplicate sources: `pages\15522.html`

### Full Text

````text
# DTC P0966, P0967 (L15B7/L15BA/L15BY (CVT))

DTC P0966 : CVT Driven Pulley Pressure Control Valve Circuit Low

DTC P0967 : CVT Driven Pulley Pressure Control Valve Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0966 CVT Driven Pulley Pressure Control Valve Circuit Low

P0967 CVT Driven Pulley Pressure Control Valve Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0966 CVT Driven Pulley Pressure Control Valve Circuit Low P0967 CVT Driven Pulley Pressure Control Valve Circuit High Is DTC P0966 or P0967 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0966 CVT Driven Pulley Pressure Control Valve Circuit Low

P0967 CVT Driven Pulley Pressure Control Valve Circuit High

Is DTC P0966 or P0967 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT driven pulley pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in DNLS line, open in DNLS/DNC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there 5.0-6.3 Ω ? 5.0-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 5.0 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14

Test point 2 | Body ground

Is there 5.0-6.3 Ω ?

5.0-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 5.0 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (DNLS line) -1. Disconnect the following connector. CVT driven pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM. NO The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14
````

## Chunk 9884: DTC P0966, P0967 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0966, P0967 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12458.html`
- Chunk ID: `chunk_cec5deb51bfd`
- Images: `images\GHH400057.jpeg`, `images\GHH400058.jpeg`
- Duplicate sources: `pages\15522.html`

### Full Text

````text
OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 14 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM. NO The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 14

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the DNLS wire between the CVT driven pulley pressure control solenoid valve and the TCM.

NO

The DNLS wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

- Open wire check (DNLS/DNC+ line) -1. Disconnect the following connector. CVT driven pulley pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 14 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DNLS/DNC+ wire is OK. Go to step 5. NO Repair an open in the DNLS/DNC+ wire between the CVT driven pulley pressure control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT driven pulley pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 14

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DNLS/DNC+ wire is OK. Go to step 5.

NO

Repair an open in the DNLS/DNC+ wire between the CVT driven pulley pressure control solenoid valve and the TCM.

- Open wire check (DNC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT driven pulley pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT driven pulley pressure control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The DNC- wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Repair an open in the DNC- wire between the CVT driven pulley pressure control solenoid valve and ground (G252), or repair poor ground (G252).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT driven pulley pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT driven pulley pressure control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The DNC- wire is OK. Faulty CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the DNC- wire between the CVT driven pulley pressure control solenoid valve and ground (G252), or repair poor ground (G252).
````

## Chunk 9885: DTC P0970, P0971 (K20C2 (CVT))

- Title: DTC P0970, P0971 (K20C2 (CVT))
- Source path: `pages\12459.html`
- Chunk ID: `chunk_989c7dd5ce1e`
- Images: `images\GHH400059.jpeg`, `images\GHH400060.jpeg`
- Duplicate sources: `pages\15500.html`

### Full Text

````text
# DTC P0970, P0971 (K20C2 (CVT))

DTC P0970 : Pressure Control Solenoid "C" Control Circuit Low

DTC P0971 : Pressure Control Solenoid "C" Control Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0970 Pressure Control Solenoid "C" Control Circuit Low

P0971 Pressure Control Solenoid "C" Control Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0970 Pressure Control Solenoid "C" Control Circuit Low P0971 Pressure Control Solenoid "C" Control Circuit High Is DTC P0970 or P0971 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT clutch pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0970 Pressure Control Solenoid "C" Control Circuit Low

P0971 Pressure Control Solenoid "C" Control Circuit High

Is DTC P0970 or P0971 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT clutch pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in CPCLS line, open in CPCLS/CPC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 13 Test point 2 Body ground Is there 4.6-6.3 Ω ? 4.6-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 4.6 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 13

Test point 2 | Body ground

Is there 4.6-6.3 Ω ?

4.6-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 4.6 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (CPCLS line) -1. Disconnect the following connector. CVT clutch pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT clutch pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 13 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the CPCLS wire between the CVT clutch pressure control solenoid valve and the TCM. NO The CPCLS wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT clutch pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT clutch pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 13

Test point 2 | Body ground

Is there continuity?

YES
````

## Chunk 9886: DTC P0970, P0971 (K20C2 (CVT))

- Title: DTC P0970, P0971 (K20C2 (CVT))
- Source path: `pages\12459.html`
- Chunk ID: `chunk_cdecacad68ea`
- Images: `images\GHH400059.jpeg`, `images\GHH400060.jpeg`
- Duplicate sources: `pages\12460.html`, `pages\15500.html`, `pages\15523.html`

### Full Text

````text
utch pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 13 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the CPCLS wire between the CVT clutch pressure control solenoid valve and the TCM. NO The CPCLS wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT clutch pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT clutch pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 13

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the CPCLS wire between the CVT clutch pressure control solenoid valve and the TCM.

NO

The CPCLS wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

- Open wire check (CPCLS/CPC+ line) -1. Disconnect the following connector. CVT clutch pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT clutch pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT clutch pressure control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 13 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The CPCLS/CPC+ wire is OK. Go to step 5. NO Repair an open in the CPCLS/CPC+ wire between the CVT clutch pressure control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT clutch pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT clutch pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT clutch pressure control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 13

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The CPCLS/CPC+ wire is OK. Go to step 5.

NO

Repair an open in the CPCLS/CPC+ wire between the CVT clutch pressure control solenoid valve and the TCM.

- Open wire check (CPC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT clutch pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT clutch pressure control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The CPC- wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly . NO Repair an open in the CPC- wire between the CVT clutch pressure control solenoid valve and ground (G251), or repair poor ground (G251).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT clutch pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT clutch pressure control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The CPC- wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the CPC- wire between the CVT clutch pressure control solenoid valve and ground (G251), or repair poor ground (G251).
````

## Chunk 9887: DTC P0970, P0971 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0970, P0971 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12460.html`
- Chunk ID: `chunk_dee5c5e92481`
- Images: `images\GHH400061.jpeg`, `images\GHH400062.jpeg`
- Duplicate sources: `pages\15523.html`

### Full Text

````text
# DTC P0970, P0971 (L15B7/L15BA/L15BY (CVT))

DTC P0970 : Pressure Control Solenoid "C" Control Circuit Low

DTC P0971 : Pressure Control Solenoid "C" Control Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0970 Pressure Control Solenoid "C" Control Circuit Low

P0971 Pressure Control Solenoid "C" Control Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0970 Pressure Control Solenoid "C" Control Circuit Low P0971 Pressure Control Solenoid "C" Control Circuit High Is DTC P0970 or P0971 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT clutch pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0970 Pressure Control Solenoid "C" Control Circuit Low

P0971 Pressure Control Solenoid "C" Control Circuit High

Is DTC P0970 or P0971 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT clutch pressure control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in CPCLS line, open in CPCLS/CPC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 13 Test point 2 Body ground Is there 4.7-5.9 Ω ? 4.7-5.9 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 4.7 Ω Go to step 3. More than 5.9 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 13

Test point 2 | Body ground

Is there 4.7-5.9 Ω ?

4.7-5.9 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 4.7 Ω

Go to step 3.

More than 5.9 Ω

Go to step 4.

- Shorted wire check (CPCLS line) -1. Disconnect the following connector. CVT clutch pressure control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT clutch pressure control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 13 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the CPCLS wire between the CVT clutch pressure control solenoid valve and the TCM. NO The CPCLS wire is OK. Faulty CVT clutch pressure control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT clutch pressure control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT clutch pressure control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 13

Test point 2 | Body ground

Is there continuity?

YES
````

## Chunk 9888: DTC P0976, P0977 (K20C2 (CVT))

- Title: DTC P0976, P0977 (K20C2 (CVT))
- Source path: `pages\12461.html`
- Chunk ID: `chunk_544e6bbda71d`
- Images: `images\GHH400063.jpeg`, `images\GHH400064.jpeg`
- Duplicate sources: `pages\15501.html`

### Full Text

````text
# DTC P0976, P0977 (K20C2 (CVT))

DTC P0976 : Shift Solenoid Valve "B" Circuit Low

DTC P0977 : Shift Solenoid Valve "B" Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0976 Shift Solenoid Valve "B" Circuit Low

P0977 Shift Solenoid Valve "B" Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Test-drive under following conditions: DTC Test-drive condition P0976 Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds. P0977 Shift the transmission to P position/mode. Start the engine, and wait for at least 10 seconds. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0976 Shift Solenoid Valve "B" Circuit Low P0977 Shift Solenoid Valve "B" Circuit High Is DTC P0976 or P0977 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between shift solenoid valve B and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Test-drive under following conditions:

DTC | Test-drive condition

P0976 | Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds.

- Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

- Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds.

P0977 | Shift the transmission to P position/mode. Start the engine, and wait for at least 10 seconds.

- Shift the transmission to P position/mode.

- Start the engine, and wait for at least 10 seconds.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0976 Shift Solenoid Valve "B" Circuit Low

P0977 Shift Solenoid Valve "B" Circuit High

Is DTC P0976 or P0977 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between shift solenoid valve B and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in SOL B line, open in SOL B/SHB+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 7 Test point 2 Body ground Is there 8.9-12.2 Ω ? 8.9-12.2 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 8.9 Ω Go to step 3. More than 12.2 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there 8.9-12.2 Ω ?

8.9-12.2 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 8.9 Ω

Go to step 3.

More than 12.2 Ω

Go to step 4.

- Shorted wire check (SOL B line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2.
````

## Chunk 9889: DTC P0976, P0977 (K20C2 (CVT))

- Title: DTC P0976, P0977 (K20C2 (CVT))
- Source path: `pages\12461.html`
- Chunk ID: `chunk_4e108bc0d503`
- Images: `images\GHH400063.jpeg`, `images\GHH400064.jpeg`
- Duplicate sources: `pages\15501.html`

### Full Text

````text
4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there 8.9-12.2 Ω ?

8.9-12.2 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 8.9 Ω

Go to step 3.

More than 12.2 Ω

Go to step 4.

- Shorted wire check (SOL B line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve B 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 7 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL B wire between shift solenoid valve B and the TCM. NO The SOL B wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

-1. Disconnect the following connector.

Shift solenoid valve B 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve B 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the SOL B wire between shift solenoid valve B and the TCM.

NO

The SOL B wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

- Open wire check (SOL B/SHB+ line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve B 2P connector: disconnected TCM 50P connector: disconnected Test point 1 Shift solenoid valve B 2P connector No. 2 Test point 2 TCM 50P connector No. 7 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SOL B/SHB+ wire is OK. Go to step 5. NO Repair an open in the SOL B/SHB+ wire between shift solenoid valve B and the TCM.

-1. Disconnect the following connector.

Shift solenoid valve B 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve B 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Shift solenoid valve B 2P connector No. 2

Test point 2 | TCM 50P connector No. 7

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL B/SHB+ wire is OK. Go to step 5.

NO

Repair an open in the SOL B/SHB+ wire between shift solenoid valve B and the TCM.

- Open wire check (SHB- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve B 2P connector: disconnected TCM 50P connector: disconnected Test point 1 Shift solenoid valve B 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SHB- wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly . NO Repair an open in the SHB- wire between the shift solenoid valve B and ground (G252), or repair poor ground (G252).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve B 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Shift solenoid valve B 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SHB- wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

NO

Repair an open in the SHB- wire between the shift solenoid valve B and ground (G252), or repair poor ground (G252).
````

## Chunk 9890: DTC P0976, P0977 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0976, P0977 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12462.html`
- Chunk ID: `chunk_3661612f5ea4`
- Images: `images\GHH400065.jpeg`
- Duplicate sources: `pages\15524.html`

### Full Text

````text
# DTC P0976, P0977 (L15B7/L15BA/L15BY (CVT))

DTC P0976 : Shift Solenoid Valve "B" Circuit Low

DTC P0977 : Shift Solenoid Valve "B" Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0976 Shift Solenoid Valve "B" Circuit Low

P0977 Shift Solenoid Valve "B" Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Test-drive under following conditions: DTC Test-drive condition P0976 Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds. P0977 Shift the transmission to P position/mode. Start the engine, and wait for at least 10 seconds. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0976 Shift Solenoid Valve "B" Circuit Low P0977 Shift Solenoid Valve "B" Circuit High Is DTC P0976 or P0977 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between shift solenoid valve B and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Test-drive under following conditions:

DTC | Test-drive condition

P0976 | Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds.

- Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice).

- Test-drive the vehicle in D position/mode on a flat road at speeds about 37 mph (60 km/h) for at least 10 seconds.

P0977 | Shift the transmission to P position/mode. Start the engine, and wait for at least 10 seconds.

- Shift the transmission to P position/mode.

- Start the engine, and wait for at least 10 seconds.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0976 Shift Solenoid Valve "B" Circuit Low

P0977 Shift Solenoid Valve "B" Circuit High

Is DTC P0976 or P0977 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between shift solenoid valve B and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in SOL B line, open in SOL B/SHB+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 7 Test point 2 Body ground Is there 10.6-13.5 Ω ? 10.6-13.5 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 10.6 Ω Go to step 3. More than 13.5 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there 10.6-13.5 Ω ?

10.6-13.5 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 10.6 Ω

Go to step 3.

More than 13.5 Ω

Go to step 4.

- Shorted wire check (SOL B line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2.
````

## Chunk 9891: DTC P0976, P0977 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P0976, P0977 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12462.html`
- Chunk ID: `chunk_5269f6b419f5`
- Images: `images\GHH400065.jpeg`
- Duplicate sources: `pages\15524.html`

### Full Text

````text
-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there 10.6-13.5 Ω ?

10.6-13.5 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 10.6 Ω

Go to step 3.

More than 13.5 Ω

Go to step 4.

- Shorted wire check (SOL B line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve B 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 7 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL B wire between shift solenoid valve B and the TCM. NO The SOL B wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

-1. Disconnect the following connector.

Shift solenoid valve B 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve B 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 7

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the SOL B wire between shift solenoid valve B and the TCM.

NO

The SOL B wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

- Open wire check (SOL B/SHB+ line) -1. Disconnect the following connector. Shift solenoid valve B 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve B 2P connector: disconnected TCM 50P connector: disconnected Test point 1 Shift solenoid valve B 2P connector No. 1 Test point 2 TCM 50P connector No. 7 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SOL B/SHB+ wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly . NO Repair an open in the SOL B/SHB+ wire between shift solenoid valve B and the TCM.

-1. Disconnect the following connector.

Shift solenoid valve B 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve B 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Shift solenoid valve B 2P connector No. 1

Test point 2 | TCM 50P connector No. 7

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL B/SHB+ wire is OK. Faulty shift solenoid valve B. Replace the valve body assembly .

NO

Repair an open in the SOL B/SHB+ wire between shift solenoid valve B and the TCM.
````

## Chunk 9892: DTC P1717 (K20C2 (CVT))

- Title: DTC P1717 (K20C2 (CVT))
- Source path: `pages\12463.html`
- Chunk ID: `chunk_959fc56fc861`
- Images: `images\GHH400066.jpeg`, `images\GHH400067.jpeg`
- Duplicate sources: `pages\15502.html`

### Full Text

````text
# DTC P1717 (K20C2 (CVT))

DTC P1717 : Transmission Range Switch ATP RVS Switch (Open or Short)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1717 Transmission Range Switch ATP RVS Switch (Open or Short)

DTC (CVT)

- Problem verification -1. Make sure the shift cable is properly adjusted . -2. Turn the vehicle to the ON mode. -3. Shift the transmission to R position/mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit A/T R Switch ON Reverse Switch(ATPRVS) ON Do the current condition(s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Make sure the shift cable is properly adjusted .

-2. Turn the vehicle to the ON mode.

-3. Shift the transmission to R position/mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

A/T R Switch | ON

Reverse Switch(ATPRVS) | ON

Do the current condition(s) match the threshold?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Open wire check (ATP-RVS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 10 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The ATP-RVS wire is OK. Go to step 3. NO Repair an open in the ATP-RVS wire between the transmission range switch and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 10

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The ATP-RVS wire is OK. Go to step 3.

NO

Repair an open in the ATP-RVS wire between the transmission range switch and the TCM.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 5 Test point 2 Transmission range switch 10P connector No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity when the shift lever is in R position/mode, and no continuity when the shift lever is shifted to any other position/mode? YES The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 5

Test point 2 | Transmission range switch 10P connector No. 10

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9893: DTC P1717 (K20C2 (CVT))

- Title: DTC P1717 (K20C2 (CVT))
- Source path: `pages\12463.html`
- Chunk ID: `chunk_c5092172bd6a`
- Images: `images\GHH400066.jpeg`, `images\GHH400067.jpeg`
- Duplicate sources: `pages\15502.html`

### Full Text

````text
on/mode? YES The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 5

Test point 2 | Transmission range switch 10P connector No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity when the shift lever is in R position/mode, and no continuity when the shift lever is shifted to any other position/mode?

YES

The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .
````

## Chunk 9894: DTC P1717 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1717 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12464.html`
- Chunk ID: `chunk_988af9ed0078`
- Images: `images\GHH400068.jpeg`, `images\GHH400069.jpeg`
- Duplicate sources: `pages\15525.html`

### Full Text

````text
# DTC P1717 (L15B7/L15BA/L15BY (CVT))

DTC P1717 : Transmission Range Switch ATP RVS Switch (Open or Short)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1717 Transmission Range Switch ATP RVS Switch (Open or Short)

DTC (CVT)

- Problem verification -1. Make sure the shift cable is properly adjusted . -2. Turn the vehicle to the ON mode. -3. Shift the transmission to R position/mode. -4. Check the parameter(s) below with the HDS. Signal Threshold Current conditions Values Unit Values Unit A/T R Switch ON Reverse Switch(ATPRVS) ON Do the current condition(s) match the threshold? YES Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. NO The failure is duplicated. Go to step 2.

-1. Make sure the shift cable is properly adjusted .

-2. Turn the vehicle to the ON mode.

-3. Shift the transmission to R position/mode.

-4. Check the parameter(s) below with the HDS.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

A/T R Switch | ON

Reverse Switch(ATPRVS) | ON

Do the current condition(s) match the threshold?

YES

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmission range switch and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

NO

The failure is duplicated. Go to step 2.

- Open wire check (ATP-RVS line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. Transmission range switch 10P connector -3. Turn the vehicle to the ON mode. -4. Measure the voltage between test points 1 and 2. Test condition Vehicle ON mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 10 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there about 5 V? YES The ATP-RVS wire is OK. Go to step 3. NO Repair an open in the ATP-RVS wire between the transmission range switch and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

Transmission range switch 10P connector

-3. Turn the vehicle to the ON mode.

-4. Measure the voltage between test points 1 and 2.

Test condition | Vehicle ON mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 10

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there about 5 V?

YES

The ATP-RVS wire is OK. Go to step 3.

NO

Repair an open in the ATP-RVS wire between the transmission range switch and the TCM.

- Transmission range switch check -1. Turn the vehicle to the OFF (LOCK) mode. -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Transmission range switch 10P connector: disconnected Test point 1 Transmission range switch 10P connector No. 1 Test point 2 Transmission range switch 10P connector No. 10 Courtesy of HONDA, U.S.A., INC. Is there continuity when the shift lever is in R position/mode, and no continuity when the shift lever is shifted to any other position/mode? YES The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 1

Test point 2 | Transmission range switch 10P connector No. 10

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9895: DTC P1717 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1717 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12464.html`
- Chunk ID: `chunk_657d8c142808`
- Images: `images\GHH400068.jpeg`, `images\GHH400069.jpeg`
- Duplicate sources: `pages\15525.html`

### Full Text

````text
on/mode? YES The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Transmission range switch 10P connector: disconnected

Test point 1 | Transmission range switch 10P connector No. 1

Test point 2 | Transmission range switch 10P connector No. 10

Courtesy of HONDA, U.S.A., INC.

Is there continuity when the shift lever is in R position/mode, and no continuity when the shift lever is shifted to any other position/mode?

YES

The transmission range switch is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Check for proper transmission range switch installation, then recheck. If the transmission range switch installation is OK, replace the transmission range switch .
````

## Chunk 9896: DTC P1840 (K20C2 (CVT))

- Title: DTC P1840 (K20C2 (CVT))
- Source path: `pages\12465.html`
- Chunk ID: `chunk_8e330807a021`
- Images: none
- Duplicate sources: `pages\15503.html`

### Full Text

````text
# DTC P1840 (K20C2 (CVT))

DTC P1840 : CVT Speed Sensor Circuit Forward Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1840 CVT Speed Sensor Circuit Forward Rotation Range/Performance

DTC (CVT)

- CVT speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Secondary-shaft Rotation Forward Do the current condition(s) match the threshold? YES The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Secondary-shaft Rotation | Forward

Do the current condition(s) match the threshold?

YES

The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT speed sensor .
````

## Chunk 9897: DTC P1840 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1840 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12466.html`
- Chunk ID: `chunk_5c012e1ecc75`
- Images: none
- Duplicate sources: `pages\15526.html`

### Full Text

````text
# DTC P1840 (L15B7/L15BA/L15BY (CVT))

DTC P1840 : CVT Speed Sensor Circuit Forward Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1840 CVT Speed Sensor Circuit Forward Rotation Range/Performance

DTC (CVT)

- CVT speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Secondary-shaft Rotation Forward Do the current condition(s) match the threshold? YES The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Secondary-shaft Rotation | Forward

Do the current condition(s) match the threshold?

YES

The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT speed sensor .
````

## Chunk 9898: DTC P1841 (K20C2 (CVT))

- Title: DTC P1841 (K20C2 (CVT))
- Source path: `pages\12467.html`
- Chunk ID: `chunk_52b0bbb82c1d`
- Images: none
- Duplicate sources: `pages\15504.html`

### Full Text

````text
# DTC P1841 (K20C2 (CVT))

DTC P1841 : CVT Speed Sensor Circuit Reverse Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1841 CVT Speed Sensor Circuit Reverse Rotation Range/Performance

DTC (CVT)

- CVT speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Secondary-shaft Rotation Reverse Do the current condition(s) match the threshold? YES The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Secondary-shaft Rotation | Reverse

Do the current condition(s) match the threshold?

YES

The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT speed sensor .
````

## Chunk 9899: DTC P1841 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1841 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12468.html`
- Chunk ID: `chunk_24e2e52c6942`
- Images: none
- Duplicate sources: `pages\15527.html`

### Full Text

````text
# DTC P1841 (L15B7/L15BA/L15BY (CVT))

DTC P1841 : CVT Speed Sensor Circuit Reverse Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1841 CVT Speed Sensor Circuit Reverse Rotation Range/Performance

DTC (CVT)

- CVT speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Secondary-shaft Rotation Reverse Do the current condition(s) match the threshold? YES The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Secondary-shaft Rotation | Reverse

Do the current condition(s) match the threshold?

YES

The CVT speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT speed sensor .
````

## Chunk 9900: DTC P1844 (K20C2, CVT model)

- Title: DTC P1844 (K20C2, CVT model)
- Source path: `pages\12469.html`
- Chunk ID: `chunk_cc1c5ce0ce57`
- Images: none
- Duplicate sources: `pages\15505.html`

### Full Text

````text
# DTC P1844 (K20C2, CVT model)

DTC P1844 : CVT Input Shaft Speed Sensor Circuit Forward Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1844 CVT Input Shaft Speed Sensor Circuit Forward Rotation Range/Performance

DTC (CVT)

- CVT drive pulley speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Drive Pulley Rotation Forward Do the current condition(s) match the threshold? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Drive Pulley Rotation | Forward

Do the current condition(s) match the threshold?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9901: DTC P1844 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1844 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12470.html`
- Chunk ID: `chunk_11b41a883c09`
- Images: none
- Duplicate sources: `pages\15528.html`

### Full Text

````text
# DTC P1844 (L15B7/L15BA/L15BY (CVT))

DTC P1844 : CVT Input Shaft Speed Sensor Circuit Forward Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1844 CVT Input Shaft Speed Sensor Circuit Forward Rotation Range/Performance

DTC (CVT)

- CVT drive pulley speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Drive Pulley Rotation Forward Do the current condition(s) match the threshold? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in D position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in D position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Drive Pulley Rotation | Forward

Do the current condition(s) match the threshold?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9902: DTC P1845 (K20C2 (CVT))

- Title: DTC P1845 (K20C2 (CVT))
- Source path: `pages\12471.html`
- Chunk ID: `chunk_4382b4cc1459`
- Images: none
- Duplicate sources: `pages\15506.html`

### Full Text

````text
# DTC P1845 (K20C2 (CVT))

DTC P1845 : CVT Input Shaft Speed Sensor Circuit Reverse Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1845 CVT Input Shaft Speed Sensor Circuit Reverse Rotation Range/Performance

DTC (CVT)

- CVT drive pulley speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Drive Pulley Rotation Reverse Do the current condition(s) match the threshold? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Drive Pulley Rotation | Reverse

Do the current condition(s) match the threshold?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9903: DTC P1845 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1845 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12472.html`
- Chunk ID: `chunk_3902ddaa0663`
- Images: none
- Duplicate sources: `pages\15529.html`

### Full Text

````text
# DTC P1845 (L15B7/L15BA/L15BY (CVT))

DTC P1845 : CVT Input Shaft Speed Sensor Circuit Reverse Rotation Range/Performance

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1845 CVT Input Shaft Speed Sensor Circuit Reverse Rotation Range/Performance

DTC (CVT)

- CVT drive pulley speed sensor check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely. -4. Start the engine, disable the VSA by pressing the VSA OFF button. NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h). -5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds. -6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode. Signal Threshold Current conditions Values Unit Values Unit Direction of Drive Pulley Rotation Reverse Do the current condition(s) match the threshold? YES The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Replace the CVT drive pulley speed sensor .

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Raise the vehicle on a lift. Make sure it is securely supported, and allow all four wheels to rotate freely.

-4. Start the engine, disable the VSA by pressing the VSA OFF button.

NOTE: Enter the VSA maintenance mode in case of the vehicle speed above 31 mph (50 km/h).

-5. Test-drive the vehicle in R position/mode at speeds over 19 mph (30 km/h) for at least 5 seconds.

-6. Check the parameter(s) below with the HDS while running the vehicle in R position/mode.

Signal | Threshold | Current conditions

Values | Unit | Values | Unit

Direction of Drive Pulley Rotation | Reverse

Do the current condition(s) match the threshold?

YES

The CVT drive pulley speed sensor is OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Replace the CVT drive pulley speed sensor .
````

## Chunk 9904: DTC P1855 (K20C2 (CVT))

- Title: DTC P1855 (K20C2 (CVT))
- Source path: `pages\12473.html`
- Chunk ID: `chunk_4e015a156eca`
- Images: none
- Duplicate sources: `pages\15507.html`

### Full Text

````text
# DTC P1855 (K20C2 (CVT))

DTC P1855 : Inclination Sensor Circuit Range/Performance

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1855 Inclination Sensor Circuit Range/Performance

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. Clear DTC (CVT) -3. Test-drive the vehicle until the OBD status of DTC P1855 changes. -4. Monitor the OBD STATUS for DTC P1855 in the DTCs MENU with the HDS. DTC Description OBD STATUS P1855 Inclination Sensor Circuit Range/Performance Does the HDS indicate FAILED? YES The failure is duplicated. Replace the SRS unit . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the SRS unit and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

Clear DTC (CVT)

-3. Test-drive the vehicle until the OBD status of DTC P1855 changes.

-4. Monitor the OBD STATUS for DTC P1855 in the DTCs MENU with the HDS.

DTC Description | OBD STATUS

P1855 Inclination Sensor Circuit Range/Performance

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the SRS unit .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the SRS unit and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot. If the HDS indicates NOT COMPLETED, go to step 1-3 and recheck.
````

## Chunk 9905: DTC P1890 (K20C2 (CVT))

- Title: DTC P1890 (K20C2 (CVT))
- Source path: `pages\12474.html`
- Chunk ID: `chunk_3bdf3c049404`
- Images: none
- Duplicate sources: `pages\15508.html`

### Full Text

````text
# DTC P1890 (K20C2 (CVT))

DTC P1890 : CVT Speed Control System

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1890 CVT Speed Control System

DTC (CVT)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame Is there any DTC(s) other than DTC P1890? YES Go to the indicated DTC's troubleshooting. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

Is there any DTC(s) other than DTC P1890?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to step 2.

- Problem verification -1. Clear the DTC with the HDS. -2. Start the engine. -3. Test-drive the vehicle in D position/mode, accelerate slowly until the vehicle speed reaches 37 mph (60 km/h) on a flat road, then keep the vehicle at speeds about 37 mph (60 km/h) for at least 60 seconds. -4. Monitor the OBD STATUS for P1890 in the DTCs MENU with the HDS. DTC Description OBD Status P1890 CVT Speed Control System Does the HDS indicate FAILED? YES The failure is duplicated. Replace the transmission . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the HDS indicates NOT COMPLETED, test-drive again. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Clear the DTC with the HDS.

-2. Start the engine.

-3. Test-drive the vehicle in D position/mode, accelerate slowly until the vehicle speed reaches 37 mph (60 km/h) on a flat road, then keep the vehicle at speeds about 37 mph (60 km/h) for at least 60 seconds.

-4. Monitor the OBD STATUS for P1890 in the DTCs MENU with the HDS.

DTC Description | OBD Status

P1890 CVT Speed Control System

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the transmission .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the HDS indicates NOT COMPLETED, test-drive again. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9906: DTC P1890 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1890 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12475.html`
- Chunk ID: `chunk_8b76faaa55d5`
- Images: none
- Duplicate sources: `pages\15530.html`

### Full Text

````text
# DTC P1890 (L15B7/L15BA/L15BY (CVT))

DTC P1890 : CVT Speed Control System

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1890 CVT Speed Control System

DTC (CVT)

- DTC check -1. Turn the vehicle to the ON mode. -2. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame Is there any DTC(s) other than DTC P1890? YES Go to the indicated DTC's troubleshooting. NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

Is there any DTC(s) other than DTC P1890?

YES

Go to the indicated DTC's troubleshooting.

NO

Go to step 2.

- Problem verification -1. Clear the DTC with the HDS. -2. Start the engine. -3. Test-drive the vehicle in D position/mode, accelerate slowly until the vehicle speed reaches 37 mph (60 km/h) on a flat road, then keep the vehicle at speeds about 37 mph (60 km/h) for at least 60 seconds. -4. Monitor the OBD STATUS for P1890 in the DTCs MENU with the HDS. DTC Description OBD Status P1890 CVT Speed Control System Does the HDS indicate FAILED? YES The failure is duplicated. Replace the transmission . NO If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the HDS indicates NOT COMPLETED, test-drive again. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Clear the DTC with the HDS.

-2. Start the engine.

-3. Test-drive the vehicle in D position/mode, accelerate slowly until the vehicle speed reaches 37 mph (60 km/h) on a flat road, then keep the vehicle at speeds about 37 mph (60 km/h) for at least 60 seconds.

-4. Monitor the OBD STATUS for P1890 in the DTCs MENU with the HDS.

DTC Description | OBD Status

P1890 CVT Speed Control System

Does the HDS indicate FAILED?

YES

The failure is duplicated. Replace the transmission .

NO

If the HDS indicates PASSED, intermittent failure, the system is OK at this time. If the HDS indicates NOT COMPLETED, test-drive again. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9907: DTC P1898 (K20C2, CVT model)

- Title: DTC P1898 (K20C2, CVT model)
- Source path: `pages\12476.html`
- Chunk ID: `chunk_f02549eef2de`
- Images: none
- Duplicate sources: `pages\15509.html`

### Full Text

````text
# DTC P1898 (K20C2, CVT model)

DTC P1898 : CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF Are DTC P1898 and P0780 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

Are DTC P1898 and P0780 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9908: DTC P1898 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1898 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12477.html`
- Chunk ID: `chunk_911f8a4695ee`
- Images: none
- Duplicate sources: `pages\15531.html`

### Full Text

````text
# DTC P1898 (L15B7/L15BA/L15BY (CVT))

DTC P1898 : CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF Are DTC P1898 and P0780 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1898 CVT Drive Pulley Pressure Control Valve Stuck ON or CVT Driven Pulley Pressure Control Valve Stuck OFF

Are DTC P1898 and P0780 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9909: DTC P1899 (K20C2 (CVT))

- Title: DTC P1899 (K20C2 (CVT))
- Source path: `pages\12478.html`
- Chunk ID: `chunk_c197a79bb710`
- Images: none
- Duplicate sources: `pages\15510.html`

### Full Text

````text
# DTC P1899 (K20C2 (CVT))

DTC P1899 : CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON Are DTC P1899 and P0780 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

Are DTC P1899 and P0780 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9910: DTC P1899 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P1899 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12479.html`
- Chunk ID: `chunk_78bdcb885e24`
- Images: none
- Duplicate sources: `pages\15532.html`

### Full Text

````text
# DTC P1899 (L15B7/L15BA/L15BY (CVT))

DTC P1899 : CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. -4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P0780 Shift Error P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON Are DTC P1899 and P0780 indicated? YES The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine.

-4. Test-drive the vehicle in D position/mode until the vehicle speed reaches 37 mph (60 km/h). Slow down and stop the vehicle, then accelerate from a stop at full throttle in D position/mode until the vehicle speed reaches 37 mph (60 km/h).

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P0780 Shift Error

P1899 CVT Drive Pulley Pressure Control Valve Stuck OFF or CVT Driven Pulley Pressure Control Valve Stuck ON

Are DTC P1899 and P0780 indicated?

YES

The failure is duplicated. Faulty CVT drive pulley pressure control solenoid valve and/or CVT driven pulley pressure control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9911: DTC P2715 (K20C2 (CVT))

- Title: DTC P2715 (K20C2 (CVT))
- Source path: `pages\12480.html`
- Chunk ID: `chunk_230edbbe76f4`
- Images: none
- Duplicate sources: `pages\15511.html`

### Full Text

````text
# DTC P2715 (K20C2 (CVT))

DTC P2715 : Pressure Control Solenoid "D" Stuck On

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2715 Pressure Control Solenoid "D" Stuck On

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode at speeds 12 mph (20 km/h) or below for at least 10 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2715 Pressure Control Solenoid "D" Stuck On Is DTC P2715 indicated? YES The failure is duplicated. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode at speeds 12 mph (20 km/h) or below for at least 10 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2715 Pressure Control Solenoid "D" Stuck On

Is DTC P2715 indicated?

YES

The failure is duplicated. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9912: DTC P2715 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P2715 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12481.html`
- Chunk ID: `chunk_190939b38371`
- Images: none
- Duplicate sources: `pages\15533.html`

### Full Text

````text
# DTC P2715 (L15B7/L15BA/L15BY (CVT))

DTC P2715 : Pressure Control Solenoid "D" Stuck On

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2715 Pressure Control Solenoid "D" Stuck On

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode at speeds 12 mph (20 km/h) or below for at least 10 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2715 Pressure Control Solenoid "D" Stuck On Is DTC P2715 indicated? YES The failure is duplicated. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly . NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode at speeds 12 mph (20 km/h) or below for at least 10 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2715 Pressure Control Solenoid "D" Stuck On

Is DTC P2715 indicated?

YES

The failure is duplicated. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9913: DTC P2720, P2721 (K20C2 (CVT))

- Title: DTC P2720, P2721 (K20C2 (CVT))
- Source path: `pages\12482.html`
- Chunk ID: `chunk_6586c277301a`
- Images: `images\GHH400070.jpeg`, `images\GHH400071.jpeg`
- Duplicate sources: `pages\15512.html`

### Full Text

````text
# DTC P2720, P2721 (K20C2 (CVT))

DTC P2720 : Pressure Control Solenoid "D" Control Circuit Low

DTC P2721 : Pressure Control Solenoid "D" Control Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2720 Pressure Control Solenoid "D" Control Circuit Low

P2721 Pressure Control Solenoid "D" Control Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2720 Pressure Control Solenoid "D" Control Circuit Low P2721 Pressure Control Solenoid "D" Control Circuit High Is DTC P2720 or P2721 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT lock-up clutch control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2720 Pressure Control Solenoid "D" Control Circuit Low

P2721 Pressure Control Solenoid "D" Control Circuit High

Is DTC P2720 or P2721 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT lock-up clutch control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in LCCLS line, open in LCCLS/LCC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 16 Test point 2 Body ground Is there 4.6-6.3 Ω ? 4.6-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 4.6 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 16

Test point 2 | Body ground

Is there 4.6-6.3 Ω ?

4.6-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 4.6 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (LCCLS line) -1. Disconnect the following connector. CVT lock-up clutch control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT lock-up clutch control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the LCCLS wire between the CVT lock-up clutch control solenoid valve and the TCM. NO The LCCLS wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT lock-up clutch control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT lock-up clutch control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 16

Test point 2 | Body ground

Is there continuity?

YES
````

## Chunk 9914: DTC P2720, P2721 (K20C2 (CVT))

- Title: DTC P2720, P2721 (K20C2 (CVT))
- Source path: `pages\12482.html`
- Chunk ID: `chunk_9a1c5991b0b3`
- Images: `images\GHH400070.jpeg`, `images\GHH400071.jpeg`
- Duplicate sources: `pages\12483.html`, `pages\15512.html`, `pages\15534.html`

### Full Text

````text
VT lock-up clutch control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the LCCLS wire between the CVT lock-up clutch control solenoid valve and the TCM. NO The LCCLS wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT lock-up clutch control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT lock-up clutch control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 16

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the LCCLS wire between the CVT lock-up clutch control solenoid valve and the TCM.

NO

The LCCLS wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

- Open wire check (LCCLS/LCC+ line) -1. Disconnect the following connector. CVT lock-up clutch control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT lock-up clutch control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT lock-up clutch control solenoid valve 2P connector No. 2 Test point 2 TCM 50P connector No. 16 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LCCLS/LCC+ wire is OK. Go to step 5. NO Repair an open in the LCCLS/LCC+ wire between the CVT lock-up clutch control solenoid valve and the TCM.

-1. Disconnect the following connector.

CVT lock-up clutch control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT lock-up clutch control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT lock-up clutch control solenoid valve 2P connector No. 2

Test point 2 | TCM 50P connector No. 16

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LCCLS/LCC+ wire is OK. Go to step 5.

NO

Repair an open in the LCCLS/LCC+ wire between the CVT lock-up clutch control solenoid valve and the TCM.

- Open wire check (LCC- line) -1. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT lock-up clutch control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 CVT lock-up clutch control solenoid valve 2P connector No. 1 Test point 2 Body ground Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The LCC- wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly . NO Repair an open in the LCC- wire between the CVT lock-up clutch control solenoid valve and ground (G251), or repair poor ground (G251).

-1. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT lock-up clutch control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CVT lock-up clutch control solenoid valve 2P connector No. 1

Test point 2 | Body ground

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The LCC- wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

NO

Repair an open in the LCC- wire between the CVT lock-up clutch control solenoid valve and ground (G251), or repair poor ground (G251).
````

## Chunk 9915: DTC P2720, P2721 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P2720, P2721 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12483.html`
- Chunk ID: `chunk_a895780bc844`
- Images: `images\GHH400072.jpeg`, `images\GHH400073.jpeg`
- Duplicate sources: `pages\15534.html`

### Full Text

````text
# DTC P2720, P2721 (L15B7/L15BA/L15BY (CVT))

DTC P2720 : Pressure Control Solenoid "D" Control Circuit Low

DTC P2721 : Pressure Control Solenoid "D" Control Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2720 Pressure Control Solenoid "D" Control Circuit Low

P2721 Pressure Control Solenoid "D" Control Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2720 Pressure Control Solenoid "D" Control Circuit Low P2721 Pressure Control Solenoid "D" Control Circuit High Is DTC P2720 or P2721 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT lock-up clutch control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2720 Pressure Control Solenoid "D" Control Circuit Low

P2721 Pressure Control Solenoid "D" Control Circuit High

Is DTC P2720 or P2721 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the CVT lock-up clutch control solenoid valve and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in LCCLS line, open in LCCLS/LCC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 16 Test point 2 Body ground Is there 5.0-6.3 Ω ? 5.0-6.3 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 5.0 Ω Go to step 3. More than 6.3 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 16

Test point 2 | Body ground

Is there 5.0-6.3 Ω ?

5.0-6.3 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 5.0 Ω

Go to step 3.

More than 6.3 Ω

Go to step 4.

- Shorted wire check (LCCLS line) -1. Disconnect the following connector. CVT lock-up clutch control solenoid valve 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CVT lock-up clutch control solenoid valve 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 16 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the LCCLS wire between the CVT lock-up clutch control solenoid valve and the TCM. NO The LCCLS wire is OK. Faulty CVT lock-up clutch control solenoid valve. Replace the valve body assembly .

-1. Disconnect the following connector.

CVT lock-up clutch control solenoid valve 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CVT lock-up clutch control solenoid valve 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 16

Test point 2 | Body ground

Is there continuity?

YES
````

## Chunk 9916: DTC P2817 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P2817 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12484.html`
- Chunk ID: `chunk_89278904a434`
- Images: none
- Duplicate sources: `pages\15535.html`

### Full Text

````text
# DTC P2817 (L15B7/L15BA/L15BY (CVT))

DTC P2817 : Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck Off

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2817 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck Off

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode until the vehicle speed reaches 12 mph (20 km/h). Slow down to a stop, and keep stopping for at least 10 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2817 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck Off Is DTC P2817 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode until the vehicle speed reaches 12 mph (20 km/h). Slow down to a stop, and keep stopping for at least 10 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2817 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck Off

Is DTC P2817 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Shift Solenoid Valve O/P operation check -1. Select the Shift Solenoid Valve O/P Test in the Miscellaneous Test Menu, and check that the shift solenoid valve O/P operates with the HDS. Shift Solenoid Valve O/P Does the shift solenoid valve O/P work properly? YES The shift solenoid valve O/P is OK. Replace the transmission fluid pump . NO Replace the shift solenoid valve O/P .

-1. Select the Shift Solenoid Valve O/P Test in the Miscellaneous Test Menu, and check that the shift solenoid valve O/P operates with the HDS.

Shift Solenoid Valve O/P

Does the shift solenoid valve O/P work properly?

YES

The shift solenoid valve O/P is OK. Replace the transmission fluid pump .

NO

Replace the shift solenoid valve O/P .
````

## Chunk 9917: DTC P2818 (L15B7/L15BA/L15BY (CVT))

- Title: DTC P2818 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12485.html`
- Chunk ID: `chunk_97b82287effc`
- Images: none
- Duplicate sources: `pages\15536.html`

### Full Text

````text
# DTC P2818 (L15B7/L15BA/L15BY (CVT))

DTC P2818 : Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck On

NOTE: Before you troubleshoot, review the General Troubleshooting Information .

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2818 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck On

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode until the vehicle speed reaches 25 mph (40 km/h). Slow down to a stop, and keep stopping for at least 10 seconds. -4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P2818 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck On Is DTC P2818 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Start the engine. With the brake pedal pressed, shift the transmission to N position/mode, then shift to D position/mode, and wait for at least 1 second. Release the brake pedal, and test-drive the vehicle in D position/mode until the vehicle speed reaches 25 mph (40 km/h). Slow down to a stop, and keep stopping for at least 10 seconds.

-4. Turn the vehicle to the OFF (LOCK) mode. Repeat the test-drive in step 1-3 again.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P2818 Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Stuck On

Is DTC P2818 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Shift Solenoid Valve O/P operation check -1. Select the Shift Solenoid Valve O/P Test in the Miscellaneous Test Menu, and check that the shift solenoid valve O/P operates with the HDS. Shift Solenoid Valve O/P Does the shift solenoid valve O/P work properly? YES The shift solenoid valve O/P is OK. Replace the transmission fluid pump . NO Replace the shift solenoid valve O/P .

-1. Select the Shift Solenoid Valve O/P Test in the Miscellaneous Test Menu, and check that the shift solenoid valve O/P operates with the HDS.

Shift Solenoid Valve O/P

Does the shift solenoid valve O/P work properly?

YES

The shift solenoid valve O/P is OK. Replace the transmission fluid pump .

NO

Replace the shift solenoid valve O/P .
````

## Chunk 9918: DTC P281D, P281E (L15B7/L15BA/L15BY (CVT))

- Title: DTC P281D, P281E (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12486.html`
- Chunk ID: `chunk_bb0e3d410052`
- Images: `images\GHH400074.jpeg`
- Duplicate sources: `pages\15537.html`

### Full Text

````text
# DTC P281D, P281E (L15B7/L15BA/L15BY (CVT))

DTC P281D : Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit Low

DTC P281E : Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit High

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P281D Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit Low

P281E Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit High

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Test-drive under following conditions: DTC Test-drive condition P281D Start the engine. Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds. P281E Start the engine. Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds. Shift the transmission to P position/mode. Turn the vehicle to the OFF (LOCK) mode. Start the engine, and wait for at least 1 second. -4. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame P281D Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit Low P281E Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit High Is DTC P281D or P281E indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the shift solenoid valve O/P and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Test-drive under following conditions:

DTC | Test-drive condition

P281D | Start the engine. Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds.

- Start the engine.

- Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds.

P281E | Start the engine. Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds. Shift the transmission to P position/mode. Turn the vehicle to the OFF (LOCK) mode. Start the engine, and wait for at least 1 second.

- Start the engine.

- Shift the transmission to D position/mode while pressing the brake pedal, and wait for at least 30 seconds.

- Shift the transmission to P position/mode.

- Turn the vehicle to the OFF (LOCK) mode.

- Start the engine, and wait for at least 1 second.

-4. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

P281D Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit Low

P281E Shift Solenoid Valve O/P (Pressure Control Solenoid "H") Control Circuit High

Is DTC P281D or P281E indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the shift solenoid valve O/P and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Determine possible failure area (TCM, short in SOL C line, open in SOL C/SHC+ line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 6 Test point 2 Body ground Is there 10.6-13.5 Ω ? 10.6-13.5 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 10.6 Ω Go to step 3. More than 13.5 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected
````

## Chunk 9919: DTC P281D, P281E (L15B7/L15BA/L15BY (CVT))

- Title: DTC P281D, P281E (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12486.html`
- Chunk ID: `chunk_eeba7a255da3`
- Images: `images\GHH400074.jpeg`
- Duplicate sources: `pages\15537.html`

### Full Text

````text
nnect the following connector. TCM 50P connector -3. Measure the resistance between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 6 Test point 2 Body ground Is there 10.6-13.5 Ω ? 10.6-13.5 Ω Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . Less than 10.6 Ω Go to step 3. More than 13.5 Ω Go to step 4.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

TCM 50P connector

-3. Measure the resistance between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 6

Test point 2 | Body ground

Is there 10.6-13.5 Ω ?

10.6-13.5 Ω

Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

Less than 10.6 Ω

Go to step 3.

More than 13.5 Ω

Go to step 4.

- Shorted wire check (SOL C line) -1. Disconnect the following connector. Shift solenoid valve O/P 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve O/P 2P connector: disconnected TCM 50P connector: disconnected Test point 1 TCM 50P connector No. 6 Test point 2 Body ground Is there continuity? YES Repair a short to ground in the SOL C wire between the shift solenoid valve O/P and the TCM. NO The SOL C wire is OK. Replace the shift solenoid valve O/P .

-1. Disconnect the following connector.

Shift solenoid valve O/P 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve O/P 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | TCM 50P connector No. 6

Test point 2 | Body ground

Is there continuity?

YES

Repair a short to ground in the SOL C wire between the shift solenoid valve O/P and the TCM.

NO

The SOL C wire is OK. Replace the shift solenoid valve O/P .

- Open wire check (SOL C/SHC+ line) -1. Disconnect the following connector. Shift solenoid valve O/P 2P connector -2. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode Shift solenoid valve O/P 2P connector: disconnected TCM 50P connector: disconnected Test point 1 Shift solenoid valve O/P 2P connector No. 1 Test point 2 TCM 50P connector No. 6 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The SOL C/SHC+ wire is OK. Replace the shift solenoid valve O/P . NO Repair an open in the SOL C/SHC+ wire between the shift solenoid valve O/P and the TCM.

-1. Disconnect the following connector.

Shift solenoid valve O/P 2P connector

-2. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

Shift solenoid valve O/P 2P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | Shift solenoid valve O/P 2P connector No. 1

Test point 2 | TCM 50P connector No. 6

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The SOL C/SHC+ wire is OK. Replace the shift solenoid valve O/P .

NO

Repair an open in the SOL C/SHC+ wire between the shift solenoid valve O/P and the TCM.
````

## Chunk 9920: DTC U0029 (K20C2 (CVT) with CAN gateway)

- Title: DTC U0029 (K20C2 (CVT) with CAN gateway)
- Source path: `pages\12487.html`
- Chunk ID: `chunk_f1fc4fe30010`
- Images: none
- Duplicate sources: `pages\15538.html`

### Full Text

````text
# DTC U0029 (K20C2 (CVT) with CAN gateway)

DTC U0029 : F-CAN Malfunction (F-CAN Bus OFF)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for CAN gateway system DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting in the CAN gateway system . NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting in the CAN gateway system .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 9921: DTC U0029 (K20C2 (CVT) without CAN gateway)

- Title: DTC U0029 (K20C2 (CVT) without CAN gateway)
- Source path: `pages\12488.html`
- Chunk ID: `chunk_cb6e31667469`
- Images: none
- Duplicate sources: `pages\15513.html`

### Full Text

````text
# DTC U0029 (K20C2 (CVT) without CAN gateway)

DTC U0029 : F-CAN Malfunction (F-CAN Bus OFF)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0029 F-CAN Malfunction (F-CAN Bus OFF) Is DTC U0029 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

Is DTC U0029 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9922: DTC U0029 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

- Title: DTC U0029 (L15B7/L15BA/L15BY (CVT) without CAN gateway)
- Source path: `pages\12489.html`
- Chunk ID: `chunk_1a05334b0608`
- Images: none
- Duplicate sources: `pages\15539.html`

### Full Text

````text
# DTC U0029 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

DTC U0029 : F-CAN Malfunction (F-CAN Bus OFF)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0029 F-CAN Malfunction (F-CAN Bus OFF) Is DTC U0029 indicated? YES The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

Is DTC U0029 indicated?

YES

The failure is duplicated. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals at the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.
````

## Chunk 9923: DTC U0029 (L15B7/L15BA/L15BY (CVT) with CAN gateway)

- Title: DTC U0029 (L15B7/L15BA/L15BY (CVT) with CAN gateway)
- Source path: `pages\12490.html`
- Chunk ID: `chunk_70d85e7d3047`
- Images: none
- Duplicate sources: `pages\15540.html`

### Full Text

````text
# DTC U0029 (L15B7/L15BA/L15BY (CVT) with CAN gateway)

DTC U0029 : F-CAN Malfunction (F-CAN Bus OFF)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0029 F-CAN Malfunction (F-CAN Bus OFF)

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Check for CAN gateway system DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the indicated DTC's troubleshooting in the CAN gateway system . NO Intermittent failure, the system is OK at this time.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the indicated DTC's troubleshooting in the CAN gateway system .

NO

Intermittent failure, the system is OK at this time.
````

## Chunk 9924: DTC U0038 (K20C2 (CVT))

- Title: DTC U0038 (K20C2 (CVT))
- Source path: `pages\12491.html`
- Chunk ID: `chunk_54a51c091891`
- Images: none
- Duplicate sources: `pages\15514.html`

### Full Text

````text
# DTC U0038 (K20C2 (CVT))

DTC U0038 : TM-CAN Malfunction (TCM-PCM)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0038 TM-CAN Malfunction (TCM-PCM)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs in the PGM-FI system with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0038 TM-CAN Malfunction (TCM-PCM) Is DTC U0038 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the PCM and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs in the PGM-FI system with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0038 TM-CAN Malfunction (TCM-PCM)

Is DTC U0038 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the PCM and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (TM-CAN_H line and TM-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. TCM 50P connector PCM connector A (50P) -4. Check for continuity between test points 1 and 2. TM-CAN_H line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 4 Test point 2 PCM connector A (50P) No. 21 TM-CAN_L line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 12 Test point 2 PCM connector A (50P) No. 20 Are there continuity? YES The TM-CAN_H wire and/or TM-CAN_L wire are not open. Go to step 3. NO Repair an open in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

TCM 50P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

TM-CAN_H line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 4

Test point 2 | PCM connector A (50P) No. 21

TM-CAN_L line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | PCM connector A (50P) No. 20

Are there continuity?

YES

The TM-CAN_H wire and/or TM-CAN_L wire are not open. Go to step 3.

NO

Repair an open in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM.

- Shorted wire check (TM-CAN_H line and TM-CAN_L line) -1. Check for continuity between test points 1 and 2. TM-CAN_H line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 4 Test point 2 Body ground TM-CAN_L line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 12 Test point 2 Body ground Are there continuity? YES Repair a short to ground in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM. NO The TM-CAN_H wire and/or TM-CAN_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

-1. Check for continuity between test points 1 and 2.

TM-CAN_H line
````

## Chunk 9925: DTC U0038 (K20C2 (CVT))

- Title: DTC U0038 (K20C2 (CVT))
- Source path: `pages\12491.html`
- Chunk ID: `chunk_48783c2d5a1e`
- Images: none
- Duplicate sources: `pages\12492.html`, `pages\15514.html`, `pages\15541.html`

### Full Text

````text
OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 4 Test point 2 Body ground TM-CAN_L line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 12 Test point 2 Body ground Are there continuity? YES Repair a short to ground in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM. NO The TM-CAN_H wire and/or TM-CAN_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

-1. Check for continuity between test points 1 and 2.

TM-CAN_H line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 4

Test point 2 | Body ground

TM-CAN_L line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | Body ground

Are there continuity?

YES

Repair a short to ground in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM.

NO

The TM-CAN_H wire and/or TM-CAN_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 9926: DTC U0038 (L15B7/L15BA/L15BY (CVT))

- Title: DTC U0038 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12492.html`
- Chunk ID: `chunk_3edd1f9e1bda`
- Images: none
- Duplicate sources: `pages\15541.html`

### Full Text

````text
# DTC U0038 (L15B7/L15BA/L15BY (CVT))

DTC U0038 : TM-CAN Malfunction (TCM-PCM)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0038 TM-CAN Malfunction (TCM-PCM)

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs in the PGM-FI system with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0038 TM-CAN Malfunction (TCM-PCM) Is DTC U0038 indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the PCM and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs in the PGM-FI system with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0038 TM-CAN Malfunction (TCM-PCM)

Is DTC U0038 indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the PCM and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (TM-CAN_H line and TM-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. TCM 50P connector PCM connector A (50P) -4. Check for continuity between test points 1 and 2. TM-CAN_H line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 4 Test point 2 PCM connector A (50P) No. 21 TM-CAN_L line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 12 Test point 2 PCM connector A (50P) No. 20 Are there continuity? YES The TM-CAN_H wire and/or TM-CAN_L wire are not open. Go to step 3. NO Repair an open in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

TCM 50P connector

PCM connector A (50P)

-4. Check for continuity between test points 1 and 2.

TM-CAN_H line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 4

Test point 2 | PCM connector A (50P) No. 21

TM-CAN_L line

Test condition | Vehicle OFF (LOCK) mode

TCM 50P connector: disconnected

PCM connector A (50P): disconnected

Test point 1 | TCM 50P connector No. 12

Test point 2 | PCM connector A (50P) No. 20

Are there continuity?

YES

The TM-CAN_H wire and/or TM-CAN_L wire are not open. Go to step 3.

NO

Repair an open in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM.

- Shorted wire check (TM-CAN_H line and TM-CAN_L line) -1. Check for continuity between test points 1 and 2. TM-CAN_H line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 4 Test point 2 Body ground TM-CAN_L line Test condition Vehicle OFF (LOCK) mode TCM 50P connector: disconnected PCM connector A (50P): disconnected Test point 1 TCM 50P connector No. 12 Test point 2 Body ground Are there continuity? YES Repair a short to ground in the TM-CAN_H wire and/or TM-CAN_L wire between the PCM and the TCM. NO The TM-CAN_H wire and/or TM-CAN_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

-1. Check for continuity between test points 1 and 2.

TM-CAN_H line
````

## Chunk 9927: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\12493.html`
- Chunk ID: `chunk_8834e366d761`
- Images: `images\GHH400075.jpeg`, `images\GHH400076.jpeg`, `images\GHH400077.jpeg`
- Duplicate sources: `pages\15542.html`

### Full Text

````text
# DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0151 : Lost Communication With SRS Unit

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0151 Lost Communication With SRS Unit

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Check for CAN gateway system DTCs with the HDS. DTC Description DTC U0029-00 CAN Gateway F-CAN ch A Bus Off U0047-00 CAN Gateway F-CAN ch B Bus Off U3000-49 CAN Gateway Internal Failure DTC (CAN GATEWAY) Is DTC U0029-00, U0047-00, and/or U3000-49 indicated? YES Go to the troubleshooting for CAN gateway system DTC(s) . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

U0029-00 CAN Gateway F-CAN ch A Bus Off

U0047-00 CAN Gateway F-CAN ch B Bus Off

U3000-49 CAN Gateway Internal Failure

DTC (CAN GATEWAY)

Is DTC U0029-00, U0047-00, and/or U3000-49 indicated?

YES

Go to the troubleshooting for CAN gateway system DTC(s) .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the TCM detect the CAN gateway Bus channels A? Bus A is Not Available Go to step 3. Bus A is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the TCM detect the CAN gateway Bus channels A?

Bus A is Not Available

Go to step 3.

Bus A is Available

Go to step 4.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector TCM 50P connector -3. Check for continuity between test points 1 and 2. F-CAN A_H line Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 12P connector No. 3 Test point 2 TCM 50P connector No. 3 F-CAN A_L line Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 12P connector No. 9 Test point 2 TCM 50P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the TCM and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 3

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 9

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK.
````

## Chunk 9928: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\12493.html`
- Chunk ID: `chunk_7e095c444761`
- Images: `images\GHH400075.jpeg`, `images\GHH400076.jpeg`, `images\GHH400077.jpeg`
- Duplicate sources: `pages\15542.html`

### Full Text

````text
or the F-CAN A_L wire between the TCM and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 3

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 9

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the TCM and the CAN gateway.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0100 PCM A, B U0122 VSA modulator-control unit A, B U0151 SRS unit B U0155 Gauge control module A Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100: PCM is Not Available for Bus A Go to step 5. U0100: PCM is Not Available for Bus B Go to step 6. U0122: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0151: SRS unit is Not Available for Bus B Go to step 6. U0155: Gauge control module is Not Available for Bus A Go to step 5.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0100 | PCM | A, B

U0122 | VSA modulator-control unit | A, B

U0151 | SRS unit | B

U0155 | Gauge control module | A

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100: PCM is Not Available for Bus A

Go to step 5.

U0100: PCM is Not Available for Bus B

Go to step 6.

U0122: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0151: SRS unit is Not Available for Bus B

Go to step 6.

U0155: Gauge control module is Not Available for Bus A

Go to step 5.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 12P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0155 Gauge control module connector A (32P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 12P connector No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 9 No. 36 U0122 F-CAN A_H CAN gateway 12P connector No. 3 VSA Modulator-Control Unit 46P connector No. 20 F-CAN A_L No. 9 No. 21 U0155 F-CAN A_H CAN gateway 12P connector No. 3 Gauge control module connector A (32P) No.
````

## Chunk 9929: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\12493.html`
- Chunk ID: `chunk_71b2e30aca36`
- Images: `images\GHH400075.jpeg`, `images\GHH400076.jpeg`, `images\GHH400077.jpeg`
- Duplicate sources: `pages\15542.html`

### Full Text

````text
tor - CAN gateway 12P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0155 Gauge control module connector A (32P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 12P connector No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 9 No. 36 U0122 F-CAN A_H CAN gateway 12P connector No. 3 VSA Modulator-Control Unit 46P connector No. 20 F-CAN A_L No. 9 No. 21 U0155 F-CAN A_H CAN gateway 12P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN A_L No. 9 No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . U0155 Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 12P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

U0155 | Gauge control module connector A (32P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN A_H | CAN gateway 12P connector | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 9 | No. 36

U0122 | F-CAN A_H | CAN gateway 12P connector | No. 3 | VSA Modulator-Control Unit 46P connector | No. 20

F-CAN A_L | No. 9 | No. 21

U0155 | F-CAN A_H | CAN gateway 12P connector | No. 3 | Gauge control module connector A (32P) | No. 19

F-CAN A_L | No. 9 | No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0155 | Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. -4.
````

## Chunk 9930: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\12493.html`
- Chunk ID: `chunk_6deda44edb74`
- Images: `images\GHH400075.jpeg`, `images\GHH400076.jpeg`, `images\GHH400077.jpeg`
- Duplicate sources: `pages\15542.html`

### Full Text

````text
ns or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0155 | Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. -4. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 12P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0151 SRS unit connector A (39P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 12P connector No. 12 PCM connector A (50P) No. 39 F-CAN B_L No. 5 No. 38 DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0122 F-CAN B_H CAN gateway 12P connector No. 12 VSA Modulator-Control Unit 46P connector No. 24 F-CAN B_L No. 5 No. 25 U0151 F-CAN B_H CAN gateway 12P connector No. 12 SRS unit connector A (39P) No. 34 F-CAN B_L No. 5 No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . U0151 Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Substitute a known-good SRS unit , then recheck. If this DTC goes away and the SRS unit was substituted, replace the original SRS unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

-4. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 12P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

U0151 | SRS unit connector A (39P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN B_H | CAN gateway 12P connector | No. 12 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 5 | No. 38

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0122 | F-CAN B_H | CAN gateway 12P connector | No. 12 | VSA Modulator-Control Unit 46P connector | No. 24

F-CAN B_L | No. 5 | No. 25

U0151 | F-CAN B_H | CAN gateway 12P connector | No. 12 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 5 | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN B_H wire and the F-CAN B_L wire are OK.
````

## Chunk 9931: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2016 2017 2018)
- Source path: `pages\12493.html`
- Chunk ID: `chunk_c167ad4992c2`
- Images: `images\GHH400075.jpeg`, `images\GHH400076.jpeg`, `images\GHH400077.jpeg`
- Duplicate sources: `pages\15542.html`

### Full Text

````text
DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN B_H | CAN gateway 12P connector | No. 12 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 5 | No. 38

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0122 | F-CAN B_H | CAN gateway 12P connector | No. 12 | VSA Modulator-Control Unit 46P connector | No. 24

F-CAN B_L | No. 5 | No. 25

U0151 | F-CAN B_H | CAN gateway 12P connector | No. 12 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 5 | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0151 | Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Substitute a known-good SRS unit , then recheck. If this DTC goes away and the SRS unit was substituted, replace the original SRS unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.
````

## Chunk 9932: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)
- Source path: `pages\12494.html`
- Chunk ID: `chunk_5127facd9f88`
- Images: `images\GHH400078.png`, `images\GHH400079.png`, `images\GHH400080.jpeg`, `images\GHH400081.png`, `images\GHH400082.png`, `images\GHH400083.jpeg`, `images\GHH400084.png`, `images\GHH400085.png`, `images\GHH400086.png`, `images\GHH400087.jpeg`, `images\GHH400088.png`, `images\GHH400089.png`, `images\GHH400090.jpeg`
- Duplicate sources: `pages\15543.html`

### Full Text

````text
# DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0151 : Lost Communication With SRS Unit

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0151 Lost Communication With SRS Unit

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Check for CAN gateway system DTCs with the HDS. DTC Description DTC DTC (CAN GATEWAY) Are any DTCs indicated? YES Go to the troubleshooting for CAN gateway system DTC(s) . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

DTC (CAN GATEWAY)

Are any DTCs indicated?

YES

Go to the troubleshooting for CAN gateway system DTC(s) .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the TCM detect the CAN gateway Bus channels A? Bus A is Not Available Go to step 3. Bus A is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the TCM detect the CAN gateway Bus channels A?

Bus A is Not Available

Go to step 3.

Bus A is Available

Go to step 4.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CAN gateway 16P connector TCM 50P connector -3. Check for continuity between test points 1 and 2 individually. F-CAN A_H line Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 3: Test point 2 TCM 50P connector No. 3 F-CAN A_L line Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 11: Test point 2 TCM 50P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CAN gateway 16P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2 individually.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM.
````

## Chunk 9933: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)
- Source path: `pages\12494.html`
- Chunk ID: `chunk_c7054713765f`
- Images: `images\GHH400078.png`, `images\GHH400079.png`, `images\GHH400080.jpeg`, `images\GHH400081.png`, `images\GHH400082.png`, `images\GHH400083.jpeg`, `images\GHH400084.png`, `images\GHH400085.png`, `images\GHH400086.png`, `images\GHH400087.jpeg`, `images\GHH400088.png`, `images\GHH400089.png`, `images\GHH400090.jpeg`
- Duplicate sources: `pages\15543.html`

### Full Text

````text
wing connector.

CAN gateway 16P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2 individually.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0100 PCM A, B U0122 VSA modulator-control unit A, B U0151 SRS unit B U0155 Gauge control module C Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100: PCM is Not Available for Bus A Go to step 5. U0100: PCM is Not Available for Bus B Go to step 6. U0122: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0151: SRS unit is Not Available for Bus B Go to step 6. U0155: Gauge control module is Not Available for Bus C Go to step 7.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0100 | PCM | A, B

U0122 | VSA modulator-control unit | A, B

U0151 | SRS unit | B

U0155 | Gauge control module | C

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100: PCM is Not Available for Bus A

Go to step 5.

U0100: PCM is Not Available for Bus B

Go to step 6.

U0122: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0151: SRS unit is Not Available for Bus B

Go to step 6.

U0155: Gauge control module is Not Available for Bus C

Go to step 7.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 11 No. 36 U0122 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 VSA Modulator-Control Unit 46P connector No. 20 F-CAN A_L No. 11 No. 21 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK.
````

## Chunk 9934: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)
- Source path: `pages\12494.html`
- Chunk ID: `chunk_27539f9fc740`
- Images: `images\GHH400078.png`, `images\GHH400079.png`, `images\GHH400080.jpeg`, `images\GHH400081.png`, `images\GHH400082.png`, `images\GHH400083.jpeg`, `images\GHH400084.png`, `images\GHH400085.png`, `images\GHH400086.png`, `images\GHH400087.jpeg`, `images\GHH400088.png`, `images\GHH400089.png`, `images\GHH400090.jpeg`
- Duplicate sources: `pages\15543.html`

### Full Text

````text
eway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 11 No. 36 U0122 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 VSA Modulator-Control Unit 46P connector No. 20 F-CAN A_L No. 11 No. 21 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 16P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 11 | No. 36

U0122 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | VSA Modulator-Control Unit 46P connector | No. 20

F-CAN A_L | No. 11 | No. 21

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. -4. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0151 SRS unit connector A (39P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122 F-CAN B_H CAN gateway 16P connector (female terminals): No.
````

## Chunk 9935: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)
- Source path: `pages\12494.html`
- Chunk ID: `chunk_c2e279354ed4`
- Images: `images\GHH400078.png`, `images\GHH400079.png`, `images\GHH400080.jpeg`, `images\GHH400081.png`, `images\GHH400082.png`, `images\GHH400083.jpeg`, `images\GHH400084.png`, `images\GHH400085.png`, `images\GHH400086.png`, `images\GHH400087.jpeg`, `images\GHH400088.png`, `images\GHH400089.png`, `images\GHH400090.jpeg`
- Duplicate sources: `pages\15543.html`

### Full Text

````text
3 minutes. -4. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0151 SRS unit connector A (39P) -5. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA Modulator-Control Unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 U0151 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 SRS unit connector A (39P) No. 34 F-CAN B_L No. 14 No. 35 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . U0151 Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Substitute a known-good SRS unit , then recheck. If this DTC goes away and the SRS unit was substituted, replace the original SRS unit . NO Repair an open in the F-CAN B_H wire and/or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

-4. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 16P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

U0151 | SRS unit connector A (39P)

-5. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0122 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | VSA Modulator-Control Unit 46P connector | No. 24

F-CAN B_L | No. 14 | No. 25

U0151 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | SRS unit connector A (39P) | No. 34

F-CAN B_L | No. 14 | No. 35

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0151 | Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Substitute a known-good SRS unit , then recheck. If this DTC goes away and the SRS unit was substituted, replace the original SRS unit .

NO

Repair an open in the F-CAN B_H wire and/or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.
````

## Chunk 9936: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2 (CVT) with CAN gateway) (2019 2020 2021)
- Source path: `pages\12494.html`
- Chunk ID: `chunk_e4243e06821d`
- Images: `images\GHH400078.png`, `images\GHH400079.png`, `images\GHH400080.jpeg`, `images\GHH400081.png`, `images\GHH400082.png`, `images\GHH400083.jpeg`, `images\GHH400084.png`, `images\GHH400085.png`, `images\GHH400086.png`, `images\GHH400087.jpeg`, `images\GHH400088.png`, `images\GHH400089.png`, `images\GHH400090.jpeg`
- Duplicate sources: `pages\15543.html`

### Full Text

````text
replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0151 | Check for poor connections or loose terminals at the CAN gateway and the SRS unit. Substitute a known-good SRS unit , then recheck. If this DTC goes away and the SRS unit was substituted, replace the original SRS unit .

NO

Repair an open in the F-CAN B_H wire and/or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN C_H line, F-CAN C_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 5: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 16P connector (female terminals) No. 13: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN C_H wire and the F-CAN C_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire and/or the F-CAN C_L wire between the gauge control module and the CAN gateway.

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

The F-CAN C_H wire and the F-CAN C_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN C_H wire and/or the F-CAN C_L wire between the gauge control module and the CAN gateway.
````

## Chunk 9937: DTC U0100, U0122, U0151, U0155 (K20C2, CVT model without CAN gateway)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2, CVT model without CAN gateway)
- Source path: `pages\12495.html`
- Chunk ID: `chunk_b29e2eabd169`
- Images: none
- Duplicate sources: `pages\15515.html`

### Full Text

````text
# DTC U0100, U0122, U0151, U0155 (K20C2, CVT model without CAN gateway)

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0151 : Lost Communication With SRS Unit

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

- Before disconnecting the SRS unit connector, do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0151 Lost Communication With SRS Unit

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0100 F-CAN Malfunction (TCM - FI Control Module) U0122 Lost Communication With Vehicle Dynamics Control Module U0151 Lost Communication With SRS Unit U0155 Lost Communication With Gauge Control Module Are any DTCs indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmitting control units and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0151 Lost Communication With SRS Unit

U0155 Lost Communication With Gauge Control Module

Are any DTCs indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmitting control units and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (F-CAN_H line, F-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes. -4. Disconnect the following connectors. TCM 50P connector DTC U0100: PCM connector A (50P) DTC U0122: VSA modulator-control unit 46P connector DTC U0151: SRS unit connector A (39P) DTC U0155: Gauge control module connector A (32P) -5. Check for continuity between the receiving control unit and the transmitting control unit on the F-CAN_H circuit and the F-CAN_L circuit. DTC Circuit name Receiving control unit Transmitting control unit U0100 F-CAN_H TCM 50P connector No. 3 PCM connector A (50P) No. 37 F-CAN_L TCM 50P connector No. 11 PCM connector A (50P) No. 36 U0122 F-CAN_H TCM 50P connector No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN_L TCM 50P connector No. 11 VSA modulator-control unit 46P connector No. 21 U0151 F-CAN_H TCM 50P connector No. 3 SRS unit connector A (39P) No. 34 F-CAN_L TCM 50P connector No. 11 SRS unit connector A (39P) No. 35 DTC Circuit name Receiving control unit Transmitting control unit U0155 F-CAN_H TCM 50P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN_L TCM 50P connector No. 11 Gauge control module connector A (32P) No. 20 Is there continuity? YES The F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table).
````

## Chunk 9938: DTC U0100, U0122, U0151, U0155 (K20C2, CVT model without CAN gateway)

- Title: DTC U0100, U0122, U0151, U0155 (K20C2, CVT model without CAN gateway)
- Source path: `pages\12495.html`
- Chunk ID: `chunk_70c96751755f`
- Images: none
- Duplicate sources: `pages\15515.html`

### Full Text

````text
t U0100 F-CAN_H TCM 50P connector No. 3 PCM connector A (50P) No. 37 F-CAN_L TCM 50P connector No. 11 PCM connector A (50P) No. 36 U0122 F-CAN_H TCM 50P connector No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN_L TCM 50P connector No. 11 VSA modulator-control unit 46P connector No. 21 U0151 F-CAN_H TCM 50P connector No. 3 SRS unit connector A (39P) No. 34 F-CAN_L TCM 50P connector No. 11 SRS unit connector A (39P) No. 35 DTC Circuit name Receiving control unit Transmitting control unit U0155 F-CAN_H TCM 50P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN_L TCM 50P connector No. 11 Gauge control module connector A (32P) No. 20 Is there continuity? YES The F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table). DTC Transmitting control unit Procedure U0100 PCM Replace the PCM U0122 VSA modulator-control unit Replace the VSA modulator-control unit U0151 SRS unit Replace the SRS unit U0155 Gauge control module Replace the gauge control module NO Repair an open in the F-CAN_H wire and/or F-CAN_L wire between the receiving control unit and the transmitting control unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. DTC U0151: Do the 12 volt battery terminal disconnection procedure , and wait for at least 3 minutes.

-4. Disconnect the following connectors.

TCM 50P connector

DTC U0100: PCM connector A (50P)

DTC U0122: VSA modulator-control unit 46P connector

DTC U0151: SRS unit connector A (39P)

DTC U0155: Gauge control module connector A (32P)

-5. Check for continuity between the receiving control unit and the transmitting control unit on the F-CAN_H circuit and the F-CAN_L circuit.

DTC | Circuit name | Receiving control unit | Transmitting control unit

U0100 | F-CAN_H | TCM 50P connector No. 3 | PCM connector A (50P) No. 37

F-CAN_L | TCM 50P connector No. 11 | PCM connector A (50P) No. 36

U0122 | F-CAN_H | TCM 50P connector No. 3 | VSA modulator-control unit 46P connector No. 20

F-CAN_L | TCM 50P connector No. 11 | VSA modulator-control unit 46P connector No. 21

U0151 | F-CAN_H | TCM 50P connector No. 3 | SRS unit connector A (39P) No. 34

F-CAN_L | TCM 50P connector No. 11 | SRS unit connector A (39P) No. 35

DTC | Circuit name | Receiving control unit | Transmitting control unit

U0155 | F-CAN_H | TCM 50P connector No. 3 | Gauge control module connector A (32P) No. 19

F-CAN_L | TCM 50P connector No. 11 | Gauge control module connector A (32P) No. 20

Is there continuity?

YES

The F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table).

DTC | Transmitting control unit | Procedure

U0100 | PCM | Replace the PCM

U0122 | VSA modulator-control unit | Replace the VSA modulator-control unit

U0151 | SRS unit | Replace the SRS unit

U0155 | Gauge control module | Replace the gauge control module

NO

Repair an open in the F-CAN_H wire and/or F-CAN_L wire between the receiving control unit and the transmitting control unit.
````

## Chunk 9939: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT) without CAN gateway)
- Source path: `pages\12496.html`
- Chunk ID: `chunk_c4e8a4fb9eda`
- Images: none
- Duplicate sources: `pages\15544.html`

### Full Text

````text
# DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- Problem verification -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Turn the vehicle to the OFF (LOCK) mode. -4. Turn the vehicle to the ON mode. -5. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0100 F-CAN Malfunction (TCM - FI Control Module) U0122 Lost Communication With Vehicle Dynamics Control Module U0155 Lost Communication With Gauge Control Module Are any DTCs indicated? YES The failure is duplicated. Go to step 2. NO Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmitting control units and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Turn the vehicle to the OFF (LOCK) mode.

-4. Turn the vehicle to the ON mode.

-5. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0155 Lost Communication With Gauge Control Module

Are any DTCs indicated?

YES

The failure is duplicated. Go to step 2.

NO

Intermittent failure, the system is OK at this time. Check for poor connections and loose terminals between the transmitting control units and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (F-CAN_H line, F-CAN_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. Disconnect the following connectors. TCM 50P connector DTC U0100: PCM connector A (50P) DTC U0122: VSA modulator-control unit 46P connector DTC U0155: Gauge control module connector A (32P) -4. Check for continuity between the receiving control unit and the transmitting control unit on the F-CAN_H circuit and the F-CAN_L circuit. DTC Circuit name Receiving control unit Transmitting control unit U0100 F-CAN_H TCM 50P connector No. 3 PCM connector A (50P) No. 37 F-CAN_L TCM 50P connector No. 11 PCM connector A (50P) No. 36 U0122 F-CAN_H TCM 50P connector No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN_L TCM 50P connector No. 11 VSA modulator-control unit 46P connector No. 21 U0155 F-CAN_H TCM 50P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN_L TCM 50P connector No. 11 Gauge control module connector A (32P) No. 20 Is there continuity? YES The F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table). DTC Transmitting control unit Procedure U0100 PCM Replace the PCM U0122 VSA Modulator-Control Unit Replace the VSA modulator-control unit DTC Transmitting control unit Procedure U0155 Gauge control module Replace the gauge control module NO Repair an open in the F-CAN_H wire and/or F-CAN_L wire between the receiving control unit and the transmitting control unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

TCM 50P connector

DTC U0100: PCM connector A (50P)

DTC U0122: VSA modulator-control unit 46P connector

DTC U0155: Gauge control module connector A (32P)

-4.
````

## Chunk 9940: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT) without CAN gateway)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT) without CAN gateway)
- Source path: `pages\12496.html`
- Chunk ID: `chunk_4f27c6daabfb`
- Images: none
- Duplicate sources: `pages\15544.html`

### Full Text

````text
e F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table). DTC Transmitting control unit Procedure U0100 PCM Replace the PCM U0122 VSA Modulator-Control Unit Replace the VSA modulator-control unit DTC Transmitting control unit Procedure U0155 Gauge control module Replace the gauge control module NO Repair an open in the F-CAN_H wire and/or F-CAN_L wire between the receiving control unit and the transmitting control unit.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. DTC U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. Disconnect the following connectors.

TCM 50P connector

DTC U0100: PCM connector A (50P)

DTC U0122: VSA modulator-control unit 46P connector

DTC U0155: Gauge control module connector A (32P)

-4. Check for continuity between the receiving control unit and the transmitting control unit on the F-CAN_H circuit and the F-CAN_L circuit.

DTC | Circuit name | Receiving control unit | Transmitting control unit

U0100 | F-CAN_H | TCM 50P connector No. 3 | PCM connector A (50P) No. 37

F-CAN_L | TCM 50P connector No. 11 | PCM connector A (50P) No. 36

U0122 | F-CAN_H | TCM 50P connector No. 3 | VSA modulator-control unit 46P connector No. 20

F-CAN_L | TCM 50P connector No. 11 | VSA modulator-control unit 46P connector No. 21

U0155 | F-CAN_H | TCM 50P connector No. 3 | Gauge control module connector A (32P) No. 19

F-CAN_L | TCM 50P connector No. 11 | Gauge control module connector A (32P) No. 20

Is there continuity?

YES

The F-CAN_H wire and the F-CAN_L wire are OK. Replace the control unit based on the instructions (see table).

DTC | Transmitting control unit | Procedure

U0100 | PCM | Replace the PCM

U0122 | VSA Modulator-Control Unit | Replace the VSA modulator-control unit

DTC | Transmitting control unit | Procedure

U0155 | Gauge control module | Replace the gauge control module

NO

Repair an open in the F-CAN_H wire and/or F-CAN_L wire between the receiving control unit and the transmitting control unit.
````

## Chunk 9941: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))
- Source path: `pages\12497.html`
- Chunk ID: `chunk_5d82ba63c95a`
- Images: `images\GHH400091.jpeg`, `images\GHH400092.jpeg`, `images\GHH400093.jpeg`
- Duplicate sources: `pages\15545.html`

### Full Text

````text
# DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Check for CAN gateway system DTCs with the HDS. DTC Description DTC U0029-00 CAN Gateway F-CAN ch A Bus Off U0047-00 CAN Gateway F-CAN ch B Bus Off U3000-49 CAN Gateway Internal Failure DTC (CAN GATEWAY) Is DTC U0029-00, U0047-00, and/or U3000-49 indicated? YES Go to the troubleshooting for CAN gateway system DTC(s) . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

U0029-00 CAN Gateway F-CAN ch A Bus Off

U0047-00 CAN Gateway F-CAN ch B Bus Off

U3000-49 CAN Gateway Internal Failure

DTC (CAN GATEWAY)

Is DTC U0029-00, U0047-00, and/or U3000-49 indicated?

YES

Go to the troubleshooting for CAN gateway system DTC(s) .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the TCM detect the CAN gateway Bus channels A? Bus A is Not Available Go to step 3. Bus A is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the TCM detect the CAN gateway Bus channels A?

Bus A is Not Available

Go to step 3.

Bus A is Available

Go to step 4.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 12P connector TCM 50P connector -3. Check for continuity between test points 1 and 2. F-CAN A_H line Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 12P connector No. 3 Test point 2 TCM 50P connector No. 3 F-CAN A_L line Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 12P connector No. 9 Test point 2 TCM 50P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the TCM and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 3

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 9

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM.
````

## Chunk 9942: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))
- Source path: `pages\12497.html`
- Chunk ID: `chunk_9988c70757d0`
- Images: `images\GHH400091.jpeg`, `images\GHH400092.jpeg`, `images\GHH400093.jpeg`
- Duplicate sources: `pages\15545.html`

### Full Text

````text
cle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 12P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 3

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 12P connector No. 9

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the TCM and the CAN gateway.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0100 PCM A, B U0122 VSA modulator-control unit A, B DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0155 Gauge control module A Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100: PCM is Not Available for Bus A Go to step 5. U0100: PCM is Not Available for Bus B Go to step 6. U0122: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0155: Gauge control module is Not Available for Bus A Go to step 5.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0100 | PCM | A, B

U0122 | VSA modulator-control unit | A, B

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0155 | Gauge control module | A

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100: PCM is Not Available for Bus A

Go to step 5.

U0100: PCM is Not Available for Bus B

Go to step 6.

U0122: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0155: Gauge control module is Not Available for Bus A

Go to step 5.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 12P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector U0155 Gauge control module connector A (32P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 12P connector No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 9 No. 36 U0122 F-CAN A_H CAN gateway 12P connector No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 9 No. 21 U0155 F-CAN A_H CAN gateway 12P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN A_L No. 9 No. 20 Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9943: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))
- Source path: `pages\12497.html`
- Chunk ID: `chunk_cf02137192fd`
- Images: `images\GHH400091.jpeg`, `images\GHH400092.jpeg`, `images\GHH400093.jpeg`
- Duplicate sources: `pages\15545.html`

### Full Text

````text
) U0122 VSA modulator-control unit 46P connector U0155 Gauge control module connector A (32P) -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 12P connector No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 9 No. 36 U0122 F-CAN A_H CAN gateway 12P connector No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 9 No. 21 U0155 F-CAN A_H CAN gateway 12P connector No. 3 Gauge control module connector A (32P) No. 19 F-CAN A_L No. 9 No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . U0155 Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module . NO Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 12P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

U0155 | Gauge control module connector A (32P)

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN A_H | CAN gateway 12P connector | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 9 | No. 36

U0122 | F-CAN A_H | CAN gateway 12P connector | No. 3 | VSA modulator-control unit 46P connector | No. 20

F-CAN A_L | No. 9 | No. 21

U0155 | F-CAN A_H | CAN gateway 12P connector | No. 3 | Gauge control module connector A (32P) | No. 19

F-CAN A_L | No. 9 | No. 20

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0155 | Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).
````

## Chunk 9944: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (12P connector type))
- Source path: `pages\12497.html`
- Chunk ID: `chunk_6789030db41d`
- Images: `images\GHH400091.jpeg`, `images\GHH400092.jpeg`, `images\GHH400093.jpeg`
- Duplicate sources: `pages\15545.html`

### Full Text

````text
ons or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

U0155 | Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN A_H wire or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 12P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 12P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 12P connector No. 12 PCM connector A (50P) No. 39 F-CAN B_L No. 5 No. 38 U0122 F-CAN B_H CAN gateway 12P connector No. 12 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 5 No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . NO Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 12P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 12P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN B_H | CAN gateway 12P connector | No. 12 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 5 | No. 38

U0122 | F-CAN B_H | CAN gateway 12P connector | No. 12 | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 5 | No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

NO

Repair an open in the F-CAN B_H wire or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.
````

## Chunk 9945: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\12498.html`
- Chunk ID: `chunk_c9aaf8076ccf`
- Images: `images\GHH400094.png`, `images\GHH400095.png`, `images\GHH400096.jpeg`, `images\GHH400097.png`, `images\GHH400098.png`, `images\GHH400099.jpeg`, `images\GHH400100.png`, `images\GHH400101.png`, `images\GHH400102.jpeg`, `images\GHH400103.png`, `images\GHH400104.png`, `images\GHH400105.jpeg`
- Duplicate sources: `pages\15546.html`

### Full Text

````text
# DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

DTC U0100 : F-CAN Malfunction (TCM - FI Control Module)

DTC U0122 : Lost Communication With Vehicle Dynamics Control Module

DTC U0155 : Lost Communication With Gauge Control Module

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- Refer to the DTC shown on the display, then inspect the connectors and terminals based on the instructions.

- According to the detected DTC(s), check for the power circuit and the ground circuit of the control unit which cannot communicate with the TCM.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0100 F-CAN Malfunction (TCM - FI Control Module)

U0122 Lost Communication With Vehicle Dynamics Control Module

U0155 Lost Communication With Gauge Control Module

DTC (CVT)

- CAN gateway system DTC check -1. Turn the vehicle to the ON mode. -2. Check for CAN gateway system DTCs with the HDS. DTC Description DTC DTC (CAN GATEWAY) Are any DTCs indicated? YES Go to the troubleshooting for CAN gateway system DTC(s) . NO Go to step 2.

-1. Turn the vehicle to the ON mode.

-2. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

DTC (CAN GATEWAY)

Are any DTCs indicated?

YES

Go to the troubleshooting for CAN gateway system DTC(s) .

NO

Go to step 2.

- F-CAN circuit communication check (Receiving control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Does the TCM detect the CAN gateway Bus channels A? Bus A is Not Available Go to step 3. Bus A is Available Go to step 4.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Does the TCM detect the CAN gateway Bus channels A?

Bus A is Not Available

Go to step 3.

Bus A is Available

Go to step 4.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connector. CAN gateway 16P connector TCM 50P connector -3. Check for continuity between test points 1 and 2 individually. F-CAN A_H line Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 3: Test point 2 TCM 50P connector No. 3 F-CAN A_L line Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM 50P connector: disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 11: Test point 2 TCM 50P connector No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connector.

CAN gateway 16P connector

TCM 50P connector

-3. Check for continuity between test points 1 and 2 individually.

F-CAN A_H line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM .

NO
````

## Chunk 9946: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\12498.html`
- Chunk ID: `chunk_51c345e333df`
- Images: `images\GHH400094.png`, `images\GHH400095.png`, `images\GHH400096.jpeg`, `images\GHH400097.png`, `images\GHH400098.png`, `images\GHH400099.jpeg`, `images\GHH400100.png`, `images\GHH400101.png`, `images\GHH400102.jpeg`, `images\GHH400103.png`, `images\GHH400104.png`, `images\GHH400105.jpeg`
- Duplicate sources: `pages\15546.html`

### Full Text

````text
connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM 50P connector No. 3

F-CAN A_L line

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM 50P connector: disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM 50P connector No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If indicated DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

- F-CAN circuit communication check (Transmitting control unit) -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally. DTC Transmitting control unit Detected CAN getaway Bus channel(s) at normal U0100 PCM A, B U0122 VSA modulator-control unit A, B U0155 Gauge control module C Is it detected normally? Detected normal Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway. U0100: PCM is Not Available for Bus A Go to step 5. U0100: PCM is Not Available for Bus B Go to step 6. U0122: VSA modulator-control unit is Not Available for Bus A Go to step 5. U0122: VSA modulator-control unit is Not Available for Bus B Go to step 6. U0155: Gauge control module is Not Available for Bus C Go to step 7.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

According to the detected DTC on the following table, make sure that the transmitting control unit detects the CAN gateway Bus channel(s) normally.

DTC | Transmitting control unit | Detected CAN getaway Bus channel(s) at normal

U0100 | PCM | A, B

U0122 | VSA modulator-control unit | A, B

U0155 | Gauge control module | C

Is it detected normally?

Detected normal

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the transmitting control unit and the CAN gateway.

U0100: PCM is Not Available for Bus A

Go to step 5.

U0100: PCM is Not Available for Bus B

Go to step 6.

U0122: VSA modulator-control unit is Not Available for Bus A

Go to step 5.

U0122: VSA modulator-control unit is Not Available for Bus B

Go to step 6.

U0155: Gauge control module is Not Available for Bus C

Go to step 7.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 11 No. 36 U0122 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 11 No. 21 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .
````

## Chunk 9947: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\12498.html`
- Chunk ID: `chunk_8daac5c8a2d8`
- Images: `images\GHH400094.png`, `images\GHH400095.png`, `images\GHH400096.jpeg`, `images\GHH400097.png`, `images\GHH400098.png`, `images\GHH400099.jpeg`, `images\GHH400100.png`, `images\GHH400101.png`, `images\GHH400102.jpeg`, `images\GHH400103.png`, `images\GHH400104.png`, `images\GHH400105.jpeg`
- Duplicate sources: `pages\15546.html`

### Full Text

````text
way 16P connector (female terminals): No. 3 PCM connector A (50P) No. 37 F-CAN A_L No. 11 No. 36 U0122 F-CAN A_H CAN gateway 16P connector (female terminals): No. 3 VSA modulator-control unit 46P connector No. 20 F-CAN A_L No. 11 No. 21 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 16P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | PCM connector A (50P) | No. 37

F-CAN A_L | No. 11 | No. 36

U0122 | F-CAN A_H | CAN gateway 16P connector (female terminals): | No. 3 | VSA modulator-control unit 46P connector | No. 20

F-CAN A_L | No. 11 | No. 21

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN B_H line, F-CAN B_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute. -3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s). DTC Connector - CAN gateway 16P connector U0100 PCM connector A (50P) U0122 VSA modulator-control unit 46P connector -4. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Transmitting control unit connector(s) for indicated DTCs: disconnected DTC Circuit name Test point 1 (Receiving control unit) Test point 2 (Transmitting control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck.
````

## Chunk 9948: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\12498.html`
- Chunk ID: `chunk_6ea0485e8468`
- Images: `images\GHH400094.png`, `images\GHH400095.png`, `images\GHH400096.jpeg`, `images\GHH400097.png`, `images\GHH400098.png`, `images\GHH400099.jpeg`, `images\GHH400100.png`, `images\GHH400101.png`, `images\GHH400102.jpeg`, `images\GHH400103.png`, `images\GHH400104.png`, `images\GHH400105.jpeg`
- Duplicate sources: `pages\15546.html`

### Full Text

````text
g control unit) Connector Terminal Connector Terminal U0100 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 PCM connector A (50P) No. 39 F-CAN B_L No. 14 No. 38 U0122 F-CAN B_H CAN gateway 16P connector (female terminals): No. 6 VSA modulator-control unit 46P connector No. 24 F-CAN B_L No. 14 No. 25 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit. DTC Operation for transmitting control unit U0100 Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM . DTC Operation for transmitting control unit U0122 Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit . NO Repair an open in the F-CAN B_H wire and/or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. U0100: Jump the SCS line with the HDS, and wait more than 1 minute.

-3. According to the detected DTC on the following table, disconnect the transmitting control unit connector(s).

DTC | Connector

- | CAN gateway 16P connector

U0100 | PCM connector A (50P)

U0122 | VSA modulator-control unit 46P connector

-4. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

Transmitting control unit connector(s) for indicated DTCs: disconnected

DTC | Circuit name | Test point 1 (Receiving control unit) | Test point 2 (Transmitting control unit)

Connector | Terminal | Connector | Terminal

U0100 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | PCM connector A (50P) | No. 39

F-CAN B_L | No. 14 | No. 38

U0122 | F-CAN B_H | CAN gateway 16P connector (female terminals): | No. 6 | VSA modulator-control unit 46P connector | No. 24

F-CAN B_L | No. 14 | No. 25

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN B_H wire and the F-CAN B_L wire are OK. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting. According to the detected DTC on the following table, substitute or replace the correspond control unit.

DTC | Operation for transmitting control unit

U0100 | Check for poor connections or loose terminals at the CAN gateway and the PCM. Substitute a known-good PCM , then recheck. If this DTC goes away and the PCM was substituted, replace the original PCM .

DTC | Operation for transmitting control unit

U0122 | Check for poor connections or loose terminals at the CAN gateway and the VSA modulator-control unit. Replace the VSA modulator-control unit .

NO

Repair an open in the F-CAN B_H wire and/or the F-CAN B_L wire between the transmitting control unit and the CAN gateway.

- Open wire check (F-CAN C_H line, F-CAN C_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector Gauge control module connector A (32P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected Gauge control module connector A (32P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 5: Test point 2 Gauge control module connector A (32P) No. 19 Test point 1 CAN gateway 16P connector (female terminals) No. 13: Test point 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN C_H wire and the F-CAN C_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire and/or the F-CAN C_L wire between the gauge control module and the CAN gateway.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

Gauge control module connector A (32P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode
````

## Chunk 9949: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)

- Title: DTC U0100, U0122, U0155 (L15B7/L15BA/L15BY (CVT): With CAN Gateway (16P connector type)) (2019 2020 2021)
- Source path: `pages\12498.html`
- Chunk ID: `chunk_88a9c3cc1ba3`
- Images: `images\GHH400094.png`, `images\GHH400095.png`, `images\GHH400096.jpeg`, `images\GHH400097.png`, `images\GHH400098.png`, `images\GHH400099.jpeg`, `images\GHH400100.png`, `images\GHH400101.png`, `images\GHH400102.jpeg`, `images\GHH400103.png`, `images\GHH400104.png`, `images\GHH400105.jpeg`
- Duplicate sources: `pages\15546.html`

### Full Text

````text
oint 2 Gauge control module connector A (32P) No. 20 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN C_H wire and the F-CAN C_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module . NO Repair an open in the F-CAN C_H wire and/or the F-CAN C_L wire between the gauge control module and the CAN gateway.

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

The F-CAN C_H wire and the F-CAN C_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the gauge control module. Substitute a known-good gauge control module , then recheck. If this DTC goes away and the gauge control module was substituted, replace the original gauge control module .

NO

Repair an open in the F-CAN C_H wire and/or the F-CAN C_L wire between the gauge control module and the CAN gateway.
````

## Chunk 9950: DTC U0146 (K20C2 (CVT)) (2019 2020 2021)

- Title: DTC U0146 (K20C2 (CVT)) (2019 2020 2021)
- Source path: `pages\12499.html`
- Chunk ID: `chunk_4ec0c709edc7`
- Images: `images\GHH400106.png`, `images\GHH400107.png`, `images\GHH400108.jpeg`
- Duplicate sources: `pages\15516.html`

### Full Text

````text
# DTC U0146 (K20C2 (CVT)) (2019 2020 2021)

DTC U0146 : F-CAN Malfunction (TCM-CAN Gateway)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- According to the detected DTC(s), check for the power circuit of the CAN gateway.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0146 F-CAN Malfunction (TCM-CAN Gateway)

DTC (CVT)

- CAN gateway system DTC check -1. Check for CAN gateway system DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the troubleshooting for CAN gateway DTC(s). NO Go to step 2.

-1. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the troubleshooting for CAN gateway DTC(s).

NO

Go to step 2.

- F-CAN circuit communication check -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? TCM (Bus A) is Not Available Go to step 3. TCM is Detected Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CAN gateway and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Which result is indicated?

TCM (Bus A) is Not Available

Go to step 3.

TCM is Detected

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CAN gateway and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector TCM connector (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM connector (50P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 3: Test point 2 TCM connector (50P) No. 3 Test point 1 CAN gateway 16P connector (female terminals) No. 11: Test point 2 TCM connector (50P) No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

TCM connector (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM connector (50P): disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM connector (50P) No. 3

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM connector (50P) No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.
````

## Chunk 9951: DTC U0146 (L15B7/L15BA/L15BY (CVT)) (2019 2020 2021)

- Title: DTC U0146 (L15B7/L15BA/L15BY (CVT)) (2019 2020 2021)
- Source path: `pages\12500.html`
- Chunk ID: `chunk_92124abfd344`
- Images: `images\GHH400109.png`, `images\GHH400110.png`, `images\GHH400111.jpeg`
- Duplicate sources: `pages\15547.html`

### Full Text

````text
# DTC U0146 (L15B7/L15BA/L15BY (CVT)) (2019 2020 2021)

DTC U0146 : F-CAN Malfunction (TCM-CAN Gateway)

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This code is caused by an electrical circuit problem and cannot be caused by a mechanical problem in the transmission.

- According to the detected DTC(s), check for the power circuit of the CAN gateway.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0146 F-CAN Malfunction (TCM-CAN Gateway)

DTC (CVT)

- CAN gateway system DTC check -1. Check for CAN gateway system DTCs with the HDS. DTC Description DTC Are any DTCs indicated? YES Go to the troubleshooting for CAN gateway DTC(s). NO Go to step 2.

-1. Check for CAN gateway system DTCs with the HDS.

DTC Description | DTC

Are any DTCs indicated?

YES

Go to the troubleshooting for CAN gateway DTC(s).

NO

Go to step 2.

- F-CAN circuit communication check -1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check. F-CAN Bus Connected Unit Check Which result is indicated? TCM (Bus A) is Not Available Go to step 3. TCM is Detected Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CAN gateway and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

-1. Select the FUNCTION TEST in the CAN gateway with the HDS, then select the F-CAN Bus Connected Unit Check.

F-CAN Bus Connected Unit Check

Which result is indicated?

TCM (Bus A) is Not Available

Go to step 3.

TCM is Detected

Intermittent failure, the system is OK at this time. Check for poor connections or loose terminals at the CAN gateway and the TCM. If the freeze data/on-board snapshot of this DTC is recorded, try to reproduce the failure under the same conditions with the freeze data/on-board snapshot.

- Open wire check (F-CAN A_H line, F-CAN A_L line) -1. Turn the vehicle to the OFF (LOCK) mode. -2. Disconnect the following connectors. CAN gateway 16P connector TCM connector (50P) -3. Check for continuity between test points 1 and 2. Test condition Vehicle OFF (LOCK) mode CAN gateway 16P connector: disconnected TCM connector (50P): disconnected Test point 1 CAN gateway 16P connector (female terminals) No. 3: Test point 2 TCM connector (50P) No. 3 Test point 1 CAN gateway 16P connector (female terminals) No. 11: Test point 2 TCM connector (50P) No. 11 Courtesy of HONDA, U.S.A., INC. Is there continuity? YES The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM . NO Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.

-1. Turn the vehicle to the OFF (LOCK) mode.

-2. Disconnect the following connectors.

CAN gateway 16P connector

TCM connector (50P)

-3. Check for continuity between test points 1 and 2.

Test condition | Vehicle OFF (LOCK) mode

CAN gateway 16P connector: disconnected

TCM connector (50P): disconnected

Test point 1 | CAN gateway 16P connector (female terminals) No. 3:

Test point 2 | TCM connector (50P) No. 3

Test point 1 | CAN gateway 16P connector (female terminals) No. 11:

Test point 2 | TCM connector (50P) No. 11

Courtesy of HONDA, U.S.A., INC.

Is there continuity?

YES

The F-CAN A_H wire and the F-CAN A_L wire are OK. Check for poor connections or loose terminals at the CAN gateway and the TCM. Check for any authorized service information related to the DTCs or symptoms you are troubleshooting, or substitute a known-good TCM , then recheck. If this DTC goes away and the TCM was substituted, replace the original TCM .

NO

Repair an open in the F-CAN A_H wire and/or the F-CAN A_L wire between the CAN gateway and the TCM.
````

## Chunk 9952: DTC U0302 (K20C2 (CVT))

- Title: DTC U0302 (K20C2 (CVT))
- Source path: `pages\12501.html`
- Chunk ID: `chunk_9f61bdd92c22`
- Images: none
- Duplicate sources: `pages\15517.html`

### Full Text

````text
# DTC U0302 (K20C2 (CVT))

DTC U0302 : PGM-FI System and A/T System Program Version Mismatch

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This DTC is indicated when the TCM update procedure is not completed.

- Do not turn the vehicle to the OFF (LOCK) mode while updating the TCM. If you do, the TCM can be damaged.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0302 PGM-FI System and A/T System Program Version Mismatch

DTC (CVT)

- Problem verification (update) -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Update the TCM . -4. Turn the vehicle to the OFF (LOCK) mode. -5. Turn the vehicle to the ON mode. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0302 PGM-FI System and A/T System Program Version Mismatch Is DTC U0302 indicated? YES The failure is duplicated. Replace the TCM . NO Update is complete.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Update the TCM .

-4. Turn the vehicle to the OFF (LOCK) mode.

-5. Turn the vehicle to the ON mode.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0302 PGM-FI System and A/T System Program Version Mismatch

Is DTC U0302 indicated?

YES

The failure is duplicated. Replace the TCM .

NO

Update is complete.
````

## Chunk 9953: DTC U0302 (L15B7/L15BA/L15BY (CVT))

- Title: DTC U0302 (L15B7/L15BA/L15BY (CVT))
- Source path: `pages\12502.html`
- Chunk ID: `chunk_df7494e37818`
- Images: none
- Duplicate sources: `pages\15548.html`

### Full Text

````text
# DTC U0302 (L15B7/L15BA/L15BY (CVT))

DTC U0302 : PGM-FI System and A/T System Program Version Mismatch

NOTE:

- Before you troubleshoot, review the General Troubleshooting Information .

- This DTC is indicated when the TCM update procedure is not completed.

- Do not turn the vehicle to the OFF (LOCK) mode while updating the TCM. If you do, the TCM can be damaged.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0302 PGM-FI System and A/T System Program Version Mismatch

DTC (CVT)

- Problem verification (update) -1. Turn the vehicle to the ON mode. -2. Clear the DTC with the HDS. -3. Update the TCM . -4. Turn the vehicle to the OFF (LOCK) mode. -5. Turn the vehicle to the ON mode. -6. Check for Pending or Confirmed DTCs with the HDS. DTC Description Confirmed DTC Pending DTC Freeze Frame U0302 PGM-FI System and A/T System Program Version Mismatch Is DTC U0302 indicated? YES The failure is duplicated. Replace the TCM . NO Update is complete.

-1. Turn the vehicle to the ON mode.

-2. Clear the DTC with the HDS.

-3. Update the TCM .

-4. Turn the vehicle to the OFF (LOCK) mode.

-5. Turn the vehicle to the ON mode.

-6. Check for Pending or Confirmed DTCs with the HDS.

DTC Description | Confirmed DTC | Pending DTC | Freeze Frame

U0302 PGM-FI System and A/T System Program Version Mismatch

Is DTC U0302 indicated?

YES

The failure is duplicated. Replace the TCM .

NO

Update is complete.
````

## Chunk 9954: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12504.html`
- Chunk ID: `chunk_34da5a3fdc60`
- Images: `images\GHH400896.jpeg`
- Duplicate sources: `pages\13903.html`

### Full Text

````text
# Removal and Installation

NOTE: Keep all foreign particles out of the transmission.

- Air Cleaner - Remove

- CVT Driven Pulley Pressure Sensor - Remove 1. Disconnect the connector (A). Fig 1: CVT Driven Pulley Pressure Sensor Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 2. Remove the CVT driven pulley pressure sensor (B) with the sealing washer (C). NOTE: Be careful not to damage the plastic part.

1. Disconnect the connector (A).

2. Remove the CVT driven pulley pressure sensor (B) with the sealing washer (C).

NOTE: Be careful not to damage the plastic part.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new sealing washer. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new sealing washer. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new sealing washer.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- TCM - Reset (Only for Replacing CVT Driven Pulley Pressure Sensor) NOTE: This procedure is not required, if the CVT driven pulley pressure sensor and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the CVT driven pulley pressure sensor and the TCM are replaced simultaneously.
````

## Chunk 9955: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12505.html`
- Chunk ID: `chunk_79b38d4a635f`
- Images: `images\GHH400897.jpeg`
- Duplicate sources: `pages\13904.html`

### Full Text

````text
# Removal and Installation

NOTE: Keep all foreign particles out of the transmission.

- Air Cleaner - Remove

- CVT Driven Pulley Pressure Sensor - Remove 1. Disconnect the connector (A). Fig 1: CVT Driven Pulley Pressure Sensor Components With Torque Specifications (L15B7/L15BA - CVT) Courtesy of HONDA, U.S.A., INC. 2. Remove the CVT driven pulley pressure sensor (B) with the sealing washer (C). NOTE: Be careful not to damage the plastic part.

1. Disconnect the connector (A).

2. Remove the CVT driven pulley pressure sensor (B) with the sealing washer (C).

NOTE: Be careful not to damage the plastic part.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new sealing washer. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new sealing washer. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new sealing washer.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- TCM - Reset (Only for Replacing CVT Driven Pulley Pressure Sensor) NOTE: This procedure is not required, if the CVT driven pulley pressure sensor and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the CVT driven pulley pressure sensor and the TCM are replaced simultaneously.
````

## Chunk 9956: Exploded View

- Title: Exploded View
- Source path: `pages\12506.html`
- Chunk ID: `chunk_bca87234467a`
- Images: `images\GHH400898.jpeg`
- Duplicate sources: `pages\12508.html`, `pages\13905.html`, `pages\13907.html`

### Full Text

````text
# Exploded View

- Speed Sensor Speed Sensor - Exploded View Courtesy of HONDA, U.S.A., INC.

Speed Sensor - Exploded View

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9957: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12507.html`
- Chunk ID: `chunk_6e53fbf7dc41`
- Images: `images\GHH400899.jpeg`, `images\GHH400900.jpeg`, `images\GHH400901.jpeg`
- Duplicate sources: `pages\13906.html`

### Full Text

````text
# Removal and Installation

NOTE: Keep all foreign particles out of the transmission.

CVT Speed Sensor

- Air Cleaner - Remove

- Intake Air Duct - Remove

- CVT Speed Sensor - Remove Fig 1: CVT Speed Sensor Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the CVT speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the CVT speed sensor (B) with the O-ring (C).

2. Remove the CVT speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

CVT Drive Pulley Speed Sensor

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine Undercover Lid - Remove

- CVT Drive Pulley Speed Sensor - Remove Fig 2: CVT Drive Pulley Speed Sensor Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

Torque Converter Turbine Speed Sensor

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine Undercover Lid - Remove

- Torque Converter Turbine Speed Sensor - Remove Fig 3: Torque Converter Turbine Speed Sensor Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.
````

## Chunk 9958: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12509.html`
- Chunk ID: `chunk_f671b31e2408`
- Images: `images\GHH400903.jpeg`, `images\GHH400904.jpeg`, `images\GHH400905.jpeg`
- Duplicate sources: `pages\13908.html`

### Full Text

````text
# Removal and Installation

NOTE:

- How to read the torque specifications .

- Keep all foreign particles out of the transmission.

CVT Speed Sensor

- CVT Speed Sensor - Remove Fig 1: CVT Speed Sensor Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the CVT speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the CVT speed sensor (B) with the O-ring (C).

2. Remove the CVT speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

CVT Drive Pulley Speed Sensor

- Air Cleaner - Remove

- CVT Drive Pulley Speed Sensor - Remove Fig 2: CVT Drive Pulley Speed Sensor Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

2. Remove the CVT drive pulley speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

Torque Converter Turbine Speed Sensor

- Vehicle - Lift

- Engine Undercover - Remove (Without Engine Undercover Lid)

- Engine Undercover Plate - Remove (With Engine Undercover Lid)

- Engine Undercover Lid - Remove (With Engine Undercover Lid)

- Torque Converter Turbine Speed Sensor - Remove Fig 3: Torque Converter Turbine Speed Sensor Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

1. Disconnect the connector (A). 2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

2. Remove the torque converter turbine speed sensor (B) with the O-ring (C).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Be sure to use a new O-ring which should be applied a light coat of clean transmission fluid before installation.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.
````

## Chunk 9959: CVT Transmission Removal and Installation (K20C2 (CVT)): Notes

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Notes
- Source path: `pages\12510.html`
- Chunk ID: `chunk_25696d88ab83`
- Images: `images\GHH3142.png`, `images\GHH3143.png`, `images\GHH3144.png`
- Duplicate sources: `pages\13909.html`

### Full Text

````text
# CVT Transmission Removal and Installation (K20C2 (CVT)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Universal Lifting Eyelet 07AAK-SNAA120

Courtesy of HONDA, U.S.A., INC. | Engine Support Hanger, A and Reds AAR-T1256*

Courtesy of HONDA, U.S.A., INC. | Subframe Adapter VSB02C000016*

*: Available through the Honda Tool and Equipment Program 888-424-6857.
````

## Chunk 9960: Exploded View

- Title: Exploded View
- Source path: `pages\12511.html`
- Chunk ID: `chunk_ec62a3962ff8`
- Images: `images\GHH400906.jpeg`, `images\GHH400907.jpeg`
- Duplicate sources: `pages\13910.html`

### Full Text

````text
# Exploded View

- Transmission Assembly Mounting Bolt Transmission Assembly Mounting Bolt - Exploded View Fig 1: Exploded View Of Transmission Assembly Mounting Bolts With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.

Transmission Assembly Mounting Bolt - Exploded View

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9961: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal
- Source path: `pages\12512.html`
- Chunk ID: `chunk_1fa965764ef5`
- Images: `images\GHH400908.jpeg`, `images\GHH400909.jpeg`, `images\GHH400910.jpeg`, `images\GHH400911.jpeg`, `images\GHH400912.jpeg`, `images\GHH400913.jpeg`, `images\GHH400914.jpeg`, `images\GHH400915.jpeg`, `images\GHH400916.jpeg`, `images\GHH400917.jpeg`, `images\GHH400918.jpeg`, `images\GHH400919.jpeg`
- Duplicate sources: `pages\13911.html`

### Full Text

````text
# CVT Transmission Removal and Installation (K20C2 (CVT)): Removal

NOTE:

- Use fender covers to avoid damaging painted surfaces.

- Keep all foreign particles out of the transmission.

- Special tool Reds engine support hanger AAR-T1256 must be used with the side engine mount installed.

- Vehicle - Lift Set

- Engine Undercover - Remove

- Engine Undercover Lid - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Vehicle - Lift Down

- Steering Joint - Disconnect NOTE: Hold the steering wheel with the steering wheel holder tool.

NOTE: Hold the steering wheel with the steering wheel holder tool.

- Front Wheel - Remove (Both Sides)

- Front Grille Cover - Remove

- Air Cleaner - Remove

- 12 Volt Battery - Remove

- 12 Volt Battery Base - Remove

- CVTF Warmer - Remove 1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel. Courtesy of HONDA, U.S.A., INC. 2. Remove the CVTF warmer with the O-rings (C) without disconnecting the CVTF warmer hoses. NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer. 3. Put plastic bag over the CVTF warmer, then swing it out of the way. 4. Remove the CVTF warmer strainer (D) with the O-ring (E). 5. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. NOTE: Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel.

Courtesy of HONDA, U.S.A., INC.

2. Remove the CVTF warmer with the O-rings (C) without disconnecting the CVTF warmer hoses.

NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer.

3. Put plastic bag over the CVTF warmer, then swing it out of the way.

4. Remove the CVTF warmer strainer (D) with the O-ring (E).

5. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged.

NOTE:

- Do not use compressed air to clean the CVTF warmer strainer.

- Soak the CVTF warmer strainer thoroughly in transmission fluid.

- EVAP Canister Purge Valve - Remove

- Engine Wire Harness - Remove 1. Disconnect the connectors (A). Courtesy of HONDA, U.S.A., INC. 2. Remove the ground cable (B). 3. Remove the harness clamps (C), then swing the engine wire harness (D) out of the way.

1. Disconnect the connectors (A).

Courtesy of HONDA, U.S.A., INC.

2. Remove the ground cable (B).

3. Remove the harness clamps (C), then swing the engine wire harness (D) out of the way.

- TCM Harness - Remove 1. Disconnect the connectors (A). Fig 1: TCM Harness Components With Connector Disconnection Sequence (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 2. Disconnect the connector (B) by pushing the lock (C) and pulling the lever (D) in the numbered sequence shown. 3. Disconnect the connector (E) by pulling the lock (F) and the lever (G) in the numbered sequence shown. 4. Remove the ground cable (H). 5. Remove the harness cover mounting bolts (J). 6. Remove the harness clamps (K), then swing the TCM harness (L) out of the way.

1. Disconnect the connectors (A).

2. Disconnect the connector (B) by pushing the lock (C) and pulling the lever (D) in the numbered sequence shown.

3. Disconnect the connector (E) by pulling the lock (F) and the lever (G) in the numbered sequence shown.

4. Remove the ground cable (H).

5. Remove the harness cover mounting bolts (J).

6. Remove the harness clamps (K), then swing the TCM harness (L) out of the way.

- Shift Cable (Transmission Side) - Remove

- Engine Support Hanger - Install NOTE: Be careful when working around the windshield. 1. Remove the front damper caps. Courtesy of HONDA, U.S.A., INC. 2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A). 3. Install the engine support hanger onto the vehicle as shown. 4. Attach the hook (B) to the slotted hole in the universal lifting eyelet. 5. Tighten the wing nut (C) by hand, and lift and support the engine/transmission.

NOTE: Be careful when working around the windshield.

1. Remove the front damper caps.
````

## Chunk 9962: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal
- Source path: `pages\12512.html`
- Chunk ID: `chunk_f8a997448068`
- Images: `images\GHH400908.jpeg`, `images\GHH400909.jpeg`, `images\GHH400910.jpeg`, `images\GHH400911.jpeg`, `images\GHH400912.jpeg`, `images\GHH400913.jpeg`, `images\GHH400914.jpeg`, `images\GHH400915.jpeg`, `images\GHH400916.jpeg`, `images\GHH400917.jpeg`, `images\GHH400918.jpeg`, `images\GHH400919.jpeg`
- Duplicate sources: `pages\13911.html`

### Full Text

````text
mbered sequence shown.

4. Remove the ground cable (H).

5. Remove the harness cover mounting bolts (J).

6. Remove the harness clamps (K), then swing the TCM harness (L) out of the way.

- Shift Cable (Transmission Side) - Remove

- Engine Support Hanger - Install NOTE: Be careful when working around the windshield. 1. Remove the front damper caps. Courtesy of HONDA, U.S.A., INC. 2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A). 3. Install the engine support hanger onto the vehicle as shown. 4. Attach the hook (B) to the slotted hole in the universal lifting eyelet. 5. Tighten the wing nut (C) by hand, and lift and support the engine/transmission.

NOTE: Be careful when working around the windshield.

1. Remove the front damper caps.

Courtesy of HONDA, U.S.A., INC.

2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A).

3. Install the engine support hanger onto the vehicle as shown.

4. Attach the hook (B) to the slotted hole in the universal lifting eyelet.

5. Tighten the wing nut (C) by hand, and lift and support the engine/transmission.

- Upper Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission Mount - Remove

- Vehicle - Lift Up

- Exhaust Pipe A - Remove

- Connector (EPS Subharness) - Disconnect Fig 2: Connector (EPS Subharness) Components With Disconnection Sequence (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Disconnect the connector (D).

1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Disconnect the connector (D).

2. Disconnect the connector (D).

- Tie-Rod End Ball Joint - Disconnect (Both Sides)

- Lower Stabilizer Link Ball Joint - Disconnect (Both Sides)

- Lower Arm Ball Joint - Disconnect (Both Sides)

- Lower Arm Mounting Bolt - Remove (Both Sides) Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Brace - Remove

- Torque Rod Mounting Bolt - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Subframe - Remove Courtesy of HONDA, U.S.A., INC. 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Remove the front subframe .

Courtesy of HONDA, U.S.A., INC. | 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Remove the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Remove the front subframe .

- Transmission - Support 1. Support the transmission with the transmission jack.

1. Support the transmission with the transmission jack.

- Drive Plate - Disconnect Courtesy of HONDA, U.S.A., INC. 1. Remove the torque converter cover (A). 2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the torque converter cover (A). 2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

- Driveshaft Inboard Joint - Disconnect (Both Sides) NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

- Lower Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission - Remove Courtesy of HONDA, U.S.A., INC. 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame. 4. Slide the transmission away from the engine, then remove it from the vehicle. NOTE: Be careful not to drop the torque converter. 5.
````

## Chunk 9963: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Removal
- Source path: `pages\12512.html`
- Chunk ID: `chunk_5408155bcfd7`
- Images: `images\GHH400908.jpeg`, `images\GHH400909.jpeg`, `images\GHH400910.jpeg`, `images\GHH400911.jpeg`, `images\GHH400912.jpeg`, `images\GHH400913.jpeg`, `images\GHH400914.jpeg`, `images\GHH400915.jpeg`, `images\GHH400916.jpeg`, `images\GHH400917.jpeg`, `images\GHH400918.jpeg`, `images\GHH400919.jpeg`
- Duplicate sources: `pages\13911.html`

### Full Text

````text
dy with a nylon strap on both sides.

NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

- Lower Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission - Remove Courtesy of HONDA, U.S.A., INC. 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame. 4. Slide the transmission away from the engine, then remove it from the vehicle. NOTE: Be careful not to drop the torque converter. 5. Lower the transmission carefully.

Courtesy of HONDA, U.S.A., INC. | 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame. 4. Slide the transmission away from the engine, then remove it from the vehicle. NOTE: Be careful not to drop the torque converter. 5. Lower the transmission carefully.

2. Hold the transmission on the transmission jack.

3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame.

4. Slide the transmission away from the engine, then remove it from the vehicle.

NOTE: Be careful not to drop the torque converter.

5. Lower the transmission carefully.

- Torque Converter - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the torque converter (A) with the O-ring (B). 2. Remove the dowel pins (C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the torque converter (A) with the O-ring (B). 2. Remove the dowel pins (C).

2. Remove the dowel pins (C).

- Harness Bracket - Remove Courtesy of HONDA, U.S.A., INC. 1. If necessary, remove the harness brackets.

Courtesy of HONDA, U.S.A., INC. | 1. If necessary, remove the harness brackets.

- Drive Plate - Inspect 1. Inspect the drive plate, and replace it if it is damaged .

1. Inspect the drive plate, and replace it if it is damaged .
````

## Chunk 9964: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation
- Source path: `pages\12513.html`
- Chunk ID: `chunk_285796474b2e`
- Images: `images\GHH400920.jpeg`, `images\GHH400921.jpeg`, `images\GHH400922.jpeg`, `images\GHH400923.jpeg`, `images\GHH400924.jpeg`, `images\GHH400925.jpeg`, `images\GHH400926.jpeg`, `images\GHH400927.jpeg`, `images\GHH400928.jpeg`, `images\GHH400929.jpeg`, `images\GHH400930.jpeg`
- Duplicate sources: `pages\13912.html`

### Full Text

````text
# CVT Transmission Removal and Installation (K20C2 (CVT)): Installation

NOTE:

- Use fender covers to avoid damaging painted surfaces.

- Keep all foreign particles out of the transmission.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- When connecting the connector, check for corrosion, dirt, or oil, and clean or repair if necessary.

- Harness Bracket - Install Fig 1: Harness Bracket Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC.

- Torque Converter - Install Courtesy of HONDA, U.S.A., INC. 1. Install the dowel pins (A). 2. Install the torque converter (B) with a new O-ring (C). NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

Courtesy of HONDA, U.S.A., INC. | 1. Install the dowel pins (A). 2. Install the torque converter (B) with a new O-ring (C). NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

2. Install the torque converter (B) with a new O-ring (C).

NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

- Transmission - Install Courtesy of HONDA, U.S.A., INC. 1. Hold the transmission (A) on a transmission jack, and raise it to engine level. NOTE: Be careful not to drop the torque converter. 2. Attach the transmission to the engine.

Courtesy of HONDA, U.S.A., INC. | 1. Hold the transmission (A) on a transmission jack, and raise it to engine level. NOTE: Be careful not to drop the torque converter. 2. Attach the transmission to the engine.

NOTE: Be careful not to drop the torque converter.

2. Attach the transmission to the engine.

- Lower Transmission Assembly Mounting Bolt - Install NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Driveshaft Inboard Joint - Connect (Both Sides)

- Drive Plate - Connect Fig 2: Drive Plate Bolts And Torque Converter Cover Bolts With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Attach the drive plate (A) to the torque converter with eight torque converter bolts (B). 2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern. 3. Check that the crankshaft rotates freely. 4. Install the torque converter cover (C).

1. Attach the drive plate (A) to the torque converter with eight torque converter bolts (B). 2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern. 3. Check that the crankshaft rotates freely. 4. Install the torque converter cover (C).

2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern.

3. Check that the crankshaft rotates freely.

4. Install the torque converter cover (C).

- Front Subframe - Install Courtesy of HONDA, U.S.A., INC. 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

Courtesy of HONDA, U.S.A., INC. | 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Install the front subframe .

- Torque Rod Mounting Bolt - Loosely Install Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Brace - Install

- Lower Arm Mounting Bolt - Install (Both Sides) Fig 3: Lower Arm Mounting Bolt With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC.

- Lower Arm Ball Joint - Connect (Both Sides)

- Lower Stabilizer Link Ball Joint - Connect (Both Sides)

- Tie-Rod End Ball Joint - Connect (Both Sides)
````

## Chunk 9965: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation
- Source path: `pages\12513.html`
- Chunk ID: `chunk_b508521a0ce1`
- Images: `images\GHH400920.jpeg`, `images\GHH400921.jpeg`, `images\GHH400922.jpeg`, `images\GHH400923.jpeg`, `images\GHH400924.jpeg`, `images\GHH400925.jpeg`, `images\GHH400926.jpeg`, `images\GHH400927.jpeg`, `images\GHH400928.jpeg`, `images\GHH400929.jpeg`, `images\GHH400930.jpeg`
- Duplicate sources: `pages\13912.html`

### Full Text

````text
Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Install the front subframe .

- Torque Rod Mounting Bolt - Loosely Install Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Brace - Install

- Lower Arm Mounting Bolt - Install (Both Sides) Fig 3: Lower Arm Mounting Bolt With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC.

- Lower Arm Ball Joint - Connect (Both Sides)

- Lower Stabilizer Link Ball Joint - Connect (Both Sides)

- Tie-Rod End Ball Joint - Connect (Both Sides)

- Connector (EPS Subharness) - Connect Courtesy of HONDA, U.S.A., INC. 1. Connect the connectors (A), and make sure they are fully seated.

Courtesy of HONDA, U.S.A., INC. | 1. Connect the connectors (A), and make sure they are fully seated.

- Exhaust Pipe A - Install

- Vehicle - Lift Down

- Transmission Mount - Loosely Install

- Upper Transmission Assembly Mounting Bolt - Install NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Engine Support Hanger - Remove 1. Remove the engine support hanger and the universal lifting eyelet. 2. Install the front damper caps.

1. Remove the engine support hanger and the universal lifting eyelet. 2. Install the front damper caps.

2. Install the front damper caps.

- Engine/Transmission Mount - Tightening Procedure

- Shift Cable (Transmission Side) - Install NOTE: Be sure to adjust the shift cable after installing the shift cable.

NOTE: Be sure to adjust the shift cable after installing the shift cable.

- TCM Harness - Install 1. Install the harness clamps (A). Fig 4: TCM Harness Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the harness cover mounting bolts (B). 3. Install the ground cable (C). 4. Connect the connectors (D), and make sure they are fully seated.

1. Install the harness clamps (A).

2. Install the harness cover mounting bolts (B).

3. Install the ground cable (C).

4. Connect the connectors (D), and make sure they are fully seated.

- Engine Wire Harness - Install 1. Install the clamps (A). Fig 5: Engine Wire Harness Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the ground cable (B). 3. Connect the connectors (C).

1. Install the clamps (A).

2. Install the ground cable (B).

3. Connect the connectors (C).

- EVAP Canister Purge Valve - Install

- CVTF Warmer - Install 1. Install the CVTF warmer strainer (A) with a new O-ring (B) in the direction shown. Fig 6: Exploded View Of CVTF Warmer Components With Torque Specifications (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the CVTF warmer (C) with new O-rings (D). NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer. Make sure the O-rings are firmly installed in the grooves. Check the connector (E) for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the CVTF warmer strainer (A) with a new O-ring (B) in the direction shown.

2. Install the CVTF warmer (C) with new O-rings (D).

NOTE:

- The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer.

- Make sure the O-rings are firmly installed in the grooves.

- Check the connector (E) for corrosion, dirt, or oil, and clean or repair if necessary.

- 12 Volt Battery Base - Install

- 12 Volt Battery - Install

- Air Cleaner - Install

- Front Grille Cover - Install

- Front Wheel - Install (Both Sides)

- Steering Joint - Connect

- Transmission Fluid - Refill

- Transmission - After Install Check 1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 5. Check the shift lever operation. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3.
````

## Chunk 9966: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation

- Title: CVT Transmission Removal and Installation (K20C2 (CVT)): Installation
- Source path: `pages\12513.html`
- Chunk ID: `chunk_af3b547f8d0d`
- Images: `images\GHH400920.jpeg`, `images\GHH400921.jpeg`, `images\GHH400922.jpeg`, `images\GHH400923.jpeg`, `images\GHH400924.jpeg`, `images\GHH400925.jpeg`, `images\GHH400926.jpeg`, `images\GHH400927.jpeg`, `images\GHH400928.jpeg`, `images\GHH400929.jpeg`, `images\GHH400930.jpeg`
- Duplicate sources: `pages\13912.html`

### Full Text

````text
nstall

- Air Cleaner - Install

- Front Grille Cover - Install

- Front Wheel - Install (Both Sides)

- Steering Joint - Connect

- Transmission Fluid - Refill

- Transmission - After Install Check 1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 5. Check the shift lever operation. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 5. Check the shift lever operation. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

2. Turn the vehicle to the ON mode.

3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation.

4. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

5. Check the shift lever operation.

6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

- Engine Undercover Lid - Install

- Engine Undercover - Install

- TCM - Reset (Only for Replacing Transmission) NOTE: This procedure is not required, if the transmission and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the transmission and the TCM are replaced simultaneously.

- Front Wheel Alignment - Check

- VSA Sensor Neutral Position - Memorize

- Vehicle - Road Test
````

## Chunk 9967: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Notes

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Notes
- Source path: `pages\12514.html`
- Chunk ID: `chunk_1134459964e1`
- Images: `images\GHH3142.png`, `images\GHH3143.png`, `images\GHH3144.png`
- Duplicate sources: `pages\13913.html`

### Full Text

````text
# CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Universal Lifting Eyelet 07AAK-SNAA120

Courtesy of HONDA, U.S.A., INC. | Engine Support Hanger, A and Reds AAR-T1256*

Courtesy of HONDA, U.S.A., INC. | Subframe Adapter VSB02C000016*

*: Available through the Honda Tool and Equipment Program 888-424-6857.
````

## Chunk 9968: Exploded View

- Title: Exploded View
- Source path: `pages\12515.html`
- Chunk ID: `chunk_c673a1dd84a4`
- Images: `images\GHH400931.jpeg`, `images\GHH400932.jpeg`
- Duplicate sources: `pages\13914.html`

### Full Text

````text
# Exploded View

NOTE: How to read the torque specifications .

- Transmission Assembly Mounting Bolt Transmission Assembly Mounting Bolt - Exploded View Fig 1: Exploded View Of Transmission Assembly Mounting Bolts With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.

Transmission Assembly Mounting Bolt - Exploded View

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 9969: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal
- Source path: `pages\12516.html`
- Chunk ID: `chunk_b015b49aff98`
- Images: `images\GHH400933.jpeg`, `images\GHH400934.jpeg`, `images\GHH400935.jpeg`, `images\GHH400936.jpeg`, `images\GHH400937.jpeg`, `images\GHH400938.jpeg`, `images\GHH400939.jpeg`, `images\GHH400940.jpeg`, `images\GHH400941.jpeg`, `images\GHH400942.jpeg`, `images\GHH400943.jpeg`, `images\GHH400944.jpeg`
- Duplicate sources: `pages\13915.html`

### Full Text

````text
# CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

NOTE:

- Use fender covers to avoid damaging painted surfaces.

- Keep all foreign particles out of the transmission.

- Special tool Reds engine support hanger AAR-T1256 must be used with the side engine mount installed.

- Vehicle - Lift Set

- Engine Undercover - Remove

- Engine Undercover Lid - Remove (With Engine Undercover Lid)

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Vehicle - Lift Down

- Steering Joint - Disconnect NOTE: Hold the steering wheel with the steering wheel holder tool.

NOTE: Hold the steering wheel with the steering wheel holder tool.

- Front Wheel - Remove (Both Sides)

- Front Grille Cover - Remove

- Air Cleaner - Remove

- 12 Volt Battery - Remove

- 12 Volt Battery Base - Remove

- CVTF Warmer - Remove 1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel. Courtesy of HONDA, U.S.A., INC. 2. Remove the CVTF warmer with the O-rings (C) without disconnecting the CVTF warmer hoses. NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer. 3. Put plastic bag over the CVTF warmer, then swing it out of the way. 4. Remove the CVTF warmer strainer (D) with the O-ring (E). 5. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel.

Courtesy of HONDA, U.S.A., INC.

2. Remove the CVTF warmer with the O-rings (C) without disconnecting the CVTF warmer hoses.

NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer.

3. Put plastic bag over the CVTF warmer, then swing it out of the way.

4. Remove the CVTF warmer strainer (D) with the O-ring (E).

5. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged.

- Do not use compressed air to clean the CVTF warmer strainer.

- Soak the CVTF warmer strainer thoroughly in transmission fluid.

- Intake Air Duct E - Remove

- Intake Air Duct F - Remove

- Engine Wire Harness - Remove 1. Disconnect the connectors (A). Courtesy of HONDA, U.S.A., INC. 2. Remove the ground cables (B). 3. Remove the harness covers (C) and the harness brackets (D), then swing the engine wire harness (E) out of the way.

1. Disconnect the connectors (A).

Courtesy of HONDA, U.S.A., INC.

2. Remove the ground cables (B).

3. Remove the harness covers (C) and the harness brackets (D), then swing the engine wire harness (E) out of the way.

- TCM Harness - Remove 1. Disconnect the connectors (A). Fig 1: TCM Harness Components With Connector Disconnection Sequence (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 2. Disconnect the connector (B) by pushing the lock (C) and pulling the lever (D) in the numbered sequence shown. 3. Disconnect the connector (E) by pulling the lock (F) and the lever (G) in the numbered sequence shown. 4. Remove the ground cable (H). 5. Remove the harness covers (J) and the harness clamp (K), then swing the TCM harness (L) out of the way.

1. Disconnect the connectors (A).

2. Disconnect the connector (B) by pushing the lock (C) and pulling the lever (D) in the numbered sequence shown.

3. Disconnect the connector (E) by pulling the lock (F) and the lever (G) in the numbered sequence shown.

4. Remove the ground cable (H).

5. Remove the harness covers (J) and the harness clamp (K), then swing the TCM harness (L) out of the way.

- Shift Cable (Transmission Side) - Remove

- Intake Manifold Bracket - Remove

- Engine Support Hanger - Install NOTE: Be careful when working around the windshield. 1. Remove the front damper caps. Courtesy of HONDA, U.S.A., INC. 2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A). 3. Install the engine support hanger onto the vehicle as shown. 4. Attach the hook (B) to the slotted hole in the universal lifting eyelet. 5.
````

## Chunk 9970: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal
- Source path: `pages\12516.html`
- Chunk ID: `chunk_ccd5dfb13aee`
- Images: `images\GHH400933.jpeg`, `images\GHH400934.jpeg`, `images\GHH400935.jpeg`, `images\GHH400936.jpeg`, `images\GHH400937.jpeg`, `images\GHH400938.jpeg`, `images\GHH400939.jpeg`, `images\GHH400940.jpeg`, `images\GHH400941.jpeg`, `images\GHH400942.jpeg`, `images\GHH400943.jpeg`, `images\GHH400944.jpeg`
- Duplicate sources: `pages\13915.html`

### Full Text

````text
the lock (C) and pulling the lever (D) in the numbered sequence shown.

3. Disconnect the connector (E) by pulling the lock (F) and the lever (G) in the numbered sequence shown.

4. Remove the ground cable (H).

5. Remove the harness covers (J) and the harness clamp (K), then swing the TCM harness (L) out of the way.

- Shift Cable (Transmission Side) - Remove

- Intake Manifold Bracket - Remove

- Engine Support Hanger - Install NOTE: Be careful when working around the windshield. 1. Remove the front damper caps. Courtesy of HONDA, U.S.A., INC. 2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A). 3. Install the engine support hanger onto the vehicle as shown. 4. Attach the hook (B) to the slotted hole in the universal lifting eyelet. 5. Tighten the wing nut (C) by hand, and lift and support the engine/transmission.

NOTE: Be careful when working around the windshield.

1. Remove the front damper caps.

Courtesy of HONDA, U.S.A., INC.

2. Install the universal lifting eyelet with an about 50 mm (2.00 in) commercially available spacer (A).

3. Install the engine support hanger onto the vehicle as shown.

4. Attach the hook (B) to the slotted hole in the universal lifting eyelet.

5. Tighten the wing nut (C) by hand, and lift and support the engine/transmission.

- Upper Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission Mount - Remove

- Vehicle - Lift Up

- Front Floor Brace - Remove (With Front Floor Brace)

- Exhaust Pipe A - Remove

- Connector (EPS Subharness) - Disconnect Fig 2: Connector (EPS Subharness) Components With Disconnection Sequence (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Disconnect the connector (D).

1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Disconnect the connector (D).

2. Disconnect the connector (D).

- Tie-Rod End Ball Joint - Disconnect (Both Sides)

- Lower Stabilizer Link Ball Joint - Disconnect (Both Sides)

- Lower Arm Ball Joint - Disconnect (Both Sides)

- Lower Arm Mounting Bolt - Remove (Both Sides) Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Brace - Remove

- Intake Air Resonator - Remove

- Torque Rod Mounting Bolt - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Front Subframe - Remove Courtesy of HONDA, U.S.A., INC. 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Remove the front subframe .

Courtesy of HONDA, U.S.A., INC. | 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Remove the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Remove the front subframe .

- Transmission - Support 1. Support the transmission with the transmission jack.

1. Support the transmission with the transmission jack.

- Drive Plate - Disconnect Courtesy of HONDA, U.S.A., INC. 1. Remove the torque converter cover (A). 2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the torque converter cover (A). 2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

- Driveshaft Inboard Joint - Disconnect (Both Sides) NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

- Intermediate Shaft - Remove

- Lower Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission - Remove Courtesy of HONDA, U.S.A., INC. 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3.
````

## Chunk 9971: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal
- Source path: `pages\12516.html`
- Chunk ID: `chunk_cc8409007caa`
- Images: `images\GHH400933.jpeg`, `images\GHH400934.jpeg`, `images\GHH400935.jpeg`, `images\GHH400936.jpeg`, `images\GHH400937.jpeg`, `images\GHH400938.jpeg`, `images\GHH400939.jpeg`, `images\GHH400940.jpeg`, `images\GHH400941.jpeg`, `images\GHH400942.jpeg`, `images\GHH400943.jpeg`, `images\GHH400944.jpeg`
- Duplicate sources: `pages\13915.html`

### Full Text

````text
onverter cover (A). 2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

2. Remove eight torque converter bolts (B) while rotating the crankshaft pulley.

- Driveshaft Inboard Joint - Disconnect (Both Sides) NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

NOTE: Secure the driveshaft to the body with a nylon strap on both sides.

- Intermediate Shaft - Remove

- Lower Transmission Assembly Mounting Bolt - Remove NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Transmission - Remove Courtesy of HONDA, U.S.A., INC. 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame. 4. Slide the transmission away from the engine, then remove it from the vehicle. NOTE: Be careful not to drop the torque converter. 5. Lower the transmission carefully.

Courtesy of HONDA, U.S.A., INC. | 1. Check once again that the transmission (A) is free of hoses and electrical wiring. 2. Hold the transmission on the transmission jack. 3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame. 4. Slide the transmission away from the engine, then remove it from the vehicle. NOTE: Be careful not to drop the torque converter. 5. Lower the transmission carefully.

2. Hold the transmission on the transmission jack.

3. Lower the transmission by loosening the wing nut of the engine support hanger, and tilt the engine just enough for the transmission to clear its end from the side frame.

4. Slide the transmission away from the engine, then remove it from the vehicle.

NOTE: Be careful not to drop the torque converter.

5. Lower the transmission carefully.

- Torque Converter - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the torque converter (A). 2. Remove the dowel pins (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the torque converter (A). 2. Remove the dowel pins (B).

2. Remove the dowel pins (B).

- Harness Bracket - Remove 1. If necessary, remove the harness brackets. Courtesy of HONDA, U.S.A., INC.

1. If necessary, remove the harness brackets.

Courtesy of HONDA, U.S.A., INC.

- Drive Plate - Inspect 1. Inspect the drive plate, and replace it if it is damaged .

1. Inspect the drive plate, and replace it if it is damaged .
````

## Chunk 9972: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation
- Source path: `pages\12517.html`
- Chunk ID: `chunk_c9ea28c099fc`
- Images: `images\GHH400945.jpeg`, `images\GHH400946.jpeg`, `images\GHH400947.jpeg`, `images\GHH400948.jpeg`, `images\GHH400949.jpeg`, `images\GHH400950.jpeg`, `images\GHH400951.jpeg`, `images\GHH400952.jpeg`, `images\GHH400953.jpeg`, `images\GHH400954.jpeg`, `images\GHH400955.jpeg`
- Duplicate sources: `pages\13916.html`

### Full Text

````text
# CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

NOTE:

- How to read the torque specifications .

- Use fender covers to avoid damaging painted surfaces.

- Keep all foreign particles out of the transmission.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- When connecting the connector, check for corrosion, dirt, or oil, and clean or repair if necessary.

- Harness Bracket - Install Fig 1: Harness Bracket Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC.

- Torque Converter - Install Courtesy of HONDA, U.S.A., INC. 1. Install the dowel pins (A). 2. Install the torque converter (B). NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

Courtesy of HONDA, U.S.A., INC. | 1. Install the dowel pins (A). 2. Install the torque converter (B). NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

2. Install the torque converter (B).

NOTE: Make sure the torque converter is fully engaged on the input shaft, the stator shaft, and the transmission fluid pump drive sprocket. Failure to do so will result in severe transmission or engine damage.

- Transmission - Install Courtesy of HONDA, U.S.A., INC. 1. Hold the transmission (A) on a transmission jack, and raise it to engine level. NOTE: Be careful not to drop the torque converter. 2. Attach the transmission to the engine.

Courtesy of HONDA, U.S.A., INC. | 1. Hold the transmission (A) on a transmission jack, and raise it to engine level. NOTE: Be careful not to drop the torque converter. 2. Attach the transmission to the engine.

NOTE: Be careful not to drop the torque converter.

2. Attach the transmission to the engine.

- Lower Transmission Assembly Mounting Bolt - Install NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Intermediate Shaft - Install

- Driveshaft Inboard Joint - Connect (Both Sides)

- Drive Plate - Connect Fig 2: Drive Plate Bolts And Torque Converter Cover Bolts With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Attach the drive plate (A) to the torque converter with eight torque converter bolts (B). 2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern. 3. Check that the crankshaft rotates freely. 4. Install the torque converter cover (C).

1. Attach the drive plate (A) to the torque converter with eight torque converter bolts (B). 2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern. 3. Check that the crankshaft rotates freely. 4. Install the torque converter cover (C).

2. Rotate the crankshaft pulley as necessary to tighten the bolt to half of the specified torque, then to the final torque, in a crisscross pattern.

3. Check that the crankshaft rotates freely.

4. Install the torque converter cover (C).

- Front Subframe - Install Courtesy of HONDA, U.S.A., INC. 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

Courtesy of HONDA, U.S.A., INC. | 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Install the front subframe .

- Torque Rod Mounting Bolt - Loosely Install Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Intake Air Resonator - Install

- Front Brace - Install

- Lower Arm Mounting Bolt - Install (Both Sides) Fig 3: Lower Arm Mounting Bolt With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC.

- Lower Arm Ball Joint - Connect (Both Sides)
````

## Chunk 9973: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation
- Source path: `pages\12517.html`
- Chunk ID: `chunk_5210d2f2bb2a`
- Images: `images\GHH400945.jpeg`, `images\GHH400946.jpeg`, `images\GHH400947.jpeg`, `images\GHH400948.jpeg`, `images\GHH400949.jpeg`, `images\GHH400950.jpeg`, `images\GHH400951.jpeg`, `images\GHH400952.jpeg`, `images\GHH400953.jpeg`, `images\GHH400954.jpeg`, `images\GHH400955.jpeg`
- Duplicate sources: `pages\13916.html`

### Full Text

````text
ll the front subframe .

Courtesy of HONDA, U.S.A., INC. | 1. Set the subframe adapter (VSB02C000016) on a transmission jack (A), line up the slots in the arms with the bolt holes on the corner of the jack base, and tighten the bolts. 2. Attach the subframe adapter to the front subframe (B). 3. Install the front subframe .

2. Attach the subframe adapter to the front subframe (B).

3. Install the front subframe .

- Torque Rod Mounting Bolt - Loosely Install Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Intake Air Resonator - Install

- Front Brace - Install

- Lower Arm Mounting Bolt - Install (Both Sides) Fig 3: Lower Arm Mounting Bolt With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC.

- Lower Arm Ball Joint - Connect (Both Sides)

- Lower Stabilizer Link Ball Joint - Connect (Both Sides)

- Tie-Rod End Ball Joint - Connect (Both Sides)

- Connector (EPS Subharness) - Connect Courtesy of HONDA, U.S.A., INC. 1. Connect the connectors (A), and make sure they are fully seated.

Courtesy of HONDA, U.S.A., INC. | 1. Connect the connectors (A), and make sure they are fully seated.

- Exhaust Pipe A - Install

- Front Floor Brace - Install (With Front Floor Brace)

- Vehicle - Lift Down

- Transmission Mount - Loosely Install

- Upper Transmission Assembly Mounting Bolt - Install NOTE: Refer to the Exploded View as needed during this procedure.

NOTE: Refer to the Exploded View as needed during this procedure.

- Engine Support Hanger - Remove 1. Remove the engine support hanger and the universal lifting eyelet. 2. Install the front damper caps.

1. Remove the engine support hanger and the universal lifting eyelet. 2. Install the front damper caps.

2. Install the front damper caps.

- Engine/Transmission Mount - Tightening Procedure

- Intake Manifold Bracket - Install

- Shift Cable (Transmission Side) - Install NOTE: Be sure to adjust the shift cable after installing the shift cable.

NOTE: Be sure to adjust the shift cable after installing the shift cable.

- TCM Harness - Install 1. Install the harness covers (A) and the harness clamp (B). Fig 4: Exploded View Of TCM Harness Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the ground cable (C). 3. Connect the connectors (D), and make sure they are fully seated.

1. Install the harness covers (A) and the harness clamp (B).

2. Install the ground cable (C).

3. Connect the connectors (D), and make sure they are fully seated.

- Engine Wire Harness - Install 1. Install the harness brackets (A) and the harness covers (B). Fig 5: Exploded View Of Engine Wire Harness Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the ground cables (C). 3. Connect the connectors (D).

1. Install the harness brackets (A) and the harness covers (B).

2. Install the ground cables (C).

3. Connect the connectors (D).

- Intake Air Duct F - Install

- Intake Air Duct E - Install

- CVTF Warmer - Install 1. Install the CVTF warmer strainer (A) with a new O-ring (B) in the direction shown. Fig 6: Exploded View Of CVTF Warmer Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 2. Install the CVTF warmer (C) with new O-rings (D). NOTE: The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer. Make sure the O-rings are firmly installed in the grooves. Check the connector (E) for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the CVTF warmer strainer (A) with a new O-ring (B) in the direction shown.

2. Install the CVTF warmer (C) with new O-rings (D).

NOTE:

- The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer.

- Make sure the O-rings are firmly installed in the grooves.

- Check the connector (E) for corrosion, dirt, or oil, and clean or repair if necessary.

- 12 Volt Battery Base - Install

- 12 Volt Battery - Install

- Air Cleaner - Install

- Front Grille Cover - Install

- Front Wheel - Install (Both Sides)

- Steering Joint - Connect

- Transmission Fluid - Refill

- Transmission Fluid Level - Check

- Transmission - After Install Check 1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine.
````

## Chunk 9974: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Title: CVT Transmission Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation
- Source path: `pages\12517.html`
- Chunk ID: `chunk_1bb121fdf913`
- Images: `images\GHH400945.jpeg`, `images\GHH400946.jpeg`, `images\GHH400947.jpeg`, `images\GHH400948.jpeg`, `images\GHH400949.jpeg`, `images\GHH400950.jpeg`, `images\GHH400951.jpeg`, `images\GHH400952.jpeg`, `images\GHH400953.jpeg`, `images\GHH400954.jpeg`, `images\GHH400955.jpeg`
- Duplicate sources: `pages\13916.html`

### Full Text

````text
tall the CVTF warmer (C) with new O-rings (D).

NOTE:

- The CVTF warmer is aluminum part. Be careful not to damage the CVTF warmer.

- Make sure the O-rings are firmly installed in the grooves.

- Check the connector (E) for corrosion, dirt, or oil, and clean or repair if necessary.

- 12 Volt Battery Base - Install

- 12 Volt Battery - Install

- Air Cleaner - Install

- Front Grille Cover - Install

- Front Wheel - Install (Both Sides)

- Steering Joint - Connect

- Transmission Fluid - Refill

- Transmission Fluid Level - Check

- Transmission - After Install Check 1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 5. Check the shift lever operation. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Make sure all four wheels to rotate freely. 2. Turn the vehicle to the ON mode. 3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 4. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 5. Check the shift lever operation. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

2. Turn the vehicle to the ON mode.

3. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation.

4. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

5. Check the shift lever operation.

6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

- Engine Undercover Lid - Install (With Engine Undercover Lid)

- Engine Undercover - Install

- TCM - Reset (Only for Replacing Transmission) NOTE: This procedure is not required, if the transmission and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the transmission and the TCM are replaced simultaneously.

- Front Wheel Alignment - Check

- VSA Sensor Neutral Position - Memorize

- Vehicle - Road Test
````

## Chunk 9975: CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Removal

- Title: CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Removal
- Source path: `pages\12518.html`
- Chunk ID: `chunk_eacf0f2880a4`
- Images: `images\GHH400956.jpeg`
- Duplicate sources: `pages\13917.html`

### Full Text

````text
# CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Removal

- Engine Coolant - Drain

- Air Cleaner - Remove

- CVTF Warmer Hose - Disconnect 1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel. Courtesy of HONDA, U.S.A., INC. 2. Disconnect the CVTF warmer inlet hose (C) and outlet hose (D). NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel.

Courtesy of HONDA, U.S.A., INC.

2. Disconnect the CVTF warmer inlet hose (C) and outlet hose (D).

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.
````

## Chunk 9976: CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Installation

- Title: CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Installation
- Source path: `pages\12519.html`
- Chunk ID: `chunk_ae2c2b0762ea`
- Images: `images\GHH400957.jpeg`, `images\GHH400958.jpeg`
- Duplicate sources: `pages\13918.html`

### Full Text

````text
# CVTF Warmer Hose Removal and Installation (K20C2 (CVT)): Installation

- CVTF Warmer Hose - Connect 1. Connect the CVTF warmer inlet hose (A) and outlet hose (B) to each bulge (C) of the CVTF warmer lines by aligning the paint marks (D) on the lines with the paint marks (E) on the hose ends. NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed. Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. 2. Secure the CVTF warmer hoses with the clamps (F). NOTE: When securing the clamps, make sure they do not interfere with the surrounding parts. Check the connector (G) for corrosion, dirt, or oil, and clean or repair if necessary.

1. Connect the CVTF warmer inlet hose (A) and outlet hose (B) to each bulge (C) of the CVTF warmer lines by aligning the paint marks (D) on the lines with the paint marks (E) on the hose ends.

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

2. Secure the CVTF warmer hoses with the clamps (F).

NOTE:

- When securing the clamps, make sure they do not interfere with the surrounding parts.

- Check the connector (G) for corrosion, dirt, or oil, and clean or repair if necessary.

- Air Cleaner - Install

- Engine Coolant - Refill
````

## Chunk 9977: CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Title: CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal
- Source path: `pages\12520.html`
- Chunk ID: `chunk_22091a78e6d4`
- Images: `images\GHH400959.jpeg`
- Duplicate sources: `pages\13919.html`

### Full Text

````text
# CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Engine Coolant - Drain

- Air Cleaner - Remove

- Intake Air Duct - Remove

- CVTF Warmer Hose - Disconnect 1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel. Courtesy of HONDA, U.S.A., INC. 2. Disconnect the CVTF warmer inlet hose (C) and outlet hose (D). NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

1. To prevent damage, cover the connector (A) located under the CVTF warmer (B) using a shop towel.

Courtesy of HONDA, U.S.A., INC.

2. Disconnect the CVTF warmer inlet hose (C) and outlet hose (D).

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.
````

## Chunk 9978: CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Title: CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation
- Source path: `pages\12521.html`
- Chunk ID: `chunk_0c8727b32feb`
- Images: `images\GHH400960.jpeg`, `images\GHH400961.jpeg`
- Duplicate sources: `pages\13920.html`

### Full Text

````text
# CVTF Warmer Hose Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- CVTF Warmer Hose - Connect 1. Connect the CVTF warmer inlet hose (A) and outlet hose (B) to each bulge (C) of the CVTF warmer lines by aligning the paint marks (D) on the lines with the paint marks (E) on the hose ends. NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed. Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. 2. Secure the CVTF warmer hoses with the clamps (F). NOTE: When securing the clamps, make sure they do not interfere with the surrounding parts. Check the connector (G) for corrosion, dirt, or oil, and clean or repair if necessary.

1. Connect the CVTF warmer inlet hose (A) and outlet hose (B) to each bulge (C) of the CVTF warmer lines by aligning the paint marks (D) on the lines with the paint marks (E) on the hose ends.

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

2. Secure the CVTF warmer hoses with the clamps (F).

NOTE:

- When securing the clamps, make sure they do not interfere with the surrounding parts.

- Check the connector (G) for corrosion, dirt, or oil, and clean or repair if necessary.

- Intake Air Duct - Install

- Air Cleaner - Install

- Engine Coolant - Refill
````

## Chunk 9979: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\12522.html`
- Chunk ID: `chunk_15ad2828d9e4`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\12524.html`, `pages\12542.html`, `pages\13921.html`, `pages\13923.html`, `pages\13941.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.
````

## Chunk 9980: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12523.html`
- Chunk ID: `chunk_7db0417ec19b`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400962.jpeg`
- Duplicate sources: `pages\13922.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Engine Coolant - Drain

- Air Cleaner - Remove

- Connector (Solenoid Wire Harness) - Cover NOTE: To prevent damage, cover the connector located under the CVTF warmer using a shop towel.

NOTE: To prevent damage, cover the connector located under the CVTF warmer using a shop towel.

- CVTF Warmer Hose - Disconnect NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

- CVTF Warmer - Remove

- CVTF Warmer Strainer - Remove 1. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. NOTE: Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

1. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. NOTE: Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

- Do not use compressed air to clean the CVTF warmer strainer.

- Soak the CVTF warmer strainer thoroughly in transmission fluid.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Make sure the O-rings are firmly installed in the grooves. Make sure the CVTF warmer strainer is installed in the correct direction. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. If necessary, add transmission fluid to the proper level .

1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Make sure the O-rings are firmly installed in the grooves. Make sure the CVTF warmer strainer is installed in the correct direction. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. If necessary, add transmission fluid to the proper level .

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Make sure the O-rings are firmly installed in the grooves.

- Make sure the CVTF warmer strainer is installed in the correct direction.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- If necessary, add transmission fluid to the proper level .

- Engine Coolant - Refill
````

## Chunk 9981: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12525.html`
- Chunk ID: `chunk_7f7af3a6399f`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400963.jpeg`
- Duplicate sources: `pages\13924.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Engine Coolant - Drain

- Air Cleaner - Remove

- Connector (Solenoid Wire Harness A) - Cover NOTE: To prevent damage, cover the connector located under the CVTF warmer using a shop towel.

NOTE: To prevent damage, cover the connector located under the CVTF warmer using a shop towel.

- CVTF Warmer Hose - Disconnect NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

NOTE: When disconnecting/connecting the hoses, do not bend the warmer pipes excessively, or they will be damaged or deformed.

- CVTF Warmer - Remove

- CVTF Warmer Strainer - Remove 1. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. NOTE: Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

1. Clean the CVTF warmer strainer if necessary. Replace the CVTF warmer strainer, if it is clogged or damaged. NOTE: Do not use compressed air to clean the CVTF warmer strainer. Soak the CVTF warmer strainer thoroughly in transmission fluid.

- Do not use compressed air to clean the CVTF warmer strainer.

- Soak the CVTF warmer strainer thoroughly in transmission fluid.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Make sure the O-rings are firmly installed in the grooves. Make sure the CVTF warmer strainer is installed in the correct direction. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. If necessary, add transmission fluid to the proper level .

1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Make sure the O-rings are firmly installed in the grooves. Make sure the CVTF warmer strainer is installed in the correct direction. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. If necessary, add transmission fluid to the proper level .

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Make sure the O-rings are firmly installed in the grooves.

- Make sure the CVTF warmer strainer is installed in the correct direction.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- If necessary, add transmission fluid to the proper level .

- Engine Coolant - Refill
````

## Chunk 9982: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12526.html`
- Chunk ID: `chunk_1d1ed027dfa4`
- Images: `images\GHH400964.jpeg`
- Duplicate sources: `pages\13925.html`

### Full Text

````text
# Removal and Installation

- Transmission - Remove

- Drive Plate - Remove Fig 1: Drive Plate Replacement Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Remove the drive plate (A) with the washer (B).

1. Remove the drive plate (A) with the washer (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Tighten eight bolts in a crisscross pattern in at least two steps.

1. Install the parts in the reverse order of removal. NOTE: Tighten eight bolts in a crisscross pattern in at least two steps.
````

## Chunk 9983: Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Notes

- Title: Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Notes
- Source path: `pages\12527.html`
- Chunk ID: `chunk_7b7c189c2ce8`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13926.html`

### Full Text

````text
# Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repair or service.

NOTE:

- Where icon is shown, for further information see below.

- Do not bend the shift cable excessively.
````

## Chunk 9984: Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Procedure

- Title: Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Procedure
- Source path: `pages\12528.html`
- Chunk ID: `chunk_3e5dd6b00f73`
- Images: `images\GHH400682.png`, `images\GHH400965.jpeg`, `images\GHH400966.jpeg`, `images\GHH400967.jpeg`
- Duplicate sources: `pages\13927.html`

### Full Text

````text
# Shift Cable Removal and Installation (K20C2 (CVT)): Removal: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

- Vehicle - Lift

- Center Console - Remove

- Shift Lever - Position Courtesy of HONDA, U.S.A., INC. 1. Insert a 6.0 mm (0.236 in) pin (A) into the positioning holes (B) with the shift lever in R position/mode. NOTE: Use only a 6.0 mm (0.236 in) pin with no burrs.

Courtesy of HONDA, U.S.A., INC. | 1. Insert a 6.0 mm (0.236 in) pin (A) into the positioning holes (B) with the shift lever in R position/mode. NOTE: Use only a 6.0 mm (0.236 in) pin with no burrs.

- Shift Cable (Shift Lever Side) - Remove NOTE: While expanding the lock tab (A), rotate the socket holder retainer (B) counterclockwise until it stops, then remove the socket holder (C). Do not remove the shift cable by pulling the shift cable guide (D). Courtesy of HONDA, U.S.A., INC.

NOTE:

- While expanding the lock tab (A), rotate the socket holder retainer (B) counterclockwise until it stops, then remove the socket holder (C).

- Do not remove the shift cable by pulling the shift cable guide (D).

Courtesy of HONDA, U.S.A., INC.

- Air Cleaner - Remove

- Intake Air Duct - Remove

- Lock Pin - Remove

- Control Pin - Remove

- Shift Cable Bracket - Remove

- Engine Undercover - Remove

- Heat Shield (Exhaust Pipe A) - Remove

- Shift Cable (Under Side) - Remove
````

## Chunk 9985: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Notes

- Title: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Notes
- Source path: `pages\12529.html`
- Chunk ID: `chunk_16a7b33a99ae`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13928.html`

### Full Text

````text
# Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repair or service.

NOTE:

- Where icon is shown, for further information see below.

- Do not bend the shift cable excessively.
````

## Chunk 9986: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Procedure

- Title: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Procedure
- Source path: `pages\12530.html`
- Chunk ID: `chunk_34b89f34b8c5`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400968.jpeg`, `images\GHH400969.png`, `images\GHH400970.jpeg`, `images\GHH400971.jpeg`, `images\GHH400972.jpeg`, `images\GHH400973.jpeg`, `images\GHH400974.jpeg`
- Duplicate sources: `pages\13929.html`

### Full Text

````text
# Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Apply molybdenum grease to inner surface of hole.

- Shift Cable (Under Side) - Install

- Heat Shield (Exhaust Pipe A) - Install

- Engine Undercover - Install

- Shift Cable Bracket - Install

- Control Pin - Install Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the control pin (A) is inserted through the shift cable end (B) and fully seated on the control lever (C).

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the control pin (A) is inserted through the shift cable end (B) and fully seated on the control lever (C).

- Lock Pin - Install Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the lock pin (A) is inserted through the control pin hole (B) to the opening (C) of the control lever (D) so that the hooked end (E) of the lock pin locks into the control pin hole.

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the lock pin (A) is inserted through the control pin hole (B) to the opening (C) of the control lever (D) so that the hooked end (E) of the lock pin locks into the control pin hole.

- Intake Air Duct - Install

- Air Cleaner - Install

- Shift Cable - Adjust

- Shift Cable (Shift Lever Side) - Install NOTE: Install the socket holder (A), then rotate the socket holder retainer (B) clockwise until it stops. Do not install the shift cable by holding the shift cable guide (C). Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the shift cable end (A) is properly installed on the mounting stud (B). If the cable end is out of position with the mounting stud, remove the shift cable from the shift cable bracket, then reinstall the cable end over the mounting stud before reinstalling the shift cable to the shift cable bracket. Do not install the shift cable end on the mounting stud with the shift cable installed on the shift cable bracket. If the shift cable end does not ride at the bottom of the mounting stud, rotate the stud to align the square fitting with the hole.

NOTE:

- Install the socket holder (A), then rotate the socket holder retainer (B) clockwise until it stops.

- Do not install the shift cable by holding the shift cable guide (C).

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the shift cable end (A) is properly installed on the mounting stud (B).

- If the cable end is out of position with the mounting stud, remove the shift cable from the shift cable bracket, then reinstall the cable end over the mounting stud before reinstalling the shift cable to the shift cable bracket. Do not install the shift cable end on the mounting stud with the shift cable installed on the shift cable bracket.

- If the shift cable end does not ride at the bottom of the mounting stud, rotate the stud to align the square fitting with the hole.

- 6.0 mm (0.236 in) Pin - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Center Console - Install

- Shift Cable - After Install Check 1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Check that the back-up lights come on when the transmission is in R position/mode. 6. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 7. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Check that the back-up lights come on when the transmission is in R position/mode. 6. Start the engine.
````

## Chunk 9987: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Procedure

- Title: Shift Cable Removal and Installation (K20C2 (CVT)): Installation: Procedure
- Source path: `pages\12530.html`
- Chunk ID: `chunk_08f73921d0db`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400968.jpeg`, `images\GHH400969.png`, `images\GHH400970.jpeg`, `images\GHH400971.jpeg`, `images\GHH400972.jpeg`, `images\GHH400973.jpeg`, `images\GHH400974.jpeg`
- Duplicate sources: `pages\12534.html`, `pages\13929.html`, `pages\13933.html`

### Full Text

````text
R position/mode. 6. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 7. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Check that the back-up lights come on when the transmission is in R position/mode. 6. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 7. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation.

3. Shift the transmission to P position/mode, and check that the shift lock works properly.

4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P.

5. Check that the back-up lights come on when the transmission is in R position/mode.

6. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

7. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.
````

## Chunk 9988: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Notes

- Title: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Notes
- Source path: `pages\12531.html`
- Chunk ID: `chunk_b74dcb9aa034`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13930.html`

### Full Text

````text
# Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repair or service.

NOTE:

- Where icon is shown, for further information see below.

- Do not bend the shift cable excessively.
````

## Chunk 9989: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Procedure

- Title: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Procedure
- Source path: `pages\12532.html`
- Chunk ID: `chunk_0824ab5c4e34`
- Images: `images\GHH400682.png`, `images\GHH400975.jpeg`, `images\GHH400976.jpeg`, `images\GHH400977.jpeg`
- Duplicate sources: `pages\13931.html`

### Full Text

````text
# Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Removal: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

- Vehicle - Lift

- Center Console - Remove

- Shift Lever - Position Courtesy of HONDA, U.S.A., INC. 1. Insert a 6.0 mm (0.236 in) pin (A) into the positioning holes (B) with the shift lever in R position/mode. NOTE: Use only a 6.0 mm (0.236 in) pin with no burrs.

Courtesy of HONDA, U.S.A., INC. | 1. Insert a 6.0 mm (0.236 in) pin (A) into the positioning holes (B) with the shift lever in R position/mode. NOTE: Use only a 6.0 mm (0.236 in) pin with no burrs.

- Shift Cable (Shift Lever Side) - Remove NOTE: While expanding the lock tab (A), rotate the socket holder retainer (B) counterclockwise until it stops, then remove the socket holder (C). Do not remove the shift cable by pulling the shift cable guide (D). Courtesy of HONDA, U.S.A., INC.

NOTE:

- While expanding the lock tab (A), rotate the socket holder retainer (B) counterclockwise until it stops, then remove the socket holder (C).

- Do not remove the shift cable by pulling the shift cable guide (D).

Courtesy of HONDA, U.S.A., INC.

- Air Cleaner - Remove

- Lock Pin - Remove

- Control Pin - Remove

- Shift Cable Bracket - Remove

- Engine Undercover - Remove

- Heat Shield (Exhaust Pipe A) - Remove

- Shift Cable (Under Side) - Remove
````

## Chunk 9990: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Notes

- Title: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Notes
- Source path: `pages\12533.html`
- Chunk ID: `chunk_a307a93081b6`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13932.html`

### Full Text

````text
# Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repair or service.

NOTE:

- Where icon is shown, for further information see below.

- Do not bend the shift cable excessively.
````

## Chunk 9991: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Procedure

- Title: Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Procedure
- Source path: `pages\12534.html`
- Chunk ID: `chunk_4db6f16a6a7b`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400969.png`, `images\GHH400978.jpeg`, `images\GHH400979.jpeg`, `images\GHH400980.jpeg`, `images\GHH400981.jpeg`, `images\GHH400982.jpeg`, `images\GHH400983.jpeg`
- Duplicate sources: `pages\13933.html`

### Full Text

````text
# Shift Cable Removal and Installation (L15B7/L15BA/L15B7 (CVT)): Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Apply molybdenum grease to inner surface of hole.

- Shift Cable (Under Side) - Install

- Heat Shield (Exhaust Pipe A) - Install

- Engine Undercover - Install

- Shift Cable Bracket - Install

- Control Pin - Install Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the control pin (A) is inserted through the shift cable end (B) and fully seated on the control lever (C).

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the control pin (A) is inserted through the shift cable end (B) and fully seated on the control lever (C).

- Lock Pin - Install Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the lock pin (A) is inserted through the control pin hole (B) to the opening (C) of the control lever (D) so that the hooked end (E) of the lock pin locks into the control pin hole.

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the lock pin (A) is inserted through the control pin hole (B) to the opening (C) of the control lever (D) so that the hooked end (E) of the lock pin locks into the control pin hole.

- Air Cleaner - Install

- Shift Cable - Adjust

- Shift Cable (Shift Lever Side) - Install NOTE: Install the socket holder (A), then rotate the socket holder retainer (B) clockwise until it stops. Do not install the shift cable by holding the shift cable guide (C). Courtesy of HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC. NOTE: Make sure the shift cable end (A) is properly installed on the mounting stud (B). If the cable end is out of position with the mounting stud, remove the shift cable from the shift cable bracket, then reinstall the cable end over the mounting stud before reinstalling the shift cable to the shift cable bracket. Do not install the shift cable end on the mounting stud with the shift cable install on the shift cable bracket. If the shift cable end does not ride at the bottom of the mounting stud, rotate the stud to align the square fitting with the hole.

NOTE:

- Install the socket holder (A), then rotate the socket holder retainer (B) clockwise until it stops.

- Do not install the shift cable by holding the shift cable guide (C).

Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

NOTE: Make sure the shift cable end (A) is properly installed on the mounting stud (B).

- If the cable end is out of position with the mounting stud, remove the shift cable from the shift cable bracket, then reinstall the cable end over the mounting stud before reinstalling the shift cable to the shift cable bracket. Do not install the shift cable end on the mounting stud with the shift cable install on the shift cable bracket.

- If the shift cable end does not ride at the bottom of the mounting stud, rotate the stud to align the square fitting with the hole.

- 6.0 mm (0.236 in) Pin - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Center Console - Install

- Shift Cable - After Install Check 1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Check that the back-up lights come on when the transmission is in R position/mode. 6. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 7. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Check that the back-up lights come on when the transmission is in R position/mode. 6. Start the engine.
````

## Chunk 9992: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12536.html`
- Chunk ID: `chunk_08c00212fc28`
- Images: `images\GHH399704.png`, `images\GHH400984.jpeg`
- Duplicate sources: `pages\13935.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

- Center Console - Remove

- Shift Cable (Shift Lever Side) - Remove

- Connector (Shift Lever) - Disconnect

- Shift Lever - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Be sure to adjust the shift cable before installing the shift cable.

1. Install the parts in the reverse order of removal. NOTE: Be sure to adjust the shift cable before installing the shift cable.

- Shift Lever - After Install Check 1. Turn the vehicle to the ON mode. 2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Turn the vehicle to the ON mode. 2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation.

3. Shift the transmission to P position/mode, and check that the shift lock works properly.

4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P.

5. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.
````

## Chunk 9993: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\12537.html`
- Chunk ID: `chunk_a0524223ffa2`
- Images: none
- Duplicate sources: `pages\13936.html`

### Full Text

````text
# Removal and Installation: Notes

SRS components are located in this area. Review the SRS component locations and the precautions and procedures before doing repair or service.

NOTE: There are two types of shift levers; type A and B. Refer to the CVT System Description - Shift Lock System for more details .
````

## Chunk 9994: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12538.html`
- Chunk ID: `chunk_29538cdf51db`
- Images: `images\GHH399704.png`, `images\GHH400985.jpeg`, `images\GHH400986.jpeg`
- Duplicate sources: `pages\13937.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

Numbered call-outs in figure pertain to list numbers in following procedure.

Torque: N.m (kgf.m, lbf.ft)

- Center Console - Remove

- Shift Cable (Shift Lever Side) - Remove

- Connector (Shift Lever) - Disconnect

- Shift Lever - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.

- Shift Cable - Adjust

- Shift Lever - After Install Check 1. Turn the vehicle to the ON mode. 2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

1. Turn the vehicle to the ON mode. 2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation. 3. Shift the transmission to P position/mode, and check that the shift lock works properly. 4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P. 5. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.

2. Move the shift lever to each position, and check that the shift position indicator follows the shift lever operation.

3. Shift the transmission to P position/mode, and check that the shift lock works properly.

4. Push the shift lock release, and check that the shift lever releases. Also check that the shift lever locks when it is shifted back to P.

5. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

6. Make sure the vehicle is turned to the OFF (LOCK) mode with the shift lever in P position/mode. If it does not, adjust the shift cable again.
````

## Chunk 9995: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12539.html`
- Chunk ID: `chunk_0dec03ed4182`
- Images: `images\GHH400987.jpeg`
- Duplicate sources: `pages\13938.html`

### Full Text

````text
# Removal and Installation

NOTE: Keep all foreign particles out of the transmission.

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Transmission Fluid Pan - Remove NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

- Shift Solenoid Valve O/P - Remove Fig 1: Shift Solenoid Valve O/P Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A). 2. Remove the shift solenoid valve O/P (B).

1. Disconnect the connector (A). 2. Remove the shift solenoid valve O/P (B).

2. Remove the shift solenoid valve O/P (B).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal.

1. Install the parts in the reverse order of removal.

- Transmission Fluid - Refill

- Transmission Fluid Level - Check
````

## Chunk 9996: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12540.html`
- Chunk ID: `chunk_f13b7a53bbd6`
- Images: `images\GHH400988.jpeg`
- Duplicate sources: `pages\13939.html`

### Full Text

````text
# Removal and Installation

- Air Cleaner - Remove

- Intake Air Duct - Remove

- TCM - Remove Fig 1: TCM Replacement Components With Torque Specifications And Connector Disconnection Sequence (K20C2 - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Remove the TCM (D).

1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Remove the TCM (D).

2. Remove the TCM (D).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. Make sure the connector is fully seated. Procedure After Replacing TCM

1. Install the parts in the reverse order of removal. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. Make sure the connector is fully seated.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Make sure the connector is fully seated.

Procedure After Replacing TCM

- TCM - Update
````

## Chunk 9997: Removal and Installation

- Title: Removal and Installation
- Source path: `pages\12541.html`
- Chunk ID: `chunk_df0648ea0d72`
- Images: `images\GHH400989.jpeg`
- Duplicate sources: `pages\13940.html`

### Full Text

````text
# Removal and Installation

- TCM - Remove Fig 1: TCM Replacement Components With Torque Specifications And Connector Disconnection Sequence (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Remove the TCM (D).

1. Disconnect the connector (A) by pushing the lock (B) and pulling the lever (C) in the numbered sequence shown. 2. Remove the TCM (D).

2. Remove the TCM (D).

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. Make sure the connector is fully seated. Procedure After Replacing TCM

1. Install the parts in the reverse order of removal. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary. Make sure the connector is fully seated.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Make sure the connector is fully seated.

Procedure After Replacing TCM

- TCM - Update
````

## Chunk 9998: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12543.html`
- Chunk ID: `chunk_ccd0dfa2d5d0`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400990.jpeg`, `images\GHH400991.jpeg`, `images\GHH400992.jpeg`, `images\GHH400993.jpeg`
- Duplicate sources: `pages\13942.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Transmission Fluid Pan - Remove NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

- Magnet - Remove

- Transmission Fluid Strainer - Remove

- Transmission Fluid Strainer - Check Courtesy of HONDA, U.S.A., INC. 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

Courtesy of HONDA, U.S.A., INC. | 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

2. Check that it is in good condition and that the inlet opening is not clogged.

3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

- Valve Body Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the valve body assembly mounting bolts. Bolt Length A 90 mm (3.54 in) B 65 mm (2.56 in) Courtesy of HONDA, U.S.A., INC. 2. Remove the valve body assembly (A) straightly and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the valve body assembly mounting bolts.

Bolt | Length

A | 90 mm (3.54 in)

B | 65 mm (2.56 in)

Courtesy of HONDA, U.S.A., INC. | 2. Remove the valve body assembly (A) straightly and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

- 10.9 x 29 mm Pipe - Remove

- 10.9 x 48 mm Pipe - Remove

- 10.9 x 75.5 mm Pipe - Remove

- 18 x 21 mm Pipe - Remove

- Transmission Fluid Pump - Remove

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Be careful not to damage the O-rings. Do not pinch the solenoid wire harnesses. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Be careful not to damage the O-rings. Do not pinch the solenoid wire harnesses. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Be careful not to damage the O-rings.

- Do not pinch the solenoid wire harnesses.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Transmission Fluid - Refill

- TCM - Reset (Only for Replacing Transmission Fluid Pump and/or Valve Body Assembly) NOTE: This procedure is not required, if the TCM, and the transmission fluid pump and/or the valve body assembly are replaced simultaneously.

NOTE: This procedure is not required, if the TCM, and the transmission fluid pump and/or the valve body assembly are replaced simultaneously.
````

## Chunk 9999: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes

- Title: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes
- Source path: `pages\12544.html`
- Chunk ID: `chunk_3ff96f421ed8`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13943.html`

### Full Text

````text
# Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.
````

## Chunk 10000: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure

- Title: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure
- Source path: `pages\12545.html`
- Chunk ID: `chunk_a6b10deea992`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400994.jpeg`, `images\GHH400995.jpeg`, `images\GHH400996.jpeg`, `images\GHH400997.jpeg`, `images\GHH400998.jpeg`
- Duplicate sources: `pages\13944.html`

### Full Text

````text
# Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Transmission Fluid Pan - Remove NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

- Magnet - Remove

- Transmission Fluid Strainer - Remove

- Transmission Fluid Strainer - Check Courtesy of HONDA, U.S.A., INC. 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

Courtesy of HONDA, U.S.A., INC. | 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

2. Check that it is in good condition and that the inlet opening is not clogged.

3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

- Valve Body Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the transmission fluid temperature sensor (A). 2. Disconnect the connectors (B). Courtesy of HONDA, U.S.A., INC. 3. Remove the guide plate (A). 4. Remove the valve body assembly (B) straightly. NOTE: Do not remove the bolts with no ↓ marked on. Check that the valve body assembly is free of solenoid wire harness A. Be careful not to damage solenoid wire harness A.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the transmission fluid temperature sensor (A). 2. Disconnect the connectors (B).

2. Disconnect the connectors (B).

Courtesy of HONDA, U.S.A., INC. | 3. Remove the guide plate (A). 4. Remove the valve body assembly (B) straightly. NOTE: Do not remove the bolts with no ↓ marked on. Check that the valve body assembly is free of solenoid wire harness A. Be careful not to damage solenoid wire harness A.

4. Remove the valve body assembly (B) straightly.

NOTE:

- Do not remove the bolts with no ↓ marked on.

- Check that the valve body assembly is free of solenoid wire harness A.

- Be careful not to damage solenoid wire harness A.

- 10.9 x 26 mm Pipe - Remove

- 8 x 133.5 mm Pipe - Remove

- 12 x 56.7 mm Pipe - Remove

- Joint Pipe - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Be careful not to drop the filter (A).

Courtesy of HONDA, U.S.A., INC.

NOTE: Be careful not to drop the filter (A).

- 10.9 x 18.5 mm Pipe - Remove

- 14.3 x 36.2 mm Pipe - Remove

- 18 x 18 mm Pipe - Remove

- Transmission Fluid Pump - Remove
````

## Chunk 10001: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes

- Title: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes
- Source path: `pages\12546.html`
- Chunk ID: `chunk_1a6b8db4ba77`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13945.html`

### Full Text

````text
# Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Be careful not to damage the O-rings.
````

## Chunk 10002: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure

- Title: Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure
- Source path: `pages\12547.html`
- Chunk ID: `chunk_c12921e3533b`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH400999.jpeg`, `images\GHH401000.jpeg`, `images\GHH401001.jpeg`, `images\GHH401002.jpeg`, `images\GHH401003.jpeg`
- Duplicate sources: `pages\13946.html`

### Full Text

````text
# Transmission Fluid Pump Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Transmission Fluid Pump - Install Courtesy of HONDA, U.S.A., INC. NOTE: Apply transmission fluid to the transmission fluid pump shaft splines (A). Align the guide pin (B) of the transmission fluid pump with the guide hole (C) of the stator shaft flange.

Courtesy of HONDA, U.S.A., INC.

NOTE:

- Apply transmission fluid to the transmission fluid pump shaft splines (A).

- Align the guide pin (B) of the transmission fluid pump with the guide hole (C) of the stator shaft flange.

- 18 x 18 mm Pipe - Install

- 14.3 x 36.2 mm Pipe - Install NOTE: You can install the pipe regardless of its direction.

NOTE: You can install the pipe regardless of its direction.

- 10.9 x 18.5 mm Pipe - Install

- Joint Pipe - Install Courtesy of HONDA, U.S.A., INC. NOTE: The joint pipe has the filter (A). The filter end should face the valve body assembly side. Be careful not to drop the filter.

Courtesy of HONDA, U.S.A., INC.

NOTE:

- The joint pipe has the filter (A). The filter end should face the valve body assembly side.

- Be careful not to drop the filter.

- 12 x 56.7 mm Pipe - Install NOTE: You can install the pipe regardless of its direction.

NOTE: You can install the pipe regardless of its direction.

- 8 x 133.5 mm Pipe - Install

- 10.9 x 26 mm Pipe - Install

- Valve Body Assembly - Install Courtesy of HONDA, U.S.A., INC. 1. Install the valve body assembly (A) straightly. NOTE: Do not pinch solenoid wire harnesses A and B. 2. Install the guide plate (G). Bolt Length B 90 mm (3.54 in) C 80 mm (3.15 in) D 65 mm (2.56 in) E 55 mm (2.17 in) F 40 mm (1.57 in) Courtesy of HONDA, U.S.A., INC. 3. Make sure each branch of solenoid wire harness A goes through the appropriate location, especially as shown, one (B) must be located to the inside from the other (C). 4. Connect the connectors (D). 5. Install the transmission fluid temperature sensor (E).

Courtesy of HONDA, U.S.A., INC. | 1. Install the valve body assembly (A) straightly. NOTE: Do not pinch solenoid wire harnesses A and B. 2. Install the guide plate (G).

2. Install the guide plate (G).

Bolt | Length

B | 90 mm (3.54 in)

C | 80 mm (3.15 in)

D | 65 mm (2.56 in)

E | 55 mm (2.17 in)

F | 40 mm (1.57 in)

Courtesy of HONDA, U.S.A., INC. | 3. Make sure each branch of solenoid wire harness A goes through the appropriate location, especially as shown, one (B) must be located to the inside from the other (C). 4. Connect the connectors (D). 5. Install the transmission fluid temperature sensor (E).

4. Connect the connectors (D).

5. Install the transmission fluid temperature sensor (E).

- Transmission Fluid Strainer - Install NOTE: Do not pinch solenoid wire harnesses A and B.

NOTE: Do not pinch solenoid wire harnesses A and B.

- Magnet - Install

- Transmission Fluid Pan - Install NOTE: Tighten the transmission fluid pan mounting bolts in a crisscross pattern in at least two steps. Do not pinch solenoid wire harnesses A and B.

NOTE:

- Tighten the transmission fluid pan mounting bolts in a crisscross pattern in at least two steps.

- Do not pinch solenoid wire harnesses A and B.

- Transmission Fluid - Refill

- Transmission Fluid Level - Check

- Engine Undercover Plate - Install

- TCM - Reset (Only for Replacing Transmission Fluid Pump and/or Valve Body Assembly) NOTE: This procedure is not required, if the TCM, and the transmission fluid pump and/or the valve body assembly are replaced simultaneously.

NOTE: This procedure is not required, if the TCM, and the transmission fluid pump and/or the valve body assembly are replaced simultaneously.
````

## Chunk 10003: Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Title: Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal
- Source path: `pages\12548.html`
- Chunk ID: `chunk_ae8774e322de`
- Images: `images\GHH401004.jpeg`, `images\GHH401005.jpeg`
- Duplicate sources: `pages\13947.html`

### Full Text

````text
# Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal

- Air Cleaner - Remove

- Intake Air Duct E - Remove

- TCM Harness - Remove Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Transmission Range Switch - Remove Fig 1: Transmission Range Switch Components With Connector Disconnection Sequence (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 1. Disconnect the connector (A) by pulling the lock (B) and the lever (C) in the numbered sequence shown. 2. Apply the parking brake. 3. Shift the transmission to N position/mode. 4. Remove the control shaft cover (D). 5. Remove the transmission range switch (E).

1. Disconnect the connector (A) by pulling the lock (B) and the lever (C) in the numbered sequence shown. 2. Apply the parking brake. 3. Shift the transmission to N position/mode. 4. Remove the control shaft cover (D). 5. Remove the transmission range switch (E).

2. Apply the parking brake.

3. Shift the transmission to N position/mode.

4. Remove the control shaft cover (D).

5. Remove the transmission range switch (E).
````

## Chunk 10004: Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Title: Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation
- Source path: `pages\12549.html`
- Chunk ID: `chunk_1cb58804205d`
- Images: `images\GHH401006.jpeg`, `images\GHH401007.jpeg`
- Duplicate sources: `pages\13948.html`

### Full Text

````text
# Transmission Range Switch Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation

- Transmission Range Switch - Install 1. Make sure the control lever (A) is in the N position. If necessary, move the control lever to the N position. NOTE: Do not use the control shaft (B) to adjust the shift position. If the control shaft tips are squeezed together, it will cause a faulty signal or position due to play between the control shaft and the transmission range switch. Fig 1: Exploded View Of Transmission Range Switch Components With Torque Specifications (L15B7/L15BA/L15BY - CVT) Courtesy of HONDA, U.S.A., INC. 2. Set the transmission range switch (C) to the N position. Align the cutouts (D) on the rotary-frame with the N positioning cutouts (E) on the transmission range switch, then put a 2.0 mm (0.079 in) feeler gauge blade (F) in the cutouts to hold the transmission range switch in the N position. NOTE: Be sure to use a 2.0 mm (0.079 in) feeler gauge blade or equivalent to hold the transmission range switch in the N position. 3. Loosely install the transmission range switch gently on the control shaft while holding it in the N position with the 2.0 mm (0.079 in) feeler gauge blade. 4. Tighten the bolts (G) on the transmission range switch while you continue holding the N position. NOTE: Do not move the transmission range switch when tightening the bolts. 5. Remove the feeler gauge. 6. Install the control shaft cover (H). 7. Connect the connector (J), and make sure it is fully seated. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Make sure the control lever (A) is in the N position. If necessary, move the control lever to the N position.

NOTE: Do not use the control shaft (B) to adjust the shift position. If the control shaft tips are squeezed together, it will cause a faulty signal or position due to play between the control shaft and the transmission range switch.

2. Set the transmission range switch (C) to the N position. Align the cutouts (D) on the rotary-frame with the N positioning cutouts (E) on the transmission range switch, then put a 2.0 mm (0.079 in) feeler gauge blade (F) in the cutouts to hold the transmission range switch in the N position.

NOTE: Be sure to use a 2.0 mm (0.079 in) feeler gauge blade or equivalent to hold the transmission range switch in the N position.

3. Loosely install the transmission range switch gently on the control shaft while holding it in the N position with the 2.0 mm (0.079 in) feeler gauge blade.

4. Tighten the bolts (G) on the transmission range switch while you continue holding the N position.

NOTE: Do not move the transmission range switch when tightening the bolts.

5. Remove the feeler gauge.

6. Install the control shaft cover (H).

7. Connect the connector (J), and make sure it is fully seated.

NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- TCM Harness - Install Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Intake Air Duct E - Install

- Air Cleaner - Install

- Transmission Range Switch - After Install Check 1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 4. Check that the back-up lights come on when the transmission is in R position/mode.

1. Turn the vehicle to the ON mode. 2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation. 3. Start the engine. NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes. 4. Check that the back-up lights come on when the transmission is in R position/mode.

2. Move the shift lever through all positions/modes, and check that the shift position indicator follows the shift lever operation.

3. Start the engine.

NOTE: Check that the engine starts in P or N position/mode, and does not start in any other positions/modes.

4. Check that the back-up lights come on when the transmission is in R position/mode.
````

## Chunk 10005: Removal and Installation: Notes

- Title: Removal and Installation: Notes
- Source path: `pages\12550.html`
- Chunk ID: `chunk_d8d49f24654d`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13949.html`

### Full Text

````text
# Removal and Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.

- The solenoid wire harness and the transmission fluid temperature sensor are not available separately. Replace them as a set.

- The valve body assembly and the following parts are not available separately. Replace them as a set.

- CVT clutch pressure control solenoid valve

- CVT clutch pressure control solenoid valve

- CVT drive pulley pressure control solenoid valve

- CVT drive pulley pressure control solenoid valve

- CVT driven pulley pressure control solenoid valve

- CVT driven pulley pressure control solenoid valve

- CVT lock-up clutch control solenoid valve

- CVT lock-up clutch control solenoid valve

- Shift solenoid valve B

- Shift solenoid valve B
````

## Chunk 10006: Removal and Installation: Procedure

- Title: Removal and Installation: Procedure
- Source path: `pages\12551.html`
- Chunk ID: `chunk_679f9330592c`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401008.jpeg`, `images\GHH401009.jpeg`, `images\GHH401010.jpeg`, `images\GHH401011.jpeg`, `images\GHH401012.jpeg`
- Duplicate sources: `pages\13950.html`

### Full Text

````text
# Removal and Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Transmission Fluid Pan - Remove NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

- Magnet - Remove

- Transmission Fluid Strainer - Remove

- Transmission Fluid Strainer - Check Courtesy of HONDA, U.S.A., INC. 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

Courtesy of HONDA, U.S.A., INC. | 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

2. Check that it is in good condition and that the inlet opening is not clogged.

3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

- Valve Body Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the valve body assembly mounting bolts. Bolt Length B 65 mm (2.56 in) Bolt Length A 90 mm (3.54 in) Courtesy of HONDA, U.S.A., INC. 2. Remove the valve body assembly (A) straightly and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the valve body assembly mounting bolts.

Bolt | Length

B | 65 mm (2.56 in)

Bolt | Length

A | 90 mm (3.54 in)

Courtesy of HONDA, U.S.A., INC. | 2. Remove the valve body assembly (A) straightly and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

- 10.9 x 29 mm Pipe - Remove

- 10.9 x 48 mm Pipe - Remove

- 10.9 x 75.5 mm Pipe - Remove

- 18 x 21 mm Pipe - Remove

- Solenoid Wire Harness - Remove Solenoid Wire Harness Location Courtesy of HONDA, U.S.A., INC.

Solenoid Wire Harness Location

Courtesy of HONDA, U.S.A., INC.

- All Removed Parts - Install 1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Be careful not to damage the O-rings. Do not pinch the solenoid wire harnesses. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

1. Install the parts in the reverse order of removal. NOTE: Apply a light coat of clean transmission fluid on all O-rings before installation. Be careful not to damage the O-rings. Do not pinch the solenoid wire harnesses. Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Be careful not to damage the O-rings.

- Do not pinch the solenoid wire harnesses.

- Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Transmission Fluid - Refill

- TCM - Reset (Only for Replacing Valve Body Assembly) NOTE: This procedure is not required, if the valve body assembly and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the valve body assembly and the TCM are replaced simultaneously.
````

## Chunk 10007: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes

- Title: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes
- Source path: `pages\12552.html`
- Chunk ID: `chunk_aa9fd3c41d4d`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13951.html`

### Full Text

````text
# Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.

- Solenoid wire harness A and the transmission fluid temperature sensor are not available separately. Replace them as a set.

- The valve body assembly and the following parts are not available separately. Replace them as a set.

- CVT clutch pressure control solenoid valve CVT drive pulley pressure control solenoid valve CVT driven pulley pressure control solenoid valve CVT lock-up clutch control solenoid valve Shift solenoid valve B Solenoid wire harness B

- CVT clutch pressure control solenoid valve

- CVT drive pulley pressure control solenoid valve

- CVT driven pulley pressure control solenoid valve

- CVT lock-up clutch control solenoid valve

- Shift solenoid valve B

- Solenoid wire harness B
````

## Chunk 10008: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure

- Title: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure
- Source path: `pages\12553.html`
- Chunk ID: `chunk_87a5069ea366`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401013.jpeg`, `images\GHH401014.jpeg`, `images\GHH401015.jpeg`, `images\GHH401016.jpeg`, `images\GHH401017.jpeg`, `images\GHH401018.jpeg`
- Duplicate sources: `pages\13952.html`

### Full Text

````text
# Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Removal: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

- Vehicle - Lift

- Engine Undercover Plate - Remove

- Engine - Warm Up 1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

1. Start the engine, and warm it up to normal operating temperature (the radiator fan comes on twice). 2. Turn the engine off.

2. Turn the engine off.

- Transmission Fluid - Drain

- Connector (Solenoid Wire Harness A) - Disconnect Courtesy of HONDA, U.S.A., INC.

Courtesy of HONDA, U.S.A., INC.

- Transmission Fluid Pan - Remove NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

NOTE: The actual transmission fluid (HCF-2) capacity will vary from the specified capacity based on the length of time the transmission fluid pan is off the transmission. Avoid leaving the transmission fluid pan off for extend periods of time.

- Magnet - Remove

- Transmission Fluid Strainer - Remove

- Transmission Fluid Strainer - Check Courtesy of HONDA, U.S.A., INC. 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

Courtesy of HONDA, U.S.A., INC. | 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

2. Check that it is in good condition and that the inlet opening is not clogged.

3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

- Valve Body Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the transmission fluid temperature sensor (A). 2. Disconnect the connectors (B). Courtesy of HONDA, U.S.A., INC. 3. Remove the guide plate (A). 4. Remove the valve body assembly (B) straightly. NOTE: Do not remove the bolts with no ↓ marked on. Check that the valve body assembly is free of solenoid wire harness A. Be careful not to damage solenoid wire harness A.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the transmission fluid temperature sensor (A). 2. Disconnect the connectors (B).

2. Disconnect the connectors (B).

Courtesy of HONDA, U.S.A., INC. | 3. Remove the guide plate (A). 4. Remove the valve body assembly (B) straightly. NOTE: Do not remove the bolts with no ↓ marked on. Check that the valve body assembly is free of solenoid wire harness A. Be careful not to damage solenoid wire harness A.

4. Remove the valve body assembly (B) straightly.

NOTE:

- Do not remove the bolts with no ↓ marked on.

- Check that the valve body assembly is free of solenoid wire harness A.

- Be careful not to damage solenoid wire harness A.

- 10.9 x 26 mm Pipe - Remove

- 8 x 133.5 mm Pipe - Remove

- 12 x 56.7 mm Pipe - Remove

- Joint Pipe - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Be careful not to drop the filter (A).

Courtesy of HONDA, U.S.A., INC.

NOTE: Be careful not to drop the filter (A).

- 10.9 x 18.5 mm Pipe - Remove

- 14.3 x 36.2 mm Pipe - Remove

- 18 x 18 mm Pipe - Remove

- Solenoid Wire Harness A - Remove
````

## Chunk 10009: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes

- Title: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes
- Source path: `pages\12554.html`
- Chunk ID: `chunk_9baf6b8c8a42`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13953.html`

### Full Text

````text
# Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.

- Apply a light coat of clean transmission fluid on all O-rings before installation.

- Be careful not to damage the O-rings.

- Solenoid wire harness A and the transmission fluid temperature sensor are not available separately. Replace them as a set.

- The valve body assembly and the following parts are not available separately. Replace them as a set.

- CVT clutch pressure control solenoid valve CVT drive pulley pressure control solenoid valve CVT driven pulley pressure control solenoid valve CVT lock-up clutch control solenoid valve Shift solenoid valve B Solenoid wire harness B

- CVT clutch pressure control solenoid valve

- CVT drive pulley pressure control solenoid valve

- CVT driven pulley pressure control solenoid valve

- CVT lock-up clutch control solenoid valve

- Shift solenoid valve B

- Solenoid wire harness B
````

## Chunk 10010: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure

- Title: Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure
- Source path: `pages\12555.html`
- Chunk ID: `chunk_8b61f04e6d36`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401019.jpeg`, `images\GHH401020.jpeg`, `images\GHH401021.jpeg`, `images\GHH401022.jpeg`, `images\GHH401023.jpeg`
- Duplicate sources: `pages\13954.html`

### Full Text

````text
# Valve Body Assembly Removal and Installation (L15B7/L15BA/L15BY (CVT)): Installation: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Solenoid Wire Harness A - Install

- 18 x 18 mm Pipe - Install

- 14.3 x 36.2 mm Pipe - Install NOTE: You can install the pipe regardless of its direction.

NOTE: You can install the pipe regardless of its direction.

- 10.9 x 18.5 mm Pipe - Install

- Joint Pipe - Install Courtesy of HONDA, U.S.A., INC. NOTE: The joint pipe has the filter (A). The filter end should face the valve body assembly side. Be careful not to drop the filter.

Courtesy of HONDA, U.S.A., INC.

NOTE:

- The joint pipe has the filter (A). The filter end should face the valve body assembly side.

- Be careful not to drop the filter.

- 12 x 56.7 mm Pipe - Install NOTE: You can install the pipe regardless of its direction.

NOTE: You can install the pipe regardless of its direction.

- 8 x 133.5 mm Pipe - Install

- 10.9 x 26 mm Pipe - Install

- Valve Body Assembly - Install Courtesy of HONDA, U.S.A., INC. 1. Install the valve body assembly (A) straightly. NOTE: Do not pinch solenoid wire harnesses A and B. 2. Install the guide plate (G). Bolt Length B 90 mm (3.54 in) C 80 mm (3.15 in) D 65 mm (2.56 in) E 55 mm (2.17 in) F 40 mm (1.57 in) Courtesy of HONDA, U.S.A., INC. 3. Make sure each branch of solenoid wire harness A goes through the appropriate location, especially as shown, one (B) must be located to the inside from the other (C). 4. Connect the connectors (D). 5. Install the transmission fluid temperature sensor (E).

Courtesy of HONDA, U.S.A., INC. | 1. Install the valve body assembly (A) straightly. NOTE: Do not pinch solenoid wire harnesses A and B. 2. Install the guide plate (G).

2. Install the guide plate (G).

Bolt | Length

B | 90 mm (3.54 in)

C | 80 mm (3.15 in)

D | 65 mm (2.56 in)

E | 55 mm (2.17 in)

F | 40 mm (1.57 in)

Courtesy of HONDA, U.S.A., INC. | 3. Make sure each branch of solenoid wire harness A goes through the appropriate location, especially as shown, one (B) must be located to the inside from the other (C). 4. Connect the connectors (D). 5. Install the transmission fluid temperature sensor (E).

4. Connect the connectors (D).

5. Install the transmission fluid temperature sensor (E).

- Transmission Fluid Strainer - Install NOTE: Do not pinch solenoid wire harnesses A and B.

NOTE: Do not pinch solenoid wire harnesses A and B.

- Magnet - Install

- Transmission Fluid Pan - Install NOTE: Tighten the transmission fluid pan mounting bolts in a crisscross pattern in at least two steps. Do not pinch solenoid wire harnesses A and B.

NOTE:

- Tighten the transmission fluid pan mounting bolts in a crisscross pattern in at least two steps.

- Do not pinch solenoid wire harnesses A and B.

- Connector (Solenoid Wire Harness A) - Connect Courtesy of HONDA, U.S.A., INC. NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

Courtesy of HONDA, U.S.A., INC.

NOTE: Check the connector for corrosion, dirt, or oil, and clean or repair if necessary.

- Transmission Fluid - Refill

- Transmission Fluid Level - Check

- Engine Undercover Plate - Install

- TCM - Reset (Only for Replacing Valve Body Assembly) NOTE: This procedure is not required, if the valve body assembly and the TCM are replaced simultaneously.

NOTE: This procedure is not required, if the valve body assembly and the TCM are replaced simultaneously.
````

## Chunk 10011: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Notes
- Source path: `pages\12556.html`
- Chunk ID: `chunk_8507c5205450`
- Images: `images\GHH2296.png`
- Duplicate sources: `pages\13955.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Installer Attachment 40 mm 07LAD-PW50601
````

## Chunk 10012: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes
- Source path: `pages\12557.html`
- Chunk ID: `chunk_e3fc324c1a0f`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13956.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- The carrier bearing and the carrier bearing outer race should be replaced as a set.
````

## Chunk 10013: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

- Title: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure
- Source path: `pages\12558.html`
- Chunk ID: `chunk_b32c37fed422`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401024.jpeg`, `images\GHH401025.jpeg`, `images\GHH401026.jpeg`
- Duplicate sources: `pages\13957.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

*1 | Left-hand threads

- Final Driven Gear - Remove

- Differential Carrier Tapered Roller Bearing - Remove Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Set a commercially available bearing puller (A) under the carrier bearings (B) as shown. 2. Remove the carrier bearings using the commercially available bearing puller and a commercially available spacer (C).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Set a commercially available bearing puller (A) under the carrier bearings (B) as shown. 2. Remove the carrier bearings using the commercially available bearing puller and a commercially available spacer (C).

2. Remove the carrier bearings using the commercially available bearing puller and a commercially available spacer (C).
````

## Chunk 10014: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes
- Source path: `pages\12559.html`
- Chunk ID: `chunk_1f18eb72593b`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13958.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- The carrier bearing and the carrier bearing outer race should be replaced as a set.

- Adjust the carrier bearing preload after replacing the carrier bearing and the carrier bearing outer race.

- Apply a light coat of clean transmission fluid on all parts before installation.
````

## Chunk 10015: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12560.html`
- Chunk ID: `chunk_8dbb95f1ff26`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401027.jpeg`, `images\GHH401028.jpeg`
- Duplicate sources: `pages\13959.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

*1 | Left-hand threads

- Differential Carrier Tapered Roller Bearing - Install Courtesy of HONDA, U.S.A., INC. 1. Install the carrier bearings (A) until it bottoms using the 40 mm installer attachment and a press.

Courtesy of HONDA, U.S.A., INC. | 1. Install the carrier bearings (A) until it bottoms using the 40 mm installer attachment and a press.

- Final Driven Gear - Install NOTE: Tighten the final driven gear bolts to the specified torque in a crisscross pattern in at least two steps.

NOTE: Tighten the final driven gear bolts to the specified torque in a crisscross pattern in at least two steps.
````

## Chunk 10016: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Notes
- Source path: `pages\12561.html`
- Chunk ID: `chunk_b86de0c97b4a`
- Images: `images\GHH1525.png`, `images\GHH174163.png`, `images\GHH2296.png`
- Duplicate sources: `pages\13960.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Driver Handle, 15 x 135L 07749-0010000

Courtesy of HONDA, U.S.A., INC. | Oil Seal Driver Attachment, 66 mm 07MAD-SP00100

Courtesy of HONDA, U.S.A., INC. | Installer Attachment 40 mm 07LAD-PW50601
````

## Chunk 10017: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Notes
- Source path: `pages\12562.html`
- Chunk ID: `chunk_1294f30006d2`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13961.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- The bearing and the bearing outer race should be replaced as a set.
````

## Chunk 10018: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Procedure

- Title: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Procedure
- Source path: `pages\12563.html`
- Chunk ID: `chunk_ae03e072527d`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401029.jpeg`, `images\GHH401030.jpeg`, `images\GHH401031.jpeg`
- Duplicate sources: `pages\13962.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Disassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

*1 | Left-hand threads

- Final Driven Gear - Remove

- Differential Carrier Tapered Roller Bearing - Remove Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. 1. Set a commercially available bearing puller (A) under the differential carrier tapered roller bearings (B) as shown. 2. Remove the bearings using the commercially available bearing puller and a commercially available spacer (C).

Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. Courtesy of HONDA, U.S.A., INC.HONDA, U.S.A., INC. | 1. Set a commercially available bearing puller (A) under the differential carrier tapered roller bearings (B) as shown. 2. Remove the bearings using the commercially available bearing puller and a commercially available spacer (C).

2. Remove the bearings using the commercially available bearing puller and a commercially available spacer (C).
````

## Chunk 10019: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Notes

- Title: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Notes
- Source path: `pages\12564.html`
- Chunk ID: `chunk_c0782d5a9da4`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13963.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- The bearing and the bearing outer race should be replaced as a set.

- Adjust the differential carrier tapered roller bearing preload whenever the bearing and the bearing outer race are replaced.

- Apply a light coat of clean transmission fluid on all parts before installation.
````

## Chunk 10020: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Procedure

- Title: CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Procedure
- Source path: `pages\12565.html`
- Chunk ID: `chunk_8ed42c268b69`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401032.jpeg`, `images\GHH401033.jpeg`, `images\GHH401034.jpeg`, `images\GHH401035.jpeg`
- Duplicate sources: `pages\13964.html`

### Full Text

````text
# CVT Differential Carrier Disassembly and Reassembly (L15B7/L15BA/L15BY (CVT)): Reassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

*1 | Left-hand threads

- Differential Carrier Tapered Roller Bearing - Install Courtesy of HONDA, U.S.A., INC. Transmission Housing Side 1. Install the differential carrier tapered roller bearing (A) until it bottoms using the 15 x 135L driver handle, the 66 mm oil seal driver attachment, and a press. Courtesy of HONDA, U.S.A., INC. Torque Converter Housing Side 2. Install the differential carrier tapered roller bearing (A) until it bottoms using the 40 mm installer attachment and a press.

Courtesy of HONDA, U.S.A., INC. | Transmission Housing Side 1. Install the differential carrier tapered roller bearing (A) until it bottoms using the 15 x 135L driver handle, the 66 mm oil seal driver attachment, and a press.

Transmission Housing Side

1. Install the differential carrier tapered roller bearing (A) until it bottoms using the 15 x 135L driver handle, the 66 mm oil seal driver attachment, and a press.

Courtesy of HONDA, U.S.A., INC. | Torque Converter Housing Side 2. Install the differential carrier tapered roller bearing (A) until it bottoms using the 40 mm installer attachment and a press.

Torque Converter Housing Side

2. Install the differential carrier tapered roller bearing (A) until it bottoms using the 40 mm installer attachment and a press.

- Final Driven Gear - Install NOTE: Tighten the final driven gear bolts to the specified torque in a crisscross pattern in at least two steps. Make sure the final driven gear is installed in the correct direction. Make sure to assemble the final drive shaft and the final driven gear correctly (Combination A or B) as shown in the chart if either one of them or both are to be replaced. Correct combinations of the shaft and gear can be identified by the presence or the absence of the groove as shown in the chart. Courtesy of HONDA, U.S.A., INC.

NOTE:

- Tighten the final driven gear bolts to the specified torque in a crisscross pattern in at least two steps.

- Make sure the final driven gear is installed in the correct direction.

- Make sure to assemble the final drive shaft and the final driven gear correctly (Combination A or B) as shown in the chart if either one of them or both are to be replaced. Correct combinations of the shaft and gear can be identified by the presence or the absence of the groove as shown in the chart.

Courtesy of HONDA, U.S.A., INC.
````

## Chunk 10021: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Notes

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Notes
- Source path: `pages\12566.html`
- Chunk ID: `chunk_a06e1bdbbb84`
- Images: `images\GHH1522.png`, `images\GHH1525.png`, `images\GHH1527.png`, `images\GHH1528.png`, `images\GHH173952.png`, `images\GHH2528.png`, `images\GHH3748.png`, `images\GHH3765.png`, `images\GHH4392.png`, `images\GHH4393.png`, `images\GHH4576.png`, `images\GHH4577.png`, `images\GHH4630.png`, `images\GHH4776.png`, `images\GHH4932.png`, `images\GHH4972.png`
- Duplicate sources: `pages\13965.html`

### Full Text

````text
# CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Notes

Special Tools Required

Image | Description/Tool Number

Courtesy of HONDA, U.S.A., INC. | Reverse Brake Spring Compressor Set 070AF-5T0A100

Courtesy of HONDA, U.S.A., INC. | Adjustable Bearing Puller, 25-40 mm 07736-A01000B*

Courtesy of HONDA, U.S.A., INC. | Bearing Driver Attachment, 52 x 55 mm 07746-0010400

Courtesy of HONDA, U.S.A., INC. | Bearing Driver Attachment, 62 x 68 mm 07746-0010500

Courtesy of HONDA, U.S.A., INC. | Attachment, 22 x 24 mm 07746-001A800

Courtesy of HONDA, U.S.A., INC. | Driver Handle, 40 mm I.D. 07746-0030100

Courtesy of HONDA, U.S.A., INC. | Bearing Driver Attachment, 30 mm I.D. 07746-0030300

Courtesy of HONDA, U.S.A., INC. | Driver Handle, 15 x 135L 07749-0010000

Courtesy of HONDA, U.S.A., INC. | Bearing Driver Attachment, 62 x 64 mm 07947-6340400

Courtesy of HONDA, U.S.A., INC. | Oil Seal Driver Attachment, 71.5 mm 07GAD-SE00100

Courtesy of HONDA, U.S.A., INC. | Oil Seal Driver Attachment, 58 mm 07JAD-PH80101

Courtesy of HONDA, U.S.A., INC. | Oil Seal Driver, 65 mm 07JAD-PL9A100

Courtesy of HONDA, U.S.A., INC. | Snap Ring Pliers 07LGC-0010100

Courtesy of HONDA, U.S.A., INC. | Adjustable Bearing Puller, 45-75 mm 07YAC-0010102*

Courtesy of HONDA, U.S.A., INC. | Clutch Compressor Attachment 07ZAE-PRP0100

Courtesy of HONDA, U.S.A., INC. | Clutch Compressor Attachment 64 mm 07ZAE-PRPA110

*: This tool must be used with a commercially available 3/8"-16 slide hammer.
````

## Chunk 10022: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes
- Source path: `pages\12567.html`
- Chunk ID: `chunk_cd8556fe2e53`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13966.html`

### Full Text

````text
# CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- Mark or place all removed parts in order in a parts rack so they can be reassembled in their original places.

- Keep all foreign particles out of the transmission.
````

## Chunk 10023: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure
- Source path: `pages\12568.html`
- Chunk ID: `chunk_0e742f8d5e12`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401036.jpeg`, `images\GHH401037.jpeg`, `images\GHH401038.jpeg`, `images\GHH401039.jpeg`, `images\GHH401040.jpeg`, `images\GHH401041.jpeg`, `images\GHH401042.jpeg`, `images\GHH401043.jpeg`, `images\GHH401044.jpeg`, `images\GHH401045.jpeg`, `images\GHH401046.jpeg`, `images\GHH401047.jpeg`, `images\GHH401048.jpeg`, `images\GHH401049.jpeg`, `images\GHH401050.jpeg`, `images\GHH401051.jpeg`, `images\GHH401052.jpeg`, `images\GHH401053.jpeg`, `images\GHH401054.jpeg`, `images\GHH401055.jpeg`, `images\GHH401056.jpeg`, `images\GHH401057.jpeg`, `images\GHH401058.jpeg`, `images\GHH401059.jpeg`, `images\GHH401060.jpeg`, `images\GHH401061.jpeg`, `images\GHH401062.jpeg`, `images\GHH401063.jpeg`, `images\GHH401064.jpeg`, `images\GHH401065.jpeg`
- Duplicate sources: `pages\13967.html`

### Full Text

````text
# CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

*1 | Selective use Integrated washer Separated washer

- Integrated washer

- Separated washer

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

- Transmission Hanger - Remove

- Filler Cap - Remove

- Breather Cap - Remove

- Left Differential Oil Seal - Remove

- TCM - Remove

- Control Lever - Remove Courtesy of HONDA, U.S.A., INC. 1. Pry down the lock tab (A) of the lock washer (B), then remove the control lever (C).

Courtesy of HONDA, U.S.A., INC. | 1. Pry down the lock tab (A) of the lock washer (B), then remove the control lever (C).

- Control Shaft Cover - Remove

- Transmission Range Switch - Remove

- CVT Speed Sensor - Remove

- CVT Drive Pulley Speed Sensor - Remove

- Torque Converter Turbine Speed Sensor - Remove

- CVT Driven Pulley Pressure Sensor - Remove

- Sealing Bolt - Remove

- Filler Plug - Remove

- Drain Plug - Remove

- Transmission Fluid Pan - Remove

- Magnet - Remove

- Transmission Fluid Strainer - Remove

- Transmission Fluid Strainer - Check Courtesy of HONDA, U.S.A., INC. 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

Courtesy of HONDA, U.S.A., INC. | 1. Clean the inlet opening (A) of the transmission fluid strainer (B) thoroughly with compressed air. 2. Check that it is in good condition and that the inlet opening is not clogged. 3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

2. Check that it is in good condition and that the inlet opening is not clogged.

3. Test the strainer by pouring clean transmission fluid through the inlet opening, and replace it if it is clogged or damaged.

- Valve Body Assembly - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the valve body assembly mounting bolts. Courtesy of HONDA, U.S.A., INC. 2. Remove the valve body assembly straightly (A) and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the valve body assembly mounting bolts.

Courtesy of HONDA, U.S.A., INC. | 2. Remove the valve body assembly straightly (A) and disconnect the connector (B). NOTE: Be careful not to damage the solenoid wire harness.

- 10.9 x 29 mm Pipe - Remove

- 10.9 x 48 mm Pipe - Remove

- 10.9 x 75.5 mm Pipe - Remove

- 18 x 21 mm Pipe - Remove

- Solenoid Wire Harness - Remove

- Solenoid Wire Harness Connector - Remove

- Transmission Fluid Pump - Remove

- Sealing Bolt - Remove

- End Cover - Remove

- End Cover Plate - Remove

- 16 mm Sealing Ring - Remove

- Snap Ring - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) using commercially available snap ring pliers (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) using commercially available snap ring pliers (B).

- Driven Pulley Shaft Bearing (End Cover Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the driven pulley shaft bearing (A) using the 45-75 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the driven pulley shaft bearing (A) using the 45-75 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

- 8 x 52.2 mm Pipe - Remove

- 8 x 244 mm Pipe - Remove

- 10.9 x 48 mm Pipe - Remove

- Cooler Pipe - Remove

- Parking Brake Pawl - Remove

- Parking Shaft - Remove

- Parking Pawl Spring - Remove
````

## Chunk 10024: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure
- Source path: `pages\12568.html`
- Chunk ID: `chunk_3ba45c289831`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401036.jpeg`, `images\GHH401037.jpeg`, `images\GHH401038.jpeg`, `images\GHH401039.jpeg`, `images\GHH401040.jpeg`, `images\GHH401041.jpeg`, `images\GHH401042.jpeg`, `images\GHH401043.jpeg`, `images\GHH401044.jpeg`, `images\GHH401045.jpeg`, `images\GHH401046.jpeg`, `images\GHH401047.jpeg`, `images\GHH401048.jpeg`, `images\GHH401049.jpeg`, `images\GHH401050.jpeg`, `images\GHH401051.jpeg`, `images\GHH401052.jpeg`, `images\GHH401053.jpeg`, `images\GHH401054.jpeg`, `images\GHH401055.jpeg`, `images\GHH401056.jpeg`, `images\GHH401057.jpeg`, `images\GHH401058.jpeg`, `images\GHH401059.jpeg`, `images\GHH401060.jpeg`, `images\GHH401061.jpeg`, `images\GHH401062.jpeg`, `images\GHH401063.jpeg`, `images\GHH401064.jpeg`, `images\GHH401065.jpeg`
- Duplicate sources: `pages\13967.html`

### Full Text

````text
the snap ring (A) using commercially available snap ring pliers (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) using commercially available snap ring pliers (B).

- Driven Pulley Shaft Bearing (End Cover Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the driven pulley shaft bearing (A) using the 45-75 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the driven pulley shaft bearing (A) using the 45-75 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

- 8 x 52.2 mm Pipe - Remove

- 8 x 244 mm Pipe - Remove

- 10.9 x 48 mm Pipe - Remove

- Cooler Pipe - Remove

- Parking Brake Pawl - Remove

- Parking Shaft - Remove

- Parking Pawl Spring - Remove

- Parking Brake Rod Holder - Remove Courtesy of HONDA, U.S.A., INC. 1. Pry down the lock tabs (A) of the lock washer (B). 2. Remove the parking brake rod holder (C).

Courtesy of HONDA, U.S.A., INC. | 1. Pry down the lock tabs (A) of the lock washer (B). 2. Remove the parking brake rod holder (C).

2. Remove the parking brake rod holder (C).

- Torque Converter Housing - Remove

- Input Shaft Oil Seal - Remove

- Right Differential Oil Seal - Remove

- Input Shaft Bearing - Remove

- Snap Ring - Remove

- Bearing Set Plate - Remove

- Driven Pulley Shaft Bearing (Torque Converter Housing Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the driven pulley shaft bearing (A) using the 25-40 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the driven pulley shaft bearing (A) using the 25-40 mm adjustable bearing puller and a commercially available 3/8"-16 slide hammer (B).

- Oil Guide Plate - Remove

- Differential Carrier Tapered Roller Bearing Outer Race (Torque Converter Housing Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the differential carrier tapered roller bearing outer race (A) by heating the torque converter housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the torque converter housing more than 212°F (100°C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the differential carrier tapered roller bearing outer race (A) by heating the torque converter housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the torque converter housing more than 212°F (100°C).

- 68 mm Thrust Shim - Remove

- Oil Guide Plate - Remove

- Final Drive Shaft Tapered Roller Bearing Outer Race (Torque Converter Housing Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the final drive shaft tapered roller bearing outer race (A) by heating the torque converter housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the torque converter housing more than 212°F (100°C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the final drive shaft tapered roller bearing outer race (A) by heating the torque converter housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the torque converter housing more than 212°F (100°C).

- 51 mm Thrust Shim - Remove

- Final Drive Shaft Assembly - Remove

- Differential Assembly - Remove

- Baffle Plate - Remove

- Transmission Fluid Pump Driven Sprocket and Transmission Fluid Pump Drive Chain - Remove Courtesy of HONDA, U.S.A., INC. 1. While expanding the snap ring (A) using the snap ring pliers, remove the transmission fluid pump driven sprocket (B) and the transmission fluid pump drive chain (C).

Courtesy of HONDA, U.S.A., INC. | 1. While expanding the snap ring (A) using the snap ring pliers, remove the transmission fluid pump driven sprocket (B) and the transmission fluid pump drive chain (C).

- Snap Ring - Remove

- Snap Ring - Remove

- Detent Spring - Remove

- Control Shaft and Detent Lever - Remove Courtesy of HONDA, U.S.A., INC. 1. Pry down the lock tab (A) of the lock washer (B). 2. Remove the roller (C), then remove the control shaft (D). 3. Remove the detent lever (E).

Courtesy of HONDA, U.S.A., INC. | 1. Pry down the lock tab (A) of the lock washer (B). 2. Remove the roller (C), then remove the control shaft (D). 3. Remove the detent lever (E).

2. Remove the roller (C), then remove the control shaft (D).

3. Remove the detent lever (E).

- Control Shaft Oil Seal - Remove

- Manual Valve Body - Remove

- Manual Valve - Remove

- Stator Shaft Flange - Remove

- Sealing Bolt - Remove

- 56.7 mm Sealing Ring - Remove
````

## Chunk 10025: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure
- Source path: `pages\12568.html`
- Chunk ID: `chunk_bb579f29a67d`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401036.jpeg`, `images\GHH401037.jpeg`, `images\GHH401038.jpeg`, `images\GHH401039.jpeg`, `images\GHH401040.jpeg`, `images\GHH401041.jpeg`, `images\GHH401042.jpeg`, `images\GHH401043.jpeg`, `images\GHH401044.jpeg`, `images\GHH401045.jpeg`, `images\GHH401046.jpeg`, `images\GHH401047.jpeg`, `images\GHH401048.jpeg`, `images\GHH401049.jpeg`, `images\GHH401050.jpeg`, `images\GHH401051.jpeg`, `images\GHH401052.jpeg`, `images\GHH401053.jpeg`, `images\GHH401054.jpeg`, `images\GHH401055.jpeg`, `images\GHH401056.jpeg`, `images\GHH401057.jpeg`, `images\GHH401058.jpeg`, `images\GHH401059.jpeg`, `images\GHH401060.jpeg`, `images\GHH401061.jpeg`, `images\GHH401062.jpeg`, `images\GHH401063.jpeg`, `images\GHH401064.jpeg`, `images\GHH401065.jpeg`
- Duplicate sources: `pages\13967.html`

### Full Text

````text
(B) and the transmission fluid pump drive chain (C).

- Snap Ring - Remove

- Snap Ring - Remove

- Detent Spring - Remove

- Control Shaft and Detent Lever - Remove Courtesy of HONDA, U.S.A., INC. 1. Pry down the lock tab (A) of the lock washer (B). 2. Remove the roller (C), then remove the control shaft (D). 3. Remove the detent lever (E).

Courtesy of HONDA, U.S.A., INC. | 1. Pry down the lock tab (A) of the lock washer (B). 2. Remove the roller (C), then remove the control shaft (D). 3. Remove the detent lever (E).

2. Remove the roller (C), then remove the control shaft (D).

3. Remove the detent lever (E).

- Control Shaft Oil Seal - Remove

- Manual Valve Body - Remove

- Manual Valve - Remove

- Stator Shaft Flange - Remove

- Sealing Bolt - Remove

- 56.7 mm Sealing Ring - Remove

- Snap Ring - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) using the snap ring pliers.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) using the snap ring pliers.

- Transmission Fluid Pump Drive Sprocket - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the transmission fluid pump drive sprocket (A) using the 15 x 135L driver handle and the 52 x 55 mm bearing driver attachment.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the transmission fluid pump drive sprocket (A) using the 15 x 135L driver handle and the 52 x 55 mm bearing driver attachment.

- Transmission Fluid Pump Drive Sprocket Bearing - Remove Courtesy of HONDA, U.S.A., INC. 1. While expanding the snap ring (A) using the snap ring pliers, remove the transmission fluid pump drive sprocket bearing (B).

Courtesy of HONDA, U.S.A., INC. | 1. While expanding the snap ring (A) using the snap ring pliers, remove the transmission fluid pump drive sprocket bearing (B).

- Snap Ring - Remove

- Lubrication Pipe - Remove

- Stator Shaft - Remove

- 42.3 mm Sealing Ring - Remove

- 26 x 38.8 mm Thrust Shim - Remove

- 26 x 40.8 x 3.2 mm Thrust Needle Bearing - Remove

- Input Shaft Assembly - Remove Courtesy of HONDA, U.S.A., INC. NOTE: Note the depth (A) between the surface of the transmission housing (B) and the clutch guide (C). The recorded value of the depth will be the standard one when installing the input shaft assembly.

Courtesy of HONDA, U.S.A., INC.

NOTE: Note the depth (A) between the surface of the transmission housing (B) and the clutch guide (C). The recorded value of the depth will be the standard one when installing the input shaft assembly.

- 22.2 mm Sealing Ring - Remove

- 16 x 20 x 16.8 mm Needle Bearing - Remove

- Snap Ring - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) using the snap ring pliers.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) using the snap ring pliers.

- 33 x 40 mm Thrust Shim - Remove

- Sun Gear - Remove

- Planetary Carrier - Remove

- 37 x 53.1 x 3 mm Thrust Needle Bearing - Remove

- Ring Gear - Remove

- 33.5 x 53 x 1 mm Thrust Washer - Remove

- 40 x 54 x 6 mm Collar - Remove

- Reverse Brake - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A). 2. Remove the reverse brake end-plate (B). 3. Remove the reverse brake discs (C) and the reverse brake plates (D). 4. Remove the disc spring (E).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A). 2. Remove the reverse brake end-plate (B). 3. Remove the reverse brake discs (C) and the reverse brake plates (D). 4. Remove the disc spring (E).

2. Remove the reverse brake end-plate (B).

3. Remove the reverse brake discs (C) and the reverse brake plates (D).

4. Remove the disc spring (E).

- Snap Ring - Remove Courtesy of HONDA, U.S.A., INC. 1. Put the reverse brake spring compressor attachment (A) on the spring retainer/return spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be removed. 5. Remove the snap ring (G), then remove the reverse brake spring compressor.

Courtesy of HONDA, U.S.A., INC. | 1. Put the reverse brake spring compressor attachment (A) on the spring retainer/return spring assembly (B).
````

## Chunk 10026: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Disassembly: Procedure
- Source path: `pages\12568.html`
- Chunk ID: `chunk_bc1cbf90b9d3`
- Images: `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401036.jpeg`, `images\GHH401037.jpeg`, `images\GHH401038.jpeg`, `images\GHH401039.jpeg`, `images\GHH401040.jpeg`, `images\GHH401041.jpeg`, `images\GHH401042.jpeg`, `images\GHH401043.jpeg`, `images\GHH401044.jpeg`, `images\GHH401045.jpeg`, `images\GHH401046.jpeg`, `images\GHH401047.jpeg`, `images\GHH401048.jpeg`, `images\GHH401049.jpeg`, `images\GHH401050.jpeg`, `images\GHH401051.jpeg`, `images\GHH401052.jpeg`, `images\GHH401053.jpeg`, `images\GHH401054.jpeg`, `images\GHH401055.jpeg`, `images\GHH401056.jpeg`, `images\GHH401057.jpeg`, `images\GHH401058.jpeg`, `images\GHH401059.jpeg`, `images\GHH401060.jpeg`, `images\GHH401061.jpeg`, `images\GHH401062.jpeg`, `images\GHH401063.jpeg`, `images\GHH401064.jpeg`, `images\GHH401065.jpeg`
- Duplicate sources: `pages\13967.html`

### Full Text

````text
A) on the spring retainer/return spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be removed. 5. Remove the snap ring (G), then remove the reverse brake spring compressor.

Courtesy of HONDA, U.S.A., INC. | 1. Put the reverse brake spring compressor attachment (A) on the spring retainer/return spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be removed. 5. Remove the snap ring (G), then remove the reverse brake spring compressor.

NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C).

2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E).

3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment.

4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be removed.

5. Remove the snap ring (G), then remove the reverse brake spring compressor.

- Spring Retainer/Return Spring Assembly - Remove

- Reverse Brake Piston - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the reverse brake piston (A) with the O-rings (B), while applying air pressure to the reverse brake pressure circuit hole (C). NOTE: Cover the hydraulic circuit hole using a shop towel to prevent scatter of the transmission fluid.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the reverse brake piston (A) with the O-rings (B), while applying air pressure to the reverse brake pressure circuit hole (C). NOTE: Cover the hydraulic circuit hole using a shop towel to prevent scatter of the transmission fluid.

- Differential Carrier Tapered Roller Bearing Outer Race (Transmission Housing Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the differential carrier tapered roller bearing outer race (A) by heating the transmission housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the transmission housing more than 212°F (100°C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the differential carrier tapered roller bearing outer race (A) by heating the transmission housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the transmission housing more than 212°F (100°C).

- Spacer - Remove

- Final Drive Shaft Tapered Roller Bearing Outer Race (Transmission Housing Side) - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the final drive shaft tapered roller bearing outer race (A) by heating the transmission housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the transmission housing more than 212°F (100°C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the final drive shaft tapered roller bearing outer race (A) by heating the transmission housing to about 212°F (100°C) using a heat gun (B). NOTE: Do not heat the transmission housing more than 212°F (100°C).

- Oil Guide Plate - Remove

- Snap Ring - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the snap ring (A) using the snap ring pliers.

Courtesy of HONDA, U.S.A., INC. | 1. Remove the snap ring (A) using the snap ring pliers.

- Cotter Retainer - Remove

- 25.5 mm Cotter - Remove

- Secondary Drive Gear - Remove Courtesy of HONDA, U.S.A., INC. 1. Remove the secondary drive gear (A) using a puller (B) and a commercially available spacer (C).

Courtesy of HONDA, U.S.A., INC. | 1. Remove the secondary drive gear (A) using a puller (B) and a commercially available spacer (C).
````

## Chunk 10027: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes
- Source path: `pages\12569.html`
- Chunk ID: `chunk_814a87b952b4`
- Images: `images\GHH400682.png`
- Duplicate sources: `pages\13968.html`

### Full Text

````text
# CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Notes

NOTE:

- Where icon is shown, for further information see below.

- Keep all foreign particles out of the transmission.

- When you reassemble the transmission, apply a light coat of clean transmission fluid on all oil seals, O-rings, bearings, and shaft splines. Also soak the forward clutch assembly and the reverse brake discs, in clean transmission fluid for at least 30 minutes prior to installation.

- Be careful not to damage the O-rings.
````

## Chunk 10028: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_0c6416d8a3e4`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
# CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

*1 | Selective use Integrated washer Separated washer

- Integrated washer

- Separated washer

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

Numbered call-outs in figure pertain to list numbers in following procedure.

Detailed information, notes and precautions

Torque: N.m (kgf.m, lbf.ft)

Replace

- Secondary Drive Gear - Install Courtesy of HONDA, U.S.A., INC. 1. Install the secondary drive gear (A) as shown using the 40 mm I.D. driver handle and the 30 mm I.D. bearing driver attachment.

Courtesy of HONDA, U.S.A., INC. | 1. Install the secondary drive gear (A) as shown using the 40 mm I.D. driver handle and the 30 mm I.D. bearing driver attachment.

- 25.5 mm Cotter - Install

- Cotter Retainer - Install

- Snap Ring - Install Courtesy of HONDA, U.S.A., INC. 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Oil Guide Plate - Install

- Final Drive Shaft Tapered Roller Bearing Outer Race (Transmission Housing Side) - Install Courtesy of HONDA, U.S.A., INC. 1. Install the final drive shaft tapered roller bearing outer race (A) until it bottoms using the 40 mm I.D. driver handle.

Courtesy of HONDA, U.S.A., INC. | 1. Install the final drive shaft tapered roller bearing outer race (A) until it bottoms using the 40 mm I.D. driver handle.

- Spacer - Install

- Differential Carrier Tapered Roller Bearing Outer Race (Transmission Housing Side) - Install Courtesy of HONDA, U.S.A., INC. 1. Install the differential carrier tapered roller bearing outer race (A) until it bottoms using the 15 x 135L driver handle and the 62 x 64 mm bearing driver attachment.

Courtesy of HONDA, U.S.A., INC. | 1. Install the differential carrier tapered roller bearing outer race (A) until it bottoms using the 15 x 135L driver handle and the 62 x 64 mm bearing driver attachment.

- Reverse Brake Piston - Install

- Spring Retainer/Return Spring Assembly - Install Courtesy of HONDA, U.S.A., INC. 1. Install the spring retainer/return spring assembly (A) by aligning their holes (B) with the bosses (C).

Courtesy of HONDA, U.S.A., INC. | 1. Install the spring retainer/return spring assembly (A) by aligning their holes (B) with the bosses (C).

- Snap Ring - Install Courtesy of HONDA, U.S.A., INC. 1. Put the reverse brake spring compressor attachment (A) on the spring retainer/return spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be installed. 5. Install the snap ring (G). Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove. 6. Remove the reverse brake spring compressor.

Courtesy of HONDA, U.S.A., INC. | 1.
````

## Chunk 10029: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_5517e246b452`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
turn spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be installed. 5. Install the snap ring (G). Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove. 6. Remove the reverse brake spring compressor.

Courtesy of HONDA, U.S.A., INC. | 1. Put the reverse brake spring compressor attachment (A) on the spring retainer/return spring assembly (B). NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C). 2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E). 3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment. 4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be installed. 5. Install the snap ring (G). Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove. 6. Remove the reverse brake spring compressor.

NOTE: Be sure the attachment is set over the return springs, not on the reverse brake piston (C).

2. Install the reverse brake spring compressor plate (D) with facing the UP mark to the upside using bolts (E).

3. Make sure that the reverse brake spring compressor bolt (F) is properly installed on the dent in the surface of the reverse brake spring compressor attachment.

4. Compress the return springs using the reverse brake spring compressor until the snap ring securing the spring retainer/return spring can be installed.

5. Install the snap ring (G).

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

6. Remove the reverse brake spring compressor.

- Reverse Brake - Install Courtesy of HONDA, U.S.A., INC. 1. Install the disc spring (A). NOTE: Be sure to install the disc spring with the indented mark (B) facing the upward. 2. Starting with the reverse brake plate (C), alternately install the reverse brake plates and the reverse brake discs (D). 3. Install the reverse brake end-plate (E) with the flat side toward the top disc. 4. Install the snap ring (F). Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. Install the disc spring (A). NOTE: Be sure to install the disc spring with the indented mark (B) facing the upward. 2. Starting with the reverse brake plate (C), alternately install the reverse brake plates and the reverse brake discs (D). 3. Install the reverse brake end-plate (E) with the flat side toward the top disc. 4. Install the snap ring (F). Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

NOTE: Be sure to install the disc spring with the indented mark (B) facing the upward.

2. Starting with the reverse brake plate (C), alternately install the reverse brake plates and the reverse brake discs (D).

3. Install the reverse brake end-plate (E) with the flat side toward the top disc.

4. Install the snap ring (F).

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Reverse Brake End-Plate Thrust Clearance - Inspect 1. Set a dial indicator (A) on the reverse brake end-plate (B). Courtesy of HONDA, U.S.A., INC. 2. Zero the dial indicator with the reverse brake end-plate is lifted up to the snap ring (C). 3. Release the reverse brake end-plate. 4. Put the clutch compressor attachment and the 64 mm clutch compressor attachment on the reverse brake end-plate. 5.
````

## Chunk 10030: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_e60468c9a232`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
facing the upward.

2. Starting with the reverse brake plate (C), alternately install the reverse brake plates and the reverse brake discs (D).

3. Install the reverse brake end-plate (E) with the flat side toward the top disc.

4. Install the snap ring (F).

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Reverse Brake End-Plate Thrust Clearance - Inspect 1. Set a dial indicator (A) on the reverse brake end-plate (B). Courtesy of HONDA, U.S.A., INC. 2. Zero the dial indicator with the reverse brake end-plate is lifted up to the snap ring (C). 3. Release the reverse brake end-plate. 4. Put the clutch compressor attachment and the 64 mm clutch compressor attachment on the reverse brake end-plate. 5. Press the clutch compressor attachment down with 39.2 N (4.00 kgf, 8.81 lbf) (the weight of the clutch compressor attachment is included) using a force gauge, and read the dial indicator. 6. The dial indicator reads the clearance (D) between the reverse brake end-plate and the top disc (E). Take measurements in at least three places, and use the average as the actual clearance. Standard: 1.0-1.2 mm (0.039-0.047 in) 7. If the clearance is out of the standard, remove the reverse brake end-plate and select a suitable one. Reverse Brake End-Plate No. Thickness 1 3.6 mm (0.142 in) 2 3.7 mm (0.146 in) 3 3.8 mm (0.150 in) 4 3.9 mm (0.154 in) 5 4.0 mm (0.157 in) 6 4.1 mm (0.161 in) 7 4.2 mm (0.165 in) 8 4.3 mm (0.169 in) 9 4.4 mm (0.173 in) 10 4.5 mm (0.177 in) 11 4.6 mm (0.181 in) 12 4.7 mm (0.185 in) 13 4.8 mm (0.189 in) 14 4.9 mm (0.193 in) 15 5.0 mm (0.197 in) 8. Install a selected reverse brake end-plate, then recheck the clearance.

1. Set a dial indicator (A) on the reverse brake end-plate (B).

Courtesy of HONDA, U.S.A., INC.

2. Zero the dial indicator with the reverse brake end-plate is lifted up to the snap ring (C).

3. Release the reverse brake end-plate.

4. Put the clutch compressor attachment and the 64 mm clutch compressor attachment on the reverse brake end-plate.

5. Press the clutch compressor attachment down with 39.2 N (4.00 kgf, 8.81 lbf) (the weight of the clutch compressor attachment is included) using a force gauge, and read the dial indicator.

6. The dial indicator reads the clearance (D) between the reverse brake end-plate and the top disc (E). Take measurements in at least three places, and use the average as the actual clearance.

Standard: | 1.0-1.2 mm (0.039-0.047 in)

7. If the clearance is out of the standard, remove the reverse brake end-plate and select a suitable one.

Reverse Brake End-Plate

No. | Thickness

1 | 3.6 mm (0.142 in)

2 | 3.7 mm (0.146 in)

3 | 3.8 mm (0.150 in)

4 | 3.9 mm (0.154 in)

5 | 4.0 mm (0.157 in)

6 | 4.1 mm (0.161 in)

7 | 4.2 mm (0.165 in)

8 | 4.3 mm (0.169 in)

9 | 4.4 mm (0.173 in)

10 | 4.5 mm (0.177 in)

11 | 4.6 mm (0.181 in)

12 | 4.7 mm (0.185 in)

13 | 4.8 mm (0.189 in)

14 | 4.9 mm (0.193 in)

15 | 5.0 mm (0.197 in)

8. Install a selected reverse brake end-plate, then recheck the clearance.

- 40 x 54 x 6 mm Collar - Install NOTE: Make sure the 40 x 54 x 6 mm collar is installed in the correct direction.

NOTE: Make sure the 40 x 54 x 6 mm collar is installed in the correct direction.

- 33.5 x 53 x 1 mm Thrust Washer - Install

- Ring Gear - Install

- 37 x 53.1 x 3 mm Thrust Needle Bearing - Install NOTE: Make sure the 37 x 53.1 x 3 mm thrust needle bearing is installed in the correct direction.

NOTE: Make sure the 37 x 53.1 x 3 mm thrust needle bearing is installed in the correct direction.

- Planetary Carrier - Install

- Sun Gear - Install

- 33 x 40 mm Thrust Shim - Install

- Snap Ring - Install Courtesy of HONDA, U.S.A., INC. 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Sun Gear Thrust Clearance - Inspect 1. Set a dial indicator (A) on the sun gear (B). Courtesy of HONDA, U.S.A., INC. 2.
````

## Chunk 10031: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_10503491d92c`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
- Sun Gear - Install

- 33 x 40 mm Thrust Shim - Install

- Snap Ring - Install Courtesy of HONDA, U.S.A., INC. 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Sun Gear Thrust Clearance - Inspect 1. Set a dial indicator (A) on the sun gear (B). Courtesy of HONDA, U.S.A., INC. 2. Zero the dial indicator with the sun gear is lifted up to the 33 x 40 mm thrust shim (C) contact the snap ring (D). 3. Release the sun gear. 4. Put the clutch compressor attachment on the sun gear. 5. Press the clutch compressor attachment down with 49 N (5.0 kgf, 11.0 lbf) (the weight of the clutch compressor attachment is included) using a force gauge, and read the dial indicator. 6. The dial indicator reads the clearance (E) between the sun gear and the 33 x 40 mm thrust shim. Take measurements in at least three places, and use the average as the actual clearance. Standard: 0.04-0.09 mm (0.0016-0.0035 in) 7. If the clearance is out of the standard, remove the 33 x 40 mm thrust shim and select a suitable one. 33 x 40 mm Thrust Shim No. Thickness 0A 1.16 mm (0.0457 in) 0B 1.19 mm (0.0469 in) 0C 1.22 mm (0.0480 in) 0D 1.25 mm (0.0492 in) 0E 1.28 mm (0.0504 in) A 1.31 mm (0.0516 in) B 1.34 mm (0.0528 in) C 1.37 mm (0.0539 in) No. Thickness D 1.40 mm (0.0551 in) E 1.43 mm (0.0563 in) F 1.46 mm (0.0575 in) G 1.49 mm (0.0587 in) H 1.52 mm (0.0598 in) I 1.55 mm (0.0610 in) J 1.58 mm (0.0622 in) K 1.61 mm (0.0634 in) L 1.64 mm (0.0646 in) M 1.67 mm (0.0657 in) N 1.70 mm (0.0669 in) O 1.73 mm (0.0681 in) P 1.76 mm (0.0693 in) Q 1.79 mm (0.0705 in) R 1.82 mm (0.0717 in) S 1.85 mm (0.0728 in) 8. Install a selected 33 x 40 mm thrust shim, then recheck the clearance.

1. Set a dial indicator (A) on the sun gear (B).

Courtesy of HONDA, U.S.A., INC.

2. Zero the dial indicator with the sun gear is lifted up to the 33 x 40 mm thrust shim (C) contact the snap ring (D).

3. Release the sun gear.

4. Put the clutch compressor attachment on the sun gear.

5. Press the clutch compressor attachment down with 49 N (5.0 kgf, 11.0 lbf) (the weight of the clutch compressor attachment is included) using a force gauge, and read the dial indicator.

6. The dial indicator reads the clearance (E) between the sun gear and the 33 x 40 mm thrust shim. Take measurements in at least three places, and use the average as the actual clearance.

Standard: | 0.04-0.09 mm (0.0016-0.0035 in)

7. If the clearance is out of the standard, remove the 33 x 40 mm thrust shim and select a suitable one.

33 x 40 mm Thrust Shim

No. | Thickness

0A | 1.16 mm (0.0457 in)

0B | 1.19 mm (0.0469 in)

0C | 1.22 mm (0.0480 in)

0D | 1.25 mm (0.0492 in)

0E | 1.28 mm (0.0504 in)

A | 1.31 mm (0.0516 in)

B | 1.34 mm (0.0528 in)

C | 1.37 mm (0.0539 in)

No. | Thickness

D | 1.40 mm (0.0551 in)

E | 1.43 mm (0.0563 in)

F | 1.46 mm (0.0575 in)

G | 1.49 mm (0.0587 in)

H | 1.52 mm (0.0598 in)

I | 1.55 mm (0.0610 in)

J | 1.58 mm (0.0622 in)

K | 1.61 mm (0.0634 in)

L | 1.64 mm (0.0646 in)

M | 1.67 mm (0.0657 in)

N | 1.70 mm (0.0669 in)

O | 1.73 mm (0.0681 in)

P | 1.76 mm (0.0693 in)

Q | 1.79 mm (0.0705 in)

R | 1.82 mm (0.0717 in)

S | 1.85 mm (0.0728 in)

8. Install a selected 33 x 40 mm thrust shim, then recheck the clearance.

- 16 x 20 x 16.8 mm Needle Bearing - Install

- 22.2 mm Sealing Ring - Install

- Input Shaft Assembly - Install Courtesy of HONDA, U.S.A., INC. 1. Install the input shaft (A) by aligning the clutch discs (B) with the sun gear (C), and aligning the clutch guide (D) with the ring gear (E). Courtesy of HONDA, U.S.A., INC. 2. Measure the depth (A) between the surface of the transmission housing (B) and the clutch guide (C), then make sure the measured value of the depth is within the recorded value when removing.

Courtesy of HONDA, U.S.A., INC. | 1. Install the input shaft (A) by aligning the clutch discs (B) with the sun gear (C), and aligning the clutch guide (D) with the ring gear (E).

Courtesy of HONDA, U.S.A., INC. | 2.
````

## Chunk 10032: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_22289c1ec03a`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
ll a selected 33 x 40 mm thrust shim, then recheck the clearance.

- 16 x 20 x 16.8 mm Needle Bearing - Install

- 22.2 mm Sealing Ring - Install

- Input Shaft Assembly - Install Courtesy of HONDA, U.S.A., INC. 1. Install the input shaft (A) by aligning the clutch discs (B) with the sun gear (C), and aligning the clutch guide (D) with the ring gear (E). Courtesy of HONDA, U.S.A., INC. 2. Measure the depth (A) between the surface of the transmission housing (B) and the clutch guide (C), then make sure the measured value of the depth is within the recorded value when removing.

Courtesy of HONDA, U.S.A., INC. | 1. Install the input shaft (A) by aligning the clutch discs (B) with the sun gear (C), and aligning the clutch guide (D) with the ring gear (E).

Courtesy of HONDA, U.S.A., INC. | 2. Measure the depth (A) between the surface of the transmission housing (B) and the clutch guide (C), then make sure the measured value of the depth is within the recorded value when removing.

- 26 x 40.8 x 3.2 mm Thrust Needle Bearing - Install NOTE: Make sure the 26 x 40.8 x 3.2 mm thrust needle bearing is installed in the correct direction.

NOTE: Make sure the 26 x 40.8 x 3.2 mm thrust needle bearing is installed in the correct direction.

- 26 x 38.8 mm Thrust Shim - Install

- 42.3 mm Sealing Ring - Install

- Stator Shaft - Install

- Lubrication Pipe - Install Courtesy of HONDA, U.S.A., INC. NOTE: Be sure to install the lubrication pipe (A) by aligning the guide tab (B) with the guide hole (C).

Courtesy of HONDA, U.S.A., INC.

NOTE: Be sure to install the lubrication pipe (A) by aligning the guide tab (B) with the guide hole (C).

- Snap Ring - Install NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

NOTE:

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Transmission Fluid Pump Drive Sprocket Bearing - Install Courtesy of HONDA, U.S.A., INC. 1. While expanding the snap ring (A) using the snap ring pliers, install the transmission fluid pump drive sprocket bearing (B) as shown. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. While expanding the snap ring (A) using the snap ring pliers, install the transmission fluid pump drive sprocket bearing (B) as shown. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Transmission Fluid Pump Drive Sprocket - Install Courtesy of HONDA, U.S.A., INC. 1. Install the transmission fluid pump drive sprocket (A) until it bottoms using the 15 x 135L driver handle and the 52 x 55 mm bearing driver attachment.

Courtesy of HONDA, U.S.A., INC. | 1. Install the transmission fluid pump drive sprocket (A) until it bottoms using the 15 x 135L driver handle and the 52 x 55 mm bearing driver attachment.

- Snap Ring - Install Courtesy of HONDA, U.S.A., INC. 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. Install the snap ring (A) using the snap ring pliers. NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- 56.7 mm Sealing Ring - Install

- Sealing Bolt - Install

- Stator Shaft Flange - Install Courtesy of HONDA, U.S.A., INC. NOTE: Align the holes (A) of the stator shaft flange with the lubrication pipe (B) and the dowel pin (C) when installing the stator shaft flange.

Courtesy of HONDA, U.S.A., INC.

NOTE: Align the holes (A) of the stator shaft flange with the lubrication pipe (B) and the dowel pin (C) when installing the stator shaft flange.

- Manual Valve - Install

- Manual Valve Body - Install

- Control Shaft Oil Seal - Install Courtesy of HONDA, U.S.A., INC. 1.
````

## Chunk 10033: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure

- Title: CVT Transmission Disassembly and Reassembly (K20C2 (CVT)): Reassembly: Procedure
- Source path: `pages\12570.html`
- Chunk ID: `chunk_4d1871a24012`
- Images: `images\GHH399704.png`, `images\GHH400682.png`, `images\GHH400684.png`, `images\GHH401066.jpeg`, `images\GHH401067.jpeg`, `images\GHH401068.jpeg`, `images\GHH401069.jpeg`, `images\GHH401070.jpeg`, `images\GHH401071.jpeg`, `images\GHH401072.jpeg`, `images\GHH401073.jpeg`, `images\GHH401074.jpeg`, `images\GHH401075.jpeg`, `images\GHH401076.jpeg`, `images\GHH401077.jpeg`, `images\GHH401078.jpeg`, `images\GHH401079.jpeg`, `images\GHH401080.jpeg`, `images\GHH401081.jpeg`, `images\GHH401082.jpeg`, `images\GHH401083.jpeg`, `images\GHH401084.jpeg`, `images\GHH401085.jpeg`, `images\GHH401086.jpeg`, `images\GHH401087.jpeg`, `images\GHH401088.jpeg`, `images\GHH401089.jpeg`, `images\GHH401090.jpeg`, `images\GHH401091.jpeg`, `images\GHH401092.jpeg`, `images\GHH401093.jpeg`, `images\GHH401094.jpeg`, `images\GHH401095.jpeg`, `images\GHH401096.jpeg`, `images\GHH401097.jpeg`, `images\GHH401098.jpeg`, `images\GHH401099.jpeg`, `images\GHH401100.jpeg`, `images\GHH401101.jpeg`, `images\GHH401102.jpeg`, `images\GHH401103.jpeg`, `images\GHH401104.jpeg`, `images\GHH401105.jpeg`, `images\GHH401106.jpeg`, `images\GHH401107.jpeg`, `images\GHH401108.jpeg`, `images\GHH401109.jpeg`
- Duplicate sources: `pages\13969.html`

### Full Text

````text
closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- 56.7 mm Sealing Ring - Install

- Sealing Bolt - Install

- Stator Shaft Flange - Install Courtesy of HONDA, U.S.A., INC. NOTE: Align the holes (A) of the stator shaft flange with the lubrication pipe (B) and the dowel pin (C) when installing the stator shaft flange.

Courtesy of HONDA, U.S.A., INC.

NOTE: Align the holes (A) of the stator shaft flange with the lubrication pipe (B) and the dowel pin (C) when installing the stator shaft flange.

- Manual Valve - Install

- Manual Valve Body - Install

- Control Shaft Oil Seal - Install Courtesy of HONDA, U.S.A., INC. 1. Install the control shaft oil seal (A) flush with the transmission housing using the 15 x 135L driver handle and the 22 x 24 mm attachment.

Courtesy of HONDA, U.S.A., INC. | 1. Install the control shaft oil seal (A) flush with the transmission housing using the 15 x 135L driver handle and the 22 x 24 mm attachment.

- Control Shaft and Detent Lever - Install Courtesy of HONDA, U.S.A., INC. 1. Install the detent lever (A) by aligning the guide tab (B) of the detent lever with the opening (C) of the manual valve. 2. Install the control shaft (D) into the transmission housing and the detent lever, then install the roller (E) to secure the control shaft. 3. Secure the control shaft and the detent lever with the mounting bolt (F) and the lock washer (G). 4. Pry up the lock tab of the lock (H) washer against the bolt head.

Courtesy of HONDA, U.S.A., INC. | 1. Install the detent lever (A) by aligning the guide tab (B) of the detent lever with the opening (C) of the manual valve. 2. Install the control shaft (D) into the transmission housing and the detent lever, then install the roller (E) to secure the control shaft. 3. Secure the control shaft and the detent lever with the mounting bolt (F) and the lock washer (G). 4. Pry up the lock tab of the lock (H) washer against the bolt head.

2. Install the control shaft (D) into the transmission housing and the detent lever, then install the roller (E) to secure the control shaft.

3. Secure the control shaft and the detent lever with the mounting bolt (F) and the lock washer (G).

4. Pry up the lock tab of the lock (H) washer against the bolt head.

- Detent Spring - Install

- Snap Ring - Install NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

NOTE:

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Snap Ring - Install NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

NOTE:

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Transmission Fluid Pump Driven Sprocket and Transmission Fluid Pump Drive Chain - Install Courtesy of HONDA, U.S.A., INC. 1. While expanding the snap ring (A) using the snap ring pliers, install the transmission fluid pump drive sprocket (B) and the transmission fluid pump drive chain (C). NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

Courtesy of HONDA, U.S.A., INC. | 1. While expanding the snap ring (A) using the snap ring pliers, install the transmission fluid pump drive sprocket (B) and the transmission fluid pump drive chain (C). NOTE: Be careful not to deform the snap ring by opening/closing it excessively. Make sure the snap ring is firmly installed in the groove.

- Be careful not to deform the snap ring by opening/closing it excessively.

- Make sure the snap ring is firmly installed in the groove.

- Baffle Plate - Install

- Differential Assembly - Install

- Final Drive Shaft Assembly - Install

- 51 mm Thrust Shim - Install

- Final Drive Shaft Tapered Roller Bearing Outer Race (Torque Converter Housing Side) - Install Courtesy of HONDA, U.S.A., INC. 1. Install the final drive shaft tapered roller bearing outer race (A) until it bottoms using the 40 mm I.D. driver handle so there is no clearance between the bearing outer race, the 51 mm thrust shim, and the torque converter housing.
````

## Sources Used

- `pages\12416.html`
- `pages\12417.html`
- `pages\12418.html`
- `pages\12419.html`
- `pages\12420.html`
- `pages\12421.html`
- `pages\12422.html`
- `pages\12423.html`
- `pages\12424.html`
- `pages\12425.html`
- `pages\12426.html`
- `pages\12427.html`
- `pages\12428.html`
- `pages\12429.html`
- `pages\12430.html`
- `pages\12431.html`
- `pages\12432.html`
- `pages\12433.html`
- `pages\12434.html`
- `pages\12435.html`
- `pages\12436.html`
- `pages\12437.html`
- `pages\12438.html`
- `pages\12439.html`
- `pages\12440.html`
- `pages\12441.html`
- `pages\12442.html`
- `pages\12443.html`
- `pages\12444.html`
- `pages\12445.html`
- `pages\12446.html`
- `pages\12447.html`
- `pages\12448.html`
- `pages\12449.html`
- `pages\12450.html`
- `pages\12451.html`
- `pages\12452.html`
- `pages\12453.html`
- `pages\12454.html`
- `pages\12455.html`
- `pages\12456.html`
- `pages\12457.html`
- `pages\12458.html`
- `pages\12459.html`
- `pages\12460.html`
- `pages\12461.html`
- `pages\12462.html`
- `pages\12463.html`
- `pages\12464.html`
- `pages\12465.html`
- `pages\12466.html`
- `pages\12467.html`
- `pages\12468.html`
- `pages\12469.html`
- `pages\12470.html`
- `pages\12471.html`
- `pages\12472.html`
- `pages\12473.html`
- `pages\12474.html`
- `pages\12475.html`
- `pages\12476.html`
- `pages\12477.html`
- `pages\12478.html`
- `pages\12479.html`
- `pages\12480.html`
- `pages\12481.html`
- `pages\12482.html`
- `pages\12483.html`
- `pages\12484.html`
- `pages\12485.html`
- `pages\12486.html`
- `pages\12487.html`
- `pages\12488.html`
- `pages\12489.html`
- `pages\12490.html`
- `pages\12491.html`
- `pages\12492.html`
- `pages\12493.html`
- `pages\12494.html`
- `pages\12495.html`
- `pages\12496.html`
- `pages\12497.html`
- `pages\12498.html`
- `pages\12499.html`
- `pages\12500.html`
- `pages\12501.html`
- `pages\12502.html`
- `pages\12504.html`
- `pages\12505.html`
- `pages\12506.html`
- `pages\12507.html`
- `pages\12509.html`
- `pages\12510.html`
- `pages\12511.html`
- `pages\12512.html`
- `pages\12513.html`
- `pages\12514.html`
- `pages\12515.html`
- `pages\12516.html`
- `pages\12517.html`
- `pages\12518.html`
- `pages\12519.html`
- `pages\12520.html`
- `pages\12521.html`
- `pages\12522.html`
- `pages\12523.html`
- `pages\12525.html`
- `pages\12526.html`
- `pages\12527.html`
- `pages\12528.html`
- `pages\12529.html`
- `pages\12530.html`
- `pages\12531.html`
- `pages\12532.html`
- `pages\12533.html`
- `pages\12534.html`
- `pages\12536.html`
- `pages\12537.html`
- `pages\12538.html`
- `pages\12539.html`
- `pages\12540.html`
- `pages\12541.html`
- `pages\12543.html`
- `pages\12544.html`
- `pages\12545.html`
- `pages\12546.html`
- `pages\12547.html`
- `pages\12548.html`
- `pages\12549.html`
- `pages\12550.html`
- `pages\12551.html`
- `pages\12552.html`
- `pages\12553.html`
- `pages\12554.html`
- `pages\12555.html`
- `pages\12556.html`
- `pages\12557.html`
- `pages\12558.html`
- `pages\12559.html`
- `pages\12560.html`
- `pages\12561.html`
- `pages\12562.html`
- `pages\12563.html`
- `pages\12564.html`
- `pages\12565.html`
- `pages\12566.html`
- `pages\12567.html`
- `pages\12568.html`
- `pages\12569.html`
- `pages\12570.html`
