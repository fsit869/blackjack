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
        logging.info("\n--------------------------------------------------\n"
                     "###### Startup_Frame constructor begins ######\n"
                     "--------------------------------------------------")

        # Public variables
        self.top_level = top_level
        self.style = style
        self.input_widgets = {} # {widget_name:widget object}
        self.input_vars = {}
        self.STARTUP_FRAME_WIDTH = int(self.top_level.SCREEN_WIDTH / 4)
        self.STARTUP_FRAME_HEIGHT = int(self.top_level.SCREEN_HEIGHT / 1.5)

        # Setup Frame
        super().__init__(parent)

        # Title
        Image_label.Image_label(self, "gui/images/card_collections/aces.png", int(self.top_level.SCREEN_HEIGHT / 2.5),
                                int(self.top_level.SCREEN_WIDTH / 8.5)).pack()
        ttk.Label(self, text="Blackjack", style="title.default.TLabel").pack()

        ##########
        # Inputs #
        ##########

        # Input frame
        input_frame = ttk.Frame(self)
        input_frame.pack(fill=tk.BOTH, padx=25)
        input_frame.columnconfigure(1, weight=1)

        # Input labels
        ttk.Label(input_frame, text="Bots: ").grid(row=0, column=0, sticky=tk.W)
        ttk.Label(input_frame, text="Bot Delay:").grid(row=1, column=0, sticky=tk.W)

        # Input variables
        self.input_vars["amtOfBotsWidget"] = tk.IntVar()
        self.input_vars["amtOfBotsWidget"].set("1")
        self.input_vars["botDelayCheckWidget"] = tk.BooleanVar()

        # Input widgets
        self.input_widgets["amtOfBotsWidget"] = ttk.Spinbox(
            input_frame, from_=1, to=3, textvariable=self.input_vars.get("amtOfBotsWidget"),
            validate="all", validatecommand=(self.register(self._validate_numbers_only),'%d', '%P', '%S','%V', '%s')
        )
        self.input_widgets["botDelayCheckWidget"] = ttk.Checkbutton(
            input_frame, variable= self.input_vars.get("botDelayCheckWidget")
        )

        self.input_widgets["amtOfBotsWidget"].grid(row=0, column=1, sticky=tk.EW, pady=5, padx=5)
        self.input_widgets["botDelayCheckWidget"].grid(row=1, column=1, sticky=tk.EW, pady=5, padx=5)

        ###########
        # Buttons #
        ###########
        ttk.Button(self, text="Quit", style="quit.startUpFrame.TButton", command=self.on_quit_button).pack(fill=tk.X, padx=25, pady=(5, 40), side=tk.BOTTOM)
        ttk.Button(self, text="Copyright", style="help.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)
        ttk.Button(self, text="Help", command=self.is_all_widgets_filled_in, style="help.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)
        ttk.Button(self, text="Play", style="play.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)

        logging.info("\n"
                     "------------------------------------------------\n"
                     "###### Startup Frame constructor finish ######\n"
                     "------------------------------------------------")

    def is_all_widgets_filled_in(self):
        items = []
        logging.info("Checking is all widgets filled")
        pass


    def get_inputs(self):
        ''' Get all inputs from input widgets

        :return: Dict {Widget name: Value}
        '''
        # todo this
        pass

    def resize_root(self):
        ''' Resizes root to size optimal for this frame

        :return: None
        '''
        logging.info("Resizing root for Startup_frame")
        self.top_level.set_root_min_size(
            self.STARTUP_FRAME_WIDTH,
            self.STARTUP_FRAME_HEIGHT
        )

    def on_quit_button(self):
        ''' Called when quit button pressed

        :return:
        '''
        logging.info("Quit button pressed on Startup Frame")
        self.top_level.quit_program()

    def on_help_button(self):
        ''' Called when help button pressed

        :return:
        '''
        pass

    def on_play_button(self):
        ''' Called when play button pressed

        :return:
        '''
        pass

    def goto_help_window(self):
        pass

    def goto_copyright_window(self):
        pass

    def goto_next_frame(self):
        pass

    def _validate_numbers_only(self, action, value_if_allowed, text, trigger_type, text_before_change):
        '''Private function. Not Meant to be accessed by other functions
        This function is used for the vertification of data
        https://infohost.nmt.edu/tcc/help/pubs/tkinter/web/entry-validation.html

        :param action: The type of action that is occuring
        :param value_if_allowed: The text inside entry if user input is allowed
        :param text: Text the user entered
        :param trigger_type: Type of event that occured. EG focusin, focusout...
        :return: True, Accept the user input
        :return: False: Reject the user input
        '''
        logging.debug("Spinbox validation run")
        if action == 0 or trigger_type == "forced":
            return True
        elif value_if_allowed == "":
            return True
        elif text in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if int(value_if_allowed) <= 3:
                return True
        return False
