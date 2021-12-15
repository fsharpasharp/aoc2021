from itertools import product

class Grid:
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            row = []
            for char in line:
                row.append(int(char))
            self.grid.append(row)
        self.height = len(self.grid)
        self.width = len(self.grid[0])

    def adjacent(self, y, x):
        candidates = [(y+i,x) for i in [-1,1]] + [(y,x+i) for i in [-1,1]]
        return filter(lambda a : 0 <= a[0] < self.height and 0 <= a[1] < self.width, candidates)

    def lower_than_neighbors(self, y, x):
        current_value = self.grid[y][x]
        neighbor_values = map(lambda a: self.grid[a[0]][a[1]], self.adjacent(y,x))
        return(all(current_value <= neighbor for neighbor in neighbor_values))

    def basin_size(self, y, x):
        self.visited = set()
        return self.DFS(y, x, -1)

    def DFS(self, y, x, prev_value):
        current_value = self.grid[y][x]
        if (y,x) in self.visited or current_value <= prev_value or current_value == 9:
            return 0
        self.visited.add((y,x))

        return 1 + sum([self.DFS(i,j, current_value) for i, j in self.adjacent(y,x)])



with open('input.txt', 'r') as file:
    lines = file.read().splitlines()

g = Grid(lines)

basin_sizes = []
for y, x in product(range(g.height), range(g.width)):
    if g.lower_than_neighbors(y, x):
        basin_sizes.append(g.basin_size(y, x))

prod = 1
for factor in sorted(basin_sizes)[-3::]:
    prod *= factor

print(prod)

