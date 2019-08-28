from tarotdb import TarotDB
from tweeter import Tweeter
from reading import Reading
from card import Card
import time

db = TarotDB("diviner.db")
reading = Reading(db,"NYSE")
tweet = reading.reading
tw = Tweeter("credentials.txt")
tw.tweet(tweet)
db.close_con()

# faces = ['Ace',
#     'Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten'#,
#     #'Page','Knight','Queen','King'
#     ]
# suits = ['Swords','Cups','Wands','Pentacles']
#
#
#
# db = TarotDB("diviner.db")
# fool = Card(db,1,0)
# strings = []
# for face in faces:
#     for suit in suits:
#         strings.append(fool.emojify(face + " of " + suit+ " Reversed"))
# tweet = ', '.join(strings)
#
#
# tw = Tweeter("credentials.txt")
# posn = 0
# # tw.tweet(fool.emojify("Two of Pentacles"))
# while posn<len(tweet):
#     tw.tweet(tweet[posn:posn+150])
#     posn+=150
#     time.sleep(5)
# db.close_con()
