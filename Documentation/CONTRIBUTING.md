Contributing to PatchIt!
========================

If you would like to contribute to the development of **PatchIt!**, please read this file beforehand.

Requirements
------------

### Dependencies

* **PatchIt!** is written with **[Python 3.3](http://www.python.org/download)**. You will need to have a complete installation of x86 and x64 Python `>=` 3.3.0 or later to edit and 
run **PatchIt!**. 
Python Versions `<=` 3.2 are not supported, and a version check will prevent it from running on lower versions.

* **Inno Setup 5.5.2 Unicode** or later is required to create the Windows installer. An ISPP check will prevent it on running on lower versions 
or non-Unicode Inno Setup.

* Releases are compiled into x86 and x64 Windows EXEs using **[cx_Freeze](http://cx-freeze.sourceforge.net)**. 

### Miscellaneous Notes

* No external packages or dependencies are needed for the ZIP archive functions, as they are implemented using native Python modules, namely `ZipFile` and `shutil`.

* [py2exe](http://www.py2exe.org) does not support Python 3.3, so it cannot be used.

* Because of the colored shell text added in V1.0.1 Stable, **PatchIt!** is a Windows-only application.
 
* Sometime in the development of V1.1.0 Stable a wrapper for JrMasterModelBuilder's **[JAM Extractor](https://github.com/JrMasterModelBuilder/JAM-Extractor)** 
will be added for extraction and recompressing of `LEGO.JAM`. The newest release of the JAM Extractor will be used for this purpose.

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

As mentioned above, **PatchIt!** is compiled into Windows EXE using cx_Freeze. If you would like to compile your own build of **PatchIt**, follow these steps.

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
Depending on the Python architecture, your newly created EXEs will be located at `PatchIt\Compile\Windows32` or `PatchIt\Compile\Windows64`.

* You'll also need to compile the **PatchIt! Uninstaller**. Compile it by running the following command:

```
cd PatchIt\Windows
python setup.py
```

It will be compiled to `PatchIt\Windows\Uninstaller`. **NOTE:** The **PatchIt! Uninstaller** requires Python 3.3 x86 to compile.

### Inno Setup Windows Installer

* Open `Windows\PatchIt Installer.iss` in Inno Setup.
* Make any changes to the script.

*Coming Soon.*