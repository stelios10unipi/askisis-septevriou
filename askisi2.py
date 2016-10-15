import json
import urllib
import urllib2

import datetime

today= []
numbers=[79]
kliroseis=[]
max=[6]
min=[6]

date = datetime.datetime.now()

websource = urllib.urlopen('http://applications.opap.gr/DrawsRestServices/kino/drawDate/15-10-2016.json')
data = json.loads(websource.read().decode())

print data
