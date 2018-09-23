#!/bin/bash

while true
do
    read -p "1. Disk Usage
2. Uptime
3. Users
Make a wish (or enter q to quit)! " Choice

    case $Choice in
        1)
            df ;;
        2)
            uptime ;;
        3)
            who ;;
        q)
            break ;;
        *)
            echo Invalid Option ;;
    esac
    echo
done
echo Goodbye!
