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
        self.GAMEPHASE = None # Set to None as not initialized yet

        # CALLBACKS. This will be used in the view layer. Used to get data from model to view
        self.CALLBACKS = {
            "startupFrame.play": self.goto_Game_Frame,
            "startupFrame.quit": self.quit_program,

            "gameFrame.hit": self.on_hit,
            "gameFrame.stand": self.on_stand,

            "game.getPlayers":self.get_players,

            "quit":self.quit_program,
        }

        self.view = View.View(self, "Blackjack", self.CALLBACKS) # View object

        # Actions
        self.set_game_phase("startup")
        self.view.show_frame("Startup_frame")
        # self.view.show_frame("Game_frame")

    def set_game_phase(self, phase):
        ''' Set the game phase

        :param GAMEPHASE: String
        :return: None
        '''
        if phase == "startup":
            self.GAMEPHASE = GAMEPHASE.STARTUP
        elif phase == "gameframe":
            self.GAMEPHASE = GAMEPHASE.GAMEFRAME
        elif phase == "endframe":
            self.GAMEPHASE = GAMEPHASE.ENDFRAME
        else:
            raise KeyError("Unknown KEY PHASE, [{}]".format(phase))

    def get_players(self):
        ''' Get players from the model
            {
                (str) current_turn : (str) player,
                (str) playername : (bool) Dead
            }
        :return: Dict
        '''
        return {
            "current_turn": "player4",
            "player1": True,
            "player2": True,
            "player3": False,
            "player4": False
        }
        # todo

    def on_stand(self):
        # todo
        print("Stand")
        pass

    def on_hit(self):
        pass

    def goto_Startup_Frame(self):
        ''' Switch to startup frame

        :return: None
        '''
        self.set_game_phase("startup")
        pass

    def goto_Game_Frame(self):
        ''' Switch to game frame

        :return:
        '''
        input_vals = self.view.current_frame.get_inputs()
        # print(input_vals)
        self.set_game_phase("gameframe")
        self.view.show_frame("Game_frame")
        self.view.update_game_frame({"current_turn": "player3",
                                     "player1": PLAYERCONSTANTS.STOOD,
                                     "player2": PLAYERCONSTANTS.BUST,
                                     "player3": PLAYERCONSTANTS.ALIVE,
                                     "player4": PLAYERCONSTANTS.ALIVE,
                                     "player5":PLAYERCONSTANTS.ALIVE},
                                    None, False)

    def game_Loop(self):
        ''' Game loop
        :return:
        '''
        # todo Loop called whenever player presses the hit or stand button
        # Here decides wut player does
        # Here does bot action
        # Here does update screen
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