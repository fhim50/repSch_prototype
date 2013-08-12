import os
import twitter


from twitter.oauth import write_token_file, read_token_file
from twitter.oauth_dance import oauth_dance


def login():

	APP_NAME = ''
	CONSUMER_KEY = ''
	CONSUMER_SECRET = ''
	TOKEN_FILE = 'auth/twitter.oauth'

	try:
		(oauth_token, oauth_token_secret) = read_token_file('auth/twitter.oauth')

	except IOError, e :
		(oauth_token, oauth_token_secret) = oauth_dance(APP_NAME, CONSUMER_KEY, CONSUMER_SECRET)

		if not os.path.isdir('auth'):
			os.mkdir('auth')

		write_token_file(TOKEN_FILE, oauth_token, oauth_token_secret)

	return twitter.Twitter(domain='api.twitter.com', api_version='1.1', auth = twitter.oauth.OAuth(oauth_token, 
							oauth_token_secret, CONSUMER_KEY, CONSUMER_SECRET))


