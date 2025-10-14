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
    # Create a set to store the unique integers
    unique_ints = set(l)
    
    # Iterate over the set of unique integers
    for i in unique_ints:
        # Check if there exists a distinct integer such that their sum is zero
        if -i in unique_ints - {i}:
            return True
    
    # If no such pair exists, return False
    return False
