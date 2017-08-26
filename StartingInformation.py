def starting_info():
    print('-'*10 + "KING" + "-"*10)
    print("Welcome! We are going to play King.")
    print("Do you know how to play? Y or N?")
    user_input = input(">")
    if user_input == "Y":
        print("Nice, you already know the rules.")
    elif user_input == "N":
        print("Alright, here is a short summary of the rules.")
        print("The game is played by four people. Your goal changes depending on"
              + "the hand you are currently playing.")
        print("There is a total of 12 hands to play:")
        print("1) No King No Jack -2pt each")
        print("2) No Queen -3pt each")
        print("3) No 8 of Diamonds -8pt")
        print("4) No King of Hearts -8pt")
        print("5) No Hearts -1pt each, but if you take all 13 Hearts, you go +13pt")
        print("6) No last two -4pt each")
        print("7) No taking -1pt each")
        print("8) Briscola #1 +1pt each")
        print("9) Briscola #2 +1pt each")
        print("10) Briscola #3 +1pt each")
        print("11) Briscola #4 +1pt each")
        print("12) Final Briscola +2pt each")
        print("Remark: The hand Domino has been skipped, because in the future"+
              " an AI will be implemented. The training in the Domino hand is"+
              " hard to be implemented in parallel with the other hands.")
        print("OK. We know the different hands, but how is the game actually implemented?")
        print("One player start by selecting a card to play. Then, every player" +
              " must answer with the same suit as the first card played. The h"+
              "ighest card wins and the player takes all card in the pit.")
        print("What if a player cannot respond with the suit being played?")
        print("Well, this is actually great news! If that is the case, the player" +
              "can play whatever he wants, and he is never going to take the pit")
        print("There is one more thing you need to know. In the briscola hands,"+
              "you need to take as many pits as you can. In that case, when you"+
              "can answer with whatever you want, you may use the suit is briscola" +
              "it beats every other suit.")
        print("Great, you are all ready to play! For more info, consult the Wikipedia page of King.")
        print('-'*10 + "The game is now starting." + "-"*10)
    else:
        print("Ops, you need to answer either with Y or N.")
    print("By default, you are going to be Player_1")
