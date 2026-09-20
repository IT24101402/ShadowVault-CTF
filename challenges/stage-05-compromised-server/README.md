# Challenge Title

Compromised Server

## Domain

Linux Forensics

## Difficulty

Medium

## Scenario

NovaTech's Linux server was suspected of being compromised. The server contains
fictional forensic artifacts that can be investigated to trace the incident.

## Learning Objective

Learn how to investigate Linux authentication logs, shell history, and recovery
files to identify suspicious activity and recover a challenge flag and token.

## Player Task

Investigate the available files inside the container and identify the suspicious
SSH activity. Recover the Stage 5 flag and the vault token required for the next stage.

## Flag Format / Flag Logic

The Stage 5 flag follows the format:

`SHADOW{...}`

The flag is recovered from the planted forensic evidence.

## Files or Service

- `/var/log/auth.log`
- `/opt/novatech/recovery-note.txt`
- `/home/analyst/.bash_history`

## Required Tools

- `grep`
- `cat`
- Basic Linux shell commands

## Intended Solution Path

1. Inspect `/var/log/auth.log`.
2. Identify the successful SSH login.
3. Review `/home/analyst/.bash_history`.
4. Read `/opt/novatech/recovery-note.txt`.
5. Recover the Stage 5 flag and vault token.
6. Use the vault token in Stage 6.

## Hints

- Look for successful authentication events.
- Shell history can reveal commands previously executed.
- The recovery note contains the clue needed for the next stage.

## Dependencies

Docker and the Stage 5 Docker image.

## Validation / Test Evidence

The container was built successfully and the forensic files were accessed from
inside the running container.

## Reset / Recovery

Stop and recreate the container from the trusted Docker image.

## Next-Stage Clue

The recovered vault token is required by the final ShadowVault stage.

## Known Limitations

All evidence is fictional and intentionally planted for the CTF challenge.
It does not represent a real compromised server.
