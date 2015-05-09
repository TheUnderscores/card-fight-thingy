from random import seed as srand, randint
from time import time

srand(time())

class Card:
    types = ("def", "atk")
    limits = {"def": (1, 25), "atk": (1, 40)}

    def __init__(self, type = None, value = None):
        if type:
            if not type in types:
                print("ERROR: Invalid card type")
                return False
        else:
            # Randomize card type
            type = Card.types[randint(len(Card.types))]

        self.type = type
        self.value = randint(Card.limits[type][0], Card.limits[type][1])
