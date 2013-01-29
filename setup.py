from cx_Freeze import setup, Executable

setup(
    name = "PatchIt!",
    version = "1.0 Beta 2",
    description = "Standard way to create and install LEGO Racers mods.",
	author = "le717",
	license = "GNU GPLv3",
    executables = [Executable("PatchIt.py")]
)
