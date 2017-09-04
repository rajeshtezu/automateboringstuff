#! /usr/bin/python3
# read Gmail inbox
import pyzmail
import imapclient
import pprint, getpass, sys

#imaplib._MAXLINE = 10000000

if len(sys.argv) < 2:
    sys.exit('Usage: python3 readMail.py <Your Email Username>')

username = sys.argv[1]
password = getpass.getpass(prompt='Password: ', stream=None)

imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login(username, password)

folderList = imapObj.list_folders()

#pprint.pprint(folderList)
imapObj.select_folder('INBOX', readonly=True)

UIDs = imapObj.search(['ALL'])
#pprint.pprint(UIDs)
    
rawMessages = imapObj.fetch(UIDs[0], ['BODY[]'])
#pprint.pprint(rawMessages)

message = pyzmail.PyzMessage.factory(rawMessages[7][b'BODY[]'])
pprint.pprint(message.get_subject())
pprint.pprint(message.get_addresses('from'))
pprint.pprint(message.get_addresses('to'))
pprint.pprint(message.get_addresses('cc'))
pprint.pprint(message.get_addresses('bcc'))

bodyText = message.text_part.get_payload().decode(message.text_part.charset)
#pprint.pprint(bodyText)
print(bodyText)

imapObj.logout()








