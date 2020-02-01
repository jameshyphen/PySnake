from domain.snake.SnakeTail import SnakeTail
from domain.Difficulty import Difficulty


class Snake:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.tail = SnakeTail(SnakeTail(SnakeTail()))
        if difficulty is Difficulty.easy:
            self.speed = 4
        elif difficulty is Difficulty.easy:
            self.speed = 5
        elif difficulty is Difficulty.easy:
            self.speed = 6


    def move_snake(self):
        tail = self.tail
        tail.move()
        while tail.has_next():
            tail = tail.next_tail
            tail.move()

    def tail_coordinates(self):
        tail = self.tail
        cords = [tail.coordinates]
        while tail.has_next():
            tail = tail.next_tail
            cords.append(tail.coordinates)
        return cords

