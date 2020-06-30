''' Application.py

This file contains the root and entire GUI. This file is the controller of the program.

'''

import tkinter as tk
import logging
from tkinter import ttk
from tkinter import messagebox
from gui import Startup_frame, Game_frame, Style

class Application(tk.Tk):

    def __init__(self, application_name, *rootargs, **rootkwargs, ):
        ''' Constructor. Setup root and frames

        :param application_name: Root name
        :param rootargs: Root arguements
        :param rootkwargs: Root keywords
        '''

        # Config root settings
        logging.info("\n--------------------------------------------------\n"
                     "###### Application constructor begins ######\n"
                     "--------------------------------------------------")
        super().__init__(*rootargs, **rootkwargs)
        self.title(application_name)
        self.protocol('WM_DELETE_WINDOW', self.quit_program) # Override 'x' close button to safely exit
        # self.resizable(False, False)
        self.SCREEN_WIDTH = self.winfo_screenwidth()  # Display width
        self.SCREEN_HEIGHT = self.winfo_screenheight()  # Display height
        self.style = Style.Style()

        # Public vars
        self.frame_objects = {} # Stores frames
        self.startup_frame_settings = {} # Store settings from startup frame

        # Create frames
        logging.info("Creating frames for application")
        self._create_frames(Startup_frame.Startup_frame, Game_frame.Game_frame)

        self.show_frame("Startup_frame")
        # self.show_frame("Game_frame")
        self.centre_root()

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
        self.minsize(width, height)

    def centre_root(self):
        ''' Centre root to screen no matter the size.

        :return: None
        '''
        self.update_idletasks()

        _ROOT_HEIGHT = self.winfo_height() # Root height
        _ROOT_WIDTH = self.winfo_width() # Root width
        _FRM_WIDTH = self.winfo_rootx() - self.winfo_x() # Find size of outer frame
        _WIN_WIDTH = self.winfo_width() + (2 * _FRM_WIDTH) # True window width
        _TITLE_BAR_HEIGHT = self.winfo_rooty() - self.winfo_y() # Title bar height
        _WIN_HEIGHT = self.winfo_height() + (_TITLE_BAR_HEIGHT + _FRM_WIDTH) # True window height

        x = self.winfo_screenwidth() // 2 - _WIN_WIDTH // 2 # Coord placement
        y = self.winfo_screenheight() // 2 - _WIN_HEIGHT // 2 # Coord placement

        logging.info("Setting root window size (%d, %d) to (%d, %d)", _ROOT_WIDTH, _ROOT_HEIGHT, x, y)
        self.geometry("{}x{}+{}+{}".format(
            _ROOT_WIDTH,
            _ROOT_HEIGHT,
            x,
            y,
        ))


    def show_frame(self, frame_name):
        ''' Show the specified frame

        :param frame_name: Frame to show
        :return: None
        '''
        self.ungrid_all_widgets(self) # Forget all items on root
        logging.info("Displaying frame (%s)", frame_name)
        frame_to_display = self.frame_objects.get(frame_name) # Get frame to display
        self.columnconfigure(index=0, weight=1)
        self.rowconfigure(index=0, weight=1)
        frame_to_display.grid(row=0, column=0, sticky=tk.NSEW)
        frame_to_display.resize_min_root()


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

    def quit_program(self):
        ''' Safely quit from program
        :return: None
        '''
        logging.info("Program quit requested")
        quit = self.question_msg_frame("Quit", "Are you sure you would like to quit?\n"
                                               "Your current game will NOT save!")
        if quit == True:
            logging.info("Program quitting")
            exit()
        logging.info("Program terminated")

    def _create_frames(self, *frames_to_init):
        ''' Private method. Creates all frames listed in constructor and stores in self._frame_objects dict
        The name will be same as class name.

        :param frames_to_init: List class to create
        :return: None
        '''
        for frame in frames_to_init:
            frame_name = frame.__name__
            frame_object = frame(parent=self, top_level=self, style=self.style)  # Create frame obj
            self.frame_objects[frame_name] = frame_object  # Store frame for future reference
            logging.info("Creating [%s] frame", frame_name)
