'''CARDCONSTANTS.py

A class containing constants of the cards. Constants referenced to img location.
Used to have common names between model and view
Similar to Java Enumerations. Python does not support Enums
Therefore a package is used to replicate.

CONSTANTS MUST BE ALL UPPER CASE.

'''
from enum import Enum

class CARDCONSTANTS(Enum):
    _file_directory = "resources/images/cards/"
    CARD_PIXEL_HEIGHT = 1056
    CARD_PIXEL_WIDTH = 691

    def IMAGELOCATION(self):
        return self.value[0]

    def CARDVALUE(self):
        return self.value[1]

    TEN_C = (_file_directory + "10C.png", 10)
    TEN_D = (_file_directory + "10D.png", 10)
    TEN_H = (_file_directory + "10H.png", 10)
    TEN_S = (_file_directory + "10S.png", 10)
    TWO_C = (_file_directory + "2C.png", 2)
    TWO_D = (_file_directory + "2D.png", 2)
    TWO_H = (_file_directory + "2H.png", 2)
    TWO_S = (_file_directory + "2S.png", 2)
    THREE_C = (_file_directory + "3C.png", 3)
    THREE_D = (_file_directory + "3D.png", 3)
    THREE_H = (_file_directory + "3H.png", 3)
    THREE_S = (_file_directory + "3S.png", 3)
    FOUR_C = (_file_directory + "4C.png", 4)
    FOUR_D = (_file_directory + "4D.png", 4)
    FOUR_H = (_file_directory + "4H.png", 4)
    FOUR_S = (_file_directory + "4S.png", 4)
    FIVE_C = (_file_directory + "5C.png", 5)
    FIVE_D = (_file_directory + "5D.png", 5)
    FIVE_H = (_file_directory + "5H.png", 5)
    FIVE_S = (_file_directory + "5S.png", 5)
    SIX_C = (_file_directory + "6C.png", 6)
    SIX_D = (_file_directory + "6D.png", 6)
    SIX_H = (_file_directory + "6H.png", 6)
    SIX_S = (_file_directory + "6S.png", 6)
    SEVEN_C = (_file_directory + "7C.png", 7)
    SEVEN_D = (_file_directory + "7D.png", 7)
    SEVEN_H = (_file_directory + "7H.png", 7)
    SEVEN_S = (_file_directory + "7S.png", 7)
    EIGHT_C = (_file_directory + "8C.png", 8)
    EIGHT_D = (_file_directory + "8D.png", 8)
    EIGHT_H = (_file_directory + "8H.png", 8)
    EIGHT_S = (_file_directory + "8S.png", 8)
    NINE_C = (_file_directory + "9C.png", 9)
    NINE_D = (_file_directory + "9D.png", 9)
    NINE_H = (_file_directory + "9H.png", 9)
    NINE_S = (_file_directory + "9S.png", 9)
    ACE_C = (_file_directory + "AC.png", (1, 11))
    ACE_D = (_file_directory + "AD.png", (1, 11))
    ACE_H = (_file_directory + "AH.png", (1, 11))
    ACE_S = (_file_directory + "AS.png", (1, 11))
    JACK_C = (_file_directory + "JC.png", 10)
    JACK_D = (_file_directory + "JD.png", 10)
    JACK_H = (_file_directory + "JH.png", 10)
    JACK_S = (_file_directory + "JS.png", 10)
    KING_C = (_file_directory + "KC.png", 10)
    KING_D = (_file_directory + "KD.png", 10)
    KING_H = (_file_directory + "KH.png", 10)
    KING_S = (_file_directory + "KS.png", 10)
    QUEEN_C = (_file_directory + "QC.png", 10)
    QUEEN_D = (_file_directory + "QD.png", 10)
    QUEEN_H = (_file_directory + "QH.png", 10)
    QUEEN_S = (_file_directory + "QS.png", 10)