python
def make_a_pile(n):
    stones_per_level = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones_per_level.append(n + i * 2)
        else:
            stones_per_level.append(n + i * 2 - 1)
    return stones_per_level
