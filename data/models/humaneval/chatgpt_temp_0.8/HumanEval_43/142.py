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
    # Check if the list has at least two elements
    if len(l) < 2:
        return False
    
    # Use a set to keep track of the elements seen so far
    seen = set()
    
    # Iterate over the elements in the list
    for x in l:
        # Check if there is another element that sums to -x
        if -x in seen:
            return True
        else:
            seen.add(x)
    
    # If we reach this point, there is no pair that sums to zero
    return False
