from random import seed as srand, randint
from time import time

srand(time())

class Card:
    typs = ('def', 'attk')
    limits = {'def': (1, 25), 'attk': (1, 40)}

    def __init__(self, typ=None, value=None):
        if typ ~= None:
            # Validate card type
            valid = False
            for t in Card.typs:
                if typ == t:
                    valid = True
                    break

            if not valid:
                print("ERROR: Invalid card type")
                return False
        else:
            # Randomize card type
            typ = Card.typs[randint(len(Card.typs))]

        self.typ = typ
        self.value = randint(Card.limits[typ][0], Card.limits[typ][1])
