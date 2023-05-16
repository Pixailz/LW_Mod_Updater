#!/usr/bin/env python3

class Logger():
	def __init__(self):
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
	def format(head, string):
		return (f" {head} \x1b[7G{string}")

	def success(self, string):
		print(self.format(self.S_head, string))

	def info(self, string):
		print(self.format(self.I_head, string))

	def warn(self, string):
		print(self.format(self.W_head, string))

	def	error(self, string):
		print(self.format(self.E_head, string))

	def commit(self, branch, local, remote):
		string = f"Branch {self.B}{branch}{self.RST} | "
		string += f"Local {{{self.G}{local[:7]}{self.RST}}} | "
		string += f"remote {{{self.R}{remote[:7]}{self.RST}}}"
		self.info(string)
