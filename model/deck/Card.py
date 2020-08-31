'''Card.py

This file contains the class for one card.
'''

from resources import CARDCONSTANTS

class Card():
    def __init__(self, CARDCONSTANT):
        ''' Create a card

        :param CARDCONSTANT: CARDCONSTANT from resources
        '''
        self.CARDCONSTANT = CARDCONSTANT
        self.CARD_NAME = self.CARDCONSTANT
        self.CARDVALUE = self.CARDCONSTANT.CARDVALUE()

    def compare_to_card(self, CARDCONSTANT):
        ''' Compares the CARDCONSTANT enum to another CARRDCONSTANT enum

        :param CARDCONSTANT:
        :return: Boolean
        '''
        if self.CARDCONSTANT == CARDCONSTANT:
            return True
        else:
            return False

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

    def get_card_constant(self):
        ''' Returns the card constant

        :return: Cardconstant
        '''
        return self.CARDCONSTANT

