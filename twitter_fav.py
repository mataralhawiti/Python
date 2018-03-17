#!/usr/bin/python
# encoding: utf-8

import tweepy 
import json
import csv
import sys
'''
Pull my favaorit tweets into Google spreadsheets

goals :
	- learn how to use Twitter API
	- Learn how to use Google Drive API
	- Undersatning how auth works
'''


# Twitter API credentials
consumer_key = 'dqFXbqLXD6Rm7fzoYh6Ra3Zos'
consumer_secret = 'yJv27ak1nXck4pXIMZkBe0fVa8x800426PeciLXEWOtrG9wAXX'
access_token = '957474764-WRlLbe6j0h93JA6jfZ5d1cPPeEdSEqvNQzUoOwtI'
access_token_secret = 'sR9b576wXlmh7wgUR3oUvfApsz7aegdDwG9KHVpt60py1'

def get_twitts(usr):
	# authorize twitter, initalize tweepy
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_token, access_token_secret)
	api = tweepy.API(auth)

	user = api.get_user(usr)

	di = {
		"name :" : user.name,
		"favourites_count :": user.favourites_count,
		"Do you follow?": user.following,
		"followers :": user.followers_count,
	}

	return di

if __name__ == '__main__' :
	tw = get_twitts(sys.argv[1])
	for k,v in tw.items():
		print(k,v)

	with open('/home/matar/fir.json', 'w') as f:
		#f.write(str(tw))
		json.dump(tw, f, sort_keys=True, indent=4, ensure_ascii=False)
#'w2me'
# print(user.screen_name)
# print(user.followers_count)
# for friend in user.friends():
#    print(friend.screen_name)

# user.screen_name >>>> variable
# user.followers_count >>>> variable
# user.friends() >>> method in User medole 