import re

def myStrip(myString, stripChar=' '):
    #stripChar = stripChar.encode('unicode_escape')
    stripRegex = re.compile(stripChar)
    stripString = stripRegex.sub('',myString)
    return stripString
    
myString = '  this is   '

newString = myStrip(myString,'i')

print(newString)