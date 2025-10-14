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
    # create a set to store the seen elements
    seen = set()
    # iterate through the list
    for num in l:
        # if the negative of the current number is in the set, return True
        if -num in seen:
            return True
        # otherwise, add the current number to the set
        seen.add(num)
    # if we reach the end of the list without finding a pair, return False
    return False
