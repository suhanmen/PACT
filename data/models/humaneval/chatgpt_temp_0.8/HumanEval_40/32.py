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
    # Loop through every element in the list
    for i in range(len(l)):
        # Loop through every element from i+1 to the end of the list
        for j in range(i+1, len(l)):
            # Loop through every element from j+1 to the end of the list
            for k in range(j+1, len(l)):
                # Check if the sum of the three elements is zero
                if l[i] + l[j] + l[k] == 0:
                    return True
    # If no triplets sum to zero, return False
    return False
