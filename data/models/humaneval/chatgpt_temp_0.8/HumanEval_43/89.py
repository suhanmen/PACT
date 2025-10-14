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
    # Check if the list is empty or contains only one element
    if len(l) < 2:
        return False

    # Create a set to store the values we've seen so far
    seen = set()

    # Loop through the list and check if the negative of each element has already been seen
    for x in l:
        if -x in seen:
            return True
        seen.add(x)

    # If we've looped through the whole list and haven't found a pair that sums to zero, return False
    return False
