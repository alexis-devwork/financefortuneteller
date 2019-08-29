import sqlite3

class TarotDB:

    def __init__(self, db):
        self.db = db
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()

    def get_card(self,card_id):
        self.cur.execute("SELECT card FROM cards WHERE ID=?",(card_id,))
        return self.cur.fetchone()[0]

    def get_card_short(self,card_id):
        self.cur.execute("SELECT abbrev FROM cards WHERE ID=?",(card_id,))
        return self.cur.fetchone()[0]

    def get_meaning(self,card_id,reversed):
        self.cur.execute("SELECT meaning FROM meanings WHERE cardid=? AND reversed=?",(card_id,reversed))
        return self.cur.fetchone()[0]

    def close_con(self):
        self.con.close()

#db = TarotDB("diviner.db")
#c = db.get_card(10)
#print(c[0])
# m = db.get_meaning(1,0)
# print(c[0])
# for v in m:
#     print(v[0])
