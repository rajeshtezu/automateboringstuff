#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

text = pyperclip.paste()

text = text.split('\n')

for i in range(len(text)):
	text[i] = '* ' + text[i] 

newText = ''

#for i in range(len(text)):
#	newText += text[i] + '\n'

text = '\n'.join(text)

#print(newText)
pyperclip.copy(text)
