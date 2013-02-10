from cx_Freeze import setup, Executable

setup(
    name = "PatchIt!",
    version = "1.0 Beta 3",
    description = "The simple and standard way to distribute and install LEGO Racers mods.",
	author = "le717",
	license = "GNU GPLv3",
	icon = "Icons/PatchIt Icon.ico",
    executables = [Executable("PatchIt.py")]
