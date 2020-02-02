from domain.Direction import Going


class SnakeTail:
    direction: int

    def __init__(self, _tail=None, _direction=Going.right):
        self.next_tail = _tail
        self.direction = _direction
        if _tail is None:
            self.coordinates = [3, 3]
        else:
            if _direction is Going.right:
                self.coordinates = [_tail.coordinates[0], _tail.coordinates[1] - 1]
            elif _direction is Going.down:
                self.coordinates = [_tail.coordinates[0] - 1, _tail.coordinates[1]]
            if _direction is Going.left:
                self.coordinates = [_tail.coordinates[0], _tail.coordinates[1] + 1]
            elif _direction is Going.down:
                self.coordinates = [_tail.coordinates[0] + 1, _tail.coordinates[1]]

    def move(self):
        if self.direction is Going.up:
            self.coordinates[0] -= 1
        elif self.direction is Going.down:
            self.coordinates[0] += 1
        elif self.direction is Going.left:
            self.coordinates[1] -= 1
        elif self.direction is Going.right:
            self.coordinates[1] += 1

        if self.has_next():
            self.direction = self.next_tail.direction

    def set_next_tail(self, tail):
        self.next_tail = tail

    def has_next(self):
        return self.next_tail is not None

    def next(self):
        return self.next_tail

    def Change_direction(self, _direction):
        self.direction = _direction

    def direction(self):
        return self.direction

    def show_tail_directions(self):
        print(self.direction)
        if self.has_next():
            self.next_tail.show_tail_directions()
