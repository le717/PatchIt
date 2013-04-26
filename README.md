PatchIt!
========

![](https://raw.github.com/le717/PatchIt/master/Icons/PatchItLogo.png?raw=true)

This is the readme to **PatchIt!**, the standard and simple way to package and install mods for the 1999 High Voltage Software PC game *LEGO Racers*, written 
purely in [Python 3](http://www.python.org).

The Plan
--------

Although *LEGO Racers* modding is still in it's early stages, many mods are already being developed, and there 
needs to be a standard way to install them. Heavily influenced and based on **Patchman**, a mod installer for 
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

If you would like to contribute to the development of **PatchIt!**, please be sure to read [*CONTRIBUTING.md*](Documentation/CONTRIBUTING.md)

The current Travis CI build for the `rewrite` is:

[![Build Status](https://travis-ci.org/le717/PatchIt.png)](https://travis-ci.org/le717/PatchIt)

(If the build status reports failed, that is incorrect. There is code Travis CI does not support, thus declaring fail. ;))

Downloads
---------

All **PatchIt!** downloads are hosted on this project, each one in a separate [Annotated Tag](https://github.com/le717/PatchIt/tags). 

* **PatchIt!** Version 1.0.3 Stable - Released March 11, 2013 

> [Source Code](https://github.com/le717/PatchIt/tree/V1.0.3Stable)

> [Direct Download](https://github.com/le717/PatchIt/raw/V1.0.3Stable/Windows/PatchIt!%20Version%201.0.3%20Stable.exe)

* **PatchIt!** Version 1.0.2 Stable - Released March 5, 2013

> [Source Code](https://github.com/le717/PatchIt/tree/V1.02Stable)

> [Direct Download](https://github.com/le717/PatchIt/raw/V1.02Stable/Windows/PatchIt!%20Version%201.0.2%20Stable.exe)

* **PatchIt!** Version 1.0.1 Stable - Released March 2, 2013

> [Source Code](https://github.com/le717/PatchIt/tree/V1.0.1Stable)

> [Direct Download](https://github.com/le717/PatchIt/raw/V1.0.1Stable/Windows/PatchIt!%20Version%201.0.1%20Stable.exe)

* **PatchIt!** Version 1.0 Stable - Released February 21, 2013

> [Source Code](https://github.com/le717/PatchIt/tree/V1.0Stable)

> [Direct Download](https://github.com/le717/PatchIt/raw/V1.0Stable/Windows/PatchIt!%20Version%201.0%20Stable.exe)

* **PatchIt!** Version 1.0 Beta 2 (Unstable) - Released February 2, 2013

> [Source Code](https://github.com/le717/PatchIt/tree/V1.0b2)

* **PatchIt!** Version 1.0 Beta 1 (Unstable) - Released January 26, 2013

> [Source Code](https://github.com/le717/PatchIt/tree/V1.0b1)

Credit
------
***PatchIt!* is created 2013 Triangle717, and released under the GNU General Public License Version 3.**
