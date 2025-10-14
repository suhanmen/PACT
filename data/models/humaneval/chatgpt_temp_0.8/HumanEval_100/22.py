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
    pile = [n]
    num_stones = n
    
    for i in range(n-1):
        if num_stones % 2 == 0:
            num_stones += 1
        else:
            num_stones += 2
        pile.append(num_stones)
    
    return pile
