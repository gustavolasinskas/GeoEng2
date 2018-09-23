#!/bin/bash

# this piece of code adds the current date to the following jpg files in the designed directory.
#cd ~/Pictures/.2/Ffs

cd ~/empty

#nullglob is some sort of pattern matching whatever and I have no idea what is shopt
#anyway, this weird command is used in case there are no matchings in the Wildcards

shopt -s nullglob

Date=$(date +"%d.%m.%y")

for File in *.jpg
do
    cp "$File" "$Date-$File"
done
