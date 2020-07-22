'''PlayerFrame.py

Contains a class PlayerFrame. Each class represents one player to be
viewed on the player board in Game_frame.py.
'''


import tkinter as tk
import logging
from tkinter import ttk
from view import Image_label

class PlayerFrame(tk.Canvas):
    def __init__(self, parent, player_name, player_colour, is_player_alive, is_current_turn=False):
        ''' Creates a player frame

        :param parent: Parent to be attached too
        :param player_name: Name of player. Also will be name of widget
        :param player_colour: Colour of player
        :param is_player_alive: Bool, True=Alive, False=Dead
        :param is_current_turn: Bol, True=Current turn, False=Not player turn
        '''
        logging.info("Creating PlayerFRAME: {%s}", player_name)
        super().__init__(parent, name=player_name)
        self.player_colour = player_colour
        self.is_player_alive = is_player_alive
        self.is_current_turn = False

        self.widgets = {}
        self.configure(background="grey")

        self.widgets["player_name"] = ttk.Label(self, text=player_name.title(), style="alive.playerFrame.TLabel")
        self.widgets["is_player_alive"] = ttk.Label(self, text="ALIVE", style="alive.playerFrame.TLabel")

        self.widgets["player_name"].grid(row=0, column=0, padx=10, pady=10)
        self.widgets["is_player_alive"].grid(row=1, column=0, padx=10, pady=10)

        # Disable if dead
        if is_player_alive: self._on_dead_entity()

        # If current player turn
        if is_current_turn: self._on_current_turn()

    def _on_current_turn(self):
        ''' Restyles if current player turn
        :return: None
        '''
        self.configure(background="#d9e324")
        self.widgets["is_player_alive"].configure(style="currentTurn.playerFrame.TLabel")
        self.widgets["player_name"].configure(style="currentTurn.playerFrame.TLabel")

    def _on_dead_entity(self):
        ''' Restyles to if player is dead
        :return: None
        '''
        for widget_name, widget_object in self.widgets.items():
            widget_object.configure(state=tk.DISABLED)
        self.widgets["is_player_alive"].configure(text="BUST")