import sys

lines = [line for line in sys.stdin.read().splitlines()]


width = len(lines[0])
height = len(lines)

freq = width*[0] 

for line in lines:
    for i, num in enumerate(line):
        freq[i] += int(num)

a = 0
b = 0
for value in freq:
    a <<= 1
    b <<= 1
    if 2*value > height:
        a += 1
    else:
        b += 1

print(a*b)
