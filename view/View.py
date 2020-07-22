''' View.py

This file contains the root and entire GUI. This file is the controller of the program.

'''

import tkinter as tk
import logging
from tkinter import messagebox
from view import Style
from view.frames import Startup_frame, Game_frame


class View():

    def __init__(self, root, application_name, callbacks):
        ''' Constructor. Setup root and frames

        :param application_name: Root name
        :param rootargs: Root arguements
        :param rootkwargs: Root keywords
        '''
        # Frames to inilized for program {referenceName : frameClass}
        self.frames_to_init = {
            "Startup_frame": Startup_frame.Startup_frame,
            "Game_frame": Game_frame.Game_frame,
        }


        # Public vars
        self.root = root
        self.current_frame = None
        self.frame_objects = {}  # Stores initlized frames
        self.style = Style.Style()
        self.callbacks = callbacks

        # Config root settings
        logging.info("\n--------------------------------------------------\n"
                     "###### Application constructor begins ######\n"
                     "--------------------------------------------------")
        self.root.title(application_name)
        self.root.protocol('WM_DELETE_WINDOW', callbacks.get("quit"))
        # self.root.resizable(False, False)
        self.SCREEN_WIDTH = self.root.winfo_screenwidth()  # Display width
        self.SCREEN_HEIGHT = self.root.winfo_screenheight()  # Display height

        # Create frames
        logging.info("Creating frames for application")
        self._create_frames(self.frames_to_init)

        logging.info("\n"
                     "------------------------------------------------\n"
                     "###### Application constructor finish ######\n"
                     "------------------------------------------------")

    def set_root_min_size(self, width, height):
        ''' Set min size of root

        :param width: Min width
        :param height: Min height
        :return: None
        '''
        logging.info("Setting root min size to %d %d", width, height)
        self.root.minsize(width, height)

    def show_frame(self, frame_name):
        ''' Show the specified frame

        :param frame_name: Frame to show
        :return: None
        '''
        self.ungrid_all_widgets(self.root) # Forget all items on root
        logging.info("Displaying frame (%s)", frame_name)
        frame_to_display = self.frame_objects.get(frame_name) # Get frame to display
        if frame_to_display == None:
            raise FileNotFoundError("Failed to load frame [{}]".format(frame_to_display))
            # todo better exception, maybe exit code 1.

        self.root.columnconfigure(index=0, weight=1)
        self.root.rowconfigure(index=0, weight=1)
        self.current_frame = frame_to_display
        frame_to_display.grid(row=0, column=0, sticky=tk.NSEW)
        frame_to_display._resize_min_root()
        self._centre_root()

    def update_game_frame(self, players, cards, enable_buttons):
        ''' Update contents from game frame

        :param players: dict Players to update
        :param cards: List Cards to update
        :param enable_buttons: Bool.
        :return: None
        '''
        if type(self.current_frame) != Game_frame.Game_frame:
            raise Exception("Incorrect frame chosen")
        self.current_frame.update_player_display(players)
        self.current_frame.update_card_display(cards)
        self.current_frame.disable_player_buttons(enable_buttons)

    def show_warning_frame(self, title, text):
        '''When called, Shows a msgbox warning type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        logging.warning("Displaying warning msgbox, %s, %s", title, text)
        messagebox.showwarning(title, text)

    def show_error_frame(self, title, text):
        '''When called, shows msgbox error type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        logging.error("Displaying err msgbox, %s, %s", title, text)
        messagebox.showerror(title, text)

    def question_msg_frame(self, title, text):
        ''' When called, shows msgbox question type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return:
        '''
        logging.debug("Displaying msgbox, %s, %s", title, text)
        answer = messagebox.askyesnocancel(title, text)
        return answer

    def unpack_all_widgets(self, window_to_unpack):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        logging.info("Unpacking all widgets from %s", window_to_unpack.__class__)
        window_slaves = window_to_unpack.pack_slaves()
        for widget in window_slaves:
            widget.pack_forget()

    def ungrid_all_widgets(self, window_to_ungrid):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        logging.info("Ungridding all widgets from %s", window_to_ungrid.__class__)
        window_slaves = window_to_ungrid.grid_slaves()
        for widget in window_slaves:
            widget.grid_forget()

    def destory_children(self, parent_frame):
        ''' Destroy all children from a frame

        :param parent_frame: Frame to destroy children
        :return:
        '''
        for child in parent_frame.winfo_children():
            child.destroy()

    def _create_frames(self, frames_to_init):
        ''' Private method. Creates all frames listed in constructor and stores in self._frame_objects dict
        The name will be same as class name.

        :param frames_to_init: List class to create
        :return: None
        '''
        for frame_name, frame_class in frames_to_init.items():
            frame_object = frame_class(
                view=self, parent=self.root, top_level=self.root,
                style=self.style, callbacks=self.callbacks
            )  # Create frame obj
            self.frame_objects[frame_name] = frame_object  # Store frame for future reference
            logging.info("Creating [%s] frame", frame_name)

    def get_root_width(self):
        ''' Get root width

        :return: int
        '''
        # Force update frame
        self.root.update_idletasks()
        self.root.update()
        return self.root.winfo_width() # Root width

    def get_root_height(self):
        ''' Get root height

        :return: int
        '''
        # Force update frame
        self.root.update_idletasks()
        self.root.update()
        return self.root.winfo_height()  # Root height

    def _centre_root(self):
        ''' Centre root to screen no matter the size.

        :return: None
        '''
        self.root.update_idletasks()
        self.root.update()

        _ROOT_HEIGHT = self.get_root_height()
        _ROOT_WIDTH = self.get_root_width()
        _FRM_WIDTH = self.root.winfo_rootx() - self.root.winfo_x() # Find size of outer frame
        _WIN_WIDTH = self.root.winfo_width() + (2 * _FRM_WIDTH) # True window width
        _TITLE_BAR_HEIGHT = self.root.winfo_rooty() - self.root.winfo_y() # Title bar height
        _WIN_HEIGHT = self.root.winfo_height() + (_TITLE_BAR_HEIGHT + _FRM_WIDTH) # True window height

        x = self.root.winfo_screenwidth() // 2 - _WIN_WIDTH // 2 # Coord placement
        y = self.root.winfo_screenheight() // 2 - _WIN_HEIGHT // 2 # Coord placement

        logging.info("Setting root window size (%d, %d) to (%d, %d)", _ROOT_WIDTH, _ROOT_HEIGHT, x, y)
        self.root.geometry("{}x{}+{}+{}".format(
            _ROOT_WIDTH,
            _ROOT_HEIGHT,
            x,
            y,
        ))
