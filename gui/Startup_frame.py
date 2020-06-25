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
        super().__init__(parent)

        # Title
        Image_label.Image_label(self, "gui/images/card_collections/aces.png", int(self.top_level.SCREEN_HEIGHT / 2.5),
                                int(self.top_level.SCREEN_WIDTH / 8.5), "lightgrey").pack()
        ttk.Label(self, text="Blackjack", style="title.default.TLabel").pack()

        ##########
        # Inputs #
        ##########
        input_frame = ttk.Frame(self)
        input_frame.pack(fill=tk.BOTH, padx=25)
        input_frame.columnconfigure(1, weight=1)
        ttk.Label(input_frame, text="Bots: ").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(input_frame, text="Bot Delay:").grid(row=1, column=0, sticky=tk.W)

        self.input_widgets["amtOfBotsWidget"] = ttk.Spinbox(input_frame)
        self.input_widgets["botDelayCheckWidget"] = ttk.Checkbutton(input_frame)
        self.input_widgets["amtOfBotsWidget"].grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)
        self.input_widgets["botDelayCheckWidget"].grid(row=1, column=1, sticky=tk.EW, pady=5, padx=5)

        # Buttons
        ttk.Button(self, text="Quit", style="quit.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=(5, 40), side=tk.BOTTOM)
        ttk.Button(self, text="Help", style="help.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)
        ttk.Button(self, text="Play", style="play.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)


