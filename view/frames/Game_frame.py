''' Startup_frame.py

This frame contains the pre-grame frame. Aka startup_frame. It allows the user to change setting
before the game starts.

'''

import logging
from tkinter import ttk as ttk

class Game_frame(ttk.Frame):
    def __init__(self, view, parent, top_level, style, callbacks):
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
        self.view = view
        self.style = style
        self.callbacks = callbacks
        self.input_vars = {}
        self.input_widgets = {}

        # Frame settings

        super().__init__(parent)
        self._resize_min_root()

        # self.top_level.overrideredirect(True)
        # root = Tk()
        # self.top_level.attributes('-fullscreen', True)

        logging.info("\n"
                     "------------------------------------------------\n"
                     "###### Game_frame constructor finish ######\n"
                     "------------------------------------------------")

    def _resize_min_root(self):
        ''' Resizes root to size optimal for this frame

                :return:
                '''
        logging.info("Resizing root for Game_frame")
        self.view.set_root_min_size(
            int(self.view.SCREEN_WIDTH/2),
            int(self.view.SCREEN_HEIGHT/2),
        )
        self.top_level.state('zoomed')
