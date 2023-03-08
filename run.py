#!/usr/bin/env python3

# TO REMOVE
from pprint import pprint
# END TO REMOVE

MODS={
	"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git" : (
		"WireTracer",
		"CustomWirePlacer"
	)
}
cache_folder=".cache/"

import os
import git

def setup():
	if os.path.isdir(cache_folder) == False:
		os.mkdir(cache_folder)

def setup_repo():
	for repo in MODS.keys():
		init_repo(repo)

def init_repo(repo_url):
	repo_folder = repo_url.split(".git")[0].split('/')[-1]
	if os.path.isdir(cache_folder + repo_folder):
		repo = git.Repo(cache_folder + repo_folder)
		pprint(repo.rev_parse('HEAD').branch)
		remote_last_commit = repo.heads.master.commit.hexsha
		local_last_commit = repo.rev_parse('HEAD').hexsha
		print(local_last_commit)
		print(remote_last_commit)
		try:
			repo.active_branch()
		except TypeError:
			print("detached branch")
		# if local_last_commit != remote_last_commit:
		# 	print("reseting to head")
		print("reseting to remote")
		repo.head.reset('origin/master', index=True, working_tree=True)
	else:
		git.Repo.clone_from(repo_url, cache_folder + repo_folder)

def main():
	setup()
	setup_repo()

main()

# if __name__ == "__main__":
# 	pprint(MODS)
