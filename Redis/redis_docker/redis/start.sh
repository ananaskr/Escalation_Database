#!/bin/bash

service ssh start

redis-server /etc/redis/redis.conf


tail -f /dev/null
