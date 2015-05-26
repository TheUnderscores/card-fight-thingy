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

from general import withinRange
from player import Player
import card

def initGame(pCount):
    """Initializes game with pCount number of players"""
    l = []

    for p in range(pCount):
        l.append(Player())

    return l

def dispPlayers(stack):
    for i, plyr in enumerate(stack):
        if plyr is None: continue

        if plyr.defense[0] == 0:
            # Defense stack is empty
            defStr = ""
        else:
            defStr = "[{} {} {}]".format(*plyr.defense)

        print("Player #{}:\t{}HP\t{}".format(i + 1, plyr.health, defStr))

    sys.stdout.write("\n")

def getInt(msg, a, b):
    try:
        num = int(input(msg))
    except ValueError:
        print("Not a valid integer. Try again...\n")
        return False

    if not withinRange(num, a, b):
        print("Number is out of range ({} - {}) Try again...\n".format(a, b))
        return False

    return num

def takeTurn(playerStack, pNum):
    """Have player at playerStack index pNum take their turn"""

    if playerStack[pNum] is None: return

    print("Player #" + str(pNum+1) + "'s turn...\n")
    curPlyr = playerStack[pNum]
    while True:
        curPlyr.showCards()

        sys.stdout.write("\n")

        # Try to get a valid integer
        cardNum = getInt(
            "Enter the number of the card you'd like to use: ",
            1, curPlyr.deckLen
        )
        if not cardNum:
            continue

        curCard = curPlyr.cards[cardNum-1]

        if type(curCard) is card.Card_Def:
            if not curCard.apply(curPlyr):
                print("Cannot use card - defense stack is full. Try again...")
                continue
        elif type(curCard) is card.Card_Atk:
            while True:
                victim = getInt(
                    "Enter the number of the player you'd like to attack: ",
                    1, len(playerStack)
                )

                if not victim:
                    continue
                if victim-1 == pNum:
                    print("You cannot attack yourself. Try again...")
                    continue

                if curCard.apply(playerStack[victim - 1]):
                    # Player was killed, remove from list
                    playerStack[victim - 1] = None

                break
        else:
            print("Did not expect object of type \"{}\"".format(type(curCard)))
            continue

        curPlyr.removeCard(cardNum-1)
        break
