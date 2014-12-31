# -*- coding: utf-8 -*-
"""PatchIt! - The simple way to package and install LEGO Racers mods.

Created 2013-2014 Triangle717
<http://Triangle717.WordPress.com/>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PatchIt! is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PatchIt! If not, see <http://www.gnu.org/licenses/>.

"""

import os
import json
import logging
import webbrowser

import tkinter as tk
from tkinter import ttk

import Color as color
import constants as const
import Color.colors as colors
from Patch import (install, create)
from Game import (Racers, rungame, legojam)

# Build number
buildNum = const.getBuildNumber()


def preload(openFile):
    """PatchIt! settings checks."""
    # Write general PatchIt! settings
    piSettings()

    # Check for/confirm settings
    Racers.main(True)

    if openFile is not None:
        # Switch to Patch Installation if needed
        if os.path.isfile(openFile):
            logging.info("A file path was given")
            install.checkPatch(openFile)

    # Display menu
    main()


def about():
    """Tkinter about box."""
    root = tk.Tk()
    root.title("About {0} Version {1}".format(const.app, const.version))
    root.minsize("420", "280")
    root.maxsize("420", "280")

    # Give it focus
    root.deiconify()
    root.lift()
    root.focus_force()

    # Frame settings
    frame = ttk.Frame(root, padding="7 7 7 7")
    frame.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))

    # PatchIt! Logo
    pi_logo = tk.PhotoImage(file="Icons/PiTk.gif")
    image_frame = ttk.Label(root)
    image_frame['image'] = pi_logo
    image_frame.grid(column=0, row=0, sticky=tk.N, pady="7")

    # Displayed text
    label = ttk.Label(frame, text='''





            {0} Version {1} {2}
                              Build {3}
               Released ?? ??, 201?

            Created 2013-2015 Triangle717

              The simple way to package
            and install LEGO Racers mods
'''.format(const.app, const.version, const.minVer,
           buildNum))
    label.grid(column=1, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))

    def close_about(*args):
        """Close the about box."""
        root.destroy()
        main()

    # Close About Window button
    close = ttk.Button(frame, default="active", text="Close",
                       command=close_about)
    close.grid(column=1, row=1, sticky=tk.N, pady="7")

    # GitHub Project button
    github = ttk.Button(frame, text="Website",
                        command=lambda: webbrowser.open_new_tab(
                            "http://le717.github.io/PatchIt"))
    github.grid(column=0, row=1, sticky=tk.N, pady="7")

    # Creator's website button
    creator_site = ttk.Button(frame, text="Triangle717",
                              command=lambda: webbrowser.open_new_tab(
                                  "http://wp.me/P1V5ge-I3"))
    creator_site.grid(column=2, row=1, sticky=tk.N, pady="7")

    # Small bit of padding around the elements
    for child in frame.winfo_children():
        child.grid_configure(padx=2, pady=2)

    # Bind the Return ("Enter") key to close the About Window
    root.bind('<Return>', close_about)

    # Make it load
    root.iconbitmap(const.appIcon)
    root.mainloop()


def main(loopNum=1):
    """PatchIt! main menu."""
    loopNum += 1

    # If the user has pressed an valid key 5 times or this is app launch
    if (loopNum == 2 or loopNum == 6):
        # Reset the count back to two,
        if loopNum == 6:
            loopNum = 2

        # And display the menu only at the valid times
        colors.text("\n{0} {1} {2}\nCreated 2013-2015 {3}".format(
                    const.app, const.version, const.minVer,
                    const.creator), color.FG_WHITE)

        logging.info("Display menu to user")
        print("""
Please make a selection:

[a] About PatchIt!            [c] Create a PatchIt! Patch
[r] Run LEGO Racers           [i] Install a PatchIt! Patch
[s] PatchIt! Settings         [j] JAM Extractor

                      [q] Quit""")

    menuChoice = input("\n> ").lower()
    while True:
        # About PatchIt! box
        if menuChoice == "a":
            logging.info("User pressed About PatchIt!")
            logging.info("Opening About Box")
            about()

        # Patch creation
        elif menuChoice == "c":
            logging.info("User pressed Create a PatchIt! Patch")
            create.main()
            main()

        # Patch installation
        elif menuChoice == "i":
            logging.info("User pressed Install a PatchIt! Patch")
            install.selectPatch()

        # JAM Extractor wrapper
        elif menuChoice == "j":
            logging.info("User pressed JAM Extractor")
            if not legojam.main():
                main()

        # PatchIt! Settings
        elif menuChoice == "s":
            logging.info("User pressed PatchIt! Settings")
            if not Racers.main():
                main()

        # Run LEGO Racers
        elif menuChoice == "r":
            rungame.PlayRacers().runGame()

        # Close PatchIt!
        elif menuChoice == "q":
            logging.info("User pressed Quit")
            logging.info('''PatchIt! is shutting down
            ''')
            logging.shutdown()
            raise SystemExit(0)

        # Undefined input
        else:
            logging.info("User pressed an undefined key ({0})".format(
                         menuChoice))
            colors.text("\nThat is an invalid option!", color.FG_LIGHT_RED)
            main(loopNum=loopNum)


def piSettings():
    """Write PatchIt! general settings."""
    # TODO: Will be expanded with more data in future releases,
    # including portable mode awareness
    theFile = os.path.join(const.settingsFol, const.piSettings)
    logging.info("Writing {0}".format(theFile))

    # If the Settings folder does not exist, create it
    if not os.path.exists(const.settingsFol):
        os.makedirs(const.settingsFol)

    jsonData = {
        "version": const.version,
        "minVer": const.minVer,
        "buildNum": buildNum
    }

    # Write the major and minor version numbers
    with open(os.path.join(theFile), "wt", encoding="utf_8") as f:
        f.write(json.dumps(jsonData, indent=4, sort_keys=True))
    return True
