''' Image_label.py

This file will contain a image ready to be displayed in Tkinter.
Image is stored through a label.

####### IMPORTANT ###############
Requires the use of Pillow
https://pypi.org/project/Pillow/
#################################

'''

import logging
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import ttk


class Image_label(ttk.Label):
    def __init__(self, parent, image_name, file_location, width=None, height=None, style=None, antialias=Image.ANTIALIAS):
        ''' Constructor

        :param parent: Parent of where image label will be placed
        :param image_name: Name of widget (For referencing)
        :param file_location: File location of image
        :param width: Custom width (Ignore for default size)
        :param height: Custom height (Ignore for default size)
        :param antialias: Custom antialias (Ignore for default Image.Antialias)
        '''
        super().__init__(parent) # name=image_name may potentially cause crashes check.
        self.configure(style=style)
        self.parent = parent
        self.image_name = image_name
        self.file_location = file_location
        self.load_image = ""
        self.rendered_image = ""

        self.RAW_WIDTH = None
        self.RAW_HEIGHT = None

        self._load_image()
        if (width != None) and (height != None):
            self.resize_image(width, height)
        self._update_image()

    def get_image_name(self):
        ''' Get name of image label

        :return: String
        '''
        return self.image_name

    def resize_image(self, width, height, antialias=Image.ANTIALIAS):
        ''' Resize the image to a fixed size

        :param width: Custom width
        :param height: Custom height
        :param antialias: Custom antialias (Ignore for default Image.Antialias)
        :return: None
        '''
        logging.info("Resizing  [%s} to ({%d},{%d})", self.image_name, width, height)
        self._load_image()
        self.load_image = self.load_image.resize((width, height), antialias)
        self._update_image()

    def resize_image_height_pixel_ratio(self, height_pixels, antialias=Image.ANTIALIAS):
        ''' Resize to specified height. The width will be automatically resized according to img ratio

        :param height_pixels: Int
        :param antialias: Type of antialias
        :return: None
        '''
        percentage_change = (height_pixels / self.RAW_HEIGHT)
        NEW_WIDTH = int(self.RAW_WIDTH * percentage_change)
        NEW_HEIGHT = int(self.RAW_HEIGHT * percentage_change)
        self.resize_image(NEW_WIDTH, NEW_HEIGHT, antialias)

    def resize_image_width_pixel_ratio(self, width_pixels, antialias=Image.ANTIALIAS):
        ''' Resize to specified height. The height will be automatically resized according to img ratio

        :param width_pixels: Int
        :param antialias: Type of antialias
        :return: None
        '''
        percentage_change = (width_pixels / self.RAW_WIDTH)
        NEW_WIDTH = int(self.RAW_WIDTH * percentage_change)
        NEW_HEIGHT = int(self.RAW_HEIGHT * percentage_change)
        self.resize_image(NEW_WIDTH, NEW_HEIGHT, antialias)

    def _load_image(self):
        ''' Private method. Loads the image

        :return: None
        '''
        try:  # Load image
            logging.info("Trying to load image [%s]", self.file_location)
            self.load_image = Image.open(self.file_location)
            self.RAW_WIDTH = self.load_image.width
            self.RAW_HEIGHT = self.load_image.height

        except Exception as e:  # If unable to load image
            logging.critical("Failed to load image [%s], Replacing with failed to load img", self.file_location)
            self.load_image = Image.open("resources/images/no_image_avaliable.png")
            self._display_error_message()

    def _update_image(self):
        ''' Update image labe. Must be called after changes to image

        :return: None
        '''
        self.rendered_image = ImageTk.PhotoImage(image=self.load_image)
        self.configure(image=self.rendered_image)

    def _display_error_message(self):
        ''' Display error message of unable to open image

        :return: None
        '''
        messagebox.showerror(
            "Error loading image", "Error in loading image \"{}\".\n"
                                   " This image has been replaced with an error img."
                                   "Note: The program will still continue to work ".format(self.file_location)
        )
