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
    pile = [n]  # Initialize pile with first level of n stones
    stones = n  # Initialize number of stones for next level as n
    for i in range(1, n):  # Loop for n-1 levels
        if n % 2 == 0:  # If n is even
            stones += 2  # Next level has two more stones
        else:  # If n is odd
            stones += 1  # Next level has one more stone
        pile.append(stones)  # Add number of stones for next level to pile
    return pile
