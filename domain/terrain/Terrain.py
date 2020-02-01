from domain.Difficulty import Difficulty
from domain.snake.SnakeTail import SnakeTail
import numpy

class Terrain:
    def __init__(self, difficulty):
        if difficulty is Difficulty.easy:
            self.area = numpy.zeros((10, 10))
        elif difficulty is Difficulty.normal:
            self.area = numpy.zeros((10, 10))
        elif difficulty is Difficulty.hard:
            self.area = numpy.zeros((10, 10))


