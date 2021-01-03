import os

from tweepy import OAuthHandler
from tweepy import Stream

from app.listener import Listener

if __name__ == '__main__':

    listener = Listener()
    auth = OAuthHandler(os.environ.get("consumerKey"), os.environ.get("consumerSecret"))
    auth.set_access_token(os.environ.get("accessToken"), os.environ.get("accessTokenSecret"))
    stream = Stream(auth, listener)
    list_users = [
        '1173809603752026113',  # InvestRepeat
        '983704336424300545',  # indiaetfs
        '1341214000059613185',  # crypto_trackr
        '121635300'  # praGeek_ambani
    ]
    stream.filter(follow=list_users)
    stream.filter()
