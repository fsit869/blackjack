import tkinter as tk


class Application(tk.Tk):
    def __init__(self, application_name, *rootargs, **rootkwargs, ):
        super().__init__(*rootargs, **rootkwargs)
        self.title(application_name)
        self.resizable(False, False)

    def create_first_frame(self):
        pass
