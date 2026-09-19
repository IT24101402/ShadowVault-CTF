# Operation ShadowVault – Platform Verification

## 1. Purpose

This document records the verification activities performed on the Operation ShadowVault CTF platform infrastructure.

The objective is to confirm that the base CTF platform is operational, persistent, isolated, and suitable for later integration of the six planned CTF challenges.

---

## 2. Test Environment

- Host OS: Kali GNU/Linux Rolling 2026.2
- Architecture: ARM64 (aarch64)
- Virtualization: UTM Virtual Machine
- Container Platform: Docker Engine
- Orchestration: Docker Compose
- CTF Platform: CTFd
- Database: MariaDB 11.4
- Cache Service: Redis 7 Alpine

---

## 3. Base Platform Verification

### 3.1 Container Startup

The following platform containers were successfully deployed:

- `shadowvault-ctfd`
- `shadowvault-db`
- `shadowvault-redis`

Result: PASS

All three containers successfully started using Docker Compose.

---

### 3.2 CTFd Web Access

CTFd was successfully accessed through:

`http://localhost:8000`

Only the CTFd service publishes a host-facing port.

Result: PASS

---

## 4. Network Isolation Verification

Two platform Docker bridge networks are currently implemented:

### Frontend Network

Network:

`shadowvault_frontend`

CTFd is connected to this network to provide participant access to the CTF web interface.

### Private Backend Network

Network:

`shadowvault_backend`

The backend network contains:

- CTFd
- MariaDB
- Redis

Docker inspection confirmed:

`Internal: true`

This prevents direct external access to the backend network while allowing CTFd to communicate with MariaDB and Redis.

Result: PASS

---

## 5. Port Exposure Verification

Docker port inspection confirmed:

- CTFd: Host port `8000` mapped to container port `8000`
- MariaDB: No host port published
- Redis: No host port published

Therefore, participants cannot directly access the database or Redis service through published Docker host ports.

Result: PASS

---

## 6. Container Privilege Verification

Docker inspection confirmed:

- `shadowvault-ctfd` → Privileged=false
- `shadowvault-db` → Privileged=false
- `shadowvault-redis` → Privileged=false

Result: PASS

The base platform containers are not running in Docker privileged mode.

---

## 7. Persistent Storage Verification

Docker-managed volumes are used for:

- CTFd uploads
- CTFd logs
- MariaDB data
- Redis data

The platform containers were recreated after configuration changes.

The previously configured CTFd challenges remained available after container recreation.

Result: PASS

This verifies that important platform state is persistent and is not dependent on the lifecycle of an individual container.

---

## 8. Resource Limit Verification

CPU and memory limits were configured for the base platform services.

Docker inspection confirmed that resource restrictions are applied to:

- CTFd
- MariaDB
- Redis

Result: PASS

This reduces the possibility of a single platform service consuming all available host resources.

---

## 9. CTF Challenge Flow Verification

Six challenge entries were configured in CTFd:

1. Stage 01 – Hidden Evidence
2. Stage 02 – Coded Message
3. Stage 03 – Broken Portal
4. Stage 04 – Network Trail
5. Stage 05 – Compromised Server
6. Stage 06 – ShadowVault

Temporary `SHADOW{...}` flags were configured for platform testing.

CTFd requirement rules were configured to provide sequential challenge progression.

The progression model is:

`Stage 01 → Stage 02 → Stage 03 → Stage 04 → Stage 05 → Stage 06`

Testing confirmed that completing a stage allows the next required stage to become accessible.

Result: PASS

---

## 10. Flag Validation Verification

A temporary Stage 01 flag was submitted through the participant interface.

CTFd successfully:

- accepted the correct flag,
- marked the challenge as solved,
- awarded the challenge points, and
- recorded the solve.

Result: PASS

Temporary flags will be replaced with final challenge flags during challenge integration.

---

## 11. Hint System Verification

Hints were configured within CTFd with point penalties.

Testing confirmed that the platform supports challenge hints and associated point costs.

Result: PASS

Final hint content may be updated when challenge development is completed.

---

## 12. Interactive Challenge Isolation

The architecture reserves separate Docker networks for the interactive stages:

- `shadowvault_stage03`
- `shadowvault_stage05`
- `shadowvault_stage06`

These networks are intended for:

- Stage 03 – Broken Portal
- Stage 05 – Compromised Server
- Stage 06 – ShadowVault

Each interactive challenge will operate in a dedicated Docker container and will not be connected to `shadowvault_backend`.

Status: PENDING INTEGRATION TESTING

The final isolation tests will be performed after the Stage 03, Stage 05, and Stage 06 challenge containers are delivered and integrated.

Required final tests include:

- Verify each challenge container is attached only to its intended challenge network.
- Verify challenge containers cannot directly access MariaDB.
- Verify challenge containers cannot directly access Redis.
- Verify challenge containers do not have access to the Docker socket.
- Verify containers are not running in privileged mode.
- Verify only required challenge ports are published.
- Verify challenge reset through container recreation.
- Verify resource restrictions are applied.

---

## 13. Current Verification Summary

| Verification Item | Status |
|---|---|
| CTFd deployment | PASS |
| MariaDB deployment | PASS |
| Redis deployment | PASS |
| CTFd web access | PASS |
| Private backend network | PASS |
| Database port isolation | PASS |
| Redis port isolation | PASS |
| Non-privileged base containers | PASS |
| Persistent platform storage | PASS |
| CPU and memory restrictions | PASS |
| Six-stage CTF configuration | PASS |
| Sequential challenge progression | PASS |
| Temporary flag validation | PASS |
| Hint mechanism | PASS |
| Interactive challenge isolation | PENDING |
| Interactive challenge reset testing | PENDING |

---

## 14. Conclusion

The Operation ShadowVault base CTF platform has been successfully deployed and verified.

The control layer, database, cache service, persistent storage, network separation, resource restrictions, challenge progression, flag validation, and hint functionality are operational.

The remaining infrastructure verification depends on integration of the interactive Stage 03, Stage 05, and Stage 06 challenge containers. These tests will be completed during the challenge integration and final testing phase.
