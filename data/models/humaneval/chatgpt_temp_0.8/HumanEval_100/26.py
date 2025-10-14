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
    # Initialize the list with the first level's number of stones
    pile = [n]

    # Initialize the next number to be added based on whether n is even or odd
    next_num = n + 1 if n % 2 == 1 else n + 2

    # Add each subsequent level to the pile
    for i in range(n - 1):
        pile.append(next_num)
        next_num += 2 if n % 2 == 1 else 2 if i % 2 == 0 else 4

    return pile
