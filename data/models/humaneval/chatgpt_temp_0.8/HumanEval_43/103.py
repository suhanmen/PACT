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
    # create a set to keep track of numbers we've seen before
    seen = set()
    
    # iterate through the list
    for num in l:
        # check if the negative version of this number has been seen before
        if -num in seen:
            # if it has, we've found a pair that sums to zero
            return True
        # add this number to the set of seen numbers
        seen.add(num)
    
    # if we've iterated through the whole list without finding a pair that sums to zero, return False
    return False
