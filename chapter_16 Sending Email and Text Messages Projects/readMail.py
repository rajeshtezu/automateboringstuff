#! /usr/bin/python3
# read Gmail inbox

import pyzmail
import imapclient
import pprint

username = 'myMail@gmail.com'
password = 'MyPassword'

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(username, password)

folderList = imapObj.list_folders()

#pprint.pprint(folderList)
imapObj.select_folder('INBOX', readonly=True)













