from itertools import product

class Grid:
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append([int(x) for x in line])

        self.n_flashes = 0

        self.height = len(lines)
        self.width = len(lines[0])

    def adjacent(self, y, x):
        adjacent = []
        one_step = range(-1, 2)

        adjacent = [(y+i, x+j) for i, j in product(one_step, repeat=2)]
        return filter(lambda yx: 0 <= yx[0] < self.height and 0 <= yx[1] < self.width, adjacent)


    def flash(self, y_orig, x_orig):
        if (y_orig, x_orig) in self.flashed:
            return

        self.flashed.add((y_orig, x_orig))
        self.n_flashes += 1

        
        for (y, x) in self.adjacent(y_orig,x_orig):
            self.grid[y][x] += 1
            if self.grid[y][x] >= 10:
                self.flash(y, x)

    
    def step(self):
        self.flashed = set()

        for y, x in product(range(self.height), range(self.width)):
            self.grid[y][x] += 1
            if self.grid[y][x] >= 10:
                self.flash(y, x)

        for y, x in product(range(self.height), range(self.width)):
            if (y, x) in self.flashed:
                self.grid[y][x] = 0



with open('input2', 'r') as f:
    lines = f.read().splitlines()

g = Grid(lines)
for i in range(100):
    g.step()
print(g.n_flashes)
