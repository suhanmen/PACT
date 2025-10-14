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
    # Check input list length, early return False for length less than 2
    if len(l) < 2:
        return False
    
    # Create a set of seen numbers
    seen = set()
    
    # Iterate over input list
    for num in l:
        # Check if the negation of the current number has been seen before
        if -num in seen:
            return True
        # Add the current number to the set of seen numbers
        seen.add(num)
    
    # No pair of distinct numbers sum to zero
    return False
