PatchIt!
========

This is the readme to **PatchIt!**, a [Python 3](http://www.python.org) application written by le717 to provide a standard way of 
installing mods for the 1999 High Voltage Software PC game *LEGO Racers*.

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on *Patchman*, a mod installer for 
the 1999 Data Design Interactive PC game *LEGO Rock Raiders*, **PatchIt!** aims to be a standard yet simple way 
to install *LEGO Racers* mods.

How It Works
------------

The three main goals for **PatchIt!** are as follows:

* Ask for *LEGO Racers* installation path, ensure it exists, and store it as a plain text file in the same folder the **PatchIt!** to be used for mod 
installation, and to create a completely portable application.
* Create **PatchIt!** patches by entering the mod's name, version, description, and creator, and pointing it to the modded files. **PatchIt!** will automatically compress the files into a normal ZIP archive, and write the details to a plain text file (.PiP) using the mod's name and version as the filename.
* Install **PatchIt!** patches by selecting the .PiP file, confirming the installation, and automatically decompressing the ZIP archive directly into the *LEGO 
Racers* installation.

Contributing
------------

If you would like to contribute to the development of *PatchIt!*, please be sure to read [*CONTRIBUTING.md*](Documentation/CONTRIBUTING.md)

Downloads
---------

All **PatchIt!** downloads will be hosted on this project, in an [Annotated Tag](https://github.com/le717/PatchIt/tags). 

So far, there have been two releases:

* [**PatchIt!** Version 1.0 Beta 2 (Unstable)](https://github.com/le717/PatchIt/tree/V1.0b2) - Released  February 2, 2013
* [**PatchIt!** Version 1.0 Beta 1 (Unstable)](https://github.com/le717/PatchIt/tree/V1.0b1) - Released  January 26, 2013

Credit
------
***PatchIt!* is copyright 2013 le717, and released under the GNU General Public License Version 3.**