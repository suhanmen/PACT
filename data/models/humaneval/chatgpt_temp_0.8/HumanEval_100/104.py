def make_a_pile(n):
    stones_per_level = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones_per_level.append(n + 2*i)
        else:
            stones_per_level.append(n + 2*(i-1) + 1)
    return stones_per_level
