''' Entity.py

Contains a abstract class Entity.py. This contains all the methods and functions needed
for a player/bot. This class is abstract. CANNOT be initiated. Rather it is implemented.

Python does not have built in abstract classes compared to other languages such as java.
Therefore a library is used to replicate this.

NOTE decision_handler and get_decision are implmented in a way to follow the template method pattern.
This allows for
'''


from resources.PLAYERCONSTANTS import PLAYERCONSTANTS

class Entity():
    def __init__(self, is_bot, name):
        self.value = 0
        self.status = PLAYERCONSTANTS.ALIVE
        self.entity_cards = []
        self.is_bot = is_bot
        self.name = name

    def check_bust_win(self): # todo maybe move this to GameModel class?
        if self.value == 21:
            pass
            # todo if player picks up ace. it could be 1 or 11

    def set_status(self, playerconstant_status): # todo fix
        if playerconstant_status == PLAYERCONSTANTS.ALIVE: self.status = PLAYERCONSTANTS.ALIVE
        elif playerconstant_status == PLAYERCONSTANTS.BUST: self.status = PLAYERCONSTANTS.BUST
        elif playerconstant_status == PLAYERCONSTANTS.STOOD: self.status = PLAYERCONSTANTS.STOOD
        else: raise KeyError("Invalid keyword, {}".format(playerconstant_status))

    def get_status(self):
        return self.status

    def get_is_bot(self):
        return self.is_bot

    def get_name(self):
        return self.name

    def add_card(self, CARD):
        ''' Add a card to the entity

        :return:
        '''
        self.entity_cards.append(CARD)

    def get_cards(self):
        ''' Get players cards

        :return:
        '''
        return self.entity_cards
