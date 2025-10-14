def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    :param l: A list of integers
    :return: A sorted list with even indices only
    
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # get a list of even indices
    even_indices = list(range(0, len(l), 2))
    # get the values of the even indices and sort them
    sorted_even_values = sorted([l[i] for i in even_indices])
    # create a new list by copying the original list and updating the even indices with the sorted values
    new_list = list(l)
    for i in even_indices:
        new_list[i] = sorted_even_values.pop(0)
    return new_list
