def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.

    >>> triples_sum_to_zero([1, 3, 5, 0])
    False
    >>> triples_sum_to_zero([1, 3, -2, 1])
    True
    >>> triples_sum_to_zero([1, 2, 3, 7])
    False
    >>> triples_sum_to_zero([2, 4, -5, 3, 9, 7])
    True
    >>> triples_sum_to_zero([1])
    False
    """
    # sort the list in ascending order
    l.sort()
    # loop through the list, with two pointers starting at opposite ends
    for i in range(len(l)-2):
        left = i + 1
        right = len(l) - 1
        while left < right:
            # check if the sum of the three elements is zero
            if l[i] + l[left] + l[right] == 0:
                return True
            # if the sum is greater than zero, move the right pointer to the left
            elif l[i] + l[left] + l[right] > 0:
                right -= 1
            # if the sum is less than zero, move the left pointer to the right
            else:
                left += 1
    # if we get through the whole list without finding a sum of zero, return False
    return False
