'''IFrame.py

This is an interface for frames.
ALL frames being displayed must implement this interface.
'''
import tkinter as tk
from tkinter import ttk
class IFrame(ttk.Frame):
    def __init__(self, view, parent, top_level, style):
        super().__init__(parent)
        self.view = view
        self.parent = parent
        self.top_level = top_level
        self.style = style

        self.STARTUP_FRAME_WIDTH = int(self.view.SCREEN_WIDTH)  # Override to change min width
        self.STARTUP_FRAME_HEIGHT = int(self.view.SCREEN_HEIGHT) # Override to change min height

        self.frame_name = self.set_frame_name()
        self.input_widgets = {} # (str)widget_name : (obj) widget
        self.input_vars = {} # (str) widget_name: (obj) Var

    def set_frame_name(self):
        '''

        :return: Str
        '''
        raise Exception("Must be overwritten")

    def update_frame(self):
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
        return self.frame_name