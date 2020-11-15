#!/usr/bin/python3
# Demonstration of the argparse package
# very usefull

import argparse
import logging
import os

logging.basicConfig(level=logging.DEBUG, format = "[%(asctime)s] [%(levelname)s]: %(message)s", datefmt="%Y%m%d %H:%M:%S")

parser = argparse.ArgumentParser(description="Imports Service-Reports (pdf-File) into SI/PAM database")

parser.add_argument("-v", "--verbose", help="increase output verbosity",
                    action="store_true")

parser.add_argument("-r", "--readonly", help="read and show data from pdf-File, no database import.",
                    action="store_true")

parser.add_argument("-db", "--db", help="Oracle Database Connection String",
                    type=str, default='PAM_WCNR_ENTW/PAM_WCNR_ENTW@PAM_CONF')

group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-f", "--file", help="provide filename of pdf-file",
                    type=str, default=None)
group.add_argument("-d", "--dir", help="provide directory containing pdf-Files",
                    type=str, default=None)

args = parser.parse_args()
logging.info("Start")

if args.file:
    # file exists and readable
    if not os.access(args.file, os.F_OK | os.R_OK):
        logging.error("Checking file")
        raise IOError('File not found: "{}"'.format(args.file))
    filename = args.file

if args.dir:
    # directory readable and executable
    if not os.access(args.dir, os.R_OK | os.X_OK):
        logging.error("Checking directory")
        raise IOError('Directory not found: "{}"'.format(args.dir))
    dirname = args.dir

if args.db:
    # db connection string valid
    p = re.compile(r'^\w+/{0,1}\w+@\w+$')
    if not p.match(args.db):
        logging.error("Checking db connection string")
        raise IOError('Must be of format <USER>/<PASSWORT>@DB')
    db_connection = args.db

# MAIN

logging.info("End")
