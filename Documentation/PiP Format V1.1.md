PatchIt! PiP Format V1.1
========================

**THIS DOCUMENT IS INCOMPLETE! While the format detailed in this file is mostly finalized, all details have not yet been added.**

General Information
-------------------

In order for **PatchIt!** to install mod packs for _LEGO® Racers_ or maps for _LEGO® LOCO_, it is required to have some sort of file to read the
information, such as name and description, but as well as to know what compressed archive to extract and install into the proper game files. 
In other words, a Patch file.

Enter the PiP format: an open file format engineered so one can be written without the use of **PatchIt!**, and an accompanying PiA archive containing the 
Patch files. 

This combination has been designed so a Patch can be created simply and quickly, and can be easily edited outside of **PatchIt!**. 
For example, a Patch may have already been created but there was a typo in the information, or a file was not included in the archive.
If **PatchIt!** was designed using non-easily editable formats, the user would have to go through the Patch Creation process all over again. 
However, this is not the case. By using a plain text file, the creator can open it in a text editor and correct the typo, 
or compress a new, corrected PiA archive with an external program.

Details
-------

#### PiP File Format

* PiP stands for <strong>P</strong>atch<strong>I</strong>t! <strong>P</strong>atch.
* A PiP file is a plain text file written with [`UTF-8-NOBOM`](http://en.wikipedia.org/wiki/UTF-8#Byte_order_mark) encoding, and can be edited on any text 
 editor that supports such encoding.
* As a validity test, each PiP file must have on line 1 a specific line of text (known as the validity line).
  This line ***must** match **PatchIt!**'s internal version exactly to confirm it is a valid Patch.
* In addition the the first line, the second line is also checked to determine if it is a valid Patch and what version Patch it is. 
  This line _**must**_ also match **PatchIt!**'s internal version exactly .
* Legacy (V1.0.1) Patches are detected by looking for that version's validity line. If it is found, it is installed using the Legacy Installation routine.
* Modern (V1.1) patches are the only new and supported Patches. Legacy Patches are installed only to retain backward.
 Legacy Patches can not and will not be created by **PatchIt!** anymore.  
* The `MP` (Multi Purpose) field contains various Patch info. For _LEGO® LOCO_ Patches, it contains the resolution the map was created with.
  For _LEGO® Racers_ Patches, it currently writes _MP_, as there is not a use for that game yet.
* The `Game` field tells what game a Patch was created for. It currently has two values: _LEGO® Racers_ and _LEGO® LOCO_. 
* The `Description` field is written on the last three lines of a Patch. Unlike V1.0.1, it does not have an 161 character limit.
* Both the PiP file and PiA Archive uses the Patch's name and version for their filenames.

**The PiP file layout can be found [below.](#pip-version-11-file-format-layouts)**

#### PiA Archive Layout

* PiA stands for <strong>P</strong>atch<strong>I</strong>t! <strong>A</strong>rchive.
* A PiA archive is a standard LZMA compressed TAR archive. 
* The PiA archive must reside in the same directory as it's accompanying .PiP file for a successful installation.
* The PiA archive must be laid out in the same way the intended game would use them. For example: 
  Any new _LEGO® Racers_ .TUN audio would go in the root of the archive, and any modified binary files that reside under `MENUDATA\ENGLISH` would belong in the 
  MENUDATA\ENGLISH folder in the archive, and so on. 
* If the PiA archive contains a folder that contains the laid out files rather than the files being laid out correctly, that folder will be installed into 
  the game and not into the proper locations. Example, if the archive is laid out like `MyMod1.PiA\MyMod1\GAMEDATA` and your game is located at
  `C:\Program Files\LEGO Racers`, the files will be installed as `C:\Program Files\LEGO Racers\MyMod1`. 
  The same goes for files that are scattered in the root of the archive. If `ENGLISH.SRF` is located in the root of the archive, it will be installed to 
  `C:\Program Files\LEGO Racers\ENGLISH.SRF`
* **PatchIt!** does **not and will never** attempt to install any files into their proper locations. 

**Example PiA archive layouts can be found [below.](#example-pia-archive-layouts)**

PiP Version 1.1 File Format Layouts
-----------------------------------

### General PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[PiA]
NameVersion.PiA
[GENERAL]
Author
Version
Name
MP
Game
[DESCRIPTION]
This is the first line of a description
This is the second line of a description
This is the third line of a description
```

### Example LEGO® Racers PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[PiA]
Racing Machine 1.0.1.PiA
[GENERAL]
Jackson
1.0.1
Racing Machine
MP
LEGO Racers
[DESCRIPTION]
Racing Machine is a example LEGO Racers PatchIt! Patch
It does not exist, and unless someone makes it,
IT NEVER WILL. :)
```


### Example LEGO® LOCO PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[PiA]
Happy Trains 5.8.PiA
[GENERAL]
Thomas
5.8
Happy Trains
1920x1280
LEGO LOCO
[DESCRIPTION]
I like trains! I really do!
My name is Thomas, just like Thomas the Tank Engine!
That is why I made this example PatchIt! Patch.
```

Example PiA Archive Layouts
---------------------------

### Example LEGO® Racers PiA Archive Layout ###

```
Racing Machine 1.0.1.PiA/
    GAMEDATA/
        RACEC2R0/
			KMT.BMP
			BACKGRND.SKB
		COMMON/
			LIGHTNG.TGA
			POWERUP.WDB
    MENUDATA/
		ENGLISH/
			FONTMENU.BMP
			MENUTEXT.SRF
        KEYBOARD.BMP
		MAINMENU.MIB
    theme.tun
	builder.tun
```

### Example LEGO® LOCO PiA Archive Layout ###

```
Happy Trains 5.8.PiA/
    art-res/
        backdrop/
			HappyTrain.bmp
			AngryTrain.bmp
		video/
			music.wav
        SAVEGAME/
            HappyTrain.sav
            AngryTrain.sav
    Video/
		locoIntr.avi
```

Revision History
----------------

* 1.1.1 Draft 2: July 4, 2013

> * Reworded sections of PiP File Format section
> * Updated PiA Archive Layout section with new details
> * Finished updating PiA Archive Layout section
> * Changed `[ZIP]` header to `[PiA]` now serves as part of the validity check

* 1.1.1 Draft 1: June 17, 2013

> * Changed ZIP archive to use _.PiA_ extension
> * Updated examples with _.PiA_ extension

* 1.1 Final: May 16, 2013

> * Finished PiP Format 1.0 history
> * Minor text improvements

* 1.1 Final: May 11, 2013 

> * Updated General Information section
> * Updated PiP File Format section

* 1.1 Final: April 14, 2013

> * Finalized PiP Format 1.1 
> * Added description of `MP` and `Game` fields
> * Added example LEGO LOCO and LEGO Racers PiP Patches

* 1.1 Draft 3 r1: April 6, 2013

> * Renamed `Mod Type` field to `MP` (Multi Purpose) field.

* 1.1 Draft 3: March 16, 2013

> * Added `Game` field, re-purposing of `Mod Type` field

* 1.1 Draft 2: March 5 & 6, 2013

> * Added `Mod Type` field, outlined in [PatchIt! Dev-log #8](http://wp.me/p1V5ge-JN)

* 1.1 Draft 1: March 3, 2013

> * Rewrite of format, outlined in [PatchIt! Dev-log #5](http://wp.me/p1V5ge-yl)

* 1.0.1: February 20, 2013

> * Added example ZIP Archive layout
> * Updated to address 161 character limit in `Description` field

* 1.0: February 18, 2013

> * Added ZIP Archive section
> * Finalized PiP Format

* Draft 3: February 15, 2013

> * Renamed `Creator` field to `Author`

* Draft 2: February 8, 2013

> * Updated validity line
> * Removed `[Misc]` header, moved `Version` field below `Name` field
> * Added PiP File Format Details

* Draft 1: February 2, 2013

> * First design
