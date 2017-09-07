import random
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def cardName(self):
        specialCards = {11: "Jack", 12:"Queen", 13:"King", 14:"Ace"}
        if self.rank in specialCards:
            return specialCards[self.rank] + "of" + self.suit
        else:
            return str(self.rank) + " of " + self.suit

def creatingDeckAlreadyShuffled():
    suits = ["Spades","Hearts","Diamonds","Clubs"]
    deck = [Card(rank, suit) for rank in range(1,14) for suit in suits]
    for i in range(1,5):
        random.shuffle(deck)
    return deck
