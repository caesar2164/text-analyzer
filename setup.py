#!/usr/bin/env python
import argparse
import logging
import sys

debug = False
sys.tracebacklimit = 0

parser = argparse.ArgumentParser(
    description='A script to analyze text and count the incidence and declensions of names/strings'
)

# Define parsable arguments for function call
parser.add_argument(
    '-v',
    '--verbose',
    help='increase output verbosity',
    action="store_true"
)
parser.add_argument(
    '-t',
    '--textfile',
    help='Pass a text file to analyze [REQUIRED]',
    action='store',
    required=True,
)
parser.add_argument(
    '-d',
    '--deffile',
    help='Pass a definition file to use for analysis [REQUIRED]',
    action='store',
    required=True,
)

def get_arguments():
    # Parse the arguments
    args = parser.parse_args()

    # Run in DEBUG MODE if -v flag is set
    if args.verbose:
        logging.basicConfig(level=logging.DEBUG)
        debug = True
        sys.tracebacklimit = 1000
        logging.debug(' Running in DEBUG MODE, showing full error output!') 

    return args.textfile, args.deffile
