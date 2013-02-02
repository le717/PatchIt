from cx_Freeze import setup, Executable

setup(
    name = "PatchIt!",
    version = "1.0 Beta 1",
    description = "The simple and standard way to create and install LEGO Racers mods.",
	author = "le717",
	license = "GNU GPLv3",
    executables = [Executable("PatchIt.py")]
)
