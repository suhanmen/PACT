def make_a_pile(n):
    stones_per_level = [n]
    for i in range(n-1):
        if n % 2 == 0:
            stones_per_level.append(n + i + 1)
        else:
            stones_per_level.append(n + 2*i + 1)
    return stones_per_level
