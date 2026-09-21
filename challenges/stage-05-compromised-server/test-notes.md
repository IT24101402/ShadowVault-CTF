# Stage 05 - Compromised Server: Test Notes

## Test Objective

Validate that Stage 05 builds and runs correctly as an isolated Docker forensic challenge and that the intended Linux forensic investigation path is reproducible.

## Test Environment

- Host: Kali Linux
- Container runtime: Docker Engine
- Challenge image: `shadowvault-stage05:test`
- Container name: `shadowvault-stage05-test`
- Container user: `analyst`
- Container working directory: `/home/analyst`
- Network access during validation: None
- Filesystem during validation: Read-only
- Memory limit: 128 MB
- CPU limit: 0.50 CPU

## 1. Clean Docker Image Build

The challenge was built from a clean state using:

```bash
docker build --no-cache \
  -t shadowvault-stage05:test \
  challenges/stage-05-compromised-server
```

Result: PASS

The Docker image built successfully.

## 2. Isolated Container Execution

The challenge was started using:

```bash
docker run -d \
  --name shadowvault-stage05-test \
  --network none \
  --read-only \
  --memory 128m \
  --cpus 0.50 \
  shadowvault-stage05:test
```

Result: PASS

The container remained operational without network access and with a read-only filesystem.

## 3. Player Identity Validation

Commands:

```bash
docker exec shadowvault-stage05-test whoami
docker exec shadowvault-stage05-test id
docker exec shadowvault-stage05-test pwd
```

Observed user:

```text
analyst
```

Observed working directory:

```text
/home/analyst
```

The challenge therefore executes using the intended non-root player account.

Result: PASS

## 4. Evidence Availability

The following forensic artifacts were confirmed inside the running container:

```text
/var/log/auth.log
/home/analyst/.bash_history
/opt/novatech/recovery-note.txt
```

The authentication log and recovery note were readable by the player, and the shell history was available to the `analyst` account.

Result: PASS

## 5. Authentication Log Investigation

The player inspected:

```bash
cat /var/log/auth.log
```

The log contained failed authentication attempts followed by a successful SSH login for the `analyst` account from:

```text
10.13.37.22
```

The log also contained evidence referencing access to the recovery note.

Result: PASS

## 6. Shell History Investigation

The player inspected:

```bash
cat ~/.bash_history
```

The history contained commands directing the investigation toward:

```text
/opt/novatech/recovery-note.txt
```

Result: PASS

## 7. Flag and Vault Token Recovery

The player followed the evidence trail and inspected:

```bash
cat /opt/novatech/recovery-note.txt
```

The expected Stage 05 flag was successfully recovered:

```text
SHADOW{compromised_server_traced}
```

The expected vault token was also recovered:

```text
NV-SV-6204
```

The next-stage clue instructed the player to use the recovered vault token in the final ShadowVault stage.

Result: PASS

## 8. Isolation Validation

Stage 05 successfully operated with:

- No container network connectivity
- Read-only container filesystem
- Non-root `analyst` user
- 128 MB memory limit
- 0.50 CPU limit

The challenge does not require an exposed network service. The SSH activity represented in `auth.log` is synthetic forensic evidence and does not require a live SSH daemon.

Result: PASS

## 9. Reset / Recovery

Stage 05 contains static forensic evidence inside its Docker image.

The challenge can be reset by removing and recreating the container:

```bash
docker rm -f shadowvault-stage05-test

docker run -d \
  --name shadowvault-stage05-test \
  --network none \
  --read-only \
  --memory 128m \
  --cpus 0.50 \
  shadowvault-stage05:test
```

This restores the challenge from the validated Docker image.

Result: PASS

## Test Conclusion

Stage 05 passed integration validation.

The Docker image builds successfully, the container operates using a non-root player account, the forensic artifacts are accessible, and the intended investigation path is reproducible.

The Stage 05 flag, vault token, and Stage 06 clue were independently recovered during testing.

Stage 05 is suitable for integration into the Operation ShadowVault CTF challenge flow.
