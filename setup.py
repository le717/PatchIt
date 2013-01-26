from cx_Freeze import setup, Executable

setup(
    name = "LEGO Racers Nyan Cat-Athon Mod",
    version = "Unknown",
    description = "Compressed with LEGO Racers Mod Installer by le717",
	author = "JimbobJeffers and le717",
	license = "GNU GPLv3",
    executables = [Executable("LRModInstaller.py")]
)
