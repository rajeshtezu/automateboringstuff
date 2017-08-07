#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe/python multiclipboard.py save <keyword> - Saves clipboard to keyword.
#        py.exe/python multiclipboard.py <keyword> - Loads keyword to clipboard.
#        py.exe/python multiclipboard.py delete <keyword> - delete keyword from shelfFile
#        py.exe/python multiclipboard.py delete - delete all keyword from shelfFile
#        py.exe/python multiclipboard.py list - Loads all keywords to clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# TODO: Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
    del mcbShelf[sys.argv[2]]
    #mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # TODO: List keywords and load content.
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
        
mcbShelf.close()
