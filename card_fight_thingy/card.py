# card-fight-thingy - Simplistic battle card game... thingy
#
# The MIT License (MIT)
#
# Copyright (c) 2015 The Underscores
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from general import withinRange
from random import seed as srand, randint
from time import time

import player

srand(time())

class Card:
    """Main card class"""

    def __init__(self, value = None, symbol = None):
        """
        Initialize card.
        May specify the cards value with the optional parameter 'value'.
        If no value if given or value is out of range, value will be randomly
        generated within proper range.
        """
        if (value != None and withinRange(value, *self.value_range)):
            self.value = value
        else:
            self.value = randint(*self.value_range)

        self.symbol = symbol

class Card_Def(Card):
    """Defense card class"""

    value_range = (1, 25)

    def __init__(self, value = None):
        """
        Initialize defense card.
        May specify the cards value with the optional parameter 'value'.
        If no value if given or value is out of range, value will be randomly
        generated within proper range.
        """
        super().__init__(value = value, symbol = "D")

    def apply(self, player):
        """
        Attempts to add value of defense card to player's defense stack.
        If player has no vacant defense slots, return False.
        If defense was successfully applies, return True.
        """
        return player.addDefense(self.value)

class Card_Atk(Card):
    """Attack card class"""

    value_range = (1, 40)

    def __init__(self, value = None):
        """
        Initialize attack card.
        May specify the cards value with the optional parameter 'value'.
        If no value if given or value is out of range, value will be randomly
        generated within proper range.
        """
        super().__init__(value = value, symbol = "A")

    def apply(self, target):
        """
        Uses card to attack other player of choice. Returns True when
        the card causes the death of the player it was used against.
        """
        try:
            target.takeDamage(self.value)
        except player.PlayerKilledException:
            return True

def randCard():
    """Return a random card"""
    if randint(0, 1) == 0:
        return Card_Def()
    else:
        return Card_Atk()
