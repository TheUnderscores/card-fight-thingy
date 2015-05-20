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
from player import Player

def initGame(pCount):
    """Initializes game with pCount number of players"""
    global playerStack
    playerStack = []
    for p in range(pCount):
        playerStack.append(Player())

def dispPlayers():
    global playerStack
    for p in range(len(playerStack)):
        plyr = playerStack[p]
        if plyr.defense[0] == 0:
            # Defense stack is empty
            defStr = ""
        else:
            defStr = "[" + str(plyr.defense[0])
            for d in range(1, len(plyr.defense)):
                if plyr.defense[d] == 0:
                    break
                defStr += ", " + str(plyr.defense[d])
            defStr += "]"
        print("Player #" + str(p+1) + ":\t" +
              str(playerStack[p].health) + "HP\t" + defStr)

def getInt(msg, a, b):
    try:
        num = int(input(msg))
    except ValueError:
        print("Not a valid integer. Try again...")
        return False

    if not withinRange(num, a, b):
        print("Number is out of range (" + str(a) + " - " + str(b) +
              ") Try again...")
        return False

    return num

def takeTurn(pNum):
    """Have player at playerStack index pNum take their turn"""
    global playerStack
    print("Player #" + str(pNum+1) + "'s turn...")
    curPlyr = playerStack[pNum]
    while True:
        curPlyr.showCards()
        # Try to get a valid integer
        cardNum = getInt(
            "Enter the number of the card you'd like to use: ",
            1, curPlyr.deckLen
        )
        if not cardNum:
            continue

        card = curPlyr.cards[cardNum-1]
        if card.type == "def":
            if not card.apply(curPlyr):
                print("Cannot use a defense card. Defense stack is full. Try again...")
                continue
        elif card.type == "atk":
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

                card.apply(playerStack[victim-1])
                break
        else:
            print("Unexpected error")
            continue

        curPlyr.removeCard(cardNum-1)
        break
