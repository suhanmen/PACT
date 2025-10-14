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
    # use a set to keep track of seen elements
    seen = set()
    # iterate over the list
    for x in l:
        # if the complement of x is in the set, we found a pair
        if -x in seen:
            return True
        # otherwise, add x to the set
        seen.add(x)
    # we finished iterating without finding a pair
    return False
