# -*- coding: utf-8 -*-
# <pep8-80 compliant>
"""
    This file is part of PatchIt!

    PatchIt!
    The standard and simple way to package and installl LEGO Racers mods

    Created 2013-2014 Triangle717
    <http://Triangle717.WordPress.com/>

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
PatchIt! JAM Extractor Wrapper
"""

import os
import logging

# RunAsAdmin wrapper
import runasadmin

# File/Folder Dialog Boxes
from tkinter import (Tk, filedialog)

# Colored shell text
import Color as color
import Color.colors as colors

# JAM Extractor
from Game import JAMExtractor

# PatchIt! Constants
import constants as const
import PatchIt

#TODO: Implement 1999 vs 2001 release logic


def selectDataFiles():
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
    jamFiles = filedialog.askdirectory(
        parent=root,
        title="Where are the extracted LEGO.JAM files located?"
    )

    if not jamFiles:
        root.destroy()
        colors.text("\nCould not find a JAM archive to compress!",
                    color.FG_LIGHT_RED)
        main()

    # Compress the JAM
    root.destroy()
    buildJAM(jamFiles)


def buildJAM(jamFiles):
    """Compress the files into LEGO.JAM"""
    try:
        os.chdir(jamFiles)
        JAMExtractor.build(jamFiles, verbose=False)

    # We don't have the rights to compress the JAM
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception("""Oops! Something went wrong! Here's what happened

""", exc_info=True)
        logging.warning("""

PatchIt! does not have the rights to save LEGO.JAM to
{0}
""".format(jamFiles))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ["""PatchIt! does not have the rights to save LEGO.JAM to
{0}""".format(jamFiles)]):
            # Do nothing
            pass

    # Go back to the menu
    finally:
        os.chdir(const.appFolder)
        main()


def main():
    """JAM Extractor Menu"""
    colors.text("""
JAM Extractor 1.0.2
COPYRIGHT (C) 2012-2013: JrMasterModelBuilder""", color.FG_WHITE)
    logging.info("Display JAM Extractor menu to user")
    print("""
[e] Extract LEGO.JAM
[c] Compress LEGO.JAM
[q] Quit""")
    menuChoice = input("\n> ")

    # User wants to compress a JAM
    if menuChoice.lower() == "c":
        logging.info("User pressed '[c] Compress LEGO.JAM'")
        selectDataFiles()

    # User wants to extract a JAM
    if menuChoice.lower() == "e":
        logging.info("User pressed '[e] Extract LEGO.JAM'")
        selectJAMArchive()

    # Go back to PatchIt! menu
    else:
        PatchIt.main()


def selectJAMArchive():
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
    jamLocation = filedialog.askopenfilename(
        parent=root,
        title="Where is LEGO.JAM",
        defaultextension=".JAM",
        filetypes=[("LEGO.JAM", "*.JAM")]
    )

    if not jamLocation:
        root.destroy()
        colors.text("\nCould not find a JAM archive to extract!",
                    color.FG_LIGHT_RED)
        main()

    # Extract the JAM
    root.destroy()
    extractJAM(jamLocation)


def extractJAM(jamLocation):
    """Extract the files from LEGO.JAM"""
    try:
        # Extract the JAM archive
        JAMExtractor.extract(jamLocation, verbose=False)

    # We don't have the rights to extract the JAM
    except PermissionError:  # lint:ok
        logging.warning("Error number '13'")
        logging.exception("""Oops! Something went wrong! Here's what happened

""", exc_info=True)
        logging.warning("""

PatchIt! does not have the rights to extract LEGO.JAM to
{0}
""".format(jamLocation))

        # User did not want to reload with Administrator rights
        if not runasadmin.AdminRun().launch(
            ["""PatchIt! does not have the rights to extract LEGO.JAM to
{0}""".format(jamLocation)]):
            # Do nothing
            pass

    # Go back to the menu
    finally:
        main()
