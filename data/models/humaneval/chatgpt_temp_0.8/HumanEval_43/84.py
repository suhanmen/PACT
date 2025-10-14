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
    # create a set to store seen values
    seen = set()
    # iterate through the list
    for x in l:
        # check if the negative of x is in seen
        if -x in seen:
            # return True if so
            return True
        # otherwise add x to seen
        seen.add(x)
    # return False if no pair sums to zero
    return False
