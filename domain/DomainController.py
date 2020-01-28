from repository.PlayerRepository import PlayerRepository
from domain.player.Player import Player


class DomainController:
    player = None
    playerRepository = PlayerRepository()

    def loginPlayer(self, name, password):
        self.player = self.playerRepository.loginPlayer(name, password)
        if self.player is not None:
            return True
        return False

    def registerPlayer(self, name, password):
        self.player = self.playerRepository.registerPlayer(name, password)
