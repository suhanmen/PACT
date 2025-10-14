def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # Make sure the input list has at least 3 elements
    if len(l) < 3:
        return False

    # Sort the list in non-decreasing order
    l.sort()

    # For each element in the list, find a pair that sums to the negation of that element using two pointers approach
    for i in range(len(l)-2):
        left = i+1
        right = len(l)-1
        while left < right:
            if l[i] + l[left] + l[right] == 0:
                return True
            elif l[i] + l[left] + l[right] < 0:
                left += 1
            else:
                right -= 1

    # If no such triple exists, return False
    return False
