#-*- coding: utf-8 -*-
from ticker import *
from httpserver import *
import time
import os.path
import thread
import sqlite3
class main:

    logpath = "pcoinlog"
    amount = 300
    ticker = ticker()
    httpserver
    coins = {}
    max = {}
    min = {}

    def createDB(self,c):
        c.execute('''CREATE TABLE IF NOT EXISTS process(
id INTEGER PRIMARY KEY,
process TEXT NOT NULL,
coin VARCHAR(100),
value TEXT NOT NULL ,
amount TEXT NOT NULL
)
''')
        c.execute('''CREATE TABLE IF NOT EXISTS datas(
id INTEGER PRIMARY KEY,
coin VARCHAR(100),
value TEXT NOT NULL
)
''')

    def __init__(self):
        thread.start_new_thread(httpserver,())

        if not os.path.exists(self.logpath):
            log = open(self.logpath,"w")
            log.write("Process\t\t\tCoinName\t\t\tValue\t\t\tAmount\n")
            log.close()

        
        datas = self.ticker.getData()
        for coin in datas:
            self.coins[coin[0]] = []

            self.max[coin[0]] = {}
            self.min[coin[0]] = {}

            self.max[coin[0]]["value"] = 0
            self.min[coin[0]]["value"] = 0

            self.max[coin[0]]["count"] = 0
            self.min[coin[0]]["count"] = 0
        
        conn = sqlite3.connect('pcoin.db')
        c = conn.cursor()
        self.createDB(c)
        datas = conn.cursor().execute("SELECT * FROM datas").fetchall()
        if len(datas) > 0:
            for item in datas:
                try:
                    self.coins[item[1]].append(float(item[2]))
                except:
                    a = True
            c.close()
            conn.close()

        while True:
            conn = sqlite3.connect('pcoin.db')
            c = conn.cursor()
            self.createDB(c)
            print("update...\r")
            log = open(self.logpath,"a")
            datas = self.ticker.getData()
            
            try:
                for coin in datas:
                    try:
                        self.coins[coin[0]].append(float(coin[1]))
                        c.execute("INSERT INTO datas (coin,value)VALUES('"+str(coin[0])+"', '"+str(float(coin[1]))+"')")
                    except Exception:
                        print(coin[0], "eklenme hatası")
            except:
                print "nullpointer"
                
            for coin in self.coins:
                t = 0
                if coin in ("litecoin","bitcoin","dogecoin","iota","ripple"):
                

                    for value in self.coins[coin]:
                        t = t + value
                    ort = t/len(self.coins[coin])
                    
                    try:
                        #print coin, ort, value
                        if value-self.coins[coin][-2] > self.max[coin]["value"]:
                            self.max[coin]["value"] = value-self.coins[coin][-2]
                            self.max[coin]["count"] = self.max[coin]["count"]+1
                            if self.max[coin]["count"] > 5:
                                print coin, ort, value, len(self.coins[coin]),"sat",value-self.coins[coin][-2], self.max[coin]["value"]
                                log.write("sat\t\t\t\t" + coin+"\t\t\t\t"+str(value)+"\t\t\t"+str(self.amount)+"\n")
                                c.execute("INSERT INTO process (process, coin,value,amount)VALUES('sat','"+str(coin)+"', '"+str(value)+"','"+str(self.amount)+"')")
                                self.max[coin]["count"] = 0
                        elif value-self.coins[coin][-2] == max:
                            a=1#coin, ort, value, len(coins[coin]),"sabit",value-coins[coin][-2], maxfark
                        elif value-self.coins[coin][-2] < self.min[coin]["value"]:
                            self.min[coin]["value"] = value-self.coins[coin][-2]
                            self.min[coin]["count"] = self.min[coin]["count"]+1
                            if self.min[coin]["count"] > 5:
                                print coin, ort, value, len(self.coins[coin]),"al",value-self.coins[coin][-2], self.min[coin]["value"]
                                log.write("sat\t\t\t\t" + coin+"\t\t\t\t"+str(value)+"\t\t\t"+str(self.amount)+"\n")
                                c.execute("INSERT INTO process (process, coin,value,amount)VALUES('al','"+str(coin)+"', '"+str(value)+"','"+str(self.amount)+"')")
                                self.min[coin]["count"] = 0
                    except IndexError:
                        print "2den az değer var"
            conn.commit()
            c.close()
            conn.close()
            log.close()
            time.sleep(50)


main()