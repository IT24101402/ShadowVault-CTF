# Stage 03 – Broken Portal: Intended Solution

## Vulnerability
Insecure Direct Object Reference (IDOR) / Broken Access Control.

The NovaTech Internal Portal retrieves project records using a numeric project identifier but does not perform an authorization check before returning the requested project.

## Intended Discovery

The participant first visits the portal root page:

`/`

The page provides a normal link to:

`/project/1`

Project 1 displays the Public Website Refresh project.

The participant should recognize that the application uses a predictable numeric identifier in the URL.

## Exploitation Path

Change the project identifier from:

`/project/1`

to:

`/project/2`

The application retrieves Project 2 without checking whether the participant is authorized to access it.

This exposes the ShadowVault project information.

## Expected Flag

`SHADOW{broken_portal_idor}`

## Next-Stage Clue

The ShadowVault project record also displays:

`NEXT: Analyze the captured network traffic.`

This directs the participant to Stage 04 – Network Trail.

## Example Verification with curl

After the challenge container is running, request the normal project:

```bash
curl http://127.0.0.1:<HOST_PORT>/project/1
