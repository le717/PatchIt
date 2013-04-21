PatchIt! TODO List
==================

An (incomplete) list of everything that needs to be done in **PatchIt!**, listed in no particular order, as well as new, upcoming features and current bugs.

* **BUG** Why do some Shell Colors keep breaking?
* **BUG** Sometimes Patch cannot be saved in a Dropbox folder
* *NEW!* Automatic LEGO.JAM extraction (upon user approval)
* *NEW!* Complete Tkinter GUI (postponed until later release)
* *NEW!* Cross-platform Compatibility (not until GUI, shell colors are Windows-only)
* IDEA? *.PiP file shell registration. If user clicks a PiP file, it will automatically load **PatchIt** and run the Patch Installation module.
At first, could be added via the Inno Setup installer only, maybe later activated by command-line parameter, and finally a (possible) check in preload(), and 
a prompt to register it if not. Naturally, Windows-only. Last idea could break goal 3 of **PatchIt!**, might require a cfg for **PatchIt!** settings only.s
* Refer to JAM Extractor 1.0.2 for command-line arguments, possibly replace argparse with a form of that in case I cannot make 
an optional argument that requires a positional argument (although this [code](http://stackoverflow.com/a/13706448) might just work...))
* Write Inno Setup Installer directions
* Write PiP Format V1.0.1 Revision History
* Any TODO items scattered around in any of the scripts