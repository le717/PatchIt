Contributing to PatchIt!
========================

If you would like to contribute to the development of **PatchIt!**, please read this file beforehand.

Requirements
------------

### Dependencies

* Download and install 32-bit [*Python 3.3.0*](http://python.org/download) or newer.
Python Versions `<=` 3.2 or 64-bit Python are not supported, and a Python version (not architecture) check will prevent it from running on lower versions.

* Download and install [*cx_Freeze*](http://cx-freeze.sourceforge.net/) for 32-bit *Python 3.3* if you would like to freeze a binary.

* Download and install [*Inno Setup 5.5.2 Unicode*](http://www.jrsoftware.org/isdl.php) or later if you would like to compile the Windows installer.
An ISPP check will prevent it on running on lower versions or ANSI Inno Setup.

### Editing

* Fork the **PatchIt!** repository by clicking ![the Fork button](http://i81.servimg.com/u/f81/16/33/06/11/forkme12.png)
* Clone **PatchIt!** onto your computer by running ```git clone https://github.com/yourusername/PatchIt.git```
* Read up on the documentation (see [**For Your Reading Pleasure**](#for-your-reading-pleasure) below)
* Edit away! Write a GUI, fix bugs, add new features, whatever is reasonable!
* Once you finish your work, submit a [Pull Request](https://github.com/le717/PatchIt/pulls) by clicking ![the Pull Request button](http://i81.servimg.com/u/f81/16/33/06/11/pullre10.png)
* If everything checks out, your changes will be merged into the main **PatchIt!** project! :grinning:
* Don't forget to ![Star!](http://i81.servimg.com/u/f81/16/33/06/11/star11.png)

### Miscellaneous Notes

* No external packages or dependencies are needed for the TAR archive functions, as it is implemented using the built-in `tarfile` Python module.

* [py2exe](http://www.py2exe.org) does not support Python 3.3, so it cannot be used.

* Because of the colored shell text added in V1.0.1 Stable, **PatchIt!** is a Windows-only application.
 
* Sometime in the development of the V1.1.x series, a wrapper for **@JrMasterModelBuilder**'s **[JAM Extractor](https://github.com/JrMasterModelBuilder/JAM-Extractor)** 
will be added for extraction and recompressing of `LEGO.JAM`. The newest release of the **JAM Extractor** will be used for this purpose.

For Your Reading Pleasure
-------------------------

* A (incomplete) of everything that needs to be done can be found under [*TODO.md*](https://github.com/le717/PatchIt/blob/rewrite/Documentation/TODO.md).
* The WIP PiP format V1.1 documentation can be found in [*PiP Format V1.1.md*](PiP%20Format%20V1.1.md).
* The PiP format V1.0.1 documentation can be found in [*PiP Format.md*](PiP%20Format.md).
* Check any open [Issues](https://github.com/le717/PatchIt/issues), as they commonly contain bug reports or errors.
* A goal of **PatchIt!** is to have a complete GUI to replace the command-line style. However, the GUI has been put on hold 
until futher notice. If you have experence in PyQt4/5 or Tkinter and would like to help out in this area, you would be hardly be turned down . :wink:

Building PatchIt!
-----------------

### Windows EXEs

**PatchIt!** is frozen into an x86 Windows Exe using cx_Freeze. If you would like to freeze your own build of **PatchIt!**, follow these steps.

* Follow the steps for forking/cloning **PatchIt!** from [above](#editing).

* Type the following command in a command prompt:

```
cd PatchIt
python setup.py
```
Your newly frozen Exe will be located at `PatchIt\Freeze\Windows`.

* You'll also need to freeze the **PatchIt! Uninstaller**. Compile it by running the following command:

```
cd PatchIt\Windows
python setup.py
```

It will be frozen to `PatchIt\Windows\Uninstaller`.

### Inno Setup Windows Installer

* Open `Windows\PatchIt Installer.iss` in the Inno Setup Compiler.
* Make desired changes to the script, as long as it is clear you made them.
* Ensuring **PatchIt!** and the **PatchIt! Uninstaller** is already frozen, and the required empty __LEGO® Racers__ and __LEGO® LOCO__ settings files
are in place, press the Compile button or `&lt;Ctrl&gt; + &lt;F9&gt;` to compile the installer.
* If all goes well, you will have sucessfully frozen and packaged a copy of **PatchIt!**