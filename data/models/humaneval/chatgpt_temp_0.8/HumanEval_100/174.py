def make_a_pile(n):
    stones_in_levels = [n]
    for i in range(1, n):
        if n % 2 == 1:
            stones_in_levels.append(stones_in_levels[-1] + 2)
        else:
            stones_in_levels.append(stones_in_levels[-1] + 1)
        n -= 1
    return stones_in_levels
