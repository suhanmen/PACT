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
    # Create an empty set to store the complements of values in the list
    complements = set()
    # Loop through each value in the list
    for value in l:
        # If the value is already in the complements set, return True
        if -value in complements:
            return True
        # Otherwise, add the complement of the value to the complements set
        complements.add(value)
    # If no pair of distinct values summed to zero, return False
    return False
