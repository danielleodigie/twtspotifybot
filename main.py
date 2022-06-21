# -*- coding: utf-8 -*-
"""
Created on Mon Jun 20 10:26:28 2022

@author: odigi
"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import cred 

def sp():
    scope = "user-read-currently-playing"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cred.client_id, client_secret= cred.client_secret, redirect_uri=cred.redirect_url, scope=scope))
    return sp

def currplay(sp):
    results = sp.current_user_playing_track()
    content = results.get('item')
    name = content['artists'][0]['name']
    song = content['name']
    return name, song



