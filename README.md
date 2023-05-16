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
MODS={
	"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git" : (
		"WireTracer",
		"CustomWirePlacer"
	)
}
```

## TODO

1. finish updater
	1. add multiple git according to `MODS` variable
	1. disect `MODS.url.mode_name`
	1. install according to `MODS.url.mode_name` disection
