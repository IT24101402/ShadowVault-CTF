# Challenge Title

ShadowVault Recovery Gateway

## Domain

Web Application Security / Multi-Stage Analysis

## Difficulty

Hard

## Scenario

The final ShadowVault recovery gateway has entered emergency recovery mode.
Access requires two authorization factors recovered through the investigation:
the recovery token obtained from the compromised server in Stage 5 and a
verification code derived from the Stage 6 recovery-service evidence.

## Learning Objective

Learn how evidence recovered across multiple CTF stages can be correlated and
used to satisfy an application's authorization requirements. Players must
analyze recovery-service evidence, convert decimal ASCII values, and combine
the resulting verification code with the Stage 5 recovery token.

## Player Task

1. Retain the recovery token recovered during Stage 5.
2. Inspect the supplied `vault-access.log` evidence.
3. Identify the three decimal verification fragments.
4. Convert the fragments to ASCII characters.
5. Join the characters in A-B-C order.
6. Submit both authorization factors to the ShadowVault Recovery Gateway.
7. Recover the final flag.

## Flag Format / Flag Logic

The final flag follows the format:

`SHADOW{...}`

The gateway reveals the final flag only when both the correct recovery token
and the correct verification code are submitted.

## Files or Service

- Flask web application
- `evidence/vault-access.log`
- `/`
- `/unlock`
- Container port: `5000`
- Validation host mapping: `127.0.0.1:5006`

## Required Tools

- Web browser or `curl`
- Text editor or `cat`
- Basic decimal-to-ASCII conversion
- Python 3 or another ASCII reference may be used for conversion

## Intended Solution Path

1. Recover the Stage 5 vault token.
2. Inspect `evidence/vault-access.log`.
3. Identify verification fragments `73`, `86`, and `54`.
4. Convert the decimal values to ASCII:
   - `73` -> `I`
   - `86` -> `V`
   - `54` -> `6`
5. Combine them in A-B-C order to obtain `IV6`.
6. Access the recovery gateway.
7. Submit the Stage 5 token and the derived verification code.
8. Recover the final ShadowVault flag.

## Hints

- Stage 5 provides one authorization factor.
- The recovery-service log provides the second factor.
- Treat each verification fragment as a decimal ASCII value.
- Preserve A-B-C ordering when joining the characters.

## Dependencies

- Docker
- Stage 6 Docker image
- Recovery token obtained from Stage 5
- `evidence/vault-access.log`

## Validation / Test Evidence

The application was tested with multiple authorization combinations.

- Wrong token with correct verification code: HTTP 403
- Correct token with wrong verification code: HTTP 403
- Correct token with correct verification code: HTTP 200 and final flag

The container was also validated using a non-root user, read-only root
filesystem, 128 MB memory limit, and 0.50 CPU limit.

## Reset / Recovery

Stop and recreate the container from the trusted Stage 6 Docker image.
The challenge application does not require persistent player state.

## Next-Stage Clue

This is the final stage of Operation ShadowVault.

## Known Limitations

All application data, tokens, logs, addresses, and evidence are fictional and
intentionally created for the authorized CTF environment.
