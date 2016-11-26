#!/usr/bin/python
# -*- coding: utf-8 -*- 
#pops an item from a list and tweets it

import twitter
import sys
import pickle

secrets_file = open("secrets.conf", "rb")
secrets = pickle.load(secrets_file)
secrets_file.close()

def verify_credentials(api):
	return api.VerifyCredentials() != None

def init_auth():
	api = twitter.Api(
	consumer_key = secrets["consumer_key"], 
	consumer_secret = secrets["consumer_secret"],
	access_token_key = secrets["access_token"], 
	access_token_secret = secrets["access_secret"])
	if verify_credentials(api):
		print('Validated credentials OK')
		return api
	else:
		print('Credentials validation failed')
		sys.exit(1)

api = init_auth()
tweet_file = open("tweetdict.pkl", "rb")
tweet_queue = pickle.load(tweet_file)
tweet_file.close()

count = 0
for tweet in tweet_queue:
	if tweet_queue[tweet] == True:
		count += 1
		continue
	else:
		print "Already tweeted " + str(count) + " tweets. Attempting next..."
		try:
			print("Tweeting: " + tweet)
			status = api.PostUpdate(tweet)
			tweet_queue[tweet] = True
			break
		except:
			print("Could not tweet!")
			sys.exit(2)
		#print("Tweeted %s, tweet #%d" %(status.text, count))

tweet_file = open("tweetdict.pkl", "wb")
pickle.dump(tweet_queue, tweet_file)
tweet_file.close()
