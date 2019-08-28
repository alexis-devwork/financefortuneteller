from tarotdb import TarotDB
import random

class Reading:

    def __init__(self,db,querent_name):
        self.querent_name = querent_name
        self.seen, self.unseen = random.sample(range(1, 79), 2)
        self.db = db
        self.reading = self.build_reading()

    def build_reading(self):
        reading = [self.querent_name]
        reading.append("Seen Factors: "+self.card_text(self.seen))
        reading.append("Hidden Factors: "+self.card_text(self.unseen))
        reading = '\n'.join(reading)
        reading = reading + self.build_hashtags(reading)
        return reading

    def build_hashtags(self,reading):
        leeway = 280-len(reading)-1
        hashtags = ["#tarot","$"+self.querent_name,"#"+self.querent_name]
        tags = []
        while leeway > 2 and hashtags:
            tag=hashtags.pop()
            length = len(tag)+1
            if leeway-length>0:
                tags.append(tag)
                leeway-=length
        return '\n'+' '.join(tags)

    def card_text(self,card_id):
        card = self.db.get_card(card_id)[0]
        reversed = random.randrange(2)
        if reversed:
            card = card + " Rev"
        descriptions = db.get_meaning(card_id,reversed)
        detail = descriptions[random.randrange(len(descriptions))][0]
        return card + ": " + detail

db = TarotDB("diviner.db")
x = Reading(db,"NYSE")
reading = x.reading
if len(reading) + reading.count(";") < 280:
    reading.replace(";",", ")
print(reading)
db.close_con()
