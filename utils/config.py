# main config

import os

def get_nt_drives():
	drives = [f"{l}:\\" for l in 'CDEFGHIJKLMNOPQRSTUVWXYZ']
	for drive in drives:
		if os.path.isdir(drive):
			NT_DRIVES.append(drive)

NT_DRIVES = []

if os.name == "nt":
	get_nt_drives()

FIND_AVOID_NT = [
	"$WINDOWS.~BT",
	"$Recycle.Bin",
]

FIND_AVOID_POSIX = [
	*FIND_AVOID_NT,	# WSL Stuff
	"dev",
	"tmp",
	"run",
	"var",
	"proc"
]


def _find_folder(folder, root=os.sep, to_avoid=[]):
	if root in to_avoid:
		return None

	try:
		for path, dirs, files in os.walk(root, topdown=True):
			dirs[:] = [d for d in dirs if d not in to_avoid]

			if folder in [ os.path.basename(d) for d in dirs ]:
				return os.path.join(path, folder)

	except PermissionError as e:
		print(e)
	return None

def	find_folder_nt(folder, root=os.sep, to_avoid=FIND_AVOID_NT):
	for drive in NT_DRIVES:
		retv = _find_folder(folder, drive, to_avoid)
		if retv != None:
			return retv

def find_folder(folder, root=os.sep):
	if os.name == "nt":
		return find_folder_nt(folder, root)
	elif os.name == "posix":
		return _find_folder(folder, root, FIND_AVOID_POSIX)

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

MODZ_FOLDER = os.path.join(MODZ_FOLDER, "GameData")

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
# Rename or not succ to jecs files
RENAME_SUCC_2_JECS = True

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
