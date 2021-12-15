import sys
from collections import defaultdict

lines = sys.stdin.read().splitlines()

count = 0
for line in lines:
    fst, snd = line.split(' | ')

    words_by_length = defaultdict(list)

    for word in fst.split():
        words_by_length[len(word)].append(set(word))

    val = {}
    val[1] = words_by_length[2][0]
    val[4] = words_by_length[4][0]
    val[7] = words_by_length[3][0]
    val[8] = words_by_length[7][0]

    for word in words_by_length[5]:
        if val[1] <= word:
            val[3] = word
        elif val[4] - val[1] <= word:
            val[5] = word
        else:
            val[2] = word

    for word in words_by_length[6]:
        if val[3] <= word:
            val[9] = word
        elif val[5] <= word:
            val[6] = word
        else:
            val[0] = word

    string_to_digit = dict((frozenset(v), str(k)) for k, v in val.items())


    number = ''
    for word in snd.split():
        number += string_to_digit[frozenset(word)]

    count += int(number)



print(count)
