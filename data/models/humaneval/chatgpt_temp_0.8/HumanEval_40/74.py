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
    # check if length of list is less than 3, then it's not possible to have 3 distinct elements that sum to zero
    if len(l) < 3:
        return False
    
    # sort the list in ascending order
    l.sort()

    # loop through the list from the beginning until the third last element
    for i in range(len(l)-2):
        # if the current element is the same as the previous, skip to the next iteration
        if i > 0 and l[i] == l[i-1]:
            continue
        # set two pointers, one at i+1 and the other at the end of the list
        left = i+1
        right = len(l) - 1
        # loop while left pointer is less than right pointer
        while left < right:
            # calculate the sum of elements at i, left, and right pointers
            sum = l[i] + l[left] + l[right]
            # if sum is zero, return True
            if sum == 0:
                return True
            # if sum is less than zero, move the left pointer to the right (to increase the sum)
            
