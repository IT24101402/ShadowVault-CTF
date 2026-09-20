# Challenge Title

ShadowVault Recovery Gateway

## Domain

Web Application Security

## Difficulty

Medium

## Scenario

The final ShadowVault gateway is protected by a recovery token obtained from
the previous compromised-server stage.

## Learning Objective

Learn how a web application validates a recovery token and how information
recovered from an earlier challenge can be used to access a protected service.

## Player Task

Access the ShadowVault gateway and submit the recovery token recovered from
Stage 5.

## Flag Format / Flag Logic

The final flag follows the format:

`SHADOW{...}`

A correct recovery token unlocks the final flag.

## Files or Service

- Flask web application
- `/`
- `/unlock`

## Required Tools

- Web browser or `curl`
- Basic HTTP knowledge

## Intended Solution Path

1. Start the Stage 6 Docker container.
2. Access the gateway at port 5006.
3. Submit the recovery token obtained from Stage 5.
4. Confirm that an incorrect token is rejected.
5. Submit the correct token.
6. Recover the final ShadowVault flag.

## Hints

- The required token was recovered in Stage 5.
- The `/unlock` endpoint accepts the recovery token.
- An incorrect token should be rejected.

## Dependencies

Docker and the Stage 6 Docker image.

## Validation / Test Evidence

The application was tested with both an incorrect token and the correct
Stage 5 recovery token. The incorrect token returned HTTP 403, while the
correct token returned the final flag.

## Reset / Recovery

Stop the container and start a new container from the trusted Docker image.

## Next-Stage Clue

This is the final stage of the ShadowVault challenge.

## Known Limitations

The application and recovery token are fictional and intentionally created
for the CTF challenge.
