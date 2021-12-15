import sys
from operator import itemgetter
from collections import defaultdict

class Board:
    def __init__(self):
        self.coords = {}
        self.sum = 0
        self.checked_x = defaultdict(int)
        self.checked_y = defaultdict(int)
        self.size = 0

    def parse_row(self, row):
        for idx, num in enumerate(row.split()):
            num = int(num)
            self.sum += num
            self.coords[num] = (self.size, idx)

        self.size += 1


    def bingo_sum(self, numbers):
        for depth, number in enumerate(numbers):
            if number not in self.coords:
                continue

            self.sum -= number
            if self.check_win(*self.coords[number]):
                return self.sum*number, depth


    def check_win(self, row, column):
        self.checked_x[row] += 1
        self.checked_y[column] += 1

        if self.checked_x[row] == self.size or self.checked_y[column] == self.size:
            return True


        return False

lines = sys.stdin.read().splitlines()

boards = []
for line in lines[1:]:
    if line == '':
        boards.append(Board())
    else:
        boards[-1].parse_row(line)

bingo_numbers = [int(x) for x in lines[0].split(',')]

bingo_sums = [board.bingo_sum(bingo_numbers) for board in boards]

fastest = min(bingo_sums, key=itemgetter(1))
print(fastest)

slowest = max(bingo_sums, key=itemgetter(1))
print(slowest)
