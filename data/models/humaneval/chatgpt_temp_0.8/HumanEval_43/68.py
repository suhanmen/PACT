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
    # First, let's check if the list is too short to have pairs
    if len(l) < 2:
        return False
    
    # We'll use a set to keep track of the numbers we've seen so far
    seen = set()
    
    # Iterate over the list
    for num in l:
        # Check if the negative of the current number is in the set
        if -num in seen:
            return True
        
        # Add the current number to the set
        seen.add(num)
    
    # If we've gone through the whole list and haven't found a pair, return False
    return False
