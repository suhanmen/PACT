def triples_sum_to_zero(l: list):
    """
    triples_sum_to_zero takes a list of integers as an input.
    it returns True if there are three distinct elements in the list that
    sum to zero, and False otherwise.
    """
    n = len(l)
    if n < 3:
        # There can't be three distinct elements in a list with less than 3 elements
        return False
    # Sort the list to facilitate the search for triplets
    l = sorted(l)
    for i in range(n):
        if i > 0 and l[i] == l[i-1]:
            # Skip duplicate elements to avoid duplicate triplets
            continue
        j = i + 1
        k = n - 1
        while j < k:
            s = l[i] + l[j] + l[k]
            if s == 0:
                # We found a triplet that sums to zero
                return True
            elif s < 0:
                j += 1
            else:
                k -= 1
    # No triplet sums to zero
    return False
