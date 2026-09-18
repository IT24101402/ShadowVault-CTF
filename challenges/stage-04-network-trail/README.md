# Network Trail

## Domain
Network Forensics

## Difficulty
Easy

## Scenario
A suspicious network capture was recovered from the NovaTech environment.

## Learning Objective
Analyze captured HTTP traffic and identify hidden evidence.

## Player Task
Inspect the provided PCAP file and locate the suspicious HTTP request and its contents.

## Flag Format / Flag Logic
SHADOW{...}

## Files or Service
files/network-trail.pcap

## Required Tools
Wireshark or tshark

## Intended Solution Path
Open the PCAP, inspect HTTP traffic, and follow the relevant TCP/HTTP stream.

## Hints
Look closely at HTTP requests and transferred file contents.

## Dependencies
None

## Validation / Test Evidence
Validated using tshark and Wireshark.

## Reset / Recovery
The PCAP is static and can be restored from the repository.

## Next-Stage Clue
The recovered evidence points the player toward investigating the compromised Linux server.

## Known Limitations
The traffic is synthetic and created only for the CTF environment.
