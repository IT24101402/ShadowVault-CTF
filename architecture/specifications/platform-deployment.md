# Operation ShadowVault - Platform Deployment Specification

## 1. Purpose

This document defines the deployment architecture for the Operation ShadowVault CTF platform.

The platform is designed to provide a reproducible and isolated environment where participants can access the CTFd platform, download static challenge artifacts, interact with containerized challenges, and submit recovered flags.

The deployment separates the CTF management infrastructure from intentionally vulnerable challenge environments.

---

## 2. Host Environment

The current development and deployment environment uses:

- Host environment: Kali Linux virtual machine
- Kali release: Kali GNU/Linux Rolling
- Architecture: ARM64 (aarch64)
- Virtualization: UTM
- Container runtime: Docker Engine
- Container orchestration: Docker Compose
- Version control: Git and GitHub

The Kali VM acts as the Docker host. Intentionally vulnerable challenge services are not installed directly on the Kali host.

---

## 3. Platform Components

The core platform consists of three containerized services.

### CTFd

CTFd provides:

- User and team management
- Challenge presentation
- Static challenge file distribution
- Hint management
- Flag validation
- Scoring
- Scoreboard functionality
- Administrative management

Container name:

`shadowvault-ctfd`

The development deployment exposes CTFd through TCP port 8000.

Development access:

`http://localhost:8000`

### MariaDB

MariaDB provides persistent database storage for the CTFd platform.

Container name:

`shadowvault-db`

Internal service port:

`3306`

MariaDB is not directly published to the host or participant network.

### Redis

Redis provides the cache/session-support service required by the platform configuration.

Container name:

`shadowvault-redis`

Internal service port:

`6379`

Redis is not directly published to the host or participant network.

---

## 4. Docker Network Architecture

The platform currently uses two logically separate Docker networks.

### Frontend Network

Network name:

`shadowvault_frontend`

Type:

Docker bridge network

Internal:

`false`

Purpose:

The frontend network provides the network path required for the CTFd service to be exposed to the host.

Only CTFd is attached to this network.

### Backend Network

Network name:

`shadowvault_backend`

Type:

Docker bridge network

Internal:

`true`

Attached services:

- shadowvault-ctfd
- shadowvault-db
- shadowvault-redis

Purpose:

The backend network provides private communication between CTFd and its supporting database and Redis services.

The network is configured as an internal Docker network to reduce unnecessary external connectivity.

MariaDB and Redis do not publish their service ports to the host.

---

## 5. Dual-Network CTFd Design

CTFd participates in both the frontend and backend networks.

This provides controlled separation between participant-facing platform access and backend service communication.

Logical communication path:

Participant
    |
    v
Kali VM : TCP/8000
    |
    v
shadowvault_frontend
    |
    v
CTFd
    |
    v
shadowvault_backend
    |
    +---- MariaDB
    |
    +---- Redis

Participants should never require direct access to MariaDB or Redis.

---

## 6. Challenge Delivery Architecture

Operation ShadowVault contains six challenges using two delivery models.

### Static Challenges

The following challenges are distributed as files through CTFd:

- Stage 01 - Hidden Evidence
- Stage 02 - Coded Message
- Stage 04 - Network Trail

These challenges do not require continuously running dedicated challenge containers.

### Interactive Challenges

The following challenges are designed as containerized interactive environments:

- Stage 03 - Broken Portal
- Stage 05 - Compromised Server
- Stage 06 - ShadowVault

Each interactive challenge is developed as an independent Docker image and is integrated with the platform after individual challenge development and validation.

---

## 7. Challenge Network Isolation

Dedicated Docker bridge networks are reserved for the interactive challenges:

- `shadowvault_stage03`
- `shadowvault_stage05`
- `shadowvault_stage06`

Interactive challenge containers must not be attached to `shadowvault_backend`.

Therefore, challenge services cannot directly communicate with the CTFd database or Redis service through the private backend network.

The intended architecture is:

Participant
    |
    +----> CTFd
    |
    +----> Stage 03 service
    |
    +----> Stage 05 environment
    |
    +----> Stage 06 service

The participant discovers flags inside the challenge environments and manually submits those flags to CTFd for validation.

