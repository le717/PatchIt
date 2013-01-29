PatchIt! Readme
===============

This is the readme to *PatchIt!*, a Python 3 application written by le717 to provide a standard way of 
installing mods for the 1999 High Voltage Software PC game *LEGO Racers*.

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on *Patchman*, a mod installer for 
the 1999 Data Design Interactive PC game *LEGO Rock Raiders*, *PatchIt!* aims to be a standard yet simple way 
to install *LEGO Racers* mods.

How It Works
------------

The three main goals for *PatchIt!*, along with a brief explanation, are as follows:

* Create  *PatchIt!* patches by entering the mod's name, version, and creator, and pointing it to the modded files. *PatchIt!* will automatically compress the 
files into a normal ZIP archive, and write the details to a plain text file ( * .PiP) using the mod's name and version as the filename.
* Install *PatchIt!* patches by selecting the * .PiP file, confirming the installation, and automatically decompressing the ZIP archive directly into the *LEGO Racers* installtion.