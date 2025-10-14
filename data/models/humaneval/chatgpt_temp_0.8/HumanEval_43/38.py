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
    # We can solve this problem using a set to keep track of seen elements,
    # and checking if the negative of the current element is in the set.
    # If it is, then we have found a pair that sums to zero.
    seen = set()
    for num in l:
        if -num in seen:
            return True
        seen.add(num)
    return False
