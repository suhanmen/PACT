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
    # Create an empty set to store the visited elements
    visited = set()

    # Loop through each element in the list
    for num in l:
        # Check if the negative of the current element has been visited before
        if -num in visited:
            return True
        # Add the current element to the visited set
        visited.add(num)

    # If no pair sums to zero, return False
    return False
