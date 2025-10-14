def make_a_pile(n):
    stones_in_level = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones_in_level.append(n + i * 2)
        else:
            stones_in_level.append(n + i * 2 - 1)
    return stones_in_level
