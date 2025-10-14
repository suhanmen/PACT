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
    # Check if the list has at least 2 elements
    if len(l) < 2:
        return False
    # Create a set to store seen values
    seen = set()
    # Iterate over the list
    for x in l:
        # Check if the complement of x has been seen before (i.e., -x)
        if -x in seen:
            return True
        # Add the current value to the set of seen values
        seen.add(x)
    # If no pair sums to zero, return False
    return False
