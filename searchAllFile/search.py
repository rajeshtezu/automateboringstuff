# python3
# 
# A program that opens all .txt files in a folder and searches for any line that matches a user-supplied 
# regular expression. The results should be printed to the screen.

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
    

