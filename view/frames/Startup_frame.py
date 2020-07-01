''' Startup_frame.py

This frame contains the pre-grame frame. Aka startup_frame. It allows the user to change setting
before the game starts.

'''

import tkinter as tk
import logging
from view import Image_label
from view.frames.subframes import Copyright_window
from tkinter import ttk as ttk

class Startup_frame(ttk.Frame):
    def __init__(self, view, parent, top_level, style, callbacks):
        ''' Constructor to create Startup_frame
        ;:param view: View layer
        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        '''
        logging.info("\n--------------------------------------------------\n"
                     "###### Startup_Frame constructor begins ######\n"
                     "--------------------------------------------------")

        # Public variables
        self.top_level = top_level
        self.view = view
        self.style = style
        self.callbacks = callbacks
        self.input_widgets = {} # {widget_name:widget object}
        self.input_vars = {}

        self.STARTUP_FRAME_WIDTH = int(self.view.SCREEN_WIDTH / 4)
        self.STARTUP_FRAME_HEIGHT = int(self.view.SCREEN_HEIGHT / 1.5)


        # Setup Frame
        super().__init__(parent)

        # Title
        Image_label.Image_label(self, "resources/images/card_collections/aces.png", int(self.view.SCREEN_HEIGHT / 2.5),
                                int(self.view.SCREEN_WIDTH / 8.5)).pack()
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
        ttk.Label(input_frame, text="Disable Bot Delay:").grid(row=1, column=0, sticky=tk.W)

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
        ttk.Button(self, text="Quit", command=self.callbacks["startupFrame.quit"], style="quit.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=(5, 40), side=tk.BOTTOM)
        ttk.Button(self, text="Copyright", command=self._on_copyright_button, style="help.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)
        ttk.Button(self, text="Help", style="help.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)
        ttk.Button(self, text="Play", command=self.callbacks["startupFrame.play"], style="play.startUpFrame.TButton").pack(fill=tk.X, padx=25, pady=5, side=tk.BOTTOM)

        logging.info("\n"
                     "------------------------------------------------\n"
                     "###### Startup Frame constructor finish ######\n"
                     "------------------------------------------------")

    def get_inputs(self):
        ''' Get all inputs from input widgets

        :return: Dict {Widget name: Value}
        '''
        input_vals = {}
        for widget_name, var_obj in self.input_vars.items():
            logging.info("Getting value from %s widget", widget_name)
            input_vals[widget_name] = var_obj.get()
        return input_vals

    def _on_help_button(self):
        pass

    def _on_copyright_button(self):
        copyright_window = Copyright_window.Copyright_window()

    def _resize_min_root(self):
        ''' Resizes root to size optimal for this frame

        :return: None
        '''
        logging.info("Resizing root for Startup_frame")
        self.view.set_root_min_size(
            self.STARTUP_FRAME_WIDTH,
            self.STARTUP_FRAME_HEIGHT
        )
        self.top_level.state('normal')

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
            return False
        elif value_if_allowed == "":
            return False
        elif text in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
            if int(value_if_allowed) <= 3:
                return True
            elif int(value_if_allowed)>3 and text in ("1", "2", "3"):
                self.input_vars["amtOfBotsWidget"].set(text)
                return True

        return False
