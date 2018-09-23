#!/bin/bash

# this piece of code renames file extension from .png files to .jpg in the folloeing directory.

#cd ~/Pictures/.2/Ffs

for file in *.png
do
  #mv $file "${file%.png}.jpg"
  echo $file
done
