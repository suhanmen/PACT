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
    if len(l) < 2: # if there are fewer than 2 elements in the list, there can be no pairs
        return False

    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 0: # if two distinct elements add up to zero, return True
                return True
    
    return False # if no such pair is found, return False
