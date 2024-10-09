#!/usr/bin/bash

# exit script if we're not root
if [ "$(id -u)" != "0" ]; then
   echo "this script must be run as root" 1>&2
   exit 1
fi

# copy systemd files
cp systemd/webgen-ext.service /etc/systemd/system/
cp systemd/webgen-int.service /etc/systemd/system/

systemctl daemon-reload

systemctl enable --now webgen-ext
systemctl enable --now webgen-int