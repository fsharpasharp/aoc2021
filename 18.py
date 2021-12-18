import ast 
import re
from itertools import product

def snail(l):
    xs = list(re.finditer(r'\d+', l))
    snailfish = list(l)[:xs[0].start()]
    for x, y in zip(xs, xs[1:]):
        snailfish.append(int(x[0]))
        snailfish += l[x.end():y.start()]
    snailfish.append(int(xs[-1][0]))
    snailfish += l[xs[-1].end():]
    return snailfish


def explode(l):
    s = 0
    def find_int(start_index, rev=False):
        r = None
        if rev:
            r = range(start_index, -1, -1)
        else:
            r = range(start_index, len(l))
        for i in r:
            if type(l[i]) == int:
                return i

    def explode_helper(i):
        left = l[i+1]
        right = l[i+3]
        del l[i+1:i+5]
        ri = find_int(i)
        if ri:
            l[ri] += right
        li = find_int(i, True)
        if li:
            l[li] += left
        l[i] = 0


    for i, c in enumerate(l):
        if c == '[':
            s += 1
        elif c == ']':
            s -= 1
        if s == 5:
            explode_helper(i)
            return True

def split(l):
    for i, c in enumerate(l):
        if type(c) == int and c > 9:
            del l[i]
            insert_this = ['[', c//2, ',', (c+1)//2, ']']

            for c in reversed(insert_this):
                l.insert(i, c)
            return True


def magnitude(node):
    if type(node) == int:
        return node
    return 3*magnitude(node[0]) + 2*magnitude(node[1])


def evaluate(a, b):
    current = ['['] + snail(a) + [','] + snail(b) + [']']
    while True:
        if explode(current):
            continue
        if split(current):
            continue
        break
    return ''.join(map(str, current))

with open('input', 'r') as f:
    ls = f.read().splitlines()

current = ls[0]
for l in ls[1:]:
    current = evaluate(current, l)

mag = lambda x : magnitude(ast.literal_eval(x))
print(mag(current))
print(max([mag(evaluate(a,b)) for a, b in product(ls, ls) if a != b]))
