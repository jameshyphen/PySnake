from domain.snake.Snake import Snake
from domain.terrain.Terrain import Terrain


class BuildTerrain:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.interval = 4000 / (4 + difficulty)
        self.area = Terrain(difficulty).area
        self.snake = Snake(difficulty)

    def spawn_food(self):
        pass

    def draw_snake_on_terrain(self):
        print(self.snake.tail_coordinates())
        self.area = Terrain(self.difficulty).area
        for tail_cord in self.snake.tail_coordinates():
            self.area[tail_cord[0]][tail_cord[1]] = 1

    def draw_game(self):
        for line in self.area:
            print(line)
