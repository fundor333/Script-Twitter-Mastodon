import tweepy
import os
import datetime

from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_KEY_SECRET = os.getenv("API_KEY_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")

AGE_OF_TWEET = int(os.getenv("AGE_OF_TWEET"))
AGE_OF_FUN_TWEET = int(os.getenv("AGE_OF_FUN_TWEET"))


def delete_it(api, status):
    print(status.created_at)
    api.destroy_status(status.id)


if __name__ == "__main__":
    auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    for status in tweepy.Cursor(api.user_timeline).items():

        now = datetime.datetime.now() - datetime.timedelta(days=AGE_OF_TWEET)
        if all([status.created_at < now, (not "Keybase" in status.text),]):
            delete_it(api, status)

        if all(
            [
                status.created_at
                < (datetime.datetime.now() - datetime.timedelta(days=AGE_OF_FUN_TWEET)),
                "#NintendoSwitch" in status.text,
            ]
        ):
            delete_it(api, status)
