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
LEGO Racers Launcher
"""

import os
import time
import subprocess
import logging

# Colored shell text
import Color as color
import Color.colors as colors

from Game import Racers
import PatchIt


class PlayRacers(object):
    """
    Launch LEGO Racers
    NOTE: This requires Administrator rights,
    and will not work without them.
    """

    def __init__(self):
        """Define exe name and game parameters"""
        self.__LRE = "LEGORacers.exe"
        # Parameter to skip intro movies
        self.__novideo = "-novideo"
        # Exe parameters for future use
        #self.__horz = horz
        #self.__vert = vert
        #self.__horzres = "-horzres {0}".format(int(self.__horz))
        #self.__vertres = "-vertres {0}".format(int(self.__vert))

    def Race(self):
        """I'll see you... at the finish line!"""
        # Get the installation path to Racers
        install_path = Racers.getRacersPath()
        logging.info("Reported LEGO Racers installation at {0}"
                     .format(install_path))
        # Run the game directly
        try:
            logging.info("Launching LEGO Racers...")
            os.chdir(install_path)
            subprocess.call(
                [os.path.join(install_path, self.__LRE), self.__novideo]
            )
            logging.shutdown()
            raise SystemExit(0)

        # Except LEGORacers.exe could not be found
        except FileNotFoundError:  # lint:ok
            logging.warning("LEGORacers.exe could not be found at {0}!"
                            .format(install_path))
            colors.text("\nLEGORacers.exe could not be found at \n\n{0}"
                  .format(install_path), color.FG_LIGHT_RED)

        # Except we need admin righs to do it
        except (OSError, PermissionError):  # lint:ok
            logging.exception('''Oops! Something went wrong! Here's what happened
''', exc_info=True)
            # Temp excuse since I can't get RunAsAdmin working
            # and I don't think I can sneak a registry string in
            # without having admin rights anyway.
            logging.warning("LEGO Racers cannot be launched at this time.")
            colors.text("\nLEGO Racers cannot be launched at this time.\n",
                        color.FG_LIGHT_RED)

        finally:
            time.sleep(1)
            PatchIt.main()
