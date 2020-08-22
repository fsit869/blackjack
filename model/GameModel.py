''' GameModel.py

THis file contains the model layer of the MVC model.
Interacts with the controller and model objects.

'''
import random
from model.deck import Deck, Card
from model.entities import Entity
from random import shuffle
from resources.PLAYERCONSTANTS import PLAYERCONSTANTS
from resources.CARDCONSTANTS import CARDCONSTANTS

class GameModel():
    def __init__(self):
        pass
        # self.entities = None # Dict containing players
        # self.deck = None # Stores the deck
        # self.current_player = None
        # self.player_order = [] # Stores entity objs. This is player order
        # self.cards_to_display = []

    def init_game(self, amt_bots, human_players=1):
        self.player_order = []  # Clears list
        self.cards_to_display = []
        self.current_player = None
        self.deck = None
        self.entities = None

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
        self.current_player = self.player_order[0]

    def current_entity_stand(self):
        self.current_player.set_status(PLAYERCONSTANTS.STOOD)

    def current_entity_hit(self):
        picked_up_card = self.deck.pickup_card()
        self.current_player.add_card(picked_up_card)

        # If current entity not bot, make sure GUI displays picked up card
        if self.current_player.get_is_bot() == False: #
            self.cards_to_display.append(picked_up_card.get_card_constant())

    def current_entity_set_status(self, PLAYERCONSTANT):
        self.current_player.set_status(PLAYERCONSTANT)

    def next_entity(self, _iterations=0):
        ''' Next entity turn thats still alive and not stood

        :return:
        '''
        if _iterations>len(self.player_order)+5:
            raise Exception("Unexpected error causing recursion.")

        current_player_index = self.player_order.index(self.current_player)
        try:
            self.current_player = self.player_order[current_player_index + 1]
        except IndexError:
            self.current_player = self.player_order[0]

        if (self.current_player.get_status() != PLAYERCONSTANTS.ALIVE):
            _iterations += 1
            self.next_entity(_iterations=_iterations)

    def is_game_playable(self):
        for player in self.player_order:
            if player.get_status() == PLAYERCONSTANTS.ALIVE:
                return True
        return False

    def get_update_commands(self):
        dict_format = {
            PLAYERCONSTANTS: {
                "current_turn": self.current_player.get_name(),
            },

            CARDCONSTANTS: self.cards_to_display
        }

        for player in self.player_order:
            player_name = player.get_name()
            player_status = player.get_status()
            player_card_amt = len(player.get_cards())
            dict_format[PLAYERCONSTANTS][player_name] = (player_status, player_card_amt)

        return dict_format

    def get_player_win_status(self): # might need to check if player is stood. If stood need to skip
        card_sum = self.get_card_total()
        if card_sum== 21:
            return PLAYERCONSTANTS.WIN
        elif card_sum<21:
            return PLAYERCONSTANTS.ALIVE
        else:
            return PLAYERCONSTANTS.BUST

    def get_card_total(self):
        entity_cards_objs = self.current_player.get_cards()
        single_value_sum = 0  # All card with one values added. EG 2 has val 2
        ace_values = []  # Contains all aces values
        for card in entity_cards_objs:
            card_value = card.get_value()
            if type(card_value) == int:
                single_value_sum += card_value
            elif type(card_value) == tuple:
                ace_values.append(max(card_value))
            else:
                raise AttributeError("Invalid type")

        card_sum = 0 + single_value_sum
        iterator = 0
        while True:
            if card_sum + sum(ace_values) == 21:
                card_sum += sum(ace_values)
                break
            elif card_sum + sum(ace_values) < 21:
                card_sum + sum(ace_values)
                break
            else:
                if iterator < len(ace_values):
                    ace_values[iterator] = 1
                    iterator += 1
                else:
                    card_sum += sum(ace_values)
                    break
        return card_sum

    def get_current_entity_status(self):
        return self.current_player.get_status()

    def get_current_entity_is_bot(self):
        return self.current_player.get_is_bot()

    def get_bot_decision(self):
        '''
        Sector          *   Deck sum * Stand threshold  * Variability
        ----------------*------------*------------------*------------
        sector_one      *   0  - 10  * 0%               * 0%
        sector_two      *   11 - 15  * 10%              * 0-10%
        sector_three    *   16 - 18  * 50%              * 0-8%
        sector_four     *   19 - 20  * 90%              * 0-6%
        sector_five     *   21       * 99%              * 0%

        :return:
        '''
        card_sum = self.get_card_total()
        action = None

        SECTOR_ONE_STAND_THRESHOLD = 0
        SECTOR_TWO_STAND_THRESHOLD = 0.1
        SECTOR_THREE_STAND_THRESHOLD = 0.5
        SECTOR_FOUR_STAND_THRESHOLD = 0.9
        SECTOR_FIVE_STAND_THRESHOLD = 0.99

        SECTOR_ONE_STAND_MAX_VARIABILITY = 0
        SECTOR_TWO_STAND_MAX_VARIABILITY = 0.1
        SECTOR_THREE_STAND_MAX_VARIABILITY = 0.08
        SECTOR_FOUR_STAND_MAX_VARIABILITY = 0.06
        SECTOR_FIVE_STAND_MAX_VARIABILITY = 0

        def calculate_action(STAND_THRESHOLD, MAX_VARIABILITY):
            _random_double = random.random()
            _varability = random.uniform(0, MAX_VARIABILITY)
            if _random_double < (STAND_THRESHOLD + _varability):
                return PLAYERCONSTANTS.STAND
            else:
                return PLAYERCONSTANTS.HIT

        if card_sum <= 10:
            action = calculate_action(SECTOR_ONE_STAND_THRESHOLD, SECTOR_ONE_STAND_MAX_VARIABILITY)
        elif (card_sum>10) and (card_sum<16):
            action = calculate_action(SECTOR_THREE_STAND_THRESHOLD, SECTOR_TWO_STAND_MAX_VARIABILITY)
        elif (card_sum > 15) and (card_sum < 19):
            action = calculate_action(SECTOR_THREE_STAND_THRESHOLD, SECTOR_THREE_STAND_MAX_VARIABILITY)
        elif (card_sum > 18) and (card_sum < 21):
            action = calculate_action(SECTOR_THREE_STAND_THRESHOLD, SECTOR_FOUR_STAND_MAX_VARIABILITY)
        elif card_sum == 21:
            action = calculate_action(SECTOR_THREE_STAND_THRESHOLD, SECTOR_FIVE_STAND_MAX_VARIABILITY)
        else:
            raise AttributeError("Card sum > 21, No action can be done")
        return action

    def get_entity_name(self):
        return self.current_player.get_name()









