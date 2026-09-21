# Stage 02 – Coded Message

## Domain
Cryptography / Encoding

## Difficulty
Easy

## Scenario
After recovering the hidden evidence from Stage 01, the investigation continues with an intercepted message associated with the NovaTech incident.

The message appears unreadable and has been encoded in multiple layers. The participant must identify the encoding methods and recover the original message.

## Learning Objective
Identify common data-encoding formats and apply the correct decoding sequence to recover hidden information.

## Player Task
Analyze the provided `intercepted_message.txt` file and decode the intercepted communication.

## Challenge File
`files/intercepted_message.txt`

## Suggested Tools
- `cat`
- `file`
- `base64`
- `xxd`
- CyberChef or equivalent decoding utilities

## Expected Approach

1. Inspect the intercepted message.
2. Recognize that the outer layer uses Base64 encoding.
3. Decode the Base64 content.
4. Identify the resulting data as hexadecimal text.
5. Convert the hexadecimal data back into plaintext.
6. Recover the Stage 02 flag.
7. Follow the recovered clue to Stage 03.

## Flag Format

`SHADOW{...}`

## Progression

Successfully decoding the intercepted communication reveals the Stage 02 flag and directs the participant to investigate the NovaTech internal portal in Stage 03.

## Challenge Type

Static file challenge.

No dedicated Docker container or network service is required for this stage. The challenge file can be distributed to participants through CTFd.

## Reset / Recovery

No reset operation is required. The original `intercepted_message.txt` file remains unchanged while participants analyze it and can be redistributed through CTFd if necessary.
