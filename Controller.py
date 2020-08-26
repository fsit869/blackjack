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
            "quit_program": self.quit_program,
            "start_frame": self._goto_start_frame,
        }
        self.view = View.View(self, "Blackjack", self.callbacks) # View object
        self.model = GameModel.GameModel()

        # Init commands
        self.view.show_frame("Startup_frame")
        # self.view.show_frame("End_frame")

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
        self.game_loop()

    def on_hit_button(self): # maybe for player add alil delay so can see wut he picked up???
        self.model.current_entity_hit()
        self.game_loop()

    def on_stand_button(self):
        self.model.current_entity_stand()
        self.game_loop()

    def game_loop(self):
        ''' Called when hit or stand button pressed

        :return:
        '''
        self.view.update_frame(self.model.get_update_commands()) # Todo possibily remove
        current_entity_status = self.model.get_player_win_status()
        if (current_entity_status == PLAYERCONSTANTS.WIN) and (self.model.get_current_entity_status()==PLAYERCONSTANTS.STOOD):
            # CHeck if player stood to win
            self.model.current_entity_set_win()
            print("Game winner")
            self.end_game()
            return None
        elif current_entity_status == PLAYERCONSTANTS.BUST:
            self.model.current_entity_set_status(PLAYERCONSTANTS.BUST)

        if self.model.is_game_playable():
            self.model.next_entity()
        else:
            print("Game end")
            self.end_game()
            return None

        if self.model.get_current_entity_is_bot():
            # todo bot calculations here, must disable player GUI buttons
            # todo bot delay, must have some indicator??
            # Must check less than= 21 to do perform
            if self.model.get_card_total() <=21:
                bot_action = self.model.get_bot_decision()
                if bot_action == PLAYERCONSTANTS.STAND:
                    self.on_stand_button()
                elif bot_action == PLAYERCONSTANTS.HIT:
                    self.on_hit_button()
                else:
                    raise AttributeError("Unexpected error, did not get stand or hit")

        self.view.update_frame(self.model.get_update_commands())

    def end_game(self):
        self.view.show_frame("End_frame")
        self.view.update_frame(self.model.get_end_game_stats())

    def quit_program(self): # todo maybe move this to view??? IDK
        ''' Safely quit from program
        :return: None
        '''
        quit = self.view.question_msg_frame("Quit", "Would you like to quit?\n"
                                                    "YOUR GAME WILL NOT BE SAVED!")
        if quit == True:
            logging.info("Program quitting")
            exit()

    def _goto_start_frame(self):
        self.view.show_frame("Startup_frame")