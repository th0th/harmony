# -*- coding: utf-8 -*-

import os, shutil
from taghandler import TagHandler

class FileHandler:
	def __init__(self):
		# properties
		self.number_of_files = 0
		self.extensions = ['mp3']
		self.list_of_files = []
		self.method = None
		self.scanned = False

		# tag handler instance
		self.tagHandler = TagHandler()
	
	def set_source(self, src):
		self.source = src
	
	def set_destination(self, dst):
		self.destination = dst
	
	def set_method(self, method):
		if ( method in ['copy', 'move'] ):
			self.method = method
			return True
		else:
			raise Exception("method not available.")
	
	def find_files(self):
		for folder, subfolder, filenames in os.walk(self.source):
			for filename in filenames:
				if ( self.check_for_extension(filename) ):
					self.list_of_files.append(os.path.join(folder, filename))

		self.scanned = True

	def check_for_extension(self, filename):
		for extension in self.extensions:
			if ( extension in filename ):
				return True
		# skip the file
		return False
	
	def copy_file(self, src, dst):
		return shutil.copy(src, dst)
	
	def move_file(self, src, dst):
		return shutil.move(src, dst)

	# link to taghandler class' method
	def set_mask(self, mask):
		self.tagHandler.mask = mask

		return True

	def process_files(self):
		if not ( self.scanned ):
			raise Exception('source isn\'t scanned yet')

		if not ( self.tagHandler.mask ):
			raise Exception('mask is not set')

		for filepath in self.list_of_files:
			filename = self.tagHandler.generate_filename(filepath)
			print filename

		if ( self.method == 'move' ):
			# move files
			pass
		else:
			# copy files
			pass