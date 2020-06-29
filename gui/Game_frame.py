''' Startup_frame.py

This frame contains the pre-grame frame. Aka startup_frame. It allows the user to change setting
before the game starts.

'''

import tkinter as tk
import logging
from gui import Image_label
from tkinter import ttk as ttk

class Game_frame(ttk.Frame):
    def __init__(self, parent, top_level, style):
        ''' Constructor to create Startup_frame

        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        '''
        logging.info("\n--------------------------------------------------\n"
                     "###### Game_frame constructor begins ######\n"
                     "--------------------------------------------------")
        # Public variables
        self.top_level = top_level
        self.style = style
        self.input_vars = {}
        self.input_widgets = {}

        # Frame settings

        super().__init__(parent)
        # self.top_level.overrideredirect(True)
        # root = Tk()
        # root.attributes('-fullscreen', True)
        logging.info("\n"
                     "------------------------------------------------\n"
                     "###### Game_frame constructor finish ######\n"
                     "------------------------------------------------")

    def resize_root(self):
        ''' Resizes root to size optimal for this frame

                :return:
                '''
        logging.info("Resizing root for Game_frame")
        self.top_level.set_root_min_size(
            int(self.top_level.SCREEN_WIDTH),
            int(self.top_level.SCREEN_HEIGHT),
        )
