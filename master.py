# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

# Handling the master user - follow, like, retweet each tweet

from time import sleep
import tweepy, threading
import rsrtime as time

exitFlag = 0 # Flag for thread exit


# Main loop function for handling master thread
def handleMasterLoop(tName,api,master):
    checkIfFollow(master)
    while 1:
        if exitFlag:
            tName.exit()
        likeAndRetweet(api,master)
        sleep(600) # Every 10 mins

# Initial check to see if I follow my master. If not, follow.
def checkIfFollow(master):
    try:
        print(time.getTime() + ' [*MASTER] Let\'s check if i\'m following my master...')
        if not master.following:
            master.follow()
            print(time.getTime() + ' Now I do!') # Should happen' only once...
        else:
            print(time.getTime() + ' I do!')

    except tweepy.TweepError as e:
        print(e.reason) 

# Like and RT last of my master's tweets.
def likeAndRetweet(api,master):
    try:
        tweets = api.user_timeline(id=master.id,count=1)
        last_tweet = tweets[0]
        if(not last_tweet.text.startswith("RT") and not last_tweet.favorited):
            print(time.getTime() + ' [*MASTER] Liking and retweeting master\'s tweet: ' + last_tweet.text)
            last_tweet.favorite()
            last_tweet.retweet()
        else:
            print(time.getTime() + ' [*MASTER] Last of my masters tweets is a retweet. Not handling.')
    except tweepy.TweepError as e:
        print(e.reason)
        