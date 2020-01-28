from domain.player.Player import Player

# this is just a test application and the passwords will not be saved like this.
def passwordCheck(password, _player):
    if password == _player.password:
        return True


class PlayerRepository:
    players = []

    def __init__(self):
        player = Player("Dzhem")
        player.wins = 100
        player.losses = 50
        self.players.append(player)
        self.players.append(Player("Kenzo"))
        self.players.append(Player("Alex"))

    def loginPlayer(self, name, password):
        playerFound = next((p for p in self.players if p.name == name), None)
        if playerFound is None:
            return None
        else:
            if passwordCheck(password, playerFound):
                return playerFound
            else:
                return None

    def registerPlayer(self, name, password):
        player = Player(name)
        player.password=password
        self.players.append(player)