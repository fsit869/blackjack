'''IFrame.py

This is an interface for frames.
ALL frames being displayed must implement this interface.
'''
import tkinter as tk
from tkinter import ttk
class IFrame(ttk.Frame):
    def __init__(self, view, parent, root, top_level, style, callbacks):
        ''' Init. ALL SUBCLASSES MUST CALL THIS ELSE EXCEPTION

        :param view:
        :param parent:
        :param top_level:
        :param style:
        '''
        super().__init__(parent)

        # Global variables each frame should implement and use
        self.view = view
        self.parent = parent
        self.top_level = top_level
        self.style = style
        self.root = root
        self.callbacks = callbacks

        self.STARTUP_FRAME_WIDTH = int(self.view.SCREEN_WIDTH)  # Override to change min width
        self.STARTUP_FRAME_HEIGHT = int(self.view.SCREEN_HEIGHT) # Override to change min height

        self.frame_name = self.set_frame_name() # Stores frame name
        self.input_widgets = {} # (str)widget_name : (obj) widget. Stores input widgets
        self.input_vars = {} # (str) widget_name: (obj) Var. Stores tkinter vars. EG STringVar

    def set_frame_name(self):
        ''' Set the name of the frame.
        Allows controller to choose what frame to display
        METHOD MUST BE OVERWRITTEN ELSE EXCEPTION

        :return: Str
        '''
        raise Exception("Must be overwritten")

    def update_frame(self, dict):
        ''' Update the frame with arguements from dict.
        If frame does not have anything to update, method does not need to be overwritten

        :param args:
        :return:
        '''
        pass

    def get_inputs(self):
        ''' Get all inputs from input widgets

           :return: Dict {Widget name: Value}
        '''
        input_vals = {}
        for widget_name, var_obj in self.input_vars.items():
            input_vals[widget_name] = var_obj.get()
        return input_vals

    def _resize_min_root(self):
        ''' Resizes root to size optimal for this frame

                :return: None
                '''
        self.view.set_root_min_size(
            self.STARTUP_FRAME_WIDTH,
            self.STARTUP_FRAME_HEIGHT
        )
        self.top_level.state('normal')

    def toString(self):
        ''' Get name of frame

        :return: Str
        '''
        return self.frame_name