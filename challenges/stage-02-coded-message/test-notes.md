# Stage 02 – Coded Message: Test Notes

## Test Objective

Verify that the Stage 02 challenge file can be successfully decoded and that it produces the expected flag and progression clue.

## Test Environment

- Operating System: Kali GNU/Linux Rolling 2026.2
- Architecture: ARM64 (aarch64)
- Environment: UTM Virtual Machine
- Challenge Type: Static file-based challenge
- Challenge File: `files/intercepted_message.txt`

## Test 1 – Verify Challenge File Exists

Command:

```bash
ls -lh files/intercepted_message.txt
```

Expected Result:

The `intercepted_message.txt` file exists and is readable.

Result:

**PASS**

## Test 2 – Inspect Encoded Message

Command:

```bash
cat files/intercepted_message.txt
```

Expected Result:

A long encoded string is displayed.

Result:

**PASS**

## Test 3 – Base64 Decode

Command:

```bash
base64 -d files/intercepted_message.txt
```

Expected Result:

The Base64 layer is successfully decoded and produces hexadecimal data.

Result:

**PASS**

## Test 4 – Hexadecimal Decode

Command:

```bash
base64 -d files/intercepted_message.txt | xxd -r -p
```

Expected Result:

The following plaintext is recovered:

```text
SHADOW{coded_message_recovered}
NEXT: Investigate the NovaTech internal portal.
```

Result:

**PASS**

## Test 5 – Flag Validation

Expected Flag:

```text
SHADOW{coded_message_recovered}
```

Observed Flag:

```text
SHADOW{coded_message_recovered}
```

Result:

**PASS**

## Test 6 – Progression Validation

Expected progression clue:

```text
NEXT: Investigate the NovaTech internal portal.
```

The recovered clue correctly directs the participant toward Stage 03 – Broken Portal.

Result:

**PASS**

## Final Test Result

**PASS**

Stage 02 was successfully tested from the supplied challenge file. The Base64 and hexadecimal encoding layers were decoded in the expected order, the correct flag was recovered, and the progression clue successfully directs the participant to Stage 03.
