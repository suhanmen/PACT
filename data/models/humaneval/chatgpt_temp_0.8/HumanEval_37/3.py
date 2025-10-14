def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # create a copy of the original list
    l_copy = l.copy()
    # get the even indices of the list
    even_indices = list(range(0, len(l_copy), 2))
    # sort the even indices
    even_indices_sorted = sorted(l_copy[even_indices])
    # replace the even indices with the sorted values
    for i in even_indices:
        l_copy[i] = even_indices_sorted.pop(0)
    return l_copy
