import time
from card import Card
from reading import Reading
from tarotdb import TarotDB
from tweeter import Tweeter

db = TarotDB("diviner.db")
reading = Reading(db,"SPY")
tweet = reading.get_reading()
tw = Tweeter("credentials.txt")
tw.tweet(tweet)
db.close_con()

# faces = ['Ace',
#     'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten',
#     'Page','Knight','Queen','King'
#     ]
# suits = ['Swords','Cups','Wands','Pentacles']
#

# tw = Tweeter("credentials.txt")
# db = TarotDB("diviner.db")
# fool = Card(db,1,0)
# tw.tweet(fool.card)
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
# db.close_con()
