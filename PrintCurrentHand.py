from Player import *
from Card import *
def printCurrentPlayerHand(PlayerID):
    for i in range(0,13):
        print(str(arrayOfPlayers[PlayerID].hand[i].rank) + "of" + arrayOfPlayers[PlayerID].hand[i].suit)
