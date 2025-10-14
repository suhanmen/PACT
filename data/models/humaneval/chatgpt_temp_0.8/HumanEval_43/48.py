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
    # create a set to store seen numbers
    seen_numbers = set()
    # iterate through the list
    for num in l:
        # check if the negative of the current number is in the seen numbers set
        if -num in seen_numbers:
            return True
        # add the current number to the seen numbers set
        seen_numbers.add(num)
    # if no pair was found, return False
    return False
