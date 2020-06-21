import tkinter as tk
from tkinter import ttk as ttk

class Startup_frame(ttk.Frame):
    def __init__(self, parent, top_level):
        super().__init__(parent)
        self.top_level = top_level

