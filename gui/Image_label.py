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
from tkinter import messagebox
from tkinter import ttk

class Image_label(ttk.Label):
    def __init__(self, parent, file_location, width, height, antialias=Image.ANTIALIAS):
        super().__init__(parent)
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
            self._display_error_message(file_location)
        self.configure(image=rendered_image)
        self.image = rendered_image

    def _display_error_message(self, file_location):
        messagebox.showerror("Error loading image", "Error in loading image \"{}\".\n"
                                                    " This image has been replaced with an error img."
                                                    "Note: The program will still continue to work ".format(file_location))

