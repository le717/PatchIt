#! /usr/bin/env python3
# -*- coding: utf-8 -*-
"""PatchIt! - The simple way to package and install LEGO Racers mods.

Created 2013-2015 Triangle717
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

import logging

__all__ = ("PiPatch")


class PiPatch(object):

    """PatchIt! Patch Constructor.

    Creates a Patch object containing all required information
        and details needed for a Patch.
    """

    def __init__(self, name, version, author, desc):
        """Create a new PatchIt! Patch object.

        @param {String} name Patch name.
        @param {String} version Patch version.
        @param {String} author Patch author.
        @param {String} desc Patch description.
        """
        logging.info("New PiPatch instance")
        self.__name = name
        self.__version = version
        self.__author = author
        self.__desc = desc.replace("|", "\n")
        self.__mp = "MP"
        self.__game = "LEGO Racers"
        self.__patch = "{0}-{1}".format(name.replace(" ", "-"), version)

    def getName(self):
        """Get the Patch name.

        @returns {String}
        """
        return self.__name

    def getVersion(self):
        """Get the Patch version.

        @returns {String}
        """
        return self.__version

    def getAuthor(self):
        """Get the Patch author.

        @returns {String}
        """
        return self.__author

    def getDesc(self):
        """Get the Patch description.

        @returns {String}
        """
        return self.__desc

    def prettyPrint(self):
        """Get a formatted version of the Patch name and version.

        @returns {String}
        """
        return "{0} v{1}".format(self.__name, self.__version)

    def getArchiveName(self):
        """Get the Patch archive name suitable for saving to disc.

        @returns {String}
        """
        return "{0}.PiA".format(self.__patch)

    def getPatchName(self):
        """Get the Patch file name suitable for saving to disc.

        @returns {String}
        """
        return "{0}.PiP".format(self.__patch)

    def getPatch(self):
        """Get the Patch format layout suitable for saving to disc.

        @returns {String}
        """
        return """// PatchIt! PiP file format V1.1, developed by le717 and rioforce
[PiA]\n{0}\n[General]\n{1}\n{2}\n{3}\n{4}\n{5}\n[Description]\n{6}
""".format(self.getArchiveName(), self.__name, self.__version,
           self.__author, self.__mp, self.__game, self.__desc)
