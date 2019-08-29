import time
from card import Card
from reading import Reading
from tarotdb import TarotDB
from tweeter import Tweeter
from os import environ

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

db = TarotDB("diviner.db")
reading = Reading(db,"SPY")
tweet = reading.get_reading()
tw = Tweeter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
tw.tweet(tweet)
db.close_con()
