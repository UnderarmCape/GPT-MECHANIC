# GPT Chunk Validation Report

Generated: 2026-05-17T11:39:11
Repository: `C:\Users\kaili\Documents\GPT-MECHANIC-REPO`
Corpus: `build_clean\chunks_jsonl_parts/*.jsonl`
Manifest: `build_clean\chunks_manifest.json`
Status: **ISSUES FOUND**

## Summary

- JSONL part files scanned: **5**
- Total lines read: **11223**
- Total valid chunk records: **11223**
- Manifest `chunks_created`: **11223**
- Total validation issue references: **49**

| Check | Result |
| --- | ---: |
| Invalid JSON lines | 0 |
| Valid JSON lines that are not objects | 0 |
| Chunks missing required fields | 0 |
| Field type issues | 0 |
| Empty text chunks | 0 |
| Chunks under 100 characters | 49 |
| Chunks over 8000 characters | 0 |
| Duplicate `chunk_id` values | 0 |
| Chunks affected by duplicate `chunk_id` values | 0 |
| Duplicate text hashes | 0 |
| Chunks affected by duplicate text hashes | 0 |
| Missing source paths | 0 |
| Missing or invalid local image paths | 0 |
| Local image path references checked | 52228 |
| External image path references skipped | 0 |
| Manifest or parts setup issues | 0 |

## Part File Counts

| Part file | Lines | Valid JSON | Valid chunks | Invalid JSON | Non-object JSON |
| --- | ---: | ---: | ---: | ---: | ---: |
| `build_clean\chunks_jsonl_parts\chunks_part_0001.jsonl` | 205 | 205 | 205 | 0 | 0 |
| `build_clean\chunks_jsonl_parts\chunks_part_0002.jsonl` | 185 | 185 | 185 | 0 | 0 |
| `build_clean\chunks_jsonl_parts\chunks_part_0003.jsonl` | 185 | 185 | 185 | 0 | 0 |
| `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl` | 3277 | 3277 | 3277 | 0 | 0 |
| `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl` | 7371 | 7371 | 7371 | 0 | 0 |

## Parts And Manifest Issues

No issues found.

## Invalid JSON Lines

No issues found.

## Valid JSON Lines That Are Not Objects

No issues found.

## Missing Required Fields

No issues found.

## Field Type Issues

No issues found.

## Empty Text Chunks

No issues found.

## Chunks Under 100 Characters

- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:147` | chunk_id=`chunk_406db4362033` | source_path=`pages\19087.html` | length=51 | preview="# Common Specs & Procedures - Specifications Index"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:269` | chunk_id=`chunk_5a516d09a77a` | source_path=`pages\19171.html` | length=46 | preview="# Brake Service Specifications - Brake System"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:302` | chunk_id=`chunk_a03de3050fdb` | source_path=`pages\19212.html` | length=91 | preview="# Engine Cooling Service Specifications - Cooling System (1.5 L) - Cooling System (2.0 L)"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:429` | chunk_id=`chunk_f2e9f6f45217` | source_path=`pages\19326.html` | length=80 | preview="# Engine Performance Safety Precautions - Engine Performance Safety Precautions"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:474` | chunk_id=`chunk_5f90f6dc76f9` | source_path=`pages\19372.html` | length=49 | preview="# HVAC Service Specifications - Air Conditioning"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:482` | chunk_id=`chunk_cbf16dc8c37e` | source_path=`pages\19374.html` | length=73 | preview="# SRS DTCS - Video - SRS DTCs - Video Procedure Video - Procedure Video"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:499` | chunk_id=`chunk_ee8545d723fd` | source_path=`pages\19385.html` | length=45 | preview="# Steering Service Specifications - Steering"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:503` | chunk_id=`chunk_8009f840dd32` | source_path=`pages\19392.html` | length=49 | preview="# Suspension Service Specifications - Suspension"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:532` | chunk_id=`chunk_583e476a1ce9` | source_path=`pages\19411.html` | length=45 | preview="# M/T Clutch Service Specifications - Clutch"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:533` | chunk_id=`chunk_acd2ca3659e1` | source_path=`pages\19412.html` | length=72 | preview="# M/T Service Specifications - Manual Transmission and M/T Differential"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:634` | chunk_id=`chunk_af553aa1bfec` | source_path=`pages\422.html` | length=66 | preview="# Driving Assistance Warning Systems See COMPONENT LOCATION INDEX"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:705` | chunk_id=`chunk_b9e4eec559b5` | source_path=`pages\546.html` | length=17 | preview="# Warning Systems"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:1118` | chunk_id=`chunk_481285a1993b` | source_path=`pages\801.html` | length=46 | preview="# A Closer Look at Radar Aiming - Video: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:1120` | chunk_id=`chunk_1a33a898d814` | source_path=`pages\804.html` | length=56 | preview="# Camera Aiming for LDW-Equipped Vehicles - Video: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:1328` | chunk_id=`chunk_75c242be490d` | source_path=`pages\955.html` | length=26 | preview="# Radar Unit Aiming: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0004.jsonl:2549` | chunk_id=`chunk_d1775a73bfd5` | source_path=`pages\2209.html` | length=96 | preview="# Removal and Installation: Notes NOTE: Where icon is shown, for further information see below."
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:1288` | chunk_id=`chunk_501666f6ae68` | source_path=`pages\6333.html` | length=47 | preview="# Firing Order & Cylinder Identification: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3576` | chunk_id=`chunk_b865bbe22a5f` | source_path=`pages\7878.html` | length=99 | preview="# Clear A/T DTCs Procedure 1. Connect the HDS to the DLC . 2. Clear the DTC(s) on the HDS screen."
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3813` | chunk_id=`chunk_0efc65c59d76` | source_path=`pages\9797.html` | length=22 | preview="# Brake Systems: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3817` | chunk_id=`chunk_9a6fa1d4cf93` | source_path=`pages\9808.html` | length=36 | preview="# Drivetrain And Transmission: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3846` | chunk_id=`chunk_709de8aad1ba` | source_path=`pages\9837.html` | length=43 | preview="# Engine Performance And Maintenance: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3878` | chunk_id=`chunk_2c36b2899987` | source_path=`pages\9877.html` | length=24 | preview="# Exhaust Systems: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3880` | chunk_id=`chunk_5522a1e6becb` | source_path=`pages\9879.html` | length=58 | preview="# Heating, Ventilation And Air Conditioning Systems: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3888` | chunk_id=`chunk_a5d3bb2be59a` | source_path=`pages\9887.html` | length=67 | preview="# Steering And Suspension, Wheel Alignment, Wheels And Tires: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3918` | chunk_id=`chunk_55493559ed66` | source_path=`pages\9919.html` | length=68 | preview="# Symptom Check List Worksheet - General Information: Purpose: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:3934` | chunk_id=`chunk_dbc8215f24ac` | source_path=`pages\9941.html` | length=71 | preview="# Gear Tooth Contact Patterns - General Information: Adjustments: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4243` | chunk_id=`chunk_fb6c1f59fc17` | source_path=`pages\10325.html` | length=84 | preview="# General Cooling System Service - General Information: Maintenance: Flushing: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4457` | chunk_id=`chunk_c1e1273268c7` | source_path=`pages\10623.html` | length=42 | preview="# The Two Types Of Injector Drivers: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4462` | chunk_id=`chunk_c67aaf4d02ef` | source_path=`pages\10628.html` | length=40 | preview="# Interpreting Injector Waveforms: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4467` | chunk_id=`chunk_bb4e36112d93` | source_path=`pages\10631.html` | length=33 | preview="# Current Waveform Samples: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4476` | chunk_id=`chunk_2039e050b72e` | source_path=`pages\10640.html` | length=33 | preview="# Voltage Waveform Samples: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4675` | chunk_id=`chunk_a1bc59c5a973` | source_path=`pages\10929.html` | length=32 | preview="# Auto Stop/Start Disable: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4719` | chunk_id=`chunk_6890717d8714` | source_path=`pages\11041.html` | length=61 | preview="# Engine Oil Replacement Reminder Reset - Procedure 17: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4723` | chunk_id=`chunk_d4760220f06c` | source_path=`pages\11045.html` | length=61 | preview="# Engine Oil Replacement Reminder Reset - Procedure 18: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4740` | chunk_id=`chunk_fa181f67c80d` | source_path=`pages\11062.html` | length=43 | preview="# TPMS Reminder Reset - Procedure 02: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4763` | chunk_id=`chunk_db44a5e802c4` | source_path=`pages\11085.html` | length=32 | preview="# Description & Operation: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4766` | chunk_id=`chunk_f6b9eb698369` | source_path=`pages\11088.html` | length=30 | preview="# TPMS Reset Procedures: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4770` | chunk_id=`chunk_5f23226a2b5a` | source_path=`pages\11093.html` | length=73 | preview="# Torque Specifications Component | Ft. Lbs. (N.m) Wheel Nut | 80 (108)"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4851` | chunk_id=`chunk_789c77d1223f` | source_path=`pages\11213.html` | length=35 | preview="# Pre-Alignment Instructions: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4853` | chunk_id=`chunk_231a5201cb26` | source_path=`pages\11215.html` | length=78 | preview="# Wheel Alignment Theory & Operation - General Information: Adjustments: Notes"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4946` | chunk_id=`chunk_79dc4b4e445d` | source_path=`pages\11376.html` | length=86 | preview="# Removal and Installation: Notes NOTE: Be careful not to damage the evaporator core."
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4950` | chunk_id=`chunk_4bd2a2349cb5` | source_path=`pages\11381.html` | length=82 | preview="# Removal and Installation: Notes NOTE: Be careful not to damage the heater core."
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:4957` | chunk_id=`chunk_7e2311ac3b6c` | source_path=`pages\11388.html` | length=98 | preview="# Disassembly and Reassembly: Notes NOTE: Where icon is shown, for further information see below."
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6647` | chunk_id=`chunk_8db95f3bb156` | source_path=`pages\148.html` | length=93 | preview="# Clean & Tighten Applies To | Note | Standard Hours | Warranty Hours | Skill Level 0.3 | D"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6676` | chunk_id=`chunk_784d0cf2759c` | source_path=`pages\180.html` | length=99 | preview="# Cooling System: Flush Applies To | Note | Standard Hours | Warranty Hours | Skill Level 0.7 | D"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6695` | chunk_id=`chunk_bc7deb66486a` | source_path=`pages\199.html` | length=95 | preview="# Fuel Lines: Clean Applies To | Note | Standard Hours | Warranty Hours | Skill Level 0.7 | D"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6697` | chunk_id=`chunk_c8c552b04858` | source_path=`pages\201.html` | length=96 | preview="# Fuel Pump: Testing Applies To | Note | Standard Hours | Warranty Hours | Skill Level 0.5 | B"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6833` | chunk_id=`chunk_95c4e8027b73` | source_path=`pages\344.html` | length=92 | preview="# Drain & Refill Applies To | Note | Standard Hours | Warranty Hours | Skill Level 0.6 | C"
- `build_clean\chunks_jsonl_parts\chunks_part_0005.jsonl:6846` | chunk_id=`chunk_814ed2dc83fa` | source_path=`pages\357.html` | length=94 | preview="# Overhaul Removed Applies To | Note | Standard Hours | Warranty Hours | Skill Level 6.9 | A"

## Chunks Over 8000 Characters

No issues found.

## Duplicate `chunk_id` Values

No issues found.

## Duplicate Text Hashes

No issues found.

## Missing Source Paths

No issues found.

## Missing Or Invalid Local Image Paths

No issues found.

