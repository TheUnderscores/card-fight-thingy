from random import seed as srand, randint
from time import time

srand(time())

class Card:
    card_types = ("def", "atk")
    card_limits = {"def": (1, 25), "atk": (1, 40)}

    def __init__(self, card_type = None, card_value = None):
        if card_type:
            if not card_type in card_types:
                print("ERROR: Invalid card type")
                return False
        else:
            # Randomize card type
            card_type = Card.card_types[randint(len(Card.card_types))]

        self.card_type = card_type
        self.value = randint(card_limits[card_type][0],
            card_limits[card_type][1])
