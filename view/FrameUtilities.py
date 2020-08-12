'''FrameUtilties.py

Class provides utilties to modify frames

'''

from tkinter import messagebox
import logging

class FrameUtitlies:
    def __init__(self):
        pass

    @staticmethod
    def show_warning_frame(self, title, text):
        '''When called, Shows a msgbox warning type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        logging.warning("Displaying warning msgbox, %s, %s", title, text)
        messagebox.showwarning(title, text)

    @staticmethod
    def show_error_frame(self, title, text):
        '''When called, shows msgbox error type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return: None
        '''
        logging.error("Displaying err msgbox, %s, %s", title, text)
        messagebox.showerror(title, text)

    @staticmethod
    def question_msg_frame(self, title, text):
        ''' When called, shows msgbox question type

        :param title: Title of msgbox
        :param text: Text content of msgbox
        :return:
        '''
        logging.debug("Displaying msgbox, %s, %s", title, text)
        answer = messagebox.askyesnocancel(title, text)
        return answer

    @staticmethod
    def unpack_all_widgets(self, window_to_unpack):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        logging.info("Unpacking all widgets from %s", window_to_unpack.__class__)
        window_slaves = window_to_unpack.pack_slaves()
        for widget in window_slaves:
            widget.pack_forget()

    @staticmethod
    def ungrid_all_widgets(self, window_to_ungrid):
        ''' Unpack all widgets from a specified frame/root

        :param window_to_ungrid: Frame/root object to ungrid
        :return: None
        '''
        logging.info("Ungridding all widgets from %s", window_to_ungrid.__class__)
        window_slaves = window_to_ungrid.grid_slaves()
        for widget in window_slaves:
            widget.grid_forget()

    @staticmethod
    def destory_children(self, parent_frame):
        ''' Destroy all children from a frame

        :param parent_frame: Frame to destroy children
        :return:
        '''
        for child in parent_frame.winfo_children():
            child.destroy()