import re
from itertools import product

with open('input', 'r') as f:
    lines = f.read().splitlines()


points = set()
for line in lines:
    command, rest = line.split()
    numbers = re.findall(r'-?\d+', rest)
    x_min, x_max, y_min, y_max, z_min, z_max = map(int, numbers)
    x_min = max(x_min, -50)
    y_min = max(y_min, -50)
    z_min = max(z_min, -50)

    x_max = min(x_max, 50)
    y_max = min(y_max, 50)
    z_max = min(z_max, 50)



    s = set(product(range(x_min,x_max+1), range(y_min, y_max+1), range(z_min, z_max+1)))
    if command == "on":
        points |= s
    elif command == "off":
        points -= s



print(len(points))
