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
    # Create a set to store the seen values
    seen = set()

    # Loop through each value in the list
    for val in l:
        # Check if the negative of the current value is in the seen set
        if -val in seen:
            # If it is, then there exists two distinct values in the list
            # that sum to zero
            return True
        else:
            # Otherwise, add the current value to the seen set
            seen.add(val)

    # Return False if no distinct values are found that sum to zero
    return False
