import tweepy
import logging
from credentials import *

logging.basicConfig(format='%(levelname)s [%(asctime)s] %(message)s', datefmt='%m/%d/%Y %r', level=logging.INFO)
logger = logging.getLogger()

search_keywords = "%23Ayato"

delay = 100

result_type = 'mixed'

number_of_tweets = 5
run_continuously = True
retweet_tweets = True
like_tweets = False


def create_api():
    auth = tweepy.OAuthHandler(TWITTER_API_KEY, TWITTER_API_KEY_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
    except Exception as e:
        logger.error('Authentication Error', exc_info=True)
        raise e
    logger.info(f"Authentication OK. Connected to @{api.me().screen_name}")

    return api
