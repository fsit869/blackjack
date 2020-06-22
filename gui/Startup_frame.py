import tkinter as tk
from tkinter import ttk as ttk

class Startup_frame(ttk.Frame):
    def __init__(self, parent, top_level, style):
        self.top_level = top_level
        self.style = style

        self.top_level.set_root_min_size(
            int(self.top_level.SCREEN_WIDTH / 4),
            int(self.top_level.SCREEN_HEIGHT / 1.5),
        )
        super().__init__(parent, style="defaultBackground.TFrame")

        self.input_vars = {}
        self.input_widgets = {}

