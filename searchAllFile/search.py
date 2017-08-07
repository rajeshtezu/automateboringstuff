# python3

import re, glob

expr = input('Enter your regular expression:\n')
userRegex = re.compile(expr)

for filename in glob.glob('*.txt'):
    # opennig all files one by one   
    fileObj = open(filename)
    fileText = fileObj.read()
    fileObj.close()
    searchedText = userRegex.findall(fileText)
    if searchedText:
        print('Inside file ' + filename + ': ')
        print(searchedText)
    

