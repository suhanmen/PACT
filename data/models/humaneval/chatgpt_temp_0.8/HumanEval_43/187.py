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
    # create an empty set to store the seen numbers
    seen = set()

    # iterate through the list of numbers
    for num in l:
        # if the negative version of the number is in the set, the two numbers sum to zero
        if -num in seen:
            return True
        # otherwise, add the number to the set
        seen.add(num)

    # if we get through the entire list without finding a sum-to-zero pair, return False
    return False
