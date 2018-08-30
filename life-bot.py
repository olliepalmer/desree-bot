# -*- coding: utf-8 -*-
# open lines_read.csv file and count number-of-lines
# open lines_alphabetised file and get number-of-lines + 1
# tweet the line, append to lines_read file with time and link to tweet

import tweepy
import os
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

life = ["Life, oh life, oh life, oh life","Doo, doo doot dooo","Life, oh life, oh life, oh life","Doo, doot dooo","I'm afraid of the dark ","Especially when I'm in a park ","And there's no-one else around","Oh, I get the shivers ","I don't want to see a ghost","It's a sight that I fear most ","I'd rather have a piece of toast ","And watch the evening news","Life, oh life, ooh liiife, oooh life","Doo, doot doot dooo. ","Life, oh life, oh life, oh life","Doo, doo do","I'm a superstitious girl","I'm the worst in the world ","Never walk under ladders ","I keep a rabbit's tail","I'll take you up on a dare","Anytime, anywhere ","Name the place, I'll be there ","Bungee jumping, I don't care!","Life, oh life, oh li-ife, oh life","Doo, doot doot doooo","Life, oh life, oh liiii-fe, oh li-ife","Doo, doo dooo","Life, doo, doot dooo ","Doo, doo do","So after all is said and done ","I know I'm not the only one ","Life indeed can be fun, if you really want to","Sometimes living out your dreams ","Ain't as easy as it seems ","You want to fly around the world","In a beautiful balloon","Life, oh life, oh life, oh life","Doo, doot doot dooo","Life, oh life, oh life, oh life","Doo, doo dooo","[instrumental]","[key change]"]

done = 0

while done < 1:
	status = random.choice(list(life))

	try:
		# api.update_status(random.choice(list(open('life.txt')))) # uncomment this if you want to load a text file
		api.update_status(status)
		print("tweeted:",status)
		done = 1
	except tweepy.error.TweepError as e:
		print("Error!")
		print (e.api_code)
		pass