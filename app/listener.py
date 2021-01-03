import json
import os

import requests
from tweepy import StreamListener


class Listener(StreamListener):
    telegram_url = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"

    def on_data(self, data):
        tweet_data = json.loads(data)
        try:
            tweet = tweet_data["text"]
            req = self.telegram_url.format(os.environ.get("telegramBotApiKey"), "@crypto_trackr", tweet)
            requests.get(req)
            pass
        except Exception as e:
            print("Oops!", e.__class__, "occurred.")
            print("Fataa!!")

        return True

    def on_error(self, status):
        print('error with status code' + str(status))
        return True
