#! python3
# 
# A program that finds all files with a given prefix, such as spam001.txt, spam002.txt, and so on, in a single 
# folder and locates any gaps in the numbering (such as if there is a spam001.txt and spam003.txt but no 
# spam002.txt). Have the program rename all the later files to close this gap.

import os, shutil


# walk through the filenames (os.walk())
# check prefix and suffix, prefix should be common and suffix should be number(use regex to check suffix)
# if suffix is not in order then rename afterwards files with consecutive numbers.




#def fillingGap(folderPath, prefix):
#    # fetch filenames into a list
#    filenames = os.listdir(folderPath)
#    prefixedFiles = []
#    
#    for filename in filenames:
#        if filename.startswith(prefix):
#            prefixedFiles.append(filename)
#    
#    prefixedFiles.sort()
#    
#    
#    
#    print(prefixedFiles)
#    
#    
#    
#fillingGap('.', 'spam')    

