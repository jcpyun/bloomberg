from threading import Thread
import urllib
import re
import json
import time
import math 

symbolslist2= open("allSymbols.txt").read()
symbolslist2= symbolslist2.split("\n")


def generateSymbolDaily(ur):
    print ur, "Data Detected"
    myfile= open("dailyPrices/"+ur+ ".txt","w+")
    myfile.close()
    htmltext= urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+ur+":US")    
    data = json.load(htmltext)
    datapoints= data["data_values"]

    myfile = open("dailyPrices/"+ur + ".txt", "a")
    print ur, "Threading Daily Data"
    for point in datapoints:
#		myfile.write(str(ur+","+str(point[0])+","+str(point[1])+"\n")) 
        myfile.write(str(str(point[0])+" "+str(point[1])+"\n"))
    myfile.close()
    print ur, "Data Processed"
    print "Accessing next Stock Quote data..."
    print "----"*9
    print "processing next..."
    print "Terminating Data...."
    print "done."

def th(ur):
#    base = "http://finance.yahoo.com/q?s="+ur
    base= "http://www.bloomberg.com/markets/chart/data/1D/"+ur+":US"
    regex = "<title>.+?</title>"
    pattern = re.compile(regex)
    htmltext= urllib.urlopen(base).read()

    results = re.findall(pattern,htmltext)
#    print results   

symbolslist=open("allSymbols.txt").read()
symbolslist=symbolslist.replace("\n",",").split(",")




threadlist = []

for u in symbolslist:
    t = Thread(target = generateSymbolDaily,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

