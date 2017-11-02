# rsrdjanizer v0.1
# Simple twitter bot
# Copyright (C) 2017 Srdjan Rajcevic srdjan[@]rajcevic.net

# Vars for holding values needed by the Twitter API - you need to create app first!
# Please chmod rsrdjanizer.db (go-rwx)
import sqlite3, sys

def dbGetCreds():
    try:
        conn = sqlite3.connect('rsrdjanizer.db')
        c = conn.cursor()
        for row in c.execute('SELECT * FROM creds'):
            creds = {'consumer_key':row[1],
                     'consumer_secret':row[2],
                     'access_token_key':row[3],
                     'access_token_secret':row[4],
                     'master_user':row[5]}
        conn.close()
    except sqlite3.DatabaseError as e:
        print(e.reason)
        sys.exit()
    return creds    