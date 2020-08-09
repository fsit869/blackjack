''' Entity.py

Contains a abstract class Entity.py. This contains all the methods and functions needed
for a player/bot. This class is abstract. CANNOT be initiated. Rather it is implemented.

Python does not have built in abstract classes compared to other languages such as java.
Therefore a library is used to replicate this.

NOTE decision_handler and get_decision are implmented in a way to follow the template method pattern.
This allows for
'''


from abc import ABC, abstractmethod
from resources import PLAYERCONSTANTS

class Abstract_Entity(ABC): # todo fix
    def __init__(self, deck_to_pull):
        self.value = 0
        self.status = PLAYERCONSTANTS.ALIVE
        self.deck_to_pull = deck_to_pull

    def hit(self):
        card_obj_picked = self.deck_to_pull.pickup_card()
        card_val = card_obj_picked.get_value()
        card_name = card_obj_picked.get_name()

        self.value += card_val
        self.check_bust()
        return card_name

    def stand(self):
        pass

    def check_bust_win(self):
        if self.value == 21:
            pass
            # todo if player picks up ace. it could be 1 or 11

    def set_status(self, status): # todo fix
        if status == PLAYERCONSTANTS.ALIVE: self.status = PLAYERCONSTANTS.ALIVE
        elif status == PLAYERCONSTANTS.BUST: self.status == PLAYERCONSTANTS.BUST
        elif status == PLAYERCONSTANTS.STOOD: self.status == PLAYERCONSTANTS.STOOD
        else: raise KeyError("Invalid keyword, {}".format(status))

    def get_decision(self):
        action = self.get_decision()
        if action == PLAYERCONSTANTS.HIT: self.hit() # todo fix
        elif action == PLAYERCONSTANTS.STAND: self.stand()
        else: raise KeyError("Invalid keyword, {}".format(action))

    @abstractmethod
    def get_decision_helper(self):
        ''' To follow the template helper pattern this method is called get_decision_helper()

        :return: int (PLAYERCONSTANTS hit/stand)
        '''
        pass