def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_list = l[::2]  # Get list of values at even indices
    sorted_even_list = sorted(even_list)  # Sort the even list
    result = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            # If even index, add sorted value from even list
            result.append(sorted_even_list.pop(0))
        else:
            # If odd index, add original value
            result.append(val)
    return result
