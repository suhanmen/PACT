def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    """
    pile = [n]  # Start with the first level of n stones
    for i in range(1, n):
        if n % 2 == 0:  # If n is even
            stone_count = n + (i * 2)  # Add the next even number
        else:  # If n is odd
            stone_count = n + ((i * 2) - 1)  # Add the next odd number
        pile.append(stone_count)  # Add the new level to the pile list
    return pile
