from domain.Difficulty import Difficulty
from domain.snake.SnakeTail import SnakeTail
import numpy

class Terrain:
    def __init__(self, difficulty):
        if difficulty is Difficulty.easy:
            self.area = numpy.zeros((6, 6))
        elif difficulty is Difficulty.normal:
            self.area = numpy.zeros((15, 15))
        elif difficulty is Difficulty.hard:
            self.area = numpy.zeros((20, 20))


