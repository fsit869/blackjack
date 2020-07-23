''' Style.py

File contains the styling for all the ttk widgets in the program.
This allows for all the styling in one place.

'''

import tkinter as tk
from tkinter import ttk
from tkinter.font import Font

class Style(ttk.Style):
    def __init__(self):
        ''' Constructor, Creates styles for entire GUI.
        '''
        super().__init__()
        self.DEFAULT_BACKGROUND_COLOUR = "lightgrey"

        # Themes ('winnative', 'clam', 'alt', 'default', 'classic', 'vista', 'xpnative')
        # class.winfo_class
        self.theme_use("clam")

        # Default Backgrounds
        self.configure('TFrame', background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("TLabel", background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("TCheckbutton", background=self.DEFAULT_BACKGROUND_COLOUR)
        self.configure("title.default.TLabel", background=self.DEFAULT_BACKGROUND_COLOUR,
                       font=Font(family="Lucida Grande", size=10))

        # Startup Frame
        self.configure("play.startUpFrame.TButton", )
        self.configure("help.startUpFrame.TButton", )
        self.configure("quit.startUpFrame.TButton", )

        ##############
        # Game Frame #
        ##############
        self.configure("playerBoard.gameFrame.TFrame", background="brown")
        self.configure("cardDisplay.gameFrame.TFrame", background="darkgreen")
        self.configure("decision.gameFrame.TFrame", background="#82411b")

        self.configure("cardBackground.gameFrame.TLabel", background="darkgreen")
        self.configure("statusBar.gameFrame.TLabel", background="#82411b")

        self.configure("hitButton.gameFrame.TButton", background="brown",font="Arial 40 bold")
        self.configure("standButton.gameFrame.TButton", background="brown",font="Arial 40 bold")

        # Player Frame
        self.configure("currentTurn.playerFrame.TLabel", background="#d9e324", font="Times 10 bold")
        self.configure("alive.playerFrame.TLabel", background="grey", font="Times 10 bold")
        self.map("alive.playerFrame.TLabel",
                 background=[('disabled', 'grey')],
                 foreground=[('disabled', "#403f3c")]
                 )
