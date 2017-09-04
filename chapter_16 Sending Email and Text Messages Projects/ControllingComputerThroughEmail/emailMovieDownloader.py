#! /usr/bin/python3
# Usage: python emailMovieDownloader.py

import pyzmail, imapclient, pprint
import subprocess, time
import smtplib

downloadPassword = 'Password'

username = 'myMail@gmail.com'
password = 'myPassword'


def downloadMovie():
	while True:
		print('Logging into account...')
		imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)		
		imapObj.login(username, password)
		
		print('Reading mail...')
		imapObj.select_folder('INBOX', readonly=False)
		
		UIDs = imapObj.search(['ALL'])
		
		if len(UIDs) > 0:
			rawMessages = imapObj.fetch(UIDs, ['BODY[]'])
			#pprint.pprint(rawMessages)
			
			for v in rawMessages.values():
				message  = pyzmail.PyzMessage.factory(v[b'BODY[]'])
				subject  = message.get_subject()
				fromAddr = message.get_addresses('from')
			
						
			bitTorrentLink = message.text_part.get_payload().decode(message.text_part.charset)
						
			# Creating smtp connection
			smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
			smtpObj.ehlo()
			smtpObj.starttls()

			if downloadPassword == subject:
				print('Starting movie downloading...')
				torrentProcess = subprocess.Popen(['/usr/bin/qbittorrent', bitTorrentLink])
				imapObj.delete_messages(UIDs)
				torrentProcess.wait()

				# Sending a success mail
				print("Movie downloaded successfully.")
				smtpObj.login(username, password)
				mailText = 'Subject: Movie downloaded successfully.\nYour movie has been successfully downloaded.'				
				smtpObj.sendmail(username, fromAddr[0][1], mailText)
				smtpObj.quit()
				
			else:
				print("Password didn't match.\nSending mail back to sender for incorrect password.")
				smtpObj.login(username, password)
				mailText = 'Subject: Incorrect password.\nPlease send correct password in subject'
				smtpObj.sendmail(username, fromAddr[0][1], mailText)
				imapObj.delete_messages(UIDs)
				smtpObj.quit()

		
		else:
			print('No email found.')
		
		imapObj.logout()
		
	
		# sleep for 10 minutes
		for i in range(10):
			time.sleep(60)
		
		

if __name__ == '__main__':
	downloadMovie()


