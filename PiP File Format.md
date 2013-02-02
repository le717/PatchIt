PatchIt! .PiP File Format
===========================

Information
-----------

In order for *PatchIt!* to install mod packs for *LEGO Racers,*, it need to have some sort of patch file to read the mod information, such as name and 
description, but as well as to know what ZIP file to extract and install into the *LEGO Racers* game files. Enter the .PiP format: a plain text file following an 
INI-esque design, but engineered so one can be written without the use of *PatchIt!*. This can be handy if someone has already made a *PatchIt!* patch, and need 
to update the mod details (they may have made a typo in the description, say), and do not want to recreate the patch from scratch.

Details
-------

* A PiP file is plain text, and can be edited on any text editor. It stands for *Patch*it*Patch*.

* File layout

```
[General]
Mod Name
Mod Creator
[Description]
Mod Description
[Misc.]
Mod Version
[ZIP]
ZIP file with modded files
```