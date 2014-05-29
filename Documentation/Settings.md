# PatchIt! Settings Files #

## Details ##

* The **PatchIt!** Settings files contains all the required info to install a Patch to the proper location.
* The Settings files are written using [`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding, and can be edited in any editor that supports such encoding.
* The _Settings_ folder, in which the Settings files are saved, is located in the same directory as `PatchIt.exe` and use the `.json` extension.
* The third line of the settings files (namely, `Racers.json`) defines the current state of the first-run check. In a fresh installation of **PatchIt!**,
the number is `0` (zero), meaning the settings have not been set up. After th game installation is selected, the number is changed to `1`,
meaning no action is needed.
* The fifth line of the settings file contains the game's version release. It has two values: `1999` and `2001`.
It detects the version by checking for the existence of `LEGORacers.icd`, which is present only in the 1999 release.
* The seventh line contains the installation path for the game. It is used during Patch Installation, as well as in
various Settings checks.
* The third line of `PatchIt.json` contain the major, minor, patch and build numbers of the **PatchIt!** version being used.

## General PatchIt! Settings ##

* File name: _**PatchIt.json**_

```
// PatchIt! General Settings
# The version of PatchIt! you have
1.1.2 Unstable Build 217
```

## LEGO Racers Settings ##

* File name: _**Racers.json**_

```
// PatchIt! V1.1.x LEGO Racers Settings
# Ensures the first-run process will be skipped next time
1
# Your version of LEGO Racers
2001
# Your LEGO Racers installation path
C:/Program Files (x86)/LEGO Media/Games/LEGO Racers
```
