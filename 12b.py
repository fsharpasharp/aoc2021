from collections import defaultdict

with open('input', 'r') as f:
    lines = f.read().splitlines()

graph = defaultdict(set)
for line in lines:
    start, end = line.split('-')
    graph[start].add(end)
    graph[end].add(start)

def DFS(word, visited, extra = 0):
    if word == "end":
        return 1

    used_extra = False
    if word.islower() and word in visited:
        if extra == 0 or word == 'start':
            return 0
        used_extra = True
        extra -= 1

    visited.add(word)
    s = sum([DFS(new_word, visited, extra) for new_word in graph[word]])
    if word in visited and not used_extra:
        visited.remove(word)
    return s

print(DFS("start", set()))
print(DFS("start", set(), 1))
