# card-fight-thingy
Simplistic 2 to 8 player card battle game... thingy

Each game has 2 to 8 human players. Each player starts with 100HP. The goal of the game is to lower the HP of other players. The last player standing is the winner.

Each player is given 7 card. There are two types of cards: attack cards and defense cards. Attack cards are applied to a player to diminish their HP. Defense card absorb attacks on a player's HP. For instance, if an attack card of 10 is used on a player with a defense card of 15, the defense card will be diminished to 5. Players can have up to 3 active defense cards. When a defense card is destroyed, any HP it didn't absorb will be carried on down the stack. If there are no defense card left in the stack when damage gets carried over, the player's HP will absorb the remaining damage. Defense cards absorb damage in a hierarchical  fashion, from top to bottom.

Each player makes one action each round. They may either add a defense card to their stack, use an attack card on another player, or discard a card in their hand.
