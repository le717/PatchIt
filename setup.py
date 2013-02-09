from cx_Freeze import setup, Executable

setup(
    name = "PatchIt!",
    version = "1.0 Beta 3",
    description = "The simple and standard way to create and install LEGO Racers mods.",
	author = "le717",
	license = "GNU GPLv3",
	icon = "Windows/PatchIt Icon.ico",
    executables = [Executable("PatchIt.py")]