def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """

    # Check if the list has at least 3 elements
    if len(l) < 3:
        return False

    # Sort the list in ascending order
    l.sort()

    # Check for triplets that sum to zero
    for i in range(len(l) - 2):
        if i > 0 and l[i] == l[i-1]:
            continue
        j = i + 1
        k = len(l) - 1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s == 0:
                return True
            elif s < 0:
                j += 1
            else:
                k -= 1

    return False
