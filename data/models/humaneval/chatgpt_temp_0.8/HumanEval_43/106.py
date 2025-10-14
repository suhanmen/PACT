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
    # create a set to keep track of the elements that have been seen
    seen = set()

    # iterate over the elements in the list
    for i in l:
        # check if the opposite of the element has been seen before
        if -i in seen:
            # if it has, we've found two distinct elements that sum to zero
            return True
        # add the current element to the set of seen elements
        seen.add(i)

    # if we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False
