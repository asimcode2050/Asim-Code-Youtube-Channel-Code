#!/bin/bash
echo "$(date) : $@" >> timefile.txt
tail -n 1 timefile.txt
