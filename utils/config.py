# main config

import os

if os.name == "posix":
	MODZ_FOLDER = "/home/pix/.local/share/Steam/steamapps/common/Logic World/GameData"
elif os.name == "nt":
	MODZ_FOLDER = "Z:\Jeux\SteamLibrary\steamapps\common\Logic World\GameData"

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
