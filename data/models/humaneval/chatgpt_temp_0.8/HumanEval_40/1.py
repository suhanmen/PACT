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
    
    # sort the list in non-descending order
    l.sort()
    
    # loop through the list and find triplets
    for i in range(len(l)-2):
        # check for duplicate triplet
        if i > 0 and l[i] == l[i-1]:
            continue
        j = i+1
        k = len(l)-1
        while j < k:
            triplet_sum = l[i] + l[j] + l[k]
            if triplet_sum < 0:
                j += 1
            elif triplet_sum > 0:
                k -= 1
            else:
                return True
    return False
