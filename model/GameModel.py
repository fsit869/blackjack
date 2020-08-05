''' GameModel.py

THis file contains the model layer of the MVC model.
Interacts with the controller and model objects.

'''
class GameModel():
    def __init__(self):
        self.players = None
        self.cards = None
        self.current_deck = None

    def init_game(self, amt_bots, bot_delay):
        ''' Initlize a new game

        :param amt_bots: (int) Amt of bots
        :param bot_delay: (bool) Bot delay
        :return: None
        '''




