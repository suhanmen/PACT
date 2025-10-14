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
    stones = [n]
    for i in range(1, n):
        if n % 2 == 0:
            stones.append(n + 2 * i)
        else:
            stones.append(n + 2 * i - 1)
    return stones
