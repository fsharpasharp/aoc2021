import sys


lines = sys.stdin.read().splitlines()

size = 1000

grid = [[0]*size for i in range(size)]

for line in lines:
    start, end = line.split(' -> ')

    x1, y1 = map(int, start.split(','))
    x2, y2 = map(int, end.split(','))


    xs = range(min(x1,x2), max(x1,x2)+1)
    ys = range(min(y1,y2), max(y1,y2)+1)

    if x1 != x2 and y1 != y2:
        if (x2 > x1 and y1 > y2) or (x2 < x1 and y1 < y2):
            ys = ys[::-1]

        for x, y in zip(xs,ys):
            grid[y][x] += 1
    else:
        for x in xs:
            for y in ys:
                grid[y][x] += 1


overlapping = 0
for y in range(size):
    for x in range(size):
        if grid[y][x] >= 2:
            overlapping += 1


print(overlapping)


