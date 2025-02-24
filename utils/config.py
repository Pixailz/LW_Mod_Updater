# main config

import os

def find_folder(folder, root="/"):
	TO_AVOID = [
		"$WINDOWS.~BT",
		"$Recycle.Bin"
		"dev",
		"tmp",
		"run"
		"var"
	]

	try:
		for path, dirs, files in os.walk(root, topdown=True):
			dirs[:] = [d for d in dirs if d not in TO_AVOID]

			if folder in [ os.path.basename(d) for d in dirs ]:
				return os.path.join(path, folder)

	except PermissionError as e:
		print(e)
	return None

MODZ_FOLDER_PATH = os.path.abspath(
	os.path.join(__file__, os.pardir, "FOUNDED_MODZ_FOLDER")
)

if os.path.isfile(MODZ_FOLDER_PATH):
	with open(MODZ_FOLDER_PATH, "r") as f:
		MODZ_FOLDER = f.read()
else:
	print("Searching for the 'Logic World' main folder")
	MODZ_FOLDER = find_folder("Logic World")
	if MODZ_FOLDER is None:
		print("Error 'Logic World' folder could not be found")
		exit(1)
	print(f"Found at {MODZ_FOLDER}")
	with open(MODZ_FOLDER_PATH, "w") as f:
		f.write(MODZ_FOLDER)

MODZ_FOLDER += "GameData"

MODZ = {
	"Ecconia's Main repo": {	# repo_name
		"repo": (
			"master",
			"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git"
		),
		"modz": [
			"HarmonyForLogicWorld",			# mandatory for gui thing
			"AssemblyLoader",				#
			"EccsGuiBuilder",				#
			"EccsLogicWorldAPI",			#

			"WireTracer",					# extra
			"CustomWirePlacer",				#
			"RandomDebugCollection",		#
			"DisableCollision",				#

			"EcconiaCPUServerComponents",	# extra ++
			"EcconiasChaosClientMod",		#
		]
	},
	"GHXX's Main repo": {
		"repo": (
			"master",
			"https://github.com/GHXX/LogicWorld-TcpBridge"
		),
		"modz": [
			"Tcp Bridge"
		]
	}
}
# where the cache are stored
GIT_CACH_DIR = ".cache"
# LOG
## padding for the level
LOG_PAD_STR = "   "
## set loging level
### -2 disable
### -1 all
### from here N contain M < N
### 0 main title
### 1 some info
### 2 finded manifest.succ, local | remote commit id from cache
### 3 succ info
LOG_DEB_LVL = 2
