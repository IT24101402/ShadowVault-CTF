# Operation ShadowVault – Challenge Container Standard

## Purpose

This document defines the standard architecture and security requirements for interactive challenge containers used in the Operation ShadowVault CTF platform.

The purpose is to ensure that challenge environments are reproducible, isolated, resettable, and consistent across the project.

## Challenge Types

Operation ShadowVault contains two challenge delivery models:

### Static Challenges
Stages 01, 02, and 04 are static challenges.

Challenge files are distributed through CTFd and do not require dedicated Docker containers.

### Interactive Challenges
Stages 03, 05, and 06 use dedicated Docker containers.

Each interactive challenge must operate independently and must not have direct access to the CTF platform backend.

## Container Naming Convention

Interactive containers should follow this naming convention:

- Stage 03: `shadowvault-stage03`
- Stage 05: `shadowvault-stage05`
- Stage 06: `shadowvault-stage06`

## Network Isolation

Each interactive challenge must use its own Docker bridge network:

- `shadowvault_stage03`
- `shadowvault_stage05`
- `shadowvault_stage06`

Challenge containers must NOT connect to:

- `shadowvault_backend`
- MariaDB
- Redis
- Docker socket
- Other challenge networks unless explicitly required by the challenge design

The CTFd platform uses two separate networks:

- `shadowvault_frontend` – participant-facing access to CTFd
- `shadowvault_backend` – internal communication between CTFd, MariaDB, and Redis

The backend network is configured as an internal Docker network.

## Port Exposure

Only ports required to solve a challenge should be published.

Examples:

- Stage 03 – HTTP web service
- Stage 05 – SSH or another intentionally exposed service
- Stage 06 – service defined by the final integrated challenge

Database and Redis ports must never be published to participants.

## Container Security Requirements

Interactive challenge containers should:

- Run without privileged mode.
- Avoid unnecessary Linux capabilities.
- Avoid mounting sensitive host directories.
- Never mount `/var/run/docker.sock`.
- Use minimal base images where practical.
- Expose only required services.
- Use resource limits where practical.
- Avoid storing platform credentials.
- Avoid direct access to the CTFd database.
- Be reproducible from Dockerfiles and project files.

## Flag Standard

All Operation ShadowVault flags use the following format:

`SHADOW{flag_value}`

Flags are validated by CTFd.

Challenge containers do not require direct communication with CTFd for flag validation.

Participants retrieve a flag from the challenge environment and manually submit it through the CTFd interface.

## Persistence and Reset

CTFd platform data is persistent.

Challenge containers are considered disposable.

Interactive challenges should be recoverable by recreating their containers from trusted Docker images.

Persistent host volumes should not be used for challenge state unless specifically required.

## Challenge Directory Standard

Each interactive challenge should contain, where applicable:

- `Dockerfile`
- `README.md`
- Application or service source files
- Required configuration files
- Reset or initialization scripts
- Testing instructions

Each challenge README should document:

- Challenge name
- Stage number
- Domain
- Difficulty
- Learning objective
- Required service
- Expected solution path
- Flag location or logic
- Hints
- Dependencies
- Reset procedure

## Architecture Principle

The challenge environment may intentionally contain vulnerabilities required by the CTF scenario.

The surrounding platform infrastructure must remain isolated from those vulnerabilities.

A compromise of one challenge container should not provide direct access to CTFd, MariaDB, Redis, the Docker host, or another challenge container.
