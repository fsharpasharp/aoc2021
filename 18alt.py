import ast
from typing import Union, List
from itertools import product

with open('input', 'r') as f:
    lines = f.read().splitlines()

class Value:
    mapping = []

    def __init__(self, value, depth):
        self.value = value
        self.depth = depth

    def __iadd__(self, other):
        self.value += other.value
        return self


    @classmethod
    def objectify(cls, tree, depth = 0):
        if depth == 0:
            cls.mapping = []
        left = tree[0] 
        right = tree[1]

        if isinstance(left, list):
            cls.objectify(left, depth+1)
        else:
            tree[0] = Value(left, depth+1)
            Value.mapping.append(tree[0])
        if isinstance(right, list):
            cls.objectify(right, depth+1)
        else:
            tree[1] = Value(right, depth+1)
            Value.mapping.append(tree[1])

    def __repr__(self):
        return f'{self.value}'
    def __str__(self):
        return f'{self.value}'


def add_surrounding(node):
    left = node[0]
    right = node[1]

    idx = Value.mapping.index(left)

    if idx > 0:
        Value.mapping[idx-1] += left
    if idx < len(Value.mapping) - 2:
        Value.mapping[idx+2] += right

    del Value.mapping[idx+1]
    v = Value(0, left.depth-1)
    Value.mapping[idx] = v
    return v

def explode(line, depth=0) -> Union[bool, List]:
    left = line[0]
    right = line[1]
    if depth >= 4 and type(left) == Value and type(right) == Value:
        return left

    if isinstance(left, list):
        e = explode(left, depth+1)
        if e == True:
            return True
        if e:
            line[0] = add_surrounding(left)
            return True

    if isinstance(right, list):
        e = explode(right, depth+1)
        if e == True:
            return True
        if e:
            line[1] = add_surrounding(right)
            return True
    return False


def add_nodes(node):
    idx = Value.mapping.index(node)

    v0 = Value(node.value // 2, node.depth+1)
    v1 = Value((node.value+1) // 2, node.depth+1)
    Value.mapping[idx] = v0
    Value.mapping.insert(idx+1, v1)
    return [v0, v1]

def split(node) -> Union[bool, Value]:
    if type(node) == Value:
        if node.value > 9:
            return node
        return False

    s = split(node[0]) 
    if s == True:
        return True
    if s:
        node[0] = add_nodes(s)
        return True

    s = split(node[1]) 
    if s == True:
        return True
    if s:
        node[1] = add_nodes(s)
        return True

    return False

def magnitude(node) -> int:
    if type(node) == Value:
        return node.value

    return 3*magnitude(node[0]) + 2*magnitude(node[1])


def run_actions(line):
    Value.objectify(line)
    while True:
        if explode(line):
            continue
        if split(line):
            continue
        return

line = ast.literal_eval(lines[0])
for new_line in lines[1:]:
    line = ast.literal_eval(f'[{line},{new_line}]')
    run_actions(line)
print(magnitude(line))


maximum = 0
for line1, line2 in product(lines, lines):
    if line1 == line2:
        continue

    line = ast.literal_eval(f'[{line1},{line2}]')
    run_actions(line)
    maximum = max(maximum, magnitude(line))

    line = ast.literal_eval(f'[{line2},{line1}]')
    run_actions(line)
    maximum = max(maximum, magnitude(line))
print(maximum)
