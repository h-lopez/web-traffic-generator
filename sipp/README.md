# sip-generator

## About

these are the file(s) necessary for sip traffic generation. this leverages sipp to make calls.

defaults are to make 5 calls at once, lasting 60 seconds each. after 60 seconds, hang up and dial again.

- call duration can be adjusted by editing `uac.xml`
- number of calls can be adjusted by editing the systemd service file (rememeber to run `systemctl daemon-reload`)

## Dependencies
- sipp

sipp must be installed via package manager or manually
if manually, make sure the executable is installed to `/usr/bin/sipp`

## Usage
1. install sipp via package manager or manually
1. create the directory `/opt/sipp`
1. copy the `file.wav` and `uac.xml` files to the directory
1. from the the `systemd` directory, copy `sipp-server.service` or `sipp-client.service` to `/etc/systemd/system` (determinant if install is client or server)
1. reload systmed (`sudo systemctl daemon-reload`)
1. enable/start the service (`sudo systemctl enable --now sipp-client`)
