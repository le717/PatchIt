PatchIt! Settings Files
=======================

Details
-------

* The **PatchIt!** Settings files contains all the required info to install a Patch to the proper location.
* The Settings files are written using UTF-8 encoding, and can be edited in any editor that supports UTF-8 encoding.
* The third line of the Settings files defines the current state of the first-run check. In a fresh installation of **PatchIt!**,
  the number is `0` (zero), meaning the settings have not been set up. After a game installation is selected, the number is changed to `1`, 
  meaning it is complete.
* The fifth line contains the version of *LEGO Racers* the user in installing mods to. It has two values: '1999' and '2001'. 
  It comes to this conclusion by checking for the existence of `LEGORacers.icd`, which is present only in the 1999 release.
* The *Settings* folder, in which the Settings files are saved, is located in the same directory as `PatchIt.exe`.
* Data for each game **PatchIt!** support is saved in a separate `.cfg` in the *Settings* folder
* Each file uses the name of the supported game (sans LEGO). 

Example LEGO Racers Settings
----------------------------

* File name: ***Racers.cfg***

```
// PatchIt! V1.1.x LEGO Racers Settings
# Ensures the first-run process will be skipped next time
1
# Your version of LEGO Racers
2001
# Your LEGO Racers installation path
C:/Program Files (x86)/LEGO Media/Games/LEGO Racers
```

Example LEGO LOCO Settings
--------------------------

* File name: ***LOCO.cfg***

```
// PatchIt! V1.1.x LEGO LOCO Settings
# Ensures the first-run process will be skipped next time
1
# Your LEGO LOCO installation path
C:/Program Files/LEGO Media/LEGO LOCO
```
