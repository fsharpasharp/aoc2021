from heapq import *

class Grid:
    def __init__(self, lines, factor):
        self.grid = []
        for line in lines:
            self.grid.append([int(x) for x in line])

        self.orig_height = len(lines)
        self.orig_width = len(lines[0])

        self.height = len(lines)*factor
        self.width = len(lines[0])*factor

    def adjacent(self, y, x):
        adjacent = [(y+1, x), (y, x+1), (y-1, x), (y, x-1)]
        return filter(lambda yx: 0 <= yx[0] < self.height and 0 <= yx[1] < self.width, adjacent)


    def BFS(self):
        q = [(0, 0, 0)]
        visited = set()
        while q:
            steps, y, x  = heappop(q)
            if (y, x) in visited:
                continue
            visited.add((y,x))

            if (y,x) == (self.height-1, self.width-1):
                return steps

            for new_y, new_x in self.adjacent(y,x):
                times = 0
                times += new_y // self.orig_height
                times += new_x // self.orig_width

                y_modulo = new_y % self.orig_height
                x_modulo = new_x % self.orig_height

                new_val = (self.grid[y_modulo][x_modulo]+times-1)%9+1

                heappush(q, (steps+new_val, new_y, new_x))

with open('input', 'r') as f:
    lines = f.read().splitlines()

g = Grid(lines,1)
print(g.BFS())
g = Grid(lines,5)
print(g.BFS())
