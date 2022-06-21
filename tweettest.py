# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 11:48:50 2022

@author: odigi
"""

import tweepy
import twtcred


oauth1_user_handler = tweepy.OAuth1UserHandler(
    twtcred.apikey, twtcred.secret,
    callback="oob"
)

print(oauth1_user_handler.get_authorization_url())

verifier = input("Input PIN: ")

token = oauth1_user_handler.get_access_token(
    verifier
)

client = tweepy.Client(
    consumer_key=twtcred.apikey,
    consumer_secret=twtcred.secret,
    access_token=token[0],
    access_token_secret=token[1]
)








