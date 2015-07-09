from threading import Thread
import urllib
import re
import json
import time
import math 



def generateSymbolDaily(ur):
    counter = 0
    htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ur+":US")
    
    data = json.load(htmltext)
    datapoints= data["data_values"]
    print ur,"company Daily Quota"
    for x in datapoints:
        print ur,datapoints
        counter+=1
    
    
    print "threading terminated","--"*20
    print "processed quotes:", counter


symbolslist= open("testSymbols.txt").read()
symbolslist= symbolslist.split("\n")


threadlist = []

for u in symbolslist:
    t = Thread(target = generateSymbolDaily,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

