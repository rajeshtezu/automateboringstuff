#! /usr/bin/python3
# mapIt.py - Launches a map in the browser using an address from the
# command line or clipboard.


import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])	# since we are getting address as a list of string, we need to join them as whole string

else:
	# Get address form clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)
