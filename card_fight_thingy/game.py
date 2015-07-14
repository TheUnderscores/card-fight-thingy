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
gameOn = False

def initGame(pCount):
    """Initializes game with pCount number of players"""
    global player_stack
    player_stack = []

    for p in range(pCount):
        player_stack.append(Player(p))

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

def tryCardApply(current_player, current_card, victim):
    """
    Try to use the card from the player.
    Return True if success, otherwise return False and a reason
    """
    if type(current_card) is card.Card_Def:
        if not current_card.apply(current_player):
            return (False, "Defense stack is full. Try again...\n")
    elif type(current_card) is card.Card_Atk:
        # TODO: Checking len(player_stack) here only works if there
        # were only ever 2 players. Make it so that it will work when
        # the game comes down to 2 players

        # Check if there are only two players. If so, automatically
        # select the second player
        #if len(player_stack) == 2:
        #    victim = 1 if pNum == 2 else 2
        #else:
        if not victim:
            return (False, "Did not say who to attack. Try again...\n")

        if not withinRange(victim, 1, len(player_stack)):
                return (
                    False,
                    "Player {} does not exist. Try again...\n".format(victim)
                )

        if player_stack[victim-1] == None:
                return (
                    False,
                    "Player {} is dead. Try again...\n".format(victim)
                )

        if victim-1 == current_player.number:
            return (False, "You cannot attack yourself. Try again...\n")

        sys.stdout.write("\n")
        if current_card.apply(player_stack[victim - 1]):
            # Player was killed, remove from list
            # We do not pop a dead player from the player stack since each
            # players' identifying number is associated with its indice
            player_stack[victim - 1] = None

    else:
        return (False, "Did not expect object {!r}".format(type(current_card)))

    return (True, "")

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

        if action.lower() in ('u', "use"):
            if not cardNum:
                print("No card number given. Try again...")
                continue

            #DOIT: Check if card in range.

            ok, msg = tryCardApply(curPlyr, curPlyr.cards[cardNum - 1], victim)

            if not ok:
                print(msg)
                continue

        elif action.lower() in ('d', "discard"):
            if not cardNum:
                print("No card number given. Try again...")
                continue

            #DOIT: Check if card in range.

            # Fall through
            pass

        elif action.lower() in ('q', 'quit', 'exit'):
            while True:
                action = input("Are you sure you want to quit to menu? (Y/n) : ")
                if action == '' or action[0].lower() == 'y':
                    doQuit = True
                    break

                elif action[0].lower() == 'n':
                    doQuit = False
                    break

                else:
                    print("Invalid option. Try again...\n")
                    continue

            sys.stdout.write('\n')
            if doQuit:
                winners = []
                topHP = 0
                for p in player_stack:
                    if not p: continue
                    if p.health > topHP:
                        winners = [p.number + 1]
                        topHP = p.health
                    elif p.health == topHP:
                        winners.append(p.number+1)
                endGame(winners)
                break
            else:
                continue

        else:
            print("Do not know action {!r}. Try again...".format(action))
            continue

        curPlyr.removeCard(cardNum-1)
        break

def endGame(whoWon=(None,)):
    global gameOn
    if gameOn == False:
        return False
    gameOn = False

    if not isinstance(whoWon, (list, tuple)):
        whoWon = (whoWon,)
    if len(whoWon) == 0 or not whoWon[0]:
        print("Game over. No one won.")
    elif len(whoWon) == 1:
        print("Game over. Player {} wins.\n".format(whoWon[0]))
    elif len(whoWon) == 2:
        print("Game over. Players {} and {} tied.\n".format(whoWon[0], whoWon[1]))
    else:
        winStr = ""
        for p_i, p in enumerate(whoWon):
            if p_i < len(whoWon)-1:
                winStr += "{}, ".format(p)
            else:
                winStr += "and {}".format(p)
        print("Game over. Players {} tied.\n".format(winStr))

def playGame():
    """
    Sets the game in motion after the game has been initialized with initGame()
    """
    global player_stack, gameOn

    gameOn = True
    while gameOn:
        for p in player_stack:
            if p == None: continue
            dispPlayers(player_stack)
            takeTurn(p.number)
            if not gameOn: break

        # Check if only one player remains
        c = 0

        winner = None
        for p in player_stack:
            if p is None: continue

            c += 1

            if c > 1:
                break
            else:
                winner = p

        if c == 1:
            endGame(winner.number+1)
            continue

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
