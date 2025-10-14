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

    # check if list has at least 3 elements
    if len(l) < 3:
        return False

    # sort the list
    l.sort()

    # loop through the list to check for triplets that sum to zero
    for i in range(len(l)-2):
        # check for duplicates
        if i > 0 and l[i] == l[i-1]:
            continue
        # initialize pointers for the next two elements in the list
        j = i+1
        k = len(l)-1
        while j < k:
            total = l[i] + l[j] + l[k]
            if total == 0:
                return True
            elif total < 0:
                j += 1
                # check for duplicates
                while j < k and l[j] == l[j-1]:
                    j += 1
            else:
                k -= 1
                # check for duplicates
                while j < k and l[k] == l[k+1]:
                    k -= 1

    return False
