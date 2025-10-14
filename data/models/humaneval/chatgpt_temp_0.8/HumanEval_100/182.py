def make_a_pile(n):
    stones = [n]
    level = n

    for i in range(n-1):
        if level % 2 == 0:
            level += 1
        else:
            level += 2

        stones.append(level)

    return stones
