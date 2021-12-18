import re
from itertools import product

with open('input2', 'r') as f:
    line = f.read().strip()

x1, x2, y1, y2 = map(int, re.findall(r'-?\d+', line))

y_max = abs(y1+1)*abs(y1)//2
print(y_max)

def update_position(x_vel, y_vel, x, y):
    return max(x_vel-1, 0 ), y_vel-1, x + x_vel, y + y_vel

s = 0
for a, b in product(range(1, x2+1), range(y1, abs(y1))):
    x, y = 0, 0
    x_vel, y_vel = a, b
    while x <= x2 and y1 <= y:
        if y <= y2 and x1 <= x:
            s += 1
            break
        x_vel, y_vel, x, y = update_position(x_vel, y_vel, x, y)
print(s)

