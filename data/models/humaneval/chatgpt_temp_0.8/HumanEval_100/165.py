def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    stones_per_level = [n]
    current_stones = n
    for i in range(1, n):
        if current_stones % 2 == 0:
            current_stones += 1
        else:
            current_stones += 2
        stones_per_level.append(current_stones)
    return stones_per_level
