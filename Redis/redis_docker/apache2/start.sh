#!/bin/bash

/usr/sbin/init

systemctl start httpd
systemctl start crond

tail -f /dev/null