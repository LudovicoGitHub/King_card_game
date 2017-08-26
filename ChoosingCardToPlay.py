from Player import *
from printCurrentHand import printCurrentPlayerHand
def ChooseYourPlay(PositionInArrayOfPlayer,pit):
    print("It is your turn,player number",PositionInArrayOfPlayer)
    print("Please, choose a card from your hand to play.")
    print("Take a look at your hand.")
    printCurrentPlayerHand(PositionInArrayOfPlayer)
    choiche = input(>>)
    pit.append(arrayOfPlayers[PositionInArrayOfPlayer].hand.pop(choiche))
    
