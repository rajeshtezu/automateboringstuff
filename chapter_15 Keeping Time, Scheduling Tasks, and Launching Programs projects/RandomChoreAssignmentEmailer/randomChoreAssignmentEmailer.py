#! /usr/bin/python3
# change the persons email and myEmail, myPassword to work with this code.

import smtplib, random

chores = ['dishes', 'bathroom', 'vacuum', 'walk dog']

persons = {
	'scott' : {
		'email' : 'scott@example.com',
		'lastChore' : 'dishes'
	},

	'john' : {
		'email' : 'john@example.com',
		'lastChore' : 'bathroom'
	},
	'kate' : {
		'email' : 'kate@example.com',
		'lastChore' : 'vacuum'
	},
	'juli' : {
		'email' : 'juli@example.com',
		'lastChore' : 'walk dog'
	}
}


smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

myEmail = 'my_email_address@gmail.com'
myPassword = 'MY_SECRET_PASSWORD'

smtpObj.login(myEmail, myPassword)

print('Assigning chores to persons...')
for k, v in persons.items():
	randomChore = random.choice(chores)

	# avoid assigning anyone the same chore they did last time.
	while randomChore == v['lastChore']:
		randomChore = random.choice(chores)

	mailText = 'Subject: Chore assigned for the week.\nDear '+ k + ', \nChore assigned to you for this week is ' + randomChore
	chores.remove(randomChore)

	# Send the mail
	status = smtpObj.sendmail(myEmail, v['email'], mailText)
	if status == {}:
		print('mail sent to ' + v['email'] + ' with chore ' + randomChore)

print('Chore assigned successfully.')
# Logout
smtpObj.quit()













