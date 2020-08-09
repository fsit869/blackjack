''' Game_frame.py

This frame contains the game. Where the user will interact with
the game and other players. Contains the possible actions the player can take.

'''

import tkinter as tk
from tkinter import ttk
from view import IFrame, Image_label
from view.frames.subframes import PlayerFrame
from view.FrameUtilities import FrameUtitlies
from resources.CARDCONSTANTS import CARDCONSTANTS
from resources.PLAYERCONSTANTS import PLAYERCONSTANTS

class Game_frame(IFrame.IFrame):
    def __init__(self, view, parent, top_level, style):
        ''' Constructor to create Startup_frame

        :param parent: Parent
        :param top_level: Toplevel
        :param style: Style
        :param callbacks: Callbacks to access
        '''
        self._playersdict = None # Current players displayed.
        self._cards = None # Current cards displayed
        self._alarm_handler_obj = None # Reference for Config _on_resize

        # Frame settings
        super().__init__(view, parent, top_level, style)
        self.set_frame_name()
        # self._resize_min_root() # todo possibly delete check

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
        self.hit_button = ttk.Button(self.bot_frame, text="Hit", style="hitButton.gameFrame.TButton")
        self.stand_button = ttk.Button(self.bot_frame, text="Stand", style="standButton.gameFrame.TButton")

        self.text_info.grid(row=0, columnspan=2, sticky=tk.NSEW, padx=10)
        self.hit_button.grid(row=1, column=0, sticky=tk.NSEW, padx=10, pady=10)
        self.stand_button.grid(row=1, column=1, sticky=tk.NSEW, padx=10, pady=10)

        # Other additions
        self.disable_player_buttons(False) # Toggle buttons
        self.bind("<Configure>", self._on_resize) # Dynamic resizing
        # self.disable_player_buttons(True)

        # Debugging
        self.update_player_display({"current_turn": "player3",
                                     "player1": (PLAYERCONSTANTS.STOOD, 1),
                                     "player2": (PLAYERCONSTANTS.BUST, 2),
                                     "player3": (PLAYERCONSTANTS.ALIVE, 3),
                                     "player4": (PLAYERCONSTANTS.ALIVE, 4),
                                     "player5":(PLAYERCONSTANTS.ALIVE, 5)})
        self.update_card_display([CARDCONSTANTS.FOUR_C, CARDCONSTANTS.FIVE_C])

    def set_frame_name(self):
        ''' Overwritten from IFrame.py

        :return:
        '''
        return "Game_frame"

    def update_frame(self, dict):
        ''' Upates the players and cards

        {
        PLAYERCONSTANTS:
            {
                str(current_turn): str(player),
                str(player1): (PLAYERCONSTANTS.STOOD, 2),
                str(player2): (PLAYERCONSTANTS.ALIVE, 4),
                str(player3): (PLAYERCONSTANTS.STOOD, 2),
            },

        CARDCONSTANTS:
            [CARDCONSTANTS.FOUR_S, CARDCONSTANTS._FIVE_C]
        }

        :param dict:
        :return:
        '''
        self.update_player_display(dict.get(PLAYERCONSTANTS))
        self.update_card_display(dict.get(CARDCONSTANTS))

    def update_player_display(self, playersdict):
        ''' Updates the player board

        :return:
        '''
        self._playersdict = playersdict.copy() # Players_dict never none thus copy used
        if playersdict != None:
            FrameUtitlies.destory_children(self, self.top_frame)
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
            # Get max size of cards
            card_width = (self.view.get_root_width() / len(cards)) - 10 # -20 To allow space in side
            max_height = int(self.view.get_root_height() / 2.5) # Max pixel height of cards. (Prevents oversize)
            FrameUtitlies.destory_children(self, self.mid_frame)
            # Find ratio of card to fit into frame
            while(True):
                # Original card sizes
                original_width = CARDCONSTANTS.CARD_PIXEL_WIDTH.value
                original_height = CARDCONSTANTS.CARD_PIXEL_HEIGHT.value

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
                img = Image_label.Image_label(self.mid_frame, card, card.IMAGELOCATION(), style="cardBackground.gameFrame.TLabel")
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
        self.view.set_root_min_size(
            int(self.view.SCREEN_WIDTH/2),
            int(self.view.SCREEN_HEIGHT/2),
        )
        self.top_level.state('zoomed')

