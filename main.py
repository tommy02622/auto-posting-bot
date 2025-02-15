import tweepy
import schedule
import time
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def authenticate_twitter_app():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    return tweepy.API(auth)

def post_tweet(api, message):
    try:
        api.update_status(message)
        print("Successfully posted tweet!")
    except Exception as e:
        print(f"Error: {e}")

def job():
    api = authenticate_twitter_app()
    message = "Hello, this is an automated tweet!"
    post_tweet(api, message)

schedule.every().day.at("10:00").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)