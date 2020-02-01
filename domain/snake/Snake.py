from domain.snake.SnakeTail import SnakeTail
from domain.Difficulty import Difficulty


class Snake:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        tail = SnakeTail(SnakeTail(SnakeTail()))
        if difficulty is Difficulty.easy:
            self.speed = 4
        elif difficulty is Difficulty.easy:
            self.speed = 5
        elif difficulty is Difficulty.easy:
            self.speed = 6


