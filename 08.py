import sys
from collections import defaultdict
from math import prod


lines = sys.stdin.read().splitlines()


product = {}
product[46410] = '0'
product[6] = '1'
product[13090] = '2'
product[5610] = '3'
product[858] = '4'
product[36465] = '5'
product[255255] = '6'
product[102] = '7'
product[510510] = '8'
product[72930] = '9'

count = 0
for line in lines:
    fst, snd = line.split(' | ')

    words_by_length = defaultdict(list)

    for word in fst.split():
        words_by_length[len(word)].append(set(word))

    a = words_by_length[3][0] - words_by_length[2][0]
    x = words_by_length[7][0] - a - words_by_length[4][0]
    y = set()
    for word in words_by_length[5]:
        y |= words_by_length[7][0] - word
    y -= words_by_length[2][0]
    common = x&y
    g = x-common
    b = y-common
    e = common
    d = words_by_length[7][0]-words_by_length[3][0]-e-g-b
    
    y = set()
    for word in words_by_length[6]:
        y |= words_by_length[7][0] - word

    c = y - d - e
    f = words_by_length[2][0] - c

    letterVal = {}
    letterVal[a.pop()] = 17
    letterVal[b.pop()] = 13
    letterVal[c.pop()] = 2
    letterVal[d.pop()] = 11
    letterVal[e.pop()] = 7
    letterVal[f.pop()] = 3
    letterVal[g.pop()] = 5


    num = ''
    for word in snd.split():
        prod = 1
        for letter in word:
            prod *= letterVal[letter]
        num += product[prod]

    count += int(num)



print(count)
