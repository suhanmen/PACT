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
    stones = [n] # initialize the first level with n stones
    for i in range(1, n):
        if n % 2 == 0: # if n is even, add the next even number to the pile
            stones.append(n + 2*i)
        else: # if n is odd, add the next odd number to the pile
            stones.append(n + 2*i - 1)
    return stones
