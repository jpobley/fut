#!/usr/bin/env python
import urllib, json, datetime, os

from time import sleep
from config import files

today = datetime.datetime.today().strftime("%Y%m%d")
data_folder = '../data/{}'.format(today)

if not os.path.exists(data_folder):
    os.makedirs(data_folder)
else:
    import random
    while os.path.exists(data_folder);
        data_folder += "_" + random.randint(0,100)
    os.makedirs(data_folder)

for name in files.keys():
    filename = '{}.json'.format(name)
    filepath = '{}/{}'.format(data_folder, filename)

    #get first page
    response = urllib.urlopen(files[name].format(1))
    data = json.loads(response.read())
    total_pages = data['totalPages']
    items = data.get('items', [])

    for i in range(2, total_pages+1):
        sleep(.5)
        response = urllib.urlopen(url.format(i))
        data = json.loads(response.read())
        items += data.get('items', [])

    with open(filepath, 'wb') as out:
        out.write(json.dumps(items))
