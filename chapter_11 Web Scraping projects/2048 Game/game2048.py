#! /usr/bin/python3

'''
Online 2048 player
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get('https://gabrielecirulli.github.io/2048/')

htmlElem = browser.find_element_by_tag_name('html')

time.sleep(2)

noticeButton = browser.find_element_by_class_name('notice-close-button')
noticeButton.click()
time.sleep(2)

newGame = browser.find_element_by_class_name('restart-button')
newGame.click()
time.sleep(1)

while True:
	htmlElem.send_keys(Keys.UP)
	time.sleep(0.5)
	htmlElem.send_keys(Keys.RIGHT)
	time.sleep(0.5)
	htmlElem.send_keys(Keys.DOWN)
	time.sleep(0.5)
	htmlElem.send_keys(Keys.LEFT)
	time.sleep(0.5)



