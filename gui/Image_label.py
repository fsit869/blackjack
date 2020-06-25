''' Image_label.py

This file will contain a image ready to be displayed in Tkinter.

####### IMPORTANT ###############
Requires the use of Pillow
https://pypi.org/project/Pillow/
#################################

'''


import tkinter as tk
import logging
from PIL import Image, ImageTk
from tkinter import ttk

class Image_label(tk.Label):
    def __init__(self, parent, file_location, width, height, background_colour=None, antialias=Image.ANTIALIAS):
        super().__init__(parent, bg=background_colour)
        rendered_image = ""

        try: # Load image
            logging.info("Trying to load image [%s] width, height (%d, %d)", file_location, width, height)
            load_image = Image.open(file_location)
            load_image = load_image.resize((width, height), antialias)
            rendered_image = ImageTk.PhotoImage(load_image)

        except Exception as e: # If unable to load image
            logging.error("Failed to load image [%s], Replacing with failed to load img", file_location)
            load_image = Image.open("gui/images/no_image_avaliable.png")
            load_image = load_image.resize((width, height), antialias)
            rendered_image = ImageTk.PhotoImage(load_image)
        self.configure(image=rendered_image)
        self.image = rendered_image

