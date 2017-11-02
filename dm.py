# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

# Handling direct messages for the bot - responds to commands issued by the master

from time import sleep
import tweepy, threading, eliza
import rsrtime as time

exitFlag = 0 # Flag for thread exit
responded = False # Flag for responded
therapist = eliza.eliza()

def handleDMLoop(tName,api,master):    
    last_msg = getLastMsg(api)
    while 1:
        try:
            if last_msg.text != getLastMsg(api).text:        
                recipient = last_msg.sender.screen_name
#            last_sent_message = api.sent_direct_messages()[0] # Last sent message
#            if last_msg.text not in last_sent_message.text:
                reply = therapist.respond(last_msg.text)
#                message_text = 'My AI is not that perfect, still.\nHey, did you say ' + last_msg.text + '?'
                sent = api.send_direct_message(user=recipient,text=reply)
                print(time.getTime() + ' [*DM] Sending to ' + recipient + ': ' + reply)
                last_msg = getLastMsg(api)
            else:
                pass
        except tweepy.TweepError as e:
            print(e.reason)
        sleep(60)

def getLastMsg(api):
    messages = api.direct_messages()
    message = messages[0] # Last received message
    return message