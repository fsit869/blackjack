import tkinter as tk
import logging
from view import View
from model import GameModel

# GAMEPHASE = {
#     "startup" : 0,
#     "gameframe": 1,
#     "endframe": 2,
# }
class GAMEPHASE:
    STARTUP = 0
    GAMEFRAME = 1
    ENDFRAME = 2



class Controller(tk.Tk):
    def __init__(self):
        super().__init__()

        # Public variables
        self.GAMEPHASE = None # Set to None as not initialized yet
        self.set_game_phase("startup")

        self.CALLBACKS = {
            "startupFrame.play": self.goto_Game_Frame,
            "startupFrame.quit": self.quit_program,
        }

        self.view = View.View(self, "Blackjack", self.CALLBACKS)

    def set_game_phase(self, phase):
        ''' Set the game pahse

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

    def goto_Startup_Frame(self):
        pass

    def goto_Game_Frame(self):
        input_vals = self.view.current_frame.get_inputs()
        self.set_game_phase("gameframe")
        self.view.show_frame("Game_frame")

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