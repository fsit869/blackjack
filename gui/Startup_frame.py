''' Startup_frame.py

This frame contains the pre-grame frame. Aka startup_frame. It allows the user to change setting
before the game starts.

'''

import tkinter as tk
import logging
from gui import Image_label
from tkinter import ttk as ttk

class Startup_frame(ttk.Frame):
    def __init__(self, parent, top_level, style):
        ''' Constructor to create Startup_frame

        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        '''
        logging.info("Setting up Startup Frame")
        # Public variables
        self.top_level = top_level
        self.style = style
        self.input_vars = {}
        self.input_widgets = {}

        # Frame settings
        self.top_level.set_root_min_size(
            int(self.top_level.SCREEN_WIDTH / 4),
            int(self.top_level.SCREEN_HEIGHT / 1.5),
        )
        super().__init__(parent, style="defaultBackground.default.TFrame")


        # Title
        ttk.Label(self, text="Blackjack", style="title.default.TLabel").pack()


