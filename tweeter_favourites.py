from time import sleep

import tweepy
from tweepy import OAuthHandler

from app import config
from app.listener import Listener

if __name__ == '__main__':

    listener = Listener()
    auth = OAuthHandler(os.environ.get("consumerKey"), os.environ.get("consumerSecret"))
    auth.set_access_token(os.environ.get("accessToken"), os.environ.get("accessTokenSecret"))

    api = tweepy.API(auth)

    file = open("my_favourites.txt", "w+")

    User = '@prageek_ambani'
    # api.favorites(screen_name="")
    for favorite in tweepy.Cursor(api.favorites, id=User).items(10000):
        print('tweet: ' + str(favorite.text.encode("utf-8")) + '\n')
        file.write('tweet: ' + str(favorite.text.encode("utf-8")) + '\n')
        sleep(3.5)
    print("We're done!!")
