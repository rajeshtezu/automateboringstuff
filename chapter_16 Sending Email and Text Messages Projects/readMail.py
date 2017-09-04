#! /usr/bin/python3
# read Gmail inbox
import pyzmail
import imapclient
import pprint

#imaplib._MAXLINE = 10000000

username = 'myEmail@gmail.com'
password = 'myPassword'

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








