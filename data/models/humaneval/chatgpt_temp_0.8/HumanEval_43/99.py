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
    # create a set to store the numbers we have seen so far
    seen = set()
    
    # iterate over each number in the list
    for num in l:
        # check if the negation of the current number is in the set
        if -num in seen:
            # if it is, then we have found two distinct elements that sum to zero
            return True
        else:
            # otherwise, add the current number to the set and continue iterating
            seen.add(num)
    
    # if we have checked all the numbers and haven't found a pair that sums to zero,
    # return False
    return False
