import tweepy
import time
from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

def authenticate_twitter_app():
    try:
        auth = tweepy.OAuth1UserHandler(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        api = tweepy.API(auth)
        print("Authentication successful")
        return api
    except Exception as e:
        print(f"Authentication error: {e}")

def upload_media(api, media_path):
    try:
        media = api.media_upload(media_path)
        print(f"Media uploaded successfully: {media.media_id}")
        return media.media_id
    except Exception as e:
        print(f"Media upload error: {e}")
        return None

def post_tweet_with_media(api, message, media_path):
    media_id = upload_media(api, media_path)
    if media_id:
        try:
            api.update_status(status=message, media_ids=[media_id])
            print("Successfully posted tweet with media!")
        except Exception as e:
            print(f"Error: {e}")

api = authenticate_twitter_app()
post_tweet_with_media(api, "이미지 테스트 트윗!", r"C:\Users\gunhu\Desktop\KickboardDetectionProject\images\1.jpg")

