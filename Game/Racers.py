# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt!
    The standard and simple way to package and install LEGO Racers mods

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
PatchIt! LEGO Racers Settings
"""

import os
import json
import logging

# Tkinter GUI library
import tkinter
from tkinter import filedialog

# PatchIt! modules
import constants as const
from Settings import encoding
from singleton import Singleton

__all__ = ["main", "Settings"]


def main(auto=False):
    """LEGO Racers settings user interface"""
    # Create the settings object
    mySettings = Settings.Instance()
    mySettings.readSettings()
    details = mySettings.getDetails()

    # Shortcut to installation path,
    # plus fix if the path is blank
    installPath = details[0]
    if installPath == "":
        installPath = const.appFolder

    # The settings do not exist
    if (
        (auto and not details[2]) or
        (not auto and not details[2])
    ):
        root = tkinter.Tk()
        root.withdraw()
        tkinter.messagebox.showerror("Invalid installation!",
                                     "Cannot find {0} installation at {1}"
                                     .format(const.LRGame, installPath))
        root.destroy()
        return False

    # The settings exist, are valid, and this is user prompt
    if not auto and details[2]:
        print("""
A {0} {1} release was found at

{2}

Would you like to change this?
""".format(const.LRGame, details[1], installPath))

        changeInstallPath = input(r"[Y\N] > ")

        # Yes, I want to change the defined installation
        if changeInstallPath.lower() == "y":
            logging.info("User wants to change LEGO Racers settings")
            if not mySettings._getInstallInfo():
                return False

        # No, I do not want to change the defined installation
        else:
            logging.info("""User does not want to change the
LEGO Racers installation or pressed an undefined key""")
            return False


@Singleton
class Settings(object):
    """LEGO Racers Settings Management"""

    def __init__(self):
        """Object-only values"""
        self.__piFirstRun = "1"
        self.__installLoc = ""
        self.__releaseVersion = ""
        self.__settingsExist = True
        self.__settingsExtension = ".json"
        self.__settingsData = None

    def getDetails(self):
        """Return LEGO Racers installation details"""
        return (self.__installLoc, self.__releaseVersion, self.__settingsExist)

    def _setDetails(self):
        """Set details gathered by from reading"""
        self.__piFirstRun = self.__settingsData["firstRun"]
        self.__releaseVersion = self.__settingsData["releaseVersion"]
        self.__installLoc = self.__settingsData["installPath"]
        return True

    # ------- Begin JSON/CFG Reading and Writing ------- #

    def _writeSettings(self, releaseVersion, installLoc):
        """Write JSON-based settings file"""
        jsonData = {
            "firstRun": "1",
            "releaseVersion": str(releaseVersion),
            "installPath": installLoc
        }

        # Create Settings directory if it does not exist
        logging.info("Creating Settings directory")
        if not os.path.exists(const.settingsFol):
            os.mkdir(const.settingsFol)

        with open(os.path.join(const.settingsFol, const.LRSettings),
                  "wt") as f:
            f.write(json.dumps(jsonData, indent=4, sort_keys=True))
        return True

    def _readSettingsJson(self):
        """Read JSON-based settings file"""
        try:
            with open(os.path.join(const.settingsFol, const.LRSettings),
                      "rt", encoding="utf-8") as f:
                self.__settingsData = json.load(f)
            return True

        # The file is not valid JSON
        except ValueError:
            logging.error("""{0} is not valid JSON!
