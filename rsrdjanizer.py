# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net. Using Tweepy library.

# Starting point for rsrdjanizer roBOT 
# If you want to run in daemon mode, try with 'nohup python rsrdjanizer.py &'

import tweepy, threading
from creds import *
import quotes as q
import master as m
import dm as dm
import feeds as fd
import rsrtime as time

# Thread classes. Each class define the functionality of one module (DMs, quotes, master handling, etc.)

class masterThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print(time.getTime() + ' Starting ' + self.name + ' thread...')
        m.handleMasterLoop(self.name,api,master)
        print(time.getTime() + ' Exiting ' + self.name + ' thread...')

class quotesThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print(time.getTime() + ' Starting ' + self.name + ' thread...')
        q.handleQuotesLoop(self.name,api)
        print(time.getTime() + ' Exiting ' + self.name + ' thread...')

class dmThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print(time.getTime() + ' Starting ' + self.name + ' thread...')
        dm.handleDMLoop(self.name,api,master)
        print(time.getTime() + ' Exiting ' + self.name + ' thread...')

class feedThread(threading.Thread):
    def __init__(self,threadID,name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
    def run(self):
        print(time.getTime() + ' Starting ' + self.name + ' thread...')
        fd.handleFeedsLoop(self.name,api,master)
        print(time.getTime() + ' Exiting ' + self.name + ' thread...')

# Authenticate to Twitter API

creds = dbGetCreds()
auth = tweepy.OAuthHandler(creds['consumer_key'], creds['consumer_secret'])
auth.set_access_token(creds['access_token_key'], creds['access_token_secret'])
api = tweepy.API(auth)

# Basic info about the bot when starting up...

profile = api.me()
print('Starting rsrdjanizer... Time: ' + time.getTime())
print ('\nHandle: @' + profile.screen_name + ' | Name: ' + profile.name)
print ('ID: ' + str(profile.id))
print ('Description: ' + profile.description)
print ('I have ' + str(profile.followers_count) + ' followers, and ' + str(profile.friends_count) + ' people are following me.\n')

master = api.get_user(creds['master_user'])

# Creating threads

thread1 = masterThread(1,"master")
thread2 = quotesThread(2, "quotes")
thread3 = dmThread(3, "dm")
thread4 = feedThread(4, "feeds")

# ... and run them.

thread1.start()
thread2.start()
thread3.start()
thread4.start()
thread1.join()
thread2.join()
thread3.join()
thread4.join()


print('Exiting...')