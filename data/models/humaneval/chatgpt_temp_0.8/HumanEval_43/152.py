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
    # create a set to store the visited elements
    visited = set()
    
    # loop through the list
    for num in l:
        # check if the complement of the number is in the set
        if -num in visited:
            # if yes, return True
            return True
        # if not, add the number to the set
        visited.add(num)
    
    # if no pairs sum up to zero, return False
    return False
