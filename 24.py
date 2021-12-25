import re

with open('input', 'r') as f:
    lines = f.read().split('inp w')[1:]

numbers = []
offsets = {}
for i, line in enumerate(lines):
    pop_or_store, retrieve, store = [int(val) for i, val in enumerate(re.findall('-?\d+', line)) if i in [2,3,9]]
    if pop_or_store == 26:
        j, stored_constant = numbers.pop() 
        offsets[j] = (i,stored_constant+retrieve)
    else: 
        numbers.append((i, store))

def combos(offsets, depth = 0, items=[0]*len(offsets)*2):
    if depth == len(offsets):
        yield int(''.join(map(str, items)))
        return
    i, (j, offset) = offsets[depth]
    for k in range(1,10):
        if 0 < k+offset < 10:
            items[i] = k
            items[j] = k+offset
            yield from combos(offsets, depth+1, items)

c = list(combos(list(offsets.items())))
print(min(c), max(c))
