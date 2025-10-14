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
    # We can solve this problem by checking if the negative of an element in the list
    # is also in the list. If so, we found two distinct elements that sum to zero.
    # We can use a set to keep track of the elements we have seen so far, and iterate over
    # the list once to check each element.
    seen = set()
    for x in l:
        if -x in seen:
            return True
        seen.add(x)
    return False
