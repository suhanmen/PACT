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
    # create an empty set to store seen values
    seen = set()
    # iterate over each element in the list
    for num in l:
        # check if the complement of the current element has been seen before
        if -num in seen:
            # if the complement has been seen, then return True
            return True
        # add the current element to the set of seen values
        seen.add(num)
    # if no pairs sum to zero, then return False
    return False
