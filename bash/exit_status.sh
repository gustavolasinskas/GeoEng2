#!/bin/bash

File=$1

if [ -f $1 ]
then
  echo "$1 is a regular file"
  exit 0
elif [ -d "$1" ]
then
  echo "$File is a directory."
  exit 1
else
  echo "$File is something other than a regular file or directory."
  exit 2
fi
