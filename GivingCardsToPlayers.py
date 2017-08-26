from Card import creatingDeckAlreadyShuffled
from Player import *
def GivingCardTo():
    my_deck = creatingDeckAlreadyShuffled()
    for i in range(0,52):
        arrayOfPlayers[i%4].hand.append(my_deck.pop())
