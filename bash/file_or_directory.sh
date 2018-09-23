#!/bin/bash

if [ "$#" -eq "0" ]
then
  echo "No arguments passed yet."
  read -p "Enter the path to a file or a directory: " FILES

else
  echo "File(s) or Directory(ies) passed are" $*
  FILES=$*
fi

for FILE in $FILES
do
  if [ -f "$FILE" ]
  then
    echo "$FILE is a regular file."
  elif [ -d "$FILE" ]
  then
    echo "$FILE is a directory."
  else
    echo "$FILE is something other than a regular file or directory."
  fi

  ls -l $FILE
done
