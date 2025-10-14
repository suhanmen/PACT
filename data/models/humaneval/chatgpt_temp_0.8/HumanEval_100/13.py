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
    # initialize the list with the number of stones in the first level
    stones = [n]
    # keep track of the current level and number of stones
    level = 1
    num_stones = n
    # iterate until we've created n levels
    while level < n:
        # determine the number of stones in the next level
        if n % 2 == 0:
            num_stones += 2
        else:
            num_stones += 1
        # add the number of stones to the list and increment the level counter
        stones.append(num_stones)
        level += 1
    return stones
