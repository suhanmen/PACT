def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Get a list of the even indices of l
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    # Get a list of the values at the even indices of l
    even_values = [l[i] for i in even_indices]
    # Sort the even values
    even_values_sorted = sorted(even_values)
    # Create a new list with the same values as l
    result = l.copy()
    # Replace the even values in the new list with the sorted even values
    for i in range(len(even_indices)):
        result[even_indices[i]] = even_values_sorted[i]
    return result
