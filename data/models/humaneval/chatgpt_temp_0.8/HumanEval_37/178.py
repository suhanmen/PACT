def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_numbers = sorted([x for x in l[::2]])
    sorted_list = []
    i = 0
    for x in l:
        if i % 2 == 0:
            sorted_list.append(even_numbers.pop(0))
        else:
            sorted_list.append(x)
        i += 1
    return sorted_list
