#!/usr/bin/env python3

import re

class Regex():
	def __init__(self):
		self.options = {
			"flags": re.MULTILINE | re.ASCII
		}
		self.compile()

	def compile(self):
		self.git_user = re.compile(
			r"^https://github\.com/(.*?)/.*$",
			**self.options
		)
		self.git_repo_name = re.compile(
			r"^https://github\.com/.*?/(.*)$",
			**self.options
		)
		self.succ_id = re.compile(
			r"^ID:(.*)$",
			**self.options
		)

