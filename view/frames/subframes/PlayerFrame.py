'''PlayerFrame.py

Contains a class PlayerFrame. Each class represents one player to be
viewed on the player board in Game_frame.py.
'''


import tkinter as tk
import logging
from tkinter import ttk
from view import Image_label
from resources.PLAYERCONSTANTS import PLAYERCONSTANTS

class PlayerFrame(tk.Canvas):
    def __init__(self, parent, player_name, player_colour, player_status, cards, is_current_turn=False):
        ''' Creates a player frame

        :param parent: Parent to be attached too
        :param player_name: Name of player. Also will be name of widget
        :param player_colour: Colour of player
        :param player_status: int. Reference to PLAYERCONSTANTS.py
        :param is_current_turn: Bol, True=Current turn, False=Not player turn
        :param cards int, Amt of cards the player has.
        '''
        logging.info("Creating PlayerFRAME: {%s}", player_name)
        super().__init__(parent, name=player_name)
        self.player_colour = player_colour
        self.player_status = player_status
        self.is_current_turn = False

        self.widgets = {}
        self.configure(background="grey")

        self.widgets["player_name"] = ttk.Label(self, text=player_name.title(), style="alive.playerFrame.TLabel")
        self.widgets["is_player_alive"] = ttk.Label(self, text="ALIVE", style="alive.playerFrame.TLabel")

        self.widgets["player_name"].grid(row=0, column=0, padx=10, pady=10)
        self.widgets["is_player_alive"].grid(row=1, column=0, padx=10, pady=10)

        self.columnconfigure(1, weight=1)
        card_img = Image_label.Image_label(self, "card_back", "resources/images/card_backs/red_back.png")
        card_img.resize_image_height_pixel_ratio(30)
        card_img.grid(row=0, column=1, sticky=tk.E, rowspan=2)

        # Widget not within dict as itll be disabled when bust.
        self.card_amt = ttk.Label(self, text=("Cards: "+str(cards)), style="alive.playerFrame.TLabel")
        self.card_amt.grid(row=0, column=2, sticky=tk.W, rowspan=2, padx=10)

        # Disable if dead # todo check wtf this is
        if player_status == PLAYERCONSTANTS.BUST: self._on_dead_entity()
        if player_status == PLAYERCONSTANTS.STOOD: self._on_stood_entity()

        # If current player turn
        if is_current_turn: self._on_current_turn()

    def _on_current_turn(self):
        ''' Restyles if current player turn
        :return: None
        '''
        self.configure(background="#d9e324")
        self.widgets["is_player_alive"].configure(style="currentTurn.playerFrame.TLabel")
        self.widgets["player_name"].configure(style="currentTurn.playerFrame.TLabel")
        self.card_amt.configure(style="currentTurn.playerFrame.TLabel")


    def _on_stood_entity(self):
        ''' Restyles to if player is stood

        :return:
        '''
        self._disable_widgets()
        self.widgets["is_player_alive"].configure(text="STOOD")


    def _on_dead_entity(self):
        ''' Restyles to if player is dead
        :return: None
        '''
        self._disable_widgets()
        self.widgets["is_player_alive"].configure(text="BUST")

    def _disable_widgets(self):
        # todo need to ignore card symbol & amt
        for widget_name, widget_object in self.widgets.items():
            widget_object.configure(state=tk.DISABLED)
