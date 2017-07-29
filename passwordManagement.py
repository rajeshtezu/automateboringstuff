#! python3
# pw.py - An insecure password locker program.

import pyperclip, sys

#import pyperclip
#pyperclip.copy('Hello World')
#message=pyperclip.paste()
#print (message)



PASSWORDS = {'email': 'F7minlBDDuvMJuxESSKHFhTxFtjVB6',
             'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
             'luggage': '12345'}

if len(sys.argv) < 2:
	print('Usage: python passwordMangaement.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in PASSWORDS.keys():
	pyperclip.copy(PASSWORDS[account])
	print('password for ' + account + ' is copied to clipboard')

else:
	print('There is no acount named ' + account)




