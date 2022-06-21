# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:25:05 2022

@author: odigi
"""

import tweepy
import main
import tweettest
import time
from datetime import datetime

while True:
    sp = main.sp()
    song = main.currplay(sp)
    yass = f"{song[0]} - {song[1]}"
    now = datetime.now()
    curr = now.strftime("%H:%M:%S")
    textie = f"I'm listening to {yass}! The time is {curr}"
    tweettest.client.create_tweet(text=textie)
    time.sleep(300)





