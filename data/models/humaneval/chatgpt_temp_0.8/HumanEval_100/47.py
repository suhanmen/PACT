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
    pile = [n] # first level has n stones
    for i in range(1, n): # iterate through the remaining levels
        if n % 2 == 0: # if n is even
            pile.append(n + 2*i) # add the next even number of stones
        else: # if n is odd
            pile.append(n + 2*i - 1) # add the next odd number of stones
    return pile
