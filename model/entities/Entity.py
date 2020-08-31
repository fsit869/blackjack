''' Entity.py

This contains all the methods and functions needed for a player/bot.
'''


from resources.PLAYERCONSTANTS import PLAYERCONSTANTS

class Entity():
    def __init__(self, is_bot, name):
        ''' Create a new entitiy

        :param is_bot: Bool
        :param name: Str, bot name
        '''
        self.value = 0
        self.status = PLAYERCONSTANTS.ALIVE
        self.entity_cards = []
        self.is_bot = is_bot
        self.name = name

    def set_status(self, playerconstant_status):
        ''' Set status of player

        :param playerconstant_status: PLAYERCONSTANT
        :return: None
        '''
        if playerconstant_status == PLAYERCONSTANTS.ALIVE: self.status = PLAYERCONSTANTS.ALIVE
        elif playerconstant_status == PLAYERCONSTANTS.BUST: self.status = PLAYERCONSTANTS.BUST
        elif playerconstant_status == PLAYERCONSTANTS.STOOD: self.status = PLAYERCONSTANTS.STOOD
        else: raise KeyError("Invalid keyword, {}".format(playerconstant_status))

    def get_status(self):
        ''' Get player status

        :return: PLAYERCONSTANT
        '''
        return self.status

    def get_is_bot(self):
        ''' Get if player is bot

        :return: Bool
        '''
        return self.is_bot

    def get_name(self):
        ''' Get player name

        :return: str
        '''
        return self.name

    def add_card(self, card_obj):
        ''' Add a card to player

        :param card_obj: CARDCONTSTANT
        :return: NONE
        '''
        self.entity_cards.append(card_obj)

    def get_cards(self):
        ''' Get players cards

        :return:
        '''
        return self.entity_cards
