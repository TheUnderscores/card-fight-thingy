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

class Player():
    def __init__(self):
        self.health = 100
        self.defense = 0
        # TODO : Implement card class
        # self.cards = Card.generateDeck()

    def takeDamage(self, damage):
        if self.defense > 0:
            if damage > self.defense:
                # Defense won't eat all damange
                damage -= self.defense
                self.defense = 0
            else:
                # Defense will eat all damage
                self.defense -= damage
                return

        self.health -= damage
