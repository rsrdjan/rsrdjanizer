# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

# Handling quotes, inside the thread

import tweepy, threading, sys, random
from time import sleep
import rsrtime as time

exitFlag = 0 # Flag for thread exit

# Main loop for handling and randomly chosing quotes in thread. Once quotes file is exhausted, thread stops.
def handleQuotesLoop(tName,api):
    while True:
        try:
            quotes_file = open('quotes.txt','r')
            quotes = quotes_file.readlines()
            quoteToSend = quotes[random.randrange(0,len(quotes))]
            quotes_file.close()
        except FileExistsError as e:
            print(time.getTime() + ' [*QUOTES] No quotes file!')
            sys.exit()

        try:
            if quoteToSend != '\n':
                print(time.getTime() + ' [*QUOTES] Tweeting quote: ' + quoteToSend)
                api.update_status(quoteToSend)
        except tweepy.TweepError as e:
            print(time.getTime() + ' [*QUOTES] Cannot tweet: ' + e.reason)
        sleep(7200) # 2 hours
        