import os
from os.path import join, dirname
from dotenv import load_dotenv
import time

from card import Card
from querent import Querent
from reading import Reading
from tarotdb import TarotDB
from tweeter import Tweeter

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
ACCESS_KEY = os.environ.get("ACCESS_KEY")
ACCESS_SECRET = os.environ.get("ACCESS_SECRET")

# tw = Tweeter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
# tw.tweet("test tweet")

db = TarotDB("diviner.db")
tw = Tweeter(CONSUMER_KEY,CONSUMER_SECRET,ACCESS_KEY,ACCESS_SECRET)
querents = Querent()
for q in querents.get_querents():
    reading = Reading(db,q)
    tweet = reading.get_reading()
    tw.tweet(tweet)
#
#
# faces = ['Ace',
#     'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
#     'Page','Knight','Queen','King'
#     ]
# suits = ['Swords','Cups','Wands','Pentacles']
#
#
# fool = Card(db,1,0)
# #tw.tweet(fool.card)
# for suit in suits:
#     strings = []
#     for face in faces:
#         strings.append(fool.emojify(face+" of "+suit))
#     tweet = ', '.join(strings)
#     posn = 0
#     # tw.tweet(fool.emojify("Two of Pentacles"))
#     while posn<len(tweet):
#         tw.tweet(tweet[posn:posn+150])
#         posn+=150
#         time.sleep(5)
#
#
# db.close_con()
