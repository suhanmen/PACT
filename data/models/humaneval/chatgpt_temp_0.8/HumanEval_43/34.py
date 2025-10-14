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
    # Check if the list has at least two distinct elements
    if len(set(l)) < 2:
        return False
    
    # Use a dictionary to keep track of the elements already visited
    visited = {}
    
    # Loop through the list and check if there is a pair that sums to zero
    for num in l:
        if -num in visited:
            return True
        visited[num] = True
    
    return False
