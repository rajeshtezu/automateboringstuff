#! /usr/bin/python3
# A program that takes an email address and string of text on the command line and then, using Selenium, 
# logs into your email account and sends an email of the string to the provided address.

# Usage: python commandLineEmailer.py <userGmail> <password> <recipientEmail> <subject> <mailText>


from selenium import webdriver
import sys, time


if len(sys.argv) < 6:
	sys.exit('Usage: python commandLineEmailer.py <userGmail> <password> <recipientEmail> <subject> <mailText>')


browser = webdriver.Firefox()
browser.get('https://accounts.google.com/')

emailElem = browser.find_element_by_id('identifierId')
emailElem.send_keys(sys.argv[1])
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()
time.sleep(3)

passwordElem = browser.find_element_by_name('password')
passwordElem.send_keys(sys.argv[2])
nextButton = browser.find_element_by_class_name('CwaK9')
nextButton.click()
time.sleep(5)

mail = browser.find_element_by_class_name('WaidBe')
mail.click()
time.sleep(5)

# compose email
compose = browser.find_element_by_id(':4j')
compose.click()
time.sleep(2)

recipient = browser.find_element_by_name('to')
recipient.send_keys(sys.argv[3])

subjectBox = browser.find_element_by_name('subjectbox')
subjectBox.send_keys(sys.argv[4])

mailText = browser.find_element_by_id(':ai')
mailText.send_keys(sys.argv[5])

send = browser.find_element_by_id(':92')
send.click()

