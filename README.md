PatchIt!
========

This is the readme to *PatchIt!*, a [Python 3](http://www.python.org) application written by le717 to provide a standard way of 
installing mods for the 1999 High Voltage Software PC game *LEGO Racers*.

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on *Patchman*, a mod installer for 
the 1999 Data Design Interactive PC game *LEGO Rock Raiders*, *PatchIt!* aims to be a standard yet simple way 
to install *LEGO Racers* mods.

How It Works
------------

The three main goals for *PatchIt!* are as follows:

* Ask for *LEGO Racers* installation path, ensure it exists, and store it as a plain text file in the same folder the *PatchIt!* to be used for mod 
installation, and to create a completely portable application.
* Create *PatchIt!* patches by entering the mod's name, version, description, and creator, and pointing it to the modded files. *PatchIt!* will automatically compress the files into a normal ZIP archive, and write the details to a plain text file (.PiP) using the mod's name and version as the filename.
* Install *PatchIt!* patches by selecting the .PiP file, confirming the installation, and automatically decompressing the ZIP archive directly into the *LEGO 
Racers* installation.

Requirements
------------

If you would like to contribute to the development of *PatchIt!*, please be sure you meet the system requirements.

* As already stated, *PatchIt!* is written in Python 3, 3.3.0 to be exact. You will need to have a complete installation of Python `>=` 3.3 to edit and run 
*PatchIt!* Versions `<=` Python 2.7 is not supported, and a Python version check will prevent it from running on lower versions.

* No external packages or dependencies are needed for the ZIP archive functions, as it is implemented using native Python modules.
* Beta builds and the final release will be compiled into x86 and x64 Windows EXEs using [cx_freeze](cx-freeze.sourceforge.net). [py2exe](http://www.py2exe.org)
 does not support Python 3.3, so I cannot use it.
 
* The .PiP file format documentation can be found under in [*PiP File Format.md*](https://github.com/le717/PatchIt/blob/rewrite/PiP%20File%20Format.md).

* The release goal of *PatchIt!* is to have a Beta 3 version ready for public use, although it may not completely bug free, while a proper GUI, written in Tkinter, will be released in Beta 4. Currently, there is no date set for the releases. Of course, if everything is written and completed before then, it will be released as a final 1.0 version.

***PatchIt!* is copyright 2013 le717, and released under the GNU General Public License Version 3.**