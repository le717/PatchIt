#! /usr/bin/env python3
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
import sys
import distutils.dir_util
import zipfile
from urllib.error import (HTTPError, URLError)

# Import wget from parent directory since the script is being run standalone
# Since I can't run `from Tools.wget import wget`
try:
    parentdir = "../wgetter"
    # Not happy with editing sys.path... >:(
    sys.path.insert(0, parentdir)
    import wgetter

# The script is being run from the main setup.py,
# so import from different location
except ImportError:
    from Tools.wgetter import wgetter  # noqa


def main():
    """Download the latest version of the PatchIt! Readme from GitHub."""
    zipLink = "https://github.com/le717/PatchIt/archive/gh-pages.zip"
    # Define proper name of Zip archive, as download link doesn't provide it
    zipName = "PatchIt-gh-pages.zip"
    # Location to save the Readme
    savePath = os.path.join("..", "..", "Documentation", "Readme")

    # Download the readme from the gh-pages branch
    try:
        wgetter.download(zipLink)
        halt = False

    # We can't download it right now, so end the process
    except (HTTPError, URLError):
        print("\nLatest PatchIt! Readme cannot be downloaded at this time.\n")
        halt = True

    if not halt:
        # Remove the directory for a clean slate
        if os.path.exists(savePath):
            distutils.dir_util.remove_tree(savePath)

        # Extract the zip to the proper location
        with zipfile.ZipFile(zipName, "r") as extract:
            extract.extractall(path=savePath)

        # Delete the zip archive
        os.unlink(zipName)

        # Copy the files out of the subfolder
        distutils.dir_util.copy_tree(os.path.join(
            savePath, "PatchIt-gh-pages"), savePath)

        # Remove all the unneeded files/folders
        distutils.dir_util.remove_tree(os.path.join(
            savePath, "PatchIt-gh-pages"))
        distutils.dir_util.remove_tree(os.path.join(
            savePath, "Documentation"))
        distutils.dir_util.remove_tree(os.path.join(savePath, "Site-Project"))
        os.unlink(os.path.join(savePath, ".gitignore"))
        os.unlink(os.path.join(savePath, ".gitattributes"))

        # And we're done!
        print("\n\nLatest PatchIt! Readme successfully downloaded.\n")

if __name__ == "__main__":
    main()
