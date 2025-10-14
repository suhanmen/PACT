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
    # If the list is empty or contains only one element, there cannot be a pair
    if len(l) < 2:
        return False
    
    # Create a set to store the already seen elements
    seen = set()
    
    # Iterate over the list
    for num in l:
        # If the negation of the current number is already in the set, we found a pair
        if -num in seen:
            return True
        # Otherwise, add the current number to the set
        seen.add(num)
    
    # If we get here, there are no pairs that sum to zero
    return False
