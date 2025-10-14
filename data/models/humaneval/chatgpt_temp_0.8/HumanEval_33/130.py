python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indices that are not divisible by three,
    while its values at the indices that are divisible by three are equal
    to the values of the corresponding indices of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    thirds = sorted([l[i] for i in range(len(l)) if i % 3 == 0])
    return [l[i] if i % 3 != 0 else thirds.pop(0) for i in range(len(l))]
