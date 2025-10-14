def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    if len(l) < 2:
        return False

    seen = set()
    for x in l:
        if -x in seen:
            return True
        seen.add(x)

    return False
