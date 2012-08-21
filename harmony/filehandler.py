# -*- coding: utf-8 -*-

import os, shutil
from taghandler import TagHandler

class FileHandler:
	def __init__(self):
		# properties
		self.number_of_files = 0
		self.extensions = ['mp3']
		self.list_of_files = []
		self.list_of_erroneous_files = []
		self.list_of_skipped_files = []
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
	
	def find_files(self, recursive=False):
		if ( recursive ):
			for folder, subfolder, filenames in os.walk(self.source):
				for filename in filenames:
					if ( self.check_for_extension(filename) ):
						self.list_of_files.append(os.path.join(folder, filename))
		else:
			for filename in os.listdir(self.source):
				if ( self.check_for_extension(filename) ):
					self.list_of_files.append(os.path.join(self.source, filename))

		self.scanned = True

	def check_for_extension(self, filename):
		for extension in self.extensions:
			if ( extension in filename ):
				return True
		# skip the file
		return False

	def prepare_dir(self, filepath):
		directory = os.path.dirname(filepath)

		if not ( os.path.isdir(directory) ):
			os.makedirs(directory)
	
	def process_file(self, src, dst, overwrite=False):
		if ( overwrite or not os.path.isfile(dst) ):
			self.prepare_dir(dst)
			return getattr(shutil, self.method)(src, dst)
		else:
			self.list_of_skipped_files.append(src)

	# link to taghandler class' method
	def set_mask(self, mask):
		self.tagHandler.mask = mask

		return True

	def process_files(self, overwrite=False, callback = None):
		if not ( self.scanned ):
			raise Exception('source isn\'t scanned yet')

		if not ( self.tagHandler.mask ):
			raise Exception('mask is not set')

		state = 0

		for filepath in self.list_of_files:
			try:
				filename = self.tagHandler.generate_filename(filepath)

				destination = os.path.join(self.destination, filename)

				# callback
				if ( callback ):
					callback(state)

				self.process_file(filepath, destination)
			except:
				self.list_of_erroneous_files.append(filepath)

			state += 100.0 / len(self.list_of_files)