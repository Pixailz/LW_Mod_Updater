#!/usr/bin/env python3

# HEADER
## BEGIN DEBUG ONLY
from pprint import pprint
## END DEBUG ONLY
import os
## UTILS
from utils.git import Git
from utils.logger import Logger

log = Logger()

MODZ = {
	"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git" : [
		"WireTracer",
		"CustomWirePlacer"
	],
	"https://github.com/GHXX/LogicWorld-TcpBridge" : [
		"Tcp Brdige"
	]
}

class Updater():
	def __init__(self):
		self.git = [ Git(link) for link in MODZ ]
		for git in self.git:
			git.get_last()

	def install(self):
		for git in self.git:
			for mod_id in MODZ[git.url]:
				log.success(mod_id)
				log.info(git.dir)
				print(self.search_for_succ_file(git.dir, mod_id))

	def find_succ_folder(self, base_folder, mod_id):
		self.already_viewed = []
		log.info(base_folder)
		while True:
			found = self.search_for_succ_file(base_folder, mod_id)
			if found == None:
				log.error("not found")
			else:
				with open(found, "r") tmo_file:

			break

	def search_for_succ_file(self, base_folder, mod_id):
		log.warn("searching in : " + base_folder)
		for root, dirs, files in os.walk(base_folder):
			for file in files:
				log.info("file found : " + file)
				if file.endswith(".succ"):
					# if file not in self.already_viewed:
					return(os.path.join(root, file))
			for dir in dirs:
				return (self.search_for_succ_file(os.path.join(base_folder, dir), mod_id))

if __name__ == "__main__":
	test = Updater()
	# test.install()
	print(test.find_succ_folder(".cache/Ecconia", "WireTracer"))
	print(test.find_succ_folder(".cache/GHXX", "Tcp Bridge"))