The content cannot be retrieved!""".format(const.LRSettings))
            return False

    def _convertToJson(self, cfgData):
        """Convert CFG-based settings to JSON-based settings"""
        try:
            # This is a first run, create the settings
            if cfgData[2].strip() == "0":
                logging.info("This is first time PatchIt! has been run")
                self._getInstallInfo()
                return False

            # The settings have been set up before, convert them
            else:
                self._writeSettings(cfgData[4].strip(), cfgData[6].strip())
                self._readSettingsJson()
                self._setDetails()
            return True

        # There was an error reading the settings
        except IndexError:
            logging.warning("There was an error reading the CFG settings!")
            self._getInstallInfo()
            return False

    def _readSettingsCfg(self):
        """Read older CFG-based settings file"""
        with open(os.path.join(const.settingsFol, const.LRSettingsCfg),
                  "rt", encoding="utf_8") as f:
            cfgData = f.readlines()
        return cfgData

    # ------- End JSON/CFG Reading and Writing ------- #

    # ------- Begin Settings Confirmation and Detection ------- #

    def _getVersion(self):
        """Detect LEGO Racers release version"""
        # Open the exe and read a small part of it
        try:
            with open(self.__exeLoc, "rb") as f:
                __offset = f.readlines()[1][8:20]

            # This is a 1999 release
            if __offset in (b"\xb7S\xfeK\xf32\x90\x18\xf32\x90\x18" or
                            b"bPE\x00\x00L\x01\x08\x00\xf1\xdb)7"):

                logging.info("According to the offset, this is a 1999 release")
                self.__releaseVersion = "1999"

            # This is a 2001 release
            elif __offset == b"\xd7\xf2J\x1a\x93\x93$I\x93\x93$I":
                logging.info("According to the offset, this is a 2001 release")
                self.__releaseVersion = "2001"
            return True

        # We could not find the data we wanted (most likely a fake exe)
        except IndexError:
            logging.warning("Game release version could not be determined!")
            self.__releaseVersion = ""
            return False

    def _confirmSettings(self):
        """Confirm information given in settings"""
        # Exe, JAM, and DLL locations
        self.__exeLoc = os.path.join(
            self.__installLoc, "legoracers.exe".lower())
        self.__jamLoc = os.path.join(self.__installLoc, "lego.jam".lower())
        self.__dllLoc = os.path.join(self.__installLoc, "goldp.dll".lower())

        # The settings have never been set up
        if self.__piFirstRun == "0" and self.__settingsExist:
            logging.warning("LEGO Racers settings have not been set up!")
            return False

        # The release version was not recognized
        if self.__releaseVersion != ("1999" or "2001"):
            logging.warning("Unrecognized game release version: {0}!".format(
                self.__releaseVersion))

            # Determine the release version
            self._getVersion()
            if self.__settingsData is not None:
                logging.info("LEGO Racers Release version {0} detected"
                             .format(self.__settingsData["releaseVersion"]))
                self.__settingsData["releaseVersion"] = self.__releaseVersion

        # The necessary files were found
        if (
            os.path.exists(self.__exeLoc) and
            os.path.exists(self.__jamLoc) and
            os.path.exists(self.__dllLoc)
        ):
            logging.info("LEGO Racers installation confirmed at {0}".format(
                self.__installLoc))
            return True

        # Nope, some files were mising :(
        logging.warning("LEGO Racers installation could not be confirmed!")
        return False

    def findSettings(self):
        """Locate the LEGO Racers settings"""
        # The preferred JSON settings do not exist
        if not os.path.exists(os.path.join(
                              const.settingsFol, const.LRSettings)):
            logging.warning("Could not find LEGO Racers JSON settings!")
            self.__settingsExtension = ".cfg"

            # Since those could not be found, look for the older CFG settings
            if not os.path.exists(os.path.join(
                                  const.settingsFol, const.LRSettingsCfg)):
                logging.warning("Could not find LEGO Racers settings!")
                self.__settingsExist = False
                return False

        # Check encoding of the file found
        logging.info("Checking encoding of settings file")
        if self.__settingsExtension == ".json":
            settingsName = const.LRSettings
        else:
            settingsName = const.LRSettingsCfg

        if encoding.checkEncoding(os.path.join(
                const.settingsFol, settingsName)):
            # The settings cannot be read
            logging.warning("LEGO Racers Settings cannot be read!")

            # Declare nonexistent settings since we can't read the file
            self.__settingsExist = False
            return False
        logging.info("File encoding check passed")
        return True

    # ------- Begin Settings Confirmation and Detection ------- #

    def _getInstallInfo(self):
        """Get details to write LEGO Racers settings"""
        # Draw (then withdraw) the root Tk window
        root = tkinter.Tk()
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
        logging.info("Display file dialog requesting LEGO Racers installation")
        newInstallLoc = filedialog.askopenfilename(
            parent=root,
            title="Where is LEGORacers.exe",
            defaultextension=".exe",
            filetypes=[("LEGORacers.exe", "*.exe")]
        )

        # Get the directory the Exe is in
        newInstallLoc = os.path.dirname(newInstallLoc)

        # Give focus back to console window
        logging.info("Give focus back to console window")
        root.destroy()

        # The user clicked the Cancel button
        if not newInstallLoc:
            # Go back to the main menu
            logging.warning(
                "User did not select a new LEGO Racers installation!")
            return False

        logging.info("User selected a new LEGO Racers installation at {0}"
                     .format(newInstallLoc))

        # Confirm given data
        self.__installLoc = newInstallLoc
        if self._confirmSettings():
            # Now that the information has been confirmed,
            # write a settings file
            self._writeSettings(self.__releaseVersion, self.__installLoc)
            self.__settingsExist = True
            return True
        return False

    def readSettings(self):
        """Read LEGO Racers Settings File"""
        # Confirm the settings exist and are readable
        self.findSettings()

        # The settings could not be found, go write the settings
        if not self.__settingsExist:
            logging.warning("LEGO Racers settings do not exist!")
            if self._getInstallInfo():
                return True
            return False

        # Read the proper file to get the data needed
        if self.__settingsExtension == ".json":
            if self._readSettingsJson():
                self._setDetails()

            # We might have encountered some invalid JSON.
            # This means we have to recreate the entire settings
            else:
                logging.warning("LEGO Racers JSON could not be parsed!")
                self.__settingsExist = False
                if self._getInstallInfo():
                    return True
                return False
        else:
            # Rewrite into JSON settings
            cfgData = self._readSettingsCfg()
            self._convertToJson(cfgData)

        # Installation confirmed, our job here is done
        if self._confirmSettings():
            logging.info("LEGO Racers Settings confirmed")
            return True

        # The installation could not be confirmed
        else:
            logging.__settingsExist(
                "LEGO Racers Settings could not be confirmed")
            self.settingsExist = False
            if self._getInstallInfo():
                return True
            return False
