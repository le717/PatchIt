PatchIt! .PiP File Format
=========================

**This document has not been finalized, and the details laid out herein are subject to change.**

General Information
-------------------

In order for *PatchIt!* to install mod packs for *LEGO Racers*, it need to have some sort of patch file to read the mod information, such as name and 
description, but as well as to know what ZIP archive to extract and install into the *LEGO Racers* game files. Enter the .PiP format: a plain text file following an INI-esque design, but engineered so one can be written without the use of *PatchIt!*. This can be handy if someone has already made a *PatchIt!* patch, and need to update the mod details (they may have made a typo in the description, say), and do not want to recreate the patch from scratch.

Details
-------

* A PiP file is plain text, and can be edited on any text editor. It stands for **P**atch **I**t **P**atch.
* A PiP file is written use UTF-8 encoding.
* The ZIP archive uses the mod's name and version as the filename.
* The ZIP archive containing the modded files must be in the same folder as the .PiP file.
* As a validity test, each PiP file **must** have on line 1 a specific line of text that must match *PatchIt!*'s internal version exactly to confirm it is a valid patch.

### PiP File Format

```
// PatchIt! Patch format, created by le717 and rioforce.
[General]
Mod Name
Mod Version
Mod Creator
[Description]
Mod Description
[ZIP]
ModNameVesion.zip
```