#! /usr/bin/python3
# read Gmail inbox

import pyzmail
import imapclient
import pprint

username = 'pypypy137@gmail.com'
password = 'Nav@ratna90'

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(username, password)

folderList = imapObj.list_folders()

#pprint.pprint(folderList)
imapObj.select_folder('INBOX', readonly=True)













