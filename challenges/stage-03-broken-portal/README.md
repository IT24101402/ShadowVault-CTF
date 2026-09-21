# Stage 03 – Broken Portal

## Domain
Web Application Security

## Difficulty
Moderate

The challenge requires the participant to identify a broken access control condition in a web application and manipulate a predictable object identifier to access information that is not linked through the normal application interface.

## Scenario
The investigation has led to the NovaTech Internal Portal. The portal provides access to internal project information. During examination of the application, the participant must determine whether project resources are properly protected from unauthorized access.

## Learning Objective
Identify and exploit an Insecure Direct Object Reference (IDOR) / broken access control vulnerability in a controlled CTF environment.

## Player Task
Investigate the NovaTech Internal Portal and examine how individual project records are accessed. Discover information that should not normally be accessible and recover the Stage 03 flag and the clue leading to Stage 04.

## Flag Format / Flag Logic
Flags use the ShadowVault format:

`SHADOW{...}`

The Stage 03 flag is stored in the data associated with the protected ShadowVault project.

## Files or Service
Interactive Flask web application running inside a Docker container.

Application service:

- Flask web application
- Container port: 5000
- Main application: `app/app.py`

The root page provides access to Project 1. Additional project records are retrieved through numeric project identifiers.

## Required Tools
A participant can solve the challenge using:

- Web browser
- curl
- Basic HTTP inspection tools

No automated exploitation tool is required.

## Intended Solution Path
1. Open the NovaTech Internal Portal.
2. Observe the link to Project 1.
3. Examine the project URL structure.
4. Notice that project resources use predictable numeric identifiers.
5. Modify the project identifier to request another project.
6. Access the ShadowVault project because the application does not perform an authorization check.
7. Recover the Stage 03 flag.
8. Read the next-stage clue directing the participant to analyze captured network traffic.

## Hints
Possible hints:

1. Examine how the application identifies individual projects.
2. Consider whether changing the numeric project identifier provides access to another resource.

Hint penalties can be configured in CTFd during platform integration.

## Dependencies
- Docker Engine
- Python 3 container image
- Flask 3.1.0

The challenge does not require direct access to the CTFd database, Redis service, or the ShadowVault private backend network.

## Validation / Test Evidence
The challenge must be tested from a clean Docker build.

Validation should confirm:

- The Docker image builds successfully.
- The Flask application starts successfully.
- The portal is reachable through the configured host port.
- Project 1 is accessible through the normal interface.
- The unlinked ShadowVault project can be reached by manipulating the numeric project identifier.
- The expected Stage 03 flag is recoverable.
- The Stage 04 clue is displayed after reaching the ShadowVault project.
- Invalid project identifiers return an HTTP 404 response.

Detailed test commands and results are recorded in `test-notes.md`.

## Reset / Recovery
The challenge is designed to be disposable and stateless. Reset can be performed by stopping and recreating the Stage 03 Docker container from the trusted challenge image.

No participant-generated state needs to be preserved.

## Next-Stage Clue
Successful completion directs the participant to analyze captured network traffic, leading to Stage 04 – Network Trail.

## Known Limitations
The application is intentionally minimal and deliberately contains broken access control for educational CTF use. It must only be deployed inside the isolated ShadowVault CTF environment.

The challenge uses predictable in-memory project records rather than a production database because the objective is to demonstrate the access-control flaw without unnecessary infrastructure.
