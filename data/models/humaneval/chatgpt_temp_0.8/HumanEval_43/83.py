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
    # Create an empty set to store the numbers
    num_set = set()
    
    # Loop through the list of numbers
    for num in l:
        # Check if the negative version of the number is already in the set
        if -num in num_set:
            # If it is, return True since we found a pair that adds up to zero
            return True
        # If the negative version of the number is not in the set, add the number to the set
        else:
            num_set.add(num)
    
    # If we finish looping through the list without finding any pairs,
    # return Fals
