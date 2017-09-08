from Player import *
from PrintCurrentHand import *

def ChooseYourPlay(PositionInArrayOfPlayer,pit):
    print("It is your turn,player number",PositionInArrayOfPlayer+1)
    print("Please, choose a card from your hand to play.")
    print("Take a look at your hand.")
    counter = 0
    printCurrentPlayerHand(PositionInArrayOfPlayer)
    choichestr = input(">>")
    choiche = int(choichestr)
    for i in range(0,4):
        if pit[i] == None:
            counter = counter + 1
    if counter == 4:
        position_of_first_suit_played = PositionInArrayOfPlayer

    pit[PositionInArrayOfPlayer] = arrayOfPlayers[PositionInArrayOfPlayer].hand.pop(choiche)
