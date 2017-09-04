#! python3
# textMyself.py - Defines the textmyself() function that texts a message
# passed to it as a string.
# Preset values:
from twilio.rest import Client


accountSID = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
authToken = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
myNumber = '+15559998888'
twilioNumber = '+15552225678'


def textmyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)


if __name__ == '__main__':
	textmyself('The boring task is finished.')
