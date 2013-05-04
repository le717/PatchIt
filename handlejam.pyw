# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! -  the standard and simple way to package and install mods for LEGO Racers
    Created 2013 Triangle717 <http://triangle717.wordpress.com>

    PatchIt! is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PatchIt! is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PatchIt! If not, see <http://www.gnu.org/licenses/>.
"""
# PatchIt! V1.1.0 Unstable JAM Handling Code

# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)
import PatchIt
import time
import logging
import os
import linecache
import JAMExtractor

def compressJAM():
    '''Passes the proper parameters to compress LEGO.JAM'''

    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root settings to basically hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can recieve the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # The files to be compressed
    jam_files = filedialog.askdirectory(
    parent=root,
    title="Where are the extracted LEGO.JAM files located?"
    )

    if len(jam_files) == 0:
        raise SystemExit

    JAMExtractor.build(jam_files)

def main():

    logging.info("Display JAM Extractor menu to user")
    print('''\nPlease make a selection:\n
[e] Extract LEGO.JAM
[c] Compress LEGO.JAM
[q] Quit''')
    jam_opt = input("\n\n> ")

    # Nothing here is complete, so redirect back to PatchIt! menu
##    if jam_opt.lower() == "e" or jam_opt.lower() == "c":
    if jam_opt.lower() == "e":
        extractJAM()

##    elif jam_opt.lower() == "c":

    else: #if jam_opt.lower():
        logging.warning("Whoops! That feature hasn't been added yet.")
        print("\nWhoops! That feature hasn't been added yet.")
        time.sleep(0.5)
        logging.info("Switching to PatchIt! main menu")
        PatchIt.main()

##    if jam_opt.lower() == "b"

def extractJAM():
    '''Passes the proper parameters to extract LEGO.JAM'''
    pass

    JAM_location = linecache.getline(os.path.join("Settings", "Racers.cfg"), 5)
    JAM_file = os.path.join(JAM_location, "LEGO.JAM")
    if os.path.exists(JAM_file):
        JAMExtractor.extract(JAM_file)
    elif not os.path.exists(JAM_file):
        raise SystemExit

findExtractor()
JAMName()
