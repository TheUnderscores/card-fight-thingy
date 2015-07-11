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

from . import general
from card_fight_thingy.general import withinRange, getInt
from . import player
from card_fight_thingy.player import Player
from . import card
from . import parser

maxPlayers = 10

def initGame(pCount):
    """Initializes game with pCount number of players"""
    global player_stack
    player_stack = []

    for p in range(pCount):
        player_stack.append(Player())

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

def takeTurn(pNum):
    """Have player at global player_stack index pNum take their turn"""
    global player_stack

    if player_stack[pNum] is None: return

    print("Player #" + str(pNum+1) + "'s turn...\n")
    curPlyr = player_stack[pNum]
    while True:
        curPlyr.showCards()

        sys.stdout.write("\n")

        # Try to get valid input
        action, cardNum, victim = parser.tokenize(input("Enter action : "))

        if not cardNum:

            continue

        curCard = curPlyr.cards[cardNum-1]

        if action.lower() == 'u':
            if type(curCard) is card.Card_Def:
                if not curCard.apply(curPlyr):
                    print("Cannot use card - defense stack is full. Try again...\n")
                    continue
                sys.stdout.write("\n")
            elif type(curCard) is card.Card_Atk:
                while True:
                    # TODO: Checking len(player_stack) here only works if there
                    # were only ever 2 players. Make it so that it will work when
                    # the game comes down to 2 players

                    # Check if there are only two players. If so, automatically
                    # select the second player
                    if len(player_stack) == 2:
                        victim = 1 if pNum == 2 else 2
                    else:
                        if not victim:
                            continue
                        if victim-1 == pNum:
                            print("You cannot attack yourself. Try again...\n")
                            continue

                    sys.stdout.write("\n")
                    if curCard.apply(player_stack[victim - 1]):
                        # Player was killed, remove from list
                        player_stack[victim - 1] = None

                    break
            else:
                print("Did not expect object of type \"{}\"".format(type(curCard)))
                continue
        elif action.lower() == 'd':
            # Fall through
            pass
        else:
            print("Do not know action \"{}\"".format(action))
            continue

        curPlyr.removeCard(cardNum-1)
        break

def playGame():
    """
    Sets the game in motion after the game has been initialized with initGame()
    """
    global player_stack

    while True:
        for p_i in range(len(player_stack)):
            dispPlayers(player_stack)
            takeTurn(p_i)

        # Check if only one player remains
        c = 0

        for p_i, p in enumerate(player_stack):
            if p is None: continue

            c += 1

            if c > 1:
                break

        if c == 1: break

    print("Game over. Player {} wins.\n".format(p_i))

def newGame():
    """
    Initializes game with user-defined number of players,
    then sets the game in motion
    """
    while True:
        pCount = getInt("How many players? Maximum of {}: ".format(maxPlayers),
                        2, maxPlayers
        )
        if not pCount:
            continue
        else:
            sys.stdout.write("\n")
            break

    initGame(pCount)
    playGame()
