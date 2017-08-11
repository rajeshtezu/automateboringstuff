#! Python3
#a program that walks through a folder tree and searches for files with a certain file extension (such as .pdf or 
#.jpg). Copy these files from whatever location they are in to a new folder.

import os, shutil

ext = input('Enter the File Extenstion:\n')

def selectiveCopy(folder, ext):
    # Create a new folder
    while True:
        newFoldername = input('Enter new folder name:\n')
        if os.path.isdir(newFoldername):
            print('Folder name already exist. Try again...\n')
            continue
        else:
            os.mkdir(newFoldername)
            break
        
    # Walk through the folder
    for foldername, subfolers, filenames in os.walk(folder):
        # search for the file extension
        for filename in filenames:
            # copy into new folder 
            if filename.endswith('.'+ext):
                #print('copying file: ' + filename + ' to folder' + './'+ foldername + '_new' )
                shutil.copy(filename, newFoldername)
    
selectiveCopy('.', ext)

