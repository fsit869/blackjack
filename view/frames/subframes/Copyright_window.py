''' Copyright_window.py

This file contains a class named Copyright_window. This contains the toplevel window for the copyright info


'''

import tkinter as tk
from tkinter import ttk
import logging

class Copyright_window(tk.Toplevel):
    def __init__(self):
        logging.info("\n--------------------------------------------------\n"
                     "###### Copyright_Window constructor begins ######\n"
                     "--------------------------------------------------")

        # Window settings
        super().__init__()
        self.title("Copyright Information")
        self.set_root_min_size(400, 700)
        self.resizable(False, False)
        self.grab_set()
        self.centre_root()
        self.protocol('WM_DELETE_WINDOW', self.on_ok_button)

        # Details
        ttk.Label(self,wraplength=390, text="""
The Python Imaging Library (PIL) is
    Copyright © 1997-2011 by Secret Labs AB
    Copyright © 1995-2011 by Fredrik Lundh

Pillow is the friendly PIL fork. It is
Copyright © 2010-2020 by Alex Clark and contributors

Like PIL, Pillow is licensed under the open source PIL Software License:

By obtaining, using, and/or copying this software and/or its associated
documentation, you agree that you have read, understood, and will comply
with the following terms and conditions:

Permission to use, copy, modify, and distribute this software and its
associated documentation for any purpose and without fee is hereby granted,
provided that the above copyright notice appears in all copies, and that
both that copyright notice and this permission notice appear in supporting
documentation, and that the name of Secret Labs AB or the author not be
used in advertising or publicity pertaining to distribution of the software
without specific, written prior permission.

SECRET LABS AB AND THE AUTHOR DISCLAIMS ALL WARRANTIES WITH REGARD TO THIS
SOFTWARE, INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS.
IN NO EVENT SHALL SECRET LABS AB OR THE AUTHOR BE LIABLE FOR ANY SPECIAL,
INDIRECT OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
        """).grid(row=0, column=0, sticky=tk.NSEW)

        ttk.Button(self, text="Agree", command=self.on_ok_button).grid(row=1, column=0, sticky=tk.NSEW)
        logging.info("\n--------------------------------------------------\n"
                     "###### Copyright_window constructor ends ######\n"
                     "--------------------------------------------------")

    def set_root_min_size(self, width, height):
        ''' Set min size of root

        :param width: Min width
        :param height: Min height
        :return: None
        '''
        logging.info("Setting copyright window min size to %d %d", width, height)
        self.minsize(width, height)

    def centre_root(self):
        ''' Centre copyright to screen no matter the size.

        :return: None
        '''
        self.update_idletasks()

        _ROOT_HEIGHT = self.winfo_height() # Root height
        _ROOT_WIDTH = self.winfo_width() # Root width
        _FRM_WIDTH = self.winfo_rootx() - self.winfo_x() # Find size of outer frame
        _WIN_WIDTH = self.winfo_width() + (2 * _FRM_WIDTH) # True window width
        _TITLE_BAR_HEIGHT = self.winfo_rooty() - self.winfo_y() # Title bar height
        _WIN_HEIGHT = self.winfo_height() + (_TITLE_BAR_HEIGHT + _FRM_WIDTH) # True window height

        x = self.winfo_screenwidth() // 2 - _WIN_WIDTH // 2 # Coord placement
        y = self.winfo_screenheight() // 2 - _WIN_HEIGHT // 2 # Coord placement

        logging.info("Setting copyright window size (%d, %d) to (%d, %d)", _ROOT_WIDTH, _ROOT_HEIGHT, x, y)
        self.geometry("{}x{}+{}+{}".format(
            _ROOT_WIDTH,
            _ROOT_HEIGHT,
            x,
            y,
        ))

    def on_ok_button(self):
        ''' Called when ok button pressed

        :return:
        '''
        logging.info("Closing copyright window")
        self.withdraw()
        self.destroy()