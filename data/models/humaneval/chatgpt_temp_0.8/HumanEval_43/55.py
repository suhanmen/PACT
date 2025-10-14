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
    # create an empty set to store the seen elements
    seen = set()
    
    # iterate over each number in the list
    for num in l:
        # check if the negative of the number is in the seen set
        if -num in seen:
            # if it is, return True
            return True
        # otherwise, add the number to the seen set
        seen.add(num)
    
    # if no pair of distinct elements sum to zero, return False
    return False
