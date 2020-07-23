''' Game_frame.py

This frame contains the game. Where the user will interact with
the game and other players. Contains the possible actions the player can take.

'''

import logging
import tkinter as tk
from tkinter import ttk as ttk
from resources import CARDCONSTANTS
from view import Image_label
from view.frames.subframes import PlayerFrame

class Game_frame(ttk.Frame):
    def __init__(self, view, parent, top_level, style, callbacks):
        ''' Constructor to create Startup_frame

        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        :param callbacks: Callbacks to access
        '''
        logging.debug("Game_frame constructor begins")

        # Public variables
        self.top_level = top_level
        self.view = view
        self.style = style
        self.callbacks = callbacks
        self.input_vars = {}
        self.input_widgets = {}

        self._playersdict = None # Current players displayed.
        self._cards = None # Current cards displayed

        self._alarm_handler_obj = None # Reference for Config _on_resize

        # Frame settings
        super().__init__(parent)
        self._resize_min_root() # Resizes root
        self.columnconfigure(0, weight=1)
        # self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        # Player Order (self.top_frame)
        self.top_frame = ttk.Frame(self, style="playerBoard.gameFrame.TFrame")
        self.top_frame.grid(row=0, column=0, sticky=tk.NSEW)

        # Card display (self.mid_frame)
        self.mid_frame = ttk.Frame(self, style="cardDisplay.gameFrame.TFrame")
        self.mid_frame.grid(row=1, column=0, sticky=tk.NSEW)
        ttk.Label(self.mid_frame, text="Your Cards").pack(padx=3)

        # Decision frame (self.bot_frame)
        self.bot_frame = ttk.Frame(self, style="decision.gameFrame.TFrame")
        self.bot_frame.columnconfigure(0, weight=1)
        self.bot_frame.columnconfigure(1, weight=1)
        self.bot_frame.rowconfigure(1, weight=1)
        self.bot_frame.grid(row=2, column=0, sticky=tk.NSEW)

        self.text_info = ttk.Label(self.bot_frame, anchor=tk.CENTER, style="statusBar.gameFrame.TLabel")
        self.hit_button = ttk.Button(self.bot_frame, text="Hit", style="hitButton.gameFrame.TButton", command=callbacks.get("gameFrame.hit"))
        self.stand_button = ttk.Button(self.bot_frame, text="Stand", style="standButton.gameFrame.TButton", command=callbacks.get("gameFrame.stand"))

        self.text_info.grid(row=0, columnspan=2, sticky=tk.NSEW, padx=10)
        self.hit_button.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.stand_button.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)

        # Other additions
        self.disable_player_buttons(False) # Toggle buttons
        self.bind("<Configure>", self._on_resize) # Dynamic resizing
        # self.disable_player_buttons(True)
        logging.debug("Game_frame constructor ends")

    def update_player_display(self, playersdict):
        ''' Updates the player board

        :return:
        '''
        self._playersdict = playersdict.copy() # Players_dict never none thus copy used
        if playersdict != None:
            logging.info("Updating player board")

            self.view.destory_children(self.top_frame)
            # playersdict = self.callbacks.get("game.getPlayers")()  # {str(current_player):player, str(player):bool(status)}
            current_turn = playersdict.pop("current_turn")

            for player in playersdict:
                player_frame = None
                if current_turn == player:
                    player_frame = PlayerFrame.PlayerFrame(
                        self.top_frame, player, "blue", playersdict.get(player)[0], playersdict.get(player)[1], True
                    )
                else:
                    player_frame = PlayerFrame.PlayerFrame(
                        self.top_frame, player, "blue", playersdict.get(player)[0], playersdict.get(player)[1], False
                    )
                player_frame.pack(side=tk.LEFT, expand=1, fill=tk.BOTH)

    def update_card_display(self, cards):
        ''' Update players card display

        :param cards: List/Tuple, Cards to display. (Use CARDCONSTANTS class)
        :return: None
        '''
        self._cards = cards # Card could be None type
        if cards != None:
            # Get size of cards
            card_width = (self.view.get_root_width() / len(cards)) - 10 # -20 To allow space in side
            max_height = int(self.view.get_root_height() / 2.5) # Max pixel height of cards. (Prevents oversize)
            self.view.destory_children(self.mid_frame)
            # Find ratio of card to fit into frame
            while(True):
                # Original card sizes
                original_width = CARDCONSTANTS.CARD_PIXEL_WIDTH
                original_height = CARDCONSTANTS.CARD_PIXEL_HEIGHT

                # Find percentage change of width, get according ratio height
                width_percentage_change = (card_width/original_width)
                new_height = int(original_height*width_percentage_change)

                # Check if height in boundaries, else reduce width and retry
                if new_height > max_height:
                    card_width -= 10
                else:
                    break

            # Pack cards
            for card in cards:
                logging.debug("Added card img %s", card)
                img = Image_label.Image_label(self.mid_frame, card, card, style="cardBackground.gameFrame.TLabel")
                img.resize_image_width_pixel_ratio(card_width)
                img.pack(side=tk.LEFT)

    def disable_player_buttons(self, bool):
        ''' Deactivate player buttons

        :param bool: If true, deactives buttons
        :return: None
        '''
        if bool == True:
            self.hit_button.configure(state=tk.DISABLED)
            self.stand_button.configure(state=tk.DISABLED)
            self.text_info.config(text="It is not your turn")
        elif bool == False:
            self.hit_button.configure(state=tk.NORMAL)
            self.stand_button.configure(state=tk.NORMAL)
            self.text_info.config(text="Your turn")
        else:
            logging.critical("Invaild key in disable_player_buttons")
            raise KeyError("Invalid key, bool required. Recieved type {}  [\"{}\"]".format(
                type(bool), bool
            ))

    def _on_resize(self, event):
        ''' Called when the window is resized.

        NOTE: ALARM HANDLER IS USED TO ALLOW DYNAMIC RESIZING OF WIDGETS WITHOUT CAUSING LAG
              The alarm handler will only execute the resize once changing of the frame has stopped.
              Without, the resize fuction will be spammed causing lag.

        :param event:event type, Configure
        :return: None
        '''
        if self._alarm_handler_obj != None: # If there is an existing alarm handler, delete
            self.after_cancel(self._alarm_handler_obj)

        # Alarm handler, executes _on_resize_actions after 200ms
        self._alarm_handler_obj = self.after(300, self._on_resize_actions)

    def _on_resize_actions(self):
        ''' Refer to _on_resize method. This method is the actions it wil take after resizing.

        :return: None
        '''
        self.update_card_display(self._cards)
        self.update_player_display(self._playersdict)

    def _resize_min_root(self):
        ''' Resize frame and apply min size

        :return:
        '''
        logging.info("Resizing root for Game_frame")
        self.view.set_root_min_size(
            int(self.view.SCREEN_WIDTH/2),
            int(self.view.SCREEN_HEIGHT/2),
        )
        self.top_level.state('zoomed')

