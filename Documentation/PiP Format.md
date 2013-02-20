PatchIt! .PiP Format
====================

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

* A PiP file is plain text. It stands for **P**atch **I**t **P**atch.
* A PiP file is written use UTF-8 encoding., and can be edited on any text editor that supports UTF-8 encoding.
* As a validity test, each PiP file **must** have on line 1 a specific line of text that **must** match **PatchIt!**'s internal version exactly to confirm it is a valid patch.
* The Description is limited to 161 characters. Anything longer will break **PatchIt!** entirely. 
* The ZIP archive and the PiP file uses the mod's name and version as the filename.

**The PiP file layout can be found below.**

* The ZIP archive containing the modded files must be in the same folder as the .PiP file.
* The ZIP archive needs to be laid out in the same way the game would use them. For example: Any TUN audio would go in the root of the archive. Anything under 
MENUDATA\ENGLISH would go under MENUDATA\ENGLISH, and so on. If your ZIP archive contains a folder that contains the files, the folder will be installed into 
the game and not the files. So, if your archive is laid out like *MyMod1.zip\MyMod1\GAMEDATA* and your game is located at *C:\Program Files\LEGO Racers*, it 
will be installed as *C:\Program Files\LEGO Racers\MyMod1\**. 
The same goes for files that are scattered in the root of the archive. If *ENGLISH.SRF* is located in the root of the archive, it will be installed to *C:\Program Files\LEGO Racer\ENGLISH.SRF*
**PatchIt!** does not and will never attempt to pull all the files from a subfolder or scattered files and attempt to install them in the proper locations. 

**An example ZIP archive layout can be found below.**

 

### PiP File Layout

```
// PatchIt! Patch format, created by le717 and rioforce.
[General]
Name
Version: Version
Author: Author
[Description]
Description
[ZIP]
NameVersion.zip
```

### Example ZIP Archive Layout

```
NameVersion.zip/
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
```
