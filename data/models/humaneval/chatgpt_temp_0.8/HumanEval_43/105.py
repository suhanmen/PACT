def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Create a set to store the seen values
    seen = set()
    
    # Loop over each element in the list
    for num in l:
        # Check if the negative version of the current element is in the seen set
        if -num in seen:
            # Found a pair that sums to zero, return True
            return True
        # Add the current element to the seen set
        seen.add(num)
    
    # No pairs found that sum to zero, return False
    return False
