import argparse

class Args:
	def __init__(self):
		self.parser = argparse.ArgumentParser(description="A music folder organizer with the help of ID3 tags.")
		
		# options
		self.parser.add_argument('-s', '--source', dest='source', help="source directory containing existing mp3 files", required=True)
		self.parser.add_argument('-d', '--destination', dest='destination', help="destination directory to move processed mp3 files", required=True)
		self.parser.add_argument('-m', '--method', dest='method', help="method for processing files", required=True, choices=['copy', 'move'])
		self.parser.add_argument('-o', '--overwrite', action='store_true', help="overwrite files already existing in destination")
		
	def get_args(self):
		return self.parser.parse_args()
