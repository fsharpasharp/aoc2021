from itertools import product, combinations
from collections import defaultdict

with open('input', 'r') as f:
    scans = [x.splitlines()[1:] for x in f.read().split('\n\n')]

class Scanner:
    def __init__(self, scans):
        self.coords = set()
        for scan in scans:
            self.coords.add(tuple(map(int, scan.split(','))))

    def normalize(self, new_coords, offsets):
        new_set = set()
        for x,y,z in new_coords:
            new_set.add((x - offsets[0], y - offsets[1], z - offsets[2]))
        self.coords = new_set
        self.offsets = offsets

    @classmethod
    def rotate_xy(cls, coords):
        for _ in range(4):
            new_set = set()
            for x, y, z in coords:
                new_set.add((y, -x, z))
            coords = new_set
            yield coords

    def orientations(self):
        coords = self.coords.copy()
        
        # shift coordinates
        for _ in range(3):
            new_set = set()
            for x, y, z in coords:
                new_set.add((z, x, y))
            coords = new_set

            yield from Scanner.rotate_xy(coords)

            # look back
            new_set = set()
            for x, y, z in coords:
                new_set.add((-x, y, -z))
            coords = new_set
            yield from Scanner.rotate_xy(coords)



def find_and_orient(this, others, unique, visited=set()):
    if this in visited:
        return
    visited.add(this)

    for other in others:
        if other == this:
            continue
        for orientation in other.orientations():
            freq = defaultdict(int)
            for (x,y,z), (a,b,c) in product(this.coords, orientation):
                freq[(a-x,b-y,c-z)] += 1

            maximum_offset = max(freq.items(), key=lambda x: x[1])
            if maximum_offset[1] >= 12:
                other.normalize(orientation, maximum_offset[0])
                unique |= other.coords

                idx = others.index(other)
                find_and_orient(others[idx], others, unique, visited)

ss = list(map(Scanner, scans))

first = ss[0]
unique = set(first.coords)
find_and_orient(first, ss, unique)
print(len(unique))

manhattan = [sum(map(lambda ab: abs(ab[0]-ab[1]), zip(x.offsets, y.offsets))) for x,y in combinations(ss,2)]
print(max(manhattan))



