using System;
using LogicAPI;
using LogicAPI.Client;
using LogicLog;
using LICC;


namespace ModUpdater.Client
{
	public class ModUpdater : ClientMod
	{
		static string TryHelp = "Try 'mod help' for more informations.\n";

		public static IModFiles files;

		protected override void Initialize()
		{
			LConsole.WriteLine("ModUpdater initialised");
		}

		public static void cmdEmpty()
		{
			LConsole.WriteLine("mod: args needed\n" + TryHelp);
		}

		public static void cmdUnknownCmd(string cmd)
		{
			LConsole.WriteLine(
				"mod: unrecognized option '" + cmd + "'\n" + TryHelp
			);
		}

		public static void cmdHelp()
		{
			LConsole.WriteLine(
				"mod: [info|help]\n" +
				"  info\n" +
				"    List all info about available mod / repo\n\n" +
				"  help\n" +
				"    Display this help message\n"
			);
		}

		public static void cmdInfo()
		{
			foreach(var file in files.EnumerateFiles())
			{
				if(file.Path.StartsWith("repo/"))
				{
					// NOT WORKINGs
					LConsole.WriteLine("repo found: " + file.Path);
				}
			}
		}

		[Command("mod", Description = "Manage all your modz", Hidden = false)]
		public static void mod(string cmd="", string args="")
		{
			if (Config.DEBUG)
			{
				LConsole.WriteLine("mod command called");
				LConsole.WriteLine("- cmd:  " + cmd);
				LConsole.WriteLine("- args: " + args);
			}

			if (cmd.Equals(""))
				cmdEmpty();
			else if (cmd.Equals("help"))
				cmdHelp();
			else if (cmd.Equals("info"))
				cmdInfo();
			else
				cmdUnknownCmd(cmd);
		}
	}
}
