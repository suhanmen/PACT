def make_a_pile(n):
    stones_per_level = [n]
    current_stones = n

    for i in range(n-1):
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
        stones_per_level.append(current_stones)

    return stones_per_level
