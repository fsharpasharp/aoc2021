from operator import not_

with open('input', 'r') as f:
    lines = f.read().splitlines()

width = len(lines[0])
def extract_line(lines, f=lambda x:x):
    for column in range(width):
        height = len(lines)
        ones = sum([int(line[column]) for line in lines])

        keep = None
        if f(2*ones >= height):
            keep = '1'
        else:
            keep = '0'
        lines = list(filter(lambda line: line[column] == keep, lines))

        if len(lines) == 1:
            return int(str(lines[0]),2)

print(extract_line(lines)*extract_line(lines, not_))
