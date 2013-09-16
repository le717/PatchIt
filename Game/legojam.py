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

-------------------------------------
PatchIt! V1.1.2 Unstable JAM Extractor Wrapper
"""

import os
import logging

# RunAsAdmin wrapper
import runasadmin

# File/Folder Dialog Boxes
from tkinter import (filedialog, Tk)

# Colored shell text
import Color as color
import Color.colors as colors

import PatchIt
from constants import (app_folder)

# JAM Extractor
from Game import JAMExtractor


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
        root.destroy()
        colors.text("\nCould not find a JAM archive to compress!",
                    color.FG_LIGHT_RED)
        main()

    # Compress the JAM
    root.destroy()
    BuildJAM(jam_files)


def BuildJAM(jam_files):
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

    # Go back to the menu
    finally:
        os.chdir(app_folder)
        main()


def main(*args):
    """JAM Extractor Menu"""
    colors.text('''
JAM Extractor 1.0.2
COPYRIGHT (C) 2012-2013: JrMasterModelBuilder''', color.FG_WHITE)
    logging.info("Display JAM Extractor menu to user")
    print('''
[e] Extract LEGO.JAM     [c] Compress LEGO.JAM

                   [q] Quit''')
    jam_opt = input("\n> ")

    # User wants to compress a JAM
    if jam_opt.lower() == "c":
        logging.info("User pressed '[c] Compress LEGO.JAM'")
        SelectDataFiles()

    # User wants to extract a JAM
    if jam_opt.lower() == "e":
        logging.info("User pressed '[e] Extract LEGO.JAM'")
        SelectJAMArchive()

    # Go back to PatchIt! menu
    else:
        PatchIt.main(count=1)


def SelectJAMArchive():
    """Select the JAM Archive to extract"""
    # Draw (then withdraw) the root Tk window
    logging.info("Drawing root Tk window")
    root = Tk()
    logging.info("Withdrawing root Tk window")
    root.withdraw()

    # Overwrite root display settings
    logging.info("Overwrite root Tk window settings to hide it")
    root.overrideredirect(True)
    root.geometry('0x0+0+0')

    # Show window again, lift it so it can receive the focus
    # Otherwise, it is behind the console window
    root.deiconify()
    root.lift()
    root.focus_force()

    # Select the LEGO Racers installation
    logging.info("Where is the JAM archive to be extracted located?")
    jam_location = filedialog.askopenfilename(
        parent=root,
        title="Where is LEGO.JAM",
        defaultextension=".JAM",
        filetypes=[("LEGO.JAM", "*.JAM")]
    )

    if not jam_location:
        root.destroy()
        colors.text("\nCould not find a JAM archive to extract!",
                    color.FG_LIGHT_RED)
        main()

    # Extract the JAM
    root.destroy()
    ExtractJAM(jam_location)


def ExtractJAM(jam_location):
    """Extract the files from LEGO.JAM"""
    try:
        # Extract the JAM archive
        JAMExtractor.extract(jam_location, verbose=False)

    # We don't have the rights to extract the JAM
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception('''Oops! Something went wrong! Here's what happened

''', exc_info=True)
        logging.warning('''

PatchIt! does not have the rights to extract LEGO.JAM to
{0}
'''.format(
    jam_location))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ['''PatchIt! does not have the rights to extract LEGO.JAM to
{0}'''
            .format(jam_location)]):
            # Do nothing, go to main menu
            pass

    # Go back to the menu
    finally:
        main()
