
class Card:

    def __init__(self,db,card_id,reversed,disable_emoji=False):
        self.card_id = card_id
        self.db = db
        self.card = self.db.get_card(self.card_id)
        self.reversed = reversed
        self.disable_emoji = disable_emoji
        if self.reversed:
            self.card = self.card + " Reversed"
        self.text = db.get_meaning(self.card_id,reversed)
        self.emo_dict = {'of':'',
            'of ':'of',
            '':'',
            'Ace':'\U0001F1E6\U0000FE0F'.encode('utf-8').decode('utf-8'),
            'Two':'\U00000032\U000020E3'.encode('utf-8').decode('utf-8'),
            'Three':'\U00000033\U000020E3'.encode('utf-8').decode('utf-8'),
            'Four':'\U00000034\U000020E3'.encode('utf-8').decode('utf-8'),
            'Five':'\U00000035\U000020E3'.encode('utf-8').decode('utf-8'),
            'Six':'\U00000036\U000020E3'.encode('utf-8').decode('utf-8'),
            'Seven':'\U00000037\U000020E3'.encode('utf-8').decode('utf-8'),
            'Eight':'\U00000038\U000020E3'.encode('utf-8').decode('utf-8'),
            'Nine':'\U00000039\U000020E3'.encode('utf-8').decode('utf-8'),
            'Ten':'\U0001F51F'.encode('utf-8').decode('utf-8'),
            'Page':'\U0001F1F5\U0000FE0F'.encode('utf-8').decode('utf-8'),
            'Knight':'\U0001F1F0\U0000FE0F'.encode('utf-8').decode('utf-8'),
            'Queen':'\U0001F1F6\U0001F451'.encode('utf-8').decode('utf-8'),
            'King':'\U0001F1F0\U0001F451'.encode('utf-8').decode('utf-8'),
            'Reversed':'\U0001F504'.encode('utf-8').decode('utf-8'),
            'Pentacles':'\U0001F1F5'.encode('utf-8').decode('utf-8'),
            'Wands':'\U0001F1FC'.encode('utf-8').decode('utf-8'),
            'Swords':'\U0001F1F8'.encode('utf-8').decode('utf-8'),
            'Cups':'\U0001F1E8'.encode('utf-8').decode('utf-8')
        }
        self.emoji_card = self.emojify(self.card)

    def get_name(self):
        if self.disable_emoji:
            return self.card
        return self.emoji_card

    def get_detail(self):
        return self.text

    def emojify(self,card):
        words = card.split(' ')
        replace = []
        emojified = False
        for word in words:
            emo, emojified = self.emojify_word(word,emojified)
            if word == "Reversed":
                replace[-1]=replace[-1]+emo
                emo = ''
            replace.append(emo)
        if emojified:
            return ''.join(replace)
        return ' '.join(replace)

    def emojify_word(self,word,emojified):
        if word in self.emo_dict:
            if not emojified:
                if word == "of" or word == "The":
                    word = word + " "
                elif word!="Reversed":
                    emojified = True
            return self.emo_dict[word], emojified
        else:
            return word, emojified


# db = TarotDB("diviner.db")
# fool = Card(db,1,0,False)
# print(fool.get_name())
# print(fool.get_detail())
# db.close_con()
