import tkinter as tk
from tkinter import ttk

class Style(ttk.Style):
    def __init__(self):
        super().__init__()
        self.configure('defaultBackground.TFrame', background='lightgrey')
