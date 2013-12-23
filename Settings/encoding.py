# -*- coding: utf-8 -*-
"""
    This file is part of PatchIt!

    PatchIt! - the standard and simple way to package and install mods
    for LEGO Racers

    Created 2013-2014 Triangle717 <http://Triangle717.WordPress.com/>

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


def check_encoding(file_path):
    """
    Check the encoding of a text file,
    ensuring it uses UTF-8-NOBOM.
    """
    logging.info("Check encoding of {0} before installation".format(file_path))

    # Open it, read just the area containing the byte mark
    with open(file_path, "rb") as encode_check:
        encoding = encode_check.readline(3)

    if (
        # The settings file uses UTF-8-BOM encoding
        encoding == b"\xef\xbb\xbf"
        # The settings file uses UCS-2 Big Endian encoding
        or encoding == b"\xfe\xff\x00"
        # The settings file uses UCS-2 Little Endian
        or encoding == b"\xff\xfe0"
    ):
        # The encoding is not correct
        return True

    # The file used the proper encoding
    else:
        return False
