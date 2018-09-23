'''     THIS FILE SELECTS AUTHOR'S NAMES AND WEBSITES FROM A CLIPBOARD COPIED TEXT TO THE CLIPBOARD, SO YOU CAN JUST
        PASTE IT IN ANY TEXT EDITOR

    To run this document enter the automate environment on terminal by typing "source activate automate"
    Later on enter the following order: python3 ./file_name.py
    Pyperclip works with cmnd+c and pastes to the clipboard
'''

import re, pyperclip



# add REGEX of any kind, for example:

sites = re.compile(r'''
Available\sat:\s
http://.*\s        # website
Access:\s
(\d\d/\d\d/\d\d\d\d) # access date
''', re.VERBOSE)

books = re.compile(r'''
\d\d?\.\s     # number
\w+,\s\w     # name, n
''', re.VERBOSE)


text = pyperclip.paste()

# extract results

extractedBooks = books.findall(text)
extractedSites = sites.findall(text)

results = '\n'.join(extractedBooks) + '\n'*4 + '\n'.join(extractedSites)

pyperclip.copy(results)
