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

from . import game
from . import general
from card_fight_thingy.general import getInt

options = []

def addOption(text, func, args=()):
    """
    Create a new menu option denoted by the string text.
    Function func is called when option is chosen.
    """
    options.append({'text': text, 'func': func, 'args': args})

def dispMenu():
    for o_i, o in enumerate(options):
        print("{}. {}".format(o_i+1, o['text']))

def chooseOption():
    while True:
        dispMenu()
        optNum = getInt("Choose a menu option: ", 1, len(options))
        if not optNum:
            continue
        else:
            sys.stdout.write("\n")
            o = options[optNum-1]
            o['func'](*o['args'])

def init():
    addOption("New Game", game.newGame)
    addOption("Quit", sys.exit, args=(0,))
