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
    # Create a set to keep track of seen values
    seen = set()
    
    # Iterate through each element in the list
    for num in l:
        # If the negation of the current number is in the set, return True
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
        
    # If there are no pairs that sum to zero, return False
    return False
