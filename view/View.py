''' View.py

This file contains the root and entire GUI. This file is the controller of the program.

'''

import tkinter as tk
import logging
from tkinter import messagebox
from view import Style
from view.FrameUtilities import FrameUtitlies
from view.frames import Startup_frame, Game_frame




class View():

    def __init__(self, root, application_name):
        ''' Constructor. Setup root and frames

        :param application_name: Root name
        :param rootargs: Root arguements
        :param rootkwargs: Root keywords
        '''
        # Frames to inilized for program {referenceName : frameClass}

        self.frames_to_init = [
            Startup_frame.Startup_frame,
            Game_frame.Game_frame,
        ]
        self.frame_objects = {}  # Stores initlized frames {frame_name: frame_obj}

        # Public vars
        self.root = root
        self._current_frame = None

        self.style = Style.Style()

        # Config root settings
        self.root.title(application_name)
        # self.root.protocol('WM_DELETE_WINDOW', callbacks.get("quit")) todo fix
        self.SCREEN_WIDTH = self.root.winfo_screenwidth()  # Display width
        self.SCREEN_HEIGHT = self.root.winfo_screenheight()  # Display height

        # Create frames
        self._create_frames(self.frames_to_init)

    def set_root_min_size(self, width, height):
        ''' Set min size of root

        :param width: Min width
        :param height: Min height
        :return: None
        '''
        self.root.minsize(width, height)

    def show_frame(self, frame_name):
        ''' Show the specified frame

        :param frame_name: Frame to show
        :return: None
        '''
        FrameUtitlies.ungrid_all_widgets(self, self.root) # Forget all items on root
        frame_to_display = self.frame_objects.get(frame_name) # Get frame to display
        if frame_to_display == None:
            raise FileNotFoundError("Failed to load frame [{}]".format(frame_to_display))
            # todo better exception, maybe exit code 1.

        self.root.columnconfigure(index=0, weight=1)
        self.root.rowconfigure(index=0, weight=1)
        self.current_frame = frame_to_display
        frame_to_display.grid(row=0, column=0, sticky=tk.NSEW)
        frame_to_display._resize_min_root() # Method all frames have inhreited from IFrame
        self._centre_root()

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

    def _create_frames(self, frames_to_init):
        ''' Private method. Creates all frames listed in constructor and stores in self._frame_objects dict
        The name will be same as class name.

        :param frames_to_init: List class to create
        :return: None
        '''
        for frame_class in frames_to_init:
            frame_object = frame_class(
                view=self, parent=self.root, top_level=self.root,
                style=self.style
            )  # Create frame obj
            frame_name = frame_object.toString() # Method all IFrame's have
            self.frame_objects[frame_name] = frame_object  # Store frame for future reference

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
