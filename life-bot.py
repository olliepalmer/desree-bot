# -*- coding: utf-8 -*-
# open lines_read.csv file and count number-of-lines
# open lines_alphabetised file and get number-of-lines + 1
# tweet the line, append to lines_read file with time and link to tweet

import tweepy
import os
from datetime import datetime
import random

# this authentication method is described [here](https://slackapi.github.io/python-slackclient/auth.html)
# basically, when the command is run, instead of running:
# $ python bot.py
# we run:
# $ consumer_key="YOUR_KEY_HERE" consumer_secret="YOUR_SECRET_HERE" access_token="YOUR_ACCESS_TOKEN_HERE" access_token_secret="YOUR_ACCESS_TOKEN_SECRET_HERE" python bot.py
# this passes these variables into the python script
consumer_key = os.environ["consumer_key"]
consumer_secret = os.environ["consumer_secret"]
access_token = os.environ["access_token"]
access_token_secret = os.environ["access_token_secret"]

# print (auth_token, auth_secret)
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

try:
	api.update_status(random.choice(list(open('life.txt'))))
except tweepy.error.TweepError:
	pass