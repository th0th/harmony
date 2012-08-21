# -*- coding: utf-8 -*-

from mutagen.easyid3 import EasyID3

class TagHandler:
	def __init__(self):
		self.mask = None

	def set_mask(self, mask):
		self.mask = mask

	def read_tags(self, filepath):
		tags = EasyID3(filepath)

		new_tags = {}

		for tag in tags:
			new_tags[tag] = tags[tag][0].encode('utf-8')

		return new_tags

	def generate_filename(self, filepath):
		filename = self.mask.format(**self.read_tags(filepath))

		return filename