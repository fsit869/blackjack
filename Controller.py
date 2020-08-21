''' Controller.py

This is the controller layer of the MVC model.
Responsible for communicating between view and controller.
It is also responsible for controlling the flow of the program
'''
import tkinter as tk
import logging
from view import View
from model import GameModel
from resources.CARDCONSTANTS import CARDCONSTANTS
from resources.PLAYERCONSTANTS import PLAYERCONSTANTS

class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        # Public variables
        self.callbacks = {
            "startup_game": self.start_game,
            "on_stand": self.on_stand_button,
            "on_hit": self.on_hit_button,
            "quit_program": self.quit_program
        }
        self.view = View.View(self, "Blackjack", self.callbacks) # View object
        self.model = GameModel.GameModel()

        # Init commands
        self.view.show_frame("Startup_frame")
        # self.view.update_frame({
        #     PLAYERCONSTANTS: {
        #         "current_turn": "player1",
        #         "player1": (PLAYERCONSTANTS.STOOD, 4),
        #         "player2": (PLAYERCONSTANTS.BUST, 2),
        #         "player3": (PLAYERCONSTANTS.ALIVE, 2),
        #     },
        #
        #     CARDCONSTANTS: [
        #         CARDCONSTANTS.CARD_FOUR_S,
        #         CARDCONSTANTS.CARD_TEN_H
        #     ]
        #
        # })

    def start_game(self):
        ''' Called at end of startup_frame.

        :return:
        '''
        startup_input_vals = self.view.get_inputs()
        amount_of_bots = startup_input_vals.get("amtOfBotsWidget")
        bot_delay = startup_input_vals.get("botDelayCheckWidget") # todo maye have botdelay a slider. If 0 it off. seconds
        self.view.show_frame("Game_frame")
        self.model.init_game(amount_of_bots)
        self.view.update_frame(self.model.get_update_commands())

    def on_hit_button(self):
        self.model.current_entity_hit()
        self.game_loop()

    def on_stand_button(self):
        self.model.current_entity_stand()
        self.game_loop()

    def game_loop(self):
        ''' Called when hit or stand button pressed

        :return:
        '''
        self.view.update_frame(self.model.get_update_commands())
        current_entity_status = self.model.return_new_player_status()
        if current_entity_status == PLAYERCONSTANTS.WIN:
            # CHeck if player stood to win
            print("Game winner")
            self.view.show_frame("Startup_frame")
            return
        elif current_entity_status == PLAYERCONSTANTS.BUST:
            self.model.current_entity_set_status(PLAYERCONSTANTS.BUST)

        if self.model.is_game_playable():
            self.model.next_entity()
        else:
            print("Game end")
            self.view.show_frame("Startup_frame")
            return

        self.view.update_frame(self.model.get_update_commands())
        # If bot then handle decision itself



        #
        # if self.model.is_current_entity_bot():
        #     # do bot calculation
        #     # View disable clicky buttons
        #     # Bot timer
        #     pass
        # else:
        #     pass
        #     # Enable clicky
        #     #




    def quit_program(self): # todo maybe move this to view??? IDK
        ''' Safely quit from program
        :return: None
        '''
        logging.info("Program quit requested")
        quit = self.view.question_msg_frame("Quit", "Would you like to quit?\n"
                                                    "YOUR GAME WILL NOT BE SAVED!")
        if quit == True:
            logging.info("Program quitting")
            exit()
        logging.info("Program terminated")