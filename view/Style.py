''' Style.py

File contains the styling for all the ttk widgets in the program.
This allows for all the styling in one place.

'''

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class Style(ttk.Style):
    def __init__(self):
        ''' Constructor, Creates styles for entire GUI.
        '''
        super().__init__()
        self.DEFAULT_BACKGROUND_COLOUR = "lightgrey"

        # Themes ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        # class.winfo_class
        self.theme_use("clam")

        # Default Backgrounds
        self.configure('TFrame', background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("TLabel", background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("TCheckbutton", background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("title.default.TLabel", background=self.DEFAULT_BACKGROUND_COLOUR,
                       font=Font(family="Lucida Grande", size=10))

        # Startup Frame
        self.configure("play.startUpFrame.TButton", )
        self.configure("help.startUpFrame.TButton", )
        self.configure("quit.startUpFrame.TButton", )
