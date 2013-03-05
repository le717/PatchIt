# PatchIt! V1.0.2 Stable Logging code

import os, logging

# ------------ Begin PatchIt! Logging Code ------------ #

def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    # The Logs folder does not exist in the current directory
    if not os.path.exists(os.path.join(os.getcwd(), "Logs")):

        # Create the Logs folder
        logsfolder = os.mkdir(os.path.join(os.getcwd(), "Logs"))
        print("\nLogs folder created\n") # Debug print

if "__main__" != __name__:
    appLoggingFolder()

    # -- Begin Logging Config -- #

    logging_file = os.path.join(os.getcwd(), "Logs", 'TheWritingsofPatchIt.log')


    # Code based on example from A Byte of Python
    # http://www.swaroopch.com/notes/Python

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s : %(levelname)s : %(message)s",
        filename = logging_file,
        filemode = 'a+',
    )

    # -- End Logging Config -- #

# ------------ End PatchIt! Logging Code ------------ #