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
PatchIt! Shell Text Colors
Taken from https://github.com/imayhaveborkedit/lms-lrr-modding-system
and updated with Python 3 support
"""

import ctypes

STD_OUTPUT_HANDLE = -11


def get_csbi_attributes(handle):
    import struct
    csbi = ctypes.create_string_buffer(22)
    res = ctypes.windll.kernel32.GetConsoleScreenBufferInfo(handle, csbi)
    assert res

    (bufx, bufy, curx, cury, wattr, left,
     top, right, bottom, maxx, maxy) = struct.unpack("hhhhHhhhhhh",
                                                     csbi.raw)
    return wattr


def text(text, color):
    """Print Colored Text"""
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, color)
    print(text)
    ctypes.windll.kernel32.SetConsoleTextAttribute(handle, reset)

handle = ctypes.windll.kernel32.GetStdHandle(STD_OUTPUT_HANDLE)
reset = get_csbi_attributes(handle)
