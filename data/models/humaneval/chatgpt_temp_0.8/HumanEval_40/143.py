def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 3:
        return False    # There must be at least three elements in the list to have a triple.

    l.sort()    # Sort the list in non-descending order.

    for i in range(len(l)-2):
        if i > 0 and l[i] == l[i-1]:
            continue    # Skip duplicate elements to avoid duplicates in the output.

        j = i + 1
        k = len(l) - 1

        while j < k:
            if l[i] + l[j] + l[k] == 0:
                return True
            elif l[i] + l[j] + l[k] < 0:
                j += 1
            else:
                k -= 1

    return False
