''' Controller.py

This is the controller layer of the MVC model.
Responsible for communicating between view and controller.
It is also responsible for controlling the flow of the program
'''
import tkinter as tk
import logging
from view import View
from model import GameModel
from resources import CARDCONSTANTS, PLAYERCONSTANTS

class GAMEPHASE:
    ''' Constants in the phase of the game. This class cannot be initiated. Else
    an exception is raised.
    '''
    def __init__(self):
        raise Exception("GAMEPHASE CANNOT BE INITIATED")

    STARTUP = 0
    GAMEFRAME = 1
    ENDFRAME = 2


class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        # Public variables
        self.view = View.View(self, "Blackjack") # View object
        # self.model = GameModel.GameModel()

        self.view.show_frame("Game_frame")

    def start_game(self):
        pass

    def game_loop(self):
        pass

    def quit_program(self):
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