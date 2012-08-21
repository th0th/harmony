# -*- coding: utf-8 -*-

import argparse

class ArgParser:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="A music folder organizer with the help of ID3 tags.")
		
		# arguments
		self.parser.add_argument('-s', '--source', dest='source', metavar='/path/to/source', help="source directory containing existing mp3 files", required=True)
		self.parser.add_argument('-r', '--recursive', dest='recursive', action='store_true', help="search source directory for mp3 files recursively")
		self.parser.add_argument('-d', '--destination', dest='destination', metavar='/path/to/destination', help="destination directory to move processed mp3 files (will be created if doesn't exist)", required=True)
		self.parser.add_argument('-x', '--mask', dest='mask', metavar='{mask}', help="mask for new files (available keys: artist, album, title, tracknumber, genre, date)", required=True)
		self.parser.add_argument('-m', '--method', dest='method', help="method for processing files", required=True, choices=['copy', 'move'])
		self.parser.add_argument('-o', '--overwrite', dest="overwrite", action='store_true', help="overwrite files already existing in destination")
		self.parser.add_argument('--version', action='version', help="display the current version and exit", version="Current version: 0.1")
		
	def get_args(self):
		return self.parser.parse_args()
