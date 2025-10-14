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
    stones_per_level = [n] # Create a list with the number of stones in the first level
    
    for i in range(n-1): # Loop through the remaining levels
        if n % 2 == 0: # If n is even, add the next even number of stones
            n += 2
        else: # If n is odd, add the next odd number of stones
            n += 1
        stones_per_level.append(n) # Add the number of stones to the list
    
    return stones_per_level
