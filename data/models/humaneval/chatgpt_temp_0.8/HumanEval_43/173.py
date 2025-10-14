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
    # Create a set to keep track of the seen elements
    seen = set()
    # Iterate over the list
    for x in l:
        # Check if the negative of the current element is in the set
        if -x in seen:
            # If so, there exist two elements that sum to zero
            return True
        # Add the current element to the set
        seen.add(x)
    # If we get here, there are no two elements that sum to zero
    return False
