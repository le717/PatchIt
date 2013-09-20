#! /usr/bin/python3
# -*- coding: utf-8 -*-

import os
import distutils.dir_util


def cleanup(destfolder):
    """ Remove unneeded Tkinter files"""
    # Small bit of whitespace
    print("\n")
    # Delete the unneeded items from the freeze
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tcl", "tzdata"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tcl", "http1.0"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tk", "demos"))
    distutils.dir_util.remove_tree(os.path.join(destfolder, "tk", "images"))