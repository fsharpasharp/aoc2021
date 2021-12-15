with open('input2', 'r') as f:
    lines = f.read().splitlines()

numbers = []
i = 0
line = lines[i]
while line:
    numbers.append(tuple(map(int, line.split(','))))
    line = lines[i]
    i += 1
folds = [lines[i].split()[2].split('=') for i in range(i, len(lines))]
points = set(numbers)

def fold_paper(fold, points):
    fold_direction = fold[0]
    where = int(fold[1])
    new_points = set()
    for (x,y) in points:
        if fold_direction == 'y' and y >= where:
            points.add((x,2*where-y))
        elif fold_direction == 'x' and x >= where:
            points.add((2*where-x,y))
        else:
            points.add((x,y))
    return new_points

for fold in folds:
    points = fold_paper(fold, points)
    print(len(points))

y_max = 0
x_max = 0
for x, y in points:
    y_max = max(y_max, y+1)
    x_max = max(x_max, x+1)

for y in range(y_max):
    for x in range(x_max):
        if (x,y) in points:
            print('#', end='')
        else:
            print('.', end='')
    print()
                    

