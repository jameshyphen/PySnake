import numpy as np
from PIL import Image
from domain.Difficulty import Difficulty
from domain.Direction import Going
from domain.terrain.BuildTerrain import BuildTerrain

build_terrain = BuildTerrain(Difficulty.hard)
build_terrain.snake.Add_Tail()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Add_Tail()
build_terrain.snake.Change_direction(Going.down)
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Change_direction(Going.right)
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Change_direction(Going.up)
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.snake.Move_snake()
build_terrain.draw_snake_on_terrain()



zvals = build_terrain.area
# gradient between 0 and 1 for 256*256
array = np.linspace(0,1,256*256)

# reshape to 2d
mat = np.reshape(array,(256,256))

# Creates PIL image
img = Image.fromarray(np.uint8(zvals * 255) , 'L')
img.show()