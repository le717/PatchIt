#!/usr/bin/env python3
# PatchIt! setup script using cx_Freeze.
# Taken from https://github.com/Lyrositor/EBPatcher

from cx_Freeze import setup, Executable
import sys

from PatchIt import majver, minver

build_exe_options = {"build_exe": "build",
					 "create_shared_zip": True,
					 "icon": "Icons/PatchItIcon.ico",
                     "optimize": "1",
                     "compressed": True,
                     "includes": ["extract", "compress", "thebookkeeper", "gametips", "color"],
                     }
base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "PatchIt!",
      version = "{0} {1}".format(majver, minver),
      author = "Triangle717",
      description = "PatchIt! {0} {1}, copyright 2013 Triangle717".format(majver, minver),
      options = {"build_exe": build_exe_options},
      executables = [Executable("PatchIt.py", base=base,
								icon="Icons/PatchItIcon.ico",
								#shortcutName="PatchIt!"
                                )])