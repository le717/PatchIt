#! /usr/bin/python3
# -*- coding: utf-8 -*-
import os
import sys
import distutils.dir_util
import zipfile
from urllib.error import HTTPError

# Import wget
parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, parentdir)
import wget

curDir = os.getcwd()
link = "https://github.com/le717/PatchIt/archive/gh-pages.zip"
name = "PatchIt-gh-pages.zip"
path = os.path.join(curDir, "Documentation", "Readme")

# Download the readme from the gh-pages branch
try:
    wget.download(link)
    halt = False
# We can't download it right now, so end the process
except HTTPError:
    print("\nReadme cannot be downloaded at this time.\n")
    halt = True

if not halt:
    # Remove the directory for a clean slate
    if os.path.exists(path):
        distutils.dir_util.remove_tree(path)

    # Extract the zip to the proper location
    with zipfile.ZipFile(name, "r") as extract:
        extract.extractall(path=path)

    # Delete the zip archive
    os.unlink(name)

    # Copy the files out of the subfolder
    distutils.dir_util.copy_tree(os.path.join(path, "PatchIt-gh-pages"), path)

    # Remove all the unneeded files/folders
    distutils.dir_util.remove_tree(os.path.join(path, "PatchIt-gh-pages"))
    distutils.dir_util.remove_tree(os.path.join(path, "Documentation"))
    distutils.dir_util.remove_tree(os.path.join(path, "Site-Project"))
    os.unlink(os.path.join(path, ".gitignore"))
    os.unlink(os.path.join(path, ".gitattributes"))

    # And we're done!
    print("\n\nDone. :)")
