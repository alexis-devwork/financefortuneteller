import os
from os.path import join, dirname
from dotenv import load_dotenv
import iexfinance
from iexfinance import stocks

class Querent:

    def __init__(self):
        self.gainers = iexfinance.stocks.get_collections('gainers', collection_type='list')
        self.losers = iexfinance.stocks.get_collections('losers', collection_type='list')
        self.querents = ["SPY",
                            self.gainers[0]['symbol'],
                            self.losers[0]['symbol']
                        ]

    def get_querents(self):
        return self.querents

# x = Querent()
# print(x.querents)
