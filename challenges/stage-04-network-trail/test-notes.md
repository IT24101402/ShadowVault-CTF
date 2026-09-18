# Test Notes

The PCAP was generated using local loopback traffic only.

HTTP server:
python3 -m http.server 8088 --bind 127.0.0.1

Capture:
sudo tcpdump -i lo -w files/network-trail.pcap tcp port 8088

Test request:
curl http://127.0.0.1:8088/evidence.txt

Validation:
tshark -r files/network-trail.pcap
tshark -r files/network-trail.pcap -Y http -T fields -e http.request.uri
tshark -r files/network-trail.pcap -Y 'http.file_data' -T fields -e http.file_data
