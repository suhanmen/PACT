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
    # Create a dictionary to store the elements of the list as keys
    # and their indices as values
    d = {}
    for i, num in enumerate(l):
        d[num] = i
    
    # Loop through the list again and check if the negative of each element
    # is in the dictionary and has a different index than the current element
    for i, num in enumerate(l):
        if -num in d and d[-num] != i:
            return True
    
    return False
