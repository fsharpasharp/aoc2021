import sys

lines = [line.split() for line in sys.stdin.read().splitlines()]

aim = 0
horizontal = 0
depth = 0

for command, value in lines:
    value = int(value)
    if command == "down":
        aim += value
    elif command == "up":
        aim -= value
    else:
        horizontal += value
        depth += aim * value

print(horizontal*depth)
