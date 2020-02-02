from domain.snake.SnakeTail import SnakeTail
from domain.Difficulty import Difficulty


class Snake:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.head_tail = SnakeTail()
        self.tail = SnakeTail(SnakeTail(self.head_tail))
        if difficulty is Difficulty.easy:
            self.speed = 4
        elif difficulty is Difficulty.easy:
            self.speed = 5
        elif difficulty is Difficulty.easy:
            self.speed = 6

    def Move_snake(self):
        tail = self.tail
        tail.move()
        while tail.has_next():
            temp_tail = tail
            tail = tail.next_tail
            temp_tail.set_direction = tail.direction
            tail.move()

    def tail_coordinates(self):
        tail = self.tail
        cords = [tail.coordinates]
        while tail.has_next():
            tail = tail.next_tail
            cords.append(tail.coordinates)
        return cords

    def Add_Tail(self):
        self.tail = SnakeTail(self.tail)

    def show_tail_directions(self):
        self.tail.show_tail_directions()

    def Change_direction(self, _direction):
        self.head_tail.Change_direction(_direction)
