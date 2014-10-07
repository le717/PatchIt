# PatchIt! [![Build Status](https://travis-ci.org/le717/PatchIt.svg?branch=rewrite)](https://travis-ci.org/le717/PatchIt) #

This is the readme to **PatchIt!**, a [Python 3](http://www.python.org) application written by [Triangle717](http://Triangle717.WordPress.com).

## What is PatchIt! ##
Although _LEGO&reg; Racers_ modding is still in it's early stages, many mods are already being developed, and there
needs to be a standard way to install them. Heavily influenced and based on **Patchman!**, a mod installer for
the 1999 Data Design Interactive PC game _LEGO Rock Raiders_, PatchIt! is the standard and simple way to
package and install mods for the 1999 High Voltage Software PC game _LEGO Racers_.

## How It Works ##
The three main goals for PatchIt! are as follows:

* Ask for the _LEGO Racers_ installation, ensure one exists at that location, and store it in an open file format in the PatchIt! installation
to be used as the Patch installation directory, and to create a completely portable (thumb-drive) application.
* Create a PatchIt! Patch by entering the mod name, version, author, and description, and point it to the modded files. Automatically compress the files into an open archive format (.PiA),
and write the details to an open file format (.PiP), using the name and version for the filenames.
* Install a PatchIt! Patch by selecting the .PiP file, confirming the installation, and automatically decompressing the Patch archive directly into the _LEGO Racers_ installation.

## Contributing ##
If you would like to contribute to the development of PatchIt!, please be sure to read [*CONTRIBUTING.md*](Documentation/CONTRIBUTING.md)

## Downloads ##
* Don't forget to ![Star!](http://i81.servimg.com/u/f81/16/33/06/11/star11.png)

All PatchIt! downloads are hosted on this project, and are available on the [Releases page](https://github.com/le717/PatchIt/releases).

## License ##
PatchIt!, created 2013-2014 Triangle717, and released under the [General Public License Version 3](http://www.gnu.org/licenses/gpl.html).

PatchIt makes use of [*RunAsAdmin*](https://github.com/QuantumCD/RunAsAdmin#readme), copyright :copyright: 2013
[QuantumCD](http://contingencycoder.wordpress.com/), and released under the [MIT License](http://opensource.org/licenses/MIT).
