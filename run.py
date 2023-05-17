#!/usr/bin/env python3

# HEADER
## BEGIN DEBUG ONLY
from pprint import pprint
## END DEBUG ONLY
import os
import shutil
## UTILS
from utils.git import ModGit
from utils.logger import Logger
from utils.regex import Regex

log = Logger()

MODZ_FOLDER = "/home/pix/.local/share/Steam/steamapps/common/Logic World/GameData"
MODZ = {
	"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git":
	[
		"EccsWindowHelper",
		"AssemblyLoader",
		"FixClientBugs",
		"WireTracer",
		"CustomWirePlacer"
	],
	"https://github.com/GHXX/LogicWorld-TcpBridge":
	[
		"Tcp Bridge"
	]
}

class Modz():
	def __init__(self):
		self.git = [ ModGit(link) for link in MODZ ]

		self.re = Regex()

	def install(self):
		for git in self.git:
			for mod_id in MODZ[git.url]:
				log.info(f"Searching for {mod_id}")
				src_mod_folder = self.find_mod_folder(git.dir, mod_id)
				if src_mod_folder == None:
					continue
				dst_mod_folder = f"{MODZ_FOLDER}/{git.dev_name}-{mod_id}"
				if os.path.isdir(dst_mod_folder):
					log.warn(f"dst folder found, removing it", 1)
					shutil.rmtree(dst_mod_folder)
				shutil.copytree(src_mod_folder, dst_mod_folder)

	def find_mod_folder(self, base_folder, mod_id):
		self.already_viewed = []
		while True:
			found = self.search_for_succ_file(base_folder, mod_id)
			if found == None:
				log.error("Not found", 1)
				return (None)
			with open(found, "r") as tmp_file:
				tmp_str = tmp_file.read()
			try:
				tmp_str = self.re.succ_name.findall(tmp_str)[0]
			except IndexError:
				self.already_viewed.append(found)
				continue
			if tmp_str == mod_id:
				log.success(f"Founded in {found}", 1)
				return (os.path.dirname(found))
			else:
				self.already_viewed.append(found)

	def search_for_succ_file(self, base_folder, mod_id):
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
				tmp_file = self.search_for_succ_file(os.path.join(base_folder, dir), mod_id)
				if tmp_file == None:
					continue
				return (tmp_file)

if __name__ == "__main__":
	test = Modz()
	test.install()
	# print(test.find_mod_folder(".cache/Ecconia", "WireTracer"))
	# print(test.find_mod_folder(".cache/GHXX", "ghxx.tcpbridge"))
