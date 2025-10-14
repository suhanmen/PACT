python
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
    # create an empty set to store seen numbers
    seen = set()
    
    # iterate over each number in the list
    for num in l:
        # if the negative of the current number is in the set
        if -num in seen:
            # return True, since we found a pair that sums to zero
            return True
        # otherwise, add the current number to the set
        seen.add(num)
    
    # if we reach this point, it means we didn't find any pairs
    return False
