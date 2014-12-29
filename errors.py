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
import tkinter
from tkinter import messagebox


def displayError(title, message, trace=None):
    """Display error message using a a Tkinter error dialog.

    @param title {String} Dialog error title.
    @param message {String} Dialog error message.
    @param trace {Exception} Exception alias for debugging.
    @returns {Boolean} Always returns False.
    """
    root = tkinter.Tk()
    root.withdraw()
    root.overrideredirect(True)
    root.geometry('0x0+0+0')
    root.deiconify()
    root.lift()
    root.focus_force()

    # Run Exception logging only if an exception occurred
    if trace is not None:
        logging.exception("\nAn error has occurred:\n", exc_info=True)

    logging.error("\nAn error has occurred:\n{0}".format(message))
    messagebox.showerror(title, message)
    return False
