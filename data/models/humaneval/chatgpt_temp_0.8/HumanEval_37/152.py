def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.
    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    even_list = []
    odd_list = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            even_list.append(val)
        else:
            odd_list.append(val)
    even_list = sorted(even_list)
    sorted_list = []
    j = 0
    k = 0
    while j < len(even_list) and k < len(odd_list):
        sorted_list.append(even_list[j])
        sorted_list.append(odd_list[k])
        j += 1
        k += 1
    if j < len(even_list):
        sorted_list.extend(even_list[j:])
    elif k < len(odd_list):
        sorted_list.extend(odd_list[k:])
    return sorted_list
