#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, csv, random, selenium
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from random import randint

# argfile = str(sys.argv[1])
 
#enter the corresponding information from your Twitter application:
CONSUMER_KEY 	= ''
CONSUMER_SECRET = ''
ACCESS_KEY 		= ''
ACCESS_SECRET 	= ''
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
# -----
# (1763 total questions in csv)
# Show Number, Air Date, Round, Category, Value, Question, Answer
# -----

def post_in_pastebin(full_q):
	browser = webdriver.Chrome()
	browser.get('http://pastebin.com')

	# populate + send
	browser.find_element_by_xpath('//*[@id="paste_code"]').send_keys(
		"category: "+str(full_q[3])+"\n"+
		"question: "+str(full_q[5])+"\n"+
		"answer: "+str(full_q[6])+"\n\n"+

		"value: "+str(full_q[4])+"\n"+
		"air date: "+str(full_q[1]))

	browser.find_element_by_xpath('//*[@id="myform"]/div[3]/div[4]/div[2]/input').send_keys("Jeopardy!")
	browser.find_element_by_xpath('//*[@id="submit"]').click()

	# return link
	url = browser.find_element_by_xpath('//*[@id="content_left"]/div[1]/div[3]/div[3]/a[2]').get_attribute('href')
	browser.close()

	return url

def main():
	with open('1.csv', 'rb') as f:
		print "opened file"
		mycsv = csv.reader(f)
		mycsv = list(mycsv)
		print "searching...."

		# pick random question
		full_q = mycsv[ randint(0,1763) ]
		print "got question"

		# post all data in pastebin
		link = post_in_pastebin(full_q)
		
		# post status with just the question
		try:
			api.update_status(str(full_q[3])+": "+str(full_q[5])+". (ans @ "+link+")")
			print "status update was successful!\n"
		except:
			print "status update was not successful. trying again....\n\n"
			main() # do over

print "started"
main()