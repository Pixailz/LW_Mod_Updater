# LW_Mod_Updater
Update mod from a repo

## HowTo

- The `Modz` class in the [run](./run) file, take two parameters
   1. `modz_folder`: the path where to install `modz`
   2. `modz`: a mod list:
- The `modz` dict is formated as the default [config.py](./config.py) file
  - a `repo_name`, must be uniq, it's contain:
    - a repo tuple with:
      1. the branch, if not provided, defaulting to `master`
      2. the link of the repo, mandatory
    - list of `modz`
      - each target is tried to be found in the `manifest.(succ|jecs)`, where:
      - `target` == `Name` THEN, `target` == `id`
- The `Modz` file clone the repo link into `.cache/repo_dev_name` if it's not found,
otherwise update if needed
- see exemple bellow

```py
# INPUT
modz_folder = "/home/pix/.local/share/Steam/steamapps/common/Logic World/GameData"
modz = {
	"Ecconia's Main repo": {
		"repo": (
			"master",
			"https://github.com/Ecconia/Ecconia-LogicWorld-Mods.git"
		),
		"modz": [
			"EccsWindowHelper",
			"AssemblyLoader",
			"WireTracer",
			"CustomWirePlacer",
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
	},
}
```

by default the script will rename all `.succ` file into `.jecs` file

used libs in [requirement.txt](./requirement.txt)
