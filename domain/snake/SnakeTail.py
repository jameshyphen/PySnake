class SnakeTail:
    def __init__(self, tail=None):
        if tail is None:
            self.position = 0
        else:
            self.position = tail.position + 1
        self.next_tail = tail
        self.coordinates = [4-self.position, 4]
        self.direction = Going.right

    def move(self):
        if self.direction is Going.up:
            self.coordinates[1] = self.coordinates[1] - 1
        elif self.direction is Going.down:
            self.coordinates[1] = self.coordinates[1] + 1
        elif self.direction is Going.left:
            self.coordinates[0] = self.coordinates[0] - 1
        elif self.direction is Going.right:
            self.coordinates[0] = self.coordinates[0] + 1

    def set_next_tail(self, tail):
        self.next_tail = tail

    def has_next(self):
        return self.next_tail is not None


class Going:
    up = 0
    down = 1
    left = 2
    right = 3
