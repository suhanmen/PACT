def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
    # Create a set to keep track of the elements seen so far
    seen = set()
    # Iterate over the list
    for x in l:
        # Compute the opposite of x
        opposite = -x
        # If the opposite has been seen before, we found a pair
        if opposite in seen:
            return True
        # Otherwise, add x to the set of seen elements
        seen.add(x)
    # If we finished the loop without finding a pair, return False
    return False
