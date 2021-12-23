from collections import defaultdict
with open('input', 'r') as f:
    lines = f.read().splitlines()[2:-1]

lines = [list(line.replace('#','').strip()) for line in lines]
transposed_lines = [[] for _ in range(len(lines[0]))]
for line in lines:
    for l, c in zip(transposed_lines, line):
        l.append(c)
    
transposed_lines = [list(reversed(l)) for l in transposed_lines]
costs = {k:v for k, v in zip('ABCD', [1,10,100,1000])}
        

class WaitingSpot:
    def __init__(self):
        self.item = None

    def __repr__(self):
        return 'Waiting spot ' + str(self.item)

    def pop(self):
        item = self.item
        self.item = None
        return item, 0

    def unpop(self, item):
        self.item = item
        return 0

    def can_walk(self):
        return self.item == None

class Stack:
    def __init__(self, char_type, items):
        self.char_type = char_type
        self.items = items
        self.capacity = len(items)

    def __repr__(self):
        return 'Pit ' + str(self.items)

    def done(self):
        return len(self.items) == self.capacity and all(map(lambda c: c == self.char_type, self.items))

    def can_walk(self):
        return all(map(lambda c: c == self.char_type, self.items))

    def pop(self):
        if self.items:
            item = self.items.pop()
            return item, self.cost(item)
        return None, 0

    def unpop(self, item):
        self.items.append(item)
        return self.cost(item)

    # Cost is proportional to empty slots
    def cost(self, item):
        return ((self.capacity-len(self.items))+1)*costs[item]



stacks = []
for c, s in zip('ABCD', transposed_lines):
    stacks.append(Stack(c, s))

row = [WaitingSpot(), WaitingSpot(), stacks[0], WaitingSpot(), stacks[1], WaitingSpot(), stacks[2], WaitingSpot(), stacks[3], WaitingSpot(), WaitingSpot()]

char_to_stack_idx = defaultdict(int)
for i, r in enumerate(row):
    if type(r) == Stack:
        char_to_stack_idx[r.char_type] = i

def path_clear(row, l, u):
    l, u = min(l, u), max(l,u)
    for i in range(l+1,u):
        if type(row[i]) == WaitingSpot and row[i].item:
            return False
    return True

best_score = float('inf')
def DFS(row, score=0):
    global best_score
    if score >= best_score:
        return
    if all(i.done() for i in stacks):
        best_score = min(best_score, score)
        print(best_score)
        return

    for i, start in enumerate(row):
        if type(start) == WaitingSpot:
            item, start_cost = start.pop()
            if item == None:
                continue
            j = char_to_stack_idx[item]
            if path_clear(row, i, j) and row[j].can_walk():
                extra_cost = row[j].unpop(item)
                DFS(row, score + start_cost + abs(j-i)*costs[item]+extra_cost)
                row[j].pop()
            start.unpop(item)
            continue

        # Let's not start from here if we're already in the right stack and it's homogeneous
        if start.can_walk():
            continue
        item, start_cost = start.pop()
        if item == None:
            continue

        for j, end in enumerate(row):
            if i == j:
                continue
            # Let's only go to the end game stack
            if type(end) == Stack and j != char_to_stack_idx[item]:
                continue

            if path_clear(row, i, j) and end.can_walk():
                extra_cost = row[j].unpop(item)
                DFS(row, score + start_cost + abs(j-i)*costs[item]+extra_cost)
                row[j].pop()

        start.unpop(item)

DFS(row)
