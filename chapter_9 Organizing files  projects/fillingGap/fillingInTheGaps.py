#! python3
# 
# A program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single 
# folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no 
# spam002.txt). Have the program rename all the later files to close this gap.
# 
# Usage: python fillingInTheGaps <filePrefix>

import os, shutil, sys

def fillingGap(folderPath, prefix):
    # fetch filenames into a list
    filenames = os.listdir(folderPath)
    prefixedFiles = []
    
    for filename in filenames:
        if filename.startswith(prefix):
            prefixedFiles.append(filename)
    
    prefixedFiles.sort()
    
    gapCounter = 0
    # Find if any gap, then rename
    prevNum = (prefixedFiles[0].split('.')[0])[len(prefix):]
    for i in range(1, len(prefixedFiles)):   
        nextNum = (prefixedFiles[i].split('.')[0])[len(prefix):]
        
        if int(nextNum) - int(prevNum) == 1:
            prevNum = nextNum
            continue
        else:
            gapCounter += 1
            print('Renaming files with gap...')
            # Rename remaining files and exit from the loop
            for j, remainingFile in  enumerate(prefixedFiles[int(prevNum)-1:len(prefixedFiles)-1]):
                #print(str(j) + ': ' +remainingFile)
                newName = prefix + str(int(prevNum) + j + 1) + '.' + remainingFile.split('.')[1]
                #print(newName)
                #print(prefixedFiles[int(prevNum) + j])
                shutil.move(prefixedFiles[int(prevNum) + j], newName)
            break
        
    if gapCounter == 0:
        print('No gap found.')
    

if len(sys.argv) != 2:
    sys.exit('Usage: python fillingInTheGaps <filePrefix>')
else:
    fillingGap('.', sys.argv[1])    

