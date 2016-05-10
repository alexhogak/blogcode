import pymongo
from time import gmtime, strftime, sleep


connection = pymongo.Connection('localhost', 27017)  #connect to database host
db = connection.ratesdb     #connect to rates database


results = {}

results["Appeals"] = appeals25
date = strftime("%d/%m/%Y %H:%M:%S", gmtime())
results["Date Added"] = date
db.testing.insert(results)