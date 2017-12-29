#-*- coding: utf-8 -*-
from ticker import *
import time
import os.path


logpath = "pcoinlog"
amount = 300
ticker = ticker()
coins = {}
max = {}
min = {}

if not os.path.exists(logpath):
    log = open(logpath,"w")
    log.write("Process\t\t\tCoinName\t\t\tValue\t\t\tAmount\n")
    log.close()


datas = ticker.getData()
for coin in datas:
    coins[coin[0]] = []

    max[coin[0]] = {}
    min[coin[0]] = {}

    max[coin[0]]["value"] = 0
    min[coin[0]]["value"] = 0

    max[coin[0]]["count"] = 0
    min[coin[0]]["count"] = 0

while True:
    print("update...\r")
    log = open(logpath,"a")
    datas = ticker.getData()
    
    for coin in datas:
        try:
            coins[coin[0]].append(float(coin[1]))
        except Exception:
            print(coin[0], "eklenme hatası")
    for coin in coins:
        t = 0
        if coin in ("litecoin","bitcoin","dogecoin","iota","ripple"):
            

            for value in coins[coin]:
                t = t + value
            ort = t/len(coins[coin])
            
            try:
                #print coin, ort, value, len(coins[coin]),value-coins[coin][-2], maxfark
                if value-coins[coin][-2] > max[coin]["value"]:
                    max[coin]["value"] = value-coins[coin][-2]
                    max[coin]["count"] = max[coin]["count"]+1
                    if max[coin]["count"] > 5:
                        print coin, ort, value, len(coins[coin]),"sat",value-coins[coin][-2], max[coin]["value"]
                        log.write("sat\t\t\t\t" + coin+"\t\t\t\t"+str(value)+"\t\t\t"+str(amount)+"\n")
                        max[coin]["count"] = 0
                elif value-coins[coin][-2] == max:
                    a=1#coin, ort, value, len(coins[coin]),"sabit",value-coins[coin][-2], maxfark
                elif value-coins[coin][-2] < min[coin]["value"]:
                    min[coin]["value"] = value-coins[coin][-2]
                    min[coin]["count"] = min[coin]["count"]+1
                    if min[coin]["count"] > 5:
                        print coin, ort, value, len(coins[coin]),"al",value-coins[coin][-2], min[coin]["value"]
                        log.write("sat\t\t\t\t" + coin+"\t\t\t\t"+str(value)+"\t\t\t"+str(amount)+"\n")
                        min[coin]["count"] = 0
            except Exception:
                print "2den az değer var"
    log.close()
    time.sleep(5)

