def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_indices = [i for i in range(len(l)) if i % 2 == 0] # get all even indices
    even_values = [l[i] for i in even_indices] # get values at even indices
    even_values.sort() # sort the even values
    l_sorted = l[:] # make a copy of l
    for i in even_indices: # replace values at even indices with sorted even values
        l_sorted[i] = even_values.pop(0)
    return l_sorted # return the sorted list
