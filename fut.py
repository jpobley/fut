#!/usr/bin/env python

import argparse, json, os, urllib2
from time import sleep
from bs4 import BeautifulSoup as bs

from config import years, base_tmpl, list_tmpl

def main():
    args = get_parser().parse_args()

    if args.html:
        get_html()
    elif args.parse:
        parse_html()


def parse_html():
    pass

def get_html():
    '''Open and save HTML lists'''
    sleeps = []
    for year, items in years.iteritems():
        html = ""
        for item in items:

            if not sleeps:
                sleeps = [1,3,5]

            list_url = list_tmpl.format(year, item)
            print "Opening", list_url

            req = urllib2.Request(list_url, None, {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"})
            response = urllib2.urlopen(req)
            html += response.read()

            sleep(sleeps.pop())

        print "Writing file for 20{}".format(year)
        with open("src_html/20{}.html".format(year, item), "wb") as out_file:
            out_file.write(html)

def get_parser():
    p = argparse.ArgumentParser(description="FUT module", formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument("--html", help="Download HTML", action="store_true")
    p.add_argument("--parse", help="Parse HTML Files into CSV", action="store_true")
    return p


if __name__ == '__main__':
    main()
