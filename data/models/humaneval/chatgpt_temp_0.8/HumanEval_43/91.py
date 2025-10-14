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
    # create a set to store the values that we have seen so far
    seen = set()
    
    # loop through the list of integers
    for num in l:
        # check if the negation of the current number is in the set of seen values
        if -num in seen:
            return True
        # add the current number to the set of seen values
        seen.add(num)
    
    # if we have looped through the entire list and haven't found any pairs that sum to zero, return False
    return False
