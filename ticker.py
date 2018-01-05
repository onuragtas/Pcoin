#-*- coding: utf-8 -*-
import requests
import json
class ticker:
    api_url = "https://api.coinmarketcap.com/v1/ticker/"
    coin = []
    count = 0
    coins = {}

    def getData(self):
        self.count = 0
        self.coin = []
        try:
            resp = requests.get(self.api_url)
            json = resp.json()
            self.count = 0
            for coindetail in json:
                self.coin.append([coindetail['id'],coindetail['price_usd']])
                self.count = self.count + 1
            return self.coin
        except:
            print "api hatası"
        

    def setData(self, coins):
        self.coins = coins