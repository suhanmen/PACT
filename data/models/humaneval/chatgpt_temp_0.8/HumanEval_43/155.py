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
    # Create a set to store seen values
    seen = set()
    
    # Iterate through list
    for num in l:
        # If the negative value of num has been seen, we have a pair that sums to zero
        if -num in seen:
            return True
        # Otherwise, add the value to the set of seen values
        seen.add(num)
    
    # If we loop through the entire list and don't find a pair that sums to zero, return False
    return False
