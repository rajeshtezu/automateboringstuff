#! python3

import re
print('Please set a new password: ')

def strongpassword():
    while True:
        password = input()        
        if lowcase.search(password) == None:
            print('The entered password doesn\'t have a lower case character')
            continue        
        if upcase.search(password) == None:
            print('The entered password doesn\'t have an upper case character')
            continue        
        if digit.search(password) == None:
            print('The entered password doesn\'t have a digit')
            continue        
        if space_8.search(password) == None:
            print('The entered password should have atleast 8 characters and no space in between')
            continue
        else:
            print('New Password is Valid and Saved')
            break


lowcase = re.compile(r'[a-z]')              # this regex searches for atleast one lower case alphabet
upcase = re.compile(r'[A-Z]')               # this regex searches for atleast one upper case alphabet
digit = re.compile(r'(\d)')                 # this regex searches for atleast one digit
space_8 = re.compile(r'^[a-zA-Z0-9]{8,}$')  # this regex searches for expressions without any space and atleast 8 characters 

strongpassword()