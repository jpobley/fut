#!/usr/bin/env python
import urllib, json, datetime, os

from time import sleep
from config import files
import log

today = datetime.datetime.today().strftime("%Y%m%d")
data_folder = os.path.abspath('../data/{}'.format(today))

if not os.path.exists(data_folder):
    os.makedirs(data_folder)
else:
    import random
    while os.path.exists(data_folder):
        data_folder += "_" + str(random.randint(0,100))
    os.makedirs(data_folder)

logger = log.get_log(data_folder)

logger.debug('Begin process')

for name in files.keys():
    filename = '{}.json'.format(name)
    filepath = '{}/{}'.format(data_folder, filename)

    logger.debug('Starting download of {}'.format(name))

    #get first page
    logger.debug('Loading page {}'.format(1))

    response = urllib.urlopen(files[name].format(1))
    data = json.loads(response.read())
    total_pages = data['totalPages']
    items = data.get('items', [])

    logger.debug('Total pages: {}'.format(total_pages))

    for i in range(2, total_pages+1):
        sleep(.5)
        logger.debug('Loading page {}'.format(i))
        try:
            response = urllib.urlopen(files[name].format(i))
            data = json.loads(response.read())
            items += data.get('items', [])
        except:
            logger.error('Unable to load page {}'.format(i))

    logger.debug('Writing out file {}'.format(filename))
    try:
        with open(filepath, 'wb') as out:
            out.write(json.dumps(items))
    except:
        logger.error('Unable to write file {}'.format(filepath))
        logger.debug(json.dumps(items))

logger.debug('Process complete')