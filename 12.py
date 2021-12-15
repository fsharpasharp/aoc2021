from collections import defaultdict

with open('input', 'r') as f:
    lines = f.read().splitlines()

graph = defaultdict(set)
for line in lines:
    start, end = line.split('-')
    graph[start].add(end)
    graph[end].add(start)

def DFS(word, visited):
    if word.islower() and word in visited:
        return 0
    if word == "end":
        return 1

    visited.add(word)
    s = sum([DFS(new_word, visited) for new_word in graph[word]])
    if word in visited:
        visited.remove(word)
    return s

print(DFS("start", set()))
