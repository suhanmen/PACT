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
    # create a set to store the elements we've seen so far
    seen = set()
    # iterate over each element in the list
    for num in l:
        # check if the negative of the current element is in the set
        if -num in seen:
            # if so, we've found a pair that sums to zero
            return True
        # otherwise, add the current element to the set
        seen.add(num)
    # if we've iterated over the entire list and haven't found a pair that sums to zero, return False
    return False
