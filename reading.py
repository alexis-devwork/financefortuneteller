from card import Card
import random

class Reading:

    def __init__(self,db,querent_name,disable_emoji=False):
        self.querent_name = querent_name
        self.db = db
        self.disable_emoji = disable_emoji
        self.seen, self.unseen = random.sample(range(1, 79), 2)
        self.seen_card = Card(self.db,self.seen,random.randrange(2),self.disable_emoji)
        self.unseen_card = Card(self.db,self.unseen,random.randrange(2),self.disable_emoji)
        self.TWITTER_MAX = 280
        self.reading = self.build_reading()

    def build_reading(self):
        reading = [self.querent_name+" Tarot"]
        reading.append("KNOWN: "+self.card_text(self.seen_card))
        reading.append("OVERLOOKED: "+self.card_text(self.unseen_card))
        chars = sum([len(x) for x in reading])+len(reading)
        tags = self.build_hashtags(chars)
        chars += sum([len(x) for x in tags])+len(tags)
        if self.TWITTER_MAX - chars >= 2:
            crystal_ball = '\U0001F52E'.encode('utf-8').decode('utf-8')
            reading[0] = crystal_ball + reading[0] + crystal_ball
        tags = ' '.join(tags)
        reading.append(tags)
        reading = '\n'.join(reading)
        return reading

    def build_hashtags(self,chars):
        leeway = self.TWITTER_MAX-chars-1
        hashtags = ["$"+self.querent_name,"#"+self.querent_name]
        tags = []
        while leeway > 2 and hashtags:
            tag=hashtags.pop()
            length = len(tag)+1
            if leeway-length>0:
                tags.append(tag)
                leeway-=length
        return tags

    def card_text(self,card):
        return card.get_name() + ": " + card.get_detail()

    def get_reading(self):
        return self.reading

# db = TarotDB("diviner.db")
# x = Reading(db,"NYSE",disable_emoji=True)
# reading = x.reading
# print(reading)
# db.close_con()
