def make_a_pile(n):
    stones_per_level = [n]
    for i in range(n-1):
        if n % 2 == 0:
            stones_per_level.append(stones_per_level[-1] + 2)
        else:
            stones_per_level.append(stones_per_level[-1] + 1)
        n += 1
    return stones_per_level
