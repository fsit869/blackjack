'''Card.py

This file contains the class for one card.
'''

from resources import CARDCONSTANTS

class Card():
    def __init__(self, card_name, card_value):
        ''' Creates a card. The parameters are implemented this way to allow for dynamic changing
        of the card reference (img location) and its value.

        :param card_name: Card constant eg TEN_C, FIVE_H...
        :param card_value: Card constant val eg TEN_C_VAL, FIVE_H_VAL
        '''
        self.CARDCONSTANT = None
        self.CARD_NAME = card_name
        self.CARDVALUE = card_value

    def get_name(self):
        ''' Returns card_name. AKA card location

        :return: str. CardConstant
        '''
        return self.CARD_NAME

    def get_value(self):
        ''' Returns card_val. Card value

        :return: int. CardConstant_val
        '''
        return self.CARDVALUE

