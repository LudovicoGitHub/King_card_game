
from ChoosingCardToPlay import *
from GivingCardsToPlayers import *

# we arrive here with a full pit and info of the first suit played.
def comparing(pit,position_of_first_suit_played):
    dominant_suit = pit[position_of_first_suit_played]
    winning_card = pit[0]
    for i in range(0,4):
        if pit[i].suit == dominant_suit and pit[i].rank > winning_card.rank:
            winning_card = pit[i]
            positon_of_winning_card = i
    # the position of the winning card is the same as the position in the array
    # of players, so we just need to pop all the cards into the cardstaken of the player.
    for i in range(0,4):
        arrayOfPlayers[winning_card].cardsTaken.append(pit.pop(i))
