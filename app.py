import time
from card import Card
from reading import Reading
from tarotdb import TarotDB
from tweeter import Tweeter
from os import environ

CONSUMER_KEY = ENV['CONSUMER_KEY']
CONSUMER_SECRET = ENV['CONSUMER_SECRET']
ACCESS_KEY = ENV['ACCESS_KEY']
ACCESS_SECRET = ENV['ACCESS_SECRET']

db = TarotDB("diviner.db")
reading = Reading(db,"SPY")
tweet = reading.get_reading()
tw = Tweeter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
tw.tweet(tweet)
db.close_con()
