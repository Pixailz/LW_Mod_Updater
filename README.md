# LW_Mod_Updater
Update mod from a repo

## ALL LIBS

```py
import os
import re
import git
```

## DATASET EXEMPLE

```py

# INPUT
MODZ_FOLDER = "/home/pix/.local/share/Steam/steamapps/common/Logic World/GameData"
MODS={
	"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git":
	[
		"EccsWindowHelper",
		"AssemblyLoader",
		"FixClientBugs",
		"WireTracer",
		"CustomWirePlacer"
	],
	"https://github.com/GHXX/LogicWorld-TcpBridge":
	[
		"Tcp Bridge"
	]
}

# OUTPUT
{
	"EccsWindowHelper": {
		"succ":
		{
			"ID":			"EccsWindowHelper",
			"Name":			"EccsWindowHelper",
			"Author":		"Ecconia",
			"Version":		"0.4.0",
			"Priority"		"90",
			"ClientOnly"	"ClientOnly"
		},
		"dir_dst": "whats_finded"
	}
	#...
	"Tcp Bridge": {
		"succ":
		{
			"ID":			"ghxx.tcpbridge",
			"Name":			"Tcp Bridge",
			"Author":		"GHXX",
			"Version":		"1.0.0",
			"Priority"		"10",
			"ClientOnly"	"ClientOnly"
		},
	}
}
```

# TODO

1. implement it in C#
