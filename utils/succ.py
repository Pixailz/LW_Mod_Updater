#!/usr/bin/env python3

import os

from utils.regex import regex
from utils.logger import log

class Succ():
	def __init__(self, base_folder, mod_target):
		self.mod_target = mod_target
		self.path_manifest = self.find_mod_folder(base_folder)
		if self.path_manifest != None:
			self.get_succ_infos()

	def get_infos(self, regex, string):
		try:
			return (regex.findall(string)[0])
		except IndexError:
			return (None)

	def get_succ_infos(self):
		with open(self.path_manifest, "r") as tmp_file:
			readed_str = tmp_file.read()
		self.man_id = self.get_infos(regex.succ_id, readed_str)
		self.man_name = self.get_infos(regex.succ_name, readed_str)
		self.man_author = self.get_infos(regex.succ_author, readed_str)
		self.man_version = self.get_infos(regex.succ_version, readed_str)
		self.man_priority = self.get_infos(regex.succ_priority, readed_str)

		log.info(self.man_id, 2)
		log.info(self.man_name, 2)
		log.info(self.man_author, 2)
		log.info(self.man_version, 2)
		log.info(self.man_priority, 2)

	def find_mod_folder(self, base_folder):
		self.already_viewed = []
		while True:
			found = self.search_for_succ_file(base_folder)
			if found == None:
				head = f"[{log.R}{self.mod_target}{log.RST}]"
				log.error(f"{head} Not found", 1)
				return (None)
			with open(found, "r") as tmp_file:
				readed = tmp_file.read()
			try:
				founded = regex.succ_name.findall(readed)[0]
			except IndexError:
				pass
			if founded != self.mod_target:
				try:
					founded = regex.succ_id.findall(readed)[0]
				except IndexError:
					self.already_viewed.append(found)
					continue
			if founded == self.mod_target:
				head = f"[{log.G}{self.mod_target}{log.RST}]"
				tail = f"{{{log.Y}{found}{log.RST}}}"
				log.success(f"{head} -> {tail}", 1)
				return (found)
			else:
				self.already_viewed.append(found)

	def search_for_succ_file(self, base_folder):
		for root, dirs, files in os.walk(base_folder):
			for file in files:
				if file == "manifest.succ":
					tmp_path = os.path.join(root, file)
					if tmp_path in self.already_viewed:
						continue
					return(tmp_path)
			for dir in dirs:
				if dir == ".git":
					continue
				tmp_file = self.search_for_succ_file(os.path.join(base_folder, dir))
				if tmp_file == None:
					continue
				return (tmp_file)
