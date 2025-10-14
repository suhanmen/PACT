def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_values = l[::2] # get the even-indexed values of l
    sorted_even = sorted(even_values) # sort these even-indexed values
    result = [] # initialize the result list
    for i, val in enumerate(l):
        if i % 2 == 0: # if the index is even
            result.append(sorted_even.pop(0)) # add the next sorted even value
        else:
            result.append(val) # add the odd value from the original list
    return result
