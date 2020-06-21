import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from gui import Startup_frame

class Application(tk.Tk):

    def __init__(self, application_name, *rootargs, **rootkwargs, ):
        super().__init__(*rootargs, **rootkwargs)
        self.title(application_name)
        self.resizable(False, False)

        self.frame_objects = {} # Stores frames
        self._create_frames(Startup_frame.Startup_frame)
        self.show_frame("Startup_frame")
        self.centre_root()

    def centre_root(self):
        ''' Centre root to screen no matter the size.

        :return: None
        '''
        self.update_idletasks()
        _SCREEN_WIDTH = self.winfo_screenwidth() # Display width
        _SCREEN_HEIGHT = self.winfo_screenheight() # Display height
        _ROOT_HEIGHT = self.winfo_height() # Root height
        _ROOT_WIDTH = self.winfo_width() # Root width
        _FRM_WIDTH = self.winfo_rootx() - self.winfo_x() # Find size of outer frame
        _WIN_WIDTH = self.winfo_width() + (2 * _FRM_WIDTH) # True window width
        _TITLE_BAR_HEIGHT = self.winfo_rooty() - self.winfo_y() # Title bar height
        _WIN_HEIGHT = self.winfo_height() + (_TITLE_BAR_HEIGHT + _FRM_WIDTH) # True window height

        x = self.winfo_screenwidth() // 2 - _WIN_WIDTH // 2 # Coord placement
        y = self.winfo_screenheight() // 2 - _WIN_HEIGHT // 2 # Coord placement

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
        frame_to_display = self.frame_objects.get(frame_name) # Get frame to display
        frame_to_display.grid(row=0, column=0)

    def show_warning_frame(self, title, text):
        '''When called, Shows a msgbox warning type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        messagebox.showwarning(title, text)

    def show_error_frame(self, title, text):
        '''When called, shows msgbox error type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        messagebox.showerror(title, text)

    def question_msg_frame(self, title, text):
        answer = messagebox.askyesnocancel(title, text)
        return answer

    def unpack_all_widgets(self, window_to_unpack):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        window_slaves = window_to_unpack.pack_slaves()
        for widget in window_slaves:
            widget.pack_forget()

    def ungrid_all_widgets(self, window_to_ungrid):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        window_slaves = window_to_ungrid.grid_slaves()
        for widget in window_slaves:
            widget.grid_forget()

    def _create_frames(self, *frames_to_init):
        ''' Private method. Creates all frames listed in constructor and stores in self._frame_objects dict
        The name will be same as class name.

        :param frames_to_init: List class to create
        :return: None
        '''
        for frame in frames_to_init:
            frame_name = frame.__name__
            frame_object = frame(parent=self, top_level=self)  # Create frame obj
            self.frame_objects[frame_name] = frame_object  # Store frame for future reference
