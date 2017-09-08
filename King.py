from StartingInformation import *
from ChoosingCardToPlay import ChooseYourPlay
from GivingCardsToPlayers import *
from Player import *
from PrintCurrentHand import *
from PrintingPoints import *
from ComparingCardInPit import *
from Card import *

starting_info()
pit = [None] * 4
GivingCardTo()
for i in range(0,4):
    printCurrentPlayerHand(i)
printingPoints()
for i in range(0,4):
    position_of_first_suit_played = ChooseYourPlay(i,pit)

comparing(pit,position_of_first_suit_played)
for i in range(0,4):
    print(arrayOfPlayers[i].cardsTaken)
