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
    # Initialize a set to store the seen numbers
    seen = set()
    
    # Iterate through the list
    for num in l:
        # If the negative of the current number is in the set, we have found a pair that sums to zero
        if -num in seen:
            return True
        # Otherwise, add the current number to the set of seen numbers
        seen.add(num)
    
    # If we reach this point, there are no pairs that sum to zero
    return False
