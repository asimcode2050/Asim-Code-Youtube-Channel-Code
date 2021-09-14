#!/bin/bash
FILENAME="/etc/passwd"
while IFS=: read -r username password userid groupid comment homedir cmdshell
do
    echo "$username, $userid, $comment $homedir"
done < $FILENAME
