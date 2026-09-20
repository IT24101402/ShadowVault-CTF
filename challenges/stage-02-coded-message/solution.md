# Stage 02 – Coded Message: Solution

## Objective

Decode the intercepted communication stored in `intercepted_message.txt` and recover the Stage 02 flag and progression clue.

## Challenge File

`files/intercepted_message.txt`

## Solution Procedure

### 1. Inspect the Intercepted Message

Display the contents of the challenge file:

```bash
cat files/intercepted_message.txt
```

The message appears as a long encoded string. The characters and `=` padding at the end indicate that Base64 encoding may have been used.

### 2. Decode the Base64 Layer

Run:

```bash
base64 -d files/intercepted_message.txt
```

The resulting output is another long string containing hexadecimal characters.

This indicates that a second encoding layer has been used.

### 3. Decode the Hexadecimal Layer

The Base64 output can be passed directly to `xxd`:

```bash
base64 -d files/intercepted_message.txt | xxd -r -p
```

The `xxd -r -p` command converts the hexadecimal representation back into plaintext.

### 4. Recover the Message

The decoded plaintext is:

```text
SHADOW{coded_message_recovered}
NEXT: Investigate the NovaTech internal portal.
```

## Correct Flag

`SHADOW{coded_message_recovered}`

## Encoding Sequence

The challenge uses two encoding layers:

```text
Original Plaintext
       ↓
Hexadecimal Encoding
       ↓
Base64 Encoding
       ↓
intercepted_message.txt
```

The participant therefore solves the challenge in the reverse order:

```text
intercepted_message.txt
       ↓
Base64 Decoding
       ↓
Hexadecimal Decoding
       ↓
Original Plaintext
```

## Progression

The recovered message instructs the participant to investigate the NovaTech internal portal.

This provides the narrative transition to:

**Stage 03 – Broken Portal**

## Validation

Stage 02 was manually tested in the Kali Linux CTF environment.

The Base64 layer was successfully decoded, the resulting hexadecimal data was converted to plaintext using `xxd -r -p`, and the expected Stage 02 flag and Stage 03 progression clue were successfully recovered.
