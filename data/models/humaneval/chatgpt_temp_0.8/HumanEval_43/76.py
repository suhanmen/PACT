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
    # Check if input list length is less than 2
    if len(l) < 2:
        return False
    
    # Create an empty set to store seen numbers
    seen = set()
    
    # Iterate over each element in the input list
    for num in l:
        
        # Calculate the complement of the current element
        complement = -num
        
        # If the complement is in the seen set, we have found a pair
        if complement in seen:
            return True
        
        # Add the current element to the seen set
        seen.add(num)
    
    # If we reach this point, no pair was found
    return False
