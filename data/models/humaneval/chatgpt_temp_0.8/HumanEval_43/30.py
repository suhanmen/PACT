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
    # Check if the list has at least two elements
    if len(l) < 2:
        return False
    
    # Use a set to keep track of the elements already seen
    seen = set()
    
    # Iterate over the list and try to find a complement for each element
    for x in l:
        if -x in seen:
            return True
        seen.add(x)
    
    # If no complement was found, return False
    return False
