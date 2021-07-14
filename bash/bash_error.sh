#!/bin/bash
cat somefile.txt
if [ $? -eq 0 ]
then
    echo "somefile.txt exists!"
    exit 0
else
    echo "somefile.txt does not exists!" >&2
    exit 11
fi
