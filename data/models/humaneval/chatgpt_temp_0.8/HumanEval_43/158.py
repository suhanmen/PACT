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
    # create an empty set to keep track of seen numbers
    seen = set()
    
    # iterate over the input list
    for num in l:
        # check if the negation of the current number has been seen before
        if -num in seen:
            # if yes, return True
            return True
        # otherwise, add the current number to the set of seen numbers
        seen.add(num)
    
    # if no pair of distinct elements summed to zero, return False
    return False
