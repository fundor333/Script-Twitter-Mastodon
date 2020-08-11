import os

import requests
from dotenv import load_dotenv

load_dotenv()

HOST_INSTANCE = os.getenv("MASTODON_HOST_INSTANCE")
TOKEN = os.getenv("MASTODON_TOKEN")


def tootTheTweet(tweet):
    headers = {}
    headers['Authorization'] = 'Bearer ' + TOKEN
    data = {}
    data['status'] = tweet
    data['visibility'] = 'public'

    response = requests.post(
        url=HOST_INSTANCE + '/api/v1/statuses', data=data, headers=headers)

    if response.status_code == 200:
        return True
    else:
        print(response.json())
        return False
