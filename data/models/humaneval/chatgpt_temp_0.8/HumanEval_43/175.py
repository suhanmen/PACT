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
    # Create an empty set to store the values we've seen so far
    seen = set()
    # Loop through each element in the list
    for num in l:
        # Check if the negative of the current element has been seen before
        if -num in seen:
            # If so, we've found a pair that sums to zero, so return True
            return True
        # Add the current element to the set of seen values
        seen.add(num)
    # If we get through the whole list without finding a pair that sums to zero, return False
    return False
