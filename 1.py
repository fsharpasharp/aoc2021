import sys
xs = [int(x) for x in sys.stdin.read().splitlines()]

def n_increasing(xs, ys): 
    return sum([b > a for (a,b) in zip(xs,ys)])

print(n_increasing(xs, xs[1:]))
print(n_increasing(xs, xs[2:]))
