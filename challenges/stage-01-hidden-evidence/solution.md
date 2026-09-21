# Stage 01 – Hidden Evidence: Solution

## Objective
Recover the hidden payload embedded inside `nova-office.jpeg` and obtain the Stage 01 flag.

## Challenge File
`files/nova-office.jpeg`

## Solution Procedure

### 1. Verify the File

```bash
file files/nova-office.jpeg
```

The file is identified as a valid JPEG image.

### 2. Inspect the Image

Basic analysis can be performed using:

```bash
exiftool files/nova-office.jpeg
```

Additional inspection can be performed using:

```bash
strings files/nova-office.jpeg
```

and:

```bash
binwalk files/nova-office.jpeg
```

### 3. Detect the Hidden Data

Check the image using Steghide:

```bash
steghide info files/nova-office.jpeg
```

When asked:

```text
Try to get information about embedded data ? (y/n)
```

enter:

```text
y
```

When prompted for a passphrase, press **Enter** without entering a password.

Steghide identifies the embedded file:

```text
stage1_payload.txt
```

### 4. Extract the Hidden File

Create a temporary directory:

```bash
mkdir -p /tmp/shadowvault-stage1-test
```

Extract the embedded file:

```bash
steghide extract -sf files/nova-office.jpeg -xf /tmp/shadowvault-stage1-test/stage1_payload.txt
```

When prompted for the passphrase, press **Enter**.

### 5. Read the Extracted File

```bash
cat /tmp/shadowvault-stage1-test/stage1_payload.txt
```

The recovered content is:

```text
SHADOW{hidden_evidence_found}
NEXT: Recover the coded message in Stage 2.
```

## Correct Flag

`SHADOW{hidden_evidence_found}`

## Progression

The recovered message directs the participant to Stage 02 – Coded Message.

## Validation

Stage 01 was manually tested on the Kali Linux CTF environment. The `stage1_payload.txt` file was successfully extracted from `nova-office.jpeg` using Steghide, and the expected flag and Stage 02 progression clue were recovered.
