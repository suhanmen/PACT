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
    stones_in_levels = [n]
    stones_in_current_level = n
    for i in range(n-1):
        if stones_in_current_level % 2 == 0:
            stones_in_current_level += 1
        else:
            stones_in_current_level += 2
        stones_in_levels.append(stones_in_current_level)
    return stones_in_levels
