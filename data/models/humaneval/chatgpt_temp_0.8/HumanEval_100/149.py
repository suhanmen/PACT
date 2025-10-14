def make_a_pile(n):
    stones_per_level = [n]  # start with n stones in the first level
    for i in range(1, n):  # add stones to each level up to level n
        if n % 2 == 0:  # if n is even
            stones_per_level.append(n + i*2)  # add even numbers
        else:
            stones_per_level.append(n + i*2 - 1)  # add odd numbers
    return stones_per_level
