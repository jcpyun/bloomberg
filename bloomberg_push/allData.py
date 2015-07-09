from threading import Thread
import urllib
import re
import json
import time
import math 

symbolslist2= open("allSymbols.txt").read()
symbolslist2= symbolslist2.split("\n")


def generateSymbolDaily():

	for symbol in symbolslist2:
	    myfile= open("dailyPrices/"+symbol+ ".txt","w+")
	    myfile.close()
	    htmltext= urllib.urlopen("http://www.bloomberg.com/markets/chart/data/1D/"+symbol+":US")
	    try:    
		data = json.load(htmltext)
		datapoints= data["data_values"]
	    except ValueError:
		continue
	    myfile = open("dailyPrices/"+symbol + ".txt", "a")

	    for point in datapoints:
		print point,datapoints
#		myfile.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
        myfile.write(str(str(point[0])+" "+str(point[1])+"\n"))
        myfile.close()


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

print symbolslist


threadlist = []

for u in symbolslist:
    t = Thread(target = th,args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

symbolslist= open("allSymbols.txt").read()
symbolslist= symbolslist.split("\n")






def changeGeneratedFile():
    myfile= open("testFile/listOfSymbols.txt","w+")
    for symbol in symbolslist:
	    myfile = open("testFile/listOfSymbols.txt", "a")	    
	    myfile.write(str(symbol+","+" "))
	    myfile.close()

changeGeneratedFile()
