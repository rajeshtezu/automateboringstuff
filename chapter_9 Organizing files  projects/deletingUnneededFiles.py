#! python3
#
# A program that walks through a folder tree and searches for exceptionally large files or folders—say, ones that 
# have a file size of more than 100MB (here we will use 1 MB). 
# Print these files with their absolute path to the screen.

import os

def getHugeFiles(folderPath):
    # walk through the folder tree
    for foldername, subfolder, filenames in os.walk(folderPath):
        for filename in filenames:
            path = os.path.join(os.path.abspath('.'), filename)
            filesizeMB = (os.path.getsize(path))/(1024*1024)
            if filesizeMB >= 1:
                print(path)
            #print(filesizeMB)

getHugeFiles('.')                


















