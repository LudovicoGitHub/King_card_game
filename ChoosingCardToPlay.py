from Player import *
from printCurrentHand import printCurrentPlayerHand
from King import pit
def ChooseYourPlay(PositionInArrayOfPlayer,pit):
    print("It is your turn,player number",PositionInArrayOfPlayer)
    print("Please, choose a card from your hand to play.")
    print("Take a look at your hand.")
    printCurrentPlayerHand(PositionInArrayOfPlayer)
    choiche = input(>>)
    for i in range(0,4):
        if pit[i] == None:
            position_of_first_suit_played = PositionInArrayOfPlayer
    pit[PositionInArrayOfPlayer] = arrayOfPlayers[PositionInArrayOfPlayer].hand.pop(choiche)
