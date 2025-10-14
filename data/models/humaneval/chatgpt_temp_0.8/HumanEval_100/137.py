def make_a_pile(n):
    stones_per_level = [n]
    num_stones = n
    for i in range(1, n):
        if n % 2 == 0:
            num_stones += i * 2
        else:
            num_stones += (i * 2) + 1
        stones_per_level.append(num_stones)
    return stones_per_level
