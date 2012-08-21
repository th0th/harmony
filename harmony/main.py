#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from argparser import ArgParser
from filehandler import FileHandler
from progressbar import ProgressBar

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

print("\nScanning source directory...")

# find files in source directory
file_handler.find_files(args.recursive)

if not ( file_handler.list_of_files ):
	print("\nNo proper file found in source directory. (are you sure you don't need --recursive?)")
	exit()

print("\nSource directory scanned. Found " + str(len(file_handler.list_of_files)) + " files.")

# set destination directory
file_handler.set_destination(args.destination)

# set method
file_handler.set_method(args.method)

# set mask
file_handler.set_mask(args.mask)

print("\nProcessing files...")

# progress bar - processing files
progress_bar = ProgressBar().start()

# let's do some magic
file_handler.process_files(overwrite=args.overwrite, callback=progress_bar.update)

# set progres bar status as finished
progress_bar.finish()

print("\nReport:")

processed_files = len(file_handler.list_of_files) - len(file_handler.list_of_erroneous_files) - len(file_handler.list_of_skipped_files)

print(str(processed_files) + " files successfully processed.")
print(str(len(file_handler.list_of_erroneous_files)) + " files couldn't be processed due to tag error.")
print(str(len(file_handler.list_of_skipped_files)) + " files skipped because a file exists in the destination (use --overwrite to overwrite).")