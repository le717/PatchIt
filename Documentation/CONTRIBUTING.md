Contributing to PatchIt!
========================

If you would like to contribute to the development of **PatchIt!**, please read this file beforehand.

Requirements
------------

* **PatchIt!** is written in Python 3.3. You will need to have a complete installation of Python `>=` 3.3.0 to edit and run *PatchIt!*. 
Python Versions `<=` 3.2 are not supported, and a version check will prevent it from running on lower versions.
* No external packages or dependencies are needed for the ZIP archive functions, as they are implemented using native Python modules.
* Beta builds and the final release will be compiled into x86 and x64 Windows EXEs using [cx_freeze](http://cx-freeze.sourceforge.net). 
[py2exe](http://www.py2exe.org) does not support Python 3.3, so it cannot be used.
* Because of the colored shell text added in V1.0.1 Stable, **PatchIt!** is a Windows-only application.

Where to Start
--------------

* A (incomplete) of everything that needs to be done can be found under [*TODO.md*](https://github.com/le717/PatchIt/blob/rewrite/Documentation/TODO.md).
 
* The PiP format V1.0.1 documentation can be found in [*PiP Format.md*](PiP%20Format.md).

* The WIP PiP format V1.1 documentation can be found in [*PiP Format V1.1.md*](PiP%20Format%20V1.1.md).

* A goal of **PatchIt!** is to have a complete Tkinter GUI for in a future version (originally Version 1.1.0 Stable). However, the GUI has been put on hold 
until futher notice.

Building PatchIt!
-----------------

### Windows EXEs

As mentioned above, **PatchIt!** is compiled into Windows EXE using cx_freeze. If you would like to compile your own build of **PatchIt**, follow these steps.

* Clone the **PatchIt!** Git repository by typing the following command:

```
git clone git://github.com/le717/PatchIt.git
```
Replace *master* with the branch or tagged release you wish to download.

* Type the following command in a command prompt:
```
cd PatchIt
python setup.py
```
Depending on the Python architecture, your newly created EXEs will be located at either *PatchIt\Compile\Windows32* 
or under *PatchIt\Compile\Windows64*. 

### Inno Setup installer