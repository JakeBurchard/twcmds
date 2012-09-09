#!/usr/bin/env python
import tweepy
import webbrowser
from read_config import ConfigInfo


class TwitConn:
    def __init__(self, consumer_key, consumer_secret):
        self.key = consumer_key
        self.secret = consumer_secret
    def start_api(self):
		auth = tweepy.OAuthHandler(self.key, self.secret)
		config = ConfigInfo('config.ini')
		if not config.has_settings('Settings'):
			auth_url = auth.get_authorization_url()
			webbrowser.open(auth_url)
			print 'Please authorize: ' + auth_url
			verifier = raw_input('PIN: ').strip()
			auth.get_access_token(verifier)
			self.token_key, self.token_secret = auth.access_token.key, auth.access_token.secret
			config.add_settings('Settings')
			config.set_settings('Settings', 'token_key', self.token_key)
			config.set_settings('Settings', 'token_secret', self.token_secret)
		else:
			self.token_key = config.settings[0][1]
			self.token_secret = config.settings[1][1]
			
		auth.set_access_token(self.token_key, self.token_secret)
		self.api = tweepy.API(auth)
			

