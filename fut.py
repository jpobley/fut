#!/usr/bin/env python

import argparse, json, os, urllib2
from time import sleep

years = {
    10: [1,2],
    11: [1,2,3,4,5],
    12: [1,2,3,4,5,6,7],
    13: [1,2,3,4,5,6,7,8,9],
    14: [1,2,3,4,5,6,7,8,9],
    15: [1,2,3,4,5,6,7,8],
    16: [1,2,3,4,5,6,7,8,9],
    17: [1,2,3,4,5,6,7]
}

base_tmpl = "http://www.futhead.com/"
list_tmpl = base_tmpl + "{}/players/?page={}&nation=95"

def main():
    args = get_parser().parse_args()

    if args.html:
        html()


def html():
    print 'woo'



def get_parser():
    p = argparse.ArgumentParser(description="FUT module", formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument("--html", help="Download HTML", action="store_true")

    return p


if __name__ == '__main__':
    main()
