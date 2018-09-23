#!/usr/bin/env Python3

import webbrowser, pyperclip, sys

sys.argv

# check if command line arguments were passed
if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])

else:
    address = pyperclip.paste()

#https://www.google.com.br/maps/place/<ADDRESS>
webbrowser.open("https://www.google.com.br/maps/place/" + address)
