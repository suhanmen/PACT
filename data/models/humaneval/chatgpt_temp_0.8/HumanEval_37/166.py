def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # get even indices
    even_vals = [l[i] for i in even_indices] # get values at even indices
    even_vals.sort() # sort the even values
    result = l[:] # create a copy of the original list
    for i in range(len(even_indices)):
        result[even_indices[i]] = even_vals[i] # replace even indices with sorted even values
    return result
