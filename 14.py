from collections import Counter, defaultdict

with open('input2', 'r') as f:
    start_string, rules = f.read().split('\n\n')


rule_mapping = {}
for rule in rules.splitlines():
    key, value = rule.split(' -> ')
    rule_mapping[key[0],key[1]] = value


def iterate(input, rules):
    new_dict = defaultdict(int)
    for k, v in input.items():
        if k not in rules:
            continue

        new_char = rules[k]

        new_dict[k[0], new_char] += v
        new_dict[new_char, k[1]] += v

    return new_dict


c = dict(Counter(zip(start_string, start_string[1:])))

for _ in range(40):
    c = iterate(c, rule_mapping)

counts = defaultdict(int)
counts[start_string[-1]] += 1
for k, v in c.items():
    counts[k[0]] += v

mc = Counter(counts).most_common()
print(mc)
print(mc[0][1] - mc[-1][1])
