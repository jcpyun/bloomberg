from threading import Thread
import urllib
import re
import json
import time
import math 



def generateSymbolDaily(ur):
    counter = 0
    highestQuote = 0
    highestStock=""
    currentQuote=0
    currentStock=""
    htmltext=urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ur+":US")
    
    data = json.load(htmltext)
    datapoints= data["data_values"]
    print ur,"company Daily Quota"
    for x in datapoints:
        print x
        counter+=1
        currentQuote=x[1]
        currentStock=ur
    if currentQuote>highestQuote:
        highestQuote=currentQuote
        highestStock= currentStock
            
        

    
    print "threading terminated","--"*20
    print "processed quotes:", counter
    print len(datapoints),"WHATS UP MA DOG-##############################" *99, "FUUUUUUUUUUUUU"*900
    print highestQuote, highestStock


symbolslist= open("testSymbols.txt").read()
symbolslist= symbolslist.split("\n")


threadlist = []

for u in symbolslist:
    t = Thread(target = generateSymbolDaily,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()




