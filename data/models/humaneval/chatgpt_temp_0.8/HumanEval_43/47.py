def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    """
    # check that the list has at least two elements
    if len(l) < 2:
        return False
    # use a set to keep track of seen numbers
    seen = set()
    # iterate over the list
    for x in l:
        # check if the negative of x has been seen before
        if -x in seen:
            return True
        # add x to the set of seen numbers
        seen.add(x)
    # no pair sums to zero
    return False
