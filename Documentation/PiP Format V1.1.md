PatchIt! PiP Format
====================

**THIS DOCUMENT IS INCOMPLETE! While the file format outlined in this document is final, complete documentation has yet to be written.**

General Information
-------------------

In order for **PatchIt!** to install mod packs for *LEGO Racers*, it need to have some sort of patch file to read the mod information, such as name and 
description, but as well as to know what ZIP archive to extract and install into the *LEGO Racers* game files. Enter the .PiP format: a plain text file 
following an INI-esque design, but engineered so one can be written without the use of **PatchIt!**, and an accompanying standard ZIP archive containing the 
mod files. This combination has been designed so a patch can be created simply and quickly, and can be easily edited outside of **PatchIt!**. For example, a 
patch may have already been created but there was a typo in the information, or a file was not included in the archive. If **PatchIt!** was designed using 
non-easily editable formats, the user would have to go through the patch creation process all over again. However, this is not the case. By using a plain text 
file, they can open it in a UTF-8 supported text editor and correct the typo, or compress a new, corrected ZIP archive with an external program.

Details
-------

#### PiP File Format

* A PiP file is plain text. It stands for **P**atch **I**t **P**atch.
* A PiP file is written use UTF-8 encoding, and can be edited on any text editor that supports UTF-8 encoding.
* As a validity test, each PiP file **must** have on line 1 a specific line of text (known as the validity line) 
that **must** match **PatchIt!**'s internal version exactly to confirm it is a valid patch.
* Legacy (V1.0.1) patches are determined by lookin for that version's validity line, and if found, is installed using the legacy installation method.
* Only Modern (post-V1.0.1) patches are written. Legacy patches are installed only for backward compatibility purposes. Legacy Patches are not and will not be 
written anymore.  
* The *MP* ( **M** ulti **P** urpose) field contains various Patch info. For *LEGO LOCO* Patches, it contains the resolution the map was created with.
For *LEGO Racers* Patches, it currently writes *MP*, as there is not a vaild input for that game yet.
* The *Game* field tells what game a Patch was created for. It currently has two values: *LEGO Racers* and *LEGO LOCO*. 
* The Description of the mod is written on the last three lines. Unlike V1.0.1, this layout does not have an 161 character limit.
* The ZIP archive and the PiP file uses the mod's name and version as the filename.

**The PiP file layout can be found [below.](#pip-version-11-file-format-layouts)**

#### PiP ZIP Archive Layout

* The ZIP archive containing the modded files must be in the same folder as the .PiP file.
* The ZIP archive needs to be laid out in the same way the game would use them. For example: Any TUN audio would go in the root of the archive. Anything under 
MENUDATA\ENGLISH would go under MENUDATA\ENGLISH, and so on. If your ZIP archive contains a folder that contains the files, the folder will be installed into 
the game and not the files. So, if your archive is laid out like *MyMod1.zip\MyMod1\GAMEDATA* and your game is located at *C:\Program Files\LEGO Racers*, it 
will be installed as *C:\Program Files\LEGO Racers\MyMod1\**. 
The same goes for files that are scattered in the root of the archive. If *ENGLISH.SRF* is located in the root of the archive, it will be installed to 
*C:\Program Files\LEGO Racer\ENGLISH.SRF*
**PatchIt!** does not and will never attempt to pull all the files from a subfolder or scattered files and attempt to install them in the proper locations. 

**Example ZIP archive layouts can be found [below.](https://github.com/le717/PatchIt/edit/rewrite/Documentation/PiP%20Format%20V1.1.md#example-zip-archive-layouts)**

PiP Version 1.1 File Format Layouts
-----------------------------------

### General PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[ZIP]
NameVersion.zip
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

### Example LEGO Racers PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[ZIP]
Racing Machine 1.0.1.zip
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


### Example LEGO LOCO PiP File Format Version 1.1 Layout

```
// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[ZIP]
Happy Trains 5.8.zip
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

Example ZIP Archive Layouts
---------------------------

### Example LEGO Racers ZIP Archive Layout

```
Racing Machine 1.0.1.zip/
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

### Example LEGO LOCO ZIP Archive Layout

```
Happy Trains 5.8.zip/
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

* 1.1 Final : April 14, 2013

> * Finalized PiP Format 1.1 
> * Added description of MP and Game fields
> * Added example LEGO LOCO and LEGO Racers PiP Patches

* 1.1 Draft 3 r1: April 6, 2013

> * Renamed Mod Type field to MP ('M'ulti-'P'urpose) field.

* 1.1 Draft 3: March 16, 2013

> * Added Game field, re-purposing of Mod Type field

* 1.1 Draft 2: March 5 & 6, 2013

> * Added Mod Type field, outlined in [PatchIt! Dev-log #8](http://wp.me/p1V5ge-JN)

* 1.1 Draft 1: March 3, 2013

> * Rewrite of format, outlined in [PatchIt! Dev-log #5](http://wp.me/p1V5ge-yl)

* 1.0.1: February 20, 2013

> * Coming Soon

* 1.0: February 18, 2013

> * Coming Soon

* Draft 3: February 15, 2013

> * Coming Soon

* Draft 2: February 8, 2013

> * Coming Soon

* Draft 1: February 2, 2013

> * First design
