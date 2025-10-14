def make_a_pile(n):
    stones_in_level = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones_in_level.append(n + i)
        else:
            stones_in_level.append(n + 2*i)
    return stones_in_level
