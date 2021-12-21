import re
from collections import  defaultdict

universes = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}

def DP(outcomes, player_wins, player):
    new_outcomes = defaultdict(int)
    for (pos, points), starting_universes in outcomes.items():
        for dice_roll, universe_factor in universes.items():
            new_pos = list(pos)
            new_pos[player] = (new_pos[player] + dice_roll)%10
            new_points = list(points)
            new_points[player] = (new_pos[player] + 1)+points[player]
            
            new_universes = starting_universes*universe_factor
            if new_points[player] >= 21:
                player_wins[player] += new_universes
                continue
            new_outcomes[(tuple(new_pos), tuple(new_points))] += new_universes
    return new_outcomes

with open('input', 'r') as f:
    lines = f.read().splitlines()
start_pos = tuple(int(re.findall(r'\d$', x).pop())-1 for x in lines)

outcomes = defaultdict(int)
outcomes[(start_pos), (0,0)] = 1
player_wins = [0,0]
i = 0

while outcomes:
    outcomes = DP(outcomes, player_wins, i%2)
    i += 1

print(player_wins)
print(max(player_wins))
