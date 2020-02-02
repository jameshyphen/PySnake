import matplotlib as mpl
from matplotlib import pyplot
import numpy as np

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


# make a color map of fixed colors
cmap = mpl.colors.ListedColormap(['white', 'black'])
bounds = [0, 0, 1, 1]
norm = mpl.colors.BoundaryNorm(bounds, cmap.N)

# tell imshow about color map so that only set colors are used
img = pyplot.imshow(zvals, interpolation='nearest',
                    cmap=cmap, norm=norm)

# make a color bar
pyplot.colorbar(img, cmap=cmap,
                norm=norm, boundaries=bounds, ticks=[1, 0])

pyplot.show()
