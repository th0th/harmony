import os, shutil

class FileHandler:
	def __init__(self):
		# properties
		self.number_of_files = 0
		self.extensions = ['mp3']
		self.list_of_files = []
		self.method = None
	
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
