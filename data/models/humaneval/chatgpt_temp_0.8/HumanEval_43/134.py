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
    # Create an empty set to store the values in the list
    s = set()
    
    # Traverse through each element in the list
    for i in l:
        # Check if the negative value of the element is present in the set
        # If yes, then return True as we have found two elements that sum to zero
        if -i in s:
            return True
        # Otherwise, add the element to the set
        s.add(i)
    
    # If we reach the end of the loop, return False as we have not found any two elements that sum to zero
    return False
