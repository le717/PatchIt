PatchIt! Settings Files
=======================

Details
-------

* The **PatchIt!** Settings files contains all the required info to install a Patch to the proper location.
* The Settings files are written using [`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding, and can be edited in any editor that supports such encoding.
* The _Settings_ folder, in which the Settings files are saved, is located in the same directory as `PatchIt.exe`.
* Data for each game **PatchIt!** support is saved in a separate `.cfg` in the _Settings_ folder
* Each file uses the name of the supported game (except for the word `LEGO`). 
* The third line of the Settings files defines the current state of the first-run check. In a fresh installation of **PatchIt!**,
the number is `0` (zero), meaning the settings have not been set up. After a game installation is selected, the number is changed to `1`, 
meaning no action is needed.
* The fifth line of the _LEGO Racers_ settings contains the game's version release. It has two values: `1999` and `2001`. 
It detects the version by checking for the existence of `LEGORacers.icd`, which is present only in the 1999 release.
There is no such check for _LEGO LOCO_.
* The seventh line contains the installation patch for the respective game. It is used during Patch Installation, as well as in
various Settings checks.

LEGO Racers Settings
----------------------------

* File name: _**Racers.cfg**_

```
// PatchIt! V1.1.x LEGO Racers Settings
# Ensures the first-run process will be skipped next time
1
# Your version of LEGO Racers
2001
# Your LEGO Racers installation path
C:/Program Files (x86)/LEGO Media/Games/LEGO Racers
```

LEGO LOCO Settings
--------------------------

* File name: _**LOCO.cfg**_

```
// PatchIt! V1.1.x LEGO LOCO Settings
# Ensures the first-run process will be skipped next time
1
# Your LEGO LOCO installation path
C:/Program Files/LEGO Media/LEGO LOCO
```