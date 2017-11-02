# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

# Handling feeds, parsing and tweeting (Currently only announcing infosec conferences)

from time import sleep
import tweepy, threading, feedparser, sys
import rsrtime as time

def handleFeedsLoop(tName,api,master):
    while 1:
        try:
            feeds_file = open('feedurls.txt','r')
            feeds = feeds_file.readlines()
            feeds_file.close()
        except FileExistsError as e:
            print(time.getTime() + ' [*FEEDS] No feeds file!')
            sys.exit()
        for feed in feeds:
            if feed != '\n':
                f = feedparser.parse(feed)
#                print(f.feed.title)
#                print(f.feed.subtitle)
                tweet = f['entries'][0]['title'] + ' ' + f['entries'][0]['link']
#                print(tweet)
                try:
                    last_tweet = api.user_timeline(count=1)[0]
                    tweet_title = f['entries'][0]['title']
                    if tweet_title not in last_tweet.text:
                        api.update_status(tweet)
                    else:
                        print(time.getTime() + ' [*FEEDS] Already tweeted that. Skipping...')
                except tweepy.TweepError as e:
                    print(e.reason)
        sleep(1800) # 1/2 hour refresh interval

