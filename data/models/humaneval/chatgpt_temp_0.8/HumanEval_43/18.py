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
    # Check that the list has at least two elements
    if len(l) < 2:
        return False
    
    # Use a set to keep track of seen elements
    seen = set()
    
    for num in l:
        # If the negative of the current number is in the set, we've found a pair that sums to zero
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we've gone through the whole list and haven't found a pair that sums to zero, return False
    return False
