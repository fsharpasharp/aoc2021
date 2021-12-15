import sys

lines = [line for line in sys.stdin.read().splitlines()]

width = len(lines[0])
height = len(lines)

for column in range(width):
    ones = sum([int(line[column]) for line in lines])
    if (2*ones >= height):
        lines = list(filter(lambda line : line[column] == '1', lines))
    else:
        lines = list(filter(lambda line : line[column] == '0', lines))
    print(list(lines))
