from domain.Difficulty import Difficulty


class Terrain:
    def __init__(self, difficulty):
        if difficulty is Difficulty.easy:
            self.area = [[0] * 10] * 10
        elif difficulty is Difficulty.normal:
            self.area = [[0] * 15] * 15
        elif difficulty is Difficulty.hard:
            self.area = [[0] * 15] * 15
