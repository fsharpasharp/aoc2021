import re
from itertools import product, count
from typing import Union

with open('input', 'r') as f:
    grid = list(map(list, f.read().splitlines()))


def step(grid):
    height = len(grid) 
    width = len(grid[0]) 

    moved = False
    new_grid = [width*['.'] for _ in range(height)]
    for i, j in product(range(height), range(width)):
        if grid[i][j] == '>':
            if grid[i][(j+1)%width] == '.':
                new_grid[i][(j+1)%width] = '>'
                moved = True
            else:
                new_grid[i][j] = '>'

    for i, j in product(range(height), range(width)):
        if grid[i][j] == 'v':
            if new_grid[(i+1)%height][j] == '.' and grid[(i+1)%height][j] != 'v':
                new_grid[(i+1)%height][j] = 'v'
                moved = True
            else:
                new_grid[i][j] = 'v'
    return moved, new_grid


moved = True
i = 0
while moved:
    moved, grid = step(grid)
    i += 1

print(i)
