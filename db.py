import sqlite3

class TarotDB:

    def __init__(self, db):
        self.db = db
        self.con=sqlite3.connect(db)
        self.cur=self.con.cursor()

    def get_card(self,card_id):
        self.cur.execute("SELECT card FROM cards WHERE ID=?",(str(card_id)))
        return self.cur.fetchone()

    def get_meaning(self,card_id,reversed):
        self.cur.execute("SELECT meaning FROM meanings WHERE cardid=? AND reversed=?",(str(card_id),str(reversed)))
        return self.cur.fetchall()

    def close_con(self):
        self.con.close()

# db = TarotDB("diviner.db")
# c = db.get_card(1)
# m = db.get_meaning(1,0)
# print(c[0])
# for v in m:
#     print(v[0])
