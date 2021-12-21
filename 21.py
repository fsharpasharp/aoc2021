import re

with open('input', 'r') as f:
    lines = f.read().splitlines()

start_pos = [int(re.findall(r'\d$', x).pop())-1 for x in lines]

class Die:
    def __init__(self):
        self.i = -1
        self.rolls = 0

    def next(self):
        self.rolls += 1
        self.i += 1
        self.i %= 100
        return self.i + 1

class Player:
    def __init__(self, pos):
        self.pos = pos
        self.points = 0

    def walk(self, walk):
        self.pos += walk
        self.pos %= 10
        self.points += self.pos+1
        if self.points >= 1000:
            return True

def play(players,d):
    while True:
        for player in players:
            roll = sum([d.next() for _ in range(3)])
            if player.walk(roll):
                return player


players = list(map(Player, start_pos))
d = Die()
p = play(players, d)
players.remove(p)
print(d.rolls * players.pop().points)

