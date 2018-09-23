#!/bin/bash

function file_count() {
  # This function only works for the first argument passed in the command line.
  local DIR=$1
  local NUMBER_OF_FILES=$(ls $DIR | wc -l)
  echo ${DIR}:
  echo $NUMBER_OF_FILES
}

file_count $1
