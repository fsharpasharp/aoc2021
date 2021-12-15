
with open('input', 'r') as f:
    lines = f.read().splitlines()



pair = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
        }
def first_illegal(string):
    stack = []

    for c in string:
        if c in pair:
            stack.append(pair[c])
        else:
            top = stack.pop()
            if not top or top != c:
                return c

points = {
        ')': 3,
        ']': 57,
        '}': 1197,
        '>': 25137,
        }

count = 0
for line in lines:
    illegal = first_illegal(line)
    if illegal:
        count += points[illegal]
print(count)
        
