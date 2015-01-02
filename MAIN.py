#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import tweepy, time, sys, csv, random, json

from random import randint
 
from pastebin import post_in_pastebin
from wordpress import post_in_wordpress
from shorten_url import shorten_url

# Twitter convention
CONSUMER_KEY = 'iq8cq3IAWBAfxjZORQ705o6zD'
CONSUMER_SECRET = 'iKNSC7ubwyeIpjmiZFQemXpAif4B7PuKM0kD7J0JjXearXy6n7'
ACCESS_KEY = '2945080696-Dz6Q1BDpHqBwXuvvonexDBaJ7Pa2592oNVH4p5I'
ACCESS_SECRET = '3uND5IeUryleHBnDRwYbdzsrWe4fZiNxxgRSyNYePsmsw'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)
 
# -----
# (1763 total questions in csv)
# Show Number, Air Date, Round, Category, Value, Question, Answer
# -----

def main():
	with open('1.csv', 'rb') as f:
		mycsv = list(csv.reader(f))

		# PICK QUEgSTION
		q = mycsv[ randint(0,1762) ]
		print '-----------\ngot question:\n'

		# CHECK TWEET LENGTH
		tweetsofar = str(q[3])+' FOR '+str(q[4])+': '+str(q[5])+'. '
		tweet = tweetsofar+'http://goo.gl/1x09QO0' # sample link
		print tweet+'\n'
		print 'length of tweet is '+str(len(tweet))

		if ( len(tweet)<140 ):

			# POST IN WORDPRESS
			link = str(post_in_wordpress(q))

			# SHORTEN LINK
			link = json.loads(shorten_url(link))
			link = link['id']
			print 'posted in wordpress. link is '+link
			
			# post status with just the question
			try:
				api.update_status(str(q[3])+' FOR '+str(q[4])+': '+str(q[5])+'. '+link)
				# api.update_status(link)
				print 'status update was successful!\n'
			except:
				print 'status update was not successful. trying again....\n\n'
				main() # do over
		
		else:
			print 'not within word limit. starting again...\n'
			main()

print '\n-----------\nGood morning, Danny\n-----------\n'
main()