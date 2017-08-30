#! /usr/bin/python
# Sending mail from Gmail account.

import smtplib, sys

smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
isConnected = smtpObj.ehlo()

# Check connection establishment
if isConnected[0] == 250:
    isServerReady = smtpObj.starttls()
    
    # Check if server is ready
    if isServerReady[0] == 220:
        yourMail = input('Enter your gmail username: ')
        yourPass = input('Enter your gmail password: ')
        
        # Login to your account
        try:
            smtpObj.login(yourMail, yourPass)
            recipientMail = input('To: ')
            subject = input('Subject: ')
            subject = 'Subject: ' + subject
            body = input('Mail Text: ')
            body = subject + '\n' + body
            
            # Send mail
            success = smtpObj.sendmail(yourMail, recipientMail, body)
            
            if success == {}:
                print('Mail sent successfully to ' + recipientMail)
                
            # Logout from your account
            logout = smtpObj.quit()
            if logout[0] == 221:
                print('Logged out from your account ' + yourMail)
                
        except smtplib.SMTPAuthenticationError:
            print('Check your username and password.')
    
    else:
        sys.exit('Server is not ready.')

else:
    sys.exit('Could not connect to smtp server.')

    

