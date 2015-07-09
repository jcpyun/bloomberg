import json
import urllib 
import time
import math 
import re

symbolslist= open("symbols.txt").read()
symbolslist= symbolslist.split("\n")

def generateSymbolDaily():

	for symbol in symbolslist:
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
		myfile.write(str(symbol+","+str(point[0])+","+str(point[1])+"\n"))
	    myfile.close()


generateSymbolDaily()

