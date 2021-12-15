with open('input', 'r') as f:
    lines = f.read().splitlines()

pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
        }
def remaining_parenthesis(string):
    stack = []

    for c in string:
        if c in pair:
            stack.append(pair[c])
        else:
            top = stack.pop()
            if not top or top != c:
                return []
    return stack

points = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4,
        }

counts = []
for line in lines:
    remaining = remaining_parenthesis(line) 
    if not remaining:
        continue

    count = 0
    while remaining:
        count *= 5
        count += points[remaining.pop()]
    counts.append(count)

counts = sorted(counts)
print(counts[len(counts)//2])
