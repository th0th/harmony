#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from argparser import ArgParser
from filehandler import FileHandler

# cli arg parser instance
arg_parser = ArgParser()

args = arg_parser.get_args()

# show version and exit
if ( args.version == True ):
	print("Current version: 0.1")
	exit()

# file handler instance
file_handler = FileHandler()

# set source directory
file_handler.set_source(args.source)

# set destination directory
file_handler.set_destination(args.destination)

# set method
file_handler.set_method(args.method)

# set mask
file_handler.set_mask(args.mask)

# find files in source directory
file_handler.find_files()

# let's do some magic
file_handler.process_files()