from repository.PlayerRepository import PlayerRepository
from domain.player.Player import Player


class DomainController:
    player = None
    player_repository = PlayerRepository()

    def login_player(self, name, password):
        self.player = self.player_repository.login_player(name, password)
        if self.player is not None:
            return True
        return False

    def register_player(self, name, password):
        self.player = self.player_repository.register_player(name, password)