The challenge containers do not require direct communication with CTFd for flag submission.

---

## 8. Persistent and Disposable State

### Persistent Platform State

The following Docker volumes are used for persistent platform data:

- `shadowvault_db_data`
- `shadowvault_redis_data`
- `shadowvault_ctfd_uploads`
- `shadowvault_ctfd_logs`

This allows the platform state to survive normal container recreation.

### Disposable Challenge State

Interactive challenge containers are designed to be disposable.

If a challenge environment becomes modified or unusable, it can be stopped, removed, and recreated from its trusted Docker image.

This provides a simple reset and recovery mechanism.

---

## 9. Secret Management

Deployment secrets are stored in a local `.env` file.

Examples include:

- Database credentials
- CTFd secret key
- Platform configuration values

The real `.env` file is excluded from Git version control.

A sanitized `.env.example` file is maintained in the repository to document the required variables without exposing operational secrets.

Passwords, authentication tokens, private keys, and other real secrets must not be committed to the repository.

---

## 10. Security Controls

The platform architecture applies the following controls:

- CTFd backend services are separated from participant-facing access.
- MariaDB is not directly exposed to participants.
- Redis is not directly exposed to participants.
- Backend communication uses an internal Docker network.
- Interactive challenge environments use dedicated networks.
- Challenge containers must not join the CTFd backend network.
- Challenge containers must not receive the Docker socket.
- Unnecessary host directories must not be mounted into challenge containers.
- Challenge containers should run without privileged mode.
- Non-root execution should be used where technically practical.
- Only required challenge ports should be published.
- Challenge data must contain only fictional or intentionally created CTF information.
- Challenge containers should be reproducible from trusted project files.

---

## 11. Current Validation

The core platform deployment has been tested with Docker Compose.

The following containers have been confirmed running:

- `shadowvault-ctfd`
- `shadowvault-db`
- `shadowvault-redis`

CTFd has been successfully accessed through:

`http://localhost:8000`

Network inspection has confirmed:

`shadowvault_frontend`
- Internal = false
- Attached container = shadowvault-ctfd

`shadowvault_backend`
- Internal = true
- Attached containers = shadowvault-ctfd, shadowvault-db, shadowvault-redis

This confirms that the core platform currently implements frontend/backend network separation.

---

## 12. Integration Plan

Challenge development is divided between team members.

- Member 2 develops Stages 01 and 02.
- Member 3 develops Stages 03 and 04.
- Member 4 develops Stages 05 and 06.
- Member 1 maintains the platform architecture and performs platform integration.

After individual challenge development:

1. Each challenge is validated independently.
2. Completed challenge work is merged through the team Git workflow.
3. Static artifacts are added to their corresponding CTFd challenges.
4. Interactive challenge Docker images are built.
5. Interactive services are connected only to their designated challenge networks.
6. Required challenge ports are configured.
7. Flags are configured in CTFd.
8. Stage-to-stage clues are validated.
9. Reset and recovery procedures are tested.
10. The complete six-stage challenge flow is tested from the participant perspective.

---

## 13. Planned Challenge Flow

The intended challenge sequence is:

Stage 01 - Hidden Evidence
        |
        v
Stage 02 - Coded Message
        |
        v
Stage 03 - Broken Portal
        |
        v
Stage 04 - Network Trail
        |
        v
Stage 05 - Compromised Server
        |
        v
Stage 06 - ShadowVault

Each stage should provide evidence or a clue that logically directs the participant toward the following stage.

The final stage acts as the capstone of the Operation ShadowVault investigation.

---

## 14. Current Implementation Status

Implemented and tested:

- Kali Linux Docker host
- Docker Engine
- Docker Compose
- CTFd container
- MariaDB container
- Redis container
- Persistent Docker volumes
- Frontend Docker network
- Internal backend Docker network
- CTFd access through TCP port 8000
- Backend isolation between participant-facing access and support services
- Dedicated challenge network definitions
- Six-stage repository directory structure

Pending team integration:

- Stage 01 artifact
- Stage 02 artifact
- Stage 03 interactive container
- Stage 04 PCAP artifact
- Stage 05 interactive container
- Stage 06 interactive container
- CTFd challenge configuration for all six stages
- Complete end-to-end challenge validation

