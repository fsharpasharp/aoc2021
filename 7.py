from collections import defaultdict

crab_pos = list(map(int, input().split(',')))

crabs = defaultdict(int)
positions = max(crab_pos)


for pos in crab_pos:
    crabs[pos] += 1

cost_func = [0]*(positions+1)
for i in range(1,len(cost_func)):
    cost_func[i] = cost_func[i-1]+i
    
cost = [0]*positions
for i in range(len(cost)):
    for key, val in crabs.items():
        cost[i] += cost_func[abs(key-i)]*val

print(min(cost))
