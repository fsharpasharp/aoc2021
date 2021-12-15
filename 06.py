timer_size = 9
fish_timer = [0]*timer_size
timers = map(int, input().split(','))

for val in timers:
    fish_timer[val] += 1

for i in range(256):
    print(sum(fish_timer))
    births = fish_timer.pop(0)
    fish_timer.append(births)
    fish_timer[6] += births


print(sum(fish_timer))

