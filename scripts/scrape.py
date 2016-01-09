#!/usr/bin/env python
import urllib, json
from time import sleep

#url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{},%22position%22:%22LF,CF,RF,ST,LW,LM,CAM,CDM,CM,RM,RW,LWB,LB,CB,RB,RWB%22%7D'
url = 'https://www.easports.com/fifa/ultimate-team/api/fut/item?jsonParamObject=%7B%22page%22:{},%22position%22:%22GK%22%7D'

print "Loading page #{}...".format(1)
print
response = urllib.urlopen(url.format(1))
data = json.loads(response.read())
total_pages = data['totalPages']
items = data.get('items', [])

print "Loaded page #{} items. Current count: {} players".format(1, len(items))
print

for moose in range(2, total_pages+1):
    sleep(.5)
    print "Loading page #{}...".format(moose)
    print
    response = urllib.urlopen(url.format(moose))
    data = json.loads(response.read())
    items += data.get('items', [])
    print "Loaded page #{} items. Current count: {} players".format(moose, len(items))
    print

with open('keepers.json', 'wb') as out:
    out.write(json.dumps(items))
