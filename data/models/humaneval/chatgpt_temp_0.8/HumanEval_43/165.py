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
    # create a set of seen elements
    seen = set()
    # loop through the list
    for i in l:
        # check if the negative of the current element is in the seen set
        if -i in seen:
            return True
        # add the current element to the seen set
        seen.add(i)
    # if we get through the whole list without finding a pair that sums to zero, return False
    return False
