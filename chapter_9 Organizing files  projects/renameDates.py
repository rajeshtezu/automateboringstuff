#! python3
# renameDates.py - Renames filenames with American MM-DD-YYYY date format
# to European DD-MM-YYYY.

import re, os, shutil

   # Create a regex that matches files with the American date format.
datePattern = re.compile(r"""^(.*?) # all text before the date
    ((0|1)?\d)-                     # one or two digits for the month
    ((0|1|2|3)?\d)-                 # one or two digits for the day
    ((19|20)\d\d)                   # four digits for the year
    (.*?)$                          # all text after the date
   """, re.VERBOSE)

# TODO: Loop over the files in the working director
for amerFilename in os.listdir('.'):
    mo = datePattern.search(amerFilename)
    
    # Skip files withoit a date.
    if mo == None:
        continue
    
    # Get the different parts of the filename.
    beforePart = mo.group(1)
    monthPart = mo.group(2)
    dayPart = mo.group(4)
    yearPart = mo.group(6)
    afterPart = mo.group(8)

    # TODO: Form the European-style filenam
    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    
    # TODO: Get the full, absolute file path
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    
    # TODO: Rename the files.
    print('Renaming "%s" to "%s" ...' % (amerFilename, euroFilename))
    shutil.move(amerFilename, euroFilename)
