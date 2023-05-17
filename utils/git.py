#!/usr/bin/env python3

import os
import git
import requests
from utils.regex import regex
from utils.logger import log
from config import GIT_CACH_DIR

if not os.path.isdir(GIT_CACH_DIR):
	os.mkdir(GIT_CACH_DIR)

GIT_TOKEN = None
if os.path.isfile("token_git.py"):
	from token_git import GIT_TOKEN

class ModzGit():
	def __init__(self, url, branch="master"):
		self.url = url
		self.branch = branch
		self.dev_name = regex.git_user.findall(self.url)[0]
		self.repo_name = regex.git_repo_name.findall(self.url)[0]
		self.repo_name = self.repo_name.replace(".git", '')
		self.cache_dir = GIT_CACH_DIR + '/' + self.dev_name
		if not os.path.isdir(self.cache_dir):
			log.warn("Repo (" + url + ") not found localy, clonning")
			self.clone(branch)
		else:
			log.info(f"Repo ({self.repo_name}) found localy")
			self.repo = git.Repo(self.cache_dir)
			self.get_last()

	def get_last_remote(self):
		url = "https://api.github.com/repos/"
		url += f"{self.dev_name}/{self.repo_name}/commits/{self.branch}"
		headers = {}
		headers["Accept"] = "application/vnd.github.VERSION.sha"
		if GIT_TOKEN != None:
			headers["Authorization"] = f"Bearer {GIT_TOKEN}"
		req = requests.get(url=url, headers=headers)
		if req.status_code != 200:
			req_status = f"{log.R}{req.status_code}{log.RST}"
			log.error(f"Error fetching latest commit [{req_status}]")
			log.error(f"-> [{url}]")
			return (None)
		return (req.text)

	def get_last(self):
		log.info("Checking for update.", 1)
		last_remote = str(self.get_last_remote())
		if last_remote == None:
			return
		last_local = str(self.repo.head.commit)
		if last_remote != last_local:
			log.warn("Not up-to-date, updating", 1)
			self.repo.remotes.origin.pull(self.branch)
		else:
			log.success("Repo up-to-date", 1)
		log.commit(self.branch, last_local, last_remote, 2)

	def clone(self, branch):
		self.repo = git.Repo.clone_from(self.url, self.cache_dir, branch=branch)
