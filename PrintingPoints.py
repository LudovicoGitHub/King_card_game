from Player import *
def printingPoints():
    print("-----POINTS-----")
    for i in range(1,5):
        print("Player_",i," has",arrayOfPlayers[i-1].points," points")
