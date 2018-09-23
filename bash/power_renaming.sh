#!/bin/bash

#cd ~/Pictures/.2/Fofas
DATE=$(date +%F)

read -p "Please enter a file extension: " EXTENSION
read -p "Please enter a file prefix or press ENTER for the current date as the prefix: " PREFIX

if [ -z $PREFIX ]
then
    PREFIX=$DATE
fi

for FILE in *.$EXTENSION
do
    #mv $FILE ${PREFIX}-$FILE
    echo "Renaming $FILE to ${PREFIX}-$FILE"
done
