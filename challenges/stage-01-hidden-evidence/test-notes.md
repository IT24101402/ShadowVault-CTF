# Stage 01 – Hidden Evidence: Test Notes

## Test Objective
Verify that the Stage 01 challenge artifact is valid, the hidden payload can be detected and extracted, and the expected flag and progression clue can be recovered.

## Test Environment

- Host: Kali Linux 2026.2 Rolling
- Architecture: ARM64 (aarch64)
- Virtualization: UTM
- Challenge Type: Static file challenge
- Challenge File: `files/nova-office.jpeg`

## Test 1 – File Validation

Command:

```bash
file files/nova-office.jpeg
```

### Result
PASS

The challenge artifact was successfully recognized as a valid JPEG image.

---

## Test 2 – Metadata Inspection

Command:

```bash
exiftool files/nova-office.jpeg
```

### Result
PASS

ExifTool successfully processed the image and reported valid JPEG properties.

---

## Test 3 – Basic Embedded-Data Analysis

Commands:

```bash
strings files/nova-office.jpeg
```

```bash
binwalk files/nova-office.jpeg
```

### Result
PASS

The image could be analyzed normally using standard forensic utilities.

---

## Test 4 – Steghide Detection

Command:

```bash
steghide info files/nova-office.jpeg
```

An empty passphrase was supplied when prompted.

### Result
PASS

Steghide detected the embedded file:

```text
stage1_payload.txt
```

---

## Test 5 – Payload Extraction

Commands:

```bash
mkdir -p /tmp/shadowvault-stage1-test
```

```bash
steghide extract -sf files/nova-office.jpeg -xf /tmp/shadowvault-stage1-test/stage1_payload.txt
```

An empty passphrase was supplied when prompted.

### Result
PASS

The embedded payload was successfully extracted.

---

## Test 6 – Flag Validation

Command:

```bash
cat /tmp/shadowvault-stage1-test/stage1_payload.txt
```

Recovered content:

```text
SHADOW{hidden_evidence_found}
NEXT: Recover the coded message in Stage 2.
```

### Result
PASS

The expected Stage 01 flag was successfully recovered:

`SHADOW{hidden_evidence_found}`

The progression clue correctly directs the participant to Stage 02.

## Reset Test

No reset mechanism is required because Stage 01 is a static challenge. The original JPEG remains unchanged during analysis and can be redistributed to participants when necessary.

## Final Test Status

**PASS**

Stage 01 is functional and ready for integration into the ShadowVault CTF platform.
