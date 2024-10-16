#!/bin/bash

TARGET="192.168.1.6"
INTERVAL=10

while true; do
    echo "Scanning $TARGET..."
    nmap -Pn $TARGET
    sleep $INTERVAL
done
