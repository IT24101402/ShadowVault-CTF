# Stage 4 Solution

1. Open `files/network-trail.pcap` in Wireshark.
2. Apply the filter:

   http

3. Locate the request for:

   /evidence.txt

4. Follow the HTTP/TCP stream.

5. The response contains:

   SHADOW{network_trail_found}

6. The next clue is:

   NEXT: Investigate the compromised Linux server.
