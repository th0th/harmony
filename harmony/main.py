#!/usr/bin/env python2

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

file_handler.find_files()

print(file_handler.list_of_files)
