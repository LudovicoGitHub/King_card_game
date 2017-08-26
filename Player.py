class Player:
    def __init__(self,id):
        self.points = 0
        self.hand = []
        self.cardsTaken = []
        self.id = id


Player_1 = Player(0)
Player_2 = Player(1)
Player_3 = Player(2)
Player_4 = Player(3)

arrayOfPlayers = [Player_1,Player_2,Player_3,Player_4]
