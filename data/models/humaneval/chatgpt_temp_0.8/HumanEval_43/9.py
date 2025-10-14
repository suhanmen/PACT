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
    # Initialize a set to keep track of the numbers we've seen so far
    seen = set()
    
    # Iterate through each number in the list
    for num in l:
        # Check if the negation of the current number is in the set
        if -num in seen:
            # If it is, then we've found two distinct numbers that sum to zero
            return True
        # Add the current number to the set
        seen.add(num)
    
    # If we reach this point, then we've iterated through the whole list without finding a pair
    return False
