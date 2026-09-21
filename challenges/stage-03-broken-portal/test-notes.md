# Stage 03 – Broken Portal: Test Notes

## Test Objective

Validate that Stage 03 builds and runs correctly as an isolated Docker challenge and that the intended IDOR / broken access control solution path is reproducible.

## Test Environment

- Host: Kali Linux
- Container runtime: Docker Engine
- Challenge image: `shadowvault-stage03:test`
- Container name: `shadowvault-stage03-test`
- Host test address: `127.0.0.1`
- Host test port: `3000`
- Container application port: `5000`
- Application framework: Flask 3.1.0

## 1. Clean Docker Image Build

Command:

```bash
docker build -t shadowvault-stage03:test challenges/stage-03-broken-portal
```

Result:

**PASS**

Docker completed all build steps successfully and created the image:

`shadowvault-stage03:test`

## 2. Clean Container Recreation

An older Stage 03 test container was found during validation. It was removed before performing the clean integration test.

Commands:

```bash
docker rm -f shadowvault-stage03-test

docker run -d \
  --name shadowvault-stage03-test \
  -p 127.0.0.1:3000:5000 \
  shadowvault-stage03:test
```

Container verification command:

```bash
docker ps --filter name=shadowvault-stage03-test
```

Result:

**PASS**

The fresh Stage 03 container started successfully.

The verified port mapping was:

`127.0.0.1:3000 -> 5000/tcp`

This maps port 3000 on the Kali host to the Flask application running on port 5000 inside the challenge container.

## 3. Portal Root Test

Command:

```bash
curl -i http://127.0.0.1:3000/
```

Result:

**PASS – HTTP 200 OK**

The response displayed:

`NovaTech Internal Portal`

The normal application interface provided a link to:

`/project/1`

This confirms that the participant entry point is reachable and functioning.

## 4. Legitimate Project Test

Command:

```bash
curl -i http://127.0.0.1:3000/project/1
```

Result:

**PASS – HTTP 200 OK**

The application returned:

- Project: `Public Website Refresh`
- Data: `Routine project.`

The Stage 03 flag was not exposed through the normal Project 1 route.

## 5. IDOR / Broken Access Control Test

Command:

```bash
curl -i http://127.0.0.1:3000/project/2
```

Result:

**PASS – HTTP 200 OK**

The predictable project identifier was manually changed from `1` to `2`.

The application returned the unlinked ShadowVault project without performing an authorization check.

The response exposed:

`ShadowVault`

Recovered Stage 03 flag:

`SHADOW{broken_portal_idor}`

Recovered next-stage clue:

`NEXT: Analyze the captured network traffic.`

This confirms that the intended IDOR / broken access control vulnerability is reproducible and that successful completion correctly directs the participant to Stage 04 – Network Trail.

## 6. Invalid Project Identifier Test

Command:

```bash
curl -i http://127.0.0.1:3000/project/999
```

Result:

**PASS – HTTP 404 NOT FOUND**

The application correctly returned an HTTP 404 response for a project identifier that does not exist.

This confirms that nonexistent project records are handled separately from the intentionally accessible ShadowVault project.

## Overall Validation Result

**PASS**

Stage 03 successfully demonstrates the intended IDOR / broken access control vulnerability inside the controlled Operation ShadowVault CTF environment.

The following items were successfully validated:

- Docker image builds successfully.
- Fresh challenge container starts successfully.
- Flask application is reachable through the configured host port.
- Portal root returns HTTP 200.
- Project 1 is accessible through the legitimate application path.
- Project 2 can be accessed by manipulating the predictable project identifier.
- The expected Stage 03 flag is recoverable.
- The Stage 04 clue is displayed correctly.
- Invalid project identifiers return HTTP 404.

## Reset / Recovery

Stage 03 does not require persistent participant state.

The challenge can be reset by removing the current challenge container and recreating it from the trusted Docker image.

Reset commands:

```bash
docker rm -f shadowvault-stage03-test

docker run -d \
  --name shadowvault-stage03-test \
  -p 127.0.0.1:3000:5000 \
  shadowvault-stage03:test
```

This recreates Stage 03 in a clean state from the validated challenge image.

## Test Conclusion

Stage 03 passed the integration validation.

The challenge is reproducible, the intended vulnerability works as designed, the flag and next-stage clue are recoverable, and the container can be reset by recreation.
