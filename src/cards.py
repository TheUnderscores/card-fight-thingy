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

from random import seed as srand, randint
from time import time

srand(time())

def withinRange(n, a, b):
    """Returns True if a <= n <= b, False otherwise"""
    if n >= a and n <= b:
        return True
    else:
        return False

class Card:
    """Main card class"""

    def __init__(self, value=None):
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

class Card_Def(Card):
    """Defense card class"""

    value_range = (1, 25)

    def __init__(self, value=None):
        """
        Initialize defense card.
        May specify the cards value with the optional parameter 'value'.
        If no value if given or value is out of range, value will be randomly
        generated within proper range.
        """
        Card.__init__(self, value=value)

    def apply(self, player):
        """
        Attempts to add value of defense card to player's defense stack.
        If player has no vacant defense slots, return False.
        If defense was successfully applies, return True.
        """
        if player.addDefense(self.value):
            # Defense succefully applied
            return True
        else:
            # Defense card could not be applied
            return False

class Card_Atk(Card):
    """Attack card class"""

    value_range = (1, 40)

    def __init__(self, value=None):
        """
        Initialize attack card.
        May specify the cards value with the optional parameter 'value'.
        If no value if given or value is out of range, value will be randomly
        generated within proper range.
        """
        Card.__init__(self, value=value)

    def apply(self, player):
        """
        Attempts to add value of defense card to player's defense stack.
        """
        player.takeDamage(self.value)
