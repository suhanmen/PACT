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
    # Create an empty set to store the seen numbers
    seen = set()

    # Loop through each number in the list
    for num in l:
        # If the negative of the number is already in seen, return True
        if -num in seen:
            return True
        # Otherwise, add the number to seen set
        seen.add(num)

    # If loop completes without finding a pair, return False
    return False
