#!/usr/bin/bash

# exit script if we're not root
if [ "$(id -u)" != "0" ]; then
   echo "this script must be run as root" 1>&2
   exit 1
fi

# script expects to tool to be installed to /opt/web-traffic-generator/

# copy systemd files
cp /opt/web-traffic-generator/systemd/webgen-ext.service /etc/systemd/system/
cp /opt/web-traffic-generator/systemd/webgen-int.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable --now webgen-ext
systemctl enable --now webgen-int