# python3
# Usage: python madLibs.py <sourceFile>

import re, sys

if len(sys.argv) == 2:
    print('Reading file ' + sys.argv[1])
    madFile = open(sys.argv[1])
    madText = madFile.read()
    madFile.close()
else:
    sys.exit('Usage: python madLibs.py <sourceFile>')

posRegex = re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB', re.I)
madList = posRegex.findall(madText)

for item in madList:
    temp = input('Enter ' + item + ':\n')
    madText = posRegex.sub(temp, madText, count=1)

print('Generating new file ' + 'new' + sys.argv[1])
newMadFile = open('new' + sys.argv[1] , 'w')
newMadFile.write(madText)
newMadFile.close()
