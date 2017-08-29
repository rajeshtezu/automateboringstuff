 #! python3
 # countdown.py - A simple countdown script.

import time, subprocess, sys

if len(sys.argv) < 2:
	sys.exit('Usage: python3 countdown.py <time in second>')

timeLeft = int(sys.argv[1])

while timeLeft > 0:
	print('Time Left : ' + str(timeLeft) + ' second')
	time.sleep(1)
	timeLeft -= 1

subprocess.Popen(['see', 'alarm.wav'])	







