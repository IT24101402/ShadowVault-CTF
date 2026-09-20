# Stage 6 Test Notes

## Build Test

docker build -t shadowvault-stage6 challenges/stage-06-recovery-gateway

The Docker image builds successfully.

## Runtime Test

docker run --rm --name shadowvault-stage6 -p 5006:5000 shadowvault-stage6

The Flask application starts successfully on port 5000 inside the container.

## Gateway Test

curl http://127.0.0.1:5006/

The ShadowVault Access Gateway is displayed.

## Invalid Token Test

curl -i -X POST -d 'token=wrong' http://127.0.0.1:5006/unlock

Expected result: HTTP 403 Access Denied.

## Valid Token Test

curl -i -X POST -d 'token=NV-SV-6204' http://127.0.0.1:5006/unlock

Expected result: the final flag is displayed.

## Expected Final Flag

SHADOW{shadowvault_recovered}

## Reset

Stop the container and recreate it from the Docker image.
