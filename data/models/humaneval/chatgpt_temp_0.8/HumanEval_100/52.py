def make_a_pile(n):
    stones_per_level = [n]
    num_stones = n
    for i in range(1, n):
        if num_stones % 2 == 0:
            num_stones += 1
        else:
            num_stones += 2
        stones_per_level.append(num_stones)
    return stones_per_level
