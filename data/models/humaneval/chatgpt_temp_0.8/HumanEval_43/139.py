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
    # create an empty set to store visited numbers
    visited = set()
    # iterate through the list
    for num in l:
        # check if the negative of the current number has already been visited
        if -num in visited:
            return True
        # add the current number to the visited set
        visited.add(num)
    # if we haven't found a pair that sums to zero, return False
    return False
