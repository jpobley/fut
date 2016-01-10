#!/usr/bin/env python
import logging

def get_log(path):
    logger = logging.getLogger('FUT')
    logger.setLevel(logging.DEBUG)

    # create file handler which logs even debug messages
    error = logging.FileHandler(path + '/errors.log')
    error.setLevel(logging.ERROR)

    debug = logging.FileHandler(path + '/debug.log')
    debug.setLevel(logging.DEBUG)

    stdout = logging.StreamHandler()
    stdout.setLevel(logging.DEBUG)

    # create formatter and add it to the handlers
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s", "%Y-%m-%d %H:%M:%S")
    error.setFormatter(formatter)
    debug.setFormatter(formatter)
    stdout.setFormatter(logging.Formatter("%(message)s"))

    # add the handlers to logger
    logger.addHandler(error)
    logger.addHandler(debug)
    logger.addHandler(stdout)

    return logger