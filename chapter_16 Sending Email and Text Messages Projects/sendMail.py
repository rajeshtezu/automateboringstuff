#! /usr/bin/python
# Sending mail from Gmail account.

import smtplib, sys, getpass, re

def main():
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    isConnected = smtpObj.ehlo()
    
    # Check connection establishment
    if isConnected[0] == 250:
        isServerReady = smtpObj.starttls()
    
        # Check if server is ready
        if isServerReady[0] == 220:
            yourMail = input('Enter your gmail username: ')
            while not validateEmail(yourMail):
                print('Incorrect mail.')
                yourMail = input('Pleae enter valid gmail address: ')
            yourPass = getpass.getpass(prompt='Password: ', stream=None)
    
            # Login to your account
            try:
                smtpObj.login(yourMail, yourPass)
                recipientMail = input('To: ')
                while not validateEmail(recipientMail):
                    print('Incorrect address.')
                    recipientMail = input('Enter valid address: ')
                
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


    
    
def validateEmail(mail):
    emailRegex = re.compile(r'''(
     [a-zA-Z0-9._%+-]+      # username
     @                      # @ symbol
     [a-zA-Z0-9.-]+         # domain name
     (\.[a-zA-Z]{2,4})      # dot-something
     )''', re.VERBOSE)
    
    if emailRegex.search(mail):
        return True
    else:
        return False

    
if __name__ == '__main__':
    main()
