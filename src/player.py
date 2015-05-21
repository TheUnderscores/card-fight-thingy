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

import sys

import card

class Player():
    deckLen = 7

    def __init__(self):
        self.health = 100
        # Up to 3 active defense cards
        self.defense = [0, 0, 0]
        self.cards = [None for c in range(self.deckLen)]
        self.generateCards()

    def generateCards(self):
        """Fills self.cards with random cards"""
        for c in range(len(self.cards)):
            self.cards[c] = card.randCard()

    def removeCard(self, c):
        """Removes and replaces card at index c from self.cards"""
        if not (0 <= c < len(self.cards)):
            return False

        self.cards[c] = card.randCard()
        return True

    def showCards(self):
        """Prints out currently held cards"""
        for i, c in enumerate(self.cards):
            print("{} - {} {}".format(i + 1, c.symbol, c.value))

    def kill(self):
        """Removes a player from the game"""
        pass

    def takeDamage(self, damage):
        """
        Applies damage to player.
        Defense is effected first, than health.
        If a player's health is below 0, player is killed with Player.kill().
        """
        # Parse through defense stack from top to bottom
        for i in range(len(self.defense)-1, -1, -1):
            if self.defense[i] >= damage:
                # Defense slot absorbs all of damage
                self.defense[i] -= damage
                damage = 0
                break
            else:
                # Defense slot absorbs some or none of damage
                damage -= self.defense[i]
                self.defense[i] = 0

        self.health -= damage

        if self.health <= 0: self.kill()

    def addDefense(self, defense):
        """
        If defense stack if empty, adds defense to stack and returns True.
        If defense stack is full, do not nothing and return False
        """
        # Parse through defense stack looking for empty slot
        for i in range(0, len(self.defense)):
            if self.defense[i] == 0:
                # Empty defense slot found and will now be filled
                self.defense[i] = defense
                return True

        # No empty slot was found
        return False
