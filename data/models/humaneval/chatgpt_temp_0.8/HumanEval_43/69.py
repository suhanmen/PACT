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
    # First, we check that the list has at least two elements
    if len(l) < 2:
        return False
    # Then, we use a set to keep track of the integers we have seen so far
    seen = set()
    for x in l:
        # For each integer x in the list, we check if its negation -x is in seen
        if -x in seen:
            # If it is, we have found two distinct integers that sum to zero
            return True
        seen.add(x)
    # If we finish the loop without finding a pair, we return False
    return False
