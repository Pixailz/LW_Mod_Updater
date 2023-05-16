#!/usr/bin/env python3

import os
import git
from utils.regex import Regex
from utils.logger import Logger

log = Logger()

## CONFIG
CACHE_DIR=".cache"

if not os.path.isdir(CACHE_DIR):
	os.mkdir(CACHE_DIR)

class Git():
	def __init__(self, url):
		self.re = Regex()
		self.url = url
		self.dev_name = self.re.git_user.findall(self.url)[0]
		self.repo_name = self.re.git_repo_name.findall(self.url)[0]
		self.repo_name = self.repo_name.replace(".git", '')
		self.dir = CACHE_DIR + '/' + self.dev_name
		if not os.path.isdir(self.dir):
			log.warn("Repo (" + url + ") not found localy, clonning")
			self.clone()
		else:
			log.info(f"Repo ({self.repo_name}) found localy")
			self.repo = git.Repo(self.dir)
		self.branch = self.repo.active_branch.name

	def get_last(self):
		log.info("Checking for update.", 1)
		last_remote = str(self.repo.rev_parse(self.branch))
		last_local = str(self.repo.head.commit)
		log.commit(self.branch, last_local, last_remote, 1)
		if last_remote != last_local:
			log.warn("Not up-to-date, updating", 2)
			self.remotes.upstream.pull(self.branch)
		else:
			log.success("Repo up-to-date", 2)

	def clone(self):
		self.repo = git.Repo.clone_from(self.url, self.dir)
