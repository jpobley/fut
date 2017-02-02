#!/usr/bin/env python

import argparse, json, os, urllib2

def main():
    pass


def get_parser():
    p = argparse.ArgumentParser(description="FUT module", formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument("--html", help="Download HTML")

    return p

if __name__ == '__main__':
    main()
