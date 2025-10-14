def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 3:
        return False
    l.sort()  # sort the list in ascending order
    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue  # skip duplicates
        left = i+1
        right = len(l)-1
        while left < right:
            s = l[i] + l[left] + l[right]
            if s < 0:
                left += 1
            elif s > 0:
                right -= 1
            else:
                return True  # found a triplet that sums to zero
    return False  # no triplet found
