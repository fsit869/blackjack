''' GameModel.py

THis file contains the model layer of the MVC model.
Interacts with the controller and model objects.

'''
from model.deck import Deck, Card
from model.entities import Entity
from random import shuffle
from resources.PLAYERCONSTANTS import PLAYERCONSTANTS
from resources.CARDCONSTANTS import CARDCONSTANTS

class GameModel():
    def __init__(self):
        self.entities = None # Dict containing players
        self.deck = None # Stores the deck
        self.current_player_turn = None
        self.player_order = [] # Stores entity objs. This is player order
        self.cards_to_display = []

    def init_game(self, amt_bots, human_players=1):
        self.player_order = []  # Clears list

        if human_players<1 or human_players>1:
            raise AttributeError("Currently only one player is supported")
        else:
            self.player_order.append(Entity.Entity(False, "You"))

        # Create Bots
        _bot_name = 1
        for i in range(amt_bots):
            self.player_order.append(Entity.Entity(True, "bot_"+str(_bot_name)))
            _bot_name += 1

        # Shuffle player order
        shuffle(self.player_order)

        # Create deck
        self.deck = Deck.Deck()

        # Set first person turn
        self.current_player_turn = self.player_order[0]

    def next_entity(self, _iterations=0):
        ''' Next entity turn thats still alive and not stood

        :return:
        '''
        if _iterations>10:
            raise Exception("Unexpected error causing recursion.")

        current_player_index = self.player_order.index(self.current_player_turn)
        try:
            self.current_player_turn = self.player_order[current_player_index+1]
        except IndexError:
            self.current_player_turn = self.player_order[0]

        if (self.current_player_turn.get_status() != PLAYERCONSTANTS.ALIVE):
            _iterations += 1
            self.next_entity(_iterations=_iterations)

    def get_update_commands(self):
        dict_format = {
            PLAYERCONSTANTS: {
                "current_turn": self.current_player_turn.get_name(),
            },

            CARDCONSTANTS: self.cards_to_display
        }

        for player in self.player_order:
            player_name = player.get_name()
            player_status = player.get_status()
            player_card_amt = len(player.get_cards())
            dict_format[PLAYERCONSTANTS][player_name] = (player_status, player_card_amt)

        return dict_format








