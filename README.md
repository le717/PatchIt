PatchIt!
========

This is the readme to **PatchIt!**, a [Python 3](http://www.python.org) application written by le717 to be the standard yet simple way to
packaging and install mods for the 1999 High Voltage Software PC game *LEGO Racers*.

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on *Patchman*, a mod installer for 
the 1999 Data Design Interactive PC game *LEGO Rock Raiders*, **PatchIt!** aims to be a standard yet simple way 
to install *LEGO Racers* mods.

How It Works
------------

The three main goals for **PatchIt!** are as follows:

* Ask for the *LEGO Racers* installation, ensure one exists at that location, and store it as a plain text file in the same folder as **PatchIt!** to be used 
as the mod installation directory, and to create a completely portable (thumb-drive) application.
* Create a **PatchIt!** patch by entering the mod name, version, author, and description, and point it to the modded files. Automatically compress the files 
into a normal ZIP archive, and write the details to a plain text patch file (.PiP), using the name and version for the filenames.
* Install a **PatchIt!** patch by selecting the .PiP file, confirm the installation, and automatically decompress the ZIP archive directly into the *LEGO 
Racers* installation.

Contributing
------------

If you would like to contribute to the development of *PatchIt!*, please be sure to read [*CONTRIBUTING.md*](Documentation/CONTRIBUTING.md)

Downloads
---------

All **PatchIt!** downloads will be hosted on this project, in an [Annotated Tag](https://github.com/le717/PatchIt/tags). 

* [**PatchIt!** Version 1.0 Stable](https://github.com/le717/PatchIt/tree/V1.0Stable) - Released February ??, 2013
* [**PatchIt!** Version 1.0 Beta 2 (Unstable)](https://github.com/le717/PatchIt/tree/V1.0b2) - Released February 2, 2013
* [**PatchIt!** Version 1.0 Beta 1 (Unstable)](https://github.com/le717/PatchIt/tree/V1.0b1) - Released January 26, 2013

Credit
------
***PatchIt!* is copyright 2013 le717, and released under the GNU General Public License Version 3.**