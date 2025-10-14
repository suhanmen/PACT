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
    # Check for edge cases
    if len(l) < 2:
        return False

    # Create a set of elements in the list
    elements = set(l)
    
    # Check if the negative of each element is in the set
    for num in l:
        if -num in elements:
            # Check if the negative element is not itself
            if num != -num:
                return True
    
    # If no pair sums to zero, return False
    return False
