# PatchIt! V1.0.3 Stable Logging code

# logging.BasicConfig code based on example from A Byte of Python
# http://www.swaroopch.com/notes/Python

import os, logging, time
import color, color.colors as colors

# ------------ Begin PatchIt! Logging Code ------------ #

def appLoggingFolder():
    '''Checks for (and creates) PatchIt! Logs folder'''

    try:
        # The Logs folder does not exist in the current directory
        if not os.path.exists(os.path.join(os.getcwd(), "Logs")):

            # Create the Logs folder
            logsfolder = os.mkdir(os.path.join(os.getcwd(), "Logs"))
    except PermissionError:
        colors.pc("\nPatchIt! does not have the user rights to operate!\nPlease relaunch PatchIt! as an Administrator.", color.FG_LIGHT_RED)
        # Display message long enough so user can read it
        time.sleep(5)
        # Close program
        raise SystemExit


# AKA if this is imported as a module
if "__main__" != __name__:
    appLoggingFolder()

    # -- Begin Logging Config -- #

    logging_file = os.path.join(os.getcwd(), "Logs", 'TheWritingsofPatchIt.log')

    logging.basicConfig(
        level = logging.DEBUG,
        format = "%(asctime)s : %(levelname)s : %(message)s",
        filename = logging_file,
        filemode = 'a+',
    )

    # -- End Logging Config -- #

# ------------ End PatchIt! Logging Code ------------ #