#!/usr/bin/env python3

# HEADER
## BEGIN DEBUG ONLY
from pprint import pprint
## END DEBUG ONLY
## UTILS
from utils.git import Git

class Updater():
	def __init__(self, url):
		self.git = Git(url)
		self.git.get_last()

if __name__ == "__main__":
	git_test = Updater("https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git")
