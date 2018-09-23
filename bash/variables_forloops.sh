#!/bin/bash

VAR="Shell scripting is fun!"
echo $VAR
VARIABLE=$HOSTNAME
echo "This script is running on ${VARIABLE}."

LIST="man bear pig dog cat sheep"
for Species in $LIST
do
  echo "$Species"
done
