Contributing to PatchIt!
========================

If you would like to contribute to the development of **PatchIt!**, please read this file beforehand.

Requirements
------------

### Dependencies ###

* Download and install 32-bit [_Python 3.3.0_](http://python.org/download) or newer. All official releases are frozen with the newest release at that time.
Python Versions `<=` 3.2 Python are not supported, and a Python version check will prevent it from running on lower versions.

* Download and install [_cx_Freeze_](http://cx-freeze.sourceforge.net/) for 32-bit _Python 3.3_ if you would like to freeze a binary. 64-bit Windows binaries 
are not support or frozen, and architecture checks will prevent this from happening.

* Download and install [_Inno Setup 5.5.2 Unicode_](http://www.jrsoftware.org/isdl.php) or later if you would like to compile the Windows installer.
An ISPP check will prevent it on running on lower versions or ANSI Inno Setup.

* A slightly edited version of [@JrMasterModelBuilder](https://github.com/JrMasterModelBuilder)'s **[JAM Extractor](https://github.com/JrMasterModelBuilder/JAM-Extractor)**
for extracting and compressing `LEGO.JAM`.

* The newest release of **[wget](https://bitbucket.org/techtonik/python-wget/overview)**, already present at `Tools/wget/wget.py`

### Editing ###

* Fork the **PatchIt!** repository by clicking ![the Fork button](http://i81.servimg.com/u/f81/16/33/06/11/forkme12.png)
* Clone **PatchIt!** onto your computer by running ```git clone https://github.com/yourusername/PatchIt.git```
* Read up on the documentation (see [**For Your Reading Pleasure**](#for-your-reading-pleasure) below)
* Edit away! Write a GUI, fix bugs, add new features, whatever is reasonable!
* Once you finish your work, submit a [Pull Request](https://github.com/le717/PatchIt/pulls) by clicking ![the Pull Request button](http://i81.servimg.com/u/f81/16/33/06/11/pullre10.png)
* Because of my lack of knowledge of how Git worked when **PatchIt!** was created, the [`rewrite`](https://github.com/le717/PatchIt/tree/rewrite) branch, where all future versions are developed, can never be merged
into the [`master`](https://github.com/le717/PatchIt/tree/master) branch, where all tagged releases are located. For this reason, please base all changes against the `rewrite` branch.
* Also because of my cluelessness into the workings of Git, all changes from the `rewrite` branch must manually be added to the `master` branch when a release is to be tagged, as a pull request would greatly break the entire repository.
I am sorry for any inconvenience this may cause.
* If everything checks out, your changes will be merged into the main **PatchIt!** project! :grinning:
* Don't forget to ![Star!](http://i81.servimg.com/u/f81/16/33/06/11/star11.png)

### Miscellaneous Notes ###

* No external packages or dependencies are needed for the TAR archive functions, as it is implemented using the built-in `tarfile` Python module.

* [py2exe](http://www.py2exe.org) does not support Python 3.3, so it cannot be used.

* Because of the colored shell text added in [**v1.0.1 Stable**](https://github.com/le717/PatchIt/releases/tag/V1.0.1Stable), **PatchIt!** is a Windows-only application.

For Your Reading Pleasure
-------------------------

* A (incomplete) of everything that needs to be done can be found under [*TODO.md*](https://github.com/le717/PatchIt/blob/rewrite/Documentation/TODO.md) and [Issues](https://github.com/le717/PatchIt/issues).
* The WIP PiP format V1.1 documentation can be found in [*PiP Format V1.1.md*](PiP%20Format%20V1.1.md).
* The PiP format V1.0.1 documentation can be found in [*PiP Format.md*](PiP%20Format.md).
* Open [Issues](https://github.com/le717/PatchIt/issues) also commonly contain bug reports or errors.
* A goal of **PatchIt!** is to have a complete GUI to replace the command-line style. However, the GUI has been put on hold
until further notice. If you have experience in PyQt4 or PyQt5 and would like to help out in this area, you would be hardly be turned down . :wink:

Building PatchIt!
-----------------

### Windows ###

**PatchIt!** is frozen into an x86 Windows Exe using cx_Freeze. If you would like to freeze your own build of **PatchIt!**, follow these steps.

* Follow the steps for forking/cloning **PatchIt!** from [above](#editing).

* Type the following command in a command prompt window:

```
cd PatchIt
python setup.py
```
Your newly frozen Exe will be located at `PatchIt\bin\Windows`. Not only will this freeze **PatchIt!**, it will download the newest version of the Readme from 
the [`gh-pages`](https://github.com/le717/PatchIt/tree/gh-pages) branch (skipping this step if it could not be downloaded at that time), remove any unnecessary 
Tkinter files, and finally freeze the **PatchIt! Uninstaller**.

* You'll also need to freeze the **PatchIt! Uninstaller**. Do this by running the following command:

```
cd PatchIt\Tools\Uninstaller
python setup.py
```

It will be frozen to `PatchIt\Tools\Uninstaller\bin`.

### Inno Setup Windows Installer ###

* Open `Windows\PatchIt Installer.iss` in the Inno Setup Compiler.
* Make desired changes to the script, as long as it is clear you made them.
* Ensuring **PatchIt!** and the **PatchIt! Uninstaller** is already frozen, and the required empty __LEGO® Racers__ and __LEGO® LOCO__ settings files
are in place, press the Compile button or &lt;Ctrl&gt; + &lt;F9&gt; to compile the installer to the `Windows` folder.
* If all goes well, you will have successfully frozen and packaged a copy of **PatchIt!**
