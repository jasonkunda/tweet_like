import tweepy
api_key = ""
api_key_secret = ""
access_token = ""
access_token_secret = ""
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
