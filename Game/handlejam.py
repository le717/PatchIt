# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013 Triangle717 <http://Triangle717.WordPress.com/>

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
# PatchIt! V1.1.2 Unstable JAM Handling Code


import os
import time
import logging

# RunAsAdmin wrapper
import runasadmin

# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

# Colored shell text
#import Color as color
#import Color.colors as colors

# PatchIt! "Constants"
from constants import (app_folder, settings_fol, LR_settings)
import PatchIt

# LEGO Racers settings and JAM Extractor
from Game import (Racers, JAMExtractor)


def SelectDataFiles():
    """Select the files to compress into a JAM"""
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

    if not jam_files:
        raise SystemExit(0)

    # Compress the JAM
    root.destroy()
    SaveJAM(jam_files)


def SaveJAM(jam_files):
    """Compress the files into LEGO.JAM"""
    try:
        os.chdir(jam_files)
        JAMExtractor.build(jam_files, verbose=False)

    # We don't have the rights to compress the JAM
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! does not have the rights to save LEGO.JAM to
{0}
'''.format(
    jam_files))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ['''PatchIt! does not have the rights to save LEGO.JAM to
{0}'''
            .format(jam_files)]):
            # Do nothing, go to main menu
            pass

    finally:
        os.chdir(app_folder)


def main(*args):
    """JAM Extractor Menu"""
    logging.info("Display JAM Extractor menu to user")
    print('''\nPlease make a selection:\n
[e] Extract LEGO.JAM
[c] Compress LEGO.JAM
[q] Quit''')
    jam_opt = input("\n\n> ")

    if jam_opt.lower() == "c":
        SelectDataFiles()

    # Nothing here is complete, so redirect back to PatchIt! menu
    else:  # if jam_opt.lower() != "q":
        print("\nWhoops! That feature hasn't been added yet.")
        time.sleep(0.5)
    logging.info("Switching to PatchIt! main menu")
    PatchIt.main(count=1)


#def extractJAM():
    #"""Passes the proper parameters to extract LEGO.JAM"""
    ## The Racers settings (required for extraction) does not exist
    #if not os.path.exists(os.path.join("Settings", "Racers.cfg")):
        #colors.text('''The LEGO Racers settings do not exist!
#Please create it, then try to extract LEGO.JAM''', color.FG_LIGHT_RED)

    ## Get location of Racers installation
    #JAM_location = linecache.getline(os.path.join("Settings", "Racers.cfg"), 5)
    ## This
    ##JAM_file = os.path.join(JAM_location, "LEGO.JAM")
    #if os.path.exists(JAM_file):
        #JAMExtractor.extract(JAM_file)
    #elif not os.path.exists(JAM_file):
        #raise SystemExit(0)

#if __name__ != "__main__":
    ##SelectDataFiles()
