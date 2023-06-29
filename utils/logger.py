#!/usr/bin/env python3

from utils.config import LOG_DEB_LVL
from utils.config import LOG_PAD_STR

class Logger():
	def	__init__(self, debug_level=LOG_DEB_LVL):
		self.R = "\x1b[31m"
		self.G = "\x1b[32m"
		self.Y = "\x1b[33m"
		self.B = "\x1b[34m"
		self.RST = "\x1b[00m"

		self.S_head = f"[{self.G}+{self.RST}]"
		self.I_head = f"[{self.B}*{self.RST}]"
		self.W_head = f"[{self.Y}!{self.RST}]"
		self.E_head = f"[{self.R}-{self.RST}]"

	@staticmethod
	def	format(head, string, level):
		if LOG_DEB_LVL == -1 or level <= LOG_DEB_LVL:
			tmp_padding = LOG_PAD_STR * level
			print(f"{tmp_padding}{head} {string}")

	def	success(self, string, level=0):
		self.format(self.S_head, string, level)

	def	info(self, string, level=0):
		self.format(self.I_head, string, level)

	def	warn(self, string, level=0):
		self.format(self.W_head, string, level)

	def	error(self, string, level=0):
		self.format(self.E_head, string, level)

	def	commit(self, branch, local, remote, level=0):
		string = f"Branch {self.B}{branch}{self.RST} | "
		string += f"Local {{{self.G}{local[:7]}{self.RST}}} | "
		string += f"remote {{{self.R}{remote[:7]}{self.RST}}}"
		self.info(string, level)

log = Logger()
