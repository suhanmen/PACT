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
    # Create an empty set to store the numbers we have seen
    seen = set()
    
    # Loop through each number in the list
    for num in l:
        # If the negative of the current number is in the set, we have found a pair that sums to zero
        if -num in seen:
            return True
        # Add the current number to the set of seen numbers
        seen.add(num)
    
    # If we have looped through the entire list without finding a pair that sums to zero, return False
    return False
