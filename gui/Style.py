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

        # Default Backgrounds
        self.configure('defaultBackground.default.TFrame', background='lightgrey')
        self.configure("title.default.TLabel", background='lightgrey',
                       font=Font(family="Lucida Grande", size=10))

        # Startup Frame
