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
    # Check if length of list is less than 2
    if len(l) < 2:
        return False
    # Create a set of the list
    s = set(l)
    # Iterate through the list
    for i in l:
        # Check if the negative value of i is in the set
        if -i in s:
            # Check if the negative value of i is not equal to i
            if i != -i:
                return True
    return False
