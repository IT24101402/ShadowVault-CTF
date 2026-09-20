# Stage 6 Solution

1. Start the Stage 6 container:

docker run --rm --name shadowvault-stage6 -p 5006:5000 shadowvault-stage6

2. Access the gateway:

curl http://127.0.0.1:5006/

3. Test an incorrect token:

curl -i -X POST -d 'token=wrong' http://127.0.0.1:5006/unlock

The server should return HTTP 403.

4. Use the recovery token obtained from Stage 5:

NV-SV-6204

5. Submit the correct token:

curl -i -X POST -d 'token=NV-SV-6204' http://127.0.0.1:5006/unlock

6. The final flag is:

SHADOW{shadowvault_recovered}

This is the final stage of the ShadowVault challenge.
