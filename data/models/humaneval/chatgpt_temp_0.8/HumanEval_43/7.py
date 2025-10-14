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
    # Check if the list has at least two elements, otherwise it is impossible
    if len(l) < 2:
        return False

    # Create a set to store the elements we have already seen
    seen = set()

    # Loop through the list and check if the complement of each element has already been seen
    for num in l:
        complement = -num
        if complement in seen:
            return True
        seen.add(num)

    # If we reach this point, no pairs were found
    return False
