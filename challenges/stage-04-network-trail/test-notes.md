# Stage 04 - Network Trail: Test Notes

## Test Objective

Validate that the Stage 04 PCAP can be analyzed successfully, that the intended HTTP evidence can be identified, and that the Stage 04 flag and Stage 05 clue are recoverable.

## Test Environment

- Host: Kali Linux
- Analysis tool: TShark 4.6.6 / Wireshark
- Challenge type: Static PCAP forensic challenge
- Challenge file: `files/network-trail.pcap`
- Capture format: PCAP
- Traffic type: Synthetic HTTP traffic
- Capture interface used during generation: Local loopback

## 1. PCAP File Validation

The challenge artifact was verified with:

```bash
file challenges/stage-04-network-trail/files/network-trail.pcap
```

The file was successfully identified as a valid PCAP capture.

Result: PASS

## 2. General Packet Parsing Test

The capture was parsed using:

```bash
tshark -r challenges/stage-04-network-trail/files/network-trail.pcap
```

TShark successfully processed the capture and displayed TCP and HTTP traffic.

The relevant HTTP communication included a request for `/evidence.txt` and its corresponding HTTP response.

Result: PASS

## 3. HTTP Request Validation

The HTTP request information was extracted using:

```bash
tshark -r challenges/stage-04-network-trail/files/network-trail.pcap \
  -Y 'http.request' \
  -T fields \
  -e http.request.method \
  -e http.request.uri
```

Observed result:

```text
GET    /evidence.txt
```

This confirms that the intended suspicious resource can be identified from the packet capture.

Result: PASS

## 4. HTTP Conversation Validation

The HTTP conversation was inspected using:

```bash
tshark -r challenges/stage-04-network-trail/files/network-trail.pcap \
  -Y 'http' \
  -T fields \
  -e frame.number \
  -e ip.src \
  -e ip.dst \
  -e http.request.method \
  -e http.request.uri \
  -e http.response.code
```

Observed relevant traffic:

```text
Frame 4: 127.0.0.1 -> 127.0.0.1    GET    /evidence.txt
Frame 8: 127.0.0.1 -> 127.0.0.1           /evidence.txt    200
```

This confirms that both the HTTP request and its successful HTTP 200 response are present.

The loopback addresses are expected because the challenge traffic was generated locally as synthetic traffic for the isolated CTF environment.

Result: PASS

## 5. HTTP Payload Extraction Test

The HTTP response payload was extracted using:

```bash
tshark -r challenges/stage-04-network-trail/files/network-trail.pcap \
  -Y 'http.file_data' \
  -T fields \
  -e http.file_data
```

TShark successfully returned the HTTP file data as hexadecimal payload data.

Result: PASS

## 6. Payload Decoding Test

The extracted hexadecimal payload was converted to readable text using:

```bash
tshark -r challenges/stage-04-network-trail/files/network-trail.pcap \
  -Y 'http.file_data' \
  -T fields \
  -e http.file_data | xxd -r -p
```

Observed result:

```text
SHADOW{network_trail_found}
NEXT: Investigate the compromised Linux server.
```

Result: PASS

## 7. Flag Validation

Expected Stage 04 flag:

```text
SHADOW{network_trail_found}
```

Recovered Stage 04 flag:

```text
SHADOW{network_trail_found}
```

The recovered flag exactly matches the expected challenge flag.

Result: PASS

## 8. Next-Stage Clue Validation

Expected clue:

```text
NEXT: Investigate the compromised Linux server.
```

Recovered clue:

```text
NEXT: Investigate the compromised Linux server.
```

The clue correctly directs the participant toward Stage 05 - Compromised Server.

Result: PASS

## 9. Player Solution Path Validation

The validated solution path is:

1. Obtain `network-trail.pcap`.
2. Open the capture using Wireshark or TShark.
3. Identify the HTTP traffic.
4. Locate the request for `/evidence.txt`.
5. Inspect the corresponding HTTP response.
6. Recover the response payload.
7. Identify `SHADOW{network_trail_found}`.
8. Read the next-stage clue.
9. Continue to Stage 05 - Compromised Server.

Result: PASS

## 10. Reset / Recovery Validation

Stage 04 is a static challenge and does not maintain runtime state.

No Docker container or service reset is required.

If the challenge artifact is modified or deleted, reset can be performed by restoring the validated repository copy:

```text
files/network-trail.pcap
```

Result: PASS

## Test Conclusion

Stage 04 passed integration validation.

The PCAP is valid and readable, the intended HTTP request can be identified, the corresponding HTTP response is present, and the evidence payload can be successfully recovered.

The expected Stage 04 flag and Stage 05 clue were both independently recovered during integration testing.

The challenge is reproducible and suitable for integration into the Operation ShadowVault CTF challenge flow.
