''' Deck.py

This class contains a deck class. A deck class contains 52 card objects.
Contains methods such as pickup card, create deck...

'''
from resources import CARDCONSTANTS
from model.deck import Card
from random import shuffle

class Deck():
    def __init__(self):
        self.deck = []
        self.picked_up_deck = []

        self.new_deck()
        self.shuffle_deck()

    def new_deck(self):
        ''' Creates a new deck with contents listed in CARDCONSTANTS.py

        :return: None
        '''
        self.deck.clear()
        self.picked_up_deck.clear()

        for CONSTANT in CARDCONSTANTS.CARDCONSTANTS.get_all_cards(): # todo may crash
            self.deck.append(Card.Card(CONSTANT))
        self.shuffle_deck()

    def shuffle_deck(self):
        ''' Shuffles the deck

        :return: None
        '''
        shuffle(self.deck)

    def pickup_card(self):
        ''' Pickup a card. (Returns a card obj) and removes it from deck.
        This card gets put in picked_up_deck[]
        If no cards in deck, a new deck is created

        :return:
        '''
        if not self.check_deck_empty():
            picked_up_card = self.deck.pop(0)
            self.picked_up_deck.append(picked_up_card)
            return picked_up_card
        else:
            # todo possibily add counter saying a new deck has been created. To allow for card counting
            self.new_deck()
            self.pickup_card()

    def check_deck_empty(self):
        ''' Check if deck is empty

        :return: Bool
        '''
        if len(self.deck) == 0:
            return True
        else:
            return False
