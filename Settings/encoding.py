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
"""

import logging


def checkEncoding(filePath):
    """
    Check the encoding of a file,
    ensuring it uses UTF-8-NOBOM.
    """
    logging.info("Check encoding of {0}".format(filePath))

    # Open it, read just the area containing the byte mark
    with open(filePath, "rb") as encodeCheck:
        encoding = encodeCheck.readline(3)

    # The settings file is encoding using either
    # UTF-8BOM, UCS-2 Big Endian, or UCS-2 Little Endian.
    # The last two items are two variants of UCS-2LE I keep coming across.
    if encoding in (b"\xef\xbb\xbf", b"\xfe\xff\x00",
                    b"\xff\xfe0", b"\xff\xfe/"):
        # The encoding is not correct
        return True

    # The file used the proper (UTF-8NOBOM) encoding
    return False
