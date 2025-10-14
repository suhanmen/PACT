def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three, while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    sorted_vals = sorted(l[::3])
    result = []
    for i, val in enumerate(l):
        if i % 3 == 0:
            result.append(sorted_vals.pop(0))
        else:
            result.append(val)
    return result
