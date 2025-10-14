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
    # check if the length of list is greater than 1
    if len(l) <= 1:
        return False
    
    # create a set of absolute values of integers in the list
    abs_set = set(abs(x) for x in l)
    
    # check if the length of set is less than the length of list
    # in order to have at least one negative and one positive integer
    if len(abs_set) < len(l):
        return True
    
    # otherwise, iterate over the integers in the list
    # and check if the negative of the integer is in the set
    for x in l:
        if -x in abs_set:
            return True
    
    # if none of the above conditions are met, return False
    return False
