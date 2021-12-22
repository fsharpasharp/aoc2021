import re
from collections import defaultdict
from functools import reduce

with open('input', 'r') as f:
    lines = f.read().splitlines()

class Cuboid:
    def __init__(self, x_min, x_max, y_min, y_max, z_min, z_max):
        x = x_min, x_max
        y = y_min, y_max
        z = z_min, z_max
        self.coords = [x,y,z]
        length = lambda ab: ab[1]-ab[0]+1
        product = lambda x, y: x*y
        self.volume = reduce(product, map(length, self.coords), 1)

    def __and__(self, other):
        new_coords = []
        for i in range(len(self.coords)):
            c_min = max(self.coords[i][0], other.coords[i][0])
            c_max = min(self.coords[i][1], other.coords[i][1])
            if c_min > c_max:
                return
            new_coords.append(c_min)
            new_coords.append(c_max)

        return Cuboid(*new_coords)


    def __repr__(self):
        return str(self.coords)


value = defaultdict(int)
for line in lines:
    command, rest = line.split()
    numbers = re.findall(r'-?\d+', rest)

    new_cube = Cuboid(*map(int, numbers))
    
    v = value.copy()
    for cube, vol in value.items():
        intersection = new_cube & cube
        if intersection:
            v[intersection] -= vol
    value = v

    if command == "on":
        value[new_cube] += 1

volume = 0
for cube, v in value.items():
    volume += cube.volume * v
print(volume)
